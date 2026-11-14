---
title: "smbspool_krb5_wrapper(8)"
name: "smbspool_krb5_wrapper"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbspool_krb5_wrapper/"
description: "smbspool_krb5_wrapper – This is a CUPS printing backend which calls smbspool"
---

<p>smbspool_krb5_wrapper &#8211; This is a CUPS printing backend which calls smbspool</p>
<h2>Synopsis</h2>
<dl>
<dd>smbspool_krb5_wrapper {job} {user} {title} {copies} {options} [filename]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbspool_krb5_wrapper is a tool that can be used to print using Kerberos credentials. To get this working smbspool_krb5_wrapper needs to be the smb backend of CUPS. It needs to be owned by root and the permissions for the binary need to be 0700. Once smbspool_krb5_wrapper switched to the user trying to print it executes smbspool. It should not be called by a user.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smbspool/">smbspool</a></code>(8).</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The smbspool_krb5_wrapper manpage was written by Andreas Schneider.</p>
