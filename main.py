import cv2

# HSV
low_black = (37, 37, 37)
high_black = (0, 0, 0)

cap = cv2.VideoCapture("/home/nikita/PycharmProjects/test_task_cv/v.mp4")

width = int(cap.get(3))
height = int(cap.get(4))
result_frames = []

#
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_b = cv2.inRange(frame, high_black, low_black)
    contours, hierarchy = cv2.findContours(frame_b.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (255, 8, 0), cv2.FILLED)

    result_frames.append(frame)

cap.release()

#
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# fourcc = cv2.VideoWriter_fourcc(*'avc1')
video = cv2.VideoWriter('/home/nikita/PycharmProjects/test_task_cv/video.mp4', fourcc, 20.0, (width, height))
#
#
for result_frame in result_frames:
    video.write(result_frame)
