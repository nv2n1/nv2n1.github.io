---
title: "ldns-keyfetcher(1)"
name: "ldns-keyfetcher"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-keyfetcher/"
description: "ldns-keyfetcher – retrieve the DNSSEC DNSKEYs for a zone"
---

<h2>NAME</h2>
<p> ldns-keyfetcher &#8211; retrieve the DNSSEC DNSKEYs for a zone</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-keyfetcher</code> [ <i>OPTIONS</i> ] <i>DOMAIN</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-keyfetcher</code> is used to retrieve the DNSKEYs of a zone. </p>
<p> First it finds all authoritative nameservers of the zone by tracing it from the root down. All authoritative nameservers are then queried (using TCP) for the DNSKEY RRset of the zone apex. If the results are all the same, the key resource record set is printed. </p>
<h2>OPTIONS</h2>
<p> <code>-4</code> <i></i> Only use IPv4 </p>
<p> <code>-6</code> <i></i> Only use IPv6 </p>
<p> <code>-h</code> <i></i> Show a help text and exit </p>
<p> <code>-i</code> Insecurer mode; there will only be one query for the DNSKEYS. There will not be crosschecking of all authoritative nameservers. </p>
<p> <code>-v</code> <i>verbosity</i> </p>
<p> Set the verbosity level. The following levels are available: </p>
<p>&nbsp;<wbr>0: default, only print the DNSKEY RRset found, or an error on failure.<br />
&nbsp;<wbr>1: Show the nameservers that are queried<br />
&nbsp;<wbr>2: Show more info on what is checked<br />
&nbsp;<wbr>3: Show the intermediate results&nbsp;<wbr>(authority and dnskey rrsets)<br />
&nbsp;<wbr>4: Print the answer packets that are returned </p>
<p> <code>-r</code> <i>file</i> </p>
<p> Use file as the root hints file, should contain A records in presentation format. The default is /etc/named.root. You can get this file from <a rel="nofollow" href="http://www.internic.net/zones/named.root.">http://www.internic.net/zones/named.root.</a> </p>
<p> <code>-s</code> <i></i> Don&#8217;t print the keys to stdout, but store them in files. </p>
<p> The filenames will be of the format K&lt;file&gt;.+&lt;alg&gt;.+&lt;keytag&gt;.key </p>
<h2>AUTHOR</h2>
<p> Written by Jelte Jansen for NLnet Labs. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
