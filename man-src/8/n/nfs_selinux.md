---
title: "nfs_selinux(8)"
name: "nfs_selinux"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfs_selinux/"
---

nfs_selinux - Security Enhanced Linux Policy for NFS

<h2>Description</h2>

Security Enhanced Linux secures the NFS server via flexible mandatory access control.

<h2>Booleans</h2>

SELinux policy is customizable based on the least level of access required. SELinux can be configured to not allow NFS to share files. If you want to share NFS partitions, and only allow read-only access to those NFS partitions, turn the nfs_export_all_ro boolean on: 

<dl><dt>setsebool -P nfs_export_all_ro 1
<dd><dt>If you want to share files read/write you must set the nfs_export_all_rw boolean.
<dd><dt>setsebool -P nfs_export_all_rw 1
<dd><dt>These booleans are not required when files to be shared are labeled with the public_content_t or public_content_rw_t types. NFS can share files labeled with the public_content_t or public_content_rw_t types even if the nfs_export_all_ro and nfs_export_all_rw booleans are off.
<dd><dt>If you want to use a remote NFS server for the home directories on this machine, you must set the use_nfs_home_dirs boolean:
<dd><dt>setsebool -P use_nfs_home_dirs 1
<dd><dt>system-config-selinux is a GUI tool available to customize SELinux policy settings.
<dd></dl>

<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>

This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-selinux/">selinux</a>(8), <a HREF="/docs/linux/man/1-chcon/">chcon</a>(1), <a HREF="/docs/linux/man/8-setsebool/">setsebool</a>(8) 
