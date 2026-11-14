---
title: "bbkeys(1)"
name: "bbkeys"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bbkeys/"
description: "bbkeys – a general XWindow keygrabber"
---

<h2>NAME</h2>
<p> bbkeys &#8211; a general XWindow keygrabber </p>
<h2>SYNOPSIS</h2>
<p> <code>bbkeys</code> [<i>OPTION</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>bbkeys</code> is the keygrabber for the blackbox window manager. <code>bbkeys</code> handles all keybindings and keyboard shortcuts for blackbox. It uses blackbox&#8217;s Image classes for rendering its look and feel so that <code>bbkeys</code> will render itself to match whatever blackbox style is used. It is highly configurable either via the <i>bbconf</i> GUI utility or the (now deprecated) <i>bbkeysconf</i> GUI utility or by hand-editting bbkeys&#8217;s config file. </p>
<h2>USAGE</h2>
<p> On startup, <code>bbkeys</code> reads <i>$HOME/.bbkeysrc</i>, which you can edit by hand or through <i>bbconf</i> or <i>bbkeysconf</i>. This is now configurable through a command-line switch as show in OPTIONS. </p>
<h2>OPTIONS</h2>
<p> A summary of the options supported by <code>bbkeys</code> is included below. </p>
<dl>
<dt><code>-d or &#8211;display</code> <i>&lt;display name&gt;</i></p>
<dd> use alternate config file. (default is ~/.bbkeysrc)</p>
<dt><code>-D or &#8211;debug</code></p>
<dd> print debugging information</p>
<dt><code>-c or &#8211;config</code> <i>&lt;filename&gt;</i></p>
<dd> use alternate config file. (default is ~/.bbkeysrc)</p>
<dt><code>-v or &#8211;version</code></p>
<dd> display version number and exit</p>
<dt><code>-h or &#8211;help</code></p>
<dd> display help message </p>
</dl>
<h2>FILES</h2>
<p> <i></i><br />
 <i>$HOME/.bbkeysrc</i> maintains keybindings<br />
 See <i><a href="/docs/linux/man/5-bbkeysrc/">bbkeysrc</a>(5)</i> </p>
<h2>VERSION</h2>
<p> 0.9.0 </p>
<h2>BUGS</h2>
<p> This application is perfect and should solve all of your problems, up to and including male pattern baldness and world hunger. Should you, against all odds, find any bugs, please report them to the author. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-bbkeysrc/">bbkeysrc</a>(5)</code> </p>
<h2>AUTHOR</h2>
<h2>Index</h2>
