---
title: "dh_usrlocal(1)"
name: "dh_usrlocal"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_usrlocal/"
description: "dh_usrlocal – migrate usr/local directories to maintainer scripts"
---

<h2 class="name">NAME</h2>
<p> dh_usrlocal &#8211; migrate usr/local directories to maintainer scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_usrlocal</code> [<i>debhelper options</i>] [<code>-n</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_usrlocal</code> is a debhelper program that can be used for building packages that will provide a subdirectory in <i>/usr/local</i> when installed. </p>
<p> It finds subdirectories of <i>usr/local</i> in the package build directory, and removes them, replacing them with maintainer script snippets (unless <code>-n</code> is used) to create the directories at install time, and remove them when the package is removed, in a manner compliant with Debian policy. These snippets are inserted into the maintainer scripts by <code>dh_installdeb</code>. See <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1) for an explanation of debhelper maintainer script snippets. </p>
<p> When the <i>Rules-Requires-Root</i> field is not (effectively) <i>binary-targets</i>, the directories in <i>/usr/local</i> will have ownership root:staff and the mode will be 02775. These values have been chosen to comply with the recommendations of the Debian policy for directories in <i>/usr/local</i>. </p>
<p> When <i>Rules-Requires-Root</i> has an effective value of <i>binary-targets</i>, the owners, groups and permissions will be preserved with one exception. If the directory is owned by root:root, then ownership will be reset to root:staff and mode will be reset to 02775. This is useful, since that is the group and mode policy recommends for directories in <i>/usr/local</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>prerm</i> scripts.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>CONFORMS TO</h2>
<p> Debian policy, version 2.2</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Andrew Stribblehill &lt;ads [at] debian.org&gt; </p>
<h2>Index</h2>
