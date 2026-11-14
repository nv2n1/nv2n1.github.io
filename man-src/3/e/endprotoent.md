---
title: "endprotoent(3)"
name: "endprotoent"
section: "3"
letter: "e"
url: "/docs/linux/man/3-endprotoent/"
description: "getprotoent, getprotobyname, getprotobynumber, setprotoent, endprotoent – get protocol entry"
---

<h2 class="name">NAME</h2>
<p> getprotoent, getprotobyname, getprotobynumber, setprotoent, endprotoent &#8211; get protocol entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
struct protoent *getprotoent(void);
struct protoent *getprotobyname(const char *name);
struct protoent *getprotobynumber(int proto);
void setprotoent(int stayopen);
void endprotoent(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>getprotoent</code>() function reads the next entry from the protocols database (see <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5)) and returns a <i>protoent</i> structure containing the broken-out fields from the entry. A connection is opened to the database if necessary. </p>
<p> The <code>getprotobyname</code>() function returns a <i>protoent</i> structure for the entry from the database that matches the protocol name <i>name</i>. A connection is opened to the database if necessary. </p>
<p> The <code>getprotobynumber</code>() function returns a <i>protoent</i> structure for the entry from the database that matches the protocol number <i>number</i>. A connection is opened to the database if necessary. </p>
<p> The <code>setprotoent</code>() function opens a connection to the database, and sets the next entry to the first entry. If <i>stayopen</i> is nonzero, then the connection to the database will not be closed between calls to one of the <code>getproto*</code>() functions. </p>
<p> The <code>endprotoent</code>() function closes the connection to the database. </p>
<p> The <i>protoent</i> structure is defined in <i>&lt;netdb.h&gt;</i> as follows: </p>
<p> struct protoent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;*p_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;official protocol name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**p_aliases;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;alias list&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_proto;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;protocol number&nbsp;*/ } </p>
<p> The members of the <i>protoent</i> structure are:</p>
<dl>
<dt><i>p_name</i></p>
<dd> The official name of the protocol.</p>
<dt><i>p_aliases</i></p>
<dd> A NULL-terminated list of alternative names for the protocol.</p>
<dt><i>p_proto</i></p>
<dd> The protocol number.</dl>
<h2>RETURN VALUE</h2>
<p> The <code>getprotoent</code>(), <code>getprotobyname</code>(), and <code>getprotobynumber</code>() functions return a pointer to a statically allocated <i>protoent</i> structure, or a null pointer if an error occurs or the end of the file is reached.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/protocols</i></p>
<dd> protocol database file</dl>
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
<td> <code>getprotoent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:protoent<br />
 race:protoentbuf locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getprotobyname</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:protobyname<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getprotobynumber</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:protobynumber<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>setprotoent</code>(),<br />
 <code>endprotoent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:protoent<br />
 locale
</td>
</tr>
</table>
<p> In the above table, <i>protoent</i> in <i>race:protoent</i> signifies that if any of the functions <code>setprotoent</code>(), <code>getprotoent</code>(), or <code>endprotoent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getnetent/">getnetent</a></code>(3), <code><a href="/docs/linux/man/3-getprotoent_r/">getprotoent_r</a></code>(3), <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3), <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
