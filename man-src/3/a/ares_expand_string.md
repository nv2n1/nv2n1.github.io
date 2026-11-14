---
title: "ares_expand_string(3)"
name: "ares_expand_string"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_expand_string/"
description: "ares_expand_string – Expand a length encoded string"
---

<h2>NAME</h2>
<p> ares_expand_string &#8211; Expand a length encoded string</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_expand_string(const unsigned char *encoded,
                       const unsigned char *abuf, int alen, unsigned char **s,
                       long *enclen)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_expand_string</code> function converts a length encoded string to a NUL-terminated C string. The argument <i>encoded</i> gives the beginning of the encoded string, and the arguments <i>abuf</i> and <i>alen</i> give the containing message buffer (necessary for the processing of indirection pointers within the encoded domain name). The result is placed in a NUL-terminated allocated buffer, a pointer to which is stored in the variable pointed to by <i>s</i>. The length of the encoded string is stored in the variable pointed to by <i>enclen</i> so that the caller can advance past the encoded string to read further data in the message.</p>
<h2>RETURN VALUES</h2>
<p> <code>ares_expand_string</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> Expansion of the encoded string succeeded.</p>
<dt><code>ARES_EBADSTR</code></p>
<dd> The encoded string was malformed and could not be expanded.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Dominick Meglio </p>
<h2>Index</h2>
