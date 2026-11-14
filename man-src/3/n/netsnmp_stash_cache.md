---
title: "netsnmp_stash_cache(3)"
name: "netsnmp_stash_cache"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_stash_cache/"
description: "stash_cache – Automatically caches data for certain handlers."
---

<p>stash_cache &#8211; Automatically caches data for certain handlers.</p>
<h3>Functions</h3>
<p><code>netsnmp_stash_cache_info</code> * <code>netsnmp_get_new_stash_cache</code> (void) </p>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_timed_bare_stash_cache_handler</code> (int timeout, oid *rootoid, size_t rootoid_len)<br />
 <i>returns a stash_cache handler that can be injected into a given handler chain (with the specified timeout and root OID values), but *only* if that handler chain explicitly supports stash cache processing. </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_get_bare_stash_cache_handler</code> (void)<br />
 <i>returns a single stash_cache handler that can be injected into a given handler chain (with a fixed timeout), but *only* if that handler chain explicitly supports stash cache processing. </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_get_stash_cache_handler</code> (void)<br />
 <i>returns a stash_cache handler sub-chain that can be injected into a given (arbitrary) handler chain, using a fixed cache timeout. </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_get_timed_stash_cache_handler</code> (int timeout, oid *rootoid, size_t rootoid_len)<br />
 <i>returns a stash_cache handler sub-chain that can be injected into a given (arbitrary) handler chain, using a configurable cache timeout. </i><br />
 <code>netsnmp_oid_stash_node</code> ** <code>netsnmp_extract_stash_cache</code> (<code>netsnmp_agent_request_info</code> *reqinfo)<br />
 <i>extracts a pointer to the stash_cache info from the reqinfo structure. </i><br />
 int <code>netsnmp_stash_cache_helper</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>_netsnmp_stash_cache_load</code> (<code>netsnmp_cache</code> *cache, void *magic)<br />
 <i>updates a given cache depending on whether it needs to or not. </i><br />
 void <code>_netsnmp_stash_cache_free</code> (<code>netsnmp_cache</code> *cache, void *magic) </p>
<p> void <code>netsnmp_init_stash_cache_helper</code> (void)<br />
 <i>initializes the stash_cache helper which then registers a stash_cache handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Automatically caches data for certain handlers. </p>
<p> This handler caches data in an optimized way which may aleviate the need for the lower level handlers to perform as much optimization. Specifically, somewhere in the lower level handlers must be a handler that supports the MODE_GET_STASH operation. Note that the table_iterator helper supports this.</p>
<h2>Function Documentation</h2>
<h3>int _netsnmp_stash_cache_load (<code>netsnmp_cache</code> * cache, void * magic)</h3>
<p>updates a given cache depending on whether it needs to or not. </p>
<p> Definition at line 194 of file stash_cache.c. </p>
<p> References netsnmp_stash_cache_info_s::cache, netsnmp_cache_s::cache_hint, netsnmp_handler_args_s::handler, netsnmp_cache_s::magic, netsnmp_agent_request_info_s::mode, netsnmp_agent_add_list_data(), netsnmp_call_next_handler(), netsnmp_create_data_list(), netsnmp_get_new_stash_cache(), netsnmp_mib_handler_s::next, NULL, netsnmp_handler_args_s::reginfo, netsnmp_handler_args_s::reqinfo, and netsnmp_handler_args_s::requests. </p>
<p> Referenced by netsnmp_get_timed_bare_stash_cache_handler().</p>
<h3><code>netsnmp_oid_stash_node</code>** netsnmp_extract_stash_cache (<code>netsnmp_agent_request_info</code> * reqinfo)</h3>
<p>extracts a pointer to the stash_cache info from the reqinfo structure. </p>
<p> Definition at line 112 of file stash_cache.c. </p>
<p> References netsnmp_agent_get_list_data(). </p>
<p> Referenced by netsnmp_stash_to_next_helper(), and netsnmp_table_iterator_helper_handler().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_bare_stash_cache_handler (void)</h3>
<p>returns a single stash_cache handler that can be injected into a given handler chain (with a fixed timeout), but *only* if that handler chain explicitly supports stash cache processing. </p>
<p> Definition at line 78 of file stash_cache.c. </p>
<p> References netsnmp_get_timed_bare_stash_cache_handler(), and NULL. </p>
<p> Referenced by netsnmp_get_stash_cache_handler().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_stash_cache_handler (void)</h3>
<p>returns a stash_cache handler sub-chain that can be injected into a given (arbitrary) handler chain, using a fixed cache timeout. </p>
<p> Definition at line 87 of file stash_cache.c. </p>
<p> References netsnmp_get_bare_stash_cache_handler(), netsnmp_get_stash_to_next_handler(), and netsnmp_mib_handler_s::next. </p>
<p> Referenced by netsnmp_init_stash_cache_helper().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_timed_bare_stash_cache_handler (int timeout, oid * rootoid, size_t rootoid_len)</h3>
<p>returns a stash_cache handler that can be injected into a given handler chain (with the specified timeout and root OID values), but *only* if that handler chain explicitly supports stash cache processing. </p>
<p> Definition at line 44 of file stash_cache.c. </p>
<p> References _netsnmp_stash_cache_free(), _netsnmp_stash_cache_load(), netsnmp_mib_handler_s::myvoid, netsnmp_cache_create(), netsnmp_cache_handler_get(), netsnmp_create_handler(), netsnmp_handler_free(), netsnmp_stash_cache_helper(), netsnmp_mib_handler_s::next, and NULL. </p>
<p> Referenced by netsnmp_get_bare_stash_cache_handler(), and netsnmp_get_timed_stash_cache_handler().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_timed_stash_cache_handler (int timeout, oid * rootoid, size_t rootoid_len)</h3>
<p>returns a stash_cache handler sub-chain that can be injected into a given (arbitrary) handler chain, using a configurable cache timeout. </p>
<p> Definition at line 100 of file stash_cache.c. </p>
<p> References netsnmp_get_stash_to_next_handler(), netsnmp_get_timed_bare_stash_cache_handler(), and netsnmp_mib_handler_s::next.</p>
<h3>void netsnmp_init_stash_cache_helper (void)</h3>
<p>initializes the stash_cache helper which then registers a stash_cache handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 237 of file stash_cache.c. </p>
<p> References netsnmp_get_stash_cache_handler(), and netsnmp_register_handler_by_name(). </p>
<p> Referenced by netsnmp_init_helpers().</p>
