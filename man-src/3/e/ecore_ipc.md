---
title: "ecore_ipc(3)"
name: "ecore_ipc"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_ipc/"
description: "Ecore_Ipc.h – Ecore inter-process communication functions."
---

<p>Ecore_Ipc.h &#8211; Ecore inter-process communication functions. </p>
<h2>Synopsis</h2>
<h3>Typedefs</h3>
<p>typedef void <code>Ecore_Ipc_Server</code><br />
 <i>An IPC connection handle. </i><br />
 typedef void <code>Ecore_Ipc_Client</code><br />
 <i>An IPC connection handle. </i></p>
<h3>Functions</h3>
<p>EAPI unsigned short <code>_ecore_ipc_swap_16</code> (unsigned short v)<br />
 <i>Macros used for generic data packing. </i><br />
 EAPI int <code>ecore_ipc_init</code> (void)<br />
 <i>Initialises the Ecore IPC library. </i><br />
 EAPI int <code>ecore_ipc_shutdown</code> (void)<br />
 <i>Shuts down the Ecore IPC library. </i><br />
 EAPI <code>Ecore_Ipc_Server</code> * <code>ecore_ipc_server_add</code> (Ecore_Ipc_Type type, const char *name, int port, const void *data)<br />
 <i>Creates an IPC server that listens for connections. </i><br />
 EAPI <code>Ecore_Ipc_Server</code> * <code>ecore_ipc_server_connect</code> (Ecore_Ipc_Type type, char *name, int port, const void *data)<br />
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
 <i>Sends a message to the given IPC server. </i><br />
 EAPI void <code>ecore_ipc_server_client_limit_set</code> (<code>Ecore_Ipc_Server</code> *svr, int client_limit, char reject_excess_clients)<br />
 <i>Sets a limit on the number of clients that can be handled concurrently by the given server, and a policy on what to do if excess clients try to connect. </i><br />
 EAPI void <code>ecore_ipc_server_data_size_max_set</code> (<code>Ecore_Ipc_Server</code> *srv, int size)<br />
 <i>Sets the max data payload size for an Ipc message in bytes. </i><br />
 EAPI int <code>ecore_ipc_server_data_size_max_get</code> (<code>Ecore_Ipc_Server</code> *srv)<br />
 <i>Gets the max data payload size for an Ipc message in bytes. </i><br />
 EAPI char * <code>ecore_ipc_server_ip_get</code> (<code>Ecore_Ipc_Server</code> *svr)<br />
 <i>Gets the IP address of a server that has been connected to. </i><br />
 EAPI void <code>ecore_ipc_server_flush</code> (<code>Ecore_Ipc_Server</code> *svr)<br />
 <i>Flushes all pending data to the given server. </i><br />
 EAPI int <code>ecore_ipc_client_send</code> (<code>Ecore_Ipc_Client</code> *cl, int major, int minor, int ref, int ref_to, int response, const void *data, int size)<br />
 <i>Sends a message to the given IPC client. </i><br />
 EAPI <code>Ecore_Ipc_Server</code> * <code>ecore_ipc_client_server_get</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Retrieves the IPC server that the given IPC client is connected to. </i><br />
 EAPI void * <code>ecore_ipc_client_del</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Closes the connection and frees memory allocated to the given IPC client. </i><br />
 EAPI void <code>ecore_ipc_client_data_set</code> (<code>Ecore_Ipc_Client</code> *cl, const void *data)<br />
 <i>Sets the IPC data associated with the given IPC client to </i>data.<br />
 EAPI void * <code>ecore_ipc_client_data_get</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Retrieves the data that has been associated with the given IPC client. </i><br />
 EAPI void <code>ecore_ipc_client_data_size_max_set</code> (<code>Ecore_Ipc_Client</code> *cl, int size)<br />
 <i>Sets the max data payload size for an Ipc message in bytes. </i><br />
 EAPI int <code>ecore_ipc_client_data_size_max_get</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Sets the max data payload size for an Ipc message in bytes. </i><br />
 EAPI char * <code>ecore_ipc_client_ip_get</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Gets the IP address of a client that has been connected to. </i><br />
 EAPI void <code>ecore_ipc_client_flush</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Flushes all pending data to the given client. </i><br />
 EAPI int <code>ecore_ipc_ssl_available_get</code> (void)<br />
 <i>Returns if SSL support is available. </i></p>
<h2>Detailed Description</h2>
<p>Ecore inter-process communication functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_ipc_client_data_size_max_get (<code>Ecore_Ipc_Client</code> * cl)</h3>
<p>Sets the max data payload size for an Ipc message in bytes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.<br />
 <i>size</i> The maximum data payload size in bytes.</dl>
<h3>EAPI void ecore_ipc_client_data_size_max_set (<code>Ecore_Ipc_Client</code> * cl, int size)</h3>
<p>Sets the max data payload size for an Ipc message in bytes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>client</i> The given client.<br />
 <i>size</i> The maximum data payload size in bytes.</dl>
<h3>EAPI void ecore_ipc_client_flush (<code>Ecore_Ipc_Client</code> * cl)</h3>
<p>Flushes all pending data to the given client. </p>
<p> Will return when done. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> References ecore_con_client_flush().</p>
<h3>EAPI char* ecore_ipc_client_ip_get (<code>Ecore_Ipc_Client</code> * cl)</h3>
<p>Gets the IP address of a client that has been connected to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an internal string that contains the IP address of the connected server in the form &#8216;XXX.YYY.ZZZ.AAA&#8217; IP notation. This string should not be modified or trusted to stay valid after deletion for the cl object. If no IP is known NULL is returned.</dl>
<p> References ecore_con_client_ip_get().</p>
<h3>EAPI void ecore_ipc_server_client_limit_set (<code>Ecore_Ipc_Server</code> * svr, int client_limit, char reject_excess_clients)</h3>
<p>Sets a limit on the number of clients that can be handled concurrently by the given server, and a policy on what to do if excess clients try to connect. </p>
<p> Beware that if you set this once ecore is already running, you may already have pending CLIENT_ADD events in your event queue. Those clients have already connected and will not be affected by this call. Only clients subsequently trying to connect will be affected. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.<br />
 <i>client_limit</i> The maximum number of clients to handle concurrently. -1 means unlimited (default). 0 effectively disables the server.<br />
 <i>reject_excess_clients</i> Set to 1 to automatically disconnect excess clients as soon as they connect if you are already handling client_limit clients. Set to 0 (default) to just hold off on the &#8216;accept()&#8217; system call until the number of active clients drops. This causes the kernel to queue up to 4096 connections (or your kernel&#8217;s limit, whichever is lower).</dl>
<p> References ecore_con_server_client_limit_set().</p>
<h3>EAPI int ecore_ipc_server_data_size_max_get (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Gets the max data payload size for an Ipc message in bytes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum data payload in bytes.</dl>
<h3>EAPI void ecore_ipc_server_data_size_max_set (<code>Ecore_Ipc_Server</code> * svr, int size)</h3>
<p>Sets the max data payload size for an Ipc message in bytes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.<br />
 <i>size</i> The maximum data payload size in bytes.</dl>
<h3>EAPI void ecore_ipc_server_flush (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Flushes all pending data to the given server. </p>
<p> Will return when done. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> References ecore_con_server_flush().</p>
<h3>EAPI char* ecore_ipc_server_ip_get (<code>Ecore_Ipc_Server</code> * svr)</h3>
<p>Gets the IP address of a server that has been connected to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svr</i> The given server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an internal string that contains the IP address of the connected server in the form &#8216;XXX.YYY.ZZZ.AAA&#8217; IP notation. This string should not be modified or trusted to stay valid after deletion for the svr object. If no IP is known NULL is returned.</dl>
<p> References ecore_con_server_ip_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
