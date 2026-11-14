---
title: "globus_xio_driver_pass_close(3)"
name: "globus_xio_driver_pass_close"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_driver_pass_close/"
description: "Globus XIO Driver –"
---

<h2 class="name">NAME</h2>
<p> Globus XIO Driver &#8211; </p>
<h3>Modules</h3>
<p> <code>Driver Programming: String options</code> </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_xio_driver_callback_t</code> )(globus_xio_operation_t op, globus_result_t result, void *user_arg)<br />
 <i>Open and Close Callback Signature. </i><br />
 typedef void(* <code>globus_xio_driver_data_callback_t</code> )(globus_xio_operation_t op, globus_result_t result, globus_size_t nbytes, void *user_arg) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_init_t</code> )(void **out_driver_attr) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_copy_t</code> )(void **dst, void *src) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_destroy_t</code> )(void *driver_attr) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_attr_cntl_t</code> )(void *attr, int cmd, va_list ap) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_init_t</code> )(void *driver_attr, const globus_xio_contact_t *contact_info, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_destroy_t</code> )(void *driver_server) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_accept_t</code> )(void *driver_server, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_server_cntl_t</code> )(void *driver_server, int cmd, va_list ap) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_link_destroy_t</code> )(void *driver_link) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_transform_open_t</code> )(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op)<br />
 <i>Open a handle. </i><br />
 typedef globus_result_t(* <code>globus_xio_driver_transport_open_t</code> )(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op)<br />
 <i>Open a handle. </i><br />
 typedef globus_result_t(* <code>globus_xio_driver_handle_cntl_t</code> )(void *handle, int cmd, va_list ap) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_close_t</code> )(void *driver_handle, void *driver_attr, globus_xio_operation_t op)<br />
 <i>Close a handle. </i><br />
 typedef globus_result_t(* <code>globus_xio_driver_read_t</code> )(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op) </p>
<p> typedef globus_result_t(* <code>globus_xio_driver_write_t</code> )(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_driver_set_server_pre_init</code> (globus_xio_driver_t driver, <code>globus_xio_driver_server_init_t</code> server_pre_init_func)<br />
 <i>Server Pre-Init. </i><br />
 globus_result_t <code>globus_xio_driver_handle_cntl</code> (globus_xio_driver_handle_t handle, globus_xio_driver_t driver, int cmd,&#8230;) </p>
<p> void <code>globus_xio_driver_finished_accept</code> (globus_xio_operation_t op, void *driver_link, globus_result_t result) </p>
<p> globus_result_t <code>globus_xio_driver_pass_open</code> (globus_xio_operation_t op, const globus_xio_contact_t *contact_info, <code>globus_xio_driver_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_open</code> (void *driver_handle, globus_xio_operation_t op, globus_result_t result) </p>
<p> globus_result_t <code>globus_xio_driver_operation_create</code> (globus_xio_operation_t *operation, globus_xio_driver_handle_t handle) </p>
<p> globus_bool_t <code>globus_xio_driver_operation_is_blocking</code> (globus_xio_operation_t operation) </p>
<p> globus_result_t <code>globus_xio_driver_pass_close</code> (globus_xio_operation_t op, <code>globus_xio_driver_callback_t</code> cb, void *callback_arg)<br />
 <i>Pass the close operation down the driver stack. </i><br />
 void <code>globus_xio_driver_finished_close</code> (globus_xio_operation_t op, globus_result_t result) </p>
<p> globus_result_t <code>globus_xio_driver_pass_read</code> (globus_xio_operation_t op, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t wait_for, <code>globus_xio_driver_data_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_read</code> (globus_xio_operation_t op, globus_result_t result, globus_size_t nread) </p>
<p> void <code>globus_xio_driver_set_eof_received</code> (globus_xio_operation_t op) </p>
<p> globus_bool_t <code>globus_xio_driver_eof_received</code> (globus_xio_operation_t op) </p>
<p> globus_result_t <code>globus_xio_driver_pass_write</code> (globus_xio_operation_t op, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t wait_for, <code>globus_xio_driver_data_callback_t</code> cb, void *user_arg) </p>
<p> void <code>globus_xio_driver_finished_write</code> (globus_xio_operation_t op, globus_result_t result, globus_size_t nwritten) </p>
<p> globus_result_t <code>globus_xio_driver_merge_operation</code> (globus_xio_operation_t top_op, globus_xio_operation_t bottom_op) </p>
<h2>Detailed Description</h2>
<p> Globus XIO introduces a notion of a driver stack to its API. Within globus_xio every I/O operation must occur on a globus_xio handle. Associated with each handle is a stack of drivers. A driver is a modulular piece of code that implements the globus_xio driver interface. The purpose of a driver is manipulate data passed in by the user in someway. Each driver in a stack will serve its own unique purpose. </p>
<p> I/O operations pass from driver to driver, starting at the top of the stack and ending at the bottom. When the bottom layer driver finishes with the operation it signals globus_xio that it has completed. Completion notification then flows up to the top of the driver stack.</p>
<h2>Driver Types</h2>
<dl>
<dt><code>Transport driver: </code></p>
<dd> A transport driver is one that is responsible for data communication. For example, a TCP or UDP driver would transmit data via network sockets, or a file driver would write data to a file.</dl>
<p> There must be exactly one transport driver in a stack, at its bottom. A transport driver never passes an operation to another driver in the stack. Instead, this type of driver relies on globus_xio system functions to implement data operations. </p>
<dl>
<dt><code>Transform driver: </code></p>
<dd> A transform driver is any intermediate driver in the stack. A transform driver relies on some other drivers on the driver stack to perform the data transport operation. An example of a transform driver would one which implements a network protocol such as http. This driver would frame and parse messages, but would rely on other drivers in the XIO stack.</dl>
<p> This allows additional transforms to happen in the XIO stack, such as layering the http protocol on top of an SSL protocol driver before transmitting the data via TCP. </p>
<h2>Driver API</h2>
<p> The Globus XIO Driver API is a set of functions and interfaces to allow a developer to create an XIO driver. To create a driver the user must implement all of the interface functions in the driver specification. There is also a set of functions provided to assist the driver author in implementing a driver.</p>
<h3>Quick Start</h3>
<p> For basic driver needs, the developer will have to pay attention to a few structures and concepts. </p>
<dl>
<dt>globus_xio_operation_t</p>
<dd> This structure represents a request for an operation. If the driver can service the operation it does so and the calls the appropriate <i>finished</i> function. If the driver cannot completely service the operation it can <i>pass</i> it to the next driver in the stack. As soon as the operation structure is either finished or passed it is no longer valid for use in any other function.</dl>
<dl>
<dt>globus_xio_driver_handle_t</p>
<dd> A globus_xio_driver_handle_t represents an open handle to the driver stack for XIO. The driver obtains a driver_handle by calling globus_xio_operation_get_driver_handle(). The driver_handle allows the user to do some complex things that will be described later.</dl>
<h3>Typical Sequence:</h3>
<p> Here is a typical sequence of events for a globus_xio transform driver. All operations are initiated either by the application calling a function in the Globus XIO API, or from a driver above the transform driver in the stack passing an operation to this driver. </p>
<dl>
<dt><code>Open </code></p>
<dd> XIO calls the globus_xio_driver_transform_open_t function of the driver, passing it the operation and, in the case of a passive open, the link from a server accept. The driver typically allocates a private data structure containing the state it wishes to associate with this handle, and passes this along with a callback function pointer to <code>globus_xio_driver_pass_open()</code>. This allows the other drivers in the XIO stack to continue to process the operation.</dl>
<p> After the lower drivers in the stack have completed processing the open, they will call <code>globus_xio_driver_finished_open()</code>, which will in turn call the callback function which the driver passed as a parameter to <code>globus_xio_driver_pass_open()</code>. The driver then does any post-open operation needed, and then finishes the operation by calling <code>globus_xio_driver_finished_open()</code>, passing the private state data as the <i>driver_handle</i> parameter. This state data will be passed to future operation implementations done with this handle. </p>
<dl>
<dt><code>Read/Write </code></p>
<dd> XIO calls the driver&#8217;s globus_xio_driver_read_t or globus_xio_driver_write_t function with an operation as a parameter and the state date from the <code>globus_xio_driver_finished_open()</code> call. The driver then transforms the data if necessary and then calls the <code>globus_xio_driver_pass_read()</code> or <code>globus_xio_driver_pass_write()</code> which passes the operation down the XIO driver stack. When the driver below it on the XIO stack calls <code>globus_xio_driver_finished_read()</code> or <code>globus_xio_driver_finished_write()</code>, the callback which was passed is invoked. In that callback, the driver should itself call <code>globus_xio_driver_finished_read()</code> or <code>globus_xio_driver_finished_write()</code> to indicate completion.</dl>
<dl>
<dt><code>Close </code></p>
<dd> XIO calls the close interface function, passing an operation and the private driver state. The driver will call <code>globus_xio_driver_pass_close()</code> passing it the operation. When the close callback is received the driver calls <code>globus_xio_driver_finished_close()</code> passing it the operation. At this point, the driver typically frees its private data, as the handle is no longer valid.</dl>
<h2>Globus XIO Attributes</h2>
<p> Attributes provide a way to pass additional metadata to driver operations. Most Globus XIO API functions include an attribute parameter. Each driver implements its own set of attribute handling function. To implement attributes, a driver must provide functions of these types: </p>
<dl>
<dt>&bull;</p>
<dd> globus_xio_driver_attr_init_t</p>
<dt>&bull;</p>
<dd> globus_xio_driver_attr_copy_t</p>
<dt>&bull;</p>
<dd> globus_xio_driver_attr_cntl_t</p>
<dt>&bull;</p>
<dd> globus_xio_driver_attr_destroy_t</dl>
<p> Pointers to these functions are associated with the driver by calling globus_xio_driver_set_attr</p>
<h2>Advanced Driver Programming</h2>
<p> The typical driver implementation is describe above. However globus_xio allows driver authors to do more advanced things such as initiating operations on their own. </p>
<dl>
<dt><code>Read Ahead </code></p>
<dd> Once a handle is open, a driver can create operation structures from it. A driver can then request I/O from the driver stack before it receives a call to its own I/O interface functions, implementing read-ahead functionality. This can be done as follows:</dl>
<dl>
<dt>1.</p>
<dd> Obtain a driver handle from the open operation by calling globus_xio_operation_get_driver_handle()</p>
<dt>2.</p>
<dd> Create an operation by calling <code>globus_xio_driver_operation_create()</code> and pass it the driver_handle from the previous step</p>
<dt>3.</p>
<dd> call <code>globus_xio_driver_pass_read()</code> using this operation. When the read callback is received, the driver saves the returned data in its private data and then calls <code>globus_xio_driver_finished_read()</code> on the operation.</p>
<dt>4.</p>
<dd> When XIO calls the driver&#8217;s read interface function, the driver can immediately call <code>globus_xio_driver_finished_read()</code> function after updating the iovec structure with the data it had previously read.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef globus_result_t(* globus_xio_driver_attr_cntl_t)(void *attr, int cmd, va_list ap)</h3>
<p> get or set information in an attr. </p>
<p> The cmd parameter determines what functionality the user is requesting. The driver is responsible for providing documentation to the user on all the possible values that cmd can be. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_attr</i> The driver specific attr, created by globus_xio_driver_attr_init_t.<br />
 <i>cmd</i> An integer representing what functionality the user is requesting.<br />
 <i>ap</i> variable arguments. These are determined by the driver and the value of cmd.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_attr_copy_t)(void **dst, void *src)</h3>
<p> Copy a driver attr. </p>
<p> When this function is called the driver will create a copy of the attr in parameter src and place it in the parameter dst.</p>
<h3>typedef globus_result_t(* globus_xio_driver_attr_destroy_t)(void *driver_attr)</h3>
<p> Destroy the driver attr. </p>
<p> Clean up all resources associate with the attr.</p>
<h3>typedef globus_result_t(* globus_xio_driver_attr_init_t)(void **out_driver_attr)</h3>
<p> Create a driver specific attribute. </p>
<p> The driver should implement this function to create a driver specific attribute and return it via the out_attr parameter.</p>
<h3>typedef void(* globus_xio_driver_callback_t)(globus_xio_operation_t op, globus_result_t result, void *user_arg)</h3>
<p> Open and Close Callback Signature. This is the function signature of callbacks for the globus_xio_pass_open() and globus_xio_pass_close() functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure associated with the open or the close requested operation. The driver should call the appropriate finished operation to clean up this structure.<br />
 <i>result</i> The result of the requested data operation<br />
 <i>user_arg</i> The user pointer that is threaded through to the callback.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_close_t)(void *driver_handle, void *driver_attr, globus_xio_operation_t op)</h3>
<p> Close a handle. This closes a handle. Driver implementations should pass the close to the other drivers in the stack by calling globus_xio_pass_close(). </p>
<p> In the close callback, the driver should clean up the data associated with driver_handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_specific_handle</i> The driver handle to be closed.<br />
 <i>driver_attr</i> A driver specific attr which may be used to alter how a close is performed (e.g. caching drivers)<br />
 <i>op</i> The open operation. When the driver is finished opening the handle, it passes this to <code>globus_xio_driver_finished_close()</code> to return status up the driver stack to the application.</dl>
<h3>typedef void(* globus_xio_driver_data_callback_t)(globus_xio_operation_t op, globus_result_t result, globus_size_t nbytes, void *user_arg)</h3>
<p> Data Callback interface </p>
<p> This is the function signature of read and write operation callbacks. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure associated with the read or write operation request. The driver should call the appropriate finished operation when it receives this operation.<br />
 <i>result</i> The result of the requested data operation<br />
 <i>nbytes</i> the number of bytes read or written<br />
 <i>user_arg</i> The user pointer that is threaded through to the callback.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_handle_cntl_t)(void *handle, int cmd, va_list ap)</h3>
<p> this call <i>must</i> return an GLOBUS_XIO_ERROR_COMMAND error for unsupported command numbers. (use GlobusXIOErrorInvalidCommand(cmd)) </p>
<p> Drivers that have reason to support the commands listed at <code>globus_xio_handle_cmd_t</code> should accept the xio generic cmd numbers and their driver specific command number. Do NOT implement those handle cntls unless you really are the definitive source.</p>
<h3>typedef globus_result_t(* globus_xio_driver_link_destroy_t)(void *driver_link)</h3>
<p> destroy a link </p>
<p> The driver should clean up all resources associated with the link when this function is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_link</i> The link to be destroyed.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_read_t)(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op)</h3>
<p> Read data from an open handle. </p>
<p> This function is called when the user requests to read data from a handle. The driver author shall implement all code needed to for there driver to complete a read operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_handle</i> The driver handle from which data should be read.<br />
 <i>iovec</i> An io vector pointing to the buffers to be read into.<br />
 <i>iovec_count</i> The number if entries in the io vector.<br />
 <i>op</i> The requested operation. When the driver is finished fulfilling the requested read operation it must use this structure to signal globus_xio that the operation is completed. This is done by calling globus_xio_driver_finished_operation().</dl>
<h3>typedef globus_result_t(* globus_xio_driver_server_accept_t)(void *driver_server, globus_xio_operation_t op)</h3>
<p> Accept a server connection </p>
<p> The driver developer should implement this function if their driver handles server operations. Once the accept operation completes, the connection is established. The user still has an opportunity to open the link or destroy it. They can query the link for additional information on which to base the decision to open. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_server</i> The server object from which the link connection will be accepted.<br />
 <i>op</i> The requested operation. When the driver is finished accepting the server connection it uses this structure to signal globus_xio that it has completed the operation.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_server_cntl_t)(void *driver_server, int cmd, va_list ap)</h3>
<p> Query a server for information. </p>
<p> This function allows a user to request information from a driver specific server handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_server</i> the server handle.<br />
 <i>cmd</i> An integer telling the driver what operation to preform on this server handle.<br />
 <i>ap</i> variable args.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_server_destroy_t)(void *driver_server)</h3>
<p> destroy a server. </p>
<p> When this function is called the driver should free up all resources associated with a server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The server that the driver should clean up.<br />
 <i>driver_server</i> The reference to the internal server that is being declared invalid with this function call.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_server_init_t)(void *driver_attr, const globus_xio_contact_t *contact_info, globus_xio_operation_t op)</h3>
<p> Initialize a server object </p>
<p> The driver developer should implement this function if their driver handles server operations (passive opens). In the TCP driver this function creates a TCP socket and calls listen() on it. Unlike all other XIO driver implementation functions, the <code>globus_xio_server_create()</code> function begins at the bottom (transport driver) of the stack, and the globus_xio_driver_pass_server_init() acts like a finished() operation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_attr</i> A driver-specific attribute. This may be NULL.<br />
 <i>contact_info</i> Contact information from the stack below this driver. This is NULL for the transport driver.<br />
 <i>op</i> An op which must be passed to globus_xio_driver_pass_server_init() to pass the server contact information up the XIO driver stack.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returning GLOBUS_SUCCESS for this means that globus_xio_driver_pass_server_init returned success and the driver&#8217;s server-specific data is initialized.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_transform_open_t)(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op)</h3>
<p> Open a handle. This is called when a user opens a handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_info</i> Contains information about the requested resource. Its members may all be null (especially when link is not null). XIO will destroy this contact info upon return from the interface function<br />
 <i>driver_link</i> Comes from server accept. Used to link an accepted connection to an xio handle. XIO will destroy this object upon the return of this interface call.<br />
 <i>driver_attr</i> A attribute describing how to open. This points to a piece of memory created by the globus_xio_driver_attr_init_t interface function.<br />
 <i>op</i> The open operation. When the driver is finished opening the handle, it passes this to <code>globus_xio_driver_finished_open()</code> to return status up the driver stack to the application.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_transport_open_t)(const globus_xio_contact_t *contact_info, void *driver_link, void *driver_attr, globus_xio_operation_t op)</h3>
<p> Open a handle. This is called when a user opens a handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_info</i> Contains information about the requested resource. Its members may all be null (especially when link is not null). XIO will destroy this contact info upon return from the interface function<br />
 <i>driver_link</i> Comes from server accept. Used to link an accepted connection to an xio handle. XIO will destroy this object upon the return of this interface call.<br />
 <i>driver_attr</i> A attribute describing how to open. This points to a piece of memory created by the globus_xio_driver_attr_init_t interface function.<br />
 <i>op</i> The open operation. When the driver is finished opening the handle, it passes this to <code>globus_xio_driver_finished_open()</code> to return status up the driver stack to the application.</dl>
<h3>typedef globus_result_t(* globus_xio_driver_write_t)(void *driver_specific_handle, const globus_xio_iovec_t *iovec, int iovec_count, globus_xio_operation_t op)</h3>
<p> Write data from an open handle. </p>
<p> This function is called when the user requests to write data to a handle. The driver author shall implement all code needed to for there driver to complete write operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_handle</i> The driver handle to which data should be written.<br />
 <i>iovec</i> An io vector pointing to the buffers to be written.<br />
 <i>iovec_count</i> The number if entries in the io vector.<br />
 <i>op</i> The requested operation. When the driver is finished fulfilling the requested read operation it must use this structure to signal globus_xio that the operation is completed. This is done by calling globus_xio_driver_finished_operation().</dl>
<h2>Function Documentation</h2>
<h3>globus_bool_t globus_xio_driver_eof_received (globus_xio_operation_top)</h3>
<p> EOF state checking </p>
<p> This function is used by drivers that allow multiple outstanding reads at a time. It can only be called on behalf of a read operation (while in the read interface call or the pass_read callback). </p>
<p> Typical use for this would be to hold a driver specific lock (the same one used when calling <code>globus_xio_driver_set_eof_received()</code>) and call this to see if an EOF has been received. If so, the operation should immediately be finished with an EOF error (do not <i>return</i> an EOF error). </p>
<p> This call will typically only be used in the read interface call. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested read operation.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_TRUE if EOF received, GLOBUS_FALSE otherwise.</dl>
<h3>void globus_xio_driver_finished_accept (globus_xio_operation_top, void *driver_link, globus_result_tresult)</h3>
<p> Driver API finished accept </p>
<p> This function should be called to signal globus_xio that it has completed the accept operation requested of it. It will free up resources associated with the accept_op and potentially cause xio to pop the signal up the driver stack. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The requested accept operation that has completed.<br />
 <i>driver_link</i> This is the initialized driver link that is that will be passed to the open interface when this handle is opened.<br />
 <i>result</i> Return status of the completed operation</dl>
<h3>void globus_xio_driver_finished_close (globus_xio_operation_top, globus_result_tresult)</h3>
<p> Driver API finished_close </p>
<p> The driver calls this function after completing a close operation on a driver_handle. Once this function returns the driver_handle is no longer valid. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The close operation that has completed.<br />
 <i>result</i> Return status of the completed operation</dl>
<h3>void globus_xio_driver_finished_open (void *driver_handle, globus_xio_operation_top, globus_result_tresult)</h3>
<p> Driver API finished open </p>
<p> This function should be called to signal globus_xio that it has completed the open operation requested of it. It will free up resources associated with the op and potentially cause xio to pop the signal up the driver stack. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_handle</i> The driver specific handle pointer that will be passed to future interface function calls.<br />
 <i>op</i> The requested open operation that has completed.<br />
 <i>result</i> Return status of the completed operation</dl>
<h3>void globus_xio_driver_finished_read (globus_xio_operation_top, globus_result_tresult, globus_size_tnread)</h3>
<p> Finished Read </p>
<p> This function is called to signal globus_xio that the requested read operation has been completed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested read operation.<br />
 <i>result</i> Return status of the completed operation<br />
 <i>nread</i> The number of bytes read</dl>
<h3>void globus_xio_driver_finished_write (globus_xio_operation_top, globus_result_tresult, globus_size_tnwritten)</h3>
<p> Finished Write </p>
<p> This function is called to signal globus_xio that the requested write operation has been completed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested write operation.<br />
 <i>result</i> Return status of the completed operation<br />
 <i>nwritten</i> The number of bytes written</dl>
<h3>globus_result_t globus_xio_driver_handle_cntl (globus_xio_driver_handle_thandle, globus_xio_driver_tdriver, intcmd, &#8230;)</h3>
<p> Touch driver specific information in a handle object. </p>
<p> pass the driver to control a specific driver pass NULL for driver for XIO specific cntls pass GLOBUS_XIO_QUERY for driver to try each driver (below current) in order</p>
<h3>globus_result_t globus_xio_driver_merge_operation (globus_xio_operation_ttop_op, globus_xio_operation_tbottom_op)</h3>
<p> Finishes an operation and merge two op structures. (XXX not implemented yet) </p>
<p> This function will join to operations together and signal globus_xio that it has completed. This is an advanced function. Most drivers will not require its use. This function takes an operation that was created by this driver and passed on to drivers lower on the stack and an operation that came in on the interface function (that has seen the top half of the stack) and joins them together. The purpose of this function is to join data descriptors that were pre-staged and cached with those that have later come in at the users request. See the read ahead doc for more information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>top_op</i> The operation that has seen the top part of the driver stack.<br />
 <i>bottom_op</i> The operation that has seen the bottom part of the driver stack.</dl>
<p> (result is always success in this case. if there is an error, use the other finish() call)</p>
<h3>globus_result_t globus_xio_driver_operation_create (globus_xio_operation_t *operation, globus_xio_driver_handle_thandle)</h3>
<p> Driver API Create Operation </p>
<p> This function will create an operation from an initialized handle This operation can then be used for io operations related to the handle that created them. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>operation</i> The operation to be created. When this function returns this structure will be populated and available for use for the driver.<br />
 <i>handle</i> The initialized handle representing the user handle from which the operation will be created.</dl>
<h3>globus_bool_t globus_xio_driver_operation_is_blocking (globus_xio_operation_toperation)</h3>
<p> Is Operation blocking. </p>
<p> If the operation is blocking the driver developer may be able to make certain optimizations. The function returns true if the given operation was created via a user call to a blocking function.</p>
<h3>globus_result_t globus_xio_driver_pass_close (globus_xio_operation_top, <code>globus_xio_driver_callback_t</code>cb, void *callback_arg)</h3>
<p> Pass the close operation down the driver stack. This function will pass a close request down the driver stack. Upon completion of the close operation globus_xio will call the function pointed to by the cb parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The close operation.<br />
 <i>cb</i> A pointer to the function to be called once all drivers lower in the stack have closed.<br />
 <i>callback_arg</i> A pointer that will be passed to the callback.</dl>
<h3>globus_result_t globus_xio_driver_pass_open (globus_xio_operation_top, const globus_xio_contact_t *contact_info, <code>globus_xio_driver_callback_t</code>cb, void *user_arg)</h3>
<p> Driver API Open </p>
<p> This function will pass an open request down the driver stack. Upon completion of the open operation globus_xio will call the <i>cb</i> function, at which point the handle structure will be initialized and available for use. </p>
<p> As soon as the function returns the handle is valid for creating other operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation from which the handle will be established. This parameter is used to determine what drivers are in the stack and other such information.<br />
 <i>contact_info</i> The contact info describing the resource the driver below should open. This will normally be the same contact info that was passed in on the open interface.<br />
 <i>cb</i> The function to be called when the open operation is complete.<br />
 <i>user_arg</i> a user pointer that will be threaded through to the callback.</dl>
<h3>globus_result_t globus_xio_driver_pass_read (globus_xio_operation_top, globus_xio_iovec_t *iovec, intiovec_count, globus_size_twait_for, <code>globus_xio_driver_data_callback_t</code>cb, void *user_arg)</h3>
<p> Driver read </p>
<p> This function passes a read operation down the driver stack. After this function is called the op structure is no longer valid. However when the driver stack finishes servicing the read request it will pass a new operation structure in the function pointed to by cb. Finish read can be called on the new operation received. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing this requested io operation.<br />
 <i>iovec</i> A pointer to the array of iovecs.<br />
 <i>iovec_count</i> The number of iovecs in the array.<br />
 <i>wait_for</i> The minimum number of bytes to read before returning. if a driver has no specifc requirement, he should use the user&#8217;s request available via GlobusXIOOperationMinimumRead(op)<br />
 <i>cb</i> The function to be called when the operation request is completed.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.</dl>
<h3>globus_result_t globus_xio_driver_pass_write (globus_xio_operation_top, globus_xio_iovec_t *iovec, intiovec_count, globus_size_twait_for, <code>globus_xio_driver_data_callback_t</code>cb, void *user_arg)</h3>
<p> Driver write </p>
<p> This function passes a write operation down the driver stack. After this function is called the op structure is no longer valid. However when the driver stack finishes servicing the write request it will pass a new operation structure in the function pointed to by cb. Finished write can be called on the new operation received. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing this requested io operation.<br />
 <i>iovec</i> A pointer to the array of iovecs.<br />
 <i>iovec_count</i> The number of iovecs in the array.<br />
 <i>wait_for</i> The minimum number of bytes to write before returning. If a driver has no specific requirement, he should use the user&#8217;s request available via GlobusXIOOperationMinimumWrite(op)<br />
 <i>cb</i> The function to be called when the operation request is completed.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.</dl>
<h3>void globus_xio_driver_set_eof_received (globus_xio_operation_top)</h3>
<p> EOF state manipulation </p>
<p> This function is used by drivers that allow multiple outstanding reads at a time. It can only be called on behalf of a read operation (while in the read interface call or the pass_read callback). </p>
<p> Typical use for this would be to hold a driver specific lock and call this when an internal EOF has been received. The read operation this is called on behalf of must be finished with an EOF error or the results are undefined. </p>
<p> In general, you should not have an EOF flag in your driver. Use this call and <code>globus_xio_driver_eof_received()</code> instead. This is necessary to support XIO&#8217;s automatic EOF resetting. If your driver absolutely can not be read after an EOF has been set, then you will need your own EOF flag. </p>
<p> This call will typically only be used just before a finished_read() call. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>op</i> The operation structure representing the requested read operation.</dl>
<h3>globus_result_t globus_xio_driver_set_server_pre_init (globus_xio_driver_tdriver, <code>globus_xio_driver_server_init_t</code>server_pre_init_func)</h3>
<p> Server Pre-Init. This function adds a callback to a driver that will be called before a server handle is created by XIO. This function has the same signature as the server_init_func in the driver, but is always called with a NULL contact string. There is no support for calling a pass() or finished() function for this interface. It may inspect and modify its attributes and operation, but can not directly return any data or set a driver-specific server handle value. If this function returns an error result, the server create will be aborted. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver</i> Driver to associate the function with<br />
 <i>server_pre_init_func</i> Function to call prior to creating a server</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_XIO_ERROR_PARAMETER</i> Invalid parameter</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBV">Author</a></p>
<dd></dl>
