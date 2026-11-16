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
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> specify xml file for output (default: &#8216;videocd.xml&#8217;)</dd>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</dt>
<dd> set image file as source (default: &#8216;videocd.bin&#8217;)</dd>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</dd>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</dt>
<dd> set Nero CD-ROM disk image image file as source</dd>
<dt><code>&#8211;toc-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;toc&quot; CD-ROM disk image file as source</dd>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</dt>
<dd> set CDROM device as source</dd>
<dt><code>&#8211;sector-2336</code></dt>
<dd> use 2336 byte sector mode for image file</dd>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</dt>
<dd> set source and determine if &quot;bin&quot; image or device</dd>
<dt><code>&#8211;no-ext-psd</code></dt>
<dd> ignore /EXT/PSD_X.VCD</dd>
<dt><code>&#8211;no-command-comment</code></dt>
<dd> Don&#8217;t include command name as a comment</dd>
<dt><code>&#8211;norip</code></dt>
<dd> only extract XML structure</dd>
<dt><code>&#8211;nofiles</code></dt>
<dd> don&#8217;t extract files</dd>
<dt><code>&#8211;nosequences</code></dt>
<dd> don&#8217;t extract sequences</dd>
<dt><code>&#8211;nosegments</code></dt>
<dd> don&#8217;t extract segment play items</dd>
<dt><code>-p</code>, <code>&#8211;progress</code></dt>
<dd> show progress</dd>
<dt><code>-t</code>, <code>&#8211;track</code>=<i>INT</i></dt>
<dd> rip only this track</dd>
<dt><code>-T</code>, <code>&#8211;notrack</code>=<i>INT</i></dt>
<dd> do not rip this track</dd>
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
<p> The full documentation for <code>vcdxrip</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcdxrip</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info vcdxrip</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
