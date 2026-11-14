---
title: "getipnodebyname(3)"
name: "getipnodebyname"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getipnodebyname/"
description: "getipnodebyname, getipnodebyaddr, freehostent – get network hostnames and addresses"
---

<h2 class="name">NAME</h2>
<p> getipnodebyname, getipnodebyaddr, freehostent &#8211; get network hostnames and addresses </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;
struct hostent *getipnodebyname(const char *name, int af,
                                int flags, int *error_num);
struct hostent *getipnodebyaddr(const void *addr, size_t len,
                                int af, int *error_num);
void freehostent(struct hostent *ip);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions are deprecated (and unavailable in glibc). Use <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) and <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3) instead. </p>
<p> The <code>getipnodebyname</code>() and <code>getipnodebyaddr</code>() functions return the names and addresses of a network host. These functions return a pointer to the following structure: </p>
<p> struct hostent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;*h_name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**h_aliases;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h_addrtype;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h_length;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**h_addr_list; }; </p>
<p> These functions replace the <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) and <code><a href="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a></code>(3) functions, which could access only the IPv4 network address family. The <code>getipnodebyname</code>() and <code>getipnodebyaddr</code>() functions can access multiple network address families. </p>
<p> Unlike the <code>gethostby</code> functions, these functions return pointers to dynamically allocated memory. The <code>freehostent</code>() function is used to release the dynamically allocated memory after the caller no longer needs the <i>hostent</i> structure.</p>
<h3>getipnodebyname() arguments</h3>
<p> The <code>getipnodebyname</code>() function looks up network addresses for the host specified by the <i>name</i> argument. The <i>af</i> argument specifies one of the following values:</p>
<dl>
<dt><code>AF_INET</code></p>
<dd> The <i>name</i> argument points to a dotted-quad IPv4 address or a name of an IPv4 network host.</p>
<dt><code>AF_INET6</code></p>
<dd> The <i>name</i> argument points to a hexadecimal IPv6 address or a name of an IPv6 network host.</dl>
<p> The <i>flags</i> argument specifies additional options. More than one option can be specified by bitwise OR-ing them together. <i>flags</i> should be set to 0 if no options are desired.</p>
<dl>
<dt><code>AI_V4MAPPED</code></p>
<dd> This flag is used with <code>AF_INET6</code> to request a query for IPv4 addresses instead of IPv6 addresses; the IPv4 addresses will be mapped to IPv6 addresses.</p>
<dt><code>AI_ALL</code></p>
<dd> This flag is used with <code>AI_V4MAPPED</code> to request a query for both IPv4 and IPv6 addresses. Any IPv4 address found will be mapped to an IPv6 address.</p>
<dt><code>AI_ADDRCONFIG</code></p>
<dd> This flag is used with <code>AF_INET6</code> to further request that queries for IPv6 addresses should not be made unless the system has at least one IPv6 address assigned to a network interface, and that queries for IPv4 addresses should not be made unless the system has at least one IPv4 address assigned to a network interface. This flag may be used by itself or with the <code>AI_V4MAPPED</code> flag.</p>
<dt><code>AI_DEFAULT</code></p>
<dd> This flag is equivalent to <code>(AI_ADDRCONFIG | AI_V4MAPPED)</code>.</dl>
<h3>getipnodebyaddr() arguments</h3>
<p> The <code>getipnodebyaddr</code>() function looks up the name of the host whose network address is specified by the <i>addr</i> argument. The <i>af</i> argument specifies one of the following values:</p>
<dl>
<dt><code>AF_INET</code></p>
<dd> The <i>addr</i> argument points to a <i>struct in_addr</i> and <i>len</i> must be set to <i>sizeof(struct in_addr)</i>.</p>
<dt><code>AF_INET6</code></p>
<dd> The <i>addr</i> argument points to a <i>struct in6_addr</i> and <i>len</i> must be set to <i>sizeof(struct in6_addr)</i>.</dl>
<h2>RETURN VALUE</h2>
<p> NULL is returned if an error occurred, and <i>error_num</i> will contain an error code from the following list:</p>
<dl>
<dt><code>HOST_NOT_FOUND</code></p>
<dd> The hostname or network address was not found.</p>
<dt><code>NO_ADDRESS</code></p>
<dd> The domain name server recognized the network address or name, but no answer was returned. This can happen if the network host has only IPv4 addresses and a request has been made for IPv6 information only, or vice versa.</p>
<dt><code>NO_RECOVERY</code></p>
<dd> The domain name server returned a permanent failure response.</p>
<dt><code>TRY_AGAIN</code></p>
<dd> The domain name server returned a temporary failure response. You might have better luck next time.</dl>
<p> A successful query returns a pointer to a <i>hostent</i> structure that contains the following fields:</p>
<dl>
<dt><i>h_name</i></p>
<dd> This is the official name of this network host.</p>
<dt><i>h_aliases</i></p>
<dd> This is an array of pointers to unofficial aliases for the same host. The array is terminated by a null pointer.</p>
<dt><i>h_addrtype</i></p>
<dd> This is a copy of the <i>af</i> argument to <code>getipnodebyname</code>() or <code>getipnodebyaddr</code>(). <i>h_addrtype</i> will always be <code>AF_INET</code> if the <i>af</i> argument was <code>AF_INET</code>. <i>h_addrtype</i> will always be <code>AF_INET6</code> if the <i>af</i> argument was <code>AF_INET6</code>.</p>
<dt><i>h_length</i></p>
<dd> This field will be set to <i>sizeof(struct in_addr)</i> if <i>h_addrtype</i> is <code>AF_INET</code>, and to <i>sizeof(struct in6_addr)</i> if <i>h_addrtype</i> is <code>AF_INET6</code>.</p>
<dt><i>h_addr_list</i></p>
<dd> This is an array of one or more pointers to network address structures for the network host. The array is terminated by a null pointer.</dl>
<h2>CONFORMING TO</h2>
<p> RFC 2553.</p>
<h2>NOTES</h2>
<p> These functions were present in glibc 2.1.91-95, but were removed again. Several UNIX-like systems support them, but all call them deprecated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3), <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
