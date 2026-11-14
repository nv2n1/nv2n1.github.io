---
title: "globus_net_manager_context_post_listen(3)"
name: "globus_net_manager_context_post_listen"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_context_post_listen/"
description: "Context –"
---

<h2 class="name">NAME</h2>
<p> Context &#8211; </p>
<p> Net Manager Context Management Functions.</p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_i_net_manager_context_s * <code>globus_net_manager_context_t</code>&quot;<br />
 <i>Net Manager Context. </i></p>
<h3>Functions</h3>
<p> void <code>globus_net_manager_context_destroy</code> (<code>globus_net_manager_context_t</code> context)<br />
 <i>Destroy Context. </i><br />
 globus_result_t <code>globus_net_manager_context_end_listen</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Call Context End Listen. </i><br />
 globus_result_t <code>globus_net_manager_context_init</code> (<code>globus_net_manager_context_t</code> *context, const <code>globus_net_manager_attr_t</code> *attrs)<br />
 <i>Initialize Context. </i><br />
 globus_result_t <code>globus_net_manager_context_post_accept</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Post Accept. </i><br />
 globus_result_t <code>globus_net_manager_context_post_close</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Call Context Post Close. </i><br />
 globus_result_t <code>globus_net_manager_context_post_connect</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Post Connect. </i><br />
 globus_result_t <code>globus_net_manager_context_post_listen</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **local_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Post Listen. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_accept</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Pre Accept. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_close</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Call Context Pre Close. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_connect</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **remote_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Pre Connect. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_listen</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Pre Listen. </i></p>
<h2>Detailed Description</h2>
<p> Net Manager Context Management Functions. </p>
<p> The Net Manager Context manages a collection of network manager plug-ins which will be called when network events occur. </p>
<p> Initialize the context by calling <code>globus_net_manager_context_init()</code>. This processes an array of attributes. The &#8216;scope&#8217; member of of attributes indicate the name of a network manager to associate with the context. The (name, value) tuples of the attributes are added to the attributes passed to all of that particular network manager&#8217;s implementation functions. </p>
<p> Once the network manager context is created, pass it to the per-operation invocation functions to trigger all of the manager callouts associated with the context. </p>
<p> When the network manager context is no longer needed, destroy it by calling <code>globus_net_manager_context_destroy()</code>.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_i_net_manager_context_s* <code>globus_net_manager_context_t</code></h3>
<p> Net Manager Context. A structure of this type is used to thread attributes through the set of configured net manager modules and invoke their functions in configuration order.</p>
<h2>Function Documentation</h2>
<h3>void globus_net_manager_context_destroy (<code>globus_net_manager_context_t</code>context)</h3>
<p> Destroy Context. This functions destroys <i>context</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Pointer to the context to destroy.</dl>
<h3>globus_result_t globus_net_manager_context_end_listen (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array)</h3>
<p> Call Context End Listen. Call the chain of end_listen() functions in a context with the given task_id, transport, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of the socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the end_listen calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_init (<code>globus_net_manager_context_t</code> *context, const <code>globus_net_manager_attr_t</code> *attrs)</h3>
<p> Initialize Context. This functions initializes <i>context</i> with the attribute list <i>attrs</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A pointer to the context to initialize.<br />
 <i>attrs</i> An array of attributes to initialize the context with.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On error, the &#8216;context&#8217; is set to NULL and this function returns an error object. Otherwise this function returns &#8216;GLOBUS_SUCCESS&#8217;</dl>
<h3>globus_result_t globus_net_manager_context_post_accept (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Call Context Post Accept. Call the chain of post_accept() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. The attributes are chained through all the calls, with any changed values returned from a manager passed to subsequent managers in the chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of the socket.<br />
 <i>remote_contact</i> The string representation of the remote address of the socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.<br />
 <i>attr_array_out</i> The resulting set of attributes from the managers. This will be set to NULL if no manager modifies the attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the post_accept calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_post_close (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)</h3>
<p> Call Context Post Close. Call the chain of post_close() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of the socket.<br />
 <i>remote_contact</i> The string representation of the remote address of the socket<br />
 <i>attr_array</i> The set of attributes to pass to the managers.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the post_close calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_post_connect (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Call Context Post Connect. Call the chain of post_connect() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of the socket.<br />
 <i>remote_contact</i> The string representation of the remote address of the socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.<br />
 <i>attr_array_out</i> The resulting set of attributes from the managers. This will be set to NULL if no manager modifies the attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the post_connect calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_post_listen (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **local_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Call Context Post Listen. Call the chain of post_listen() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of the socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.<br />
 <i>local_contact_out</i> The resulting local contact from the managers. This will be set to NULL if no manager modifies the local contact.<br />
 <i>attr_array_out</i> The resulting set of attributes from the managers. This will be set to NULL if no manager modifies the attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the post_listen() calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_pre_accept (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Call Context Pre Accept. Call the chain of pre_accept() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.<br />
 <i>attr_array_out</i> The resulting set of attributes from the managers. This will be set to NULL if no manager modifies the attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the pre_accept() calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_pre_close (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)</h3>
<p> Call Context Pre Close. Call the chain of pre_close() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>local_contact</i> The string representation of the local address of socket.<br />
 <i>remote_contact</i> The string representation of the remote address of socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the pre_close() calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_pre_connect (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **remote_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Call Context Pre Connect. Call the chain of pre_connect() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>remote_contact</i> The string representation of the remote address of socket.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.<br />
 <i>remote_contact_out</i> The resulting string representation of the remote address. This will be set to NULL if no manager modifies the address.<br />
 <i>attr_array_out</i> The resulting set of attributes from the managers. This will be set to NULL if no manager modifies the attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the pre_connect() calls stop and the error is returned to the caller.</dl>
<h3>globus_result_t globus_net_manager_context_pre_listen (<code>globus_net_manager_context_t</code>context, const char *task_id, const char *transport, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Call Context Pre Listen. Call the chain of pre_listen() functions in a context with the given task_id, transport, contact information, and attributes. If any manager in the context returns an error, the subsequent managers will not be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The context to call functions in.<br />
 <i>task_id</i> The task_id associated with this network operation.<br />
 <i>transport</i> The transport driver associated with this network operation.<br />
 <i>attr_array</i> The set of attributes to pass to the managers.<br />
 <i>attr_array_out</i> The resulting set of attributes from the managers. This will be set to NULL if no manager modifies the attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. If any manager returns an error, the pre_listen() calls stop and the error is returned to the caller.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_net_manager from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAT">Author</a></p>
<dd></dl>
