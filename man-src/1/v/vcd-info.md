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
<p> <code>lt-vcd-info</code> [<i>OPTION</i>&#8230;]</p>
<dl>
<dt><code>-a</code>, <code>&#8211;access-mode</code>=<i>ACCESS</i></dt>
<dd> set CD-ROM access mode (IOCTL, READ_10, READ_CD)</dd>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;bin&quot; CD-ROM disk image file as source</dd>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</dd>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</dt>
<dd> set Nero CD-ROM disk image file as source</dd>
<dt><code>&#8211;toc-file</code>[=<i>FILE</i>]</dt>
<dd> set &quot;toc&quot; CD-ROM disk image file as source</dd>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</dt>
<dd> set source and determine if &quot;bin&quot; image or device</dd>
<dt><code>&#8211;no-ext-psd</code></dt>
<dd> ignore information in /EXT/PSD_X.VCD</dd>
<dt><code>&#8211;sector-2336</code></dt>
<dd> use 2336 byte sector mode for image file</dd>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</dt>
<dd> set CD-ROM device as source</dd>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></dt>
<dd> Set debugging output to LEVEL</dd>
<dt><code>-t</code>, <code>&#8211;terse</code></dt>
<dd> same as <code>&#8211;no-header</code> <code>&#8211;no-banner</code> <code>&#8211;no-delimiter</code></dd>
<dt><code>-B</code>, <code>&#8211;no-banner</code></dt>
<dd> do not show program banner header and RCS version string</dd>
<dt><code>-D</code>, <code>&#8211;no-delimiter</code></dt>
<dd> do not show delimiter lines around various sections of output</dd>
<dt><code>-H</code>, <code>&#8211;no-header</code></dt>
<dd> do not show section header titles</dd>
<dt><code>&#8211;show-entries</code>=<i>STRING</i></dt>
<dd> show specific entry of the ENTRIES section</dd>
<dt><code>-E</code>, <code>&#8211;show-entries-all</code></dt>
<dd> show ENTRIES section</dd>
<dt><code>-F</code>, <code>&#8211;show-filesystem</code></dt>
<dd> show filesystem info</dd>
<dt><code>&#8211;show-info</code>=<i>STRING</i></dt>
<dd> show specific entry of the INFO section</dd>
<dt><code>-I</code>, <code>&#8211;show-info-all</code></dt>
<dd> show INFO section</dd>
<dt><code>-L</code>, <code>&#8211;show-lot</code></dt>
<dd> show LOT section</dd>
<dt><code>-p</code>, <code>&#8211;show-psd</code></dt>
<dd> show PSD section(s)</dd>
<dt><code>-P</code>, <code>&#8211;show-pvd-all</code></dt>
<dd> show PVD section(s)</dd>
<dt><code>&#8211;show-pvd</code>=<i>STRING</i></dt>
<dd> show a specific entry of the Primary Volume Descriptor (PVD) section</dd>
<dt><code>-s</code>, <code>&#8211;show-scandata</code></dt>
<dd> show scan data</dd>
<dt><code>-X</code>, <code>&#8211;show-search</code></dt>
<dd> show search data</dd>
<dt><code>-S</code>, <code>&#8211;show-source</code></dt>
<dd> show source image filename and size</dd>
<dt><code>-T</code>, <code>&#8211;show-tracks</code></dt>
<dd> show tracks</dd>
<dt><code>-f</code>, <code>&#8211;show-format</code></dt>
<dd> show VCD format (VCD 1.1, VCD 2.0, SVCD, &#8230;)</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> show only critical messages</dd>
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
<p> The full documentation for <code>vcd-info</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcd-info</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info vcd-info</code></dd></dl>
<p> should give you access to the complete manual. </p>
