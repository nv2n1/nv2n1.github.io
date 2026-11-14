---
title: "tv_augment_tz(1)"
name: "tv_augment_tz"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_augment_tz/"
description: "tv_augment_tz – Convert floating time to explicit time."
---

<h2 class="name">NAME</h2>
<p> tv_augment_tz &#8211; Convert floating time to explicit time. </p>
<h2>SYNOPSIS</h2>
<p> tv_augment_tz [&#8211;help] [&#8211;output <font SIZE="-1">FILE</font>] [&#8211;tz <font SIZE="-1">TIMEZONE</font>] [<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Read <font SIZE="-1">XMLTV</font> data and augment all times with the correct offset. Times that are already explicit will be converted to <font SIZE="-1">TIMEZONE</font> as well. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output </p>
<p> <code>&#8211;tz </code><font SIZE="-1"><code>TIMEZONE</code></font> use <font SIZE="-1">TIMEZONE </font>(e.g. Europe/Berlin) rather then the default of <font SIZE="-1">UTC</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Karl Dietz, &lt;dekarl [at] spaetfruehstuecken.org&gt;</p>
<h2>BUGS</h2>
<p> Guessing the right time when local time is abigous doesn&#8217;t work properly. </p>
<h2>Index</h2>
