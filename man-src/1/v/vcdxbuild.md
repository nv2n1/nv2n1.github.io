---

title: "vcdxbuild(1)"
name: "vcdxbuild"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcdxbuild/"
description: "vcdxbuild – manual page for vcdxbuild 0.7.24"
---

<p> vcdxbuild &#8211; manual page for vcdxbuild 0.7.24</p>
<h2>SYNOPSIS</h2>
<p> <code>vcdxbuild</code> [<i>OPTION</i>&#8230;] <i>&lt;xml-control-file&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;image-type</code>=<i>TYPE</i></dt>
<dd> specify image type for output (default: &#8216;bincue&#8217;)</dd>
<dt><code>-o</code>, <code>&#8211;image-option</code>=<i>KEY=VALUE</i></dt>
<dd> specify image option</dd>
<dt><code>-c</code>, <code>&#8211;cue-file</code>=<i>FILE</i></dt>
<dd> specify cue file for output (default: &#8216;videocd.cue&#8217;)</dd>
<dt><code>-b</code>, <code>&#8211;bin-file</code>=<i>FILE</i></dt>
<dd> specify bin file for output (default: &#8216;videocd.bin&#8217;)</dd>
<dt><code>&#8211;cdrdao-file</code>=<i>FILE</i></dt>
<dd> specify cdrdao-style image filename base</dd>
<dt><code>&#8211;sector-2336</code></dt>
<dd> use 2336 byte sectors for output</dd>
<dt><code>-T</code>, <code>&#8211;create-time</code>=<i>STRING</i></dt>
<dd> specify creation date on files in CD image (default: current date)</dd>
<dt><code>-p</code>, <code>&#8211;progress</code></dt>
<dd> show progress</dd>
<dt><code>&#8211;dump-dtd</code></dt>
<dd> dump internal DTD to stdout</dd>
<dt><code>&#8211;filename-encoding</code>=<i>STRING</i></dt>
<dd> use given charset encoding for filenames instead of UTF8</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> show only critical messages</dd>
<dt><code>&#8211;gui</code></dt>
<dd> enable GUI mode</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> display version and copyright information and exit</dd></dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd> Show this help message</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Herbert Valerio Riedel and Rocky Bernstein. </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/vcdimager/">http://www.gnu.org/software/vcdimager/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2003 Herbert Valerio Riedel &lt;hvr [at] gnu.org&gt;</p>
<dl>
<dt>
</dt><dd> 2003 Rocky Bernstein &lt;rocky [at] panix.com&gt;</dd></dl>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>vcdxbuild</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcdxbuild</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info vcdxbuild</code></dd></dl>
<p> should give you access to the complete manual. </p>
