import time
import torch
import easyocr

print(torch.cuda.is_available())

lpr_model = torch.hub.load('yolov5', 'custom', source='local', path='modules/number_plates_detection.onnx')

numbers_model = torch.hub.load('yolov5', 'custom', source='local', path='modules/numbers_recognition.onnx')

classes = numbers_model.names

camera_url = 'test1.mp4'
prev_frame_time = 0
fps = 0
true_fps = 0
lpr = False

frame_count = 0
detections = ["Not defined", 0.0]
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

reader = easyocr.Reader(['en'])

import cv2



def run_lpr(frame):
    try:
        height, width, channels = frame.shape
        #ROI = frame[int(height * 0.1):int(height * 0.4), 0:width]
        results = lpr_model(frame)
        labels, cordinates = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        n = len(labels)

        for i in range(n):
            row = cordinates[i]

            if row[4] >= 0.85:
                x1, y1, x2, y2 = int(row[0] * x_shape), int(
                            (row[1] * y_shape)), int(
                            row[2] * x_shape), int((row[3] * y_shape))
                plate = frame[y1:y2, x1:x2]
                detect_characters(plate, frame)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y1 - 20), (x2, y1), (0, 255, 0), -1)
                cv2.putText(frame, f"{detections[0]}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (255, 255, 255), 2)


    except:
        pass

def class_to_label(x):

    #plates = []
    #plates.append(classes[int(x)])
    #print(plates)

    """
    For a given label value, return corresponding string label.
    :param x: numeric label
    :return: corresponding string label
    """
    #print(classes[int(x)])
    return classes[int(x)]



def detect_characters(plate, frame):
    platez = []
    plate = cv2.resize(plate, (416, 416))
    cv2.imshow('plate', plate)
    results = numbers_model(plate)
    labels, cordinates = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    print(results.xyxyn[0])
    print(labels)
    print(cordinates)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    n = len(labels)

    for i in range(n):
        row = cordinates[i]

        if row[4] >= 0.70:
            platez.append(class_to_label(labels[i]))
            x1, y1, x2, y2 = int(row[0] * x_shape), int(
                (row[1] * y_shape)), int(
                row[2] * x_shape), int((row[3] * y_shape))
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.rectangle(frame, (x1, y1 - 20), (x2, y1), (255, 0, 0), -1)
            cv2.putText(frame, class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255, 255, 255), 2)
    print(platez)



    # this needs to run only once to load the model into memory
    #result = reader.readtext (plate, batch_size = 10)
    #print(result)

    #probability = result[0][2]
    #if probability >= 0.90:
            #plate_num = result[0][1]
            #print(plate_num, probability)
            #if detections[0] != plate_num:
                #detections[0] = plate_num
                #detections[1] = probability

        # probability = [line[1][1] for line in result]
        #probability = ''.join([str(f) for f in probability])
        #if float(probability) >= 0.90:
            #plate_detected = True
            #plate_num = [line[1][0] for line in result]
            #plate_num = ''.join(plate_num)
            #print(plate_num, detections[0])
            #if detections[0] != plate_num:
                #detections[0] = plate_num
                #detections[1] = float(probability)



cap = cv2.VideoCapture(camera_url)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video file")

# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        run_lpr(frame)
        #time.sleep(0.3)
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()