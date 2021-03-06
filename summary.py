from core import reader, visual
import matplotlib.pyplot as plt
import cv2
import numpy as np

list_imagenet_label = [['barber chair', 'folding chair', 'rocking chair'],
                       ['lampshade', 'lamp shade', 'table lamp'],
                       ['china cabinet', 'file cabinet', 'filing cabinet', 'medicine cabinet'],
                       ['dining table', 'pool table', 'billiard table', 'snooker table'],
                       ['cassette player', 'CD player', 'tape player'],
                       ['analog clock', 'digital clock', 'wall clock'],
                       ['bookcase'],
                       ['grand piano', 'upright piano'],
                       ['prayer rug'],
                       ['television'],
                       ['frying pan', 'frypan', 'skillet'],
                       ['ashcan', 'trash can', 'garbage can', 'wastebin',
                        'ash bin', 'ash-bin', 'ashbin', 'dustbin',
                        'trash barrel', 'trash bin'],
                       ['coffeepot'],
                       ['dishwasher', 'dish washer', 'dishwashing machine'],
                       ['stove'],
                       ['broom'],
                       ['hand blower', 'blow dryer', 'blow drier',
                        'hair dryer', 'hair drier'],
                       ['vacuum cleaner'],
                       ['washer', 'automatic washer', 'washing machine'],
                       ['cot'],
                       ['wardrobe', 'closet', 'press'],
                       ['desk'],
                       ['desktop computer'],
                       ['laptop computer'],
                       ['barrow', 'garden cart', 'lawn cart', 'wheelbarrow'],
                       ["lawn mower"]
                       ]

mapping_label = {'chair': ['n02791124', 'n03376595', 'n04099969'],
                 'lamp': ['n03637318', 'n04380533'],
                 'cabinet': ['n03018349', 'n03337140', 'n03742115'],
                 'table': ['n03201208', 'n03982430'],
                 'CD player': ['n02979186', 'n02988304', 'n04392985'],
                 'clock': ['n02708093', 'n03196217', 'n04548280'],
                 'bookcase': ['n02870880'],
                 'piano': ['n03452741', 'n04515003'],
                 'rug': ['n03998194'],
                 'television': ['n04404412'],
                 'pans': ['n03400231'],
                 'bin': ['n02747177'],
                 'coffeepot': ['n03063689'],
                 'dishwashing machine': ['n03207941'],
                 'stove': ['n04330267'],
                 'broom': ['n02906734'],
                 'hair dryer': ['n03483316'],
                 'vacuum cleaner': ['n04517823'],
                 'washing machine': ['n04554684'],
                 'cot': ['n03131574'],
                 'wardrobe': ['n04550184'],
                 'desk': ['n03179701'],
                 'desktop computer': ['n03180011'],
                 'laptop computer': ['n03642806'],
                 'wheelbarrow': ['n02797295'],
                 'lawn mower': ['n03649909']}
