import webbrowser , cv2

camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

QRencontrado = False
while QRencontrado==False:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for QRcodigo, p in zip(decoded_info, points):
                if QRcodigo:
                    color = (0, 255, 0)
                    QRencontrado = True
                    #cv2.destroyWindow(window_name)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines( frame , [ p.astype(int) ], True , color , 8 )
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)
print( QRcodigo ) #Codigo QR en texto


webbrowser.open( QRcodigo )  # Go to example.com