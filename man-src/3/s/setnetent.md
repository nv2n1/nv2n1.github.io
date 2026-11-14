---
title: "setnetent(3)"
name: "setnetent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setnetent/"
description: "getnetent, getnetbyname, getnetbyaddr, setnetent, endnetent – get network entry"
---

<p>getnetent, getnetbyname, getnetbyaddr, setnetent, endnetent &#8211; get network entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netdb.h&gt;

struct netent *getnetent(void);

struct netent *getnetbyname(const char *name);

struct netent *getnetbyaddr(uint32_t net, int type);

void setnetent(int stayopen);

void endnetent(void);</code></pre>
<h2>Description</h2>
<p>The <code>getnetent</code>() function reads the next entry from the networks database and returns a <i>netent</i> structure containing the broken-out fields from the entry. A connection is opened to the database if necessary. The <code>getnetbyname</code>() function returns a <i>netent</i> structure for the entry from the database that matches the network <i>name</i>. The <code>getnetbyaddr</code>() function returns a <i>netent</i> structure for the entry from the database that matches the network number <i>net</i> of type <i>type</i>. The <i>net</i> argument must be in host byte order. The <code>setnetent</code>() function opens a connection to the database, and sets the next entry to the first entry. If <i>stayopen</i> is nonzero, then the connection to the database will not be closed between calls to one of the <code>getnet*</code>() functions. The <code>endnetent</code>() function closes the connection to the database. The <i>netent</i> structure is defined in <i>&lt;netdb.h&gt;</i> as follows: </p>
<pre><code>struct netent {
    char *n_name;     /* official network name */
    char **n_aliases; /* alias list */
    int n_addrtype;   /* net address type */
    uint32_t n_net;   /* network number */
}</code></pre>
<p> The members of the <i>netent</i> structure are:</p>
<dl>
<dt><i>n_name</i></p>
<dd>The official name of the network.</p>
<dt><i>n_aliases</i></p>
<dd>A NULL-terminated list of alternative names for the network.</p>
<dt><i>n_addrtype</i></p>
<dd>The type of the network number; always <code>AF_INET</code>.</p>
<dt><i>n_net</i></p>
<dd>The network number in host byte order.</dl>
<h2>Return Value</h2>
<p>The <code>getnetent</code>(), <code>getnetbyname</code>(), and <code>getnetbyaddr</code>() functions return a pointer to a statically allocated <i>netent</i> structure, or a null pointer if an error occurs or the end of the file is reached.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/networks</i></p>
<dd>networks database file</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getnetent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:netent<br />
 race:netentbuf env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getnetbyname</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:netbyname<br />
 env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getnetbyaddr</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:netbyaddr<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>setnetent</code>(),<br />
 <code>endnetent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:netent env<br />
 locale
</td>
</tr>
</table>
<p> In the above table, <i>netent</i> in <i>race:netent</i> signifies that if any of the functions <code>setnetent</code>(), <code>getnetent</code>(), or <code>endnetent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>Notes</h2>
<p>In glibc versions before 2.2, the <i>net</i> argument of <code>getnetbyaddr</code>() was of type <i>long</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getnetent_r/">getnetent_r</a></code>(3), <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3)<br />
 RFC 1101</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
