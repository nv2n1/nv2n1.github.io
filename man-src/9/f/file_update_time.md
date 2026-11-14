---
title: "file_update_time(9)"
name: "file_update_time"
section: "9"
letter: "f"
url: "/docs/linux/man/9-file_update_time/"
---

file_update_time - update mtime and ctime time

<h2>Synopsis</h2>

<pre><code>int file_update_time(struct file *file);</code></pre>

<h2>Arguments</h2>

<i>file</i>
<dl><dd><dd>file accessed</dl>

<h2>Description</h2>

Update the mtime and ctime members of an inode and mark the inode for writeback. Note that this function is meant exclusively for usage in the file write path of filesystems, and filesystems may choose to explicitly ignore update via this function with the S_NOCMTIME inode flag, e.g. for network filesystem where these timestamps are handled by the server. This can return an error for file systems who need to allocate space in order to update an inode.

<h2>Copyright</h2>


