---
title: "ecore_ipc_server_group(3)"
name: "ecore_ipc_server_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_ipc_server_group/"
description: "IPC Server Functions – Functions the deal with IPC server objects."
---

<p>IPC Server Functions &#8211; Functions the deal with IPC server objects. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Ipc_Server</code> * <code>ecore_ipc_server_add</code> (Ecore_Ipc_Type compl_type, const char *name, int port, const void *data)<br />
 <i>Creates an IPC server that listens for connections. </i><br />
 EAPI <code>Ecore_Ipc_Server</code> * <code>ecore_ipc_server_connect</code> (Ecore_Ipc_Type compl_type, char *name, int port, const void *data)<br />
 <i>Creates an IPC server object to represent the IPC server listening on the given port. </i><br />
 EAPI void * <code>ecore_ipc_server_del</code> (<code>Ecore_Ipc_Server</code> *svr)<br />
 <i>Closes the connection and frees the given IPC server. </i><br />
 EAPI void * <code>ecore_ipc_server_data_get</code> (<code>Ecore_Ipc_Server</code> *svr)<br />
 <i>Retrieves the data associated with the given IPC server. </i><br />
 EAPI int <code>ecore_ipc_server_connected_get</code> (<code>Ecore_Ipc_Server</code> *svr)<br />
 <i>Retrieves whether the given IPC server is currently connected. </i><br />
 EAPI Ecore_List * <code>ecore_ipc_server_clients_get</code> (<code>Ecore_Ipc_Server</code> *svr)<br />
 <i>Retrieves the list of clients for this server. </i><br />
 EAPI int <code>ecore_ipc_server_send</code> (<code>Ecore_Ipc_Server</code> *svr, int major, int minor, int ref, int ref_to, int response, const void *data, int size)<br />
 <i>Sends a message to the given IPC server. </i></p>
<h2>Detailed Description</h2>
<p>Functions the deal with IPC server objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Ecore_Ipc_Server</code>* ecore_ipc_server_add (Ecore_Ipc_Type compl_type, const char * name, int port, const void * data)</h3>
<p>Creates an IPC server that listens for connections. </p>
<p> For more details about the compl_type, name and port parameters, see the <code>ecore_con_server_add</code> documentation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>compl_type</i> The connection type.<br />
 <i>name</i> Name to associate with the socket used for connection.<br />
 <i>port</i> Number to identify with socket used for connection.<br />
 <i>data</i> Data to associate with the IPC server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>New IPC server. If there is an error, NULL is returned.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Need to add protocol type parameter to this function.</dl>
<p> References ecore_con_server_add(), ecore_list_init(), and ecore_list_new().</p>
<h3>EAPI Ecore_List* ecore_ipc_server_clients_get (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Retrieves the list of clients for this server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given IPC server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Ecore_List with the clients.</dl>
<h3>EAPI <code>Ecore_Ipc_Server</code>* ecore_ipc_server_connect (Ecore_Ipc_Type compl_type, char * name, int port, const void * data)</h3>
<p>Creates an IPC server object to represent the IPC server listening on the given port. </p>
<p> For more details about the compl_type, name and port parameters, see the <code>ecore_con_server_connect</code> documentation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>compl_type</i> The IPC connection type.<br />
 <i>name</i> Name used to determine which socket to use for the IPC connection.<br />
 <i>port</i> Number used to identify the socket to use for the IPC connection.<br />
 <i>data</i> Data to associate with the server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new IPC server. NULL is returned on error.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Need to add protocol type parameter.</dl>
<p> References ecore_con_server_connect().</p>
<h3>EAPI int ecore_ipc_server_connected_get (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Retrieves whether the given IPC server is currently connected. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given IPC server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the server is connected. 0 otherwise.</dl>
<p> References ecore_con_server_connected_get().</p>
<h3>EAPI void* ecore_ipc_server_data_get (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Retrieves the data associated with the given IPC server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given IPC server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The associated data.</dl>
<h3>EAPI void* ecore_ipc_server_del (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Closes the connection and frees the given IPC server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given IPC server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data associated with the server when it was created.</dl>
<p> References ecore_con_server_del(), ecore_ipc_client_del(), and ecore_list_destroy(). </p>
<p> Referenced by ecore_ipc_shutdown().</p>
<h3>EAPI int ecore_ipc_server_send (<code>Ecore_Ipc_Server</code> * svr, int major, int minor, int ref, int ref_to, int response, const void * data, int size)</h3>
<p>Sends a message to the given IPC server. </p>
<p> The content of the parameters, excluding the svr paramter, is up to the client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given IPC server.<br />
 <i>major</i> Major opcode of the message.<br />
 <i>minor</i> Minor opcode of the message.<br />
 <i>ref</i> Message reference number.<br />
 <i>ref_to</i> Reference number of the message this message refers to.<br />
 <i>response</i> Requires response.<br />
 <i>data</i> The data to send as part of the message.<br />
 <i>size</i> Length of the data, in bytes, to send.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes sent. 0 is returned if there is an error.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>This function needs to become an IPC message. </p>
<p> Fix up the documentation: Make sure what ref_to and response are.</dl>
<p> References ecore_con_server_send().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
