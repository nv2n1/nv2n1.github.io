---
title: "ncmpc(1)"
name: "ncmpc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncmpc/"
description: "ncmpc – curses Music Player Daemon (MPD) client."
---

<h2>NAME</h2>
<p> ncmpc &#8211; curses Music Player Daemon (MPD) client.</p>
<h2>SYNOPSIS</h2>
<p> <code>ncmpc</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> ncmpc is a client for MPD, the Music Player Daemon. ncmpc connects to a MPD running on a machine on the local network. </p>
<p> By default, ncmpc connects to localhost:6600. This can be changed either at compile-time, or by exporting the MPD_HOST and MPD_PORT environment variables, or by the command line options &#8211;host and &#8211;port. </p>
<p> $ ncmpc &#8211;host=musicserver &#8211;port=44000 </p>
<p> To use a password with mpd, set MPD_HOST to password [at] host or use the command line option &#8211;password. Values from the command line overrides values from the environment. </p>
<p> Read more about MPD on <a rel="nofollow" href="http://www.musicpd.org">http://www.musicpd.org</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Display help.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-c, &#8211;colors</code></p>
<dd> Enable colors.</p>
<dt><code>-C, &#8211;no-colors</code></p>
<dd> Disable colors.</p>
<dt><code>-e, &#8211;exit</code></p>
<dd> Exit on connection errors. The default is to reconnect.</p>
<dt><code>-h, &#8211;host=HOSTNAME</code></p>
<dd> Specify MPD host.</p>
<dt><code>-p, &#8211;port=PORT</code></p>
<dd> Connect to server on PORT.</p>
<dt><code>-P, &#8211;password=PASSWORD</code></p>
<dd> Use password when connecting.</p>
<dt><code>-f, &#8211;config=FILE</code></p>
<dd> Read configuration from file.</p>
<dt><code>-k, &#8211;key-file=FILE</code></p>
<dd> Read key bindings from FILE.</p>
<dt><code>-P, &#8211;no-splash=FILE</code></p>
<dd> Disable the splash screen.</p>
<dt>Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<dd></dl>
<h2>CONFIGURATION</h2>
<p> When ncmpc start it tries to read user setting from the ~/.ncmpc/config. If no user configuration is found ncmpc tries to load global settings from $SYSCONFDIR/ncmpc/config (the actual path is displayed on the help screen). An example configuration file (config.sample) should be provided with ncmpc. </p>
<h3>Connection</h3>
<dl>
<dt><code>host = HOST</code></p>
<dd> Connect to mpd running on specified host</p>
<dt><code>port = PORT</code></p>
<dd> Connect to mpd on the specified port</p>
<dt><code>password = PASSWORD</code></p>
<dd> Connect to mpd using the specified password.</dl>
<h3>Interface</h3>
<dl>
<dt><code>enable-mouse = yes|no</code></p>
<dd> Enable mouse support (if enabled at compile time).</p>
<dt><code>screen-list = SCREEN1 SCREEN2&#8230;</code></p>
<dd> A list of screens to cycle through when using the previous/next screen commands. Valid choices, if enabled at compile time, are playlist, browse, artist, help, search, song, keydef, lyrics, and outputs.</p>
<dt><code>search-mode = MODE</code></p>
<dd> Default search mode for the search screen. The mode is an integer index, with 0 for title, 1 for artist, 2 for album, 3 for filename, and 4 for artist+title.</p>
<dt><code>auto-center = yes|no</code></p>
<dd> Enable/disable auto center mode. When auto center mode is enabled ncmpc centers the current track in the playlist window.</p>
<dt><code>scroll-offset = NUM</code></p>
<dd> Keep at least NUM lines above and below the cursor on list windows, if possible.</p>
<dt><code>find-show-last = yes|no</code></p>
<dd> Show the most recent query instead of a blank line for a find.</p>
<dt><code>find-wrap = yes|no</code></p>
<dd> Wrapped find mode.</p>
<dt><code>wrap-around = yes|no</code></p>
<dd> Wrapped cursor movement.</p>
<dt><code>bell-on-wrap = yes|no</code></p>
<dd> Ring bell when find wraps around.</p>
<dt><code>audible-bell = yes|no</code></p>
<dd> Sound audible bell on alerts.</p>
<dt><code>visible-bell = yes|no</code></p>
<dd> Visible bell on alerts.</p>
<dt><code>crossfade-time = CROSSFADE TIME</code></p>
<dd> Default crossfade time in seconds</p>
<dt><code>seek-time = NUM</code></p>
<dd> Seek forward/backward by NUM seconds.</p>
<dt><code>lyrics-timeout = NUM</code></p>
<dd> Quits downloading lyrics of a song after the timeout of NUM seconds is reached.</p>
<dt><code>jump-prefix-only = yes|no</code></p>
<dd> When using the jump command, search for the prefix of an entry. That means typing &quot;m&quot; will start to the first entry which begins with &quot;m&quot;.</dl>
<h3>Display</h3>
<dl>
<dt><code>welcome-screen-list = yes|no</code></p>
<dd> Show a list of the screens in the top line on startup.</p>
<dt><code>wide-cursor = yes|no</code></p>
<dd> Make the cursor as wide as the screen.</p>
<dt><code>hide-cursor = NUM</code></p>
<dd> Hide the playlist cursor after NUM seconds of inactivity.</p>
<dt><code>scroll = yes|no</code></p>
<dd> Scroll the title if it is too long for the screen.</p>
<dt><code>scroll-sep = STRING</code></p>
<dd> The separator to show at the end of the scrolling title.</p>
<dt><code>list-format = SONG FORMAT</code></p>
<dd> The format used to display songs in the main window.</p>
<dt><code>status-format = SONG FORMAT</code></p>
<dd> The format used to display songs on the status line.</p>
<dt><code>status-message-time = TIME</code></p>
<dd> The time, in seconds, for which status messages will be displayed.</p>
<dt><code>display-time = yes|no</code></p>
<dd> Display the time in the status bar when idle.</p>
<dt><code>timedisplay-type = elapsed/remaining</code></p>
<dd> Sets whether to display remaining or elapsed time in the status window. Default is elapsed.</p>
<dt><code>visible-bitrate = yes|no</code></p>
<dd> Show the bitrate in the status bar when playing a stream. <code></p>
<dt>set-xterm-title = yes|no</code></p>
<dd> Change the XTerm title (ncmpc will not restore the title).</p>
<dt><code>xterm-title-format = SONG FORMAT</code></p>
<dd> The format used to for the xterm title when ncmpc is playing.</dl>
<h3>Colors</h3>
<dl>
<dt><code>enable-colors = yes|no</code></p>
<dd> Enable/disable colors.</p>
<dt><code>color background = COLOR</code></p>
<dd> Set the background color. If the background color is assigned to the keyword <code>none</code>, ncmpc will not change the background color. Valid background colors are the base colors: black, red, green, yellow, blue, magenta, cyan and white.</p>
<dt><code>color title = TEXTCOLOR</code></p>
<dd> Set the text color for the title row. Possible text colors are the base colors plus grey, brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan and brightwhite.</p>
<dt><code>color title-bold = TEXTCOLOR</code></p>
<dd> Set the text color for the title row (the bold part).</p>
<dt><code>color line = TEXTCOLOR</code></p>
<dd> Set the color of the line on the second row.</p>
<dt><code>color line-flags = TEXTCOLOR</code></p>
<dd> Set the text color used to indicate mpd flags on the second row.</p>
<dt><code>color list = TEXTCOLOR</code></p>
<dd> Set the text color in the main area of ncmpc.</p>
<dt><code>color list-bold = TEXTCOLOR</code></p>
<dd> Set the bold text color in the main area of ncmpc.</p>
<dt><code>color progressbar = TEXTCOLOR</code></p>
<dd> Set the color of the progress indicator.</p>
<dt><code>color status-state = TEXTCOLOR</code></p>
<dd> Set the text color used to display mpd status in the status window.</p>
<dt><code>color status-song = TEXTCOLOR</code></p>
<dd> Set the text color used to display song names in the status window.</p>
<dt><code>color status-time = TEXTCOLOR</code></p>
<dd> Set the text color used to display time the status window.</p>
<dt><code>color alert = TEXTCOLOR</code></p>
<dd> Text color used to display alerts in the status window.</p>
<dt><code>colordef COLOR = R, G, B</code></p>
<dd> Redefine any of the base colors. The RGB values must be an integer value between 0 and 1000. <code>Note</code>: Only some terminals allow redefinitions of colors! </p>
</dl>
<h2>KEYS</h2>
<p> When ncmpc start it tries to read user key bindings from the ~/.ncmpc/keys file. If no user key bindings is found ncmpc tries to load global key bindings from $SYSCONFDIR/ncmpc/keys (the actual path is displayed on the help screen). </p>
<p> You can view ncmpc&#8217;s key bindings by pressing &#8216;1&#8217; (help) when ncmpc is running. To edit key bindings use the key editor in ncmpc (press &#8216;K&#8217;).</p>
<h2>SONG FORMAT</h2>
<p> Format of song display for status and the list window. The metadata delimeters are: %name%, %artist%, %track%, %time%, %file%, %shortfile%. </p>
<p> The [] operators is used to group output such that if no metadata delimeters are found or matched between &#8216;[&#8216; and &#8216;]&#8217;, then none of the characters between &#8216;[&#8216; and &#8216;]&#8217; are outputed. &#8216;&amp;&#8217; and &#8216;|&#8217; are logical operators for and and or. &#8216;#&#8217; is used to escape characters. </p>
<p> Some useful examples for format are: </p>
<p>&quot;%file%&quot;&nbsp;<wbr> </p>
<p> and </p>
<p>&quot;[[%artist%&nbsp;<wbr>&#8211;&nbsp;<wbr>]%title%]|[%file]&quot;&nbsp;<wbr></p>
<h2>BUGS</h2>
<p> Report bugs on <a rel="nofollow" href="http://www.musicpd.org/mantis/">http://www.musicpd.org/mantis/</a></p>
<h2>NOTE</h2>
<p> Since MPD uses UTF-8, ncmpc needs to convert characters to the charset used by the local system. If you get character conversion errors when your running ncmpc you probably need to set up your locale. This is done by setting any of the LC_CTYPE, LANG or LC_ALL enviroment variables (LC_CTYPE only affects character handling). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mpc/">mpc</a>(1), <a href="/docs/linux/man/1-mpd/">mpd</a>(1), <a href="/docs/linux/man/5-locale/">locale</a>(5), <a href="/docs/linux/man/7-locale/">locale</a>(7) </p>
<h2>Index</h2>
