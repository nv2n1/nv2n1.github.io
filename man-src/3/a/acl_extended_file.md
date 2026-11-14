---
title: "acl_extended_file(3)"
name: "acl_extended_file"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_extended_file/"
description: "acl_extended_file, acl_extended_file_nofollow – test for information in ACLs by file name"
---

<h2 class="name">NAME</h2>
<p> <code>acl_extended_file, acl_extended_file_nofollow</code> &#8211; test for information in ACLs by file name </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_extended_file const char *path_p Ft int Fn acl_extended_file_nofollow const char *path_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_extended_file function returns <code>1</code> if the file or directory referred to by the argument <i>path_p</i> is associated with an extended access ACL, or if the directory referred to by <i>path_p</i> is associated with a default ACL. The function returns <code>0</code> if the file has neither an extended access ACL nor a default ACL. </p>
<p> An extended ACL is an ACL that contains entries other than the three required entries of tag types ACL_USER_OBJ, ACL_GROUP_OBJ and ACL_OTHER. If the result of the Fn acl_extended_file function for a file object is <code>0</code> then ACLs define no discretionary access rights other than those already defined by the traditional file permission bits. </p>
<p> Access to the file object may be further restricted by other mechanisms, such as Mandatory Access Control schemes. The <a href="/docs/linux/man/2-access/">access</a>(2) system call can be used to check whether a given type of access to a file object would be granted. </p>
<p> Fn acl_extended_file_nofollow is identical to Fn acl_extended_file , except in the case of a symbolic link, where the link itself is interrogated, not the file that it refers to. Since symbolic links have no ACL themselves, the operation is supposed to fail on them.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the Fn acl_extended_file function returns <code>1</code> if the file object referred to by <i>path_p</i> has an extended access ACL or a default ACL, and <code>0</code> if the file object referred to by <i>path_p</i> has neither an extended access ACL nor a default ACL. Otherwise, the value <code>-1</code> is returned and the global variable <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_extended_file function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EACCES</p>
<dd> Search permission is denied for a component of the path prefix.</p>
<dt><code>Bq </code>Er ENAMETOOLONG</p>
<dd> The length of the argument <i>path_p</i> is too long.</p>
<dt><code>Bq </code>Er ENOENT</p>
<dd> The named object does not exist or the argument <i>path_p</i> points to an empty string.</p>
<dt><code>Bq </code>Er ENOTDIR</p>
<dd> A component of the path prefix is not a directory.</p>
<dt><code>Bq </code>Er ENOTSUP</p>
<dd> The file system on which the file identified by <i>path_p</i> is located does not support ACLs, or ACLs are disabled.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-access/">access</a>(2), acl_get_file3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
