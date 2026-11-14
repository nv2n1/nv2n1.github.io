---
title: "grolbp(1)"
name: "grolbp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grolbp/"
description: "grolbp – groff driver for Canon CAPSL printers (LBP-4 and LBP-8 series laser printers)"
---

<h2 class="name">NAME</h2>
<p> grolbp &#8211; groff driver for Canon CAPSL printers (LBP-4 and LBP-8 series laser printers) </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-l</code> ] [ <code>-c </code><i>num-copies</i> ] [ <code>-F </code><i>font-directory</i> ] [ <code>-o </code><i>orientation</i> ] [ <code>-p </code><i>paper-size</i> ] [ <code>-w </code><i>width</i> ] [<i>file</i> &#8230;] [<code>&#8211;copies=</code><i>num-copies</i>] [<code>&#8211;fontdir=</code><i>font-directory</i>] [<code>&#8211;landscape</code>] [<code>&#8211;linewidth=</code><i>width</i>] [<code>&#8211;orientation=</code><i>orientation</i>] [<code>&#8211;papersize=</code><i>paper-size</i>] [<i>file</i> &#8230;] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>grolbp</code> is a driver for <code>groff</code> that produces output in CAPSL and VDM format suitable for Canon LBP-4 and LBP-8 printers. </p>
<p> For compatibility with <code><a href="/docs/linux/man/1-grolj4/">grolj4</a></code>(1) there is an additional drawing command available:</p>
<dl>
<dt><code>\D&#8217;R&nbsp;</code><i>dh dv</i><code>&#8216;</code></p>
<dd> Draw a rule (i.e., a solid black rectangle), with one corner at the current position, and the diagonally opposite corner at the current position +(<i>dh</i>,<i>dv</i>).</dl>
<h2>OPTIONS</h2>
<p> Note that there can be whitespace between a one-letter option and its argument; on the other hand, there must be whitespace and/or an equal sign (&#8216;=&#8217;) between a long-name option and its argument.</p>
<dl>
<dt><code>-c</code><i> num-copies</i></p>
<dd> <code>&#8211;copies=</code><i>num-copies</i> Print <i>num-copies</i> copies of each page.</p>
<dt><code>-F</code><i> font-directory</i></p>
<dd> <code>&#8211;fontdir=</code><i>font-directory</i> Prepend directory font-directory<i>/dev</i>name to the search path for font and device description files; <i>name</i> is the name of the device, usually <code>lbp</code>.</p>
<dt><code>-h</code></p>
<dd> <code>&#8211;help</code> Print a short help text.</p>
<dt><code>-l</code></p>
<dd> <code>&#8211;landscape</code> Print the document with a landscape orientation.</p>
<dt><code>-o</code><i> orientation</i></p>
<dd> <code>&#8211;orientation=</code><i>orientation</i> Print the document with <i>orientation</i> orientation, which must be &#8216;portrait&#8217; or &#8216;landscape&#8217;.</p>
<dt><code>-p</code><i> paper-size</i></p>
<dd> <code>&#8211;papersize=</code><i>paper-size</i> Set the paper size to <i>paper-size</i>, which must be a valid paper size description as indicated in section &#8220;Paper Sizes&#8221;, below.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Print the version number.</p>
<dt><code>-w</code><i> width</i></p>
<dd> <code>&#8211;linewidth=</code><i>width</i> Set the default line thickness to <i>width</i> thousandths of an em. If this option isn&#8217;t specified, the line thickness defaults to 0.04~em.</dl>
<h2>TYPEFACES</h2>
<p> The driver supports the Dutch, Swiss and Swiss-Narrow scalable typefaces, each one in the Regular, Bold, Italic and Bold-Italic styles. Additionally, the Courier and Elite monospaced typefaces at the sizes 8 and 12 points (for Courier) resp. 8 and 10 points (for Elite) are supported, each one in the Regular, Bold and Italic styles. </p>
<p> The following chart summarizes the font names you can use to access these fonts: </p>
<p> <center></p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center>Typeface </td>
<td ALIGN=center> Regular </td>
<td ALIGN=center> Bold </td>
<td ALIGN=center> Italic </td>
<td ALIGN=center> Bold-Italic
</td>
</tr>
<tr VALIGN=top>
<td><code>Dutch </code></td>
<td ALIGN=center> TR </td>
<td ALIGN=center> TB </td>
<td ALIGN=center> TI </td>
<td ALIGN=center> TBI
</td>
</tr>
<tr VALIGN=top>
<td>Swiss </td>
</tr>
<tr VALIGN=top>
<td>Swiss Narrow </td>
</tr>
<tr VALIGN=top>
<td>Courier </td>
</tr>
<tr VALIGN=top>
<td>Elite </td>
</tr>
</table>
<p></center></p>
<h2>PAPER SIZES</h2>
<p> The paper size can be set in the <i>DESC</i> file or with command-line options to <code>grolbp</code>. If the paper size is specified both ways, the command-line options take precedence over the contents of the <i>DESC</i> file (this applies to the page orientation too). </p>
<p> See <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) how to set the paper dimensions in the <i>DESC</i> file. </p>
<p> To set the paper size in the command line, add </p>
<p> <code>-p</code><i>&nbsp;paper-size</i> </p>
<p> or </p>
<p> <code>&#8211;papersize=</code><i>paper-size</i> </p>
<p> to the other <code>grolbp</code> options, where <i>paper-size</i> is in the same format as in the <i>DESC</i> file. </p>
<p> If no paper size is specified in the <i>DESC</i> file or the command line, a default size of A4 is used.</p>
<h2>PAGE ORIENTATION</h2>
<p> As with the page size, the orientation of the printed page (<code>portrait</code> or <code>landscape</code>) can be set in the <i>DESC</i> file or with command-line options. It is also case insensitive. </p>
<p> To set the orientation in the <i>DESC</i> file, insert a line with the following content: </p>
<p> <code>orientation</code> [<code>portrait</code>|<code>landscape</code>] </p>
<p> Only the first valid orientation command in the <i>DESC</i> file is used. </p>
<p> To set the page orientation with command-line options you can use the <code>-o</code> or <code>&#8211;orientation</code> option with the same parameters (<code>portrait</code> or <code>landscape</code>) as in the <i>DESC</i> file. Or you can use the <code>-l</code> option to force the pages to be printed in landscape.</p>
<h2>FONT FILE FORMAT</h2>
<p> In addition to the usual commands described in <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code>grolbp</code> provides the command <i>lbpname</i> which sets the font name sent to the printer when requesting this font. The syntax of this command is: </p>
<p> <code>lbpname</code> <i>printer_font_name</i></p>
<dl>
<dt>&bull;</p>
<dd> For bitmapped fonts, <i>printer_font_name</i> has the form </p>
<p> N&lt;<i>base_fontname</i>&gt;&lt;<i>font_style</i>&gt; </p>
<p> <i>base_fontname</i> is the font name as it appears in the printers font listings without the first letter, up to (but not including) the font size. <i>font_style</i> can be one of the letters <code>R</code>, <code>I</code>, or <code>B</code>, indicating the font styles Roman, Italic and Bold respectively.</p>
<dt>
<dd> For instance, if the printer&#8217;s <i>font listing A</i> shows font &#8216;Nelite12I.ISO_USA&#8217;, the corresponding entry in the font description file is </p>
<p> <code>lbpname NeliteI</code></p>
<dt>
<dd> Note that you may need to modify <code>grolbp</code> to add support for new bitmapped fonts, since the available font names and font sizes of bitmapped fonts (as documented above) are hard-coded into the program.</p>
<dt>&bull;</p>
<dd> For scalable fonts, <i>printer_font_name</i> is identical to the font name as it appears in the printer&#8217;s <i>font listing A</i>.</p>
<dt>
<dd> For instance, to select the &#8216;Swiss&#8217; font in bold style, which appears in the printer&#8217;s <i>font listing A</i> as &#8216;Swiss-Bold&#8217;, the required <code>lbpname</code> command line is </p>
<p> <code>lbpname Swiss-Bold</code> </p>
</dl>
<p> The argument of <code>lbpname</code> is case sensitive.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A list of directories in which to search for the <i>dev</i>name directory in addition to the default ones. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more details.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devlbp/DESC</i></p>
<dd> Device description file.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devlbp/</i>F</p>
<dd> Font description file for font <i>F</i>.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/lbp.tmac</i></p>
<dd> Macros for use with <code>grolbp</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) </p>
<h2>Index</h2>
