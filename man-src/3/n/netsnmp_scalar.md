---
title: "netsnmp_scalar(3)"
name: "netsnmp_scalar"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_scalar/"
description: "scalar – Process scalars easily."
---

<p>scalar &#8211; Process scalars easily.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_scalar_handler</code> (void)<br />
 <i>Creates a scalar handler calling netsnmp_create_handler with a handler name defaulted to &#8216;scalar&#8217; and access method, netsnmp_scalar_helper_handler. </i><br />
 int <code>netsnmp_register_scalar</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>This function registers a scalar helper handler. </i><br />
 int <code>netsnmp_register_read_only_scalar</code> (<code>netsnmp_handler_registration</code> *reginfo)<br />
 <i>This function registers a read only scalar helper handler. </i><br />
 int <code>netsnmp_scalar_helper_handler</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests)</p>
<h2>Detailed Description</h2>
<p>Process scalars easily.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_scalar_handler (void)</h3>
<p>Creates a scalar handler calling netsnmp_create_handler with a handler name defaulted to &#8216;scalar&#8217; and access method, netsnmp_scalar_helper_handler. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns a pointer to a netsnmp_mib_handler struct which contains the handler&#8217;s name and the access method</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>netsnmp_get_scalar_handler</code> </p>
<p> <code>netsnmp_register_scalar</code></dl>
<p> Definition at line 46 of file scalar.c. </p>
<p> References netsnmp_create_handler(), and netsnmp_scalar_helper_handler(). </p>
<p> Referenced by netsnmp_register_read_only_scalar(), netsnmp_register_scalar(), and netsnmp_register_scalar_group().</p>
<h3>int netsnmp_register_read_only_scalar (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>This function registers a read only scalar helper handler. </p>
<p> This function is very similar to netsnmp_register_scalar the only addition is that the &#8216;read_only&#8217; handler is injected into the handler chain prior to injecting the serialize handler and registering reginfo. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>reginfo</i> a handler registration structure which could get created using netsnmp_create_handler_registration. Used to register a read only scalar helper handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>MIB_REGISTERED_OK is returned if the registration was a success. Failures are MIB_REGISTRATION_FAILURE and MIB_DUPLICATE_REGISTRATION.</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>netsnmp_register_scalar</code> </p>
<p> <code>netsnmp_get_scalar_handler</code></dl>
<p> Definition at line 109 of file scalar.c. </p>
<p> References netsnmp_get_instance_handler(), netsnmp_get_read_only_handler(), netsnmp_get_scalar_handler(), netsnmp_inject_handler(), netsnmp_register_serialize(), netsnmp_handler_registration_s::rootoid, and netsnmp_handler_registration_s::rootoid_len.</p>
<h3>int netsnmp_register_scalar (<code>netsnmp_handler_registration</code> * reginfo)</h3>
<p>This function registers a scalar helper handler. </p>
<p> The registered OID, reginfo-&gt;rootoid, space is extended for the instance subid using realloc() but the reginfo-&gt;rootoid_len length is not extended just yet. .This function subsequently injects the instance, scalar, and serialize helper handlers before actually registering reginfo. </p>
<p> Each handler is injected/pushed to the top of the handler chain list and will be processed last in first out, LIFO. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>reginfo</i> a handler registration structure which could get created using netsnmp_create_handler_registration. Used to register a scalar helper handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>MIB_REGISTERED_OK is returned if the registration was a success. Failures are MIB_REGISTRATION_FAILURE and MIB_DUPLICATE_REGISTRATION.</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>netsnmp_register_read_only_scalar</code> </p>
<p> <code>netsnmp_get_scalar_handler</code></dl>
<p> Definition at line 74 of file scalar.c. </p>
<p> References netsnmp_get_instance_handler(), netsnmp_get_scalar_handler(), netsnmp_inject_handler(), netsnmp_register_serialize(), netsnmp_handler_registration_s::rootoid, and netsnmp_handler_registration_s::rootoid_len. </p>
<p> Referenced by netsnmp_register_watched_scalar(), and netsnmp_watched_timestamp_register().</p>
