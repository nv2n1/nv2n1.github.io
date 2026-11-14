---
title: "bson_strndup(3)"
name: "bson_strndup"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strndup/"
description: "bson_strndup() – Allocates a new string and copies up to n_bytes from str into it. A trailing is always set."
---

<h2>NAME</h2>
<p> bson_strndup() &#8211; Allocates a new string and copies up to n_bytes from str into it. A trailing &nbsp;<wbr> is always set.</p>
<h2>SYNOPSIS</h2>
<pre><code>
char *
bson_strndup(const char *str,
             size_t n_bytes);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></p>
<dd> A string to copy.</dl>
<dl>
<dt><code>n_bytes</code></p>
<dd> A size_t.</dl>
<h2>DESCRIPTION</h2>
<p> Allocates a new string and copies up to <code>n_bytes</code> from <code>str</code> into it. A trailing <code>
