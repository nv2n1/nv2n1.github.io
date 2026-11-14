---
title: "ares_mkquery(3)"
name: "ares_mkquery"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_mkquery/"
description: "ares_mkquery – Compose a single-question DNS query buffer"
---

<h2>NAME</h2>
<p> ares_mkquery &#8211; Compose a single-question DNS query buffer</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_mkquery(const char *name, int dnsclass, int type,
</code></pre>
<h2>DESCRIPTION</h2>
<p> Deprecated function. See <i><a href="/docs/linux/man/3-ares_create_query/">ares_create_query</a>(3)</i> instead! </p>
<p> The <code>ares_mkquery</code> function composes a DNS query with a single question. The parameter <i>name</i> gives the query name as a NUL-terminated C string of period-separated labels optionally ending with a period; periods and backslashes within a label must be escaped with a backlash. The parameters <i>dnsclass</i> and <i>type</i> give the class and type of the query using the values defined in <code>&lt;arpa/nameser.h&gt;</code>. The parameter <i>id</i> gives a 16-bit identifier for the query. The parameter <i>rd</i> should be nonzero if recursion is desired, zero if not. The query will be placed in an allocated buffer, a pointer to which will be stored in the variable pointed to by <i>buf</i>, and the length of which will be stored in the variable pointed to by <i>buflen</i>. It is the caller&#8217;s responsibility to free this buffer using <i><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a>(3)</i> when it is no longer needed. </p>
<p> Usage of <i><a href="/docs/linux/man/3-ares_mkquery/">ares_mkquery</a>(3)</i> is deprecated, whereas the function is equivalent to <i><a href="/docs/linux/man/3-ares_create_query/">ares_create_query</a>(3)</i> with <code>max_udp_size</code> set to 0. </p>
<h2>RETURN VALUES</h2>
<p> <code>ares_mkquery</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> Construction of the DNS query succeeded.</p>
<dt><code>ARES_EBADNAME</code></p>
<dd> The query name <i>name</i> could not be encoded as a domain name, either because it contained a zero-length label or because it contained a label of more than 63 characters.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_expand_name/">ares_expand_name</a></code>(3), <code><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998, 2000 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
