---
title: "afile(1)"
name: "afile"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afile/"
description: "afile – display type and creator of Apple Macintosh files (netatalk format)"
---

<h2 class="name">NAME</h2>
<p> afile &#8211; display type and creator of Apple Macintosh files (netatalk format) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>afile</code> [-a] <i>file</i>&#8230;</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>afile</code></p>
<dd>displays the name and Macintosh type and creator of the <i>file</i> arguments. Tests whether the file is an AppleDouble header, in which case it checks the corresponding data fork exists, or assumes it is a data fork in which case it looks for the corresponding AppleDouble to find the type/creator information. </p>
<p> <code>afile</code> does not look at any of the extension mapping files such as AppleVolumes.system.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Include directories and data files of unknown type (i.e. without corresponding AppleDouble) in output.</dl>
<h2>DIAGNOSTICS</h2>
<p> returns exit status 0 if all files have a corresponding valid .AppleDouble header or data fork, or 99 for bad command line options. Otherwise it returns the following error code relating to the last invalid file. </p>
<p> 1 file doesn&#8217;t exist </p>
<p> 2 file is unreadable </p>
<p> 3 file is directory </p>
<p> 4 file is AppleDouble without data fork </p>
<p> 5 file is AppleDouble with unreadable data fork </p>
<p> 6 file is data fork without AppleDouble </p>
<p> 7 file is data fork with unreadable AppleDouble </p>
<p> 8 file is data fork with short AppleDouble </p>
<p> 9 bad magic in AppleDouble</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-achfile/">achfile</a></code>(1), <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
<h2>Index</h2>
