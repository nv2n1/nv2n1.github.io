---
title: "jstest(1)"
name: "jstest"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstest/"
description: "jstest – joystick test program"
---

<h2>NAME</h2>
<p> jstest &#8211; joystick test program</p>
<h2>SYNOPSIS</h2>
<p> <code>jstest</code> [<code>&#8211;normal</code>] [<code>&#8211;old</code>] [<code>&#8211;event</code>] [<code>&#8211;nonblock</code>] [<code>&#8211;select</code>] &lt;<i>device-name</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>jstest</code> can be used to test all the features of the Linux joystick API, including non-blocking and <code><a href="/docs/linux/man/2-select/">select</a></code>(2) access, as well as version 0.x compatibility mode. </p>
<p> It is also intended to serve as an example implementation for those who wish to learn how to write their own joystick using applications.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;normal</code></p>
<dd> One-line mode showing immediate status.</p>
<dt><code>&#8211;old</code></p>
<dd> Same as &#8211;normal, using 0.x interface.</p>
<dt><code>&#8211;event</code></p>
<dd> Prints events as they come in.</p>
<dt><code>&#8211;nonblock</code></p>
<dd> Same as &#8211;event, in nonblocking mode.</p>
<dt><code>&#8211;select</code></p>
<dd> Same as &#8211;event, using <code><a href="/docs/linux/man/2-select/">select</a></code>(2) call.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fftest/">fftest</a></code>(1), <code><a href="/docs/linux/man/1-jscal/">jscal</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>jstest</code> was written by Vojtech Pavlik. </p>
<p> This manual page was written by Stephen Kitt &lt;steve [at] sk2.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
