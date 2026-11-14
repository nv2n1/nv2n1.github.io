---
title: "vcdxbuild(1)"
name: "vcdxbuild"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcdxbuild/"
description: "vcdxbuild – manual page for vcdxbuild 0.7.24"
---

<h2>NAME</h2>
<p> vcdxbuild &#8211; manual page for vcdxbuild 0.7.24</p>
<h2>SYNOPSIS</h2>
<p> <code>vcdxbuild</code> [<i>OPTION</i>&#8230;] <i>&lt;xml-control-file&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;image-type</code>=<i>TYPE</i></p>
<dd> specify image type for output (default: &#8216;bincue&#8217;)</p>
<dt><code>-o</code>, <code>&#8211;image-option</code>=<i>KEY=VALUE</i></p>
<dd> specify image option</p>
<dt><code>-c</code>, <code>&#8211;cue-file</code>=<i>FILE</i></p>
<dd> specify cue file for output (default: &#8216;videocd.cue&#8217;)</p>
<dt><code>-b</code>, <code>&#8211;bin-file</code>=<i>FILE</i></p>
<dd> specify bin file for output (default: &#8216;videocd.bin&#8217;)</p>
<dt><code>&#8211;cdrdao-file</code>=<i>FILE</i></p>
<dd> specify cdrdao-style image filename base</p>
<dt><code>&#8211;sector-2336</code></p>
<dd> use 2336 byte sectors for output</p>
<dt><code>-T</code>, <code>&#8211;create-time</code>=<i>STRING</i></p>
<dd> specify creation date on files in CD image (default: current date)</p>
<dt><code>-p</code>, <code>&#8211;progress</code></p>
<dd> show progress</p>
<dt><code>&#8211;dump-dtd</code></p>
<dd> dump internal DTD to stdout</p>
<dt><code>&#8211;filename-encoding</code>=<i>STRING</i></p>
<dd> use given charset encoding for filenames instead of UTF8</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> show only critical messages</p>
<dt><code>&#8211;gui</code></p>
<dd> enable GUI mode</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version and copyright information and exit</dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</dl>
<h2>AUTHOR</h2>
<p> Written by Herbert Valerio Riedel and Rocky Bernstein. </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/vcdimager/">http://www.gnu.org/software/vcdimager/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2003 Herbert Valerio Riedel &lt;hvr [at] gnu.org&gt;</p>
<dl>
<dt>
<dd> 2003 Rocky Bernstein &lt;rocky [at] panix.com&gt;</dl>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>vcdxbuild</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcdxbuild</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info vcdxbuild</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
