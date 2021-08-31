import bpy
from ..data import map_data
from ..ops.importer_common import game_version

#######################################################
class DFFSceneProps(bpy.types.PropertyGroup):

    #######################################################    
    def update_map_sections(self, context):
        return map_data.data[self.game_version_dropdown]['IPL_paths']
        
    game_version_dropdown : bpy.props.EnumProperty(
        name = 'Game',
        items = (
            (game_version.III, 'DBO 1', '3.3.0.2'),
            (game_version.VC, 'DBO 2', '3.4.0.3'),
            (game_version.SA, 'DBO 3', '3.6.0.2'),
            (game_version.LCS, 'DBO 4', 'Unknow'),
            (game_version.VCS, 'DBO 5', 'Unknow'),
        )
    )

    map_sections : bpy.props.EnumProperty(
        name = 'Map segment',
        items = update_map_sections
    )

    skip_lod: bpy.props.BoolProperty(
        name        = "Skip LOD Objects",
        default     = False
    )

    game_root : bpy.props.StringProperty(
        name = 'Game root',
        default = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\',
        description = "Folder with the game's executable",
        subtype = 'DIR_PATH'
    )

    dff_folder : bpy.props.StringProperty(
        name = 'Dff folder',
        default = 'C:\\Users\\blaha\\Documents\\GitHub\\Dragon Ball OnLine\\tests\\dff',
        description = "Define a folder where all of the dff models are stored.",
        subtype = 'DIR_PATH'
    )

    # txd_folder = bpy.props.StringProperty \
    #     (
    #     name = 'Txd folder',
    #     default = 'C:\\Users\\blaha\\Documents\\GitHub\\Dragon Ball OnLine\\tests\\txd',
    #     description = "Define a folder where all of the txd models are stored.",
    #     subtype = 'DIR_PATH'
    #     )

    #######################################################    
    def register():
        bpy.types.Scene.dff = bpy.props.PointerProperty(type=DFFSceneProps)

#######################################################
class MapImportPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Dragon Ball OnLine - Map Import"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    #######################################################
    def draw(self, context):
        layout = self.layout
        settings = context.scene.dff

        flow = layout.grid_flow(row_major=True,
                                columns=0,
                                even_columns=True,
                                even_rows=False,
                                align=True)

        col = flow.column()
        col.prop(settings, "game_version_dropdown", text="Game")
        col.prop(settings, "map_sections", text="Map segment")
        col.separator()
        col.prop(settings, "skip_lod", text="Skip LOD objects")

        layout.separator()

        layout.prop(settings, 'game_root')
        layout.prop(settings, 'dff_folder')

        row = layout.row()
        row.operator("scene.Dragon Ball OnLine_map_import")
