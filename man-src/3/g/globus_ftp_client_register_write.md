---
title: "globus_ftp_client_register_write(3)"
name: "globus_ftp_client_register_write"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_register_write/"
description: "Reading and Writing Data –"
---

<h2 class="name">NAME</h2>
<p> Reading and Writing Data &#8211; </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_ftp_client_data_callback_t</code> )(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_register_read</code> (<code>globus_ftp_client_handle_t</code> *handle, globus_byte_t *buffer, globus_size_t buffer_length, <code>globus_ftp_client_data_callback_t</code> callback, void *callback_arg) </p>
<p> globus_result_t <code>globus_ftp_client_register_write</code> (<code>globus_ftp_client_handle_t</code> *handle, globus_byte_t *buffer, globus_size_t buffer_length, globus_off_t offset, globus_bool_t eof, <code>globus_ftp_client_data_callback_t</code> callback, void *callback_arg) </p>
<h2>Detailed Description</h2>
<p> Certain FTP client operations require the user to supply buffers for reading or writing data to an FTP server. These operations are <code>globus_ftp_client_get()</code>, <code>globus_ftp_client_partial_get()</code>, <code>globus_ftp_client_put()</code>, <code>globus_ftp_client_partial_put()</code>, <code>globus_ftp_client_list()</code>, <code>globus_ftp_client_machine_list()</code>, <code>globus_ftp_client_recursive_list()</code>, and <code>globus_ftp_client_verbose_list()</code>. </p>
<p> When doing these operations, the user must pass data buffers to the FTP Client library. Data is read or written directly from the data buffers, without any internal copies being done. </p>
<p> The functions in this section of the manual may be called as soon as the operation function has returned. Multiple data blocks may be registered with the FTP Client Library at once, and may be sent in parallel to or from the FTP server if the GridFTP protocol extensions are being used.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_client_data_callback_t)(void *user_arg, <code>globus_ftp_client_handle_t</code> *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof)</h3>
<p> Data Callback. </p>
<p> Each read or write operation in the FTP Client library is asynchronous. A callback of this type is passed to each of the data operation function calls to let the user know when the data block has been processed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_arg</i> The user_arg parameter passed to the read or write function.<br />
 <i>handle</i> The handle on which the data block operation was done.<br />
 <i>error</i> A Globus error object indicating any problem which occurred processing this data block, or or GLOBUS_SUCCESS if the operation completed successfully.<br />
 <i>buffer</i> The data buffer passed to the original read or write call.<br />
 <i>length</i> The amount of data in the data buffer. When reading data, this may be smaller than original buffer&#8217;s length.<br />
 <i>offset</i> The offset into the file which this data block contains.<br />
 <i>eof</i> GLOBUS_TRUE if EOF has been reached on this data transfer, GLOBUS_FALSE otherwise. This may be set to GLOBUS_TRUE for multiple callbacks.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_register_read (<code>globus_ftp_client_handle_t</code> *handle, globus_byte_t *buffer, globus_size_tbuffer_length, <code>globus_ftp_client_data_callback_t</code>callback, void *callback_arg)</h3>
<p> Register a data buffer to handle a part of the FTP data transfer. </p>
<p> The data buffer will be associated with the current get being performed on this client handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP Client handle which contains state information about the get operation.<br />
 <i>buffer</i> A user-supplied buffer into which data from the FTP server will be stored.<br />
 <i>buffer_length</i> The maximum amount of data that can be stored into the buffer.<br />
 <i>callback</i> The function to be called once the data has been read.<br />
 <i>callback_arg</i> Argument passed to the callback function</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_operationattr_set_read_all()</code></dl>
<h3>globus_result_t globus_ftp_client_register_write (<code>globus_ftp_client_handle_t</code> *handle, globus_byte_t *buffer, globus_size_tbuffer_length, globus_off_toffset, globus_bool_teof, <code>globus_ftp_client_data_callback_t</code>callback, void *callback_arg)</h3>
<p> Register a data buffer to handle a part of the FTP data transfer. </p>
<p> The data buffer will be associated with the current &#8216;put&#8217; being performed on this client handle. Multiple data buffers may be registered on a handle at once. There is no guaranteed ordering of the data callbacks in extended block mode. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP Client handle which contains state information about the put operation.<br />
 <i>buffer</i> A user-supplied buffer containing the data to write to the server.<br />
 <i>buffer_length</i> The size of the buffer to be written.<br />
 <i>offset</i> The offset of the buffer to be written. In extended-block mode, the data does not need to be sent in order. In stream mode (the default), data must be sent in sequential order. The behavior is undefined if multiple writes overlap.<br />
 <i>eof</i><br />
 <i>callback</i> The function to be called once the data has been written.<br />
 <i>callback_arg</i> Argument passed to the callback function</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
