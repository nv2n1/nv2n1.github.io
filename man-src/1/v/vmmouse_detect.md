---
title: "vmmouse_detect(1)"
name: "vmmouse_detect"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vmmouse_detect/"
description: "vmmouse_detect – VMware mouse device autodetection tool"
---

<h2>NAME</h2>
<p> vmmouse_detect &#8211; VMware mouse device autodetection tool</p>
<h2>SYNOPSIS</h2>
<p> vmmouse_detect</p>
<h2>OPTIONS</h2>
<p> vmmouse_detect has no options</p>
<h2>DESCRIPTION</h2>
<p> <code>vmmouse_detect</code> is a tool for detecting if running in a VMware environment where vmmouse is used. It exits with a 0 return value if the vmmouse client is enabled, and 1 if not.</p>
<h2>DIAGNOSTICS</h2>
<p> <code>vmmouse_detect</code>&#8216;s exit status is used to communicate information.</p>
<dl>
<dt>0</p>
<dd> <code>vmmouse_detect</code> found a mouse and exited normally.</p>
<dt>1</p>
<dd> Either the vmmouse client was not enabled, or it is not being run from within a VMware virtual machine.</dl>
<h2>BUGS</h2>
<p> Please report bugs in <code>vmmouse_detect</code> &lt;<a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/+source/mdetect/vmmouse_detect">https://bugs.launchpad.net/ubuntu/+source/mdetect/vmmouse_detect</a>&gt;.</p>
<h2>AUTHORS</h2>
<p> <code>vmmouse_detect</code> is copyright 2007 VMware, Inc.</p>
<h2>LICENSING</h2>
<p> The <code>vmmouse_detect</code> source code is licensed under a BSD-like license. See COPYING for details. </p>
<p> This manual page is licensed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mdetect/">mdetect</a></i>(1), <i><a href="/docs/linux/man/1-xfree86/">XFree86</a></i>(1) </p>
<h2>Index</h2>
