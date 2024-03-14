from spatialmath import SE3
from matplotlib import pyplot as plt

plt.rcParams['animation.ffmpeg_path'] = r"C:\Users\andre\Downloads\ffmpeg-6.1.1-full_build\ffmpeg-6.1.1-full_build\bin\ffmpeg.exe"

A = SE3(0, 0, 0)
B = SE3(2, 2, 2) * SE3.RPY([0, 0, 60], unit="deg")
C = SE3(4, 4, 4) * SE3.RPY([0, 45, 60], unit="deg")
D = SE3(6, 6, 6) * SE3.RPY([30, 45, 60], unit="deg")
print(A, B, C, D)
A.plot()
B.plot()
C.plot()
D.plot()
plt.show()

A = SE3(0, 0, 0)
B = SE3(2, 2, 2) * SE3.RPY([30, 0, 0], unit="deg")
C = SE3(4, 4, 4) * SE3.RPY([30, 45, 0], unit="deg")
D = SE3(6, 6, 6) * SE3.RPY([30, 45, 60], unit="deg")
print(A, B, C, D)
A.plot()
B.plot()
C.plot()
D.plot()
plt.show()
