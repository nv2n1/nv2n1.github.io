---
title: "pbmtoppa(1)"
name: "pbmtoppa"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtoppa/"
description: "pbmtoppa – convert PBM image to HP Printer Performance Architecture (PPA)"
---

<h2 class="name">NAME</h2>
<p> pbmtoppa &#8211; convert PBM image to HP Printer Performance Architecture (PPA) </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtoppa</code> </p>
<p> [<i>pbm_file</i> [<i>ppa_file</i>]] </p>
<h2>DESCRIPTION</h2>
<p> <code>pbmtoppa</code> converts page images in PBM format to Hewlett Packard&#8217;s PPA (Printer Performance Architecture) format, which is the data stream format expected by some HP &quot;Windows-only&quot; printers including the HP Deskjet 820C series, the HP DeskJet 720 series, and the HP DeskJet 1000 series. </p>
<p> <i>pbm_file</i> is the file specification of the input file or <code>&#8211;</code> for Standard Input. The default is Standard Input. </p>
<p> The input file contains one or more PBM images, with each one being a single page. Each image must have the exact dimensions of a page (at 600 pixels per inch in both directions). Significantly, this is the format the Ghostscript produces. </p>
<p> <i>ppa_file</i> is the file specification of the output file or <code>&#8211;</code> for Standard Output. The default is Standard Output. </p>
<p> To print Postscript on an HP PPA printer, just use Ghostscript with the <code>pbmraw</code> (or <code>pbm</code>) device driver. </p>
<p> You can generate a test page for use with this program with <code>pbmpage</code>. </p>
<p> You can also set up a printer filter so you can submit PBM input directly to your print queue. See the documentation for your print spooler for information on how to do that, or look in hp820install.doc for an example lpd print filter for Postscript and text files. </p>
<p> Sometimes, <code>pbmtoppa</code> generates a file which the printer will not print (because <code>pbmtoppa</code>&#8216;s input is unprintable). When this happens, all three lights blink to signal the error. This is usually because there is material outside of the printer&#8217;s printable area. To make the file print, increase the margins via <code>pbmtoppa</code> options or a configuration file. See the CALIBRATION section below. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v </code><i>version</i></p>
<dd> printer version (720, 820, or 1000)</p>
<dt><code>-x </code><i>xoff</i></p>
<dd> vertical offset adjustment in 1&quot;/600</p>
<dt><code>-y </code><i>yoff</i></p>
<dd> horizontal offset adjustment in 1&quot;/600</p>
<dt><code>-t </code><i>topmarg</i></p>
<dd> top margin in 1&quot;/600 (default: 150 = 0.25&quot;)</p>
<dt><code>-l </code><i>leftmarg</i></p>
<dd> left margin in 1&quot;/600 (default: 150 = 0.25&quot;)</p>
<dt><code>-r </code><i>rightmarg</i></p>
<dd> right margin in 1&quot;/600 (default: 150 = 0.25&quot;)</p>
<dt><code>-b </code><i>botmarg</i></p>
<dd> bottom margin in 1&quot;/600 (default: 150 = 0.25&quot;)</p>
<dt><code>-s </code><i>paper</i></p>
<dd> paper size: <code>us </code> or <code>a4</code>. Default is <code>us</code>.</p>
<dt><code>-f </code><i>cfgfile</i></p>
<dd> read parameters from configuration file <i>cfgfile </i> </p>
</dl>
<p> The <code>-x </code> and <code>-y </code> options accumulate. </p>
<p> The <code>-v </code> option resets the horizontal and vertical adjustments to an internal default. </p>
<h2>CONFIGURATION FILES</h2>
<p> You can use configuration files to specify parameters rather than use invocation options. <code>pbmtoppa</code> processes the file /etc/pbmtoppa.conf, if it exists, before processing any options. It then processes each configuration file named by a <code>-f</code> option in order, applying the parameters from the configuration file as if they were invocation options used in the place of the <code>-f</code> option. </p>
<p> Configuration files have the following format: </p>
<p> <code>#</code><i>Comment</i><br />
 <i>key1</i> <i>value1</i><br />
 <i>key2</i> <i>value2</i><br />
 [etc.] </p>
<p> Valid <i>key</i>s are <code>version</code>, <code>xoffset</code>, <code>yoffset</code>, <code>topmargin</code>, <code>leftmargin</code>, <code>rightmargin</code>, <code>bottommargin</code>, <code>papersize</code>, or any non-null prefix of these words. Valid values are the same as with the corresponding invocation parameters. </p>
<h2>EXAMPLES</h2>
<p> Print a test pattern: </p>
<p> <code>pbmpage | pbmppa &gt;/dev/lp1</code> </p>
<p> Print three pages: </p>
<p> <code>cat page1.pbm page2.pbm page3.pbm | pbmppa &gt;/dev/lp1</code> </p>
<p> Print the Postscript file myfile.ps: </p>
<p> <code>gs -sDEVICE=rawpbm -q -dNOPAUSE -r600 \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-sOutputFile=- myfile.ps&nbsp;\<br />
 | pbmtoppa | lpr </code> </p>
<h2>CALIBRATION</h2>
<p> To be able to print successfully and properly, you need to tell <code>pbmtoppa</code> an X and a Y offset appropriate for your printer to use when generating the page. You can specify these offsets with the <code>-x </code> and <code>-y</code> invocation options or with the <code>xoff</code> and <code>yoff</code> parameters in a <code>pbmtoppa</code> configuration file. </p>
<p> To determine the correct offsets, use the <code>pbmpage</code> program. </p>
<p> If while trying to do this calibration, the printer refuses to print a page, but just blinks all three lights, specify large margins (e.g. 600 pixels &#8212; one inch) via <code>pbmpage</code> invocation options while doing the calibration. </p>
<p> For example: </p>
<p> <code>pbmpage | pbmtoppa &gt;/dev/lp1</code><br />
 or<br />
 <code>pbmpage | pbmtoppa | lpr -l</code><br />
 (if your printer filter recognizes the &#8216;-l&#8217; (direct output) parameter). </p>
<p> In the test pattern, the grid is marked off in pixel coordinate numbers. Unfortunately, these coordinates are probably cut off before the edge of the paper. You&#8217;ll have to use a ruler to estimate the pixel coordinate of the left and top edges of the actual sheet of paper (should be within +/- 300, may be negative; there are 600 pixels per inch). </p>
<p> Add these coordinates to the X and Y offsets by either editing the configuration file or using the <code>-x </code> and <code>-y</code> command-line parameters. </p>
<p> When <code>pbmtoppa</code> is properly calibrated, the center mark should be in the center of the paper. Also, the margins should be able to be as small as 1/4 inch without causing the printer to choke with &#8216;blinking lights syndrome&#8217;. </p>
<h2>REDHAT LINUX INSTALLATION</h2>
<p> RedHat users may find the following tip from Panayotis Vryonis &lt;vrypan [at] hol.gr&gt; helpful. The same should work for the 820 and 1000, but it hasn&#8217;t been tested. Also, use the pbmraw GSDriver if you have it; it&#8217;s faster. </p>
<p> Here is a tip to intergrate HP720C support in RedHat&#8217;s printtool: </p>
<p> Install pbm2ppa. Copy pbm2ppa to /usr/bin. </p>
<p> Edit &quot;printerdb&quot; (in my system it is found in /usr/lib/rhs/rhs-printfilters ) and append the following lines: </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-Cut here&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
 StartEntry: DeskJet720C<br />
&nbsp;<wbr>&nbsp;GSDriver: pbm<br />
&nbsp;<wbr>&nbsp;Description:&nbsp;{HP DeskJet 720C}<br />
&nbsp;<wbr>&nbsp;About:&nbsp;{&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This driver supports the HP DeskJet 720C&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inkjet printer.&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;It does does not support color printing.&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IMPORTANT!&nbsp;Insert&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;- | pbm2ppa -&quot;&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in the&nbsp;&quot;Extra GS Otions&quot;&nbsp;field.\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;Resolution:&nbsp;{600}&nbsp;{600}&nbsp;{}<br />
 EndEntry &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;- </p>
<p> Now you can add an HP720C printer just like any other, using printtool. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmpage/">pbmpage</a></code>(1), <code><a href="/docs/linux/man/1-pstopnm/">pstopnm</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<p> <code>pnm2ppa</code> is not part of Netpbm, but does the same things as <code>pbmtoppa</code> except it also works with color and has lots more features. See &lt;<a rel="nofollow" href="http://sourceforge.net/project/?group_id=1322">http://sourceforge.net/project/?group_id=1322</a>&gt;. </p>
<p> The file INSTALL-MORE in the pbmtoppa directory of the Netpbm source code contains detailed instructions on setting up a system to use pbmtoppa to allow convenient printing on HP PPA printers. It was written by Michael Buehlmann. </p>
<p> For information about the PPA protocol and the separately distributed pbm2ppa program from which <code>pbmtoppa</code> was derived, see &lt;<a rel="nofollow" href="http://www.httptech.com/ppa">http://www.httptech.com/ppa</a>&gt;. </p>
<h2>AUTHOR</h2>
<p> Tim Norman. Copyright (C) 1998. Licensed under GNU Public License </p>
<p> Manual page by Bryan Henderson, May 2000. </p>
<h2>Index</h2>
