---
title: "cd-read(1)"
name: "cd-read"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-read/"
description: "cd-read – reads Information from a CD or CD-image"
---

<h2>NAME</h2>
<p> cd-read &#8211; reads Information from a CD or CD-image</p>
<h2>SYNOPSIS</h2>
<p> <code>cd-read</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;access-mode</code>=<i>STRING</i></p>
<dd> Set CD control access mode</p>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>MODE-TYPE</i></p>
<dd> set CD-ROM read mode (audio, auto, m1f1, m1f2, m2mf1, m2f2)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></p>
<dd> Set debugging to LEVEL</p>
<dt><code>-x</code>, <code>&#8211;hexdump</code></p>
<dd> Show output as a hex dump. The default is a hex dump when output goes to stdout and no hex dump when output is to a file.</p>
<dt><code>-j</code>, <code>&#8211;just-hex</code></p>
<dd> Don&#8217;t display printable chars on hex dump. The default is print chars too.</p>
<dt><code>&#8211;no-header</code></p>
<dd> Don&#8217;t display header and copyright (for regression testing)</p>
<dt><code>&#8211;no-hexdump</code></p>
<dd> Don&#8217;t show output as a hex dump.</p>
<dt><code>-s</code>, <code>&#8211;start</code>=<i>INT</i></p>
<dd> Set LBA to start reading from</p>
<dt><code>-e</code>, <code>&#8211;end</code>=<i>INT</i></p>
<dd> Set LBA to end reading from</p>
<dt><code>-n</code>, <code>&#8211;number</code>=<i>INT</i></p>
<dd> Set number of sectors to read</p>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;bin&quot; CD-ROM disk image file as source</p>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</p>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</p>
<dd> set source and determine if &quot;bin&quot; image or device</p>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</p>
<dd> set CD-ROM device as source</p>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</p>
<dd> set Nero CD-ROM disk image file as source</p>
<dt><code>-t</code>, <code>&#8211;toc-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;TOC&quot; CD-ROM disk image file as source</p>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> Output blocks to file rather than give a hexdump.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version and copyright information and exit</dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</dl>
<h2>AUTHOR</h2>
<p> Rocky Bernstein &lt;rocky [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2005, 2007-2008, 2011-2013 R. Bernstein<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Have driver: GNU/Linux ioctl and MMC driver Have driver: cdrdao (TOC) disk image driver Have driver: bin/cuesheet disk image driver Have driver: Nero NRG disk image driver Default CD-ROM device: /dev/sr0</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-cd-info/">cd-info</a>(1)</tt> for information about a CD; <tt><a href="/docs/linux/man/1-cd-drive/">cd-drive</a>(1)</tt> for CD-ROM characteristics; <tt><a href="/docs/linux/man/1-iso-read/">iso-read</a>(1)</tt> for information about an ISO-9660 image. </p>
<h2>Index</h2>
