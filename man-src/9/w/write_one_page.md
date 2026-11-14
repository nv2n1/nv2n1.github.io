---
title: "write_one_page(9)"
name: "write_one_page"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_one_page/"
description: "write_one_page – write out a single page and optionally wait on I/O"
---

<p>write_one_page &#8211; write out a single page and optionally wait on I/O</p>
<h2>Synopsis</h2>
<pre><code>int write_one_page(struct page *page, int wait);</code></pre>
<h2>Arguments</h2>
<p><i>page</i></p>
<dl>
<dd>
<dd>the page to write</dl>
<p> <i>wait</i></p>
<dl>
<dd>if true, wait on writeout</dl>
<h2>Description</h2>
<p>The page must be locked by the caller and will be unlocked upon return. </p>
<p> <code>write_one_page</code> returns a negative error code if I/O failed.</p>
<h2>Copyright</h2>
