---
title: "xdpr(1)"
name: "xdpr"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdpr/"
description: "xdpr – dump an X window directly to a printer"
---

<h2>NAME</h2>
<p> xdpr &#8211; dump an X window directly to a printer</p>
<h2>SYNOPSIS</h2>
<p> <code>xdpr</code> [ <i>filename</i> ] [ <code>-display</code> <i>host:display</i> ] [ <code>-P</code><i>printer</i> ] [ <code>-device</code> <i>devtype</i> ] [ <i>option</i> &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <i>Xdpr</i> uses the commands <i>xwd,</i> <i>xpr,</i> and <i>lpr</i> or <i>lp</i> to dump an X window, process it for a particular printer type, and print it out on the printer of your choice. This is the easiest way to get a printout of a window. <i>Xdpr</i> by default will print the largest possible representation of the window on the output page. </p>
<p> The options for <i>xdpr</i> are the same as those for <i>xpr</i>, <i>xwd</i>, and <i>lpr</i> or <i>lp</i>. The most commonly-used options are described below; see the manual pages for these commands for more detailed descriptions of the many options available.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>filename</i></dt>
<dd> Specifies a file containing a window dump (created by <i>xwd</i>) to be printed instead of selecting an X window.</dd>
<dt><code>-P</code><i>printer</i></dt>
<dd> Specifies a printer to send the output to. If a printer name is not specified here, <i>xdpr</i> (really, <i>lpr</i> or <i>lp</i>) will send your output to the printer specified by the <i>PRINTER</i> environment variable. Be sure that type of the printer matches the type specified with the <i>-device</i> option.</dd>
<dt><code>-display </code><i>host:display</i>[<i>.screen</i>]</dt>
<dd> Normally, <i>xdpr</i> gets the host and display number to use from the environment variable &#8220;DISPLAY.&#8221; One can, however, specify them explicitly; see <i>X</i>(1).</dd>
<dt><code>-device </code><i>devtype</i></dt>
<dd> Specifies the device on which the file will be printed. Currently supported:</dd>
<dl>
<dl>
<dt><code>la100</code></dt>
<dd> Digital LA100</dd>
<dt><code>ljet</code></dt>
<dd> HP LaserJet series and other monochrome PCL devices such as ThinkJet, QuietJet, RuggedWriter, <font SIZE="-1">HP</font>2560 series, and HP 2930 series printers</dd>
<dt><code>ln03</code></dt>
<dd> Digital LN03</dd>
<dt><code>pjet</code></dt>
<dd> HP PaintJet (color mode)</dd>
<dt><code>pjetxl</code></dt>
<dd> HP HP PaintJet XL Color Graphics Printer (color mode)</dd>
<dt><code>pp</code></dt>
<dd> IBM PP3812</dd>
<dt><code>ps</code></dt>
<dd> PostScript printer</dd></dl>
</dl>
<dt>
</dt><dd> The default is PostScript. <code>-device lw</code> (LaserWriter) is equivalent to <code>-device ps</code> and is provided only for backwards compatibility.</dd>
<dt><code>-help</code></dt>
<dd> This option displays the list of options known to <i>xdpr.</i></dd></dl>
<p> Any other arguments will be passed to the <i>xwd,</i> <i>xpr,</i> and <i>lpr</i> or <i>lp</i> commands as appropriate for each.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-xwd/">xwd</a></i>(1), <i><a href="/docs/linux/man/1-xpr/">xpr</a></i>(1), <i><a href="/docs/linux/man/1-lpr/">lpr</a></i>(1), <i><a href="/docs/linux/man/1-lp/">lp</a></i>(1), <i><a href="/docs/linux/man/1-xwud/">xwud</a></i>(1), <i>X</i>(1)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>DISPLAY</dt>
<dd> which display to use by default.</dd>
<dt>PRINTER</dt>
<dd> which printer to use by default.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright X Consortium<br />
 See <i>X(1)</i> for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> Paul Boutin, MIT Project Athena<br />
 Michael R. Gretzinger, MIT Project Athena<br />
 Jim Gettys, MIT Project Athena </p>
<h2>Index</h2>
