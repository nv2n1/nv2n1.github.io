---
title: "getcifsacl(1)"
name: "getcifsacl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcifsacl/"
description: "getcifsacl – Userspace helper to display an ACL in a security descriptor for Common Internet File System (CIFS)"
---

<h2 class="name">NAME</h2>
<p> getcifsacl &#8211; Userspace helper to display an ACL in a security descriptor for Common Internet File System (CIFS) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>getcifsacl [-v|-r] {file system object}</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the cifs-utils suite. </p>
<p> getcifsacl is a userspace helper program for the Linux CIFS client file system. It is intended to display a security descriptor including ACL for a file system object. </p>
<p> This program uses a plugin to handle the mapping of SIDs to user and group names. <code>/etc/cifs-utils/idmap-plugin</code> should be a symlink that points to the correct plugin to use. </p>
<p> Fields of an ACE such as SID, type, flags, and mask are displayed separated by /. Numeric values of type, flags, and mask are displayed in hexadecimal format.</p>
<h2>OPTIONS</h2>
<p> -v</p>
<dl>
<dt>
<dd> Print version number and exit.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Display a security descriptor in raw mode. Values such as type and flags are displayed in hexadecimal format, a SID is not mapped to a name.</dl>
<h2>NOTES</h2>
<p> Kernel support for getcifsacl/setcifsacl utilities was initially introduced in the 2.6.37 kernel.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mount-cifs/">mount.cifs</a></code>(8), <code><a href="/docs/linux/man/1-setcifsacl/">setcifsacl</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Shirish Pargaonkar wrote the getcifsacl program. </p>
<p> The Linux CIFS Mailing list is the preferred place to ask questions regarding these programs. </p>
<h2>Index</h2>
