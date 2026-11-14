---
title: "getdns_root_trust_anchor(3)"
name: "getdns_root_trust_anchor"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_root_trust_anchor/"
description: "getdns_root_trust_anchor — return the getdns list of default root trust anchors"
---

<h2>NAME</h2>
<p> <code>getdns_root_trust_anchor</code> &#8212; return the getdns list of default root trust anchors </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_list *<br />
 <code>getdns_root_trust_anchor</code> (time_t *utc_date_of_anchor) </p>
<h2>DESCRIPTION</h2>
<p> If an application wants the API to perform DNSSEC validation without using the extensions, it can use the getdns_validate_dnssec() helper function. The API will use the resource records in bundle_of_support_records to construct the validation chain and the DNSKEY or DS records in trust_anchor_records as trust anchors. The default list of trust anchor records that is used by the library to validate DNSSEC can be retrieved by using the getdns_root_trust_anchor helper function. </p>
<dl>
<dt> <i>utc_date_of_anchor</i></p>
<dd>time the trust anchors were obtained in epoch seconds (on success) </p>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Returns the default list of trust anchor records used by the library to validate DNSSEC or NULL if no default trust anchors are available. </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getdns_validate_dnssec/">getdns_validate_dnssec</a></code>(3) <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3) </p>
<h2>Index</h2>
