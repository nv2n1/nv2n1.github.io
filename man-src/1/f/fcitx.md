---
title: "fcitx(1)"
name: "fcitx"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcitx/"
description: "fcitx – Free Chinese Input Toy of X – a Chinese IME for XIM"
---

<h2 class="name">NAME</h2>
<p> fcitx &#8211; Free Chinese Input Toy of X &#8211; a Chinese IME for XIM </p>
<h2>SYNOPSIS</h2>
<p> <code>fcitx</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>fcitx</code> command. </p>
<p> <code>fcitx</code> is a Chinese IME for XIM intentionally designed not to depend on any Desktop Environment. It includes Pinyin and Table for input by default, but it can also support other Input Method.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> replace existing fcitx</p>
<dt><code>-d</code></p>
<dd> run as daemon(default)</p>
<dt><code>-D</code></p>
<dd> don&#8217;t run as daemon</p>
<dt><code>-s</code>[<i>sleep time</i>]</p>
<dd> override delay start time in config file, 0 for immediate start</p>
<dt><code>-u, &#8211;ui</code>[<i>ui name</i>]</p>
<dd> force to use specified user interface</p>
<dt><code>&#8211;enable</code>[<i>addon A,addon B</i>]</p>
<dd> specify a comma separated list for addon that will override the enable option</p>
<dt><code>&#8211;disable</code>[<i>addon A,addon B</i>]</p>
<dd> specify a comma separated list for addon that will explicitly disabled, priority is higher than &#8211;enable</p>
<dt><code>-v</code></p>
<dd> display the version information and exit</p>
<dt><code>-h</code></p>
<dd> display help and exit</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>XMODIFIERS</code></p>
<dd> If $<code>XMODIFIERS</code> is set, fcitx will run with the name that specified in $<code>XMODIFIERS</code> , otherwise it will run with im name fcitx.</dl>
<h2>SEE ALSO</h2>
<p> Please see the homepage at <code><a rel="nofollow" href="https://fcitx-im.org/">https://fcitx-im.org/</a></code> </p>
<h2>Index</h2>
