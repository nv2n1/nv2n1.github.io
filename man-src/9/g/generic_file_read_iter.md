---
title: "generic_file_read_iter(9)"
name: "generic_file_read_iter"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_file_read_iter/"
description: "generic_file_read_iter – generic filesystem read routine"
---

<p>generic_file_read_iter &#8211; generic filesystem read routine</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t generic_file_read_iter(struct kiocb&nbsp;<wbr>*&nbsp;<wbr></code><i>iocb</i><code>, struct iov_iter&nbsp;<wbr>*&nbsp;<wbr></code><i>iter</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>iocb</i></p>
<dl>
<dd>
<dd>kernel I/O control block</dl>
<p> <i>iter</i></p>
<dl>
<dd>destination for the data read</dl>
<h2>Description</h2>
<p>This is the &#8220;<code>read_iter</code>&#8221; routine for all filesystems that can use the page cache directly.</p>
<h2>Copyright</h2>
