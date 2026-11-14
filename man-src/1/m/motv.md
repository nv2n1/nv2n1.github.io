---
title: "motv(1)"
name: "motv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-motv/"
description: "motv – a Motif program for watching TV"
---

<h2>NAME</h2>
<p> motv &#8211; a Motif program for watching TV</p>
<h2>SYNOPSIS</h2>
<p> <code>motv [ options ] [ station name ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>motv</code> is a Motif application for watching TV with your unix box. </p>
<p> It is basically xawtv with a more userfriendly GUI. It has the same features, uses the same config file, has the same command line switches, you can control it using xawtv-remote. Most keyboards shortcuts are identical too.</p>
<h2>OPTIONS</h2>
<p> All command line options also have a Resource, so you can put them into your .Xdefaults file too.</p>
<dl>
<dt><code>-h</code>, <code>-help</code></p>
<dd> Print a short description of all command line options.</p>
<dt><code>-hwscan</code></p>
<dd> Print a list of available devices.</p>
<dt><code>-f</code>, <code>-fullscreen</code></p>
<dd> startup in fullscreen mode.<br />
 Resource: motv.fullscreen (bool).</p>
<dt><code>-n</code>, <code>-noconf</code></p>
<dd> don&#8217;t read the config file ($HOME/.xawtv).<br />
 Resource: motv.readconfig (bool).</p>
<dt><code>-o</code>, <code>-outfile</code> base</p>
<dd> set basestring for the snapshot output files. The filename will be &quot;base-timestamp-nr.ext&quot;.<br />
 Resource: motv.basename (string).</p>
<dt><code>-c</code>, <code>-device</code> device</p>
<dd> set video4linux device (default is /dev/video0). This option also disables Xvideo support.<br />
 Resource: motv.device (string).</p>
<dt><code>-D</code>, <code>-driver</code> name</p>
<dd> set video4linux driver (default is &quot;libv4l&quot;). This option also disables Xvideo support.<br />
 Resource: motv.driver (string).</p>
<dt><code>-C</code>, <code>-dspdev</code> device</p>
<dd> set audio device (default is /dev/dsp).<br />
 Resource: motv.dspdev (string).</p>
<dt><code>-vbidev</code> device</p>
<dd> set vbi device (default is /dev/vbi0).<br />
 Resource: motv.vbidev (string).</p>
<dt><code>-c</code>, <code>-xvport</code> number</p>
<dd> set Xvideo port (defaults to the first usable if Xvideo is available). This option also enables Xvideo support.<br />
 Resource: motv.xvport (int).</p>
<dt><code>-joydev</code> device</p>
<dd> joystick device to use for controlling xawtv.<br />
 Resource: xawtv.joydev (string).</p>
<dt><code>-v</code>, <code>-debug</code> level</p>
<dd> Be verbose, <code>level</code> may be 0 (default), 1 or 2. It exists just for debugging and trouble-shooting.<br />
 Resource: motv.debug (int).</p>
<dt><code>-remote</code></p>
<dd> X11 display is remote. This basically disables overlay mode, you might need this if xawtv fails to autodetect a remote X11 display.<br />
 Resource: motv.remote (bool).</p>
<dt><code>-b</code>, <code>-bpp</code> n</p>
<dd> force xawtv into <code>n</code> bpp color depth. Works for switching between 15/16 and 24/32 bpp. This gets just passed through to <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8).<br />
 Resource: motv.bpp (int).</p>
<dt><code>-shift</code> n</p>
<dd> Shift the video display by <code>n</code> bytes. Try this if your video display is&#8217;nt within the xawtv window, some older matrox cards show this problem. This gets passed through to <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8) too.<br />
 Resource: motv.shift (int).</p>
<dt><code>-fb</code></p>
<dd> Use the framebuffer device to determine the video framebuffer address (instead of the DGA extension). Yet another pass through argument.<br />
 Resource: motv.fbdev (bool).</p>
<dt><code>-xv/-noxv </code></p>
<dd> enable/disable the usage of the Xvideo extension altogether, i.e. -noxv has the same effect as both -noxv-video and -noxv-image switches (see below).<br />
 Resource: xawtv.xv (bool).</p>
<dt><code>-xv-video/-noxv-video </code></p>
<dd> enable/disable the usage of the Xvideo extension for video overlay (i.e. XvPutVideo). overlay mode uses this. default is on.<br />
 Resource: xawtv.xvVideo (bool).</p>
<dt><code>-xv-image/-noxv-image </code></p>
<dd> enable/disable the usage of the Xvideo extension for image scaling (i.e. XvPutImage). grabdisplay mode uses this. default is on.<br />
 Resource: xawtv.xvImage (bool).</p>
<dt><code>-vm/-novm</code></p>
<dd> enable/disable the usage of the VidMode extension, default is off. If there is a fullscreen video mode configured in the config file, the vidmode extension will be enabled automatically.<br />
 Resource: motv.vidmode (bool).</p>
<dt><code>-dga/-nodga</code></p>
<dd> enable/disable the usage of the DGA extension, default is on.<br />
 Resource: motv.dga (bool).</p>
<dt><code>-parallel</code> n</p>
<dd> use n compression threads (default: one).<br />
 Resource: xawtv.parallel (int).</dl>
<p> The usual toolkit options like <code>-geometry</code> are supported too.</p>
<h2>SUPPORTED HARDWARE / INTERFACES</h2>
<dl>
<dt><code>v4l</code></p>
<dd> video4linux &#8211; <code>the</code> linux video capture API.</p>
<dt><code>v4l2</code></p>
<dd> video4linux two &#8211; new, improved capture interface which fixes a number of v4l design bugs.</p>
<dt><code>bktr</code></p>
<dd> FreeBSD / OpenBSD driver for bt848/878 grabber cards.</p>
<dt><code>Xvideo</code></p>
<dd> X11 Extension for video devices. Note that the Xvideo extension does support overlay only, you can&#8217;t capture images/movies if the Xvideo extension is used. On the other hand this is the only way to scaled video overlay (i.e. fullscreen without black borders @ 1024&#215;748) if both hardware and xfree86 driver support it. See README.xfree4 for more details and hints on how to setup Xvideo.</dl>
<h2>GETTING STARTED</h2>
<p> <code>motv</code> starts up with the TV window. The left mouse button shows a menu with all TV Stations (empty until you have defined some). The right mouse button brings up the control window. </p>
<p> The first time you have configure motv, i.e. set TV norm and frequency table to the correct values. Check if the hardware works correctly (if tuning does not work it is very likely a driver configuration issue). If the hardware operates fine, you can let motv look for TV stations (Options =&gt; Channel scan). The channel buttons have a context menu for deleting and editing. Don&#8217;t forget to save your configuration when you are done. </p>
<p> You can also create/edit a config file with any text editor, see <a href="/docs/linux/man/5-xawtvrc/">xawtvrc</a>(5) for a description of the config file syntax. There are a number of config options which can only be set by editing the config file.</p>
<h2>KEYBOARD SHORTCUTS</h2>
<p> Some of them work in the TV window only. The cursor keys for example are used by the motif toolkit to allow full keyboard control of the GUI and therefore have other functions in the control window. </p>
<pre>
V            <i>V</i>ideo (Capture) on/off
A            <i>A</i>udio on/off
F            <i>F</i>ullscreen on/off
G            <i>G</i>rab picture (full size, ppm)
J            Grab picture (full size, <i>j</i>peg)
Ctrl+G       <i>G</i>rab picture (window size, ppm)
Ctrl+J       Grab picture (window size, <i>j</i>peg)
Ctrl+C       Copy to clipboard.
C            Popup <i>C</i>ontrol Window
R            Popup AVI <i>R</i>ecording Window
S            Popup <i>S</i>cale controls
Z            Channel Hopper (<i>z</i>apping, tune in every
             station a few seconds)
Ctrl+Z       Fast Channel Hopping (grab the images for the
             Channel Bottons)
up/down      tune up/down one channel
left/right   fine tuning
pgup/pgdown  station up/down (the ones you have in the config file)
space        next station (same as pgup)
backspace    previously tuned station
Ctrl+up      scan for next station
ESC,Q        <i>Q</i>uit
+/-          Volume up/down (keypad)
Enter        mute (keypad)
</pre>
<h2>BUGS</h2>
<p> <code>Bug reports with images attached go to /dev/null unseen.</code> </p>
<p> motv depends on a correct driver configuration. If you can&#8217;t tune TV stations even if the settings in the options window are correct it is very likely a driver issue.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xawtvrc/">xawtvrc</a>(5), <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1), <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8), <a href="/docs/linux/man/1-mtt/">mtt</a>(1)<br />
 <a rel="nofollow" href="http://bytesex.org/xawtv/">http://bytesex.org/xawtv/</a> (homepage)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2001 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>MISC</h2>
<p> Huh? Still with me? Looks like some people <code>do</code> read manuals carefully. </p>
<h2>Index</h2>
