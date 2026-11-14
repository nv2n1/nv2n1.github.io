---
title: "globus_ftp_client_data(3)"
name: "globus_ftp_client_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_data/"
---

<h2 class="name">NAME</h2>
 

 Reading and Writing Data - 

<h3>Typedefs</h3>

 

 
 typedef void(* <b>globus_ftp_client_data_callback_t</b> )(void *user_arg, <b>globus_ftp_client_handle_t</b> *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof) 

<h3>Functions</h3>

 

 
 globus_result_t <b>globus_ftp_client_register_read</b> (<b>globus_ftp_client_handle_t</b> *handle, globus_byte_t *buffer, globus_size_t buffer_length, <b>globus_ftp_client_data_callback_t</b> callback, void *callback_arg) 
 
 globus_result_t <b>globus_ftp_client_register_write</b> (<b>globus_ftp_client_handle_t</b> *handle, globus_byte_t *buffer, globus_size_t buffer_length, globus_off_t offset, globus_bool_t eof, <b>globus_ftp_client_data_callback_t</b> callback, void *callback_arg) 

<h2>Detailed Description</h2>

 

 Certain FTP client operations require the user to supply buffers for reading or writing data to an FTP server. These operations are <b>globus_ftp_client_get()</b>, <b>globus_ftp_client_partial_get()</b>, <b>globus_ftp_client_put()</b>, <b>globus_ftp_client_partial_put()</b>, <b>globus_ftp_client_list()</b>, <b>globus_ftp_client_machine_list()</b>, <b>globus_ftp_client_recursive_list()</b>, and <b>globus_ftp_client_verbose_list()</b>. 

 When doing these operations, the user must pass data buffers to the FTP Client library. Data is read or written directly from the data buffers, without any internal copies being done. 

 The functions in this section of the manual may be called as soon as the operation function has returned. Multiple data blocks may be registered with the FTP Client Library at once, and may be sent in parallel to or from the FTP server if the GridFTP protocol extensions are being used.

<h2>Typedef Documentation</h2>

 

<h3>typedef void(* globus_ftp_client_data_callback_t)(void *user_arg, <b>globus_ftp_client_handle_t</b> *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof)</h3>

 Data Callback. 

 Each read or write operation in the FTP Client library is asynchronous. A callback of this type is passed to each of the data operation function calls to let the user know when the data block has been processed. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>user_arg</i> The user_arg parameter passed to the read or write function. 
 <i>handle</i> The handle on which the data block operation was done. 
 <i>error</i> A Globus error object indicating any problem which occurred processing this data block, or or GLOBUS_SUCCESS if the operation completed successfully. 
 <i>buffer</i> The data buffer passed to the original read or write call. 
 <i>length</i> The amount of data in the data buffer. When reading data, this may be smaller than original buffer's length. 
 <i>offset</i> The offset into the file which this data block contains. 
 <i>eof</i> GLOBUS_TRUE if EOF has been reached on this data transfer, GLOBUS_FALSE otherwise. This may be set to GLOBUS_TRUE for multiple callbacks.</dl>
 

 

<h2>Function Documentation</h2>

 

<h3>globus_result_t globus_ftp_client_register_read (<b>globus_ftp_client_handle_t</b> *handle, globus_byte_t *buffer, globus_size_tbuffer_length, <b>globus_ftp_client_data_callback_t</b>callback, void *callback_arg)</h3>

 Register a data buffer to handle a part of the FTP data transfer. 

 The data buffer will be associated with the current get being performed on this client handle. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP Client handle which contains state information about the get operation. 
 <i>buffer</i> A user-supplied buffer into which data from the FTP server will be stored. 
 <i>buffer_length</i> The maximum amount of data that can be stored into the buffer. 
 <i>callback</i> The function to be called once the data has been read. 
 <i>callback_arg</i> Argument passed to the callback function</dl>
 

 <b>See Also:</b>
<dl>
<dt>
<dd> <b>globus_ftp_client_operationattr_set_read_all()</b></dl>
 

 

<h3>globus_result_t globus_ftp_client_register_write (<b>globus_ftp_client_handle_t</b> *handle, globus_byte_t *buffer, globus_size_tbuffer_length, globus_off_toffset, globus_bool_teof, <b>globus_ftp_client_data_callback_t</b>callback, void *callback_arg)</h3>

 Register a data buffer to handle a part of the FTP data transfer. 

 The data buffer will be associated with the current 'put' being performed on this client handle. Multiple data buffers may be registered on a handle at once. There is no guaranteed ordering of the data callbacks in extended block mode. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP Client handle which contains state information about the put operation. 
 <i>buffer</i> A user-supplied buffer containing the data to write to the server. 
 <i>buffer_length</i> The size of the buffer to be written. 
 <i>offset</i> The offset of the buffer to be written. In extended-block mode, the data does not need to be sent in order. In stream mode (the default), data must be sent in sequential order. The behavior is undefined if multiple writes overlap. 
 <i>eof</i> 
 <i>callback</i> The function to be called once the data has been written. 
 <i>callback_arg</i> Argument passed to the callback function</dl>
 

 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_ftp_client from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbAH">Function Documentation</a>
<dd>


<dt><a HREF="#lbAK">Author</a>
<dd></dl>
