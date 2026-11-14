---
title: "innetgr(3)"
name: "innetgr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-innetgr/"
description: "setnetgrent, endnetgrent, getnetgrent, getnetgrent_r, innetgr – handle network group entries"
---

<h2 class="name">NAME</h2>
<p> setnetgrent, endnetgrent, getnetgrent, getnetgrent_r, innetgr &#8211; handle network group entries </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
int setnetgrent(const char *netgroup);
void endnetgrent(void);
int getnetgrent(char **host, char **user, char **domain);
int getnetgrent_r(char **host, char **user,
                  char **domain, char *buf, size_t buflen);
int innetgr(const char *netgroup, const char *host,
            const char *user, const char *domain);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>setnetgrent</code>(), <code>endnetgrent</code>(), <code>getnetgrent</code>(), <code>getnetgrent_r</code>(), <code>innetgr</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <i>netgroup</i> is a SunOS invention. A netgroup database is a list of string triples (<i>hostname</i>, <i>username</i>, <i>domainname</i>) or other netgroup names. Any of the elements in a triple can be empty, which means that anything matches. The functions described here allow access to the netgroup databases. The file <i>/etc/nsswitch.conf</i> defines what database is searched. </p>
<p> The <code>setnetgrent</code>() call defines the netgroup that will be searched by subsequent <code>getnetgrent</code>() calls. The <code>getnetgrent</code>() function retrieves the next netgroup entry, and returns pointers in <i>host</i>, <i>user</i>, <i>domain</i>. A null pointer means that the corresponding entry matches any string. The pointers are valid only as long as there is no call to other netgroup-related functions. To avoid this problem you can use the GNU function <code>getnetgrent_r</code>() that stores the strings in the supplied buffer. To free all allocated buffers use <code>endnetgrent</code>(). </p>
<p> In most cases you want to check only if the triplet (<i>hostname</i>, <i>username</i>, <i>domainname</i>) is a member of a netgroup. The function <code>innetgr</code>() can be used for this without calling the above three functions. Again, a null pointer is a wildcard and matches any string. The function is thread-safe.</p>
<h2>RETURN VALUE</h2>
<p> These functions return 1 on success and 0 for failure.</p>
<h2>FILES</h2>
<p> <i>/etc/netgroup</i><br />
 <i>/etc/nsswitch.conf</i></p>
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
<td> <code>setnetgrent</code>(),<br />
 <code>getnetgrent_r</code>(),<br />
 <code>innetgr</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:netgrent<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>endnetgrent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:netgrent
</td>
</tr>
<tr VALIGN=top>
<td> <code>getnetgrent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:netgrent<br />
 race:netgrentbuf locale
</td>
</tr>
</table>
<p> In the above table, <i>netgrent</i> in <i>race:netgrent</i> signifies that if any of the functions <code>setnetgrent</code>(), <code>getnetgrent_r</code>(), <code>innetgr</code>(), <code>getnetgrent</code>(), or <code>endnetgrent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> These functions are not in POSIX.1, but <code>setnetgrent</code>(), <code>endnetgrent</code>(), <code>getnetgrent</code>(), and <code>innetgr</code>() are available on most UNIX systems. <code>getnetgrent_r</code>() is not widely available on other systems.</p>
<h2>NOTES</h2>
<p> In the BSD implementation, <code>setnetgrent</code>() returns void.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-sethostent/">sethostent</a></code>(3), <code><a href="/docs/linux/man/3-setprotoent/">setprotoent</a></code>(3), <code><a href="/docs/linux/man/3-setservent/">setservent</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
