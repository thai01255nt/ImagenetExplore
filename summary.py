from core import reader
import matplotlib.pyplot as plt

list_label = [['barber chair', 'folding chair', 'rocking chair'],
              ['lampshade', 'lamp shade', 'table lamp'],
              ['china cabinet', 'file cabinet', 'filing cabinet', 'medicine cabinet'],
              ['dining table', 'pool table', 'billiard table', 'snooker table'],
              ['cassette player', 'CD player', 'tape player'],
              ['analog clock', 'digital clock', 'wall clock'],
              ['bookcase'],
              ['grand piano', 'upright piano'],
              ['prayer rug'],
              ['television'],
              ]

id = reader.get_label_id('prayer rug')
images = reader.random_images_from_id(id, 3)
