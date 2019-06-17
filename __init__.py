import bpy
import os
from mathutils import *
from math import *
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)
from bpy.props import (
    BoolProperty,
)

bl_info = {
    "name": "Iterative tools for rendering and exporting",
    "author": "Stefan Stefanov",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Custom tools for iterating",
    "warning": "",
    "wiki_url": "",
    "category": "Render",
}


class IRT_OT_render(Operator):
    bl_idname = "render.irt_local"
    bl_description = "Render with predefind settings"
    bl_label = "Render Iteration"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        file_path = bpy.path.abspath("//")
        bpy.data.scenes["Scene"].render.filepath = file_path + "image"
        bpy.ops.render.render(write_still=True)
        print("Render complete")
        return {"FINISHED"}


class IRT_OT_export(Operator):
    bl_idname = "export.irt_export"
    bl_description = "Export the selected object, offseted or not"
    bl_label = "Export Selection"

    export_with_offset = BoolProperty(
        name="Export bool",
        description="Export with offset or not",
        default=False
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if export_with_offset == True:
            obj = context.active_object
            location = obj.location.copy()
            obj.location = Vector((0, 0, 0))

            filename = bpy.path.abspath(
                "//") + context.active_object.name + ".fbx"
            bpy.ops.export_scene.fbx(filepath=filename, use_selection=True)

            obj.location = location
            print("Export completed [ 0 0 0 ]")
            return {"FINISHED"}

        else:
            filename = bpy.path.abspath(
                "//") + context.active_object.name + ".fbx"
            bpy.ops.export_scene.fbx(filepath=filename, use_selection=True)
            print("Export completed [ offseted ]")
            return {"FINISHED"}


class IRT_OT_hide_overlay_studio_objects(Operator):
    bl_idname = "render.irt_hide_studio"
    bl_description = "Hides all the non-essential overlays in the scene"
    bl_label = "Hide non-essentials"

    # @classmethod
    def execute(self, context):
        spacedata = bpy.context.space_data
        spacedata.show_object_viewport_light = False
        spacedata.show_gizmo = False
        spacedata.show_object_viewport_camera = False
        return {"FINISHED"}


class IRT_PT_panel(Panel):
    bl_label = "Iterate Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_region_type = "UI"
    bl_category = "IRT"

    def draw(self, context):
        layout = self.layout
        # Render Iteration button
        row = layout.row()
        row.operator("render.irt_local", icon="CAMERA_DATA")

        # Hide non-essential overlays in the viewport
        row = layout.row()
        row.operator("render.irt_hide_studio", icon="WORLD_DATA")

        # Export selection button
        col = layout.column(align=True)
        col.operator("export.irt_export", icon="WORLD_DATA")

        offset_export = col.operator(
            "export.irt_export", text="Export Selection With Offset", icon="WORLD_DATA")
        offset_export.export_with_offset = True


__classes__ = (
    IRT_PT_panel,
    IRT_OT_render,
    IRT_OT_export,
    IRT_OT_hide_overlay_studio_objects
)

register, unregister = bpy.utils.register_classes_factory(__classes__)


if __name__ == "__main__":
    register()
