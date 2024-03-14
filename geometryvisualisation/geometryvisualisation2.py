import open3d as o3d
import numpy as np

points = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [0.25, 0.5, 0.5],
]
points = [[i[0], i[1]+1, i[2]] for i in points]
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
line_set.colors = o3d.utility.Vector3dVector(colors)
mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
    size=1, origin=[0, 0, 0])

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(line_set)
vis.add_geometry(mesh_frame)

ctrl = vis.get_view_control()
# ctrl.camera_local_translate(-2.5, -2, 0)
ctrl.camera_local_translate(-2, 0, 0)
# ctrl.camera_local_rotate(600, 0)

iterations = 100

rotation = np.eye(4)
rotation[:3, :3] = mesh_frame.get_rotation_matrix_from_xyz([np.pi / 2 / iterations, 0, 0])
# rotation[:3, :3] = mesh_frame.get_rotation_matrix_from_xyz([0, np.pi / 2 / iterations, 0])
# rotation[:3, :3] = mesh_frame.get_rotation_matrix_from_xyz([0, 0, np.pi / 2 / iterations])
translate = np.asarray([1/iterations, 0, 0])

for i in range(iterations):
    axis_coords = np.asarray(line_set.points)[4]
    axis = np.eye(4)
    axis[:3, 3] = axis_coords
    new_axis = np.eye(4)
    new_axis[:3, 3] = axis_coords + translate
    line_set.transform(new_axis @ rotation @ np.linalg.inv(axis))  # rotate around the axis, the fourth point
    vis.update_geometry(line_set)
    vis.poll_events()
    vis.update_renderer()

