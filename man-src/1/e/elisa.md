---
title: "elisa(1)"
name: "elisa"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elisa/"
description: "elisa – media center solution"
---

<h2>NAME</h2>
<p> elisa &#8211; media center solution</p>
<h2>SYNOPSIS</h2>
<p> <code>elisa</code> [<i>option&#8230;</i>]<i> </i>[<i>config_file</i>]<br />
 <code>elisa</code> [<i>option&#8230;</i>]<i> </i>-i<i> </i>import_file.py</p>
<h2>DESCRIPTION</h2>
<p> <code>elisa</code> is a open source media center solution. Elisa runs on the top of the GStreamer multimedia framework and uses the pigment lib for graphical user interaction. It is meant to be the all-in-one multimedia solution for your managing and playing your videos, audios and watch slide shows of your photos. It also automatically detects samba-shares, UPnP-devices and DAAP shares sharing media and makes them accessible from inside elisa. You can use it with your mouse, lirc-input device or simply with the keyboard.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v,&#8211;version</code></p>
<dd> Print the version of elisa</p>
<dt><code>&#8211;twisted-version</code></p>
<dd> Print the version of twisted</p>
<dt><code>-t, &#8211;tracebacks</code></p>
<dd> Output tracebacks on the console output. Disabled by default.</p>
<dt><code>-l, &#8211;log</code></p>
<dd> Log the output to the given file</p>
<dt><code>-i, &#8211;import FILE</code></p>
<dd> Import the given python file and run it in the elisa environment </p>
</dl>
<h2>KEYBOARD CONTROL</h2>
<p> To navigate through the menus, elisa reacts on key presses:</p>
<dl>
<dt><code>Basic keys</code></p>
<dd> <code>q or ESC</code><br />
&nbsp;<wbr>Exit from Elisa<br />
 <code>f</code><br />
&nbsp;<wbr>Toggle fullscreen<br />
 <code>Space</code><br />
&nbsp;<wbr>Toggle menu/player<br />
 <code>Enter</code><br />
&nbsp;<wbr>Activate Action on the selected Item </p>
<dt><code>Menu hidden and player active</code></p>
<dd> <code>Left or v</code><br />
&nbsp;<wbr>Seek backward<br />
 <code>Right or b</code><br />
&nbsp;<wbr>Seek forward<br />
 <code>Up/Down</code><br />
&nbsp;<wbr>Volume up/down<br />
 <code>Enter</code><br />
&nbsp;<wbr>Toggle play/pause<br />
 <code>x</code><br />
&nbsp;<wbr>Previous track of playlist<br />
 <code>c</code><br />
&nbsp;<wbr>Next track of playlist<br />
 <code>Space</code><br />
&nbsp;<wbr>Show the menu </p>
<dt><code>List menu mode</code></p>
<dd> <code>Up/Down</code><br />
&nbsp;<wbr>Navigate in the current menu level<br />
 <code>Right</code><br />
&nbsp;<wbr>Go to the top context bar<br />
 <code>Backspace</code><br />
&nbsp;<wbr>Go to previous menu<br />
 <code>Enter</code><br />
&nbsp;<wbr>Play media if it&#8217;s a media or navigate in the selected directory </p>
<dt><code>Grid menu mode</code></p>
<dd> The user can navigate in the 4 directions (up, down, left, right) using the direction keys. When the first row of the grid is reached, the user can enter the top context bar by hitting &quot;Up&quot; key once more. When the last row of the grid is reached, the user can enter the grid context bar by hitting &quot;Down&quot; key once more. </p>
<p> Navigation inside the grid context bar is horizontal, use Left/Right keys to navigate in the 3 buttons. To activate a button, press Enter. To leave the context bar, press Up key.</p>
<dt><code>Cover flow menu mode</code></p>
<dd>
 <code>Left/Right</code><br />
&nbsp;<wbr>Navigate in the current menu level<br />
 <code>Up</code><br />
&nbsp;<wbr>Go to the top context bar<br />
 <code>Backspace</code><br />
&nbsp;<wbr>Go to previous menu<br />
 <code>Enter</code><br />
&nbsp;<wbr>Play media if it&#8217;s a media or navigate in the selected directory </p>
<dt><code>Top context bar</code></p>
<dd> When navigating inside menus, there should always be a context bar available on the top of the window. Navigation inside this bar is horizontal, use Left/Right keys to navigate in the bar buttons. To activate a button, press Enter. To leave the context bar, press Down key. </p>
</dl>
<h2>AUTHORS</h2>
<p> <code>elisa</code> was written by the Elisa team &lt;contact [at] fluendo.com&gt; This manual page was previously written Philippe Normand and got reworked by Benjamin Kampmann</p>
<h2>DISTRIBUTION</h2>
<p> The latest version of Elisa may be downloaded from &lt;<a rel="nofollow" href="http://www.elisa.fluendo.com/">http://www.elisa.fluendo.com/</a>&gt; </p>
<h2>Index</h2>
