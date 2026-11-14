---
title: "me-tv(1)"
name: "me-tv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-me-tv/"
description: "me-tv – a digital television (DVB) viewer for GNOME"
---

<h2 class="name">NAME</h2>
<p> me-tv &#8211; a digital television (DVB) viewer for GNOME</p>
<h2>SYNOPSIS</h2>
<p> <code>me-tv</code> <i>[-?|&#8211;help]</i> <i>[-v|&#8211;verbose]</i> <i>[-s|&#8211;safe-mode]</i> <i>[-m|&#8211;minimised]</i> <i>[&#8211;disable-epg]</i> <i>[&#8211;disable-epg-thread]</i> <i>[&#8211;no-screensaver-inhibit]</i> <i>[&#8211;devices]</i> <i>[&#8211;read-timeout]</i> <i>[&#8211;display=DISPLAY]</i> </p>
<h2>DESCRIPTION</h2>
<p> Me TV is a GTK desktop application for watching digital television services that use the DVB standard. Me TV works with DVB-T/C/S and ATSC cards that have kernel driver support. </p>
<p> Me TV uses the xine video player to render its output onto its video window. Me TV reads the Electronic Program Guide (EPG) data that is transmitted over the air to populate a built-in program guide which can be used for scheduling recordings. </p>
<p> Me TV has a built-in scanner which can autoscan certain countries or use an initial scan file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?|&#8211;help</code></p>
<dd> Show help options.</p>
<dt><code>-v|&#8211;verbose</code></p>
<dd> Show verbose output.</p>
<dt><code>-s|&#8211;safe-mode</code></p>
<dd> Show the preferences dialog an don&#8217;t show video upon start.</p>
<dt><code>-m|&#8211;minimised-mode</code></p>
<dd> Show minimised in notification area at startup.</p>
<dt><code>&#8211;disable-epg</code></p>
<dd> Stops the rendering of the EPG event buttons on the UI.</p>
<dt><code>&#8211;disable-epg-thread</code></p>
<dd> Disable the EPG thread. Me TV will stop collecting EPG events.</p>
<dt><code>&#8211;no-screensaver-inhibit</code></p>
<dd> Tells Me TV not to call the screensaver Inhibit/UnInhibit methods for GNOME Screensaver.</p>
<dt><code>&#8211;devices</code></p>
<dd> Only use the specified frontend devices. You can specify more than one device by using a comma or colon separator. (e.g. &#8211;devices=/dev/dvb/adapter0/frontend1)</p>
<dt><code>&#8211;read-timeout</code></p>
<dd> How long to wait (in seconds) before timing out while waiting for data from demuxer (default 5)</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> X display to use </p>
</dl>
<h2>AUTHOR</h2>
<p> Michael Lamothe (2007-2010) &lt;michael.lamothe [at] gmail.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 Michael Lamothe &lt;michael.lamothe [at] gmail.com&gt;. </p>
<h2>Index</h2>
