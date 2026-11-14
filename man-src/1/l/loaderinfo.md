---
title: "loaderinfo(1)"
name: "loaderinfo"
section: "1"
letter: "l"
url: "/docs/linux/man/1-loaderinfo/"
description: "loaderinfo – report SCSI tape device info"
---

<h2>NAME</h2>
<p> loaderinfo &#8211; report SCSI tape device info</p>
<h2>SYNOPSIS</h2>
<p> loaderinfo -f &lt;scsi-generic-device&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>loaderinfo</code> command reads various information from SCSI tape loaders. Its intended use is for high-level programs that are trying to decide what the capabilities of a device are. </p>
<p> The following are printed:</p>
<dl>
<dt><code>Element Address Assignment Page:</code></p>
<dd> This tells how many elements are in the loader, and what their raw hardware addresses are. </p>
<dt><code>Transport Geometry Descriptor Page:</code></p>
<dd> Will display whether media is invertible or not (usable with some optical jukeboxes for detirmining whether to &quot;flip&quot; media after writing to the first side). </p>
<dt><code>Device Capabilities Page</code></p>
<dd> Currently will only display whether we can transfer between slots (i.e. whether &#8216;mtx transfer&#8217; works). </p>
<dt><code>Inquiry Page</code></p>
<dd> Aside from the normal inquiry info, will also print out whether we have a bar code reader (for loaders that support the Exabyte extension for reporting presense of said reader). </p>
</dl>
<h2>OPTIONS</h2>
<p> The first argument, given following <code>-f</code> , is the SCSI generic device corresponding to your tape loader. Consult your operating system&#8217;s documentation for more information (for example, under Linux these are generally start at /dev/sg0 under FreeBSD these start at /dev/pass0). </p>
<p> Under FreeBSD, &#8216;camcontrol devlist&#8217; will tell you what SCSI devices you have, along with which &#8216;pass&#8217; device controls them. Under Linux, &quot;cat /proc/scsi/scsi&quot; will tell you what SCSI devices you have. Under Solaris 8, <code>find /devices -name &#8216;*changer*&#8217;</code> will display the device names for your attached changers. Make sure to configure your &#8216;sgen&#8217; driver first. </p>
<h2>BUGS AND LIMITATIONS</h2>
<p> This program has only been tested on Linux with a limited number of loaders (Ecrix Autopack, Exabyte 220). </p>
<h2>AVAILABILITY</h2>
<p> <code>loaderinfo</code> is currently being maintained by Robert Nelson &lt;robertnelson [at] users.sourceforge.net&gt; as part of the &#8216;mtx&#8217; suite of programs. The &#8216;mtx&#8217; home page is <a rel="nofollow" href="http://mtx.sourceforge.net">http://mtx.sourceforge.net</a> and the actual code is currently available there and via SVN from <a rel="nofollow" href="http://sourceforge.net/projects/mtx.">http://sourceforge.net/projects/mtx.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mt/">mt</a></code>(1),<code><a href="/docs/linux/man/1-tapeinfo/">tapeinfo</a></code>(1),<code><a href="/docs/linux/man/1-mtx/">mtx</a></code>(1) </p>
<h2>Index</h2>
