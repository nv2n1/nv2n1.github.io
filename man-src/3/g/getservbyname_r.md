---
title: "getservbyname_r(3)"
name: "getservbyname_r"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getservbyname_r/"
description: "getservent_r, getservbyname_r, getservbyport_r – get service entry (reentrant)"
---

<h2 class="name">NAME</h2>
<p> getservent_r, getservbyname_r, getservbyport_r &#8211; get service entry (reentrant) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
int getservent_r(struct servent *result_buf, char *buf,
                 size_t buflen, struct servent **result);
int getservbyname_r(const char *name, const char *proto,
                    struct servent *result_buf, char *buf,
                    size_t buflen, struct servent **result);
int getservbyport_r(int port, const char *proto,
                    struct servent *result_buf, char *buf,
                    size_t buflen, struct servent **result);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getservent_r</code>(), <code>getservbyname_r</code>(), <code>getservbyport_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getservent_r</code>(), <code>getservbyname_r</code>(), and <code>getservbyport_r</code>() functions are the reentrant equivalents of, respectively, <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3), and <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3). They differ in the way that the <i>servent</i> structure is returned, and in the function calling signature and return value. This manual page describes just the differences from the nonreentrant functions. </p>
<p> Instead of returning a pointer to a statically allocated <i>servent</i> structure as the function result, these functions copy the structure into the location pointed to by <i>result_buf</i>. </p>
<p> The <i>buf</i> array is used to store the string fields pointed to by the returned <i>servent</i> structure. (The nonreentrant functions allocate these strings in static storage.) The size of this array is specified in <i>buflen</i>. If <i>buf</i> is too small, the call fails with the error <code>ERANGE</code>, and the caller must try again with a larger buffer. (A buffer of length 1024 bytes should be sufficient for most applications.) </p>
<p> If the function call successfully obtains a service record, then <i>*result</i> is set pointing to <i>result_buf</i>; otherwise, <i>*result</i> is set to NULL.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return 0. On error, they return one of the positive error numbers listed in errors. </p>
<p> On error, record not found (<code>getservbyname_r</code>(), <code>getservbyport_r</code>()), or end of input (<code>getservent_r</code>()) <i>result</i> is set to NULL.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd> (<code>getservent_r</code>()) No more records in database.</p>
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
<td> <code>getservent_r</code>(), <code>getservbyname_r</code>(), <code>getservbyport_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions. Functions with similar names exist on some other systems, though typically with different calling signatures.</p>
<h2>EXAMPLES</h2>
<p> The program below uses <code>getservbyport_r</code>() to retrieve the service record for the port and protocol named in its first command-line argument. If a third (integer) command-line argument is supplied, it is used as the initial value for <i>buflen</i>; if <code>getservbyport_r</code>() fails with the error <code>ERANGE</code>, the program retries with larger buffer sizes. The following shell session shows a couple of sample runs: </p>
<p> $<code> ./a.out 7 tcp 1</code> ERANGE! Retrying with larger buffer getservbyport_r() returned: 0 (success) (buflen=87) s_name=echo; s_proto=tcp; s_port=7; aliases= $<code> ./a.out 77777 tcp</code> getservbyport_r() returned: 0 (success) (buflen=1024) Call failed/record not found</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;ctype.h&gt; #include &lt;netdb.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;errno.h&gt; #include &lt;string.h&gt; </p>
<p> #define MAX_BUF 10000 </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int buflen, erange_cnt, port, s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct servent result_buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct servent&nbsp;*result;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[MAX_BUF];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*protop; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Usage:&nbsp;%s port-num proto-name&nbsp;[buflen]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;port&nbsp;=&nbsp;htons(atoi(argv[1]));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;protop&nbsp;=&nbsp;(strcmp(argv[2],&nbsp;&quot;null&quot;)&nbsp;==&nbsp;0 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strcmp(argv[2],&nbsp;&quot;NULL&quot;)&nbsp;==&nbsp;0)&nbsp;?&nbsp;<wbr>&nbsp;NULL : argv[2]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buflen&nbsp;=&nbsp;1024;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;3)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buflen&nbsp;=&nbsp;atoi(argv[3]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buflen&nbsp;&gt;&nbsp;MAX_BUF)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Exceeded buffer limit&nbsp;(%d)
&quot;, MAX_BUF);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erange_cnt&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;getservbyport_r(port, protop,&nbsp;&amp;result_buf,<br />
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
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;getservbyport_r()&nbsp;returned:&nbsp;%s&nbsp;<wbr>&nbsp;(buflen=%d)
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(s&nbsp;==&nbsp;0)&nbsp;?&nbsp;&quot;0&nbsp;(success)&quot;&nbsp;:&nbsp;(s&nbsp;==&nbsp;ENOENT)&nbsp;?&nbsp;&quot;ENOENT&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(s), buflen); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;0 || result&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Call failed/record not found
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;s_name=%s;&nbsp;s_proto=%s;&nbsp;s_port=%d;&nbsp;aliases=&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;result_buf.s_name, result_buf.s_proto,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ntohs(result_buf.s_port));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(char&nbsp;**p&nbsp;=&nbsp;result_buf.s_aliases;&nbsp;*p&nbsp;!=&nbsp;NULL;&nbsp;p++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s&nbsp;&quot;,&nbsp;*p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), <code><a href="/docs/linux/man/5-services/">services</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
