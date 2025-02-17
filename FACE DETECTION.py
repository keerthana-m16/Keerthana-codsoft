import cv2
import face_recognition

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it
known_image = face_recognition.load_image_file("known_face.jpg")  # Replace with your image path
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create an array of known face encodings and their names
known_face_encodings = [known_face_encoding]
known_face_names = ["Known Person"]

print("Starting video stream. Press 'q' to quit.")

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (OpenCV default) to RGB color (face_recognition default)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations and face encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # Use the known face with the smallest distance if a match was found
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = face_distances.argmin() if len(face_distances) > 0 else None
        if best_match_index is not None and matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
video_capture.release()
cv2.destroyAllWindows()
