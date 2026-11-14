---
title: "netsnmp_mode_end_call(3)"
name: "netsnmp_mode_end_call"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_mode_end_call/"
description: "mode_end_call – At the end of a series of requests, call another handler hook."
---

<p>mode_end_call &#8211; At the end of a series of requests, call another handler hook.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_mode_end_call_handler</code> (<code>netsnmp_mode_handler_list</code> *endlist)<br />
 <i>returns a mode_end_call handler that can be injected into a given handler chain. </i><br />
 <code>netsnmp_mode_handler_list</code> * <code>netsnmp_mode_end_call_add_mode_callback</code> (<code>netsnmp_mode_handler_list</code> *endlist, int mode, <code>netsnmp_mib_handler</code> *callbackh)<br />
 <i>adds a mode specific callback to the callback list. </i><br />
 int <code>netsnmp_mode_end_call_helper</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)</p>
<h2>Detailed Description</h2>
<p>At the end of a series of requests, call another handler hook. </p>
<p> Handlers that want to loop through a series of requests and then receive a callback at the end of a particular MODE can use this helper to make this possible. For most modules, this is not needed as the handler itself could perform a for() loop around the request list and then perform its actions afterwards. However, if something like the serialize helper is in use this isn&#8217;t possible because not all the requests for a given handler are being passed downward in a single group. Thus, this helper *must* be added above other helpers like the serialize helper to be useful. </p>
<p> Multiple mode specific handlers can be registered and will be called in the order they were regestered in. Callbacks regesterd with a mode of NETSNMP_MODE_END_ALL_MODES will be called for all modes.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_mode_end_call_handler (<code>netsnmp_mode_handler_list</code> * endlist)</h3>
<p>returns a mode_end_call handler that can be injected into a given handler chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>endlist</i> The callback list for the handler to make use of.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An injectable Net-SNMP handler.</dl>
<p> Definition at line 45 of file mode_end_call.c. </p>
<p> References netsnmp_mib_handler_s::myvoid, netsnmp_create_handler(), netsnmp_mode_end_call_helper(), and NULL.</p>
<h3><code>netsnmp_mode_handler_list</code>* netsnmp_mode_end_call_add_mode_callback (<code>netsnmp_mode_handler_list</code> * endlist, int mode, <code>netsnmp_mib_handler</code> * callbackh)</h3>
<p>adds a mode specific callback to the callback list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>endlist</i> the information structure for the mode_end_call helper. Can be NULL to create a new list.<br />
 <i>mode</i> the mode to be called upon. A mode of NETSNMP_MODE_END_ALL_MODES = all modes.<br />
 <i>callbackh</i> the netsnmp_mib_handler callback to call.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the new registration information list upon success.</dl>
<p> Definition at line 65 of file mode_end_call.c. </p>
<p> References netsnmp_mode_handler_list_s::callback_handler, netsnmp_mode_handler_list_s::mode, netsnmp_mode_handler_list_s::next, NULL, and SNMP_MALLOC_TYPEDEF.</p>
