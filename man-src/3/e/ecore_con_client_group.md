---
title: "ecore_con_client_group(3)"
name: "ecore_con_client_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_con_client_group/"
description: "Ecore Connection Client Functions – Functions that operate on Ecore connection client objects."
---

<p>Ecore Connection Client Functions &#8211; Functions that operate on Ecore connection client objects. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_con_client_send</code> (<code>Ecore_Con_Client</code> *cl, const void *data, int size)<br />
 <i>Sends the given data to the given client. </i><br />
 EAPI <code>Ecore_Con_Server</code> * <code>ecore_con_client_server_get</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Retrieves the server representing the socket the client has connected to. </i><br />
 EAPI void * <code>ecore_con_client_del</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Closes the connection and frees memory allocated to the given client. </i><br />
 EAPI void <code>ecore_con_client_data_set</code> (<code>Ecore_Con_Client</code> *cl, const void *data)<br />
 <i>Sets the data associated with the given client to </i>data.<br />
 EAPI void * <code>ecore_con_client_data_get</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Retrieves the data associated with the given client. </i><br />
 EAPI char * <code>ecore_con_client_ip_get</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Gets the IP address of a cleint that has connected. </i><br />
 EAPI void <code>ecore_con_client_flush</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Flushes all pending data to the given client. </i><br />
 EAPI int <code>ecore_con_ssl_available_get</code> (void)<br />
 <i>Returns if SSL support is available. </i><br />
 EAPI int <code>ecore_ipc_ssl_available_get</code> (void)<br />
 <i>Returns if SSL support is available. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on Ecore connection client objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_con_client_data_get (<code>Ecore_Con_Client</code> * cl)</h3>
<p>Retrieves the data associated with the given client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data associated with cl.</dl>
<h3>EAPI void ecore_con_client_data_set (<code>Ecore_Con_Client</code> * cl, const void * data)</h3>
<p>Sets the data associated with the given client to data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.<br />
 <i>data</i> What to set the data to.</dl>
<h3>EAPI void* ecore_con_client_del (<code>Ecore_Con_Client</code> * cl)</h3>
<p>Closes the connection and frees memory allocated to the given client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Data associated with the client.</dl>
<p> References ecore_list_goto(), ecore_list_remove(), and ecore_main_fd_handler_del(). </p>
<p> Referenced by ecore_ipc_client_del().</p>
<h3>EAPI void ecore_con_client_flush (<code>Ecore_Con_Client</code> * cl)</h3>
<p>Flushes all pending data to the given client. </p>
<p> Will return when done. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> Referenced by ecore_ipc_client_flush().</p>
<h3>EAPI char* ecore_con_client_ip_get (<code>Ecore_Con_Client</code> * cl)</h3>
<p>Gets the IP address of a cleint that has connected. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an internal string that contains the IP address of the connected client in the form &#8216;XXX.YYY.ZZZ.AAA&#8217; IP notation. This string should not be modified or trusted to stay valid after deletion for the cl object. If no IP is known NULL is returned.</dl>
<p> Referenced by ecore_ipc_client_ip_get().</p>
<h3>EAPI int ecore_con_client_send (<code>Ecore_Con_Client</code> * cl, const void * data, int size)</h3>
<p>Sends the given data to the given client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.<br />
 <i>data</i> The given data.<br />
 <i>size</i> Length of the data, in bytes, to send.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of bytes sent. 0 will be returned if there is an error.</dl>
<p> References ECORE_FD_READ, ECORE_FD_WRITE, and ecore_main_fd_handler_active_set(). </p>
<p> Referenced by ecore_ipc_client_send().</p>
<h3>EAPI <code>Ecore_Con_Server</code>* ecore_con_client_server_get (<code>Ecore_Con_Client</code> * cl)</h3>
<p>Retrieves the server representing the socket the client has connected to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The server that the client connected to.</dl>
<p> Referenced by ecore_ipc_client_del(), and ecore_ipc_client_server_get().</p>
<h3>EAPI int ecore_con_ssl_available_get (void)</h3>
<p>Returns if SSL support is available. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if SSL is available, 0 if it is not.</dl>
<p> Referenced by ecore_ipc_ssl_available_get().</p>
<h3>EAPI int ecore_ipc_ssl_available_get (void)</h3>
<p>Returns if SSL support is available. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if SSL is available, 0 if it is not.</dl>
<p> References ecore_con_ssl_available_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
