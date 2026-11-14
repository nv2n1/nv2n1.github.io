---
title: "getdns_validate_dnssec(3)"
name: "getdns_validate_dnssec"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_validate_dnssec/"
description: "getdns_validate_dnssec — DNSSEC validate a given getdns record"
---

<h2>NAME</h2>
<p> <code>getdns_validate_dnssec</code> &#8212; DNSSEC validate a given getdns record </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_validate_dnssec</code> (getdns_list *record_to_validate, </p>
<dl>
<dt>
<dd> getdns_list *bundle_of_support_records,<br />
 getdns_list *trust_anchor_records)</dl>
<h2>DESCRIPTION</h2>
<p> If an application wants the API to perform DNSSEC validation without using the extensions, it can use the getdns_validate_dnssec() helper function. The API will use the resource records in bundle_of_support_records to construct the validation chain and the DNSKEY or DS records in trust_anchor_records as trust anchors. The default list of trust anchor records that is used by the library to validate DNSSEC can be retrieved by using the getdns_root_trust_anchor helper function. </p>
<dl>
<dt> <i>record_to_validate</i></p>
<dd>the resource record being validated </p>
<dt> <i>bundle_of_support_records</i></p>
<dd>records used to construct the validation chain </p>
<dt> <i>trust_anchor_records</i></p>
<dd>trust anchor records to use for the validation </p>
<dt></dl>
<h2>RETURN VALUES</h2>
<p> <code>GETDNS_DNSSEC_BOGUS</code></p>
<dd>the DNSSEC signature is bogus </p>
<p> <code>GETDNS_DNSSEC_INDETERMINATE</code> validation could not be completed </p>
<p> <code>GETDNS_DNSSEC_INSECURE</code> one or more pieces of the validation chain are demonstrably incorrect </p>
<p> <code>GETDNS_DNSSEC_SECURE</code> validation succeeded </p>
<p> <code>GETDNS_RETURN_MEMORY_ERROR</code> an attempt to allocate memory failed </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getdns_root_trust_anchor/">getdns_root_trust_anchor</a></code>(3) <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3) </p>
<h2>Index</h2>
