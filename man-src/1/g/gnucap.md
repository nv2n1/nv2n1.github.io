---
title: "gnucap(1)"
name: "gnucap"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnucap/"
description: "gnucap – GNU Circuit Analysis Package"
---

<h2 class="name">NAME</h2>
<p> gnucap &#8211; GNU Circuit Analysis Package </p>
<h2>SYNOPSIS</h2>
<p> <code>gnucap</code> [<code>-b</code> filename] [<code>-i</code> filename] </p>
<h2>DESCRIPTION</h2>
<p> <i>GNUCAP </i> is a general purpose circuit simulator. It performs nonlinear dc and transient analyses, fourier analysis, and ac analysis linearized at an operating point. It is fully interactive and command driven. It can also be run in batch mode or as a server. The output is produced as it simulates. Spice compatible models for the MOSFET (level 1,2,3) and diode are included in this release. </p>
<p> Since it is fully interactive, it is possible to make changes and re-simulate quickly. The interactive design makes it well suited to the typical iterative design process used it optimizing a circuit design. It is also well suited to undergraduate teaching where Spice in batch mode can be quite intimidating. This version, while still officially in beta test, should be stable enough for basic undergraduate teaching and courses in MOS design, but not for bipolar design. </p>
<p> In batch mode it is mostly Spice compatible, so it is often possible to use the same file for both GNUCAP and Spice. </p>
<p> The analog simulation is based on traditional nodal analysis with iteration by Newton&#8217;s method and LU decomposition. An event queue and incremental matrix update speed up the solution for large circuits (at some expense for small circuits). </p>
<p> It also has digital devices for mixed signal simulation. The digital devices may be implemented as either analog subcircuits or as true digital models. The simulator will automatically determine which to use. Networks of digital devices are simulated as digital, with no conversions to analog between gates. This results in digital circuits being simulated faster than on a typical analog simulator, even with behavioral models. The digital mode is experimental and needs work. There will be substantial improvements in future releases. </p>
<h2>OPTIONS</h2>
<p> Two command-line options are available. Only one of these may be specified. If no parameters are given, gnucap will start in interactive mode.</p>
<dl>
<dt><i>-b filename</i></p>
<dd> execute the commands in the named file then exit (batch mode)</p>
<dt><i>-i filename</p>
<dd> execute the commands in the named file then go into interactive mode</dl>
<p> </i></p>
<h2>BUGS</h2>
<p> See <code>/usr/share/doc/gnucap/bugs </code> for a list of known bugs in this release. </p>
<p> GNUCAP is an ongoing research project. It is being released in a preliminary phase in hopes that it will be useful and that others will use it as a thrust or base for their research. I also hope for some comments that may help me direct my research. </p>
<h2>AUTHOR</h2>
<p> GNUCAP is being written by Albert Davis &lt;aldavis [at] ieee.org&gt; </p>
<p> This manual page was written by Jon Rabone &lt;jkr [at] debian.org&gt; and maintained by Hamish Moffatt &lt;hamish [at] debian.org&gt; for the Debian package of gnucap. For the full LaTeX documentation, please see <code>/usr/share/doc/gnucap/manual.</code> </p>
<h2>Index</h2>
