---
title: "fd2ps(1)"
name: "fd2ps"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fd2ps/"
description: "fd2ps – Translates fdesign output to PostScript"
---

<h2>NAME</h2>
<p> fd2ps &#8211; Translates fdesign output to PostScript</p>
<h2>SYNOPSIS</h2>
<p> fd2ps [-options] input.[fd] [output]</p>
<h2>DESCRIPTION</h2>
<p> The program <i>fd2ps</i> translates the <i>fd</i> file produced by the interface builder program <i>fdesign</i> of the <code>Forms Library</code> into PostScript (ps), or optionally Encapsulated PostScript (eps) for printing or inclusion into other documents. The input file can be given with or without the .fd extension. If output file name is not specified, used is a filename derived from the input file name by replacing the .fd extension with ps or eps. If output filename is specified as -, stdout is used. </p>
<h2>OPTIONS</h2>
<p> <i>fd2ps</i> accepts the following command line options</p>
<dl>
<dt><code>-help</code></p>
<dd> Prints a brief summary of all command line options.</p>
<dt><code>-version</code></p>
<dd> Prints the current version of <i>fd2ps</i> and exits.</p>
<dt><code>-p</code></p>
<dd> The option requests portrait orientation. By default, the orientation is switched to landscape if portrait will not fit the page. This option overrides the default.</p>
<dt><code>-l</code></p>
<dd> This options requests landscape output.</p>
<dt><code>-bw</code><i> n</i></p>
<dd> Specifies the border width of the interface. By default this information is obtained from the .fd file.</p>
<dt><code>-eps</code></p>
<dd> This option requests Encapsulated PostScript instead of the plain PostScript output.</p>
<dt><code>-gray</code></p>
<dd> This options requests all colors be converted to gray levels. By default, <i>fd2ps</i> outputs colors as specified in the .fd file.</p>
<dt><code>-G f</code></p>
<dd> specifies a gamma factor that will be used to adjust the builtin colors in a non-linear fashion. It can be thought as a way to brighten or dim the builtin colors: larger the gamma, brighter the color. The default gamma is 1.0.</p>
<dt><code>-dpi</code><i> f</i></p>
<dd> This option specifies the screen resolution on which the user interface is designed. By giving a smaller or larger dpi number than that of the screen, the output is in effect being enlarged or shrunk. This flag does not affect text size. The default DPI is 85. If the .fd file is specified in device independent unit, this flag does not have effect.</p>
<dt><code>-rgb</code><i> file</i></p>
<dd> This option specifies the path to the X color database (rgb.txt) for use in parsing XPM colornames. The default is /usr/lib/X11/rgb.txt. Environment variable <code>RGBFile</code> can be used to change the default.</p>
<dt><code>-paper</code><i> name</i></p>
<dd> This option specifies the paper name, such as A4, Letter etc. The output PostScript will always center on the page. Use name <i>all</i> to get a list of the known paper names and sizes. The default is US Letter unless environment variable <code>PAPER</code> is set to one of the known paper names.</p>
<dt><code>-pw</code><i> f</i></p>
<dd> Specifies the paper width, in inches.</p>
<dt><code>-ph</code><i> f</i></p>
<dd> Specifies the paper height, in inches.</p>
<dt><code>-verbose</code></p>
<dd> This option specifies verbose output, i.e., comments in the output PostScript file. Most useful for debugging the <i>fd2ps</i> program.</dl>
<h2>BUGS</h2>
<p> Not all objects are currently supported.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1L-fdesign/">fdesign</a>(1L), <a href="/docs/linux/man/5-xforms/">xforms</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (c) 1997-98 by T.C. Zhao (tc_zhao [at] yahoo.com)<br />
 Since 2002: GNU Lesser General Public License<br />
 Maintainers: Jean-Marc Lasgouttes, Angus Leeming and Jens Thoms Toerring &lt;jt [at] toerring.de&gt;</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://xforms-toolkit.org">http://xforms-toolkit.org</a><br />
 <a rel="nofollow" href="http://world.std.com/~xforms">http://world.std.com/~xforms</a> </p>
<h2>Index</h2>
