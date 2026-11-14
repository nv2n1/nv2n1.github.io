---
title: "netsnmp_serialize(3)"
name: "netsnmp_serialize"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_serialize/"
description: "serialize – Calls sub handlers one request at a time."
---

<p>serialize &#8211; Calls sub handlers one request at a time.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_serialize_handler</code> (void)<br />
 <i>returns a serialize handler that can be injected into a given handler chain. </i><br />
 int <code>netsnmp_register_serialize</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>functionally the same as calling </i><code>netsnmp_register_handler()</code> but also injects a serialize handler at the same time for you.<br />
 int <code>netsnmp_serialize_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)<br />
 <i>Implements the serial handler. </i><br />
 void <code>netsnmp_init_serialize</code> (void)<br />
 <i>initializes the serialize helper which then registers a serialize handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Calls sub handlers one request at a time. </p>
<p> This functionally passes in one request at a time into lower handlers rather than a whole bunch of requests at once. This is useful for handlers that don&#8217;t want to iterate through the request lists themselves. Generally, this is probably less efficient so use with caution. The serialize handler might be useable to dynamically fix handlers with broken looping code, however.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_serialize_handler (void)</h3>
<p>returns a serialize handler that can be injected into a given handler chain. </p>
<p> Definition at line 31 of file serialize.c. </p>
<p> References netsnmp_create_handler(), and netsnmp_serialize_helper_handler(). </p>
<p> Referenced by netsnmp_init_serialize(), and netsnmp_register_serialize().</p>
<h3>void netsnmp_init_serialize (void)</h3>
<p>initializes the serialize helper which then registers a serialize handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 93 of file serialize.c. </p>
<p> References netsnmp_get_serialize_handler(), and netsnmp_register_handler_by_name().</p>
<h3>int netsnmp_register_serialize (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>functionally the same as calling <code>netsnmp_register_handler()</code> but also injects a serialize handler at the same time for you. </p>
<p> Definition at line 40 of file serialize.c. </p>
<p> References netsnmp_get_serialize_handler(), netsnmp_inject_handler(), and netsnmp_register_handler(). </p>
<p> Referenced by netsnmp_register_instance(), netsnmp_register_read_only_instance(), netsnmp_register_read_only_scalar(), netsnmp_register_scalar(), and netsnmp_register_scalar_group().</p>
<h3>int netsnmp_serialize_helper_handler (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>Implements the serial handler. </p>
<p> Definition at line 48 of file serialize.c. </p>
<p> References netsnmp_call_next_handler(), netsnmp_request_info_s::next, and NULL. </p>
<p> Referenced by netsnmp_get_serialize_handler().</p>
