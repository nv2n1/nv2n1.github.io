---
title: "struct_pipe_inode_info(9)"
name: "struct_pipe_inode_info"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_pipe_inode_info/"
---

struct_pipe_inode_info - a linux kernel pipe

<h2>Synopsis</h2>

<pre><code>struct pipe_inode_info {
    struct mutex mutex;
    wait_queue_head_t wait;
    unsigned int nrbufs;
    unsigned int curbuf;
    unsigned int buffers;
    unsigned int readers;
    unsigned int writers;
    unsigned int files;
    unsigned int waiting_writers;
    unsigned int r_counter;
    unsigned int w_counter;
    struct page *tmp_page;
    struct fasync_struct *fasync_readers;
    struct fasync_struct *fasync_writers;
    struct pipe_buffer *bufs;
    struct user_struct *user;
};</code></pre>

<h2>Members</h2>

mutex
<dl><dd>mutex protecting the whole thing</dd></dl>
 

 wait
<dl><dd>reader/writer wait point in case of empty/full pipe</dd></dl>
 

 nrbufs
<dl><dd>the number of non-empty pipe buffers in this pipe</dd></dl>
 

 curbuf
<dl><dd>the current pipe buffer entry</dd></dl>
 

 buffers
<dl><dd>total number of buffers (should be a power of 2)</dd></dl>
 

 readers
<dl><dd>number of current readers of this pipe</dd></dl>
 

 writers
<dl><dd>number of current writers of this pipe</dd></dl>
 

 files
<dl><dd>number of struct file referring this pipe (protected by -&gt;i_lock)</dd></dl>
 

 waiting_writers
<dl><dd>number of writers blocked waiting for room</dd></dl>
 

 r_counter
<dl><dd>reader counter</dd></dl>
 

 w_counter
<dl><dd>writer counter</dd></dl>
 

 tmp_page
<dl><dd>cached released page</dd></dl>
 

 fasync_readers
<dl><dd>reader side fasync</dd></dl>
 

 fasync_writers
<dl><dd>writer side fasync</dd></dl>
 

 bufs
<dl><dd>the circular array of pipe buffers</dd></dl>
 

 user
<dl><dd>the user who created this pipe</dd></dl>

<h2>Copyright</h2>


