---
title: "globus_ftp_client_plugin_write_t(3)"
name: "globus_ftp_client_plugin_write_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_plugin_write_t/"
---

<h2 class="name">NAME</h2>
 

 Plugins - 

 Plugin API.

<h3>Modules</h3>

 

 
 <b>Debugging Plugin</b> 
 
 <b>Performance Marker Plugin</b> 
 
 <b>Restart Marker Plugin</b> 
 
 <b>Restart Plugin</b> 
 
 <b>Netlogger Throughput Plugin</b> 
 
 <b>Throughput Performance Plugin</b> 

<h3>Data Structures</h3>

 

 
 struct <b>globus_i_ftp_client_plugin_t</b> 
 <i>FTP Client Plugin.</i> 

 Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. &quot;

<h3>Typedefs</h3>

 

 
 typedef struct 
 <b>globus_i_ftp_client_plugin_t</b> * <b>globus_ftp_client_plugin_t</b>&quot; 
 <i>FTP Client plugin</i> 

 An FTP Client plugin is used to add restart, monitoring, and performance tuning operations to the FTP Client library, without modifying the base API. Multiple plugins may be associated with a globus_ftp_client_handle_t. &quot; 
 typedef 
 <b>globus_ftp_client_plugin_t</b> *(* <b>globus_ftp_client_plugin_copy_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin_template, void *plugin_specific)&quot; 
 
 typedef void(* <b>globus_ftp_client_plugin_destroy_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific) 
 
 typedef void(* <b>globus_ftp_client_plugin_connect_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url) 
 
 typedef void(* <b>globus_ftp_client_plugin_authenticate_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const globus_ftp_control_auth_info_t *auth_info) 
 
 typedef void(* <b>globus_ftp_client_plugin_chmod_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, int mode, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_chgrp_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *group, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_utime_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const struct tm *utime_time, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_symlink_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *utime_time, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_cksm_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_off_t offset, globus_off_t length, const char *algorithm, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_delete_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_feat_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_mkdir_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_rmdir_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_list_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_verbose_list_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_machine_list_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_recursive_list_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_mlst_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_stat_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_move_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_get_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_put_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_third_party_transfer_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *dest_attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_modification_time_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_size_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart) 
 
 typedef void(* <b>globus_ftp_client_plugin_abort_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle) 
 
 typedef void(* <b>globus_ftp_client_plugin_read_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const globus_byte_t *buffer, globus_size_t buffer_length) 
 
 typedef void(* <b>globus_ftp_client_plugin_write_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const globus_byte_t *buffer, globus_size_t buffer_length, globus_off_t offset, globus_bool_t eof) 
 
 typedef void(* <b>globus_ftp_client_plugin_data_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, globus_object_t *error, const globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof) 
 
 typedef void(* <b>globus_ftp_client_plugin_command_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *command) 
 
 typedef void(* <b>globus_ftp_client_plugin_response_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_object_t *error, const globus_ftp_control_response_t *ftp_response) 
 
 typedef void(* <b>globus_ftp_client_plugin_fault_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_object_t *error) 
 
 typedef void(* <b>globus_ftp_client_plugin_complete_t</b> )(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle) 
 
 typedef struct 
 <b>globus_i_ftp_client_plugin_t</b> <b>globus_i_ftp_client_plugin_t</b>&quot; 
 <i>FTP Client Plugin.</i> 

 Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. &quot;

<h3>Enumerations</h3>

 

 
 enum <b>globus_ftp_client_plugin_command_mask_t</b> { , <b>GLOBUS_FTP_CLIENT_CMD_MASK_CONTROL_ESTABLISHMENT</b> = 1&lt;&lt;0, <b>GLOBUS_FTP_CLIENT_CMD_MASK_DATA_ESTABLISHMENT</b> = 1&lt;&lt;1, <b>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_PARAMETERS</b> = 1&lt;&lt;2, <b>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_MODIFIERS</b> = 1&lt;&lt;3, <b>GLOBUS_FTP_CLIENT_CMD_MASK_FILE_ACTIONS</b> = 1&lt;&lt;4, <b>GLOBUS_FTP_CLIENT_CMD_MASK_INFORMATION</b> = 1&lt;&lt;5, <b>GLOBUS_FTP_CLIENT_CMD_MASK_MISC</b> = 1&lt;&lt;6, <b>GLOBUS_FTP_CLIENT_CMD_MASK_BUFFER</b> = 1&lt;&lt;7, <b>GLOBUS_FTP_CLIENT_CMD_MASK_ALL</b> = 0x7fffffff } 

<h3>Functions</h3>

 

 
 globus_result_t <b>globus_ftp_client_plugin_restart_list</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_verbose_list</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_machine_list</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_recursive_list</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_mlst</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_stat</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_chmod</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, int mode, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_chgrp</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *group, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_utime</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const struct tm *utime_time, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_symlink</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *link_url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_cksm</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_off_t offset, globus_off_t length, const char *algorithm, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_delete</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_feat</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_mkdir</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_rmdir</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_move</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_get</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart_marker, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_put</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart_marker, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_third_party_transfer</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *dest_attr, <b>globus_ftp_client_restart_marker_t</b> *restart_marker, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_size</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_modification_time</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when) 
 
 globus_result_t <b>globus_ftp_client_plugin_restart_get_marker</b> (<b>globus_ftp_client_handle_t</b> *handle, <b>globus_ftp_client_restart_marker_t</b> *marker) 
 
 globus_result_t <b>globus_ftp_client_plugin_abort</b> (<b>globus_ftp_client_handle_t</b> *handle) 
 
 globus_result_t <b>globus_ftp_client_plugin_add_data_channels</b> (<b>globus_ftp_client_handle_t</b> *handle, unsigned int num_channels, unsigned int stripe) 
 
 globus_result_t <b>globus_ftp_client_plugin_remove_data_channels</b> (<b>globus_ftp_client_handle_t</b> *handle, unsigned int num_channels, unsigned int stripe) 

<h2>Detailed Description</h2>

 

 Plugin API. 

 A plugin is a way to implement application-independent reliability and performance tuning behavior. Plugins are written using the API described in this document. 

 A plugin is created by defining a globus_ftp_client_plugin_t which contains the function pointers and plugin-specific data needed for the plugin's operation. It is recommended that a plugin define a a globus_module_descriptor_t and plugin initialization functions, to ensure that the plugin is properly initialized. 

 The functions pointed to in a plugin are called when significant events in the life of an FTP Client operation occur. Note that plugins will only be called when the plugin has the function pointer for both the operation (get, put, list, etc), and the event (connect, authenticate, command, etc), are defined. The command and response functions are filtered based on the command_mask defined in the plugin structure. 

 Every plugin must define <b>copy </b> and <b>destroy </b> functions. The copy function is called when the plugin is added to an attribute set or a handle is initialized with an attribute set containing the plugin. The destroy function is called when the handle or attribute set is destroyed.

<h2>Typedef Documentation</h2>

 

<h3>typedef void(* globus_ftp_client_plugin_abort_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle)</h3>

 Plugin abort notification callback. 

 This callback is used to notify a plugin that an abort is being requested on a client handle. This notification happens both when the user aborts a request and when a plugin aborts the currently active request. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_authenticate_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const globus_ftp_control_auth_info_t *auth_info)</h3>

 Plugin authentication notification callback. 

 This callback is used to notify a plugin that an authentication handshake is being done for this client handle. This notification can occur when a new request is made or when a hard restart is done by a plugin. 

 If a response_callback is defined by a plugin, then that will be once the authentication has completed (successfully or unsuccessfully). 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the connection. 
 <i>url</i> The URL of the server to connect to. 
 <i>auth_info</i> Authentication and authorization info being used to authenticate with the FTP or GridFTP server.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_chgrp_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *group, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin chgrp notification callback. 

 This callback is used to notify a plugin that a chgrp is being requested on a client handle. This notification happens both when the user requests a chgrp, and when a plugin restarts the currently active chgrp request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the chgrp will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the delete operation. 
 <i>url</i> The url to chgrp. 
 <i>group</i> The group name or ID to change to. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_chmod_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, int mode, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin chmod notification callback. 

 This callback is used to notify a plugin that a chmod is being requested on a client handle. This notification happens both when the user requests a chmod, and when a plugin restarts the currently active chmod request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the chmod will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the delete operation. 
 <i>url</i> The url to chmod. 
 <i>mode</i> The file mode to be applied. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_cksm_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_off_t offset, globus_off_t length, const char *algorithm, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin cksm notification callback. 

 This callback is used to notify a plugin that a cksm is being requested on a client handle. This notification happens both when the user requests a cksm, and when a plugin restarts the currently active cksm request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the cksm will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the delete operation. 
 <i>url</i> The url to cksm. 
 <i>offset</i> File offset to start calculating checksum. 
 <i>length</i> Length of data to read from the starting offset. Use -1 to read the entire file. 
 <i>algorithm</i> A pointer to a string to be filled with the checksum of the file. On error the value pointed to by it is undefined. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_command_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *command)</h3>

 Command callback. 

 This callback is used to notify a plugin that a FTP control command is being sent. The client library will only call this function for response callbacks associated with a command which is in the plugin's command mask, and associated with one of the other ftp operations with a defined callback in the plugin. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request. 
 <i>url</i> The URL which this command is being sent to. 
 <i>command</i> A string containing the command which is being sent to the server (TYPE I, for example).</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_complete_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle)</h3>

 Completion notification callback. 

 This callback is used to notify a plugin that an operation previously begun has completed. The plugin may not call any other plugin operation on this handle after this has occurred. This is the final callback for the plugin while processing the operation. The plugin may free any internal state associated with the operation at this point. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the operation.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_connect_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url)</h3>

 Plugin connection begin function. 

 This callback is used to notify a plugin that connection establishment is being done for this client handle. This notification can occur when a new request is made or when a restart is done by a plugin. 

 If a response_callback is defined by a plugin, then that will be once the connection establishment has completed (successfully or unsuccessfully). 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the connection.</dl>
 

 <b>Note:</b>
<dl>
<dt>
<dd> This function will not be called for a get, put, or third-party transfer operation when a cached connection is used.</dl>
 

 

<h3>typedef <b>globus_ftp_client_plugin_t</b>*(* globus_ftp_client_plugin_copy_t)(<b>globus_ftp_client_plugin_t</b> *plugin_template, void *plugin_specific)</h3>

 Plugin copy function. 

 This function is used to create a new copy or reference count a plugin. This function is called by the FTP Client library when a plugin is added to a handle attribute set, or when a handle is initialized with an attribute which contains the plugin. 

 A plugin may not call any of the plugin API functions from it's instantiate method. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin_template</i> A plugin previously initialized by a call to the plugin-specific initialization function. by the user. 
 <i>plugin_specific</i> Plugin-specific data.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> A pointer to a plugin. This plugin copy must remain valid until the copy's <b>destroy</b> function is called on the copy.</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_plugin_destroy_t</b></dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_data_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, globus_object_t *error, const globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof)</h3>

 Plugin data callback handler. 

 This callback is used to notify a plugin that a read or write operation previously registered has completed. The buffer pointer will match that of a previous plugin read or write registration callback. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request. 
 <i>buffer</i> The buffer which was successfully transferred over the network. 
 <i>length</i> The amount of data to read or written. 
 <i>offset</i> The offset into the file where this data buffer belongs. 
 <i>eof</i> This value is set to GLOBUS_TRUE if end-of-file is being processed for this transfer.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_delete_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin delete notification callback. 

 This callback is used to notify a plugin that a delete is being requested on a client handle. This notification happens both when the user requests a delete, and when a plugin restarts the currently active delete request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the delete will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the delete operation. 
 <i>url</i> The url to be deleted. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_destroy_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific)</h3>

 Plugin destroy function. 

 This function is used to free or unreference a copy of a plugin which was allocated by calling the instantiate function from the plugin. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin, created by the create function, which is to be destroyed. 
 <i>plugin_specific</i> Plugin-specific data.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_fault_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_object_t *error)</h3>

 Fault notification callback. 

 This callback is used to notify a plugin that a fault occurred while processing the request. The fault may be internally generated, or come from a call to another library. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request. 
 <i>url</i> The url being processed when the fault ocurred. 
 <i>error</i> An error object describing the fault.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_feat_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin feat notification callback. 

 This callback is used to notify a plugin that a feat is being requested on a client handle. This notification happens both when the user requests a feat, and when a plugin restarts the currently active feat request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the feat will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the feat operation. 
 <i>url</i> The url to be feat'd. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current feat operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_get_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin get notification callback. 

 This callback is used to notify a plugin that a get is being requested on a client handle. This notification happens both when the user requests a get, and when a plugin restarts the currently active get request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the get will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the get operation. 
 <i>url</i> The url of the get operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current get transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_list_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin list notification callback. 

 This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_machine_list_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin machine list notification callback. 

 This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_mkdir_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin mkdir notification callback. 

 This callback is used to notify a plugin that a mkdir is being requested on a client handle. This notification happens both when the user requests a mkdir, and when a plugin restarts the currently active mkdir request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the mkdir will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the mkdir operation. 
 <i>url</i> The url of the directory to create. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current mkdir operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_mlst_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin mlst notification callback. 

 This callback is used to notify a plugin that a mlst is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_modification_time_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin modification time notification callback. 

 This callback is used to notify a plugin that a modification time check is being requested on a client handle. This notification happens both when the user requests the modification time of a file, and when a plugin restarts the currently active request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the modification time request will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_move_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin move notification callback. 

 This callback is used to notify a plugin that a move is being requested on a client handle. This notification happens both when the user requests a move, and when a plugin restarts the currently active move request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the move will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the move operation. 
 <i>source_url</i> The source url of the move operation. 
 <i>dest_url</i> The destination url of the move operation. 
 <i>attr</i> The attributes to be used during this move. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current move transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_put_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin put notification callback. 

 This callback is used to notify a plugin that a put is being requested on a client handle. This notification happens both when the user requests a put, and when a plugin restarts the currently active put request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the put will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the put operation. 
 <i>url</i> The url of the put operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current put transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_read_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const globus_byte_t *buffer, globus_size_t buffer_length)</h3>

 Plugin read registration callback. 

 This callback is used to notify a plugin that the client API has registered a buffer with the FTP control API for reading when processing a get. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request. 
 <i>buffer</i> The data buffer to read into. 
 <i>buffer_length</i> The maximum amount of data to read into the buffer.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_recursive_list_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin recursive list notification callback. 

 This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_response_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_object_t *error, const globus_ftp_control_response_t *ftp_response)</h3>

 Response callback. 

 This callback is used to notify a plugin that a FTP control response has occurred on a control connection. FTP response callbacks will come back to the user in the order which the commands were executed. The client library will only call this function for response callbacks associated with a command which is in the plugin's command mask, or associated with one of the other ftp operations with a defined callback in the plugin. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request. 
 <i>url</i> The URL which this response came from. 
 <i>error</i> An error which occurred while processing this command/response pair. 
 <i>ftp_response</i> The response structure from the ftp control library.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_rmdir_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin rmdir notification callback. 

 This callback is used to notify a plugin that a rmdir is being requested on a client handle. This notification happens both when the user requests a rmdir, and when a plugin restarts the currently active rmdir request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the rmdir will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the rmdir operation. 
 <i>url</i> The url of the rmdir operation. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current rmdir operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_size_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin size notification callback. 

 This callback is used to notify a plugin that a size check is being requested on a client handle. This notification happens both when the user requests the size of a file, and when a plugin restarts the currently active request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the size request will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_stat_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin stat notification callback. 

 This callback is used to notify a plugin that a stat is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_symlink_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *utime_time, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin symlink notification callback. 

 This callback is used to notify a plugin that a symlink is being requested on a client handle. This notification happens both when the user requests a symlink, and when a plugin restarts the currently active symlink request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the symlink will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the symlink operation. 
 <i>url</i> The url of the new link. 
 <i>link_url</i> The url to which the new link should point. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current utime operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef struct <b>globus_i_ftp_client_plugin_t</b>* <b>globus_ftp_client_plugin_t</b></h3>

 

 

 FTP Client plugin 

 An FTP Client plugin is used to add restart, monitoring, and performance tuning operations to the FTP Client library, without modifying the base API. Multiple plugins may be associated with a globus_ftp_client_handle_t. 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_handle_init()</b>, <b>globus_ftp_client_handle_destroy()</b>, <b>globus_ftp_client_handleattr_t</b>, <b>Debugging Plugin </b></dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_third_party_transfer_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *dest_attr, globus_bool_t restart)</h3>

 Plugin third-party transfer notification callback. 

 This callback is used to notify a plugin that a transfer is being requested on a client handle. This notification happens both when the user requests a transfer, and when a plugin restarts the currently active transfer request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the third-party transfer will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the transfer operation. 
 <i>source_url</i> The source url of the transfer operation. 
 <i>source_attr</i> The attributes to be used during this transfer on the source. 
 <i>dest_url</i> The destination url of the third-party transfer operation. 
 <i>dest_attr</i> The attributes to be used during this transfer on the destination. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current transfer transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_utime_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const struct tm *utime_time, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin utime notification callback. 

 This callback is used to notify a plugin that a utime is being requested on a client handle. This notification happens both when the user requests a utime, and when a plugin restarts the currently active utime request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the utime will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the utime operation. 
 <i>url</i> The url to utime. 
 <i>utime_time</i> The modification time to change the file to. 
 <i>attr</i> The attributes to be used during this operation. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current utime operation; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_verbose_list_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, globus_bool_t restart)</h3>

 Plugin verbose list notification callback. 

 This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. 

 If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the list operation. 
 <i>url</i> The url of the list operation. 
 <i>attr</i> The attributes to be used during this transfer. 
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
 

 

<h3>typedef void(* globus_ftp_client_plugin_write_t)(<b>globus_ftp_client_plugin_t</b> *plugin, void *plugin_specific, <b>globus_ftp_client_handle_t</b> *handle, const globus_byte_t *buffer, globus_size_t buffer_length, globus_off_t offset, globus_bool_t eof)</h3>

 Plugin write registration callback. 

 This callback is used to notify a plugin that the client API has registered a buffer with the FTP control API for writing when processing a put. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified. 
 <i>plugin_specific</i> Plugin-specific data. 
 <i>handle</i> The handle associated with the request. 
 <i>buffer</i> The buffer which is being written. 
 <i>buffer_length</i> The amount of data in the buffer. 
 <i>offset</i> The offset within the file where the buffer is to be written. 
 <i>eof</i> This value is set to GLOBUS_TRUE if this is the last data buffer to be sent for this put request.</dl>
 

 

<h3>typedef struct <b>globus_i_ftp_client_plugin_t</b> <b>globus_i_ftp_client_plugin_t</b></h3>

 

 

 FTP Client Plugin. 

 Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. Each plugin function may be either GLOBUS_NULL, or a valid function pointer. If the function is GLOBUS_NULL, then the plugin will not be notified when the corresponding event happens.

<h2>Enumeration Type Documentation</h2>

 

<h3>enum <b>globus_ftp_client_plugin_command_mask_t</b></h3>

 Command Mask. 

 This enumeration includes the types of commands which the plugin is interested in. 

 <b>Enumerator</b>
<dl>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_CONTROL_ESTABLISHMENT </i>
<dd> connect, authenticate
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_DATA_ESTABLISHMENT </i>
<dd> PASV, PORT, SPOR, SPAS
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_PARAMETERS </i>
<dd> MODE, TYPE, STRU, OPTS RETR, DCAU
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_MODIFIERS </i>
<dd> ALLO, REST
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_FILE_ACTIONS </i>
<dd> STOR, RETR, ESTO, ERET, APPE, LIST, NLST, MLSD, MLSR, GET, PUT
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_INFORMATION </i>
<dd> HELP, SITE HELP, FEAT, STAT, SYST, SIZE
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_MISC </i>
<dd> SITE, NOOP
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_BUFFER </i>
<dd> SBUF, ABUF
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_ALL </i>
<dd> All possible commands</dl>

<h2>Function Documentation</h2>

 

<h3>globus_result_t globus_ftp_client_plugin_abort (<b>globus_ftp_client_handle_t</b> *handle)</h3>

 Abort a transfer operation. 

 This function will cause the currently executing transfer operation to be aborted. When this happens, all plugins will be notified by their abort callbacks. Once those are processed, the complete callback will be called for all plugins, and then for the user's callback. 

 The complete callback will indicate that the transfer did not complete successfully. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_add_data_channels (<b>globus_ftp_client_handle_t</b> *handle, unsigned intnum_channels, unsigned intstripe)</h3>

 Add data channels to an existing put transfer. 

 This function will cause the currently executing transfer operation to have additional data channels acquired if the attribute set allows it. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer. 
 <i>num_channels</i> The number of channels to add to the transfer. 
 <i>stripe</i> The stripe number to have the channels added to.</dl>
 

 <b>Note:</b>
<dl>
<dt>
<dd> Do the plugins need to be notified when this happens?</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_remove_data_channels (<b>globus_ftp_client_handle_t</b> *handle, unsigned intnum_channels, unsigned intstripe)</h3>

 Remove data channels from an existing put transfer. 

 This function will cause the currently executing transfer operation to have data channels removed, if the attribute set allows it. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer. 
 <i>num_channels</i> The number of channels to remove from the transfer. 
 <i>stripe</i> The stripe number to have the channels removed from.</dl>
 

 <b>Note:</b>
<dl>
<dt>
<dd> Do the plugins need to be notified when this happens?</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_chgrp (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *group, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing chgrp. 

 This function will cause the currently executing chgrp operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in chgrp events will receive a chgrp callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chgrp. 
 <i>url</i> The destination URL of the transfer. This may be different than the original chgrp's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>group</i> The group name or ID to change the file to. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original chgrp's attribute set. 
 <i>when</i> Absolute time for when to restart the chgrp. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_chmod (<b>globus_ftp_client_handle_t</b> *handle, const char *url, intmode, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing chmod. 

 This function will cause the currently executing chmod operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in chmod events will receive a chmod callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chmod. 
 <i>url</i> The destination URL of the transfer. This may be different than the original chmod's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>mode</i> The file mode that will be applied. Must be an octal number repre- senting the bit pattern for the new permissions. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original chmod's attribute set. 
 <i>when</i> Absolute time for when to restart the chmod. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_cksm (<b>globus_ftp_client_handle_t</b> *handle, const char *url, globus_off_toffset, globus_off_tlength, const char *algorithm, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing cksm. 

 This function will cause the currently executing cksm operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in cksm events will receive a cksm callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the cksm. 
 <i>url</i> The destination URL of the transfer. This may be different than the original cksm's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>offset</i> File offset to start calculating checksum. 
 <i>length</i> Length of data to read from the starting offset. Use -1 to read the entire file. 
 <i>algorithm</i> A pointer to a string to be filled with the checksum of the file. On error the value pointed to by it is undefined. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original cksm's attribute set. 
 <i>when</i> Absolute time for when to restart the cksm. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_delete (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing delete. 

 This function will cause the currently executing delete operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in delete events will receive a delete callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the delete. 
 <i>url</i> The destination URL of the transfer. This may be different than the original delete's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original delete's attribute set. 
 <i>when</i> Absolute time for when to restart the delete. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_feat (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing feat. 

 This function will cause the currently executing feat operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in feat events will receive a feat callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the feat. 
 <i>url</i> The destination URL of the transfer. This may be different than the original feat's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original feat's attribute set. 
 <i>when</i> Absolute time for when to restart the feat. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_get (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart_marker, const globus_abstime_t *when)</h3>

 Restart an existing get. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in get events will receive a get callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the get. 
 <i>url</i> The source URL of the transfer. This may be different than the original get's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original get's attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent. 
 <i>restart_marker</i> Plugin-provided restart marker for resuming at a non-default restart point. This may be used to implement a persistent restart across process invocations. The default behavior if this is NULL is to use any restart information which has been received by the ftp client library while processing this operation when restarted. 
 <i>when</i> Absolute time for when to restart the get. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_get_marker (<b>globus_ftp_client_handle_t</b> *handle, <b>globus_ftp_client_restart_marker_t</b> *marker)</h3>

 Get restart marker 

 This function will allow this user to get the restart marker associated with a restarted file transfer. This function may only be called within the get, put, or third party transfer callback in which the 'restart' argument is GLOBUS_TRUE 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer. 
 <i>marker</i> Pointer to an uninitialized restart marker type</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> Error on NULL handle or marker
<dt>&bull;
<dd> Error on invalid use of function
<dt>&bull;
<dd> GLOBUS_SUCCESS (marker will be populated)</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_list (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing list. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list. 
 <i>url</i> The destination URL of the transfer. This may be different than the original list's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list's attribute set. 
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_machine_list (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing machine list. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list. 
 <i>url</i> The destination URL of the transfer. This may be different than the original list's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list's attribute set. 
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_mkdir (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing mkdir. 

 This function will cause the currently executing operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in mkdir events will receive a mkdir callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the mkdir. 
 <i>url</i> The destination URL of the transfer. This may be different than the original mkdir's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original mkdir's attribute set. 
 <i>when</i> Absolute time for when to restart the mkdir. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_mlst (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing MLST. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list. 
 <i>url</i> The destination URL of the transfer. This may be different than the original list's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list's attribute set. 
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_modification_time (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart a modification time check operation. 

 This function will cause the currently executing modification time check operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in modification time operations will receive a modification time callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the operation. 
 <i>url</i> The source URL of the modification time check. This may be different than the original operations URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new operation. This may be a modified version of the original operations's attribute set. 
 <i>when</i> Absolute time for when to restart the modification time check. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_move (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing move. 

 This function will cause the currently executing move operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially new URLs and attributes. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in get events will receive a move callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the move. 
 <i>source_url</i> The source URL of the move. This may be different than the original get's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>dest_url</i> The destination URL of the move. This may be different than the original get's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. Note that only the path component of this URL is used. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original move's attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent. 
 <i>when</i> Absolute time for when to restart the move. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_put (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart_marker, const globus_abstime_t *when)</h3>

 Restart an existing put. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued but not called back will be resent once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in get events will receive a put callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the put. 
 <i>url</i> The URL of the transfer. This may be different than the original put's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. If the put is restarted with a different URL, the plugin must re-send any data which has already been acknowledged by it's callback. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original put's attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent. 
 <i>restart_marker</i> Plugin-provided restart marker for resuming at a non-default restart point. This may be used to implement a persistent restart across process invocations. The default behavior if this is NULL is to use any restart information which has been received by the ftp client library while processing this operation when restarted. 
 <i>when</i> Absolute time for when to restart the put. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_recursive_list (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing recursive list. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list. 
 <i>url</i> The destination URL of the transfer. This may be different than the original list's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list's attribute set. 
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_rmdir (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing rmdir. 

 This function will cause the currently executing operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in rmdir events will receive a rmdir callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the rmdir. 
 <i>url</i> The destination URL of the transfer. This may be different than the original rmdir's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original rmdir's attribute set. 
 <i>when</i> Absolute time for when to restart the rmdir. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_size (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart a size check operation. 

 This function will cause the currently executing size check operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in size operations will receive a size callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the operation. 
 <i>url</i> The source URL of the size check. This may be different than the original operations URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new operation. This may be a modified version of the original operations's attribute set. 
 <i>when</i> Absolute time for when to restart the size check. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_stat (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing STAT. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list. 
 <i>url</i> The destination URL of the transfer. This may be different than the original list's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list's attribute set. 
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_symlink (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const char *link_url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing symlink. 

 This function will cause the currently executing symlink operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in chgrp events will receive a chgrp callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chgrp. 
 <i>url</i> The destination URL of the transfer. This may be different than the original symlink's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>link_url</i> The URL to symbolically link the file to. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original symlink's attribute set. 
 <i>when</i> Absolute time for when to restart the symlink. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_third_party_transfer (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, const <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, const <b>globus_ftp_client_operationattr_t</b> *dest_attr, <b>globus_ftp_client_restart_marker_t</b> *restart_marker, const globus_abstime_t *when)</h3>

 Restart an existing third-party transfer. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URLs and attributes. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in third-party transfer events will receive a transfer callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer. 
 <i>source_url</i> The source URL of the transfer. This may be different than the original URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL 
 <i>source_attr</i> The attributes to use for the new transfer. This may be a modified version of the original transfer's attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent. 
 <i>dest_url</i> The destination URL of the transfer. This may be different than the original destination URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>dest_attr</i> The attributes to use for the new transfer. This may be a modified version of the original transfer's attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent. 
 <i>restart_marker</i> Plugin-provided restart marker for resuming at a non-default restart point. This may be used to implement a persistent restart across process invocations. The default behavior if this is NULL is to use any restart information which has been received by the ftp client library while processing this operation when restarted. 
 <i>when</i> Absolute time for when to restart the transfer. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_utime (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const struct tm *utime_time, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing utime. 

 This function will cause the currently executing utime operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in utime events will receive a utime callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chgrp. 
 <i>url</i> The destination URL of the transfer. This may be different than the original utime's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>utime_time</i> The time value to change the file to. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original utime's attribute set. 
 <i>when</i> Absolute time for when to restart the utime. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h3>globus_result_t globus_ftp_client_plugin_restart_verbose_list (<b>globus_ftp_client_handle_t</b> *handle, const char *url, const <b>globus_ftp_client_operationattr_t</b> *attr, const globus_abstime_t *when)</h3>

 Restart an existing verbose list. 

 This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. 

 The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list. 
 <i>url</i> The destination URL of the transfer. This may be different than the original list's URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. 
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list's attribute set. 
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <b>when</b>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
 

 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_ftp_client from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbBS">Enumeration Type Documentation</a>
<dd>


<dt><a HREF="#lbBU">Function Documentation</a>
<dd>


<dt><a HREF="#lbCU">Author</a>
<dd></dl>
