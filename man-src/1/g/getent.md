---
title: "getent(1)"
name: "getent"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getent/"
description: "getent – get entries from Name Service Switch libraries"
---

<h2 class="name">NAME</h2>
<p> getent &#8211; get entries from Name Service Switch libraries </p>
<h2>SYNOPSIS</h2>
<p> <code>getent&nbsp;[</code><i>option</i>]&#8230;&nbsp;<i>database</i>&nbsp;<i>key</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>getent</code> command displays entries from databases supported by the Name Service Switch libraries, which are configured in <i>/etc/nsswitch.conf</i>. If one or more <i>key</i> arguments are provided, then only the entries that match the supplied keys will be displayed. Otherwise, if no <i>key</i> is provided, all entries will be displayed (unless the database does not support enumeration). </p>
<p> The <i>database</i> may be any of those supported by the GNU C Library, listed below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ahosts</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-sethostent/">sethostent</a></code>(3), <code><a href="/docs/linux/man/3-gethostent/">gethostent</a></code>(3), and <code><a href="/docs/linux/man/3-endhostent/">endhostent</a></code>(3) to enumerate the hosts database. This is identical to using <code>hosts</code>. When one or more <i>key</i> arguments are provided, pass each <i>key</i> in succession to <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) with the address family <code>AF_UNSPEC</code>, enumerating each socket address structure returned.</p>
<dt><code>ahostsv4</code></p>
<dd> Same as <code>ahosts</code>, but use the address family <code>AF_INET</code>.</p>
<dt><code>ahostsv6</code></p>
<dd> Same as <code>ahosts</code>, but use the address family <code>AF_INET6</code>. The call to <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) in this case includes the <code>AI_V4MAPPED</code> flag.</p>
<dt><code>aliases</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setaliasent/">setaliasent</a></code>(3), <code><a href="/docs/linux/man/3-getaliasent/">getaliasent</a></code>(3), and <code><a href="/docs/linux/man/3-endaliasent/">endaliasent</a></code>(3) to enumerate the aliases database. When one or more <i>key</i> arguments are provided, pass each <i>key</i> in succession to <code><a href="/docs/linux/man/3-getaliasbyname/">getaliasbyname</a></code>(3) and display the result.</p>
<dt><code>ethers</code></p>
<dd> When one or more <i>key</i> arguments are provided, pass each <i>key</i> in succession to <code><a href="/docs/linux/man/3-ether_aton/">ether_aton</a></code>(3) and <code><a href="/docs/linux/man/3-ether_hostton/">ether_hostton</a></code>(3) until a result is obtained, and display the result. Enumeration is not supported on <code>ethers</code>, so a <i>key</i> must be provided.</p>
<dt><code>group</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setgrent/">setgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), and <code><a href="/docs/linux/man/3-endgrent/">endgrent</a></code>(3) to enumerate the group database. When one or more <i>key</i> arguments are provided, pass each numeric <i>key</i> to <code><a href="/docs/linux/man/3-getgrgid/">getgrgid</a></code>(3) and each nonnumeric <i>key</i> to <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3) and display the result.</p>
<dt><code>gshadow</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setsgent/">setsgent</a></code>(3), <code><a href="/docs/linux/man/3-getsgent/">getsgent</a></code>(3), and <code><a href="/docs/linux/man/3-endsgent/">endsgent</a></code>(3) to enumerate the gshadow database. When one or more <i>key</i> arguments are provided, pass each <i>key</i> in succession to <code><a href="/docs/linux/man/3-getsgnam/">getsgnam</a></code>(3) and display the result.</p>
<dt><code>hosts</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-sethostent/">sethostent</a></code>(3), <code><a href="/docs/linux/man/3-gethostent/">gethostent</a></code>(3), and <code><a href="/docs/linux/man/3-endhostent/">endhostent</a></code>(3) to enumerate the hosts database. When one or more <i>key</i> arguments are provided, pass each <i>key</i> to <code><a href="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a></code>(3) or <code><a href="/docs/linux/man/3-gethostbyname2/">gethostbyname2</a></code>(3), depending on whether a call to <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3) indicates that the <i>key</i> is an IPv6 or IPv4 address or not, and display the result.</p>
<dt><code>initgroups</code></p>
<dd> When one or more <i>key</i> arguments are provided, pass each <i>key</i> in succession to <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3) and display the result. Enumeration is not supported on <code>initgroups</code>, so a <i>key</i> must be provided.</p>
<dt><code>netgroup</code></p>
<dd> When one <i>key</i> is provided, pass the <i>key</i> to <code><a href="/docs/linux/man/3-setnetgrent/">setnetgrent</a></code>(3) and, using <code><a href="/docs/linux/man/3-getnetgrent/">getnetgrent</a></code>(3) display the resulting string triple (<i>hostname</i>, <i>username</i>, <i>domainname</i>). Alternatively, three <i>keys</i> may be provided, which are interpreted as the <i>hostname</i>, <i>username</i>, and <i>domainname</i> to match to a netgroup name via <code><a href="/docs/linux/man/3-innetgr/">innetgr</a></code>(3). Enumeration is not supported on <code>netgroup</code>, so either one or three <i>keys</i> must be provided.</p>
<dt><code>networks</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setnetent/">setnetent</a></code>(3), <code><a href="/docs/linux/man/3-getnetent/">getnetent</a></code>(3), and <code><a href="/docs/linux/man/3-endnetent/">endnetent</a></code>(3) to enumerate the networks database. When one or more <i>key</i> arguments are provided, pass each numeric <i>key</i> to <code><a href="/docs/linux/man/3-getnetbyaddr/">getnetbyaddr</a></code>(3) and each nonnumeric <i>key</i> to <code><a href="/docs/linux/man/3-getnetbyname/">getnetbyname</a></code>(3) and display the result.</p>
<dt><code>passwd</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setpwent/">setpwent</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), and <code><a href="/docs/linux/man/3-endpwent/">endpwent</a></code>(3) to enumerate the passwd database. When one or more <i>key</i> arguments are provided, pass each numeric <i>key</i> to <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3) and each nonnumeric <i>key</i> to <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3) and display the result.</p>
<dt><code>protocols</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setprotoent/">setprotoent</a></code>(3), <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), and <code><a href="/docs/linux/man/3-endprotoent/">endprotoent</a></code>(3) to enumerate the protocols database. When one or more <i>key</i> arguments are provided, pass each numeric <i>key</i> to <code><a href="/docs/linux/man/3-getprotobynumber/">getprotobynumber</a></code>(3) and each nonnumeric <i>key</i> to <code><a href="/docs/linux/man/3-getprotobyname/">getprotobyname</a></code>(3) and display the result.</p>
<dt><code>rpc</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setrpcent/">setrpcent</a></code>(3), <code><a href="/docs/linux/man/3-getrpcent/">getrpcent</a></code>(3), and <code><a href="/docs/linux/man/3-endrpcent/">endrpcent</a></code>(3) to enumerate the rpc database. When one or more <i>key</i> arguments are provided, pass each numeric <i>key</i> to <code><a href="/docs/linux/man/3-getrpcbynumber/">getrpcbynumber</a></code>(3) and each nonnumeric <i>key</i> to <code><a href="/docs/linux/man/3-getrpcbyname/">getrpcbyname</a></code>(3) and display the result.</p>
<dt><code>services</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setservent/">setservent</a></code>(3), <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), and <code><a href="/docs/linux/man/3-endservent/">endservent</a></code>(3) to enumerate the services database. When one or more <i>key</i> arguments are provided, pass each numeric <i>key</i> to <code><a href="/docs/linux/man/3-getservbynumber/">getservbynumber</a></code>(3) and each nonnumeric <i>key</i> to <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3) and display the result.</p>
<dt><code>shadow</code></p>
<dd> When no <i>key</i> is provided, use <code><a href="/docs/linux/man/3-setspent/">setspent</a></code>(3), <code><a href="/docs/linux/man/3-getspent/">getspent</a></code>(3), and <code><a href="/docs/linux/man/3-endspent/">endspent</a></code>(3) to enumerate the shadow database. When one or more <i>key</i> arguments are provided, pass each <i>key</i> in succession to <code><a href="/docs/linux/man/3-getspnam/">getspnam</a></code>(3) and display the result.</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s&nbsp;</code><i>service</i>, <code>&#8211;service&nbsp;</code><i>service</i></p>
<dd> Override all databases with the specified service. (Since glibc 2.2.5.)</p>
<dt><code>-s&nbsp;</code><i>database</i>:<i>service</i>, &#8211;service&nbsp;<i>database</i>:<i>service</i></p>
<dd> Override only specified databases with the specified service. The option may be used multiple times, but only the last service for each database will be used. (Since glibc 2.4.)</p>
<dt><code>-i</code>, <code>&#8211;no-idn</code></p>
<dd> Disables IDN encoding in lookups for <code>ahosts</code>/<code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) (Since glibc-2.13.)</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a usage summary and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage summary and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number, license, and disclaimer of warranty for <code>getent</code>.</dl>
<h2>EXIT STATUS</h2>
<p> One of the following exit values can be returned by <code>getent</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Command completed successfully.</p>
<dt><code>1</code></p>
<dd> Missing arguments, or <i>database</i> unknown.</p>
<dt><code>2</code></p>
<dd> One or more supplied <i>key</i> could not be found in the <i>database</i>.</p>
<dt><code>3</code></p>
<dd> Enumeration not supported on this <i>database</i>.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
