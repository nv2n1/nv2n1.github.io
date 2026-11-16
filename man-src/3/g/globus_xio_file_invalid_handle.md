---
title: "globus_xio_file_invalid_handle(3)"
name: "globus_xio_file_invalid_handle"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_file_invalid_handle/"
description: "Types –"
---

<p>Types &#8211; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_XIO_FILE_INVALID_HANDLE</code> </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_file_flag_t</code> { <code>GLOBUS_XIO_FILE_CREAT</code> = O_CREAT, <code>GLOBUS_XIO_FILE_EXCL</code> = O_EXCL, <code>GLOBUS_XIO_FILE_RDONLY</code> = O_RDONLY, <code>GLOBUS_XIO_FILE_WRONLY</code> = O_WRONLY, <code>GLOBUS_XIO_FILE_RDWR</code> = O_RDWR, <code>GLOBUS_XIO_FILE_TRUNC</code> = O_TRUNC, <code>GLOBUS_XIO_FILE_APPEND</code> = O_APPEND, <code>GLOBUS_XIO_FILE_BINARY</code> = 0, <code>GLOBUS_XIO_FILE_TEXT</code> = 0 } </p>
<p> enum <code>globus_xio_file_mode_t</code> { <code>GLOBUS_XIO_FILE_IRWXU</code> = S_IRWXU, <code>GLOBUS_XIO_FILE_IRUSR</code> = S_IRUSR, <code>GLOBUS_XIO_FILE_IWUSR</code> = S_IWUSR, <code>GLOBUS_XIO_FILE_IXUSR</code> = S_IXUSR, <code>GLOBUS_XIO_FILE_IRWXO</code> = S_IRWXO, <code>GLOBUS_XIO_FILE_IROTH</code> = S_IROTH, <code>GLOBUS_XIO_FILE_IWOTH</code> = S_IWOTH, <code>GLOBUS_XIO_FILE_IXOTH</code> = S_IXOTH, <code>GLOBUS_XIO_FILE_IRWXG</code> = S_IRWXG, <code>GLOBUS_XIO_FILE_IRGRP</code> = S_IRGRP, <code>GLOBUS_XIO_FILE_IWGRP</code> = S_IWGRP, <code>GLOBUS_XIO_FILE_IXGRP</code> = S_IXGRP } </p>
<p> enum <code>globus_xio_file_whence_t</code> { <code>GLOBUS_XIO_FILE_SEEK_SET</code> = SEEK_SET, <code>GLOBUS_XIO_FILE_SEEK_CUR</code> = SEEK_CUR, <code>GLOBUS_XIO_FILE_SEEK_END</code> = SEEK_END } </p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_XIO_FILE_INVALID_HANDLE</h3>
<p>Invalid handle type </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_HANDLE</code></dd></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_file_flag_t</code></h3>
<p>File driver open flags </p>
<p> OR together all the flags you want </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_FLAGS</code></dd></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_CREAT </i></dt>
<dd>Create a new file if it doesn&#8217;t exist (default)</dd>
<dt><i>GLOBUS_XIO_FILE_EXCL </i></dt>
<dd>Fail if file already exists</dd>
<dt><i>GLOBUS_XIO_FILE_RDONLY </i></dt>
<dd>Open for read only</dd>
<dt><i>GLOBUS_XIO_FILE_WRONLY </i></dt>
<dd>Open for write only</dd>
<dt><i>GLOBUS_XIO_FILE_RDWR </i></dt>
<dd>Open for reading and writing (default)</dd>
<dt><i>GLOBUS_XIO_FILE_TRUNC </i></dt>
<dd>Truncate file</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_TRUNC_OFFSET</code></dd></dl>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_APPEND </i></dt>
<dd>Open file for appending</dd>
<dt><i>GLOBUS_XIO_FILE_BINARY </i></dt>
<dd>File is binary (default)</dd>
<dt><i>GLOBUS_XIO_FILE_TEXT </i></dt>
<dd>File is text</dd></dl>
<h3>enum <code>globus_xio_file_mode_t</code></h3>
<p>File driver create mode </p>
<p> OR these modes together to get the mode you want. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_MODE</code></dd></dl>
<p> NOTE: for Win32, you only have a choice between read-only and read-write. If the chosen mode does not specify writing, the file will be read only </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_IRWXU </i></dt>
<dd>User read, write, and execute</dd>
<dt><i>GLOBUS_XIO_FILE_IRUSR </i></dt>
<dd>User read</dd>
<dt><i>GLOBUS_XIO_FILE_IWUSR </i></dt>
<dd>User write</dd>
<dt><i>GLOBUS_XIO_FILE_IXUSR </i></dt>
<dd>User execute</dd>
<dt><i>GLOBUS_XIO_FILE_IRWXO </i></dt>
<dd>Others read, write, and execute</dd>
<dt><i>GLOBUS_XIO_FILE_IROTH </i></dt>
<dd>Others read</dd>
<dt><i>GLOBUS_XIO_FILE_IWOTH </i></dt>
<dd>Others write</dd>
<dt><i>GLOBUS_XIO_FILE_IXOTH </i></dt>
<dd>Others execute</dd>
<dt><i>GLOBUS_XIO_FILE_IRWXG </i></dt>
<dd>Group read, write, and execute</dd>
<dt><i>GLOBUS_XIO_FILE_IRGRP </i></dt>
<dd>Group read</dd>
<dt><i>GLOBUS_XIO_FILE_IWGRP </i></dt>
<dd>Group write</dd>
<dt><i>GLOBUS_XIO_FILE_IXGRP </i></dt>
<dd>Group execute</dd></dl>
<h3>enum <code>globus_xio_file_whence_t</code></h3>
<p>File driver seek options </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SEEK</code></dd></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_SEEK_SET </i></dt>
<dd>set the file pointer at the specified offset</dd>
<dt><i>GLOBUS_XIO_FILE_SEEK_CUR </i></dt>
<dd>set the file pointer at current position + offset</dd>
<dt><i>GLOBUS_XIO_FILE_SEEK_END </i></dt>
<dd>set the file pointer at size of file + offset</dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
