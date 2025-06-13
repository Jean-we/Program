import cv2
import numpy as np
import mediapipe as mp


# 打开默认摄像头
cap = cv2.VideoCapture(0)
# 初始化模型
my_hands = mp.solutions.hands.Hands(
    static_image_mode=False,  # 首帧检测后开始追崇
    max_num_hands=2,  # 最多检测的手
    min_detection_confidence=0.5,  # 探测手掌成功的置信度阈值（模型判断的概率）
    min_tracking_confidence=0.5,  # 追踪失败时重新检测的阈值（模型判断的概率）
)
# 初始化人脸检测模型
face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)


try:
    while True:
        # 读取每一帧
        ret, frame = cap.read()
        if ret:
            # 转换RGB(numpy数组)
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 接受RGBnumpy数组
            res = my_hands.process(img_rgb)
            # 人脸检测
            face_results = face_detection.process(img_rgb)
            if face_results.detections:
                for detection in face_results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    x, y, w, h = (
                        int(bboxC.xmin * iw),
                        int(bboxC.ymin * ih),
                        int(bboxC.width * iw),
                        int(bboxC.height * ih),
                    )
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (25, 255, 255), 2)
                    cv2.putText(
                        frame,
                        "Face",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (29, 255, 255),
                        2,
                    )

            # 手部检测
            if (
                res.multi_hand_landmarks and res.multi_handedness
            ):  # res.multi_head_landmarks关键点坐标信息 ，res.multi_handedness左右手分类和其他信息
                # 循环匹配
                for hand_landmarks, handedness in zip(
                    res.multi_hand_landmarks, res.multi_handedness
                ):
                    # 设置关键点和线条的样式
                    mp.solutions.drawing_utils.draw_landmarks(
                        frame,  # 注意这里要用BGR格式的frame
                        hand_landmarks,
                        mp.solutions.hands.HAND_CONNECTIONS,  # 连接关系
                        mp.solutions.drawing_utils.DrawingSpec(
                            color=(0, 255, 27), thickness=2, circle_radius=6
                        ),  # 关键点样式
                        mp.solutions.drawing_utils.DrawingSpec(
                            color=(255, 0, 0), thickness=2, circle_radius=6
                        ),  # 线条样式
                    )

                    # 指尖和PIP的索引
                    finger_tips = [4, 8, 12, 16, 20]
                    finger_PIP = [3, 6, 10, 14, 18]
                    # 获取关键点坐标
                    landmarks = hand_landmarks.landmark
                    # 统计伸出的手指数量
                    fingers_up = 0
                    # 循环判断
                    for tip, pip in zip(finger_tips, finger_PIP):
                        # y值越小越靠上，tip在pip上方则为伸出
                        if (
                            landmarks[tip].y < landmarks[pip].y - 0.092
                        ):  # 0.01是经验阈值，可调整
                            fingers_up += 1

                    # 判断左右手
                    hand_label = handedness.classification[0].label  # "Left" 或 "Right"
                    if hand_label == "Left":
                        cv2.putText(
                            frame,
                            f"Left: {fingers_up}",
                            (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            2,
                            (0, 255, 0),
                            3,
                        )

                    else:
                        cv2.putText(
                            frame,
                            f"Right: {fingers_up}",
                            (1620, 60),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            2,
                            (255, 0, 0),
                            3,
                        )

            cv2.imshow("视觉检测", frame)
            # 按下'1'退出
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            print("打开失败")
            break


finally:
    # 释放资源
    cap.release()
    # 关闭所有创建的窗口
    cv2.destroyAllWindows()
