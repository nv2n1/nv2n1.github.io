---
title: "isoinfo(1)"
name: "isoinfo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isoinfo/"
description: "devdump, isoinfo, isovfy, isodump – Utility programs for dumping and verifying iso9660 images."
---

<h2 class="name">NAME</h2>
<p> devdump, isoinfo, isovfy, isodump &#8211; Utility programs for dumping and verifying iso9660 images. </p>
<h2>SYNOPSIS</h2>
<p> <code>devdump </code> <i>isoimage</i> </p>
<p> <code>isodump </code> <i>isoimage</i> </p>
<p> <code>isoinfo</code> [ <code>-d</code> ] [ <code>-h</code> ] [ <code>-R</code> ] [ <code>-J</code> ] [ <code>-j</code> <i>charset</i> ] [ <code>-f</code> ] [ <code>-l</code> ] [ <code>-p</code> ] [ <code>-T</code> <i>sector</i> ] [ <code>-N</code> <i>sector</i> ] [ <code>-i</code> <i>isoimage</i> ] [ <code>-x</code> <i>path</i> ] </p>
<p> <code>isovfy </code> <i>isoimage</i></p>
<h2>DESCRIPTION</h2>
<p> <code>devdump</code> is a crude utility to interactively display the contents of device or filesystem images. The initial screen is a display of the first 256 bytes of the first 2048 byte sector. The commands are the same as with <code>isodump</code>. </p>
<p> <code>isodump</code> is a crude utility to interactively display the contents of iso9660 images in order to verify directory integrity. The initial screen is a display of the first part of the root directory, and the prompt shows you the extent number and offset in the extent.</p>
<dl>
<dt>
<dd>
<p> You can use the &#8216;a&#8217; and &#8216;b&#8217; commands to move backwards and forwards within the image. The &#8216;g&#8217; command allows you to goto an arbitrary extent, and the &#8216;f&#8217; command specifies a search string to be used. The &#8216;+&#8217; command searches forward for the next instance of the search string, and the &#8216;q&#8217; command exits <code>devdump</code> or <code>isodump</code>.</dl>
<p> <code>isoinfo</code> is a utility to perform directory like listings of iso9660 images. </p>
<p> <code>isovfy</code> is a utility to verify the integrity of an iso9660 image. Most of the tests in <code>isovfy</code> were added after bugs were discovered in early versions of <code>genisoimage.</code> It isn&#8217;t all that clear how useful this is anymore, but it doesn&#8217;t hurt to have this around. </p>
<h2>OPTIONS</h2>
<p> The options common to all programs are <code>-help</code>,<code>-h</code>,<code>-version</code>, <code>i</code><i>=name,</i><code>dev</code><i>=name.</i> The <code>isoinfo</code> program has additional command line options. The options are:</p>
<dl>
<dt><code>-help</code></p>
<dd>
<dt><code>-h</code></p>
<dd> print a summary of all options.</p>
<dt><code>-d</code></p>
<dd> Print information from the primary volume descriptor (PVD) of the iso9660 image. This includes information about Rock Ridge, Joliet extensions and Eltorito boot information if present.</p>
<dt><code>-f</code></p>
<dd> generate output as if a &#8216;find . -print&#8217; command had been run on the iso9660 image. You should not use the <code>-l</code> image with the <code>-f</code> option.</p>
<dt><code>-i iso_image</code></p>
<dd> Specifies the path of the iso9660 image that we wish to examine. The options <code>-i</code> and <code>dev=</code><i>target</i> are mutual exclusive.</p>
<dt><code>dev=</code><i>target</i></p>
<dd> Sets the SCSI target for the drive, see notes above. A typical device specification is <code>dev=</code><i>6,0</i> . If a filename must be provided together with the numerical target specification, the filename is implementation specific. The correct filename in this case can be found in the system specific manuals of the target operating system. On a <i>FreeBSD</i> system without <i>CAM</i> support, you need to use the control device (e.g. <i>/dev/rcd0.ctl</i>). A correct device specification in this case may be <code>dev=</code><i>/dev/rcd0.ctl:@</i> . </p>
<p> On Linux, drives connected to a parallel port adapter are mapped to a virtual SCSI bus. Different adapters are mapped to different targets on this virtual SCSI bus. </p>
<p> If no <i>dev</i> option is present, the program will try to get the device from the <code>CDR_DEVICE</code> environment. </p>
<p> If the argument to the <code>dev=</code> option does not contain the characters &#8216;,&#8217;, &#8216;/&#8217;, &#8216;@&#8217; or &#8216;:&#8217;, it is interpreted as an label name that may be found in the file /etc/wodim.conf (see FILES section). </p>
<p> The options <code>-i</code> and <code>dev=</code><i>target</i> are mutual exclusive.</p>
<dt><code>-l</code></p>
<dd> generate output as if a &#8216;ls -lR&#8217; command had been run on the iso9660 image. You should not use the <code>-f</code> image with the <code>-l</code> option.</p>
<dt><code>-N sector</code></p>
<dd> Quick hack to help examine single session disc files that are to be written to a multi-session disc. The sector number specified is the sector number at which the iso9660 image should be written when send to the cd-writer. Not used for the first session on the disc.</p>
<dt><code>-p</code></p>
<dd> Print path table information.</p>
<dt><code>-R</code></p>
<dd> Extract information from Rock Ridge extensions (if present) for permissions, file names and ownerships.</p>
<dt><code>-J</code></p>
<dd> Extract information from Joliet extensions (if present) for file names.</p>
<dt><code>-j charset</code></p>
<dd> Convert Joliet file names (if present) to the supplied charset. See <code><a href="/docs/linux/man/8-genisoimage/">genisoimage</a></code>(8) for details.</p>
<dt><code>-T sector</code></p>
<dd> Quick hack to help examine multi-session images that have already been burned to a multi-session disc. The sector number specified is the sector number for the start of the session we wish to display.</p>
<dt><code>-x pathname</code></p>
<dd> Extract specified file to stdout.</dl>
<h2>AUTHOR</h2>
<p> The author of the original sources (1993 &#8230; 1998) is Eric Youngdale &lt;ericy [at] gnu.ai.mit.edu&gt; or &lt;eric [at] andante.jic.com&gt; is to blame for these shoddy hacks. Joerg Schilling wrote the SCSI transport library and its adaptation layer to the programs and newer parts (starting from 1999) of the utilities, this makes them Copyright (C) 1999-2004 Joerg Schilling. Patches to improve general usability would be gladly accepted. </p>
<p> This manpage describes the program implementation of <code>isoinfo</code> as shipped by the cdrkit distribution. See <code><a rel="nofollow" href="http://alioth.debian.org/projects/debburn/">http://alioth.debian.org/projects/debburn/</a></code> for details. It is a spinoff from the original program distributed in the cdrtools package [1]. However, the cdrtools developers are not involved in the development of this spinoff and therefore shall not be made responsible for any problem caused by it. Do not try to get support for this program by contacting the original author(s). </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; into the first line of the mail body.</p>
<h2>BUGS</h2>
<p> The user interface really sucks.</p>
<h2>FUTURE IMPROVEMENTS</h2>
<p> These utilities are really quick hacks, which are very useful for debugging problems in genisoimage or in an iso9660 filesystem. In the long run, it would be nice to have a daemon that would NFS export a iso9660 image. </p>
<p> The isoinfo program is probably the program that is of the most use to the general user.</p>
<h2>AVAILABILITY</h2>
<p> These utilities come with the <code>cdrkit</code> package, and the primary download site is <a rel="nofollow" href="http://debburn.alioth.debian.org/">http://debburn.alioth.debian.org/</a> and FTP mirrors of distributions. Despite the name, the software is not beta. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>CDR_DEVICE</code></p>
<dd> This may either hold a device identifier that is suitable to the open call of the SCSI transport library or a label in the file /etc/wodim.conf.</p>
<dt><code>RSH</code></p>
<dd> If the <code>RSH</code> environment is present, the remote connection will not be created via <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) but by calling the program pointed to by <code>RSH</code>. Use e.g. <code>RSH=</code>/usr/bin/ssh to create a secure shell connection. </p>
<p> Note that this forces the program to create a pipe to the <code><a href="/docs/linux/man/1-rsh/">rsh</a>(1)</code> program and disallows the program to directly access the network socket to the remote server. This makes it impossible to set up performance parameters and slows down the connection compared to a <code>root</code> initiated <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code> connection.</p>
<dt><code>RSCSI</code></p>
<dd> If the <code>RSCSI</code> environment is present, the remote SCSI server will not be the program <code>/opt/schily/sbin/rscsi</code> but the program pointed to by <code>RSCSI</code>. Note that the remote SCSI server program name will be ignored if you log in using an account that has been created with a remote SCSI server program as login shell. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/wodim.conf</p>
<dd> Default values can be set for the following options in /etc/wodim.conf.</p>
<dl>
<dt>
<dd>
<dl>
<dt>CDR_DEVICE</p>
<dd> This may either hold a device identifier that is suitable to the open call of the SCSI transport library or a label in the file /etc/wodim.conf that allows to identify a specific drive on the system.</p>
<dt>Any other label</p>
<dd> is an identifier for a specific drive on the system. Such an identifier may not contain the characters &#8216;,&#8217;, &#8216;/&#8217;, &#8216;@&#8217; or &#8216;:&#8217;. </p>
<p> Each line that follows a label contains a TAB separated list of items. Currently, four items are recognized: the SCSI ID of the drive, the default speed that should be used for this drive, the default FIFO size that should be used for this drive and drive specific options. The values for <i>speed</i> and <i>fifosize</i> may be set to -1 to tell the program to use the global defaults. The value for driveropts may be set to &quot;&quot; if no driveropts are used. A typical line may look this way: </p>
<p> teac1= 0,5,0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>4<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>8m<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&quot;&quot;</p>
<p> yamaha= 1,6,0<tt>&nbsp;<wbr>&nbsp;</tt>-1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>burnfree</p>
<p> This tells the program that a drive named <i>teac1</i> is at scsibus 0, target 5, lun 0 and should be used with speed 4 and a FIFO size of 8 MB. A second drive may be found at scsibus 1, target 6, lun 0 and uses the default speed and the default FIFO size.</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1), <code><a href="/docs/linux/man/1-wodim/">wodim</a></code>(1), <code><a href="/docs/linux/man/1-readcd/">readcd</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1).</p>
<h2>SOURCES</h2>
<p> [1] Cdrtools 2.01.01a08 from May 2006, <a rel="nofollow" href="http://cdrecord.berlios.de">http://cdrecord.berlios.de</a> </p>
<h2>Index</h2>
