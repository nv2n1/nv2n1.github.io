---
title: "night_exposure(1)"
name: "night_exposure"
section: "1"
letter: "n"
url: "/docs/linux/man/1-night_exposure/"
description: "night_exposure – make a single exposure on a camera"
---

<h2>NAME</h2>
<p> night_exposure &#8211; make a single exposure on a camera</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>night_exposure&nbsp;<wbr>[-t time]&nbsp;<wbr>[-s shutter on|off]&nbsp;<wbr>[-b 1|2|3]&nbsp;<wbr>[-o output]</p>
<h2>DESCRIPTION</h2>
<p> The options are as follows: </p>
<p> options:</p>
<dl>
<dt><code>-t</code></p>
<dd>
exposure time in seconds</p>
<dt><code>-s</code></p>
<dd>
shutter state, on &#8211; open, off &#8211; close for dark frame</p>
<dt><code>-r</code></p>
<dd>
select region by format:&nbsp;<wbr>(x1,y1,x2,y2), default: full area</p>
<dt><code>-b</code></p>
<dd>
binning, 1 &#8211; 1&#215;1, 2 &#8211; 2&#215;2, 3 &#8211; 3&#215;3, default: 3&nbsp;<wbr></p>
<dt><code>-c</code></p>
<dd>
select chip, I &#8211; imaging&nbsp;<wbr>(default), T &#8211; tracking</p>
<dt><code>-m</code></p>
<dd>
readout mode&nbsp;<wbr>(see output of&nbsp;<wbr>&#8216;night_power info&#8217;)</p>
<dt><code>-o</code></p>
<dd>
name of an output file, default to nightview.fits</p>
<dt><code>-name</code></p>
<dd> object&#8217;s name</p>
<dt><code>-obsname</code></p>
<dd> observer&#8217;s name</p>
<dt><code>-p</code></p>
<dd>
show progress indicator</p>
<dt><code>-pn</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>show progress indicator&nbsp;<wbr>(on new line)</p>
<dt><code>-host</code></p>
<dd> address:port internet address server, default: local connect</dl>
<p> Use Ctrl-C to interrupt the exposure or download in progress.</p>
<h2>ENVIRONMENT</h2>
<p> Setting of environment variable NIGHTVIEW_HOST is equivalent to -host option.</p>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://integral.sci.muni.cz">http://integral.sci.muni.cz</a></p>
<h2>BUGS</h2>
<p> Not found except listed on <a rel="nofollow" href="http://integral.sci.muni.cz.">http://integral.sci.muni.cz.</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nightview/">nightview</a>(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/">http://www.physics.muni.cz/mb/nightview/</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
