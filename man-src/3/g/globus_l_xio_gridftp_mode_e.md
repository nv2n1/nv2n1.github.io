---
title: "globus_l_xio_gridftp_mode_e(3)"
name: "globus_l_xio_gridftp_mode_e"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_l_xio_gridftp_mode_e/"
description: "Globus XIO GRIDFTP Client Driver –"
---

<h2 class="name">NAME</h2>
<p> Globus XIO GRIDFTP Client Driver &#8211; </p>
<h3>Typedefs</h3>
<p> typedef enum<br />
 <code>globus_l_xio_gridftp_mode_e</code> <code>globus_l_xio_gridftp_mode_t</code>&quot; </p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_gridftp_error_type_t</code> { <code>GLOBUS_XIO_GRIDFTP_ERROR_ATTR</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_SEEK</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER</code> } </p>
<p> enum <code>globus_xio_gridftp_cmd_t</code> { <code>GLOBUS_XIO_GRIDFTP_SEEK</code>, <code>GLOBUS_XIO_GRIDFTP_SET_HANDLE</code>, <code>GLOBUS_XIO_GRIDFTP_GET_HANDLE</code>, <code>GLOBUS_XIO_GRIDFTP_SET_APPEND</code>, <code>GLOBUS_XIO_GRIDFTP_GET_APPEND</code>, <code>GLOBUS_XIO_GRIDFTP_SET_ERET</code>, <code>GLOBUS_XIO_GRIDFTP_GET_ERET</code>, <code>GLOBUS_XIO_GRIDFTP_SET_ESTO</code>, <code>GLOBUS_XIO_GRIDFTP_GET_ESTO</code>, <code>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER</code>, <code>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER</code>, <code>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS</code>, <code>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS</code>, <code>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER</code>, <code>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER</code>, <code>GLOBUS_XIO_GRIDFTP_SET_MODE</code>, <code>GLOBUS_XIO_GRIDFTP_GET_MODE</code>, <code>GLOBUS_XIO_GRIDFTP_SET_AUTH</code>, <code>GLOBUS_XIO_GRIDFTP_GET_AUTH</code>, <code>GLOBUS_XIO_GRIDFTP_SET_DCAU</code>, <code>GLOBUS_XIO_GRIDFTP_GET_DCAU</code>, <code>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION</code>, <code>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION</code>, <code>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION</code>, <code>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION</code> } </p>
<p> enum <code>globus_l_xio_gridftp_mode_e</code> </p>
<h2>Detailed Description</h2>
<h2>Handles</h2>
<p> An XIO handle with the gridftp client driver can be created with globus_xio_handle_create() </p>
<p> The GridFTP client driver makes use of globus ftp client library. globus_xio_register_open() call creates a new ftp client handle (unless one is set on the attr passed), establishes connection with the GridFTP server. The contact string must contain the scheme, host name, and the resource, optionally it might contain port and subject also. </p>
<p> When the XIO handle is closed, the GridFTP driver will destroy its internal resources and the ftp client handle (unless this handle was set on an attr).</p>
<h2>Reading/Writing</h2>
<p> The globus_xio_register_read() enforce that the waitforbytes parameter should be one. When multiple TCP streams are used between the client and the server, data might not be delivered in order. globus_xio_data_descriptor_cntl() can be used to get the offset of the data. </p>
<p> globus_xio_register_write() does not enforce any restriction on the waitforbytes parameter. </p>
<p> In any case, when an error or EOF occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read/written before the error or EOF occurred.</p>
<h2>Environment Variables</h2>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_XIO_GRIDFTP_DEBUG Available if using a debug build. See globus_debug.h for format.</dl>
<h2>Attributes and Cntls</h2>
<p> GridFTP driver specific attrs and cntls. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_xio_attr_cntl () </p>
<p> globus_xio_handle_cntl () </p>
<p> globus_xio_data_descriptor_cntl ()</dl>
<h2>Types</h2>
<p> The errors reported by the GRIDFTP driver include GLOBUS_XIO_ERROR_EOF, GLOBUS_XIO_ERROR_CANCELED, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_SEEK</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE</code>, <code>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER</code> </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_xio_driver_error_match() </p>
<p> globus_error_errno_match()</dl>
<h2>Typedef Documentation</h2>
<h3>typedef enum <code>globus_l_xio_gridftp_mode_e</code> <code>globus_l_xio_gridftp_mode_t</code></h3>
<p> GRIDFTP driver specific types</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_l_xio_gridftp_mode_e</code></h3>
<p> GRIDFTP driver specific types</p>
<h3>enum <code>globus_xio_gridftp_cmd_t</code></h3>
<p> doxygen varargs filter stuff GRIDFTP driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_GRIDFTP_SEEK </i></p>
<dd> See usage for: <code>globus_xio_gridftp_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_HANDLE </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_HANDLE </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_APPEND </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_APPEND </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_ERET </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_ERET </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_ESTO </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_ESTO </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_MODE </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_MODE </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_AUTH </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_AUTH </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_DCAU </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_DCAU </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION </i></p>
<dd> See usage for: <code>globus_xio_gridftp_attr_cntl </code></dl>
<h3>enum <code>globus_xio_gridftp_error_type_t</code></h3>
<p> GridFTP driver specific error types </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_ATTR </i></p>
<dd> Indicates that an error occurred in the attribute control</p>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_SEEK </i></p>
<dd> Indicates that a seek has been called while there is an outstanding I/O</p>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ </i></p>
<dd> Indicates that a write has been called while there is an outstanding read</p>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE </i></p>
<dd> Indicates that a read has been called while there is an outstanding write</p>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ </i></p>
<dd> Indicates that a write has been called while there is a read pending</p>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE </i></p>
<dd> Indicates that a read has been called while there is a write pending</p>
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER </i></p>
<dd> Indicates that a second partial xfer has been initiated while the first one is still outstanding</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio_gridftp_driver from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAQ">Author</a></p>
<dd></dl>
