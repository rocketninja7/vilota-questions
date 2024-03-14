import open3d as o3d
import numpy as np

mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
    size=1, origin=[0, 0, 0])

points = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [0.25, 0.5, 0.5],
]
lines = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [0, 4],
    [1, 4],
    [2, 4],
    [3, 4],
]
colors = [[1, 0, 0] for i in range(len(lines))]
line_set = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(points),
    lines=o3d.utility.Vector2iVector(lines),
)

radius = 3
height = 2

init_transform = np.eye(4)
init_transform[:3, 3] = [radius - points[4][0], 0 - points[4][1], height - points[4][2]]
init_transform[:3, :3] = mesh_frame.get_rotation_matrix_from_xyz([0, -np.arctan(height/radius), 0])
line_set.transform(init_transform)
line_set.colors = o3d.utility.Vector3dVector(colors)

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(line_set)
vis.add_geometry(mesh_frame)

ctrl = vis.get_view_control()
ctrl.camera_local_rotate(0, -700)
ctrl.camera_local_translate(0, 1, -7)

iterations = 1000

rotation = np.eye(4)
rotation[:3, :3] = mesh_frame.get_rotation_matrix_from_xyz([0, 0, 2 * np.pi / iterations])
translate = []
for i in range(iterations):
    translate.append(np.array([radius * np.cos(2 * np.pi * i / iterations), radius * np.sin(2 * np.pi * i / iterations), 0]))

curr_iter = 0
while True:
    axis_coords = np.asarray(line_set.points)[4]
    axis = np.eye(4)
    axis[:3, 3] = axis_coords
    new_axis = np.eye(4)
    new_axis[:3, 3] = axis_coords + translate[(curr_iter+1) % iterations] - translate[curr_iter % iterations]
    line_set.transform(new_axis @ rotation @ np.linalg.inv(axis))  # rotate around the axis, the fourth point
    vis.update_geometry(line_set)
    vis.poll_events()
    vis.update_renderer()
    curr_iter += 1

