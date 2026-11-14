---
title: "check-bios-nx(1)"
name: "check-bios-nx"
section: "1"
letter: "c"
url: "/docs/linux/man/1-check-bios-nx/"
description: "check-bios-nx – determine if BIOS has blocked CPU’s NX capabilities"
---

<h2 class="name">NAME</h2>
<p> <code>check-bios-nx</code> &#8211; determine if BIOS has blocked CPU&#8217;s NX capabilities</p>
<h2>SYNOPSIS</h2>
<p> <code>check-bios-nx [-h|&#8211;help] [&#8211;verbose]</code> </p>
<h2>OPTIONS</h2>
<p> <code>-h|&#8211;help</code> &#8211; display a help message and exit </p>
<p> <code>&#8211;verbose</code> &#8211; explain in detail what has been detected </p>
<h2>DESCRIPTION</h2>
<p> This program attempts to determine if the running x86-based CPU has NX capabilities (regardless of it being disabled by the BIOS). </p>
<p> If the CPU is NX-capable but the nx bit is missing from flags, exit 1 (i.e. &quot;BIOS settings need changing&quot;), otherwise exit 0 (i.e. &quot;nothing wrong with BIOS&quot;) </p>
<h2>MORE INFORMATION</h2>
<p> <i><a rel="nofollow" href="http://launchpad.net/cpu-checker">http://launchpad.net/cpu-checker</a></i> </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-3. </p>
<h2>Index</h2>
