---
title: "tapeinfo(1)"
name: "tapeinfo"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tapeinfo/"
description: "tapeinfo – report SCSI tape device info"
---

<h2>NAME</h2>
<p> tapeinfo &#8211; report SCSI tape device info</p>
<h2>SYNOPSIS</h2>
<p> tapeinfo -f &lt;scsi-generic-device&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>tapeinfo</code> command reads various information from SCSI tape drives that is not generally available via most vendors&#8217; tape drivers. It issues raw commands directly to the tape drive, using either the operating system&#8217;s SCSI generic device ( e.g. /dev/sg0 on Linux, /dev/pass0 on FreeBSD) or the raw SCSI I/O ioctl on a tape device on some operating systems. </p>
<p> One good time to use &#8216;tapeinfo&#8217; is immediately after a tape i/o operation has failed. On tape drives that support HP&#8217;s &#8216;tapealert&#8217; API, &#8216;tapeinfo&#8217; will report a more exact description of what went wrong. </p>
<p> Do be aware that &#8216;tapeinfo&#8217; is not a substitute for your operating system&#8217;s own &#8216;mt&#8217; or similar tape driver control program. It is intended to supplement, not replace, programs like &#8216;mt&#8217; that access your operating system&#8217;s tape driver in order to report or set information.</p>
<h2>OPTIONS</h2>
<p> The first argument, given following <code>-f</code> , is the SCSI generic device corresponding to your tape drive. Consult your operating system&#8217;s documentation for more information (for example, under Linux these are generally start at /dev/sg0 under FreeBSD these start at /dev/pass0). </p>
<p> Under FreeBSD, &#8216;camcontrol devlist&#8217; will tell you what SCSI devices you have, along with which &#8216;pass&#8217; device controls them. Under Linux, &quot;cat /proc/scsi/scsi&quot; will tell you what SCSI devices you have. </p>
<h2>BUGS AND LIMITATIONS</h2>
<p> This program has only been tested on Linux with a limited number of tape drives (HP DDS4, Seagate AIT). </p>
<h2>AVAILABILITY</h2>
<p> <code>tapeinfo</code> is currently being maintained by Robert Nelson &lt;robertnelson [at] users.sourceforge.net&gt; as part of the &#8216;mtx&#8217; suite of programs. The &#8216;mtx&#8217; home page is <a rel="nofollow" href="http://mtx.sourceforge.net">http://mtx.sourceforge.net</a> and the actual code is currently available there and via SVN from <a rel="nofollow" href="http://sourceforge.net/projects/mtx.">http://sourceforge.net/projects/mtx.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mt/">mt</a></code>(1),<code><a href="/docs/linux/man/1-mtx/">mtx</a></code>(1),<code><a href="/docs/linux/man/1-scsitape/">scsitape</a></code>(1),<code><a href="/docs/linux/man/1-scsieject/">scsieject</a></code>(1),<code><a href="/docs/linux/man/1-loaderinfo/">loaderinfo</a></code>(1) </p>
<h2>Index</h2>
