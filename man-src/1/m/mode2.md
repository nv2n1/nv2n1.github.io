---

title: "mode2(1)"
name: "mode2"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mode2/"
description: "mode2, xmode2 – shows the pulse/space length of infrared signals"
---

<h2>NAME</h2>
<p> mode2, xmode2 &#8211; shows the pulse/space length of infrared signals</p>
<p> <code>mode2</code> [<i>options</i>]</p>
<p> The main purpose of these programs is to check operation of your home-brew LIRC receiver hardware and to see the IR waveform of the remote controller without an expensive oscilloscope. Very useful for debugging. Of course this program won&#8217;t work with hardware that decodes the signals itself like e.g. TV cards or the Irman. </p>
<p> mode2 will simply print pulse&amp;space lengths to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> display usage summary</dd>
<dt><code>-v</code> <code>&#8211;version</code></dt>
<dd> display version</dd>
<dt><code>-d</code> <code>&#8211;device</code>=<i>device</i></dt>
<dd> read from given device</dd>
<dt><code>-H</code> <code>&#8211;driver</code>=<i>driver</i></dt>
<dd> use given driver</dd>
<dt><code>-m</code> <code>&#8211;mode</code></dt>
<dd> enable alternative display mode</dd>
<dt><code>-r</code> <code>&#8211;raw</code></dt>
<dd> access device directly</dd></dl>
<h2>DRIVER LOADING</h2>
<p> Drivers are loaded dynamically. The search path used for this is determined by (falling priority):</p>
<dl>
<dt>&#8211;</dt>
<dd> The &#8211;plugindir option if available.</dd>
<dt>&#8211;</dt>
<dd> The &#8216;plugindir&#8217; entry in the [lircd] section of the lirc_options.conf file.</dd>
<dt>&#8211;</dt>
<dd> The environment variable LIRC_PLUGINDIR.</dd>
<dt>&#8211;</dt>
<dd> A hardcoded default (usually /usr/lib[64]/lirc/plugins). </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.cache/mode2.log</code></dt>
<dd> Debug output. Setting the XDG_CACHE_HOME environment variable relocates this file to $XDG_CACHE_HOME/mode2.log </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mode2/">mode2</a>(1), <a href="/docs/linux/man/1-xmode2/">xmode2</a>(1) </p>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
