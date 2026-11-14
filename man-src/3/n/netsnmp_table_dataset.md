---
title: "netsnmp_table_dataset(3)"
name: "netsnmp_table_dataset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_table_dataset/"
description: "table_dataset – Helps you implement a table with automatted storage."
---

<p>table_dataset &#8211; Helps you implement a table with automatted storage.</p>
<h3>Functions</h3>
<p>void <code>netsnmp_init_table_dataset</code> (void) </p>
<p> <code>netsnmp_table_data_set</code> * <code>netsnmp_create_table_data_set</code> (const char *table_name)<br />
 <i>Create a netsnmp_table_data_set structure given a table_data definition. </i><br />
 <code>netsnmp_table_row</code> * <code>netsnmp_table_data_set_clone_row</code> (<code>netsnmp_table_row</code> *row)<br />
 <i>clones a dataset row, including all data. </i><br />
 NETSNMP_INLINE <code>netsnmp_table_data_set_storage</code> * <code>netsnmp_table_dataset_delete_data</code> (<code>netsnmp_table_data_set_storage</code> *data)<br />
 <i>deletes a single dataset table data. </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_delete_all_data</code> (<code>netsnmp_table_data_set_storage</code> *data)<br />
 <i>deletes all the data from this node and beyond in the linked list </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_delete_row</code> (<code>netsnmp_table_row</code> *row)<br />
 <i>deletes all the data from this node and beyond in the linked list </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_add_row</code> (<code>netsnmp_table_data_set</code> *table, <code>netsnmp_table_row</code> *row)<br />
 <i>adds a new row to a dataset table </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_replace_row</code> (<code>netsnmp_table_data_set</code> *table, <code>netsnmp_table_row</code> *origrow, <code>netsnmp_table_row</code> *newrow)<br />
 <i>adds a new row to a dataset table </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_remove_row</code> (<code>netsnmp_table_data_set</code> *table, <code>netsnmp_table_row</code> *row)<br />
 <i>removes a row from the table, but doesn&#8217;t delete/free the column values </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_remove_and_delete_row</code> (<code>netsnmp_table_data_set</code> *table, <code>netsnmp_table_row</code> *row)<br />
 <i>removes a row from the table and then deletes it (and all its data) </i><br />
 <code>netsnmp_table_row</code> * <code>netsnmp_table_data_set_create_row_from_defaults</code> (<code>netsnmp_table_data_set_storage</code> *defrow)<br />
 <i>creates a new row from an existing defined default set </i><br />
 int <code>netsnmp_table_set_add_default_row</code> (<code>netsnmp_table_data_set</code> *table_set, unsigned int column, int type, int writable, void *default_value, size_t default_value_len)<br />
 <i>adds a new default row to a table_set. </i><br />
 void <code>netsnmp_table_set_multi_add_default_row</code> (<code>netsnmp_table_data_set</code> *tset,&#8230;)<br />
 <i>adds multiple data column definitions to each row. </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_get_table_data_set_handler</code> (<code>netsnmp_table_data_set</code> *data_set)<br />
 <i>Given a netsnmp_table_data_set definition, create a handler for it. </i><br />
 int <code>netsnmp_register_table_data_set</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_table_data_set</code> *data_set, <code>netsnmp_table_registration_info</code> *table_info)<br />
 <i>register a given data_set at a given oid (specified in the netsnmp_handler_registration pointer). </i><br />
 <code>newrow_stash</code> * <code>netsnmp_table_data_set_create_newrowstash</code> (<code>netsnmp_table_data_set</code> *datatable, <code>netsnmp_table_request_info</code> *table_info) </p>
<p> int <code>netsnmp_table_data_set_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> NETSNMP_INLINE <code>netsnmp_table_data_set</code> * <code>netsnmp_extract_table_data_set</code> (<code>netsnmp_request_info</code> *request)<br />
 <i>extracts a netsnmp_table_data_set pointer from a given request </i><br />
 <code>netsnmp_table_data_set_storage</code> * <code>netsnmp_extract_table_data_set_column</code> (<code>netsnmp_request_info</code> *request, unsigned int column)<br />
 <i>extracts a netsnmp_table_data_set pointer from a given request </i><br />
 void <code>netsnmp_register_auto_data_table</code> (<code>netsnmp_table_data_set</code> *table_set, char *registration_name)<br />
 <i>registers a table_dataset so that the &#8216;add_row&#8217; snmpd.conf token can be used to add data to this table. </i><br />
 void <code>netsnmp_config_parse_table_set</code> (const char *token, char *line) </p>
<p> void <code>netsnmp_config_parse_add_row</code> (const char *token, char *line) </p>
<p> <code>netsnmp_table_row</code> * <code>netsnmp_table_data_set_get_first_row</code> (<code>netsnmp_table_data_set</code> *table)<br />
 <i>returns the first row in the table </i><br />
 <code>netsnmp_table_row</code> * <code>netsnmp_table_data_set_get_next_row</code> (<code>netsnmp_table_data_set</code> *table, <code>netsnmp_table_row</code> *row)<br />
 <i>returns the next row in the table </i><br />
 int <code>netsnmp_table_set_num_rows</code> (<code>netsnmp_table_data_set</code> *table) </p>
<p> <code>netsnmp_table_data_set_storage</code> * <code>netsnmp_table_data_set_find_column</code> (<code>netsnmp_table_data_set_storage</code> *start, unsigned int column)<br />
 <i>Finds a column within a given storage set, given the pointer to the start of the storage set list. </i><br />
 int <code>netsnmp_mark_row_column_writable</code> (<code>netsnmp_table_row</code> *row, int column, int writable)<br />
 <i>marks a given column in a row as writable or not. </i><br />
 int <code>netsnmp_set_row_column</code> (<code>netsnmp_table_row</code> *row, unsigned int column, int type, const char *value, size_t value_len)<br />
 <i>sets a given column in a row with data given a type, value, and length. </i><br />
 NETSNMP_INLINE void <code>netsnmp_table_dataset_add_index</code> (<code>netsnmp_table_data_set</code> *table, u_char type)<br />
 <i>adds an index to the table. </i><br />
 void <code>netsnmp_table_set_add_indexes</code> (<code>netsnmp_table_data_set</code> *tset,&#8230;)<br />
 <i>adds multiple indexes to a table_dataset helper object. </i></p>
<h2>Detailed Description</h2>
<p>Helps you implement a table with automatted storage. </p>
<p> This helper is obsolete. If you are writing a new module, please consider using the table_dataset2 helper instead. </p>
<p> This handler helps you implement a table where all the data is expected to be stored within the agent itself and not in some external storage location. It handles all MIB requests including GETs, GETNEXTs and SETs. It&#8217;s possible to simply create a table without actually ever defining a handler to be called when SNMP requests come in. To use the data, you can either attach a sub-handler that merely uses/manipulates the data further when requests come in, or you can loop through it externally when it&#8217;s actually needed. This handler is most useful in cases where a table is holding configuration data for something which gets triggered via another event. </p>
<p> NOTE NOTE NOTE: This helper isn&#8217;t complete and is likely to change somewhat over time. Specifically, the way it stores data internally may change drastically.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_table_data_set</code>* netsnmp_create_table_data_set (const char * table_name)</h3>
<p>Create a netsnmp_table_data_set structure given a table_data definition. </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 80 of file table_dataset.c. </p>
<p> References netsnmp_create_table_data(), NULL, SNMP_MALLOC_TYPEDEF, and netsnmp_table_data_set_s::table. </p>
<p> Referenced by netsnmp_config_parse_table_set().</p>
<h3>NETSNMP_INLINE <code>netsnmp_table_data_set</code>* netsnmp_extract_table_data_set (<code>netsnmp_request_info</code> * request)</h3>
<p>extracts a netsnmp_table_data_set pointer from a given request </p>
<p> Definition at line 816 of file table_dataset.c. </p>
<p> References netsnmp_request_get_list_data().</p>
<h3><code>netsnmp_table_data_set_storage</code>* netsnmp_extract_table_data_set_column (<code>netsnmp_request_info</code> * request, unsigned int column)</h3>
<p>extracts a netsnmp_table_data_set pointer from a given request </p>
<p> Definition at line 826 of file table_dataset.c. </p>
<p> References netsnmp_extract_table_row_data(), and netsnmp_table_data_set_find_column().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_table_data_set_handler (<code>netsnmp_table_data_set</code> * data_set)</h3>
<p>Given a netsnmp_table_data_set definition, create a handler for it. </p>
<p> Definition at line 356 of file table_dataset.c. </p>
<p> References netsnmp_mib_handler_s::flags, MIB_HANDLER_AUTO_NEXT, netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_table_data_set_helper_handler(), NULL, and snmp_log(). </p>
<p> Referenced by netsnmp_register_table_data_set().</p>
<h3>int netsnmp_mark_row_column_writable (<code>netsnmp_table_row</code> * row, int column, int writable)</h3>
<p>marks a given column in a row as writable or not. </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 1187 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::column, netsnmp_table_row_s::data, netsnmp_table_data_set_find_column(), netsnmp_table_data_set_storage_s::next, snmp_log(), SNMP_MALLOC_TYPEDEF, and netsnmp_table_data_set_storage_s::writable. </p>
<p> Referenced by netsnmp_config_parse_add_row(), and netsnmp_table_data_set_create_row_from_defaults().</p>
<h3>void netsnmp_register_auto_data_table (<code>netsnmp_table_data_set</code> * table_set, char * registration_name)</h3>
<p>registers a table_dataset so that the &#8216;add_row&#8217; snmpd.conf token can be used to add data to this table. </p>
<p> If registration_name is NULL then the name used when the table was created will be used instead. </p>
<p> <code>Todo</code></p>
<dl>
<dd>create a properly free&#8217;ing registeration pointer for the datalist, and get the datalist freed at shutdown.</dl>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 853 of file table_dataset.c. </p>
<p> References netsnmp_table_data_s::name, netsnmp_add_list_data(), netsnmp_create_data_list(), NULL, SNMP_MALLOC_TYPEDEF, netsnmp_table_data_set_s::table, and data_set_tables_s::table_set. </p>
<p> Referenced by netsnmp_config_parse_table_set().</p>
<h3>int netsnmp_register_table_data_set (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_table_data_set</code> * data_set, <code>netsnmp_table_registration_info</code> * table_info)</h3>
<p>register a given data_set at a given oid (specified in the netsnmp_handler_registration pointer). </p>
<p> The reginfo-&gt;handler-&gt;access_method *may* be null if the call doesn&#8217;t ever want to be called for SNMP operations. </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 382 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::column, netsnmp_table_data_set_s::default_row, netsnmp_table_registration_info_s::indexes, netsnmp_table_data_s::indexes_template, netsnmp_table_registration_info_s::max_column, netsnmp_table_registration_info_s::min_column, netsnmp_get_table_data_set_handler(), netsnmp_inject_handler(), netsnmp_register_table_data(), netsnmp_table_data_set_storage_s::next, NULL, snmp_clone_varbind(), SNMP_MALLOC_TYPEDEF, SNMP_MAX, SNMP_MIN, and netsnmp_table_data_set_s::table. </p>
<p> Referenced by netsnmp_config_parse_table_set().</p>
<h3>int netsnmp_set_row_column (<code>netsnmp_table_row</code> * row, unsigned int column, int type, const char * value, size_t value_len)</h3>
<p>sets a given column in a row with data given a type, value, and length. </p>
<p> Data is memdup&#8217;ed by the function. </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 1222 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::column, netsnmp_table_row_s::data, netsnmp_table_data_set_storage_s::data, netsnmp_table_data_set_storage_s::data_len, memdup(), netsnmp_table_data_set_find_column(), netsnmp_table_data_set_storage_s::next, SNMP_FREE, snmp_log(), SNMP_MALLOC_TYPEDEF, netsnmp_table_data_set_storage_s::string, netsnmp_table_data_set_storage_s::type, and netsnmp_table_data_set_storage_s::voidp. </p>
<p> Referenced by netsnmp_config_parse_add_row(), and netsnmp_table_data_set_create_row_from_defaults().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_set_clone_row (<code>netsnmp_table_row</code> * row)</h3>
<p>clones a dataset row, including all data. </p>
<p> Definition at line 92 of file table_dataset.c. </p>
<p> References netsnmp_table_row_s::data, memdup(), netsnmp_table_data_clone_row(), netsnmp_table_dataset_delete_row(), netsnmp_table_data_set_storage_s::next, and NULL. </p>
<p> Referenced by netsnmp_table_data_set_helper_handler().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_set_create_row_from_defaults (<code>netsnmp_table_data_set_storage</code> * defrow)</h3>
<p>creates a new row from an existing defined default set </p>
<p> Definition at line 226 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::column, netsnmp_table_data_set_storage_s::data, netsnmp_table_data_set_storage_s::data_len, netsnmp_create_table_data_row(), netsnmp_mark_row_column_writable(), netsnmp_set_row_column(), netsnmp_table_data_set_storage_s::next, NULL, netsnmp_table_data_set_storage_s::type, netsnmp_table_data_set_storage_s::voidp, and netsnmp_table_data_set_storage_s::writable. </p>
<p> Referenced by netsnmp_table_data_set_create_newrowstash().</p>
<h3><code>netsnmp_table_data_set_storage</code>* netsnmp_table_data_set_find_column (<code>netsnmp_table_data_set_storage</code> * start, unsigned int column)</h3>
<p>Finds a column within a given storage set, given the pointer to the start of the storage set list. </p>
<p> Definition at line 1175 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::column, and netsnmp_table_data_set_storage_s::next. </p>
<p> Referenced by netsnmp_extract_table_data_set_column(), netsnmp_mark_row_column_writable(), netsnmp_set_row_column(), netsnmp_table_data_set_helper_handler(), and netsnmp_table_set_add_default_row().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_set_get_first_row (<code>netsnmp_table_data_set</code> * table)</h3>
<p>returns the first row in the table </p>
<p> Definition at line 1144 of file table_dataset.c. </p>
<p> References netsnmp_table_data_get_first_row(), and netsnmp_table_data_set_s::table.</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_set_get_next_row (<code>netsnmp_table_data_set</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>returns the next row in the table </p>
<p> Definition at line 1151 of file table_dataset.c. </p>
<p> References netsnmp_table_data_get_next_row(), and netsnmp_table_data_set_s::table.</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_add_index (<code>netsnmp_table_data_set</code> * table, u_char type)</h3>
<p>adds an index to the table. </p>
<p> Call this repeatly for each index. </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 1276 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_s::table. </p>
<p> Referenced by netsnmp_table_set_add_indexes().</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_add_row (<code>netsnmp_table_data_set</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>adds a new row to a dataset table </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 171 of file table_dataset.c. </p>
<p> References netsnmp_table_data_add_row(), and netsnmp_table_data_set_s::table. </p>
<p> Referenced by netsnmp_table_data_set_helper_handler().</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_delete_all_data (<code>netsnmp_table_data_set_storage</code> * data)</h3>
<p>deletes all the data from this node and beyond in the linked list </p>
<p> Definition at line 148 of file table_dataset.c. </p>
<p> References netsnmp_table_dataset_delete_data(). </p>
<p> Referenced by netsnmp_table_dataset_delete_row(), and netsnmp_table_dataset_remove_and_delete_row().</p>
<h3>NETSNMP_INLINE <code>netsnmp_table_data_set_storage</code>* netsnmp_table_dataset_delete_data (<code>netsnmp_table_data_set_storage</code> * data)</h3>
<p>deletes a single dataset table data. </p>
<p> returns the (possibly still good) next pointer of the deleted data object. </p>
<p> Definition at line 135 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::data, netsnmp_table_data_set_storage_s::next, NULL, SNMP_FREE, and netsnmp_table_data_set_storage_s::voidp. </p>
<p> Referenced by netsnmp_table_dataset_delete_all_data().</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_delete_row (<code>netsnmp_table_row</code> * row)</h3>
<p>deletes all the data from this node and beyond in the linked list </p>
<p> Definition at line 158 of file table_dataset.c. </p>
<p> References netsnmp_table_data_delete_row(), and netsnmp_table_dataset_delete_all_data(). </p>
<p> Referenced by netsnmp_table_data_set_clone_row(), and netsnmp_table_data_set_helper_handler().</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_remove_and_delete_row (<code>netsnmp_table_data_set</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>removes a row from the table and then deletes it (and all its data) </p>
<p> Definition at line 203 of file table_dataset.c. </p>
<p> References netsnmp_table_data_remove_and_delete_row(), netsnmp_table_dataset_delete_all_data(), and netsnmp_table_data_set_s::table. </p>
<p> Referenced by netsnmp_table_data_set_helper_handler().</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_remove_row (<code>netsnmp_table_data_set</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>removes a row from the table, but doesn&#8217;t delete/free the column values </p>
<p> Definition at line 192 of file table_dataset.c. </p>
<p> References netsnmp_table_data_remove_and_delete_row(), and netsnmp_table_data_set_s::table.</p>
<h3>NETSNMP_INLINE void netsnmp_table_dataset_replace_row (<code>netsnmp_table_data_set</code> * table, <code>netsnmp_table_row</code> * origrow, <code>netsnmp_table_row</code> * newrow)</h3>
<p>adds a new row to a dataset table </p>
<p> Definition at line 181 of file table_dataset.c. </p>
<p> References netsnmp_table_data_replace_row(), and netsnmp_table_data_set_s::table. </p>
<p> Referenced by netsnmp_table_data_set_helper_handler().</p>
<h3>int netsnmp_table_set_add_default_row (<code>netsnmp_table_data_set</code> * table_set, unsigned int column, int type, int writable, void * default_value, size_t default_value_len)</h3>
<p>adds a new default row to a table_set. </p>
<p> Arguments should be the table_set, column number, variable type and finally a 1 if it is allowed to be writable, or a 0 if not. If the default_value field is not NULL, it will be used to populate new valuse in that column fro newly created rows. It is copied into the storage template (free your calling argument). </p>
<p> returns SNMPERR_SUCCESS or SNMPERR_FAILURE </p>
<p> Definition at line 252 of file table_dataset.c. </p>
<p> References netsnmp_table_data_set_storage_s::column, netsnmp_table_data_set_storage_s::data, netsnmp_table_data_set_storage_s::data_len, netsnmp_table_data_set_s::default_row, memdup(), netsnmp_table_data_set_find_column(), netsnmp_table_data_set_storage_s::next, NULL, snmp_log(), SNMP_MALLOC_TYPEDEF, netsnmp_table_data_set_storage_s::type, netsnmp_table_data_set_storage_s::voidp, and netsnmp_table_data_set_storage_s::writable. </p>
<p> Referenced by netsnmp_config_parse_table_set(), and netsnmp_table_set_multi_add_default_row().</p>
<h3>void netsnmp_table_set_add_indexes (<code>netsnmp_table_data_set</code> * tset, &#8230;)</h3>
<p>adds multiple indexes to a table_dataset helper object. </p>
<p> To end the list, use a 0 after the list of ASN index types. </p>
<p> Definition at line 1287 of file table_dataset.c. </p>
<p> References netsnmp_table_dataset_add_index().</p>
<h3>void netsnmp_table_set_multi_add_default_row (<code>netsnmp_table_data_set</code> * tset, &#8230;)</h3>
<p>adds multiple data column definitions to each row. </p>
<p> Functionally, this is a wrapper around calling netsnmp_table_set_add_default_row repeatedly for you. </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 313 of file table_dataset.c. </p>
<p> References netsnmp_table_set_add_default_row().</p>
