---
title: "gnome-mplayer(1)"
name: "gnome-mplayer"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-mplayer/"
description: "gnome-mplayer – a simple GUI for MPlayer"
---

<h2>NAME</h2>
<p> gnome-mplayer &#8211; a simple GUI for MPlayer</p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-mplayer</code> [<i>options</i>]<i> files</i>&#8230;<br />
 <code>gnome-mplayer</code> [<i>options</i>]<i> cdda://</i><br />
 <code>gnome-mplayer</code> [<i>options</i>]<i> [dvd|dvdnav]://</i><br />
 <code>gnome-mplayer</code> [<i>options</i>]<i> [http|mms|rtsp]://</i><br />
 <code>gnome-mplayer</code> [<i>options</i>]<i> /dev/[sd*|dvd|cdrom]</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gnome-mplayer</code> command. </p>
<p> <code>gnome-mplayer</code> provides a simple and clean interface to MPlayer.<br />
 GNOME MPlayer has a rich API that is exposed via DBus.<br />
 Using DBus you can control a single or multiple instances of GNOME MPlayer from a single command.<br />
 GNOME MPlayer can be used to play media on websites when used in conjunction with Gecko Mediaplayer. </p>
<p> Homepage: <a rel="nofollow" href="http://kdekorte.googlepages.com/gnomemplayer">http://kdekorte.googlepages.com/gnomemplayer</a></p>
<h2>INTERACTIVE CONTROL</h2>
<p> Many of the keyboard shortcuts in gnome-mplayer are the same as those found in mplayer. Here is a list of more of the commonly used shortcuts.</p>
<h3>Keyboard Controls</h3>
<dl>
<dt>
<dd>Media Position<br />
 Right Arrow &#8211; Fast Forward<br />
 Left Arrow &#8211; Fast Reverse<br />
 Page Up &#8211; Seek 10min forward<br />
 Page Down &#8211; Seek 10min backward<br />
 Up Arrow &#8211; Seek 1 min forward<br />
 Down Arrow &#8211; Seek 1 min backward<br />
 Space &#8211; Pause<br />
 p &#8211; Pause</p>
<dt>
<dd>Video Adjustment<br />
 1 &#8211; Contrast down 5<br />
 2 &#8211; Contrast up 5<br />
 3 &#8211; Brightness down 5<br />
 4 &#8211; Brightness up 5<br />
 5 &#8211; Hue down 5<br />
 6 &#8211; Hue up 5<br />
 7 &#8211; Saturation down 5<br />
 8 &#8211; Saturation up 5</p>
<dt>
<dd>Playback Adjustment<br />
 [ &#8211; Play 10% slower<br />
 ] &#8211; Play 10% faster<br />
 { &#8211; Half speed playback<br />
 } &#8211; Double speed playback</p>
<dt>
<dd>Volume Adjustement<br />
 9 &#8211; Volume down 10<br />
 0 &#8211; Volume up 10<br />
 m &#8211; Mute</p>
<dt>
<dd>Audio and Subtitle Track Adjustment<br />
 # &#8211; Switch Audio Track<br />
 j &#8211; Subtitle select<br />
 v &#8211; Subtitle visibility<br />
 + &#8211; Increase Audio Delay<br />
 &#8211; &#8211; Decreate Audio Delay<br />
 z &#8211; Decrease Subtitle Delay<br />
 x &#8211; Increate Subtitle Delay</p>
<dt>
<dd>Other Options<br />
 Ctrl-D &#8211; Show/Hide file details<br />
 Ctrl-P &#8211; Show/Hide playlist<br />
 Ctrl-F/F &#8211; Un/Fullscreen<br />
 q &#8211; Quit immediately </p>
</dl>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> Help Options:</p>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-gtk</code></p>
<dd> Show GTK+ Options</dl>
<p> Application Options:</p>
<dl>
<dt><code>&#8211;window=WID</code></p>
<dd> Window to embed in</p>
<dt><code>-w, &#8211;width=X</code></p>
<dd> Width of window to embed in</p>
<dt><code>-h, &#8211;height=Y</code></p>
<dd> Height of window to embed in</p>
<dt><code>&#8211;controlid=CID</code></p>
<dd> Unique DBUS controller id</p>
<dt><code>&#8211;playlist</code></p>
<dd> File Argument is a playlist</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Show more output on the console</p>
<dt><code>&#8211;reallyverbose</code></p>
<dd> Show even more output on the console</p>
<dt><code>&#8211;fullscreen</code></p>
<dd> Start in fullscreen mode</p>
<dt><code>&#8211;softvol</code></p>
<dd> Use mplayer software volume control</p>
<dt><code>&#8211;mixer=MIXER</code></p>
<dd> Mixer to use</p>
<dt><code>&#8211;volume</code></p>
<dd> Set initial volume percentage</p>
<dt><code>&#8211;showcontrols=[0|1]</code></p>
<dd> Show the controls in window</p>
<dt><code>&#8211;showsubtitles=[0|1]</code></p>
<dd> Show the subtitles if available, defaults to 1 (yes)</p>
<dt><code>&#8211;autostart=[0|1]</code></p>
<dd> Autostart the media. Default is 1, set to 0 to load but don&#8217;t play</p>
<dt><code>&#8211;disablecontextmenu</code></p>
<dd> Disable popup menu on right click</p>
<dt><code>&#8211;disablefullscreen</code></p>
<dd> Disable fullscreen options in browser mode</p>
<dt><code>&#8211;loop</code></p>
<dd> Play all files on the playlist forever</p>
<dt><code>-q, &#8211;quit_on_complete</code></p>
<dd> Quit application when last file on playlist is played</p>
<dt><code>&#8211;random</code></p>
<dd> Play items on playlist in random order</p>
<dt><code>&#8211;cache</code></p>
<dd> Set cache size</p>
<dt><code>&#8211;forcecache</code></p>
<dd> Force cache usage on streaming sites</p>
<dt><code>&#8211;disabledeinterlace</code></p>
<dd> Disable the deinterlace filter</p>
<dt><code>&#8211;disableframedrop</code></p>
<dd> Don&#8217;t skip drawing frames to better keep sync</p>
<dt><code>&#8211;disableass</code></p>
<dd> Use the old subtitle rendering system</p>
<dt><code>&#8211;disableembeddedfonts</code></p>
<dd> Don&#8217;t use fonts embedded on matroska files</p>
<dt><code>&#8211;vertical</code></p>
<dd> Use Vertical Layout</p>
<dt><code>&#8211;showplaylist</code></p>
<dd> Start with playlist open</p>
<dt><code>&#8211;showdetails</code></p>
<dd> Start with details visible</p>
<dt><code>&#8211;rpname=NAME</code></p>
<dd> Real Player Name</p>
<dt><code>&#8211;rpconsole=CONSOLE</code></p>
<dd> Real Player Console ID</p>
<dt><code>&#8211;rpcontrols=Control Name,&#8230;</code></p>
<dd> Real Player Console Controls</p>
<dt><code>&#8211;subtitle=FILENAME</code></p>
<dd> Subtitle file for first media file</p>
<dt><code>&#8211;tvdevice=DEVICE</code></p>
<dd> TV device name</p>
<dt><code>&#8211;tvdriver=DRIVER</code></p>
<dd> TV driver name (v4l|v4l2)</p>
<dt><code>&#8211;tvinput=INPUT</code></p>
<dd> TV input name</p>
<dt><code>&#8211;tvwidth=WIDTH</code></p>
<dd> Width of TV input</p>
<dt><code>&#8211;tvheight=HEIGHT</code></p>
<dd> Height of TV input</p>
<dt><code>&#8211;tvfps=FPS</code></p>
<dd> Frames per second from TV input</p>
<dt><code>&#8211;single_instance</code></p>
<dd> Only allow one instance</p>
<dt><code>&#8211;replace_and_play</code></p>
<dd> Put single instance mode into replace and play mode</p>
<dt><code>&#8211;large_buttons</code></p>
<dd> show interface with bigger icons, useful for touchscreens</p>
<dt><code>&#8211;always_hide_after_timeout</code></p>
<dd> control bar will always slide away, useful for small screens</p>
<dt><code>&#8211;new_instance</code></p>
<dd> Ignore single instance preference for this instance</p>
<dt><code>&#8211;keep_on_top</code></p>
<dd> Keep window on top</p>
<dt><code>&#8211;disable_cover_art_fetch</code></p>
<dd> Don&#8217;t fetch new cover art images</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> X display to use
</dl>
<h2>AUTHOR</h2>
<p> gnome-mplayer was written by Kevin DeKorte &lt;kdekorte [at] gmail.com&gt;. </p>
<h2>Index</h2>
