---
title: "v4lctl(1)"
name: "v4lctl"
section: "1"
letter: "v"
url: "/docs/linux/man/1-v4lctl/"
description: "xawtv-remote, v4lctl — control video4linux devices"
---

<h2>NAME</h2>
<p> xawtv-remote, v4lctl &#8212; control video4linux devices</p>
<h2>SYNOPSIS</h2>
<p> <code>xawtv-remote [ options ] command</code><br />
 <code>v4lctl [ options ] command</code></p>
<h2>DESCRIPTION</h2>
<p> <code>xawtv-remote</code> and <code>v4lctl</code> can be used to control a video4linux driven TV card. <code>xawtv-remote</code> passes the command to a already running xawtv or motv instance using X11 properties. <code>v4lctl</code> sets the parameters directly.</p>
<h2>OPTIONS</h2>
<p> <code>xawtv-remote</code> knows the following options:</p>
<dl>
<dt><code>-h</code></p>
<dd> print a short help text</p>
<dt><code>-d dpy</code></p>
<dd> Set the X11 display</p>
<dt><code>-i id</code></p>
<dd> Set the Window ID.</dl>
<p> <code>v4lctl</code> understands these options:</p>
<dl>
<dt><code>-h</code></p>
<dd> print a short help text</p>
<dt><code>-c device</code></p>
<dd> Set video4linux device.</p>
<dt><code>-D driver</code></p>
<dd> Set video4linux driver.</p>
<dt><code>-v n</code></p>
<dd> Set debug level to <code>n</code>, where n = [0..2]</dl>
<h2>COMMANDS</h2>
<p> Both tools basically use the same set of commands. Some of them are useful for xawtv-remote only (fullscreen for example).</p>
<dl>
<dt><code>setstation [ &lt;name&gt; | &lt;nr&gt; | next | prev | back ]</code></p>
<dd> Set the TV station. This selects on of the TV stations which are configured in the .xawtv config file. The argument can be the station name or a number (the first one listed in the config file is 0, &#8230;). next/prev jumps to the next/previous station in the list, back to the previously selected one.</p>
<dt><code>setchannel [ &lt;name&gt; | next | prev ]</code></p>
<dd> Tune in some channel.</p>
<dt><code>setfreqtab &lt;table&gt;</code></p>
<dd> Set the frequency table. See the menu in xawtv for a list of valid choices.</p>
<dt><code>setnorm &lt;norm&gt;</code></p>
<dd> Set the TV norm (NTSC/PAL/SECAM).</p>
<dt><code>setinput [ &lt;input&gt; | next ]</code></p>
<dd> Set the video input (Television/Composite1/&#8230;)</p>
<dt><code>capture [ on | off | overlay | grabdisplay ]</code></p>
<dd> Set capture mode.</p>
<dt><code>volume mute on | off</code></p>
<dd> mute / unmute audio.</p>
<dt><code>volume &lt;arg&gt;</code></p>
<dd>
<dt><code>color &lt;arg&gt;</code></p>
<dd>
<dt><code>hue &lt;arg&gt;</code></p>
<dd>
<dt><code>bright &lt;arg&gt;</code></p>
<dd>
<dt><code>contrast &lt;arg&gt;</code></p>
<dd> Set the parameter to the specified value. &lt;arg&gt; can be one of the following: A percent value (&quot;70%&quot; for example). Some absolute value (&quot;32768&quot;), the valid range is hardware specific. Relative values can be specified too by prefixing with &quot;+=&quot; or &quot;-=&quot; (&quot;+=10%&quot; or &quot;-=2000&quot;). The keywords &quot;inc&quot; and &quot;dec&quot; are accepted to and will increase and decrease the given value in small steps.</p>
<dt><code>setattr &lt;name&gt; &lt;value&gt;</code></p>
<dd> Set set the value of some attribute (color, contrast, &#8230; can be set this way too).</p>
<dt><code>show [ &lt;name&gt; ]</code></p>
<dd> Show the value current of some attribute.</p>
<dt><code>list</code></p>
<dd> List all available attributes with all properties (default value, range, &#8230;)</p>
<dt><code>snap [ jpeg | ppm ] [ full | win | widthxheight ] &lt;filename&gt;</code></p>
<dd> Capture one image.</p>
<dt><code>webcam &lt;filename&gt;</code></p>
<dd> Capture one image. Does basically the same as &quot;snap jpeg win &lt;filename&gt;&quot;. Works also while avi recording is active. It writes to a temporary file and renames it when done, so there is never a invalid file.</p>
<dt><code>movie driver [ files | raw | avi | qt ]</code></p>
<dd>
<dt><code>movie video [ ppm | pgm | jpeg | rgb | gray | 422 | 422p | rgb15 | rgb24 | mjpeg | jpeg | raw | mjpa | png ]</code></p>
<dd>
<dt><code>movie fps &lt;frames per second&gt;</code></p>
<dd>
<dt><code>movie audio [ mono8 | mono16 | stereo ]</code></p>
<dd>
<dt><code>movie rate &lt;sample rate&gt;</code></p>
<dd>
<dt><code>movie fvideo &lt;filename&gt;</code></p>
<dd>
<dt><code>movie faudio &lt;filename&gt;</code></p>
<dd>
<dt><code>movie start</code></p>
<dd>
<dt><code>movie stop</code></p>
<dd> control xawtv&#8217;s movie recorder.</p>
<dt><code>fullscreen</code></p>
<dd> Toggle fullscreen mode.</p>
<dt><code>showtime</code></p>
<dd> Display time (same what the &#8216;D&#8217; key does in xawtv).</p>
<dt><code>msg text</code></p>
<dd> Display text on the on-screen display (window title / upper left corner in fullscreen mode).</p>
<dt><code>vtx line1 line2 [ &#8230; ]</code></p>
<dd> Display subtitles. It pops up a small window at the bottom of the screen. It is intended to be used as an interface for displaying subtitles (often on videotext page 150 in Europe, that&#8217;s why the name) by external programs.<br />
 Every command line argument is one line, zero lines removes the window. You can colorize the text with the control sequence &quot;ESC foreground background&quot;. foreground/background has the range 0-7 (ansi term colors). Example: &quot;�7 hello world &quot; is blue on white. &quot;&quot; must be a real escape character, the string doesn&#8217;t work. With the bash you&#8217;ll get it with ^V ESC. vtx does also understand the ANSI tty escape sequences for color.</p>
<dt><code>quit</code></p>
<dd> quit xawtv</p>
<dt><code>keypad n</code></p>
<dd> enter digit &#8216;n&#8217;. That&#8217;s the two-digit channel selection, entering two digits within 5 seconds switches to the selected station. Useful for lirc.</p>
<dt><code>vdr command</code></p>
<dd> send &quot;command&quot; to vdr (via connect on localhost:2001).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-motv/">motv</a>(1), <a href="/docs/linux/man/5-xawtvrc/">xawtvrc</a>(5)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2001 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
