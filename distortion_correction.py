import cv2
import numpy as np

# 카메라 캘리브레이션 결과
camera_matrix = np.array([[1662.27, 0, 952.06],
                          [0, 1663.99, 542.80],
                          [0, 0, 1]])
dist_coeffs = np.array([0.2060, -0.5026, -0.00009, -0.00277, -0.4573])

# 왜곡된 이미지 경로
input_image_path = "frames/frame_018.jpg"
output_image_path = "corrected_image.png"

# 이미지 읽기
img = cv2.imread(input_image_path)
if img is None:
    raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {input_image_path}")

h, w = img.shape[:2]

# 새로운 카메라 행렬 계산
new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w, h), 1, (w, h))

# 왜곡 보정
undistorted_img = cv2.undistort(img, camera_matrix, dist_coeffs, None, new_camera_mtx)

# 결과 저장
cv2.imwrite(output_image_path, undistorted_img)
print(f"보정된 이미지가 저장되었습니다: {output_image_path}")
