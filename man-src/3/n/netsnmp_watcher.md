---
title: "netsnmp_watcher(3)"
name: "netsnmp_watcher"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_watcher/"
description: "watcher – Watch a specified variable and process it as an instance or scalar object."
---

<p>watcher &#8211; Watch a specified variable and process it as an instance or scalar object.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_watcher_handler</code> (void) </p>
<p> <code>netsnmp_watcher_info</code> * <code>netsnmp_create_watcher_info</code> (void *data, size_t size, u_char type, int flags) </p>
<p> int <code>netsnmp_register_watched_instance</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_watcher_info</code> *watchinfo) </p>
<p> int <code>netsnmp_register_watched_scalar</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_watcher_info</code> *watchinfo) </p>
<p> int <code>netsnmp_watcher_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_watched_timestamp_handler</code> (void) </p>
<p> int <code>netsnmp_watched_timestamp_register</code> (<code>netsnmp_mib_handler</code> *whandler, <code>netsnmp_handler_registration</code> *reginfo, <code>marker_t</code> timestamp) </p>
<p> int <code>netsnmp_register_watched_timestamp</code> (<code>netsnmp_handler_registration</code> *reginfo, <code>marker_t</code> timestamp) </p>
<p> int <code>netsnmp_watched_timestamp_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_watched_spinlock_handler</code> (void) </p>
<p> int <code>netsnmp_register_watched_spinlock</code> (<code>netsnmp_handler_registration</code> *reginfo, int *spinlock) </p>
<p> int <code>netsnmp_watched_spinlock_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_register_ulong_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_ulong_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_long_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_long_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, long *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_int_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_int_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, int *it, <code>Netsnmp_Node_Handler</code> *subhandler) </p>
<p> int <code>netsnmp_register_read_only_counter32_scalar</code> (const char *name, oid *reg_oid, size_t reg_oid_len, u_long *it, <code>Netsnmp_Node_Handler</code> *subhandler)</p>
<h2>Detailed Description</h2>
<p>Watch a specified variable and process it as an instance or scalar object.</p>
