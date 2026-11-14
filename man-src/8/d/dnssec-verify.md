---
title: "dnssec-verify(8)"
name: "dnssec-verify"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-verify/"
description: "dnssec-verify – DNSSEC zone verification tool"
---

<p>dnssec-verify &#8211; DNSSEC zone verification tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-verify</code> [<code>-c&nbsp;<wbr></code><i>class</i>] [<code>-E&nbsp;<wbr></code><i>engine</i>] [<code>-I&nbsp;<wbr></code><i>input-format</i>] [<code>-o&nbsp;<wbr></code><i>origin</i>] [<code>-v&nbsp;<wbr></code><i>level</i>] [<code>-x</code>] [<code>-z</code>] {zonefile}</dl>
<h2>Description</h2>
<p><code>dnssec-verify</code></p>
<dd>verifies that a zone is fully signed for each algorithm found in the DNSKEY RRset for the zone, and that the NSEC / NSEC3 chains are complete.</p>
<h2>Options</h2>
<p>-c <i>class</i></p>
<dl>
<dd>Specifies the DNS class of the zone.</dl>
<p> -I <i>input-format</i></p>
<dl>
<dd>The format of the input zone file. Possible formats are <code>&quot;text&quot;</code> (default) and <code>&quot;raw&quot;</code>. This option is primarily intended to be used for dynamic signed zones so that the dumped zone file in a non-text format containing updates can be verified independently. The use of this option does not make much sense for non-dynamic zones.</dl>
<p> -o <i>origin</i></p>
<dl>
<dd>The zone origin. If not specified, the name of the zone file is assumed to be the origin.</dl>
<p> -v <i>level</i></p>
<dl>
<dd>Sets the debugging level.</dl>
<p> -x</p>
<dl>
<dd>Only verify that the DNSKEY RRset is signed with key-signing keys. Without this flag, it is assumed that the DNSKEY RRset will be signed by all active keys. When this flag is set, it will not be an error if the DNSKEY RRset is not signed by zone-signing keys. This corresponds to the <code>-x</code> option in <code>dnssec-signzone</code>.</dl>
<p> -z</p>
<dl>
<dd>Ignore the KSK flag on the keys when determining whether the zone if correctly signed. Without this flag it is assumed that there will be a non-revoked, self-signed DNSKEY with the KSK flag set for each algorithm and that RRsets other than DNSKEY RRset will be signed with a different DNSKEY without the KSK flag set. </p>
<p> With this flag set, we only require that for each algorithm, there will be at least one non-revoked, self-signed DNSKEY, regardless of the KSK flag state, and that other RRsets will be signed by a non-revoked key for the same algorithm that includes the self-signed key; the same key may be used for both purposes. This corresponds to the <code>-z</code> option in <code>dnssec-signzone</code>.</dl>
<p> zonefile</p>
<dl>
<dd>The file containing the zone to be signed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-signzone/">dnssec-signzone</a></code>(8), BIND 9 Administrator Reference Manual, RFC 4033.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
