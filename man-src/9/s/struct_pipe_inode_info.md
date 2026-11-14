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
<dl><dd>mutex protecting the whole thing</dl>
 

 wait
<dl><dd>reader/writer wait point in case of empty/full pipe</dl>
 

 nrbufs
<dl><dd>the number of non-empty pipe buffers in this pipe</dl>
 

 curbuf
<dl><dd>the current pipe buffer entry</dl>
 

 buffers
<dl><dd>total number of buffers (should be a power of 2)</dl>
 

 readers
<dl><dd>number of current readers of this pipe</dl>
 

 writers
<dl><dd>number of current writers of this pipe</dl>
 

 files
<dl><dd>number of struct file referring this pipe (protected by -&gt;i_lock)</dl>
 

 waiting_writers
<dl><dd>number of writers blocked waiting for room</dl>
 

 r_counter
<dl><dd>reader counter</dl>
 

 w_counter
<dl><dd>writer counter</dl>
 

 tmp_page
<dl><dd>cached released page</dl>
 

 fasync_readers
<dl><dd>reader side fasync</dl>
 

 fasync_writers
<dl><dd>writer side fasync</dl>
 

 bufs
<dl><dd>the circular array of pipe buffers</dl>
 

 user
<dl><dd>the user who created this pipe</dl>

<h2>Copyright</h2>


