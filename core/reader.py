import pandas as pd
import numpy as np
import glob, os
import explore_config as config
import cv2


def read_synset_mapping(path):
    result = []
    with open(path, 'r') as f:
        lines = f.read()
        lines = lines.split(sep="\n")
        for line in lines:
            if line == "":
                break
            _line = line.split(sep=", ")
            id = _line[0].split(sep=" ")[0]
            _line[0] = _line[0][len(id) + 1:]
            _line = [id] + _line
            result.append(_line)
    result = np.array(pd.DataFrame(result))
    result[np.where(result == None)] = ""
    return np.array(pd.DataFrame(result)).astype(str)


SYNSET_MAPPING = read_synset_mapping(config.SYNSET_MAPPING_FILE)


def get_label_id(label: str):
    label = label.lower()
    matching_index = np.where(SYNSET_MAPPING == label)
    if len(matching_index[0]) == 0:
        return None
    return SYNSET_MAPPING[matching_index[0][0], 0]


def get_label_contain(label: str):
    label = label.lower()
    matching_index = np.where(np.char.find(SYNSET_MAPPING, label) >= 0)
    if len(matching_index[0]) == 0:
        return None
    return SYNSET_MAPPING[matching_index].tolist()


def random_images_from_id(label_id, num):
    images_path = glob.glob(os.path.join(config.IMAGE_FOLDER, label_id) + "/*")
    random_index = np.random.choice(len(images_path), num)
    images = []
    for index in random_index:
        image = cv2.imread(images_path[index])
        images.append(image)
    return images
    pass
