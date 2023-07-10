
import cv2
import os

def images_to_video(image_folder, output_path, fps):
    # 이미지 폴더에서 파일 목록 가져오기
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

    # 첫 번째 이미지 로드
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = first_image.shape

    # 비디오 작성기 생성
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 이미지를 비디오로 변환하여 작성
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    # 작업 완료 후 리소스 해제
    video.release()
    cv2.destroyAllWindows()

# 이미지가 있는 폴더 경로와 출력 MP4 파일 경로를 지정합니다.
image_folder = "./clover"
output_path = "./output.mp4"

# 프레임 속도(fps)를 조정합니다.
fps = 24

# 이미지 시퀀스를 MP4로 변환합니다.
images_to_video(image_folder, output_path, fps)