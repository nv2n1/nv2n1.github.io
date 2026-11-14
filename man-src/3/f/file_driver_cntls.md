---
title: "file_driver_cntls(3)"
name: "file_driver_cntls"
section: "3"
letter: "f"
url: "/docs/linux/man/3-file_driver_cntls/"
description: "Attributes and Cntls –"
---

<h2 class="name">NAME</h2>
<p> Attributes and Cntls &#8211; </p>
<p> File driver specific attrs and cntls.</p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_file_attr_cmd_t</code> { <code>GLOBUS_XIO_FILE_SET_MODE</code>, <code>GLOBUS_XIO_FILE_GET_MODE</code>, <code>GLOBUS_XIO_FILE_SET_FLAGS</code>, <code>GLOBUS_XIO_FILE_GET_FLAGS</code>, <code>GLOBUS_XIO_FILE_SET_TRUNC_OFFSET</code>, <code>GLOBUS_XIO_FILE_GET_TRUNC_OFFSET</code>, <code>GLOBUS_XIO_FILE_SET_HANDLE</code>, <code>GLOBUS_XIO_FILE_GET_HANDLE</code>, <code>GLOBUS_XIO_FILE_SET_BLOCKING_IO</code>, <code>GLOBUS_XIO_FILE_GET_BLOCKING_IO</code>, <code>GLOBUS_XIO_FILE_SEEK</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_SET_MODE, int mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_GET_MODE, int *mode_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_SET_FLAGS, int flags) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_GET_FLAGS, int *flags_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_SET_TRUNC_OFFSET, globus_off_t offset) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_GET_TRUNC_OFFSET, globus_off_t *offset_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_SET_HANDLE, globus_xio_system_file_t handle) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_GET_HANDLE, globus_xio_system_file_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_FILE_GET_HANDLE, globus_xio_system_file_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_SET_BLOCKING_IO, globus_bool_t use_blocking_io) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_FILE_SET_BLOCKING_IO, globus_bool_t use_blocking_io) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_FILE_GET_BLOCKING_IO, globus_bool_t *use_blocking_io_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_FILE_GET_BLOCKING_IO, globus_bool_t *use_blocking_io_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_FILE_SEEK, globus_off_t *in_out_offset, <code>globus_xio_file_whence_t</code> whence) </p>
<h2>Detailed Description</h2>
<p> File driver specific attrs and cntls. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_file_attr_cmd_t</code></h3>
<p> doxygen varargs filter stuff File driver specific cntls </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_FILE_SET_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_GET_MODE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_SET_FLAGS </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_GET_FLAGS </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_SET_TRUNC_OFFSET </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_GET_TRUNC_OFFSET </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_SET_HANDLE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_GET_HANDLE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_SET_BLOCKING_IO </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_GET_BLOCKING_IO </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_FILE_SEEK </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_SET_MODE, int mode)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the file create mode. Use this to set the permissions a non-existent file is created with, The default mode is 0644. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mode</i> A bitwise OR of all the modes desired</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_file_mode_t</code></dl>
<p> string opt: mode=&lt;int&gt;</p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_GET_MODE, int * mode_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the file create mode. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mode_out</i> The current mode will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_SET_FLAGS, int flags)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the file open flags. The default flags specify to create the file if it doesn&#8217;t exist, open it for reading and writing, and interpret it as a binary file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>flags</i> A bitwise OR of all the flags desired</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_file_flag_t</code></dl>
<p> string opt: flags=&lt;int&gt;</p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_GET_FLAGS, int * flags_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the file open flags. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>flags_out</i> The current flags will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_SET_TRUNC_OFFSET, globus_off_t offset)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the file truncate offset. Use this in conjunction with the <code>GLOBUS_XIO_FILE_TRUNC</code> flag to truncate a file to a non-zero offset. If the file was larger than offset bytes, the extra data is lost. If the file was shorter or non-existent, it is extended and the extended part reads as zeros. (default is 0) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>offset</i> The desired size of the file.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_GET_TRUNC_OFFSET, globus_off_t * offset_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the file truncate offset. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>offset_out</i> The offset will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_SET_HANDLE, globus_xio_system_file_t handle)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the file handle to use. Do not open a new file, use this preopened handle instead. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Use this handle (fd or HANDLE) for the file. Note: close() will not be called on this handle.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_GET_HANDLE, globus_xio_system_file_t * handle_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the file handle in use or in attr. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_out</i> The file handle (fd or HANDLE) will be stored here. If none is set, GLOBUS_XIO_TCP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_FILE_GET_HANDLE, globus_xio_system_file_t * handle_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the file handle in use or in attr. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_out</i> The file handle (fd or HANDLE) will be stored here. If none is set, GLOBUS_XIO_TCP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_SET_BLOCKING_IO, globus_bool_t use_blocking_io)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable true blocking io when making globus_xio_read/write() calls. Note: use with caution. you can deadlock an entire app with this. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io</i> If GLOBUS_TRUE, true blocking io will be enabled. GLOBUS_FALSE will disable it (default);</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_FILE_SET_BLOCKING_IO, globus_bool_t use_blocking_io)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable true blocking io when making globus_xio_read/write() calls. Note: use with caution. you can deadlock an entire app with this. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io</i> If GLOBUS_TRUE, true blocking io will be enabled. GLOBUS_FALSE will disable it (default);</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_FILE_GET_BLOCKING_IO, globus_bool_t * use_blocking_io_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the blocking io status in use or in attr. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io_out</i> The flag will be set here. GLOBUS_TRUE for enabled.</dl>
<p> string opt: blocking=&lt;bool&gt;</p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_FILE_GET_BLOCKING_IO, globus_bool_t * use_blocking_io_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the blocking io status in use or in attr. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io_out</i> The flag will be set here. GLOBUS_TRUE for enabled.</dl>
<p> string opt: blocking=&lt;bool&gt;</p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_FILE_SEEK, globus_off_t * in_out_offset, <code>globus_xio_file_whence_t</code> whence)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Reposition read/write file offset. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>in_out_offset</i> Specify the desired offset (according to whence). On success, the actual file offset will be stored here.<br />
 <i>whence</i> Specify how offset should be interpreted.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_file_whence_t</code> </p>
<p> <code>GLOBUS_XIO_SEEK</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAW">Author</a></p>
<dd></dl>
