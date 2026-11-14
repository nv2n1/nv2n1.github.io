---
title: "acl_set_fd(3)"
name: "acl_set_fd"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_set_fd/"
description: "acl_set_fd – set an ACL by file descriptor"
---

<h2 class="name">NAME</h2>
<p> <code>acl_set_fd</code> &#8211; set an ACL by file descriptor </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_set_fd int fd acl_t acl</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_set_fd function associates an access ACL with the file referred to by <i>fd</i> </p>
<p> The effective user ID of the process must match the owner of the file or the process must have the CAP_FOWNER capability for the request to succeed.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_set_fd</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_set_fd function returns the value <code>-1</code> and and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EBADF</p>
<dd> The <i>fd</i> argument is not a valid file descriptor.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> does not point to a valid ACL. </p>
<p> The ACL has more entries than the file referred to by <i>fd</i> can obtain.</p>
<dt><code>Bq </code>Er ENOSPC</p>
<dd> The directory or file system that would contain the new ACL cannot be extended or the file system is out of file allocation resources.</p>
<dt><code>Bq </code>Er ENOTSUP</p>
<dd> The file identified by <i>fd </i> cannot be associated with the ACL because the file system on which the file is located does not support this.</p>
<dt><code>Bq </code>Er EPERM</p>
<dd> The process does not have appropriate privilege to perform the operation to set the ACL.</p>
<dt><code>Bq </code>Er EROFS</p>
<dd> This function requires modification of a file system which is currently read-only.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_delete_def_file3, acl_get_file3, acl_set_file3, acl_valid3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
