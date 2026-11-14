---
title: "wbc_account_io(9)"
name: "wbc_account_io"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wbc_account_io/"
description: "wbc_account_io – account IO issued during writeback"
---

<p>wbc_account_io &#8211; account IO issued during writeback</p>
<h2>Synopsis</h2>
<pre><code>void wbc_account_io(struct writeback_control *wbc, struct page *page, size_t bytes);</code></pre>
<h2>Arguments</h2>
<p><i>wbc</i></p>
<dl>
<dd>
<dd>writeback_control of the writeback in progress</dl>
<p> <i>page</i></p>
<dl>
<dd>page being written out</dl>
<p> <i>bytes</i></p>
<dl>
<dd>number of bytes being written out</dl>
<h2>Description</h2>
<p><i>bytes</i> from <i>page</i> are about to written out during the writeback controlled by <i>wbc</i>. Keep the book for foreign inode detection. See <code>wbc_detach_inode</code>.</p>
<h2>Copyright</h2>
