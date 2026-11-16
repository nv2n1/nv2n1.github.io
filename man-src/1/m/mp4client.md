---
title: "mp4client(1)"
name: "mp4client"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp4client/"
description: "MP4Client – GPAC MPEG-4 command-line Player"
---

<h2>NAME</h2>
<p> MP4Client &#8211; GPAC MPEG-4 command-line Player</p>
<h2>SYNOPSIS</h2>
<p> <code>MP4Client</code> [options]<i>&nbsp;<wbr>[file]</i> </p>
<h2>DESCRIPTION</h2>
<p> MP4Client is GPAC command-line player. It supports all GPAC playback features (2D and 3D support, local playback, RTP streaming, HTTP faststart, many audio and video codecs &#8230;). MP4Client also supports visual extraction to BMP, RAW or AVI (no compression, no audio).</p>
<h2>STARTUP OPTIONS</h2>
<dl>
<dt><code>-c file</code></dt>
<dd> specifies config file to use. Default config file is located in user home directory and created if not found.</dd>
<dt><code>-rti file</code></dt>
<dd> logs run-time information to file. Information logged is: FPS, CPU, Memory usage.</dd>
<dt><code>-quiet</code></dt>
<dd> removes script message, buffering and downloading status.</dd>
<dt><code>-strict-error</code></dt>
<dd> exits after the first error is reported.</dd>
<dt><code>-log-file FILE</code></dt>
<dd> specifies where to write logs. Default is stdout. Same as -lf.</dd>
<dt><code>-logs TOOLS</code></dt>
<dd> sets log tools and levels, formatted as a &#8216;:&#8217;-separated list of toolX[:toolZ]@level. By default all errors are logged. level can be one of quiet, error, warning, info or debug. tool can be:<br />
 core: libgpac core<br />
 coding: bitstream formats (audio, video, scene)<br />
 container: container formats (ISO File, MPEG-2 TS, AVI, &#8230;)<br />
 network: network data exept RTP trafic<br />
 rtp: rtp trafic<br />
 author: authoring tools (hint, import, export)<br />
 sync: terminal sync layer<br />
 codec: terminal codec messages<br />
 parser: scene parsers (svg, xmt, bt) and other<br />
 media: terminal media object management<br />
 scene: scene graph and scene manager<br />
 script: scripting engine messages<br />
 interact: interaction engine (events, scripts, etc)<br />
 smil: SMIL timing engine<br />
 compose: composition engine (2D, 3D, etc)<br />
 mmio: Audio/Video HW I/O management<br />
 rti: various run-time stats<br />
 cache: HTTP cache subsystem<br />
 audio: Audio renderer and mixers<br />
 mem: GPAC memory tracker<br />
 module: GPAC modules debugging<br />
 mutex: mutex<br />
 none: no tool logged<br />
 all: all tools logged &#8211; other tools can be specified afterwards.
</dd></dl>
<h2>PLAYBACK OPTIONS</h2>
<p> A file can be controled during playback by typing one of the following key at prompt.</p>
<dl>
<dt><code>o</code></dt>
<dd> connects to a new URL entered at prompt by user.</dd>
<dt><code>r</code></dt>
<dd> restarts the current presentation</dd>
<dt><code>p</code></dt>
<dd> plays/pauses the current presentation</dd>
<dt><code>s</code></dt>
<dd> step one frame ahead in the current presentation</dd>
<dt><code>z</code></dt>
<dd> seek into presentation. Seek percentage is entered at prompt</dd>
<dt><code>t</code></dt>
<dd> prints current timing of the main timeline of the presentation</dd>
<dt><code>w</code></dt>
<dd> prints world info of the current presentation</dd>
<dt><code>v</code></dt>
<dd> prints list of all GF_ObjectDescriptor used in current presentation.</dd>
<dt><code>i</code></dt>
<dd> prints information of a given OD. Object ID is entered at prompt.</dd>
<dt><code>b</code></dt>
<dd> prints all objects timing and buffering info.</dd>
<dt><code>m</code></dt>
<dd> prints all objects buffering and memory info.</dd>
<dt><code>d</code></dt>
<dd> dumps current presentation scene graph to file or stdout.</dd>
<dt><code>k</code></dt>
<dd> Turns stress mode on/off.</dd>
<dt><code>n</code></dt>
<dd> Changes current navigation mode if possible/allowed. When a Layer3D is selected, sets layer3D navigation if allowed.</dd>
<dt><code>x</code></dt>
<dd> Reset to last active viewpoint. When a layer3D is selected, resets layer3D viewpoint.</dd>
<dt><code>2</code></dt>
<dd> Reload MPEG-4 Client with GPAC 2D Renderer.</dd>
<dt><code>3</code></dt>
<dd> Reload MPEG-4 Client with GPAC 3D Renderer.</dd>
<dt><code>4</code></dt>
<dd> forces 4/3 Aspect Ratio.</dd>
<dt><code>5</code></dt>
<dd> forces 16/9 Aspect Ratio.</dd>
<dt><code>6</code></dt>
<dd> forces no aspect ratio (always fill screen).</dd>
<dt><code>7</code></dt>
<dd> forces original Aspect Ratio (default mode).</dd>
<dt><code>l</code></dt>
<dd> prints the list of available plugins.</dd>
<dt><code>c</code></dt>
<dd> prints some GPAC configuration info.</dd>
<dt><code>q</code></dt>
<dd> quits the application.</dd>
<dt><code>C</code></dt>
<dd> enables streaming cache.</dd>
<dt><code>S</code></dt>
<dd> stops streaming cache and record it.</dd>
<dt><code>A</code></dt>
<dd> stops streaming cache and discard it.</dd>
<dt><code>h</code></dt>
<dd> prints list of available commands.</dd></dl>
<h2>WINDOW SHORTCUTS</h2>
<p> When MP4Client window has the focus, the following shortcuts are available</p>
<dl>
<dt><code>Alt + right</code></dt>
<dd> Seeks 5% ahead from current time.</dd>
<dt><code>Alt + left</code></dt>
<dd> Seeks 5% before the current time</dd>
<dt><code>Alt + up</code></dt>
<dd> Increases volume by 5%</dd>
<dt><code>Alt + down</code></dt>
<dd> Decreases volume by 5%</dd>
<dt><code>HOME</code></dt>
<dd> Resets navigation to last bound viewpoint/viewport</dd>
<dt><code>4, 5, 6, 7</code></dt>
<dd> Same as non-window values</dd>
<dt><code>ESCAPE , alt+return, doubleclick</code></dt>
<dd> Toggles fullscreen on/off.</dd>
<dt><code>ctrl + &#8216;f&#8217;</code></dt>
<dd> Prints current rendering framerate.</dd>
<dt><code>ctrl + &#8216;R&#8217;</code></dt>
<dd> Sends a redraw message (complete scene state recompute).</dd>
<dt><code>ctrl + &#8216;P&#8217;</code></dt>
<dd> Play/Pause.</dd>
<dt><code>ctrl + &#8216;S&#8217;</code></dt>
<dd> Step one frame ahead.</dd></dl>
<h2>CONFIGURATION FILE</h2>
<p> When launched for the first time, MP4Client will ask for a font directory and a cache directory.</p>
<dl>
<dt><code>Font Directory</code></dt>
<dd> Indicates the absolute path to a directory containing a TrueType font repository. In case this directory is not specified or does not contain valid TrueType fonts, text will be disabled.</dd>
<dt><code>Cache Directory</code></dt>
<dd> Indicates the absolute path to a directory with write access to store files retrieved through HTTP downloads. In case this directory is not specified or has no write access HTTP downloads won&#8217;t work.</dd></dl>
<h2>NAVIGATION</h2>
<p> Navigation with MP4Client depends on the renderer type (2D or 3D) and also on content &#8211; some content may disable user selectable navigation.</p>
<dl>
<dt><code>Walk &amp; Fly modes</code></dt>
<dd> Mouse: Horizontal move: Horizontal pan &#8211; Vertical move: Z-translate &#8211; Vertical move+CTRL or Wheel: Vertical pan &#8211; Right Click (Walk mode only): Jump Keys: left/right: Horizontal pan &#8211; left/right+CTRL: Horizontal translate &#8211; up/down: Z-translate &#8211; up/down+CTRL: Vertical pan</dd>
<dt><code>Pan mode</code></dt>
<dd> Mouse: Horizontal move: Horizontal pan &#8211; Vertical move: Vertical pan &#8211; Vertical move+CTRL or Wheel: Z-translate Keys: left/right: Horizontal pan &#8211; left/right+CTRL: Horizontal translate &#8211; up/down: Vertical pan &#8211; up/down+CTRL: Z-translate</dd>
<dt><code>Slide mode</code></dt>
<dd> Mouse: Horizontal move: Horizontal translate &#8211; Vertical move: Vertical translate &#8211; Vertical move+CTRL or Wheel: Z-translate Keys: left/right: Horizontal translate &#8211; left/right+CTRL: Horizontal pan &#8211; up/down: Vertical translate &#8211; up/down+CTRL: Z-translate</dd>
<dt><code>Examine &amp; Orbit mode</code></dt>
<dd> Mouse: Horizontal move: Y-Axis rotate &#8211; Horizontal move+CTRL: No move &#8211; Vertical move: X-Axis rotate &#8211; Vertical move+CTRL or Wheel: Z-translate Keys: left/right: Y-Axis rotate &#8211; left/right+CTRL: Horizontal translate &#8211; up/down: X-Axis rotate &#8211; up/down+CTRL: Y-translate</dd>
<dt><code>Game mode (press END to escape)</code></dt>
<dd> Mouse: Horizontal move: H pan &#8211; Vertical move: Vertical pan Keys: left/right: Horizontal translate &#8211; up/down: Z-translate</dd>
<dt><code>All 3D modes</code></dt>
<dd> CTRL+PGUP/PGDOWN will zoom in/out camera (field of view)</dd>
<dt><code>Slide Mode in 2D</code></dt>
<dd> Mouse: Horizontal move: Horizontal translate &#8211; Vertical move: Vertical translate &#8211; V move+CTRL: zoom Keys: left/right: Horizontal translate &#8211; up/down: Vertical translate &#8211; up/down+CTRL: zoom</dd>
<dt><code>Examine Mode in 2D (3D renderer only)</code></dt>
<dd> Mouse: Horizontal move: Y-Axis rotate &#8211; Vertical move: X-Axis rotate Keys: left/right: Y-Axis rotate &#8211; up/down: X-Axis rotate</dd>
<dt><code>SHIFT</code></dt>
<dd> Speeds up movement</dd></dl>
<h2>VISUAL EXTRACTION OPTIONS</h2>
<p> When used to dump a visual presentation, the client is no longer interactive. All GPAC features are supported during capture, except audio-related ones. The following options can be passed at prompt: </p>
<dl>
<dt><code>-bmp [times]</code></dt>
<dd> dumps the specified frames to BMP format. If no time is specified, capture is made at t=0s. time is given in millisecond, as an SMPTE time code or as HH:MM:SS:MS time code. You may specify several frame times by using a dash-separated list of times (eg, &#8216;0-10-15&#8217;).</dd>
<dt><code>-raw [times]</code></dt>
<dd> dumps the specified frames to RAW format. If no time is specified, cpature is made at t=0s.</dd>
<dt><code>-avi start:end</code></dt>
<dd> dumps the specified segment to uncompressed AVI format.</dd>
<dt><code>-fps rate</code></dt>
<dd> specifies frame rate for AVI dumping. Default frame rate is 25.0.</dd>
<dt><code>-size WxH</code></dt>
<dd> specifies frame size for dumping. Default frame size is the scene size.</dd>
<dt><code>-fill</code></dt>
<dd> uses fill aspect ratio. By default, the scene aspect ratio is preserved when dumping.</dd>
<dt><code>-show</code></dt>
<dd> show window while dumping the content. By default, the window is hidden during capture.</dd>
<dt><code>-2d</code></dt>
<dd> forces usage of 2D renderer. By default, MP4Client uses the renderer indicated in GPAC configuration file.</dd>
<dt><code>-3d</code></dt>
<dd> forces usage of 3D renderer. By default, MP4Client uses the renderer indicated in GPAC configuration file.</dd>
<dt><code>-quiet</code></dt>
<dd> removes script message, buffering and downloading status.</dd></dl>
<h2>FILES</h2>
<p> <code>GPAC Configuration File:</code> ~/.gpacrc</p>
<h2>AUTHORS</h2>
<p> Jean Le Feuvre &lt;jeanlf [at] users.sourceforge.net&gt; &#8211; GPAC (c) 2000-2005 &#8211; ENST 2005-200X</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gpac/">GPAC</a>(1), <a href="/docs/linux/man/1-mp4box/">MP4Box</a>(1) </p>
<h2>Index</h2>
