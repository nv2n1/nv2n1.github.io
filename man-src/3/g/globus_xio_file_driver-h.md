---
title: "globus_xio_file_driver-h(3)"
name: "globus_xio_file_driver-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_file_driver-h/"
description: "builtins/file/globus_xio_file_driver.h – XIO File Driver."
---

<p>builtins/file/globus_xio_file_driver.h &#8211; XIO File Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_xio_system.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_XIO_FILE_INVALID_HANDLE</code> </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_file_attr_cmd_t</code> { <code>GLOBUS_XIO_FILE_SET_MODE</code>, <code>GLOBUS_XIO_FILE_GET_MODE</code>, <code>GLOBUS_XIO_FILE_SET_FLAGS</code>, <code>GLOBUS_XIO_FILE_GET_FLAGS</code>, <code>GLOBUS_XIO_FILE_SET_TRUNC_OFFSET</code>, <code>GLOBUS_XIO_FILE_GET_TRUNC_OFFSET</code>, <code>GLOBUS_XIO_FILE_SET_HANDLE</code>, <code>GLOBUS_XIO_FILE_GET_HANDLE</code>, <code>GLOBUS_XIO_FILE_SET_BLOCKING_IO</code>, <code>GLOBUS_XIO_FILE_GET_BLOCKING_IO</code>, <code>GLOBUS_XIO_FILE_SEEK</code> } </p>
<p> enum <code>globus_xio_file_flag_t</code> { <code>GLOBUS_XIO_FILE_CREAT</code> = O_CREAT, <code>GLOBUS_XIO_FILE_EXCL</code> = O_EXCL, <code>GLOBUS_XIO_FILE_RDONLY</code> = O_RDONLY, <code>GLOBUS_XIO_FILE_WRONLY</code> = O_WRONLY, <code>GLOBUS_XIO_FILE_RDWR</code> = O_RDWR, <code>GLOBUS_XIO_FILE_TRUNC</code> = O_TRUNC, <code>GLOBUS_XIO_FILE_APPEND</code> = O_APPEND, <code>GLOBUS_XIO_FILE_BINARY</code> = 0, <code>GLOBUS_XIO_FILE_TEXT</code> = 0 } </p>
<p> enum <code>globus_xio_file_mode_t</code> { <code>GLOBUS_XIO_FILE_IRWXU</code> = S_IRWXU, <code>GLOBUS_XIO_FILE_IRUSR</code> = S_IRUSR, <code>GLOBUS_XIO_FILE_IWUSR</code> = S_IWUSR, <code>GLOBUS_XIO_FILE_IXUSR</code> = S_IXUSR, <code>GLOBUS_XIO_FILE_IRWXO</code> = S_IRWXO, <code>GLOBUS_XIO_FILE_IROTH</code> = S_IROTH, <code>GLOBUS_XIO_FILE_IWOTH</code> = S_IWOTH, <code>GLOBUS_XIO_FILE_IXOTH</code> = S_IXOTH, <code>GLOBUS_XIO_FILE_IRWXG</code> = S_IRWXG, <code>GLOBUS_XIO_FILE_IRGRP</code> = S_IRGRP, <code>GLOBUS_XIO_FILE_IWGRP</code> = S_IWGRP, <code>GLOBUS_XIO_FILE_IXGRP</code> = S_IXGRP } </p>
<p> enum <code>globus_xio_file_whence_t</code> { <code>GLOBUS_XIO_FILE_SEEK_SET</code> = SEEK_SET, <code>GLOBUS_XIO_FILE_SEEK_CUR</code> = SEEK_CUR, <code>GLOBUS_XIO_FILE_SEEK_END</code> = SEEK_END } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_SET_MODE</code>, int mode) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_GET_MODE</code>, int *mode_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_SET_FLAGS</code>, int flags) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_GET_FLAGS</code>, int *flags_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_SET_TRUNC_OFFSET</code>, globus_off_t offset) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_GET_TRUNC_OFFSET</code>, globus_off_t *offset_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_SET_HANDLE</code>, globus_xio_system_file_t handle) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_GET_HANDLE</code>, globus_xio_system_file_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_FILE_GET_HANDLE</code>, globus_xio_system_file_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_SET_BLOCKING_IO</code>, globus_bool_t use_blocking_io) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_FILE_SET_BLOCKING_IO</code>, globus_bool_t use_blocking_io) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_FILE_GET_BLOCKING_IO</code>, globus_bool_t *use_blocking_io_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_FILE_GET_BLOCKING_IO</code>, globus_bool_t *use_blocking_io_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_FILE_SEEK</code>, globus_off_t *in_out_offset, <code>globus_xio_file_whence_t</code> whence) </p>
<h2>Detailed Description</h2>
<p>XIO File Driver. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
