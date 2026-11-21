---

title: "night_flats(1)"
name: "night_flats"
section: "1"
letter: "n"
url: "/docs/linux/man/1-night_flats/"
description: "night_flats – non-iteractive flat snapshoting with CCD camera"
---

<h2>NAME</h2>
<p> night_flats &#8211; non-iteractive flat snapshoting with CCD camera</p>
<p>&nbsp;<wbr>night_flats&nbsp;<wbr>[options]&nbsp;<wbr>exptime1,filter1&nbsp;<wbr>[exptime2,filter2]&nbsp;<wbr>&#8230;</p>
<p> The options are as follows:</p>
<dl>
<dt><code>-oo</code></dt>
<dd> output filename mask, default: &#8221;</dd>
<dt><code>-o</code></dt>
<dd> output prefix name, default: &#8216;f&#8217;</dd>
<dt><code>-n</code></dt>
<dd> number of exposures, default=0</dd>
<dt><code>-obsname,-observer</code></dt>
<dd> observer&#8217;s name</dd>
<dt><code>-name,-object</code></dt>
<dd> object&#8217;s name, default: -name flat</dd>
<dt><code>-d</code></dt>
<dd> auto-dark substract, dark interval, default: 0 no darks</dd>
<dt><code>-w</code></dt>
<dd> wait for specified num. of seconds, integer, default: 1</dd>
<dt><code>-b</code></dt>
<dd> binning, default=3</dd>
<dt><code>-r</code></dt>
<dd> select region by format: (x1,y1,x2,y2), default: full area</dd>
<dt><code>-c</code></dt>
<dd> select chip, I &#8211; imaging (default), T &#8211; tracking</dd>
<dt><code>-v</code></dt>
<dd> view exposed image with xnightview</dd>
<dt><code>-host</code></dt>
<dd> address:port internet address server, default: local connect</dd>
<dt><code>-h</code></dt>
<dd> print help</dd></dl>
<h2>ENVIRONMENT</h2>
<p> Setting of environment variable NIGHTVIEW_HOST is equivalent to -host option. </p>
<p> List of possible filters:</p>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://integral.sci.muni.cz">http://integral.sci.muni.cz</a></p>
<h2>BUGS</h2>
<p> Not found except listed on <a rel="nofollow" href="http://integral.sci.muni.cz.">http://integral.sci.muni.cz.</a></p>
<h2>SEE ALSO</h2>
<p> nightview(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/">http://www.physics.muni.cz/mb/nightview/</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
