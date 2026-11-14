---
title: "vcdxrip(1)"
name: "vcdxrip"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcdxrip/"
description: "vcdxrip – manual page for vcdxrip 0.7.24"
---

<h2>NAME</h2>
<p> vcdxrip &#8211; manual page for vcdxrip 0.7.24</p>
<h2>SYNOPSIS</h2>
<p> <code>lt-vcdxrip</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> specify xml file for output (default: &#8216;videocd.xml&#8217;)</p>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</p>
<dd> set image file as source (default: &#8216;videocd.bin&#8217;)</p>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</p>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</p>
<dd> set Nero CD-ROM disk image image file as source</p>
<dt><code>&#8211;toc-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;toc&quot; CD-ROM disk image file as source</p>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</p>
<dd> set CDROM device as source</p>
<dt><code>&#8211;sector-2336</code></p>
<dd> use 2336 byte sector mode for image file</p>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</p>
<dd> set source and determine if &quot;bin&quot; image or device</p>
<dt><code>&#8211;no-ext-psd</code></p>
<dd> ignore /EXT/PSD_X.VCD</p>
<dt><code>&#8211;no-command-comment</code></p>
<dd> Don&#8217;t include command name as a comment</p>
<dt><code>&#8211;norip</code></p>
<dd> only extract XML structure</p>
<dt><code>&#8211;nofiles</code></p>
<dd> don&#8217;t extract files</p>
<dt><code>&#8211;nosequences</code></p>
<dd> don&#8217;t extract sequences</p>
<dt><code>&#8211;nosegments</code></p>
<dd> don&#8217;t extract segment play items</p>
<dt><code>-p</code>, <code>&#8211;progress</code></p>
<dd> show progress</p>
<dt><code>-t</code>, <code>&#8211;track</code>=<i>INT</i></p>
<dd> rip only this track</p>
<dt><code>-T</code>, <code>&#8211;notrack</code>=<i>INT</i></p>
<dd> do not rip this track</p>
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
<p> The full documentation for <code>vcdxrip</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcdxrip</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info vcdxrip</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
