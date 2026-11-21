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
<dt><code>get:</code></dt>
<dd> (specify nothing, one or more option)</dd>
<dt><code>-ra</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print Right Ascension in degrees</dd>
<dt><code>-dec</code></dt>
<dd>
&nbsp;<wbr>print Declination in degrees</dd>
<dt><code>-a</code></dt>
<dd>
print Azimuth&nbsp;<wbr>(180 deg&nbsp;<wbr>=&nbsp;<wbr>sud)</dd>
<dt><code>-z</code></dt>
<dd>
print Altitude</dd>
<dt><code>-ha</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print Hour Angle</dd>
<dt><code>-jd</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print Julian date</dd>
<dt><code>-synchro</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>sychronisation,(1=values are probably correct)</dd>
<dt><code>-status</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>print status of moving telescope</dd>
<dt><code>-velstat</code></dt>
<dd>
&nbsp;<wbr>RA and Dec velocities in format current/max</dd>
<dt><code>set:</code></dt>
<dd> (every option needs additional argument(s))</dd>
<dt><code>-coo</code></dt>
<dd> RA Dec set the Equatorial coordinates in degrees</dd>
<dt><code>-coa</code></dt>
<dd> HA Dec set the Equatorial coordinates (I. kind) in degrees</dd>
<dt><code>-cal</code></dt>
<dd> RA Dec calibrate Equatorial the coordinates in degrees</dd>
<dt><code>+ra</code></dt>
<dd> [ddd.d..] add value (may be negative) to R.A. in degrees</dd>
<dt><code>+dec</code></dt>
<dd> [ddd.d..] add value (may be negative) to Dec in degrees</dd>
<dt><code>+ra</code></dt>
<dd> [+|-] for continue slew without endpoint</dd>
<dt><code>+dec</code></dt>
<dd> [+|-] for continue slew without endpoint</dd>
<dt><code>+ra</code></dt>
<dd> ! stop slew in Right Ascension</dd>
<dt><code>+dec</code></dt>
<dd> ! stop slew in Declination</dd>
<dt><code>-vra</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>set velocity of Right Ascension in degrees per second</dd>
<dt><code>-vdec</code></dt>
<dd>
&nbsp;<wbr>set velocity of Declination in degress per seconds</dd>
<dt><code>-vclock</code></dt>
<dd> set velocity of the hour clock</dd>
<dt><code>-c</code></dt>
<dd> on start the hour clock</dd>
<dt><code>-c</code></dt>
<dd> off stop the hour clock</dd></dl>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> options:</p>
<dl>
<dt><code>-host</code></dt>
<dd> address[:port] hostname of server, default to local</dd>
<dt><code>-q</code></dt>
<dd> don&#8217;t print telescope status during setting of telescope</dd>
<dt><code>-pn</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>show progress indicator&nbsp;<wbr>(on new line)</dd>
<dt><code>-h</code></dt>
<dd> print this info</dd></dl>
<p> Setting of environment variable TELESCOPE_HOST is equivalent to -host option.</p>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://integral.sci.muni.cz">http://integral.sci.muni.cz</a></p>
<h2>BUGS</h2>
<p> Not found except listed on <a rel="nofollow" href="http://integral.sci.muni.cz.">http://integral.sci.muni.cz.</a></p>
<h2>SEE ALSO</h2>
<p> nightview(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/">http://www.physics.muni.cz/mb/nightview/</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
