---
title: "xdg-screensaver(1)"
name: "xdg-screensaver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-screensaver/"
description: "xdg-screensaver – command line tool for controlling the screensaver"
---

<h2 class="name">NAME</h2>
<p> xdg-screensaver &#8211; command line tool for controlling the screensaver </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-screensaver</code> <code>suspend&nbsp;</code><i>WindowID</i></p>
<dt> <code>xdg-screensaver</code> <code>resume&nbsp;</code><i>WindowID</i></p>
<dt> <code>xdg-screensaver</code> {<code>activate</code> | <code>lock</code> | <code>reset</code> | <code>status</code>}</p>
<dt> <code>xdg-screensaver</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dl>
<h2>DESCRIPTION</h2>
<dd>xdg-screensaver provides commands to control the screensaver. </p>
<p> xdg-screensaver is for use inside a desktop session only. It is not recommended to use xdg-screensaver as root.</p>
<h2>COMMANDS</h2>
<p> <code>suspend </code><i>WindowID</i></p>
<dl>
<dt>
<dd> Suspends the screensaver and monitor power management. <i>WindowID</i> must be the X Window ID of an existing window of the calling application. The window must remain in existence for the duration of the suspension. </p>
<p> WindowID can be represented as either a decimal number or as a hexadecimal number consisting of the prefix <i>0x</i> followed by one or more hexadecimal digits. </p>
<p> The screensaver can be suspended in relation to multiple windows at the same time. In that case screensaver operation is only restored once the screensaver has been resumed in relation to each of the windows</dl>
<p> <code>resume </code><i>WindowID</i></p>
<dl>
<dt>
<dd> Resume the screensaver and monitor power management after being suspended. <i>WindowID</i> must be the same X Window ID that was passed to a previous call of <code>xdg-screensaver suspend</code></dl>
<p> <code>activate</code></p>
<dl>
<dt>
<dd> Turns the screensaver on immediately. This may result in the screen getting locked, depending on existing system policies.</dl>
<p> <code>lock</code></p>
<dl>
<dt>
<dd> Lock the screen immediately.</dl>
<p> <code>reset</code></p>
<dl>
<dt>
<dd> Turns the screensaver off immediately. If the screen was locked the user may be asked to authenticate first.</dl>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Prints <i>enabled</i> to stdout if the screensaver is enabled to turn on after a period of inactivity and prints <i>disabled</i> if the screensaver is not enabled.</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show command synopsis.</dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
<dd> Show this manual page.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the xdg-utils version information.</dl>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned: </p>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Error in command line syntax.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> A required tool could not be found.</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> The action failed.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
xdg-screensaver suspend 0x1c00007
</pre>
</dl>
<p> Causes the screensaver to be disabled till <code>xdg-screensaver resume 0x1c00007</code> is called. <i>0x1c00007</i> must be the X Window ID of an existing window.</p>
<h2>AUTHOR</h2>
<p> <code>Bryce Harrington</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 </p>
<h2>Index</h2>
