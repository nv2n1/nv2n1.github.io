---
title: "wl_shm_buffer(3)"
name: "wl_shm_buffer"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_shm_buffer/"
description: "wl_shm_buffer –"
---

<p>wl_shm_buffer &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>void * wl_shm_buffer_get_data (struct wl_shm_buffer *buffer)



void wl_shm_buffer_begin_access (struct wl_shm_buffer *buffer)



void wl_shm_buffer_end_access (struct wl_shm_buffer *buffer)



Public Attributes
struct wl_resource * resource



int32_t width



int32_t height



int32_t stride



uint32_t format



int offset



struct wl_shm_pool * pool</code></pre>
<h2>Member Function Documentation</h2>
<h3>void wl_shm_buffer_begin_access (struct <code>wl_shm_buffer</code> *buffer)</h3>
<p>Mark that the given SHM buffer is about to be accessed </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> The SHM buffer</dl>
<p> An SHM buffer is a memory-mapped file given by the client. According to POSIX, reading from a memory-mapped region that extends off the end of the file will cause a SIGBUS signal to be generated. Normally this would cause the compositor to terminate. In order to make the compositor robust against clients that change the size of the underlying file or lie about its size, you should protect access to the buffer by calling this function before reading from the memory and call wl_shm_buffer_end_access afterwards. This will install a signal handler for SIGBUS which will prevent the compositor from crashing. </p>
<p> After calling this function the signal handler will remain installed for the lifetime of the compositor process. Note that this function will not work properly if the compositor is also installing its own handler for SIGBUS. </p>
<p> If a SIGBUS signal is received for an address within the range of the SHM pool of the given buffer then the client will be sent an error event when wl_shm_buffer_end_access is called. If the signal is for an address outside that range then the signal handler will reraise the signal which would will likely cause the compositor to terminate. </p>
<p> It is safe to nest calls to these functions as long as the nested calls are all accessing the same buffer. The number of calls to wl_shm_buffer_end_access must match the number of calls to wl_shm_buffer_begin_access. These functions are thread-safe and it is allowed to simultaneously access different buffers or the same buffer from multiple threads.</p>
<h3>void wl_shm_buffer_end_access (struct <code>wl_shm_buffer</code> *buffer)</h3>
<p>Ends the access to a buffer started by wl_shm_buffer_begin_access </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> The SHM buffer</dl>
<p> This should be called after wl_shm_buffer_begin_access once the buffer is no longer being accessed. If a SIGBUS signal was generated in-between these two calls then the resource for the given buffer will be sent an error.</p>
<h3>void * wl_shm_buffer_get_data (struct <code>wl_shm_buffer</code> *buffer)</h3>
<p>Get a pointer to the memory for the SHM buffer </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> The buffer object</dl>
<p> Returns a pointer which can be used to read the data contained in the given SHM buffer. </p>
<p> As this buffer is memory-mapped, reading it from may generate SIGBUS signals. This can happen if the client claims that the buffer is larger than it is or if something truncates the underlying file. To prevent this signal from causing the compositor to crash you should call wl_shm_buffer_begin_access and wl_shm_buffer_end_access around code that reads from the memory.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
