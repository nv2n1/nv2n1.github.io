---
title: "globus_xio_server_accept(3)"
name: "globus_xio_server_accept"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_server_accept/"
description: "Globus XIO API –"
---

<h2 class="name">NAME</h2>
<p> Globus XIO API &#8211; </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_xio_accept_callback_t</code> )(globus_xio_server_t server, globus_xio_handle_t handle, globus_result_t result, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_server_callback_t</code> )(globus_xio_server_t server, void *user_arg) </p>
<p> typedef globus_bool_t(* <code>globus_xio_timeout_callback_t</code> )(globus_xio_handle_t handle, <code>globus_xio_operation_type_t</code> type, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_callback_t</code> )(globus_xio_handle_t handle, globus_result_t result, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_data_callback_t</code> )(globus_xio_handle_t handle, globus_result_t result, globus_byte_t *buffer, globus_size_t len, globus_size_t nbytes, globus_xio_data_descriptor_t data_desc, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_iovec_callback_t</code> )(globus_xio_handle_t handle, globus_result_t result, globus_xio_iovec_t *iovec, int count, globus_size_t nbytes, globus_xio_data_descriptor_t data_desc, void *user_arg) </p>
<p> typedef enum <code>globus_i_xio_op_type_e</code> <code>globus_xio_operation_type_t</code> </p>
<h3>Enumerations</h3>
<p> enum <code>globus_i_xio_op_type_e</code> </p>
<p> enum <code>globus_xio_handle_cmd_t</code> { <code>GLOBUS_XIO_GET_LOCAL_CONTACT</code> = 12345, <code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_GET_REMOTE_CONTACT</code>, <code>GLOBUS_XIO_GET_REMOTE_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_SEEK</code>, <code>GLOBUS_XIO_SET_STRING_OPTIONS</code>, <code>GLOBUS_XIO_GET_STRING_OPTIONS</code>, <code>GLOBUS_XIO_GET_DRIVER_NAME</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_attr_init</code> (globus_xio_attr_t *attr) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (globus_xio_attr_t attr, globus_xio_driver_t driver, int cmd,&#8230;) </p>
<p> globus_result_t <code>globus_xio_attr_copy</code> (globus_xio_attr_t *dst, globus_xio_attr_t src) </p>
<p> globus_result_t <code>globus_xio_attr_destroy</code> (globus_xio_attr_t attr) </p>
<p> globus_result_t <code>globus_xio_stack_init</code> (globus_xio_stack_t *stack, globus_xio_attr_t stack_attr) </p>
<p> globus_result_t <code>globus_xio_stack_push_driver</code> (globus_xio_stack_t stack, globus_xio_driver_t driver) </p>
<p> globus_result_t <code>globus_xio_stack_copy</code> (globus_xio_stack_t *dst, globus_xio_stack_t src) </p>
<p> globus_result_t <code>globus_xio_stack_destroy</code> (globus_xio_stack_t stack) </p>
<p> globus_result_t <code>globus_xio_server_create</code> (globus_xio_server_t *server, globus_xio_attr_t server_attr, globus_xio_stack_t stack) </p>
<p> globus_result_t <code>globus_xio_server_get_contact_string</code> (globus_xio_server_t server, char **contact_string) </p>
<p> globus_result_t <code>globus_xio_server_register_close</code> (globus_xio_server_t server, <code>globus_xio_server_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_server_close</code> (globus_xio_server_t server) </p>
<p> globus_result_t <code>globus_xio_server_cntl</code> (globus_xio_server_t server, globus_xio_driver_t driver, int cmd,&#8230;) </p>
<p> globus_result_t <code>globus_xio_server_accept</code> (globus_xio_handle_t *out_handle, globus_xio_server_t server) </p>
<p> globus_result_t <code>globus_xio_server_register_accept</code> (globus_xio_server_t server, <code>globus_xio_accept_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_handle_create</code> (globus_xio_handle_t *handle, globus_xio_stack_t stack) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_init</code> (globus_xio_data_descriptor_t *data_desc, globus_xio_handle_t handle) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_destroy</code> (globus_xio_data_descriptor_t data_desc) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (globus_xio_data_descriptor_t data_desc, globus_xio_driver_t driver, int cmd,&#8230;) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (globus_xio_handle_t handle, globus_xio_driver_t driver, int cmd,&#8230;) </p>
<p> globus_result_t <code>globus_xio_register_open</code> (globus_xio_handle_t handle, const char *contact_string, globus_xio_attr_t attr, <code>globus_xio_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_open</code> (globus_xio_handle_t handle, const char *contact_string, globus_xio_attr_t attr) </p>
<p> globus_result_t <code>globus_xio_register_read</code> (globus_xio_handle_t handle, globus_byte_t *buffer, globus_size_t buffer_length, globus_size_t waitforbytes, globus_xio_data_descriptor_t data_desc, <code>globus_xio_data_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_read</code> (globus_xio_handle_t handle, globus_byte_t *buffer, globus_size_t buffer_length, globus_size_t waitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_t data_desc) </p>
<p> globus_result_t <code>globus_xio_register_readv</code> (globus_xio_handle_t handle, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t waitforbytes, globus_xio_data_descriptor_t data_desc, <code>globus_xio_iovec_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_readv</code> (globus_xio_handle_t handle, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t waitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_t data_desc) </p>
<p> globus_result_t <code>globus_xio_register_write</code> (globus_xio_handle_t handle, globus_byte_t *buffer, globus_size_t buffer_length, globus_size_t waitforbytes, globus_xio_data_descriptor_t data_desc, <code>globus_xio_data_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_write</code> (globus_xio_handle_t handle, globus_byte_t *buffer, globus_size_t buffer_length, globus_size_t waitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_t data_desc) </p>
<p> globus_result_t <code>globus_xio_register_writev</code> (globus_xio_handle_t handle, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t waitforbytes, globus_xio_data_descriptor_t data_desc, <code>globus_xio_iovec_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_writev</code> (globus_xio_handle_t handle, globus_xio_iovec_t *iovec, int iovec_count, globus_size_t waitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_t data_desc) </p>
<p> globus_result_t <code>globus_xio_register_close</code> (globus_xio_handle_t handle, globus_xio_attr_t attr, <code>globus_xio_callback_t</code> cb, void *user_arg) </p>
<p> globus_result_t <code>globus_xio_close</code> (globus_xio_handle_t handle, globus_xio_attr_t attr) </p>
<p> globus_result_t <code>globus_xio_handle_create_from_url</code> (globus_xio_handle_t *out_h, const char *scheme, globus_xio_attr_t attr, char *param_string) </p>
<p> globus_result_t <code>globus_xio_driver_list_to_stack_attr</code> (globus_list_t *driver_list, globus_xio_stack_t stack, globus_xio_attr_t attr)<br />
 <i>Add a list of driver entries to a stack. </i><br />
 globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GET_LOCAL_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GET_REMOTE_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GET_REMOTE_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_SEEK</code>, globus_off_t offset) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_SET_STRING_OPTIONS</code>, char *config_string) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GET_STRING_OPTIONS</code>, char **config_string) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_GET_DRIVER_NAME</code>, const char **driver_name) </p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_xio_accept_callback_t)(globus_xio_server_t server, globus_xio_handle_t handle, globus_result_t result, void *user_arg)</h3>
<p> Callback signature for accept. </p>
<p> When a registered accept operation completes the users function of this signature is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The server object on which the accept was registered.<br />
 <i>handle</i> The newly created handle that was created by the accept operation.<br />
 <i>result</i> A result code indicating the success of the accept operation. GLOBUS_SUCCESS indicates a successful accept.<br />
 <i>user_arg</i> A user argument that is threaded from the registration to the callback.</dl>
<h3>typedef void(* globus_xio_callback_t)(globus_xio_handle_t handle, globus_result_t result, void *user_arg)</h3>
<p> globus_xio_callback_t </p>
<p> This callback is used for the open and close asynchronous operations.</p>
<h3>typedef void(* globus_xio_data_callback_t)(globus_xio_handle_t handle, globus_result_t result, globus_byte_t *buffer, globus_size_t len, globus_size_t nbytes, globus_xio_data_descriptor_t data_desc, void *user_arg)</h3>
<p> globus_xio_data_callback_t </p>
<p> This callback is used for asynchronous operations that send or receive data. </p>
<p> On EOF, result_t will be of type GLOBUS_XIO_ERROR_EOF</p>
<h3>typedef void(* globus_xio_iovec_callback_t)(globus_xio_handle_t handle, globus_result_t result, globus_xio_iovec_t *iovec, int count, globus_size_t nbytes, globus_xio_data_descriptor_t data_desc, void *user_arg)</h3>
<p> globus_xio_iovec_callback_t </p>
<p> This callback is used for asynchronous operations that send or receive data with an iovec structure. </p>
<p> On EOF, result_t will be of type GLOBUS_XIO_ERROR_EOF</p>
<h3>typedef enum <code>globus_i_xio_op_type_e</code> <code>globus_xio_operation_type_t</code></h3>
<p> Operation types </p>
<p> An enumeration of operation types. Used in the timeout callback to indicate what operation typed timedout.</p>
<h3>typedef void(* globus_xio_server_callback_t)(globus_xio_server_t server, void *user_arg)</h3>
<p> Server callback signature. </p>
<p> This is the generic server callback signature. It is currently only used for the register close operation.</p>
<h3>typedef globus_bool_t(* globus_xio_timeout_callback_t)(globus_xio_handle_t handle, <code>globus_xio_operation_type_t</code> type, void *user_arg)</h3>
<p> The timeout callback function signature. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle the handle on which the timeout operation was requested.<br />
 <i>type</i> The type of operation that timed out: GLOBUS_XIO_OPERATION_OPEN GLOBUS_XIO_OPERATION_CLOSE GLOBUS_XIO_OPERATION_READ GLOBUS_XIO_OPERATION_WRITE<br />
 <i>arg</i> A user arg threaded through to the callback.</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_i_xio_op_type_e</code></h3>
<p> Operation types </p>
<p> An enumeration of operation types. Used in the timeout callback to indicate what operation typed timedout.</p>
<h3>enum <code>globus_xio_handle_cmd_t</code></h3>
<p> doxygen varargs filter stuff Common driver handle cntls. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_GET_LOCAL_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GET_REMOTE_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GET_REMOTE_NUMERIC_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_SEEK </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_SET_STRING_OPTIONS </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GET_STRING_OPTIONS </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GET_DRIVER_NAME </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (globus_xio_attr_tattr, globus_xio_driver_tdriver, intcmd, &#8230;)</h3>
<p> Manipulate the values associated in the attr. </p>
<p> This function provides a means to access the attr structure. What exactly this function does is determined by the value in the parameter cmd and the value of the parameter driver. When the driver parameter is NULL it indicates that this function applies to general Globus XIO values. If it is not NULL it indicates that the function will effect driver specific values. Each driver is responsible for defining its own enumeration of values for cmd and the var args associated with that command. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> the attribute structure to be manipulated.<br />
 <i>driver</i> This parameter indicates which driver the user would like to perform the requested operation. If this parameter is NULL this request will be scoped to general attribute functions.<br />
 <i>cmd</i> an enum that determines what specific operation the user is requesting. Each driver will determine the value for this enumeration.</dl>
<h3>globus_result_t globus_xio_attr_copy (globus_xio_attr_t *dst, globus_xio_attr_tsrc)</h3>
<p> Copy an attribute structure.</p>
<h3>globus_result_t globus_xio_attr_destroy (globus_xio_attr_tattr)</h3>
<p> Clean up resources associated with an attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Upon completion of this function all resources associated with this structure will returned to the system and the attr will no longer be valid.</dl>
<h3>globus_result_t globus_xio_attr_init (globus_xio_attr_t *attr)</h3>
<p> Initialize a Globus XIO attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> upon return from this function this out parameter will be initialized. Once the user is finished with the attribute they should make sure they destroy it in order to free resources associated with it.</dl>
<h3>globus_result_t globus_xio_close (globus_xio_handle_thandle, globus_xio_attr_tattr)</h3>
<p> Blocking close</p>
<h3>globus_result_t globus_xio_data_descriptor_cntl (globus_xio_data_descriptor_tdata_desc, globus_xio_driver_tdriver, intcmd, &#8230;)</h3>
<p> Touch driver specific data in data descriptors </p>
<p> This function allows the user to communicate directly with a driver in association with a data descriptors. The driver defines what operations can be preformed.</p>
<h3>globus_result_t globus_xio_data_descriptor_destroy (globus_xio_data_descriptor_tdata_desc)</h3>
<p> clean up a data descriptor.</p>
<h3>globus_result_t globus_xio_data_descriptor_init (globus_xio_data_descriptor_t *data_desc, globus_xio_handle_thandle)</h3>
<p> Initialize a data descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data_desc</i> An out parameter. The data descriptor to be initialized.<br />
 <i>handle</i> The handle this data descriptor will be used with. This parameter is require in order to optimize the code handling the data descriptors use.</dl>
<h3>globus_result_t globus_xio_driver_list_to_stack_attr (globus_list_t *driver_list, globus_xio_stack_tstack, globus_xio_attr_tattr)</h3>
<p> Add a list of driver entries to a stack. This function walks a list of globus_xio_driver_list_ent_t * values passed as the driver_list parameter, and pushes them onto the XIO stack passed as the stack parameter and sets attributes for those drivers in the attr passed as the attr parameter to this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_list</i> A list of driver list entries in stack order (transport, followed by transform). Each entry may contain a option string for attributes to set for this driver.<br />
 <i>stack</i> A pointer to an XIO stack which will have the drivers pushed onto. It must be previously initialized by calling <code>globus_xio_stack_init()</code>. This function does not overwrite the stack, so the drivers passed in the driver list will be pushed on top of any existing drivers in the stack.<br />
 <i>attr</i> A pointer to an XIO attribute which will have the driver-specific string options set on it, after the drivers are pushed onto the stack. The opts field of the list entries are passed to the GLOBUS_XIO_SET_STRING_OPTIONS attr control function. This value must be previously initialized by calling <code>globus_xio_attr_init()</code>. Errors from the attr control function are ignored.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> If the driver can not be pushed onto the stack, an error result is returned; otherwise, GLOBUS_SUCCESS. If an error occurs, some of the entries MAY be pushed on to the stack and some attributes may have been set in the attr. Both should be destroyed by the caller.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_GET_LOCAL_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get local connection info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the local end of a connected handle. Where possible, it will be in symbolic form (FQDN).</dl>
<p> The user must free the returned string. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_server_get_contact_string()</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get local connection info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the local end of a connected handle. Where possible, it will be in numeric form. (IP)</dl>
<p> The user must free the returned string.</p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_GET_REMOTE_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get remote connection info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the remote end of a connected handle. Where possible, it will be in symbolic form (FQDN).</dl>
<p> The user must free the returned string.</p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_GET_REMOTE_NUMERIC_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get remote connection info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the remote end of a connected handle. Where possible, it will be in numeric form. (IP)</dl>
<p> The user must free the returned string.</p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_SEEK</code>, globus_off_toffset)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Reposition read/write offset. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>offset</i> Specify the desired offset.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_SET_STRING_OPTIONS</code>, char *config_string)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the driver specific configuration string. The format of the string is defined by the driver. It is typically a set of key=value pairs </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>config_string</i> The driver specific parameter string.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_GET_STRING_OPTIONS</code>, char **config_string)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the driver specific configuration string. The format of the string is defined by the driver. It is typically a set of key=value pairs </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>config_string</i> The driver specific parameter string.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_GET_DRIVER_NAME</code>, const char **driver_name)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the driver specific configuration string. The format of the string is defined by the driver. It is typically a set of key=value pairs </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>driver_name</i> The driver name.</dl>
<h3>globus_result_t globus_xio_handle_cntl (globus_xio_handle_thandle, globus_xio_driver_tdriver, intcmd, &#8230;)</h3>
<p> Touch driver specific information in a handle object. </p>
<p> This function allows the user to communicate directly with a driver in association with a handle object. The driver defines what operations can be preformed. </p>
<p> pass the driver to control a specific driver pass NULL for driver for XIO specific cntls pass GLOBUS_XIO_QUERY for driver to try each driver in order until success</p>
<h3>globus_result_t globus_xio_handle_create (globus_xio_handle_t *handle, globus_xio_stack_tstack)</h3>
<p> Initialize a handle for client opens </p>
<p> This function will initialize a handle for active opens (client side connections).</p>
<h3>globus_result_t globus_xio_handle_create_from_url (globus_xio_handle_t *out_h, const char *scheme, globus_xio_attr_tattr, char *param_string)</h3>
<p> Initializes a handle based on the scheme given. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>out_h</i> An uninitialized handle that will be initialized in the function to correspond to the scheme given. This handle should be used for any I/O operations.<br />
 <i>scheme</i> A string containing the protocol which the handle should be initialized to. The string can either be a protocol by itself, for example, &#8216;http&#8217;, or a complete scheme such as &#8216;<a rel="nofollow" href="http://www.example.com'.">http://www.example.com&#8217;.</a><br />
 <i>attr</i> Attribute to be used for setting parameter string. It is initialized by the function. Can be NULL if attributes are not being used.<br />
 <i>param_string</i> A string containing attributes to be set for the drivers associated with the scheme. This should be in the form &#8216;protocol1:option1=value1;option2=value2,protocol2:option1=value1;<br />
&nbsp;<wbr>option2=value2&#8242;&nbsp;<wbr>Can be NULL if attributes are not being used.&nbsp;<wbr></dl>
<h3>globus_result_t globus_xio_open (globus_xio_handle_thandle, const char *contact_string, globus_xio_attr_tattr)</h3>
<p> blocking open</p>
<h3>globus_result_t globus_xio_read (globus_xio_handle_thandle, globus_byte_t *buffer, globus_size_tbuffer_length, globus_size_twaitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_tdata_desc)</h3>
<p> Read data from a handle</p>
<h3>globus_result_t globus_xio_readv (globus_xio_handle_thandle, globus_xio_iovec_t *iovec, intiovec_count, globus_size_twaitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_tdata_desc)</h3>
<p> Read data from a handle into a globus_xio_iovec_t (struct iovec)</p>
<h3>globus_result_t globus_xio_register_close (globus_xio_handle_thandle, globus_xio_attr_tattr, <code>globus_xio_callback_t</code>cb, void *user_arg)</h3>
<p> Close a handle </p>
<p> This functions servers as a destroy for the handle. As soon as the operations completes (the callback is called). The handle is destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to be closed.<br />
 <i>attr</i> how to close attribute<br />
 <i>cb</i> The function to be called when the close operation completes.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.</dl>
<h3>globus_result_t globus_xio_register_open (globus_xio_handle_thandle, const char *contact_string, globus_xio_attr_tattr, <code>globus_xio_callback_t</code>cb, void *user_arg)</h3>
<p> Open a handle </p>
<p> Creates an open handle based on the state contained in the given stack. </p>
<p> No operation can be preformed on a handle until it is initialized and then opened. If an already open handle used the information contained in that handle will be destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle created with <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code> that is to be opened.<br />
 <i>attr</i> how to open attribute. can be NULL<br />
 <i>cb</i> The function to be called when the open operation completes.<br />
 <i>user_arg</i> A user pointer that will be threaded through to the callback.<br />
 <i>contact_string</i> An url describing the resource. NULL is allowed. Drivers interpret the various parts of this url as described in their documentation. An alternative form is also supported: if contact_string does not specify a scheme (e.g. <a rel="nofollow" href="http://)">http://)</a> and it contains a &#8216;:&#8217;, it will be parsed as a host:port pair. if it does not contain a &#8216;:&#8217;, it will be parsed as the path</dl>
<p> the following are examples of valid formats: </p>
<pre><code>
   &lt;path to file&gt;
   host-name ':' &lt;service or port&gt;
   'file:' &lt;path to file&gt;
   &lt;scheme&gt; '://' [ '/' [ &lt;path to resource&gt; ]  ]
   &lt;scheme&gt; '://' location [ '/' [ &lt;path to resource&gt; ] ]
     location:
         [ auth-part ] host-part
     auth-part:
         &lt;user&gt; [ ':' &lt;password&gt; ] '@' 
     host-part:
         [ '&lt;' &lt;subject&gt; '&gt;' ] host-name [ ':' &lt;port or service&gt; ]
     host-name:
         &lt;hostname&gt; | &lt;dotted quad&gt; | '[' &lt;ipv6 address&gt; ']'
   
</code></pre>
<p> Except for use as the above delimiters, the following special characters MUST be encoded with the %HH format where H == hex char. </p>
<pre>
   '/' and '@' in location except subject
   '&lt;' and '&gt;' in location
   ':' everywhere except ipv6 address and subject
   '%' everywhere (can be encoded with %HH or %%)
   
</pre>
<p>&nbsp;<wbr></p>
<h3>globus_result_t globus_xio_register_read (globus_xio_handle_thandle, globus_byte_t *buffer, globus_size_tbuffer_length, globus_size_twaitforbytes, globus_xio_data_descriptor_tdata_desc, <code>globus_xio_data_callback_t</code>cb, void *user_arg)</h3>
<p> Read data from a handle</p>
<h3>globus_result_t globus_xio_register_readv (globus_xio_handle_thandle, globus_xio_iovec_t *iovec, intiovec_count, globus_size_twaitforbytes, globus_xio_data_descriptor_tdata_desc, <code>globus_xio_iovec_callback_t</code>cb, void *user_arg)</h3>
<p> Read data from a handle into a globus_xio_iovec_t (struct iovec)</p>
<h3>globus_result_t globus_xio_register_write (globus_xio_handle_thandle, globus_byte_t *buffer, globus_size_tbuffer_length, globus_size_twaitforbytes, globus_xio_data_descriptor_tdata_desc, <code>globus_xio_data_callback_t</code>cb, void *user_arg)</h3>
<p> Write data to a handle</p>
<h3>globus_result_t globus_xio_register_writev (globus_xio_handle_thandle, globus_xio_iovec_t *iovec, intiovec_count, globus_size_twaitforbytes, globus_xio_data_descriptor_tdata_desc, <code>globus_xio_iovec_callback_t</code>cb, void *user_arg)</h3>
<p> Write data to a handle from a globus_xio_iovec_t (struct iovec)</p>
<h3>globus_result_t globus_xio_server_accept (globus_xio_handle_t *out_handle, globus_xio_server_tserver)</h3>
<p> Accept a connection </p>
<p> This function will accept a connection on the given server object and the parameter out_handle will be valid if the function returns successfully.</p>
<h3>globus_result_t globus_xio_server_close (globus_xio_server_tserver)</h3>
<p> A blocking server close</p>
<h3>globus_result_t globus_xio_server_cntl (globus_xio_server_tserver, globus_xio_driver_tdriver, intcmd, &#8230;)</h3>
<p> Touch driver specific information in a server object. </p>
<p> This function allows the user to communicate directly with a driver in association with a server object. The driver defines what operations can be preformed.</p>
<h3>globus_result_t globus_xio_server_create (globus_xio_server_t *server, globus_xio_attr_tserver_attr, globus_xio_stack_tstack)</h3>
<p> Create a server object. </p>
<p> This function allows the user to create a server object which can then be used to accept connections. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> An out parameter. Once the function successfully returns this will point to a valid server object.<br />
 <i>server_attr</i> an attribute structure used to alter the default server initialization. This will mostly be used in a driver specific manner. can be NULL.<br />
 <i>stack</i></dl>
<h3>globus_result_t globus_xio_server_get_contact_string (globus_xio_server_tserver, char **contact_string)</h3>
<p> get contact string </p>
<p> This function allows the user to get the contact string for a server. this string could be used as the contact string for the client side. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> An initialized server handle created with <code>globus_xio_server_create()</code><br />
 <i>contact_string</i> an out variable. Will point to a newly allocated string on success. must be freed by the caller.</dl>
<h3>globus_result_t globus_xio_server_register_accept (globus_xio_server_tserver, <code>globus_xio_accept_callback_t</code>cb, void *user_arg)</h3>
<p> Asynchronous accept. </p>
<p> This function posts an nonblocking accept. Once the operation has completed the user function pointed to by the parameter cb is called.</p>
<h3>globus_result_t globus_xio_server_register_close (globus_xio_server_tserver, <code>globus_xio_server_callback_t</code>cb, void *user_arg)</h3>
<p> post a close on a server object </p>
<p> This function registers a close operation on a server. When the user function pointed to by parameter cb is called the server object is closed.</p>
<h3>globus_result_t globus_xio_stack_copy (globus_xio_stack_t *dst, globus_xio_stack_tsrc)</h3>
<p> Copy a stack object</p>
<h3>globus_result_t globus_xio_stack_destroy (globus_xio_stack_tstack)</h3>
<p> Destroy a stack object.</p>
<h3>globus_result_t globus_xio_stack_init (globus_xio_stack_t *stack, globus_xio_attr_tstack_attr)</h3>
<p> Initialize a stack object</p>
<h3>globus_result_t globus_xio_stack_push_driver (globus_xio_stack_tstack, globus_xio_driver_tdriver)</h3>
<p> Push a driver onto a stack. </p>
<p> No attrs are associated with a driver. The stack represents the ordered lists of transform drivers and 1 transport driver. The transport driver must be pushed on first.</p>
<h3>globus_result_t globus_xio_write (globus_xio_handle_thandle, globus_byte_t *buffer, globus_size_tbuffer_length, globus_size_twaitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_tdata_desc)</h3>
<p> Write data to a handle</p>
<h3>globus_result_t globus_xio_writev (globus_xio_handle_thandle, globus_xio_iovec_t *iovec, intiovec_count, globus_size_twaitforbytes, globus_size_t *nbytes, globus_xio_data_descriptor_tdata_desc)</h3>
<p> Write data to a handle from a globus_xio_iovec_t (struct iovec)</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAR">Function Documentation</a></p>
<dd>
<dt><a href="#lbCI">Author</a></p>
<dd></dl>
