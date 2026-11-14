---
title: "ecore_ipc_client_group(3)"
name: "ecore_ipc_client_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_ipc_client_group/"
description: "IPC Client Functions – Functions that deal with IPC client objects."
---

<p>IPC Client Functions &#8211; Functions that deal with IPC client objects. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_ipc_client_send</code> (<code>Ecore_Ipc_Client</code> *cl, int major, int minor, int ref, int ref_to, int response, const void *data, int size)<br />
 <i>Sends a message to the given IPC client. </i><br />
 EAPI <code>Ecore_Ipc_Server</code> * <code>ecore_ipc_client_server_get</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Retrieves the IPC server that the given IPC client is connected to. </i><br />
 EAPI void * <code>ecore_ipc_client_del</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Closes the connection and frees memory allocated to the given IPC client. </i><br />
 EAPI void <code>ecore_ipc_client_data_set</code> (<code>Ecore_Ipc_Client</code> *cl, const void *data)<br />
 <i>Sets the IPC data associated with the given IPC client to </i>data.<br />
 EAPI void * <code>ecore_ipc_client_data_get</code> (<code>Ecore_Ipc_Client</code> *cl)<br />
 <i>Retrieves the data that has been associated with the given IPC client. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with IPC client objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_ipc_client_data_get (<code>Ecore_Ipc_Client</code> * cl)</h3>
<p>Retrieves the data that has been associated with the given IPC client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data associated with the IPC client.</dl>
<h3>EAPI void ecore_ipc_client_data_set (<code>Ecore_Ipc_Client</code> * cl, const void * data)</h3>
<p>Sets the IPC data associated with the given IPC client to data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given IPC client.<br />
 <i>data</i> The data to associate with the IPC client.</dl>
<h3>EAPI void* ecore_ipc_client_del (<code>Ecore_Ipc_Client</code> * cl)</h3>
<p>Closes the connection and frees memory allocated to the given IPC client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Data associated with the client.</dl>
<p> References ecore_con_client_del(), ecore_con_client_server_get(), and ecore_con_server_data_get(). </p>
<p> Referenced by ecore_ipc_server_del().</p>
<h3>EAPI int ecore_ipc_client_send (<code>Ecore_Ipc_Client</code> * cl, int major, int minor, int ref, int ref_to, int response, const void * data, int size)</h3>
<p>Sends a message to the given IPC client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given IPC client.<br />
 <i>major</i> Major opcode of the message.<br />
 <i>minor</i> Minor opcode of the message.<br />
 <i>ref</i> Reference number of the message.<br />
 <i>ref_to</i> Reference number of the message this message refers to.<br />
 <i>response</i> Requires response.<br />
 <i>data</i> The data to send as part of the message.<br />
 <i>size</i> Length of the data, in bytes, to send.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of bytes sent. 0 will be returned if there is an error.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>This function needs to become an IPC message. </p>
<p> Make sure ref_to and response parameters are described correctly.</dl>
<p> References ecore_con_client_send().</p>
<h3>EAPI <code>Ecore_Ipc_Server</code>* ecore_ipc_client_server_get (<code>Ecore_Ipc_Client</code> * cl)</h3>
<p>Retrieves the IPC server that the given IPC client is connected to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cl</i> The given IPC client.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The IPC server the IPC client is connected to.</dl>
<p> References ecore_con_client_server_get(), and ecore_con_server_data_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
