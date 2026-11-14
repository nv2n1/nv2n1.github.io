---
title: "gpsflash(1)"
name: "gpsflash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsflash/"
description: "gpsflash – 2-stage firmware loader for GPS chipsets"
---

<h2 class="name">NAME</h2>
<p> gpsflash &#8211; 2-stage firmware loader for GPS chipsets </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpsflash</code> [-n] [-l&nbsp;<wbr><i>loader-file</i>] -f&nbsp;<wbr><i>firmware-file</i> {<i>tty</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>This program is a firmware loader for GPSes connected to your host computer via serial or USB port. Presently it supports only SiRF GPSes. Other GPSes may be supported in the future if the vendors cooperate. </p>
<p> For operation, this program requires a flashloader binary (found by default in a file named <i>dlgsp2.bin</i>) and a firmware image. This program first ships a command that tells the GPS a flashloader image will follow, then gives the GPS time to reboot into the flashloader. The flashloader then accepts S-records from the serial or USB port until it sees a termination record, at which point it writes the new firmware into the GPS&#8217;s non-volatile memory and reboots the chip into the new firmware. </p>
<p> There is one required argument, specifying the serial device to which the GPS is connected. </p>
<p> The -l option specifies the flashloader binary. The -f option specifies the firmware image file, and is required unless you are just probing the GPS (-n option). </p>
<p> If the -n option is specified, the program will probe the GPS to try to determine its type and whether the upload is compatible, but not actually perform the upload. When this option is specified, the -f option is not required. </p>
<p> You will need to obtain your own copy of <i>dlgsp2.bin</i> and your own firmware image. The GPSD project does not yet have permission to distribute these files, so don&#8217;t ask us for copies. </p>
<p> Depending on your GPS type, this program may or may not attempt to check that the flashloader or firmware image is compatible with your GPS; in some cases no check is possible. <code>EXPERIMENT AT YOUR OWN RISK.</code> </p>
<p> This program will only work with firmware images in S-record format, which is the form SiRF normally distributes them in. If you get a binary firmware image from somewhere, you can use <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1), from the GNU binutils to convert it to S-records. </p>
<p> Realize that we are not kidding around when we say that this could very well break your receiver permanently, and if it does, it&#8217;s no one&#8217;s fault but your own. For this program to flash your GPS, you must set an environment variable called I_READ_THE_WARNING with the value &quot;why oh why didn&#8217;t i take the blue pill&quot;. </p>
<p> This program emits progress messages to standard output. </p>
<p> The GPS will be reset to 4800bps NMEA after flash.</p>
<h2>BUGS AND LIMITAIONS</h2>
<p> Warning </p>
<p> THIS PROGRAM CAN DESTROY YOUR GPS. A botched firmware upload will turn it into a paperweight. USE AT YOUR OWN RISK. Maintainers are not responsible for direct or incidental damages. YOU HAVE BEEN WARNED.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/5-srec/">srec</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> Chris Kuethe &lt;chris.kuethe [at] gmail.com&gt;. There is a project page for gpsd <i>here</i>[1].</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> here</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://gpsd.berlios.de/">http://gpsd.berlios.de/</a></dl>
</dl>
<h2>Index</h2>
