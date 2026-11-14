---
title: "ecore_con_server_group(3)"
name: "ecore_con_server_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_con_server_group/"
description: "Ecore Connection Server Functions – Functions that operate on Ecore server objects."
---

<p>Ecore Connection Server Functions &#8211; Functions that operate on Ecore server objects. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Con_Server</code> * <code>ecore_con_server_add</code> (Ecore_Con_Type compl_type, const char *name, int port, const void *data)<br />
 <i>Creates a server to listen for connections. </i><br />
 EAPI <code>Ecore_Con_Server</code> * <code>ecore_con_server_connect</code> (Ecore_Con_Type compl_type, const char *name, int port, const void *data)<br />
 <i>Creates a server object to represent the server listening at the given port. </i><br />
 EAPI void * <code>ecore_con_server_del</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Closes the connection and frees the given server. </i><br />
 EAPI void * <code>ecore_con_server_data_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Retrieves the data associated with the given server. </i><br />
 EAPI int <code>ecore_con_server_connected_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Retrieves whether the given server is currently connected. </i><br />
 EAPI Ecore_List * <code>ecore_con_server_clients_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Retrieves the current list of clients. </i><br />
 EAPI int <code>ecore_con_server_send</code> (<code>Ecore_Con_Server</code> *svr, const void *data, int size)<br />
 <i>Sends the given data to the given server. </i><br />
 EAPI void <code>ecore_con_server_client_limit_set</code> (<code>Ecore_Con_Server</code> *svr, int client_limit, char reject_excess_clients)<br />
 <i>Sets a limit on the number of clients that can be handled concurrently by the given server, and a policy on what to do if excess clients try to connect. </i><br />
 EAPI char * <code>ecore_con_server_ip_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Gets the IP address of a server that has been connected to. </i><br />
 EAPI void <code>ecore_con_server_flush</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Flushes all pending data to the given server. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on Ecore server objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Ecore_Con_Server</code>* ecore_con_server_add (Ecore_Con_Type compl_type, const char * name, int port, const void * data)</h3>
<p>Creates a server to listen for connections. </p>
<p> The socket on which the server listens depends on the connection type: </p>
<dl COMPACT>
<dt>*</p>
<dd>If <i>compl_type</i> is ECORE_CON_LOCAL_USER, the server will listen on the Unix socket &#8216;~/.ecore/[name]/[port]&#8217;.</p>
<dt>*</p>
<dd>If <i>compl_type</i> is ECORE_CON_LOCAL_SYSTEM, the server will listen on Unix socket &#8216;/tmp/.ecore_service|[name]|[port]&#8217;.</p>
<dt>*</p>
<dd>If <i>compl_type</i> is ECORE_CON_REMOTE_SYSTEM, the server will listen on TCP port port.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>compl_type</i> The connection type.<br />
 <i>name</i> Name to associate with the socket. It is used when generating the socket name of a Unix socket. Though it is not used for the TCP socket, it still needs to be a valid character array. NULL will not be accepted.<br />
 <i>port</i> Number to identify socket. When a Unix socket is used, it becomes part of the socket name. When a TCP socket is used, it is used as the TCP port.<br />
 <i>data</i> Data to associate with the created Ecore_Con_Server object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Ecore_Con_Server.</dl>
<p> References ECORE_FD_READ, ecore_list_append(), ecore_list_new(), ecore_main_fd_handler_add(), and ecore_main_fd_handler_del(). </p>
<p> Referenced by ecore_ipc_server_add().</p>
<h3>EAPI void ecore_con_server_client_limit_set (<code>Ecore_Con_Server</code> * svr, int client_limit, char reject_excess_clients)</h3>
<p>Sets a limit on the number of clients that can be handled concurrently by the given server, and a policy on what to do if excess clients try to connect. </p>
<p> Beware that if you set this once ecore is already running, you may already have pending CLIENT_ADD events in your event queue. Those clients have already connected and will not be affected by this call. Only clients subsequently trying to connect will be affected. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.<br />
 <i>client_limit</i> The maximum number of clients to handle concurrently. -1 means unlimited (default). 0 effectively disables the server.<br />
 <i>reject_excess_clients</i> Set to 1 to automatically disconnect excess clients as soon as they connect if you are already handling client_limit clients. Set to 0 (default) to just hold off on the &#8216;accept()&#8217; system call until the number of active clients drops. This causes the kernel to queue up to 4096 connections (or your kernel&#8217;s limit, whichever is lower).</dl>
<p> Referenced by ecore_ipc_server_client_limit_set().</p>
<h3>EAPI Ecore_List* ecore_con_server_clients_get (<code>Ecore_Con_Server</code> * svr)</h3>
<p>Retrieves the current list of clients. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The list of clients on this server.</dl>
<h3>EAPI <code>Ecore_Con_Server</code>* ecore_con_server_connect (Ecore_Con_Type compl_type, const char * name, int port, const void * data)</h3>
<p>Creates a server object to represent the server listening at the given port. </p>
<p> The socket to which the server connects depends on the connection type: </p>
<dl COMPACT>
<dt>*</p>
<dd>If <i>compl_type</i> is ECORE_CON_LOCAL_USER, the function will connect to the server listening on the Unix socket &#8216;~/.ecore/[name]/[port]&#8217;.</p>
<dt>*</p>
<dd>If <i>compl_type</i> is ECORE_CON_LOCAL_SYSTEM, the function will connect to the server listening on the Unix socket &#8216;/tmp/.ecore_service|[name]|[port]&#8217;.</p>
<dt>*</p>
<dd>If <i>compl_type</i> is ECORE_CON_REMOTE_SYSTEM, the function will connect to the server listening on the TCP port &#8216;[name]:[port]&#8217;.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>compl_type</i> The connection type.<br />
 <i>name</i> Name used when determining what socket to connect to. It is used to generate the socket name when the socket is a Unix socket. It is used as the hostname when connecting with a TCP socket.<br />
 <i>port</i> Number to identify the socket to connect to. Used when generating the socket name for a Unix socket, or as the TCP port when connecting to a TCP socket.<br />
 <i>data</i> Data to associate with the created Ecore_Con_Server object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Ecore_Con_Server.</dl>
<p> References ecore_event_add(), ECORE_FD_READ, ecore_list_append(), ecore_list_new(), ecore_main_fd_handler_add(), and ecore_main_fd_handler_del(). </p>
<p> Referenced by ecore_ipc_server_connect().</p>
<h3>EAPI int ecore_con_server_connected_get (<code>Ecore_Con_Server</code> * svr)</h3>
<p>Retrieves whether the given server is currently connected. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Check that this function does what the documenter believes it does.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the server is connected. 0 otherwise.</dl>
<p> Referenced by ecore_ipc_server_connected_get().</p>
<h3>EAPI void* ecore_con_server_data_get (<code>Ecore_Con_Server</code> * svr)</h3>
<p>Retrieves the data associated with the given server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The associated data.</dl>
<p> Referenced by ecore_ipc_client_del(), and ecore_ipc_client_server_get().</p>
<h3>EAPI void* ecore_con_server_del (<code>Ecore_Con_Server</code> * svr)</h3>
<p>Closes the connection and frees the given server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Data associated with the server when it was created.</dl>
<p> References ecore_list_goto(), ecore_list_remove(), and ecore_main_fd_handler_del(). </p>
<p> Referenced by ecore_ipc_server_del().</p>
<h3>EAPI void ecore_con_server_flush (<code>Ecore_Con_Server</code> * svr)</h3>
<p>Flushes all pending data to the given server. </p>
<p> Will return when done. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> Referenced by ecore_ipc_server_flush().</p>
<h3>EAPI char* ecore_con_server_ip_get (<code>Ecore_Con_Server</code> * svr)</h3>
<p>Gets the IP address of a server that has been connected to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an internal string that contains the IP address of the connected server in the form &#8216;XXX.YYY.ZZZ.AAA&#8217; IP notation. This string should not be modified or trusted to stay valid after deletion for the svr object. If no IP is known NULL is returned.</dl>
<p> Referenced by ecore_ipc_server_ip_get().</p>
<h3>EAPI int ecore_con_server_send (<code>Ecore_Con_Server</code> * svr, const void * data, int size)</h3>
<p>Sends the given data to the given server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.<br />
 <i>data</i> The given data.<br />
 <i>size</i> Length of the data, in bytes, to send.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of bytes sent. 0 will be returned if there is an error.</dl>
<p> References ECORE_FD_READ, ECORE_FD_WRITE, and ecore_main_fd_handler_active_set(). </p>
<p> Referenced by ecore_ipc_server_send().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
