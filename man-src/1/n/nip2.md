---
title: "nip2(1)"
name: "nip2"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nip2/"
description: "nip2 – image processing with the VIPS library"
---

<h2 class="name">NAME</h2>
<p> nip2 &#8211; image processing with the VIPS library</p>
<h2>SYNOPSIS</h2>
<p> <code>nip2 [filename1 &#8230;]</code><br />
 <code>nip2 -s filename [arg1 &#8230;]</code><br />
 <code>nip2 -e expression [arg1 &#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>nip2</code> (for New Image Processing) is a tool for manipulating images using the VIPS image processing library. </p>
<p> There are three principal modes: </p>
<p> <code>nip2 [filename1 &#8230;]</code> </p>
<p>&nbsp;<wbr>&nbsp;start in GUI mode, loading the named files </p>
<p> <code>nip2 -e expression [arg1 &#8230;]</code><br />
 <code>nip2 &#8211;expression=EXPRESSION [arg1 &#8230;]</code> </p>
<p>&nbsp;<wbr>&nbsp;start in no-GUI mode;&nbsp;set main&nbsp;=&nbsp;expression, set list argv to<br />
&nbsp;<wbr>&nbsp;[&quot;filename&quot;,&nbsp;&quot;arg1&quot;,&nbsp;&quot;arg2&quot;, &#8230;], set argc to length of list;&nbsp;print<br />
&nbsp;<wbr>&nbsp;the value of symbol&nbsp;&quot;main&quot;&nbsp;to stdout;&nbsp;exit </p>
<p> <code>nip2 -s filename [arg1 &#8230;]</code><br />
 <code>nip2 &#8211;script=FILENAME [arg1 &#8230;]</code> </p>
<p>&nbsp;<wbr>&nbsp;start in no-GUI mode;&nbsp;read in filename as a set of definitions,&nbsp;<br />
&nbsp;<wbr>&nbsp;set list argv to&nbsp;[&quot;filename&quot;,&nbsp;&quot;arg1&quot;,&nbsp;&quot;arg2&quot;, &#8230;], set argc to&nbsp;<br />
&nbsp;<wbr>&nbsp;length of list;&nbsp;print the value of symbol&nbsp;&quot;main&quot;&nbsp;to stdout;&nbsp;exit;&nbsp;<br />
&nbsp;<wbr>&nbsp;useful for running nip2 as an interpreter on unix </p>
<p> You can use <code>-o</code> to direct output to a file rather than stdout. </p>
<p> <code>-o filename</code><br />
 <code>&#8211;output=FILENAME</code> </p>
<p>&nbsp;<wbr>&nbsp;the value of main is written to the named file. If main is a&nbsp;<br />
&nbsp;<wbr>&nbsp;list, the filename is incremented between objects. You can use&nbsp;<br />
&nbsp;<wbr>&nbsp;the suffix to specify the format and options to write in </p>
<p> Other options provide finer control over startup and shutdown. If you need to do something strange, don&#8217;t use -e/-s, use these in combination. </p>
<p> <code>-b</code><br />
 <code>&#8211;batch</code> </p>
<p>&nbsp;<wbr>&nbsp;batch&nbsp;(ie. non-GUI)&nbsp;mode </p>
<p> <code>-m</code><br />
 <code>&#8211;no-load-menus</code> </p>
<p>&nbsp;<wbr>&nbsp;don&#8217;t load menus, for faster startup </p>
<p> <code>-a</code><br />
 <code>&#8211;no-load-args</code> </p>
<p>&nbsp;<wbr>&nbsp;don&#8217;t load extra command-line arguments </p>
<p> <code>-w</code><br />
 <code>&#8211;stdin-ws</code> </p>
<p>&nbsp;<wbr>&nbsp;load stdin as a workspace </p>
<p> <code>-d</code><br />
 <code>&#8211;stdin-def</code> </p>
<p>&nbsp;<wbr>&nbsp;load stdin as a set of definitions </p>
<p> <code>-p</code><br />
 <code>&#8211;print-main</code> </p>
<p>&nbsp;<wbr>&nbsp;print the value of main on exit. nip2 will check for a top-level&nbsp;<br />
&nbsp;<wbr>&nbsp;symbol called main, and also check each workspace for a main </p>
<p> Finally some other options are useful for debugging, timing and for generating strings for internationalisation. </p>
<p> <code>-V</code><br />
 <code>&#8211;verbose</code> </p>
<p>&nbsp;<wbr>&nbsp;produce verbose error messages: handy for debugging in batch mode </p>
<p> <code>-i</code><br />
 <code>&#8211;i18n</code> </p>
<p>&nbsp;<wbr>&nbsp;output strings from .def files for internationalisation </p>
<p> <code>-v</code><br />
 <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>&nbsp;print version information </p>
<p> <code>-c</code><br />
 <code>&#8211;benchmark</code> </p>
<p>&nbsp;<wbr>&nbsp;benchmark: no GUI, just start up and shut down </p>
<p> <code>-t</code><br />
 <code>&#8211;time-save</code> </p>
<p>&nbsp;<wbr>&nbsp;time saves: after every image save a popup tells you the time the&nbsp;<br />
&nbsp;<wbr>&nbsp;save took in seconds </p>
<p> <code>-T</code><br />
 <code>&#8211;test</code> </p>
<p>&nbsp;<wbr>&nbsp;test: start up&nbsp;(including any arg processing), test for any errors,&nbsp;<br />
&nbsp;<wbr>&nbsp;and exit with an error code if any occured. Useful for running&nbsp;<br />
&nbsp;<wbr>&nbsp;automated tests. </p>
<p> <code>-x PREFIX</code><br />
 <code>&#8211;prefix=PREFIX</code> </p>
<p>&nbsp;<wbr>&nbsp;set install prefix: start up as if nip2 had been installed to PREFIX.<br />
&nbsp;<wbr>&nbsp;Useful for running automated tests without installing the thing. </p>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>&nbsp;nip2 fred.jpg </p>
<p> Start nip2, loading fred.jpg. </p>
<p>&nbsp;<wbr>&nbsp;nip2 -e&nbsp;&quot;2&nbsp;+&nbsp;2&quot; </p>
<p> Prints 4 to stdout. </p>
<p>&nbsp;<wbr>&nbsp;nip2 -e&nbsp;&quot;99&nbsp;+&nbsp;Image_file argv?1&quot;&nbsp;-o result.png fred.jpg </p>
<p> Load argv1 (fred.jpg), add 99, output to result.png. </p>
<p>&nbsp;<wbr>&nbsp;nip2 -e&nbsp;&quot;Matrix&nbsp;[[1,2],[4,5]]&nbsp;**&nbsp;-1&quot;&nbsp;-o poop.mat </p>
<p> Invert the 2&#215;2 matrix and write the result to poop.mat. </p>
<h2>COPYRIGHT</h2>
<p> 2008 (c) Imperial College, London </p>
<h2>Index</h2>
