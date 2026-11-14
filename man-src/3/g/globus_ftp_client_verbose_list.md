---
title: "globus_ftp_client_verbose_list(3)"
name: "globus_ftp_client_verbose_list"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_verbose_list/"
description: "FTP Operations –"
---

<h2 class="name">NAME</h2>
<p> FTP Operations &#8211; </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_ftp_client_complete_callback_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error) </p>
<p> typedef struct<br />
 <code>globus_i_ftp_client_features_s</code> * <code>globus_ftp_client_features_t</code>&quot;<br />
 <i>Feature Handle</i> </p>
<p> Handle used to associate state with feature operations. &quot;</p>
<h3>Enumerations</h3>
<p> enum <code>globus_ftp_client_tristate_t</code> </p>
<p> enum <code>globus_ftp_client_probed_feature_t</code> </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_machine_list</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_recursive_list</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>File or Directory Existence</h3>
<p> globus_result_t <code>globus_ftp_client_exists</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Features</h3>
<p> globus_result_t <code>globus_ftp_client_features_init</code> (<code>globus_ftp_client_features_t</code> *u_features) </p>
<p> globus_result_t <code>globus_ftp_client_features_destroy</code> (<code>globus_ftp_client_features_t</code> *u_features) </p>
<p> globus_result_t <code>globus_ftp_client_feat</code> (<code>globus_ftp_client_handle_t</code> *u_handle, char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_features_t</code> *u_features, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_is_feature_supported</code> (const <code>globus_ftp_client_features_t</code> *u_features, <code>globus_ftp_client_tristate_t</code> *answer, <code>globus_ftp_client_probed_feature_t</code> feature) </p>
<h3>Make Directory</h3>
<p> globus_result_t <code>globus_ftp_client_mkdir</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Remove Directory</h3>
<p> globus_result_t <code>globus_ftp_client_rmdir</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Change Working Directory</h3>
<p> globus_result_t <code>globus_ftp_client_cwd</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_byte_t **cwd_buffer, globus_size_t *cwd_buffer_length, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Delete</h3>
<p> globus_result_t <code>globus_ftp_client_delete</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>List</h3>
<p> globus_result_t <code>globus_ftp_client_list</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_verbose_list</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>STAT</h3>
<p> globus_result_t <code>globus_ftp_client_stat</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_byte_t **stat_buffer, globus_size_t *stat_buffer_length, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>MLST</h3>
<p> globus_result_t <code>globus_ftp_client_mlst</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_byte_t **mlst_buffer, globus_size_t *mlst_buffer_length, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Move</h3>
<p> globus_result_t <code>globus_ftp_client_move</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *source_url, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>chmod</h3>
<p> globus_result_t <code>globus_ftp_client_chmod</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, int mode, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>chgrp</h3>
<p> globus_result_t <code>globus_ftp_client_chgrp</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, const char *group, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>utime</h3>
<p> globus_result_t <code>globus_ftp_client_utime</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, const struct tm *utime_time, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>symlink</h3>
<p> globus_result_t <code>globus_ftp_client_symlink</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *source_url, const char *link_url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Get</h3>
<p> globus_result_t <code>globus_ftp_client_get</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_partial_get</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, globus_off_t partial_offset, globus_off_t partial_end_offset, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_extended_get</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, const char *eret_alg_str, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Put</h3>
<p> globus_result_t <code>globus_ftp_client_put</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_partial_put</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, globus_off_t partial_offset, globus_off_t partial_end_offset, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_extended_put</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, const char *esto_alg_str, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>3rd Party Transfer</h3>
<p> globus_result_t <code>globus_ftp_client_third_party_transfer</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *dest_attr, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_partial_third_party_transfer</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *dest_attr, <code>globus_ftp_client_restart_marker_t</code> *restart, globus_off_t partial_offset, globus_off_t partial_end_offset, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_extended_third_party_transfer</code> (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *eret_alg_str, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *dest_attr, const char *esto_alg_str, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Modification Time</h3>
<p> globus_result_t <code>globus_ftp_client_modification_time</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_abstime_t *modification_time, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Size</h3>
<p> globus_result_t <code>globus_ftp_client_size</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_off_t *size, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Cksm</h3>
<p> globus_result_t <code>globus_ftp_client_cksm</code> (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, char *cksm, globus_off_t offset, globus_off_t length, const char *algorithm, <code>globus_ftp_client_complete_callback_t</code> complete_callback, void *callback_arg) </p>
<h3>Abort</h3>
<p> globus_result_t <code>globus_ftp_client_abort</code> (<code>globus_ftp_client_handle_t</code> *u_handle) </p>
<h2>Detailed Description</h2>
<p> Initiate an FTP operation. </p>
<p> This module contains the API functions for a user to request a get, put, third-party transfer, or other FTP file operation.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_client_complete_callback_t)(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error)</h3>
<p> Operation complete callback. </p>
<p> Every FTP Client operation (get, put, transfer, mkdir, etc) is asynchronous. A callback of this type is passed to each of the operation function calls to let the user know when the operation is complete. The completion callback is called only once per operation, after all other callbacks for the operation have returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_arg</i> The user_arg parameter passed to the operation.<br />
 <i>handle</i> The handle on which the operation was done.<br />
 <i>error</i> A Globus error object indicating any problem which occurred, or GLOBUS_SUCCESS, if the operation completed successfully.</dl>
<h3>typedef struct <code>globus_i_ftp_client_features_s</code>* <code>globus_ftp_client_features_t</code></h3>
<p> Feature Handle </p>
<p> Handle used to associate state with feature operations. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_feat</code>, <code>globus_ftp_client_features_init</code>, <code>globus_ftp_client_features_destroy</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_ftp_client_probed_feature_t</code></h3>
<p> Types of features</p>
<h3>enum <code>globus_ftp_client_tristate_t</code></h3>
<p> Types for feature existence </p>
<p> FALSE and TRUE are known to be fact that a feature does or does not exist MAYBE means that the feature may exist</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_abort (<code>globus_ftp_client_handle_t</code> *u_handle)</h3>
<p> Abort the operation currently in progress. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> Handle which to abort.</dl>
<h3>globus_result_t globus_ftp_client_chgrp (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, const char *group, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Change group membership on a file. </p>
<p> This function changes file group membership </p>
<p> When the response to the group change request has been received the complete_callback will be invoked with the result of the operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the change operation.<br />
 <i>url</i> The URL of the file to modify group membership.<br />
 <i>group</i> The group name or numeric identifier for the group that the file should become a member of.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the change is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_chmod (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, intmode, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Change permissions on a file. </p>
<p> This function changes file permissions </p>
<p> When the response to the move request has been received the complete_callback will be invoked with the result of the operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the move operation.<br />
 <i>url</i> The URL of the file to modify permissions.<br />
 <i>mode</i> The integer file mode to change to. Be sure that the integer is in the proper base, i.e. 0777 (octal) vs 777 (decimal).<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the move is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_cksm (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, char *cksm, globus_off_toffset, globus_off_tlength, const char *algorithm, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file&#8217;s checksum from an FTP server. </p>
<p> This function requests the checksum of a file from an FTP server. </p>
<p> When the request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the checksum will be stored in the char * buffer provided in the &#8216;checksum&#8217; parameter to this function. The buffer must be large enough to hold the expected checksum result. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>cksm</i> A pointer to a buffer to be filled with the checksum of the file. On error the buffer contents are undefined.<br />
 <i>offset</i> File offset to start calculating checksum.<br />
 <i>length</i> Length of data to read from the starting offset. Use -1 to read the entire file.<br />
 <i>algorithm</i> A pointer to a string to specifying the desired algorithm Currently, GridFTP servers only support the MD5 algorithm.<br />
 <i>complete_callback</i> Callback to be invoked once the checksum is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> size is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_cwd (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_byte_t **cwd_buffer, globus_size_t *cwd_buffer_length, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Make a directory on an FTP server. </p>
<p> This function starts a cwd operation on a FTP server. </p>
<p> When the response to the cwd request has been received the complete_callback will be invoked with the result of the cwd operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the cwd operation.<br />
 <i>url</i> The URL for the directory to cd into. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>cwd_buffer</i> A pointer to a globus_byte_t * to be allocated and filled with the directory name returned by the CWD, if it succeeds. Otherwise, the value pointed to by it is undefined. It is up the user to free this memory.<br />
 <i>cwd_buffer_length</i> A pointer to a globus_size_t to be filled with the length of the data in cwd_buffer.<br />
 <i>complete_callback</i> Callback to be invoked once the cwd is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> u_handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> cwd_buffer is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> cwd_buffer_length is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_delete (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Delete a file on an FTP server. </p>
<p> This function starts a delete operation on a FTP server. Note that this functions will only delete files, not directories. </p>
<p> When the response to the delete request has been received the complete_callback will be invoked with the result of the delete operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the delete operation.<br />
 <i>url</i> The URL for the file to delete. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>complete_callback</i> Callback to be invoked once the delete is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> u_handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_exists (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Check for the existence of a file or directory on an FTP server. </p>
<p> This function attempts to determine whether the specified URL points to a valid file or directory. The <i>complete_callback</i> will be invoked with the result of the existence check passed as a globus error object, or GLOBUS_SUCCESS. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the existence check operation.<br />
 <i>url</i> The URL of the directory or file to check. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes to use for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the existence operation is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> u_handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_extended_get (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, const char *eret_alg_str, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file from an FTP server with server-side processing. </p>
<p> This function starts a &#8216;get&#8217; file transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this URL. </p>
<p> When all of the data associated with this URL is retrieved, and all of the data callbacks have been called, or if the get request is aborted, the complete_callback will be invoked with the final status of the get. </p>
<p> This function differs from the <code>globus_ftp_client_get()</code> function by allowing the user to invoke server-side data processing algorithms. GridFTP servers may support support algorithms for data reduction or other customized data storage requirements. There is no client-side verification done on the algorithm string provided by the user. If the server does not understand the requested algorithm, the transfer will fail. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation.<br />
 <i>url</i> The URL to download. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>eret_alg_str</i> The ERET algorithm string. This string contains information needed to invoke a server-specific data reduction algorithm on the file being retrieved.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;get&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_read()</code></dl>
<h3>globus_result_t globus_ftp_client_extended_put (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, const char *esto_alg_str, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Store a file on an FTP server with server-side processing. </p>
<p> This function starts a &#8216;put&#8217; file transfer to an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_write()</code> to send the data associated with this URL. </p>
<p> When all of the data associated with this URL is sent, and all of the data callbacks have been called, or if the put request is aborted, the complete_callback will be invoked with the final status of the put. </p>
<p> This function differs from the <code>globus_ftp_client_put()</code> function by allowing the user to invoke server-side data processing algorithms. GridFTP servers may support algorithms for data reduction or other customized data storage requirements. There is no client-side verification done on the alogirhtm string provided by the user. if the server does not understand the requested algorithm, the transfer will fail. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the put operation.<br />
 <i>url</i> The URL to store the data to. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>esto_alg_str</i><br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;put&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_write()</code></dl>
<h3>globus_result_t globus_ftp_client_extended_third_party_transfer (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *eret_alg_str, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *dest_attr, const char *esto_alg_str, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Transfer a file between two FTP servers with server-side processing. </p>
<p> This function starts up a third-party file transfer between FTP server. This function returns immediately. </p>
<p> When the transfer is completed or if the transfer is aborted, the complete_callback will be invoked with the final status of the transfer. </p>
<p> This function differes from the <code>globus_ftp_client_third_party_transfer()</code> funciton by allowing the user to invoke server-side data processing algorithms. GridFTP servers may support algorithms for data reduction or other customized data storage requirements. There is no client-side verification done on the alogirhtm string provided by the user. if the server does not understand * the requested algorithm, the transfer will fail. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation.<br />
 <i>source_url</i> The URL to transfer. The URL may be an ftp or gsiftp URL.<br />
 <i>source_attr</i> Attributes for the souce URL.<br />
 <i>eret_alg_str</i><br />
 <i>dest_url</i> The destination URL for the transfer. The URL may be an ftp or gsiftp URL.<br />
 <i>dest_attr</i> Attributes for the destination URL.<br />
 <i>esto_alg_str</i><br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;put&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The source_attr and dest_attr MUST be compatible. For example, the MODE and TYPE should match for both the source and destination.</dl>
<h3>globus_result_t globus_ftp_client_feat (<code>globus_ftp_client_handle_t</code> *u_handle, char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_features_t</code> *u_features, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Check the features supported by the server (FTP FEAT command). After this procedure completes, the features set (parameter u_features) represents the features supported by the server. Prior to calling this procedure, the structure should have been initialized by <code>globus_ftp_client_features_init()</code>; afterwards, it should be destroyed by <code>globus_ftp_client_features_destroy()</code>. After <code>globus_ftp_client_feat()</code> returns, each feature in the list has one of the values: GLOBUS_FTP_CLIENT_TRUE, GLOBUS_FTP_CLIENT_FALSE, or GLOBUS_FTP_CLIENT_MAYBE. The first two denote the server supporting, or not supporting, the given feature. The last one means that the test has not been performed. This is not necessarily caused by error; there might have been no reason to check for this particular feature. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>u_features</i> A pointer to a globus_ftp_client_features_t to be filled with the feature set supported by the server.<br />
 <i>complete_callback</i> Callback to be invoked once the size check is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> u_handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> source_url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> source_url cannot be parsed</p>
<dt>&bull;</p>
<dd> source_url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> u_features is GLOBUS_NULL or badly initialized</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_features_destroy (<code>globus_ftp_client_features_t</code> *u_features)</h3>
<p> Destroy the feature set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Structure passed to this function must have been previously initialized by <code>globus_ftp_client_features_init()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS on success, otherwise error.</dl>
<h3>globus_result_t globus_ftp_client_features_init (<code>globus_ftp_client_features_t</code> *u_features)</h3>
<p> Initialize the feature set, to be later used by <code>globus_ftp_client_feat()</code>. Each feature gets initial value GLOBUS_FTP_CLIENT_MAYBE. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Structure initialized by this function must be destroyed using <code>globus_ftp_client_features_destroy()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS on success, otherwise error.</dl>
<h3>globus_result_t globus_ftp_client_get (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file from an FTP server. </p>
<p> This function starts a &#8216;get&#8217; file transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this URL. </p>
<p> When all of the data associated with this URL is retrieved, and all of the data callbacks have been called, or if the get request is aborted, the complete_callback will be invoked with the final status of the get. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation.<br />
 <i>url</i> The URL to download. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;get&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_read()</code></dl>
<p> <code>Examples: </code> <code>globus_ftp_client_debug_plugin.example</code>, and <code>globus_ftp_client_restart_plugin.example</code>.</p>
<h3>globus_result_t globus_ftp_client_is_feature_supported (const <code>globus_ftp_client_features_t</code> *u_features, <code>globus_ftp_client_tristate_t</code> *answer, <code>globus_ftp_client_probed_feature_t</code>feature)</h3>
<p> Check if the feature is supported by the server. After the function completes, parameter answer contains the state of the server support of the given function. It can have one of the values: GLOBUS_FTP_CLIENT_TRUE, GLOBUS_FTP_CLIENT_FALSE, or GLOBUS_FTP_CLIENT_MAYBE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_features</i> list of features, as returned by <code>globus_ftp_client_feat()</code><br />
 <i>answer</i> this variable will contain the answer<br />
 <i>feature</i> feature number, 0 &lt;= feature &lt; GLOBUS_FTP_CLIENT_FEATURE_MAX</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> error when any of the parameters is null or badly initialized</dl>
<h3>globus_result_t globus_ftp_client_list (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file listing from an FTP server. </p>
<p> This function starts a &#8216;NLST&#8217; transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this listing. </p>
<p> When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;list&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_read()</code></dl>
<h3>globus_result_t globus_ftp_client_machine_list (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a machine parseable file listing from an FTP server. </p>
<p> This function starts a &#8216;MLSD&#8217; transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this listing. </p>
<p> When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;list&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_read()</code></dl>
<h3>globus_result_t globus_ftp_client_mkdir (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Make a directory on an FTP server. </p>
<p> This function starts a mkdir operation on a FTP server. </p>
<p> When the response to the mkdir request has been received the complete_callback will be invoked with the result of the mkdir operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the mkdir operation.<br />
 <i>url</i> The URL for the directory to create. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the mkdir is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> u_handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_mlst (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_byte_t **mlst_buffer, globus_size_t *mlst_buffer_length, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get information about a file or directory from a FTP server. </p>
<p> This function requests the MLST fact string of a file or directory from an FTP server. </p>
<p> When the MLST request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the MLST fact string will be stored in the globus_byte_t * pointed to by the mlst_buffer parameter to this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL of a file or directory to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>mlst_buffer</i> A pointer to a globus_byte_t * to be allocated and filled with the MLST fact string of the file, if it exists. Otherwise, the value pointed to by it is undefined. It is up to the user to free this memory.<br />
 <i>mlst_buffer_length</i> A pointer to a globus_size_t to be filled with the length of the data in mlst_buffer.<br />
 <i>complete_callback</i> Callback to be invoked once the MLST command is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> mlst_buffer is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> mlst_buffer_length is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_modification_time (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_abstime_t *modification_time, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file&#8217;s modification time from an FTP server. </p>
<p> This function requests the modification time of a file from an FTP server. </p>
<p> When the modification time request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the modification time will be stored in the globus_abstime_t value pointed to by the modification_time parameter to this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>modification_time</i> A pointer to a globus_abstime_t to be filled with the modification time of the file, if it exists. Otherwise, the value pointed to by it is undefined.<br />
 <i>complete_callback</i> Callback to be invoked once the modification time check is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> modification time is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_move (<code>globus_ftp_client_handle_t</code> *u_handle, const char *source_url, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Move a file on an FTP server. </p>
<p> This function starts a move (rename) operation on an FTP server. Note that this function does not move files between FTP servers and that the host:port part of the destination url is ignored. </p>
<p> When the response to the move request has been received the complete_callback will be invoked with the result of the move operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the move operation.<br />
 <i>source_url</i> The URL for the file to move.<br />
 <i>dest_url</i> The URL for the target of the move. The host:port part of this URL is ignored.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the move is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> source_url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> source_url cannot be parsed</p>
<dt>&bull;</p>
<dd> source_url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_partial_get (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, globus_off_tpartial_offset, globus_off_tpartial_end_offset, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file from an FTP server. </p>
<p> This function starts a &#8216;get&#8217; file transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this URL. </p>
<p> When all of the data associated with this URL is retrieved, and all of the data callbacks have been called, or if the get request is aborted, the complete_callback will be invoked with the final status of the get. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation.<br />
 <i>url</i> The URL to download. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>partial_offset</i> Starting offset for a partial file get.<br />
 <i>partial_end_offset</i> Ending offset for a partial file get. Use -1 for EOF.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;get&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_partial_put (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, globus_off_tpartial_offset, globus_off_tpartial_end_offset, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Store a file on an FTP server. </p>
<p> This function starts a &#8216;put&#8217; file transfer to an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_write()</code> to send the data associated with this URL. </p>
<p> When all of the data associated with this URL is sent, and all of the data callbacks have been called, or if the put request is aborted, the complete_callback will be invoked with the final status of the put. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the put operation.<br />
 <i>url</i> The URL to store the data to. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>partial_offset</i> Starting offset for a partial file put.<br />
 <i>partial_end_offset</i> Ending offset for a partial file put.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;put&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_write()</code></dl>
<h3>globus_result_t globus_ftp_client_partial_third_party_transfer (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *dest_attr, <code>globus_ftp_client_restart_marker_t</code> *restart, globus_off_tpartial_offset, globus_off_tpartial_end_offset, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Transfer a file between two FTP servers. </p>
<p> This function starts up a third-party file transfer between FTP server. This function returns immediately. </p>
<p> When the transfer is completed or if the transfer is aborted, the complete_callback will be invoked with the final status of the transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation.<br />
 <i>source_url</i> The URL to transfer. The URL may be an ftp or gsiftp URL.<br />
 <i>source_attr</i> Attributes for the souce URL.<br />
 <i>dest_url</i> The destination URL for the transfer. The URL may be an ftp or gsiftp URL.<br />
 <i>dest_attr</i> Attributes for the destination URL.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>partial_offset</i> Starting offset for a partial file get.<br />
 <i>partial_end_offset</i> Ending offset for a partial file get. Use -1 for EOF.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;put&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The source_attr and dest_attr MUST be compatible. For example, the MODE and TYPE should match for both the source and destination.</dl>
<h3>globus_result_t globus_ftp_client_put (<code>globus_ftp_client_handle_t</code> *handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Store a file on an FTP server. </p>
<p> This function starts a &#8216;put&#8217; file transfer to an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_write()</code> to send the data associated with this URL. </p>
<p> When all of the data associated with this URL is sent, and all of the data callbacks have been called, or if the put request is aborted, the complete_callback will be invoked with the final status of the put. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the put operation.<br />
 <i>url</i> The URL to store the data to. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;put&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_write()</code></dl>
<h3>globus_result_t globus_ftp_client_recursive_list (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a machine parseable recursive file listing from an FTP server. </p>
<p> This function starts a &#8216;MLSR&#8217; transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this listing. </p>
<p> When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;list&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_read()</code></dl>
<h3>globus_result_t globus_ftp_client_rmdir (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Make a directory on an FTP server. </p>
<p> This function starts a rmdir operation on a FTP server. </p>
<p> When the response to the rmdir request has been received the complete_callback will be invoked with the result of the rmdir operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the rmdir operation.<br />
 <i>url</i> The URL for the directory to create. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the rmdir is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> u_handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_size (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_off_t *size, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file&#8217;s size from an FTP server. </p>
<p> This function requests the size of a file from an FTP server. </p>
<p> When the size request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the size will be stored in the globus_off_t value pointed to by the size parameter to this function. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> In ASCII mode, the size will be the size of the file after conversion to ASCII mode. The actual amount of data which is returned in the data callbacks may be less than this amount.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>size</i> A pointer to a globus_off_t to be filled with the total size of the file, if it exists. Otherwise, the value pointed to by it is undefined.<br />
 <i>complete_callback</i> Callback to be invoked once the size check is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> size is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_stat (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, globus_byte_t **stat_buffer, globus_size_t *stat_buffer_length, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get information about a file or directory from a FTP server. </p>
<p> This function requests the STAT listing of a file or directory from an FTP server. </p>
<p> When the STAT request is completed or aborted, the complete_callback will be invoked with the final status of the operation. If the callback is returns without an error, the STAT fact string will be stored in the globus_byte_t * pointed to by the stat_buffer parameter to this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL of a file or directory to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>stat_buffer</i> A pointer to a globus_byte_t * to be allocated and filled with the STAT listing of the file, if it exists. Otherwise, the value pointed to by it is undefined. It is up to the user to free this memory.<br />
 <i>stat_buffer_length</i> A pointer to a globus_size_t to be filled with the length of the data in stat_buffer.<br />
 <i>complete_callback</i> Callback to be invoked once the STAT command is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> stat_buffer is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> stat_buffer_length is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_symlink (<code>globus_ftp_client_handle_t</code> *u_handle, const char *source_url, const char *link_url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Create a symbolic link on the FTP server. </p>
<p> This function creates a symbolic link on the FTP server pointing to a given path. Note that this function does not link files between FTP servers and that the host:port part of the link url is ignored. </p>
<p> When the response to the symlink request has been received the complete_callback will be invoked with the result of the move operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the move operation.<br />
 <i>source_url</i> The URL for the symbolic link to create.<br />
 <i>link_url</i> The URL for the target of the link. The host:port part of this URL is ignored.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the symlink is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> source_url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> source_url cannot be parsed</p>
<dt>&bull;</p>
<dd> source_url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_third_party_transfer (<code>globus_ftp_client_handle_t</code> *handle, const char *source_url, <code>globus_ftp_client_operationattr_t</code> *source_attr, const char *dest_url, <code>globus_ftp_client_operationattr_t</code> *dest_attr, <code>globus_ftp_client_restart_marker_t</code> *restart, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Transfer a file between two FTP servers. </p>
<p> This function starts up a third-party file transfer between FTP server. This function returns immediately. </p>
<p> When the transfer is completed or if the transfer is aborted, the complete_callback will be invoked with the final status of the transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> An FTP Client handle to use for the get operation.<br />
 <i>source_url</i> The URL to transfer. The URL may be an ftp or gsiftp URL.<br />
 <i>source_attr</i> Attributes for the souce URL.<br />
 <i>dest_url</i> The destination URL for the transfer. The URL may be an ftp or gsiftp URL.<br />
 <i>dest_attr</i> Attributes for the destination URL.<br />
 <i>restart</i> Pointer to a restart marker.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;put&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The source_attr and dest_attr MUST be compatible. For example, the MODE and TYPE should match for both the source and destination.</dl>
<h3>globus_result_t globus_ftp_client_utime (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, const struct tm *utime_time, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Set the modification time on a file. </p>
<p> This function changes file modification time </p>
<p> When the response to the modification time request has been received the complete_callback will be invoked with the result of the operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the change operation.<br />
 <i>url</i> The URL of the file to modify group membership.<br />
 <i>utime_time</i> The absolute time to which the file&#8217;s modification time should be set.<br />
 <i>attr</i> Attributes for this operation.<br />
 <i>complete_callback</i> Callback to be invoked once the change is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<h3>globus_result_t globus_ftp_client_verbose_list (<code>globus_ftp_client_handle_t</code> *u_handle, const char *url, <code>globus_ftp_client_operationattr_t</code> *attr, <code>globus_ftp_client_complete_callback_t</code>complete_callback, void *callback_arg)</h3>
<p> Get a file listing from an FTP server. </p>
<p> This function starts a &#8216;LIST&#8217; transfer from an FTP server. If this function returns GLOBUS_SUCCESS, then the user may immediately begin calling <code>globus_ftp_client_register_read()</code> to retrieve the data associated with this listing. </p>
<p> When all of the data associated with the listing is retrieved, and all of the data callbacks have been called, or if the list request is aborted, the complete_callback will be invoked with the final status of the list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>u_handle</i> An FTP Client handle to use for the list operation.<br />
 <i>url</i> The URL to list. The URL may be an ftp or gsiftp URL.<br />
 <i>attr</i> Attributes for this file transfer.<br />
 <i>complete_callback</i> Callback to be invoked once the &#8216;list&#8217; is completed.<br />
 <i>callback_arg</i> Argument to be passed to the complete_callback.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns an error when any of these conditions are true:</p>
<dl>
<dt>&bull;</p>
<dd> handle is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> url cannot be parsed</p>
<dt>&bull;</p>
<dd> url is not a ftp or gsiftp url</p>
<dt>&bull;</p>
<dd> complete_callback is GLOBUS_NULL</p>
<dt>&bull;</p>
<dd> handle already has an operation in progress</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_register_read()</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBE">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbBH">Function Documentation</a></p>
<dd>
<dt><a href="#lbCP">Author</a></p>
<dd></dl>
