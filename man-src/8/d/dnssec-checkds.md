---
title: "dnssec-checkds(8)"
name: "dnssec-checkds"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-checkds/"
description: "dnssec-checkds – A DNSSEC delegation consistency checking tool."
---

<p>dnssec-checkds &#8211; A DNSSEC delegation consistency checking tool.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-checkds</code> [<code>-l&nbsp;<wbr></code><i>domain</i>] [<code>-f&nbsp;<wbr></code><i>file</i>] [<code>-d&nbsp;<wbr></code><i>dig path</i>] [<code>-D&nbsp;<wbr></code><i>dsfromkey path</i>] {zone}</p>
<dt> <code>dnssec-dsfromkey</code> [<code>-l&nbsp;<wbr></code><i>domain</i>] [<code>-f&nbsp;<wbr></code><i>file</i>] [<code>-d&nbsp;<wbr></code><i>dig path</i>] [<code>-D&nbsp;<wbr></code><i>dsfromkey path</i>] {zone}</dl>
<h2>Description</h2>
<p><code>dnssec-checkds</code></p>
<dd>verifies the correctness of Delegation Signer (DS) or DNSSEC Lookaside Validation (DLV) resource records for keys in a specified zone.</p>
<h2>Options</h2>
<p>-f <i>file</i></p>
<dl>
<dd>If a <code>file</code> is specified, then the zone is read from that file to find the DNSKEY records. If not, then the DNSKEY records for the zone are looked up in the DNS.</dl>
<p> -l <i>domain</i></p>
<dl>
<dd>Check for a DLV record in the specified lookaside domain, instead of checking for a DS record in the zone&#8217;s parent. For example, to check for DLV records for &quot;example.com&quot; in ISC&#8217;s DLV zone, use: <code>dnssec-checkds -l dlv.isc.org example.com</code></dl>
<p> -d <i>dig path</i></p>
<dl>
<dd>Specifies a path to a <code>dig</code> binary. Used for testing.</dl>
<p> -D <i>dsfromkey path</i></p>
<dl>
<dd>Specifies a path to a <code>dnssec-dsfromkey</code> binary. Used for testing.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-dsfromkey/">dnssec-dsfromkey</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-signzone/">dnssec-signzone</a></code>(8),</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012, 2013 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
