---

title: "mpc(1)"
name: "mpc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpc/"
description: "mpc – Program for controlling Music Player Daemon (MPD)"
---

<h2>NAME</h2>
<p> mpc &#8211; Program for controlling Music Player Daemon (MPD)</p>
<p> mpc [&lt;command&gt; &lt;arguments&gt;]</p>
<p> mpc is a client for MPD, the Music Player Daemon. mpc connects to a MPD and controls it according to commands and arguments passed to it. If no arguments are passed, current status is given.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;format</code></dt>
<dd>
 Configure the format of song display for status and the playlist. The metadata delimiters are &quot;%name%&quot;, &quot;%artist%&quot;, &quot;%album%&quot;, &quot;%title%&quot;, &quot;%track%&quot;, &quot;%time%&quot;, and &quot;%file%&quot;. The [] operator is used to group output such that if no metadata delimiters are found or matched between &#8216;[&#8216; and &#8216;]&#8217;, then none of the characters between &#8216;[&#8216; and &#8216;]&#8217; are output. &#8216;&amp;&#8217; and &#8216;|&#8217; are logical operators for and and or. &#8216;#&#8217; is used to escape characters. Some useful examples for format are: &quot;%file%&quot; and &quot;[[%artist% &#8211; ]%title%]|[%file%]&quot;. This command also takes the following defined escape sequences:<br />
 \ &#8211; backslash<br />
  &#8211; alert<br />
  &#8211; backspace<br />
 	 &#8211; tab<br />
 &#8211; newline<br />
  &#8211; vertical tab<br />
  &#8211; form-feed<br />
 &#8211; carriage return</dd>
<dt><code>&#8211;no-status</code></dt>
<dd>
 Prevents the current song status from being printed on completion of some of the commands.</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>add &lt;file&gt;</code></dt>
<dd> Adds a song from the music database to the playlist. Can also read input from pipes. Use &quot;mpc ls | mpc add&quot; to add all files to the playlist.</dd>
<dt><code>clear</code></dt>
<dd> Empties playlist.</dd>
<dt><code>crop</code></dt>
<dd> Remove all songs except for the currently playing song.</dd>
<dt><code>current</code></dt>
<dd> Show the currently playing song</dd>
<dt><code>crossfade [&lt;seconds&gt;]</code></dt>
<dd> Gets and sets the current amount of crossfading between songs (0 disables crossfading).</dd>
<dt><code>del &lt;songpos&gt;</code></dt>
<dd> Removes a playlist number from the playlist. Can also read input from pipes (0 deletes the current playing song).</dd>
<dt><code>disable &lt;output #&gt;</code></dt>
<dd> Disables the output, number is required.</dd>
<dt><code>enable &lt;output #&gt;</code></dt>
<dd> Enables the output, number is required.</dd>
<dt><code>idle</code></dt>
<dd> Waits until an event occurs. Prints a list of event names, one per line. See the MPD protocol documentation for further information.</dd>
<dt><code>listall [&lt;file&gt;]</code></dt>
<dd> Lists &lt;file&gt; from playlist. If no &lt;file&gt; is specified, lists all songs.</dd>
<dt><code>load &lt;file&gt;</code></dt>
<dd> Loads &lt;file&gt; as playlist.</dd>
<dt><code>ls [&lt;directory&gt;]</code></dt>
<dd> Lists all files/folders in &lt;directory&gt;. If no &lt;directory&gt; is specified, lists all files in music directory.</dd>
<dt><code>lsplaylists</code></dt>
<dd> Lists available playlists.</dd>
<dt><code>move &lt;from&gt; &lt;to&gt;</code></dt>
<dd> Moves song at position &lt;from&gt; to the position &lt;to&gt; in the playlist.</dd>
<dt><code>next</code></dt>
<dd> Starts playing next song on playlist.</dd>
<dt><code>outputs</code></dt>
<dd> Lists all available outputs</dd>
<dt><code>pause</code></dt>
<dd> Pauses playing.</dd>
<dt><code>play &lt;position&gt;</code></dt>
<dd> Starts playing the song-number specified. If none is specified, plays number 1.</dd>
<dt><code>playlist</code></dt>
<dd> Prints entire playlist.</dd>
<dt><code>prev</code></dt>
<dd> Starts playing previous song.</dd>
<dt><code>random &lt;on|off&gt;</code></dt>
<dd> Toggle random mode if state (&quot;on&quot; or &quot;off&quot;) is not specified.</dd>
<dt><code>repeat &lt;on|off&gt;</code></dt>
<dd> Toggle repeat mode if state (&quot;on&quot; or &quot;off&quot;) is not specified.</dd>
<dt><code>single &lt;on|off&gt;</code></dt>
<dd> Toggle single mode if state (&quot;on&quot; or &quot;off&quot;) is not specified.</dd>
<dt><code>consume &lt;on|off&gt;</code></dt>
<dd> Toggle consume mode if state (&quot;on&quot; or &quot;off&quot;) is not specified.</dd>
<dt><code>rm &lt;file&gt;</code></dt>
<dd> Deletes a specific playlist.</dd>
<dt><code>save &lt;file&gt;</code></dt>
<dd> Saves playlist as &lt;file&gt;.</dd>
<dt><code>search &lt;type&gt; &lt;query&gt; [&lt;type&gt; &lt;query&gt;]&#8230;</code></dt>
<dd> Searches for songs where all of the given tag &lt;type&gt;s match the given &lt;query&gt;s. Any number of tag type and query combinations can be specified. Possible tag types are: artist, album, title, track, name, genre, date, composer, performer, comment, disc, filename, or any (to match any tag).</dd>
<dt><code>find &lt;type&gt; &lt;query&gt; [&lt;type&gt; &lt;query&gt;]&#8230;</code></dt>
<dd> Same as search, but match &lt;query&gt;s exactly.</dd>
<dt><code>list &lt;type&gt; [&lt;type&gt; &lt;query&gt;]&#8230;</code></dt>
<dd> Return a list of all tags of given tag &lt;type&gt;. Optional search &lt;type&gt;s/&lt;query&gt;s limit results in a way similar to search.</dd>
<dt><code>seek [+-][&lt;HH:MM:SS&gt;] or &lt;[+-]&lt;0-100&gt;%&gt;</code></dt>
<dd> Seeks by hour, minute or seconds, hours or minutes can be omitted. If seeking by percentage, seeks within the current song in the specified manner. If a &quot;+&quot; or &quot;-&quot; is used, the seek is done relative to the current song position. Absolute seeking by default.</dd>
<dt><code>shuffle</code></dt>
<dd> Shuffles all songs on the playlist.</dd>
<dt><code>stats</code></dt>
<dd> Displays statistics about MPD.</dd>
<dt><code>stop</code></dt>
<dd> Stops playing.</dd>
<dt><code>toggle</code></dt>
<dd> Toggles between play and pause. If stopped starts playing. Does not support start playing at song number (use play).</dd>
<dt><code>update [&lt;path&gt;]</code></dt>
<dd> Scans music directory for updates if no &lt;path&gt; is specified. If one or more &lt;path&gt;&#8217;s are specified, scans only those path&#8217;s for updates. Can take input from a pipe.</dd>
<dt><code>version</code></dt>
<dd> Reports the version of MPD.</dd>
<dt><code>volume [+-]&lt;num&gt;</code></dt>
<dd> Sets the volume to &lt;num&gt; (0-100). If &quot;+&quot; or &quot;-&quot; is used, then it adjusts the volume relative to the current volume.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>This section describes some environment variables that affect how mpc operates.</dt>
<dd></dd></dl>
<p> MPD_HOST, MPD_PORT</p>
<dl>
<dt>
</dt><dd> By default, mpc connects to localhost:6600. This can be changed either at compile-time, or by exporting the MPD_HOST and MPD_PORT environment variables.<br />
 If you specify an absolute path in MPD_HOST, mpc attempts a connection via Unix Domain Socket.<br />
 To use a password with MPD, set MPD_HOST to password [at] host.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> For useful examples of mpc use in playlist parsing, see mpd-m3u-playlist.sh and mpd-pls-playlist.sh.
</dd></dl>
<h2>BUGS</h2>
<p> Report bugs on <a rel="nofollow" href="http://www.musicpd.org/mantis/">http://www.musicpd.org/mantis/</a></p>
<h2>NOTE</h2>
<p> Since MPD uses UTF-8, mpc needs to convert characters to the charset used by the local system. If you get character conversion errors when you&#8217;re running mpc you probably need to set up your locale. This is done by setting any of the LC_CTYPE, LANG or LC_ALL environment variables (LC_CTYPE only affects character handling).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mpd/">mpd</a>(1)</p>
<h2>AUTHOR</h2>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>See &lt;<a rel="nofollow" href="https://svn.musicpd.org/mpc/trunk/AUTHORS">https://svn.musicpd.org/mpc/trunk/AUTHORS</a>&gt;, for contributors to mpc</p>
