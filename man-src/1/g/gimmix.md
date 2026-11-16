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
<dt><code>mpd_hostname (mandatory)</code></dt>
<dd> hostname </dd>
<dt><code>mpd_port (mandatory)</code></dt>
<dd> port number </dd>
<dt><code>mpd_port (mandatory)</code></dt>
<dd> mpd password. Leave blank for no password </dd>
<dt><code>enable_systray (mandatory)</code></dt>
<dd> Enable/Disable the system tray icon. Enable is true, Disable is false. </dd>
<dt><code>enable_notification (mandatory)</code></dt>
<dd> Enable/Disable the notification tooltip. Enable is true, Disable is false. </dd>
<dt><code>music_directory (mandatory)</code></dt>
<dd> The absolute path to the directory where your music is stored. This is same as the one you specified in your mpd.conf. This setting is required for the tag editor to function properly. </dd>
<dt><code>play_on_add</code></dt>
<dd> If true, songs will automatically be played when you add them to the playlist. If false, songs will just be added to the playlist. Default value is false. </dd>
<dt><code>stop_on_exit</code></dt>
<dd> If true, gimmix will stop playing when user quits gimmix. If false, gimmix will not stop playing when user quits gimmix. Default value is false. </dd>
<dt><code>enable_search</code></dt>
<dd> If true, search mode is enabled in library browser. If false, search mode will be disabled. Default value is true. </dd>
<dt><code>update_on_startup</code></dt>
<dd> If true, gimmix will update the mpd database everytime on startup. If false, gimmix won&#8217;t update the mpd database on startup. Default value is false. </dd>
<dt><code>full_view_mode</code></dt>
<dd> If true, the playlist will be expanded by default when gimmix starts. If false, gimmix will start in compact mode (This is automatically set by gimmix, so, its not necessary to set this value always) </dd>
<dt><code>window_xpos and window_ypos</code></dt>
<dd> x and y co-ordinates representing window position of gimmix (These values are automatically set, so, its not necessary to set these values) </dd>
<dt><code>window_width and window_height</code></dt>
<dd> These represt the window geometry of gimmix (These values are automatically set, so, its not necessary to set these values) </dd>
<dt><code>coverart_enable</code></dt>
<dd> Enable/disable amazon cover art plugin </dd>
<dt><code>coverart_location</code></dt>
<dd> Amazon&#8217;s server location to fetch covers from. Values : com | co.uk | jp | fr | ca | de </dd>
</dl>
<h2>SEE ALSO</h2>
<p> Website: <a rel="nofollow" href="http://gimmix.berlios.de">http://gimmix.berlios.de</a></p>
<h2>AUTHOR</h2>
<p> Gimmix was written by Priyank Gosalia &lt;priyankmg [at] gmail.com&gt;. </p>
<p> This manual page was written by Vincent Legout &lt;vincent [at] legout.info&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
