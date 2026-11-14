---
title: "mpd-conf(5)"
name: "mpd-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mpd-conf/"
description: "mpd.conf – Music Player Daemon configuration file"
---

<p>mpd.conf &#8211; Music Player Daemon configuration file</p>
<h2>Description</h2>
<p><code>mpd.conf</code> is the configuration file for <a href="/docs/linux/man/1-mpd/">mpd</a>(1). If not specified on the command line, MPD first searches for it at <code>$XDG_CONFIG_HOME/mpd/mpd.conf</code> then at <code>~/.mpdconf</code> then at <code>~/.mpd/mpd.conf</code> and then in <code>/etc/mpd.conf</code>. </p>
<p> Lines beginning with a &quot;#&quot; character are comments. All other non-empty lines specify parameters and their values. These lines contain the parameter name and parameter value (surrounded by double quotes) separated by whitespace (either tabs or spaces). For example: </p>
<p> parameter &quot;value&quot; </p>
<p> The exception to this rule is the audio_output parameter, which is of the form: </p>
<p> audio_output { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>parameter1&nbsp;<wbr>&quot;value&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>parameter2&nbsp;<wbr>&quot;value&quot;<br />
 } </p>
<p> Parameters that take a file or directory as an argument should use absolute paths. </p>
<p> See <code>docs/mpdconf.example</code> in the source tarball for an example configuration file. </p>
<p> This manual is not complete, it lists only the most important options. Please read the MPD user manual for a complete configuration guide: &lt;<code><a rel="nofollow" href="http://www.musicpd.org/doc/user/">http://www.musicpd.org/doc/user/</a></code>&gt;</p>
<h2>Required Parameters</h2>
<dl>
<dt><code>db_file &lt;file&gt;</code></p>
<dd>This specifies where the db file will be stored.</p>
<dt><code>log_file &lt;file&gt;</code></p>
<dd>This specifies where the log file should be located. The special value &quot;syslog&quot; makes MPD use the local syslog daemon.</dl>
<h2>Optional Parameters</h2>
<dl>
<dt><code>sticker_file &lt;file&gt;</code></p>
<dd>The location of the sticker database. This is a database which manages dynamic information attached to songs.</p>
<dt><code>pid_file &lt;file&gt;</code></p>
<dd>This specifies the file to save mpd&#8217;s process ID in.</p>
<dt><code>music_directory &lt;directory&gt;</code></p>
<dd>This specifies the directory where music is located. If you do not configure this, you can only play streams.</p>
<dt><code>playlist_directory &lt;directory&gt;</code></p>
<dd>This specifies the directory where saved playlists are stored. If you do not configure this, you cannot save playlists.</p>
<dt><code>state_file &lt;file&gt;</code></p>
<dd>This specifies if a state file is used and where it is located. The state of mpd will be saved to this file when mpd is terminated by a TERM signal or by the &quot;kill&quot; command. When mpd is restarted, it will read the state file and restore the state of mpd (including the playlist).</p>
<dt><code>restore_paused &lt;yes or no&gt;</code></p>
<dd>Put MPD into pause mode instead of starting playback after startup.</p>
<dt><code>user &lt;username&gt;</code></p>
<dd>This specifies the user that MPD will run as, if set. MPD should never run as root, and you may use this option to make MPD change its user id after initialization. Do not use this option if you start MPD as an unprivileged user.</p>
<dt><code>bind_to_address &lt;ip address or hostname or any&gt;</code></p>
<dd>This specifies which address mpd binds to and listens on. Multiple bind_to_address parameters may be specified. The default is &quot;any&quot;, which binds to all available addresses. </p>
<p> You can set a port that is different from the global port setting, e.g. &quot;localhost:6602&quot;. IPv6 addresses must be enclosed in square brackets if you want to configure a port, e.g. &quot;[::1]:6602&quot;. </p>
<p> To bind to a Unix domain socket, specify an absolute path or a path starting with a tilde (~). For a system-wide MPD, we suggest the path &quot;<code>/var/run/mpd/socket</code>&quot;.</p>
<dt><code>port &lt;port&gt;</code></p>
<dd>This specifies the port that mpd listens on. The default is 6600.</p>
<dt><code>log_level &lt;default, secure, or verbose&gt;</code></p>
<dd>This specifies how verbose logs are. &quot;default&quot; is minimal logging, &quot;secure&quot; reports from what address a connection is opened, and when it is closed, and &quot;verbose&quot; records excessive amounts of information for debugging purposes. The default is &quot;default&quot;.</p>
<dt><code>follow_outside_symlinks &lt;yes or no&gt;</code></p>
<dd>Control if MPD will follow symbolic links pointing outside the music dir. You must recreate the database after changing this option. The default is &quot;yes&quot;.</p>
<dt><code>follow_inside_symlinks &lt;yes or no&gt;</code></p>
<dd>Control if MPD will follow symbolic links pointing inside the music dir, potentially adding duplicates to the database. You must recreate the database after changing this option. The default is &quot;yes&quot;.</p>
<dt><code>zeroconf_enabled &lt;yes or no&gt;</code></p>
<dd>If yes, and MPD has been compiled with support for Avahi or Bonjour, service information will be published with Zeroconf. The default is yes.</p>
<dt><code>zeroconf_name &lt;name&gt;</code></p>
<dd>If Zeroconf is enabled, this is the service name to publish. This name should be unique to your local network, but name collisions will be properly dealt with. The default is &quot;Music Player&quot;.</p>
<dt><code>password &lt;password [at] permissions&gt;</code></p>
<dd>This specifies a password for access to mpd. The format is &quot;password [at] permissions&quot; where permissions is a comma delimited list composed of &quot;read&quot;, &quot;add&quot;, &quot;control&quot;, and/or &quot;admin&quot;. &quot;read&quot; allows for reading of the database, displaying the current playlist, and current status of mpd. &quot;add&quot; allows for adding songs and loading playlists. &quot;control&quot; allows for all other player and playlist manipulations. &quot;admin&quot; allows the db to be updated and for the client to kill mpd. An example value is &quot;somePassword [at] read,add&quot;. Multiple password parameters may be specified.</p>
<dt><code>default_permissions &lt;permissions&gt;</code></p>
<dd>This specifies the permissions of a client that has not been authenticated using a password. The format of permissions is specified in the description of the &quot;password&quot; config parameter. If no passwords are specified, the default is &quot;read,add,control,admin&quot;, otherwise it is &quot;&quot; (no permissions).</p>
<dt><code>audio_output</code></p>
<dd>See <code>DESCRIPTION</code> and the various <code>AUDIO OUTPUT PARAMETERS</code> sections for the format of this parameter. Multiple audio_output sections may be specified. If no audio_output section is specified, then MPD will scan for a usable audio output.</p>
<dt><code>replaygain &lt;off or album or track or auto&gt;</code></p>
<dd>If specified, mpd will adjust the volume of songs played using ReplayGain tags (see &lt;<code><a rel="nofollow" href="http://www.replaygain.org/">http://www.replaygain.org/</a></code>&gt;). Setting this to &quot;album&quot; will adjust volume using the album&#8217;s ReplayGain tags, while setting it to &quot;track&quot; will adjust it using the track ReplayGain tags. &quot;auto&quot; uses the track ReplayGain tags if random play is activated otherwise the album ReplayGain tags. Currently only FLAC, Ogg Vorbis, Musepack, and MP3 (through ID3v2 ReplayGain tags, not APEv2) are supported.</p>
<dt><code>replaygain_preamp &lt;-15 to 15&gt;</code></p>
<dd>This is the gain (in dB) applied to songs with ReplayGain tags.</p>
<dt><code>volume_normalization &lt;yes or no&gt;</code></p>
<dd>If yes, mpd will normalize the volume of songs as they play. The default is no.</p>
<dt><code>filesystem_charset &lt;charset&gt;</code></p>
<dd>This specifies the character set used for the filesystem. A list of supported character sets can be obtained by running &quot;iconv -l&quot;. The default is determined from the locale when the db was originally created.</p>
<dt><code>id3v1_encoding &lt;charset&gt;</code></p>
<dd>This specifies the character set which ID3v1 tags are encoded in. A list of supported character sets can be obtained by running &quot;iconv -l&quot;. The default is to let libid3tag convert them (from ISO-8859-1, as the standard specifies) and do no additional conversion.</p>
<dt><code>gapless_mp3_playback &lt;yes or no&gt;</code></p>
<dd>This specifies whether to support gapless playback of MP3s which have the necessary headers. Useful if your MP3s have headers with incorrect information. If you have such MP3s, it is highly recommended that you fix them using vbrfix (available from &lt;<a rel="nofollow" href="http://www.willwap.co.uk/Programs/vbrfix.php">http://www.willwap.co.uk/Programs/vbrfix.php</a>&gt;) instead of disabling gapless MP3 playback. The default is to support gapless MP3 playback.</p>
<dt><code>save_absolute_paths_in_playlists &lt;yes or no&gt;</code></p>
<dd>This specifies whether relative or absolute paths for song filenames are used when saving playlists. The default is &quot;no&quot;.</p>
<dt><code>metadata_to_use &lt;tags&gt;</code></p>
<dd>This specifies the tag types that will be scanned for and made available to clients. Note that you must recreate (not update) your database for changes to this parameter to take effect. Possible values are artist, album, title, track, name, genre, date, composer, performer, comment, disc, musicbrainz_artistid, musicbrainz_albumid, musicbrainz_albumartistid, musicbrainz_releasetrackid, musicbrainz_trackid. Multiple tags may be specified as a comma separated list. An example value is &quot;artist,album,title,track&quot;. The special value &quot;none&quot; may be used alone to disable all metadata. The default is to use all known tag types except for comments and those starting with &quot;musicbrainz&quot;.</p>
<dt><code>auto_update &lt;yes or no&gt;</code></p>
<dd>This specifies the whether to support automatic update of music database when files are changed in music_directory. The default is to disable autoupdate of database.</p>
<dt><code>auto_update_depth &lt;N&gt;</code></p>
<dd>Limit the depth of the directories being watched, 0 means only watch the music directory itself. There is no limit by default.</p>
<dt></dl>
<h2>Required Audio Output Parameters</h2>
<dd>
<dl>
<dt><code>type &lt;type&gt;</code></p>
<dd>This specifies the audio output type. See the list of supported outputs in mpd &#8211;version for possible values.</p>
<dt><code>name &lt;name&gt;</code></p>
<dd>This specifies a unique name for the audio output.</dl>
<h2>Optional Audio Output Parameters</h2>
<dl>
<dt><code>format &lt;sample_rate:bits:channels&gt;</code></p>
<dd>This specifies the sample rate, bits per sample, and number of channels of audio that is sent to the audio output device. See documentation for the <code>audio_output_format</code> parameter for more details. The default is to use whatever audio format is passed to the audio output. Any of the three attributes may be an asterisk to specify that this attribute should not be enforced</p>
<dt><code>replay_gain_handler &lt;software, mixer or none&gt;</code></p>
<dd>Specifies how replay gain is applied. The default is &quot;software&quot;, which uses an internal software volume control. &quot;mixer&quot; uses the configured (hardware) mixer control. &quot;none&quot; disables replay gain on this audio output.</dl>
<h2>Optional Alsa Output Parameters</h2>
<dl>
<dt><code>device &lt;dev&gt;</code></p>
<dd>This specifies the device to use for audio output. The default is &quot;default&quot;.</p>
<dt><code>mixer_type &lt;hardware, software or none&gt;</code></p>
<dd>Specifies which mixer should be used for this audio output: the hardware mixer (available for ALSA, OSS and PulseAudio), the software mixer or no mixer (&quot;none&quot;). By default, the hardware mixer is used for devices which support it, and none for the others.</p>
<dt><code>mixer_device &lt;mixer dev&gt;</code></p>
<dd>This specifies which mixer to use. The default is &quot;default&quot;. To use the second sound card in a system, use &quot;hw:1&quot;.</p>
<dt><code>mixer_control &lt;mixer ctrl&gt;</code></p>
<dd>This specifies which mixer control to use (sometimes referred to as the &quot;device&quot;). The default is &quot;PCM&quot;. Use &quot;amixer scontrols&quot; to see the list of possible controls.</p>
<dt><code>mixer_index &lt;mixer index&gt;</code></p>
<dd>A number identifying the index of the named mixer control. This is probably only useful if your alsa device has more than one identically-named mixer control. The default is &quot;0&quot;. Use &quot;amixer scontrols&quot; to see the list of controls with their indexes.</p>
<dt><code>use_mmap &lt;yes or no&gt;</code></p>
<dd>Setting this allows you to use memory-mapped I/O. Certain hardware setups may benefit from this, but most do not. Most users do not need to set this. The default is to not use memory-mapped I/O.</p>
<dt><code>auto_resample &lt;yes or no&gt;</code></p>
<dd>Setting this to &quot;no&quot; disables ALSA&#8217;s software resampling, if the hardware does not support a specific sample rate. This lets MPD do the resampling. &quot;yes&quot; is the default and allows ALSA to resample.</p>
<dt><code>auto_channels &lt;yes or no&gt;</code></p>
<dd>Setting this to &quot;no&quot; disables ALSA&#8217;s channel conversion, if the hardware does not support a specific number of channels. Default: &quot;yes&quot;.</p>
<dt><code>auto_format &lt;yes or no&gt;</code></p>
<dd>Setting this to &quot;no&quot; disables ALSA&#8217;s sample format conversion, if the hardware does not support a specific sample format. Default: &quot;yes&quot;.</p>
<dt><code>buffer_time &lt;time in microseconds&gt;</code></p>
<dd>This sets the length of the hardware sample buffer in microseconds. Increasing it may help to reduce or eliminate skipping on certain setups. Most users do not need to change this. The default is 500000 microseconds (0.5 seconds).</p>
<dt><code>period_time &lt;time in microseconds&gt;</code></p>
<dd>This sets the time between hardware sample transfers in microseconds. Increasing this can reduce CPU usage while lowering it can reduce underrun errors on bandwidth-limited devices. Some users have reported good results with this set to 50000, but not all devices support values this high. Most users do not need to change this. The default is 256000000 / sample_rate(kHz), or 5804 microseconds for CD-quality audio.</dl>
<h2>Files</h2>
<dl>
<dt><code>~/.mpdconf</code></p>
<dd>User configuration file.</p>
<dt><code>/etc/mpd.conf</code></p>
<dd>Global configuration file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mpd/">mpd</a>(1), <a href="/docs/linux/man/1-mpc/">mpc</a>(1) </p>
