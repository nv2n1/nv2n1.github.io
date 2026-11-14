---
title: "netsnmp_old_api(3)"
name: "netsnmp_old_api"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_old_api/"
description: "old_api – Calls mib module code written in the old style of code."
---

<p>old_api &#8211; Calls mib module code written in the old style of code.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>get_old_api_handler</code> (void)<br />
 <i>returns a old_api handler that should be the final calling handler. </i><br />
 int <code>netsnmp_register_old_api</code> (const char *moduleName, struct <code>variable</code> *var, size_t varsize, size_t numvars, oid *mibloc, size_t mibloclen, int priority, int range_subid, oid range_ubound, <code>netsnmp_session</code> *ss, const char *context, int timeout, int flags)<br />
 <i>Registers an old API set into the mib tree. </i><br />
 int <code>netsnmp_register_mib_table_row</code> (const char *moduleName, struct <code>variable</code> *var, size_t varsize, size_t numvars, oid *mibloc, size_t mibloclen, int priority, int var_subid, <code>netsnmp_session</code> *ss, const char *context, int timeout, int flags)<br />
 <i>registers a row within a mib table </i><br />
 int <code>netsnmp_old_api_helper</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)<br />
 <i>implements the old_api handler </i></p>
<h2>Detailed Description</h2>
<p>Calls mib module code written in the old style of code. </p>
<p> This is a backwards compatilibity module that allows code written in the old API to be run under the new handler based architecture. Use it by calling <code>netsnmp_register_old_api()</code>.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* get_old_api_handler (void)</h3>
<p>returns a old_api handler that should be the final calling handler. </p>
<p> Don&#8217;t use this function. Use the <code>netsnmp_register_old_api()</code> function instead. </p>
<p> Definition at line 37 of file old_api.c. </p>
<p> References netsnmp_create_handler(), and netsnmp_old_api_helper(). </p>
<p> Referenced by netsnmp_register_mib_table_row(), and netsnmp_register_old_api().</p>
<h3>int netsnmp_old_api_helper (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>implements the old_api handler </p>
<p> Definition at line 226 of file old_api.c. </p>
<p> References variable::acl, variable::findVar, variable::magic, MIB_CLIENTS_ARE_EVIL, netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::myvoid, variable_list::name, variable::name, variable_list::name_length, variable::namelen, netsnmp_request_info_s::next, NULL, netsnmp_request_info_s::requestvb, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_set_var_objid(), and variable::type. </p>
<p> Referenced by get_old_api_handler().</p>
<h3>int netsnmp_register_mib_table_row (const char * moduleName, struct <code>variable</code> * var, size_t varsize, size_t numvars, oid * mibloc, size_t mibloclen, int priority, int var_subid, <code>netsnmp_session</code> * ss, const char * context, int timeout, int flags)</h3>
<p>registers a row within a mib table </p>
<p> Definition at line 107 of file old_api.c. </p>
<p> References netsnmp_handler_registration_s::contextName, register_parameters::contextName, register_parameters::flags, get_old_api_handler(), netsnmp_handler_registration_s::handler, HANDLER_CAN_RWRITE, netsnmp_handler_registration_s::handlerName, netsnmp_handler_registration_s::modes, netsnmp_mib_handler_s::myvoid, register_parameters::name, register_parameters::namelen, netsnmp_handler_registration_free(), netsnmp_register_handler_nocallback(), NULL, netsnmp_handler_registration_s::priority, register_parameters::priority, netsnmp_handler_registration_s::range_subid, register_parameters::range_subid, netsnmp_handler_registration_s::range_ubound, register_parameters::range_ubound, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_call_callbacks(), SNMP_MALLOC_TYPEDEF, netsnmp_handler_registration_s::timeout, and register_parameters::timeout.</p>
<h3>int netsnmp_register_old_api (const char * moduleName, struct <code>variable</code> * var, size_t varsize, size_t numvars, oid * mibloc, size_t mibloclen, int priority, int range_subid, oid range_ubound, <code>netsnmp_session</code> * ss, const char * context, int timeout, int flags)</h3>
<p>Registers an old API set into the mib tree. </p>
<p> Functionally this mimics the old <code>register_mib_context()</code> function (and in fact the new <code>register_mib_context()</code> function merely calls this new old_api one). </p>
<p> netsnmp_handler_registration_free(reginfo); already freed </p>
<p> Definition at line 48 of file old_api.c. </p>
<p> References netsnmp_handler_registration_s::contextName, get_old_api_handler(), netsnmp_handler_registration_s::handler, HANDLER_CAN_RWRITE, netsnmp_handler_registration_s::handlerName, memdup(), netsnmp_handler_registration_s::modes, netsnmp_mib_handler_s::myvoid, netsnmp_register_handler(), NULL, netsnmp_handler_registration_s::priority, netsnmp_handler_registration_s::range_subid, netsnmp_handler_registration_s::range_ubound, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, SNMP_FREE, SNMP_MALLOC_TYPEDEF, and netsnmp_handler_registration_s::timeout. </p>
<p> Referenced by register_mib_context().</p>
