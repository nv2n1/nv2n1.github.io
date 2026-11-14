---
title: "mate-screenshot(1)"
name: "mate-screenshot"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-screenshot/"
description: "mate-screenshot – capture the screen, a window, or an user-defined area and save the snapshot image to a file."
---

<h2>NAME</h2>
<p> mate-screenshot &#8211; capture the screen, a window, or an user-defined area and save the snapshot image to a file.</p>
<h2>SYNOPSIS</h2>
<p> <code>mate-screenshot</code> [ <code>-w</code> ] [ <code>-a</code> ] [ <code>-b</code> ] [ <code>-B</code> ] [ <code>-d </code><i>SECONDS</i> ] [ <code>-e </code><i>EFFECT</i> ] [ <code>-i</code> ] [ <code>&#8211;display </code><i>DISPLAY</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>mate-screenshot</code> is a MATE utility for taking screenshots of the entire screen, a window or an user-defined area of the screen, with optional beutifying border effects.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w, &#8211;window</code></p>
<dd> Grab the current active window instead of the entire screen.</p>
<dt><code>-a, &#8211;area</code></p>
<dd> Grab an area of the screen instead of the entire screen.</p>
<dt><code>-b, &#8211;include-border</code></p>
<dd> Include the window border within the screenshot.</p>
<dt><code>-B, &#8211;remove-border</code></p>
<dd> Remove the window border from the screenshot.</p>
<dt><code>-d, &#8211;delay=</code><i>SECONDS</i><code>,</code></p>
<dd> Take the screenshot after the specified delay [in seconds].</p>
<dt><code>-e, &#8211;effect=</code><i>EFFECT</i><code>,</code></p>
<dd> Add an effect to the outside of the screenshot border. <i>EFFECT</i> can be &#8220;shadow&#8221; (adding drop shadow), &#8220;border&#8221; (adding rectangular space around the screenshot) or &#8220;none&#8221; (no effect). Default is &#8220;none&#8221;.</p>
<dt><code>-i, &#8211;interactive</code></p>
<dd> Interactively set options in a dialog.</p>
<dt><code>&#8211;display=</code><i>DISPLAY</i></p>
<dd> X display to use.</p>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Show a summary of the available options.</dl>
<p> In addition, the usual GTK+ and MATE command line options apply. See the output of &#8211;help for details. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-mate-options/">mate-options</a>(7), <a href="/docs/linux/man/7-gtk-options/">gtk-options</a>(7)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Marillat &lt;marillat [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<p> Updated by Theppitak Karoonboonyanan &lt;thep [at] linux.thai.net&gt;, Tom Feiner &lt;feiner.tom [at] gmail.com&gt; and Cosimo Cecchi &lt;cosimoc [at] gnome.org&gt; </p>
<h2>Index</h2>
