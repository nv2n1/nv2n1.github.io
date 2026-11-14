---
title: "ibus-setup(1)"
name: "ibus-setup"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibus-setup/"
description: "ibus-setup – configuration program for ibus"
---

<h2 class="name">NAME</h2>
<p> <code>ibus-setup</code> &#8211; configuration program for ibus</p>
<h2>SYNOPSIS</h2>
<p> <code>ibus-setup</code> </p>
<h2>DESCRIPTION</h2>
<p> IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. </p>
<p> <code>ibus-setup</code> is the configuration program for IBus. </p>
<p> Homepage: <a rel="nofollow" href="https://github.com/ibus/ibus/wiki">https://github.com/ibus/ibus/wiki</a> </p>
<h2>ADVANCED</h2>
<dl>
<dt><code>Use system keyboard layout</code></p>
<dd> If this option is enabled, use your system keymap instead and IBus does not change it with any input method engines. The system keymap is decided by your desktop session. IBus calls <code>setxkbmap (1)</code> command internally to set the selected keymap and override the system keymap if this options is disabled. You can check the current keymap with <code>setxkbmap -query</code> command.</p>
<dt><code>Share the same input method among all applications</code></p>
<dd> If this option is disabled, You can choose an input metod engine by input context. </p>
</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibus/">ibus</a></code>(1) </p>
<h2>Index</h2>
