---
title: "services(5)"
name: "services"
section: "5"
letter: "s"
url: "/docs/linux/man/5-services/"
description: "services – Internet network services list"
---

<p>services &#8211; Internet network services list</p>
<h2>Description</h2>
<p><code>services</code> is a plain ASCII file providing a mapping between human-friendly textual names for internet services, and their underlying assigned port numbers and protocol types. Every networking program should look into this file to get the port number (and protocol) for its service. The C library routines <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3), <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3), <code><a href="/docs/linux/man/3-setservent/">setservent</a></code>(3), and <code><a href="/docs/linux/man/3-endservent/">endservent</a></code>(3) support querying this file from programs. </p>
<p> Port numbers are assigned by the IANA (Internet Assigned Numbers Authority), and their current policy is to assign both TCP and UDP protocols when assigning a port number. Therefore, most entries will have two entries, even for TCP-only services. </p>
<p> Port numbers below 1024 (so-called &quot;low numbered&quot; ports) can be bound to only by root (see <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), and <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7)). This is so clients connecting to low numbered ports can trust that the service running on the port is the standard implementation, and not a rogue service run by a user of the machine. Well-known port numbers specified by the IANA are normally located in this root-only space. </p>
<p> The presence of an entry for a service in the <code>services</code> file does not necessarily mean that the service is currently running on the machine. See <code><a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a></code>(5) for the configuration of Internet services offered. Note that not all networking services are started by <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), and so won&#8217;t appear in <code><a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a></code>(5). In particular, news (NNTP) and mail (SMTP) servers are often initialized from the system boot scripts. </p>
<p> The location of the <code>services</code> file is defined by <code>_PATH_SERVICES</code> in <i>&lt;netdb.h&gt;</i>. This is usually set to <i>/etc/services</i>. </p>
<p> Each line describes one service, and is of the form:</p>
<dl>
<dd><i>service-name&nbsp;<wbr>&nbsp;<wbr>&nbsp;port</i><code>/</code><i>protocol&nbsp;<wbr>&nbsp;<wbr>&nbsp;</i>[<i>aliases &#8230;</i>]</p>
<dt>where:</p>
<dd>
<dt><i>service-name</i></p>
<dd>is the friendly name the service is known by and looked up under. It is case sensitive. Often, the client program is named after the <i>service-name</i>.</p>
<dt><i>port</i></p>
<dd>is the port number (in decimal) to use for this service.</p>
<dt><i>protocol</i></p>
<dd>is the type of protocol to be used. This field should match an entry in the <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5) file. Typical values include <code>tcp</code> and <code>udp</code>.</p>
<dt><i>aliases</i></p>
<dd>is an optional space or tab separated list of other names for this service. Again, the names are case sensitive.</dl>
<p> Either spaces or tabs may be used to separate the fields. </p>
<p> Comments are started by the hash sign (#) and continue until the end of the line. Blank lines are skipped. </p>
<p> The <i>service-name</i> should begin in the first column of the file, since leading spaces are not stripped. <i>service-names</i> can be any printable characters excluding space and tab. However, a conservative choice of characters should be used to minimize compatibility problems. For example, a-z, 0-9, and hyphen (-) would seem a sensible choice. </p>
<p> Lines not matching this format should not be present in the file. (Currently, they are silently skipped by <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3), and <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3). However, this behavior should not be relied on.) </p>
<p> This file might be distributed over a network using a network-wide naming service like Yellow Pages/NIS or BIND/Hesiod. </p>
<p> A sample <code>services</code> file might look like this: </p>
<p> netstat 15/tcp qotd 17/tcp quote msp 18/tcp # message send protocol msp 18/udp # message send protocol chargen 19/tcp ttytst source chargen 19/udp ttytst source ftp 21/tcp # 22 &#8211; unassigned telnet 23/tcp</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/services</i></p>
<dd>The Internet network services list</p>
<dt><i>&lt;netdb.h&gt;</i></p>
<dd>Definition of <code>_PATH_SERVICES</code></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/3-endservent/">endservent</a></code>(3), <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3), <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3), <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), <code><a href="/docs/linux/man/3-setservent/">setservent</a></code>(3), <code><a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a></code>(5), <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) </p>
<p> Assigned Numbers RFC, most recently RFC 1700, (AKA STD0002).</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
