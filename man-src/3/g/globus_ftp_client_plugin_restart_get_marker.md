---
title: "globus_ftp_client_plugin_restart_get_marker(3)"
name: "globus_ftp_client_plugin_restart_get_marker"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_plugin_restart_get_marker/"
description: "Plugins –"
---

<h2 class="name">NAME</h2>
<p> Plugins &#8211; </p>
<p> Plugin API.</p>
<h3>Modules</h3>
<p> <code>Debugging Plugin</code> </p>
<p> <code>Performance Marker Plugin</code> </p>
<p> <code>Restart Marker Plugin</code> </p>
<p> <code>Restart Plugin</code> </p>
<p> <code>Netlogger Throughput Plugin</code> </p>
<p> <code>Throughput Performance Plugin</code> </p>
<h3>Data Structures</h3>
<p> struct <code>globus_i_ftp_client_plugin_t</code><br />
 <i>FTP Client Plugin.</i> </p>
<p> Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. &quot;</p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 <code>globus_i_ftp_client_plugin_t</code> * <code>globus_ftp_client_plugin_t</code>&quot;<br />
 <i>FTP Client plugin</i> </p>
<p> An FTP Client plugin is used to add restart, monitoring, and performance tuning operations to the FTP Client library, without modifying the base API. Multiple plugins may be associated with a globus_ftp_client_handle_t. &quot;<br />
 typedef<br />
 <code>globus_ftp_client_plugin_t</code> *(* <code>globus_ftp_client_plugin_copy_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin_template, void *plugin_specific)&quot; </p>
<p> typedef void(* <code>globus_ftp_client_plugin_destroy_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_connect_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_authenticate_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const globus_ftp_control_auth_info_t *auth_info) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_chmod_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, int mode, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_chgrp_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *group, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_utime_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const struct tm *utime_time, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_symlink_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *utime_time, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_cksm_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_off_t offset, globus_off_t length, const char *algorithm, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_delete_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_feat_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_mkdir_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_rmdir_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_list_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_verbose_list_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_machine_list_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_recursive_list_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_mlst_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_stat_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_move_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_get_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_put_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_third_party_transfer_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *dest_attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_modification_time_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_size_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_abort_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_read_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const globus_byte_t *buffer, globus_size_t buffer_length) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_write_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const globus_byte_t *buffer, globus_size_t buffer_length, globus_off_t offset, globus_bool_t eof) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_data_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, const globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_command_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *command) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_response_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_object_t *error, const globus_ftp_control_response_t *ftp_response) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_fault_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_object_t *error) </p>
<p> typedef void(* <code>globus_ftp_client_plugin_complete_t</code> )(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle) </p>
<p> typedef struct<br />
 <code>globus_i_ftp_client_plugin_t</code> <code>globus_i_ftp_client_plugin_t</code>&quot;<br />
 <i>FTP Client Plugin.</i> </p>
<p> Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. &quot;</p>
<h3>Enumerations</h3>
<p> enum <code>globus_ftp_client_plugin_command_mask_t</code> { , <code>GLOBUS_FTP_CLIENT_CMD_MASK_CONTROL_ESTABLISHMENT</code> = 1&lt;&lt;0, <code>GLOBUS_FTP_CLIENT_CMD_MASK_DATA_ESTABLISHMENT</code> = 1&lt;&lt;1, <code>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_PARAMETERS</code> = 1&lt;&lt;2, <code>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_MODIFIERS</code> = 1&lt;&lt;3, <code>GLOBUS_FTP_CLIENT_CMD_MASK_FILE_ACTIONS</code> = 1&lt;&lt;4, <code>GLOBUS_FTP_CLIENT_CMD_MASK_INFORMATION</code> = 1&lt;&lt;5, <code>GLOBUS_FTP_CLIENT_CMD_MASK_MISC</code> = 1&lt;&lt;6, <code>GLOBUS_FTP_CLIENT_CMD_MASK_BUFFER</code> = 1&lt;&lt;7, <code>GLOBUS_FTP_CLIENT_CMD_MASK_ALL</code> = 0x7fffffff } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_list</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_verbose_list</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_machine_list</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_recursive_list</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_mlst</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_stat</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_chmod</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, int mode, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_chgrp</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *group, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_utime</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const struct tm *utime_time, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_symlink</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *link_url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_cksm</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_off_t offset, globus_off_t length, const char *algorithm, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_delete</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_feat</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_mkdir</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_rmdir</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_move</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_get</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart_marker, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_put</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart_marker, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_third_party_transfer</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *dest_attr, <code>globus_ftp_client_restart_marker_t</code> *restart_marker, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_size</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_modification_time</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_restart_get_marker</code> (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_restart_marker_t</code> *marker) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_abort</code> (<code>globus_ftp_client_handle_t</code> *handle) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_add_data_channels</code> (<code>globus_ftp_client_handle_t</code> *handle, unsigned int num_channels, unsigned int stripe) </p>
<p> globus_result_t <code>globus_ftp_client_plugin_remove_data_channels</code> (<code>globus_ftp_client_handle_t</code> *handle, unsigned int num_channels, unsigned int stripe) </p>
<h2>Detailed Description</h2>
<p> Plugin API. </p>
<p> A plugin is a way to implement application-independent reliability and performance tuning behavior. Plugins are written using the API described in this document. </p>
<p> A plugin is created by defining a globus_ftp_client_plugin_t which contains the function pointers and plugin-specific data needed for the plugin&#8217;s operation. It is recommended that a plugin define a a globus_module_descriptor_t and plugin initialization functions, to ensure that the plugin is properly initialized. </p>
<p> The functions pointed to in a plugin are called when significant events in the life of an FTP Client operation occur. Note that plugins will only be called when the plugin has the function pointer for both the operation (get, put, list, etc), and the event (connect, authenticate, command, etc), are defined. The command and response functions are filtered based on the command_mask defined in the plugin structure. </p>
<p> Every plugin must define <code>copy </code> and <code>destroy </code> functions. The copy function is called when the plugin is added to an attribute set or a handle is initialized with an attribute set containing the plugin. The destroy function is called when the handle or attribute set is destroyed.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_client_plugin_abort_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle)</h3>
<p> Plugin abort notification callback. </p>
<p> This callback is used to notify a plugin that an abort is being requested on a client handle. This notification happens both when the user aborts a request and when a plugin aborts the currently active request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.</dl>
<h3>typedef void(* globus_ftp_client_plugin_authenticate_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const globus_ftp_control_auth_info_t *auth_info)</h3>
<p> Plugin authentication notification callback. </p>
<p> This callback is used to notify a plugin that an authentication handshake is being done for this client handle. This notification can occur when a new request is made or when a hard restart is done by a plugin. </p>
<p> If a response_callback is defined by a plugin, then that will be once the authentication has completed (successfully or unsuccessfully). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the connection.<br />
 <i>url</i> The URL of the server to connect to.<br />
 <i>auth_info</i> Authentication and authorization info being used to authenticate with the FTP or GridFTP server.</dl>
<h3>typedef void(* globus_ftp_client_plugin_chgrp_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *group, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin chgrp notification callback. </p>
<p> This callback is used to notify a plugin that a chgrp is being requested on a client handle. This notification happens both when the user requests a chgrp, and when a plugin restarts the currently active chgrp request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the chgrp will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the delete operation.<br />
 <i>url</i> The url to chgrp.<br />
 <i>group</i> The group name or ID to change to.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_chmod_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, int mode, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin chmod notification callback. </p>
<p> This callback is used to notify a plugin that a chmod is being requested on a client handle. This notification happens both when the user requests a chmod, and when a plugin restarts the currently active chmod request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the chmod will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the delete operation.<br />
 <i>url</i> The url to chmod.<br />
 <i>mode</i> The file mode to be applied.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_cksm_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_off_t offset, globus_off_t length, const char *algorithm, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin cksm notification callback. </p>
<p> This callback is used to notify a plugin that a cksm is being requested on a client handle. This notification happens both when the user requests a cksm, and when a plugin restarts the currently active cksm request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the cksm will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the delete operation.<br />
 <i>url</i> The url to cksm.<br />
 <i>offset</i> File offset to start calculating checksum.<br />
 <i>length</i> Length of data to read from the starting offset. Use -1 to read the entire file.<br />
 <i>algorithm</i> A pointer to a string to be filled with the checksum of the file. On error the value pointed to by it is undefined.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_command_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *command)</h3>
<p> Command callback. </p>
<p> This callback is used to notify a plugin that a FTP control command is being sent. The client library will only call this function for response callbacks associated with a command which is in the plugin&#8217;s command mask, and associated with one of the other ftp operations with a defined callback in the plugin. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.<br />
 <i>url</i> The URL which this command is being sent to.<br />
 <i>command</i> A string containing the command which is being sent to the server (TYPE I, for example).</dl>
<h3>typedef void(* globus_ftp_client_plugin_complete_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle)</h3>
<p> Completion notification callback. </p>
<p> This callback is used to notify a plugin that an operation previously begun has completed. The plugin may not call any other plugin operation on this handle after this has occurred. This is the final callback for the plugin while processing the operation. The plugin may free any internal state associated with the operation at this point. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the operation.</dl>
<h3>typedef void(* globus_ftp_client_plugin_connect_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url)</h3>
<p> Plugin connection begin function. </p>
<p> This callback is used to notify a plugin that connection establishment is being done for this client handle. This notification can occur when a new request is made or when a restart is done by a plugin. </p>
<p> If a response_callback is defined by a plugin, then that will be once the connection establishment has completed (successfully or unsuccessfully). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the connection.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function will not be called for a get, put, or third-party transfer operation when a cached connection is used.</dl>
<h3>typedef <code>globus_ftp_client_plugin_t</code>*(* globus_ftp_client_plugin_copy_t)(<code>globus_ftp_client_plugin_t</code> *plugin_template, void *plugin_specific)</h3>
<p> Plugin copy function. </p>
<p> This function is used to create a new copy or reference count a plugin. This function is called by the FTP Client library when a plugin is added to a handle attribute set, or when a handle is initialized with an attribute which contains the plugin. </p>
<p> A plugin may not call any of the plugin API functions from it&#8217;s instantiate method. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin_template</i> A plugin previously initialized by a call to the plugin-specific initialization function. by the user.<br />
 <i>plugin_specific</i> Plugin-specific data.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A pointer to a plugin. This plugin copy must remain valid until the copy&#8217;s <code>destroy</code> function is called on the copy.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_plugin_destroy_t</code></dl>
<h3>typedef void(* globus_ftp_client_plugin_data_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, const globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof)</h3>
<p> Plugin data callback handler. </p>
<p> This callback is used to notify a plugin that a read or write operation previously registered has completed. The buffer pointer will match that of a previous plugin read or write registration callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.<br />
 <i>buffer</i> The buffer which was successfully transferred over the network.<br />
 <i>length</i> The amount of data to read or written.<br />
 <i>offset</i> The offset into the file where this data buffer belongs.<br />
 <i>eof</i> This value is set to GLOBUS_TRUE if end-of-file is being processed for this transfer.</dl>
<h3>typedef void(* globus_ftp_client_plugin_delete_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin delete notification callback. </p>
<p> This callback is used to notify a plugin that a delete is being requested on a client handle. This notification happens both when the user requests a delete, and when a plugin restarts the currently active delete request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the delete will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the delete operation.<br />
 <i>url</i> The url to be deleted.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current delete operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_destroy_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific)</h3>
<p> Plugin destroy function. </p>
<p> This function is used to free or unreference a copy of a plugin which was allocated by calling the instantiate function from the plugin. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin, created by the create function, which is to be destroyed.<br />
 <i>plugin_specific</i> Plugin-specific data.</dl>
<h3>typedef void(* globus_ftp_client_plugin_fault_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_object_t *error)</h3>
<p> Fault notification callback. </p>
<p> This callback is used to notify a plugin that a fault occurred while processing the request. The fault may be internally generated, or come from a call to another library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.<br />
 <i>url</i> The url being processed when the fault ocurred.<br />
 <i>error</i> An error object describing the fault.</dl>
<h3>typedef void(* globus_ftp_client_plugin_feat_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin feat notification callback. </p>
<p> This callback is used to notify a plugin that a feat is being requested on a client handle. This notification happens both when the user requests a feat, and when a plugin restarts the currently active feat request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the feat will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the feat operation.<br />
 <i>url</i> The url to be feat&#8217;d.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current feat operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_get_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin get notification callback. </p>
<p> This callback is used to notify a plugin that a get is being requested on a client handle. This notification happens both when the user requests a get, and when a plugin restarts the currently active get request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the get will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the get operation.<br />
 <i>url</i> The url of the get operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current get transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_list_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin list notification callback. </p>
<p> This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_machine_list_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin machine list notification callback. </p>
<p> This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_mkdir_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin mkdir notification callback. </p>
<p> This callback is used to notify a plugin that a mkdir is being requested on a client handle. This notification happens both when the user requests a mkdir, and when a plugin restarts the currently active mkdir request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the mkdir will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the mkdir operation.<br />
 <i>url</i> The url of the directory to create.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current mkdir operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_mlst_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin mlst notification callback. </p>
<p> This callback is used to notify a plugin that a mlst is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_modification_time_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin modification time notification callback. </p>
<p> This callback is used to notify a plugin that a modification time check is being requested on a client handle. This notification happens both when the user requests the modification time of a file, and when a plugin restarts the currently active request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the modification time request will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_move_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin move notification callback. </p>
<p> This callback is used to notify a plugin that a move is being requested on a client handle. This notification happens both when the user requests a move, and when a plugin restarts the currently active move request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the move will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the move operation.<br />
 <i>source_url</i> The source url of the move operation.<br />
 <i>dest_url</i> The destination url of the move operation.<br />
 <i>attr</i> The attributes to be used during this move.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current move transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_put_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin put notification callback. </p>
<p> This callback is used to notify a plugin that a put is being requested on a client handle. This notification happens both when the user requests a put, and when a plugin restarts the currently active put request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the put will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the put operation.<br />
 <i>url</i> The url of the put operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current put transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_read_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const globus_byte_t *buffer, globus_size_t buffer_length)</h3>
<p> Plugin read registration callback. </p>
<p> This callback is used to notify a plugin that the client API has registered a buffer with the FTP control API for reading when processing a get. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.<br />
 <i>buffer</i> The data buffer to read into.<br />
 <i>buffer_length</i> The maximum amount of data to read into the buffer.</dl>
<h3>typedef void(* globus_ftp_client_plugin_recursive_list_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin recursive list notification callback. </p>
<p> This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_response_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_object_t *error, const globus_ftp_control_response_t *ftp_response)</h3>
<p> Response callback. </p>
<p> This callback is used to notify a plugin that a FTP control response has occurred on a control connection. FTP response callbacks will come back to the user in the order which the commands were executed. The client library will only call this function for response callbacks associated with a command which is in the plugin&#8217;s command mask, or associated with one of the other ftp operations with a defined callback in the plugin. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.<br />
 <i>url</i> The URL which this response came from.<br />
 <i>error</i> An error which occurred while processing this command/response pair.<br />
 <i>ftp_response</i> The response structure from the ftp control library.</dl>
<h3>typedef void(* globus_ftp_client_plugin_rmdir_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin rmdir notification callback. </p>
<p> This callback is used to notify a plugin that a rmdir is being requested on a client handle. This notification happens both when the user requests a rmdir, and when a plugin restarts the currently active rmdir request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the rmdir will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the rmdir operation.<br />
 <i>url</i> The url of the rmdir operation.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current rmdir operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_size_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin size notification callback. </p>
<p> This callback is used to notify a plugin that a size check is being requested on a client handle. This notification happens both when the user requests the size of a file, and when a plugin restarts the currently active request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the size request will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_stat_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin stat notification callback. </p>
<p> This callback is used to notify a plugin that a stat is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_symlink_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *utime_time, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin symlink notification callback. </p>
<p> This callback is used to notify a plugin that a symlink is being requested on a client handle. This notification happens both when the user requests a symlink, and when a plugin restarts the currently active symlink request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the symlink will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the symlink operation.<br />
 <i>url</i> The url of the new link.<br />
 <i>link_url</i> The url to which the new link should point.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current utime operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef struct <code>globus_i_ftp_client_plugin_t</code>* <code>globus_ftp_client_plugin_t</code></h3>
<p> FTP Client plugin </p>
<p> An FTP Client plugin is used to add restart, monitoring, and performance tuning operations to the FTP Client library, without modifying the base API. Multiple plugins may be associated with a globus_ftp_client_handle_t. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_handle_init()</code>, <code>globus_ftp_client_handle_destroy()</code>, <code>globus_ftp_client_handleattr_t</code>, <code>Debugging Plugin </code></dl>
<h3>typedef void(* globus_ftp_client_plugin_third_party_transfer_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *dest_attr, globus_bool_t restart)</h3>
<p> Plugin third-party transfer notification callback. </p>
<p> This callback is used to notify a plugin that a transfer is being requested on a client handle. This notification happens both when the user requests a transfer, and when a plugin restarts the currently active transfer request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the third-party transfer will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the transfer operation.<br />
 <i>source_url</i> The source url of the transfer operation.<br />
 <i>source_attr</i> The attributes to be used during this transfer on the source.<br />
 <i>dest_url</i> The destination url of the third-party transfer operation.<br />
 <i>dest_attr</i> The attributes to be used during this transfer on the destination.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current transfer transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_utime_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const struct tm *utime_time, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin utime notification callback. </p>
<p> This callback is used to notify a plugin that a utime is being requested on a client handle. This notification happens both when the user requests a utime, and when a plugin restarts the currently active utime request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the utime will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the utime operation.<br />
 <i>url</i> The url to utime.<br />
 <i>utime_time</i> The modification time to change the file to.<br />
 <i>attr</i> The attributes to be used during this operation.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current utime operation; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_verbose_list_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, globus_bool_t restart)</h3>
<p> Plugin verbose list notification callback. </p>
<p> This callback is used to notify a plugin that a list is being requested on a client handle. This notification happens both when the user requests a list, and when a plugin restarts the currently active list request. </p>
<p> If this function is not defined by the plugin, then no plugin callbacks associated with the list will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the list operation.<br />
 <i>url</i> The url of the list operation.<br />
 <i>attr</i> The attributes to be used during this transfer.<br />
 <i>restart</i> This value is set to GLOBUS_TRUE when this callback is caused by a plugin restarting the current list transfer; otherwise, this is set to GLOBUS_FALSE.</dl>
<h3>typedef void(* globus_ftp_client_plugin_write_t)(<code>globus_ftp_client_plugin_t</code> *plugin, void *plugin_specific, <code>globus_ftp_client_handle_t</code> *handle, const globus_byte_t *buffer, globus_size_t buffer_length, globus_off_t offset, globus_bool_t eof)</h3>
<p> Plugin write registration callback. </p>
<p> This callback is used to notify a plugin that the client API has registered a buffer with the FTP control API for writing when processing a put. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> The plugin which is being notified.<br />
 <i>plugin_specific</i> Plugin-specific data.<br />
 <i>handle</i> The handle associated with the request.<br />
 <i>buffer</i> The buffer which is being written.<br />
 <i>buffer_length</i> The amount of data in the buffer.<br />
 <i>offset</i> The offset within the file where the buffer is to be written.<br />
 <i>eof</i> This value is set to GLOBUS_TRUE if this is the last data buffer to be sent for this put request.</dl>
<h3>typedef struct <code>globus_i_ftp_client_plugin_t</code> <code>globus_i_ftp_client_plugin_t</code></h3>
<p> FTP Client Plugin. </p>
<p> Each plugin implementation should define a method for initializing one of these structures. Plugins may be implemented as either a static function table, or a specialized plugin with plugin-specific attributes. Each plugin function may be either GLOBUS_NULL, or a valid function pointer. If the function is GLOBUS_NULL, then the plugin will not be notified when the corresponding event happens.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_ftp_client_plugin_command_mask_t</code></h3>
<p> Command Mask. </p>
<p> This enumeration includes the types of commands which the plugin is interested in. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_CONTROL_ESTABLISHMENT </i></p>
<dd> connect, authenticate</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_DATA_ESTABLISHMENT </i></p>
<dd> PASV, PORT, SPOR, SPAS</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_PARAMETERS </i></p>
<dd> MODE, TYPE, STRU, OPTS RETR, DCAU</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_TRANSFER_MODIFIERS </i></p>
<dd> ALLO, REST</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_FILE_ACTIONS </i></p>
<dd> STOR, RETR, ESTO, ERET, APPE, LIST, NLST, MLSD, MLSR, GET, PUT</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_INFORMATION </i></p>
<dd> HELP, SITE HELP, FEAT, STAT, SYST, SIZE</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_MISC </i></p>
<dd> SITE, NOOP</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_BUFFER </i></p>
<dd> SBUF, ABUF</p>
<dt><i>GLOBUS_FTP_CLIENT_CMD_MASK_ALL </i></p>
<dd> All possible commands</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_plugin_abort (<code>globus_ftp_client_handle_t</code> *handle)</h3>
<p> Abort a transfer operation. </p>
<p> This function will cause the currently executing transfer operation to be aborted. When this happens, all plugins will be notified by their abort callbacks. Once those are processed, the complete callback will be called for all plugins, and then for the user&#8217;s callback. </p>
<p> The complete callback will indicate that the transfer did not complete successfully. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer.</dl>
<h3>globus_result_t globus_ftp_client_plugin_add_data_channels (<code>globus_ftp_client_handle_t</code> *handle, unsigned intnum_channels, unsigned intstripe)</h3>
<p> Add data channels to an existing put transfer. </p>
<p> This function will cause the currently executing transfer operation to have additional data channels acquired if the attribute set allows it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer.<br />
 <i>num_channels</i> The number of channels to add to the transfer.<br />
 <i>stripe</i> The stripe number to have the channels added to.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Do the plugins need to be notified when this happens?</dl>
<h3>globus_result_t globus_ftp_client_plugin_remove_data_channels (<code>globus_ftp_client_handle_t</code> *handle, unsigned intnum_channels, unsigned intstripe)</h3>
<p> Remove data channels from an existing put transfer. </p>
<p> This function will cause the currently executing transfer operation to have data channels removed, if the attribute set allows it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer.<br />
 <i>num_channels</i> The number of channels to remove from the transfer.<br />
 <i>stripe</i> The stripe number to have the channels removed from.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Do the plugins need to be notified when this happens?</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_chgrp (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *group, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing chgrp. </p>
<p> This function will cause the currently executing chgrp operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in chgrp events will receive a chgrp callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chgrp.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original chgrp&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>group</i> The group name or ID to change the file to.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original chgrp&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the chgrp. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_chmod (<code>globus_ftp_client_handle_t</code> *handle, const char *url, intmode, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing chmod. </p>
<p> This function will cause the currently executing chmod operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in chmod events will receive a chmod callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chmod.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original chmod&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>mode</i> The file mode that will be applied. Must be an octal number repre- senting the bit pattern for the new permissions.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original chmod&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the chmod. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_cksm (<code>globus_ftp_client_handle_t</code> *handle, const char *url, globus_off_toffset, globus_off_tlength, const char *algorithm, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing cksm. </p>
<p> This function will cause the currently executing cksm operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in cksm events will receive a cksm callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the cksm.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original cksm&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>offset</i> File offset to start calculating checksum.<br />
 <i>length</i> Length of data to read from the starting offset. Use -1 to read the entire file.<br />
 <i>algorithm</i> A pointer to a string to be filled with the checksum of the file. On error the value pointed to by it is undefined.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original cksm&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the cksm. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_delete (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing delete. </p>
<p> This function will cause the currently executing delete operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in delete events will receive a delete callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the delete.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original delete&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original delete&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the delete. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_feat (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing feat. </p>
<p> This function will cause the currently executing feat operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in feat events will receive a feat callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the feat.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original feat&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original feat&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the feat. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_get (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart_marker, const globus_abstime_t *when)</h3>
<p> Restart an existing get. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in get events will receive a get callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the get.<br />
 <i>url</i> The source URL of the transfer. This may be different than the original get&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original get&#8217;s attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent.<br />
 <i>restart_marker</i> Plugin-provided restart marker for resuming at a non-default restart point. This may be used to implement a persistent restart across process invocations. The default behavior if this is NULL is to use any restart information which has been received by the ftp client library while processing this operation when restarted.<br />
 <i>when</i> Absolute time for when to restart the get. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_get_marker (<code>globus_ftp_client_handle_t</code> *handle, <code>globus_ftp_client_restart_marker_t</code> *marker)</h3>
<p> Get restart marker </p>
<p> This function will allow this user to get the restart marker associated with a restarted file transfer. This function may only be called within the get, put, or third party transfer callback in which the &#8216;restart&#8217; argument is GLOBUS_TRUE </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer.<br />
 <i>marker</i> Pointer to an uninitialized restart marker type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error on NULL handle or marker</p>
<dt>&bull;</p>
<dd> Error on invalid use of function</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS (marker will be populated)</dl>
</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_list (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing list. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original list&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_machine_list (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing machine list. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original list&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_mkdir (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing mkdir. </p>
<p> This function will cause the currently executing operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in mkdir events will receive a mkdir callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the mkdir.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original mkdir&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original mkdir&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the mkdir. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_mlst (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing MLST. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original list&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_modification_time (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart a modification time check operation. </p>
<p> This function will cause the currently executing modification time check operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in modification time operations will receive a modification time callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the operation.<br />
 <i>url</i> The source URL of the modification time check. This may be different than the original operations URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new operation. This may be a modified version of the original operations&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the modification time check. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_move (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing move. </p>
<p> This function will cause the currently executing move operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially new URLs and attributes. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in get events will receive a move callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the move.<br />
 <i>source_url</i> The source URL of the move. This may be different than the original get&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>dest_url</i> The destination URL of the move. This may be different than the original get&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. Note that only the path component of this URL is used.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original move&#8217;s attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent.<br />
 <i>when</i> Absolute time for when to restart the move. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_put (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart_marker, const globus_abstime_t *when)</h3>
<p> Restart an existing put. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued but not called back will be resent once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in get events will receive a put callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the put.<br />
 <i>url</i> The URL of the transfer. This may be different than the original put&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL. If the put is restarted with a different URL, the plugin must re-send any data which has already been acknowledged by it&#8217;s callback.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original put&#8217;s attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent.<br />
 <i>restart_marker</i> Plugin-provided restart marker for resuming at a non-default restart point. This may be used to implement a persistent restart across process invocations. The default behavior if this is NULL is to use any restart information which has been received by the ftp client library while processing this operation when restarted.<br />
 <i>when</i> Absolute time for when to restart the put. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_recursive_list (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing recursive list. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original list&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_rmdir (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing rmdir. </p>
<p> This function will cause the currently executing operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in rmdir events will receive a rmdir callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the rmdir.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original rmdir&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original rmdir&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the rmdir. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_size (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart a size check operation. </p>
<p> This function will cause the currently executing size check operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in size operations will receive a size callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the operation.<br />
 <i>url</i> The source URL of the size check. This may be different than the original operations URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new operation. This may be a modified version of the original operations&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the size check. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_stat (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing STAT. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original list&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_symlink (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const char *link_url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing symlink. </p>
<p> This function will cause the currently executing symlink operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in chgrp events will receive a chgrp callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chgrp.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original symlink&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>link_url</i> The URL to symbolically link the file to.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original symlink&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the symlink. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_third_party_transfer (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, const <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, const <code>globus_ftp_client_operationattr_t</code> *dest_attr, <code>globus_ftp_client_restart_marker_t</code> *restart_marker, const globus_abstime_t *when)</h3>
<p> Restart an existing third-party transfer. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URLs and attributes. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in third-party transfer events will receive a transfer callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the transfer.<br />
 <i>source_url</i> The source URL of the transfer. This may be different than the original URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL<br />
 <i>source_attr</i> The attributes to use for the new transfer. This may be a modified version of the original transfer&#8217;s attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent.<br />
 <i>dest_url</i> The destination URL of the transfer. This may be different than the original destination URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>dest_attr</i> The attributes to use for the new transfer. This may be a modified version of the original transfer&#8217;s attribute set. This may be useful when the plugin wishes to send restart markers to the FTP server to prevent re-sending the data which has already been sent.<br />
 <i>restart_marker</i> Plugin-provided restart marker for resuming at a non-default restart point. This may be used to implement a persistent restart across process invocations. The default behavior if this is NULL is to use any restart information which has been received by the ftp client library while processing this operation when restarted.<br />
 <i>when</i> Absolute time for when to restart the transfer. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_utime (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const struct tm *utime_time, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing utime. </p>
<p> This function will cause the currently executing utime operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in utime events will receive a utime callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the chgrp.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original utime&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>utime_time</i> The time value to change the file to.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original utime&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the utime. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h3>globus_result_t globus_ftp_client_plugin_restart_verbose_list (<code>globus_ftp_client_handle_t</code> *handle, const char *url, const <code>globus_ftp_client_operationattr_t</code> *attr, const globus_abstime_t *when)</h3>
<p> Restart an existing verbose list. </p>
<p> This function will cause the currently executing transfer operation to be restarted. When a restart happens, the operation will be silently aborted, and then restarted with potentially a new URL and attributes. Any data buffers which are currently queued will be cleared and reused once the connection is re-established. </p>
<p> The user will not receive any notification that a restart has happened. Each plugin which is interested in list events will receive a list callback with the restart boolean set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle which is associated with the list.<br />
 <i>url</i> The destination URL of the transfer. This may be different than the original list&#8217;s URL, if the plugin decides to redirect to another FTP server due to performance or reliability problems with the original URL.<br />
 <i>attr</i> The attributes to use for the new transfer. This may be a modified version of the original list&#8217;s attribute set.<br />
 <i>when</i> Absolute time for when to restart the list. The current control and data connections will be stopped immediately. If this completes before <code>when</code>, then the restart will be delayed until that time. Otherwise, it will be immediately restarted.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBS">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbBU">Function Documentation</a></p>
<dd>
<dt><a href="#lbCU">Author</a></p>
<dd></dl>
