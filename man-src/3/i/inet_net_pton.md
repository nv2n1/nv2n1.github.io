---
title: "inet_net_pton(3)"
name: "inet_net_pton"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inet_net_pton/"
description: "inet_net_pton, inet_net_ntop – Internet network number conversion"
---

<h2 class="name">NAME</h2>
<p> inet_net_pton, inet_net_ntop &#8211; Internet network number conversion </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;arpa/inet.h&gt;
int inet_net_pton(int af, const char *pres,
                  void *netp, size_t nsize);
char *inet_net_ntop(int af, const void *netp, int bits,
                    char *pres, size_t psize);
</code></pre>
<p> Link with <i>-lresolv</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>inet_net_pton</code>(), <code>inet_net_ntop</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.20:</p>
<dd> _DEFAULT_SOURCE</p>
<dt>Before glibc 2.20:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> These functions convert network numbers between presentation (i.e., printable) format and network (i.e., binary) format. </p>
<p> For both functions, <i>af</i> specifies the address family for the conversion; the only supported value is <code>AF_INET</code>.</p>
<h3>inet_net_pton()</h3>
<p> The <code>inet_net_pton</code>() function converts <i>pres</i>, a null-terminated string containing an Internet network number in presentation format to network format. The result of the conversion, which is in network byte order, is placed in the buffer pointed to by <i>net</i>. (The <i>netp</i> argument typically points to an <i>in_addr</i> structure.) The <i>nsize</i> argument specifies the number of bytes available in <i>netp</i>. </p>
<p> On success, <code>inet_net_pton</code>() returns the number of bits in the network number field of the result placed in <i>netp</i>. For a discussion of the input presentation format and the return value, see NOTES. </p>
<p> <i>Note</i>: the buffer pointed to by <i>netp</i> should be zeroed out before calling <code>inet_net_pton</code>(), since the call writes only as many bytes as are required for the network number (or as are explicitly specified by <i>pres</i>), which may be less than the number of bytes in a complete network address.</p>
<h3>inet_net_ntop()</h3>
<p> The <code>inet_net_ntop</code>() function converts the network number in the buffer pointed to by <i>netp</i> to presentation format; <i>*netp</i> is interpreted as a value in network byte order. The <i>bits</i> argument specifies the number of bits in the network number in <i>*netp</i>. </p>
<p> The null-terminated presentation-format string is placed in the buffer pointed to by <i>pres</i>. The <i>psize</i> argument specifies the number of bytes available in <i>pres</i>. The presentation string is in CIDR format: a dotted-decimal number representing the network address, followed by a slash, and the size of the network number in bits.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>inet_net_pton</code>() returns the number of bits in the network number. On error, it returns -1, and <i>errno</i> is set to indicate the cause of the error. </p>
<p> On success, <code>inet_net_ntop</code>() returns <i>pres</i>. On error, it returns NULL, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAFNOSUPPORT</code></p>
<dd> <i>af</i> specified a value other than <code>AF_INET</code>.</p>
<dt><code>EMSGSIZE</code></p>
<dd> The size of the output buffer was insufficient.</p>
<dt><code>ENOENT</code></p>
<dd> (<code>inet_net_pton</code>()) <i>pres</i> was not in correct presentation format.</dl>
<h2>CONFORMING TO</h2>
<p> The <code>inet_net_pton</code>() and <code>inet_net_ntop</code>() functions are nonstandard, but widely available.</p>
<h2>NOTES</h2>
<h3>Input presentation format for inet_net_pton()</h3>
<p> The network number may be specified either as a hexadecimal value or in dotted-decimal notation. </p>
<p> Hexadecimal values are indicated by an initial &quot;0x&quot; or &quot;0X&quot;. The hexadecimal digits populate the nibbles (half octets) of the network number from left to right in network byte order. </p>
<p> In dotted-decimal notation, up to four octets are specified, as decimal numbers separated by dots. Thus, any of the following forms are accepted: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a.b.c.d<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a.b.c<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a.b<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a </p>
<p> Each part is a number in the range 0 to 255 that populates one byte of the resulting network number, going from left to right, in network-byte (big endian) order. Where a part is omitted, the resulting byte in the network number is zero. </p>
<p> For either hexadecimal or dotted-decimal format, the network number can optionally be followed by a slash and a number in the range 0 to 32, which specifies the size of the network number in bits.</p>
<h3>Return value of inet_net_pton()</h3>
<p> The return value of <code>inet_net_pton</code>() is the number of bits in the network number field. If the input presentation string terminates with a slash and an explicit size value, then that size becomes the return value of <code>inet_net_pton</code>(). Otherwise, the return value, <i>bits</i>, is inferred as follows:</p>
<dl>
<dt>*</p>
<dd> If the most significant byte of the network number is greater than or equal to 240, then <i>bits</i> is 32.</p>
<dt>*</p>
<dd> Otherwise, if the most significant byte of the network number is greater than or equal to 224, then <i>bits</i> is 4.</p>
<dt>*</p>
<dd> Otherwise, if the most significant byte of the network number is greater than or equal to 192, then <i>bits</i> is 24.</p>
<dt>*</p>
<dd> Otherwise, if the most significant byte of the network number is greater than or equal to 128, then <i>bits</i> is 16.</p>
<dt>*</p>
<dd> Otherwise, <i>bits</i> is 8.</dl>
<p> If the resulting <i>bits</i> value from the above steps is greater than or equal to 8, but the number of octets specified in the network number exceed <i>bits/8</i>, then <i>bits</i> is set to 8 times the number of octets actually specified.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>inet_net_pton</code>() and <code>inet_net_ntop</code>(). It uses <code>inet_net_pton</code>() to convert the presentation format network address provided in its first command-line argument to binary form, displays the return value from <code>inet_net_pton</code>(). It then uses <code>inet_net_ntop</code>() to convert the binary form back to presentation format, and displays the resulting string. </p>
<p> In order to demonstrate that <code>inet_net_pton</code>() may not write to all bytes of its <i>netp</i> argument, the program allows an optional second command-line argument, a number used to initialize the buffer before <code>inet_net_pton</code>() is called. As its final line of output, the program displays all of the bytes of the buffer returned by <code>inet_net_pton</code>() allowing the user to see which bytes have not been touched by <code>inet_net_pton</code>(). </p>
<p> An example run, showing that <code>inet_net_pton</code>() infers the number of bits in the network number: </p>
<p> $ <code>./a.out 193.168</code> inet_net_pton() returned: 24 inet_net_ntop() yielded: 193.168.0/24 Raw address: c1a80000 </p>
<p> Demonstrate that <code>inet_net_pton</code>() does not zero out unused bytes in its result buffer: </p>
<p> $ <code>./a.out 193.168 0xffffffff</code> inet_net_pton() returned: 24 inet_net_ntop() yielded: 193.168.0/24 Raw address: c1a800ff </p>
<p> Demonstrate that <code>inet_net_pton</code>() will widen the inferred size of the network number, if the supplied number of bytes in the presentation string exceeds the inferred value: </p>
<p> $ <code>./a.out 193.168.1.128</code> inet_net_pton() returned: 32 inet_net_ntop() yielded: 193.168.1.128/32 Raw address: c1a80180 </p>
<p> Explicitly specifying the size of the network number overrides any inference about its size (but any extra bytes that are explicitly specified will still be used by <code>inet_net_pton</code>(): to populate the result buffer): </p>
<p> $ <code>./a.out 193.168.1.128/24</code> inet_net_pton() returned: 24 inet_net_ntop() yielded: 193.168.1/24 Raw address: c1a80180</p>
<h3>Program source</h3>
<p> /* Link with &quot;-lresolv&quot; */ </p>
<p> #include &lt;arpa/inet.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[100];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bits; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;Usage:&nbsp;%s presentation-form&nbsp;[addr-init-value]
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If argv[2]&nbsp;is supplied&nbsp;(a numeric value), use it to initialize<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the output buffer given to inet_net_pton(), so that we can see<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;that inet_net_pton()&nbsp;initializes only those bytes needed for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the network number. If argv[2]&nbsp;is not supplied, then initialize<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the buffer to zero&nbsp;(as is recommended practice).&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.s_addr&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;2)&nbsp;?&nbsp;strtod(argv[2], NULL)&nbsp;: 0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Convert presentation network number in argv[1]&nbsp;to binary&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bits&nbsp;=&nbsp;inet_net_pton(AF_INET, argv[1],&nbsp;&amp;addr, sizeof(addr));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(bits&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;inet_net_ntop&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;inet_net_pton()&nbsp;returned:&nbsp;%d
&quot;, bits); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Convert binary format back to presentation, using&nbsp;&#8216;bits&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returned by inet_net_pton()&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(inet_net_ntop(AF_INET,&nbsp;&amp;addr, bits, buf, sizeof(buf))&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;inet_net_ntop&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;inet_net_ntop()&nbsp;yielded:&nbsp;<wbr>&nbsp;%s
&quot;, buf); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display&nbsp;&#8216;addr&#8217;&nbsp;in raw form&nbsp;(in network byte order), so we can<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;see bytes not displayed by inet_net_ntop();&nbsp;some of those bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;may not have been touched by inet_net_ntop(), and so will still<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;have any initial value that was specified in argv[2].&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Raw address:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%x
&quot;, htonl(addr.s_addr)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-inet/">inet</a></code>(3), <code><a href="/docs/linux/man/5-networks/">networks</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
