---
title: "ibus-conf(5)"
name: "ibus-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ibus-conf/"
description: "ibus.conf – X input preload/configuration file for ibus"
---

<p><code>ibus.conf</code> &#8211; X input preload/configuration file for ibus </p>
<h2>Synopsis</h2>
<p><code>/etc/X11/xinit/xinput.d/ibus.conf</code> </p>
<h2>Description</h2>
<p>IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. <code>ibus.conf</code> is a configuration file containing X input setting values to be read in and set by /etc/X11/xinit/xinitrc-common. <i><a href="/docs/linux/man/1-imsettings-switch/">imsettings-switch</a>(1)</i> is called from XDG auto-start and invokes xinitrc-common. If this file is the alias of <i>/etc/X11/xinit/xinputrc</i> for the system setting or <i>[$XDG_CONFIG_HOME|$HOME/.config]/imsettings/xinputrc</i> for the user setting, the setting can be default. <i><a href="/docs/linux/man/1-im-chooser/">im-chooser</a>(1)</i> can choose the user setting. The configuration options are:</p>
<dl>
<dt><code>XIM</code></p>
<dd>XIM name for XMODIFIERS</p>
<dt><code>XIM_PROGRAM</code></p>
<dd>XIM executable program name</p>
<dt><code>XIM_ARGS</code></p>
<dd>XIM arguments for XIM_PROGRAM</p>
<dt><code>SHORT_DESC</code></p>
<dd>XIM human readable name for <i><a href="/docs/linux/man/1-im-chooser/">im-chooser</a>(1)</i></p>
<dt><code>ICON</code></p>
<dd>icon file for <i><a href="/docs/linux/man/1-im-chooser/">im-chooser</a>(1)</i></p>
<dt><code>PREFERENCE_PROGRAM</code></p>
<dd>XIM setup program for <i><a href="/docs/linux/man/1-im-chooser/">im-chooser</a>(1)</i></p>
<dt><code>GTK_IM_MODULE</code></p>
<dd>IM environment valuable for GTK+ applications.</p>
<dt><code>QT_IM_MODULE</code></p>
<dd>IM environment valuable for QT applications. </p>
<h2>Bugs</h2>
<p>If you find a bug, please report it at <a rel="nofollow" href="http://code.google.com/p/ibus/issues/list">http://code.google.com/p/ibus/issues/list</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ibus-daemon/">ibus-daemon</a></code>(1) <code><a href="/docs/linux/man/1-imsettings-switch/">imsettings-switch</a></code>(1) <code><a href="/docs/linux/man/1-im-chooser/">im-chooser</a></code>(1) <code><a href="/docs/linux/man/7-x/">X</a></code>(7) </p>
