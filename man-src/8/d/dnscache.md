---
title: "dnscache(8)"
name: "dnscache"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnscache/"
description: "dnscache – djbdns DNS cache daemon."
---

<p><code>dnscache</code> &#8211; djbdns DNS cache daemon. </p>
<h2>Synopsis</h2>
<dl>
<dt><code>dnscache</code> [<code>OPTIONS</code>]</p>
<dd>
<h2>Description</h2>
<p><code>dnscache</code> is used to map a domain name to its IP address and vice versa. Upon invocation, <code>dnscache</code> reads from its configuration file and listens on TCP/UDP port 53 for incoming requests. Typically <code>dnscache</code> accepts incoming requests only from localhost(127.0.0.1). To accept requests from external machine or subnet, create a file, named after the IP address of a machine or subnet from which to accept requests, under the `ip/&#8217; directory. Ie. <code>dnscache</code> would accept requests from IP address 1.2.3.4, if there is a file named 1.2.3.4 OR 1.2.3 OR 1.2 OR 1. under the `ip/&#8217; directory. To resolve a domain name, <code>dnscache</code> contacts the name servers listed in files under the `servers/&#8217; directory. File `roots&#8217; lists the root name servers. <code>dnscache</code> would contact servers listed in the `servers/mydomain.com&#8217; file, to resolve domain names that end with mydomain.com, like say: mail.mydomain.com or irc.mydomain.com etc. Note: these files list IP addresses of name servers one on each line. From version <code>1.05.9</code>, <code>dnscache</code> introduced support for the DNS(or Domain) Block List. DNS Block List is a list of domain names which are to be blocked by the resolver. Client requests querying for such domain names are dropped by the resolver. This would add an additional layer of security for DNS clients and also help to reduce malicious traffic. DNS block list is a &#8216;cdb&#8217; database created using <a href="/docs/linux/man/1-tinydns-data/">tinydns-data</a>(1) tool. List the malicious domain names into a &#8216;data&#8217; file as generic domain records, one on each line, as:<br />
&nbsp;<wbr>:bad.domain.com:284:::: Number &#8216;284&#8217; is not used, it can be any number between 256&#8230;65535. <a href="/docs/linux/man/1-tinydns-data/">tinydns-data</a>(1) would create a &#8216;data.cdb&#8217; database from this &#8216;data&#8217; file. Rename <code>data.cdb</code> to <code>dnsbl.cdb</code>, because that is the file read by <code>dnscache</code> server.<br />
&nbsp;<wbr>$&nbsp;<wbr>mv data.cdb dnsbl.cdb <code>dnscache</code> would read &#8216;dnsbl.cdb&#8217; from its working($ROOT) directory defined in the &#8216;dnscache.conf&#8217; file. </p>
<h2>Options</h2>
<dl>
<dt><code>-d &lt;value&gt;</code></p>
<dd>&nbsp;<wbr>print debug messages as per the debug level 1, 2 or 3.</p>
<dt><code>-D</code></p>
<dd>&nbsp;<wbr>run as a daemon.</p>
<dt><code>-h &#8211;help</code></p>
<dd>&nbsp;<wbr>print this help.</p>
<dt><code>-v &#8211;version</code></p>
<dd>&nbsp;<wbr>print version information. </p>
</dl>
<h2>Files</h2>
<p>&nbsp;<wbr>/etc/ndjbdns/ip/<br />
&nbsp;<wbr>/etc/ndjbdns/servers/<br />
&nbsp;<wbr>/etc/ndjbdns/dnscache.conf </p>
<p>&nbsp;<wbr>/var/log/dnscached.log</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Author</h2>
<p>Prasad J Pandit</p>
