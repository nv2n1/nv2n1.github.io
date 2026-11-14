---
title: "netsnmp_table(3)"
name: "netsnmp_table"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_table/"
description: "table – Helps you implement a table."
---

<p>table &#8211; Helps you implement a table.</p>
<h3>Modules</h3>
<p><code>table_array</code><br />
 <i>Helps you implement a table when data can be stored locally. </i><br />
 <code>table_container</code><br />
 <i>Helps you implement a table when data can be found via a netsnmp_container. </i><br />
 <code>table_data</code><br />
 <i>Helps you implement a table with datamatted storage. </i><br />
 <code>generic_table_API</code><br />
 <i>General requirements for a table helper. </i><br />
 <code>table_iterator</code><br />
 <i>The table iterator helper is designed to simplify the task of writing a table handler for the net-snmp agent when the data being accessed is not in an oid sorted form and must be accessed externally. </i><br />
 <code>table_row</code><br />
 <i>Helps you implement a table shared across two or more subagents, or otherwise split into individual row slices. </i><br />
 <code>tdata</code><br />
 <i>Implement a table with datamatted storage. </i></p>
<h3>Defines</h3>
<pre><code>#define SPARSE_TABLE_HANDLER_NAME   'sparse_table'



Functions</code></pre>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_table_handler</code> (<code>netsnmp_table_registration_info</code> *tabreq)<br />
 <i>Given a netsnmp_table_registration_info object, creates a table handler. </i><br />
 int <code>netsnmp_register_table</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_table_registration_info</code> *tabreq)<br />
 <i>creates a table handler given the netsnmp_table_registration_info object, inserts it into the request chain and then calls </i><code>netsnmp_register_handler()</code> to register the table into the agent.<br />
 NETSNMP_INLINE <code>netsnmp_table_request_info</code> * <code>netsnmp_extract_table_info</code> (<code>netsnmp_request_info</code> *request)<br />
 <i>Extracts the processed table information from a given request. </i><br />
 <code>netsnmp_table_registration_info</code> * <code>netsnmp_find_table_registration_info</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>extracts the registered netsnmp_table_registration_info object from a netsnmp_handler_registration object </i><br />
 int <code>table_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)<br />
 <i>implements the table helper handler </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_sparse_table_handler_get</code> (void)<br />
 <i>create sparse table handler </i><br />
 int <code>netsnmp_sparse_table_register</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_table_registration_info</code> *tabreq)<br />
 <i>creates a table handler given the netsnmp_table_registration_info object, inserts it into the request chain and then calls </i><code>netsnmp_register_handler()</code> to register the table into the agent.<br />
 int <code>netsnmp_table_build_result</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_request_info</code> *reqinfo, <code>netsnmp_table_request_info</code> *table_info, u_char type, u_char *result, size_t result_len)<br />
 <i>Builds the result to be returned to the agent given the table information. </i><br />
 int <code>netsnmp_table_build_oid</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_request_info</code> *reqinfo, <code>netsnmp_table_request_info</code> *table_info)<br />
 <i>given a registration info object, a request object and the table info object it builds the request-&gt;requestvb-&gt;name oid from the index values and column information found in the table_info object. </i><br />
 int <code>netsnmp_table_build_oid_from_index</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_request_info</code> *reqinfo, <code>netsnmp_table_request_info</code> *table_info)<br />
 <i>given a registration info object, a request object and the table info object it builds the request-&gt;requestvb-&gt;name oid from the index values and column information found in the table_info object. </i><br />
 int <code>netsnmp_update_variable_list_from_index</code> (<code>netsnmp_table_request_info</code> *tri)<br />
 <i>parses an OID into table indexses </i><br />
 int <code>netsnmp_update_indexes_from_variable_list</code> (<code>netsnmp_table_request_info</code> *tri)<br />
 <i>builds an oid given a set of indexes. </i><br />
 int <code>netsnmp_check_getnext_reply</code> (<code>netsnmp_request_info</code> *request, oid *prefix, size_t prefix_len, <code>netsnmp_variable_list</code> *newvar, <code>netsnmp_variable_list</code> **outvar)<br />
 <i>checks the original request against the current data being passed in if its greater than the request oid but less than the current valid return, set the current valid return to the new value. </i></p>
<h2>Detailed Description</h2>
<p>Helps you implement a table. </p>
<p> This handler helps you implement a table by doing some of the processing for you. </p>
<p> This handler truly shows the power of the new handler mechanism. By creating a table handler and injecting it into your calling chain, or by using the <code>netsnmp_register_table()</code> function to register your table, you get access to some pre-parsed information. Specifically, the table handler pulls out the column number and indexes from the request oid so that you don&#8217;t have to do the complex work to do that parsing within your own code. </p>
<p> To do this, the table handler needs to know up front how your table is structured. To inform it about this, you fill in a table_registeration_info structure that is passed to the table handler. It contains the asn index types for the table as well as the minimum and maximum column that should be used.</p>
<h2>Function Documentation</h2>
<h3>int netsnmp_check_getnext_reply (<code>netsnmp_request_info</code> * request, oid * prefix, size_t prefix_len, <code>netsnmp_variable_list</code> * newvar, <code>netsnmp_variable_list</code> ** outvar)</h3>
<p>checks the original request against the current data being passed in if its greater than the request oid but less than the current valid return, set the current valid return to the new value. </p>
<p> returns 1 if outvar was replaced with the oid from newvar (success). returns 0 if not. </p>
<p> Definition at line 884 of file table.c. </p>
<p> References build_oid_noalloc(), variable_list::name, variable_list::name_length, netsnmp_request_info_s::requestvb, snmp_clone_varbind(), snmp_free_varbind(), snmp_oid_compare(), snmp_set_var_objid(), snmp_set_var_typed_value(), netsnmp_vardata::string, variable_list::type, variable_list::val, and variable_list::val_len.</p>
<h3>NETSNMP_INLINE <code>netsnmp_table_request_info</code>* netsnmp_extract_table_info (<code>netsnmp_request_info</code> * request)</h3>
<p>Extracts the processed table information from a given request. </p>
<p> Call this from subhandlers on a request to extract the processed netsnmp_request_info information. The resulting information includes the index values and the column number. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>request</i> populated netsnmp request structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>populated netsnmp_table_request_info structure</dl>
<p> Definition at line 125 of file table.c. </p>
<p> References netsnmp_request_get_list_data(). </p>
<p> Referenced by _netsnmp_tdata_helper_handler(), netsnmp_container_table_row_insert(), netsnmp_insert_iterator_context(), netsnmp_insert_table_row(), netsnmp_table_data_helper_handler(), netsnmp_table_data_set_helper_handler(), netsnmp_table_iterator_helper_handler(), and table_helper_handler().</p>
<h3><code>netsnmp_table_registration_info</code>* netsnmp_find_table_registration_info (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>extracts the registered netsnmp_table_registration_info object from a netsnmp_handler_registration object </p>
<p> Definition at line 134 of file table.c. </p>
<p> References netsnmp_find_handler_data_by_name(). </p>
<p> Referenced by netsnmp_table_data_helper_handler(), and netsnmp_table_iterator_helper_handler().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_table_handler (<code>netsnmp_table_registration_info</code> * tabreq)</h3>
<p>Given a netsnmp_table_registration_info object, creates a table handler. </p>
<p> You can use this table handler by injecting it into a calling chain. When the handler gets called, it&#8217;ll do processing and store it&#8217;s information into the request-&gt;parent_data structure. </p>
<p> The table helper handler pulls out the column number and indexes from the request oid so that you don&#8217;t have to do the complex work of parsing within your own code. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>tabreq</i> is a pointer to a netsnmp_table_registration_info struct. The table handler needs to know up front how your table is structured. A netsnmp_table_registeration_info structure that is passed to the table handler should contain the asn index types for the table as well as the minimum and maximum column that should be used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns a pointer to a netsnmp_mib_handler struct which contains the handler&#8217;s name and the access method</dl>
<p> Definition at line 85 of file table.c. </p>
<p> References count_varbinds(), netsnmp_table_registration_info_s::indexes, netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), NULL, netsnmp_table_registration_info_s::number_indexes, snmp_log(), and table_helper_handler(). </p>
<p> Referenced by netsnmp_register_table(), and netsnmp_sparse_table_register().</p>
<h3>int netsnmp_register_table (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_table_registration_info</code> * tabreq)</h3>
<p>creates a table handler given the netsnmp_table_registration_info object, inserts it into the request chain and then calls <code>netsnmp_register_handler()</code> to register the table into the agent. </p>
<p> Definition at line 108 of file table.c. </p>
<p> References netsnmp_get_table_handler(), netsnmp_inject_handler(), and netsnmp_register_handler(). </p>
<p> Referenced by netsnmp_container_table_register(), netsnmp_register_table_data(), netsnmp_register_table_iterator(), netsnmp_table_container_register(), and netsnmp_table_row_register().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_sparse_table_handler_get (void)</h3>
<p>create sparse table handler </p>
<p> Definition at line 722 of file table.c. </p>
<p> References netsnmp_create_handler(), and SPARSE_TABLE_HANDLER_NAME.</p>
<h3>int netsnmp_sparse_table_register (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_table_registration_info</code> * tabreq)</h3>
<p>creates a table handler given the netsnmp_table_registration_info object, inserts it into the request chain and then calls <code>netsnmp_register_handler()</code> to register the table into the agent. </p>
<p> Definition at line 733 of file table.c. </p>
<p> References netsnmp_create_handler(), netsnmp_get_table_handler(), netsnmp_inject_handler(), netsnmp_register_handler(), and SPARSE_TABLE_HANDLER_NAME.</p>
<h3>int netsnmp_table_build_oid (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_request_info</code> * reqinfo, <code>netsnmp_table_request_info</code> * table_info)</h3>
<p>given a registration info object, a request object and the table info object it builds the request-&gt;requestvb-&gt;name oid from the index values and column information found in the table_info object. </p>
<p> Index values are extracted from the table_info varbinds. </p>
<p> Definition at line 784 of file table.c. </p>
<p> References build_oid(), netsnmp_table_request_info_s::colnum, netsnmp_table_request_info_s::indexes, variable_list::name, variable_list::name_length, netsnmp_request_info_s::requestvb, netsnmp_handler_registration_s::rootoid, and netsnmp_handler_registration_s::rootoid_len. </p>
<p> Referenced by netsnmp_table_build_result().</p>
<h3>int netsnmp_table_build_oid_from_index (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_request_info</code> * reqinfo, <code>netsnmp_table_request_info</code> * table_info)</h3>
<p>given a registration info object, a request object and the table info object it builds the request-&gt;requestvb-&gt;name oid from the index values and column information found in the table_info object. </p>
<p> Index values are extracted from the table_info index oid. </p>
<p> Definition at line 821 of file table.c. </p>
<p> References netsnmp_table_request_info_s::colnum, netsnmp_table_request_info_s::index_oid, netsnmp_table_request_info_s::index_oid_len, variable_list::name, variable_list::name_length, variable_list::name_loc, netsnmp_request_info_s::requestvb, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_clone_mem(), and SNMP_FREE.</p>
<h3>int netsnmp_table_build_result (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_request_info</code> * reqinfo, <code>netsnmp_table_request_info</code> * table_info, u_char type, u_char * result, size_t result_len)</h3>
<p>Builds the result to be returned to the agent given the table information. </p>
<p> Use this function to return results from lowel level handlers to the agent. It takes care of building the proper resulting oid (containing proper indexing) and inserts the result value into the returning varbind. </p>
<p> Definition at line 751 of file table.c. </p>
<p> References variable_list::name, variable_list::name_loc, netsnmp_table_build_oid(), NULL, netsnmp_request_info_s::requestvb, and snmp_set_var_typed_value().</p>
<h3>int netsnmp_update_indexes_from_variable_list (<code>netsnmp_table_request_info</code> * tri)</h3>
<p>builds an oid given a set of indexes. </p>
<p> Definition at line 866 of file table.c. </p>
<p> References build_oid_noalloc(), netsnmp_table_request_info_s::index_oid, netsnmp_table_request_info_s::index_oid_len, netsnmp_table_request_info_s::indexes, and NULL.</p>
<h3>int netsnmp_update_variable_list_from_index (<code>netsnmp_table_request_info</code> * tri)</h3>
<p>parses an OID into table indexses </p>
<p> Definition at line 850 of file table.c. </p>
<p> References netsnmp_table_request_info_s::index_oid, netsnmp_table_request_info_s::index_oid_len, netsnmp_table_request_info_s::indexes, parse_oid_indexes(), and snmp_reset_var_buffers().</p>
<h3>int table_helper_handler (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>implements the table helper handler </p>
<p> XXX-rks: memory leak. add cleanup handler? </p>
<p> none available </p>
<p> got one ok </p>
<p> for loop </p>
<p> Definition at line 142 of file table.c. </p>
<p> References netsnmp_table_request_info_s::colnum, netsnmp_mib_handler_s::handler_name, netsnmp_table_request_info_s::index_oid, netsnmp_table_request_info_s::index_oid_len, netsnmp_table_request_info_s::indexes, netsnmp_table_registration_info_s::indexes, netsnmp_table_registration_info_s::max_column, netsnmp_table_registration_info_s::min_column, netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::myvoid, netsnmp_agent_get_list_data(), netsnmp_call_next_handler(), netsnmp_create_data_list(), netsnmp_extract_table_info(), netsnmp_free_agent_data_sets(), netsnmp_request_add_list_data(), netsnmp_set_request_error(), netsnmp_request_info_s::next, netsnmp_mib_handler_s::next, variable_list::next_variable, NULL, netsnmp_table_registration_info_s::number_indexes, netsnmp_table_request_info_s::number_indexes, parse_one_oid_index(), netsnmp_request_info_s::processed, netsnmp_table_request_info_s::reg_info, netsnmp_request_info_s::requestvb, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_clone_varbind(), SNMP_FREE, snmp_log(), SNMP_MALLOC_TYPEDEF, snmp_oid_compare(), snmp_set_var_objid(), sprint_realloc_by_type(), netsnmp_request_info_s::status, variable_list::type, and netsnmp_table_registration_info_s::valid_columns. </p>
<p> Referenced by netsnmp_get_table_handler().</p>
