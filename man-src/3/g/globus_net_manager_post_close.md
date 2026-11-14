---
title: "globus_net_manager_post_close(3)"
name: "globus_net_manager_post_close"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_post_close/"
description: "Function Signatures –"
---

<h2 class="name">NAME</h2>
<p> Function Signatures &#8211; </p>
<p> Net Manager Function Signatures </p>
<p> Function signatures for the Net Manager interface. <code>Net Manager Implementation Tutorial</code>.</p>
<h3>Typedefs</h3>
<p> typedef globus_result_t(* <code>globus_net_manager_pre_listen</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Pre-Listen Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_listen</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **local_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Post-Listen Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_end_listen</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Net Manager End-Listen Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_pre_accept</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Pre-Accept Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_accept</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Post-Accept Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_pre_connect</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **remote_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Pre-Connect Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_connect</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Post-Connect Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_pre_close</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Net Manager Pre-Close Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_close</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Net Manager Post-Close Function Signature. </i></p>
<h2>Detailed Description</h2>
<p> Net Manager Function Signatures </p>
<p> Function signatures for the Net Manager interface. <code>Net Manager Implementation Tutorial</code>. </p>
<h2>Typedef Documentation</h2>
<h3>typedef globus_result_t(* globus_net_manager_end_listen)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array)</h3>
<p> Net Manager End-Listen Function Signature. A function of this signature, if included in a network manager implementation, is called when the transport-specific listening port will be closed. </p>
<p> The network manager is passed the network transport-specific options and contact string for the listener. </p>
<p> The globus_net_manager library aborts the closing of the listening port if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_end_listen functions configured for this listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>local_contact</i> The transport-specific contact string for the listener [in].<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.</dl>
<h3>typedef globus_result_t(* globus_net_manager_post_accept)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Net Manager Post-Accept Function Signature. A function of this signature, if included in a network manager implementation, is called after accepting a connection on a transport-specific listening port. </p>
<p> The network manager is passed the network transport-specific options and contact string for both ends of the connection. It may modify the attributes of the local side of the connection. </p>
<p> The globus_net_manager library aborts the accept operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_post_accept functions configured for this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>local_contact</i> The transport-specific contact string for the local side of the connection.<br />
 <i>remote_contact</i> The transport-specific contact string for the remote side of the connection.<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>attr_array_out</i> A pointer to an array of transport options to apply to the listener prior to returning it to the service. This may be NULL to indicate no change in the options. If non-NULL, this array must be terminated with an attribute having a NULL scope. The array and the members of the globus_net_manager_attr_t struct will be freed by the globus_net_manager library by calling free().</dl>
<h3>typedef globus_result_t(* globus_net_manager_post_close)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)</h3>
<p> Net Manager Post-Close Function Signature. A function of this signature, if included in a network manager implementation, is called after closing a connection. </p>
<p> The network manager is passed the network transport-specific options and contact string for both ends of the connection. </p>
<p> The globus_net_manager library aborts the close operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_pre_close functions configured for this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>local_contact</i> The transport-specific contact string for the local side of the connection.<br />
 <i>remote_contact</i> The transport-specific contact string for the remote side of the connection.<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.</dl>
<h3>typedef globus_result_t(* globus_net_manager_post_connect)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Net Manager Post-Connect Function Signature. A function of this signature, if included in a network manager implementation, is called after establishing a connection to a transport-specific listener. </p>
<p> The network manager is passed the network transport-specific options and contact string for both ends of the connection. It may modify the attributes of the local side of the connection. </p>
<p> The globus_net_manager library aborts the connect operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_post_connect functions configured for this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>remote_contact</i> The transport-specific contact string for the remote side of the connection.<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>attr_array_out</i> A pointer to an array of transport options to apply to the listener prior to returning it to the service. This may be NULL to indicate no change in the options. If non-NULL, this array must be terminated with an attribute having a NULL scope. The array and the members of the globus_net_manager_attr_t struct will be freed by the globus_net_manager library by calling free().</dl>
<h3>typedef globus_result_t(* globus_net_manager_post_listen)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **local_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Net Manager Post-Listen Function Signature. A function of this signature, if included in a network manager implementation, is called after the transport-specific listening port has been created. </p>
<p> The network manager is passed the network transport-specific options and contact string for the listener. It may modify either of these before the transport listener is made available to the service which requested the listening port. </p>
<p> The globus_net_manager library aborts the listen operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_post_listen functions configured for this listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>local_contact</i> The transport-specific contact string for the listener [in].<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>local_contact_out</i> A pointer to the local contact which the network manager wants to return to the service. This may be NULL to indicate no change in the contact. This value will be freed() by the globus_net_manager library.<br />
 <i>attr_array_out</i> A pointer to an array of transport options to apply to the listener prior to returning it to the service. This may be NULL to indicate no change in the options. If non-NULL, this array must be terminated with an attribute having a NULL scope. The array and the members of the globus_net_manager_attr_t struct will be freed by the globus_net_manager library by calling free().</dl>
<h3>typedef globus_result_t(* globus_net_manager_pre_accept)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Net Manager Pre-Accept Function Signature. A function of this signature, if included in a network manager implementation, is called before accepting a connection on a transport-specific listening port. </p>
<p> The network manager is passed the network transport-specific options and contact string for the listener. It may modify the options before the accept operation is complete. </p>
<p> The globus_net_manager library aborts the accept operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_pre_accept functions configured for this listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>local_contact</i> The transport-specific contact string for the listener.<br />
 <i>attr_array</i> A NULL-terminated array of transport attributes associated with the listener.<br />
 <i>attr_array_out</i> A pointer to an array of transport options to apply to the listener prior to returning it to the service. This may be NULL to indicate no change in the options. If non-NULL, this array must be terminated with an attribute having a NULL scope. The array and the members of the globus_net_manager_attr_t struct will be freed by the globus_net_manager library by calling free().</dl>
<h3>typedef globus_result_t(* globus_net_manager_pre_close)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)</h3>
<p> Net Manager Pre-Close Function Signature. A function of this signature, if included in a network manager implementation, is called prior to closing a connection. </p>
<p> The network manager is passed the network transport-specific options and contact string for both ends of the connection. </p>
<p> The globus_net_manager library aborts the close operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_pre_close functions configured for this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>local_contact</i> The transport-specific contact string for the local side of the connection.<br />
 <i>remote_contact</i> The transport-specific contact string for the remote side of the connection.<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.</dl>
<h3>typedef globus_result_t(* globus_net_manager_pre_connect)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **remote_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Net Manager Pre-Connect Function Signature. A function of this signature, if included in a network manager implementation, is called after initiating a connection to a transport-specific listener. </p>
<p> The network manager is passed the network transport-specific options and contact string for both ends of the connection. It may modify the attributes of the local side of the connection. </p>
<p> The globus_net_manager library aborts the connect operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_pre_connect functions configured for this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>remote_contact</i> The transport-specific contact string for the remote side of the connection.<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>remote_contact_out</i> A pointer to the remote contact which the network manager wants to connect to. This may be NULL to indicate no change in the contact. This value will be freed() by the globus_net_manager library.<br />
 <i>attr_array_out</i> A pointer to an array of transport options to apply to the listener prior to returning it to the service. This may be NULL to indicate no change in the options. If non-NULL, this array must be terminated with an attribute having a NULL scope. The array and the members of the globus_net_manager_attr_t struct will be freed by the globus_net_manager library by calling free().</dl>
<h3>typedef globus_result_t(* globus_net_manager_pre_listen)(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)</h3>
<p> Net Manager Pre-Listen Function Signature. A function of this signature, if included in a network manager implementation, is called before the transport-specific listening port has been created. </p>
<p> The network manager is passed the network transport-specific options for the listener. It may modify these before the listener is created by the transport. </p>
<p> The globus_net_manager library aborts the listen operation if this function returns a value other than GLOBUS_SUCCESS. In this case, the globus_net_manager will not call any other globus_net_manager_pre_listen functions configured for this listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Pointer to the network manager struct that is being invoked.<br />
 <i>manager_attr_array</i> An array of attributes associated with the manager. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>task_id</i> An application-specific task ID associated with this network operation.<br />
 <i>transport</i> The name of the transport associated with this listener.<br />
 <i>attr_array</i> An array of transport attributes associated with the listener. The end of the array is indicated by an attribute containing a NULL scope.<br />
 <i>attr_array_out</i> A pointer to an array of transport options to apply to the listener prior to returning it to the service. This may be NULL to indicate no change in the options. If non-NULL, this array must be terminated with an attribute having a NULL scope. The array and the members of the globus_net_manager_attr_t struct will be freed by the globus_net_manager library by calling free().</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_net_manager from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
