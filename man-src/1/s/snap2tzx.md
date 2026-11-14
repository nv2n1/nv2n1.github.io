---
title: "snap2tzx(1)"
name: "snap2tzx"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snap2tzx/"
description: "snap2tzx – Convert ZX Spectrum snapshot to .tzx tape images"
---

<h2 class="name">NAME</h2>
<p> snap2tzx &#8211; Convert ZX Spectrum snapshot to .tzx tape images </p>
<h2>SYNOPSIS</h2>
<p> <code>snap2tzx</code> [-1 <i>string</i>] [-2 <i>string</i>] [-b <i>colour</i>] [-g <i>string</i>] [-l <i>string</i>] [-o <i>filename</i>] [-r] [-s <i>speed</i>] [-v] [-$ <i>filename</i>] <i>snapshot</i></p>
<h2>DESCRIPTION</h2>
<p> snap2tzx converts a ZX Spectrum snapshot into a .tzx tape image.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-1 <i>string</i></p>
<dd> causes <i>string</i> (which has a maximum of 32 characters) to be shown while loading.</p>
<dt>-2 <i>string</i></p>
<dd> causes <i>string</i> (maximum 32 characters) to also be shown while loading.</p>
<dt>-b <i>colour</i></p>
<dd> specifies the border colour while loading.</p>
<dt>-g <i>string</i></p>
<dd> causes <i>string</i> (maximum 32 characters) to be used as the game name while loading.</p>
<dt>-l <i>string</i></p>
<dd> causes <i>string</i> (maximum 8 characters) to be used as the BASIC filename in the loader.</p>
<dt>-o <i>filename</i></p>
<dd> causes the output to be sent to <i>filename</i>.</p>
<dt>-r</p>
<dd> causes the final line of attribute data in the loading screen to be bright.</p>
<dt>-s <i>speed</i></p>
<dd> specifies the speed of the loader; available values for <i>speed</i> are 0 (1500 bps), 1 (2250 bps), 2 (3000 bps) and 3 (6000 bps).</p>
<dt>-v</p>
<dd> specifies verbose output.</p>
<dt>-$ <i>filename</i></p>
<dd> specifies that the ZX Spectrum screen stored in <i>filename</i> should be used as the loading screen.</p>
<dt><i>snapshot</i></p>
<dd> specifies the snapshot (in a format supported by <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3)) to be converted.</dl>
<p> In any <i>string</i> parameter, the tilde (~) will be converted into a copyright symbol.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3), <i><a href="/docs/linux/man/1-listbasic/">listbasic</a></i>(1), <i><a href="/docs/linux/man/1-snapconv/">snapconv</a></i>(1) </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Philip Kendall (philip-fuse [at] shadowmagic.org.uk). </p>
<p> Tomaz Kac wrote <i>z802tzx</i> (<i><a href="ftp://ftp.worldofspectrum.org/pub/sinclair/tools/unix/z802tzx-1.2.tar.gz">ftp://ftp.worldofspectrum.org/pub/sinclair/tools/unix/z802tzx-1.2.tar.gz</a></i>), on which <i>snap2tzx</i> is very heavily based. </p>
<p> Martijn van der Heide wrote the turbo-loading code, originally for <i>Taper </i>(<i><a rel="nofollow" href="http://www.worldofspectrum.org/taper.html">http://www.worldofspectrum.org/taper.html</a></i>). </p>
<h2>Index</h2>
