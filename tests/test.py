from tyssue import Sheet
from tyssue.generation import three_faces_sheet
from collisions import self_intersections


sheet = Sheet("test", *three_faces_sheet())
assert len(self_intersections(sheet) == 0)
