---
title: "netsnmp_instance(3)"
name: "netsnmp_instance"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_instance/"
description: "instance – Process individual MIB instances easily."
---

<p>instance &#8211; Process individual MIB instances easily.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_instance_handler</code> (void)<br />
 <i>Creates an instance helper handler, calls netsnmp_create_handler, which then could be registered, using </i><code>netsnmp_register_handler()</code>.<br />
 int <code>netsnmp_register_instance</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>This function registers an instance helper handler, which is a way of registering an exact OID such that GENEXT requests are handled entirely by the helper. </i><br />
 int <code>netsnmp_register_read_only_instance</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>This function injects a &#8216;read only&#8217; handler into the handler chain prior to serializing/registering the handler. </i><br />
 int <code>netsnmp_register_read_only_ulong_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_ulong_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_counter32_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_long_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_long_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_uint_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, unsigned int *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_uint_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, unsigned int *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_int_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>register_read_only_int_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_ulong_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_ulong_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_read_only_counter32_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_read_only_long_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, long *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_long_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, long *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_int_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_read_only_int_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>register_read_only_int_instance_context</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_num_file_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, char *file_name, int asn_type, int mode, <code>Netsnmp_Node_Handler</code> *subhandler, const char *contextName) </p>
<p> int <code>netsnmp_register_int_instance</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler)<br />
 <i>This function registers an int helper handler to a specified OID. </i><br />
 int <code>netsnmp_instance_ulong_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_instance_counter32_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_instance_long_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_instance_int_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_instance_num_file_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_instance_uint_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_instance_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)</p>
<h2>Detailed Description</h2>
<p>Process individual MIB instances easily.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_instance_handler (void)</h3>
<p>Creates an instance helper handler, calls netsnmp_create_handler, which then could be registered, using <code>netsnmp_register_handler()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns a pointer to a netsnmp_mib_handler struct which contains the handler&#8217;s name and the access method</dl>
<p> Definition at line 48 of file instance.c. </p>
<p> References netsnmp_create_handler(), and netsnmp_instance_helper_handler(). </p>
<p> Referenced by netsnmp_register_instance(), netsnmp_register_read_only_instance(), netsnmp_register_read_only_scalar(), netsnmp_register_scalar(), and netsnmp_register_scalar_group().</p>
<h3>int netsnmp_instance_num_file_handler (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>Definition at line 741 of file instance.c. </p>
<p> References netsnmp_mib_handler_s::access_method, netsnmp_num_file_instance_s::file_name, netsnmp_num_file_instance_s::filep, netsnmp_vardata::integer, memdup(), netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::myvoid, netsnmp_call_next_handler(), netsnmp_create_data_list(), netsnmp_request_add_list_data(), netsnmp_request_get_list_data(), netsnmp_set_request_error(), netsnmp_mib_handler_s::next, NULL, netsnmp_request_info_s::requestvb, snmp_set_var_typed_value(), variable_list::type, netsnmp_num_file_instance_s::type, and variable_list::val. </p>
<p> Referenced by netsnmp_register_num_file_instance().</p>
<h3>int netsnmp_register_instance (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>This function registers an instance helper handler, which is a way of registering an exact OID such that GENEXT requests are handled entirely by the helper. </p>
<p> First need to inject it into the calling chain of the handler defined by the netsnmp_handler_registration struct, reginfo. The new handler is injected at the top of the list and will be the new handler to be called first. This function also injects a serialize handler before actually calling netsnmp_register_handle, registering reginfo. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>reginfo</i> a handler registration structure which could get created using netsnmp_create_handler_registration. Used to register an instance helper handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>MIB_REGISTERED_OK is returned if the registration was a success. Failures are MIB_REGISTRATION_FAILED and MIB_DUPLICATE_REGISTRATION.</dl>
<p> <code>Examples: </code> <code>delayed_instance.c</code>. </p>
<p> Definition at line 73 of file instance.c. </p>
<p> References netsnmp_mib_handler_s::flags, MIB_HANDLER_INSTANCE, netsnmp_get_instance_handler(), netsnmp_inject_handler(), and netsnmp_register_serialize(). </p>
<p> Referenced by netsnmp_register_int_instance(), netsnmp_register_int_instance_context(), netsnmp_register_long_instance(), netsnmp_register_long_instance_context(), netsnmp_register_num_file_instance(), netsnmp_register_uint_instance(), netsnmp_register_ulong_instance(), netsnmp_register_ulong_instance_context(), and netsnmp_register_watched_instance().</p>
<h3>int netsnmp_register_int_instance (const char * name, oid * reg_oid, size_t reg_oid_len, int * it, <code>Netsnmp_Node_Handler</code> * subhandler)</h3>
<p>This function registers an int helper handler to a specified OID. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> the name used for registration pruposes.<br />
 <i>reg_oid</i> the OID where you want to register your integer at<br />
 <i>reg_oid_len</i> the length of the OID<br />
 <i>it</i> the integer value to be registered during initialization<br />
 <i>subhandler</i> a handler to do whatever you want to do, otherwise use NULL to use the default int handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>MIB_REGISTERED_OK is returned if the registration was a success. Failures are MIB_REGISTRATION_FAILED and MIB_DUPLICATE_REGISTRATION.</dl>
<p> <code>Examples: </code> <code>scalar_int.c</code>. </p>
<p> Definition at line 460 of file instance.c. </p>
<p> References HANDLER_CAN_RWRITE, netsnmp_instance_int_handler(), netsnmp_register_instance(), and NULL.</p>
<h3>int netsnmp_register_read_only_instance (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>This function injects a &#8216;read only&#8217; handler into the handler chain prior to serializing/registering the handler. </p>
<p> The only purpose of this &#8216;read only&#8217; handler is to return an appropriate error for any requests passed to it in a SET mode. Inserting it into your handler chain will ensure you&#8217;re never asked to perform a SET request so you can ignore those error conditions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>reginfo</i> a handler registration structure which could get created using netsnmp_create_handler_registration. Used to register a read only instance helper handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>MIB_REGISTERED_OK is returned if the registration was a success. Failures are MIB_REGISTRATION_FAILED and MIB_DUPLICATE_REGISTRATION.</dl>
<p> Definition at line 100 of file instance.c. </p>
<p> References netsnmp_get_instance_handler(), netsnmp_get_read_only_handler(), netsnmp_inject_handler(), and netsnmp_register_serialize(). </p>
<p> Referenced by netsnmp_register_num_file_instance(), netsnmp_register_read_only_counter32_instance(), netsnmp_register_read_only_counter32_instance_context(), netsnmp_register_read_only_int_instance(), netsnmp_register_read_only_int_instance_context(), netsnmp_register_read_only_long_instance(), netsnmp_register_read_only_long_instance_context(), netsnmp_register_read_only_uint_instance(), netsnmp_register_read_only_ulong_instance(), and netsnmp_register_read_only_ulong_instance_context().</p>
