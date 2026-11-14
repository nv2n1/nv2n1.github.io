---
title: "netsnmp_multiplexer(3)"
name: "netsnmp_multiplexer"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_multiplexer/"
description: "multiplexer – Splits mode requests into calls to different handlers."
---

<p>multiplexer &#8211; Splits mode requests into calls to different handlers.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_multiplexer_handler</code> (<code>netsnmp_mib_handler_methods</code> *req)<br />
 <i>returns a multiplixer handler given a </i><code>netsnmp_mib_handler_methods</code> structure of subhandlers.<br />
 int <code>netsnmp_multiplexer_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)<br />
 <i>implements the multiplexer helper </i></p>
<h2>Detailed Description</h2>
<p>Splits mode requests into calls to different handlers. </p>
<p> The multiplexer helper lets you split the calling chain depending on the calling mode (get vs getnext vs set). Useful if you want different routines to handle different aspects of SNMP requests, which is very common for GET vs SET type actions. </p>
<p> Functionally: </p>
<dl>
<dt>1.</p>
<dd>GET requests call the get_method</p>
<dt>2.</p>
<dd>GETNEXT requests call the getnext_method, or if not present, the get_method.</p>
<dt>3.</p>
<dd>GETBULK requests call the getbulk_method, or if not present, the getnext_method, or if even that isn&#8217;t present the get_method.</p>
<dt>4.</p>
<dd>SET requests call the set_method, or if not present return a SNMP_ERR_NOTWRITABLE error.</dl>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_multiplexer_handler (<code>netsnmp_mib_handler_methods</code> * req)</h3>
<p>returns a multiplixer handler given a <code>netsnmp_mib_handler_methods</code> structure of subhandlers. </p>
<p> Definition at line 33 of file multiplexer.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_multiplexer_helper_handler(), NULL, and snmp_log().</p>
<h3>int netsnmp_multiplexer_helper_handler (<code>netsnmp_mib_handler</code> * handler, <code>netsnmp_handler_registration</code> * reginfo, <code>netsnmp_agent_request_info</code> * reqinfo, <code>netsnmp_request_info</code> * requests)</h3>
<p>implements the multiplexer helper </p>
<p> Definition at line 54 of file multiplexer.c. </p>
<p> References netsnmp_agent_request_info_s::mode, netsnmp_mib_handler_s::myvoid, netsnmp_call_handler(), netsnmp_request_set_error_all(), and snmp_log(). </p>
<p> Referenced by netsnmp_get_multiplexer_handler().</p>
