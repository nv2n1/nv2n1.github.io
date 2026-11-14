---
title: "ncpumount(8)"
name: "ncpumount"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ncpumount/"
description: "ncpumount – unmount a NetWare filesystem mounted with ncpmount."
---

<p>ncpumount &#8211; unmount a NetWare filesystem mounted with ncpmount.</p>
<h2>Synopsis</h2>
<p><code>ncpumount</code> <code>mount-point</code> </p>
<h2>Description</h2>
<p>This utility unmounts a NetWare filesystem that was previously mounted with the ncpmount utility. If the this utility is made suid root then non-root users will also be able to make use of it. <code>ncpumount</code> has been written to give normal linux-users more control over their resources. It is safe to install this program suid root, because only the user who has mounted a filesystem is allowed to unmount it again. For root it is not necessary to use ncpumount. The normal umount program works perfectly well, but it would certainly be problematic to make umount setuid root. </p>
<h2>Options</h2>
<p><code>mount-point</code></p>
<dl>
<dd><code>mount-point</code> is the directory you want to unmount. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8)</code> </p>
