---
title: "tv_check(1)"
name: "tv_check"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_check/"
description: "tv_check – Check TV guide listings"
---

<h2 class="name">NAME</h2>
<p> tv_check &#8211; Check TV guide listings </p>
<h2>SYNOPSIS</h2>
<p> tv_check &#8211;configure|&#8211;scan [other options]</p>
<h2>DESCRIPTIONS</h2>
<p> tv_check is a Perl script that reads in a file with show information and checks it against a <font SIZE="-1">TV</font> guide listing, reporting on upcoming episodes and alerting you to unexpected episodes or schedule changes.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Run configuration <font SIZE="-1">GUI. </font> Either this option or &#8211;scan must be provided. </p>
<p> <code>&#8211;season-reset</code> special &#8211;configure option to remove everything but the title to help new season setup. The idea is to keep everything a &#8220;title-only&#8221; search until seasons begin. Then you update the details including record device. *expirimental* </p>
<p> <code>&#8211;scan</code> Scan <font SIZE="-1">TV</font> listings. Either this option or &#8211;configure must be provided. </p>
<p> <code>&#8211;myreplaytv=UNIT,USERNAME,PASSWORD</code> ** Feature removed ** This option used to auto-populate a config file based on myreplaytv.com. </p>
<p> <code>&#8211;shows=FILE</code> Specify the name of <font SIZE="-1">XML</font> shows file (default: shows.xml). </p>
<p> <code>&#8211;guide=FILE</code>, <code>&#8211;listings=FILE</code> Specify the name of <font SIZE="-1">XML</font> guide file (default: guide.xml). </p>
<p> <code>&#8211;html</code> Generate output in <font SIZE="-1">HTML</font> format. </p>
<p> <code>&#8211;bluenew</code> Highlights new episodes in blue (helpful back when there was an off-season) </p>
<p> <code>&#8211;output=FILE</code> Write to <font SIZE="-1">FILE</font> rather than standard output </p>
<p> <code>&#8211;help</code> Provide a usage/help listing.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Robert Eden; manpage by Kenneth J. Pronovici. </p>
<h2>Index</h2>
