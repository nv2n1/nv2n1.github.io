---
title: "globus_xio_gridftp_set_eret(3)"
name: "globus_xio_gridftp_set_eret"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_gridftp_set_eret/"
---

Globus XIO GRIDFTP Client Driver - 

<h3>Typedefs</h3>typedef enum 
 <b>globus_l_xio_gridftp_mode_e</b> <b>globus_l_xio_gridftp_mode_t</b>&quot; 

<h3>Enumerations</h3>enum <b>globus_xio_gridftp_error_type_t</b> { <b>GLOBUS_XIO_GRIDFTP_ERROR_ATTR</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_SEEK</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER</b> } 
 
 enum <b>globus_xio_gridftp_cmd_t</b> { <b>GLOBUS_XIO_GRIDFTP_SEEK</b>, <b>GLOBUS_XIO_GRIDFTP_SET_HANDLE</b>, <b>GLOBUS_XIO_GRIDFTP_GET_HANDLE</b>, <b>GLOBUS_XIO_GRIDFTP_SET_APPEND</b>, <b>GLOBUS_XIO_GRIDFTP_GET_APPEND</b>, <b>GLOBUS_XIO_GRIDFTP_SET_ERET</b>, <b>GLOBUS_XIO_GRIDFTP_GET_ERET</b>, <b>GLOBUS_XIO_GRIDFTP_SET_ESTO</b>, <b>GLOBUS_XIO_GRIDFTP_GET_ESTO</b>, <b>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER</b>, <b>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER</b>, <b>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS</b>, <b>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS</b>, <b>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER</b>, <b>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER</b>, <b>GLOBUS_XIO_GRIDFTP_SET_MODE</b>, <b>GLOBUS_XIO_GRIDFTP_GET_MODE</b>, <b>GLOBUS_XIO_GRIDFTP_SET_AUTH</b>, <b>GLOBUS_XIO_GRIDFTP_GET_AUTH</b>, <b>GLOBUS_XIO_GRIDFTP_SET_DCAU</b>, <b>GLOBUS_XIO_GRIDFTP_GET_DCAU</b>, <b>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION</b>, <b>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION</b>, <b>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION</b>, <b>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION</b> } 
 
 enum <b>globus_l_xio_gridftp_mode_e</b> 

<h2>Detailed Description</h2><h2>Handles</h2>An XIO handle with the gridftp client driver can be created with globus_xio_handle_create() 

 The GridFTP client driver makes use of globus ftp client library. globus_xio_register_open() call creates a new ftp client handle (unless one is set on the attr passed), establishes connection with the GridFTP server. The contact string must contain the scheme, host name, and the resource, optionally it might contain port and subject also. 

 When the XIO handle is closed, the GridFTP driver will destroy its internal resources and the ftp client handle (unless this handle was set on an attr).
<h2>Reading/Writing</h2>The globus_xio_register_read() enforce that the waitforbytes parameter should be one. When multiple TCP streams are used between the client and the server, data might not be delivered in order. globus_xio_data_descriptor_cntl() can be used to get the offset of the data. 

 globus_xio_register_write() does not enforce any restriction on the waitforbytes parameter. 

 In any case, when an error or EOF occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read/written before the error or EOF occurred.
<h2>Environment Variables</h2><dl COMPACT><dt>&bull;
<dd>GLOBUS_XIO_GRIDFTP_DEBUG Available if using a debug build. See globus_debug.h for format.</dl><h2>Attributes and Cntls</h2>GridFTP driver specific attrs and cntls. 

 <b>See Also:</b>
<dl COMPACT><dd>globus_xio_attr_cntl () 

 globus_xio_handle_cntl () 

 globus_xio_data_descriptor_cntl ()</dl><h2>Types</h2>The errors reported by the GRIDFTP driver include GLOBUS_XIO_ERROR_EOF, GLOBUS_XIO_ERROR_CANCELED, <b>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_SEEK</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE</b>, <b>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER</b> 

 <b>See Also:</b>
<dl COMPACT><dd>globus_xio_driver_error_match() 

 globus_error_errno_match()</dl><h2>Typedef Documentation</h2><h3>typedef enum <b>globus_l_xio_gridftp_mode_e</b> <b>globus_l_xio_gridftp_mode_t</b></h3>GRIDFTP driver specific types
<h2>Enumeration Type Documentation</h2><h3>enum <b>globus_l_xio_gridftp_mode_e</b></h3>GRIDFTP driver specific types
<h3>enum <b>globus_xio_gridftp_cmd_t</b></h3>doxygen varargs filter stuff GRIDFTP driver specific cntls 

 <b>Enumerator</b>
<dl COMPACT><dt><i>GLOBUS_XIO_GRIDFTP_SEEK </i>
<dd>See usage for: <b>globus_xio_gridftp_handle_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_HANDLE </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_HANDLE </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_APPEND </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_APPEND </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_ERET </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_ERET </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_ESTO </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_ESTO </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_PARTIAL_TRANSFER </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_PARTIAL_TRANSFER </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_NUM_STREAMS </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_NUM_STREAMS </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_TCP_BUFFER </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_TCP_BUFFER </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_MODE </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_MODE </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_AUTH </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_AUTH </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_DCAU </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_DCAU </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_DATA_PROTECTION </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_DATA_PROTECTION </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_SET_CONTROL_PROTECTION </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b>
<dt><i>GLOBUS_XIO_GRIDFTP_GET_CONTROL_PROTECTION </i>
<dd>See usage for: <b>globus_xio_gridftp_attr_cntl </b></dl><h3>enum <b>globus_xio_gridftp_error_type_t</b></h3>GridFTP driver specific error types 

 <b>Enumerator</b>
<dl COMPACT><dt><i>GLOBUS_XIO_GRIDFTP_ERROR_ATTR </i>
<dd>Indicates that an error occurred in the attribute control
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_SEEK </i>
<dd>Indicates that a seek has been called while there is an outstanding I/O
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_READ </i>
<dd>Indicates that a write has been called while there is an outstanding read
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_WRITE </i>
<dd>Indicates that a read has been called while there is an outstanding write
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_READ </i>
<dd>Indicates that a write has been called while there is a read pending
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_PENDING_WRITE </i>
<dd>Indicates that a read has been called while there is a write pending
<dt><i>GLOBUS_XIO_GRIDFTP_ERROR_OUTSTANDING_PARTIAL_XFER </i>
<dd>Indicates that a second partial xfer has been initiated while the first one is still outstanding</dl><h2>Author</h2>Generated automatically by Doxygen for globus_xio_gridftp_driver from the source code.
