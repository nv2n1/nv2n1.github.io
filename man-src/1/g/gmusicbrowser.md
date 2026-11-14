---
title: "gmusicbrowser(1)"
name: "gmusicbrowser"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmusicbrowser/"
description: "gmusicbrowser – Jukebox for large collections of audio files"
---

<h2>NAME</h2>
<p> gmusicbrowser &#8211; Jukebox for large collections of audio files </p>
<h2>SYNOPSIS</h2>
<p> <code>gmusicbrowser</code> [-c] [-s] [-demo] [-ro] [-rotags] [-play] [-nodbus] [-gst|-nogst] [-server] [-port N] [-C FILE] [-F FIFO|-nofifo] [-debug] [-layout NAME] [-load FILE] [-use-gnome-session] [-cmd|-launch_or_cmd CMD&#8230;] </p>
<p> <code>gmusicbrowser</code> -listcmd </p>
<p> <code>gmusicbrowser</code> -remotecmd<i>CMD&#8230;</i> </p>
<p> <code>gmusicbrowser</code> -tagedit<i>FOLDER_OR_FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page explains the <code>gmusicbrowser</code> program. </p>
<p> <code>gmusicbrowser</code> can play and manage your songs, currently supports mp3, ogg, flac, mpc file formats. see <a rel="nofollow" href="http://gmusicbrowser.sourceforge.net/">http://gmusicbrowser.sourceforge.net/</a> for more informations.</p>
<h2>OPTIONS</h2>
<p> <code></p>
<dl>
<dt>-c</code></p>
<dd> don&#8217;t check for updated/deleted songs on startup</p>
<dt><code>-s</code></p>
<dd> don&#8217;t scan folders for songs on startup</p>
<dt><code>-demo</code></p>
<dd> don&#8217;t check if current song has been updated/deleted</p>
<dt><code>-ro</code></p>
<dd> prevent modifying/renaming/deleting song files</p>
<dt><code>-rotags</code></p>
<dd> prevent modifying tags of music files</p>
<dt><code>-play</code></p>
<dd> start playing on startup</p>
<dt><code>-gst</code></p>
<dd> use gstreamer</p>
<dt><code>-nogst</code></p>
<dd> do not use gstreamer</p>
<dt><code>-nodbus</code></p>
<dd> do not use DBus</p>
<dt><code>-server</code></p>
<dd> send playing song to connected icecast client</p>
<dt><code>-port N</code></p>
<dd> listen for connection on port N in icecast server mode</p>
<dt><code>-C FILE</code></p>
<dd> use FILE as configuration file (instead of ~/.gmusicbroser/tags)</p>
<dt><code>-F FIFO</code></p>
<dd> use FIFO as named pipe to receive commans (instead of ~/.gmusicbroser/gmusicbrowser.fifo)</p>
<dt><code>-nofifo</code></p>
<dd> do not use/create named pipe $FIFOFile</p>
<dt><code>-debug</code></p>
<dd> print lots of useless informations</p>
<dt><code>-layout NAME</code></p>
<dd> use layout NAME for player window</p>
<dt><code>-load FILE</code></p>
<dd> Load FILE as a plugin</p>
<dt><code>-use-gnome-session</code></p>
<dd> Use gnome libraries to save tags/settings on session logout (needs the Gnome2 perl module).</p>
<dt><code>-cmd CMD&#8230;</code></p>
<dd> launch gmusicbrowser if not already running, and execute command CMD.</p>
<dt><code>-remotecmd CMD&#8230;</code></p>
<dd> execute command CMD in a running gmusicbrowser</p>
<dt><code>-launch_or_cmd CMD&#8230;</code></p>
<dd> launch gmusicbrowser if not already running OR execute command CMD in a running gmusicbrowser</p>
<dt><code>-listcmd</code></p>
<dd> list the available fifo commands and exit</p>
<dt><code>-tagedit FOLDER_OR_FILE &#8230;</code></p>
<dd> Load songs in FOLDER_OR_FILE and display a dialog to edit their tags. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.gmusicbrowser/tags</i></p>
<dd> contains songs tags and program options</p>
<dt><i>/usr/share/gmusicbrowser/plugins/</i>, <i>~/.gmusicbrowser/plugins/</i></p>
<dd> files with extention .pm in these folders are loaded as plugins on startup</p>
<dt><i>/usr/share/gmusicbrowser/layouts</i>, <i>~/.gmusicbrowser/layouts</i></p>
<dd> contains layouts definitions</p>
<dt><i>~/.gmusicbrowser/gmusicbrowser.fifo</i></p>
<dd> can be used to send commands to a running gmusicbrowser, eg : echo CMD &gt;~/.gmusicbrowser/gmusicbrowser.fifo where CMD is (run &quot;gmusicbrowser -listcmd&quot; for an up-to-date list of commands) :</p>
<dt><code>NextSong</code></p>
<dd> Skip current song</p>
<dt><code>PrevSong</code></p>
<dd> choose previously played song</p>
<dt><code>PlayPause</code></p>
<dd> toggle Play/Pause mode</p>
<dt><code>Stop</code></p>
<dd> stop playing</p>
<dt><code>Rewind</code> SEC</p>
<dd> rewind SEC seconds</p>
<dt><code>Forward</code> SEC</p>
<dd> forward SEC seconds</p>
<dt><code>Browser</code></p>
<dd> open browser window</p>
<dt><code>ShowHide</code></p>
<dd> hide/show gmusicbrowser windows</p>
<dt><code>Quit</code></p>
<dd> quit gmusicbrowser</p>
<dt><code>Save</code></p>
<dd> immediately save settings/song tags in ~/.gmusicbrowser/tags</p>
<dt><code>ChangeDisplay</code> DISPLAY</p>
<dd> migrate the program to display DISPLAY (example : &quot;:1&quot;) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://squentin.free.fr/gmusicbrowser/gmusicbrowser.html,">http://squentin.free.fr/gmusicbrowser/gmusicbrowser.html,</a> </p>
<h2>BUGS</h2>
<p> If you wish to report a bug please use the <a href="/docs/linux/man/1-reportbug/">reportbug</a>(1) command. </p>
<h2>AUTHOR</h2>
<p> Copyright (c) 2005-2008 Quentin Sculo &lt;squentin [at] free.fr&gt; </p>
<h2>Index</h2>
