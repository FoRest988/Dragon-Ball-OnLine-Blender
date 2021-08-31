

import bpy
from .gui import gui
from .ops import map_importer

from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "Dragon Ball OnLine Model",
    "author": "Parik",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "category": "Import-Export",
    "location": "File > Import/Export",
    "description": "Importer and Exporter for DBO Formats"
}


# Class list to register
_classes = [
    gui.IMPORT_OT_dff,
    gui.EXPORT_OT_dff,
    gui.EXPORT_OT_col,
    gui.MATERIAL_PT_dffMaterials,
    gui.OBJECT_PT_dffObjects,
    gui.DFFMaterialProps,
    gui.DFFObjectProps,
    gui.MapImportPanel,
    gui.DFFSceneProps,
    gui.DFF_MT_ExportChoice,
    map_importer.Map_Import_Operator
]
#######################################################
def register():

    # Register all the classes
    for cls in _classes:
        register_class(cls)

    if (2, 80, 0) > bpy.app.version:        
        bpy.types.INFO_MT_file_import.append(gui.import_dff_func)
        bpy.types.INFO_MT_file_export.append(gui.export_dff_func)
        
    else:
        bpy.types.TOPBAR_MT_file_import.append(gui.import_dff_func)
        bpy.types.TOPBAR_MT_file_export.append(gui.export_dff_func)
        
    

#######################################################
def unregister():

    if (2, 80, 0) > bpy.app.version:
        bpy.types.INFO_MT_file_import.remove(gui.import_dff_func)
        bpy.types.INFO_MT_file_export.remove(gui.export_dff_func)

    else:
        bpy.types.TOPBAR_MT_file_import.remove(gui.import_dff_func)
        bpy.types.TOPBAR_MT_file_export.remove(gui.export_dff_func)
    
    # Unregister all the classes
    for cls in _classes:
        unregister_class(cls)      
