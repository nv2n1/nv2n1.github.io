---
title: "atomic-unmount(1)"
name: "atomic-unmount"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-unmount/"
description: "atomic-unmount – Unmount Images/Containers"
---

<h2 class="name">NAME</h2>
<p> atomic-unmount &#8211; Unmount Images/Containers </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic unmount</code> [<code>-h</code>|<code>&#8211;help</code>] DIRECTORY </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic unmount</code> will unmount a container/image previously mounted with <code>atomic mount</code>. If the UID of the user is not zero, i.e. if the user is not root, it will expect the image being deleted was mounted by non-root user and will delete the files rather than use the unmount system call. </p>
<h2>OPTIONS:</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>HISTORY</h2>
<p> June 2015, Originally compiled by William Temple (wtemple at redhat dot com) </p>
<h2>Index</h2>
