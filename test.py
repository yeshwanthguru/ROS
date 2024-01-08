import cv2
import mediapipe as mp
import rospy
from std_msgs.msg import Bool

# Initialize ROS node
rospy.init_node('hand_tracking_node')

# Create a publisher for the hand detection status
hand_status_publisher = rospy.Publisher('/hand_detected', Bool, queue_size=10)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

# Open Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Check if hand landmarks are detected
    hand_detected = False
    if results.multi_hand_landmarks:
        hand_detected = True
        for landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract coordinates of specific landmarks (e.g., right hand)
            right_hand_landmarks = []
            for idx, landmark in enumerate(landmarks.landmark):
                if idx in [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.THUMB_TIP,
                           mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                           mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]:
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    right_hand_landmarks.append((cx, cy))

            # Print or use right_hand_landmarks as needed
            print("Right Hand Landmarks:", right_hand_landmarks)

    # Publish the hand detection status to the ROS topic
    hand_status_publisher.publish(hand_detected)

    # Display the frame
    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
