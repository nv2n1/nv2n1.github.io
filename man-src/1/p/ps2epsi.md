---
title: "ps2epsi(1)"
name: "ps2epsi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2epsi/"
description: "ps2epsi – generate conforming Encapsulated PostScript"
---

<h2 class="name">NAME</h2>
<p> ps2epsi &#8211; generate conforming Encapsulated PostScript </p>
<h2>SYNOPSIS</h2>
<p> <code>ps2epsi</code> <i>infile.ps</i> [ <i>outfile.epsi</i> ] <code>(Unix)</code><br />
 <code>ps2epsi</code> <i>infile.ps</i> [ <i>outfile.epi</i> ] <code>(DOS)</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ps2epsi</code> uses <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to process a <code>PostScript</code>(tm) file and generate as output a new file which conforms to Adobe&#8217;s <code>Encapsulated PostScript Interchange</code> (EPSI) format. EPSI is a special form of encapsulated PostScript (EPS) which adds to the beginning of the file in the form of PostScript comments a bitmapped version of the final displayed page. Programs which understand EPSI (usually word processors or DTP programs) can use this bitmap to give a preview version on screen of the PostScript. The displayed quality is often not very good (e.g., low resolution, no colours), but the final printed version uses the real PostScript, and thus has the normal PostScript quality.</p>
<h2>USAGE</h2>
<p> On Unix systems invoke <code>ps2epsi</code> like this: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><code>ps2epsi</code> <i>infile.ps</i> [ <i>outfile.epsi</i> ]</p>
<p> where &quot;infile.ps&quot; is the input file and &quot;outfile.epsi&quot; is the resulting EPSI file. If the output filename is omitted, it is generated from the input filename. When a standard extension (&quot;.ps&quot;, &quot;.cps&quot;, &quot;.eps&quot; or &quot;.epsf&quot;) is used, it is replaced with the output extension &quot;.epsi&quot;. On DOS systems the command is: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><code>ps2epsi</code> <i>infile.ps outfile.epi</i></p>
<p> where &quot;infile.ps&quot; is the original PostScript file, and &quot;outfile.epi&quot; is the name of the output file.</p>
<h2>LIMITATIONS</h2>
<p> Not every PostScript file can be encapsulated successfully, because there are restrictions on what PostScript constructs a correct encapsulated file may contain. <code>ps2epsi</code> does a little extra work to try to help encapsulation, and it automatically calculates the bounding box required for all encapsulated PostScript files, so most of the time it does a pretty good job. There are certain to be cases, however, where the encapsulation does not work because of the content of the original PostScript file.</p>
<h2>COMPATIBILITY</h2>
<p> The <code>Framemaker</code> DTP system is one application which understands EPSI files, and <code>ps2epsi</code> has been tested on a number of PostScript diagrams from a variety of sources, using Framemaker 3.0 on a Sun workstation. Framemaker on other platforms should be able to use these files, although I have not been able to test this.</p>
<h2>FILES</h2>
<table>
<tr VALIGN=top>
<td>ps2epsi</td>
<td>Unix shell script
</td>
</tr>
<tr VALIGN=top>
<td>ps2epsi.bat</td>
<td>DOS batch file
</td>
</tr>
<tr VALIGN=top>
<td>ps2epsi.ps</td>
<td>the Ghostscript program which does the work
</td>
</tr>
</table>
<h2>SEE ALSO</h2>
<p> gs (1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0. However, the content may be obsolete, or inconsistent with ps2epsi.txt.</p>
<h2>AUTHOR</h2>
<p> George Cameron </p>
<h2>Index</h2>
