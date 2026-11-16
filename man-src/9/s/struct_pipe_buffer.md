---
title: "struct_pipe_buffer(9)"
name: "struct_pipe_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_pipe_buffer/"
---

struct_pipe_buffer - a linux kernel pipe buffer

<h2>Synopsis</h2>

<pre><code>struct pipe_buffer {
    struct page *page;
    unsigned int offset;
    unsigned int len;
    const struct pipe_buf_operations *ops;
    unsigned int flags;
    unsigned long private;
};</code></pre>

<h2>Members</h2>

page
<dl><dd>the page containing the data for the pipe buffer</dd></dl>
 

 offset
<dl><dd>offset of data inside the <i>page</i></dd></dl>
 

 len
<dl><dd>length of data inside the <i>page</i></dd></dl>
 

 ops
<dl><dd>operations associated with this buffer. See <i>pipe_buf_operations</i>.</dd></dl>
 

 flags
<dl><dd>pipe buffer flags. See above.</dd></dl>
 

 private
<dl><dd>private data owned by the ops.</dd></dl>

<h2>Copyright</h2>


