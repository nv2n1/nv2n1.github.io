---
title: "generic_file_write_iter(9)"
name: "generic_file_write_iter"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_file_write_iter/"
description: "generic_file_write_iter – write data to a file"
---

<p>generic_file_write_iter &#8211; write data to a file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t generic_file_write_iter(struct kiocb&nbsp;<wbr>*&nbsp;<wbr></code><i>iocb</i><code>, struct iov_iter&nbsp;<wbr>*&nbsp;<wbr></code><i>from</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>iocb</i></p>
<dl>
<dd>
<dd>IO state structure</dl>
<p> <i>from</i></p>
<dl>
<dd>iov_iter with data to write</dl>
<h2>Description</h2>
<p>This is a wrapper around <code>__generic_file_write_iter</code> to be used by most filesystems. It takes care of syncing the file in case of O_SYNC file and acquires i_mutex as needed.</p>
<h2>Copyright</h2>
