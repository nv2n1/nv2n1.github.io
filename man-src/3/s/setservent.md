---
title: "setservent(3)"
name: "setservent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setservent/"
description: "getservent, getservbyname, getservbyport, setservent, endservent – get service entry"
---

<p>getservent, getservbyname, getservbyport, setservent, endservent &#8211; get service entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netdb.h&gt;

struct servent *getservent(void);

struct servent *getservbyname(const char *name, const char *proto);

struct servent *getservbyport(int port, const char *proto);

void setservent(int stayopen);

void endservent(void);</code></pre>
<h2>Description</h2>
<p>The <code>getservent</code>() function reads the next entry from the services database (see <code><a href="/docs/linux/man/5-services/">services</a></code>(5)) and returns a <i>servent</i> structure containing the broken-out fields from the entry. A connection is opened to the database if necessary. The <code>getservbyname</code>() function returns a <i>servent</i> structure for the entry from the database that matches the service <i>name</i> using protocol <i>proto</i>. If <i>proto</i> is NULL, any protocol will be matched. A connection is opened to the database if necessary. The <code>getservbyport</code>() function returns a <i>servent</i> structure for the entry from the database that matches the port <i>port</i> (given in network byte order) using protocol <i>proto</i>. If <i>proto</i> is NULL, any protocol will be matched. A connection is opened to the database if necessary. The <code>setservent</code>() function opens a connection to the database, and sets the next entry to the first entry. If <i>stayopen</i> is nonzero, then the connection to the database will not be closed between calls to one of the <code>getserv*</code>() functions. The <code>endservent</code>() function closes the connection to the database. The <i>servent</i> structure is defined in <i>&lt;netdb.h&gt;</i> as follows: </p>
<pre><code>struct servent {
    char *s_name;     /* official service name */
    char **s_aliases; /* alias list */
    int s_port;       /* port number */
    char *s_proto;    /* protocol to use */
}</code></pre>
<p> The members of the <i>servent</i> structure are:</p>
<dl>
<dt><i>s_name</i></p>
<dd>The official name of the service.</p>
<dt><i>s_aliases</i></p>
<dd>A NULL-terminated list of alternative names for the service.</p>
<dt><i>s_port</i></p>
<dd>The port number for the service given in network byte order.</p>
<dt><i>s_proto</i></p>
<dd>The name of the protocol to use with this service.</dl>
<h2>Return Value</h2>
<p>The <code>getservent</code>(), <code>getservbyname</code>(), and <code>getservbyport</code>() functions return a pointer to a statically allocated <i>servent</i> structure, or NULL if an error occurs or the end of the file is reached.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/services</i></p>
<dd>services database file</dl>
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
<td> <code>getservent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:servent<br />
 race:serventbuf locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getservbyname</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:servbyname<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getservbyport</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:servbyport<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>setservent</code>(),<br />
 <code>endservent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:servent<br />
 locale
</td>
</tr>
</table>
<p> In the above table, <i>servent</i> in <i>race:servent</i> signifies that if any of the functions <code>setservent</code>(), <code>getservent</code>(), or <code>endservent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getnetent/">getnetent</a></code>(3), <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), <code><a href="/docs/linux/man/3-getservent_r/">getservent_r</a></code>(3), <code><a href="/docs/linux/man/5-services/">services</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
