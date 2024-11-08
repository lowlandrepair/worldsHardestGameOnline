import _pickle as pickle
import pygame, csv, os
from dot import *
from coin import *

def set_map(num):
    map = []
   
    walls = [pygame.Rect(494, 126, 6, 294), pygame.Rect(499, 126, 139, 6), pygame.Rect(638, 126, 6, 102),
             pygame.Rect(547, 222, 91, 6), pygame.Rect(542, 222, 6, 54), pygame.Rect(547, 270, 43, 6),
             pygame.Rect(590, 270, 6, 198), pygame.Rect(499, 462, 91, 6), pygame.Rect(494, 462, 6, 54),
             pygame.Rect(499, 510, 235, 6), pygame.Rect(734, 462, 6, 54), pygame.Rect(643, 462, 91, 6),
             pygame.Rect(638, 270, 6, 198), pygame.Rect(643, 270, 43, 6), pygame.Rect(686, 126, 6, 150),
             pygame.Rect(691, 126, 139, 6), pygame.Rect(830, 126, 6, 102), pygame.Rect(739, 222, 91, 6),
             pygame.Rect(734, 222, 6, 198), pygame.Rect(739, 414, 91, 6), pygame.Rect(830, 414, 6, 150), 
             pygame.Rect(739, 558, 91, 6), pygame.Rect(734, 558, 6, 54), pygame.Rect(499, 606, 235, 6), 
             pygame.Rect(494, 558, 6, 54), pygame.Rect(403, 558, 91, 6), pygame.Rect(398, 414, 6, 150),
             pygame.Rect(403, 414, 91, 6)]

   
    home = (552, 160)

  
    dots = [LinearDot((520, 296), (576, 296), 2, True), LinearDot((576, 344), (520, 344), 2, True),
            LinearDot((520, 392), (576, 392), 2, True),LinearDot((576, 440), (520, 440), 2, True),
            LinearDot((472, 440), (416, 440), 2, True), LinearDot((416, 488), (472, 488), 2, True),
            LinearDot((472, 536), (416, 536), 2, True), LinearDot((520, 592), (520, 536), 2, False), 
            LinearDot((568, 536), (568, 592), 2, False), LinearDot((616, 592), (616, 536), 2, False),
            LinearDot((664, 536), (664, 592), 2, False), LinearDot((712, 592), (712, 536), 2, False),
            LinearDot((760, 440), (816, 440), 2, True), LinearDot((816, 488), (760, 488), 2, True),
            LinearDot((760, 536), (816, 536), 2, True), LinearDot((712, 296), (656, 296), 2, True),
            LinearDot((656, 344), (712, 344), 2, True), LinearDot((712, 392), (656, 392), 2, True),
            LinearDot((656, 440), (712, 440), 2, True)]

  
    end = pygame.Rect(668, 128, 144, 96)

  
    coins = []

   
    cp = []

    with open(os.path.join(f'levels/level{num}.csv')) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    # map = load_map(num)['map']
    data = {'map': map, 'walls': walls, 'home': home, 'dots': dots, 'end': end, 'coins': coins, 'checkpoints': cp}
    # data = load_map(num)
    # data['checkpoints'] = cp
    with open(f'levels/level{num}.pkl', 'wb') as f:
        data = pickle.dump(data, f, -1)
    f.close()


def load_map(num):
    try:
        with open('levels/level'+str(num)+'.pkl', 'rb') as f:
            data = pickle.load(f)
        f.close()
        return data
    except:
        return None

