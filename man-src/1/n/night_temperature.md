---
title: "night_temperature(1)"
name: "night_temperature"
section: "1"
letter: "n"
url: "/docs/linux/man/1-night_temperature/"
description: "night_temperature – a camera temperature"
---

<h2>NAME</h2>
<p> night_temperature &#8211; a camera temperature</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>night_temperature&nbsp;<wbr>[get|set]&nbsp;<wbr>[-t temperature]&nbsp;<wbr>[-off]&nbsp;<wbr>[-host address]</p>
<h2>DESCRIPTION</h2>
<p> The options are as follows: </p>
<p> options </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> get:</p>
<dl>
<dt><code>-t</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print ccd current temperature in degrees of Celsius</p>
<dt><code>-ta</code></p>
<dd>
&nbsp;<wbr>print air current temperature in degrees of Celsius</p>
<dt><code>-ts</code></p>
<dd>
&nbsp;<wbr>print temperature setpoint in degrees of Celsius</p>
<dt><code>-r</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print current cooling power&nbsp;<wbr>(relatively, in percents)</p>
<dt><code>-f</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print current status of fan, on or off</dl>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> without switches print all available cooling information</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> set:</p>
<dl>
<dt><code>-t</code></p>
<dd> temperature set temperature of a cooler</p>
<dt><code>-off</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set regulation of temperature to off</p>
<dt><code>-host</code></p>
<dd> address:port internet address server, local connect is default</dl>
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
