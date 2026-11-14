---
title: "d_path(9)"
name: "d_path"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_path/"
---

d_path - return the path of a dentry

<h2>Synopsis</h2>

<pre><code>char *d_path(const struct path *path, char *buf, int buflen);</code></pre>

<h2>Arguments</h2>

<i>path</i>
<dl><dd><dd>path to report</dl>
 

 <i>buf</i>
<dl><dd>buffer to return value in</dl>
 

 <i>buflen</i>
<dl><dd>buffer length</dl>

<h2>Description</h2>

Convert a dentry into an ASCII path name. If the entry has been deleted the string " (deleted)" is appended. Note that this is ambiguous. 

 Returns a pointer into the buffer or an error code if the path was too long. Note: Callers should use the returned pointer, not the passed in buffer, to use the name! The implementation often starts at an offset into the buffer, and may leave 0 bytes at the start. 

 "buflen" should be positive.

<h2>Copyright</h2>


