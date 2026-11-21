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
<p>&nbsp;<wbr>night_exposure&nbsp;<wbr>[-t time]&nbsp;<wbr>[-s shutter on|off]&nbsp;<wbr>[-b 1|2|3]&nbsp;<wbr>[-o output]</p>
<p> The options are as follows: </p>
<p> options:</p>
<dl>
<dt><code>-t</code></dt>
<dd>
exposure time in seconds</dd>
<dt><code>-s</code></dt>
<dd>
shutter state, on &#8211; open, off &#8211; close for dark frame</dd>
<dt><code>-r</code></dt>
<dd>
select region by format:&nbsp;<wbr>(x1,y1,x2,y2), default: full area</dd>
<dt><code>-b</code></dt>
<dd>
binning, 1 &#8211; 1&#215;1, 2 &#8211; 2&#215;2, 3 &#8211; 3&#215;3, default: 3&nbsp;<wbr></dd>
<dt><code>-c</code></dt>
<dd>
select chip, I &#8211; imaging&nbsp;<wbr>(default), T &#8211; tracking</dd>
<dt><code>-m</code></dt>
<dd>
readout mode&nbsp;<wbr>(see output of&nbsp;<wbr>&#8216;night_power info&#8217;)</dd>
<dt><code>-o</code></dt>
<dd>
name of an output file, default to nightview.fits</dd>
<dt><code>-name</code></dt>
<dd> object&#8217;s name</dd>
<dt><code>-obsname</code></dt>
<dd> observer&#8217;s name</dd>
<dt><code>-p</code></dt>
<dd>
show progress indicator</dd>
<dt><code>-pn</code></dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>show progress indicator&nbsp;<wbr>(on new line)</dd>
<dt><code>-host</code></dt>
<dd> address:port internet address server, default: local connect</dd></dl>
<p> Use Ctrl-C to interrupt the exposure or download in progress.</p>
<h2>ENVIRONMENT</h2>
<p> Setting of environment variable NIGHTVIEW_HOST is equivalent to -host option.</p>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://integral.sci.muni.cz">http://integral.sci.muni.cz</a></p>
<h2>BUGS</h2>
<p> Not found except listed on <a rel="nofollow" href="http://integral.sci.muni.cz.">http://integral.sci.muni.cz.</a></p>
<h2>SEE ALSO</h2>
<p> nightview(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/">http://www.physics.muni.cz/mb/nightview/</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
