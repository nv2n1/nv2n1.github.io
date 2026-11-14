---
title: "getrpcbynumber_r(3)"
name: "getrpcbynumber_r"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getrpcbynumber_r/"
description: "getrpcent_r, getrpcbyname_r, getrpcbynumber_r – get RPC entry (reentrant)"
---

<h2 class="name">NAME</h2>
<p> getrpcent_r, getrpcbyname_r, getrpcbynumber_r &#8211; get RPC entry (reentrant) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
int getrpcent_r(struct rpcent *result_buf, char *buf,
                size_t buflen, struct rpcent **result);
int getrpcbyname_r(const char *name,
                   struct rpcent *result_buf, char *buf,
                   size_t buflen, struct rpcent **result);
int getrpcbynumber_r(int number,
                     struct rpcent *result_buf, char *buf,
                     size_t buflen, struct rpcent **result);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getrpcent_r</code>(), <code>getrpcbyname_r</code>(), <code>getrpcbynumber_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getrpcent_r</code>(), <code>getrpcbyname_r</code>(), and <code>getrpcbynumber_r</code>() functions are the reentrant equivalents of, respectively, <code><a href="/docs/linux/man/3-getrpcent/">getrpcent</a></code>(3), <code><a href="/docs/linux/man/3-getrpcbyname/">getrpcbyname</a></code>(3), and <code><a href="/docs/linux/man/3-getrpcbynumber/">getrpcbynumber</a></code>(3). They differ in the way that the <i>rpcent</i> structure is returned, and in the function calling signature and return value. This manual page describes just the differences from the nonreentrant functions. </p>
<p> Instead of returning a pointer to a statically allocated <i>rpcent</i> structure as the function result, these functions copy the structure into the location pointed to by <i>result_buf</i>. </p>
<p> The <i>buf</i> array is used to store the string fields pointed to by the returned <i>rpcent</i> structure. (The nonreentrant functions allocate these strings in static storage.) The size of this array is specified in <i>buflen</i>. If <i>buf</i> is too small, the call fails with the error <code>ERANGE</code>, and the caller must try again with a larger buffer. (A buffer of length 1024 bytes should be sufficient for most applications.) </p>
<p> If the function call successfully obtains an RPC record, then <i>*result</i> is set pointing to <i>result_buf</i>; otherwise, <i>*result</i> is set to NULL.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return 0. On error, they return one of the positive error numbers listed in ERRORS. </p>
<p> On error, record not found (<code>getrpcbyname_r</code>(), <code>getrpcbynumber_r</code>()), or end of input (<code>getrpcent_r</code>()) <i>result</i> is set to NULL.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd> (<code>getrpcent_r</code>()) No more records in database.</p>
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
<td> <code>getrpcent_r</code>(), <code>getrpcbyname_r</code>(), <code>getrpcbynumber_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions. Functions with similar names exist on some other systems, though typically with different calling signatures.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getrpcent/">getrpcent</a></code>(3), <code><a href="/docs/linux/man/5-rpc/">rpc</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
