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
<h2>SYNOPSIS</h2>
<p> <code>audtool</code> [&#8211;[[handler [parameters]] [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>audtool</code> is designed to send commands to a running Audacious. </p>
<p> It can handle various things like jumping to the next track in playlist or returning the current playing track title, as well as other status information.</p>
<h2>OPTIONS</h2>
<p> <code>Now playing information:</code></p>
<dl>
<dt><i>&#8211;current-song</i></p>
<dd> Returns current song title.</p>
<dt><i>&#8211;current-song-filename</i></p>
<dd> Returns current song filename.</p>
<dt><i>&#8211;current-song-length</i></p>
<dd> Returns current song length.</p>
<dt><i>&#8211;current-song-length-seconds</i></p>
<dd> Returns current song length in seconds.</p>
<dt><i>&#8211;current-song-length-frames</i></p>
<dd> Returns current song length in frames.</p>
<dt><i>&#8211;current-song-output-length</i></p>
<dd> Returns current song output length.</p>
<dt><i>&#8211;current-song-output-length-seconds</i></p>
<dd> Returns current song output length in seconds.</p>
<dt><i>&#8211;current-song-output-length-frames</i></p>
<dd> Returns current song output length in frames.</p>
<dt><i>&#8211;current-song-bitrate</i></p>
<dd> Returns current song bitrate in bits per second.</p>
<dt><i>&#8211;current-song-bitrate-kbps</i></p>
<dd> Returns current song bitrate in kilobits per second.</p>
<dt><i>&#8211;current-song-frequency</i></p>
<dd> Returns current song frequency in hertz.</p>
<dt><i>&#8211;current-song-frequency-khz</i></p>
<dd> Returns current song frequency in kilohertz.</p>
<dt><i>&#8211;current-song-channels</i></p>
<dd> Returns current song channels.</p>
<dt><i>&#8211;current-song-tuple-data &lt;fieldname&gt;</i></p>
<dd> Returns the value of a tuple field for the current song.</p>
<dt><i>&#8211;current-song-info</i></p>
<dd> Returns current song bitrate, frequency and channels.</dl>
<p> <code>Playlist manipulation:</code></p>
<dl>
<dt><i>&#8211;playlist-advance</i></p>
<dd> Go to the next song in the playlist.</p>
<dt><i>&#8211;playlist-reverse</i></p>
<dd> Go to the previous song in the playlist.</p>
<dt><i>&#8211;playlist-addurl &lt;uri&gt;</i></p>
<dd> Adds a URI to the playlist.</p>
<dt><i>&#8211;playlist-insurl &lt;uri&gt; &lt;position&gt;</i></p>
<dd> Inserts a URL at specified position in the playlist.</p>
<dt><i>&#8211;playlist-delete &lt;position&gt;</i></p>
<dd> Deletes the song at &lt;position&gt; from the playlist.</p>
<dt><i>&#8211;playlist-length</i></p>
<dd> Returns the total length of the playlist.</p>
<dt><i>&#8211;playlist-song &lt;position&gt;</i></p>
<dd> Returns the title of the song at &lt;position&gt; in the playlist.</p>
<dt><i>&#8211;playlist-song-filename &lt;position&gt;</i></p>
<dd> Returns the filename of the song at &lt;position&gt; in the playlist.</p>
<dt><i>&#8211;playlist-song-length &lt;position&gt;</i></p>
<dd> Returns the length of the song at &lt;position&gt; in the playlist.</p>
<dt><i>&#8211;playlist-song-length-seconds &lt;position&gt;</i></p>
<dd> Returns the length of the song at &lt;position&gt; in the playlist in seconds.</p>
<dt><i>&#8211;playlist-song-length-frames &lt;position&gt;</i></p>
<dd> Returns the length of the song at &lt;position&gt; in the playlist in frames.</p>
<dt><i>&#8211;playlist-display</i></p>
<dd> Returns the entire playlist.</p>
<dt><i>&#8211;playlist-position</i></p>
<dd> Returns the current position in the playlist.</p>
<dt><i>&#8211;playlist-jump &lt;position&gt;</i></p>
<dd> Jumps to &lt;position&gt; in the playlist.</p>
<dt><i>&#8211;playlist-clear</i></p>
<dd> Clears the playlist.</p>
<dt><i>&#8211;playlist-repeat-status</i></p>
<dd> Returns the status of playlist repeat.</p>
<dt><i>&#8211;playlist-repeat-toggle</i></p>
<dd> Toggles playlist repeat.</p>
<dt><i>&#8211;playlist-shuffle-status</i></p>
<dd> Returns the status of playlist shuffle.</p>
<dt><i>&#8211;playlist-shuffle-toggle</i></p>
<dd> Toggles playlist shuffle.</p>
<dt><i>&#8211;playlist-stop-after-status</i></p>
<dd> Queries whether the &quot;stop after current song&quot; option is set.</p>
<dt><i>&#8211;playlist-stop-after-toggle</i></p>
<dd> Toggles the &quot;stop after current song&quot; option.</p>
<dt><i>&#8211;playlist-tuple-data &lt;fieldname&gt; &lt;position&gt;</i></p>
<dd> Returns the value of a tuple field for a song in the playlist.</dl>
<p> <code>More playlist manipulation:</code></p>
<dl>
<dt><i>&#8211;number-of-playlists</i></p>
<dd> Returns the number of open playlists.</p>
<dt><i>&#8211;current-playlist</i></p>
<dd> Returns the number of the active playlist.</p>
<dt><i>&#8211;set-current-playlist</i></p>
<dd> Activates the specified playlist.</p>
<dt><i>&#8211;current-playlist-name</i></p>
<dd> Returns the title of the active playlist.</p>
<dt><i>&#8211;set-current-playlist-name</i></p>
<dd> Sets the title of the active playlist.</p>
<dt><i>&#8211;new-playlist</i></p>
<dd> Creates a new playlist.</p>
<dt><i>&#8211;delete-current-playlist</i></p>
<dd> Removes the active playlist.</p>
<dt><i>&#8211;play-current-playlist</i></p>
<dd> Starts or resumes playing the active playlist.</dl>
<p> <code>Playqueue manipulation:</code></p>
<dl>
<dt><i>&#8211;playqueue-add &lt;position&gt;</i></p>
<dd> Adds the song at &lt;position&gt; in the playlist to the playqueue.</p>
<dt><i>&#8211;playqueue-remove &lt;position&gt;</i></p>
<dd> Removes the song at &lt;position&gt; in the playlist from the playqueue.</p>
<dt><i>&#8211;playqueue-is-queued &lt;position&gt;</i></p>
<dd> Returns OK if the song at &lt;position&gt; in the playlist is queued.</p>
<dt><i>&#8211;playqueue-get-position &lt;position&gt;</i></p>
<dd> Returns the playqueue position of the song at &lt;position&gt; in the playlist.</p>
<dt><i>&#8211;playqueue-get-queue-position &lt;position&gt;</i></p>
<dd> Returns the playqueue position of a song in the given &lt;position&gt; in the playlist.</p>
<dt><i>&#8211;playqueue-get-list-position &lt;position&gt;</i></p>
<dd> Returns the playlist position of a song in the given position in the playqueue.</p>
<dt><i>&#8211;playqueue-length</i></p>
<dd> Returns the length of the playqueue.</p>
<dt><i>&#8211;playqueue-display</i></p>
<dd> Returns a list of currently-queued songs.</p>
<dt><i>&#8211;playqueue-clear</i></p>
<dd> Clears the playqueue.</dl>
<p> <code>Playback manipulation:</code></p>
<dl>
<dt><i>&#8211;playback-play</i></p>
<dd> Starts/unpauses song playback.</p>
<dt><i>&#8211;playback-pause</i></p>
<dd> (Un)pauses song playback.</p>
<dt><i>&#8211;playback-playpause</i></p>
<dd> Plays/(un)pauses song playback.</p>
<dt><i>&#8211;playback-stop</i></p>
<dd> Stops song playback.</p>
<dt><i>&#8211;playback-playing</i></p>
<dd> Returns OK if Audacious is playing.</p>
<dt><i>&#8211;playback-paused</i></p>
<dd> Returns OK if Audacious is paused.</p>
<dt><i>&#8211;playback-stopped</i></p>
<dd> Returns OK if Audacious is stopped.</p>
<dt><i>&#8211;playback-status</i></p>
<dd> Returns the playback status.</p>
<dt><i>&#8211;playback-seek</i></p>
<dd> Performs an absolute seek in seconds.</p>
<dt><i>&#8211;playback-seek-relative</i></p>
<dd> Performs a seek relative to the current position in seconds.</dl>
<p> <code>Volume control:</code></p>
<dl>
<dt><i>&#8211;get-volume</i></p>
<dd> Returns the current volume level in percent.</p>
<dt><i>&#8211;set-volume &lt;level&gt;</i></p>
<dd> Sets the current volume level in percent.</dl>
<p> <code>Equalizer manipulation:</code></p>
<dl>
<dt><i>&#8211;equalizer-activate &lt;on/off&gt;</i></p>
<dd> Activates/deactivates the equalizer.</p>
<dt><i>&#8211;equalizer-get</i></p>
<dd> Gets the equalizer settings.</p>
<dt><i>&#8211;equalizer-set &lt;preamp&gt; &lt;band0&gt; &lt;band1&gt; &lt;band2&gt; &lt;band3&gt; &lt;band4&gt; &lt;band5&gt; &lt;band6&gt; &lt;band7&gt; &lt;band8&gt; &lt;band9&gt;</i></p>
<dd> Sets the equalizer settings.</p>
<dt><i>&#8211;equalizer-get-preamp</i></p>
<dd> Gets the equalizer pre-amplification.</p>
<dt><i>&#8211;equalizer-set-preamp &lt;preamp&gt;</i></p>
<dd> Gets the equalizer pre-amplification.</p>
<dt><i>&#8211;equalizer-get-band &lt;band&gt;</i></p>
<dd> Gets the equalizer value in specified band.</p>
<dt><i>&#8211;equalizer-set-band &lt;band&gt; &lt;value&gt;</i></p>
<dd> Sets the equalizer value in specified band.</dl>
<p> <code>Miscellaneous:</code></p>
<dl>
<dt><i>&#8211;mainwin-show &lt;on/off&gt;</i></p>
<dd> Shows/hides the main window.</p>
<dt><i>&#8211;filebrowser-show &lt;on/off&gt;</i></p>
<dd> Shows/hides the filebrowser.</p>
<dt><i>&#8211;jumptofile-show &lt;on/off&gt;</i></p>
<dd> Shows/hides the jump to file window.</p>
<dt><i>&#8211;preferences-show &lt;on/off&gt;</i></p>
<dd> Shows/hides the preferences window.</p>
<dt><i>&#8211;about-show &lt;on/off&gt;</i></p>
<dd> Shows/hides the about window.</p>
<dt><i>&#8211;version</i></p>
<dd> Displays Audacious version.</p>
<dt><i>&#8211;shutdown</i></p>
<dd> Shuts down Audacious.</dl>
<p> <code>Help system:</code></p>
<dl>
<dt><i>&#8211;list-handlers</i></p>
<dd> Shows handlers list.</p>
<dt><i>&#8211;help</i></p>
<dd> Shows handlers list.</dl>
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
<h2>Index</h2>
