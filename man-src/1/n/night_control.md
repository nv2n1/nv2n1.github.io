---
title: "night_control(1)"
name: "night_control"
section: "1"
letter: "n"
url: "/docs/linux/man/1-night_control/"
description: "night_batch – non-interactive snapshoting with CCD camera"
---

<h2>NAME</h2>
<p> night_batch &#8211; non-interactive snapshoting with CCD camera</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>night_control&nbsp;<wbr>[options]&nbsp;<wbr>exptime1,filter1&nbsp;<wbr>[exptime2,filter2]&nbsp;<wbr>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The options are as follows:</p>
<dl>
<dt><code>-oo</code></p>
<dd> output filename mask, default: &#8221;</p>
<dt><code>-o</code></p>
<dd> output prefix name, default: &#8216;image&#8217;</p>
<dt><code>-n</code></p>
<dd> number of exposures, default=0</p>
<dt><code>-obsname,-observer</code></p>
<dd> observer&#8217;s name</p>
<dt><code>-name,-object</code></p>
<dd> object&#8217;s name</p>
<dt><code>-d</code></p>
<dd> auto-dark substract, dark interval, default: 0 no darks</p>
<dt><code>-w</code></p>
<dd> wait for specified num. of seconds, integer, default: 1</p>
<dt><code>-b</code></p>
<dd> binning, default=3</p>
<dt><code>-r</code></p>
<dd> select region by format: (x1,y1,x2,y2), default: full area</p>
<dt><code>-c</code></p>
<dd> select chip, I &#8211; imaging (default), T &#8211; tracking</p>
<dt><code>-v</code></p>
<dd> view exposed image with xnightview</p>
<dt><code>-p</code></p>
<dd> &lt;x,y&gt; point mode</p>
<dt><code>-pr</code></p>
<dd> radius to locate pointer star on image in pixels (default: 30)</p>
<dt><code>-pp</code></p>
<dd> toleration for pointer mode in arc seconds (default: 10)</p>
<dt><code>-host</code></p>
<dd> address:port internet address server, default: local connect</p>
<dt><code>-h</code></p>
<dd> print help</dl>
<h2>ENVIRONMENT</h2>
<p> Setting of environment variable NIGHTVIEW_HOST is equivalent to -host option. </p>
<p> List of possible filters:</p>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://integral.sci.muni.cz">http://integral.sci.muni.cz</a></p>
<h2>BUGS</h2>
<p> Not found except listed on <a rel="nofollow" href="http://integral.sci.muni.cz.">http://integral.sci.muni.cz.</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nightview/">nightview</a>(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/">http://www.physics.muni.cz/mb/nightview/</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
