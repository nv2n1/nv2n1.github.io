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
<dt><code>-c file</code></p>
<dd> specifies config file to use. Default config file is located in user home directory and created if not found.</p>
<dt><code>-rti file</code></p>
<dd> logs run-time information to file. Information logged is: FPS, CPU, Memory usage.</p>
<dt><code>-quiet</code></p>
<dd> removes script message, buffering and downloading status.</p>
<dt><code>-strict-error</code></p>
<dd> exits after the first error is reported.</p>
<dt><code>-log-file FILE</code></p>
<dd> specifies where to write logs. Default is stdout. Same as -lf.</p>
<dt><code>-logs TOOLS</code></p>
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
</dl>
<h2>PLAYBACK OPTIONS</h2>
<p> A file can be controled during playback by typing one of the following key at prompt.</p>
<dl>
<dt><code>o</code></p>
<dd> connects to a new URL entered at prompt by user.</p>
<dt><code>r</code></p>
<dd> restarts the current presentation</p>
<dt><code>p</code></p>
<dd> plays/pauses the current presentation</p>
<dt><code>s</code></p>
<dd> step one frame ahead in the current presentation</p>
<dt><code>z</code></p>
<dd> seek into presentation. Seek percentage is entered at prompt</p>
<dt><code>t</code></p>
<dd> prints current timing of the main timeline of the presentation</p>
<dt><code>w</code></p>
<dd> prints world info of the current presentation</p>
<dt><code>v</code></p>
<dd> prints list of all GF_ObjectDescriptor used in current presentation.</p>
<dt><code>i</code></p>
<dd> prints information of a given OD. Object ID is entered at prompt.</p>
<dt><code>b</code></p>
<dd> prints all objects timing and buffering info.</p>
<dt><code>m</code></p>
<dd> prints all objects buffering and memory info.</p>
<dt><code>d</code></p>
<dd> dumps current presentation scene graph to file or stdout.</p>
<dt><code>k</code></p>
<dd> Turns stress mode on/off.</p>
<dt><code>n</code></p>
<dd> Changes current navigation mode if possible/allowed. When a Layer3D is selected, sets layer3D navigation if allowed.</p>
<dt><code>x</code></p>
<dd> Reset to last active viewpoint. When a layer3D is selected, resets layer3D viewpoint.</p>
<dt><code>2</code></p>
<dd> Reload MPEG-4 Client with GPAC 2D Renderer.</p>
<dt><code>3</code></p>
<dd> Reload MPEG-4 Client with GPAC 3D Renderer.</p>
<dt><code>4</code></p>
<dd> forces 4/3 Aspect Ratio.</p>
<dt><code>5</code></p>
<dd> forces 16/9 Aspect Ratio.</p>
<dt><code>6</code></p>
<dd> forces no aspect ratio (always fill screen).</p>
<dt><code>7</code></p>
<dd> forces original Aspect Ratio (default mode).</p>
<dt><code>l</code></p>
<dd> prints the list of available plugins.</p>
<dt><code>c</code></p>
<dd> prints some GPAC configuration info.</p>
<dt><code>q</code></p>
<dd> quits the application.</p>
<dt><code>C</code></p>
<dd> enables streaming cache.</p>
<dt><code>S</code></p>
<dd> stops streaming cache and record it.</p>
<dt><code>A</code></p>
<dd> stops streaming cache and discard it.</p>
<dt><code>h</code></p>
<dd> prints list of available commands.</dl>
<h2>WINDOW SHORTCUTS</h2>
<p> When MP4Client window has the focus, the following shortcuts are available</p>
<dl>
<dt><code>Alt + right</code></p>
<dd> Seeks 5% ahead from current time.</p>
<dt><code>Alt + left</code></p>
<dd> Seeks 5% before the current time</p>
<dt><code>Alt + up</code></p>
<dd> Increases volume by 5%</p>
<dt><code>Alt + down</code></p>
<dd> Decreases volume by 5%</p>
<dt><code>HOME</code></p>
<dd> Resets navigation to last bound viewpoint/viewport</p>
<dt><code>4, 5, 6, 7</code></p>
<dd> Same as non-window values</p>
<dt><code>ESCAPE , alt+return, doubleclick</code></p>
<dd> Toggles fullscreen on/off.</p>
<dt><code>ctrl + &#8216;f&#8217;</code></p>
<dd> Prints current rendering framerate.</p>
<dt><code>ctrl + &#8216;R&#8217;</code></p>
<dd> Sends a redraw message (complete scene state recompute).</p>
<dt><code>ctrl + &#8216;P&#8217;</code></p>
<dd> Play/Pause.</p>
<dt><code>ctrl + &#8216;S&#8217;</code></p>
<dd> Step one frame ahead.</dl>
<h2>CONFIGURATION FILE</h2>
<p> When launched for the first time, MP4Client will ask for a font directory and a cache directory.</p>
<dl>
<dt><code>Font Directory</code></p>
<dd> Indicates the absolute path to a directory containing a TrueType font repository. In case this directory is not specified or does not contain valid TrueType fonts, text will be disabled.</p>
<dt><code>Cache Directory</code></p>
<dd> Indicates the absolute path to a directory with write access to store files retrieved through HTTP downloads. In case this directory is not specified or has no write access HTTP downloads won&#8217;t work.</dl>
<h2>NAVIGATION</h2>
<p> Navigation with MP4Client depends on the renderer type (2D or 3D) and also on content &#8211; some content may disable user selectable navigation.</p>
<dl>
<dt><code>Walk &amp; Fly modes</code></p>
<dd> Mouse: Horizontal move: Horizontal pan &#8211; Vertical move: Z-translate &#8211; Vertical move+CTRL or Wheel: Vertical pan &#8211; Right Click (Walk mode only): Jump Keys: left/right: Horizontal pan &#8211; left/right+CTRL: Horizontal translate &#8211; up/down: Z-translate &#8211; up/down+CTRL: Vertical pan</p>
<dt><code>Pan mode</code></p>
<dd> Mouse: Horizontal move: Horizontal pan &#8211; Vertical move: Vertical pan &#8211; Vertical move+CTRL or Wheel: Z-translate Keys: left/right: Horizontal pan &#8211; left/right+CTRL: Horizontal translate &#8211; up/down: Vertical pan &#8211; up/down+CTRL: Z-translate</p>
<dt><code>Slide mode</code></p>
<dd> Mouse: Horizontal move: Horizontal translate &#8211; Vertical move: Vertical translate &#8211; Vertical move+CTRL or Wheel: Z-translate Keys: left/right: Horizontal translate &#8211; left/right+CTRL: Horizontal pan &#8211; up/down: Vertical translate &#8211; up/down+CTRL: Z-translate</p>
<dt><code>Examine &amp; Orbit mode</code></p>
<dd> Mouse: Horizontal move: Y-Axis rotate &#8211; Horizontal move+CTRL: No move &#8211; Vertical move: X-Axis rotate &#8211; Vertical move+CTRL or Wheel: Z-translate Keys: left/right: Y-Axis rotate &#8211; left/right+CTRL: Horizontal translate &#8211; up/down: X-Axis rotate &#8211; up/down+CTRL: Y-translate</p>
<dt><code>Game mode (press END to escape)</code></p>
<dd> Mouse: Horizontal move: H pan &#8211; Vertical move: Vertical pan Keys: left/right: Horizontal translate &#8211; up/down: Z-translate</p>
<dt><code>All 3D modes</code></p>
<dd> CTRL+PGUP/PGDOWN will zoom in/out camera (field of view)</p>
<dt><code>Slide Mode in 2D</code></p>
<dd> Mouse: Horizontal move: Horizontal translate &#8211; Vertical move: Vertical translate &#8211; V move+CTRL: zoom Keys: left/right: Horizontal translate &#8211; up/down: Vertical translate &#8211; up/down+CTRL: zoom</p>
<dt><code>Examine Mode in 2D (3D renderer only)</code></p>
<dd> Mouse: Horizontal move: Y-Axis rotate &#8211; Vertical move: X-Axis rotate Keys: left/right: Y-Axis rotate &#8211; up/down: X-Axis rotate</p>
<dt><code>SHIFT</code></p>
<dd> Speeds up movement</dl>
<h2>VISUAL EXTRACTION OPTIONS</h2>
<p> When used to dump a visual presentation, the client is no longer interactive. All GPAC features are supported during capture, except audio-related ones. The following options can be passed at prompt: </p>
<dl>
<dt><code>-bmp [times]</code></p>
<dd> dumps the specified frames to BMP format. If no time is specified, capture is made at t=0s. time is given in millisecond, as an SMPTE time code or as HH:MM:SS:MS time code. You may specify several frame times by using a dash-separated list of times (eg, &#8216;0-10-15&#8217;).</p>
<dt><code>-raw [times]</code></p>
<dd> dumps the specified frames to RAW format. If no time is specified, cpature is made at t=0s.</p>
<dt><code>-avi start:end</code></p>
<dd> dumps the specified segment to uncompressed AVI format.</p>
<dt><code>-fps rate</code></p>
<dd> specifies frame rate for AVI dumping. Default frame rate is 25.0.</p>
<dt><code>-size WxH</code></p>
<dd> specifies frame size for dumping. Default frame size is the scene size.</p>
<dt><code>-fill</code></p>
<dd> uses fill aspect ratio. By default, the scene aspect ratio is preserved when dumping.</p>
<dt><code>-show</code></p>
<dd> show window while dumping the content. By default, the window is hidden during capture.</p>
<dt><code>-2d</code></p>
<dd> forces usage of 2D renderer. By default, MP4Client uses the renderer indicated in GPAC configuration file.</p>
<dt><code>-3d</code></p>
<dd> forces usage of 3D renderer. By default, MP4Client uses the renderer indicated in GPAC configuration file.</p>
<dt><code>-quiet</code></p>
<dd> removes script message, buffering and downloading status.</dl>
<h2>FILES</h2>
<p> <code>GPAC Configuration File:</code> ~/.gpacrc</p>
<h2>AUTHORS</h2>
<p> Jean Le Feuvre &lt;jeanlf [at] users.sourceforge.net&gt; &#8211; GPAC (c) 2000-2005 &#8211; ENST 2005-200X</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gpac/">GPAC</a>(1), <a href="/docs/linux/man/1-mp4box/">MP4Box</a>(1) </p>
<h2>Index</h2>
