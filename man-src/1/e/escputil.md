---
title: "escputil(1)"
name: "escputil"
section: "1"
letter: "e"
url: "/docs/linux/man/1-escputil/"
description: "escputil – maintain Epson Stylus inkjet printers"
---

<h2>NAME</h2>
<p> escputil &#8211; maintain Epson Stylus inkjet printers</p>
<h2>SYNOPSIS</h2>
<p> <code>escputil</code> [ <i>-P</i> <i>printer</i> | <i>-r</i> <i>device</i> ] [ <i>-m</i> <i>model</i> ] [ <i>-S</i> ] [ <i>-C</i> ] [ <i>-p</i> ] [ <i>-u</i> ] [ <i>-c</i> | <i>-n</i> | <i>-a</i> | <i>-i</i> | <i>-d</i> | <i>-o</i> | <i>-s</i> | <i>-l</i> | <i>-M</i> | <i>-h</i> ] [ <i>-q</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>escputil</code> is a command line utility to perform various maintenance tasks on Epson Stylus inkjet printers. These tasks include head alignment, head cleaning, nozzle check, printer identification, and retrieval of ink level from the printer.</p>
<h2>OPTIONS</h2>
<p> <code>escputil</code> accepts the following options:</p>
<dl>
<dt><code>-P, &#8211;printer-name=</code><i>printer</i></p>
<dd> Specify the name of the printer to operate on. The default is the default system printer.</p>
<dt><code>-r, &#8211;raw-device=</code><i>device</i></p>
<dd> Specify the name of the device to write to directly rather than going through a printer queue. You must use this (rather than specifying a printer) when retrieving ink levels or identifying the printer, or if you wish to perform head alignment without specifying the printer model.</p>
<dt><code>-m, &#8211;model=</code><i>model</i></p>
<dd> Specify the precise printer model for head alignment.</p>
<dt><code>-u, &#8211;new</code></p>
<dd> The printer is a new printer (Stylus Color 740 or newer).</p>
<dt><code>-S, &#8211;short-name</code></p>
<dd> Print the short name of the printer with &#8211;identify.</p>
<dt><code>-C, &#8211;choices</code></p>
<dd> Specify the number of pattern choices for alignment.</p>
<dt><code>-p, &#8211;patterns</code></p>
<dd> Specify the number of sets of patterns for alignment.</p>
<dt><code>-c, &#8211;clean-head</code></p>
<dd> Clean the print head. This can also be performed from the printer front panel.</p>
<dt><code>-n, &#8211;nozzle-check</code></p>
<dd> Print a nozzle test pattern. Dirty or clogged nozzles will show as gaps in the pattern. If you see any gaps, you should run a head cleaning pass or two.</p>
<dt><code>-a, &#8211;align-head</code></p>
<dd> Align the print head. CAUTION: Misuse of this option may result in poor print quality and/or damage to the printer. You must either specify the printer model with the -m option, or use the raw printer device to allow escputil to detect the printer model.</p>
<dt><code>-i, &#8211;ink-level</code></p>
<dd> Obtain the ink level from the printer. This requires read/write access to the raw printer device.</p>
<dt><code>-d, &#8211;identify</code></p>
<dd> Query the printer for make and model information. This requires read/write access to the raw printer device.</p>
<dt><code>-o, &#8211;align-color</code></p>
<dd> Align the color print head (used by Stylus Color 480 and 580 only). CAUTION: Misuse of this option may result in poor print quality and/or damage to the printer.</p>
<dt><code>-s, &#8211;status</code></p>
<dd> Retrieve printer status.</p>
<dt><code>-l, &#8211;license</code></p>
<dd> Display the license/warranty terms of this program.</p>
<dt><code>-M, &#8211;list-models</code></p>
<dd> List the supported printer models.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a list of all command line options.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress the banner.</dl>
<h2>BUGS</h2>
<p> USB-connected printers sometimes fail to identify or return ink levels. You may have to repeat the command. This is probably a timing issue in escputil, not a flaw in the printer. </p>
<p> Anything requiring bidirectional communication with the printer (identify, ink levels, or head alignment without specifying the printer model) requires read/write access to the printer port (for example /dev/lp0). This may require these operations to be performed as root. In addition, kernel support is required for bidirectional communication. For Linux version 2.2, <i>CONFIG_PRINTER_READBACK</i> should be enabled; this is called <i>CONFIG_PARPORT_1284</i> on 2.4 and later kernels. </p>
<p> If the printer is performing self-test or head cleaning on power up, the identify and ink level commands will time out, although the printer successfully receives the command. The command will need to be reissued when the printer is quiescent.</p>
<h2>AUTHORS</h2>
<p> Robert Krawitz.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000 Robert Krawitz (rlk [at] alum.mit.edu) </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>OTHER INFORMATION</h2>
<p> The homepage of the Gutenprint project from which this utility was contributed is located at <a rel="nofollow" href="http://gimp-print.sourceforge.net/.">http://gimp-print.sourceforge.net/.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/4-lp/">lp</a></code>(4), <code><a href="/docs/linux/man/8-tunelp/">tunelp</a></code>(8). </p>
<h2>Index</h2>
