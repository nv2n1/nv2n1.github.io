---
title: "mpg123-alsa(1)"
name: "mpg123-alsa"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpg123-alsa/"
description: "mpg123 – play audio MPEG 1.0/2.0/2.5 stream (layers 1, 2 and 3)"
---

<h2 class="name">NAME</h2>
<p> mpg123 &#8211; play audio MPEG 1.0/2.0/2.5 stream (layers 1, 2 and 3) </p>
<h2>SYNOPSIS</h2>
<p> <code>mpg123</code> [ <code>options</code> ] <i>file-or-URL</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>mpg123</code> reads one or more <i>file</i>s (or standard input if &#8220;-&#8221; is specified) or <i>URL</i>s and plays them on the audio device (default) or outputs them to stdout. <i>file</i>/<i>URL</i> is assumed to be an MPEG audio bit stream.</p>
<h2>OPERANDS</h2>
<p> The following operands are supported:</p>
<dl>
<dt><i>file</i>(s)</p>
<dd> The path name(s) of one or more input files. They must be valid MPEG-1.0/2.0/2.5 audio layer 1, 2 or 3 bit streams. If a dash &#8220;-&#8221; is specified, MPEG data will be read from the standard input. Furthermore, any name starting with &#8220;<a rel="nofollow" href="http://''">http://&#8221;</a> is recognized as <i>URL</i> (see next section).</dl>
<h2>OPTIONS</h2>
<p> <code>mpg123</code> options may be either the traditional POSIX one letter options, or the GNU style long options. POSIX style options start with a single &#8220;-&#8221;, while GNU long options start with &#8220;&#8211;&#8221;. Option arguments (if needed) follow separated by whitespace (not &#8220;=&#8221;). Note that some options can be absent from your installation when disabled in the build process.</p>
<h2>INPUT OPTIONS</h2>
<dl>
<dt><code>-k </code><i>num</i>, <code>&#8211;skip </code><i>num</p>
<dd> Skip first num</i> frames. By default the decoding starts at the first frame.</p>
<dt><code>-n </code><i>num</i>, <code>&#8211;frames </code><i>num</p>
<dd> Decode only num</i> frames. By default the complete stream is decoded.</p>
<dt><code>&#8211;fuzzy</code></p>
<dd> Enable fuzzy seeks (guessing byte offsets or using approximate seek points from Xing TOC). Without that, seeks need a first scan through the file before they can jump at positions. You can decide here: sample-accurate operation with gapless features or faster (fuzzy) seeking.</p>
<dt><code>-y</code>, <code>&#8211;no-resync</code></p>
<dd> Do NOT try to resync and continue decoding if an error occurs in the input file. Normally, <code>mpg123</code> tries to keep the playback alive at all costs, including skipping invalid material and searching new header when something goes wrong. With this switch you can make it bail out on data errors (and perhaps spare your ears a bad time). Note that this switch has been renamed from &#8211;resync. The old name still works, but is not advertised or recommened to use (subject to removal in future).</p>
<dt><code>&#8211;resync-limit </code><i>bytes</i></p>
<dd> Set number of bytes to search for valid MPEG data once lost in stream; &lt;0 means search whole stream. If you know there are huge chunks of invalid data in your files&#8230; here is your hammer. Note: Only since version 1.14 this also increases the amount of junk skipped on beginning.</p>
<dt><code>-p </code><i>URL </i>| <code>none</code>, <code>&#8211;proxy </code><i>URL </i>| <code>none</p>
<dd> The specified </code><i>proxy</i> will be used for HTTP requests. It should be specified as full URL (&#8220;<a rel="nofollow" href="http://host.domain:port/''">http://host.domain:port/&#8221;</a>), but the &#8220;<a rel="nofollow" href="http://''">http://&#8221;</a> prefix, the port number and the trailing slash are optional (the default port is 80). Specifying <code>none</code> means not to use any proxy, and to retrieve files directly from the respective servers. See also the &#8220;HTTP SUPPORT&#8221; section.</p>
<dt><code>-u </code><i>auth</i>, <code>&#8211;auth </code><i>auth</p>
<dd> HTTP authentication to use when recieving files via HTTP. The format used is user:password.</p>
<dt></i><code>&#8211;ignore-mime</p>
<dd> Ignore MIME types given by HTTP server. If you know better and want mpg123 to decode something the server thinks is image/png, then just do it.</p>
<dt>&#8211;no-seekbuffer</p>
<dd> Disable the default micro-buffering of non-seekable streams that gives the parser a safer footing.</p>
<dt>-@ </code><i>file</i>, <code>&#8211;list </code><i>file</p>
<dd> Read filenames and/or URLs of MPEG audio streams from the specified file</i> in addition to the ones specified on the command line (if any). Note that <i>file</i> can be either an ordinary file, a dash &#8220;-&#8221; to indicate that a list of filenames/URLs is to be read from the standard input, or an URL pointing to a an appropriate list file. Note: only one <code>-@</code> option can be used (if more than one is specified, only the last one will be recognized).</p>
<dt><code>-l </code><i>n</i>, <code>&#8211;listentry </code><i>n</p>
<dd> Of the playlist, play specified entry only. n</i> is the number of entry starting at 1. A value of 0 is the default and means playling the whole list, a negative value means showing of the list of titles with their numbers&#8230;</p>
<dt><code>&#8211;continue</p>
<dd> Enable playlist continuation mode. This changes frame skipping to apply only to the first track and also continues to play following tracks in playlist after the selected one. Also, the option to play a number of frames only applies to the whole playlist. Basically, this tries to treat the playlist more like one big stream (like, an audio book). The current track number in list (1-based) and frame number (0-based) are printed at exit (useful if you interrupted playback and want to continue later). Note that the continuation info is printed to standard output unless the switch for piping audio data to standard out is used. Also, it really makes sense to work with actual playlist files instead of lists of file names as arguments, to keep track positions consistent.</p>
<dt>&#8211;loop </code><i>times</i></p>
<dd> for looping track(s) a certain number of times, &lt; 0 means infinite loop (not with &#8211;random!).</p>
<dt><code>&#8211;keep-open</code></p>
<dd> For remote control mode: Keep loaded file open after reaching end.</p>
<dt><code>&#8211;timeout </code><i>seconds</i></p>
<dd> Timeout in (integer) seconds before declaring a stream dead (if &lt;= 0, wait forever).</p>
<dt><code>-z</code>, <code>&#8211;shuffle</code></p>
<dd> Shuffle play. Randomly shuffles the order of files specified on the command line, or in the list file.</p>
<dt><code>-Z</code>, <code>&#8211;random</code></p>
<dd> Continuous random play. Keeps picking a random file from the command line or the play list. Unlike shuffle play above, random play never ends, and plays individual songs more than once.</p>
<dt><code>&#8211;no-icy-meta</p>
<dd> Do not accept ICY meta data.</p>
<dt>-i, &#8211;index</p>
<dd> Index / scan through the track before playback. This fills the index table for seeking (if enabled in libmpg123) and may make the operating system cache the file contents for smoother operating on playback.</p>
<dt>&#8211;index-size </code><i>size</i></p>
<dd> Set the number of entries in the seek frame index table.</p>
<dt><code>&#8211;preframes </code><i>num</i></p>
<dd> Set the number of frames to be read as lead-in before a seeked-to position. This serves to fill the layer 3 bit reservoir, which is needed to faithfully reproduce a certain sample at a certain position. Note that for layer 3, a minimum of 1 is enforced (because of frame overlap), and for layer 1 and 2, this is limited to 2 (no bit reservoir in that case, but engine spin-up anyway). </p>
</dl>
<h2>OUTPUT and PROCESSING OPTIONS</h2>
<dl>
<dt><code>-o </code><i>module</i>, &#8211;output <i>module</i></p>
<dd> Select audio output module. You can provide a comma-separated list to use the first one that works.</p>
<dt><code>&#8211;list-modules</p>
<dd> List the available modules.</p>
<dt>-a </code><i>dev</i>, <code>&#8211;audiodevice </code><i>dev</p>
<dd> Specify the audio device to use. The default is system-dependent (usually /dev/audio or /dev/dsp). Use this option if you have multiple audio devices and the default is not what you want.</p>
<dt></i><code>-s</code>, <code>&#8211;stdout</code></p>
<dd> The decoded audio samples are written to standard output, instead of playing them through the audio device. This option must be used if your audio hardware is not supported by <code>mpg123</code>. The output format per default is raw (headerless) linear PCM audio data, 16 bit, stereo, host byte order (you can force mono or 8bit).</p>
<dt><code>-O </code><i>file</i>, <code>&#8211;outfile</p>
<dd> Write raw output into a file (instead of simply redirecting standard output to a file with the shell).</p>
<dt>-w </code><i>file</i>, <code>&#8211;wav</p>
<dd> Write output as WAV file. This will cause the MPEG stream to be decoded and saved as file </code><i>file</i> , or standard output if <i>&#8211;</i> is used as file name. You can also use <i>&#8211;au</i> and <i>&#8211;cdr</i> for AU and CDR format, respectively. Note that WAV/AU writing to non-seekable files, or redirected stdout, needs some thought. Since 1.16.0, the logic changed to writing the header with the first actual data. This avoids spurious WAV headers in a pipe, for example. The result of decoding nothing to WAV/AU is a file consisting just of the header when it is seekable and really nothing when not (not even a header). Correctly writing data with prophetic headers to stdout is no easy business.</p>
<dt><code>&#8211;au </code><i>file</p>
<dd> Does not play the MPEG file but writes it to file</i> in SUN audio format. If &#8211; is used as the filename, the AU file is written to stdout. See paragraph about WAV writing for header fun with non-seekable streams.</p>
<dt><code>&#8211;cdr </code><i>file</p>
<dd> Does not play the MPEG file but writes it to file</i> as a CDR file. If &#8211; is used as the filename, the CDR file is written to stdout.</p>
<dt><code>&#8211;reopen</code></p>
<dd> Forces reopen of the audiodevice after ever song</p>
<dt><code>&#8211;cpu&nbsp;</code><i>decoder-type</i></p>
<dd> Selects a certain decoder (optimized for specific CPU), for example i586 or MMX. The list of available decoders can vary; depending on the build and what your CPU supports. This options is only availabe when the build actually includes several optimized decoders.</p>
<dt><code>&#8211;test-cpu</code></p>
<dd> Tests your CPU and prints a list of possible choices for &#8211;cpu.</p>
<dt><code>&#8211;list-cpu</code></p>
<dd> Lists all available decoder choices, regardless of support by your CPU.</p>
<dt><code>-g </code><i>gain</i>, <code>&#8211;gain </code><i>gain</p>
<dd> [DEPRECATED] Set audio hardware output gain (default: don&#8217;t change). The unit of the gain value is hardware and output module dependent. (This parameter is only provided for backwards compatibility and may be removed in the future without prior notice. Use the audio player for playing and a mixer app for mixing, UNIX style!)</p>
<dt></i><code>-f </code><i>factor</i>, <code>&#8211;scale </code><i>factor</p>
<dd> Change scale factor (default: 32768).</p>
<dt></i><code>&#8211;rva-mix, &#8211;rva-radio</code></p>
<dd> Enable RVA (relative volume adjustment) using the values stored for ReplayGain radio mode / mix mode with all tracks roughly equal loudness. The first valid information found in ID3V2 Tags (Comment named RVA or the RVA2 frame) or ReplayGain header in Lame/Info Tag is used.</p>
<dt><code>&#8211;rva-album, &#8211;rva-audiophile</code></p>
<dd> Enable RVA (relative volume adjustment) using the values stored for ReplayGain audiophile mode / album mode with usually the effect of adjusting album loudness but keeping relative loudness inside album. The first valid information found in ID3V2 Tags (Comment named RVA_ALBUM or the RVA2 frame) or ReplayGain header in Lame/Info Tag is used.</p>
<dt><code>-0</code>, <code>&#8211;single0</code>; <code>-1</code>, <code>&#8211;single1</code></p>
<dd> Decode only channel 0 (left) or channel 1 (right), respectively. These options are available for stereo MPEG streams only.</p>
<dt><code>-m</code>, <code>&#8211;mono</code>, <code>&#8211;mix</code>, <code>&#8211;singlemix</code></p>
<dd> Mix both channels / decode mono. It takes less CPU time than full stereo decoding.</p>
<dt><code>&#8211;stereo</code></p>
<dd> Force stereo output</p>
<dt><code>-r </code><i>rate</i>, <code>&#8211;rate </code><i>rate</p>
<dd> Set sample rate (default: automatic). You may want to change this if you need a constant bitrate independent of the mpeg stream rate. mpg123 automagically converts the rate. You should then combine this with &#8211;stereo or &#8211;mono.</p>
<dt></i><code>-2</code>, <code>&#8211;2to1</code>; <code>-4</code>, <code>&#8211;4to1</code></p>
<dd> Performs a downsampling of ratio 2:1 (22 kHz) or 4:1 (11 kHz) on the output stream, respectively. Saves some CPU cycles, but at least the 4:1 ratio sounds ugly.</p>
<dt><code>&#8211;pitch&nbsp;</code><i>value</i></p>
<dd> Set hardware pitch (speedup/down, 0 is neutral; 0.05 is 5%). This changes the output sampling rate, so it only works in the range your audio system/hardware supports.</p>
<dt><code>&#8211;8bit</code></p>
<dd> Forces 8bit output</p>
<dt><code>&#8211;float</p>
<dd> Forces f32 encoding</p>
<dt>-e </code><i>enc</i>, <code>&#8211;encoding </code><i>enc</p>
<dd> Choose output sample encoding. Possible values look like f32 (32-bit floating point), s32 (32-bit signed integer), u32 (32-bit unsigned integer) and the variants with different numbers of bits (s24, u24, s16, u16, s8, u8) and also special variants like ulaw and alaw 8-bit. See the output of mpg123&#8217;s longhelp for actually available encodings.</p>
<dt></i><code>-d </code><i>n</i>, <code>&#8211;doublespeed </code><i>n</p>
<dd> Only play every n</i>&#8216;th frame. This will cause the MPEG stream to be played <i>n</i> times faster, which can be used for special effects. Can also be combined with the <code>&#8211;halfspeed</code> option to play 3 out of 4 frames etc. Don&#8217;t expect great sound quality when using this option.</p>
<dt><code>-h </code><i>n</i>, <code>&#8211;halfspeed </code><i>n</p>
<dd> Play each frame n</i> times. This will cause the MPEG stream to be played at <i>1</i>/<i>n</i>&#8216;th speed (n times slower), which can be used for special effects. Can also be combined with the <code>&#8211;doublespeed</code> option to double every third frame or things like that. Don&#8217;t expect great sound quality when using this option.</p>
<dt><code>-E </code><i>file</i>, <code>&#8211;equalizer</p>
<dd> Enables equalization, taken from </code><i>file</i>. The file needs to contain 32 lines of data, additional comment lines may be prefixed with <i>#</i>. Each data line consists of two floating-point entries, separated by whitespace. They specify the multipliers for left and right channel of a certain frequency band, respectively. The first line corresponds to the lowest, the 32nd to the highest frequency band. Note that you can control the equalizer interactively with the generic control interface.</p>
<dt><code>&#8211;gapless</p>
<dd> Enable code that cuts (junk) samples at beginning and end of tracks, enabling gapless transitions between MPEG files when encoder padding and codec delays would prevent it. This is enabled per default beginning with mpg123 version 1.0.0 .</p>
<dt>&#8211;no-gapless</p>
<dd> Disable the gapless code. That gives you MP3 decodings that include encoder delay and padding plus mpg123&#8217;s decoder delay.</p>
<dt>&#8211;no-infoframe</p>
<dd> Do not parse the Xing/Lame/VBR/Info frame, decode it instead just like a stupid old MP3 hardware player. This implies disabling of gapless playback as the necessary information is in said metadata frame.</p>
<dt>-D </code><i>n</i>, <code>&#8211;delay </code><i>n</p>
<dd> Insert a delay of n</i> seconds before each track.</p>
<dt><code>-o h</code>, <code>&#8211;headphones</code></p>
<dd> Direct audio output to the headphone connector (some hardware only; AIX, HP, SUN).</p>
<dt><code>-o s</code>, <code>&#8211;speaker</code></p>
<dd> Direct audio output to the speaker (some hardware only; AIX, HP, SUN).</p>
<dt><code>-o l</code>, <code>&#8211;lineout</code></p>
<dd> Direct audio output to the line-out connector (some hardware only; AIX, HP, SUN).</p>
<dt><code>-b </code><i>size</i>, <code>&#8211;buffer </code><i>size</p>
<dd> Use an audio output buffer of size</i> Kbytes. This is useful to bypass short periods of heavy system activity, which would normally cause the audio output to be interrupted. You should specify a buffer size of at least 1024 (i.e. 1 Mb, which equals about 6 seconds of audio data) or more; less than about 300 does not make much sense. The default is 0, which turns buffering off.</p>
<dt><code>&#8211;preload </code><i>fraction</p>
<dd> Wait for the buffer to be filled to fraction</i> before starting playback (fraction between 0 and 1). You can tune this prebuffering to either get faster sound to your ears or safer uninterrupted web radio. Default is 0.2 (wait for 20 % of buffer to be full, changed from 1 in version 1.23).</p>
<dt><code>&#8211;devbuffer </code><i>seconds</p>
<dd> Set device buffer in seconds; &lt;= 0 means default value. This is the small buffer between the application and the audio backend, possibly directly related to hardware buffers.</p>
<dt></i><code>&#8211;smooth</p>
<dd> Keep buffer over track boundaries &#8212; meaning, do not empty the buffer between tracks for possibly some added smoothness. </p>
</dl>
<p> </code></p>
<h2>MISC OPTIONS</h2>
<dl>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> Test mode. The audio stream is decoded, but no output occurs.</p>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> Check for filter range violations (clipping), and report them for each frame if any occur.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Increase the verbosity level. For example, displays the frame numbers during decoding.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Quiet. Suppress diagnostic messages.</p>
<dt><code>-C</code>, <code>&#8211;control</code></p>
<dd> Enable terminal control keys. This is enabled automatically if a terminal is detected. By default use &#8216;s&#8217; or the space bar to stop/restart (pause, unpause) playback, &#8216;f&#8217; to jump forward to the next song, &#8216;b&#8217; to jump back to the beginning of the song, &#8216;,&#8217; to rewind, &#8216;.&#8217; to fast forward, and &#8216;q&#8217; to quit. Type &#8216;h&#8217; for a full list of available controls.</p>
<dt><code>&#8211;no-control</p>
<dd> Disable terminal control even if terminal is detected.</p>
<dt>&#8211;title</p>
<dd> In an xterm, rxvt, screen, iris-ansi (compatible, TERM environment variable is examined), change the window&#8217;s title to the name of song currently playing.</p>
<dt>&#8211;name </code><i>name</p>
<dd> Set the name of this instance, possibly used in various places. This sets the client name for JACK output.</p>
<dt></i><code>&#8211;long-tag</p>
<dd> Display ID3 tag info always in long format with one line per item (artist, title, &#8230;)</p>
<dt>&#8211;utf8</code></p>
<dd> Regardless of environment, print metadata in UTF-8 (otherwise, when not using UTF-8 locale, you&#8217;ll get ASCII stripdown).</p>
<dt><code>-R</code>, <code>&#8211;remote</code></p>
<dd> Activate generic control interface. <code>mpg123</code> will then read and execute commands from stdin. Basic usage is &#8220;load &lt;filename&gt; &#8221; to play some file and the obvious &#8220;pause&#8221;, &#8220;command. &#8220;jump &lt;frame&gt;&#8221; will jump/seek to a given point (MPEG frame number). Issue &#8220;help&#8221; to get a full list of commands and syntax.</p>
<dt><code>&#8211;remote-err</code></p>
<dd> Print responses for generic control mode to standard error, not standard out. This is automatically triggered when using <code>-s</code> N.</p>
<dt><code>&#8211;fifo </code><i>path</p>
<dd> Create a fifo / named pipe on the given path and use that for reading commands instead of standard input.</p>
<dt></i><code>&#8211;aggressive</p>
<dd> Tries to get higher priority</p>
<dt>-T</code>, <code>&#8211;realtime</code></p>
<dd> Tries to gain realtime priority. This option usually requires root privileges to have any effect.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Shows short usage instructions.</p>
<dt><code>&#8211;longhelp</code></p>
<dd> Shows long usage instructions.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version string.</dl>
<h2>HTTP SUPPORT</h2>
<p> In addition to reading MPEG audio streams from ordinary files and from the standard input, <code>mpg123</code> supports retrieval of MPEG audio files or playlists via the HTTP protocol, which is used in the World Wide Web (WWW). Such files are specified using a so-called URL, which starts with &#8220;<a rel="nofollow" href="http://''.">http://&#8221;.</a> When a file with that prefix is encountered, <code>mpg123</code> attempts to open an HTTP connection to the server in order to retrieve that file to decode and play it. </p>
<p> It is often useful to retrieve files through a WWW cache or so-called proxy. To accomplish this, <code>mpg123</code> examines the environment for variables named <code>MP3_HTTP_PROXY</code>, <code>http_proxy</code> and <code>HTTP_PROXY</code>, in this order. The value of the first one that is set will be used as proxy specification. To override this, you can use the <code>-p</code> command line option (see the &#8220;OPTIONS&#8221; section). Specifying <code>-p none</code> will enforce contacting the server directly without using any proxy, even if one of the above environment variables is set. </p>
<p> Note that, in order to play MPEG audio files from a WWW server, it is necessary that the connection to that server is fast enough. For example, a 128 kbit/s MPEG file requires the network connection to be at least 128 kbit/s (16 kbyte/s) plus protocol overhead. If you suffer from short network outages, you should try the <code>-b</code> option (buffer) to bypass such outages. If your network connection is generally not fast enough to retrieve MPEG audio files in realtime, you can first download the files to your local harddisk (e.g. using <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1)) and then play them from there. </p>
<p> If authentication is needed to access the file it can be specified with the <code>-u user:pass.</code></p>
<h2>INTERRUPT</h2>
<p> When in terminal control mode, you can quit via pressing the q key, while any time you can abort <code>mpg123</code> by pressing Ctrl-C. If not in terminal control mode, this will skip to the next file (if any). If you want to abort playing immediately in that case, press Ctrl-C twice in short succession (within about one second). </p>
<p> Note that the result of quitting <code>mpg123</code> pressing Ctrl-C might not be audible immediately, due to audio data buffering in the audio device. This delay is system dependent, but it is usually not more than one or two seconds. </p>
<h2>PLAYBACK STATUS LINE</h2>
<p> In verbose mode, mpg123 updates a line with various information centering around the current playback position. On any decent terminal, the line also works as a progress bar in the current file by reversing video for a fraction of the line according to the current position. An example for a full line is this: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&gt; 0291+0955 00:01.68+00:28.22 [00:05.30] mix 100=085 192 kb/s 576 B acc 18 clip p+0.014</p>
<p> The information consists of, in order:</p>
<dl>
<dt><code>&gt;</code></p>
<dd> single-character playback state (&#8220;&gt;&#8221; for playing, &#8220;=&#8221; for pausing/looping, &#8220;_&#8221; for stopped)</p>
<dt><code>0291+0955</code></p>
<dd> current frame offset and number of remaining frames after the plus sign</p>
<dt><code>00:01.68+00:28.22</code></p>
<dd> current position from and remaining time in human terms (hours, minutes, seconds)</p>
<dt><code>[00:05.30]</code></p>
<dd> fill of the output buffer in terms of playback time, if the buffer is enabled</p>
<dt><code>mix</code></p>
<dd> selected RVA mode (possible values: mix, alb (album), and &#8212; (neutral, off))</p>
<dt><code>100=085</code></p>
<dd> set volume and the RVA-modified effective volume after the equal sign</p>
<dt><code>192 kb/s</code></p>
<dd> current bitrate</p>
<dt><code>576 B</code></p>
<dd> size of current frame in bytes</p>
<dt><code>acc</code></p>
<dd> if positions are accurate, possible values are &#8220;acc&#8221; for accurate positions or &#8220;fuz&#8221; for fuzzy (with guessed byte offsets using mean frame size)</p>
<dt><code>18 clip</code></p>
<dd> amount of clipped samples, non-zero only if decoder reports that (generic does, some optimized ones not)</p>
<dt><code>p+0.014</code></p>
<dd> pitch change (increased/decreased playback sampling rate on user request) </p>
</dl>
<h2>NOTES</h2>
<p> MPEG audio decoding requires a good deal of CPU performance, especially layer-3. To decode it in realtime, you should have at least an i486DX4, Pentium, Alpha, SuperSparc or equivalent processor. You can also use the <code>-m</code> option to decode mono only, which reduces the CPU load somewhat for layer-3 streams. See also the <code>-2</code> and <code>-4</code> options. </p>
<p> If everything else fails, have mpg123 decode to a file and then use an appropriate utility to play that file with less CPU load. Most probably you can configure mpg123 to produce a format suitable for your audio device (see above about encodings and sampling rates). </p>
<p> If your system is generally fast enough to decode in realtime, but there are sometimes periods of heavy system load (such as cronjobs, users logging in remotely, starting of &#8220;big&#8221; programs etc.) causing the audio output to be interrupted, then you should use the <code>-b</code> option to use a buffer of reasonable size (at least 1000 Kbytes).</p>
<h2>BUGS</h2>
<p> Mostly MPEG-1 layer 2 and 3 are tested in real life. Please report any issues and provide test files to help fixing them. </p>
<p> No CRC error checking is performed. </p>
<p> Some platforms lack audio hardware support; you may be able to use the <code>-s</code> switch to feed the decoded data to a program that can play it on your audio device.</p>
<h2>AUTHORS</h2>
<dl>
<dt>Maintainer:</p>
<dd>
 Thomas Orgis &lt;maintainer [at] mpg123.org&gt;, &lt;thomas [at] orgis.org&gt;</p>
<dt>Original Creator:</p>
<dd>
 Michael Hipp</dl>
<p> Uses code or ideas from various people, see the AUTHORS file accompanying the source code.</p>
<h2>LICENSE</h2>
<p> <code>mpg123</code> is licensed under the GNU Lesser/Library General Public License, LGPL, version 2.1 .</p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.mpg123.org">http://www.mpg123.org</a><br />
 <a rel="nofollow" href="http://sourceforge.net/projects/mpg123">http://sourceforge.net/projects/mpg123</a> </p>
<h2>Index</h2>
