---
title: "gtkpod(1)"
name: "gtkpod"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtkpod/"
description: "gtkpod – GTK2 based software for managing songs and playlists on an Apple iPod"
---

<h2 class="name">NAME</h2>
<p> gtkpod &#8211; GTK2 based software for managing songs and playlists on an Apple iPod </p>
<h2>SYNOPSIS</h2>
<p> <code>gtkpod</code> [<code>-h</code>] [<code>-m</code> <i>path</i>] [<code>-p</code> <i>filename</i>] [<code>&#8211;hash</code> <i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly describes the gtkpod command.</p>
<h2>OPTIONS</h2>
<p> <code>gtkpod</code> supports the following options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Displays the help message.</p>
<dt><code>-m</code>, <code>&#8211;mountpoint</code> <i>path</i></p>
<dd> Define the mountpoint of your iPod.</p>
<dt><code>-p</code> <i>filename</i></p>
<dd> Increment playcount for file <i>filename</i> by one.</p>
<dt><code>&#8211;hash</code> <i>filename</i></p>
<dd> Print gtkpod hash for file <i>filename</i>.</dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.gtkpod/prefs</i></p>
<dd> Per user configuration file. Should normally only updated through the program itself.</p>
<dt><i>/etc/gtkpod/prefs</i></p>
<dd> Global configuration file. Used if no configuration file exist for the user starting gtkpod.</p>
<dt><i>~/.gtkpod/gtkpod.in</i></p>
<dd> If this file exists, gtkpod will try to execute it at startup This is done before attempting to mount the iPod directory (optional) or read the iTunesDB (optional).</p>
<dt><i>~/.gtkpod/gtkpod.out</i></p>
<dd> If this file exists, gtkpod will try to execute it while exiting the program. This is done after attempting to unmount the iPod directory (optional) and sending the &#8220;eject&#8221; command to the iPod (optional).</p>
<dt><i>/etc/gtkpod/gtkpod.in</i>, <i>/etc/gtkpod/gtkpod.out</i></p>
<dd> Used instead of the per user scripts if the former ones don&#8217;t exist and these do.</p>
<dt><i>~/.gtkpod/gtkpod.load</i></p>
<dd> If this file exists, gtkpod will execute it before loading the contents of an iPod with the iPod&#8217;s mountpoint as the only command line argument. Put any commands needed to access the iPod here, for example if you need to mount the iPod manually.</p>
<dt><i>~/.gtkpod/gtkpod.eject</i></p>
<dd> If this file exists, gtkpod will execute it when ejecting an iPod with the the iPod&#8217;s mountpoint as the only command line argument. Put any commands you want to execute after gtkpod has written the changes to the iPod here. For example: </p>
<p> sudo eject <tt>$1</tt> </p>
<p> gtkpod will not attempt to do any magic of it&#8217;s own to mount/unmount/eject the iPod.</dl>
<h2>AUTHOR</h2>
<pre>
 Jorg Schuler &lt;jcsjcs at users.sourceforge.net&gt;
 Corey Donohoe &lt;atmos at atmos.org&gt;
 Adrian Ulrich &lt;pab at blinkenlights.ch&gt;
 and others
</pre>
<p> This manpage was written by Frank Lichtenheld.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<h2>Index</h2>
