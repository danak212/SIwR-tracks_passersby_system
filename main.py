import os
import cv2
import numpy as np


def load_bboxes(bboxes_file):
    with open(bboxes_file, 'r') as f:
        lines = f.readlines()

    bboxes_dict = {}
    i = 0
    while i < len(lines):
        image_name = lines[i].strip()
        num_boxes = int(lines[i + 1].strip())
        boxes = []
        for j in range(num_boxes):
            x, y, w, h = map(float, lines[i + 2 + j].strip().split())
            boxes.append((x, y, w, h))
        bboxes_dict[image_name] = boxes
        i += 2 + num_boxes
    return bboxes_dict


def track_pedestrians(frames_path, bboxes_file):
    bboxes_dict = load_bboxes(bboxes_file)
    frame_files = sorted([f for f in os.listdir(frames_path) if f.endswith('.jpg')])

    prev_boxes = None
    for frame_file in frame_files:
        frame_path = os.path.join(frames_path, frame_file)
        frame = cv2.imread(frame_path)

        current_boxes = bboxes_dict.get(frame_file, [])
        print(" ".join(str(i) for i in match_boxes(prev_boxes, current_boxes)))

        prev_boxes = current_boxes


def match_boxes(prev_boxes, current_boxes):
    if prev_boxes is None:
        return [-1] * len(current_boxes)

    # Example: Naive matching based on proximity
    matches = [-1] * len(current_boxes)
    for i, cur_box in enumerate(current_boxes):
        min_dist = float('inf')
        min_index = -1
        for j, prev_box in enumerate(prev_boxes):
            dist = np.linalg.norm(np.array(cur_box[:2]) - np.array(prev_box[:2]))
            if dist < min_dist:
                min_dist = dist
                min_index = j
        matches[i] = min_index
    return matches


if __name__ == "__main__":
    import sys

    frames_path = sys.argv[1]
    bboxes_file = os.path.join(frames_path, 'bboxes.txt')
    track_pedestrians(frames_path, bboxes_file)
