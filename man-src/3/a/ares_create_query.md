---
title: "ares_create_query(3)"
name: "ares_create_query"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_create_query/"
description: "ares_create_query – Compose a single-question DNS query buffer"
---

<h2>NAME</h2>
<p> ares_create_query &#8211; Compose a single-question DNS query buffer</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_create_query(const char *name, int dnsclass,                         int type,
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_create_query</code> function composes a DNS query with a single question. The parameter <i>name</i> gives the query name as a NUL-terminated C string of period-separated labels optionally ending with a period; periods and backslashes within a label must be escaped with a backlash. The parameters <i>dnsclass</i> and <i>type</i> give the class and type of the query using the values defined in <code>&lt;arpa/nameser.h&gt;</code>. The parameter <i>id</i> gives a 16-bit identifier for the query. The parameter <i>rd</i> should be nonzero if recursion is desired, zero if not. The query will be placed in an allocated buffer, a pointer to which will be stored in the variable pointed to by <i>buf</i>, and the length of which will be stored in the variable pointed to by <i>buflen</i>. It is the caller&#8217;s responsibility to free this buffer using <i><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a>(3)</i> when it is no longer needed. The parameter <i>max_udp_size</i> should be nonzero to activate EDNS. Usage of <i><a href="/docs/linux/man/3-ares_create_query/">ares_create_query</a>(3)</i>&nbsp;<wbr>with <i>max_udp_size</i> set to zero is equivalent to <i><a href="/docs/linux/man/3-ares_mkquery/">ares_mkquery</a>(3)</i>.</p>
<h2>RETURN VALUES</h2>
<p> <code>ares_create_query</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> Construction of the DNS query succeeded.</p>
<dt><code>ARES_EBADNAME</code></p>
<dd> The query name <i>name</i> could not be encoded as a domain name, either because it contained a zero-length label or because it contained a label of more than 63 characters.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<h2>AVAILABILITY</h2>
<p> Added in c-ares 1.10.0</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_expand_name/">ares_expand_name</a></code>(3), <code><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a></code>(3)</p>
<h2>AUTHOR</h2>
<h2>Index</h2>
