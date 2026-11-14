---
title: "shutter(1)"
name: "shutter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shutter/"
description: "Shutter – Feature-rich Screenshot Tool"
---

<h2 class="name">NAME</h2>
<p> Shutter &#8211; Feature-rich Screenshot Tool </p>
<h2>SYNOPSIS</h2>
<p> shutter [options]</p>
<h2>COPYRIGHT</h2>
<p> Shutter is Copyright (C) by Mario Kemper and Shutter Team</p>
<h2>DESCRIPTION</h2>
<p> <code>Shutter</code> is a feature-rich screenshot program. You can take a screenshot of a specific area, window, your whole screen, or even of a website &#8211; apply different effects to it, draw on it to highlight points, and then upload to an image hosting site, all within one window.</p>
<h2>OPTIONS</h2>
<dl>
<dt>Example 1</p>
<dd> shutter -a -p=myprofile &#8211;min_at_startup</p>
<dt>Example 2</p>
<dd> shutter -s=100,100,300,300 -e</p>
<dt>Example 3</p>
<dd> shutter &#8211;window=.*firefox.*</p>
<dt>Example 4</p>
<dd> shutter &#8211;web=<a rel="nofollow" href="http://shutter-project.org/">http://shutter-project.org/</a> -e</dl>
<h3><font SIZE="-1">CAPTURE</font> <font SIZE="-1">MODE</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>-s, &#8211;select=[X,Y,WIDTH,HEIGHT]</code></p>
<dd> Capture an area of the screen. Providing X,Y,WIDTH,HEIGHT is optional.</p>
<dt><code>-f, &#8211;full</code></p>
<dd> Capture the entire screen.</p>
<dt><code>-w, &#8211;window=[</code><font SIZE="-1"><code>NAME_PATTERN</code></font><code>]</code></p>
<dd> Select a window to capture. Providing a <font SIZE="-1">NAME_PATTERN</font> (Perl-style regex) ist optional.</p>
<dt><code>-a, &#8211;active</code></p>
<dd> Capture the current active window.</p>
<dt><code>&#8211;section</code></p>
<dd> Capture a section. You will be able to select any child window by moving the mouse over it.</p>
<dt><code>-m, &#8211;menu</code></p>
<dd> Capture a menu.</p>
<dt><code>-t, &#8211;tooltip</code></p>
<dd> Capture a tooltip.</p>
<dt><code>&#8211;web=[</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> Capture a webpage. Providing an <font SIZE="-1">URL</font> ist optional.</p>
<dt><code>-r, &#8211;redo</code></p>
<dd> Redo last screenshot.</dl>
<h3><font SIZE="-1">SETTINGS</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>-p, &#8211;profile=NAME</code></p>
<dd> Load a specific profile on startup.</p>
<dt><code>-o, &#8211;output=FILENAME</code></p>
<dd> Specify a filename to save the screenshot to (overwrites any profile-related setting). </p>
<p> <code>Supported image formats:</code> You can save to any popular image format (e.g. jpeg, png, gif, bmp). Additionally it is possible to save to pdf, ps or svg. </p>
<p> <code>Please note:</code> There are several wildcards available, like </p>
<pre>
 %Y = year
 %m = month
 %d = day
 %T = time
 $w = width
 $h = height
 $name = multi-purpose (e.g. window title)
 $nb_name = like $name but without blanks in resulting strings
 $profile = name of current profile
 $R = random char (e.g. $RRRR = ag4r)
 %NN = counter
</pre>
<p> The string is interpretted by strftime. See <tt>&quot;man strftime&quot;</tt> for more examples. </p>
<p> <code>As an example:</code> shutter -f -e -o &#8216;./%y-%m-%d_$w_$h.png&#8217; would create a file named &#8217;11-10-28_1280_800.png&#8217; in the current directory.</p>
<dt><code>-d, &#8211;delay=SECONDS</code></p>
<dd> Wait n seconds before taking a screenshot.</p>
<dt><code>-c, &#8211;include_cursor</code></p>
<dd> Include cursor when taking a screenshot.</p>
<dt><code>-C, &#8211;remove_cursor</code></p>
<dd> Remove cursor when taking a screenshot.</dl>
<h3><font SIZE="-1">APPLICATION</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints a brief help message and exits.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Prints version information.</p>
<dt><code>&#8211;debug</code></p>
<dd> Prints a lot of debugging information to <font SIZE="-1">STDOUT</font>.</p>
<dt><code>&#8211;clear_cache</code></p>
<dd> Clears cache, e.g. installed plugins, at startup.</p>
<dt><code>&#8211;min_at_startup</code></p>
<dd> Starts Shutter minimized to tray.</p>
<dt><code>&#8211;disable_systray</code></p>
<dd> Disables systray icon.</p>
<dt><code>-e, &#8211;exit_after_capture</code></p>
<dd> Exit after the first capture has been made. This is useful when using Shutter in scripts.</p>
<dt><code>-n, &#8211;no_session</code></p>
<dd> Do not add the screenshot to the session. This is useful when using Shutter in scripts.</dl>
<h2>BUG REPORTS</h2>
<p> If you find a bug in Shutter, you should report it. But first, you should make sure that it really is a bug, and that it appears in the latest version of Shutter. </p>
<p> The latest version is always available from: <code><a rel="nofollow" href="https://launchpad.net/shutter">https://launchpad.net/shutter</a></code> </p>
<p> Once you have determined that a bug actually exists, please report it at launchpad: <code><a rel="nofollow" href="https://bugs.launchpad.net/shutter/+filebug">https://bugs.launchpad.net/shutter/+filebug</a></code> </p>
<h2>Index</h2>
<dt><a href="#lbAJ">BUG REPORTS</a></p>
<dd></dl>
