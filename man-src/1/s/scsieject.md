---
title: "scsieject(1)"
name: "scsieject"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scsieject/"
description: "scsieject – control SCSI tape devices"
---

<h2>NAME</h2>
<p> scsieject &#8211; control SCSI tape devices</p>
<h2>SYNOPSIS</h2>
<p> scsieject [-f &lt;scsi-generic-device&gt;] commands</p>
<h2>DESCRIPTION</h2>
<p> The <code>scsieject</code> command controls SCSI devices in a platform-independent manner. As long as &#8216;mtx&#8217; works on the platform, so does &#8216;scsieject&#8217;.</p>
<h2>OPTIONS</h2>
<p> The first argument, given following <code>-f</code> , is the SCSI generic device corresponding to your tape drive. Consult your operating system&#8217;s documentation for more information (for example, under Linux these are generally /dev/sg0 through /dev/sg15, under FreeBSD these are /dev/pass0 through /dev/passX. Under Solaris this is usually the same as your tape drive (Solaris has a SCSI passthrough ioctl). You can set the STAPE or TAPE environment variable rather than use -f. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>load</code></p>
<dd> Load the medium into the drive. When this command is issued to a CD/DVD drive and the tray is extended the tray will be retracted if the drive is capable of it. </p>
<dt><code>unload</code></p>
<dd> Unload the medium from the drive (also known as eject). When this command is issued to a CD/DVD drive or a tape drive the media will be ejected if the device supports it. </p>
<dt><code>start</code></p>
<dd> Start the device. Some devices require a start command after a media changer has loaded new media into the device. </p>
<dt><code>stop</code></p>
<dd> Stop the device. Some devices require a stop command prior to unloading the medium from the device when using a media changer. </p>
<dt><code>lock</code></p>
<dd> Lock the device. Locks the device so that the medium cannot be removed manually. </p>
<dt><code>unlock</code></p>
<dd> Unlock the device. Unlocks the device so that the medium can be removed manually. </p>
</dl>
<h2>AUTHORS</h2>
<p> This program was written by Robert Nelson &lt;robertnelson [at] users.sourceforge.net&gt; based on the scsitape program written by Eric Lee Green &lt;eric [at] badtux.org&gt;. Major portions of the &#8216;mtxl.c&#8217; library used herein were written by Leonard Zubkoff. </p>
<h2>HINTS</h2>
<p> Under Linux, <code>cat /proc/scsi/scsi</code> will tell you what SCSI devices you have. You can then refer to them as <code>/dev/sga,</code> <code>/dev/sgb, </code> etc. by the order they are reported. </p>
<p> Under FreeBSD, <code>camcontrol devlist</code> will tell you what SCSI devices you have, along with which <code>pass</code> device controls them. </p>
<p> Under Solaris 7 and 8, <code>/usr/sbin/devfsadm -C</code> will clean up your /devices directory. Then <code>find /devices -name &#8216;st@*&#8217; -print </code> will return a list of all tape drives. /dev on Solaris is apparently only of historical interest. </p>
<h2>BUGS AND LIMITATIONS</h2>
<p> There are no known bugs or limitations. </p>
<h2>AVAILABILITY</h2>
<p> This version of <code>scsieject</code> is currently being maintained by Robert Nelson &lt;robertnelson [at] users.sourceforge.net&gt; as part of the &#8216;mtx&#8217; suite of programs. The &#8216;mtx&#8217; home page is <a rel="nofollow" href="http://mtx.sourceforge.net">http://mtx.sourceforge.net</a> and the actual code is currently available there and via SVN from <a rel="nofollow" href="http://sourceforge.net/projects/mtx.">http://sourceforge.net/projects/mtx.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loaderinfo/">loaderinfo</a></code>(1),<code><a href="/docs/linux/man/1-tapeinfo/">tapeinfo</a></code>(1),<code><a href="/docs/linux/man/1-mtx/">mtx</a></code>(1) </p>
<h2>Index</h2>
