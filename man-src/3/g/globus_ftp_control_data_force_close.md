---
title: "globus_ftp_control_data_force_close(3)"
name: "globus_ftp_control_data_force_close"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_control_data_force_close/"
description: "GridFTP Data Connections –"
---

<h2 class="name">NAME</h2>
<p> GridFTP Data Connections &#8211; </p>
<p> Data Connections.</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_control_data_connect_read</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_connect_callback_t callback, void *user_arg)<br />
 <i>Create an incoming FTP data connection. </i><br />
 globus_result_t <code>globus_ftp_control_data_set_interface</code> (globus_ftp_control_handle_t *handle, const char *interface_addr)<br />
 <i>Create an outgoing FTP data connection. </i><br />
 globus_result_t <code>globus_ftp_control_data_connect_write</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_connect_callback_t callback, void *user_arg)<br />
 <i>Create an outgoing FTP data connection. </i><br />
 globus_result_t <code>globus_ftp_control_data_add_channels</code> (globus_ftp_control_handle_t *handle, unsigned int num_channels, unsigned int stripe_ndx)<br />
 <i>Add data channels. </i><br />
 globus_result_t <code>globus_ftp_control_data_send_eof</code> (globus_ftp_control_handle_t *handle, int count[], int array_size, globus_bool_t eof_message, <code>globus_ftp_control_callback_t</code> cb, void *user_arg)<br />
 <i>Send EOF. </i><br />
 globus_result_t <code>globus_ftp_control_data_remove_channels</code> (globus_ftp_control_handle_t *handle, unsigned int num_channels, unsigned int stripe_ndx)<br />
 <i>Remove Data Channels. </i><br />
 globus_result_t <code>globus_ftp_control_data_query_channels</code> (globus_ftp_control_handle_t *handle, unsigned int *num_channels, unsigned int stripe_ndx)<br />
 <i>Number of data channels. </i><br />
 globus_result_t <code>globus_ftp_control_data_get_total_data_channels</code> (globus_ftp_control_handle_t *handle, unsigned int *num_channels, unsigned int stripe_ndx)<br />
 <i>Get Total Data Channels For a Stripe. </i><br />
 globus_result_t <code>globus_ftp_control_local_send_eof</code> (globus_ftp_control_handle_t *handle, globus_bool_t send_eof)<br />
 <i>Enable or disable automatic EOF handling. </i><br />
 globus_result_t <code>globus_ftp_control_local_parallelism</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_parallelism_t</code> *parallelism)<br />
 <i>Set control handle parallelism. </i><br />
 globus_result_t <code>globus_ftp_control_local_pasv</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *address)<br />
 <i>Create a passive socket. </i><br />
 globus_result_t <code>globus_ftp_control_local_spas</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t addresses[], unsigned int num_addresses)<br />
 <i>Create multiple passive sockets. </i><br />
 globus_result_t <code>globus_ftp_control_local_port</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *address)<br />
 <i>Set remote data address. </i><br />
 globus_result_t <code>globus_ftp_control_local_spor</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t addresses[], unsigned int num_addresses)<br />
 <i>Set remote data addresses. </i><br />
 globus_result_t <code>globus_ftp_control_local_type</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_type_t</code> type, int form_code)<br />
 <i>Set control handle TYPE value. </i><br />
 globus_result_t <code>globus_ftp_control_local_mode</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_mode_t</code> mode)<br />
 <i>Set data handle mode. </i><br />
 globus_result_t <code>globus_ftp_control_set_force_order</code> (globus_ftp_control_handle_t *handle, globus_bool_t order_data, globus_off_t starting_offset)<br />
 <i>Set data handle to return read mode E data in order. </i><br />
 globus_result_t <code>globus_ftp_control_local_tcp_buffer</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_tcpbuffer_t</code> *tcp_buffer)<br />
 <i>Set data handle TCP buffer size. </i><br />
 globus_result_t <code>globus_ftp_control_local_dcau</code> (globus_ftp_control_handle_t *handle, const <code>globus_ftp_control_dcau_t</code> *dcau, gss_cred_id_t delegated_credential_handle)<br />
 <i>Set data channel DCAU. </i><br />
 globus_result_t <code>globus_ftp_control_local_pbsz</code> (globus_ftp_control_handle_t *handle, unsigned long bufsize)<br />
 <i>Set data channel protection buffer size. </i><br />
 globus_result_t <code>globus_ftp_control_get_pbsz</code> (globus_ftp_control_handle_t *handle, unsigned long *bufsize)<br />
 <i>Get data channel protection buffer size. </i><br />
 globus_result_t <code>globus_ftp_control_local_stru</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_structure_t</code> structure)<br />
 <i>Set data channel structure. </i><br />
 globus_result_t <code>globus_ftp_control_data_write</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Write data to data connections. </i><br />
 globus_result_t <code>globus_ftp_control_data_read</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t max_length, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Read data from data connections. </i><br />
 globus_result_t <code>globus_ftp_control_local_layout</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_layout_t</code> *layout, globus_size_t data_size)<br />
 <i>Set data layout. </i><br />
 globus_result_t <code>globus_ftp_control_create_data_info</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_write_info_t *data_info, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Create a globus_ftp_control_data_write_info_t structure. </i><br />
 globus_result_t <code>globus_ftp_control_release_data_info</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_write_info_t *data_info)<br />
 <i>Release a data_info structure. </i><br />
 globus_result_t <code>globus_ftp_control_data_write_stripe</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, int stripe_ndx, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Write FTP data to a stripe. </i><br />
 globus_result_t <code>globus_X_ftp_control_data_write_stripe</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, int stripe_ndx, globus_ftp_control_data_write_info_t *data_info)<br />
 <i>Write data to a stripe from an enqueue callback. </i><br />
 globus_result_t <code>globus_ftp_control_data_force_close</code> (globus_ftp_control_handle_t *control_handle, <code>globus_ftp_control_callback_t</code> close_callback_func, void *close_arg)<br />
 <i>Close data connections. </i></p>
<h2>Detailed Description</h2>
<p> Data Connections. </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_control_create_data_info (globus_ftp_control_handle_t *handle, globus_ftp_control_data_write_info_t *data_info, globus_byte_t *buffer, globus_size_tlength, globus_off_toffset, globus_bool_teof, <code>globus_ftp_control_data_callback_t</code>callback, void *callback_arg)</h3>
<p> Create a globus_ftp_control_data_write_info_t structure. This function populates a globus_ftp_control_data_callback_t structure with valid information. This structure provides the user a way to register several data writes with a single callback. This is quite useful to the writer of enqueue functions. It allows a single call to <code>globus_ftp_control_data_write()</code> to be broken up into many writes, potentially on different stripes, and for a single callback to be called when all are finished. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>data_info</i> The globus_ftp_control_data_write_info_t structure to be released.<br />
 <i>buffer</i> The pointer to the user buffer that will be passed to the callback argument when there are zero references to data_info. This is intended to be the start of all the data the user intends to write using <code>globus_ftp_control_data_write_stripe()</code>, but it does not have to be.<br />
 <i>length</i> The length of the memory segment pointed to by the argument buffer.<br />
 <i>offset</i> The file offset of the data segment specified.<br />
 <i>eof</i> This should be set to true if the user plans on registering eof on the data_info structure.<br />
 <i>callback</i> The user function to be called when all references to data_info are released. This occurs after all data registered for write from globus_ftp_control_data_write_stripe have occurred and the user calls <code>globus_ftp_control_release_data_info()</code>. The callback is passed all of the arguments passed to this function with the exception of data_info.<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<h3>globus_result_t globus_ftp_control_data_add_channels (globus_ftp_control_handle_t *handle, unsigned intnum_channels, unsigned intstripe_ndx)</h3>
<p> Add data channels. Opens additional data channels (connections) to the host identified by the stripe parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. This handle is used to determine the host corresponding to the stripe number and to store information about any channels added by this function.<br />
 <i>num_channels</i> The number of additional channels to add.<br />
 <i>stripe_ndx</i> A integer identifying the stripe to add channels too. In the case of non-striped transfer this parameter will be ignored.</dl>
<h3>globus_result_t globus_ftp_control_data_connect_read (globus_ftp_control_handle_t *handle, globus_ftp_control_data_connect_callback_tcallback, void *user_arg)</h3>
<p> Create an incoming FTP data connection. This function will register a globus_io_{accept, connect}. Further accepts/connects are done by registering a new accept/connect in the current accept/connect callback. A call to either <code>globus_ftp_control_local_pasv()</code> or <code>globus_ftp_control_local_port()</code> needs to precede this calling this function. This function may be followed by a globus_ftp_data_read. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle which is configured to create an incoming data connection.<br />
 <i>callback</i> This callback is called when the connection occurs. This parameter may be NULL.<br />
 <i>user_arg</i> The user argument passed to the connect callback.</dl>
<h3>globus_result_t globus_ftp_control_data_connect_write (globus_ftp_control_handle_t *handle, globus_ftp_control_data_connect_callback_tcallback, void *user_arg)</h3>
<p> Create an outgoing FTP data connection. This function will register a globus_io_{accept, connect}. Further accepts/connects are done by registering a new accept/connect in the current accept/connect callback. A call to either <code>globus_ftp_control_local_pasv()</code> or <code>globus_ftp_control_local_port()</code> needs to precede this calling this function. This function may be followed by a globus_ftp_data_write. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle which is configured to create an outgoing data connection.<br />
 <i>callback</i> This callback is called when the connection occurs. This parameter may be NULL.<br />
 <i>user_arg</i> The user argument passed to the connect callback.</dl>
<h3>globus_result_t globus_ftp_control_data_force_close (globus_ftp_control_handle_t *control_handle, <code>globus_ftp_control_callback_t</code>close_callback_func, void *close_arg)</h3>
<p> Close data connections. Forces an immediate close of all data connections. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>control_handle</i> The globus_ftp_control_handle that is have its data connections closed.<br />
 <i>close_callback_func</i> A user function that will be called when the data connections are closed.<br />
 <i>close_arg</i> The user argument that will be threaded through to close_callback_func.</dl>
<h3>globus_result_t globus_ftp_control_data_get_total_data_channels (globus_ftp_control_handle_t *handle, unsigned int *num_channels, unsigned intstripe_ndx)</h3>
<p> Get Total Data Channels For a Stripe. Returns the total number of data channels used so far in the current transfer on the given stripe. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. This handle is used to determine the host corresponding to &#8216;stripe&#8217; and number of channels corresponding to that host.<br />
 <i>num_channels</i><br />
 <i>stripe_ndx</i> A integer identifying the stripe for which to return the number of channels. In the case of non-striped transfer this parameter should be zero.</dl>
<h3>globus_result_t globus_ftp_control_data_query_channels (globus_ftp_control_handle_t *handle, unsigned int *num_channels, unsigned intstripe_ndx)</h3>
<p> Number of data channels. Returns the number of currently open channels for the host identified by the stripe parameter. This number may be less then the level of parallelism specified in local_parallelism, due to the possibility that some channels have not yet connected. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. This handle is used to determine the host corresponding to &#8216;stripe&#8217; and number of channels corresponding to that host.<br />
 <i>num_channels</i><br />
 <i>stripe_ndx</i> A integer identifying the stripe for which to return the number of channels. In the case of non-striped transfer this parameter should be zero.</dl>
<h3>globus_result_t globus_ftp_control_data_read (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_tmax_length, <code>globus_ftp_control_data_callback_t</code>callback, void *callback_arg)</h3>
<p> Read data from data connections. Reads data from data connection(s) and put them in the supplied buffer. </p>
<p> This function takes the given buffer and will try to read data from the data connection(s). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>buffer</i> A user supplied buffer into which data from the data connection(s) will be written<br />
 <i>max_length</i> The maximum length of the data that can be written to the buffer<br />
 <i>callback</i> The function to be called once the data has been read<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<h3>globus_result_t globus_ftp_control_data_remove_channels (globus_ftp_control_handle_t *handle, unsigned intnum_channels, unsigned intstripe_ndx)</h3>
<p> Remove Data Channels. Removes data channels (connections) to the host identified by the stripe parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. This handle is used to determine the host corresponding to the stripe number and to update information about any channels removed by this function.<br />
 <i>num_channels</i> The number of channels to remove.<br />
 <i>stripe_ndx</i> A integer identifying the stripe to remove channels from. In the case of non-striped transfer this parameter will be ignored.</dl>
<h3>globus_result_t globus_ftp_control_data_send_eof (globus_ftp_control_handle_t *handle, intcount[], intarray_size, globus_bool_teof_message, <code>globus_ftp_control_callback_t</code>cb, void *user_arg)</h3>
<p> Send EOF. Sends an EOF message to each stripe along an open data connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. This handle contains the state for a connection.<br />
 <i>count[]</i> This array of integers should contain an integer that will be added to the current parallel data connection count on each stripe. The order of the integers corresponds to each stripe in the same order as what was returned from local_port().</dl>
<p> An EOF message must be sent to all receiving hosts in a transfer. The message contains the total number of data connections used by each stripe. Many stripes may be sending to a single receiver but only one EOF message may be sent. The count parameter allows the user to pass in the total number of data connections used by all other hosts. The local values are added to the passed in values and then sent to the receiver. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>array_size</i> The number of elements in count[].<br />
 <i>eof_message</i><br />
 <i>cb</i> The function to be called when the eof message has been called.<br />
 <i>user_arg</i> A user pointer that is threaded through to the user callback.</dl>
<h3>globus_result_t globus_ftp_control_data_set_interface (globus_ftp_control_handle_t *handle, const char *interface_addr)</h3>
<p> Create an outgoing FTP data connection. This function sets the interface that will be used to send and receive information along the data channel. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle which is configured to create an outgoing data connection.<br />
 <i>interface_addr</i></dl>
<h3>globus_result_t globus_ftp_control_data_write (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_tlength, globus_off_toffset, globus_bool_teof, <code>globus_ftp_control_data_callback_t</code>callback, void *callback_arg)</h3>
<p> Write data to data connections. Writes data from the supplied buffer to data connection(s) </p>
<p> This function writes contained in the buffer to the data channel(s). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>buffer</i> A user supplied buffer from which data will written to the data connection(s)<br />
 <i>length</i> The length of the data contained in the buffer.<br />
 <i>offset</i> The offset in the file at which the data in the buffer starts<br />
 <i>eof</i> Indicates that the buffer is that last part of a file. In the striped case this will cause a EOF block to be send to every data node involved in the transfer.<br />
 <i>callback</i> The function to be called once the data has been sent<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<h3>globus_result_t globus_ftp_control_data_write_stripe (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_tlength, globus_off_toffset, globus_bool_teof, intstripe_ndx, <code>globus_ftp_control_data_callback_t</code>callback, void *callback_arg)</h3>
<p> Write FTP data to a stripe. This function allows the user to write to a specified stripe. The stripe index relates to the order passsed into local_spor(). This function differs from <code>globus_ftp_control_data_write()</code> in that no enqueue function is needed since the user specifies the stripe on which data is written. In order to use this function the user must have a valid pointer to a globus_ftp_control_data_write_info_t structure. The data_info structure can be obtained by a call to <code>globus_ftp_control_create_data_info()</code>. Many calls to this function can be made, but only a single user callback occurs per creation of a globus_ftp_control_data_write_info_t structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>buffer</i> a pointer to the data the user wishes to send along the FTP data channels.<br />
 <i>length</i> the length of the data pointer to by the parameter buffer.<br />
 <i>offset</i> the offset into the file of the data.<br />
 <i>eof</i> A boolean stating that this will be the last chuck of data registered on the given stripe. In order to properly send an eof message the user must register an eof on every stripe.<br />
 <i>stripe_ndx</i> The index of the stripe on which the data will be sent. The index of each stripe is determined by the call to local_spas or local_spor.<br />
 <i>callback</i> The function to be called once the data has been sent<br />
 <i>callback_arg</i> User supplied argument to the callback function</dl>
<h3>globus_result_t globus_ftp_control_get_pbsz (globus_ftp_control_handle_t *handle, unsigned long *bufsize)</h3>
<p> Get data channel protection buffer size. Query the FTP control handle for the protection buffer size information. </p>
<p> This function queries the handle to determine the protection buffer size which is used by this handle. This value is used to determine how much data will be sent in each packet during a protected data transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>bufsize</i> A pointer to a parameter to store the value of the protection buffer size.</dl>
<h3>globus_result_t globus_ftp_control_local_dcau (globus_ftp_control_handle_t *handle, const <code>globus_ftp_control_dcau_t</code> *dcau, gss_cred_id_tdelegated_credential_handle)</h3>
<p> Set data channel DCAU. Update the FTP control handle with the given data channel authentication information. </p>
<p> If authentication is set to GLOBUS_FTP_CONTROL_DCAU_NONE, then protection will also be disabled for this control handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>dcau</i> A parameter specifying the data channel authentication mode. Possible values are No Authentication, Self Authentication and Subject-name authentication.<br />
 <i>delegated_credential_handle</i></dl>
<h3>globus_result_t globus_ftp_control_local_layout (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_layout_t</code> *layout, globus_size_tdata_size)</h3>
<p> Set data layout. Update the handle with the layout and the size of the data sent over the data channel. </p>
<p> This function is deprecated. The interface will be the changed to that of globus_X_ftp_control_local_layout() </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle into which to insert the layout information.<br />
 <i>layout</i> A variable containing the layout information<br />
 <i>data_size</i> The size of the data that is going to be sent. This may be needed to interpret the layout information.</dl>
<h3>globus_result_t globus_ftp_control_local_mode (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_mode_t</code>mode)</h3>
<p> Set data handle mode. Update the FTP control handle with the given mode information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>mode</i> Specifies the mode of the data connection. Possible modes are STREAM, BLOCK, EXTENDED BLOCK and COMPRESSED. Out of these only STREAM and EXTENDED BLOCK are supported in this implementation. Also, EXTENDED BLOCK is only supported in combination with the IMAGE type.</dl>
<h3>globus_result_t globus_ftp_control_local_parallelism (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_parallelism_t</code> *parallelism)</h3>
<p> Set control handle parallelism. Set the parallelism information in a FTP control handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle for which the parallelism information is to be updated<br />
 <i>parallelism</i> A structure containing parallelism information</dl>
<h3>globus_result_t globus_ftp_control_local_pasv (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *address)</h3>
<p> Create a passive socket. Create a local listening socket, bind it and return the address the socket is listening to. If there is a existing data connection it is closed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. Information about the listening socket is stored in the handle.<br />
 <i>address</i> The host IP address and port is returned through this parameter.</dl>
<h3>globus_result_t globus_ftp_control_local_pbsz (globus_ftp_control_handle_t *handle, unsigned longbufsize)</h3>
<p> Set data channel protection buffer size. Update the FTP control handle with the given protection buffer size information. </p>
<p> This function sets protection buffer size to be used by this handle. This value is used to determine how much data will be sent in each packet during a protected data transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>bufsize</i> A parameter specifying the protection buffer size value.</dl>
<h3>globus_result_t globus_ftp_control_local_port (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *address)</h3>
<p> Set remote data address. Insert the host/port information returned by a PASV on the remote host into the local FTP control handle. (close any outstanding data con) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle into which to insert the host/port information<br />
 <i>address</i> The host IP address and port</dl>
<h3>globus_result_t globus_ftp_control_local_send_eof (globus_ftp_control_handle_t *handle, globus_bool_tsend_eof)</h3>
<p> Enable or disable automatic EOF handling. Determines if the library will automatically send an EOF message in extended block mode, or if the user will have to explicitly do it by calling <code>globus_ftp_control_data_send_eof()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The ftp handle you wish to sent the send_eof attribute on.<br />
 <i>send_eof</i> A boolean representing whether or not to automatically send an EOF message.</dl>
<h3>globus_result_t globus_ftp_control_local_spas (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_taddresses[], unsigned intnum_addresses)</h3>
<p> Create multiple passive sockets. Create num_addresses local listening sockets, bind them and return the addresses the sockets are listening to. If there is a existing data connection it is closed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. Information about the listening sockets is stored in the handle.<br />
 <i>addresses</i> The host IP addresses and ports are returned through this parameter.<br />
 <i>num_addresses</i> The number of listening sockets to create</dl>
<h3>globus_result_t globus_ftp_control_local_spor (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_taddresses[], unsigned intnum_addresses)</h3>
<p> Set remote data addresses. Insert the host/port addresses returned by a SPAS on the remote host into the local FTP control handle. If there are any outstanding data connections at this point, they are closed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle into which to insert the host/port addresses<br />
 <i>addresses</i> The host IP addresses and port numbers<br />
 <i>num_addresses</i> The number of addresses</dl>
<h3>globus_result_t globus_ftp_control_local_stru (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_structure_t</code>structure)</h3>
<p> Set data channel structure. Updates the handle with information on the structure of the data being sent on the data channel. </p>
<p> This function updates the handle with the provided structure information. At this point the only structure type that is supported is the file type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>structure</i> This parameter is used to pass the structure information. Possible values are file, record and page. Only the file type is supported</dl>
<h3>globus_result_t globus_ftp_control_local_tcp_buffer (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_tcpbuffer_t</code> *tcp_buffer)</h3>
<p> Set data handle TCP buffer size. Update the FTP control handle with the given socket buffer information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>tcp_buffer</i> A pointer to the socket buffer.</dl>
<h3>globus_result_t globus_ftp_control_local_type (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_type_t</code>type, intform_code)</h3>
<p> Set control handle TYPE value. Update the FTP control handle with the given type information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>type</i> The type of the data connection. Possible values are: ASCII, EBCDIC, IMAGE and LOCAL. Currently only ASCII and IMAGE types are supported.<br />
 <i>form_code</i> The logical byte size parameter for the LOCAL type.</dl>
<h3>globus_result_t globus_ftp_control_release_data_info (globus_ftp_control_handle_t *handle, globus_ftp_control_data_write_info_t *data_info)</h3>
<p> Release a data_info structure. This function releases all memory and references created when a call to <code>globus_ftp_control_create_data_info()</code> was made. For every call to <code>globus_ftp_control_create_data_info()</code> a call to this function must be made. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>data_info</i> The globus_ftp_control_data_write_info_t structure to be released.</dl>
<h3>globus_result_t globus_ftp_control_set_force_order (globus_ftp_control_handle_t *handle, globus_bool_torder_data, globus_off_tstarting_offset)</h3>
<p> Set data handle to return read mode E data in order. Update the FTP control handle forced data order flag. Must be called before <code>globus_ftp_control_data_connect_read()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to the FTP control handle to be updated<br />
 <i>order_data</i> GLOBUS_TRUE if data must be ordered, false if not.<br />
 <i>starting_offset</i> The starting offset to expect. May not be 0 for restarted transfers.</dl>
<p> Note that this may result in slower transfers, or, if the data arrives far out of order, failed transfers.</p>
<h3>globus_result_t globus_X_ftp_control_data_write_stripe (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_tlength, globus_off_toffset, globus_bool_teof, intstripe_ndx, globus_ftp_control_data_write_info_t *data_info)</h3>
<p> Write data to a stripe from an enqueue callback. This function allows the user to register the write of ftp data on a specific stripe. This function can only be called from an enqueue function callback. This function should be used only by the implementor of an enqueue function. It should be viewed as unstable and used used only by advanced users. This is the only function in the library that the enqueue function implementor is allowed from the enqueue callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A pointer to a FTP control handle. The handle contains information about the current state of the control and data connections.<br />
 <i>buffer</i> a pointer to the data the user wishes to send along the FTP data channels.<br />
 <i>length</i> the length of the data pointer to by the parameter buffer.<br />
 <i>offset</i> the offset into the file of the data.<br />
 <i>eof</i> a boolean stating that this is the last buffer to be registered. When using the <i>X</i> version of this function the user does not need to register an eof on each stripe, the control library will take care of that internally.<br />
 <i>stripe_ndx</i> The index of the stripe on which the data will be sent. The index of each stripe is determined by the call to local_spas or local_spor.<br />
 <i>data_info</i> An opaque structure that is passed into the enqueue function and contains reference count and state information. The same data_info pointer that is passed into the enqueue function must be used for this parameter.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_control from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBJ">Author</a></p>
<dd></dl>
