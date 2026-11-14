---
title: "netsnmp_handler(3)"
name: "netsnmp_handler"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_handler/"
description: "Net-SNMP Agent handler and extensibility API – The basic theory goes something like this: In the past, with the original mib module api (which derived from the original CMU SNMP code) the underlyin..."
---

<p>Net-SNMP Agent handler and extensibility API &#8211; The basic theory goes something like this: In the past, with the original mib module api (which derived from the original CMU SNMP code) the underlying mib modules were passed very little information (only the truly most basic information about a request).</p>
<h3>Modules</h3>
<p><code>utility_handlers</code><br />
 <i>Simplify request processing A group of handlers intended to simplify certain aspects of processing a request for a MIB object. </i><br />
 <code>leaf_handlers</code><br />
 <i>Process individual leaf objects A group of handlers to implement individual leaf objects and instances (both scalar objects, and individual objects and instances within a table). </i><br />
 <code>baby_steps</code><br />
 <i>Calls your handler in baby_steps for set processing. </i><br />
 <code>old_api</code><br />
 <i>Calls mib module code written in the old style of code. </i><br />
 <code>stash_cache</code><br />
 <i>Automatically caches data for certain handlers. </i><br />
 <code>table</code><br />
 <i>Helps you implement a table. </i></p>
<h3>Data Structures</h3>
<pre><code>struct netsnmp_mib_handler_s


the mib handler structure to be registered


struct netsnmp_handler_registration_s


Root registration info.


struct netsnmp_handler_args_s



struct netsnmp_delegated_cache_s



struct netsnmp_mib_handler_s


the mib handler structure to be registered


struct netsnmp_handler_registration_s


Root registration info.



Defines
#define MIB_HANDLER_AUTO_NEXT   0x00000001



#define MIB_HANDLER_AUTO_NEXT_OVERRIDE_ONCE   0x00000002



#define MIB_HANDLER_INSTANCE   0x00000004



#define MIB_HANDLER_CUSTOM4   0x10000000



#define MIB_HANDLER_CUSTOM3   0x20000000



#define MIB_HANDLER_CUSTOM2   0x40000000



#define MIB_HANDLER_CUSTOM1   0x80000000



#define HANDLER_CAN_GETANDGETNEXT   0x01



#define HANDLER_CAN_SET   0x02



#define HANDLER_CAN_GETBULK   0x04



#define HANDLER_CAN_NOT_CREATE   0x08



#define HANDLER_CAN_BABY_STEP   0x10



#define HANDLER_CAN_STASH   0x20



#define HANDLER_CAN_RONLY   (HANDLER_CAN_GETANDGETNEXT)



#define HANDLER_CAN_RWRITE   (HANDLER_CAN_GETANDGETNEXT | HANDLER_CAN_SET)



#define HANDLER_CAN_SET_ONLY   (HANDLER_CAN_SET | HANDLER_CAN_NOT_CREATE)



#define HANDLER_CAN_DEFAULT   (HANDLER_CAN_RONLY | HANDLER_CAN_NOT_CREATE)



#define REQUEST_IS_DELEGATED   1



#define REQUEST_IS_NOT_DELEGATED   0



Typedefs</code></pre>
<p> typedef <code>netsnmp_mib_handler_s</code> <code>netsnmp_mib_handler</code><br />
 <i>Typedefs the </i><code>netsnmp_mib_handler_s</code> struct into netsnmp_mib_handler.<br />
 typedef <code>netsnmp_handler_registration_s</code> <code>netsnmp_handler_registration</code><br />
 <i>Typedefs the </i><code>netsnmp_handler_registration_s</code> struct into netsnmp_handler_registration.<br />
 typedef int( <code>Netsnmp_Node_Handler</code> )(<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> typedef <code>netsnmp_handler_args_s</code> <code>netsnmp_handler_args</code> </p>
<p> typedef <code>netsnmp_delegated_cache_s</code> <code>netsnmp_delegated_cache</code></p>
<h3>Functions</h3>
<pre><code>netsnmp_mib_handler * netsnmp_create_handler (const char *name, Netsnmp_Node_Handler *handler_access_method)


creates a netsnmp_mib_handler structure given a name and a access method.


netsnmp_handler_registration * netsnmp_handler_registration_create (const char *name, netsnmp_mib_handler *handler, oid *reg_oid, size_t reg_oid_len, int modes)


creates a handler registration structure given a name, a access_method function, a registration location oid and the modes the handler supports.


netsnmp_handler_registration * netsnmp_create_handler_registration (const char *name, Netsnmp_Node_Handler *handler_access_method, oid *reg_oid, size_t reg_oid_len, int modes)



int netsnmp_register_handler (netsnmp_handler_registration *reginfo)


register a handler, as defined by the netsnmp_handler_registration pointer.


int netsnmp_unregister_handler (netsnmp_handler_registration *reginfo)


unregister a handler, as defined by the netsnmp_handler_registration pointer.


int netsnmp_register_handler_nocallback (netsnmp_handler_registration *reginfo)


register a handler, as defined by the netsnmp_handler_registration pointer.


int netsnmp_inject_handler_before (netsnmp_handler_registration *reginfo, netsnmp_mib_handler *handler, const char *before_what)


inject a new handler into the calling chain of the handlers definedy by the netsnmp_handler_registration pointer.


int netsnmp_inject_handler (netsnmp_handler_registration *reginfo, netsnmp_mib_handler *handler)


inject a new handler into the calling chain of the handlers definedy by the netsnmp_handler_registration pointer.


NETSNMP_INLINE int netsnmp_call_handler (netsnmp_mib_handler *next_handler, netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *requests)


calls a handler with with appropriate NULL checking of arguments, etc.


int netsnmp_call_handlers (netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *requests)



NETSNMP_INLINE int netsnmp_call_next_handler (netsnmp_mib_handler *current, netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *requests)


calls the next handler in the chain after the current one with with appropriate NULL checking, etc.


NETSNMP_INLINE int netsnmp_call_next_handler_one_request (netsnmp_mib_handler *current, netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *requests)


calls the next handler in the chain after the current one with with appropriate NULL checking, etc.


void netsnmp_handler_free (netsnmp_mib_handler *handler)


free's the resourceses associated with a given handler


netsnmp_mib_handler * netsnmp_handler_dup (netsnmp_mib_handler *handler)


dulpicates a handler and all subsequent handlers see also _clone_handler


void netsnmp_handler_registration_free (netsnmp_handler_registration *reginfo)


free the resources associated with a handler registration object


netsnmp_handler_registration * netsnmp_handler_registration_dup (netsnmp_handler_registration *reginfo)


duplicates the handler registration object


NETSNMP_INLINE netsnmp_delegated_cache * netsnmp_create_delegated_cache (netsnmp_mib_handler *handler, netsnmp_handler_registration *reginfo, netsnmp_agent_request_info *reqinfo, netsnmp_request_info *requests, void *localinfo)


creates a cache of information which can be saved for future reference.


NETSNMP_INLINE netsnmp_delegated_cache * netsnmp_handler_check_cache (netsnmp_delegated_cache *dcache)


check's a given cache and returns it if it is still valid (ie, the agent still considers it to be an outstanding request.


NETSNMP_INLINE void netsnmp_free_delegated_cache (netsnmp_delegated_cache *dcache)


frees a cache once you're finished using it


void netsnmp_handler_mark_requests_as_delegated (netsnmp_request_info *requests, int isdelegated)


marks a list of requests as delegated (or not if isdelegaded = 0)


NETSNMP_INLINE void netsnmp_request_add_list_data (netsnmp_request_info *request, netsnmp_data_list *node)


add data to a request that can be extracted later by submodules


NETSNMP_INLINE int netsnmp_request_remove_list_data (netsnmp_request_info *request, const char *name)


remove data from a request


NETSNMP_INLINE void * netsnmp_request_get_list_data (netsnmp_request_info *request, const char *name)


extract data from a request that was added previously by a parent module


NETSNMP_INLINE void netsnmp_free_request_data_set (netsnmp_request_info *request)


Free the extra data stored in a request.


NETSNMP_INLINE void netsnmp_free_request_data_sets (netsnmp_request_info *request)


Free the extra data stored in a bunch of requests (all data in the chain).


netsnmp_mib_handler * netsnmp_find_handler_by_name (netsnmp_handler_registration *reginfo, const char *name)


Returns a handler from a chain based on the name.


void * netsnmp_find_handler_data_by_name (netsnmp_handler_registration *reginfo, const char *name)


Returns a handler's void * pointer from a chain based on the name.


void handler_free_callback (void *free)



void netsnmp_register_handler_by_name (const char *name, netsnmp_mib_handler *handler)


registers a given handler by name so that it can be found easily later.


void netsnmp_clear_handler_list (void)


clears the entire handler-registration list


void netsnmp_inject_handler_into_subtree (netsnmp_subtree *tp, const char *name, netsnmp_mib_handler *handler, const char *before_what)



void parse_injectHandler_conf (const char *token, char *cptr)



void netsnmp_init_handler_conf (void)



void * netsnmp_handler_get_parent_data (netsnmp_request_info *, const char *)</code></pre>
<h2>Detailed Description</h2>
<p>The basic theory goes something like this: In the past, with the original mib module api (which derived from the original CMU SNMP code) the underlying mib modules were passed very little information (only the truly most basic information about a request). </p>
<p> This worked well at the time but in todays world of subagents, device instrumentation, low resource consumption, etc, it just isn&#8217;t flexible enough. &#8216;handlers&#8217; are here to fix all that. </p>
<p> With the rewrite of the agent internals for the net-snmp 5.0 release, we introduce a modular calling scheme that allows agent modules to be written in a very flexible manner, and more importantly allows reuse of code in a decent way (and without the memory and speed overheads of OO languages like C++). </p>
<p> Functionally, the notion of what a handler does is the same as the older api: A handler is <code>created</code> and then <code>registered</code> with the main agent at a given OID in the OID tree and gets called any time a request is made that it should respond to. You probably should use one of the convenience helpers instead of doing anything else yourself though: </p>
<p> Most importantly, though, is that the handlers are built on the notion of modularity and reuse. Specifically, rather than do all the really hard work (like parsing table indexes out of an incoming oid request) in each module, the API is designed to make it easy to write &#8216;helper&#8217; handlers that merely process some aspect of the request before passing it along to the final handler that returns the real answer. Most people will want to make use of the <code>instance</code>, <code>table</code>, <code>table_iterator</code>, <code>table_data</code>, or <code>table_dataset</code> helpers to make their life easier. These &#8216;helpers&#8217; interpert important aspects of the request and pass them on to you. </p>
<p> For instance, the <code>table</code> helper is designed to hand you a list of extracted index values from an incoming request. THe <code>table_iterator</code> helper is built on top of the table helper, and is designed to help you iterate through data stored elsewhere (like in a kernel) that is not in OID lexographical order (ie, don&#8217;t write your own index/oid sorting routine, use this helper instead). The beauty of the <code>table_iterator helper</code>, as well as the <code>instance</code> helper is that they take care of the complex GETNEXT processing entirely for you and hand you everything you need to merely return the data as if it was a GET request. Much less code and hair pulling. I&#8217;ve pulled all my hair out to help you so that only one of us has to be bald.</p>
<h2>Typedef Documentation</h2>
<h3>struct <code>netsnmp_handler_registration_s</code> <code>netsnmp_handler_registration</code></h3>
<p>Typedefs the <code>netsnmp_handler_registration_s</code> struct into netsnmp_handler_registration.</p>
<h3>struct <code>netsnmp_mib_handler_s</code> <code>netsnmp_mib_handler</code></h3>
<p>Typedefs the <code>netsnmp_mib_handler_s</code> struct into netsnmp_mib_handler.</p>
<h2>Function Documentation</h2>
<h3>int netsnmp_call_handler (<code>netsnmp_mib_handler</code> * next_handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>calls a handler with with appropriate NULL checking of arguments, etc. </p>
<p> Definition at line 394 of file agent_handler.c. </p>
<p> References netsnmp_mib_handler_s::access_method, netsnmp_mib_handler_s::handler_name, MIB_HANDLER_AUTO_NEXT, MIB_HANDLER_AUTO_NEXT_OVERRIDE_ONCE, netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::next, NULL, and snmp_log(). </p>
<p> Referenced by netsnmp_call_handlers(), netsnmp_call_next_handler(), netsnmp_call_next_handler_one_request(), netsnmp_mode_end_call_helper(), and netsnmp_multiplexer_helper_handler().</p>
<h3>int netsnmp_call_next_handler (<code>netsnmp_mib_handler</code> * current, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>calls the next handler in the chain after the current one with with appropriate NULL checking, etc. </p>
<p> Definition at line 524 of file agent_handler.c. </p>
<p> References netsnmp_call_handler(), netsnmp_mib_handler_s::next, NULL, and snmp_log(). </p>
<p> Referenced by _netsnmp_stash_cache_load(), netsnmp_bulk_to_next_helper(), netsnmp_debug_helper(), netsnmp_instance_counter32_handler(), netsnmp_instance_helper_handler(), netsnmp_instance_int_handler(), netsnmp_instance_long_handler(), netsnmp_instance_num_file_handler(), netsnmp_instance_uint_handler(), netsnmp_instance_ulong_handler(), netsnmp_mode_end_call_helper(), netsnmp_row_merge_helper_handler(), netsnmp_scalar_group_helper_handler(), netsnmp_scalar_helper_handler(), netsnmp_serialize_helper_handler(), netsnmp_stash_to_next_helper(), and table_helper_handler().</p>
<h3>int netsnmp_call_next_handler_one_request (<code>netsnmp_mib_handler</code> * current, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>calls the next handler in the chain after the current one with with appropriate NULL checking, etc. </p>
<p> Definition at line 546 of file agent_handler.c. </p>
<p> References netsnmp_call_handler(), netsnmp_mib_handler_s::next, netsnmp_request_info_s::next, NULL, and snmp_log().</p>
<h3>void netsnmp_clear_handler_list (void)</h3>
<p>clears the entire handler-registration list </p>
<p> Definition at line 905 of file agent_handler.c. </p>
<p> References netsnmp_free_all_list_data(), and NULL. </p>
<p> Referenced by shutdown_agent().</p>
<h3>NETSNMP_INLINE <code>netsnmp_delegated_cache</code> * netsnmp_create_delegated_cache (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests, void * localinfo)</h3>
<p>creates a cache of information which can be saved for future reference. </p>
<p> Use <code>netsnmp_handler_check_cache()</code> later to make sure it&#8217;s still valid before referencing it in the future. </p>
<p> <code>Examples: </code> <code>delayed_instance.c</code>. </p>
<p> Definition at line 696 of file agent_handler.c. </p>
<p> References netsnmp_agent_request_info_s::asp, netsnmp_delegated_cache_s::handler, netsnmp_delegated_cache_s::localinfo, netsnmp_agent_session_s::pdu, netsnmp_delegated_cache_s::reginfo, netsnmp_delegated_cache_s::reqinfo, netsnmp_delegated_cache_s::requests, SNMP_MALLOC_TYPEDEF, netsnmp_delegated_cache_s::transaction_id, and snmp_pdu::transid.</p>
<h3><code>netsnmp_mib_handler</code> * netsnmp_create_handler (const char * name, <code>Netsnmp_Node_Handler</code> * handler_access_method)</h3>
<p>creates a netsnmp_mib_handler structure given a name and a access method. </p>
<p> The returned handler should then be <code>registered.</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> is the handler name and is copied then assigned to netsnmp_mib_handler-&gt;handler_name<br />
 <i>handler_access_method</i> is a function pointer used as the access method for this handler registration instance for whatever required needs.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a pointer to a populated netsnmp_mib_handler struct to be registered</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>netsnmp_create_handler_registration()</code> </p>
<p> <code>netsnmp_register_handler()</code></dl>
<p> Definition at line 105 of file agent_handler.c. </p>
<p> References netsnmp_mib_handler_s::access_method, netsnmp_mib_handler_s::handler_name, NULL, SNMP_FREE, and SNMP_MALLOC_TYPEDEF. </p>
<p> Referenced by get_old_api_handler(), netsnmp_baby_steps_access_multiplexer_get(), netsnmp_baby_steps_handler_get(), netsnmp_cache_handler_get(), netsnmp_container_table_handler_get(), netsnmp_create_handler_registration(), netsnmp_get_bulk_to_next_handler(), netsnmp_get_debug_handler(), netsnmp_get_instance_handler(), netsnmp_get_mode_end_call_handler(), netsnmp_get_multiplexer_handler(), netsnmp_get_read_only_handler(), netsnmp_get_row_merge_handler(), netsnmp_get_scalar_group_handler(), netsnmp_get_scalar_handler(), netsnmp_get_serialize_handler(), netsnmp_get_stash_to_next_handler(), netsnmp_get_table_data_handler(), netsnmp_get_table_data_set_handler(), netsnmp_get_table_handler(), netsnmp_get_table_iterator_handler(), netsnmp_get_tdata_handler(), netsnmp_get_timed_bare_stash_cache_handler(), netsnmp_get_watched_spinlock_handler(), netsnmp_get_watched_timestamp_handler(), netsnmp_get_watcher_handler(), netsnmp_sparse_table_handler_get(), netsnmp_sparse_table_register(), netsnmp_table_array_register(), and netsnmp_table_row_handler_get().</p>
<h3><code>netsnmp_mib_handler</code> * netsnmp_find_handler_by_name (<code>netsnmp_handler_registration</code> * reginfo, const char * name)</h3>
<p>Returns a handler from a chain based on the name. </p>
<p> Definition at line 838 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::handler, netsnmp_mib_handler_s::handler_name, netsnmp_mib_handler_s::next, and NULL. </p>
<p> Referenced by netsnmp_find_handler_data_by_name().</p>
<h3>void * netsnmp_find_handler_data_by_name (<code>netsnmp_handler_registration</code> * reginfo, const char * name)</h3>
<p>Returns a handler&#8217;s void * pointer from a chain based on the name. </p>
<p> This probably shouldn&#8217;t be used by the general public as the void * data may change as a handler evolves. Handlers should really advertise some function for you to use instead. </p>
<p> Definition at line 855 of file agent_handler.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_find_handler_by_name(), and NULL. </p>
<p> Referenced by netsnmp_find_table_registration_info().</p>
<h3>NETSNMP_INLINE void netsnmp_free_delegated_cache (<code>netsnmp_delegated_cache</code> * dcache)</h3>
<p>frees a cache once you&#8217;re finished using it </p>
<p> <code>Examples: </code> <code>delayed_instance.c</code>. </p>
<p> Definition at line 734 of file agent_handler.c. </p>
<p> References SNMP_FREE.</p>
<h3>NETSNMP_INLINE void netsnmp_free_request_data_set (<code>netsnmp_request_info</code> * request)</h3>
<p>Free the extra data stored in a request. </p>
<p> Definition at line 820 of file agent_handler.c. </p>
<p> References netsnmp_free_list_data(), and netsnmp_request_info_s::parent_data.</p>
<h3>NETSNMP_INLINE void netsnmp_free_request_data_sets (<code>netsnmp_request_info</code> * request)</h3>
<p>Free the extra data stored in a bunch of requests (all data in the chain). </p>
<p> Definition at line 828 of file agent_handler.c. </p>
<p> References netsnmp_free_all_list_data(), NULL, and netsnmp_request_info_s::parent_data. </p>
<p> Referenced by free_agent_snmp_session(), get_set_cache(), netsnmp_add_varbind_to_cache(), and netsnmp_delete_request_infos().</p>
<h3>NETSNMP_INLINE <code>netsnmp_delegated_cache</code> * netsnmp_handler_check_cache (<code>netsnmp_delegated_cache</code> * dcache)</h3>
<p>check&#8217;s a given cache and returns it if it is still valid (ie, the agent still considers it to be an outstanding request. </p>
<p> Returns NULL if it&#8217;s no longer valid. </p>
<p> <code>Examples: </code> <code>delayed_instance.c</code>. </p>
<p> Definition at line 720 of file agent_handler.c. </p>
<p> References netsnmp_check_transaction_id(), NULL, and netsnmp_delegated_cache_s::transaction_id.</p>
<h3><code>netsnmp_mib_handler</code> * netsnmp_handler_dup (<code>netsnmp_mib_handler</code> * handler)</h3>
<p>dulpicates a handler and all subsequent handlers see also _clone_handler </p>
<p> Definition at line 591 of file agent_handler.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_handler_free(), netsnmp_mib_handler_s::next, NULL, and netsnmp_mib_handler_s::prev. </p>
<p> Referenced by netsnmp_handler_registration_dup().</p>
<h3>void netsnmp_handler_free (<code>netsnmp_mib_handler</code> * handler)</h3>
<p>free&#8217;s the resourceses associated with a given handler </p>
<p> make sure we aren&#8217;t pointing to ourselves. </p>
<p> XXX : segv here at shutdown if SHUTDOWN_AGENT_CLEANLY defined. About 30 functions down the stack, starting in <code>clear_context()</code> -&gt; <code>clear_subtree()</code> </p>
<p> Definition at line 569 of file agent_handler.c. </p>
<p> References netsnmp_mib_handler_s::handler_name, netsnmp_mib_handler_s::next, NULL, and SNMP_FREE. </p>
<p> Referenced by handler_free_callback(), netsnmp_baby_steps_handler_get(), netsnmp_get_scalar_group_handler(), netsnmp_get_timed_bare_stash_cache_handler(), netsnmp_handler_dup(), and netsnmp_handler_registration_free().</p>
<h3>void netsnmp_handler_mark_requests_as_delegated (<code>netsnmp_request_info</code> * requests, int isdelegated)</h3>
<p>marks a list of requests as delegated (or not if isdelegaded = 0) </p>
<p> Definition at line 748 of file agent_handler.c. </p>
<p> References netsnmp_request_info_s::delegated, and netsnmp_request_info_s::next.</p>
<h3><code>netsnmp_handler_registration</code> * netsnmp_handler_registration_create (const char * name, <code>netsnmp_mib_handler</code> * handler, oid * reg_oid, size_t reg_oid_len, int modes)</h3>
<p>creates a handler registration structure given a name, a access_method function, a registration location oid and the modes the handler supports. </p>
<p> If modes == 0, then modes will automatically be set to the default value of only HANDLER_CAN_DEFAULT, which is by default read-only GET and GETNEXT requests. A hander which supports sets but not row creation should set us a mode of HANDLER_CAN_SET_ONLY. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This ends up calling netsnmp_create_handler(name, handler_access_method)</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> is the handler name and is copied then assigned to netsnmp_handler_registration-&gt;handlerName.<br />
 <i>handler</i> is a function pointer used as the access method for this handler registration instance for whatever required needs.<br />
 <i>reg_oid</i> is the registration location oid.<br />
 <i>reg_oid_len</i> is the length of reg_oid, can use the macro, OID_LENGTH<br />
 <i>modes</i> is used to configure read/write access. If modes == 0, then modes will automatically be set to the default value of only HANDLER_CAN_DEFAULT, which is by default read-only GET and GETNEXT requests. The other two mode options are read only, HANDLER_CAN_RONLY, and read/write, HANDLER_CAN_RWRITE.</dl>
<dl>
<dt>*</p>
<dd>HANDLER_CAN_GETANDGETNEXT</p>
<dt>*</p>
<dd>HANDLER_CAN_SET</p>
<dt>*</p>
<dd>HANDLER_CAN_GETBULK</dl>
<dl>
<dt>*</p>
<dd>HANDLER_CAN_RONLY (HANDLER_CAN_GETANDGETNEXT)</p>
<dt>*</p>
<dd>HANDLER_CAN_RWRITE (HANDLER_CAN_GETANDGETNEXT | HANDLER_CAN_SET)</p>
<dt>*</p>
<dd>HANDLER_CAN_DEFAULT HANDLER_CAN_RONLY</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns a pointer to a netsnmp_handler_registration struct. NULL is returned only when memory could not be allocated for the netsnmp_handler_registration struct.</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>netsnmp_create_handler()</code> </p>
<p> <code>netsnmp_register_handler()</code></dl>
<p> Definition at line 163 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::handler, HANDLER_CAN_DEFAULT, netsnmp_handler_registration_s::handlerName, memdup(), netsnmp_handler_registration_s::modes, NULL, netsnmp_handler_registration_s::priority, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, and SNMP_MALLOC_TYPEDEF. </p>
<p> Referenced by netsnmp_create_handler_registration().</p>
<h3><code>netsnmp_handler_registration</code> * netsnmp_handler_registration_dup (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>duplicates the handler registration object </p>
<p> Definition at line 634 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::contextName, netsnmp_handler_registration_s::handler, netsnmp_handler_registration_s::handlerName, memdup(), netsnmp_handler_registration_s::modes, netsnmp_handler_dup(), netsnmp_handler_registration_free(), NULL, netsnmp_handler_registration_s::priority, netsnmp_handler_registration_s::range_subid, netsnmp_handler_registration_s::range_ubound, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, and netsnmp_handler_registration_s::timeout. </p>
<p> Referenced by netsnmp_subtree_deepcopy().</p>
<h3>void netsnmp_handler_registration_free (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>free the resources associated with a handler registration object </p>
<p> Definition at line 620 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::contextName, netsnmp_handler_registration_s::handler, netsnmp_handler_registration_s::handlerName, netsnmp_handler_free(), NULL, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, and SNMP_FREE. </p>
<p> Referenced by netsnmp_handler_registration_dup(), netsnmp_register_mib(), netsnmp_register_mib_table_row(), netsnmp_subtree_free(), and unregister_mibs_by_session().</p>
<h3>int netsnmp_inject_handler (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_mib_handler</code> * handler)</h3>
<p>inject a new handler into the calling chain of the handlers definedy by the netsnmp_handler_registration pointer. </p>
<p> The new handler is injected at the top of the list and hence will be the new handler to be called first. </p>
<p> Definition at line 386 of file agent_handler.c. </p>
<p> References netsnmp_inject_handler_before(), and NULL. </p>
<p> Referenced by netsnmp_cache_handler_register(), netsnmp_container_table_register(), netsnmp_register_cache_handler(), netsnmp_register_handler(), netsnmp_register_instance(), netsnmp_register_read_only_instance(), netsnmp_register_read_only_scalar(), netsnmp_register_read_only_table_data(), netsnmp_register_row_merge(), netsnmp_register_scalar(), netsnmp_register_scalar_group(), netsnmp_register_serialize(), netsnmp_register_table(), netsnmp_register_table_data(), netsnmp_register_table_data_set(), netsnmp_register_table_iterator(), netsnmp_register_watched_instance(), netsnmp_register_watched_scalar(), netsnmp_register_watched_spinlock(), netsnmp_sparse_table_register(), netsnmp_table_array_register(), netsnmp_table_row_register(), netsnmp_tdata_register(), and netsnmp_watched_timestamp_register().</p>
<h3>int netsnmp_inject_handler_before (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_mib_handler</code> * handler, const char * before_what)</h3>
<p>inject a new handler into the calling chain of the handlers definedy by the netsnmp_handler_registration pointer. </p>
<p> The new handler is injected after the before_what handler, or if NULL at the top of the list and hence will be the new handler to be called first. </p>
<p> Definition at line 329 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::handler, netsnmp_mib_handler_s::handler_name, netsnmp_mib_handler_s::next, NULL, netsnmp_mib_handler_s::prev, and snmp_log(). </p>
<p> Referenced by netsnmp_inject_handler(), and netsnmp_inject_handler_into_subtree().</p>
<h3>int netsnmp_register_handler (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>register a handler, as defined by the netsnmp_handler_registration pointer. </p>
<p> Definition at line 202 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::contextName, netsnmp_mib_handler_s::flags, netsnmp_handler_registration_s::handler, HANDLER_CAN_DEFAULT, HANDLER_CAN_GETBULK, netsnmp_mib_handler_s::handler_name, netsnmp_handler_registration_s::handlerName, MIB_HANDLER_INSTANCE, netsnmp_handler_registration_s::modes, netsnmp_get_bulk_to_next_handler(), netsnmp_inject_handler(), netsnmp_register_mib(), netsnmp_mib_handler_s::next, NULL, netsnmp_handler_registration_s::priority, netsnmp_handler_registration_s::range_subid, netsnmp_handler_registration_s::range_ubound, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_log(), and netsnmp_handler_registration_s::timeout. </p>
<p> Referenced by netsnmp_cache_handler_register(), netsnmp_register_cache_handler(), netsnmp_register_old_api(), netsnmp_register_row_merge(), netsnmp_register_serialize(), netsnmp_register_table(), netsnmp_sparse_table_register(), and netsnmp_table_row_register().</p>
<h3>void netsnmp_register_handler_by_name (const char * name, <code>netsnmp_mib_handler</code> * handler)</h3>
<p>registers a given handler by name so that it can be found easily later. </p>
<p> Definition at line 893 of file agent_handler.c. </p>
<p> References handler_free_callback(), netsnmp_add_list_data(), and netsnmp_create_data_list(). </p>
<p> Referenced by netsnmp_baby_steps_handler_init(), netsnmp_init_bulk_to_next_helper(), netsnmp_init_debug_helper(), netsnmp_init_read_only_helper(), netsnmp_init_row_merge(), netsnmp_init_serialize(), and netsnmp_init_stash_cache_helper().</p>
<h3>int netsnmp_register_handler_nocallback (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>register a handler, as defined by the netsnmp_handler_registration pointer. </p>
<p> Definition at line 277 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::contextName, netsnmp_handler_registration_s::handler, HANDLER_CAN_DEFAULT, netsnmp_mib_handler_s::handler_name, netsnmp_handler_registration_s::modes, netsnmp_register_mib(), netsnmp_mib_handler_s::next, NULL, netsnmp_handler_registration_s::priority, netsnmp_handler_registration_s::range_subid, netsnmp_handler_registration_s::range_ubound, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_log(), and netsnmp_handler_registration_s::timeout. </p>
<p> Referenced by netsnmp_register_mib_table_row().</p>
<h3>NETSNMP_INLINE void netsnmp_request_add_list_data (<code>netsnmp_request_info</code> * request, <code>netsnmp_data_list</code> * node)</h3>
<p>add data to a request that can be extracted later by submodules </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>request</i> the netsnmp request info structure<br />
 <i>node</i> this is the data to be added to the linked list request-&gt;parent_data</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>void</dl>
<p> <code>Examples: </code> <code>delayed_instance.c</code>. </p>
<p> Definition at line 768 of file agent_handler.c. </p>
<p> References netsnmp_add_list_data(), and netsnmp_request_info_s::parent_data. </p>
<p> Referenced by _netsnmp_tdata_helper_handler(), netsnmp_container_table_row_insert(), netsnmp_insert_iterator_context(), netsnmp_insert_table_row(), netsnmp_instance_int_handler(), netsnmp_instance_long_handler(), netsnmp_instance_num_file_handler(), netsnmp_instance_uint_handler(), netsnmp_instance_ulong_handler(), netsnmp_table_data_helper_handler(), netsnmp_table_data_set_helper_handler(), netsnmp_table_iterator_helper_handler(), netsnmp_watcher_helper_handler(), and table_helper_handler().</p>
<h3>NETSNMP_INLINE void * netsnmp_request_get_list_data (<code>netsnmp_request_info</code> * request, const char * name)</h3>
<p>extract data from a request that was added previously by a parent module </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>request</i> the netsnmp request info function<br />
 <i>name</i> used to compare against the request-&gt;parent_data-&gt;name value, if a match is found request-&gt;parent_data-&gt;data is returned</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a void pointer(request-&gt;parent_data-&gt;data), otherwise NULL is returned if request is NULL or request-&gt;parent_data is NULL or request-&gt;parent_data object is not found.</dl>
<p> <code>Examples: </code> <code>delayed_instance.c</code>. </p>
<p> Definition at line 810 of file agent_handler.c. </p>
<p> References netsnmp_get_list_data(), NULL, and netsnmp_request_info_s::parent_data. </p>
<p> Referenced by netsnmp_container_table_container_extract(), netsnmp_container_table_extract_context(), netsnmp_container_table_row_extract(), netsnmp_extract_array_context(), netsnmp_extract_iterator_context(), netsnmp_extract_table(), netsnmp_extract_table_data_set(), netsnmp_extract_table_info(), netsnmp_extract_table_row(), netsnmp_instance_int_handler(), netsnmp_instance_long_handler(), netsnmp_instance_num_file_handler(), netsnmp_instance_uint_handler(), netsnmp_instance_ulong_handler(), netsnmp_table_iterator_helper_handler(), netsnmp_table_row_extract(), netsnmp_tdata_extract_container(), netsnmp_tdata_extract_table(), and netsnmp_watcher_helper_handler().</p>
<h3>NETSNMP_INLINE int netsnmp_request_remove_list_data (<code>netsnmp_request_info</code> * request, const char * name)</h3>
<p>remove data from a request </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>request</i> the netsnmp request info structure<br />
 <i>name</i> this is the name of the previously added data</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on successful find-and-delete, 1 otherwise.</dl>
<p> Definition at line 789 of file agent_handler.c. </p>
<p> References netsnmp_remove_list_node(), NULL, and netsnmp_request_info_s::parent_data. </p>
<p> Referenced by netsnmp_table_data_set_helper_handler().</p>
<h3>int netsnmp_unregister_handler (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>unregister a handler, as defined by the netsnmp_handler_registration pointer. </p>
<p> Definition at line 267 of file agent_handler.c. </p>
<p> References netsnmp_handler_registration_s::contextName, netsnmp_handler_registration_s::priority, netsnmp_handler_registration_s::range_subid, netsnmp_handler_registration_s::range_ubound, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, and unregister_mib_context().</p>
