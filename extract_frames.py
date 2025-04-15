import cv2
import os
import glob

# 영상이 저장된 폴더 경로 설정
video_folder = "videos"
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

video_files = glob.glob(os.path.join(video_folder, "*.MOV")) + \
              glob.glob(os.path.join(video_folder, "*.mov"))

frame_count = 0

for video_path in video_files:
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 중간 프레임 위치 계산
    target_frames = [total_frames // 3, (2 * total_frames) // 3]

    for idx in target_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frame_name = f"frame_{frame_count:03d}.jpg"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
            print(f"Saved {frame_name}")
            frame_count += 1

    cap.release()

print("모든 프레임 추출 완료")
