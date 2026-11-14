---
title: "ibus-daemon(1)"
name: "ibus-daemon"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibus-daemon/"
description: "ibus-daemon – daemon program for ibus"
---

<h2 class="name">NAME</h2>
<p> <code>ibus-daemon</code> &#8211; daemon program for ibus</p>
<h2>SYNOPSIS</h2>
<p> <code>ibus-daemon</code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. </p>
<p> <code>ibus-daemon</code> is a daemon program for ibus and it is also a start up program for users to activate ibus daemon, engines and panel. </p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options </p>
</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;daemonize</code></p>
<dd> run ibus as background process.</p>
<dt><code>-s</code>, <code>&#8211;single</code></p>
<dd> do not execute panel and config module.</p>
<dt><code>-x</code>, <code>&#8211;xim</code></p>
<dd> execute ibus XIM server.</p>
<dt><code>-n</code>, <code>&#8211;desktop</code>=<i>name</i></p>
<dd> specify the name of desktop session. [default=gnome]</p>
<dt><code>-p</code>, <code>&#8211;panel</code>=<i>cmdline</i></p>
<dd> specify the cmdline of panel program.</p>
<dt><code>-c</code>, <code>&#8211;config</code>=<i>cmdline</i></p>
<dd> specify the cmdline of config program.</p>
<dt><code>-a</code>, <code>&#8211;address</code>=<i>address</i></p>
<dd> specify the address of ibus daemon.</p>
<dt><code>-r</code>, <code>&#8211;replace</code></p>
<dd> if there is an old ibus-daemon is running, it will be replaced.</p>
<dt><code>-t</code>, <code>&#8211;cache</code>=<i>mode</i> [default is auto]</p>
<dd> force to re-scan components, and re-create registry cache. auto, refresh, none is available.</p>
<dt><code>-o</code>, <code>&#8211;timeout</code>=<i>timeout</i> [default is 2000]</p>
<dd> dbus reply timeout in milliseconds.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> verbose. </p>
</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibus/">ibus</a></code>(1) </p>
<h2>Index</h2>
