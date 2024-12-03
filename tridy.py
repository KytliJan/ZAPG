import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from matplotlib.path import Path

class n_uhelnik:
    def __init__(self, vrcholy):

        self.vrcholy = vrcholy
        self.polygon = Polygon(vrcholy)

    def obvod(self):
  
        obvod = 0
        for i in range(len(self.vrcholy)):
            x1, y1 = self.vrcholy[i]
            x2, y2 = self.vrcholy[(i + 1) % len(self.vrcholy)]
            obvod += np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return obvod

    def obsah(self): # Pomocí shoelace theorem
     
        x = [v[0] for v in self.vrcholy]
        y = [v[1] for v in self.vrcholy]
        return 0.5 * abs(sum(x[i] * y[i - 1] - y[i] * x[i - 1] for i in range(len(self.vrcholy))))

    def intersects(self, other):
     
        return self.polygon.intersects(other.polygon)
    def plot(self, ax=None, **kwargs):
     """
     Vykreslení n-úhelníku.
     :param ax: Objekt matplotlib.axes.Axes (volitelný).
     :param kwargs: Další parametry pro vykreslovací funkci matplotlib.
     """

     if ax is None:
         ax = plt.gca()
     # Uzavření polygonu pro vykreslení
     x = [v[0] for v in self.vrcholy] + [self.vrcholy[0][0]]
     y = [v[1] for v in self.vrcholy] + [self.vrcholy[0][1]]
     ax.plot(x, y, **kwargs)

    def intersects(self, other):
     """
     Zjištění, zda se tento n-úhelník protíná s jiným.
     :param other: Jiný n-úhelník (instance třídy NPolygon)
     :return: True, pokud se protínají, jinak False
     """
    
     poly1_path = Path(self.vrcholy)
     poly2_path = Path(other.vrcholy)
     return poly1_path.intersects_path(poly2_path)

######################################################################
#TEST#
######################################################################

if __name__ == "__main__":
    
    polygon1 = n_uhelnik([(0, 0), (4, 0), (4.5,2), (4, 3), (0, 3)])
    polygon2 = n_uhelnik([(2, 1), (6, 1), (6, 2), (8,3),(2, 4)])

# Kontrola průniku
if polygon1.intersects(polygon2):
    print("Polygony se protínají.")
else:
    print("Polygony se neprotínají.")

print("Obvod polygonu 1:", polygon1.obvod())
print("Obsah polygonu 1:", polygon1.obsah())
print("Obvod polygonu 2:", polygon2.obvod())
print("Obsah polygonu 2:", polygon2.obsah())

fig, ax = plt.subplots()
polygon1.plot(ax=ax, label="Polygon 1", color="blue", linewidth=2)
polygon2.plot(ax=ax, label="Polygon 2", color="red", linewidth=2)
ax.legend()
ax.set_aspect('equal')
plt.show()
