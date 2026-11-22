---

title: "tv_augment_tz(1)"
name: "tv_augment_tz"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_augment_tz/"
description: "tv_augment_tz – Convert floating time to explicit time."
---

<p> tv_augment_tz &#8211; Convert floating time to explicit time. </p>
<h2>SYNOPSIS</h2>
<p> tv_augment_tz [&#8211;help] [&#8211;output FILE] [&#8211;tz TIMEZONE] [FILE&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Read XMLTV data and augment all times with the correct offset. Times that are already explicit will be converted to TIMEZONE as well. </p>
<p> <code>&#8211;output </code><code>FILE</code> write to FILE rather than standard output </p>
<p> <code>&#8211;tz </code><code>TIMEZONE</code> use TIMEZONE (e.g. Europe/Berlin) rather then the default of UTC</p>
<h2>SEE ALSO</h2>
<p> <i>xmltv</i>(5).</p>
<h2>AUTHOR</h2>
<p> Karl Dietz, &lt;dekarl [at] spaetfruehstuecken.org&gt;</p>
<h2>BUGS</h2>
<p> Guessing the right time when local time is abigous doesn&#8217;t work properly. </p>
