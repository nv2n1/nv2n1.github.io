---
title: "acl_get_file(3)"
name: "acl_get_file"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_get_file/"
description: "acl_get_file – get an ACL by filename"
---

<h2 class="name">NAME</h2>
<p> <code>acl_get_file</code> &#8211; get an ACL by filename </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft acl_t Fn acl_get_file const char *path_p acl_type_t type</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_get_file function retrieves the access ACL associated with a file or directory, or the default ACL associated with a directory. The pathname for the file or directory is pointed to by the argument <i>path_p</i> The ACL is placed into working storage and Fn acl_get_file returns a pointer to that storage. </p>
<p> In order to read an ACL from an object, a process must have read access to the object&#8217;s attributes. </p>
<p> The value of the argument <i>type</i> is used to indicate whether the access ACL or the default ACL associated with <i>path_p</i> is returned. If <i>type</i> is ACL_TYPE_ACCESS, the access ACL of <i>path_p</i> is returned. If <i>type</i> is ACL_TYPE_DEFAULT, the default ACL of <i>path_p</i> is returned. If <i>type</i> is ACL_TYPE_DEFAULT and no default ACL is associated with the directory <i>path_p</i> then an ACL containing zero ACL entries is returned. If <i>type</i> specifies a type of ACL that cannot be associated with <i>path_p</i> then the function fails. </p>
<p> This function may cause memory to be allocated. The caller should free any releasable memory, when the new ACL is no longer required, by calling acl_free3 with the <i>(void*)acl_t</i> returned by Fn acl_get_file as an argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns a pointer to the working storage. On error, a value of <code>(acl_t)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_get_file function returns a value of <code>(acl_t)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EACCES</p>
<dd> Search permission is denied for a component of the path prefix or the object exists and the process does not have appropriate access rights. </p>
<p> Argument <i>type</i> specifies a type of ACL that cannot be associated with <i>path_p</i></p>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>type</i> is not ACL_TYPE_ACCESS or ACL_TYPE_DEFAULT.</p>
<dt><code>Bq </code>Er ENAMETOOLONG</p>
<dd> The length of the argument <i>path_p</i> is too long.</p>
<dt><code>Bq </code>Er ENOENT</p>
<dd> The named object does not exist or the argument <i>path_p</i> points to an empty string.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The ACL working storage requires more memory than is allowed by the hardware or system-imposed memory management constraints.</p>
<dt><code>Bq </code>Er ENOTDIR</p>
<dd> A component of the path prefix is not a directory.</p>
<dt><code>Bq </code>Er ENOTSUP</p>
<dd> The file system on which the file identified by <i>path_p</i> is located does not support ACLs, or ACLs are disabled.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_free3, acl_get_entry3, acl_get_fd3, acl_set_file3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
