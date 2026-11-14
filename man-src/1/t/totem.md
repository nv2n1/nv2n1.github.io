---
title: "totem(1)"
name: "totem"
section: "1"
letter: "t"
url: "/docs/linux/man/1-totem/"
description: "Totem – GNOME desktop movie player based on GStreamer"
---

<h2 class="name">NAME</h2>
<p> Totem &#8211; GNOME desktop movie player based on GStreamer </p>
<h2>SYNOPSIS</h2>
<p> <code>totem</code> [<i>option&#8230;</i>]<i> </i>[<i>filenames</i>|<i>URI</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Totem</code> is a movie player for the GNOME desktop. Through use of the <code>GStreamer</code> backend many popular file and streaming formats are supported including: MPEG audio and video (MP3/MPV), Ogg, AVI, ASF, MOV, WMV, QuickTime, and more. Playing of DVD and VCD media is also possible. Although primarily intended as a movie player, <code>Totem</code> can also play many audio formats. </p>
<p> For additional documentation on interactive use of <code>Totem</code> select the <i>Help</i> menu option. The menus allow access to some features not available through keybindings or command-line options.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Output a longer help message then quit. (Any discrepancies between this man page and the output of <code>totem &#8211;help</code> should be reported as a documentation bug.)</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information then quit.</dl>
<p> The following options command an already-running instance of <code>Totem</code> to do something; they are useful for remote-control scripting. If <code>Totem</code> is not already running, these commands will launch a new instance of <code>Totem</code> but will not do anything further.</p>
<dl>
<dt><code>&#8211;play-pause</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to toggle between play and pause.</p>
<dt><code>&#8211;play</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to play (has no effect if already playing)</p>
<dt><code>&#8211;pause</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to pause (has no effect if already paused)</p>
<dt><code>&#8211;next</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to skip to the next movie or chapter in the playlist.</p>
<dt><code>&#8211;previous</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to return to the previous movie or chapter in the playlist.</p>
<dt><code>&#8211;seek-fwd</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to seek forwards 15 seconds in the current movie.</p>
<dt><code>&#8211;seek-bwd</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to seek backwards 15 seconds in the current movie.</p>
<dt><code>&#8211;volume-up</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to raise the volume by 8%.</p>
<dt><code>&#8211;volume-down</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to lower the volume by 8%.</p>
<dt><code>&#8211;mute</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to toggle between muted and unmuted audio.</p>
<dt><code>&#8211;fullscreen</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to toggle fullscreen mode.</p>
<dt><code>&#8211;quit</code></p>
<dd> Tell an already-running instance of <code>Totem</code> to quit.</p>
<dt><code>&#8211;enqueue </code><i>filename|URI</i></p>
<dd> Tell an already-running instance of Totem to add a new stream to the playlist.</p>
<dt><code>&#8211;replace </code><i>filename|URI</i></p>
<dd> Tell an already-running instance of Totem to play from the playlist.</dl>
<h2>KEYBINDINGS</h2>
<p> Global keybindings for <code>Totem</code>: </p>
<p> a<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>cycle between aspect ratios</p>
<p> p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>toggle between play and pause</p>
<p> Esc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>exit full screen mode</p>
<p> f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>toggle full screen</p>
<p> h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>toggle display of on-screen controls</p>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>resize window to 50% original size</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>resize window to 100% original size</p>
<p> 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>resize window to 200% original size</p>
<p> r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>zoom in the video</p>
<p> t<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>zoom out the video</p>
<p> d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>start and stop the telestrator (drawing) mode</p>
<p> e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>erase the drawing</p>
<p> Left-arrow skip back 15 seconds<br />
 Right-arrow skip forward 60 seconds<br />
 Shift+Left-arrow skip back 5 seconds<br />
 Shift+Right-arrow skip forward 15 seconds<br />
 Ctrl+Left-arrow skip back 3 minutes<br />
 Ctrl+Right arrow skip forward 10 minutes<br />
 Up-arrow<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>increase volume by 8%</p>
<p> Down-arrow<tt>&nbsp;<wbr>&nbsp;</tt>decrease volume by 8%</p>
<p> b<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>jump back to previous chapter/movie in playlist</p>
<p> n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>jump to next chapter/movie in playlist</p>
<p> q<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>quit</p>
<p> Ctrl+E eject the playing optical media<br />
 Ctrl+O<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>open a new file</p>
<p> Ctrl+L<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>open a new URI</p>
<p> F9<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>toggle display of the playlist</p>
<p> m<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>show the DVD menu</p>
<p> c<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>show the DVD chapter menu</p>
<h2>FILES</h2>
<p> <i>/usr/lib/totem/plugins/</i></p>
<dl>
<dt>
<dd> The global plugins directory, which contains all the system-installed plugins.</dl>
<p> <i>~/.local/share/totem/plugins/</i></p>
<dl>
<dt>
<dd> The user plugins directory, containing plugins available only to that user. It is always in the &quot;totem/plugins&quot; subdirectory of your <code>XDG_DATA_HOME</code> directory.</dl>
<p> <i>~/.config/totem/state.ini</i></p>
<dl>
<dt>
<dd> The configuration file for the main window&#8217;s appearance, stored in a simple INI format.</dl>
<h2>BUGS</h2>
<p> <code>Totem</code> cannot play files using some proprietary codecs.</p>
<h2>AUTHOR</h2>
<p> <code>Totem</code> was written by Bastien Nocera &lt;hadess [at] hadess.net&gt;. This manual page was written by Andre Lehovich for the Debian Project.</p>
<h2>DISTRIBUTION</h2>
<p> The latest version of Totem may be downloaded from &lt;<a rel="nofollow" href="https://wiki.gnome.org/Apps/Videos">https://wiki.gnome.org/Apps/Videos</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-totem-video-thumbnailer/">totem-video-thumbnailer</a></code>(1), </p>
<p> The online documentation available through the program&#8217;s <i>Help</i> menu. </p>
<h2>Index</h2>
