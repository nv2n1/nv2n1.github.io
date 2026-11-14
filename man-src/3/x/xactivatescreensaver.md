---
title: "xactivatescreensaver(3)"
name: "xactivatescreensaver"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xactivatescreensaver/"
description: "XSetScreenSaver, XForceScreenSaver, XActivateScreenSaver, XResetScreenSaver, XGetScreenSaver – manipulate the screen saver"
---

<p>XSetScreenSaver, XForceScreenSaver, XActivateScreenSaver, XResetScreenSaver, XGetScreenSaver &#8211; manipulate the screen saver </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetScreenSaver(Display *<i>display</i>, int <i>timeout</i>, int <i>interval</i>, int <i>prefer_blanking</i>, int <i>allow_exposures</i>);</p>
<dd>int XForceScreenSaver(Display *<i>display</i>, int <i>mode</i>);</p>
<dd>int XActivateScreenSaver(Display *<i>display</i>);</p>
<dd>int XResetScreenSaver(Display *<i>display</i>);</p>
<dd>int XGetScreenSaver(Display *<i>display</i>, int *<i>timeout_return</i>, int *<i>interval_return</i>, int *<i>prefer_blanking_return</i>, int *<i>allow_exposures_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>allow_exposures</i></p>
<dd>Specifies the screen save control values. You can pass <code>DontAllowExposures</code>, <code>AllowExposures</code>, or <code>DefaultExposures</code>.</p>
<dt><i>allow_exposures_return</i></p>
<dd>Returns the current screen save control value <code>AllowExposures</code>, or <code>DefaultExposures</code>).</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>interval</i></p>
<dd>Specifies the interval, in seconds, between screen saver alterations.</p>
<dt><i>interval_return</i></p>
<dd>Returns the interval between screen saver invocations.</p>
<dt><i>mode</i></p>
<dd>Specifies the mode that is to be applied. You can pass <code>ScreenSaverActive</code> or <code>ScreenSaverReset</code>.</p>
<dt><i>prefer_blanking</i></p>
<dd>Specifies how to enable screen blanking. You can pass <code>DontPreferBlanking</code>, <code>PreferBlanking</code>, or <code>DefaultBlanking</code>.</p>
<dt><i>prefer_blanking_return</i></p>
<dd>Returns the current screen blanking preference <code>PreferBlanking</code>, or <code>DefaultBlanking</code>).</p>
<dt><i>timeout</i></p>
<dd>Specifies the timeout, in seconds, until the screen saver turns on.</p>
<dt><i>timeout_return</i></p>
<dd>Returns the timeout, in seconds, until the screen saver turns on.</dl>
<h2>Description</h2>
<p>Timeout and interval are specified in seconds. A timeout of 0 disables the screen saver (but an activated screen saver is not deactivated), and a timeout of -1 restores the default. Other negative values generate a <code>BadValue</code> error. If the timeout value is nonzero, <code>XSetScreenSaver</code></p>
