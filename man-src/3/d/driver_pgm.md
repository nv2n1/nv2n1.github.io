---
title: "driver_pgm(3)"
name: "driver_pgm"
section: "3"
letter: "d"
url: "/docs/linux/man/3-driver_pgm/"
description: "Driver Programming –"
---

<h2 class="name">NAME</h2>
<p> Driver Programming &#8211; </p>
<p> The set of interface functions that the driver author must implement to create a driver and the functions to assist in the creation.</p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_xio_driver_callback_t</code> )(globus_xio_operation_t op, globus_result_t result, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_driver_data_callback_t</code> )(globus_xio_operation_t op, globus_result_t result, globus_size_t nbytes, void *user_arg) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_init_t</code> )(void **out_driver_attr) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_copy_t</code> )(void **dst, void *src) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_destroy_t</code> )(void *driver_attr) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_cntl_t</code> )(void *attr, int cmd, va_list ap) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_init_t</code> )(void *driver_attr, const globus_xio_contact_t *contact_info, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_destroy_t</code> )(void *driver_server) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_accept_t</code> )(void *driver_server, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_cntl_t</code> )(void *driver_server, int cmd, va_list ap) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_link_destroy_t</code> )(void *driver_link) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_transform_open_t</code> )(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_transport_open_t</code> )(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_handle_cntl_t</code> )(void *handle, int cmd, va_list ap) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_close_t</code> )(void *driver_handle, void *driver_attr, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_read_t</code> )(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_write_t</code> )(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_driver_handle_cntl</code> (globus_xio_driver_handle_t handle, globus_xio_driver_t driver, int cmd,&#8230;) </p>
<p> void <code>globus_xio_driver_finished_accept</code> (globus_xio_operation_t op, void *driver_link, globus_result_t result) </p>
<p> globus_result_t <code>globus_xio_driver_pass_open</code> (globus_xio_operation_t op, const globus_xio_contact_t *contact_info, <code>globus_xio_driver_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_open</code> (void *driver_handle, globus_xio_operation_t op, globus_result_t result) </p>
<p> globus_result_t <code>globus_xio_driver_operation_create</code> (globus_xio_operation_t *operation, globus_xio_driver_handle_t handle) </p>
<p> globus_bool_t <code>globus_xio_driver_operation_is_blocking</code> (globus_xio_operation_t operation) </p>
<p> globus_result_t <code>globus_xio_driver_pass_close</code> (globus_xio_operation_t op, <code>globus_xio_driver_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_close</code> (globus_xio_operation_t op, globus_result_t result) </p>
<p> globus_result_t <code>globus_xio_driver_pass_read</code> (globus_xio_operation_t op, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t wait_for, <code>globus_xio_driver_data_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_read</code> (globus_xio_operation_t op, globus_result_t result, globus_size_t nread) </p>
<p> void <code>globus_xio_driver_set_eof_received</code> (globus_xio_operation_t op) </p>
<p> globus_bool_t <code>globus_xio_driver_eof_received</code> (globus_xio_operation_t op) </p>
<p> globus_result_t <code>globus_xio_driver_pass_write</code> (globus_xio_operation_t op, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t wait_for, <code>globus_xio_driver_data_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_write</code> (globus_xio_operation_t op, globus_result_t result, globus_size_t nwritten) </p>
<p> globus_result_t <code>globus_xio_driver_merge_operation</code> (globus_xio_operation_t top_op, globus_xio_operation_t bottom_op) </p>
<h2>Detailed Description</h2>
<p> The set of interface functions that the driver author must implement to create a driver and the functions to assist in the creation. </p>
<p> Driver attribute functions </p>
<p> If the driver wishes to provide driver specific attributes to the user it must implement the following functions: </p>
<p> globus_xio_driver_attr_init_t globus_xio_driver_attr_copy_t globus_xio_driver_attr_cntl_t globus_xio_driver_attr_destroy_t</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* <code>globus_xio_driver_callback_t</code>)(globus_xio_operation_t op, globus_result_t result, void *user_arg)</h3>
<p> callback interface </p>
<p> This is the function signature of callbacks for the globus_xio_driver_open/close(). <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure associated with the open or the close requested operation. The driver should call the appropriate finished operation to clean up this structure.<br />
 <i>result</i> The result of the requested data operation<br />
 <i>user_arg</i> The user pointer that is threaded through to the callback.</dl>
<h3>typedef void(* <code>globus_xio_driver_data_callback_t</code>)(globus_xio_operation_t op, globus_result_t result, globus_size_t nbytes, void *user_arg)</h3>
<p> Data Callback interface </p>
<p> This is the function signature of read and write operation callbacks. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure associated with the read or write operation request. The driver should call the approriate finished operation when it receives this operation.<br />
 <i>result</i> The result of the requested data operation<br />
 <i>nbytes</i> the number of bytes read or written<br />
 <i>user_arg</i> The user pointer that is threaded through to the callback.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_attr_init_t</code>)(void **out_driver_attr)</h3>
<p> Create a driver specific attribute. The driver should implement this function to create a driver specific attribute and return it via the out_attr parameter.</p>
<h3>typedef globus_result_t(* <code>globus_xio_driver_attr_copy_t</code>)(void **dst, void *src)</h3>
<p> Copy a driver attr. When this function is called the driver will create a copy of the attr in parameter src and place it in the parameter dst.</p>
<h3>typedef globus_result_t(* <code>globus_xio_driver_attr_destroy_t</code>)(void *driver_attr)</h3>
<p> Destroy the driver attr. Clean up all resources associate with the attr.</p>
<h3>typedef globus_result_t(* <code>globus_xio_driver_attr_cntl_t</code>)(void *attr, int cmd, va_list ap)</h3>
<p> get or set information in an attr. The cmd parameter determines what functionality the user is requesting. The driver is resonsible for providing documentation to the user on all the possible values that cmd can be. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_attr</i> The driver specific attr, created by globus_xio_driver_attr_init_t.<br />
 <i>cmd</i> An integer representing what functionality the user is requesting.<br />
 <i>ap</i> variable arguments. These are determined by the driver and the value of cmd.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_server_init_t</code>)(void *driver_attr, const globus_xio_contact_t *contact_info, globus_xio_operation_t op)</h3>
<p> Initialize a server object. The driver developer should implement this function if their driver handles server operations (pasive opens). In the tcp driver this function should create a listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> An op which should be passed to globus_xio_driver_server_created. Note, that unlike most operations, the server is created from the bottom of the stack to the top.<br />
 <i>contact_info</i> This the contact info for the stack below this driver. (entries will always be NULL for the transport driver)<br />
 <i>driver_attr</i> A server attr if the user specified any driver specific attributes. This may be NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returning GLOBUS_SUCCESS for this means that ` globus_xio_driver_pass_server_init returned success and the driver&#8217;s server was successfully initialized.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_server_destroy_t</code>)(void *driver_server)</h3>
<p> destroy a server. When this function is called the driver should free up all resources associated with a server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The server that the driver should clean up.<br />
 <i>driver_server</i> The reference to the iunternal server that is being declaired invaild with this function call.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_server_accept_t</code>)(void *driver_server, globus_xio_operation_t op)</h3>
<p> Accept a server connection. The driver developer should implement this function if their driver handles server operations. Once the accept operation completes, the connection is established. The user still has an opertunity to open the link or destroy it. They can query the link for additional information on which to base the decision to open. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_server</i> The server object from which the link connection will be accepted.<br />
 <i>op</i> The requested operation. When the driver is finished acepting the server connection it uses this structure to signal globus_xio that it has completed the operation.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_server_cntl_t</code>)(void *driver_server, int cmd, va_list ap)</h3>
<p> Query a server for information. This function allows a user to request information from a driver specific server handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_server</i> the server handle.<br />
 <i>cmd</i> An integer telling the driver what operation to preform on this server handle.<br />
 <i>ap</i> variable args.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_link_destroy_t</code>)(void *driver_link)</h3>
<p> destroy a link The driver should clean up all resources associated with the link when this function is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_link</i> The link to be destroyed.</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_transform_open_t</code>)(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op)</h3>
<p> Open a handle </p>
<p> This is called when a user requests to open a handle. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_link</i> Comes from server accept. Used to link an accepted connection to an xio handle. xio will destroy this object upon the return of this interface call.<br />
 <i>driver_attr</i> A attribute describing how to open. This points to a piece of memory created by the globus_xio_driver_driver_attr_init_t interface funstion.<br />
 <i>contact_info</i> Contains information about the requested resource. Its members may all be null (especially when link is not null). XIO will destroy this contact info upon return from the interface function<br />
 <i>op</i> The requested operation. When the driver is finished opening the handle it uses this structure to signal globus_xio that it has completed the operation requested. It does this by calling <code>globus_xio_driver_finished_open()</code></dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_transport_open_t</code>)(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op)</h3>
<p> transport open</p>
<h3>typedef globus_result_t(* <code>globus_xio_driver_handle_cntl_t</code>)(void *handle, int cmd, va_list ap)</h3>
<p> this call *must* return an GLOBUS_XIO_ERROR_COMMAND error for unsupported command numbers. (use GlobusXIOErrorInvalidCommand(cmd)) </p>
<p> Drivers that have reason to support the commands listed at <code>globus_xio_handle_cmd_t</code> should accept the xio generic cmd numbers and their driver specific command number. Do NOT implement those handle cntls unless you really are the definitive source.</p>
<h3>typedef globus_result_t(* <code>globus_xio_driver_close_t</code>)(void *driver_handle, void *driver_attr, globus_xio_operation_t op)</h3>
<p> Close an open handle </p>
<p> This is called when a user requests to close a handle. The driver implemntor should clean up all resources connected to there driver handle when this function is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_specific_handle</i> The driver handle to be closed.<br />
 <i>driver_attr</i> A driver specific attr which may be used to alter how a close is performed (e,g, caching drivers)<br />
 <i>op</i> The requested operation. When the driver is finished closing the handle it uses this structure to signal globus_xio that it has completed the operation requested. It does this by calling <code>globus_xio_driver_finished_close()</code></dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_read_t</code>)(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op)</h3>
<p> Read data from an open handle. This function is called when the user requests to read data from a handle. The driver author shall implement all code needed to for there driver to complete a read operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_handle</i> The driver handle from which data should be read.<br />
 <i>iovec</i> An io vector pointing to the buffers to be read into.<br />
 <i>iovec_count</i> The number if entries in the io vector.<br />
 <i>op</i> The requested operation. When the driver is finished fullfilling the requested read operation it must use this structure to signal globus_xio that the operation is completed. This is done by calling globus_xio_driver_finished_operation()..</dl>
<h3>typedef globus_result_t(* <code>globus_xio_driver_write_t</code>)(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op)</h3>
<p> Write data from an open handle. This function is called when the user requests to write data to a handle. The driver author shall implement all code needed to for there driver to complete write operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_handle</i> The driver handle to which data should be writen.<br />
 <i>iovec</i> An io vector pointing to the buffers to be written.<br />
 <i>iovec_count</i> The number if entries in the io vector.<br />
 <i>op</i> The requested operation. When the driver is finished fullfilling the requested read operation it must use this structure to signal globus_xio that the operation is completed. This is done by calling globus_xio_driver_finished_operation()..</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_driver_handle_cntl (globus_xio_driver_handle_t handle, globus_xio_driver_t driver, int cmd, &#8230;)</h3>
<p> Touch driver specific information in a handle object. pass the driver to control a specific driver pass NULL for driver for XIO specific cntls pass GLOBUS_XIO_QUERY for driver to try each driver (below current) in order </p>
<p> References globus_xio_driver_handle_cntl().</p>
<h3>void globus_xio_driver_finished_accept (globus_xio_operation_t op, void * driver_link, globus_result_t result)</h3>
<p> Driver API finished accept. This function should be called to signal globus_xio that it has completed the accept operation requested of it. It will free up resources associated with the accept_op and potientially cause xio to pop the signal up the driver stack. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The requested accept operation that has completed.<br />
 <i>driver_link</i> This is the initialized driver link that is that will be passed to the open interface when this handle is opened.<br />
 <i>result</i> Return status of the completed operation</dl>
<p> References globus_xio_driver_finished_accept().</p>
<h3>globus_result_t globus_xio_driver_pass_open (globus_xio_operation_t op, const globus_xio_contact_t * contact_info, <code>globus_xio_driver_callback_t</code> cb, void * user_arg)</h3>
<p> Driver API Open </p>
<p> This function will pass an open request down the driver stack. Upon completion of the open operation globus_xio will call the <i>cb</i> function, at which point the handle structure will be intialized and available for use. </p>
<p> As soon as the function returns the handle is valid for creating other operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation from which the handle will be established. This parameter is used to determine what drivers are in the stack and other such information.<br />
 <i>contact_info</i> The contact info describing the resource the driver below should open. This will normally be the same contact info that was passed in on the open interface.<br />
 <i>cb</i> The function to be called wehn the open operation is complete.<br />
 <i>user_arg</i> a user pointer that will be threaded through to the callback.</dl>
<p> References globus_xio_driver_pass_open().</p>
<h3>void globus_xio_driver_finished_open (void * driver_handle, globus_xio_operation_t op, globus_result_t result)</h3>
<p> Driver API finished open </p>
<p> This function should be called to signal globus_xio that it has completed the open operation requested of it. It will free up resources associated with the op and potientially cause xio to pop the signal up the driver stack. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_handle</i> The driver specific handle pointer that will be passed to future interface funstion calls.<br />
 <i>op</i> The requested open operation that has completed.<br />
 <i>result</i> Return status of the completed operation</dl>
<p> References globus_xio_driver_finished_open().</p>
<h3>globus_result_t globus_xio_driver_operation_create (globus_xio_operation_t * operation, globus_xio_driver_handle_t handle)</h3>
<p> Driver API Create Operation </p>
<p> This function will create an operation from an initialized handle This operation can then be used for io operations related to the handle that created them. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>operation</i> The operation to be created. When this function returns this structure will be populated and available for use for the driver.<br />
 <i>handle</i> The initialized handle representing the user handle from which the operation will be created.</dl>
<p> References globus_xio_driver_operation_create().</p>
<h3>globus_bool_t globus_xio_driver_operation_is_blocking (globus_xio_operation_t operation)</h3>
<p> Is Operation blocking. If the operation is blocking the driver developer may be able to make certian optimizations. The function returns true if the given operation was created via a user call to a blocking funciton.</p>
<h3>globus_result_t globus_xio_driver_pass_close (globus_xio_operation_t op, <code>globus_xio_driver_callback_t</code> cb, void * user_arg)</h3>
<p> Driver API Close </p>
<p> This function will pass a close request down the driver stack. Upon completion of the close operation globus_xio will call the funciton pointed to by the cb argument. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation to pass along the driver stack for closing.<br />
 <i>cb</i> A pointer to the function to be called once all drivers lower in the stack have closed.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.</dl>
<p> References globus_xio_driver_pass_close().</p>
<h3>void globus_xio_driver_finished_close (globus_xio_operation_t op, globus_result_t result)</h3>
<p> Driver API finished_close </p>
<p> The driver calls this function after completing a close operation on a driver_handle. Once this function returns the driver_handle is no longer valid. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The close operation that has completed.<br />
 <i>result</i> Return status of the completed operation</dl>
<p> References globus_xio_driver_finished_close().</p>
<h3>globus_result_t globus_xio_driver_pass_read (globus_xio_operation_t op, globus_xio_iovec_t * iovec, int iovec_count, globus_size_t wait_for, <code>globus_xio_driver_data_callback_t</code> cb, void * user_arg)</h3>
<p> Driver read </p>
<p> This function passes a read operation down the driver stack. After this function is called the op structure is no longer valid. However when the driver stack finishes servicing the read request it will pass a new operation structure in the funciton pointed to by cb. Finishe read can be called on the new operation received. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing this requested io operation.<br />
 <i>iovec</i> A pointer to the array of iovecs.<br />
 <i>iovec_count</i> The number of iovecs in the array.<br />
 <i>wait_for</i> The minimum number of bytes to read before returning&#8230; if a driver has no specifc requirement, he should use the user&#8217;s request&#8230; available via GlobusXIOOperationMinimumRead(op)<br />
 <i>cb</i> The function to be called when the operation request is completed.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.</dl>
<p> References globus_xio_driver_pass_read().</p>
<h3>void globus_xio_driver_finished_read (globus_xio_operation_t op, globus_result_t result, globus_size_t nread)</h3>
<p> Finished Read </p>
<p> This function is called to signal globus_xio that the requested read operation has been completed. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested read operation.<br />
 <i>result</i> Return status of the completed operation<br />
 <i>nread</i> The number of bytes read</dl>
<p> References globus_xio_driver_finished_read().</p>
<h3>void globus_xio_driver_set_eof_received (globus_xio_operation_t op)</h3>
<p> EOF state manipulation </p>
<p> This function is used by drivers that allow multiple outstanding reads at a time. It can only be called on behalf of a read operation (while in the read interface call or the pass_read callback). </p>
<p> Typical use for this would be to hold a driver specific lock and call this when an internal eof has been received. The read operation this is called on behalf of must be finished with an eof error or the results are undefined. </p>
<p> In general, you should not have an eof flag in your driver. Use this call and <code>globus_xio_driver_eof_received()</code> instead. This is necessary to support xio&#8217;s automatic eof resetting. If your driver absolutely can not be read after an eof has been set, then you will need your own eof flag. </p>
<p> This call will typically only be used just before a finished_read() call. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested read operation.</dl>
<p> References globus_xio_driver_set_eof_received().</p>
<h3>globus_bool_t globus_xio_driver_eof_received (globus_xio_operation_t op)</h3>
<p> EOF state checking </p>
<p> This function is used by drivers that allow multiple outstanding reads at a time. It can only be called on behalf of a read operation (while in the read interface call or the pass_read callback). </p>
<p> Typical use for this would be to hold a driver specific lock (the same one used when calling <code>globus_xio_driver_set_eof_received()</code>) and call this to see if an eof has been received. If so, the operation should immediately be finished with an eof error (do not _return_ an eof error). </p>
<p> This call will typically only be used in the read interface call. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested read operation.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_TRUE if eof received, GLOBUS_FALSE otherwise.</dl>
<p> References globus_xio_driver_eof_received().</p>
<h3>globus_result_t globus_xio_driver_pass_write (globus_xio_operation_t op, globus_xio_iovec_t * iovec, int iovec_count, globus_size_t wait_for, <code>globus_xio_driver_data_callback_t</code> cb, void * user_arg)</h3>
<p> Driver write </p>
<p> This function passes a write operation down the driver stack. After this function is called the op structure is no longer valid. However when the driver stack finishes servicing the write request it will pass a new operation structure in the funciton pointed to by cb. Finished write can be called on the new operation received. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing this requested io operation.<br />
 <i>iovec</i> A pointer to the array of iovecs.<br />
 <i>iovec_count</i> The number of iovecs in the array.<br />
 <i>wait_for</i> The minimum number of bytes to write before returning&#8230; if a driver has no specifc requirement, he should use the user&#8217;s request&#8230; available via GlobusXIOOperationMinimumWrite(op)<br />
 <i>cb</i> The function to be called when the operation request is completed.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.</dl>
<p> References globus_xio_driver_pass_write().</p>
<h3>void globus_xio_driver_finished_write (globus_xio_operation_t op, globus_result_t result, globus_size_t nwritten)</h3>
<p> Finished Write </p>
<p> This function is called to signal globus_xio that the requested write operation has been completed. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested write operation.<br />
 <i>result</i> Return status of the completed operation<br />
 <i>nwritten</i> The number of bytes written</dl>
<p> References globus_xio_driver_finished_write().</p>
<h3>globus_result_t globus_xio_driver_merge_operation (globus_xio_operation_t top_op, globus_xio_operation_t bottom_op)</h3>
<p> Finishes an operation and merge two op structures. (XXX not implemented yet) </p>
<p> This function will join to operations together and signal globus_xio that it has completed. This is an advanced function. Most drivers will not require its use. This function takes an operation that was created by this driver and passed on to drivers lower on the stack and an operation that came in on the interface function (that has seen the top half of the stack) and joins them together. The purpose of this function is to join data descriptors that were prestaged and cached with those that have later come in at the users request. See the read ahead doc for more information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>top_op</i> The operation that has seen the top part of the driver stack.<br />
 <i>bottom_op</i> The operation that has seen the bottom part of the driver stack.</dl>
<p> (result is always success in this case.. if there is an error, use the other finish() call)</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAX">Function Documentation</a></p>
<dd>
<dt><a href="#lbBN">Author</a></p>
<dd></dl>
