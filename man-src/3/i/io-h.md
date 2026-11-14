---
title: "io-h(3)"
name: "io-h"
section: "3"
letter: "i"
url: "/docs/linux/man/3-io-h/"
description: "io.h –"
---

<p>io.h &#8211; </p>
<p> C wrapper for I/O interfaces.</p>
<h2>Synopsis</h2>
<p>#include &#8216;dmlite.h&#8217;<br />
 #include &#8216;any.h&#8217;<br />
 #include &#8216;pool.h&#8217;<br />
 #include &lt;sys/uio.h&gt;<br />
 #include &lt;unistd.h&gt; </p>
<h3>Macros</h3>
<p>#define <code>O_INSECURE</code> 010 </p>
<h3>Typedefs</h3>
<p>typedef struct <code>dmlite_fd</code> <code>dmlite_fd</code> </p>
<h3>Functions</h3>
<p><code>dmlite_fd</code> * <code>dmlite_fopen</code> (<code>dmlite_context</code> *context, const char *path, int flags, const <code>dmlite_any_dict</code> *extra,&#8230;)<br />
 <i>Opens a file. </i><br />
 int <code>dmlite_fclose</code> (<code>dmlite_fd</code> *fd)<br />
 <i>Closes a file. </i><br />
 int <code>dmlite_fstat</code> (<code>dmlite_fd</code> *fd, struct stat *buf)<br />
 <i>Gets information about a file descriptor. </i><br />
 int <code>dmlite_fseek</code> (<code>dmlite_fd</code> *fd, off_t offset, int whence)<br />
 <i>Sets the file position. </i><br />
 off_t <code>dmlite_ftell</code> (<code>dmlite_fd</code> *fd)<br />
 <i>Returns the cursor position. </i><br />
 ssize_t <code>dmlite_fread</code> (<code>dmlite_fd</code> *fd, void *buffer, size_t count)<br />
 <i>Reads from a file. </i><br />
 ssize_t <code>dmlite_fwrite</code> (<code>dmlite_fd</code> *fd, const void *buffer, size_t count)<br />
 <i>Writes to a file. </i><br />
 ssize_t <code>dmlite_freadv</code> (<code>dmlite_fd</code> *fd, const struct iovec *vector, size_t count)<br />
 <i>Reads from a file into multiple buffers. </i><br />
 ssize_t <code>dmlite_fwritev</code> (<code>dmlite_fd</code> *fd, const struct iovec *vector, size_t count)<br />
 <i>Reads from a file into multiple buffers. </i><br />
 ssize_t <code>dmlite_fpread</code> (<code>dmlite_fd</code> *fd, void *buffer, size_t count, off_t offset)<br />
 <i>Reads up to count bytes starting at the given offset. Does not change internal offset. </i><br />
 ssize_t <code>dmlite_fpwrite</code> (<code>dmlite_fd</code> *fd, const void *buffer, size_t count, off_t offset)<br />
 <i>Writes count bytes starting at the given offset. Does not change internal offset. </i><br />
 int <code>dmlite_feof</code> (<code>dmlite_fd</code> *fd)<br />
 <i>Returns 1 if EOF. </i><br />
 int <code>dmlite_ferrno</code> (<code>dmlite_fd</code> *fd)<br />
 <i>Returns the last errror code. </i><br />
 const char * <code>dmlite_ferror</code> (<code>dmlite_fd</code> *fd)<br />
 <i>Returns the last error message. </i><br />
 int <code>dmlite_donewriting</code> (<code>dmlite_context</code> *context, const <code>dmlite_location</code> *loc)<br />
 <i>Finishes a PUT. </i><br />
 int <code>dmlite_fileno</code> (<code>dmlite_fd</code> *fd)<br />
 <i>Returns the system file descriptor if available. </i></p>
<h2>Detailed Description</h2>
<p>C wrapper for I/O interfaces. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define O_INSECURE 010</h3>
<p>Use this flag in addition to the standard ones to skip any security check (i.e. token validation)</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_fd</code> <code>dmlite_fd</code></h3>
<p>Handle for a file descriptor.</p>
<h2>Function Documentation</h2>
<h3>int dmlite_donewriting (<code>dmlite_context</code> *context, const <code>dmlite_location</code> *loc)</h3>
<p>Finishes a PUT. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>loc</i> The location as returned by dmlite_put.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_fclose (<code>dmlite_fd</code> *fd)</h3>
<p>Closes a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor as returned by dmlite_open.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_feof (<code>dmlite_fd</code> *fd)</h3>
<p>Returns 1 if EOF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 if there is more to read. 1 if EOF.</dl>
<h3>int dmlite_ferrno (<code>dmlite_fd</code> *fd)</h3>
<p>Returns the last errror code. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The last error code.</dl>
<h3>const char* dmlite_ferror (<code>dmlite_fd</code> *fd)</h3>
<p>Returns the last error message. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an internal buffer with the last error message.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This buffer is specific to each file descriptor.</dl>
<h3>int dmlite_fileno (<code>dmlite_fd</code> *fd)</h3>
<p>Returns the system file descriptor if available. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The file descriptor, -1 if it can not be retrieved.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Support depends on the plugin providing the file. </p>
<p> Calling dmlite_fclose <i>will</i> close the file descriptor returned by this.</dl>
<h3><code>dmlite_fd</code>* dmlite_fopen (<code>dmlite_context</code> *context, const char *path, intflags, const <code>dmlite_any_dict</code> *extra, &#8230;)</h3>
<p>Opens a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The path to open.<br />
 <i>flags</i> See open()<br />
 <i>extra</i> The key-value pairs.<br />
 <i>&#8230;</i> Should be mode_t when called with O_CREAT.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An opaque handler for the file, NULL on failure.</dl>
<h3>ssize_t dmlite_fpread (<code>dmlite_fd</code> *fd, void *buffer, size_tcount, off_toffset)</h3>
<p>Reads up to count bytes starting at the given offset. Does not change internal offset. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> File descriptor.<br />
 <i>buffer</i> Buffer where to put the data.<br />
 <i>count</i> Number of bytes to read.<br />
 <i>offset</i> Read offset.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes actually read on success. -1 on failure.</dl>
<h3>ssize_t dmlite_fpwrite (<code>dmlite_fd</code> *fd, const void *buffer, size_tcount, off_toffset)</h3>
<p>Writes count bytes starting at the given offset. Does not change internal offset. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> File descriptor.<br />
 <i>buffer</i> Data to write.<br />
 <i>count</i> Number of bytes to read.<br />
 <i>offset</i> Write offset.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes actually write on success. -1 on failure.</dl>
<h3>ssize_t dmlite_fread (<code>dmlite_fd</code> *fd, void *buffer, size_tcount)</h3>
<p>Reads from a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.<br />
 <i>buffer</i> Where to put the data.<br />
 <i>count</i> Number of bytes to read.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes actually read on success. -1 on failure.</dl>
<h3>ssize_t dmlite_freadv (<code>dmlite_fd</code> *fd, const struct iovec *vector, size_tcount)</h3>
<p>Reads from a file into multiple buffers. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.<br />
 <i>vector</i> Array of buffers.<br />
 <i>count</i> Number of elements in the array of buffers.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes actually read on success. -1 on failure.</dl>
<h3>int dmlite_fseek (<code>dmlite_fd</code> *fd, off_toffset, intwhence)</h3>
<p>Sets the file position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.<br />
 <i>offset</i> The offset.<br />
 <i>whence</i> See fseek()</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_fstat (<code>dmlite_fd</code> *fd, struct stat *buf)</h3>
<p>Gets information about a file descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.<br />
 <i>buf</i> Where to put the information.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Not all plug-ins will fill all the fields, but st_size is a reasonable expectation.</dl>
<h3>off_t dmlite_ftell (<code>dmlite_fd</code> *fd)</h3>
<p>Returns the cursor position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The cursor position, or -1 on error.</dl>
<h3>ssize_t dmlite_fwrite (<code>dmlite_fd</code> *fd, const void *buffer, size_tcount)</h3>
<p>Writes to a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.<br />
 <i>buffer</i> A pointer to the data.<br />
 <i>count</i> Number of bytes to write.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes actually written. -1 on failure.</dl>
<h3>ssize_t dmlite_fwritev (<code>dmlite_fd</code> *fd, const struct iovec *vector, size_tcount)</h3>
<p>Reads from a file into multiple buffers. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor.<br />
 <i>vector</i> Array of buffers.<br />
 <i>count</i> Number of elements in the array of buffers.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of bytes actually read on success. -1 on failure.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
