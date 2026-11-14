---
title: "netsnmp_cache_handler(3)"
name: "netsnmp_cache_handler"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_cache_handler/"
description: "cache_handler – Maintains a cache of data for use by lower level handlers."
---

<p>cache_handler &#8211; Maintains a cache of data for use by lower level handlers.</p>
<h3>Functions</h3>
<p><code>netsnmp_cache</code> * <code>netsnmp_cache_get_head</code> (void)<br />
 <i>get cache head </i><br />
 <code>netsnmp_cache</code> * <code>netsnmp_cache_find_by_oid</code> (oid *rootoid, int rootoid_len)<br />
 <i>find existing cache </i><br />
 <code>netsnmp_cache</code> * <code>netsnmp_cache_create</code> (int timeout, NetsnmpCacheLoad *load_hook, NetsnmpCacheFree *free_hook, oid *rootoid, int rootoid_len)<br />
 <i>returns a cache </i><br />
 unsigned int <code>netsnmp_cache_timer_start</code> (<code>netsnmp_cache</code> *cache)<br />
 <i>starts the recurring cache_load callback </i><br />
 void <code>netsnmp_cache_timer_stop</code> (<code>netsnmp_cache</code> *cache)<br />
 <i>stops the recurring cache_load callback </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_cache_handler_get</code> (<code>netsnmp_cache</code> *cache)<br />
 <i>returns a cache handler that can be injected into a given handler chain. </i><br />
 <code>netsnmp_mib_handler</code> * <code>netsnmp_get_cache_handler</code> (int timeout, NetsnmpCacheLoad *load_hook, NetsnmpCacheFree *free_hook, oid *rootoid, int rootoid_len)<br />
 <i>returns a cache handler that can be injected into a given handler chain. </i><br />
 int <code>netsnmp_cache_handler_register</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_cache</code> *cache)<br />
 <i>functionally the same as calling </i><code>netsnmp_register_handler()</code> but also injects a cache handler at the same time for you.<br />
 int <code>netsnmp_register_cache_handler</code> (<code>netsnmp_handler_registration</code> *reginfo, int timeout, NetsnmpCacheLoad *load_hook, NetsnmpCacheFree *free_hook)<br />
 <i>functionally the same as calling </i><code>netsnmp_register_handler()</code> but also injects a cache handler at the same time for you.<br />
 NETSNMP_STATIC_INLINE char * <code>_build_cache_name</code> (const char *name) </p>
<p> void <code>netsnmp_cache_reqinfo_insert</code> (<code>netsnmp_cache</code> *cache, <code>netsnmp_agent_request_info</code> *reqinfo, const char *name)<br />
 <i>Insert the cache information for a given request (PDU). </i><br />
 <code>netsnmp_cache</code> * <code>netsnmp_cache_reqinfo_extract</code> (<code>netsnmp_agent_request_info</code> *reqinfo, const char *name)<br />
 <i>Extract the cache information for a given request (PDU). </i><br />
 <code>netsnmp_cache</code> * <code>netsnmp_extract_cache_info</code> (<code>netsnmp_agent_request_info</code> *reqinfo)<br />
 <i>Extract the cache information for a given request (PDU). </i><br />
 int <code>netsnmp_cache_check_expired</code> (<code>netsnmp_cache</code> *cache)<br />
 <i>Check if the cache timeout has passed. </i><br />
 int <code>netsnmp_cache_check_and_reload</code> (<code>netsnmp_cache</code> *cache)<br />
 <i>Reload the cache if required. </i><br />
 int <code>netsnmp_cache_is_valid</code> (<code>netsnmp_agent_request_info</code> *reqinfo, const char *name)<br />
 <i>Is the cache valid for a given request? </i><br />
 int <code>netsnmp_is_cache_valid</code> (<code>netsnmp_agent_request_info</code> *reqinfo)<br />
 <i>for backwards compat </i><br />
 int <code>netsnmp_cache_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)<br />
 <i>Implements the cache handler. </i><br />
 void <code>release_cached_resources</code> (unsigned int regNo, void *clientargs)<br />
 <i>run regularly to automatically release cached resources. </i></p>
<h2>Detailed Description</h2>
<p>Maintains a cache of data for use by lower level handlers. </p>
<p> This helper checks to see whether the data has been loaded &#8216;recently&#8217; (according to the timeout for that particular cache) and calls the registered &#8216;load_cache&#8217; routine if necessary. The lower handlers can then work with this local cached data. </p>
<p> A timeout value of -1 will cause <code>netsnmp_cache_check_expired()</code> to always return true, and thus the cache will be reloaded for every request. </p>
<p> To minimze resource use by the agent, a periodic callback checks for expired caches, and will call the free_cache function for any expired cache. </p>
<p> The load_cache route should return a negative number if the cache was not successfully loaded. 0 or any positive number indicates successs. </p>
<p> Several flags can be set to affect the operations on the cache. </p>
<p> If NETSNMP_CACHE_DONT_INVALIDATE_ON_SET is set, the free_cache method will not be called after a set request has processed. It is assumed that the lower mib handler using the cache has maintained cache consistency. </p>
<p> If NETSNMP_CACHE_DONT_FREE_BEFORE_LOAD is set, the free_cache method will not be called before the load_cache method is called. It is assumed that the load_cache routine will properly deal with being called with a valid cache. </p>
<p> If NETSNMP_CACHE_DONT_FREE_EXPIRED is set, the free_cache method will not be called with the cache expires. The expired flag will be set, but the valid flag will not be cleared. It is assumed that the load_cache routine will properly deal with being called with a valid cache. </p>
<p> If NETSNMP_CACHE_PRELOAD is set when a the cache handler is created, the cache load routine will be called immediately. </p>
<p> If NETSNMP_CACHE_DONT_AUTO_RELEASE is set, the periodic callback that checks for expired caches will skip the cache. The cache will only be checked for expiration when a request triggers the cache handler. This is useful if the cache has it&#8217;s own periodic callback to keep the cache fresh. </p>
<p> If NETSNMP_CACHE_AUTO_RELOAD is set, a timer will be set up to reload the cache when it expires. This is useful for keeping the cache fresh, even in the absence of incoming snmp requests. </p>
<p> Here are some suggestions for some common situations. </p>
<p> Cached File: If your table is based on a file that may periodically change, you can test the modification date to see if the file has changed since the last cache load. To get the cache helper to call the load function for every request, set the timeout to -1, which will cause the cache to always report that it is expired. This means that you will want to prevent the agent from flushing the cache when it has expired, and you will have to flush it manually if you detect that the file has changed. To accomplish this, set the following flags: </p>
<p> NETSNMP_CACHE_DONT_FREE_EXPIRED NETSNMP_CACHE_DONT_AUTO_RELEASE </p>
<p> Constant (periodic) reload: If you want the cache kept up to date regularly, even if no requests for the table are received, you can have your cache load routine called periodically. This is very useful if you need to monitor the data for changes (eg a <i>LastChanged</i> object). You will need to prevent the agent from flushing the cache when it expires. Set the cache timeout to the frequency, in seconds, that you wish to reload your cache, and set the following flags: </p>
<p> NETSNMP_CACHE_DONT_FREE_EXPIRED NETSNMP_CACHE_DONT_AUTO_RELEASE NETSNMP_CACHE_AUTO_RELOAD</p>
<h2>Function Documentation</h2>
<h3>int netsnmp_cache_check_and_reload (<code>netsnmp_cache</code> * cache)</h3>
<p>Reload the cache if required. </p>
<p> Definition at line 385 of file cache_handler.c. </p>
<p> References netsnmp_cache_check_expired(), and netsnmp_cache_s::valid. </p>
<p> Referenced by netsnmp_cache_helper_handler().</p>
<h3>int netsnmp_cache_check_expired (<code>netsnmp_cache</code> * cache)</h3>
<p>Check if the cache timeout has passed. </p>
<p> Sets and return the expired flag. </p>
<p> Definition at line 370 of file cache_handler.c. </p>
<p> References atime_ready(), netsnmp_cache_s::expired, NULL, netsnmp_cache_s::timeout, netsnmp_cache_s::timestamp, and netsnmp_cache_s::valid. </p>
<p> Referenced by netsnmp_cache_check_and_reload(), and release_cached_resources().</p>
<h3><code>netsnmp_cache</code>* netsnmp_cache_create (int timeout, NetsnmpCacheLoad * load_hook, NetsnmpCacheFree * free_hook, oid * rootoid, int rootoid_len)</h3>
<p>returns a cache </p>
<p> Definition at line 136 of file cache_handler.c. </p>
<p> References netsnmp_cache_s::enabled, netsnmp_cache_s::free_cache, netsnmp_cache_s::load_cache, netsnmp_ds_get_int(), netsnmp_cache_s::next, NULL, netsnmp_cache_s::prev, netsnmp_cache_s::rootoid, netsnmp_cache_s::rootoid_len, snmp_duplicate_objid(), snmp_log(), SNMP_MALLOC_TYPEDEF, and netsnmp_cache_s::timeout. </p>
<p> Referenced by netsnmp_get_cache_handler(), and netsnmp_get_timed_bare_stash_cache_handler().</p>
<h3><code>netsnmp_cache</code>* netsnmp_cache_find_by_oid (oid * rootoid, int rootoid_len)</h3>
<p>find existing cache </p>
<p> Definition at line 120 of file cache_handler.c. </p>
<p> References netsnmp_oid_equals(), netsnmp_cache_s::next, NULL, netsnmp_cache_s::rootoid, and netsnmp_cache_s::rootoid_len.</p>
<h3><code>netsnmp_cache</code>* netsnmp_cache_get_head (void)</h3>
<p>get cache head </p>
<p> Definition at line 112 of file cache_handler.c.</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_cache_handler_get (<code>netsnmp_cache</code> * cache)</h3>
<p>returns a cache handler that can be injected into a given handler chain. </p>
<p> Definition at line 247 of file cache_handler.c. </p>
<p> References netsnmp_mib_handler_s::flags, netsnmp_cache_s::flags, MIB_HANDLER_AUTO_NEXT, netsnmp_mib_handler_s::myvoid, netsnmp_cache_helper_handler(), netsnmp_cache_timer_start(), netsnmp_create_handler(), NULL, and netsnmp_cache_s::valid. </p>
<p> Referenced by netsnmp_cache_handler_register(), netsnmp_get_cache_handler(), and netsnmp_get_timed_bare_stash_cache_handler().</p>
<h3>int netsnmp_cache_handler_register (<code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_cache</code> * cache)</h3>
<p>functionally the same as calling <code>netsnmp_register_handler()</code> but also injects a cache handler at the same time for you. </p>
<p> Definition at line 295 of file cache_handler.c. </p>
<p> References netsnmp_cache_handler_get(), netsnmp_inject_handler(), netsnmp_register_handler(), and NULL.</p>
<h3>int netsnmp_cache_helper_handler (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>Implements the cache handler. </p>
<p> next handler called automatically &#8211; &#8216;AUTO_NEXT&#8217; </p>
<p> next handler called automatically &#8211; &#8216;AUTO_NEXT&#8217; </p>
<p> next handler called automatically &#8211; &#8216;AUTO_NEXT&#8217; </p>
<p> Definition at line 420 of file cache_handler.c. </p>
<p> References netsnmp_cache_s::cache_hint, netsnmp_cache_s::enabled, netsnmp_cache_s::flags, netsnmp_mib_handler_s::flags, netsnmp_cache_s::free_cache, netsnmp_handler_args_s::handler, netsnmp_handler_registration_s::handlerName, netsnmp_cache_s::load_cache, netsnmp_cache_s::magic, MIB_HANDLER_AUTO_NEXT, netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::myvoid, netsnmp_cache_check_and_reload(), netsnmp_cache_is_valid(), netsnmp_cache_reqinfo_insert(), netsnmp_ds_get_boolean(), netsnmp_request_set_error_all(), NULL, netsnmp_handler_args_s::reginfo, netsnmp_handler_args_s::reqinfo, netsnmp_handler_args_s::requests, netsnmp_handler_registration_s::rootoid, netsnmp_handler_registration_s::rootoid_len, snmp_log(), and netsnmp_cache_s::valid. </p>
<p> Referenced by netsnmp_cache_handler_get().</p>
<h3>int netsnmp_cache_is_valid (<code>netsnmp_agent_request_info</code> * reqinfo, const char * name)</h3>
<p>Is the cache valid for a given request? </p>
<p> Definition at line 402 of file cache_handler.c. </p>
<p> References netsnmp_cache_reqinfo_extract(), and netsnmp_cache_s::valid. </p>
<p> Referenced by netsnmp_cache_helper_handler(), and netsnmp_is_cache_valid().</p>
<h3><code>netsnmp_cache</code>* netsnmp_cache_reqinfo_extract (<code>netsnmp_agent_request_info</code> * reqinfo, const char * name)</h3>
<p>Extract the cache information for a given request (PDU). </p>
<p> Definition at line 350 of file cache_handler.c. </p>
<p> References _build_cache_name(), netsnmp_agent_get_list_data(), and SNMP_FREE. </p>
<p> Referenced by netsnmp_cache_is_valid(), netsnmp_extract_cache_info(), and netsnmp_stash_cache_helper().</p>
<h3>void netsnmp_cache_reqinfo_insert (<code>netsnmp_cache</code> * cache, <code>netsnmp_agent_request_info</code> * reqinfo, const char * name)</h3>
<p>Insert the cache information for a given request (PDU). </p>
<p> Definition at line 333 of file cache_handler.c. </p>
<p> References _build_cache_name(), netsnmp_agent_add_list_data(), netsnmp_agent_get_list_data(), netsnmp_create_data_list(), NULL, and SNMP_FREE. </p>
<p> Referenced by netsnmp_cache_helper_handler().</p>
<h3>unsigned int netsnmp_cache_timer_start (<code>netsnmp_cache</code> * cache)</h3>
<p>starts the recurring cache_load callback </p>
<p> Definition at line 191 of file cache_handler.c. </p>
<p> References netsnmp_cache_s::flags, NULL, netsnmp_cache_s::rootoid, netsnmp_cache_s::rootoid_len, snmp_alarm_register(), snmp_log(), netsnmp_cache_s::timeout, and netsnmp_cache_s::timer_id. </p>
<p> Referenced by netsnmp_cache_handler_get().</p>
<h3>void netsnmp_cache_timer_stop (<code>netsnmp_cache</code> * cache)</h3>
<p>stops the recurring cache_load callback </p>
<p> Definition at line 226 of file cache_handler.c. </p>
<p> References netsnmp_cache_s::flags, NULL, snmp_alarm_unregister(), snmp_log(), and netsnmp_cache_s::timer_id.</p>
<h3><code>netsnmp_cache</code>* netsnmp_extract_cache_info (<code>netsnmp_agent_request_info</code> * reqinfo)</h3>
<p>Extract the cache information for a given request (PDU). </p>
<p> Definition at line 362 of file cache_handler.c. </p>
<p> References netsnmp_cache_reqinfo_extract().</p>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_cache_handler (int timeout, NetsnmpCacheLoad * load_hook, NetsnmpCacheFree * free_hook, oid * rootoid, int rootoid_len)</h3>
<p>returns a cache handler that can be injected into a given handler chain. </p>
<p> Definition at line 276 of file cache_handler.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_cache_create(), netsnmp_cache_handler_get(), and NULL. </p>
<p> Referenced by netsnmp_register_cache_handler().</p>
<h3>int netsnmp_is_cache_valid (<code>netsnmp_agent_request_info</code> * reqinfo)</h3>
<p>for backwards compat </p>
<p> <code>netsnmp_cache_is_valid()</code> is preferred. </p>
<p> Definition at line 413 of file cache_handler.c. </p>
<p> References netsnmp_cache_is_valid().</p>
<h3>int netsnmp_register_cache_handler (<code>netsnmp_handler_registration</code> * reginfo, int timeout, NetsnmpCacheLoad * load_hook, NetsnmpCacheFree * free_hook)</h3>
<p>functionally the same as calling <code>netsnmp_register_handler()</code> but also injects a cache handler at the same time for you. </p>
<p> Definition at line 308 of file cache_handler.c. </p>
<p> References netsnmp_get_cache_handler(), netsnmp_inject_handler(), netsnmp_register_handler(), NULL, netsnmp_handler_registration_s::rootoid, and netsnmp_handler_registration_s::rootoid_len.</p>
<h3>void release_cached_resources (unsigned int regNo, void * clientargs)</h3>
<p>run regularly to automatically release cached resources. </p>
<p> xxx &#8211; method to prevent cache from expiring while a request is being processed (e.g. delegated request). proposal: set a flag, which would be cleared when request finished (which could be acomplished by a dummy data list item in agent req info &amp; custom free function). </p>
<p> Definition at line 575 of file cache_handler.c. </p>
<p> References netsnmp_cache_s::flags, netsnmp_cache_check_expired(), netsnmp_cache_s::next, NULL, and netsnmp_cache_s::valid.</p>
