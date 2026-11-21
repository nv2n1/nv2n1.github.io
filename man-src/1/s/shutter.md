---
title: "shutter(1)"
name: "shutter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shutter/"
description: "Shutter – Feature-rich Screenshot Tool"
---

<h2>SYNOPSIS</h2>
<p> shutter [options]</p>
<h2>COPYRIGHT</h2>
<p> Shutter is Copyright (C) by Mario Kemper and Shutter Team</p>
<h2>DESCRIPTION</h2>
<p> <code>Shutter</code> is a feature-rich screenshot program. You can take a screenshot of a specific area, window, your whole screen, or even of a website &#8211; apply different effects to it, draw on it to highlight points, and then upload to an image hosting site, all within one window.</p>
<h2>OPTIONS</h2>
<dl>
<dt>Example 1</dt>
<dd> shutter -a -p=myprofile &#8211;min_at_startup</dd>
<dt>Example 2</dt>
<dd> shutter -s=100,100,300,300 -e</dd>
<dt>Example 3</dt>
<dd> shutter &#8211;window=.*firefox.*</dd>
<dt>Example 4</dt>
<dd> shutter &#8211;web=<a rel="nofollow" href="http://shutter-project.org/">http://shutter-project.org/</a> -e</dd></dl>
<h3><font SIZE="-1">CAPTURE</font> <font SIZE="-1">MODE</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>-s, &#8211;select=[X,Y,WIDTH,HEIGHT]</code></dt>
<dd> Capture an area of the screen. Providing X,Y,WIDTH,HEIGHT is optional.</dd>
<dt><code>-f, &#8211;full</code></dt>
<dd> Capture the entire screen.</dd>
<dt><code>-w, &#8211;window=[</code><font SIZE="-1"><code>NAME_PATTERN</code></font><code>]</code></dt>
<dd> Select a window to capture. Providing a <font SIZE="-1">NAME_PATTERN</font> (Perl-style regex) ist optional.</dd>
<dt><code>-a, &#8211;active</code></dt>
<dd> Capture the current active window.</dd>
<dt><code>&#8211;section</code></dt>
<dd> Capture a section. You will be able to select any child window by moving the mouse over it.</dd>
<dt><code>-m, &#8211;menu</code></dt>
<dd> Capture a menu.</dd>
<dt><code>-t, &#8211;tooltip</code></dt>
<dd> Capture a tooltip.</dd>
<dt><code>&#8211;web=[</code><font SIZE="-1"><code>URL</code></font><code>]</code></dt>
<dd> Capture a webpage. Providing an <font SIZE="-1">URL</font> ist optional.</dd>
<dt><code>-r, &#8211;redo</code></dt>
<dd> Redo last screenshot.</dd></dl>
<h3><font SIZE="-1">SETTINGS</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>-p, &#8211;profile=NAME</code></dt>
<dd> Load a specific profile on startup.</dd>
<dt><code>-o, &#8211;output=FILENAME</code></dt>
<dd> Specify a filename to save the screenshot to (overwrites any profile-related setting). </dd>
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
<dt><code>-d, &#8211;delay=SECONDS</code></dt>
<dd> Wait n seconds before taking a screenshot.</dd>
<dt><code>-c, &#8211;include_cursor</code></dt>
<dd> Include cursor when taking a screenshot.</dd>
<dt><code>-C, &#8211;remove_cursor</code></dt>
<dd> Remove cursor when taking a screenshot.</dd></dl>
<h3><font SIZE="-1">APPLICATION</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Prints a brief help message and exits.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Prints version information.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Prints a lot of debugging information to <font SIZE="-1">STDOUT</font>.</dd>
<dt><code>&#8211;clear_cache</code></dt>
<dd> Clears cache, e.g. installed plugins, at startup.</dd>
<dt><code>&#8211;min_at_startup</code></dt>
<dd> Starts Shutter minimized to tray.</dd>
<dt><code>&#8211;disable_systray</code></dt>
<dd> Disables systray icon.</dd>
<dt><code>-e, &#8211;exit_after_capture</code></dt>
<dd> Exit after the first capture has been made. This is useful when using Shutter in scripts.</dd>
<dt><code>-n, &#8211;no_session</code></dt>
<dd> Do not add the screenshot to the session. This is useful when using Shutter in scripts.</dd></dl>
<h2>BUG REPORTS</h2>
<p> If you find a bug in Shutter, you should report it. But first, you should make sure that it really is a bug, and that it appears in the latest version of Shutter. </p>
<p> The latest version is always available from: <code><a rel="nofollow" href="https://launchpad.net/shutter">https://launchpad.net/shutter</a></code> </p>
<p> Once you have determined that a bug actually exists, please report it at launchpad: <code><a rel="nofollow" href="https://bugs.launchpad.net/shutter/+filebug">https://bugs.launchpad.net/shutter/+filebug</a></code> </p>
