---
title: "radio(1)"
name: "radio"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radio/"
description: "radio – console radio application"
---

<h2>NAME</h2>
<p> radio &#8211; console radio application</p>
<h2>SYNOPSIS</h2>
<p> <code>radio [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>radio</code> is a interactive, ncurses-bases console radio application.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print a short help text.</p>
<dt><code>-d</code></p>
<dd> enable debug output.</p>
<dt><code>-q</code></p>
<dd> quit after processing the cmd line options, don&#8217;t enter interactive ncurses mode. Only useful together with other options for obvious reasons &#8230;</p>
<dt><code>-m</code></p>
<dd> mute radio.</p>
<dt><code>-f freq</code></p>
<dd> tune the specified radio frequency (and unmute the radio).</p>
<dt><code>-c dev</code></p>
<dd> specify radio device (default is /dev/radio0).</p>
<dt><code>-s</code></p>
<dd> Do a scan for radio stations.</p>
<dt><code>-S</code></p>
<dd> Same as above + write a radio.fmmap with the signal for every frequency. You can get a graph for it with gnuplot (plot &quot;radio.fmmap&quot; w lin).</p>
<dt><code>-i</code></p>
<dd> Scan, write a initial ~/.radio file to stdout and quit. So you can create a config file where you only have to fill in the correct station names later this way: &quot;radio -i &gt; ~/.radio&quot;. See below for the config file syntax.</dl>
<h2>CONFIGURATION</h2>
<p> <code>radio</code> picks up station names and present stations from a config file. It can parse kradio (KDE radio app) config files, therefore it first tries the usual KDE config file location: <code>~/.kde/share/config/kradiorc</code>. Failing that, <code>radio</code> tries <code>~/.radio</code> (which makes things a bit easier for people who don&#8217;t use kradio). </p>
<p> The format looks like this: </p>
<pre><code>
#KDE Config File
[Buttons] 1 = 95800000 2 = 91400000
    [Stations] 100600000 = Hundert,
          6 95800000 = Radio eins 102600000 = Fritz 94300000 = r.s .2 91400000 = Berliner Rundfunk
</code></pre>
<p> The [Buttons] section can have up to eight entries. That are the present stations, they get mapped to F1-F8. The [Stations] section maps frequencies to station names. The frequencies in both sections are specified in Hz.</p>
<h2>KEYS</h2>
<pre>
X            exit
ESC,Q,E      mute and exit.
up/down      inc/dec frequency
pgup/pgdown  next/previous station.  This one uses the
             stations from the config file by default.
             When started with the -s option these keys
             will cycle througth the stations found during
             the scan.
F1-F8, 1-8   preset buttons.
Ctrl+L       redraw screen.
</pre>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2001 Gerd Knorr </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
