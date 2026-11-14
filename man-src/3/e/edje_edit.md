---
title: "edje_edit(3)"
name: "edje_edit"
section: "3"
letter: "e"
url: "/docs/linux/man/3-edje_edit/"
description: "Edje_Edit.h – Functions to deal with edje internal object."
---

<p>Edje_Edit.h &#8211; Functions to deal with edje internal object. </p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<p><code>General API</code><br />
 General functions that don&#8217;t fit in other cateories. </p>
<p> EAPI void <code>edje_edit_string_list_free</code> (Evas_List *lst)<br />
 <i>Free a generic Evas_List of (char *) allocated by an edje_edit_*_get() function. </i><br />
 EAPI void <code>edje_edit_string_free</code> (const char *str)<br />
 <i>Free a generic string (char *) allocated by an edje_edit_*_get() function. </i><br />
 EAPI int <code>edje_edit_save</code> (Evas_Object *obj)<br />
 <i>Save the modified edje object back to his file. </i><br />
 EAPI void <code>edje_edit_print_internal_status</code> (Evas_Object *obj)<br />
 <i>Print on standard output many information about the internal status of the edje object. </i> </p>
<p> <code>Groups API</code><br />
 Functions to deal with groups property (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI unsigned char <code>edje_edit_group_add</code> (Evas_Object *obj, const char *name)<br />
 <i>Create a new empty group in the given edje. </i><br />
 EAPI unsigned char <code>edje_edit_group_del</code> (Evas_Object *obj)<br />
 <i>Delete the current group from the given edje. </i><br />
 EAPI unsigned char <code>edje_edit_group_exist</code> (Evas_Object *obj, const char *group)<br />
 <i>Check if a group with the given name exist in the edje. </i><br />
 EAPI unsigned char <code>edje_edit_group_name_set</code> (Evas_Object *obj, const char *new_name)<br />
 <i>Set a new name for the current open group. </i><br />
 EAPI int <code>edje_edit_group_min_w_get</code> (Evas_Object *obj)<br />
 <i>Get the group min width. </i><br />
 EAPI void <code>edje_edit_group_min_w_set</code> (Evas_Object *obj, int w)<br />
 <i>Set the group min width. </i><br />
 EAPI int <code>edje_edit_group_min_h_get</code> (Evas_Object *obj)<br />
 <i>Get the group min height. </i><br />
 EAPI void <code>edje_edit_group_min_h_set</code> (Evas_Object *obj, int h)<br />
 <i>Set the group min height. </i><br />
 EAPI int <code>edje_edit_group_max_w_get</code> (Evas_Object *obj)<br />
 <i>Get the group max width. </i><br />
 EAPI void <code>edje_edit_group_max_w_set</code> (Evas_Object *obj, int w)<br />
 <i>Set the group max width. </i><br />
 EAPI int <code>edje_edit_group_max_h_get</code> (Evas_Object *obj)<br />
 <i>Get the group max height. </i><br />
 EAPI void <code>edje_edit_group_max_h_set</code> (Evas_Object *obj, int h)<br />
 <i>Set the group max height. </i> </p>
<p> <code>Data API</code><br />
 Functions to deal with data embedded in the edje (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI Evas_List * <code>edje_edit_data_list_get</code> (Evas_Object *obj)<br />
 <i>Retrieves a list with the item names inside the data block. </i><br />
 EAPI unsigned char <code>edje_edit_data_add</code> (Evas_Object *obj, const char *itemname, const char *value)<br />
 <i>Create a new data object in the given edje If another data with the same name exists nothing is created and FALSE is returned. </i><br />
 EAPI unsigned char <code>edje_edit_data_del</code> (Evas_Object *obj, const char *itemname)<br />
 <i>Delete the given data object from edje. </i><br />
 EAPI const char * <code>edje_edit_data_value_get</code> (Evas_Object *obj, char *itemname)<br />
 <i>Get the data associated with the given itemname. </i><br />
 EAPI unsigned char <code>edje_edit_data_value_set</code> (Evas_Object *obj, const char *itemname, const char *value)<br />
 <i>Set the data associated with the given itemname. </i> </p>
<p> <code>Parts API</code><br />
 Functions to deal with part objects (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI Evas_List * <code>edje_edit_parts_list_get</code> (Evas_Object *obj)<br />
 <i>Get the list of all the parts in the given edje object. </i><br />
 EAPI unsigned char <code>edje_edit_part_add</code> (Evas_Object *obj, const char *name, unsigned char type)<br />
 <i>Create a new part in the given edje If another part with the same name just exists nothing is created and FALSE is returned. </i><br />
 EAPI unsigned char <code>edje_edit_part_del</code> (Evas_Object *obj, const char *part)<br />
 <i>Delete the given part from the edje All the reference to this part will be zeroed. </i><br />
 EAPI unsigned char <code>edje_edit_part_exist</code> (Evas_Object *obj, const char *part)<br />
 <i>Check if a part with the given name exist in the edje object. </i><br />
 EAPI unsigned char <code>edje_edit_part_restack_below</code> (Evas_Object *obj, const char *part)<br />
 <i>Move the given part below the previous one. </i><br />
 EAPI unsigned char <code>edje_edit_part_restack_above</code> (Evas_Object *obj, const char *part)<br />
 <i>Move the given part above the next one. </i><br />
 EAPI unsigned char <code>edje_edit_part_name_set</code> (Evas_Object *obj, const char *part, const char *new_name)<br />
 <i>Set a new name for part. </i><br />
 EAPI unsigned char <code>edje_edit_part_type_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get the type of a part. </i><br />
 EAPI const char * <code>edje_edit_part_clip_to_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get the clip_to part. </i><br />
 EAPI unsigned char <code>edje_edit_part_clip_to_set</code> (Evas_Object *obj, const char *part, const char *clip_to)<br />
 <i>Set a part to clip part to. </i><br />
 EAPI const char * <code>edje_edit_part_source_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get the source of part. </i><br />
 EAPI unsigned char <code>edje_edit_part_source_set</code> (Evas_Object *obj, const char *part, const char *source)<br />
 <i>Set the source of part. </i><br />
 EAPI unsigned char <code>edje_edit_part_effect_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get the effect for a given part. </i><br />
 EAPI void <code>edje_edit_part_effect_set</code> (Evas_Object *obj, const char *part, unsigned char effect)<br />
 <i>Set the effect for a given part. </i><br />
 EAPI const char * <code>edje_edit_part_selected_state_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get the current selected state in part. </i><br />
 EAPI unsigned char <code>edje_edit_part_selected_state_set</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Set the current state in part. </i><br />
 EAPI unsigned char <code>edje_edit_part_mouse_events_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get mouse_events for part. </i><br />
 EAPI void <code>edje_edit_part_mouse_events_set</code> (Evas_Object *obj, const char *part, unsigned char mouse_events)<br />
 <i>Set mouse_events for part. </i><br />
 EAPI unsigned char <code>edje_edit_part_repeat_events_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get repeat_events for part. </i><br />
 EAPI void <code>edje_edit_part_repeat_events_set</code> (Evas_Object *obj, const char *part, unsigned char repeat_events)<br />
 <i>Set repeat_events for part. </i><br />
 EAPI Evas_Event_Flags <code>edje_edit_part_ignore_flags_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get ignore_flags for part. </i><br />
 EAPI void <code>edje_edit_part_ignore_flags_set</code> (Evas_Object *obj, const char *part, Evas_Event_Flags ignore_flags)<br />
 <i>Set repeat_events for part. </i> </p>
<p> <code>States API</code><br />
 Functions to deal with part states (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI Evas_List * <code>edje_edit_part_states_list_get</code> (Evas_Object *obj, const char *part)<br />
 <i>Get the list of all the states in the given part. </i><br />
 EAPI int <code>edje_edit_state_name_set</code> (Evas_Object *obj, const char *part, const char *state, const char *new_name)<br />
 <i>Set a new name for the given state in the given part. </i><br />
 EAPI void <code>edje_edit_state_add</code> (Evas_Object *obj, const char *part, const char *name)<br />
 <i>Create a new state to the give part. </i><br />
 EAPI void <code>edje_edit_state_del</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Delete the given part state from the edje. </i><br />
 EAPI unsigned char <code>edje_edit_state_exist</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Check if a part state with the given name exist. </i><br />
 EAPI double <code>edje_edit_state_rel1_relative_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel1 relative x value of state. </i><br />
 EAPI double <code>edje_edit_state_rel1_relative_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel1 relative y value of state. </i><br />
 EAPI double <code>edje_edit_state_rel2_relative_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel2 relative x value of state. </i><br />
 EAPI double <code>edje_edit_state_rel2_relative_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel2 relative y value of state. </i><br />
 EAPI void <code>edje_edit_state_rel1_relative_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the rel1 relative x value of state. </i><br />
 EAPI void <code>edje_edit_state_rel1_relative_y_set</code> (Evas_Object *obj, const char *part, const char *state, double y)<br />
 <i>Set the rel1 relative y value of state. </i><br />
 EAPI void <code>edje_edit_state_rel2_relative_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the rel2 relative x value of state. </i><br />
 EAPI void <code>edje_edit_state_rel2_relative_y_set</code> (Evas_Object *obj, const char *part, const char *state, double y)<br />
 <i>Set the rel2 relative y value of state. </i><br />
 EAPI int <code>edje_edit_state_rel1_offset_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel1 offset x value of state. </i><br />
 EAPI int <code>edje_edit_state_rel1_offset_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel1 offset y value of state. </i><br />
 EAPI int <code>edje_edit_state_rel2_offset_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel2 offset x value of state. </i><br />
 EAPI int <code>edje_edit_state_rel2_offset_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the rel2 offset y value of state. </i><br />
 EAPI void <code>edje_edit_state_rel1_offset_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the rel1 offset x value of state. </i><br />
 EAPI void <code>edje_edit_state_rel1_offset_y_set</code> (Evas_Object *obj, const char *part, const char *state, double y)<br />
 <i>Get the rel1 offset y value of state. </i><br />
 EAPI void <code>edje_edit_state_rel2_offset_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Get the rel2 offset x value of state. </i><br />
 EAPI void <code>edje_edit_state_rel2_offset_y_set</code> (Evas_Object *obj, const char *part, const char *state, double y)<br />
 <i>Get the rel2 offset y value of state. </i><br />
 EAPI const char * <code>edje_edit_state_rel1_to_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the part name rel1x is relative to. </i><br />
 EAPI const char * <code>edje_edit_state_rel1_to_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the part name rel1y is relative to. </i><br />
 EAPI const char * <code>edje_edit_state_rel2_to_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the part name rel2x is relative to. </i><br />
 EAPI const char * <code>edje_edit_state_rel2_to_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the part name rel2y is relative to. </i><br />
 EAPI void <code>edje_edit_state_rel1_to_x_set</code> (Evas_Object *obj, const char *part, const char *state, const char *rel_to)<br />
 <i>Set the part rel1x is relative to. </i><br />
 EAPI void <code>edje_edit_state_rel1_to_y_set</code> (Evas_Object *obj, const char *part, const char *state, const char *rel_to)<br />
 <i>Set the part rel1y is relative to. </i><br />
 EAPI void <code>edje_edit_state_rel2_to_x_set</code> (Evas_Object *obj, const char *part, const char *state, const char *rel_to)<br />
 <i>Set the part rel2x is relative to. </i><br />
 EAPI void <code>edje_edit_state_rel2_to_y_set</code> (Evas_Object *obj, const char *part, const char *state, const char *rel_to)<br />
 <i>Set the part rel2y is relative to. </i><br />
 EAPI void <code>edje_edit_state_color_get</code> (Evas_Object *obj, const char *part, const char *state, int *r, int *g, int *b, int *a)<br />
 <i>Get the color of a part state. </i><br />
 EAPI void <code>edje_edit_state_color2_get</code> (Evas_Object *obj, const char *part, const char *state, int *r, int *g, int *b, int *a)<br />
 <i>Get the color2 of a part state. </i><br />
 EAPI void <code>edje_edit_state_color3_get</code> (Evas_Object *obj, const char *part, const char *state, int *r, int *g, int *b, int *a)<br />
 <i>Get the color3 of a part state. </i><br />
 EAPI void <code>edje_edit_state_color_set</code> (Evas_Object *obj, const char *part, const char *state, int r, int g, int b, int a)<br />
 <i>Set the color of a part state. </i><br />
 EAPI void <code>edje_edit_state_color2_set</code> (Evas_Object *obj, const char *part, const char *state, int r, int g, int b, int a)<br />
 <i>Set the color2 of a part state. </i><br />
 EAPI void <code>edje_edit_state_color3_set</code> (Evas_Object *obj, const char *part, const char *state, int r, int g, int b, int a)<br />
 <i>Set the color3 of a part state. </i><br />
 EAPI double <code>edje_edit_state_align_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the align_x value of a part state. </i><br />
 EAPI double <code>edje_edit_state_align_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the align_y value of a part state. </i><br />
 EAPI void <code>edje_edit_state_align_x_set</code> (Evas_Object *obj, const char *part, const char *state, double align)<br />
 <i>Set the align_x value of a part state. </i><br />
 EAPI void <code>edje_edit_state_align_y_set</code> (Evas_Object *obj, const char *part, const char *state, double align)<br />
 <i>Set the align_y value of a part state. </i><br />
 EAPI int <code>edje_edit_state_min_w_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the min_w value of a part state. </i><br />
 EAPI void <code>edje_edit_state_min_w_set</code> (Evas_Object *obj, const char *part, const char *state, int min_w)<br />
 <i>Set the min_w value of a part state. </i><br />
 EAPI int <code>edje_edit_state_min_h_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the min_h value of a part state. </i><br />
 EAPI void <code>edje_edit_state_min_h_set</code> (Evas_Object *obj, const char *part, const char *state, int min_h)<br />
 <i>Set the min_h value of a part state. </i><br />
 EAPI int <code>edje_edit_state_max_w_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the max_w value of a part state. </i><br />
 EAPI void <code>edje_edit_state_max_w_set</code> (Evas_Object *obj, const char *part, const char *state, int max_w)<br />
 <i>Set the max_w value of a part state. </i><br />
 EAPI int <code>edje_edit_state_max_h_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the max_h value of a part state. </i><br />
 EAPI void <code>edje_edit_state_max_h_set</code> (Evas_Object *obj, const char *part, const char *state, int max_h)<br />
 <i>Set the max_h value of a part state. </i><br />
 EAPI double <code>edje_edit_state_aspect_min_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the minimum aspect value of a part state. </i><br />
 EAPI double <code>edje_edit_state_aspect_max_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the maximum aspect value of a part state. </i><br />
 EAPI void <code>edje_edit_state_aspect_min_set</code> (Evas_Object *obj, const char *part, const char *state, double aspect)<br />
 <i>Set the minimum aspect value of a part state. </i><br />
 EAPI void <code>edje_edit_state_aspect_max_set</code> (Evas_Object *obj, const char *part, const char *state, double aspect)<br />
 <i>Set the maximum aspect value of a part state. </i><br />
 EAPI unsigned char <code>edje_edit_state_aspect_pref_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the aspect preference value of a part state. </i><br />
 EAPI void <code>edje_edit_state_aspect_pref_set</code> (Evas_Object *obj, const char *part, const char *state, unsigned char pref)<br />
 <i>Set the aspect preference value of a part state. </i><br />
 EAPI double <code>edje_edit_state_fill_origin_relative_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill origin relative x value of a part state. </i><br />
 EAPI double <code>edje_edit_state_fill_origin_relative_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill origin relative y value of a part state. </i><br />
 EAPI int <code>edje_edit_state_fill_origin_offset_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill origin offset x value of a part state. </i><br />
 EAPI int <code>edje_edit_state_fill_origin_offset_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill origin offset y value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_origin_relative_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the fill origin relative x value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_origin_relative_y_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the fill origin relative y value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_origin_offset_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the fill origin offset x value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_origin_offset_y_set</code> (Evas_Object *obj, const char *part, const char *state, double y)<br />
 <i>Set the fill origin offset x value of a part state. </i><br />
 EAPI double <code>edje_edit_state_fill_size_relative_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill size relative x value of a part state. </i><br />
 EAPI double <code>edje_edit_state_fill_size_relative_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill size relative y value of a part state. </i><br />
 EAPI int <code>edje_edit_state_fill_size_offset_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill size offset x value of a part state. </i><br />
 EAPI int <code>edje_edit_state_fill_size_offset_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the fill size offset y value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_size_relative_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the fill size relative x value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_size_relative_y_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the fill size relative y value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_size_offset_x_set</code> (Evas_Object *obj, const char *part, const char *state, double x)<br />
 <i>Set the fill size offset x value of a part state. </i><br />
 EAPI void <code>edje_edit_state_fill_size_offset_y_set</code> (Evas_Object *obj, const char *part, const char *state, double y)<br />
 <i>Set the fill size offset x value of a part state. </i><br />
 EAPI unsigned char <code>edje_edit_state_visible_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the visibility of a part state. </i><br />
 EAPI void <code>edje_edit_state_visible_set</code> (Evas_Object *obj, const char *part, const char *state, unsigned char visible)<br />
 <i>Set the visibility of a part state. </i> </p>
<p> <code>Text API</code><br />
 Functions to deal with text objects (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI const char * <code>edje_edit_state_text_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the text of a part state. </i><br />
 EAPI void <code>edje_edit_state_text_set</code> (Evas_Object *obj, const char *part, const char *state, const char *text)<br />
 <i>Set the text of a part state. </i><br />
 EAPI int <code>edje_edit_state_text_size_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the text size of a part state. </i><br />
 EAPI void <code>edje_edit_state_text_size_set</code> (Evas_Object *obj, const char *part, const char *state, int size)<br />
 <i>Set the text size of a part state. </i><br />
 EAPI double <code>edje_edit_state_text_align_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the text horizontal align of a part state. </i><br />
 EAPI double <code>edje_edit_state_text_align_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the text vertical align of a part state. </i><br />
 EAPI void <code>edje_edit_state_text_align_x_set</code> (Evas_Object *obj, const char *part, const char *state, double align)<br />
 <i>Set the text horizontal align of a part state. </i><br />
 EAPI void <code>edje_edit_state_text_align_y_set</code> (Evas_Object *obj, const char *part, const char *state, double align)<br />
 <i>Set the text vertical align of a part state. </i><br />
 EAPI Evas_List * <code>edje_edit_fonts_list_get</code> (Evas_Object *obj)<br />
 <i>Get the list of all the fonts in the given edje. </i><br />
 EAPI unsigned char <code>edje_edit_font_add</code> (Evas_Object *obj, const char *path)<br />
 <i>Add a new ttf font to the edje file. </i><br />
 EAPI const char * <code>edje_edit_state_font_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get font name for a given part state. </i><br />
 EAPI void <code>edje_edit_state_font_set</code> (Evas_Object *obj, const char *part, const char *state, const char *font)<br />
 <i>Set font name for a given part state. </i> </p>
<p> <code>Images API</code><br />
 Functions to deal with image objects (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI Evas_List * <code>edje_edit_images_list_get</code> (Evas_Object *obj)<br />
 <i>Get the list of all the images in the given edje. </i><br />
 EAPI unsigned char <code>edje_edit_image_add</code> (Evas_Object *obj, const char *path)<br />
 <i>Add an new image to the image collection. </i><br />
 EAPI const char * <code>edje_edit_state_image_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get normal image name for a given part state. </i><br />
 EAPI void <code>edje_edit_state_image_set</code> (Evas_Object *obj, const char *part, const char *state, const char *image)<br />
 <i>Set normal image for a given part state. </i><br />
 EAPI int <code>edje_edit_image_id_get</code> (Evas_Object *obj, const char *image_name)<br />
 <i>Get image id for a given image name. </i><br />
 EAPI int <code>edje_edit_image_compression_type_get</code> (Evas_Object *obj, const char *image)<br />
 <i>Get compression type for the given image. </i><br />
 EAPI int <code>edje_edit_image_compression_rate_get</code> (Evas_Object *obj, const char *image)<br />
 <i>Get compression rate for the given image. </i><br />
 EAPI void <code>edje_edit_state_image_border_get</code> (Evas_Object *obj, const char *part, const char *state, int *l, int *r, int *t, int *b)<br />
 <i>Get the image border of a part state. </i><br />
 EAPI void <code>edje_edit_state_image_border_set</code> (Evas_Object *obj, const char *part, const char *state, int l, int r, int t, int b)<br />
 <i>Set the image border of a part state. </i><br />
 EAPI Evas_List * <code>edje_edit_state_tweens_list_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the list of all the tweens images in the given part state. </i><br />
 EAPI unsigned char <code>edje_edit_state_tween_add</code> (Evas_Object *obj, const char *part, const char *state, const char *tween)<br />
 <i>Add a new tween frame to the given part state The tween param must be the name of an existing image. </i><br />
 EAPI unsigned char <code>edje_edit_state_tween_del</code> (Evas_Object *obj, const char *part, const char *state, const char *tween)<br />
 <i>Remove the first tween with the given name. </i> </p>
<p> <code>Spectrum API</code><br />
 Functions to manage spectrum (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI Evas_List * <code>edje_edit_spectrum_list_get</code> (Evas_Object *obj)<br />
 <i>Get the list of all the spectrum in the given edje object. </i><br />
 EAPI unsigned char <code>edje_edit_spectra_add</code> (Evas_Object *obj, const char *name)<br />
 <i>Add a new spectra in the given edje object. </i><br />
 EAPI unsigned char <code>edje_edit_spectra_del</code> (Evas_Object *obj, const char *spectra)<br />
 <i>Delete the given spectra from the edje object. </i><br />
 EAPI unsigned char <code>edje_edit_spectra_name_set</code> (Evas_Object *obj, const char *spectra, const char *name)<br />
 <i>Change the name of the given spectra. </i><br />
 EAPI int <code>edje_edit_spectra_stop_num_get</code> (Evas_Object *obj, const char *spectra)<br />
 <i>Get the number of stops in the given spectra. </i><br />
 EAPI unsigned char <code>edje_edit_spectra_stop_num_set</code> (Evas_Object *obj, const char *spectra, int num)<br />
 <i>Set the number of stops in the given spectra. </i><br />
 EAPI unsigned char <code>edje_edit_spectra_stop_color_get</code> (Evas_Object *obj, const char *spectra, int stop_number, int *r, int *g, int *b, int *a, int *d)<br />
 <i>Get the colors of the given stop. </i><br />
 EAPI unsigned char <code>edje_edit_spectra_stop_color_set</code> (Evas_Object *obj, const char *spectra, int stop_number, int r, int g, int b, int a, int d)<br />
 <i>Set the colors of the given stop. </i> </p>
<p> <code>Gradient API</code><br />
 Functions to deal with gradient objects (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI const char * <code>edje_edit_state_gradient_type_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the type of gradient. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_type_set</code> (Evas_Object *obj, const char *part, const char *state, const char *type)<br />
 <i>Set the type of gradient. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_use_fill_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get if the current gradient use the fill properties or the gradient_rel as params. </i><br />
 EAPI const char * <code>edje_edit_state_gradient_spectra_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the spectra used by part state. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_spectra_set</code> (Evas_Object *obj, const char *part, const char *state, const char *spectra)<br />
 <i>Set the spectra used by part state. </i><br />
 EAPI double <code>edje_edit_state_gradient_rel1_relative_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel1 relative x value. </i><br />
 EAPI double <code>edje_edit_state_gradient_rel1_relative_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel1 relative y value. </i><br />
 EAPI double <code>edje_edit_state_gradient_rel2_relative_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel2 relative x value. </i><br />
 EAPI double <code>edje_edit_state_gradient_rel2_relative_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel2 relative y value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel1_relative_x_set</code> (Evas_Object *obj, const char *part, const char *state, double val)<br />
 <i>Set the gradien rel1 relative x value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel1_relative_y_set</code> (Evas_Object *obj, const char *part, const char *state, double val)<br />
 <i>Set the gradien rel1 relative y value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel2_relative_x_set</code> (Evas_Object *obj, const char *part, const char *state, double val)<br />
 <i>Set the gradien rel2 relative x value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel2_relative_y_set</code> (Evas_Object *obj, const char *part, const char *state, double val)<br />
 <i>Set the gradien rel2 relative y value. </i><br />
 EAPI int <code>edje_edit_state_gradient_rel1_offset_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel1 offset x value. </i><br />
 EAPI int <code>edje_edit_state_gradient_rel1_offset_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel1 offset y value. </i><br />
 EAPI int <code>edje_edit_state_gradient_rel2_offset_x_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel2 offset x value. </i><br />
 EAPI int <code>edje_edit_state_gradient_rel2_offset_y_get</code> (Evas_Object *obj, const char *part, const char *state)<br />
 <i>Get the gradien rel2 offset y value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel1_offset_x_set</code> (Evas_Object *obj, const char *part, const char *state, int val)<br />
 <i>Set the gradien rel1 offset x value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel1_offset_y_set</code> (Evas_Object *obj, const char *part, const char *state, int val)<br />
 <i>Set the gradien rel1 offset y value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel2_offset_x_set</code> (Evas_Object *obj, const char *part, const char *state, int val)<br />
 <i>Set the gradien rel2 offset x value. </i><br />
 EAPI unsigned char <code>edje_edit_state_gradient_rel2_offset_y_set</code> (Evas_Object *obj, const char *part, const char *state, int val)<br />
 <i>Set the gradien rel2 offset y value. </i> </p>
<p> <code>Programs API</code><br />
 Functions to deal with programs (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI Evas_List * <code>edje_edit_programs_list_get</code> (Evas_Object *obj)<br />
 <i>Get the list of all the programs in the given edje object. </i><br />
 EAPI unsigned char <code>edje_edit_program_add</code> (Evas_Object *obj, const char *name)<br />
 <i>Add a new program to the edje file If a program with the same name just exist the function will fail. </i><br />
 EAPI unsigned char <code>edje_edit_program_del</code> (Evas_Object *obj, const char *prog)<br />
 <i>Remove the given program from the edje file. </i><br />
 EAPI unsigned char <code>edje_edit_program_exist</code> (Evas_Object *obj, const char *prog)<br />
 <i>Check if a program with the given name exist in the edje object. </i><br />
 EAPI unsigned char <code>edje_edit_program_run</code> (Evas_Object *obj, const char *prog)<br />
 <i>Run the given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_name_set</code> (Evas_Object *obj, const char *prog, const char *new_name)<br />
 <i>Set a new name for the given program. </i><br />
 EAPI const char * <code>edje_edit_program_source_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get source of a given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_source_set</code> (Evas_Object *obj, const char *prog, const char *source)<br />
 <i>Set source of the given program. </i><br />
 EAPI const char * <code>edje_edit_program_signal_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get signal of a given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_signal_set</code> (Evas_Object *obj, const char *prog, const char *signal)<br />
 <i>Set signal of the given program. </i><br />
 EAPI double <code>edje_edit_program_in_from_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get in.from of a given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_in_from_set</code> (Evas_Object *obj, const char *prog, double seconds)<br />
 <i>Set in.from of a given program. </i><br />
 EAPI double <code>edje_edit_program_in_range_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get in.range of a given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_in_range_set</code> (Evas_Object *obj, const char *prog, double seconds)<br />
 <i>Set in.range of a given program. </i><br />
 EAPI int <code>edje_edit_program_action_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the action of a given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_action_set</code> (Evas_Object *obj, const char *prog, int action)<br />
 <i>Set the action of a given program. </i><br />
 EAPI Evas_List * <code>edje_edit_program_targets_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the list of the targets for the given program Return a list of target name Use </i><code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore.<br />
 EAPI unsigned char <code>edje_edit_program_target_add</code> (Evas_Object *obj, const char *prog, const char *target)<br />
 <i>Add a new target name to the list of &#8216;targets&#8217; in the given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_targets_clear</code> (Evas_Object *obj, const char *prog)<br />
 <i>Clear the &#8216;targets&#8217; list of the given program. </i><br />
 EAPI Evas_List * <code>edje_edit_program_afters_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the list of action that will be run after the give program Return a list of program name. </i><br />
 EAPI unsigned char <code>edje_edit_program_after_add</code> (Evas_Object *obj, const char *prog, const char *after)<br />
 <i>Add a new program name to the list of &#8216;afters&#8217; in the given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_afters_clear</code> (Evas_Object *obj, const char *prog)<br />
 <i>Clear the &#8216;afters&#8217; list of the given program. </i><br />
 EAPI const char * <code>edje_edit_program_state_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the state for the given program In a STATE_SET action this is the name of state to set. </i><br />
 EAPI unsigned char <code>edje_edit_program_state_set</code> (Evas_Object *obj, const char *prog, const char *state)<br />
 <i>Set the state for the given program In a STATE_SET action this is the name of state to set. </i><br />
 EAPI double <code>edje_edit_program_value_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the value of state for the given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_value_set</code> (Evas_Object *obj, const char *prog, double value)<br />
 <i>Set the value of state for the given program. </i><br />
 EAPI const char * <code>edje_edit_program_state2_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the state2 for the given program In a STATE_SET action is not used In a SIGNAL_EMIT action is the source of the emitted signal. </i><br />
 EAPI unsigned char <code>edje_edit_program_state2_set</code> (Evas_Object *obj, const char *prog, const char *state2)<br />
 <i>Set the state2 for the given program In a STATE_SET action is not used In a SIGNAL_EMIT action is the source of the emitted signal. </i><br />
 EAPI double <code>edje_edit_program_value2_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the value of state2 for the given program. </i><br />
 EAPI unsigned char <code>edje_edit_program_value2_set</code> (Evas_Object *obj, const char *prog, double value)<br />
 <i>Set the value2 of state for the given program. </i><br />
 EAPI int <code>edje_edit_program_transition_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the type of transition to use when apply animations. </i><br />
 EAPI unsigned char <code>edje_edit_program_transition_set</code> (Evas_Object *obj, const char *prog, int transition)<br />
 <i>Set the type of transition to use when apply animations. </i><br />
 EAPI double <code>edje_edit_program_transition_time_get</code> (Evas_Object *obj, const char *prog)<br />
 <i>Get the duration of the transition in seconds. </i><br />
 EAPI unsigned char <code>edje_edit_program_transition_time_set</code> (Evas_Object *obj, const char *prog, double seconds)<br />
 <i>Set the duration of the transition in seconds. </i> </p>
<p> <code>Scripts API</code><br />
 Functions to deal with embryo scripts (see <code>Edje Data Collection reference</code>). </p>
<p> EAPI const char * <code>edje_edit_script_get</code> (Evas_Object *obj) </p>
<h2>Detailed Description</h2>
<p>Functions to deal with edje internal object. </p>
<p> Don&#8217;t use in standard situations. The use of any of the edje_edit_* functions can break your theme ability, remember that the program must be separated from the interface! </p>
<p> The API can be used to query or set every part of an edje object in real time. You can manage every aspect of parts, part states, programs, script and whatever is contained in the edje file. For a reference of what all parameter means look at the complete <code>Edje Data Collection reference</code>. </p>
<p> All the functions that deals with part states include the state value inside the returned strings (ex: &#8216;defaut 0.00&#8217;). For this reason there aren&#8217;t functions to set/get a state value, you have to pass the value inside the name string (always in the form &#8216;state x.xx&#8217;). </p>
<p> Don&#8217;t forget to free all the strings and the lists returned by any edje_edit_*() functions using <code>edje_edit_string_free()</code> and <code>edje_edit_string_list_free()</code> when you don&#8217;t need anymore. </p>
<p> Example: print all the part in a loaded edje_object </p>
<pre> Evas_List *parts, *l;
 parts = edje_edit_parts_list_get(edje_object);
 while(l = parts; l; l = l-&gt;next)
 {
 printf('Part: %s, (char*)l-&gt;data);
 }
 edje_edit_string_list_free(parts);</pre>
<p>Example: Change the color of a rect inside an edje file </p>
<pre> Evas_Object *edje;
 edje = edje_object_add(evas);
 edje_object_file_set(edje,'edj/file/name', 'group to load');
 edje_edit_state_color_set(edje, 'MyRectName', 'default 0.00', 255, 255, 0, 255);
 edje_edit_save(edje);</pre>
<p>&nbsp;<wbr></p>
<h2>Function Documentation</h2>
<h3>EAPI unsigned char edje_edit_data_add (Evas_Object * obj, const char * itemname, const char * value)</h3>
<p>Create a new data object in the given edje If another data with the same name exists nothing is created and FALSE is returned. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>itemname</i> The name for the new data<br />
 <i>value</i> The value for the new data</dl>
<h3>EAPI unsigned char edje_edit_data_del (Evas_Object * obj, const char * itemname)</h3>
<p>Delete the given data object from edje. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>itemname</i> The name of the data to remove</dl>
<h3>EAPI Evas_List* edje_edit_data_list_get (Evas_Object * obj)</h3>
<p>Retrieves a list with the item names inside the data block. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string (char *)containing all the data names.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI const char* edje_edit_data_value_get (Evas_Object * obj, char * itemname)</h3>
<p>Get the data associated with the given itemname. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>itemname</i> The name of the data item</dl>
<h3>EAPI unsigned char edje_edit_data_value_set (Evas_Object * obj, const char * itemname, const char * value)</h3>
<p>Set the data associated with the given itemname. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>itemname</i> The name of the data item<br />
 <i>value</i> The new value to set</dl>
<h3>EAPI unsigned char edje_edit_font_add (Evas_Object * obj, const char * path)</h3>
<p>Add a new ttf font to the edje file. </p>
<p> The newly created font will be available to all the groups in the edje, not only the current one. If font can&#8217;t be load FALSE is returned. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success or FALSE on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>path</i> The file path to load the ttf font from</dl>
<h3>EAPI Evas_List* edje_edit_fonts_list_get (Evas_Object * obj)</h3>
<p>Get the list of all the fonts in the given edje. </p>
<p> Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need the list anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string (char *)containing all the fonts names found in the edje file.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI unsigned char edje_edit_group_add (Evas_Object * obj, const char * name)</h3>
<p>Create a new empty group in the given edje. </p>
<p> If a group with the same name exist none is created. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>name</i> The name for the new empty group</dl>
<h3>EAPI unsigned char edje_edit_group_del (Evas_Object * obj)</h3>
<p>Delete the current group from the given edje. </p>
<p> You can only delete the currently loaded group. All the parts and the programs inside the group will be deleted as well, but not image or font embedded in the edje. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI unsigned char edje_edit_group_exist (Evas_Object * obj, const char * group)</h3>
<p>Check if a group with the given name exist in the edje. </p>
<p> &lt; 1 if the group exist, 0 otherwise. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>group</i> The name of the group</dl>
<h3>EAPI int edje_edit_group_max_h_get (Evas_Object * obj)</h3>
<p>Get the group max height. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The maxh value or -1 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI void edje_edit_group_max_h_set (Evas_Object * obj, int h)</h3>
<p>Set the group max height. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>h</i> The new group maximum height in pixel</dl>
<h3>EAPI int edje_edit_group_max_w_get (Evas_Object * obj)</h3>
<p>Get the group max width. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The maxw value or -1 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI void edje_edit_group_max_w_set (Evas_Object * obj, int w)</h3>
<p>Set the group max width. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>w</i> The new group maximum width in pixel</dl>
<h3>EAPI int edje_edit_group_min_h_get (Evas_Object * obj)</h3>
<p>Get the group min height. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The minh value or -1 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI void edje_edit_group_min_h_set (Evas_Object * obj, int h)</h3>
<p>Set the group min height. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>h</i> The new group minimum height in pixel</dl>
<h3>EAPI int edje_edit_group_min_w_get (Evas_Object * obj)</h3>
<p>Get the group min width. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The minw value or -1 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI void edje_edit_group_min_w_set (Evas_Object * obj, int w)</h3>
<p>Set the group min width. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>w</i> The new group minimum width in pixel</dl>
<h3>EAPI unsigned char edje_edit_group_name_set (Evas_Object * obj, const char * new_name)</h3>
<p>Set a new name for the current open group. </p>
<p> You can only rename a group that is currently loaded Note that the relative getter function don&#8217;t exist as it don&#8217;t make sense ;) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>new_name</i> The new name for the group</dl>
<h3>EAPI unsigned char edje_edit_image_add (Evas_Object * obj, const char * path)</h3>
<p>Add an new image to the image collection. </p>
<p> This function add the given image inside the edje. Don&#8217;t add a new image part but only put the image inside the edje file. It actually write directly to the file so you don&#8217;t have to save (and you can&#8217;t undo!). After you have to create a new image_part that use this image. Note that all the parts in the edje share the same image collection, thus you can/must use the same image for different part. </p>
<p> The format of the image files that can be loaded depend on the evas engine on your system </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success or FALSE on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>path</i> The name of the image file to include in the edje</dl>
<h3>EAPI int edje_edit_image_compression_rate_get (Evas_Object * obj, const char * image)</h3>
<p>Get compression rate for the given image. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the compression rate if the image is EDJE_EDIT_IMAGE_COMP_LOSSY. Or &lt; 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>image</i> The name of the image</dl>
<h3>EAPI int edje_edit_image_compression_type_get (Evas_Object * obj, const char * image)</h3>
<p>Get compression type for the given image. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>One of EDJE_EDIT_IMAGE_COMP_RAW, EDJE_EDIT_IMAGE_COMP_USER, EDJE_EDIT_IMAGE_COMP_COMP or EDJE_EDIT_IMAGE_COMP_LOSSY</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>image</i> The name of the image</dl>
<h3>EAPI int edje_edit_image_id_get (Evas_Object * obj, const char * image_name)</h3>
<p>Get image id for a given image name. </p>
<p> Could be usefull to directly load the image from the eet file. &lt; The ID of the givan image name <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI Evas_List* edje_edit_images_list_get (Evas_Object * obj)</h3>
<p>Get the list of all the images in the given edje. </p>
<p> Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need the list anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string (char *)containing all the images names found in the edje file.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI unsigned char edje_edit_part_add (Evas_Object * obj, const char * name, unsigned char type)</h3>
<p>Create a new part in the given edje If another part with the same name just exists nothing is created and FALSE is returned. </p>
<p> Note that this function also create a default description for the part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE if the part can&#8217;t be created</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>name</i> The name for the new part<br />
 <i>type</i> The type of the part to create (One of: EDJE_PART_TYPE_NONE, EDJE_PART_TYPE_RECTANGLE, EDJE_PART_TYPE_TEXT,EDJE_PART_TYPE_IMAGE, EDJE_PART_TYPE_SWALLOW, EDJE_PART_TYPE_TEXTBLOCK,EDJE_PART_TYPE_GRADIENT or EDJE_PART_TYPE_GROUP)</dl>
<h3>EAPI const char* edje_edit_part_clip_to_get (Evas_Object * obj, const char * part)</h3>
<p>Get the clip_to part. </p>
<p> NULL is returned on errors and if the part don&#8217;t have a clip. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the part to clip part to. Use <code>edje_edit_string_free()</code> when you don&#8217;t need it anymore.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI unsigned char edje_edit_part_clip_to_set (Evas_Object * obj, const char * part, const char * clip_to)</h3>
<p>Set a part to clip part to. </p>
<p> If clip_to is NULL then the clipping value will be cancelled (unset clipping) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>clip_to</i> The name of the part to clip part to.</dl>
<h3>EAPI unsigned char edje_edit_part_del (Evas_Object * obj, const char * part)</h3>
<p>Delete the given part from the edje All the reference to this part will be zeroed. </p>
<p> A group must have at least one part, so it&#8217;s not possible to remove the last remaining part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 if the part can&#8217;t be removed</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part to remove</dl>
<h3>EAPI unsigned char edje_edit_part_effect_get (Evas_Object * obj, const char * part)</h3>
<p>Get the effect for a given part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>One of: EDJE_TEXT_EFFECT_NONE, _PLAIN, _OUTLINE, _SOFT_OUTLINE, _SHADOW, _SOFT_SHADOW, _OUTLINE_SHADOW, _OUTLINE_SOFT_SHADOW, _FAR_SHADOW, _FAR_SOFT_SHADOW, _GLOW.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI void edje_edit_part_effect_set (Evas_Object * obj, const char * part, unsigned char effect)</h3>
<p>Set the effect for a given part. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>effect</i> The effect to set. See <code>edje_edit_part_effect_get()</code> for possible value</dl>
<h3>EAPI unsigned char edje_edit_part_exist (Evas_Object * obj, const char * part)</h3>
<p>Check if a part with the given name exist in the edje object. </p>
<p> &lt; 1 if the part exist, 0 otherwise. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI Evas_Event_Flags edje_edit_part_ignore_flags_get (Evas_Object * obj, const char * part)</h3>
<p>Get ignore_flags for part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>event flags ignored</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI void edje_edit_part_ignore_flags_set (Evas_Object * obj, const char * part, Evas_Event_Flags ignore_flags)</h3>
<p>Set repeat_events for part. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>ignore_flags</i> event flags to be ignored</dl>
<h3>EAPI unsigned char edje_edit_part_mouse_events_get (Evas_Object * obj, const char * part)</h3>
<p>Get mouse_events for part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if part accept mouse events, 0 if not</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI void edje_edit_part_mouse_events_set (Evas_Object * obj, const char * part, unsigned char mouse_events)</h3>
<p>Set mouse_events for part. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>mouse_events</i> If set to 1 part will accept mouse events, 0 to ignore all mouse events from part.</dl>
<h3>EAPI unsigned char edje_edit_part_name_set (Evas_Object * obj, const char * part, const char * new_name)</h3>
<p>Set a new name for part. </p>
<p> Note that the relative getter function don&#8217;t exist as it don&#8217;t make sense ;) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part to rename<br />
 <i>new_name</i> The new name for the part</dl>
<h3>EAPI unsigned char edje_edit_part_repeat_events_get (Evas_Object * obj, const char * part)</h3>
<p>Get repeat_events for part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if part will pass all events to the other parts, 0 if not</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI void edje_edit_part_repeat_events_set (Evas_Object * obj, const char * part, unsigned char repeat_events)</h3>
<p>Set repeat_events for part. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>repeat_events</i> If set to 1 part will repeat all the received mouse events to other parts. If set to 0 the events received will not propagate to other parts.</dl>
<h3>EAPI unsigned char edje_edit_part_restack_above (Evas_Object * obj, const char * part)</h3>
<p>Move the given part above the next one. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part to restack</dl>
<h3>EAPI unsigned char edje_edit_part_restack_below (Evas_Object * obj, const char * part)</h3>
<p>Move the given part below the previous one. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part to restack</dl>
<h3>EAPI const char* edje_edit_part_selected_state_get (Evas_Object * obj, const char * part)</h3>
<p>Get the current selected state in part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the selected state including the float value. Use <code>edje_edit_string_free()</code> when you don&#8217;t need it anymore.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI unsigned char edje_edit_part_selected_state_set (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Set the current state in part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the state to set (including the float value)</dl>
<h3>EAPI const char* edje_edit_part_source_get (Evas_Object * obj, const char * part)</h3>
<p>Get the source of part. </p>
<p> Source is used in part of type EDJE_PART_TYPE_GROUP to specify the group to &#8216;autoswallow&#8217; inside the given part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the group to source the given part. Use <code>edje_edit_string_free()</code> when you don&#8217;t need it anymore.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI unsigned char edje_edit_part_source_set (Evas_Object * obj, const char * part, const char * source)</h3>
<p>Set the source of part. </p>
<p> Source is used in part of type EDJE_PART_TYPE_GROUP to specify the group to &#8216;autoswallow&#8217; inside the given part. NOTE: This is not applied now. You must reload the edje to see the change. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>source</i> The name of the group to autoswallow in the given part</dl>
<h3>EAPI Evas_List* edje_edit_part_states_list_get (Evas_Object * obj, const char * part)</h3>
<p>Get the list of all the states in the given part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string (char *)containing all the states names found in part, including the float value (ex: &#8216;default 0.00&#8217;). Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI unsigned char edje_edit_part_type_get (Evas_Object * obj, const char * part)</h3>
<p>Get the type of a part. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>One of: EDJE_PART_TYPE_NONE, EDJE_PART_TYPE_RECTANGLE, EDJE_PART_TYPE_TEXT,EDJE_PART_TYPE_IMAGE, EDJE_PART_TYPE_SWALLOW, EDJE_PART_TYPE_TEXTBLOCK,EDJE_PART_TYPE_GRADIENT or EDJE_PART_TYPE_GROUP</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part</dl>
<h3>EAPI Evas_List* edje_edit_parts_list_get (Evas_Object * obj)</h3>
<p>Get the list of all the parts in the given edje object. </p>
<p> Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string (char *)containing all the part names.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI void edje_edit_print_internal_status (Evas_Object * obj)</h3>
<p>Print on standard output many information about the internal status of the edje object. </p>
<p> This is probably only usefull to debug. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object to inspect</dl>
<h3>EAPI int edje_edit_program_action_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the action of a given program. </p>
<p> Action can be one of EDJE_ACTION_TYPE_NONE, _STATE_SET, ACTION_STOP, SIGNAL_EMIT, DRAG_VAL_SET, _DRAG_VAL_STEP, _DRAG_VAL_PAGE, _SCRIPT </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The action type, or -1 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_action_set (Evas_Object * obj, const char * prog, int action)</h3>
<p>Set the action of a given program. </p>
<p> Action can be one of EDJE_ACTION_TYPE_NONE, _STATE_SET, ACTION_STOP, SIGNAL_EMIT, DRAG_VAL_SET, _DRAG_VAL_STEP, _DRAG_VAL_PAGE, _SCRIPT </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>action</i> The new action type</dl>
<h3>EAPI unsigned char edje_edit_program_add (Evas_Object * obj, const char * name)</h3>
<p>Add a new program to the edje file If a program with the same name just exist the function will fail. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>name</i> The name of the new program</dl>
<h3>EAPI unsigned char edje_edit_program_after_add (Evas_Object * obj, const char * prog, const char * after)</h3>
<p>Add a new program name to the list of &#8216;afters&#8217; in the given program. </p>
<p> All the programs listed in &#8216;afters&#8217; will be executed after program execution. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>after</i> The name of another program to add to the afters list</dl>
<h3>EAPI unsigned char edje_edit_program_afters_clear (Evas_Object * obj, const char * prog)</h3>
<p>Clear the &#8216;afters&#8217; list of the given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI Evas_List* edje_edit_program_afters_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the list of action that will be run after the give program Return a list of program name. </p>
<p> Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List of char*, or NULL on error</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_del (Evas_Object * obj, const char * prog)</h3>
<p>Remove the given program from the edje file. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The name of the program to remove</dl>
<h3>EAPI unsigned char edje_edit_program_exist (Evas_Object * obj, const char * prog)</h3>
<p>Check if a program with the given name exist in the edje object. </p>
<p> &lt; 1 if the program exist, 0 otherwise. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The name of the program</dl>
<h3>EAPI double edje_edit_program_in_from_get (Evas_Object * obj, const char * prog)</h3>
<p>Get in.from of a given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The delay</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_in_from_set (Evas_Object * obj, const char * prog, double seconds)</h3>
<p>Set in.from of a given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>seconds</i> Number of seconds to delay the program execution</dl>
<h3>EAPI double edje_edit_program_in_range_get (Evas_Object * obj, const char * prog)</h3>
<p>Get in.range of a given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The delay random</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_in_range_set (Evas_Object * obj, const char * prog, double seconds)</h3>
<p>Set in.range of a given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>seconds</i> Max random number of seconds to delay</dl>
<h3>EAPI unsigned char edje_edit_program_name_set (Evas_Object * obj, const char * prog, const char * new_name)</h3>
<p>Set a new name for the given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>new_name</i> The new name to assign</dl>
<h3>EAPI unsigned char edje_edit_program_run (Evas_Object * obj, const char * prog)</h3>
<p>Run the given program. </p>
<p> &lt; 1 on success, 0 otherwise. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The name of the program to execute</dl>
<h3>EAPI const char* edje_edit_program_signal_get (Evas_Object * obj, const char * prog)</h3>
<p>Get signal of a given program. </p>
<p> Remember to free the returned string using <code>edje_edit_string_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The signal value for prog</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_signal_set (Evas_Object * obj, const char * prog, const char * signal)</h3>
<p>Set signal of the given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>signal</i> The new signal value</dl>
<h3>EAPI const char* edje_edit_program_source_get (Evas_Object * obj, const char * prog)</h3>
<p>Get source of a given program. </p>
<p> Remember to free the returned string using <code>edje_edit_string_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The source value for prog</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_source_set (Evas_Object * obj, const char * prog, const char * source)</h3>
<p>Set source of the given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>source</i> The new source value</dl>
<h3>EAPI const char* edje_edit_program_state2_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the state2 for the given program In a STATE_SET action is not used In a SIGNAL_EMIT action is the source of the emitted signal. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The source to emit for prog</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_state2_set (Evas_Object * obj, const char * prog, const char * state2)</h3>
<p>Set the state2 for the given program In a STATE_SET action is not used In a SIGNAL_EMIT action is the source of the emitted signal. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>state2</i> The state2 value to set</dl>
<h3>EAPI const char* edje_edit_program_state_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the state for the given program In a STATE_SET action this is the name of state to set. </p>
<p> In a SIGNAL_EMIT action is the name of the signal to emit. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of state for prog</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_state_set (Evas_Object * obj, const char * prog, const char * state)</h3>
<p>Set the state for the given program In a STATE_SET action this is the name of state to set. </p>
<p> In a SIGNAL_EMIT action is the name of the signal to emit. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>state</i> The state to set (not including the state value)</dl>
<h3>EAPI unsigned char edje_edit_program_target_add (Evas_Object * obj, const char * prog, const char * target)</h3>
<p>Add a new target name to the list of &#8216;targets&#8217; in the given program. </p>
<p> If program action is EDJE_ACTION_TYPE_ACTION_STOP then &#8216;target&#8217; must be an existing program name. If action is EDJE_ACTION_TYPE_STATE_SET then &#8216;target&#8217; must be an existing part name. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>target</i> The name of another program or another part</dl>
<h3>EAPI unsigned char edje_edit_program_targets_clear (Evas_Object * obj, const char * prog)</h3>
<p>Clear the &#8216;targets&#8217; list of the given program. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI Evas_List* edje_edit_program_targets_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the list of the targets for the given program Return a list of target name Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List of char*, or NULL on error</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI int edje_edit_program_transition_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the type of transition to use when apply animations. </p>
<p> Can be one of: EDJE_TWEEN_MODE_NONE, EDJE_TWEEN_MODE_LINEAR, EDJE_TWEEN_MODE_SINUSOIDAL, EDJE_TWEEN_MODE_ACCELERATE or EDJE_TWEEN_MODE_DECELERATE. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The type of transition used by program</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_transition_set (Evas_Object * obj, const char * prog, int transition)</h3>
<p>Set the type of transition to use when apply animations. </p>
<p> Can be one of: EDJE_TWEEN_MODE_NONE, EDJE_TWEEN_MODE_LINEAR, EDJE_TWEEN_MODE_SINUSOIDAL, EDJE_TWEEN_MODE_ACCELERATE or EDJE_TWEEN_MODE_DECELERATE. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>transition</i> The transition type to set</dl>
<h3>EAPI double edje_edit_program_transition_time_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the duration of the transition in seconds. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The duration of the transition</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_transition_time_set (Evas_Object * obj, const char * prog, double seconds)</h3>
<p>Set the duration of the transition in seconds. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>seconds</i> The duration of the transition (in seconds)</dl>
<h3>EAPI double edje_edit_program_value2_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the value of state2 for the given program. </p>
<p> I don&#8217;t know what this is used for. :P </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The value of state2 for prog</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_value2_set (Evas_Object * obj, const char * prog, double value)</h3>
<p>Set the value2 of state for the given program. </p>
<p> This is used in DRAG_ACTION </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>value</i> The value to set</dl>
<h3>EAPI double edje_edit_program_value_get (Evas_Object * obj, const char * prog)</h3>
<p>Get the value of state for the given program. </p>
<p> In a STATE_SET action this is the value of state to set. Not used on SIGNAL_EMIT action. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The value of state for prog</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name</dl>
<h3>EAPI unsigned char edje_edit_program_value_set (Evas_Object * obj, const char * prog, double value)</h3>
<p>Set the value of state for the given program. </p>
<p> In a STATE_SET action this is the value of state to set. Not used on SIGNAL_EMIT action. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>prog</i> The program name<br />
 <i>value</i> The value to set</dl>
<h3>EAPI Evas_List* edje_edit_programs_list_get (Evas_Object * obj)</h3>
<p>Get the list of all the programs in the given edje object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string (char *)containing all the program names. Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore. </p>
<p> A string list containing all the program names</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI int edje_edit_save (Evas_Object * obj)</h3>
<p>Save the modified edje object back to his file. </p>
<p> Use this function when you are done with your editing, all the change made to the current loaded group will be saved back to the original file. </p>
<p> NOTE: for now this as 2 limitations -the saved edje file cannot be decompiled anymore -you will lost your define in the edc source </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object to save</dl>
<h3>EAPI unsigned char edje_edit_spectra_add (Evas_Object * obj, const char * name)</h3>
<p>Add a new spectra in the given edje object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>name</i> The name of the new spectra</dl>
<h3>EAPI unsigned char edje_edit_spectra_del (Evas_Object * obj, const char * spectra)</h3>
<p>Delete the given spectra from the edje object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>spectra</i> The name of the spectra to delete</dl>
<h3>EAPI unsigned char edje_edit_spectra_name_set (Evas_Object * obj, const char * spectra, const char * name)</h3>
<p>Change the name of the given spectra. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>spectra</i> The current name of the spectra<br />
 <i>name</i> The new name to assign</dl>
<h3>EAPI unsigned char edje_edit_spectra_stop_color_get (Evas_Object * obj, const char * spectra, int stop_number, int * r, int * g, int * b, int * a, int * d)</h3>
<p>Get the colors of the given stop. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>spectra</i> The name of the spectra<br />
 <i>stop_number</i> The number of the stop<br />
 <i>r</i> Where to store the red color value<br />
 <i>g</i> Where to store the green color value<br />
 <i>b</i> Where to store the blue color value<br />
 <i>a</i> Where to store the alpha color value<br />
 <i>d</i> Where to store the delta stop value</dl>
<h3>EAPI unsigned char edje_edit_spectra_stop_color_set (Evas_Object * obj, const char * spectra, int stop_number, int r, int g, int b, int a, int d)</h3>
<p>Set the colors of the given stop. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>spectra</i> The name of the spectra<br />
 <i>stop_number</i> The number of the stop<br />
 <i>r</i> The red color value to set<br />
 <i>g</i> The green color value to set<br />
 <i>b</i> The blue color value to set<br />
 <i>a</i> The alpha color value to set<br />
 <i>d</i> The delta stop value to set</dl>
<h3>EAPI int edje_edit_spectra_stop_num_get (Evas_Object * obj, const char * spectra)</h3>
<p>Get the number of stops in the given spectra. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of stops, or 0 on errors</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>spectra</i> The name of the spectra</dl>
<h3>EAPI unsigned char edje_edit_spectra_stop_num_set (Evas_Object * obj, const char * spectra, int num)</h3>
<p>Set the number of stops in the given spectra. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>spectra</i> The name of the spectra<br />
 <i>num</i> The number of stops you want</dl>
<h3>EAPI Evas_List* edje_edit_spectrum_list_get (Evas_Object * obj)</h3>
<p>Get the list of all the spectrum in the given edje object. </p>
<p> Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Evas_List* of string(char *) containing all the spectra names.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object</dl>
<h3>EAPI void edje_edit_state_add (Evas_Object * obj, const char * part, const char * name)</h3>
<p>Create a new state to the give part. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>name</i> The name for the new state (not including the state value)</dl>
<h3>EAPI double edje_edit_state_align_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the align_x value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The horizontal align value for the given state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_align_x_set (Evas_Object * obj, const char * part, const char * state, double align)</h3>
<p>Set the align_x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>align</i> The new horizontal align to set</dl>
<h3>EAPI double edje_edit_state_align_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the align_y value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The vertical align value for the given state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_align_y_set (Evas_Object * obj, const char * part, const char * state, double align)</h3>
<p>Set the align_y value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>align</i> The new vertical align to set</dl>
<h3>EAPI double edje_edit_state_aspect_max_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the maximum aspect value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The aspect maximum value of a part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_aspect_max_set (Evas_Object * obj, const char * part, const char * state, double aspect)</h3>
<p>Set the maximum aspect value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>aspect</i> The new maximum aspect value to set</dl>
<h3>EAPI double edje_edit_state_aspect_min_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the minimum aspect value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The aspect minimum value of a part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_aspect_min_set (Evas_Object * obj, const char * part, const char * state, double aspect)</h3>
<p>Set the minimum aspect value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>aspect</i> The new minimum aspect value to set</dl>
<h3>EAPI unsigned char edje_edit_state_aspect_pref_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the aspect preference value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The aspect preference (0=none, 1=vertical, 2=horizontal, 3=both)</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_aspect_pref_set (Evas_Object * obj, const char * part, const char * state, unsigned char pref)</h3>
<p>Set the aspect preference value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>pref</i> The new aspect preference to set (0=none, 1=vertical, 2=horizontal, 3=both)</dl>
<h3>EAPI void edje_edit_state_color2_get (Evas_Object * obj, const char * part, const char * state, int * r, int * g, int * b, int * a)</h3>
<p>Get the color2 of a part state. </p>
<p> Pass NULL to any of [r,g,b,a] to get only the others. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>r</i> A pointer to store the red value<br />
 <i>g</i> A pointer to store the green value<br />
 <i>b</i> A pointer to store the blue value<br />
 <i>a</i> A pointer to store the alpha value</dl>
<h3>EAPI void edje_edit_state_color2_set (Evas_Object * obj, const char * part, const char * state, int r, int g, int b, int a)</h3>
<p>Set the color2 of a part state. </p>
<p> Pass -1 to any of [r,g,b,a] to leave the value untouched. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>r</i> The red value of the color<br />
 <i>g</i> The green value of the color<br />
 <i>b</i> The blue value of the color<br />
 <i>a</i> The alpha value of the color</dl>
<h3>EAPI void edje_edit_state_color3_get (Evas_Object * obj, const char * part, const char * state, int * r, int * g, int * b, int * a)</h3>
<p>Get the color3 of a part state. </p>
<p> Pass NULL to any of [r,g,b,a] to get only the others. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>r</i> A pointer to store the red value<br />
 <i>g</i> A pointer to store the green value<br />
 <i>b</i> A pointer to store the blue value<br />
 <i>a</i> A pointer to store the alpha value</dl>
<h3>EAPI void edje_edit_state_color3_set (Evas_Object * obj, const char * part, const char * state, int r, int g, int b, int a)</h3>
<p>Set the color3 of a part state. </p>
<p> Pass -1 to any of [r,g,b,a] to leave the value untouched. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>r</i> The red value of the color<br />
 <i>g</i> The green value of the color<br />
 <i>b</i> The blue value of the color<br />
 <i>a</i> The alpha value of the color</dl>
<h3>EAPI void edje_edit_state_color_get (Evas_Object * obj, const char * part, const char * state, int * r, int * g, int * b, int * a)</h3>
<p>Get the color of a part state. </p>
<p> Pass NULL to any of [r,g,b,a] to get only the others. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>r</i> A pointer to store the red value<br />
 <i>g</i> A pointer to store the green value<br />
 <i>b</i> A pointer to store the blue value<br />
 <i>a</i> A pointer to store the alpha value</dl>
<h3>EAPI void edje_edit_state_color_set (Evas_Object * obj, const char * part, const char * state, int r, int g, int b, int a)</h3>
<p>Set the color of a part state. </p>
<p> Pass -1 to any of [r,g,b,a] to leave the value untouched. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>r</i> The red value of the color<br />
 <i>g</i> The green value of the color<br />
 <i>b</i> The blue value of the color<br />
 <i>a</i> The alpha value of the color</dl>
<h3>EAPI void edje_edit_state_del (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Delete the given part state from the edje. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part that contain state<br />
 <i>state</i> The current name of the state (including the state value)</dl>
<h3>EAPI unsigned char edje_edit_state_exist (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Check if a part state with the given name exist. </p>
<p> &lt; 1 if the part state exist, 0 otherwise. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the state to check (including the state value)</dl>
<h3>EAPI int edje_edit_state_fill_origin_offset_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill origin offset x value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill origin offset x relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_origin_offset_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the fill origin offset x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new value to set</dl>
<h3>EAPI int edje_edit_state_fill_origin_offset_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill origin offset y value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill origin offset y relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_origin_offset_y_set (Evas_Object * obj, const char * part, const char * state, double y)</h3>
<p>Set the fill origin offset x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>y</i> The new value to set</dl>
<h3>EAPI double edje_edit_state_fill_origin_relative_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill origin relative x value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill offset x relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_origin_relative_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the fill origin relative x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new value to set</dl>
<h3>EAPI double edje_edit_state_fill_origin_relative_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill origin relative y value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill origin y relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_origin_relative_y_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the fill origin relative y value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new value to set</dl>
<h3>EAPI int edje_edit_state_fill_size_offset_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill size offset x value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill size offset x relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_size_offset_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the fill size offset x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new value to set</dl>
<h3>EAPI int edje_edit_state_fill_size_offset_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill size offset y value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill size offset y relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_size_offset_y_set (Evas_Object * obj, const char * part, const char * state, double y)</h3>
<p>Set the fill size offset x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>y</i> The new value to set</dl>
<h3>EAPI double edje_edit_state_fill_size_relative_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill size relative x value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill size offset x relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_size_relative_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the fill size relative x value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new value to set</dl>
<h3>EAPI double edje_edit_state_fill_size_relative_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the fill size relative y value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The fill size y relative to area</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_fill_size_relative_y_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the fill size relative y value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new value to set</dl>
<h3>EAPI const char* edje_edit_state_font_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get font name for a given part state. </p>
<p> Remember to free the returned string using <code>edje_edit_string_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the font used in the given part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_font_set (Evas_Object * obj, const char * part, const char * state, const char * font)</h3>
<p>Set font name for a given part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>font</i> The name of the font to use in the given part state</dl>
<h3>EAPI int edje_edit_state_gradient_rel1_offset_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel1 offset x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradient rel1 offset x value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel1_offset_x_set (Evas_Object * obj, const char * part, const char * state, int val)</h3>
<p>Set the gradien rel1 offset x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI int edje_edit_state_gradient_rel1_offset_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel1 offset y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradient rel1 offset y value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel1_offset_y_set (Evas_Object * obj, const char * part, const char * state, int val)</h3>
<p>Set the gradien rel1 offset y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI double edje_edit_state_gradient_rel1_relative_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel1 relative x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradien rel1 relative x value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel1_relative_x_set (Evas_Object * obj, const char * part, const char * state, double val)</h3>
<p>Set the gradien rel1 relative x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI double edje_edit_state_gradient_rel1_relative_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel1 relative y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradien rel1 relative y value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel1_relative_y_set (Evas_Object * obj, const char * part, const char * state, double val)</h3>
<p>Set the gradien rel1 relative y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI int edje_edit_state_gradient_rel2_offset_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel2 offset x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradient rel2 offset x value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel2_offset_x_set (Evas_Object * obj, const char * part, const char * state, int val)</h3>
<p>Set the gradien rel2 offset x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI int edje_edit_state_gradient_rel2_offset_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel2 offset y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradient rel2 offset y value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel2_offset_y_set (Evas_Object * obj, const char * part, const char * state, int val)</h3>
<p>Set the gradien rel2 offset y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI double edje_edit_state_gradient_rel2_relative_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel2 relative x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradien rel2 relative x value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel2_relative_x_set (Evas_Object * obj, const char * part, const char * state, double val)</h3>
<p>Set the gradien rel2 relative x value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI double edje_edit_state_gradient_rel2_relative_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the gradien rel2 relative y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The gradien rel2 relative y value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_rel2_relative_y_set (Evas_Object * obj, const char * part, const char * state, double val)</h3>
<p>Set the gradien rel2 relative y value. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI const char* edje_edit_state_gradient_spectra_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the spectra used by part state. </p>
<p> Remember to free the string with <code>edje_edit_string_free()</code> </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The spectra name used in state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_spectra_set (Evas_Object * obj, const char * part, const char * state, const char * spectra)</h3>
<p>Set the spectra used by part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>spectra</i> The spectra name to assign</dl>
<h3>EAPI const char* edje_edit_state_gradient_type_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the type of gradient. </p>
<p> Remember to free the string with <code>edje_edit_string_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The type of gradient used in state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_type_set (Evas_Object * obj, const char * part, const char * state, const char * type)</h3>
<p>Set the type of gradient. </p>
<p> Gradient type can be on of the following: linear, linear.diag, linear.codiag, radial, rectangular, angular, sinusoidal </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>type</i> The type of gradient to use</dl>
<h3>EAPI unsigned char edje_edit_state_gradient_use_fill_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get if the current gradient use the fill properties or the gradient_rel as params. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if use fill, 0 if use gradient_rel</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_image_border_get (Evas_Object * obj, const char * part, const char * state, int * l, int * r, int * t, int * b)</h3>
<p>Get the image border of a part state. </p>
<p> Pass NULL to any of [r,g,b,a] to get only the others. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>l</i> A pointer to store the left value<br />
 <i>r</i> A pointer to store the right value<br />
 <i>t</i> A pointer to store the top value<br />
 <i>b</i> A pointer to store the bottom value</dl>
<h3>EAPI void edje_edit_state_image_border_set (Evas_Object * obj, const char * part, const char * state, int l, int r, int t, int b)</h3>
<p>Set the image border of a part state. </p>
<p> Pass -1 to any of [l,r,t,b] to leave the value untouched. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>l</i> The new left border (or -1)<br />
 <i>r</i> The new right border (or -1)<br />
 <i>t</i> The new top border (or -1)<br />
 <i>b</i> The new bottom border (or -1)</dl>
<h3>EAPI const char* edje_edit_state_image_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get normal image name for a given part state. </p>
<p> Remember to free the returned string using <code>edje_edit_string_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the image used by state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_image_set (Evas_Object * obj, const char * part, const char * state, const char * image)</h3>
<p>Set normal image for a given part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>image</i> The name of the image for the given state (must be an image contained in the edje file)</dl>
<h3>EAPI int edje_edit_state_max_h_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the max_h value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum height of a part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_max_h_set (Evas_Object * obj, const char * part, const char * state, int max_h)</h3>
<p>Set the max_h value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>max_h</i> The new maximum height to set for the part state</dl>
<h3>EAPI int edje_edit_state_max_w_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the max_w value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum width of a part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_max_w_set (Evas_Object * obj, const char * part, const char * state, int max_w)</h3>
<p>Set the max_w value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>max_w</i> The new maximum width to set for the part state</dl>
<h3>EAPI int edje_edit_state_min_h_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the min_h value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The minimum height of a part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_min_h_set (Evas_Object * obj, const char * part, const char * state, int min_h)</h3>
<p>Set the min_h value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>min_h</i> The new minimum height to set for the part state</dl>
<h3>EAPI int edje_edit_state_min_w_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the min_w value of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The minimum width of a part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_min_w_set (Evas_Object * obj, const char * part, const char * state, int min_w)</h3>
<p>Set the min_w value of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>min_w</i> The new minimum width to set for the part state</dl>
<h3>EAPI int edje_edit_state_name_set (Evas_Object * obj, const char * part, const char * state, const char * new_name)</h3>
<p>Set a new name for the given state in the given part. </p>
<p> Note that state and new_name must include the floating value inside the string (ex. &#8216;default 0.00&#8217;) <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part that contain state<br />
 <i>state</i> The current name of the state<br />
 <i>new_name</i> The new name to assign (including the value)</dl>
<h3>EAPI int edje_edit_state_rel1_offset_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel1 offset x value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel1 offset X&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel1_offset_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the rel1 offset x value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new &#8216;rel1 offset X&#8217; value to set</dl>
<h3>EAPI int edje_edit_state_rel1_offset_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel1 offset y value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel1 offset Y&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel1_offset_y_set (Evas_Object * obj, const char * part, const char * state, double y)</h3>
<p>Get the rel1 offset y value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>y</i> The new &#8216;rel1 offset Y&#8217; value to set</dl>
<h3>EAPI double edje_edit_state_rel1_relative_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel1 relative x value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel1 relative X&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the part state (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel1_relative_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the rel1 relative x value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new &#8216;rel1 relative X&#8217; value to set</dl>
<h3>EAPI double edje_edit_state_rel1_relative_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel1 relative y value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel1 relative Y&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel1_relative_y_set (Evas_Object * obj, const char * part, const char * state, double y)</h3>
<p>Set the rel1 relative y value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>y</i> The new &#8216;rel1 relative Y&#8217; value to set</dl>
<h3>EAPI const char* edje_edit_state_rel1_to_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the part name rel1x is relative to. </p>
<p> The function return NULL if the part is relative to the whole interface. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the part to apply the relativity</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel1_to_x_set (Evas_Object * obj, const char * part, const char * state, const char * rel_to)</h3>
<p>Set the part rel1x is relative to. </p>
<p> Set rel_to to NULL make the part relative to the whole interface. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>rel_to</i> The name of the part that is used as container/parent</dl>
<h3>EAPI const char* edje_edit_state_rel1_to_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the part name rel1y is relative to. </p>
<p> The function return NULL if the part is relative to the whole interface. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the part to apply the relativity</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel1_to_y_set (Evas_Object * obj, const char * part, const char * state, const char * rel_to)</h3>
<p>Set the part rel1y is relative to. </p>
<p> Set rel_to to NULL make the part relative to the whole interface. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>rel_to</i> The name of the part that is used as container/parent</dl>
<h3>EAPI int edje_edit_state_rel2_offset_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel2 offset x value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel2 offset X&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel2_offset_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Get the rel2 offset x value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new &#8216;rel2 offset X&#8217; value to set</dl>
<h3>EAPI int edje_edit_state_rel2_offset_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel2 offset y value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel2 offset Y&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel2_offset_y_set (Evas_Object * obj, const char * part, const char * state, double y)</h3>
<p>Get the rel2 offset y value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>y</i> The new &#8216;rel2 offset Y&#8217; value to set</dl>
<h3>EAPI double edje_edit_state_rel2_relative_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel2 relative x value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel2 relative X&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel2_relative_x_set (Evas_Object * obj, const char * part, const char * state, double x)</h3>
<p>Set the rel2 relative x value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>x</i> The new &#8216;rel2 relative X&#8217; value to set</dl>
<h3>EAPI double edje_edit_state_rel2_relative_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the rel2 relative y value of state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The &#8216;rel2 relative Y&#8217; value of the part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel2_relative_y_set (Evas_Object * obj, const char * part, const char * state, double y)</h3>
<p>Set the rel2 relative y value of state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>y</i> The new &#8216;rel2 relative Y&#8217; value to set</dl>
<h3>EAPI const char* edje_edit_state_rel2_to_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the part name rel2x is relative to. </p>
<p> The function return NULL if the part is relative to the whole interface. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the part to apply the relativity</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel2_to_x_set (Evas_Object * obj, const char * part, const char * state, const char * rel_to)</h3>
<p>Set the part rel2x is relative to. </p>
<p> Set rel_to to NULL make the part relative to the whole interface. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>rel_to</i> The name of the part that is used as container/parent</dl>
<h3>EAPI const char* edje_edit_state_rel2_to_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the part name rel2y is relative to. </p>
<p> The function return NULL if the part is relative to the whole interface. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the part to apply the relativity</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_rel2_to_y_set (Evas_Object * obj, const char * part, const char * state, const char * rel_to)</h3>
<p>Set the part rel2y is relative to. </p>
<p> Set rel_to to NULL make the part relative to the whole interface. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>rel_to</i> The name of the part that is used as container/parent</dl>
<h3>EAPI double edje_edit_state_text_align_x_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the text horizontal align of a part state. </p>
<p> The value range is from 0.0(right) to 1.0(left) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The text align X value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_text_align_x_set (Evas_Object * obj, const char * part, const char * state, double align)</h3>
<p>Set the text horizontal align of a part state. </p>
<p> The value range is from 0.0(right) to 1.0(left) <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>align</i> The new text align X value</dl>
<h3>EAPI double edje_edit_state_text_align_y_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the text vertical align of a part state. </p>
<p> The value range is from 0.0(top) to 1.0(bottom) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The text align Y value</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_text_align_y_set (Evas_Object * obj, const char * part, const char * state, double align)</h3>
<p>Set the text vertical align of a part state. </p>
<p> The value range is from 0.0(top) to 1.0(bottom) <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>align</i> The new text align Y value</dl>
<h3>EAPI const char* edje_edit_state_text_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the text of a part state. </p>
<p> Remember to free the returned string with <code>edje_edit_string_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated string containing the text for the given state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_text_set (Evas_Object * obj, const char * part, const char * state, const char * text)</h3>
<p>Set the text of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>text</i> The new text to assign</dl>
<h3>EAPI int edje_edit_state_text_size_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the text size of a part state. </p>
<p> The function will return -1 on errors. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The font size in pixel or -1 on errors.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_text_size_set (Evas_Object * obj, const char * part, const char * state, int size)</h3>
<p>Set the text size of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>size</i> The new font size to set (in pixel)</dl>
<h3>EAPI unsigned char edje_edit_state_tween_add (Evas_Object * obj, const char * part, const char * state, const char * tween)</h3>
<p>Add a new tween frame to the given part state The tween param must be the name of an existing image. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>tween</i> The name of the image to add.</dl>
<h3>EAPI unsigned char edje_edit_state_tween_del (Evas_Object * obj, const char * part, const char * state, const char * tween)</h3>
<p>Remove the first tween with the given name. </p>
<p> If none is removed the function return 0. The image is not removed from the edje. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>tween</i> The name of the image to remove from the tween list.</dl>
<h3>EAPI Evas_List* edje_edit_state_tweens_list_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the list of all the tweens images in the given part state. </p>
<p> Use <code>edje_edit_string_list_free()</code> when you don&#8217;t need it anymore. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A string list containing all the image name that form a tween animation in the given part state</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI unsigned char edje_edit_state_visible_get (Evas_Object * obj, const char * part, const char * state)</h3>
<p>Get the visibility of a part state. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if the state is visible</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)</dl>
<h3>EAPI void edje_edit_state_visible_set (Evas_Object * obj, const char * part, const char * state, unsigned char visible)</h3>
<p>Set the visibility of a part state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The edje object<br />
 <i>part</i> The name of the part<br />
 <i>state</i> The name of the &#8216;part state&#8217; (ex. &#8216;default 0.00&#8217;)<br />
 <i>visible</i> TRUE to set the state visible</dl>
<h3>EAPI void edje_edit_string_free (const char * str)</h3>
<p>Free a generic string (char *) allocated by an edje_edit_*_get() function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> The string to free.</dl>
<h3>EAPI void edje_edit_string_list_free (Evas_List * lst)</h3>
<p>Free a generic Evas_List of (char *) allocated by an edje_edit_*_get() function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lst</i> The list to free. Will also free all the strings.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Edje from the source code.</p>
