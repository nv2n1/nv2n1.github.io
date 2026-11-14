---
title: "netsnmp_debug(3)"
name: "netsnmp_debug"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_debug/"
description: "debug – Print out debugging information about the handler chain being called."
---

<p>debug &#8211; Print out debugging information about the handler chain being called.</p>
<h3>handler</h3>
<pre><code>void netsnmp_init_serialize (void)


initializes the serialize helper which then registers a serialize handler as a run-time injectable handler for configuration file use.


void netsnmp_init_read_only_helper (void)


initializes the read_only helper which then registers a read_only handler as a run-time injectable handler for configuration file use.


void netsnmp_init_bulk_to_next_helper (void)


initializes the bulk_to_next helper which then registers a bulk_to_next handler as a run-time injectable handler for configuration file use.


void netsnmp_init_table_dataset (void)



void netsnmp_init_stash_cache_helper (void)


initializes the stash_cache helper which then registers a stash_cache handler as a run-time injectable handler for configuration file use.


void netsnmp_init_helpers (void)


call the initialization sequence for all handlers with init_ routines.



Functions</code></pre>
<p> <code>netsnmp_mib_handler</code> * <code>netsnmp_get_debug_handler</code> (void)<br />
 <i>returns a debug handler that can be injected into a given handler chain. </i><br />
 void <code>debug_print_requests</code> (<code>netsnmp_request_info</code> *requests) </p>
<p> int <code>netsnmp_debug_helper</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> void <code>netsnmp_init_debug_helper</code> (void)<br />
 <i>initializes the debug helper which then registers a debug handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Print out debugging information about the handler chain being called. </p>
<p> This is a useful module for run-time debugging of requests as the pass this handler in a calling chain. All debugging output is done via the standard debugging routines with a token name of &#8216;helper:debug&#8217;, so use the -Dhelper:debug command line flag to see the output when running the snmpd demon. It&#8217;s not recommended you compile this into a handler chain during compile time, but instead use the &#8216;injectHandler&#8217; token in the snmpd.conf file (or similar) to add it to the chain later: </p>
<p> injectHandler debug my_module_name </p>
<p> to see an example output, try: </p>
<p> injectHandler debug mibII/system </p>
<p> and then run snmpwalk on the &#8216;system&#8217; group.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_debug_handler (void)</h3>
<p>returns a debug handler that can be injected into a given handler chain. </p>
<p> Definition at line 51 of file debug_handler.c. </p>
<p> References netsnmp_create_handler(), and netsnmp_debug_helper(). </p>
<p> Referenced by netsnmp_init_debug_helper().</p>
<h3>void netsnmp_init_bulk_to_next_helper (void)</h3>
<p>initializes the bulk_to_next helper which then registers a bulk_to_next handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 139 of file bulk_to_next.c. </p>
<p> Referenced by netsnmp_init_helpers().</p>
<h3>void netsnmp_init_debug_helper (void)</h3>
<p>initializes the debug helper which then registers a debug handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 155 of file debug_handler.c. </p>
<p> References netsnmp_get_debug_handler(), and netsnmp_register_handler_by_name().</p>
<h3>void netsnmp_init_helpers (void)</h3>
<p>call the initialization sequence for all handlers with init_ routines. </p>
<p> Definition at line 36 of file all_helpers.c. </p>
<p> References netsnmp_init_bulk_to_next_helper(), netsnmp_init_debug_helper(), netsnmp_init_read_only_helper(), netsnmp_init_serialize(), netsnmp_init_stash_cache_helper(), and netsnmp_init_table_dataset(). </p>
<p> Referenced by init_agent().</p>
<h3>void netsnmp_init_read_only_helper (void)</h3>
<p>initializes the read_only helper which then registers a read_only handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 81 of file read_only.c. </p>
<p> Referenced by netsnmp_init_helpers().</p>
<h3>void netsnmp_init_serialize (void)</h3>
<p>initializes the serialize helper which then registers a serialize handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 93 of file serialize.c. </p>
<p> Referenced by netsnmp_init_helpers().</p>
<h3>void netsnmp_init_stash_cache_helper (void)</h3>
<p>initializes the stash_cache helper which then registers a stash_cache handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 237 of file stash_cache.c. </p>
<p> References netsnmp_get_stash_cache_handler(), and netsnmp_register_handler_by_name(). </p>
<p> Referenced by netsnmp_init_helpers().</p>
