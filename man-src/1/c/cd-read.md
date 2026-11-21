---

title: "cd-read(1)"
name: "cd-read"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-read/"
description: "cd-read – reads Information from a CD or CD-image"
---

<p> cd-read &#8211; reads Information from a CD or CD-image</p>
<h2>SYNOPSIS</h2>
<p> <code>cd-read</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;access-mode</code>=<i>STRING</i></dt>
<dd> Set CD control access mode</dd>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>MODE-TYPE</i></dt>
<dd> set CD-ROM read mode (audio, auto, m1f1, m1f2, m2mf1, m2f2)</dd>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></dt>
<dd> Set debugging to LEVEL</dd>
<dt><code>-x</code>, <code>&#8211;hexdump</code></dt>
<dd> Show output as a hex dump. The default is a hex dump when output goes to stdout and no hex dump when output is to a file.</dd>
<dt><code>-j</code>, <code>&#8211;just-hex</code></dt>
<dd> Don&#8217;t display printable chars on hex dump. The default is print chars too.</dd>
<dt><code>&#8211;no-header</code></dt>
<dd> Don&#8217;t display header and copyright (for regression testing)</dd>
<dt><code>&#8211;no-hexdump</code></dt>
<dd> Don&#8217;t show output as a hex dump.</dd>
<dt><code>-s</code>, <code>&#8211;start</code>=<i>INT</i></dt>
<dd> Set LBA to start reading from</dd>
<dt><code>-e</code>, <code>&#8211;end</code>=<i>INT</i></dt>
<dd> Set LBA to end reading from</dd>
<dt><code>-n</code>, <code>&#8211;number</code>=<i>INT</i></dt>
<dd> Set number of sectors to read</dd>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;bin&quot; CD-ROM disk image file as source</dd>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</dd>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</dt>
<dd> set source and determine if &quot;bin&quot; image or device</dd>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</dt>
<dd> set CD-ROM device as source</dd>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</dt>
<dd> set Nero CD-ROM disk image file as source</dd>
<dt><code>-t</code>, <code>&#8211;toc-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;TOC&quot; CD-ROM disk image file as source</dd>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> Output blocks to file rather than give a hexdump.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> display version and copyright information and exit</dd></dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd> Show this help message</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message</dd></dl>
<h2>AUTHOR</h2>
<p> Rocky Bernstein &lt;rocky [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2005, 2007-2008, 2011-2013 R. Bernstein<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Have driver: GNU/Linux ioctl and MMC driver Have driver: cdrdao (TOC) disk image driver Have driver: bin/cuesheet disk image driver Have driver: Nero NRG disk image driver Default CD-ROM device: /dev/sr0</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-cd-info/">cd-info</a>(1)</tt> for information about a CD; <tt><a href="/docs/linux/man/1-cd-drive/">cd-drive</a>(1)</tt> for CD-ROM characteristics; <tt><a href="/docs/linux/man/1-iso-read/">iso-read</a>(1)</tt> for information about an ISO-9660 image. </p>
