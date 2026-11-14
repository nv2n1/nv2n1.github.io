---
title: "if_freenameindex(3)"
name: "if_freenameindex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-if_freenameindex/"
description: "if_nameindex, if_freenameindex – get network interface names and indexes"
---

<h2 class="name">NAME</h2>
<p> if_nameindex, if_freenameindex &#8211; get network interface names and indexes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;net/if.h&gt;
struct if_nameindex *if_nameindex(void);
void if_freenameindex(struct if_nameindex *ptr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>if_nameindex</code>() function returns an array of <i>if_nameindex</i> structures, each containing information about one of the network interfaces on the local system. The <i>if_nameindex</i> structure contains at least the following entries: </p>
<p> unsigned int if_index; /* Index of interface (1, 2, &#8230;) */ char *if_name; /* Null-terminated name (&quot;eth0&quot;, etc.) */ </p>
<p> The <i>if_index</i> field contains the interface index. The <i>if_name</i> field points to the null-terminated interface name. The end of the array is indicated by entry with <i>if_index</i> set to zero and <i>if_name</i> set to NULL. </p>
<p> The data structure returned by <code>if_nameindex</code>() is dynamically allocated and should be freed using <code>if_freenameindex</code>() when no longer needed.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>if_nameindex</code>() returns pointer to the array; on error, NULL is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> <code>if_nameindex</code>() may fail and set <i>errno</i> if:</p>
<dl>
<dt><code>ENOBUFS</code></p>
<dd> Insufficient resources available.</dl>
<p> <code>if_nameindex</code>() may also fail for any of the errors specified for <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), or <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> The <code>if_nameindex</code>() function first appeared in glibc 2.1, but before glibc 2.3.4, the implementation supported only interfaces with IPv4 addresses. Support of interfaces that don&#8217;t have IPv4 addresses is available only on kernels that support netlink.</p>
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
<td> <code>if_nameindex</code>(),<br />
 <code>if_freenameindex</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, RFC 3493. </p>
<p> This function first appeared in BSDi.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of the functions described on this page. An example of the output this program might produce is the following: </p>
<p> $ <code>./a.out</code><i> 1: lo 2: wlan0 3: em1 </i></p>
<h3>Program source</h3>
<p> #include &lt;net/if.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct if_nameindex&nbsp;*if_ni,&nbsp;*i; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if_ni&nbsp;=&nbsp;if_nameindex();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(if_ni&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;if_nameindex&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(i&nbsp;=&nbsp;if_ni;&nbsp;!&nbsp;(i-&gt;if_index&nbsp;==&nbsp;0&nbsp;&amp;&amp;&nbsp;i-&gt;if_name&nbsp;==&nbsp;NULL);&nbsp;i++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%u:&nbsp;%s
&quot;, i-&gt;if_index, i-&gt;if_name); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if_freenameindex(if_ni); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), <code><a href="/docs/linux/man/3-getifaddrs/">getifaddrs</a></code>(3), <code><a href="/docs/linux/man/3-if_indextoname/">if_indextoname</a></code>(3), <code><a href="/docs/linux/man/3-if_nametoindex/">if_nametoindex</a></code>(3), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
