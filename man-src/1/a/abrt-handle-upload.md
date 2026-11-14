---
title: "abrt-handle-upload(1)"
name: "abrt-handle-upload"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-handle-upload/"
---

<h2 class="name">NAME</h2>
 

 abrt-handle-upload - Unpacks and moves problem data. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-handle-upload</i> ABRT_DIR UPLOAD_DIR FILENAME

<h2>DESCRIPTION</h2>

 

 The tool unpacks FILENAME located in UPLOAD_DIR and moves the problem data found in it to ABRT_DIR. It supports unpacking tarballs compressed by gzip, bzip2 or xz. It's called by abrtd when a new file is noticed in the upload directory configured by the <i>WatchCrashdumpArchiveDir</i> option.

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5) 

<h2>Index</h2>


