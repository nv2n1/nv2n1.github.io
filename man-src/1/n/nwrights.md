---
title: "nwrights(1)"
name: "nwrights"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwrights/"
description: "nwrights – Show effective rights for file or directory"
---

<h2>NAME</h2>
<p> nwrights &#8211; Show effective rights for file or directory</p>
<h2>SYNOPSIS</h2>
<p> <code>nwrights</code> [ <code>-h</code> ] <code>file/directory</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>nwrights</code> asks the NetWare server for the effective rights the user has for a specific file or directory. The rights the server grants are the definitive restriction for what you may do with files or directories. The Linux permission bits are not really relevant, they can only restrict the possibilities further. </p>
<p> <code>nwrights</code> operates on the current directory or the file or directory that is given as an argument. Certainly the file or directory you specify has to reside on a ncpfs mounted directory for nwrights to work properly. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print out a short help text.</dl>
<p> <code>file/directory</code></p>
<dl>
<dt>
<dd> You can specify the file or directory you want information about. The default is the current working directory.</dl>
<h2>AUTHORS</h2>
<p> nwrights was written by Volker Lendecke with the corresponding NetWare utility in mind. See the Changes file of ncpfs for other contributors. </p>
<h2>Index</h2>
