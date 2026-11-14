---
title: "mmafm(1)"
name: "mmafm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmafm/"
description: "mmafm – creates AFM font metrics for multiple master fonts"
---

<h2 class="name">NAME</h2>
<p> mmafm &#8211; creates AFM font metrics for multiple master fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>mmafm</code> [OPTIONS&#8230;] <i>font</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Mmafm</code> creates AFM font metrics for PostScript multiple master fonts by interpolation. You pass it an AMFM file (multiple master font metrics) and options specifying the design point you want, and it writes the resulting AFM file to the standard output. </p>
<p> Each <i>font</i> argument is either the filename of an AFM or AMFM font metrics file, or a PostScript font name. If you give a font name, <code>mmafm</code> will look up the actual font metrics file using the PSRESOURCEPATH environment variable. This colon-separated path is searched for `PSres.upr&#8217; files, an Adobe method for indexing PostScript resources. </p>
<p> You can also give the name of a multiple master font instance, like `MinionMM_367_400_12_&#8217;. <code>Mmafm</code> will parse the font name and create that instance for you. `PSres.upr&#8217; files must be set up for this to work. </p>
<p> Any multiple master font should be distributed with a single AMFM file and several AFM files (one for each master). For Myriad, for example, the AMFM file is MyriadMM.amfm and the AFM files are MyriadMM-LightCn.afm, MyriadMM-LightSemiEx.afm, MyriadMM-BlackCn.afm, and MyriadMM-BlackSemiEx.afm. <code>Mmafm</code> needs to find all these files to function. For fonts in the Adobe type library, you can download the necessary files from &lt;<a rel="nofollow" href="http://www.lcdf.org/type">http://www.lcdf.org/type</a>&gt;; look for the mm-metrics package. </p>
<p> You must always supply the AMFM file (or its font name) on the command line, but <code>mmafm</code> will look for any required AFM files you don&#8217;t supply yourself. It tries the PSRESOURCEPATH environment variable, and also looks for files named `<i>FontName</i>.afm&#8217; or `<i>FontName</i>.AFM&#8217; in the directory that contained the AMFM file. (The Myriad filenames given above fit this pattern.) </p>
<p> <code>Mmafm</code> supports fonts with intermediate masters, like Adobe Jenson and Kepler. If your PSRESOURCEPATH environment variable is set up, it will handle these fonts automatically. Otherwise, you must first run `<code>mmpfb &#8211;amcp-info</code>&#8216; on the font outline files to create auxiliary AMCP files for these fonts. Each AMCP file should be in the same directory as its corresponding AMFM file and should have the same root filename, but with a `.amcp&#8217; extension instead of `.amfm&#8217;. See for more information.</p>
<h2>EXAMPLE</h2>
<pre>
% mmafm --weight=400 --width=600 MyriadMM.amfm &gt; MyriadMM_400_600_.afm
</pre>
<h2>OPTIONS</h2>
<p> Long options may be abbreviated to their unique prefixes.</p>
<dl>
<dt> <code>&#8211;output</code>=<i>file</i>, <code>-o </code><i>file</i><i></i></p>
<dd> Send output to <i>file</i> instead of standard output.</p>
<dt> <code>&#8211;weight</code>=<i>N</i>, <code>-w </code><i>N</i><i></i></p>
<dd> Set the weight axis to <i>N</i>.</p>
<dt> <code>&#8211;width</code>=<i>N</i>, <code>-W </code><i>N</i><i></i></p>
<dd> Set the width axis to <i>N</i>.</p>
<dt> <code>&#8211;optical-size</code>=<i>N</i>, <code>-O </code><i>N</i><i></i></p>
<dd> Set the optical size axis to <i>N</i>.</p>
<dt> <code>&#8211;style</code>=<i>N</i><i></i><i></i></p>
<dd> Set the style axis to <i>N</i>.</p>
<dt><code>&#8211;1</code>=<i>N</i> (<code>&#8211;2</code>=<i>N</i>, <code>&#8211;3</code>=<i>N</i>, <code>&#8211;4</code>=<i>N</i>)</p>
<dd> Set the first (second, third, fourth) axis to <i>N</i>.</p>
<dt> <code>&#8211;precision</code>=<i>N</i>, <code>-p </code><i>N</i><i></i></p>
<dd> Round output numbers so they have at most <i>N</i> digits after the decimal point. Smaller numbers are less precise; `<code>-p </code>0&#8242; rounds all numbers to integers. The default precision is 3.</p>
<dt> <code>&#8211;min-kern</code>=<i>N</i>, <code>-k </code><i>N</i><i></i></p>
<dd> Only output kerning pairs whose absolute value is <i>N</i> or larger. Smaller minimum kerns make kerning more precise and the output AFM file bigger. The default minimum kern is 2.0.</dl>
<h2>TROUBLESHOOTING</h2>
<p> Some programs, such as TeX&#8217;s <code>fontinst</code>, can choke on AFM files that include fractional numbers. Therefore, if you have trouble with an AFM file, try rerunning <code>mmafm</code> with the <code>&#8211;precision=0</code> option.</p>
<h2>SEE ALSO</h2>
<h2>DIAGNOSTICS</h2>
<dl>
<dt><i>Font</i> requires intermediate master conversion programs</p>
<dd> You haven&#8217;t yet created an AMCP file for <i>Font</i>.</dl>
<h2>AUTHOR</h2>
<p> Eddie Kohler, ekohler [at] gmail.com </p>
<p> The latest version is available from:<br />
 <a rel="nofollow" href="http://www.lcdf.org/type/">http://www.lcdf.org/type/</a><br />
 AMFM and AFM files for Adobe Type Library fonts are also available at that URL. </p>
<p> Thanks to Melissa O&#8217;Neill for suggestions and patient debugging. </p>
<h2>Index</h2>
