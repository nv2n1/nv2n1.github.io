---
title: "netsnmp_table_iterator(3)"
name: "netsnmp_table_iterator"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_table_iterator/"
description: "table_iterator – The table iterator helper is designed to simplify the task of writing a table handler for the net-snmp agent when the data being accessed is not in an oid sorted form and must be a..."
---

<p>table_iterator &#8211; The table iterator helper is designed to simplify the task of writing a table handler for the net-snmp agent when the data being accessed is not in an oid sorted form and must be accessed externally.</p>
<h3>Data Structures</h3>
<pre><code>struct ti_cache_info_s



struct netsnmp_iterator_info_s


Holds iterator information containing functions which should be called by the iterator_handler to loop over your data set and sort it in a SNMP specific manner.


struct netsnmp_iterator_info_s


Holds iterator information containing functions which should be called by the iterator_handler to loop over your data set and sort it in a SNMP specific manner.



Defines
#define TI_REQUEST_CACHE   'ti_cache'



#define TABLE_ITERATOR_NOTAGAIN   255



#define TABLE_ITERATOR_NAME   'table_iterator'



Typedefs</code></pre>
<p> typedef <code>ti_cache_info_s</code> <code>ti_cache_info</code> </p>
<p> typedef <code>netsnmp_variable_list</code> *( <code>Netsnmp_First_Data_Point</code> )(void **loop_context, void **data_context, <code>netsnmp_variable_list</code> *, struct <code>netsnmp_iterator_info_s</code> *) </p>
<p> typedef <code>netsnmp_variable_list</code> *( <code>Netsnmp_Next_Data_Point</code> )(void **loop_context, void **data_context, <code>netsnmp_variable_list</code> *, struct <code>netsnmp_iterator_info_s</code> *) </p>
<p> typedef void *( <code>Netsnmp_Make_Data_Context</code> )(void *loop_context, struct <code>netsnmp_iterator_info_s</code> *) </p>
<p> typedef void( <code>Netsnmp_Free_Loop_Context</code> )(void *, struct <code>netsnmp_iterator_info_s</code> *) </p>
<p> typedef void( <code>Netsnmp_Free_Data_Context</code> )(void *, struct <code>netsnmp_iterator_info_s</code> *) </p>
<p> typedef <code>netsnmp_iterator_info_s</code> <code>netsnmp_iterator_info</code><br />
 <i>Typedefs the </i><code>netsnmp_iterator_info_s</code> struct into netsnmp_iterator_info.</p>
<h3>Functions</h3>
<p><code>netsnmp_iterator_info</code> * <code>netsnmp_iterator_create_table</code> (<code>Netsnmp_First_Data_Point</code> *firstDP, <code>Netsnmp_Next_Data_Point</code> *nextDP, <code>Netsnmp_First_Data_Point</code> *getidx, <code>netsnmp_variable_list</code> *indexes) </p>
<p> void <code>netsnmp_iterator_delete_table</code> (<code>netsnmp_iterator_info</code> *iinfo) </p>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_table_iterator_handler</code> (<code>netsnmp_iterator_info</code> *iinfo)<br />
 <i>returns a netsnmp_mib_handler object for the table_iterator helper </i><br />
 int <code>netsnmp_register_table_iterator</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_iterator_info</code> *iinfo)<br />
 <i>Creates and registers a table iterator helper handler calling netsnmp_create_handler with a handler name set to TABLE_ITERATOR_NAME and access method, netsnmp_table_iterator_helper_handler. </i><br />
 NETSNMP_INLINE void * <code>netsnmp_extract_iterator_context</code> (<code>netsnmp_request_info</code> *request)<br />
 <i>extracts the table_iterator specific data from a request. </i><br />
 NETSNMP_INLINE void <code>netsnmp_insert_iterator_context</code> (<code>netsnmp_request_info</code> *request, void *data)<br />
 <i>inserts table_iterator specific data for a newly created row into a request </i><br />
 int <code>netsnmp_table_iterator_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> void * <code>netsnmp_iterator_row_first</code> (<code>netsnmp_iterator_info</code> *iinfo) </p>
<p> void * <code>netsnmp_iterator_row_get</code> (<code>netsnmp_iterator_info</code> *iinfo, void *row) </p>
<p> void * <code>netsnmp_iterator_row_next</code> (<code>netsnmp_iterator_info</code> *iinfo, void *row) </p>
<p> void * <code>netsnmp_iterator_row_get_byidx</code> (<code>netsnmp_iterator_info</code> *iinfo, <code>netsnmp_variable_list</code> *indexes) </p>
<p> void * <code>netsnmp_iterator_row_next_byidx</code> (<code>netsnmp_iterator_info</code> *iinfo, <code>netsnmp_variable_list</code> *indexes) </p>
<p> void * <code>netsnmp_iterator_row_get_byoid</code> (<code>netsnmp_iterator_info</code> *iinfo, oid *instance, size_t len) </p>
<p> void * <code>netsnmp_iterator_row_next_byoid</code> (<code>netsnmp_iterator_info</code> *iinfo, oid *instance, size_t len) </p>
<p> int <code>netsnmp_iterator_row_count</code> (<code>netsnmp_iterator_info</code> *iinfo)</p>
<h3>Variables</h3>
<p><code>Netsnmp_Node_Handler</code> <code>netsnmp_table_iterator_helper_handler</code></p>
<h2>Detailed Description</h2>
<p>The table iterator helper is designed to simplify the task of writing a table handler for the net-snmp agent when the data being accessed is not in an oid sorted form and must be accessed externally. </p>
<p> Functionally, it is a specialized version of the more generic table helper but easies the burden of GETNEXT processing by manually looping through all the data indexes retrieved through function calls which should be supplied by the module that wishes help. The module the table_iterator helps should, afterwards, never be called for the case of &#8216;MODE_GETNEXT&#8217; and only for the GET and SET related modes instead. </p>
<p> The fundamental notion between the table iterator is that it allows your code to iterate over each &#8216;row&#8217; within your data storage mechanism, without requiring that it be sorted in a SNMP-index-compliant manner. Through the get_first_data_point and get_next_data_point hooks, the table_iterator helper will repeatedly call your hooks to find the &#8216;proper&#8217; row of data that needs processing. The following concepts are important: </p>
<dl>
<dt>*</p>
<dd>A loop context is a pointer which indicates where in the current processing of a set of rows you currently are. Allows the get_*_data_point routines to move from one row to the next, once the iterator handler has identified the appropriate row for this request, the job of the loop context is done. The most simple example would be a pointer to an integer which simply counts rows from 1 to X. More commonly, it might be a pointer to a linked list node, or someother internal or external reference to a data set (file seek value, array pointer, &#8230;). If allocated during iteration, either the free_loop_context_at_end (preferably) or the free_loop_context pointers should be set.</dl>
<dl>
<dt>*</p>
<dd>A data context is something that your handler code can use in order to retrieve the rest of the data for the needed row. This data can be accessed in your handler via netsnmp_extract_iterator_context api with the netsnmp_request_info structure that&#8217;s passed in. The important difference between a loop context and a data context is that multiple data contexts can be kept by the table_iterator helper, where as only one loop context will ever be held by the table_iterator helper. If allocated during iteration the free_data_context pointer should be set to an appropriate function.</dl>
<p> The table iterator operates in a series of steps that call your code hooks from your netsnmp_iterator_info registration pointer. </p>
<dl>
<dt>*</p>
<dd>the get_first_data_point hook is called at the beginning of processing. It should set the variable list to a list of indexes for the given table. It should also set the loop_context and maybe a data_context which you will get a pointer back to when it needs to call your code to retrieve actual data later. The list of indexes should be returned after being update.</dl>
<dl>
<dt>*</p>
<dd>the get_next_data_point hook is then called repeatedly and is passed the loop context and the data context for it to update. The indexes, loop context and data context should all be updated if more data is available, otherwise they should be left alone and a NULL should be returned. Ideally, it should update the loop context without the need to reallocate it. If reallocation is necessary for every iterative step, then the free_loop_context function pointer should be set. If not, then the free_loop_context_at_end pointer should be set, which is more efficient since a malloc/free will only be performed once for every iteration.</dl>
<h2>Typedef Documentation</h2>
<h3>struct <code>netsnmp_iterator_info_s</code> <code>netsnmp_iterator_info</code></h3>
<p>Typedefs the <code>netsnmp_iterator_info_s</code> struct into netsnmp_iterator_info.</p>
<h2>Function Documentation</h2>
<h3>void * netsnmp_extract_iterator_context (<code>netsnmp_request_info</code> * request)</h3>
<p>extracts the table_iterator specific data from a request. </p>
<p> This function extracts the table iterator specific data from a netsnmp_request_info object. Calls netsnmp_request_get_list_data with request-&gt;parent_data set with data from a request that was added previously by a module and TABLE_ITERATOR_NAME handler name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>request</i> the netsnmp request info structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a void pointer(request-&gt;parent_data-&gt;data), otherwise NULL is returned if request is NULL or request-&gt;parent_data is NULL or request-&gt;parent_data object is not found.the net</dl>
<p> Definition at line 234 of file table_iterator.c. </p>
<p> References netsnmp_request_get_list_data(), and TABLE_ITERATOR_NAME.</p>
<h3><code>netsnmp_mib_handler</code> * netsnmp_get_table_iterator_handler (<code>netsnmp_iterator_info</code> * iinfo)</h3>
<p>returns a netsnmp_mib_handler object for the table_iterator helper </p>
<p> Definition at line 169 of file table_iterator.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_table_iterator_helper_handler, NULL, and TABLE_ITERATOR_NAME. </p>
<p> Referenced by netsnmp_register_table_iterator().</p>
<h3>void netsnmp_insert_iterator_context (<code>netsnmp_request_info</code> * request, void * data)</h3>
<p>inserts table_iterator specific data for a newly created row into a request </p>
<p> Definition at line 242 of file table_iterator.c. </p>
<p> References build_oid_noalloc(), netsnmp_table_request_info_s::indexes, netsnmp_create_data_list(), netsnmp_extract_table_info(), netsnmp_request_add_list_data(), netsnmp_request_info_s::next, NULL, netsnmp_request_info_s::prev, snmp_oid_compare(), and TABLE_ITERATOR_NAME.</p>
<h3>int netsnmp_register_table_iterator (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_iterator_info</code> * iinfo)</h3>
<p>Creates and registers a table iterator helper handler calling netsnmp_create_handler with a handler name set to TABLE_ITERATOR_NAME and access method, netsnmp_table_iterator_helper_handler. </p>
<p> If NOT_SERIALIZED is not defined the function injects the serialize handler into the calling chain prior to calling netsnmp_register_table. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>reginfo</i> is a pointer to a netsnmp_handler_registration struct<br />
 <i>iinfo</i> is a pointer to a netsnmp_iterator_info struct</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>MIB_REGISTERED_OK is returned if the registration was a success. Failures are MIB_REGISTRATION_FAILED, MIB_DUPLICATE_REGISTRATION. If iinfo is NULL, SNMPERR_GENERR is returned.</dl>
<p> Definition at line 205 of file table_iterator.c. </p>
<p> References HANDLER_CAN_STASH, netsnmp_table_registration_info_s::indexes, netsnmp_iterator_info_s::indexes, netsnmp_handler_registration_s::modes, netsnmp_get_table_iterator_handler(), netsnmp_inject_handler(), netsnmp_register_table(), snmp_clone_varbind(), and netsnmp_iterator_info_s::table_reginfo.</p>
