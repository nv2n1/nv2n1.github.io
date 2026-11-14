---
title: "fbtv(1)"
name: "fbtv"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbtv/"
description: "fbtv – a console program for watching TV"
---

<h2>NAME</h2>
<p> fbtv &#8211; a console program for watching TV</p>
<h2>SYNOPSIS</h2>
<p> <code>fbtv [ options ] [ station name ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>fbtv</code> is a program for watching TV with your linux box. It runs on top of a graphic framebuffer device (/dev/fb0). You&#8217;ll need a new 2.1.x kernel to play with this. <code>fbtv</code> shares the config file ($HOME/.xawtv) with the <code>xawtv</code> application. Check the <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1) manpage for details about the config file format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o base</code></p>
<dd> set basestring for the snapshot output files. The filename will be &quot;base-timestamp-nr.ext&quot;.</p>
<dt><code>-v</code></p>
<dd> Be verbose.</p>
<dt><code>-c device</code></p>
<dd> video4linux device (default is /dev/video0).</p>
<dt><code>-D driver</code></p>
<dd> video4linux driver (default is &quot;libv4l&quot;).</p>
<dt><code>-d device</code></p>
<dd> framebuffer device (default is $FRAMEBUFFER; /dev/fb0 if unset)</p>
<dt><code>-g</code></p>
<dd> grayscaled display (works for 256 color mode only)</p>
<dt><code>-s widthxheight</code></p>
<dd> display the TV picture in <code>width</code> x <code>height</code> size in the upper right corner.</p>
<dt><code>-f font</code></p>
<dd> font for text. Default is to look for lat1-16.psf in /usr/lib/kbd/consolefonts and /usr/share/consolefonts. If you have a local X11 font server running (or the FONTSERVER environment variable set to some working server), you can also give X11 font specs here.</p>
<dt><code>-m mode</code></p>
<dd> video mode for TV. fbtv will look up the mode in /etc/fb.modes.</p>
<dt><code>-j joydev</code></p>
<dd> joystick device to use for controlling fbtv.</p>
<dt><code>-k</code></p>
<dd> keep capture on when switching consoles. Might be useful together with -s switch, you have a video picture while working on another console. This is more or less a dirty hack. Works only if all your consoles have the same video mode and fbcon does not use panning to speed up scrolling. For a multiheaded setup this is useful too.</p>
<dt><code>-q</code></p>
<dd> quiet mode. Doesn&#8217;t reserve space for the status line at the top, doesn&#8217;t display the status messages and clock. You can toggle this at runtime too (&#8216;F&#8217;).</p>
<dt><code>-M</code></p>
<dd> EXPERIMENTAL: Turn on backend scaler mode (write yuv to offscreen memory and let the gfx board scale up the video). Supported hardware: Matrox G200/G400 (with matroxfb) and ATI Mach64 VT/GT (with atyfb, 16bpp only). You&#8217;ll need at least bttv-0.7.16 or kernel 2.3.50.</dl>
<h2>USAGE</h2>
<p> fbtv is supported to work much like xawtv from user&#8217;s point of view. You might have noticed that xawtv has a lot of keyboard shortcuts. They work in fbtv too (if it useful). Here is the list: </p>
<pre>
G            <code>G</code>rab picture (full size, ppm)
J            Grab picture (full size, <code>j</code>peg)
F            <code>F</code>ullscreen.  Toggle quiet mode (see above).
up/down      tune up/down one channel
left/right   fine tuning
pgup/pgdown  station up/down
ESC,Q        <code>Q</code>uit
X            <code>Q</code>uit, but leave sound on.
+/-          Volume up/down
Enter        mute
</pre>
<p> The channel hotkeys defined in $HOME/.xawtv are supported too, with one exception: modifier keys (something like &quot;key = Ctrl+F1&quot;) do not work. </p>
<h2>FULLSCREEN TV</h2>
<p> Some hints from Dag Bakke &lt;dag.bakke [at] riksnett.no&gt;: </p>
<p> The BT8xx cards can produce images up to 768&#215;576 pixels. In order to have fbtv make use of your entire monitor-size and get maximum image quality, you need to create a 768&#215;576 pixels framebufferconsole. This can be accomplished with the <a href="/docs/linux/man/1-fbset/">fbset</a>(1) utility, which is available at various locations. See: <a rel="nofollow" href="http://www.cs.kuleuven.ac.be/~geert/bin/">http://www.cs.kuleuven.ac.be/~geert/bin/</a> </p>
<p> Or, you can let fbtv handle the videomode changes with the -m switch. This requires that you have a small database with the various videomodes available. The file containing the videomodes is normally named /etc/fb.modes. For example, the following entry produces a 768x576x32bpp mode, with 75Hz refresh on a Matrox G200. </p>
<pre>
mode &quot;tv&quot;
    # D: 49.188 MHz, H: 46.580 kHz, V: 75.008 Hz
    geometry 768 576 768 576 32
    timings 20330 128 32 32 8 128 5
endmode
</pre>
<p> The command &quot;fbtv -q -mtv&quot; thus gives you crisp clear (well, as good as the received signal anyway) tv on your entire screen. Alias this command to &#8216;tv&#8217;, and you&#8217;re set. </p>
<p> <code>NB!</code> Please note that your monitor may or may not be able to handle such a &quot;custom&quot; resolution. And that misuse of the aforementioned fbset utility can toast your monitor. It is a lot easier to pull smoke out of electronic components, than to put it back in. </p>
<p> A database of the standard VESA-modes can be downloaded from: <a href="ftp://platan.vc.cvut.cz/pub/linux/matrox-latest/fb.modes.vesa60.gz">ftp://platan.vc.cvut.cz/pub/linux/matrox-latest/fb.modes.vesa60.gz</a> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] goldbach.in-berlin.de&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997,98 Gerd Knorr &lt;kraxel [at] goldbach.in-berlin.de&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
