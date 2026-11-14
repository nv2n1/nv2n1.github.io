---
title: "vcd-info(1)"
name: "vcd-info"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcd-info/"
description: "vcd-info – manual page for vcd-info 0.7.24"
---

<h2>NAME</h2>
<p> vcd-info &#8211; manual page for vcd-info 0.7.24</p>
<h2>SYNOPSIS</h2>
<p> <code>lt-vcd-info</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;access-mode</code>=<i>ACCESS</i></p>
<dd> set CD-ROM access mode (IOCTL, READ_10, READ_CD)</p>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;bin&quot; CD-ROM disk image file as source</p>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</p>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</p>
<dd> set Nero CD-ROM disk image file as source</p>
<dt><code>&#8211;toc-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;toc&quot; CD-ROM disk image file as source</p>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</p>
<dd> set source and determine if &quot;bin&quot; image or device</p>
<dt><code>&#8211;no-ext-psd</code></p>
<dd> ignore information in /EXT/PSD_X.VCD</p>
<dt><code>&#8211;sector-2336</code></p>
<dd> use 2336 byte sector mode for image file</p>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</p>
<dd> set CD-ROM device as source</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></p>
<dd> Set debugging output to LEVEL</p>
<dt><code>-t</code>, <code>&#8211;terse</code></p>
<dd> same as <code>&#8211;no-header</code> <code>&#8211;no-banner</code> <code>&#8211;no-delimiter</code></p>
<dt><code>-B</code>, <code>&#8211;no-banner</code></p>
<dd> do not show program banner header and RCS version string</p>
<dt><code>-D</code>, <code>&#8211;no-delimiter</code></p>
<dd> do not show delimiter lines around various sections of output</p>
<dt><code>-H</code>, <code>&#8211;no-header</code></p>
<dd> do not show section header titles</p>
<dt><code>&#8211;show-entries</code>=<i>STRING</i></p>
<dd> show specific entry of the ENTRIES section</p>
<dt><code>-E</code>, <code>&#8211;show-entries-all</code></p>
<dd> show ENTRIES section</p>
<dt><code>-F</code>, <code>&#8211;show-filesystem</code></p>
<dd> show filesystem info</p>
<dt><code>&#8211;show-info</code>=<i>STRING</i></p>
<dd> show specific entry of the INFO section</p>
<dt><code>-I</code>, <code>&#8211;show-info-all</code></p>
<dd> show INFO section</p>
<dt><code>-L</code>, <code>&#8211;show-lot</code></p>
<dd> show LOT section</p>
<dt><code>-p</code>, <code>&#8211;show-psd</code></p>
<dd> show PSD section(s)</p>
<dt><code>-P</code>, <code>&#8211;show-pvd-all</code></p>
<dd> show PVD section(s)</p>
<dt><code>&#8211;show-pvd</code>=<i>STRING</i></p>
<dd> show a specific entry of the Primary Volume Descriptor (PVD) section</p>
<dt><code>-s</code>, <code>&#8211;show-scandata</code></p>
<dd> show scan data</p>
<dt><code>-X</code>, <code>&#8211;show-search</code></p>
<dd> show search data</p>
<dt><code>-S</code>, <code>&#8211;show-source</code></p>
<dd> show source image filename and size</p>
<dt><code>-T</code>, <code>&#8211;show-tracks</code></p>
<dd> show tracks</p>
<dt><code>-f</code>, <code>&#8211;show-format</code></p>
<dd> show VCD format (VCD 1.1, VCD 2.0, SVCD, &#8230;)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> show only critical messages</p>
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
<p> The full documentation for <code>vcd-info</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcd-info</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info vcd-info</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
