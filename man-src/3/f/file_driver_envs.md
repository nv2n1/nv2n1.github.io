---
title: "file_driver_envs(3)"
name: "file_driver_envs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-file_driver_envs/"
---

<h2 class="name">NAME</h2>
 

 Env Variables - 

 The file driver uses the following environment variables
<dl>
<dt>*
<dd> GLOBUS_XIO_FILE_DEBUG Available if using a debug build.</dl>
 

 
&nbsp;<wbr> The file driver uses the following environment variables
<dl>
<dt>*
<dd> GLOBUS_XIO_FILE_DEBUG Available if using a debug build.</dl>
 

 

 

 See globus_debug.h for format. The File driver defines the levels TRACE for all function call tracing and INFO for write buffer sizes
<dl>
<dt>*
<dd> GLOBUS_XIO_SYSTEM_DEBUG Available if using a debug build. See globus_debug.h for format. The File driver uses globus_xio_system (along with the TCP and UDP drivers) which defines the following levels: TRACE for all function call tracing, DATA for data read and written counts, INFO for some special events, and RAW which dumps the raw buffers actually read or written. This can contain binary data, so be careful when you enable it.</dl>
 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus xio from the source code. 

<h2>Index</h2>


