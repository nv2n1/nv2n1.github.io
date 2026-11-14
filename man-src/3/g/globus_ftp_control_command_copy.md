---
title: "globus_ftp_control_command_copy(3)"
name: "globus_ftp_control_command_copy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_control_command_copy/"
description: "GridFTP Server Control –"
---

<h2 class="name">NAME</h2>
<p> GridFTP Server Control &#8211; </p>
<p> Manage GridFTP Server Control Connections.</p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_ftp_control_server_callback_t</code> )(void *callback_arg, struct globus_ftp_control_server_s *server_handle, globus_object_t *error)<br />
 <i>Server callback</i> </p>
<p> A function with this signature can be used as general callbacks for the GridFTP server API. &quot;</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_control_server_handle_init</code> (globus_ftp_control_server_t *handle)<br />
 <i>Initialize a GridFTP server handle. </i><br />
 globus_result_t <code>globus_ftp_control_server_handle_destroy</code> (globus_ftp_control_server_t *handle)<br />
 <i>Destroy a GridFTP server handle. </i><br />
 globus_result_t <code>globus_ftp_control_server_listen</code> (globus_ftp_control_server_t *server_handle, unsigned short *port, <code>globus_ftp_control_server_callback_t</code> callback, void *callback_arg)<br />
 <i>Listen on for FTP Client Connections. </i><br />
 globus_result_t <code>globus_ftp_control_server_listen_ex</code> (globus_ftp_control_server_t *server_handle, globus_io_attr_t *attr, unsigned short *port, <code>globus_ftp_control_server_callback_t</code> callback, void *callback_arg)<br />
 <i>Listen on for FTP Client Connections. </i><br />
 globus_result_t <code>globus_ftp_control_command_init</code> (globus_ftp_control_command_t *command, char *raw_command, <code>globus_ftp_control_auth_info_t</code> *auth_info)<br />
 <i>Initialize a GridFTP command. </i><br />
 globus_result_t <code>globus_ftp_control_command_destroy</code> (globus_ftp_control_command_t *command)<br />
 <i>Destroy a GridFTP command. </i><br />
 globus_result_t <code>globus_ftp_control_command_copy</code> (globus_ftp_control_command_t *dest, globus_ftp_control_command_t *src)<br />
 <i>Copy of GridFTP command. </i><br />
 globus_result_t <code>globus_ftp_control_server_stop</code> (globus_ftp_control_server_t *listener, <code>globus_ftp_control_server_callback_t</code> callback, void *callback_arg)<br />
 <i>Stop listening for GridFTP client connections. </i><br />
 globus_result_t <code>globus_ftp_control_server_accept</code> (globus_ftp_control_server_t *listener, globus_ftp_control_handle_t *handle, <code>globus_ftp_control_callback_t</code> callback, void *callback_arg)<br />
 <i>Accept a Client Connection. </i><br />
 globus_result_t <code>globus_ftp_control_server_authenticate</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_requirements_t</code> auth_requirements, <code>globus_ftp_control_auth_callback_t</code> callback, void *callback_arg)<br />
 <i>Authenticate a GridFTP Client Connection. </i><br />
 globus_result_t <code>globus_ftp_control_read_commands</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_command_callback_t</code> callback, void *callback_arg)<br />
 <i>Read GridFTP commands. </i><br />
 globus_result_t <code>globus_ftp_control_send_response</code> (globus_ftp_control_handle_t *handle, const char *respspec, <code>globus_ftp_control_callback_t</code> callback, void *callback_arg,&#8230;)<br />
 <i>Send a GridFTP response. </i></p>
<h2>Detailed Description</h2>
<p> Manage GridFTP Server Control Connections. </p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_control_server_callback_t)(void *callback_arg, struct globus_ftp_control_server_s *server_handle, globus_object_t *error)</h3>
<p> Server callback </p>
<p> A function with this signature can be used as general callbacks for the GridFTP server API. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server_handle</i> The server handle associated with callback.<br />
 <i>result</i> Indicates if the operation completed successfully or if a failure occurred.<br />
 <i>callback_arg</i> The user argument passed to the callback function.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_control_command_copy (globus_ftp_control_command_t *dest, globus_ftp_control_command_t *src)</h3>
<p> Copy of GridFTP command. This function should be called when the user needs to make a copy of a command structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dest</i> The area of memory that the command structure is copied to.<br />
 <i>src</i> The command structure to be copied.</dl>
<h3>globus_result_t globus_ftp_control_command_destroy (globus_ftp_control_command_t *command)</h3>
<p> Destroy a GridFTP command. This function frees up the memory allocated to the command argument. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>command</i> The command structure whose associated memory is to be freed</dl>
<h3>globus_result_t globus_ftp_control_command_init (globus_ftp_control_command_t *command, char *raw_command, <code>globus_ftp_control_auth_info_t</code> *auth_info)</h3>
<p> Initialize a GridFTP command. This function initializes a command structure based on a null terminated string representing one line of input from the client. The command structure is used as a convenience to determine what command the client issued. This function parses a command string sent by a client and populates the command argument appropriately. In the GSSAPI case it will also decode and unwrap the command before parsing it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>command</i> A pointer to the command structure to be initialized<br />
 <i>raw_command</i> A null terminated line of client input. Should contain one command.<br />
 <i>auth_info</i> Authentication information needed for unwrapping a command</dl>
<h3>globus_result_t globus_ftp_control_read_commands (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_command_callback_t</code>callback, void *callback_arg)</h3>
<p> Read GridFTP commands. This function begins reading control commands on a globus_ftp_control_handle_t. When a command is read the callback function is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The control connection handle that commands will be read from. Prior to calling this the function globus_ftp_control_handle_t must be populated via a call to globus_ftp_control_accept().<br />
 <i>callback</i> The user callback that will be called when commands are read.<br />
 <i>callback_arg</i> The user argument passed to the callback.</dl>
<h3>globus_result_t globus_ftp_control_send_response (globus_ftp_control_handle_t *handle, const char *respspec, <code>globus_ftp_control_callback_t</code>callback, void *callback_arg, &#8230;)</h3>
<p> Send a GridFTP response. This function sends a GridFTP formatted response to the client. When a command callback is received the user calls this function to respond to the clients request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The control connection to send the response across.<br />
 <i>respspec</i> A formated string representing the users response.<br />
 <i>callback</i> The user callback that will be called when the response has been sent.<br />
 <i>callback_arg</i> The user argument passed to the callback.</dl>
<h3>globus_result_t globus_ftp_control_server_accept (globus_ftp_control_server_t *listener, globus_ftp_control_handle_t *handle, <code>globus_ftp_control_callback_t</code>callback, void *callback_arg)</h3>
<p> Accept a Client Connection. This function is called to accept a connection request from a client. </p>
<p> When the listen callback is called (see globus_ftp_control_server_listen) a client has requested a connection. This function must be called to accept that user connection request. Once the connection is established or if a error occurs, the callback function is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> The server object that received the connection request.<br />
 <i>handle</i> The control connection object. This structure will be populated and passed to the callback when the client is authorized. This structure represents the control connection between the server and client. It will be used to read commands from the client and send responses to the client.]<br />
 <i>callback</i> The function called when the client connection has been accepted.<br />
 <i>callback_arg</i> The user argument passed to the callback.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This functions assumes the server and control handles have been initialized prior to calling this function.</dl>
<h3>globus_result_t globus_ftp_control_server_authenticate (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_requirements_t</code>auth_requirements, <code>globus_ftp_control_auth_callback_t</code>callback, void *callback_arg)</h3>
<p> Authenticate a GridFTP Client Connection. This function is called to authenticate a connection from a client. </p>
<p> After a client connection has been accepted (using the globus_ftp_control_server_accept call), this function should be called to authenticate the client. The caller of this function may specify certain authentication requirements using the auth_requirements parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The control connection object. This structure will be populated and passed to the callback when the client is authorized. This structure represents the control connection between the server and client. It will be used to read commands from the client and send responses to the client.]<br />
 <i>auth_requirements</i> This structure represents the authentication requirements that the user has for a given connection. For example GridFTP user name, password, and account.<br />
 <i>callback</i> The function called when the client authentication has been accepted or rejected.<br />
 <i>callback_arg</i> The user argument passed to the callback.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> It is up to the user of this function to send the reply to the last command of the authentication sequence. </p>
<p> This functions assumes the server and control handles have been initialized prior to calling this function.</dl>
<h3>globus_result_t globus_ftp_control_server_handle_destroy (globus_ftp_control_server_t *handle)</h3>
<p> Destroy a GridFTP server handle. This function will free up all dynamically allocated memory associated with a given globus ftp server handle. It will also remove the handle from a list used by the module activation/deactivation functions. This function should only be called after a call to globus_ftp_control_server_stop. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> success</p>
<dt>&bull;</p>
<dd> invalid handle</p>
<dt>&bull;</p>
<dd> handle is still in listening state</dl>
</dl>
<h3>globus_result_t globus_ftp_control_server_handle_init (globus_ftp_control_server_t *handle)</h3>
<p> Initialize a GridFTP server handle. This function will set up (i.e. initialize all mutexes and variables) a globus ftp server handle. It will also enter the handle in a list used by the module activation/deactivation functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to initialize.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> invalid handle</dl>
</dl>
<h3>globus_result_t globus_ftp_control_server_listen (globus_ftp_control_server_t *server_handle, unsigned short *port, <code>globus_ftp_control_server_callback_t</code>callback, void *callback_arg)</h3>
<p> Listen on for FTP Client Connections. This function starts the listening on *port for connections from ftp clients. When a connection request is made callback is called and passed callback_arg. Upon return from this function the server_handle structure is initialized. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server_handle</i> A pointer to a initialized server handle.<br />
 <i>port</i> A pointer to the port to listen on. If the initial value is zero it will be set to the default value.<br />
 <i>callback</i> The callback function called when connection requests are made.<br />
 <i>callback_arg</i> The user argument passed to the callback function when connection requests are made.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> I&#8217;m not providing any mechanism for making sure that this function is only called once. Is this needed?</dl>
<h3>globus_result_t globus_ftp_control_server_listen_ex (globus_ftp_control_server_t *server_handle, globus_io_attr_t *attr, unsigned short *port, <code>globus_ftp_control_server_callback_t</code>callback, void *callback_arg)</h3>
<p> Listen on for FTP Client Connections. This function starts the listening on *port for connections from ftp clients. When a connection request is made callback is called and passed callback_arg. Upon return from this function the server_handle structure is initialized. </p>
<p> This is an extendend version of <code>globus_ftp_control_server_listen()</code> that provides additional control over the listening socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server_handle</i> A pointer to a initialized server handle.<br />
 <i>attr</i> A pointer to a globus_io_attr_t providing additional attributes for the listening socket.<br />
 <i>port</i> A pointer to the port to listen on. If the initial value is zero it will be set to the default value.<br />
 <i>callback</i> The callback function called when connection requests are made.<br />
 <i>callback_arg</i> The user argument passed to the callback function when connection requests are made.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> I&#8217;m not providing any mechanism for making sure that this function is only called once. Is this needed?</dl>
<h3>globus_result_t globus_ftp_control_server_stop (globus_ftp_control_server_t *listener, <code>globus_ftp_control_server_callback_t</code>callback, void *callback_arg)</h3>
<p> Stop listening for GridFTP client connections. This function stops listening on the given listener object for client connections. All existing client connections are left open. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener</i> the globus_ftp_control_server_t object that should no longer listen for connections.<br />
 <i>callback</i> The user callback that will be called when the server structure is no longer listening.<br />
 <i>callback_arg</i> The user argument that is passed into callback.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_control from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAU">Author</a></p>
<dd></dl>
