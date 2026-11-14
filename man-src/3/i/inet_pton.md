---
title: "inet_pton(3)"
name: "inet_pton"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inet_pton/"
description: "inet_pton – convert IPv4 and IPv6 addresses from text to binary form"
---

<h2 class="name">NAME</h2>
<p> inet_pton &#8211; convert IPv4 and IPv6 addresses from text to binary form </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;arpa/inet.h&gt;
int inet_pton(int af, const char *src, void *dst);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function converts the character string <i>src</i> into a network address structure in the <i>af</i> address family, then copies the network address structure to <i>dst</i>. The <i>af</i> argument must be either <code>AF_INET</code> or <code>AF_INET6</code>. <i>dst</i> is written in network byte order. </p>
<p> The following address families are currently supported:</p>
<dl>
<dt><code>AF_INET</code></p>
<dd> <i>src</i> points to a character string containing an IPv4 network address in dotted-decimal format, &quot;<i>ddd.ddd.ddd.ddd</i>&quot;, where <i>ddd</i> is a decimal number of up to three digits in the range 0 to 255. The address is converted to a <i>struct in_addr</i> and copied to <i>dst</i>, which must be <i>sizeof(struct in_addr)</i> (4) bytes (32 bits) long.</p>
<dt><code>AF_INET6</code></p>
<dd> <i>src</i> points to a character string containing an IPv6 network address. The address is converted to a <i>struct in6_addr</i> and copied to <i>dst</i>, which must be <i>sizeof(struct in6_addr)</i> (16) bytes (128 bits) long. The allowed formats for IPv6 addresses follow these rules:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> The preferred format is <i>x:x:x:x:x:x:x:x</i>. This form consists of eight hexadecimal numbers, each of which expresses a 16-bit value (i.e., each <i>x</i> can be up to 4 hex digits).</p>
<dt>2.</p>
<dd> A series of contiguous zero values in the preferred format can be abbreviated to <i>::</i>. Only one instance of <i>::</i> can occur in an address. For example, the loopback address <i>0:0:0:0:0:0:0:1</i> can be abbreviated as <i>::1</i>. The wildcard address, consisting of all zeros, can be written as <i>::</i>.</p>
<dt>3.</p>
<dd> An alternate format is useful for expressing IPv4-mapped IPv6 addresses. This form is written as <i>x:x:x:x:x:x:d.d.d.d</i>, where the six leading <i>x</i>s are hexadecimal values that define the six most-significant 16-bit pieces of the address (i.e., 96 bits), and the <i>d</i>s express a value in dotted-decimal notation that defines the least significant 32 bits of the address. An example of such an address is <i>::FFFF:204.152.189.116</i>.</dl>
</dl>
<dt>
<dd> See RFC 2373 for further details on the representation of IPv6 addresses.</dl>
<h2>RETURN VALUE</h2>
<p> <code>inet_pton</code>() returns 1 on success (network address was successfully converted). 0 is returned if <i>src</i> does not contain a character string representing a valid network address in the specified address family. If <i>af</i> does not contain a valid address family, -1 is returned and <i>errno</i> is set to <code>EAFNOSUPPORT</code>.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>inet_pton</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Unlike <code><a href="/docs/linux/man/3-inet_aton/">inet_aton</a></code>(3) and <code><a href="/docs/linux/man/3-inet_addr/">inet_addr</a></code>(3), <code>inet_pton</code>() supports IPv6 addresses. On the other hand, <code>inet_pton</code>() accepts only IPv4 addresses in dotted-decimal notation, whereas <code><a href="/docs/linux/man/3-inet_aton/">inet_aton</a></code>(3) and <code><a href="/docs/linux/man/3-inet_addr/">inet_addr</a></code>(3) allow the more general numbers-and-dots notation (hexadecimal and octal number formats, and formats that don&#8217;t require all four bytes to be explicitly written). For an interface that handles both IPv6 addresses, and IPv4 addresses in numbers-and-dots notation, see <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<h2>BUGS</h2>
<p> <code>AF_INET6</code> does not recognize IPv4 addresses. An explicit IPv4-mapped IPv6 address must be supplied in <i>src</i> instead.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>inet_pton</code>() and <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3). Here are some example runs: </p>
<p> $<code> ./a.out i6 0:0:0:0:0:0:0:0</code> :: $<code> ./a.out i6 1:0:0:0:0:0:0:8</code> 1::8 $<code> ./a.out i6 0:0:0:0:0:FFFF:204.152.189.116</code> ::ffff:204.152.189.116</p>
<h3>Program source</h3>
<p> #include &lt;arpa/inet.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char buf[sizeof(struct in6_addr)];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int domain, s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char str[INET6_ADDRSTRLEN]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;{i4|i6|&lt;num&gt;}&nbsp;string
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;domain&nbsp;=&nbsp;(strcmp(argv[1],&nbsp;&quot;i4&quot;)&nbsp;==&nbsp;0)&nbsp;?&nbsp;AF_INET :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(strcmp(argv[1],&nbsp;&quot;i6&quot;)&nbsp;==&nbsp;0)&nbsp;?&nbsp;AF_INET6 : atoi(argv[1]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;inet_pton(domain, argv[2], buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;&lt;=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Not in presentation format&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;inet_pton&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(inet_ntop(domain, buf, str, INET6_ADDRSTRLEN)&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;inet_ntop&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, str); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-inet/">inet</a></code>(3), <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
