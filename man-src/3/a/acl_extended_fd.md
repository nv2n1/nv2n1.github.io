---
title: "acl_extended_fd(3)"
name: "acl_extended_fd"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_extended_fd/"
description: "acl_extended_fd – test for information in the ACL by file descriptor"
---

<h2 class="name">NAME</h2>
<p> <code>acl_extended_fd</code> &#8211; test for information in the ACL by file descriptor </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_extended_fd int fd</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_extended_fd function returns <code>1</code> if the file identified by the argument <i>fd</i> is associated with an extended access ACL. The function returns <code>0</code> if the file does not have an extended access ACL. </p>
<p> An extended ACL is an ACL that contains entries other than the three required entries of tag types ACL_USER_OBJ, ACL_GROUP_OBJ and ACL_OTHER. If the result of the Fn acl_extended_fd function for a file object is <code>0</code> then the ACL defines no discretionary access rights other than those already defined by the traditional file permission bits. </p>
<p> Access to the file object may be further restricted by other mechanisms, such as Mandatory Access Control schemes. The <a href="/docs/linux/man/2-access/">access</a>(2) system call can be used to check whether a given type of access to a file object would be granted.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the Fn acl_extended_fd function returns <code>1</code> if the file object identified by <i>fd</i> has an extended access ACL, and <code>0</code> if the file object identified by <i>fd</i> does not have an extended access ACL. Otherwise, the value <code>-1</code> is returned and the global variable <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_extended_fd function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EBADF</p>
<dd> The <i>fd</i> argument is not a valid file descriptor.</p>
<dt><code>Bq </code>Er ENOTSUP</p>
<dd> The file system on which the file identified by <i>fd</i> is located does not support ACLs, or ACLs are disabled.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-access/">access</a>(2), acl_get_fd3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
