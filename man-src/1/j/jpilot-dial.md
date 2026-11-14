---
title: "jpilot-dial(1)"
name: "jpilot-dial"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpilot-dial/"
description: "jpilot-dial – generates the DTMF tone signals used for telephone dialing"
---

<h2>NAME</h2>
<p> jpilot-dial &#8211; generates the DTMF tone signals used for telephone dialing</p>
<h2>SYNOPSIS</h2>
<p> <code>jpilot-dial</code> [<i>options</i>]<i> number</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>jpilot-dial</code> generates the DTMF tone signals used for telephone dialing and by default sends the signals to the sound card. </p>
<p> It can be used for easy dialing, simply put the telephone microphone near the computer speaker and let the software dial for you. </p>
<p> It is intended for dialing from within database programs that also store telephone numbers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;tone-time</code></p>
<dd> milliseconds, default 100</p>
<dt><code>&#8211;silent-time</code></p>
<dd> milliseconds, default 50</p>
<dt><code>&#8211;sleep-time</code></p>
<dd> milliseconds, default 500</p>
<dt><code>&#8211;output-dev</code></p>
<dd> default <i>/dev/dsp</i></p>
<dt><code>&#8211;use-audio</code></p>
<dd> default 1</p>
<dt><code>&#8211;bufsize</code></p>
<dd> default 4096</p>
<dt><code>&#8211;speed</code></p>
<dd> default 8000</p>
<dt><code>&#8211;bits</code></p>
<dd> default 8</p>
<dt><code>&#8211;lv</code></p>
<dd> left speaker volume</p>
<dt><code>&#8211;rv</code></p>
<dd> right speaker volume</p>
<dt><code>&#8211;table-size</code></p>
<dd> default 256</p>
<dt><code>&#8211;volume</code></p>
<dd> default 100</p>
<dt><code>&#8211;left</code></p>
<dd> default 0</p>
<dt><code>&#8211;right</code></p>
<dd> default 0</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpilot/">jpilot</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ludovic Rousseau &lt;rousseau [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
