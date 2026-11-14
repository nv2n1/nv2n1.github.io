---
title: "ares_expand_name(3)"
name: "ares_expand_name"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_expand_name/"
description: "ares_expand_name – Expand a DNS-encoded domain name"
---

<h2>NAME</h2>
<p> ares_expand_name &#8211; Expand a DNS-encoded domain name</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_expand_name(const unsigned char *encoded,
                     const unsigned char *abuf, int alen, char **s,
                     long *enclen)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_expand_name</code> function converts a DNS-encoded domain name to a dot-separated C string. The argument <i>encoded</i> gives the beginning of the encoded domain name, and the arguments <i>abuf</i> and <i>alen</i> give the containing message buffer (necessary for the processing of indirection pointers within the encoded domain name). The result is placed in a NUL-terminated allocated buffer, a pointer to which is stored in the variable pointed to by <i>s</i>. The length of the encoded name is stored in the variable pointed to by <i>enclen</i> so that the caller can advance past the encoded domain name to read further data in the message. </p>
<p> Use <i><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a>(3)</i> to free the allocated hostname.</p>
<h2>RETURN VALUES</h2>
<p> <code>ares_expand_name</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> Expansion of the encoded name succeeded.</p>
<dt><code>ARES_EBADNAME</code></p>
<dd> The encoded domain name was malformed and could not be expanded.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_mkquery/">ares_mkquery</a></code>(3),<code><a href="/docs/linux/man/3-ares_free_string/">ares_free_string</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
