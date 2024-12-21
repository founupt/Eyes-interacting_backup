import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

LEFT_EYE_INDICES = [ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
RIGHT_EYE_INDICES = [ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398 ]
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye = []
            for index in LEFT_EYE_INDICES:
                lm = face_landmarks.landmark[index]
                x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                left_eye.append((x, y))

            right_eye = []
            for index in RIGHT_EYE_INDICES:
                lm = face_landmarks.landmark[index]
                x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                right_eye.append((x, y))

            for lm in left_eye:
                cv2.circle(frame, lm, 2, (0, 255, 0), -1)

            for lm in right_eye:
                cv2.circle(frame, lm, 2, (0, 255, 0), -1)

    cv2.imshow("Eye Landmarks", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()