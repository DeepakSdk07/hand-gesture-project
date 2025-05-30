import cv2
import mediapipe as mp
mp_hands=mp.solutions.mp_hands
mp_drawing=mp.solutions.drawing utilis
cap =cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.7,min_trackinng_confidence=0.5)as hands:
    while True:
        ret,frame-cpa.read()
        if not ret:
            break
        frame=cv2.flip(frame,1)
        rgb_frame=cv2.cvtColor(frame,cv2.COLOR_RGB2RGB)
        results-hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
        cv2.imshow("Hand Gesture Recognition",frame)
        key=cv2.waitkey(1)
        if key==27:
            break
cap.release()
cv2.destroyAllWindows()
