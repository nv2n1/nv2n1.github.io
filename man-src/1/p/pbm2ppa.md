---
title: "pbm2ppa(1)"
name: "pbm2ppa"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbm2ppa/"
description: "pbm2ppa – convert portable bitmap (PBM) to HP’s Printing Performance Architecture (PPA) file format"
---

<h2>NAME</h2>
<p> pbm2ppa &#8211; convert portable bitmap (PBM) to HP&#8217;s Printing Performance Architecture (PPA) file format</p>
<h2>SYNOPSIS</h2>
<p> pbm2ppa [options] [ &lt;<i>infile</i>] &gt; [ &lt;<i>outfile</i>]&gt; ] ] </p>
<h2>DESCRIPTION</h2>
<p> Reads portable bitmap (PBM) format as input. Outputs a stream suitable for processing by Hewlett-Packard&#8217;s range of Printing Performance Architecture (PPA) printers. pnm2ppa supports the HP 710c, 712c, 720c, 722c, 820c, and 1000c series printers. </p>
<p> (Portable bitmap (PBM) format output can be produced from PostScript(tm) input by the GhostScript driver &quot;pbmraw&quot;.) </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>Iinfile</code></p>
<dd> Input file <i>infile</i> is either a path to a file or device, or &#8216;-&#8216; to indicate stdin (defaults to stdin) </p>
<dt><code>Ioutfile</code></p>
<dd> Output file <i>outfile</i> is either a path to a file or device, or &#8216;-&#8216; to indicate stdout (defaults to stdout) </p>
<dt><code>-b </code><i>bottommargin</i></p>
<dd> Sets the bottom margin <i>bottommargin</i> in units of 1/600 inches (e.g., -b 150 = 0.25&quot;) </p>
<dt><code>-d</code></p>
<dd> Displays the current configuration </p>
<dt><code>-f </code><i>configfile</i></p>
<dd> Overrides reading the configuration from /etc/pnm2ppa.conf, and uses <i>configfile</i> instead. </p>
<dt><code>-h</code></p>
<dd> Displays program usage </p>
<dt><code>-l </code><i>leftmargin</i></p>
<dd> Sets the left margin <i>leftmargin</i> in units of 1/600 inches (e.g., -l 150 = 0.25&quot;) </p>
<dt><code>-r </code><i>rightmargin</i></p>
<dd> Sets the right margin <i>rightmargin</i> in units of 1/600 inches (e.g., -r 150 = 0.25&quot;) </p>
<dt><code>-s </code><i>papersize</i></p>
<dd> Sets the paper size. Possible values for <i>papersize</i> are <code>a4</code> (A4), <code>letter</code> or <code>us</code> (US Letter, 8.5&quot;x11&quot;), and <code>legal</code> (US Legal, 8.5&quot;x14&quot;). The default is US Letter. </p>
<dt><code>-t </code><i>topmargin</i></p>
<dd> Sets the top margin <i>topmargin</i> in units of 1/600 inches (ie -t 150 = 0.25&quot;) </p>
<dt><code>-v </code><i>printertype</i></p>
<dd> Selects the printer model. Possible values of <i>printertype</i> are: <code>710</code>, <code>712</code>, <code>720</code>, <code>722</code>, <code>820</code> and <code>1000</code>. The default is the HP DeskJet 7X0 Series (710, 712, 720, 722). </p>
<dt><code>-x </code><i>xoffset</i></p>
<dd> Sets the x-offset <code>xoffset</code> from the left of the page. Units are 1/600 inches </p>
<dt><code>-y </code><i>yoffset</i></p>
<dd> Sets the y-offset <code>yoffset</code> from the top of the page. Units are 1/600 inches </p>
<p>&nbsp;<wbr></dl>
<h2>NOTES</h2>
<p> The configuration file is read in first. Command line arguments then modify the resulting definitions. </p>
<p> The -x and -y options accumulate. The -v option resets all definitions back to an inbuilt default for that printer and should be used before subsequent -b -l -r, -t, -x, and -y arguments.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pbm/">pbm</a>(5) </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/pbm2ppa.conf</i></p>
<dd> Default configuration file </p>
</dl>
<h2>AUTHOR</h2>
<p> This code is licensed under the GNU Public License version 2. See LICENSE for details. </p>
<p> (c) 1998<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Tim Norman</p>
<h2>HISTORY</h2>
<p> This program was written by Tim Norman. It originally supported black and white output on the 820 series. This program is almost obsolete; its successor pnm2ppa will support color printing.</p>
<h2>BUGS</h2>
<p> This is a stable driver, but does not support color printing. </p>
<h2>Index</h2>
