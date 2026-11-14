---
title: "fgetgrent_r(3)"
name: "fgetgrent_r"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetgrent_r/"
description: "getgrent_r, fgetgrent_r – get group file entry reentrantly"
---

<h2 class="name">NAME</h2>
<p> getgrent_r, fgetgrent_r &#8211; get group file entry reentrantly </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;grp.h&gt;
int getgrent_r(struct group *gbuf, char *buf,
               size_t buflen, struct group **gbufp);
int fgetgrent_r(FILE *stream, struct group *gbuf, char *buf,
                size_t buflen, struct group **gbufp);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getgrent_r</code>(): _GNU_SOURCE<br />
 <code>fgetgrent_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The functions <code>getgrent_r</code>() and <code>fgetgrent_r</code>() are the reentrant versions of <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) and <code><a href="/docs/linux/man/3-fgetgrent/">fgetgrent</a></code>(3). The former reads the next group entry from the stream initialized by <code><a href="/docs/linux/man/3-setgrent/">setgrent</a></code>(3). The latter reads the next group entry from <i>stream</i>. </p>
<p> The <i>group</i> structure is defined in <i>&lt;grp.h&gt;</i> as follows: </p>
<p> struct group {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;gr_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;**gr_mem;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;NULL-terminated array of pointers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to names of group members&nbsp;*/ }; </p>
<p> For more information about the fields of this structure, see <code><a href="/docs/linux/man/5-group/">group</a></code>(5). </p>
<p> The nonreentrant functions return a pointer to static storage, where this static storage contains further pointers to group name, password and members. The reentrant functions described here return all of that in caller-provided buffers. First of all there is the buffer <i>gbuf</i> that can hold a <i>struct group</i>. And next the buffer <i>buf</i> of size <i>buflen</i> that can hold additional strings. The result of these functions, the <i>struct group</i> read from the stream, is stored in the provided buffer <i>*gbuf</i>, and a pointer to this <i>struct group</i> is returned in <i>*gbufp</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return 0 and <i>*gbufp</i> is a pointer to the <i>struct group</i>. On error, these functions return an error value and <i>*gbufp</i> is NULL.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd> No more entries.</p>
<dt><code>ERANGE</code></p>
<dd> Insufficient buffer space supplied. Try again with larger buffer.</dl>
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
<td> <code>getgrent_r</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:grent locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>fgetgrent_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<p> In the above table, <i>grent</i> in <i>race:grent</i> signifies that if any of the functions <code><a href="/docs/linux/man/3-setgrent/">setgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-endgrent/">endgrent</a></code>(3), or <code>getgrent_r</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions, done in a style resembling the POSIX version of functions like <code><a href="/docs/linux/man/3-getpwnam_r/">getpwnam_r</a></code>(3). Other systems use the prototype </p>
<p> struct group *getgrent_r(struct group *grp, char *buf,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int buflen); </p>
<p> or, better, </p>
<p> int getgrent_r(struct group *grp, char *buf, int buflen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;**gr_fp);</p>
<h2>NOTES</h2>
<p> The function <code>getgrent_r</code>() is not really reentrant since it shares the reading position in the stream with all other threads.</p>
<h2>EXAMPLES</h2>
<p> #define _GNU_SOURCE #include &lt;grp.h&gt; #include &lt;stdio.h&gt; #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #define BUFLEN 4096 </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct group grp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct group&nbsp;*grpp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[BUFLEN];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int i; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setgrent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i&nbsp;=&nbsp;getgrent_r(&amp;grp, buf, sizeof(buf),&nbsp;&amp;grpp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(i)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s&nbsp;(%jd):&quot;, grpp-&gt;gr_name,&nbsp;(intmax_t)&nbsp;grpp-&gt;gr_gid);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(grpp-&gt;gr_mem[j]&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;%s&quot;, grpp-&gt;gr_mem[j]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;endgrent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetgrent/">fgetgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrgid/">getgrgid</a></code>(3), <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/3-putgrent/">putgrent</a></code>(3), <code><a href="/docs/linux/man/5-group/">group</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
