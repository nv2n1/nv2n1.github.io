---
title: "hosts(5)"
name: "hosts"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hosts/"
description: "hosts – static table lookup for hostnames"
---

<p>hosts &#8211; static table lookup for hostnames</p>
<h2>Synopsis</h2>
<p><code>/etc/hosts</code></p>
<h2>Description</h2>
<p>This manual page describes the format of the <i>/etc/hosts</i> file. This file is a simple text file that associates IP addresses with hostnames, one line per IP address. For each host a single line should be present with the following information:</p>
<dl>
<dd>IP_address canonical_hostname [aliases&#8230;]</dl>
<p> The IP address can conform to either IPv4 or IPv6. Fields of the entry are separated by any number of blanks and/or tab characters. Text from a &quot;#&quot; character until the end of the line is a comment, and is ignored. Host names may contain only alphanumeric characters, minus signs (&quot;-&quot;), and periods (&quot;.&quot;). They must begin with an alphabetic character and end with an alphanumeric character. Optional aliases provide for name changes, alternate spellings, shorter hostnames, or generic hostnames (for example, <i>localhost</i>). If required, a host may have two separate entries in this file; one for each version of the Internet Protocol (IPv4 and IPv6). </p>
<p> The Berkeley Internet Name Domain (BIND) Server implements the Internet name server for UNIX systems. It augments or replaces the <i>/etc/hosts</i> file or hostname lookup, and frees a host from relying on <i>/etc/hosts</i> being up to date and complete. </p>
<p> In modern systems, even though the host table has been superseded by DNS, it is still widely used for:</p>
<dl>
<dt><code>bootstrapping</code></p>
<dd>Most systems have a small host table containing the name and address information for important hosts on the local network. This is useful when DNS is not running, for example during system bootup.</p>
<dt><code>NIS</code></p>
<dd>Sites that use NIS use the host table as input to the NIS host database. Even though NIS can be used with DNS, most NIS sites still use the host table with an entry for all local hosts as a backup.</p>
<dt><code>isolated nodes</code></p>
<dd>Very small sites that are isolated from the network use the host table instead of DNS. If the local information rarely changes, and the network is not connected to the Internet, DNS offers little advantage.</dl>
<h2>Files</h2>
<p><i>/etc/hosts</i></p>
<h2>Notes</h2>
<p>Modifications to this file normally take effect immediately, except in cases where the file is cached by applications.</p>
<h3>Historical notes</h3>
<p>RFC 952 gave the original format for the host table, though it has since changed. </p>
<p> Before the advent of DNS, the host table was the only way of resolving hostnames on the fledgling Internet. Indeed, this file could be created from the official host data base maintained at the Network Information Control Center (NIC), though local changes were often required to bring it up to date regarding unofficial aliases and/or unknown hosts. The NIC no longer maintains the hosts.txt files, though looking around at the time of writing (circa 2000), there are historical hosts.txt files on the WWW. I just found three, from 92, 94, and 95.</p>
<h2>Examples</h2>
<p># The following lines are desirable for IPv4 capable hosts 127.0.0.1 localhost </p>
<p> # 127.0.1.1 is often used for the FQDN of the machine 127.0.1.1 thishost.mydomain.org thishost 192.168.1.10 foo.mydomain.org foo 192.168.1.13 bar.mydomain.org bar 146.82.138.7 master.debian.org master 209.237.226.90 <a rel="nofollow" href="http://www.opensource.org">www.opensource.org</a> </p>
<p> # The following lines are desirable for IPv6 capable hosts ::1 localhost ip6-localhost ip6-loopback ff02::1 ip6-allnodes ff02::2 ip6-allrouters</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1), <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3), <code><a href="/docs/linux/man/5-host-conf/">host.conf</a></code>(5), <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8) </p>
<p> Internet RFC 952</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
