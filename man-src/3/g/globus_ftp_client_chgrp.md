---
title: "globus_ftp_client_chgrp(3)"
name: "globus_ftp_client_chgrp"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_chgrp/"
---

<h2 class="name">NAME</h2>
 

 FTP Operations - 

<h3>Typedefs</h3>

 

 
 typedef void(* <b>globus_ftp_client_complete_callback_t</b> )(void *user_arg, <b>globus_ftp_client_handle_t</b> *handle, globus_object_t *error) 
 
 typedef struct 
 <b>globus_i_ftp_client_features_s</b> * <b>globus_ftp_client_features_t</b>&quot; 
 <i>Feature Handle</i> 

 Handle used to associate state with feature operations. &quot;

<h3>Enumerations</h3>

 

 
 enum <b>globus_ftp_client_tristate_t</b> 
 
 enum <b>globus_ftp_client_probed_feature_t</b> 

<h3>Functions</h3>

 

 
 globus_result_t <b>globus_ftp_client_machine_list</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_recursive_list</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>File or Directory Existence</h3>

 

 
 globus_result_t <b>globus_ftp_client_exists</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Features</h3>

 

 
 globus_result_t <b>globus_ftp_client_features_init</b> (<b>globus_ftp_client_features_t</b> *u_features) 
 
 globus_result_t <b>globus_ftp_client_features_destroy</b> (<b>globus_ftp_client_features_t</b> *u_features) 
 
 globus_result_t <b>globus_ftp_client_feat</b> (<b>globus_ftp_client_handle_t</b> *u_handle, char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_features_t</b> *u_features, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_is_feature_supported</b> (const <b>globus_ftp_client_features_t</b> *u_features, <b>globus_ftp_client_tristate_t</b> *answer, <b>globus_ftp_client_probed_feature_t</b> feature) 

<h3>Make Directory</h3>

 

 
 globus_result_t <b>globus_ftp_client_mkdir</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Remove Directory</h3>

 

 
 globus_result_t <b>globus_ftp_client_rmdir</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Change Working Directory</h3>

 

 
 globus_result_t <b>globus_ftp_client_cwd</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_byte_t **cwd_buffer, globus_size_t *cwd_buffer_length, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Delete</h3>

 

 
 globus_result_t <b>globus_ftp_client_delete</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>List</h3>

 

 
 globus_result_t <b>globus_ftp_client_list</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_verbose_list</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>STAT</h3>

 

 
 globus_result_t <b>globus_ftp_client_stat</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_byte_t **stat_buffer, globus_size_t *stat_buffer_length, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>MLST</h3>

 

 
 globus_result_t <b>globus_ftp_client_mlst</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_byte_t **mlst_buffer, globus_size_t *mlst_buffer_length, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Move</h3>

 

 
 globus_result_t <b>globus_ftp_client_move</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *source_url, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>chmod</h3>

 

 
 globus_result_t <b>globus_ftp_client_chmod</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, int mode, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>chgrp</h3>

 

 
 globus_result_t <b>globus_ftp_client_chgrp</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, const char *group, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>utime</h3>

 

 
 globus_result_t <b>globus_ftp_client_utime</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, const struct tm *utime_time, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>symlink</h3>

 

 
 globus_result_t <b>globus_ftp_client_symlink</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *source_url, const char *link_url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Get</h3>

 

 
 globus_result_t <b>globus_ftp_client_get</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_partial_get</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, globus_off_t partial_offset, globus_off_t partial_end_offset, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_extended_get</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, const char *eret_alg_str, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Put</h3>

 

 
 globus_result_t <b>globus_ftp_client_put</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_partial_put</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, globus_off_t partial_offset, globus_off_t partial_end_offset, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_extended_put</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, const char *esto_alg_str, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>3rd Party Transfer</h3>

 

 
 globus_result_t <b>globus_ftp_client_third_party_transfer</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *dest_attr, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_partial_third_party_transfer</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *dest_attr, <b>globus_ftp_client_restart_marker_t</b> *restart, globus_off_t partial_offset, globus_off_t partial_end_offset, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_extended_third_party_transfer</b> (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *eret_alg_str, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *dest_attr, const char *esto_alg_str, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Modification Time</h3>

 

 
 globus_result_t <b>globus_ftp_client_modification_time</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_abstime_t *modification_time, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Size</h3>

 

 
 globus_result_t <b>globus_ftp_client_size</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_off_t *size, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Cksm</h3>

 

 
 globus_result_t <b>globus_ftp_client_cksm</b> (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, char *cksm, globus_off_t offset, globus_off_t length, const char *algorithm, <b>globus_ftp_client_complete_callback_t</b> complete_callback, void *callback_arg) 

<h3>Abort</h3>

 

 
 globus_result_t <b>globus_ftp_client_abort</b> (<b>globus_ftp_client_handle_t</b> *u_handle) 

<h2>Detailed Description</h2>

 

 Initiate an FTP operation. 

 This module contains the API functions for a user to request a get, put, third-party transfer, or other FTP file operation.

<h2>Typedef Documentation</h2>

 

<h3>typedef void(* globus_ftp_client_complete_callback_t)(void *user_arg, <b>globus_ftp_client_handle_t</b> *handle, globus_object_t *error)</h3>

 Operation complete callback. 

 Every FTP Client operation (get, put, transfer, mkdir, etc) is asynchronous. A callback of this type is passed to each of the operation function calls to let the user know when the operation is complete. The completion callback is called only once per operation, after all other callbacks for the operation have returned. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>user_arg</i> The user_arg parameter passed to the operation. 
 <i>handle</i> The handle on which the operation was done. 
 <i>error</i> A Globus error object indicating any problem which occurred, or GLOBUS_SUCCESS, if the operation completed successfully.</dl>
 

 

<h3>typedef struct <b>globus_i_ftp_client_features_s</b>* <b>globus_ftp_client_features_t</b></h3>

 

 

 Feature Handle 

 Handle used to associate state with feature operations. 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_feat</b>, <b>globus_ftp_client_features_init</b>, <b>globus_ftp_client_features_destroy</b></dl>
 

 

<h2>Enumeration Type Documentation</h2>

 

<h3>enum <b>globus_ftp_client_probed_feature_t</b></h3>

 Types of features

<h3>enum <b>globus_ftp_client_tristate_t</b></h3>

 Types for feature existence 

 FALSE and TRUE are known to be fact that a feature does or does not exist MAYBE means that the feature may exist

<h2>Function Documentation</h2>

 

<h3>globus_result_t globus_ftp_client_abort (<b>globus_ftp_client_handle_t</b> *u_handle)</h3>

 Abort the operation currently in progress. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> Handle which to abort.</dl>
 

 

<h3>globus_result_t globus_ftp_client_chgrp (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, const char *group, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Change group membership on a file. 

 This function changes file group membership 

 When the response to the group change request has been received the complete_callback will be invoked with the result of the operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the change operation. 
 <i>url</i> The URL of the file to modify group membership. 
 <i>group</i> The group name or numeric identifier for the group that the file should become a member of. 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the change is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_chmod (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, intmode, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Change permissions on a file. 

 This function changes file permissions 

 When the response to the move request has been received the complete_callback will be invoked with the result of the operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the move operation. 
 <i>url</i> The URL of the file to modify permissions. 
 <i>mode</i> The integer file mode to change to. Be sure that the integer is in the proper base, i.e. 0777 (octal) vs 777 (decimal). 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the move is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_cksm (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, char *cksm, globus_off_toffset, globus_off_tlength, const char *algorithm, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file's checksum from an FTP server. 

 This function requests the checksum of a file from an FTP server. 

 When the request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the checksum will be stored in the char * buffer provided in the 'checksum' parameter to this function. The buffer must be large enough to hold the expected checksum result. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>cksm</i> A pointer to a buffer to be filled with the checksum of the file. On error the buffer contents are undefined. 
 <i>offset</i> File offset to start calculating checksum. 
 <i>length</i> Length of data to read from the starting offset. Use -1 to read the entire file. 
 <i>algorithm</i> A pointer to a string to specifying the desired algorithm Currently, GridFTP servers only support the MD5 algorithm. 
 <i>complete_callback</i> Callback to be invoked once the checksum is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> size is GLOBUS_NULL
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_cwd (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_byte_t **cwd_buffer, globus_size_t *cwd_buffer_length, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Make a directory on an FTP server. 

 This function starts a cwd operation on a FTP server. 

 When the response to the cwd request has been received the complete_callback will be invoked with the result of the cwd operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the cwd operation. 
 <i>url</i> The URL for the directory to cd into. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this operation. 
 <i>cwd_buffer</i> A pointer to a globus_byte_t * to be allocated and filled with the directory name returned by the CWD, if it succeeds. Otherwise, the value pointed to by it is undefined. It is up the user to free this memory. 
 <i>cwd_buffer_length</i> A pointer to a globus_size_t to be filled with the length of the data in cwd_buffer. 
 <i>complete_callback</i> Callback to be invoked once the cwd is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> u_handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> cwd_buffer is GLOBUS_NULL
<dt>&bull;
<dd> cwd_buffer_length is GLOBUS_NULL
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_delete (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Delete a file on an FTP server. 

 This function starts a delete operation on a FTP server. Note that this functions will only delete files, not directories. 

 When the response to the delete request has been received the complete_callback will be invoked with the result of the delete operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the delete operation. 
 <i>url</i> The URL for the file to delete. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>complete_callback</i> Callback to be invoked once the delete is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> u_handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_exists (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Check for the existence of a file or directory on an FTP server. 

 This function attempts to determine whether the specified URL points to a valid file or directory. The <i>complete_callback</i> will be invoked with the result of the existence check passed as a globus error object, or GLOBUS_SUCCESS. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the existence check operation. 
 <i>url</i> The URL of the directory or file to check. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes to use for this operation. 
 <i>complete_callback</i> Callback to be invoked once the existence operation is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> u_handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_extended_get (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, const char *eret_alg_str, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file from an FTP server with server-side processing. 

 This function starts a 'get' file transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this URL. 

 When all of the data associated with this URL is retrieved, and all of the data callbacks have been called, or if the get request is aborted, the complete_callback will be invoked with the final status of the get. 

 This function differs from the <b>globus_ftp_client_get()</b> function by allowing the user to invoke server-side data processing algorithms. GridFTP servers may support support algorithms for data reduction or other customized data storage requirements. There is no client-side verification done on the algorithm string provided by the user. If the server does not understand the requested algorithm, the transfer will fail. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation. 
 <i>url</i> The URL to download. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>restart</i> Pointer to a restart marker. 
 <i>eret_alg_str</i> The ERET algorithm string. This string contains information needed to invoke a server-specific data reduction algorithm on the file being retrieved. 
 <i>complete_callback</i> Callback to be invoked once the 'get' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_read()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_extended_put (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, const char *esto_alg_str, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Store a file on an FTP server with server-side processing. 

 This function starts a 'put' file transfer to an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_write()</b> to send the data associated with this URL. 

 When all of the data associated with this URL is sent, and all of the data callbacks have been called, or if the put request is aborted, the complete_callback will be invoked with the final status of the put. 

 This function differs from the <b>globus_ftp_client_put()</b> function by allowing the user to invoke server-side data processing algorithms. GridFTP servers may support algorithms for data reduction or other customized data storage requirements. There is no client-side verification done on the alogirhtm string provided by the user. if the server does not understand the requested algorithm, the transfer will fail. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the put operation. 
 <i>url</i> The URL to store the data to. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>restart</i> Pointer to a restart marker. 
 <i>esto_alg_str</i> 
 <i>complete_callback</i> Callback to be invoked once the 'put' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_write()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_extended_third_party_transfer (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *eret_alg_str, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *dest_attr, const char *esto_alg_str, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Transfer a file between two FTP servers with server-side processing. 

 This function starts up a third-party file transfer between FTP server. This function returns immediately. 

 When the transfer is completed or if the transfer is aborted, the complete_callback will be invoked with the final status of the transfer. 

 This function differes from the <b>globus_ftp_client_third_party_transfer()</b> funciton by allowing the user to invoke server-side data processing algorithms. GridFTP servers may support algorithms for data reduction or other customized data storage requirements. There is no client-side verification done on the alogirhtm string provided by the user. if the server does not understand * the requested algorithm, the transfer will fail. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation. 
 <i>source_url</i> The URL to transfer. The URL may be an ftp or gsiftp URL. 
 <i>source_attr</i> Attributes for the souce URL. 
 <i>eret_alg_str</i> 
 <i>dest_url</i> The destination URL for the transfer. The URL may be an ftp or gsiftp URL. 
 <i>dest_attr</i> Attributes for the destination URL. 
 <i>esto_alg_str</i> 
 <i>restart</i> Pointer to a restart marker. 
 <i>complete_callback</i> Callback to be invoked once the 'put' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Note:</b>
<dl>
<dt>
<dd> The source_attr and dest_attr MUST be compatible. For example, the MODE and TYPE should match for both the source and destination.</dl>
 

 

<h3>globus_result_t globus_ftp_client_feat (<b>globus_ftp_client_handle_t</b> *u_handle, char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_features_t</b> *u_features, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Check the features supported by the server (FTP FEAT command). After this procedure completes, the features set (parameter u_features) represents the features supported by the server. Prior to calling this procedure, the structure should have been initialized by <b>globus_ftp_client_features_init()</b>; afterwards, it should be destroyed by <b>globus_ftp_client_features_destroy()</b>. After <b>globus_ftp_client_feat()</b> returns, each feature in the list has one of the values: GLOBUS_FTP_CLIENT_TRUE, GLOBUS_FTP_CLIENT_FALSE, or GLOBUS_FTP_CLIENT_MAYBE. The first two denote the server supporting, or not supporting, the given feature. The last one means that the test has not been performed. This is not necessarily caused by error; there might have been no reason to check for this particular feature. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>u_features</i> A pointer to a globus_ftp_client_features_t to be filled with the feature set supported by the server. 
 <i>complete_callback</i> Callback to be invoked once the size check is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> u_handle is GLOBUS_NULL
<dt>&bull;
<dd> source_url is GLOBUS_NULL
<dt>&bull;
<dd> source_url cannot be parsed
<dt>&bull;
<dd> source_url is not a ftp or gsiftp url
<dt>&bull;
<dd> u_features is GLOBUS_NULL or badly initialized
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_features_destroy (<b>globus_ftp_client_features_t</b> *u_features)</h3>

 Destroy the feature set. 

 <b>Note:</b>
<dl>
<dt>
<dd> Structure passed to this function must have been previously initialized by <b>globus_ftp_client_features_init()</b>.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> GLOBUS_SUCCESS on success, otherwise error.</dl>
 

 

<h3>globus_result_t globus_ftp_client_features_init (<b>globus_ftp_client_features_t</b> *u_features)</h3>

 Initialize the feature set, to be later used by <b>globus_ftp_client_feat()</b>. Each feature gets initial value GLOBUS_FTP_CLIENT_MAYBE. 

 <b>Note:</b>
<dl>
<dt>
<dd> Structure initialized by this function must be destroyed using <b>globus_ftp_client_features_destroy()</b></dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> GLOBUS_SUCCESS on success, otherwise error.</dl>
 

 

<h3>globus_result_t globus_ftp_client_get (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file from an FTP server. 

 This function starts a 'get' file transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this URL. 

 When all of the data associated with this URL is retrieved, and all of the data callbacks have been called, or if the get request is aborted, the complete_callback will be invoked with the final status of the get. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation. 
 <i>url</i> The URL to download. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>restart</i> Pointer to a restart marker. 
 <i>complete_callback</i> Callback to be invoked once the 'get' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_read()</b></dl>
 

 

 

 <b>Examples: </b> <b>globus_ftp_client_debug_plugin.example</b>, and <b>globus_ftp_client_restart_plugin.example</b>.

<h3>globus_result_t globus_ftp_client_is_feature_supported (const <b>globus_ftp_client_features_t</b> *u_features, <b>globus_ftp_client_tristate_t</b> *answer, <b>globus_ftp_client_probed_feature_t</b>feature)</h3>

 Check if the feature is supported by the server. After the function completes, parameter answer contains the state of the server support of the given function. It can have one of the values: GLOBUS_FTP_CLIENT_TRUE, GLOBUS_FTP_CLIENT_FALSE, or GLOBUS_FTP_CLIENT_MAYBE. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_features</i> list of features, as returned by <b>globus_ftp_client_feat()</b> 
 <i>answer</i> this variable will contain the answer 
 <i>feature</i> feature number, 0 &lt;= feature &lt; GLOBUS_FTP_CLIENT_FEATURE_MAX</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> error when any of the parameters is null or badly initialized</dl>
 

 

<h3>globus_result_t globus_ftp_client_list (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file listing from an FTP server. 

 This function starts a 'NLST' transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this listing. 

 When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>complete_callback</i> Callback to be invoked once the 'list' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_read()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_machine_list (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a machine parseable file listing from an FTP server. 

 This function starts a 'MLSD' transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this listing. 

 When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>complete_callback</i> Callback to be invoked once the 'list' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_read()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_mkdir (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Make a directory on an FTP server. 

 This function starts a mkdir operation on a FTP server. 

 When the response to the mkdir request has been received the complete_callback will be invoked with the result of the mkdir operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the mkdir operation. 
 <i>url</i> The URL for the directory to create. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the mkdir is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> u_handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_mlst (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_byte_t **mlst_buffer, globus_size_t *mlst_buffer_length, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get information about a file or directory from a FTP server. 

 This function requests the MLST fact string of a file or directory from an FTP server. 

 When the MLST request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the MLST fact string will be stored in the globus_byte_t * pointed to by the mlst_buffer parameter to this function. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL of a file or directory to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>mlst_buffer</i> A pointer to a globus_byte_t * to be allocated and filled with the MLST fact string of the file, if it exists. Otherwise, the value pointed to by it is undefined. It is up to the user to free this memory. 
 <i>mlst_buffer_length</i> A pointer to a globus_size_t to be filled with the length of the data in mlst_buffer. 
 <i>complete_callback</i> Callback to be invoked once the MLST command is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> mlst_buffer is GLOBUS_NULL
<dt>&bull;
<dd> mlst_buffer_length is GLOBUS_NULL
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_modification_time (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_abstime_t *modification_time, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file's modification time from an FTP server. 

 This function requests the modification time of a file from an FTP server. 

 When the modification time request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the modification time will be stored in the globus_abstime_t value pointed to by the modification_time parameter to this function. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>modification_time</i> A pointer to a globus_abstime_t to be filled with the modification time of the file, if it exists. Otherwise, the value pointed to by it is undefined. 
 <i>complete_callback</i> Callback to be invoked once the modification time check is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> modification time is GLOBUS_NULL
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_move (<b>globus_ftp_client_handle_t</b> *u_handle, const char *source_url, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Move a file on an FTP server. 

 This function starts a move (rename) operation on an FTP server. Note that this function does not move files between FTP servers and that the host:port part of the destination url is ignored. 

 When the response to the move request has been received the complete_callback will be invoked with the result of the move operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the move operation. 
 <i>source_url</i> The URL for the file to move. 
 <i>dest_url</i> The URL for the target of the move. The host:port part of this URL is ignored. 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the move is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> source_url is GLOBUS_NULL
<dt>&bull;
<dd> source_url cannot be parsed
<dt>&bull;
<dd> source_url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_partial_get (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, globus_off_tpartial_offset, globus_off_tpartial_end_offset, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file from an FTP server. 

 This function starts a 'get' file transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this URL. 

 When all of the data associated with this URL is retrieved, and all of the data callbacks have been called, or if the get request is aborted, the complete_callback will be invoked with the final status of the get. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation. 
 <i>url</i> The URL to download. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>restart</i> Pointer to a restart marker. 
 <i>partial_offset</i> Starting offset for a partial file get. 
 <i>partial_end_offset</i> Ending offset for a partial file get. Use -1 for EOF. 
 <i>complete_callback</i> Callback to be invoked once the 'get' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_partial_put (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, globus_off_tpartial_offset, globus_off_tpartial_end_offset, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Store a file on an FTP server. 

 This function starts a 'put' file transfer to an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_write()</b> to send the data associated with this URL. 

 When all of the data associated with this URL is sent, and all of the data callbacks have been called, or if the put request is aborted, the complete_callback will be invoked with the final status of the put. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the put operation. 
 <i>url</i> The URL to store the data to. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>restart</i> Pointer to a restart marker. 
 <i>partial_offset</i> Starting offset for a partial file put. 
 <i>partial_end_offset</i> Ending offset for a partial file put. 
 <i>complete_callback</i> Callback to be invoked once the 'put' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_write()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_partial_third_party_transfer (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *dest_attr, <b>globus_ftp_client_restart_marker_t</b> *restart, globus_off_tpartial_offset, globus_off_tpartial_end_offset, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Transfer a file between two FTP servers. 

 This function starts up a third-party file transfer between FTP server. This function returns immediately. 

 When the transfer is completed or if the transfer is aborted, the complete_callback will be invoked with the final status of the transfer. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation. 
 <i>source_url</i> The URL to transfer. The URL may be an ftp or gsiftp URL. 
 <i>source_attr</i> Attributes for the souce URL. 
 <i>dest_url</i> The destination URL for the transfer. The URL may be an ftp or gsiftp URL. 
 <i>dest_attr</i> Attributes for the destination URL. 
 <i>restart</i> Pointer to a restart marker. 
 <i>partial_offset</i> Starting offset for a partial file get. 
 <i>partial_end_offset</i> Ending offset for a partial file get. Use -1 for EOF. 
 <i>complete_callback</i> Callback to be invoked once the 'put' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Note:</b>
<dl>
<dt>
<dd> The source_attr and dest_attr MUST be compatible. For example, the MODE and TYPE should match for both the source and destination.</dl>
 

 

<h3>globus_result_t globus_ftp_client_put (<b>globus_ftp_client_handle_t</b> *handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Store a file on an FTP server. 

 This function starts a 'put' file transfer to an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_write()</b> to send the data associated with this URL. 

 When all of the data associated with this URL is sent, and all of the data callbacks have been called, or if the put request is aborted, the complete_callback will be invoked with the final status of the put. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the put operation. 
 <i>url</i> The URL to store the data to. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>restart</i> Pointer to a restart marker. 
 <i>complete_callback</i> Callback to be invoked once the 'put' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_write()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_recursive_list (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a machine parseable recursive file listing from an FTP server. 

 This function starts a 'MLSR' transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this listing. 

 When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>complete_callback</i> Callback to be invoked once the 'list' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_read()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_rmdir (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Make a directory on an FTP server. 

 This function starts a rmdir operation on a FTP server. 

 When the response to the rmdir request has been received the complete_callback will be invoked with the result of the rmdir operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the rmdir operation. 
 <i>url</i> The URL for the directory to create. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the rmdir is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> u_handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_size (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_off_t *size, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file's size from an FTP server. 

 This function requests the size of a file from an FTP server. 

 When the size request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the size will be stored in the globus_off_t value pointed to by the size parameter to this function. 

 <b>Note:</b>
<dl>
<dt>
<dd> In ASCII mode, the size will be the size of the file after conversion to ASCII mode. The actual amount of data which is returned in the data callbacks may be less than this amount.</dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>size</i> A pointer to a globus_off_t to be filled with the total size of the file, if it exists. Otherwise, the value pointed to by it is undefined. 
 <i>complete_callback</i> Callback to be invoked once the size check is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> size is GLOBUS_NULL
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_stat (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, globus_byte_t **stat_buffer, globus_size_t *stat_buffer_length, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get information about a file or directory from a FTP server. 

 This function requests the STAT listing of a file or directory from an FTP server. 

 When the STAT request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the STAT fact string will be stored in the globus_byte_t * pointed to by the stat_buffer parameter to this function. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL of a file or directory to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>stat_buffer</i> A pointer to a globus_byte_t * to be allocated and filled with the STAT listing of the file, if it exists. Otherwise, the value pointed to by it is undefined. It is up to the user to free this memory. 
 <i>stat_buffer_length</i> A pointer to a globus_size_t to be filled with the length of the data in stat_buffer. 
 <i>complete_callback</i> Callback to be invoked once the STAT command is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> stat_buffer is GLOBUS_NULL
<dt>&bull;
<dd> stat_buffer_length is GLOBUS_NULL
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_symlink (<b>globus_ftp_client_handle_t</b> *u_handle, const char *source_url, const char *link_url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Create a symbolic link on the FTP server. 

 This function creates a symbolic link on the FTP server pointing to a given path. Note that this function does not link files between FTP servers and that the host:port part of the link url is ignored. 

 When the response to the symlink request has been received the complete_callback will be invoked with the result of the move operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the move operation. 
 <i>source_url</i> The URL for the symbolic link to create. 
 <i>link_url</i> The URL for the target of the link. The host:port part of this URL is ignored. 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the symlink is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> source_url is GLOBUS_NULL
<dt>&bull;
<dd> source_url cannot be parsed
<dt>&bull;
<dd> source_url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_third_party_transfer (<b>globus_ftp_client_handle_t</b> *handle, const char *source_url, <b>globus_ftp_client_operationattr_t</b> *source_attr, const char *dest_url, <b>globus_ftp_client_operationattr_t</b> *dest_attr, <b>globus_ftp_client_restart_marker_t</b> *restart, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Transfer a file between two FTP servers. 

 This function starts up a third-party file transfer between FTP server. This function returns immediately. 

 When the transfer is completed or if the transfer is aborted, the complete_callback will be invoked with the final status of the transfer. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation. 
 <i>source_url</i> The URL to transfer. The URL may be an ftp or gsiftp URL. 
 <i>source_attr</i> Attributes for the souce URL. 
 <i>dest_url</i> The destination URL for the transfer. The URL may be an ftp or gsiftp URL. 
 <i>dest_attr</i> Attributes for the destination URL. 
 <i>restart</i> Pointer to a restart marker. 
 <i>complete_callback</i> Callback to be invoked once the 'put' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Note:</b>
<dl>
<dt>
<dd> The source_attr and dest_attr MUST be compatible. For example, the MODE and TYPE should match for both the source and destination.</dl>
 

 

<h3>globus_result_t globus_ftp_client_utime (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, const struct tm *utime_time, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Set the modification time on a file. 

 This function changes file modification time 

 When the response to the modification time request has been received the complete_callback will be invoked with the result of the operation. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the change operation. 
 <i>url</i> The URL of the file to modify group membership. 
 <i>utime_time</i> The absolute time to which the file's modification time should be set. 
 <i>attr</i> Attributes for this operation. 
 <i>complete_callback</i> Callback to be invoked once the change is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 

<h3>globus_result_t globus_ftp_client_verbose_list (<b>globus_ftp_client_handle_t</b> *u_handle, const char *url, <b>globus_ftp_client_operationattr_t</b> *attr, <b>globus_ftp_client_complete_callback_t</b>complete_callback, void *callback_arg)</h3>

 Get a file listing from an FTP server. 

 This function starts a 'LIST' transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <b>globus_ftp_client_register_read()</b> to retrieve the data associated with this listing. 

 When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation. 
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL. 
 <i>attr</i> Attributes for this file transfer. 
 <i>complete_callback</i> Callback to be invoked once the 'list' is completed. 
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:
<dl>
<dt>&bull;
<dd> handle is GLOBUS_NULL
<dt>&bull;
<dd> url is GLOBUS_NULL
<dt>&bull;
<dd> url cannot be parsed
<dt>&bull;
<dd> url is not a ftp or gsiftp url
<dt>&bull;
<dd> complete_callback is GLOBUS_NULL
<dt>&bull;
<dd> handle already has an operation in progress</dl>
 

</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_register_read()</b></dl>
 

 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_ftp_client from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbBE">Enumeration Type Documentation</a>
<dd>


<dt><a HREF="#lbBH">Function Documentation</a>
<dd>


<dt><a HREF="#lbCP">Author</a>
<dd></dl>
