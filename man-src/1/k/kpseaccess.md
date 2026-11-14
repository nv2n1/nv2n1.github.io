---
title: "kpseaccess(1)"
name: "kpseaccess"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpseaccess/"
description: "kpseaccess – determine whether a file can be accessed"
---

<h2 class="name">NAME</h2>
<p> kpseaccess &#8211; determine whether a file can be accessed </p>
<h2>SYNOPSIS</h2>
<p> <code>kpseaccess</code> <i>mode</i> <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> Exit successfully if <i>file</i> can be accessed with the specified <i>mode</i>. The <i>mode</i> is an optional dash (`<code>&#8211;</code>&#8216;) followed by zero or more letters of <code>rwx</code>, where <code>r</code> is for readable, <code>w</code> is for writable, and <code>x</code> is for executable. </p>
<p> The difference between <code>kpseaccess</code> and <code>test</code> is that the latter looks at the permission bits, while the former checks using the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call. This makes a difference when file systems have been mounted read-only.</p>
<h2>OPTIONS</h2>
<p> <code>kpseaccess</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-access/">access</a></code>(2) </p>
<h2>Index</h2>
