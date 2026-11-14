---
title: "audacious2(1)"
name: "audacious2"
section: "1"
letter: "a"
url: "/docs/linux/man/1-audacious2/"
description: "audacious2 – an advanced audio player."
---

<h2 class="name">NAME</h2>
<p> audacious2 &#8211; an advanced audio player.</p>
<h2>SYNOPSIS</h2>
<p> <code>audacious2</code> [OPTION] &#8230; [FILE] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Audacious is a free advanced audio player for Linux and many other UNIX-compatible systems. It focuses on low resource usage, high audio quality, and support for a wide range of audio formats. It was originally based on Beep Media Player, which was in turn based on XMMS. </p>
<h2>OPTIONS</h2>
<p> <code>Getting help:</code> </p>
<dl>
<dt><i>-?, &#8211;help</i></p>
<dd> Show a brief list of options. </p>
<dt><i>&#8211;help-all</i></p>
<dd> Show a complete list of options. </p>
<dt><i>&#8211;help-gtk</i></p>
<dd> Show a list of GTK+-related options. </p>
<dt><i>&#8211;help-sm-client</i></p>
<dd> Show a list of session management options. </p>
</dl>
<p> <code>Opening files:</code> </p>
<dl>
<dt><i>-e, &#8211;enqueue</i></p>
<dd> Add the files on the command line to the current playlist but do not start playback. </p>
<dt><i>-E, &#8211;enqueue-to-temp</i></p>
<dd> Add the files on the command line to a temporary playlist and start playback. </p>
</dl>
<p> <code>Controlling playback:</code> </p>
<dl>
<dt><i>-p, &#8211;play</i></p>
<dd> If currently playing, go to the beginning of the song; otherwise, begin playing. </p>
<dt><i>-u, &#8211;pause</i></p>
<dd> Stop playing. </p>
<dt><i>-t, &#8211;play-pause</i></p>
<dd> If currently playing, stop playing; otherwise, begin playing. </p>
<dt><i>-s, &#8211;stop</i></p>
<dd> Stop playing and go to the beginning of the song. </p>
<dt><i>-r, &#8211;rew</i></p>
<dd> Go to the previous song in the playlist. </p>
<dt><i>-f, &#8211;fwd</i></p>
<dd> Go to the next song in the playlist. </p>
</dl>
<p> <code>Miscellaneous:</code> </p>
<dl>
<dt><i>-v, &#8211;version</i></p>
<dd> Show the installed version of Audacious. </p>
<dt><i>-i, &#8211;interface newui | skinned | headless</i></p>
<dd> Start Audacious with the given interface. &quot;newui&quot; is the native GTK+ interface. &quot;skinned&quot; is an interface which uses Winamp Classic skins. (Skins can be placed in <i>${prefix}/share/audacious/Skins</i>, <i>~/.local/share/audacious/Skins</i>, and the folder specified by the environment variable <i>SKINSDIR</i>. They can be unarchived or in the following archive formats: <i>.zip</i>, <i>.wsz</i>, <i>.tgz</i>, <i>.tar.gz</i>, and <i>.tar.bz2</i>.) In &quot;headless&quot; mode, Audacious starts without a user interface. In this mode, it can only be controlled from the command line or by a compatible client program. </p>
<dt><i>-m, &#8211;show-main-window</i></p>
<dd> Show the Audacious window if it is hidden and bring it to the top. </p>
</dl>
<p> <code>GTK+-related:</code> </p>
<dl>
<dt><i>&#8211;display DISPLAY</i></p>
<dd> Start Audacious on the given X display. </p>
<dt><i>&#8211;screen SCREEN</i></p>
<dd> Start Audacious on the given X screen. </p>
<dt><i>&#8211;sync</i></p>
<dd> Use synchronous X calls. </p>
<dt><i>&#8211;name NAME</i></p>
<dd> Set Audacious&#8217;s program name (for use by the window manager). </p>
<dt><i>&#8211;class CLASS</i></p>
<dd> Set Audacious&#8217;s program class (for use by the window manager). </p>
<dt><i>&#8211;gtk-module MODULE</i></p>
<dd> Load a GTK+ module manually. </p>
<dt><i>&#8211;g-fatal-warnings</i></p>
<dd> Treat all warnings as fatal errors. </p>
</dl>
<p> <code>Session management:</code> </p>
<dl>
<dt><i>&#8211;sm-client-disable</i></p>
<dd> Do not connect to the session manager. </p>
<dt><i>&#8211;sm-client-id ID</i></p>
<dd> Set session management ID. </p>
<dt><i>&#8211;sm-client-state-file FILE</i></p>
<dd> Load saved configuration from FILE. </p>
</dl>
<h2>KEYBINDINGS</h2>
<p> z<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Previous song</p>
<p> x<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Play</p>
<p> c, Space<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Pause</p>
<p> v<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Stop</p>
<p> b<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Next song</p>
<p> Right arrow<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Seek forward 5 seconds</p>
<p> Left arrow<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Seek backward 5 seconds</p>
<p> Control + z<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Go to beginning of playlist</p>
<p> Escape<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Scroll to current song</p>
<p> Control + a<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Select all songs in playlist</p>
<p> Shift + Control + a<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Cancel selection</p>
<p> s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle shuffle</p>
<p> r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle repeat</p>
<p> Control + n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle advancing in playlist</p>
<p> Control + m<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle stopping after current song</p>
<p> Control + e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Show elapsed time</p>
<p> Control + r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Show time remaining</p>
<p> Alt + e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Show/hide playlist</p>
<p> Alt + g<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Show/hide equalizer</p>
<p> Control + o<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle windows always on top</p>
<p> Control + s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle windows on all workspaces</p>
<p> Control + w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle rolling up main window</p>
<p> Control + Alt + w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle rolling up equalizer</p>
<p> Shift + Control + w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle rolling up playlist</p>
<p> Control + d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle double size</p>
<p> i<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Song Information dialog</p>
<p> Control + j<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Jump to Time dialog</p>
<p> j<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Jump to Song dialog</p>
<p> Control + f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Search dialog</p>
<p> l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Open dialog</p>
<p> f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Add dialog</p>
<p> Control + l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Open Internet Address dialog</p>
<p> Control + h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Add Internet Address dialog</p>
<p> Control + p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display Preferences dialog</p>
<h2>FILES</h2>
<dl>
<dt>~/.config/audacious/config</p>
<dd> User&#8217;s Audacious configuration.</p>
<dt>~/.config/audacious/playlist.xspf</p>
<dd> Default playlist usually loaded on startup.</p>
<dt>~/.config/audacious/gtkrc</p>
<dd> User&#8217;s set of Audacious-specific GTK+ config settings. Options such as widget color and fonts sizes can be set here.</p>
<dt>~/.local/share/audacious/Skins, ${prefix}/share/audacious/Skins</p>
<dd> Default location(s) where Audacious should look for skinfiles.</p>
<dt>~/.local/share/audacious/Plugins</p>
<dd> Location of user-installed plugins.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SKINSDIR</code></p>
<dd> Colon separated list of paths where Audacious should look for skinfiles.</p>
<dt><code>TARCMD</code></p>
<dd> Tar command supporting GNU tar style decompression. Used for unpacking gzip and bzip2 compressed skins. Default is <i>tar</i>.</p>
<dt><code>UNZIPCMD</code></p>
<dd> Command for decompressing zip files (skins). Default is <i>unzip</i>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-audtool2/">audtool2</a></code>(1) </p>
<h2>WEBSITE</h2>
<p> <i><a rel="nofollow" href="http://audacious-media-player.org">http://audacious-media-player.org</a></i> </p>
<h2>Index</h2>
