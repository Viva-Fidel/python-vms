import numpy as np
import torch
from PySide6.QtCore import QThread, Slot, Signal, QObject

import cv2

import asyncio

class Lpr_analytics:

    print(torch.cuda.is_available())
    lpr_model = torch.hub.load('yolov5', 'custom', source='local', path='modules/number_plates_detection.onnx')
    OCR_model = torch.hub.load('yolov5', 'custom', source='local', path='modules/numbers_recognition.onnx')

    def __init__(self):
        super().__init__()
        self.detections = ["Not defined"]
        self.plate_detected = False
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def class_to_label(self, x):
        return Lpr_analytics.OCR_model.names[int(x)]

    async def detect_characters(self, plate):
        plate = cv2.resize(plate, (416, 416))
        plate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        results = Lpr_analytics.OCR_model(plate)
        list_results = results.xyxyn[0].cpu().detach().numpy()
        sorted_results = sorted(list_results, key=lambda x: (x[0], x[1]))
        labels, cordinates = [arr[5] for arr in sorted_results], [arr[:-1] for arr in sorted_results]

        n = len(labels)

        detected_characters = []

        for i in range(n):
            row = cordinates[i]
            if row[4] >= 0.60:
                detected_characters.append(self.class_to_label(labels[i]))

        try:
            for k in range(6):
                if k <= 2:
                    if detected_characters[k] == 'i':
                        detected_characters[k] = 'I'
                    elif detected_characters[k] == '0':
                        detected_characters[k] = 'O'
                elif k >= 3:
                    if detected_characters[k] == 'i':
                        detected_characters[k] = '1'
        except:
            pass

        print(detected_characters)
        self.detections = detected_characters

    async def run_lpr(self, frame):
        results = Lpr_analytics.lpr_model(frame)
        labels, cordinates = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        n = len(labels)

        for i in range(n):
            row = cordinates[i]
                
            if row[4] >= 0.80:
                x1, y1, x2, y2 = int(row[0] * x_shape), int((row[1] * y_shape)), int(
                        row[2] * x_shape), int((row[3] * y_shape))
                plate = frame[y1:y2, x1:x2]
                if self.plate_detected == False:
                    await self.detect_characters(plate)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y1 - 20), (x2, y1), (0, 255, 0), -1)
                    cv2.putText(frame, f"{''.join(self.detections)}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                    return frame
            else:
                self.plate_detected = False
                return frame




