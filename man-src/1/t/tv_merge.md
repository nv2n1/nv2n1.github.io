---
title: "tv_merge(1)"
name: "tv_merge"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_merge/"
description: "tv_merge – Merge (combine) two XMLTV files."
---

<h2 class="name">NAME</h2>
<p> tv_merge &#8211; Merge (combine) two XMLTV files. </p>
<h2>SYNOPSIS</h2>
<p> tv_merge -i <font SIZE="-1">FILE</font> -m <font SIZE="-1">FILE</font> -o <font SIZE="-1">FILE</font></p>
<h2>DESCRIPTION</h2>
<p> Read <font SIZE="-1">XMLTV</font> listings from two files and merge them together. Unlike tv_cat (which just joins files) this will update (add/replace/delete) the origin <font SIZE="-1">XMLTV</font> file with channels and programmes contained in the second file. </p>
<p> It works with multiple channels, and will insert any new programmes and delete any overlapping programmes. </p>
<p> <font SIZE="-1"><code>IMPORTANT</code></font> The input files must be pre-sorted into datetime within channel order by using the &#8220;&#8211;by-channel&#8221; option to tv_sort<br />
&nbsp;<wbr>&nbsp;<wbr>e.g. tv_sort &#8211;by-channel &#8211;output&nbsp;<wbr><font SIZE="-1">FILE&nbsp;<wbr>&nbsp;<wbr>FILE</font> </p>
<p> All programmes must have start and stop times. </p>
<p> (Note: Programmes in the merged-in file <i>replace</i> any in the master file, i.e. data are not updated <i>within</i> programmes) </p>
<p> This program uses XML::TreePP which doesn&#8217;t write &lt;<font SIZE="-1">DOCTYPE</font>&gt; definitions in the output file. If you need to add a suitable &lt;<font SIZE="-1">DOCTYPE</font>&gt; tag then use the -t parameter.<br />
&nbsp;<wbr>&nbsp;<wbr>e.g. tv_merge -i&nbsp;<wbr><font SIZE="-1">FILE</font>&nbsp;<wbr>-m&nbsp;<wbr><font SIZE="-1">FILE</font>&nbsp;<wbr>-o&nbsp;<wbr><font SIZE="-1">FILE</font>&nbsp;<wbr>-t</p>
<h2>EXAMPLE</h2>
<p> Use <tt>&quot;tv_merge -i master.xml -m newadditions.xml -o newmaster.xml&quot;</tt> to merge all channels/programmes in <i>newadditions.xml</i>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright Geoff Westcott, February 2013. </p>
<p> This code is distributed under the <font SIZE="-1">GNU</font> General Public License v2 (GPLv2) . </p>
<h2>Index</h2>
