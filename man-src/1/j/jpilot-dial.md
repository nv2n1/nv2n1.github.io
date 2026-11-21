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
<p> <code>jpilot-dial</code> [<i>options</i>]<i> number</i>&#8230;</p>
<p> <code>jpilot-dial</code> generates the DTMF tone signals used for telephone dialing and by default sends the signals to the sound card. </p>
<p> It can be used for easy dialing, simply put the telephone microphone near the computer speaker and let the software dial for you. </p>
<p> It is intended for dialing from within database programs that also store telephone numbers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;tone-time</code></dt>
<dd> milliseconds, default 100</dd>
<dt><code>&#8211;silent-time</code></dt>
<dd> milliseconds, default 50</dd>
<dt><code>&#8211;sleep-time</code></dt>
<dd> milliseconds, default 500</dd>
<dt><code>&#8211;output-dev</code></dt>
<dd> default <i>/dev/dsp</i></dd>
<dt><code>&#8211;use-audio</code></dt>
<dd> default 1</dd>
<dt><code>&#8211;bufsize</code></dt>
<dd> default 4096</dd>
<dt><code>&#8211;speed</code></dt>
<dd> default 8000</dd>
<dt><code>&#8211;bits</code></dt>
<dd> default 8</dd>
<dt><code>&#8211;lv</code></dt>
<dd> left speaker volume</dd>
<dt><code>&#8211;rv</code></dt>
<dd> right speaker volume</dd>
<dt><code>&#8211;table-size</code></dt>
<dd> default 256</dd>
<dt><code>&#8211;volume</code></dt>
<dd> default 100</dd>
<dt><code>&#8211;left</code></dt>
<dd> default 0</dd>
<dt><code>&#8211;right</code></dt>
<dd> default 0</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpilot/">jpilot</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ludovic Rousseau &lt;rousseau [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
