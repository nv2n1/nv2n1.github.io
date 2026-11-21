---

title: "fcitx(1)"
name: "fcitx"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcitx/"
description: "fcitx – Free Chinese Input Toy of X – a Chinese IME for XIM"
---

<p> fcitx &#8211; Free Chinese Input Toy of X &#8211; a Chinese IME for XIM </p>
<h2>SYNOPSIS</h2>
<p> <code>fcitx</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>fcitx</code> command. </p>
<p> <code>fcitx</code> is a Chinese IME for XIM intentionally designed not to depend on any Desktop Environment. It includes Pinyin and Table for input by default, but it can also support other Input Method.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></dt>
<dd> replace existing fcitx</dd>
<dt><code>-d</code></dt>
<dd> run as daemon(default)</dd>
<dt><code>-D</code></dt>
<dd> don&#8217;t run as daemon</dd>
<dt><code>-s</code>[<i>sleep time</i>]</dt>
<dd> override delay start time in config file, 0 for immediate start</dd>
<dt><code>-u, &#8211;ui</code>[<i>ui name</i>]</dt>
<dd> force to use specified user interface</dd>
<dt><code>&#8211;enable</code>[<i>addon A,addon B</i>]</dt>
<dd> specify a comma separated list for addon that will override the enable option</dd>
<dt><code>&#8211;disable</code>[<i>addon A,addon B</i>]</dt>
<dd> specify a comma separated list for addon that will explicitly disabled, priority is higher than &#8211;enable</dd>
<dt><code>-v</code></dt>
<dd> display the version information and exit</dd>
<dt><code>-h</code></dt>
<dd> display help and exit</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>XMODIFIERS</code></dt>
<dd> If $<code>XMODIFIERS</code> is set, fcitx will run with the name that specified in $<code>XMODIFIERS</code> , otherwise it will run with im name fcitx.</dd></dl>
<h2>SEE ALSO</h2>
<p> Please see the homepage at <code><a rel="nofollow" href="https://fcitx-im.org/">https://fcitx-im.org/</a></code> </p>
