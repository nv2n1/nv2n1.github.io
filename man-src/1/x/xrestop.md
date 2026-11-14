---
title: "xrestop(1)"
name: "xrestop"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrestop/"
description: "xrestop – monitor server resources used by X11 clients"
---

<h2>NAME</h2>
<p> xrestop &#8211; monitor server resources used by X11 clients</p>
<h2>SYNOPSIS</h2>
<p> <code>xrestop &#8211;help</code><br />
 <code>xrestop</code> [ <code>&#8211;display</code> display ] [ <code>&#8211;batch</code> ] [ <code>&#8211;delay-time</code> seconds ] [ <code>&#8211;max-samples</code> count ]</p>
<h2>DESCRIPTION</h2>
<p> Xrestop uses the X-Resource extension to provide &#8216;top&#8217;-like statistics of each connected X11 client&#8217;s server-side resource usage. It is intended as a developer tool to aid more efficient server resource usage and debug server-side resource leakage.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show usage.</p>
<dt><code>&#8211;display, -d</code> &lt;display&gt;</p>
<dd> Specify X11 display to monitor.</p>
<dt><code>&#8211;delay-time, -t</code> &lt;seconds&gt;</p>
<dd> Time in seconds between taking samples. Default is 2 seconds.</p>
<dt><code>&#8211;batch, -b</code></p>
<dd> Run in batch mode. Slightly more detailed infomation is streamed to stdout rather than the usual curses interface. This mode is intended for debugging a single client with something like </p>
<p>&nbsp;<wbr>&nbsp;<wbr>xrestop -b | grep -A 14 appname</p>
<dt><code>&#8211;max-samples, -m</code> &lt;count&gt;</p>
<dd> Specify number of times to gather and display results. Default is continuous, which can be set with 0 (zero).
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-top/">top</a></code>(1)<code>.</code></p>
<h2>BUGS</h2>
<p> The X-Resource extension is very new and may not be 100% accurate.</p>
<h2>AUTHOR</h2>
<p> <code>xrestop</code> was written by Matthew Allum &lt;mallum [at] handhelds.org&gt;. </p>
<h2>Index</h2>
