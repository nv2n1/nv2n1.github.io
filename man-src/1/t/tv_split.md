---
title: "tv_split(1)"
name: "tv_split"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_split/"
description: "tv_split – Split XMLTV listings into separate files by date and channel."
---

<h2 class="name">NAME</h2>
<p> tv_split &#8211; Split XMLTV listings into separate files by date and channel. </p>
<h2>SYNOPSIS</h2>
<p> tv_split &#8211;output <font SIZE="-1">TEMPLATE</font> [<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Read <font SIZE="-1">XMLTV</font> listings and split them into some number of output files. The output file chosen for each programme is given by substitutions on the filename template supplied. You can split listings by time and by channel. </p>
<p> The <font SIZE="-1">TEMPLATE</font> is a filename but substitutions are applied: first <tt>%channel</tt> is replaced with the id of a programme&#8217;s channel, and then Date::Manip substitutions (which broadly follow <i><a href="/docs/linux/man/1-date/">date</a></i>(1)) are applied based on the start time of each programme. In this way each programme is written to a particular output file. When an output file is created it will also contain all the channel elements from the input. </p>
<p> One or more input files can be given; if more than one then they are concatenated in the same way as tv_cat. If no input files are given then standard input is read.</p>
<h2>EXAMPLE</h2>
<p> Use <tt>&quot;tv_split --output %channel-%Y%m%d.xml&quot;</tt> to separate standard input into separate files for each day and channel. The files will be created with names like <code>bbc1.bbc.co.uk-20020330.xml</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-date--manip/">Date::Manip</a></i>(3).</p>
<h2>AUTHOR</h2>
<p> Ed Avis, ed [at] membled.com. </p>
<h2>Index</h2>
