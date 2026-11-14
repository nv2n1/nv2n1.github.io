---
title: "dnssec-coverage(8)"
name: "dnssec-coverage"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-coverage/"
description: "dnssec-coverage – checks future DNSKEY coverage for a zone"
---

<p>dnssec-coverage &#8211; checks future DNSKEY coverage for a zone</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-coverage</code> [<code>-K&nbsp;<wbr></code><i>directory</i>] [<code>-f&nbsp;<wbr></code><i>file</i>] [<code>-d&nbsp;<wbr></code><i>DNSKEY TTL</i>] [<code>-m&nbsp;<wbr></code><i>max TTL</i>] [<code>-r&nbsp;<wbr></code><i>interval</i>] [<code>-c&nbsp;<wbr></code><i>compilezone path</i>] [zone]</dl>
<h2>Description</h2>
<p><code>dnssec-coverage</code></p>
<dd>verifies that the DNSSEC keys for a given zone or a set of zones have timing metadata set properly to ensure no future lapses in DNSSEC coverage. </p>
<p> If <code>zone</code> is specified, then keys found in the key repository matching that zone are scanned, and an ordered list is generated of the events scheduled for that key (i.e., publication, activation, inactivation, deletion). The list of events is walked in order of occurrence. Warnings are generated if any event is scheduled which could cause the zone to enter a state in which validation failures might occur: for example, if the number of published or active keys for a given algorithm drops to zero, or if a key is deleted from the zone too soon after a new key is rolled, and cached data signed by the prior key has not had time to expire from resolver caches. </p>
<p> If <code>zone</code> is not specified, then all keys in the key repository will be scanned, and all zones for which there are keys will be analyzed. (Note: This method of reporting is only accurate if all the zones that have keys in a given repository share the same TTL parameters.)</p>
<h2>Options</h2>
<p>-f <i>file</i></p>
<dl>
<dd>If a <code>file</code> is specified, then the zone is read from that file; the largest TTL and the DNSKEY TTL are determined directly from the zone data, and the <code>-m</code> and <code>-d</code> options do not need to be specified on the command line.</dl>
<p> -K <i>directory</i></p>
<dl>
<dd>Sets the directory in which keys can be found. Defaults to the current working directory.</dl>
<p> -m <i>maximum TTL</i></p>
<dl>
<dd>Sets the value to be used as the maximum TTL for the zone or zones being analyzed when determining whether there is a possibility of validation failure. When a zone-signing key is deactivated, there must be enough time for the record in the zone with the longest TTL to have expired from resolver caches before that key can be purged from the DNSKEY RRset. If that condition does not apply, a warning will be generated. </p>
<p> The length of the TTL can be set in seconds, or in larger units of time by adding a suffix: &#8216;mi&#8217; for minutes, &#8216;h&#8217; for hours, &#8216;d&#8217; for days, &#8216;w&#8217; for weeks, &#8216;mo&#8217; for months, &#8216;y&#8217; for years. </p>
<p> This option is mandatory unless the <code>-f</code> has been used to specify a zone file. (If <code>-f</code> has been specified, this option may still be used; it will overrde the value found in the file.)</dl>
<p> -d <i>DNSKEY TTL</i></p>
<dl>
<dd>Sets the value to be used as the DNSKEY TTL for the zone or zones being analyzed when determining whether there is a possibility of validation failure. When a key is rolled (that is, replaced with a new key), there must be enough time for the old DNSKEY RRset to have expired from resolver caches before the new key is activated and begins generating signatures. If that condition does not apply, a warning will be generated. </p>
<p> The length of the TTL can be set in seconds, or in larger units of time by adding a suffix: &#8216;mi&#8217; for minutes, &#8216;h&#8217; for hours, &#8216;d&#8217; for days, &#8216;w&#8217; for weeks, &#8216;mo&#8217; for months, &#8216;y&#8217; for years. </p>
<p> This option is mandatory unless the <code>-f</code> has been used to specify a zone file, or a default key TTL was set with the <code>-L</code> to <code>dnssec-keygen</code>. (If either of those is true, this option may still be used; it will overrde the value found in the zone or key file.)</dl>
<p> -r <i>resign interval</i></p>
<dl>
<dd>Sets the value to be used as the resign interval for the zone or zones being analyzed when determining whether there is a possibility of validation failure. This value defaults to 22.5 days, which is also the default in <code>named</code>. However, if it has been changed by the <code>sig-validity-interval</code> option in <i>named.conf</i>, then it should also be changed here. </p>
<p> The length of the interval can be set in seconds, or in larger units of time by adding a suffix: &#8216;mi&#8217; for minutes, &#8216;h&#8217; for hours, &#8216;d&#8217; for days, &#8216;w&#8217; for weeks, &#8216;mo&#8217; for months, &#8216;y&#8217; for years.</dl>
<p> -c <i>compilezone path</i></p>
<dl>
<dd>Specifies a path to a <code>named-compilezone</code> binary. Used for testing.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-checkds/">dnssec-checkds</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-dsfromkey/">dnssec-dsfromkey</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-signzone/">dnssec-signzone</a></code>(8)</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
