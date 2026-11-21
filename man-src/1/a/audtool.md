---

title: "audtool(1)"
name: "audtool"
section: "1"
letter: "a"
url: "/docs/linux/man/1-audtool/"
description: "audtool – a small tool to modify behavior of a running Audacious instance."
---

<h2>NAME</h2>
<p> <code>audtool</code> &#8211; a small tool to modify behavior of a running Audacious instance.</p>
<p> <code>audtool</code> [&#8211;[[handler [parameters]] [&#8230;]</p>
<p> <code>audtool</code> is designed to send commands to a running Audacious. </p>
<p> It can handle various things like jumping to the next track in playlist or returning the current playing track title, as well as other status information.</p>
<h2>OPTIONS</h2>
<p> <code>Now playing information:</code></p>
<dl>
<dt><i>&#8211;current-song</i></dt>
<dd> Returns current song title.</dd>
<dt><i>&#8211;current-song-filename</i></dt>
<dd> Returns current song filename.</dd>
<dt><i>&#8211;current-song-length</i></dt>
<dd> Returns current song length.</dd>
<dt><i>&#8211;current-song-length-seconds</i></dt>
<dd> Returns current song length in seconds.</dd>
<dt><i>&#8211;current-song-length-frames</i></dt>
<dd> Returns current song length in frames.</dd>
<dt><i>&#8211;current-song-output-length</i></dt>
<dd> Returns current song output length.</dd>
<dt><i>&#8211;current-song-output-length-seconds</i></dt>
<dd> Returns current song output length in seconds.</dd>
<dt><i>&#8211;current-song-output-length-frames</i></dt>
<dd> Returns current song output length in frames.</dd>
<dt><i>&#8211;current-song-bitrate</i></dt>
<dd> Returns current song bitrate in bits per second.</dd>
<dt><i>&#8211;current-song-bitrate-kbps</i></dt>
<dd> Returns current song bitrate in kilobits per second.</dd>
<dt><i>&#8211;current-song-frequency</i></dt>
<dd> Returns current song frequency in hertz.</dd>
<dt><i>&#8211;current-song-frequency-khz</i></dt>
<dd> Returns current song frequency in kilohertz.</dd>
<dt><i>&#8211;current-song-channels</i></dt>
<dd> Returns current song channels.</dd>
<dt><i>&#8211;current-song-tuple-data &lt;fieldname&gt;</i></dt>
<dd> Returns the value of a tuple field for the current song.</dd>
<dt><i>&#8211;current-song-info</i></dt>
<dd> Returns current song bitrate, frequency and channels.</dd></dl>
<p> <code>Playlist manipulation:</code></p>
<dl>
<dt><i>&#8211;playlist-advance</i></dt>
<dd> Go to the next song in the playlist.</dd>
<dt><i>&#8211;playlist-reverse</i></dt>
<dd> Go to the previous song in the playlist.</dd>
<dt><i>&#8211;playlist-addurl &lt;uri&gt;</i></dt>
<dd> Adds a URI to the playlist.</dd>
<dt><i>&#8211;playlist-insurl &lt;uri&gt; &lt;position&gt;</i></dt>
<dd> Inserts a URL at specified position in the playlist.</dd>
<dt><i>&#8211;playlist-delete &lt;position&gt;</i></dt>
<dd> Deletes the song at &lt;position&gt; from the playlist.</dd>
<dt><i>&#8211;playlist-length</i></dt>
<dd> Returns the total length of the playlist.</dd>
<dt><i>&#8211;playlist-song &lt;position&gt;</i></dt>
<dd> Returns the title of the song at &lt;position&gt; in the playlist.</dd>
<dt><i>&#8211;playlist-song-filename &lt;position&gt;</i></dt>
<dd> Returns the filename of the song at &lt;position&gt; in the playlist.</dd>
<dt><i>&#8211;playlist-song-length &lt;position&gt;</i></dt>
<dd> Returns the length of the song at &lt;position&gt; in the playlist.</dd>
<dt><i>&#8211;playlist-song-length-seconds &lt;position&gt;</i></dt>
<dd> Returns the length of the song at &lt;position&gt; in the playlist in seconds.</dd>
<dt><i>&#8211;playlist-song-length-frames &lt;position&gt;</i></dt>
<dd> Returns the length of the song at &lt;position&gt; in the playlist in frames.</dd>
<dt><i>&#8211;playlist-display</i></dt>
<dd> Returns the entire playlist.</dd>
<dt><i>&#8211;playlist-position</i></dt>
<dd> Returns the current position in the playlist.</dd>
<dt><i>&#8211;playlist-jump &lt;position&gt;</i></dt>
<dd> Jumps to &lt;position&gt; in the playlist.</dd>
<dt><i>&#8211;playlist-clear</i></dt>
<dd> Clears the playlist.</dd>
<dt><i>&#8211;playlist-repeat-status</i></dt>
<dd> Returns the status of playlist repeat.</dd>
<dt><i>&#8211;playlist-repeat-toggle</i></dt>
<dd> Toggles playlist repeat.</dd>
<dt><i>&#8211;playlist-shuffle-status</i></dt>
<dd> Returns the status of playlist shuffle.</dd>
<dt><i>&#8211;playlist-shuffle-toggle</i></dt>
<dd> Toggles playlist shuffle.</dd>
<dt><i>&#8211;playlist-stop-after-status</i></dt>
<dd> Queries whether the &quot;stop after current song&quot; option is set.</dd>
<dt><i>&#8211;playlist-stop-after-toggle</i></dt>
<dd> Toggles the &quot;stop after current song&quot; option.</dd>
<dt><i>&#8211;playlist-tuple-data &lt;fieldname&gt; &lt;position&gt;</i></dt>
<dd> Returns the value of a tuple field for a song in the playlist.</dd></dl>
<p> <code>More playlist manipulation:</code></p>
<dl>
<dt><i>&#8211;number-of-playlists</i></dt>
<dd> Returns the number of open playlists.</dd>
<dt><i>&#8211;current-playlist</i></dt>
<dd> Returns the number of the active playlist.</dd>
<dt><i>&#8211;set-current-playlist</i></dt>
<dd> Activates the specified playlist.</dd>
<dt><i>&#8211;current-playlist-name</i></dt>
<dd> Returns the title of the active playlist.</dd>
<dt><i>&#8211;set-current-playlist-name</i></dt>
<dd> Sets the title of the active playlist.</dd>
<dt><i>&#8211;new-playlist</i></dt>
<dd> Creates a new playlist.</dd>
<dt><i>&#8211;delete-current-playlist</i></dt>
<dd> Removes the active playlist.</dd>
<dt><i>&#8211;play-current-playlist</i></dt>
<dd> Starts or resumes playing the active playlist.</dd></dl>
<p> <code>Playqueue manipulation:</code></p>
<dl>
<dt><i>&#8211;playqueue-add &lt;position&gt;</i></dt>
<dd> Adds the song at &lt;position&gt; in the playlist to the playqueue.</dd>
<dt><i>&#8211;playqueue-remove &lt;position&gt;</i></dt>
<dd> Removes the song at &lt;position&gt; in the playlist from the playqueue.</dd>
<dt><i>&#8211;playqueue-is-queued &lt;position&gt;</i></dt>
<dd> Returns OK if the song at &lt;position&gt; in the playlist is queued.</dd>
<dt><i>&#8211;playqueue-get-position &lt;position&gt;</i></dt>
<dd> Returns the playqueue position of the song at &lt;position&gt; in the playlist.</dd>
<dt><i>&#8211;playqueue-get-queue-position &lt;position&gt;</i></dt>
<dd> Returns the playqueue position of a song in the given &lt;position&gt; in the playlist.</dd>
<dt><i>&#8211;playqueue-get-list-position &lt;position&gt;</i></dt>
<dd> Returns the playlist position of a song in the given position in the playqueue.</dd>
<dt><i>&#8211;playqueue-length</i></dt>
<dd> Returns the length of the playqueue.</dd>
<dt><i>&#8211;playqueue-display</i></dt>
<dd> Returns a list of currently-queued songs.</dd>
<dt><i>&#8211;playqueue-clear</i></dt>
<dd> Clears the playqueue.</dd></dl>
<p> <code>Playback manipulation:</code></p>
<dl>
<dt><i>&#8211;playback-play</i></dt>
<dd> Starts/unpauses song playback.</dd>
<dt><i>&#8211;playback-pause</i></dt>
<dd> (Un)pauses song playback.</dd>
<dt><i>&#8211;playback-playpause</i></dt>
<dd> Plays/(un)pauses song playback.</dd>
<dt><i>&#8211;playback-stop</i></dt>
<dd> Stops song playback.</dd>
<dt><i>&#8211;playback-playing</i></dt>
<dd> Returns OK if Audacious is playing.</dd>
<dt><i>&#8211;playback-paused</i></dt>
<dd> Returns OK if Audacious is paused.</dd>
<dt><i>&#8211;playback-stopped</i></dt>
<dd> Returns OK if Audacious is stopped.</dd>
<dt><i>&#8211;playback-status</i></dt>
<dd> Returns the playback status.</dd>
<dt><i>&#8211;playback-seek</i></dt>
<dd> Performs an absolute seek in seconds.</dd>
<dt><i>&#8211;playback-seek-relative</i></dt>
<dd> Performs a seek relative to the current position in seconds.</dd></dl>
<p> <code>Volume control:</code></p>
<dl>
<dt><i>&#8211;get-volume</i></dt>
<dd> Returns the current volume level in percent.</dd>
<dt><i>&#8211;set-volume &lt;level&gt;</i></dt>
<dd> Sets the current volume level in percent.</dd></dl>
<p> <code>Equalizer manipulation:</code></p>
<dl>
<dt><i>&#8211;equalizer-activate &lt;on/off&gt;</i></dt>
<dd> Activates/deactivates the equalizer.</dd>
<dt><i>&#8211;equalizer-get</i></dt>
<dd> Gets the equalizer settings.</dd>
<dt><i>&#8211;equalizer-set &lt;preamp&gt; &lt;band0&gt; &lt;band1&gt; &lt;band2&gt; &lt;band3&gt; &lt;band4&gt; &lt;band5&gt; &lt;band6&gt; &lt;band7&gt; &lt;band8&gt; &lt;band9&gt;</i></dt>
<dd> Sets the equalizer settings.</dd>
<dt><i>&#8211;equalizer-get-preamp</i></dt>
<dd> Gets the equalizer pre-amplification.</dd>
<dt><i>&#8211;equalizer-set-preamp &lt;preamp&gt;</i></dt>
<dd> Gets the equalizer pre-amplification.</dd>
<dt><i>&#8211;equalizer-get-band &lt;band&gt;</i></dt>
<dd> Gets the equalizer value in specified band.</dd>
<dt><i>&#8211;equalizer-set-band &lt;band&gt; &lt;value&gt;</i></dt>
<dd> Sets the equalizer value in specified band.</dd></dl>
<p> <code>Miscellaneous:</code></p>
<dl>
<dt><i>&#8211;mainwin-show &lt;on/off&gt;</i></dt>
<dd> Shows/hides the main window.</dd>
<dt><i>&#8211;filebrowser-show &lt;on/off&gt;</i></dt>
<dd> Shows/hides the filebrowser.</dd>
<dt><i>&#8211;jumptofile-show &lt;on/off&gt;</i></dt>
<dd> Shows/hides the jump to file window.</dd>
<dt><i>&#8211;preferences-show &lt;on/off&gt;</i></dt>
<dd> Shows/hides the preferences window.</dd>
<dt><i>&#8211;about-show &lt;on/off&gt;</i></dt>
<dd> Shows/hides the about window.</dd>
<dt><i>&#8211;version</i></dt>
<dd> Displays Audacious version.</dd>
<dt><i>&#8211;shutdown</i></dt>
<dd> Shuts down Audacious.</dd></dl>
<p> <code>Help system:</code></p>
<dl>
<dt><i>&#8211;list-handlers</i></dt>
<dd> Shows handlers list.</dd>
<dt><i>&#8211;help</i></dt>
<dd> Shows handlers list.</dd></dl>
<p> Handlers may be prefixed with `&#8211;&#8216; (GNU-style long-options) or not, your choice.</p>
<h2>BUGS</h2>
<p> There are no known bugs in audtool at this time; if you find any please report them on &lt;<a rel="nofollow" href="http://www.redmine.audacious-media-player.org">www.redmine.audacious-media-player.org</a>&gt; in the Audacious issue tracker.</p>
<h2>AUTHORS</h2>
<p> <code>audtool</code> was written by George Averill &lt;nhjm [at] nhjm.net&gt; and William Pitcock &lt;nenolod [at] atheme.org&gt;. </p>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; and Kiyoshi Aman &lt;kiyoshi [at] atheme.org&gt;. Some additional tweaks were done by William Pitcock &lt;nenolod [at] atheme.org&gt; and Tony Vroon &lt;chainsaw [at] gentoo.org&gt;. </p>
<p> This work is licensed under a Creative Commons Attribution 3.0 Unported License &lt;<a rel="nofollow" href="http://creativecommons.org/licenses/by/3.0/">http://creativecommons.org/licenses/by/3.0/</a>&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-audacious/">audacious</a></code>(1) </p>
<h2>WEBSITE</h2>
<p> <i><a rel="nofollow" href="http://audacious-media-player.org">http://audacious-media-player.org</a></i> </p>
