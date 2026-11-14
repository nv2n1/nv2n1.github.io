---
title: "acl_delete_def_file(3)"
name: "acl_delete_def_file"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_delete_def_file/"
description: "acl_delete_def_file – delete a default ACL by filename"
---

<h2 class="name">NAME</h2>
<p> <code>acl_delete_def_file</code> &#8211; delete a default ACL by filename </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_delete_def_file const char *path_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_delete_def_file function deletes a default ACL from the directory whose pathname is pointed to by the argument <i>path_p</i> </p>
<p> The effective user ID of the process must match the owner of the file or directory or the process must have the CAP_FOWNER capability for the request to succeed. </p>
<p> If the argument <i>path_p</i> is not a directory, then the function fails. It is no error if the directory whose pathname is pointed to by the argument <i>path_p</i> does not have a default ACL.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_delete_def_file</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_delete_def_file function returns the value <code>-1</code> and and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The file referred to by <i>path_p</i> is not a directory.</p>
<dt><code>Bq </code>Er ENOTSUP</p>
<dd> The file system on which the file identified by <i>path_p</i> is located does not support ACLs, or ACLs are disabled.</p>
<dt><code>Bq </code>Er EPERM</p>
<dd> The process does not have appropriate privilege to perform the operation to delete the default ACL.</p>
<dt><code>Bq </code>Er EROFS</p>
<dd> This function requires modification of a file system which is currently read-only.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_get_file3, acl_set_file3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
