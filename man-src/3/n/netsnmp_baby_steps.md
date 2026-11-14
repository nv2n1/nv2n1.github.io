---
title: "netsnmp_baby_steps(3)"
name: "netsnmp_baby_steps"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_baby_steps/"
description: "baby_steps – Calls your handler in baby_steps for set processing."
---

<p>baby_steps &#8211; Calls your handler in baby_steps for set processing.</p>
<h3>Modules</h3>
<p><code>baby_steps_access_multiplexer: calls individual access methods based on baby_step mode.</code></p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_baby_steps_handler_get</code> (u_long modes)<br />
 <i>returns a baby_steps handler that can be injected into a given handler chain. </i><br />
 void <code>netsnmp_baby_steps_handler_init</code> (void)<br />
 <i>initializes the baby_steps helper which then registers a baby_steps handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Calls your handler in baby_steps for set processing.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_baby_steps_handler_get (u_long modes)</h3>
<p>returns a baby_steps handler that can be injected into a given handler chain. </p>
<p> Definition at line 58 of file baby_steps.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_handler_free(), NULL, netsnmp_baby_steps_modes_s::registered, snmp_log(), and SNMP_MALLOC_TYPEDEF. </p>
<p> Referenced by netsnmp_baby_steps_handler_init().</p>
<h3>void netsnmp_baby_steps_handler_init (void)</h3>
<p>initializes the baby_steps helper which then registers a baby_steps handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 319 of file baby_steps.c. </p>
<p> References netsnmp_baby_steps_handler_get(), and netsnmp_register_handler_by_name().</p>
