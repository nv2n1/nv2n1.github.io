---
title: "netsnmp_table_data(3)"
name: "netsnmp_table_data"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_table_data/"
description: "table_data – Helps you implement a table with datamatted storage."
---

<p>table_data &#8211; Helps you implement a table with datamatted storage.</p>
<h3>Modules</h3>
<p><code>table_dataset</code><br />
 <i>Helps you implement a table with automatted storage. </i></p>
<h3>Functions</h3>
<pre><code>void netsnmp_table_data_generate_index_oid (netsnmp_table_row *row)



netsnmp_table_data * netsnmp_create_table_data (const char *name)


creates and returns a pointer to table data set


netsnmp_table_row * netsnmp_create_table_data_row (void)


creates and returns a pointer to table data set


netsnmp_table_row * netsnmp_table_data_clone_row (netsnmp_table_row *row)


clones a data row.


void * netsnmp_table_data_delete_row (netsnmp_table_row *row)


deletes a row's memory.


int netsnmp_table_data_add_row (netsnmp_table_data *table, netsnmp_table_row *row)


Adds a row of data to a given table (stored in proper lexographical order).


NETSNMP_INLINE void netsnmp_table_data_replace_row (netsnmp_table_data *table, netsnmp_table_row *origrow, netsnmp_table_row *newrow)


swaps out origrow with newrow.


netsnmp_table_row * netsnmp_table_data_remove_row (netsnmp_table_data *table, netsnmp_table_row *row)


removes a row of data to a given table and returns it (no free's called)


void * netsnmp_table_data_remove_and_delete_row (netsnmp_table_data *table, netsnmp_table_row *row)


removes and frees a row of data to a given table and returns the void *


netsnmp_table_data * netsnmp_table_data_create_table (const char *name, long flags)



void netsnmp_table_data_delete_table (netsnmp_table_data *table)



netsnmp_table_row * netsnmp_table_data_create_row (void *entry)



int netsnmp_table_data_copy_row (netsnmp_table_row *old_row, netsnmp_table_row *new_row)



void * netsnmp_table_data_remove_delete_row (netsnmp_table_data *table, netsnmp_table_row *row)



netsnmp_mib_handler * netsnmp_get_table_data_handler (netsnmp_table_data *table)


Creates a table_data handler and returns it.


int netsnmp_register_table_data (netsnmp_handler_registration *reginfo, netsnmp_table_data *table, netsnmp_table_registration_info *table_info)


registers a handler as a data table.


int netsnmp_register_read_only_table_data (netsnmp_handler_registration *reginfo, netsnmp_table_data *table, netsnmp_table_registration_info *table_info)


registers a handler as a read-only data table If table_info != NULL, it registers it as a normal table too.


int netsnmp_table_data_helper_handler (netsnmp_mib_handler *handler, netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *requests)



netsnmp_table_data * netsnmp_extract_table (netsnmp_request_info *request)


extracts the table being accessed passed from the table_data helper


netsnmp_table_row * netsnmp_extract_table_row (netsnmp_request_info *request)


extracts the row being accessed passed from the table_data helper


void * netsnmp_extract_table_row_data (netsnmp_request_info *request)


extracts the data from the row being accessed passed from the table_data helper


NETSNMP_INLINE void netsnmp_insert_table_row (netsnmp_request_info *request, netsnmp_table_row *row)


inserts a newly created table_data row into a request


int netsnmp_table_data_build_result (netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *request, netsnmp_table_row *row, int column, u_char type, u_char *result_data, size_t result_data_len)



netsnmp_table_row * netsnmp_table_data_get_first_row (netsnmp_table_data *table)


returns the first row in the table


netsnmp_table_row * netsnmp_table_data_get_next_row (netsnmp_table_data *table, netsnmp_table_row *row)


returns the next row in the table


netsnmp_table_row * netsnmp_table_data_get (netsnmp_table_data *table, netsnmp_variable_list *indexes)


finds the data in 'datalist' stored at 'indexes'


netsnmp_table_row * netsnmp_table_data_get_from_oid (netsnmp_table_data *table, oid *searchfor, size_t searchfor_len)


finds the data in 'datalist' stored at the searchfor oid


int netsnmp_table_data_num_rows (netsnmp_table_data *table)



netsnmp_table_row * netsnmp_table_data_row_first (netsnmp_table_data *table)



netsnmp_table_row * netsnmp_table_data_row_get (netsnmp_table_data *table, netsnmp_table_row *row)



netsnmp_table_row * netsnmp_table_data_row_next (netsnmp_table_data *table, netsnmp_table_row *row)



netsnmp_table_row * netsnmp_table_data_row_get_byoid (netsnmp_table_data *table, oid *instance, size_t len)



netsnmp_table_row * netsnmp_table_data_row_next_byoid (netsnmp_table_data *table, oid *instance, size_t len)



netsnmp_table_row * netsnmp_table_data_row_get_byidx (netsnmp_table_data *table, netsnmp_variable_list *indexes)



netsnmp_table_row * netsnmp_table_data_row_next_byidx (netsnmp_table_data *table, netsnmp_variable_list *indexes)



int netsnmp_table_data_row_count (netsnmp_table_data *table)



void * netsnmp_table_data_entry_first (netsnmp_table_data *table)



void * netsnmp_table_data_entry_get (netsnmp_table_data *table, netsnmp_table_row *row)



void * netsnmp_table_data_entry_next (netsnmp_table_data *table, netsnmp_table_row *row)



void * netsnmp_table_data_entry_get_byidx (netsnmp_table_data *table, netsnmp_variable_list *indexes)



void * netsnmp_table_data_entry_next_byidx (netsnmp_table_data *table, netsnmp_variable_list *indexes)



void * netsnmp_table_data_entry_get_byoid (netsnmp_table_data *table, oid *instance, size_t len)



void * netsnmp_table_data_entry_next_byoid (netsnmp_table_data *table, oid *instance, size_t len)</code></pre>
<h2>Detailed Description</h2>
<p>Helps you implement a table with datamatted storage. </p>
<p> This helper is obsolete. If you are writing a new module, please consider using the table_tdata helper instead. </p>
<p> This helper helps you implement a table where all the indexes are expected to be stored within the agent itself and not in some external storage location. It can be used to store a list of rows, where a row consists of the indexes to the table and a generic data pointer. You can then implement a subhandler which is passed the exact row definition and data it must return data for or accept data for. Complex GETNEXT handling is greatly simplified in this case.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_table_data</code>* netsnmp_create_table_data (const char * name)</h3>
<p>creates and returns a pointer to table data set </p>
<p> Definition at line 52 of file table_data.c. </p>
<p> References netsnmp_table_data_s::name, and SNMP_MALLOC_TYPEDEF. </p>
<p> Referenced by netsnmp_create_table_data_set(), and netsnmp_table_data_create_table().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_create_table_data_row (void)</h3>
<p>creates and returns a pointer to table data set </p>
<p> <code>Examples: </code> <code>data_set.c</code>. </p>
<p> Definition at line 62 of file table_data.c. </p>
<p> References SNMP_MALLOC_TYPEDEF. </p>
<p> Referenced by netsnmp_config_parse_add_row(), and netsnmp_table_data_set_create_row_from_defaults().</p>
<h3><code>netsnmp_table_data</code>* netsnmp_extract_table (<code>netsnmp_request_info</code> * request)</h3>
<p>extracts the table being accessed passed from the table_data helper </p>
<p> Definition at line 649 of file table_data.c. </p>
<p> References netsnmp_request_get_list_data().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_extract_table_row (<code>netsnmp_request_info</code> * request)</h3>
<p>extracts the row being accessed passed from the table_data helper </p>
<p> Definition at line 657 of file table_data.c. </p>
<p> References netsnmp_request_get_list_data(). </p>
<p> Referenced by netsnmp_extract_table_row_data(), and netsnmp_table_data_set_helper_handler().</p>
<h3>void* netsnmp_extract_table_row_data (<code>netsnmp_request_info</code> * request)</h3>
<p>extracts the data from the row being accessed passed from the table_data helper </p>
<p> Definition at line 666 of file table_data.c. </p>
<p> References netsnmp_table_row_s::data, netsnmp_extract_table_row(), and NULL. </p>
<p> Referenced by netsnmp_extract_table_data_set_column().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_table_data_handler (<code>netsnmp_table_data</code> * table)</h3>
<p>Creates a table_data handler and returns it. </p>
<p> Definition at line 371 of file table_data.c. </p>
<p> References netsnmp_mib_handler_s::flags, MIB_HANDLER_AUTO_NEXT, netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_table_data_helper_handler(), NULL, and snmp_log(). </p>
<p> Referenced by netsnmp_register_table_data().</p>
<h3>NETSNMP_INLINE void netsnmp_insert_table_row (<code>netsnmp_request_info</code> * request, <code>netsnmp_table_row</code> * row)</h3>
<p>inserts a newly created table_data row into a request </p>
<p> Definition at line 678 of file table_data.c. </p>
<p> References build_oid_noalloc(), netsnmp_table_request_info_s::indexes, netsnmp_create_data_list(), netsnmp_extract_table_info(), netsnmp_request_add_list_data(), netsnmp_request_info_s::next, NULL, netsnmp_request_info_s::prev, and snmp_oid_compare().</p>
<h3>int netsnmp_register_read_only_table_data (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_table_data</code> * table, <code>netsnmp_table_registration_info</code> * table_info)</h3>
<p>registers a handler as a read-only data table If table_info != NULL, it registers it as a normal table too. </p>
<p> Definition at line 405 of file table_data.c. </p>
<p> References netsnmp_get_read_only_handler(), netsnmp_inject_handler(), and netsnmp_register_table_data().</p>
<h3>int netsnmp_register_table_data (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_table_data</code> * table, <code>netsnmp_table_registration_info</code> * table_info)</h3>
<p>registers a handler as a data table. </p>
<p> If table_info != NULL, it registers it as a normal table too. </p>
<p> Definition at line 394 of file table_data.c. </p>
<p> References netsnmp_get_table_data_handler(), netsnmp_inject_handler(), and netsnmp_register_table(). </p>
<p> Referenced by netsnmp_register_read_only_table_data(), and netsnmp_register_table_data_set().</p>
<h3>int netsnmp_table_data_add_row (<code>netsnmp_table_data</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>Adds a row of data to a given table (stored in proper lexographical order). </p>
<p> returns SNMPERR_SUCCESS on successful addition. or SNMPERR_GENERR on failure (E.G., indexes already existed) </p>
<p> xxx-rks: remove invalid row? </p>
<p> Definition at line 130 of file table_data.c. </p>
<p> References netsnmp_table_data_s::first_row, netsnmp_table_row_s::index_oid, netsnmp_table_row_s::index_oid_len, netsnmp_table_row_s::indexes, netsnmp_table_data_s::last_row, netsnmp_table_data_s::name, netsnmp_table_data_generate_index_oid(), netsnmp_table_row_s::next, NULL, netsnmp_table_row_s::prev, snmp_free_varbind(), snmp_log(), snmp_oid_compare(), and netsnmp_table_data_s::store_indexes. </p>
<p> Referenced by netsnmp_config_parse_add_row(), netsnmp_table_data_replace_row(), and netsnmp_table_dataset_add_row().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_clone_row (<code>netsnmp_table_row</code> * row)</h3>
<p>clones a data row. </p>
<p> DOES NOT CLONE THE CONTAINED DATA. </p>
<p> Definition at line 70 of file table_data.c. </p>
<p> References memdup(), NULL, and snmp_clone_varbind(). </p>
<p> Referenced by netsnmp_table_data_set_clone_row().</p>
<h3>void* netsnmp_table_data_delete_row (<code>netsnmp_table_row</code> * row)</h3>
<p>deletes a row&#8217;s memory. </p>
<p> returns the void data that it doesn&#8217;t know how to delete. </p>
<p> Definition at line 101 of file table_data.c. </p>
<p> References netsnmp_table_row_s::data, netsnmp_table_row_s::index_oid, netsnmp_table_row_s::indexes, NULL, SNMP_FREE, and snmp_free_varbind(). </p>
<p> Referenced by netsnmp_table_data_delete_table(), netsnmp_table_data_remove_and_delete_row(), and netsnmp_table_dataset_delete_row().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_get (<code>netsnmp_table_data</code> * table, <code>netsnmp_variable_list</code> * indexes)</h3>
<p>finds the data in &#8216;datalist&#8217; stored at &#8216;indexes&#8217; </p>
<p> Definition at line 804 of file table_data.c. </p>
<p> References build_oid_noalloc(), netsnmp_table_data_get_from_oid(), and NULL. </p>
<p> Referenced by netsnmp_table_data_row_get_byidx().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_get_first_row (<code>netsnmp_table_data</code> * table)</h3>
<p>returns the first row in the table </p>
<p> Definition at line 785 of file table_data.c. </p>
<p> References netsnmp_table_data_s::first_row, and NULL. </p>
<p> Referenced by netsnmp_table_data_entry_first(), netsnmp_table_data_row_first(), and netsnmp_table_data_set_get_first_row().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_get_from_oid (<code>netsnmp_table_data</code> * table, oid * searchfor, size_t searchfor_len)</h3>
<p>finds the data in &#8216;datalist&#8217; stored at the searchfor oid </p>
<p> Definition at line 818 of file table_data.c. </p>
<p> References netsnmp_table_data_s::first_row, netsnmp_table_row_s::index_oid, netsnmp_table_row_s::index_oid_len, netsnmp_table_row_s::next, NULL, and snmp_oid_compare(). </p>
<p> Referenced by netsnmp_table_data_get(), netsnmp_table_data_row_get(), and netsnmp_table_data_row_get_byoid().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_get_next_row (<code>netsnmp_table_data</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>returns the next row in the table </p>
<p> Definition at line 794 of file table_data.c. </p>
<p> References netsnmp_table_row_s::next, and NULL. </p>
<p> Referenced by netsnmp_table_data_row_next(), and netsnmp_table_data_set_get_next_row().</p>
<h3>void* netsnmp_table_data_remove_and_delete_row (<code>netsnmp_table_data</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>removes and frees a row of data to a given table and returns the void * </p>
<p> returns the void * data on successful deletion. or NULL on failure (bad arguments) </p>
<p> Definition at line 270 of file table_data.c. </p>
<p> References netsnmp_table_data_delete_row(), netsnmp_table_data_remove_row(), and NULL. </p>
<p> Referenced by netsnmp_table_data_remove_delete_row(), netsnmp_table_dataset_remove_and_delete_row(), and netsnmp_table_dataset_remove_row().</p>
<h3><code>netsnmp_table_row</code>* netsnmp_table_data_remove_row (<code>netsnmp_table_data</code> * table, <code>netsnmp_table_row</code> * row)</h3>
<p>removes a row of data to a given table and returns it (no free&#8217;s called) </p>
<p> returns the row pointer itself on successful removing. or NULL on failure (bad arguments) </p>
<p> Definition at line 244 of file table_data.c. </p>
<p> References netsnmp_table_data_s::first_row, netsnmp_table_data_s::last_row, netsnmp_table_row_s::next, NULL, and netsnmp_table_row_s::prev. </p>
<p> Referenced by netsnmp_table_data_remove_and_delete_row(), and netsnmp_table_data_replace_row().</p>
<h3>NETSNMP_INLINE void netsnmp_table_data_replace_row (<code>netsnmp_table_data</code> * table, <code>netsnmp_table_row</code> * origrow, <code>netsnmp_table_row</code> * newrow)</h3>
<p>swaps out origrow with newrow. </p>
<p> This does *not* delete/free anything! </p>
<p> Definition at line 229 of file table_data.c. </p>
<p> References netsnmp_table_data_add_row(), and netsnmp_table_data_remove_row(). </p>
<p> Referenced by netsnmp_table_dataset_replace_row().</p>
