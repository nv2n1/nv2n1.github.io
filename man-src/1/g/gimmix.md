---
title: "gimmix(1)"
name: "gimmix"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gimmix/"
description: "Gimmix – a graphical music player daemon (MPD) client"
---

<h2 class="name">NAME</h2>
<p> Gimmix &#8211; a graphical music player daemon (MPD) client </p>
<h2>SYNOPSIS</h2>
<p> <code>gimmix</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gimmix</code> command. </p>
<p> <code>gimmix</code> is a graphical music player daemon (MPD) client written in C using GTK+2. It&#8217;s very simple and easy to use, yet offers many features to make your audio experience a pleasant one. </p>
<h2>CONFIGURATION</h2>
<p> Default configuration file location is $HOME/.gimmixrc. </p>
<p> List of valid configuration options :</p>
<dl>
<dt><code>mpd_hostname (mandatory)</code></p>
<dd> hostname </p>
<dt><code>mpd_port (mandatory)</code></p>
<dd> port number </p>
<dt><code>mpd_port (mandatory)</code></p>
<dd> mpd password. Leave blank for no password </p>
<dt><code>enable_systray (mandatory)</code></p>
<dd> Enable/Disable the system tray icon. Enable is true, Disable is false. </p>
<dt><code>enable_notification (mandatory)</code></p>
<dd> Enable/Disable the notification tooltip. Enable is true, Disable is false. </p>
<dt><code>music_directory (mandatory)</code></p>
<dd> The absolute path to the directory where your music is stored. This is same as the one you specified in your mpd.conf. This setting is required for the tag editor to function properly. </p>
<dt><code>play_on_add</code></p>
<dd> If true, songs will automatically be played when you add them to the playlist. If false, songs will just be added to the playlist. Default value is false. </p>
<dt><code>stop_on_exit</code></p>
<dd> If true, gimmix will stop playing when user quits gimmix. If false, gimmix will not stop playing when user quits gimmix. Default value is false. </p>
<dt><code>enable_search</code></p>
<dd> If true, search mode is enabled in library browser. If false, search mode will be disabled. Default value is true. </p>
<dt><code>update_on_startup</code></p>
<dd> If true, gimmix will update the mpd database everytime on startup. If false, gimmix won&#8217;t update the mpd database on startup. Default value is false. </p>
<dt><code>full_view_mode</code></p>
<dd> If true, the playlist will be expanded by default when gimmix starts. If false, gimmix will start in compact mode (This is automatically set by gimmix, so, its not necessary to set this value always) </p>
<dt><code>window_xpos and window_ypos</code></p>
<dd> x and y co-ordinates representing window position of gimmix (These values are automatically set, so, its not necessary to set these values) </p>
<dt><code>window_width and window_height</code></p>
<dd> These represt the window geometry of gimmix (These values are automatically set, so, its not necessary to set these values) </p>
<dt><code>coverart_enable</code></p>
<dd> Enable/disable amazon cover art plugin </p>
<dt><code>coverart_location</code></p>
<dd> Amazon&#8217;s server location to fetch covers from. Values : com | co.uk | jp | fr | ca | de </p>
</dl>
<h2>SEE ALSO</h2>
<p> Website: <a rel="nofollow" href="http://gimmix.berlios.de">http://gimmix.berlios.de</a></p>
<h2>AUTHOR</h2>
<p> Gimmix was written by Priyank Gosalia &lt;priyankmg [at] gmail.com&gt;. </p>
<p> This manual page was written by Vincent Legout &lt;vincent [at] legout.info&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
