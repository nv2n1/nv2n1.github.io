---
title: "telescope(1)"
name: "telescope"
section: "1"
letter: "t"
url: "/docs/linux/man/1-telescope/"
description: "Telescope mount position control"
---

<h2>NAME</h2>
<p> Telescope mount position control</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>telescope&nbsp;<wbr>[options]&nbsp;<wbr>[set | get]&nbsp;<wbr>[commands]</p>
<h2>DESCRIPTION</h2>
<p> The options are as follows: </p>
<p> options:</p>
<dl>
<dt><code>get:</code></p>
<dd> (specify nothing, one or more option)</p>
<dt><code>-ra</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print Right Ascension in degrees</p>
<dt><code>-dec</code></p>
<dd>
&nbsp;<wbr>print Declination in degrees</p>
<dt><code>-a</code></p>
<dd>
print Azimuth&nbsp;<wbr>(180 deg&nbsp;<wbr>=&nbsp;<wbr>sud)</p>
<dt><code>-z</code></p>
<dd>
print Altitude</p>
<dt><code>-ha</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print Hour Angle</p>
<dt><code>-jd</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print Julian date</p>
<dt><code>-synchro</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>sychronisation,(1=values are probably correct)</p>
<dt><code>-status</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print status of moving telescope</p>
<dt><code>-velstat</code></p>
<dd>
&nbsp;<wbr>RA and Dec velocities in format current/max</p>
<dt><code>set:</code></p>
<dd> (every option needs additional argument(s))</p>
<dt><code>-coo</code></p>
<dd> RA Dec set the Equatorial coordinates in degrees</p>
<dt><code>-coa</code></p>
<dd> HA Dec set the Equatorial coordinates (I. kind) in degrees</p>
<dt><code>-cal</code></p>
<dd> RA Dec calibrate Equatorial the coordinates in degrees</p>
<dt><code>+ra</code></p>
<dd> [ddd.d..] add value (may be negative) to R.A. in degrees</p>
<dt><code>+dec</code></p>
<dd> [ddd.d..] add value (may be negative) to Dec in degrees</p>
<dt><code>+ra</code></p>
<dd> [+|-] for continue slew without endpoint</p>
<dt><code>+dec</code></p>
<dd> [+|-] for continue slew without endpoint</p>
<dt><code>+ra</code></p>
<dd> ! stop slew in Right Ascension</p>
<dt><code>+dec</code></p>
<dd> ! stop slew in Declination</p>
<dt><code>-vra</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>set velocity of Right Ascension in degrees per second</p>
<dt><code>-vdec</code></p>
<dd>
&nbsp;<wbr>set velocity of Declination in degress per seconds</p>
<dt><code>-vclock</code></p>
<dd> set velocity of the hour clock</p>
<dt><code>-c</code></p>
<dd> on start the hour clock</p>
<dt><code>-c</code></p>
<dd> off stop the hour clock</dl>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> options:</p>
<dl>
<dt><code>-host</code></p>
<dd> address[:port] hostname of server, default to local</p>
<dt><code>-q</code></p>
<dd> don&#8217;t print telescope status during setting of telescope</p>
<dt><code>-pn</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>show progress indicator&nbsp;<wbr>(on new line)</p>
<dt><code>-h</code></p>
<dd> print this info</dl>
<p> Setting of environment variable TELESCOPE_HOST is equivalent to -host option.</p>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://integral.sci.muni.cz">http://integral.sci.muni.cz</a></p>
<h2>BUGS</h2>
<p> Not found except listed on <a rel="nofollow" href="http://integral.sci.muni.cz.">http://integral.sci.muni.cz.</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nightview/">nightview</a>(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/">http://www.physics.muni.cz/mb/nightview/</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
