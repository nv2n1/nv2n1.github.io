---
title: "netsnmp_row_merge(3)"
name: "netsnmp_row_merge"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_row_merge/"
description: "row_merge – Calls sub handlers with request for one row at a time."
---

<p>row_merge &#8211; Calls sub handlers with request for one row at a time.</p>
<h3>Defines</h3>
<pre><code>#define ROW_MERGE_WAITING   0



#define ROW_MERGE_ACTIVE   1



#define ROW_MERGE_DONE   2



#define ROW_MERGE_HEAD   3



Functions</code></pre>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_row_merge_handler</code> (int prefix_len)<br />
 <i>returns a row_merge handler that can be injected into a given handler chain. </i><br />
 int <code>netsnmp_register_row_merge</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>functionally the same as calling </i><code>netsnmp_register_handler()</code> but also injects a row_merge handler at the same time for you.<br />
 <code>netsnmp_row_merge_status</code> * <code>netsnmp_row_merge_status_get</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, int create_missing)<br />
 <i>retrieve row_merge_status </i><br />
 int <code>netsnmp_row_merge_status_first</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo)<br />
 <i>Determine if this is the first row. </i><br />
 int <code>netsnmp_row_merge_status_last</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo)<br />
 <i>Determine if this is the last row. </i><br />
 int <code>netsnmp_row_merge_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)<br />
 <i>Implements the row_merge handler. </i><br />
 void <code>netsnmp_init_row_merge</code> (void)<br />
 <i>initializes the row_merge helper which then registers a row_merge handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Calls sub handlers with request for one row at a time. </p>
<p> This helper splits a whole bunch of requests into chunks based on the row index that they refer to, and passes all requests for a given row to the lower handlers. This is useful for handlers that don&#8217;t want to process multiple rows at the same time, but are happy to iterate through the request list for a single row.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_row_merge_handler (int prefix_len)</h3>
<p>returns a row_merge handler that can be injected into a given handler chain. </p>
<p> Definition at line 28 of file row_merge.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_row_merge_helper_handler(), and NULL. </p>
<p> Referenced by netsnmp_init_row_merge(), and netsnmp_register_row_merge().</p>
<h3>void netsnmp_init_row_merge (void)</h3>
<p>initializes the row_merge helper which then registers a row_merge handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 360 of file row_merge.c. </p>
<p> References netsnmp_get_row_merge_handler(), and netsnmp_register_handler_by_name().</p>
<h3>int netsnmp_register_row_merge (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>functionally the same as calling <code>netsnmp_register_handler()</code> but also injects a row_merge handler at the same time for you. </p>
<p> Definition at line 42 of file row_merge.c. </p>
<p> References netsnmp_get_row_merge_handler(), netsnmp_inject_handler(), netsnmp_register_handler(), and netsnmp_handler_registration_s::rootoid_len.</p>
<h3>int netsnmp_row_merge_helper_handler (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>Implements the row_merge handler. </p>
<p> Definition at line 154 of file row_merge.c. </p>
<p> References netsnmp_row_merge_status_x::count, netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::myvoid, variable_list::name, variable_list::name_length, netsnmp_call_next_handler(), netsnmp_row_merge_status_get(), netsnmp_request_info_s::next, NULL, netsnmp_request_info_s::prev, netsnmp_request_info_s::processed, netsnmp_request_info_s::requestvb, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, ROW_MERGE_DONE, ROW_MERGE_WAITING, netsnmp_row_merge_status_x::rows, netsnmp_row_merge_status_x::saved_requests, netsnmp_row_merge_status_x::saved_status, and SNMP_FREE. </p>
<p> Referenced by netsnmp_get_row_merge_handler().</p>
<h3>int netsnmp_row_merge_status_first (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo)</h3>
<p>Determine if this is the first row. </p>
<p> returns 1 if this is the first row for this pass of the handler. </p>
<p> Definition at line 110 of file row_merge.c. </p>
<p> References netsnmp_row_merge_status_x::count, netsnmp_row_merge_status_x::current, netsnmp_row_merge_status_get(), and NULL.</p>
<h3><code>netsnmp_row_merge_status</code>* netsnmp_row_merge_status_get (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, int create_missing)</h3>
<p>retrieve row_merge_status </p>
<p> Definition at line 67 of file row_merge.c. </p>
<p> References netsnmp_agent_add_list_data(), netsnmp_agent_get_list_data(), netsnmp_create_data_list(), NULL, snmp_log(), and SNMP_MALLOC_TYPEDEF. </p>
<p> Referenced by netsnmp_row_merge_helper_handler(), netsnmp_row_merge_status_first(), and netsnmp_row_merge_status_last().</p>
<h3>int netsnmp_row_merge_status_last (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo)</h3>
<p>Determine if this is the last row. </p>
<p> returns 1 if this is the last row for this pass of the handler. </p>
<p> Definition at line 130 of file row_merge.c. </p>
<p> References netsnmp_row_merge_status_x::count, netsnmp_row_merge_status_x::current, netsnmp_row_merge_status_get(), NULL, and netsnmp_row_merge_status_x::rows.</p>
