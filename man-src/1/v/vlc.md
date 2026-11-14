---
title: "vlc(1)"
name: "vlc"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vlc/"
description: "vlc, qvlc, svlc, nvlc, rvlc, cvlc – the VLC media player"
---

<h2 class="name">NAME</h2>
<p> vlc, qvlc, svlc, nvlc, rvlc, cvlc &#8211; the VLC media player </p>
<h2>SYNOPSIS</h2>
<p> <code>vlc</code> [<i>OPTIONS</i>] [<i>ITEMS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>VLC</code> multimedia player and server. </p>
<h2>OPTIONS</h2>
<p> <code>VLC</code> follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). For a precise description of options, please use &quot;vlc &#8211;help&quot;. </p>
<p> The complete list of <code>VLC</code> options depends on what plugins are installed because they automatically add their own options. Please use &quot;vlc &#8211;longhelp &#8211;advanced&quot; for a complete list of available options. </p>
<h2>ITEMS</h2>
<p> <code>VLC</code> recognizes several URL-style items:</p>
<dl>
<dt><code>*.mpg, *.vob, *.avi, *.mp3, *.ogg, *.opus</code></p>
<dd> Various multimedia file formats</p>
<dt><code><a href="dvd://[">dvd://[</a>&lt;device&gt;][@&lt;raw device&gt;][#[&lt;title&gt;][:[&lt;chapter&gt;][:&lt;angle&gt;]]]</code></p>
<dd> DVD device (for instance <a href="dvd:///dev/dvd">dvd:///dev/dvd</a>). The raw device is optional and must have been prepared beforehand.</p>
<dt><code><a href="vcd://[">vcd://[</a>&lt;device&gt;][@{E|P|E|T|S}[&lt;number&gt;]]</code></p>
<dd> VCD device (for instance <a href="vcd:///dev/cdrom">vcd:///dev/cdrom</a>).</p>
<dt><code><a href="udp://[@[">udp://[@[</a>&lt;multicast address&gt;][:&lt;local port&gt;]]</code></p>
<dd> UDP stream, such as one sent by VLS or another VLC. Usually &quot;udp://&quot; is enough.</p>
<dt><code>http://&lt;server address&gt;[:&lt;server port&gt;]/[&lt;file&gt;]</code></p>
<dd> HTTP stream</p>
<dt><code>rtsp://&lt;server address&gt;[:&lt;server port&gt;]/&lt;stream name&gt;</code></p>
<dd> RTSP Video On Demand stream</p>
<dt><code>vlc://&lt;command&gt;</code></p>
<dd> Execute a playlist command. Commands are: <code>pause</code> (pause execution of other items), and <code>quit</code> (close VLC). </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may affect VLC: </p>
<dl>
<dt><code>DISPLAY</code></p>
<dd> The X11 display server address. </p>
<dt><code>http_proxy</code></p>
<dd> The HTTP proxy server URL. </p>
<dt><code>OSSAUDIO_DEV</code></p>
<dd> The default audio output device, used by the OSSv4 output plugin. </p>
<dt><code>VLC_DATA_PATH</code></p>
<dd> The directory containing VLC run-time data files (e.g. /usr/share/vlc). </p>
<dt><code>VLC_PLUGIN_PATH</code></p>
<dd> An extra directory to load VLC plugins from. </p>
<dt><code>VLC_VERBOSE</code></p>
<dd> The level of verbosity for log messages (0: silent, 1: error/info, 2: warning, 3: debug). </p>
<dt><code>XDG_CACHE_DIR XDG_CONFIG_DIR XDG_DATA_DIR</code></p>
<dd> The directories to store user cached data, user configuration files and user data files respectively. </p>
<dt><code>XDG_DOCUMENTS_DIR XDG_DOWNLOAD_DIR XDG_MUSIC_DIR XDG_PICTURES_DIR XDG_VIDEO_DIR</code></p>
<dd> The directories to fetch or store user text files, downloads, music, pictures (i.e. snapshots), and video respectively. </p>
<dt><code>XDG_SESSION_COOKIE</code></p>
<dd> The unique identifier of the desktop session, used by the PulseAudio output plugin. </p>
</dl>
<h2>SEE ALSO</h2>
<p> Online documentation: <a rel="nofollow" href="http://www.videolan.org/doc/">http://www.videolan.org/doc/</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sam Hocevar &lt;sam [at] zoy.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
