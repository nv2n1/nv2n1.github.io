---
title: "release_bitmap(3)"
name: "release_bitmap"
section: "3"
letter: "r"
url: "/docs/linux/man/3-release_bitmap/"
description: "release_bitmap – Releases a previously locked bitmap. Allegro game programming library."
---

<p>release_bitmap &#8211; Releases a previously locked bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void release_bitmap(BITMAP *bmp);</code></pre>
<h2>Description</h2>
<p>Releases a bitmap that was previously locked by calling acquire_bitmap(). If the bitmap was locked multiple times, you must release it the same number of times before it will truly be unlocked. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-acquire_bitmap/">acquire_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-acquire_screen/">acquire_screen</a></code>(3), <code><a href="/docs/linux/man/3-release_screen/">release_screen</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exaccel/">exaccel</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3), <code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3), <code><a href="/docs/linux/man/3-exscroll/">exscroll</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
