---
title: "memzero_explicit(9)"
name: "memzero_explicit"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memzero_explicit/"
description: "memzero_explicit – Fill a region of memory (e.g. sensitive keying data) with 0s."
---

<p>memzero_explicit &#8211; Fill a region of memory (e.g. sensitive keying data) with 0s.</p>
<h2>Synopsis</h2>
<pre><code>void memzero_explicit(void *s, size_t count);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>Pointer to the start of the area.</dl>
<p> <i>count</i></p>
<dl>
<dd>The size of the area.</dl>
<h2>Note</h2>
<p>usually using <code>memset</code> is just fine (!), but in cases where clearing out _local_ data at the end of a scope is necessary, <code>memzero_explicit</code> should be used instead in order to prevent the compiler from optimising away zeroing. </p>
<p> <code>memzero_explicit</code> doesn&#8217;t need an arch-specific version as it just invokes the one of <code>memset</code> implicitly.</p>
<h2>Copyright</h2>
