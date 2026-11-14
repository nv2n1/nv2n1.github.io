---
title: "cd-info(1)"
name: "cd-info"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-info/"
description: "cd-info – shows Information about a CD or CD-image"
---

<h2>NAME</h2>
<p> cd-info &#8211; shows Information about a CD or CD-image</p>
<h2>SYNOPSIS</h2>
<p> <code>cd-info</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;access-mode</code>=<i>STRING</i></p>
<dd> Set CD access method</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></p>
<dd> Set debugging to LEVEL</p>
<dt><code>-T</code>, <code>&#8211;no-tracks</code></p>
<dd> Don&#8217;t show track information</p>
<dt><code>-A</code>, <code>&#8211;no-analyze</code></p>
<dd> Don&#8217;t show filesystem analysis</p>
<dt><code>&#8211;no-cddb</code></p>
<dd> Don&#8217;t look up audio CDDB information or print it</p>
<dt><code>-P</code>, <code>&#8211;cddb-port</code>=<i>INT</i></p>
<dd> CDDB port number to use (default 8880)</p>
<dt><code>-H</code>, <code>&#8211;cddb-http</code></p>
<dd> Lookup CDDB via HTTP proxy (default no proxy)</p>
<dt><code>&#8211;cddb-server</code>=<i>STRING</i></p>
<dd> CDDB server to contact for information (default: freedb.freedb.org)</p>
<dt><code>&#8211;cddb-cache</code>=<i>STRING</i></p>
<dd> Location of CDDB cache directory (default ~/.cddbclient)</p>
<dt><code>&#8211;cddb-email</code>=<i>STRING</i></p>
<dd> Email address to give CDDB server (default me [at] home)</p>
<dt><code>&#8211;no-cddb-cache</code></p>
<dd> Disable caching of CDDB entries locally (default caches)</p>
<dt><code>&#8211;cddb-timeout</code>=<i>INT</i></p>
<dd> CDDB timeout value in seconds (default 10 seconds)</p>
<dt><code>&#8211;no-device-info</code></p>
<dd> Don&#8217;t show device info, just CD info</p>
<dt><code>&#8211;no-disc-mode</code></p>
<dd> Don&#8217;t show disc-mode info</p>
<dt><code>&#8211;dvd</code></p>
<dd> Attempt to give DVD information if a DVD is found.</p>
<dt><code>-v</code>, <code>&#8211;no-vcd</code></p>
<dd> Don&#8217;t look up Video CD information &#8211; for this build, this is always set</p>
<dt><code>-I</code>, <code>&#8211;no-ioctl</code></p>
<dd> Don&#8217;t show ioctl() information</p>
<dt><code>-b</code>, <code>&#8211;bin-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;bin&quot; CD-ROM disk image file as source</p>
<dt><code>-c</code>, <code>&#8211;cue-file</code>[=<i>FILE</i>]</p>
<dd> set &quot;cue&quot; CD-ROM disk image file as source</p>
<dt><code>-N</code>, <code>&#8211;nrg-file</code>[=<i>FILE</i>]</p>
<dd> set Nero CD-ROM disk image file as source</p>
<dt><code>-t</code>, <code>&#8211;toc-file</code>[=<i>FILE</i>]</p>
<dd> set cdrdao CD-ROM disk image file as source</p>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</p>
<dd> set source and determine if &quot;bin&quot; image or device</p>
<dt><code>&#8211;iso9660</code></p>
<dd> print directory contents of any ISO-9660 filesystems</p>
<dt><code>-C</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</p>
<dd> set CD-ROM device as source</p>
<dt><code>-l</code>, <code>&#8211;list-drives</code></p>
<dd> Give a list of CD-drives</p>
<dt><code>&#8211;no-header</code></p>
<dd> Don&#8217;t display header and copyright (for regression testing)</p>
<dt><code>&#8211;no-joliet</code></p>
<dd> Don&#8217;t use Joliet extensions</p>
<dt><code>&#8211;no-rock-ridge</code></p>
<dd> Don&#8217;t use Rock-Ridge-extension information</p>
<dt><code>&#8211;no-xa</code></p>
<dd> Don&#8217;t use XA-extension information</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Don&#8217;t produce warning output</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version and copyright information and exit</dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</dl>
<h2>AUTHOR</h2>
<p> Rocky Bernstein rocky [at] gnu.org, based on the cdinfo program by Gerd Knorr &lt;kraxel [at] bytesex.org&gt; and Heiko Eissfeldt &lt;heiko [at] hexco.de&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2005, 2007-2008, 2011-2013 R. Bernstein<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Have driver: GNU/Linux ioctl and MMC driver Have driver: cdrdao (TOC) disk image driver Have driver: bin/cuesheet disk image driver Have driver: Nero NRG disk image driver Default CD-ROM device: /dev/sr0</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-cd-drive/">cd-drive</a>(1)</tt> for CD-ROM characteristics; <tt><a href="/docs/linux/man/1-iso-info/">iso-info</a>(1)</tt> for information about an ISO-9660 image. </p>
<h2>Index</h2>
