import open3d as o3d
import numpy as np
import lineset_init

line_set = lineset_init.lineset_init()
mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
    size=1, origin=[0, 0, 0])

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(line_set)
vis.add_geometry(mesh_frame)

ctrl = vis.get_view_control()
ctrl.camera_local_rotate(300, 0)
ctrl.camera_local_translate(-2, -2, 0)

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

