---
title: "setrpcent(3)"
name: "setrpcent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setrpcent/"
description: "getrpcent, getrpcbyname, getrpcbynumber, setrpcent, endrpcent – get RPC entry"
---

<p>getrpcent, getrpcbyname, getrpcbynumber, setrpcent, endrpcent &#8211; get RPC entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netdb.h&gt;

struct rpcent *getrpcent(void);

struct rpcent *getrpcbyname(const char *name);

struct rpcent *getrpcbynumber(int number);

void setrpcent(int stayopen);

void endrpcent(void);</code></pre>
<h2>Description</h2>
<p>The <code>getrpcent</code>(), <code>getrpcbyname</code>(), and <code>getrpcbynumber</code>() functions each return a pointer to an object with the following structure containing the broken-out fields of an entry in the RPC program number data base. </p>
<pre><code>struct rpcent {
    char *r_name;     /* name of server for this RPC program */
    char **r_aliases; /* alias list */
    long r_number;    /* RPC program number */
};</code></pre>
<p> The members of this structure are:</p>
<dl>
<dt><i>r_name</i></p>
<dd>The name of the server for this RPC program.</p>
<dt><i>r_aliases</i></p>
<dd>A NULL-terminated list of alternate names for the RPC program.</p>
<dt><i>r_number</i></p>
<dd>The RPC program number for this service.</dl>
<p> The <code>getrpcent</code>() function reads the next entry from the database. A connection is opened to the database if necessary. The <code>setrpcent</code>() function opens a connection to the database, and sets the next entry to the first entry. If <i>stayopen</i> is nonzero, then the connection to the database will not be closed between calls to one of the <code>getrpc*</code>() functions. The <code>endrpcent</code>() function closes the connection to the database. The <code>getrpcbyname</code>() and <code>getrpcbynumber</code>() functions sequentially search from the beginning of the file until a matching RPC program name or program number is found, or until end-of-file is encountered.</p>
<h2>Return Value</h2>
<p>On success, <code>getrpcent</code>(), <code>getrpcbyname</code>(), and <code>getrpcbynumber</code>() return a pointer to a statically allocated <i>rpcent</i> structure. NULL is returned on EOF or error.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/rpc</i></p>
<dd>RPC program number database.</dl>
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
<td> <code>getrpcent</code>(), <code>getrpcbyname</code>(),<br />
 <code>getrpcbynumber</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
<tr VALIGN=top>
<td> <code>setrpcent</code>(), <code>endrpcent</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>Not in POSIX.1. Present on the BSDs, Solaris, and many other systems.</p>
<h2>Bugs</h2>
<p>All information is contained in a static area so it must be copied if it is to be saved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getrpcent_r/">getrpcent_r</a></code>(3), <code><a href="/docs/linux/man/5-rpc/">rpc</a></code>(5), <code><a href="/docs/linux/man/8-rpcinfo/">rpcinfo</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
