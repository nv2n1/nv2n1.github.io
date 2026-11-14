---
title: "netsnmp_bulk_to_next(3)"
name: "netsnmp_bulk_to_next"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_bulk_to_next/"
description: "bulk_to_next – Convert GETBULK requests into GETNEXT requests for the handler."
---

<p>bulk_to_next &#8211; Convert GETBULK requests into GETNEXT requests for the handler.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_bulk_to_next_handler</code> (void)<br />
 <i>returns a bulk_to_next handler that can be injected into a given handler chain. </i><br />
 void <code>netsnmp_bulk_to_next_fix_requests</code> (<code>netsnmp_request_info</code> *requests)<br />
 <i>takes answered requests and decrements the repeat count and updates the requests to the next to-do varbind in the list </i><br />
 int <code>netsnmp_bulk_to_next_helper</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> void <code>netsnmp_init_bulk_to_next_helper</code> (void)<br />
 <i>initializes the bulk_to_next helper which then registers a bulk_to_next handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Convert GETBULK requests into GETNEXT requests for the handler. </p>
<p> The only purpose of this handler is to convert a GETBULK request to a GETNEXT request. It is inserted into handler chains where the handler has not set the HANDLER_CAN_GETBULK flag.</p>
<h2>Function Documentation</h2>
<h3>void netsnmp_bulk_to_next_fix_requests (<code>netsnmp_request_info</code> * requests)</h3>
<p>takes answered requests and decrements the repeat count and updates the requests to the next to-do varbind in the list </p>
<p> Definition at line 42 of file bulk_to_next.c. </p>
<p> References netsnmp_request_info_s::inclusive, variable_list::name, variable_list::name_length, netsnmp_request_info_s::next, variable_list::next_variable, netsnmp_request_info_s::range_end, netsnmp_request_info_s::range_end_len, netsnmp_request_info_s::repeat, netsnmp_request_info_s::requestvb, snmp_oid_compare(), snmp_set_var_objid(), and variable_list::type. </p>
<p> Referenced by netsnmp_bulk_to_next_helper().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_bulk_to_next_handler (void)</h3>
<p>returns a bulk_to_next handler that can be injected into a given handler chain. </p>
<p> Definition at line 27 of file bulk_to_next.c. </p>
<p> References netsnmp_mib_handler_s::flags, MIB_HANDLER_AUTO_NEXT, netsnmp_bulk_to_next_helper(), netsnmp_create_handler(), and NULL. </p>
<p> Referenced by netsnmp_init_bulk_to_next_helper(), and netsnmp_register_handler().</p>
<h3>void netsnmp_init_bulk_to_next_helper (void)</h3>
<p>initializes the bulk_to_next helper which then registers a bulk_to_next handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 139 of file bulk_to_next.c. </p>
<p> References netsnmp_get_bulk_to_next_handler(), and netsnmp_register_handler_by_name().</p>
