---
title: "getprotoent_r(3)"
name: "getprotoent_r"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getprotoent_r/"
description: "getprotoent_r, getprotobyname_r, getprotobynumber_r – get protocol entry (reentrant)"
---

<h2 class="name">NAME</h2>
<p> getprotoent_r, getprotobyname_r, getprotobynumber_r &#8211; get protocol entry (reentrant) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
int getprotoent_r(struct protoent *result_buf, char *buf,
                  size_t buflen, struct protoent **result);
int getprotobyname_r(const char *name,
                     struct protoent *result_buf, char *buf,
                     size_t buflen, struct protoent **result);
int getprotobynumber_r(int proto,
                       struct protoent *result_buf, char *buf,
                       size_t buflen, struct protoent **result);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getprotoent_r</code>(), <code>getprotobyname_r</code>(), <code>getprotobynumber_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getprotoent_r</code>(), <code>getprotobyname_r</code>(), and <code>getprotobynumber_r</code>() functions are the reentrant equivalents of, respectively, <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), <code><a href="/docs/linux/man/3-getprotobyname/">getprotobyname</a></code>(3), and <code><a href="/docs/linux/man/3-getprotobynumber/">getprotobynumber</a></code>(3). They differ in the way that the <i>protoent</i> structure is returned, and in the function calling signature and return value. This manual page describes just the differences from the nonreentrant functions. </p>
<p> Instead of returning a pointer to a statically allocated <i>protoent</i> structure as the function result, these functions copy the structure into the location pointed to by <i>result_buf</i>. </p>
<p> The <i>buf</i> array is used to store the string fields pointed to by the returned <i>protoent</i> structure. (The nonreentrant functions allocate these strings in static storage.) The size of this array is specified in <i>buflen</i>. If <i>buf</i> is too small, the call fails with the error <code>ERANGE</code>, and the caller must try again with a larger buffer. (A buffer of length 1024 bytes should be sufficient for most applications.) </p>
<p> If the function call successfully obtains a protocol record, then <i>*result</i> is set pointing to <i>result_buf</i>; otherwise, <i>*result</i> is set to NULL.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return 0. On error, they return one of the positive error numbers listed in ERRORS. </p>
<p> On error, record not found (<code>getprotobyname_r</code>(), <code>getprotobynumber_r</code>()), or end of input (<code>getprotoent_r</code>()) <i>result</i> is set to NULL.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd> (<code>getprotoent_r</code>()) No more records in database.</p>
<dt><code>ERANGE</code></p>
<dd> <i>buf</i> is too small. Try again with a larger buffer (and increased <i>buflen</i>).</dl>
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
<td> <code>getprotoent_r</code>(),<br />
 <code>getprotobyname_r</code>(),<br />
 <code>getprotobynumber_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions. Functions with similar names exist on some other systems, though typically with different calling signatures.</p>
<h2>EXAMPLES</h2>
<p> The program below uses <code>getprotobyname_r</code>() to retrieve the protocol record for the protocol named in its first command-line argument. If a second (integer) command-line argument is supplied, it is used as the initial value for <i>buflen</i>; if <code>getprotobyname_r</code>() fails with the error <code>ERANGE</code>, the program retries with larger buffer sizes. The following shell session shows a couple of sample runs: </p>
<p> $<code> ./a.out tcp 1</code> ERANGE! Retrying with larger buffer getprotobyname_r() returned: 0 (success) (buflen=78) p_name=tcp; p_proto=6; aliases=TCP $<code> ./a.out xxx 1</code> ERANGE! Retrying with larger buffer getprotobyname_r() returned: 0 (success) (buflen=100) Call failed/record not found</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;ctype.h&gt; #include &lt;netdb.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;errno.h&gt; #include &lt;string.h&gt; </p>
<p> #define MAX_BUF 10000 </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int buflen, erange_cnt, s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct protoent result_buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct protoent&nbsp;*result;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[MAX_BUF]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Usage:&nbsp;%s proto-name&nbsp;[buflen]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buflen&nbsp;=&nbsp;1024;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;2)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buflen&nbsp;=&nbsp;atoi(argv[2]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buflen&nbsp;&gt;&nbsp;MAX_BUF)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Exceeded buffer limit&nbsp;(%d)
&quot;, MAX_BUF);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erange_cnt&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;getprotobyname_r(argv[1],&nbsp;&amp;result_buf,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf, buflen,&nbsp;&amp;result);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;ERANGE)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(erange_cnt&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;ERANGE!&nbsp;Retrying with larger buffer
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erange_cnt++; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Increment a byte at a time so we can see exactly<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;what size buffer was required&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buflen++; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buflen&nbsp;&gt;&nbsp;MAX_BUF)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Exceeded buffer limit&nbsp;(%d)
&quot;, MAX_BUF);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(s&nbsp;==&nbsp;ERANGE); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;getprotobyname_r()&nbsp;returned:&nbsp;%s&nbsp;<wbr>&nbsp;(buflen=%d)
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(s&nbsp;==&nbsp;0)&nbsp;?&nbsp;&quot;0&nbsp;(success)&quot;&nbsp;:&nbsp;(s&nbsp;==&nbsp;ENOENT)&nbsp;?&nbsp;&quot;ENOENT&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(s), buflen); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;0 || result&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Call failed/record not found
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;p_name=%s;&nbsp;p_proto=%d;&nbsp;aliases=&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;result_buf.p_name, result_buf.p_proto);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(char&nbsp;**p&nbsp;=&nbsp;result_buf.p_aliases;&nbsp;*p&nbsp;!=&nbsp;NULL;&nbsp;p++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s&nbsp;&quot;,&nbsp;*p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
