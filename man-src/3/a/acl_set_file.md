---
title: "acl_set_file(3)"
name: "acl_set_file"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_set_file/"
description: "acl_set_file – set an ACL by filename"
---

<h2 class="name">NAME</h2>
<p> <code>acl_set_file</code> &#8211; set an ACL by filename </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_set_file const char *path_p acl_type_t type acl_t acl</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_set_file function associates an access ACL with a file or directory, or associates a default ACL with a directory. The pathname for the file or directory is pointed to by the argument <i>path_p</i> </p>
<p> The effective user ID of the process must match the owner of the file or directory or the process must have the CAP_FOWNER capability for the request to succeed. </p>
<p> The value of the argument <i>type</i> is used to indicate whether the access ACL or the default ACL associated with <i>path_p</i> is being set. If the <i>type</i> parameter is ACL_TYPE_ACCESS, the access ACL of <i>path_p</i> shall be set. If the <i>type</i> parameter is ACL_TYPE_DEFAULT, the default ACL of <i>path_p</i> shall be set. If the argument <i>type</i> specifies a type of ACL that cannot be associated with <i>path_p</i> then the function fails. </p>
<p> The <i>acl</i> parameter must reference a valid ACL according to the rules described on the acl_valid3 manual page if the <i>type</i> parameter is ACL_TYPE_ACCESS, and must either reference a valid ACL or an ACL with zero ACL entries if the <i>type</i> parameter is ACL_TYPE_DEFAULT. If the <i>acl</i> parameter references an empty ACL, then the Fn acl_set_file function removes any default ACL associated with the directory referred to by the <i>path_p</i> parameter.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_set_file</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_set_file function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EACCES</p>
<dd> Search permission is denied for a component of the path prefix or the object exists and the process does not have appropriate access rights. </p>
<p> Argument <i>type</i> specifies a type of ACL that cannot be associated with <i>path_p</i></p>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> does not point to a valid ACL. </p>
<p> The ACL has more entries than the file referred to by <i>path_p</i> can obtain. </p>
<p> The <i>type</i> parameter is not ACL_TYPE_ACCESS or ACL_TYPE_DEFAULT. </p>
<p> The <i>type</i> parameter is ACL_TYPE_DEFAULT, but the file referred to by <i>path_p</i> is not a directory.</p>
<dt><code>Bq </code>Er ENAMETOOLONG</p>
<dd> The length of the argument <i>path_p</i> is too long.</p>
<dt><code>Bq </code>Er ENOENT</p>
<dd> The named object does not exist or the argument <i>path_p</i> points to an empty string.</p>
<dt><code>Bq </code>Er ENOSPC</p>
<dd> The directory or file system that would contain the new ACL cannot be extended or the file system is out of file allocation resources.</p>
<dt><code>Bq </code>Er ENOTDIR</p>
<dd> A component of the path prefix is not a directory.</p>
<dt><code>Bq </code>Er ENOTSUP</p>
<dd> The file identified by <i>path_p </i> cannot be associated with the ACL because the file system on which the file is located does not support this.</p>
<dt><code>Bq </code>Er EPERM</p>
<dd> The process does not have appropriate privilege to perform the operation to set the ACL.</p>
<dt><code>Bq </code>Er EROFS</p>
<dd> This function requires modification of a file system which is currently read-only.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned) </p>
<p> The behavior of Fn acl_set_file when the <i>acl</i> parameter refers to an empty ACL and the <i>type</i> parameter is ACL_TYPE_DEFAULT is an extension in the Linux implementation, in order that all values returned by Fn acl_get_file can be passed to Fn acl_set_file . The POSIX.1e function for removing a default ACL is Fn acl_delete_def_file .</p>
<h2>SEE ALSO</h2>
<p> acl_delete_def_file3, acl_get_file3, acl_set_fd3, acl_valid3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
