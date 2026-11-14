---
title: "xawtv(1)"
name: "xawtv"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xawtv/"
description: "xawtv – a X11 program for watching TV"
---

<h2>NAME</h2>
<p> xawtv &#8211; a X11 program for watching TV</p>
<h2>SYNOPSIS</h2>
<p> <code>xawtv [ options ] [ station name ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>xawtv</code> is a X11 application for watching TV with your unix box. It uses the Athena widgets.</p>
<h2>OPTIONS</h2>
<p> All command line options also have a Resource, so you can put them into your .Xdefaults file too.</p>
<dl>
<dt><code>-h</code>, <code>-help</code></p>
<dd> Print a short description of all command line options.</p>
<dt><code>-hwscan</code></p>
<dd> Print a list of available devices.</p>
<dt><code>-f</code>, <code>-fullscreen</code></p>
<dd> startup in fullscreen mode.<br />
 Resource: xawtv.fullscreen (bool).</p>
<dt><code>-n</code>, <code>-noconf</code></p>
<dd> don&#8217;t read the config file ($HOME/.xawtv).<br />
 Resource: xawtv.readconfig (bool).</p>
<dt><code>-o</code>, <code>-outfile</code> base</p>
<dd> set basestring for the snapshot output files. The filename will be &quot;base-timestamp-nr.ext&quot;.<br />
 Resource: xawtv.basename (string).</p>
<dt><code>-c</code>, <code>-device</code> device</p>
<dd> set video4linux device (default is /dev/video0). This option also disables Xvideo support.<br />
 Resource: xawtv.device (string).</p>
<dt><code>-D</code>, <code>-driver</code> name</p>
<dd> set video4linux driver (default is &quot;libv4l&quot;). This option also disables Xvideo support.<br />
 Resource: xawtv.driver (string).</p>
<dt><code>-C</code>, <code>-dspdev</code> device</p>
<dd> set audio device (default is /dev/dsp).<br />
 Resource: xawtv.dspdev (string).</p>
<dt><code>-vbidev</code> device</p>
<dd> set vbi device (default is /dev/vbi0).<br />
 Resource: xawtv.vbidev (string).</p>
<dt><code>-c</code>, <code>-xvport</code> number</p>
<dd> set Xvideo port (defaults to the first usable if Xvideo is available). This option also enables Xvideo support.<br />
 Resource: xawtv.xvport (int).</p>
<dt><code>-joydev</code> device</p>
<dd> joystick device to use for controlling xawtv.<br />
 Resource: xawtv.joydev (string).</p>
<dt><code>-v</code>, <code>-debug</code> level</p>
<dd> Be verbose, <code>level</code> may be 0 (default), 1 or 2. It exists just for debugging and trouble-shooting.<br />
 Resource: xawtv.debug (int).</p>
<dt><code>-remote</code></p>
<dd> X11 display is remote. This basically disables overlay mode, you might need this if xawtv fails to autodetect a remote X11 display.<br />
 Resource: xawtv.remote (bool).</p>
<dt><code>-b</code>, <code>-bpp</code> n</p>
<dd> force xawtv into <code>n</code> bpp color depth. Works for switching between 15/16 and 24/32 bpp. This gets just passed through to <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8).<br />
 Resource: xawtv.bpp (int).</p>
<dt><code>-shift</code> n</p>
<dd> Shift the video display by <code>n</code> bytes. Try this if your video display isn&#8217;t within the xawtv window, some older matrox cards show this problem. This gets passed through to <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8) too.<br />
 Resource: xawtv.shift (int).</p>
<dt><code>-fb</code></p>
<dd> Use the framebuffer device to determine the video framebuffer address (instead of the DGA extension). Yet another pass through argument.<br />
 Resource: xawtv.fbdev (bool).</p>
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
 Resource: xawtv.vidmode (bool).</p>
<dt><code>-dga/-nodga</code></p>
<dd> enable/disable the usage of the DGA extension, default is on.<br />
 Resource: xawtv.dga (bool).</p>
<dt><code>-parallel</code> n</p>
<dd> use n compression threads (default: one).<br />
 Resource: xawtv.parallel (int).</dl>
<p> The usual toolkit options like <code>-geometry</code> are supported too.</p>
<h2>SUPPORTED HARDWARE / INTERFACES</h2>
<dl>
<dt><code>v4l2</code></p>
<dd> video4linux two &#8211; modern standard linux video capture API</p>
<dt><code>libv4l</code></p>
<dd> work through the libv4l library, which provides an additional thin layer on top of video4linux2 devices for support of more wide range of devices&#8217; pixel formats (often required for webcams etc.) It is default for Xawtv on Linux systems.</p>
<dt><code>bktr</code></p>
<dd> FreeBSD / OpenBSD driver for bt848/878 grabber cards.</p>
<dt><code>Xvideo</code></p>
<dd> X11 Extension for video devices. Note that the Xvideo extension does support overlay only, you can&#8217;t capture images/movies if the Xvideo extension is used. On the other hand this is the only way to scaled video overlay (i.e. fullscreen without black borders @ 1024&#215;748) if both hardware and xfree86 driver support it. See README.xfree4 for more details and hints on how to setup Xvideo.</dl>
<h2>GETTING STARTED</h2>
<p> Just start xawtv. Then verify the settings in the options menu (right mouse button) and adjust the settings (TV norm, Video source, frequency table). With the cursor keys you can control the tuner and look for TV Stations. Other useful hotkeys are listed below. </p>
<p> The hotkey &#8216;E&#8217; will show the channel editor where you can create/edit entries your TV stations. Don&#8217;t forget to click on &quot;save&quot; to write a config file. You can also create/edit a config file with any text editor, see <a href="/docs/linux/man/5-xawtvrc/">xawtvrc</a>(5) for a description of the config file syntax. There are a number of config options which can only be set by editing the config file. </p>
<p> You can also check out scantv. That&#8217;s a command line tool which will perform a channel scan and write out a xawtv config file with all channels it has found.</p>
<h3>Mouse functions</h3>
<p> The left mouse button will popup a menu with all TV stations found in the config file. The middle button switches to the next station. The right button brings up a window with a lot of options and control functions.</p>
<h3>Keyboard Shortcuts</h3>
<pre>
V            <i>V</i>ideo (Capture) on/off
A            <i>A</i>udio on/off
F            <i>F</i>ullscreen on/off
G            <i>G</i>rab picture (full size, ppm)
J            Grab picture (full size, <i>j</i>peg)
Ctrl+G       <i>G</i>rab picture (window size, ppm)
Ctrl+J       Grab picture (window size, <i>j</i>peg)
O            Popup <i>O</i>ptions Window
C            Popup <i>C</i>hannels Window
E            Popup Channel <i>E</i>ditor
R            Popup AVI <i>R</i>ecording Window
Z            Channel Hopper (<i>z</i>apping, tune in every
             station a few seconds)
Ctrl+Z       Fast Channel Hopping (grab the images for the
             Channel Buttons)
up/down      tune up/down one channel
left/right   fine tuning
pgup/pgdown  station up/down (the ones you have in the config file)
space        next station (same as pgup)
backspace    previously tuned station
Ctrl+up      scan for next station
F5-F12       adjust bright/hue/contrast/color
ESC,Q        <i>Q</i>uit
+/-          Volume up/down (keypad)
Enter        mute (keypad)
</pre>
<h2>BUGS</h2>
<p> <code>Bug reports with images attached go to /dev/null unseen.</code> </p>
<p> xawtv depends on a correct driver configuration. If you can&#8217;t tune TV stations even if the settings in the options window are correct it is very likely a driver issue. </p>
<p> The mono/stereo display is <code>not</code> reliable due to v4l API restrictions. The API can not report back the current audio mode, but a list of the currently available modes. xawtv just does a guess based on that, assuming the driver uses the best available mode. Depending on your hardware this might not be true. If in doubt whenever stereo <code>really</code> works, please tune in MTV and listen, don&#8217;t trust what xawtv says.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xawtvrc/">xawtvrc</a>(5), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1), <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8), <a href="/docs/linux/man/1-scantv/">scantv</a>(1)<br />
 <a rel="nofollow" href="http://bytesex.org/xawtv/">http://bytesex.org/xawtv/</a> (homepage)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2001 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>MISC</h2>
<p> You are the 4711th visitor of this page. </p>
<h2>Index</h2>
