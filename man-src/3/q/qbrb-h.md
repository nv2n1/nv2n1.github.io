---
title: "qbrb-h(3)"
name: "qbrb-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbrb-h/"
description: "qbrb.h –"
---

<p>qbrb.h &#8211; </p>
<p> This implements a ring buffer that works in &#8216;chunks&#8217; not bytes.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;sys/types.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<h3>Macros</h3>
<pre><code>#define QB_RB_FLAG_CREATE   0x01


create a ring buffer (rather than open and existing one)


#define QB_RB_FLAG_OVERWRITE   0x02


New calls to qb_rb_chunk_write() will call qb_rb_chunk_reclaim() if there is not enough space.


#define QB_RB_FLAG_SHARED_THREAD   0x04


The ringbuffer will be shared between pthreads not processes.


#define QB_RB_FLAG_SHARED_PROCESS   0x08


The ringbuffer will be shared between processes.


#define QB_RB_FLAG_NO_SEMAPHORE   0x10


Don't use semaphores, only atomic ops.



Typedefs</code></pre>
<p> typedef struct qb_ringbuffer_s <code>qb_ringbuffer_t</code></p>
<h3>Functions</h3>
<p><code>qb_ringbuffer_t</code> * <code>qb_rb_open</code> (const char *name, size_t size, uint32_t flags, size_t shared_user_data_size)<br />
 <i>Create the ring buffer with the given type. </i><br />
 void <code>qb_rb_close</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>Dereference the ringbuffer and if we are the last user destroy it. </i><br />
 char * <code>qb_rb_name_get</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>Get the name of the ringbuffer. </i><br />
 void * <code>qb_rb_shared_user_data_get</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>Get a point to user shared data area. </i><br />
 ssize_t <code>qb_rb_chunk_write</code> (<code>qb_ringbuffer_t</code> *rb, const void *data, size_t len)<br />
 <i>Write a chunk to the ring buffer. </i><br />
 void * <code>qb_rb_chunk_alloc</code> (<code>qb_ringbuffer_t</code> *rb, size_t len)<br />
 <i>Allocate space for a chunk of the given size. </i><br />
 int32_t <code>qb_rb_chunk_commit</code> (<code>qb_ringbuffer_t</code> *rb, size_t len)<br />
 <i>finalize the chunk. </i><br />
 ssize_t <code>qb_rb_chunk_peek</code> (<code>qb_ringbuffer_t</code> *rb, void **data_out, int32_t ms_timeout)<br />
 <i>Read (without reclaiming) the last chunk. </i><br />
 void <code>qb_rb_chunk_reclaim</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>Reclaim the oldest chunk. </i><br />
 ssize_t <code>qb_rb_chunk_read</code> (<code>qb_ringbuffer_t</code> *rb, void *data_out, size_t len, int32_t ms_timeout)<br />
 <i>Read the oldest chunk into data_out. </i><br />
 int32_t <code>qb_rb_refcount_get</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>Get the reference count. </i><br />
 ssize_t <code>qb_rb_space_free</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>The amount of free space in the ring buffer. </i><br />
 ssize_t <code>qb_rb_space_used</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>The total amount of data in the buffer. </i><br />
 ssize_t <code>qb_rb_chunks_used</code> (<code>qb_ringbuffer_t</code> *rb)<br />
 <i>The total number of chunks in the buffer. </i><br />
 ssize_t <code>qb_rb_write_to_file</code> (<code>qb_ringbuffer_t</code> *rb, int32_t fd)<br />
 <i>Write the contents of the Ring Buffer to file. </i><br />
 <code>qb_ringbuffer_t</code> * <code>qb_rb_create_from_file</code> (int32_t fd, uint32_t flags)<br />
 <i>Load the saved ring buffer from file into tempory memory. </i><br />
 int32_t <code>qb_rb_chown</code> (<code>qb_ringbuffer_t</code> *rb, uid_t owner, gid_t group)<br />
 <i>Like &#8216;chown&#8217; it changes the owner and group of the ringbuffers resources. </i><br />
 int32_t <code>qb_rb_chmod</code> (<code>qb_ringbuffer_t</code> *rb, mode_t mode)<br />
 <i>Like &#8216;chmod&#8217; it changes the mode of the ringbuffers resources. </i></p>
<h2>Detailed Description</h2>
<p>This implements a ring buffer that works in &#8216;chunks&#8217; not bytes. </p>
<p> So you write/read a complete chunk or not at all. There are two types of ring buffer normal and overwrite. Overwrite will reclaim the oldest chunks inorder to make way for new ones, the normal version will refuse to write a new chunk if the ring buffer is full. </p>
<p> This implementation is capable of working across processes, but one process must only write and the other prrocess read. </p>
<p> The read process will do the following: </p>
<pre>* rb = qb_rb_open(&quot;test2&quot;, 2000, QB_RB_FLAG_SHARED_PROCESS|QB_RB_FLAG_CREATE);
* for (i = 0; i &lt; 200; i++) {
* try_read_again:
* l = qb_rb_chunk_read(rb, (void *)out, 32, 1000);
* if (l &lt; 0) {
* goto try_read_again;
* }
* }
* ...
* qb_rb_close(rb);
* 
* </pre>
<p>The write process will do the following: </p>
<pre>* rb = qb_rb_open(&quot;test2&quot;, 2000, QB_RB_FLAG_SHARED_PROCESS);
* for (i = 0; i &lt; 200; i++) {
* try_write_again:
* l = qb_rb_chunk_write(rb, &amp;v, sizeof(v));
* if (l &lt; sizeof(v)) {
* goto try_write_again;
* }
* }
* ...
* qb_rb_close(rb);
* </pre>
<p><code>Author:</code></p>
<dl>
<dd>Angus Salkeld asalkeld [at] redhat.com</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define QB_RB_FLAG_CREATE 0x01</h3>
<p>create a ring buffer (rather than open and existing one) </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_open()</code></dl>
<h3>#define QB_RB_FLAG_NO_SEMAPHORE 0x10</h3>
<p>Don&#8217;t use semaphores, only atomic ops. This mean that the timeout passed into <code>qb_rb_chunk_read()</code> will be ignored.</p>
<h3>#define QB_RB_FLAG_OVERWRITE 0x02</h3>
<p>New calls to <code>qb_rb_chunk_write()</code> will call <code>qb_rb_chunk_reclaim()</code> if there is not enough space. If this is not set then new writes will be refused. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_open()</code></dl>
<h3>#define QB_RB_FLAG_SHARED_PROCESS 0x08</h3>
<p>The ringbuffer will be shared between processes. This effects the type of locks/semaphores that are used. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_open()</code></dl>
<h3>#define QB_RB_FLAG_SHARED_THREAD 0x04</h3>
<p>The ringbuffer will be shared between pthreads not processes. This effects the type of locks/semaphores that are used. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_open()</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct qb_ringbuffer_s <code>qb_ringbuffer_t</code></h3>
<h2>Function Documentation</h2>
<h3>int32_t qb_rb_chmod (<code>qb_ringbuffer_t</code> *rb, mode_tmode)</h3>
<p>Like &#8216;chmod&#8217; it changes the mode of the ringbuffers resources. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mode</i> mode to change to<br />
 <i>rb</i> ringbuffer instance</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>0</i> == ok<br />
 <i>-errno</i> for error</dl>
<h3>int32_t qb_rb_chown (<code>qb_ringbuffer_t</code> *rb, uid_towner, gid_tgroup)</h3>
<p>Like &#8216;chown&#8217; it changes the owner and group of the ringbuffers resources. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>owner</i> uid of the owner to change to<br />
 <i>group</i> gid of the group to change to<br />
 <i>rb</i> ringbuffer instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>status (0 = ok, -errno for error)</dl>
<h3>void* qb_rb_chunk_alloc (<code>qb_ringbuffer_t</code> *rb, size_tlen)</h3>
<p>Allocate space for a chunk of the given size. If type == QB_RB_FLAG_OVERWRITE and NULL is returned, memory corruption of the memory file has occured. The ringbuffer should be destroyed. If type == QB_RB_NORMAL then when there is not enough space it will return NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance<br />
 <i>len</i> (in) the size to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>pointer to chunk to write to, or NULL (if no space).</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_chunk_alloc()</code></dl>
<h3>int32_t qb_rb_chunk_commit (<code>qb_ringbuffer_t</code> *rb, size_tlen)</h3>
<p>finalize the chunk. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance<br />
 <i>len</i> (in) the size of the chunk.</dl>
<h3>ssize_t qb_rb_chunk_peek (<code>qb_ringbuffer_t</code> *rb, void **data_out, int32_tms_timeout)</h3>
<p>Read (without reclaiming) the last chunk. This function is a way of accessing the next chunk without a memcpy(). You can read the chunk data in place. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This function will not &#8216;pop&#8217; the chunk, you will need to call <code>qb_rb_chunk_reclaim()</code>.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance<br />
 <i>data_out</i> (out) a pointer to the next chunk to read (not copied).<br />
 <i>ms_timeout</i> (in) time to wait for new data.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the size of the chunk (0 if buffer empty).</dl>
<h3>ssize_t qb_rb_chunk_read (<code>qb_ringbuffer_t</code> *rb, void *data_out, size_tlen, int32_tms_timeout)</h3>
<p>Read the oldest chunk into data_out. This is the same as <code>qb_rb_chunk_peek()</code> memcpy() and <code>qb_rb_chunk_reclaim()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance<br />
 <i>data_out</i> (in/out) the chunk will be memcpy&#8217;ed into this.<br />
 <i>len</i> (in) the size of data_out.<br />
 <i>ms_timeout</i> the amount od time to wait for new data.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the size of the chunk, or error.</dl>
<h3>void qb_rb_chunk_reclaim (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>Reclaim the oldest chunk. You will need to call this if using <code>qb_rb_chunk_peek()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<h3>ssize_t qb_rb_chunk_write (<code>qb_ringbuffer_t</code> *rb, const void *data, size_tlen)</h3>
<p>Write a chunk to the ring buffer. This simply calls <code>qb_rb_chunk_alloc()</code> and then <code>qb_rb_chunk_commit()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance<br />
 <i>data</i> (in) the data to write<br />
 <i>len</i> (in) the size of the chunk.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the amount of bytes actually buffered (either len or -1).</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_chunk_alloc()</code> </p>
<p> <code>qb_rb_chunk_commit()</code></dl>
<h3>ssize_t qb_rb_chunks_used (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>The total number of chunks in the buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<h3>void qb_rb_close (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>Dereference the ringbuffer and if we are the last user destroy it. All files, mmaped memory, semaphores and locks will be destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<h3><code>qb_ringbuffer_t</code>* qb_rb_create_from_file (int32_tfd, uint32_tflags)</h3>
<p>Load the saved ring buffer from file into tempory memory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fd</i> file with saved ringbuffer data.<br />
 <i>flags</i> same flags as passed into <code>qb_rb_open()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dd>new ringbuffer instance</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_write_to_file()</code></dl>
<h3>char* qb_rb_name_get (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>Get the name of the ringbuffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>name.</dl>
<h3><code>qb_ringbuffer_t</code>* qb_rb_open (const char *name, size_tsize, uint32_tflags, size_tshared_user_data_size)</h3>
<p>Create the ring buffer with the given type. This creates allocates a ring buffer in shared memory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> the unique name of this ringbuffer.<br />
 <i>size</i> the requested size.<br />
 <i>flags</i> or&#8217;ed flags<br />
 <i>shared_user_data_size</i> size for a shared data area.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the actual size will be rounded up to the next page size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a new ring buffer or NULL if there was a problem.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>QB_RB_FLAG_CREATE</code>, <code>QB_RB_FLAG_OVERWRITE</code>, <code>QB_RB_FLAG_SHARED_THREAD</code>, <code>QB_RB_FLAG_SHARED_PROCESS</code></dl>
<h3>int32_t qb_rb_refcount_get (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>Get the reference count. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the number of references</dl>
<h3>void* qb_rb_shared_user_data_get (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>Get a point to user shared data area. </p>
<p> <code>Note:</code></p>
<dl>
<dd>this is of size &#8216;shared_user_data_size&#8217; passed into <code>qb_rb_open()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>pointer to shared data.</dl>
<h3>ssize_t qb_rb_space_free (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>The amount of free space in the ring buffer. </p>
<p> <code>Note:</code></p>
<dl>
<dd>Some of this space will be consumed by the chunk headers.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<h3>ssize_t qb_rb_space_used (<code>qb_ringbuffer_t</code> *rb)</h3>
<p>The total amount of data in the buffer. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This includes the chunk headers (8 bytes per chunk).</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rb</i> ringbuffer instance</dl>
<h3>ssize_t qb_rb_write_to_file (<code>qb_ringbuffer_t</code> *rb, int32_tfd)</h3>
<p>Write the contents of the Ring Buffer to file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fd</i> open file to write the ringbuffer data to.<br />
 <i>rb</i> ringbuffer instance</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_rb_create_from_file()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
