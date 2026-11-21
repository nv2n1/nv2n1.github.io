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
</dt><dd>Media Position<br />
 Right Arrow &#8211; Fast Forward<br />
 Left Arrow &#8211; Fast Reverse<br />
 Page Up &#8211; Seek 10min forward<br />
 Page Down &#8211; Seek 10min backward<br />
 Up Arrow &#8211; Seek 1 min forward<br />
 Down Arrow &#8211; Seek 1 min backward<br />
 Space &#8211; Pause<br />
 p &#8211; Pause</dd>
<dt>
</dt><dd>Video Adjustment<br />
 1 &#8211; Contrast down 5<br />
 2 &#8211; Contrast up 5<br />
 3 &#8211; Brightness down 5<br />
 4 &#8211; Brightness up 5<br />
 5 &#8211; Hue down 5<br />
 6 &#8211; Hue up 5<br />
 7 &#8211; Saturation down 5<br />
 8 &#8211; Saturation up 5</dd>
<dt>
</dt><dd>Playback Adjustment<br />
 [ &#8211; Play 10% slower<br />
 ] &#8211; Play 10% faster<br />
 { &#8211; Half speed playback<br />
 } &#8211; Double speed playback</dd>
<dt>
</dt><dd>Volume Adjustement<br />
 9 &#8211; Volume down 10<br />
 0 &#8211; Volume up 10<br />
 m &#8211; Mute</dd>
<dt>
</dt><dd>Audio and Subtitle Track Adjustment<br />
 # &#8211; Switch Audio Track<br />
 j &#8211; Subtitle select<br />
 v &#8211; Subtitle visibility<br />
 + &#8211; Increase Audio Delay<br />
 &#8211; &#8211; Decreate Audio Delay<br />
 z &#8211; Decrease Subtitle Delay<br />
 x &#8211; Increate Subtitle Delay</dd>
<dt>
</dt><dd>Other Options<br />
 Ctrl-D &#8211; Show/Hide file details<br />
 Ctrl-P &#8211; Show/Hide playlist<br />
 Ctrl-F/F &#8211; Un/Fullscreen<br />
 q &#8211; Quit immediately </dd>
</dl>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> Help Options:</p>
<dl>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show summary of options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd></dl>
<p> Application Options:</p>
<dl>
<dt><code>&#8211;window=WID</code></dt>
<dd> Window to embed in</dd>
<dt><code>-w, &#8211;width=X</code></dt>
<dd> Width of window to embed in</dd>
<dt><code>-h, &#8211;height=Y</code></dt>
<dd> Height of window to embed in</dd>
<dt><code>&#8211;controlid=CID</code></dt>
<dd> Unique DBUS controller id</dd>
<dt><code>&#8211;playlist</code></dt>
<dd> File Argument is a playlist</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Show more output on the console</dd>
<dt><code>&#8211;reallyverbose</code></dt>
<dd> Show even more output on the console</dd>
<dt><code>&#8211;fullscreen</code></dt>
<dd> Start in fullscreen mode</dd>
<dt><code>&#8211;softvol</code></dt>
<dd> Use mplayer software volume control</dd>
<dt><code>&#8211;mixer=MIXER</code></dt>
<dd> Mixer to use</dd>
<dt><code>&#8211;volume</code></dt>
<dd> Set initial volume percentage</dd>
<dt><code>&#8211;showcontrols=[0|1]</code></dt>
<dd> Show the controls in window</dd>
<dt><code>&#8211;showsubtitles=[0|1]</code></dt>
<dd> Show the subtitles if available, defaults to 1 (yes)</dd>
<dt><code>&#8211;autostart=[0|1]</code></dt>
<dd> Autostart the media. Default is 1, set to 0 to load but don&#8217;t play</dd>
<dt><code>&#8211;disablecontextmenu</code></dt>
<dd> Disable popup menu on right click</dd>
<dt><code>&#8211;disablefullscreen</code></dt>
<dd> Disable fullscreen options in browser mode</dd>
<dt><code>&#8211;loop</code></dt>
<dd> Play all files on the playlist forever</dd>
<dt><code>-q, &#8211;quit_on_complete</code></dt>
<dd> Quit application when last file on playlist is played</dd>
<dt><code>&#8211;random</code></dt>
<dd> Play items on playlist in random order</dd>
<dt><code>&#8211;cache</code></dt>
<dd> Set cache size</dd>
<dt><code>&#8211;forcecache</code></dt>
<dd> Force cache usage on streaming sites</dd>
<dt><code>&#8211;disabledeinterlace</code></dt>
<dd> Disable the deinterlace filter</dd>
<dt><code>&#8211;disableframedrop</code></dt>
<dd> Don&#8217;t skip drawing frames to better keep sync</dd>
<dt><code>&#8211;disableass</code></dt>
<dd> Use the old subtitle rendering system</dd>
<dt><code>&#8211;disableembeddedfonts</code></dt>
<dd> Don&#8217;t use fonts embedded on matroska files</dd>
<dt><code>&#8211;vertical</code></dt>
<dd> Use Vertical Layout</dd>
<dt><code>&#8211;showplaylist</code></dt>
<dd> Start with playlist open</dd>
<dt><code>&#8211;showdetails</code></dt>
<dd> Start with details visible</dd>
<dt><code>&#8211;rpname=NAME</code></dt>
<dd> Real Player Name</dd>
<dt><code>&#8211;rpconsole=CONSOLE</code></dt>
<dd> Real Player Console ID</dd>
<dt><code>&#8211;rpcontrols=Control Name,&#8230;</code></dt>
<dd> Real Player Console Controls</dd>
<dt><code>&#8211;subtitle=FILENAME</code></dt>
<dd> Subtitle file for first media file</dd>
<dt><code>&#8211;tvdevice=DEVICE</code></dt>
<dd> TV device name</dd>
<dt><code>&#8211;tvdriver=DRIVER</code></dt>
<dd> TV driver name (v4l|v4l2)</dd>
<dt><code>&#8211;tvinput=INPUT</code></dt>
<dd> TV input name</dd>
<dt><code>&#8211;tvwidth=WIDTH</code></dt>
<dd> Width of TV input</dd>
<dt><code>&#8211;tvheight=HEIGHT</code></dt>
<dd> Height of TV input</dd>
<dt><code>&#8211;tvfps=FPS</code></dt>
<dd> Frames per second from TV input</dd>
<dt><code>&#8211;single_instance</code></dt>
<dd> Only allow one instance</dd>
<dt><code>&#8211;replace_and_play</code></dt>
<dd> Put single instance mode into replace and play mode</dd>
<dt><code>&#8211;large_buttons</code></dt>
<dd> show interface with bigger icons, useful for touchscreens</dd>
<dt><code>&#8211;always_hide_after_timeout</code></dt>
<dd> control bar will always slide away, useful for small screens</dd>
<dt><code>&#8211;new_instance</code></dt>
<dd> Ignore single instance preference for this instance</dd>
<dt><code>&#8211;keep_on_top</code></dt>
<dd> Keep window on top</dd>
<dt><code>&#8211;disable_cover_art_fetch</code></dt>
<dd> Don&#8217;t fetch new cover art images</dd>
<dt><code>&#8211;display=DISPLAY</code></dt>
<dd> X display to use
</dd></dl>
<h2>AUTHOR</h2>
<p> gnome-mplayer was written by Kevin DeKorte &lt;kdekorte [at] gmail.com&gt;. </p>
