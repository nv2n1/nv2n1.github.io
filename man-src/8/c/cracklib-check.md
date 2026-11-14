---
title: "cracklib-check(8)"
name: "cracklib-check"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cracklib-check/"
description: "cracklib-check – Check passwords using libcrack2"
---

<p>cracklib-check &#8211; Check passwords using libcrack2</p>
<h2>Synopsis</h2>
<p><code>cracklib-check</code> </p>
<h2>Description</h2>
<p><code>cracklib-check</code> takes a list of passwords from stdin and checks them via libcrack2&#8217;s <code><a href="/docs/linux/man/3-fascistcheck/">FascistCheck</a></code>(3) sub routine. </p>
<h2>Result</h2>
<p><code>cracklib-check</code> prints each checked password and the corresponding result of <code><a href="/docs/linux/man/3-fascistcheck/">FascistCheck</a></code>(3) to stdout. The password and the result are separated by a colon.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fascistcheck/">FascistCheck</a></code>(3) </p>
<h2>Author</h2>
<p>This man page was written by Jan Dittberner &lt;jandd [at] debian.org&gt; for the Debian GNU/Linux System (but may be used by others).</p>
