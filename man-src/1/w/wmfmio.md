---
title: "wmfmio(1)"
name: "wmfmio"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmfmio/"
description: "wmfmio – WindowMaker dockable application to manipulate fm radio card"
---

<h2>NAME</h2>
<p> <code>wmfmio</code> &#8211; WindowMaker dockable application to manipulate fm radio card</p>
<h2>SYNOPSIS</h2>
<p> <code>wmfmio</code> [-<code>n</code> ] [-<code>t </code><i>&lt;##:##&gt;</i> ] [-<code>p </code><i>&lt;##&gt;</i> ] [-<code>h</code> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>wmfmio</code> is a wmtune based WindowMaker dockable application that controls radio tuner cards supported by fmio utility. </p>
<p> The `+&#8217; and `-&#8216; buttons are for FINE tuning. </p>
<p> The 2 buttons to the right of the FINE tuning buttons are the SCAN buttons. </p>
<p> The 2 SCAN buttons also double as VOLUME UP/DOWN when using the RIGHT mouse button. </p>
<p> In the bottom left there is a small two digit box in which the currently selected preset will be shown. The `&lt;&#8216; and `&gt;&#8217; arrow buttons to the left of the box allow to switch between presets easily and quickly. </p>
<p> To the right of the above described things there is yet another button with a miniature ON/OFF logo. This is used to turn your radio card on/off. </p>
<p> The button with the inscribed letter &quot;A&quot; allows you to control the internal alarm clock/delay timer. Upon pressing the &quot;A&quot; button you will be allowed to set the timer/delay to a time you wish the radio to turn on/off (depending on the current state of the radio) automatically. </p>
<p> After pressing the &quot;A&quot; button the first time you may set the now displayed clock type panel to the desired setting using the SCAN buttons to set your timer in the 24-hour format. Be aware in this state other buttons cease to work. You must press the A button again at which point the indicator light will turn on and the alarm will be set. Lastly, pressing the &quot;A&quot; button once more, will disengance the timer. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-n</code></p>
<dd> Turn radio on initially on startup.</p>
<dt><code>-t </code><i>&lt;##:##&gt;</i></p>
<dd> Set timer on startup, military time.</p>
<dt><code>-p </code><i>&lt;##&gt;</i></p>
<dd> Set startup preset <i>&lt;##&gt;</i> listed in wmfmiorc file.</p>
<dt><code>-d </code><i>display</i></p>
<dd> Selects target display.</p>
<dt><code>-h</code></p>
<dd> Display help screen.</dl>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>wmfmio -n -p 5</code></p>
<dd> Turn on radio on startup using preset 5</p>
<dt><code>wmfmio -p 2 -t 14:35</code></p>
<dd> Turn radio on at 2:35pm using preset 2</p>
<dt><code>wmfmio -n -t 00:00</code></p>
<dd> Turn on radio on startup and turn radio off at midnight</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/wmfmiorc </code></p>
<dd> Global configuration file</p>
<dt><code>~/.wmfmiorc </code></p>
<dd> User configuration file</p>
<dt><code>/usr/local/bin/fmio </code></p>
<dd> Utility used to control the radiocard</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fmio/">fmio</a>(1)</p>
<h2>AUTHORS</h2>
<p> Author of wmtune &#8211; Soren Aq soren [at] leiden.org </p>
<p> Author of fmio &#8211; Vladimir Popov Aq jumbo [at] narod.ru </p>
<h2>Index</h2>
