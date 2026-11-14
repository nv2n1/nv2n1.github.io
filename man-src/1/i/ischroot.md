---
title: "ischroot(1)"
name: "ischroot"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ischroot/"
description: "ischroot – detect if running in a chroot"
---

<h2 class="name">NAME</h2>
<p> ischroot &#8211; detect if running in a chroot </p>
<h2>SYNOPSIS</h2>
<p> <code>ischroot</code> [&#8211;default-false] [&#8211;default-true] [&#8211;help] [&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <code>ischroot</code> detects if it is currently running in a chroot. The exit status is:</p>
<dl>
<dt>0</p>
<dd> if currently running in a chroot</p>
<dt>1</p>
<dd> if currently not running in a chroot</p>
<dt>2</p>
<dd> if the detection is not possible (On GNU/Linux this happens if the script is not run as root).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;default-false</code></p>
<dd> Exit with status 1 if the detection is not possible.</p>
<dt><code>-t, &#8211;default-true</code></p>
<dd> Exit with status 0 if the detection is not possible.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message on standard output and exit successfully.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information on standard output and exit successfully.</dl>
<h2>BUGS</h2>
<p> On GNU/Linux, chroot detection is not possible when not root. This works correctly on GNU/Hurd and GNU/kFreeBSD. </p>
<h2>Index</h2>
