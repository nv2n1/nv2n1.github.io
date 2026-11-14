---
title: "globus_xio_file_irusr(3)"
name: "globus_xio_file_irusr"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_file_irusr/"
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
<dd><code>GLOBUS_XIO_FILE_SET_HANDLE</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_file_flag_t</code></h3>
<p>File driver open flags </p>
<p> OR together all the flags you want </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_FLAGS</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_CREAT </i></p>
<dd>Create a new file if it doesn&#8217;t exist (default)</p>
<dt><i>GLOBUS_XIO_FILE_EXCL </i></p>
<dd>Fail if file already exists</p>
<dt><i>GLOBUS_XIO_FILE_RDONLY </i></p>
<dd>Open for read only</p>
<dt><i>GLOBUS_XIO_FILE_WRONLY </i></p>
<dd>Open for write only</p>
<dt><i>GLOBUS_XIO_FILE_RDWR </i></p>
<dd>Open for reading and writing (default)</p>
<dt><i>GLOBUS_XIO_FILE_TRUNC </i></p>
<dd>Truncate file</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_TRUNC_OFFSET</code></dl>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_APPEND </i></p>
<dd>Open file for appending</p>
<dt><i>GLOBUS_XIO_FILE_BINARY </i></p>
<dd>File is binary (default)</p>
<dt><i>GLOBUS_XIO_FILE_TEXT </i></p>
<dd>File is text</dl>
<h3>enum <code>globus_xio_file_mode_t</code></h3>
<p>File driver create mode </p>
<p> OR these modes together to get the mode you want. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SET_MODE</code></dl>
<p> NOTE: for Win32, you only have a choice between read-only and read-write. If the chosen mode does not specify writing, the file will be read only </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_IRWXU </i></p>
<dd>User read, write, and execute</p>
<dt><i>GLOBUS_XIO_FILE_IRUSR </i></p>
<dd>User read</p>
<dt><i>GLOBUS_XIO_FILE_IWUSR </i></p>
<dd>User write</p>
<dt><i>GLOBUS_XIO_FILE_IXUSR </i></p>
<dd>User execute</p>
<dt><i>GLOBUS_XIO_FILE_IRWXO </i></p>
<dd>Others read, write, and execute</p>
<dt><i>GLOBUS_XIO_FILE_IROTH </i></p>
<dd>Others read</p>
<dt><i>GLOBUS_XIO_FILE_IWOTH </i></p>
<dd>Others write</p>
<dt><i>GLOBUS_XIO_FILE_IXOTH </i></p>
<dd>Others execute</p>
<dt><i>GLOBUS_XIO_FILE_IRWXG </i></p>
<dd>Group read, write, and execute</p>
<dt><i>GLOBUS_XIO_FILE_IRGRP </i></p>
<dd>Group read</p>
<dt><i>GLOBUS_XIO_FILE_IWGRP </i></p>
<dd>Group write</p>
<dt><i>GLOBUS_XIO_FILE_IXGRP </i></p>
<dd>Group execute</dl>
<h3>enum <code>globus_xio_file_whence_t</code></h3>
<p>File driver seek options </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_FILE_SEEK</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_FILE_SEEK_SET </i></p>
<dd>set the file pointer at the specified offset</p>
<dt><i>GLOBUS_XIO_FILE_SEEK_CUR </i></p>
<dd>set the file pointer at current position + offset</p>
<dt><i>GLOBUS_XIO_FILE_SEEK_END </i></p>
<dd>set the file pointer at size of file + offset</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
