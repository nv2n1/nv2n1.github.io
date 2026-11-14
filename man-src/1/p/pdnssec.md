---
title: "pdnssec(1)"
name: "pdnssec"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdnssec/"
description: "pdnssec – PowerDNSSEC command and control"
---

<h2>NAME</h2>
<p> pdnssec &#8211; PowerDNSSEC command and control</p>
<h2>SYNOPSIS</h2>
<p> <code>pdnssec </code><i>[options]</i> command</p>
<h2>DESCRIPTION</h2>
<p> <i>pdnssec</i> is a powerful command that is the operator-friendly gateway into PowerDNSSEC configuration. Behind the scenes, <i>pdnssec</i> manipulates a PowerDNS backend database, which also means that for many databases, <i>pdnssec</i> can be run remotely, and can configure key material on different servers.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-h [ &#8211;help ]</code></p>
<dd>
 Show summary of options.</p>
<dt><code>-v [ &#8211;verbose ]</code></p>
<dd>
 Be more verbose.</p>
<dt><code>&#8211;force</code></p>
<dd>
 force an action</p>
<dt><code>&#8211;config-name arg</code></p>
<dd>
 Virtual configuration name</p>
<dt><code>&#8211;config-dir arg (=/etc/powerdns)</code></p>
<dd>
 Location of pdns.conf</p>
<dt><code>&#8211;commands arg</code></p>
<dd>
 Commands given as an argument</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>activate-zone-key ZONE KEY-ID</code></p>
<dd> Activate a key with id KEY-ID within a zone called ZONE.</p>
<dt><code>add-zone-key ZONE [zsk|ksk] [bits] [rsasha1|rsasha256|rsasha512|gost|ecdsa256|ecdsa384]</code></p>
<dd> Create a new key for zone ZONE, and make it a KSK or a ZSK, with the specified algorithm.</p>
<dt><code>check-zone ZONE</code></p>
<dd> Check a zone for correctness</p>
<dt><code>deactivate-zone-key ZONE KEY-ID</code></p>
<dd> Deactivate a key with id KEY-ID within a zone called ZONE.</p>
<dt><code>disable-dnssec ZONE</code></p>
<dd> Deactivate all keys and unset PRESIGNED in ZONE</p>
<dt><code>export-zone-dnskey ZONE KEY-ID</code></p>
<dd> Export to standard output DNSKEY and DS of key with key id KEY-ID within zone called ZONE.</p>
<dt><code>export-zone-key ZONE KEY-ID</code></p>
<dd> Export to standard output full (private) key with key id KEY-ID within zone called ZONE. The format used is compatible with BIND and NSD/LDNS.</p>
<dt><code>hash-zone-record ZONE RNAME</code></p>
<dd> This convenience command hashes the name &#8216;recordname&#8217; according to the NSEC3 settings of ZONE. Refuses to hash for zones with no NSEC3 settings.</p>
<dt><code>import-zone-key ZONE FILE [ksk|zsk]</code></p>
<dd> Import from &#8216;filename&#8217; a full (private) key for zone called ZONE. The format used is compatible with BIND and NSD/LDNS. KSK or ZSK specifies the flags this key should have on import.</p>
<dt><code>rectify-zone ZONE</code></p>
<dd> Calculates the &#8216;ordername&#8217; and &#8216;auth&#8217; fields for a zone called ZONE so they comply with DNSSEC settings. Can be used to fix up migrated data. Can always safely be run, it does no harm.</p>
<dt><code>remove-zone-key ZONE KEY-ID</code></p>
<dd> Remove a key with id KEY-ID from a zone called ZONE.</p>
<dt><code>secure-zone ZONE</code></p>
<dd> Configures a zone called ZONE with reasonable DNSSEC settings. You should manually run &#8216;pdnssec rectify-zone&#8217; afterwards.</p>
<dt><code>set-nsec3 ZONE &#8216;params&#8217; [narrow]</code></p>
<dd> Sets NSEC3 parameters for this zone. A sample commandline is: &quot;pdnssec set-nsec3 powerdnssec.org &#8216;1 1 1 ab&#8217; narrow&quot;. The NSEC3 parameters must be quoted on the command line.<br />
 <code>WARNING:</code><br />
 If running in RSASHA1 mode (algorithm 5 or 7), switching from NSEC to NSEC3 will require a DS update at the parent zone!</p>
<dt><code>set-presigned ZONE</code></p>
<dd> Switches zone to presigned operation, utilizing in-zone RRSIGs.</p>
<dt><code>show-zone ZONE</code></p>
<dd> Shows all DNSSEC related settings of a zone called ZONE.</p>
<dt><code>unset-nsec3 ZONE</code></p>
<dd> Converts a zone to NSEC operations.<br />
 <code>WARNING:</code><br />
 If running in RSASHA1 mode (algorithm 5 or 7), switching from NSEC to NSEC3 will require a DS update at the parent zone!</p>
<dt><code>unset-presigned ZONE</code></p>
<dd> Disables presigned operation for ZONE.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Matthijs Möhlmann &lt;matthijs [at] cacholong.nl&gt; for the Debian Project (but may be used by others)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pdns_server/">pdns_server</a></code>(8),<code><a href="/docs/linux/man/8-pdns_control/">pdns_control</a></code>(8) </p>
<h2>Index</h2>
