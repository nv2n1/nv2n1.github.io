---
title: "magnifier(1)"
name: "magnifier"
section: "1"
letter: "m"
url: "/docs/linux/man/1-magnifier/"
description: "magnifier – GNOME Magnifier (gnome-mag)"
---

<h2>NAME</h2>
<p> magnifier &#8211; GNOME Magnifier (gnome-mag)</p>
<h2>SYNOPSIS</h2>
<p> <code>magnifier</code> [-vhmif?] [-t|&#8211;target-display STRING] [-s|&#8211;source-display STRING] [&#8211;cursor-set=STRING] [&#8211;cursor-size=INT] [&#8211;cursor-scale-factor=FLOAT] [&#8211;cursor-color=LONG] [-v|&#8211;vertical] [-h|&#8211;horizontal] [-m|&#8211;mouse-follow] [-r|&#8211;refresh-time INT] [&#8211;mouse-latency=INT] [-z|&#8211;zoom-factor FLOAT] [-i|&#8211;invert-image] [&#8211;no-initial-region] [&#8211;timing-iterations=INT] [&#8211;timing-output] [&#8211;timing-pan-rate=INT] [&#8211;timing-delta-x=INT] [&#8211;timing-delta-y=INT] [&#8211;smoothing-type=STRING] [-f|&#8211;fullscreen] [&#8211;smooth-scrolling] [-b|&#8211;border-size INT] [-c|&#8211;border-color LONG] [&#8211;use-test-pattern] [&#8211;override-redirect] [&#8211;ignore-damage] [-?|&#8211;help] [&#8211;usage]</p>
<h2>AVAILABILITY</h2>
<p> The GNOME magnifier (gnome-mag) provides a command-line interface for standalone use, although its primary goal is to provide a set of magnification services for use by other client applications and assistive technologies, like Gnopernicus, Orca or LSR. This magnifier is compatible with operating systems using X Window System, although the magnifier will have a better performance and functionality when the Damage and Fixes extensions are present.</p>
<h2>DESCRIPTION</h2>
<p> A desktop screen magnifier. If present, the Region Of Interest (ROI) for the magnifier can be driven by a screen reader via the Assistive Technology Service Provider Interface (ATSPI); otherwise, the magnifier will be centered to the pointer position.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t, &#8211;target-display=STRING</code></dt>
<dd> specify display on which to show magnified view</dd>
<dt><code>-s, &#8211;source-display=STRING</code></dt>
<dd> specify display to magnify</dd>
<dt><code>&#8211;cursor-set=STRING</code></dt>
<dd> cursor set to use in target display</dd>
<dt><code>&#8211;cursor-size=INT</code></dt>
<dd> cursor size to use (overrides cursor-scale-factor)</dd>
<dt><code>&#8211;cursor-scale-factor=FLOAT</code></dt>
<dd> cursor scale factor</dd>
<dt><code>&#8211;cursor-color=LONG</code></dt>
<dd> cursor color (applied to &#8216;black&#8217; pixels</dd>
<dt><code>-v, -vertical</code></dt>
<dd> split screen vertically (if target display = source display)</dd>
<dt><code>-h, &#8211;horizontal </code></dt>
<dd> split screen horizontally (if target display = source display)</dd>
<dt><code>-m, &#8211;mouse-follow </code></dt>
<dd> track mouse movements</dd>
<dt><code>-r, &#8211;refresh-time=INT </code></dt>
<dd> minimum refresh time for idle, in ms</dd>
<dt><code>&#8211;mouse-latency=INT </code></dt>
<dd> maximum mouse latency time, in ms</dd>
<dt><code>-z, &#8211;zoom-factor=FLOAT </code></dt>
<dd> zoom (scale) factor used to magnify source display</dd>
<dt><code>-i, &#8211;invert-image </code></dt>
<dd> invert the image colormap</dd>
<dt><code>&#8211;no-initial-region </code></dt>
<dd> don&#8217;t create an initial zoom region</dd>
<dt><code>&#8211;timing-iterations=INT </code></dt>
<dd> iterations to run timing benchmark test (0=continuous)</dd>
<dt><code>&#8211;timing-output </code></dt>
<dd> display performance ouput</dd>
<dt><code>&#8211;timing-pan-rate=INT </code></dt>
<dd> timing pan rate in lines per frame</dd>
<dt><code>&#8211;timing-delta-x=INT </code></dt>
<dd> pixels to pan in x-dimension each frame in timing update test</dd>
<dt><code>&#8211;timing-delta-y=INT </code></dt>
<dd> pixels to pan in y-dimension each frame in timing update test</dd>
<dt><code>&#8211;smoothing-type=STRING </code></dt>
<dd> image smoothing algorithm to apply (bilinear-interpolation | none)</dd>
<dt><code>-f, \&#8211;fullscreen </code></dt>
<dd> fullscreen magnification, covers entire target display [REQUIRES &#8211;source-display and &#8211;target-display]</dd>
<dt><code>&#8211;smooth-scrolling </code></dt>
<dd> use smooth scrolling</dd>
<dt><code>-b, &#8211;border-size=INT </code></dt>
<dd> width of border</dd>
<dt><code>-c, &#8211;border-color=LONG </code></dt>
<dd> border color specified as (A)RGB 23-bit value, Alpha-MSB</dd>
<dt><code>&#8211;use-test-pattern </code></dt>
<dd> use test pattern as source</dd>
<dt><code>&#8211;override-redirect </code></dt>
<dd> make the magnifier window totally unmanaged by the window manager</dd>
<dt><code>&#8211;ignore-damage </code></dt>
<dd> ignore the X server DAMAGE extension, if present</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> command line help</dd>
<dt><code>&#8211;usage</code></dt>
<dd> command line synopsis</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/gnome-mag/1_32/*.xpm</code></dt>
<dd>
</dd><dt><code>/usr/lib/bonobo/servers/GNOME_Magnifier.server</code></dt>
<dd>
</dd><dt><code>/usr/lib/libgnome-mag.so.2</code></dt>
<dd></dd></dl>
<h2>BUGS</h2>
<p> See <i><a rel="nofollow" href="http://bugs.gnome.org">http://bugs.gnome.org</a></i></p>
<h2>AUTHORS</h2>
<dl>
<dt>Erwann Chenede &lt;erwann.chenede [at] sun.com&gt;</dt>
<dd>
</dd><dt>Bill Haneman &lt;bill.haneman [at] sun.com&gt;</dt>
<dd></dd></dl>
<h2>LICENSE</h2>
<p> Licensed under the GNU Lesser Public License (LGPL) v2.1</p>
<h2>SEE ALSO</h2>
<p> <i>gnopernicus(1), </i> <i><a href="/docs/linux/man/1-orca/">orca</a>(1), </i> <i>lsr(1),</i> Bonobo, Assistive Technology Service Provider Interface (AT-SPI) </p>
<h2>Index</h2>
