---
title: "xine(1)"
name: "xine"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xine/"
description: "xine – a free video player"
---

<h2 class="name">NAME</h2>
<p> xine &#8211; a free video player </p>
<h2>SYNOPSIS</h2>
<p> <code>xine</code> <i>[options] [MRL] &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>xine</code> audio/video player. </p>
<p> <code>xine</code> plays MPEG system (audio and video) streams, mpeg elementary streams (e.g. .mp3 or .mpv files), mpeg transport streams, ogg files, avi files, asf files, quicktime files, (S)VCDs and DVDs and many more.</p>
<h2>OPTIONS</h2>
<p> The programs follow the usual GNU command line syntax, with long options starting with two dashes (`&#8211;&#8216;). A summary of options are included below. For a complete description, see <i>README</i> and <i>FAQ</i> in <i>/usr/share/doc/xine-ui-0.99.9</i> or on the xine home page.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options and available output drivers (plugins).</p>
<dt><code>&#8211;verbose</code><i>[=level]</i></p>
<dd> Set verbose level.</p>
<dt><code>-c, &#8211;config&nbsp;<wbr></code><i>&lt;file&gt;</i></p>
<dd> Use <code>config</code> file instead of default one.</p>
<dt><code>-a, &#8211;audio-channel&nbsp;<wbr></code><i>&lt;num&gt;</i></p>
<dd> Select the given audio channel. <i>&lt;num&gt;</i> is the audio channel number, default is <code>0</code>.<br />
 xine 0.5 and newer tries its best to collect all valid audio channels (ac3, mpeg audio, avi audio, &#8230;) from the stream and maps them to &quot;virtual channels&quot; with channel numbers starting at <code>0</code>.</p>
<dt><code>-V, &#8211;video-driver&nbsp;<wbr></code><i>&lt;drv&gt;</i></p>
<dd> Select video driver. Check out <i>xine &#8211;help</i> for a list of available video output plugins on your system. This selection is stored automatically in your <i>~/.xine/config</i> so you&#8217;ll have to specify the video driver only once.</p>
<dt><code>-A, &#8211;audio-driver&nbsp;<wbr></code><i>&lt;drv&gt;</i></p>
<dd> Select audio driver. Check out <i>xine &#8211;help</i> for a list of available audio output plugins on your system. This selection is stored automatically in your <i>~/.xine/config</i> so you&#8217;ll have to specify the audio driver only once.</p>
<dt><code>-u, &#8211;spu-channel&nbsp;<wbr></code><i>&lt;num&gt;</i></p>
<dd> Select subpicture (subtitle) channel. <i>&lt;num&gt;</i> is the subpicture channel id, default is no subtitle (<code>-1</code>).</p>
<dt><code>-p, &#8211;auto-play=</code><i>[f][F][h][w][q][d][v]</i></p>
<dd> Start playing immediately after start. Can be followed by:<br />
 `<i>f</i>&#8216; in fullscreen mode,<br />
 `<i>F</i>&#8216; in xinerama fullscreen mode,<br />
 `<i>h</i>&#8216; hide GUI (main panel, etc&#8230;),<br />
 `<i>w</i>&#8216; hide video output window,<br />
 `<i>q</i>&#8216; for quitting after playback,<br />
 It is also possible to request the playlist from DVD `<i>d</i>&#8216;, or VCD `<i>v</i>&#8216;. There is now a more generic option, <i>&#8211;auto-scan</i>, for that (see below).</p>
<dt><code>-s, &#8211;auto-scan&nbsp;<wbr></code><i>&lt;plugin&gt;</i></p>
<dd> Auto-scan playlist from named input plugin. Many plugins allow to read a default playlist, in order to play <code>everything</code>. This works fine for DVDs or VCDs, for example. Giving this option has the same effect as pressing the according button on xine&#8217;s main panel. </p>
<p> This option is especially useful in combination with auto-play. You could start <i>xine~&#8211;auto-play~&#8211;auto-scan~dvd</i> in order to play a whole DVD without having to press any additional buttons. This also works for plugins that are not supplied with xine, just give the name of the button that the desired plugin adds to the xine panel!</p>
<dt><code>-f, &#8211;fullscreen</code></p>
<dd> Switch xine to fullscreen mode on start (just like pressing `<code>f</code>&#8216;)</p>
<dt><code>-F, &#8211;xineramafull</code></p>
<dd> Switch xine to xinerama fullscreen mode on start (just like pressing `<code>F</code>&#8216;). That is to say, try to expand display on several screens. Screens to use are defined in config file.</p>
<dt><code>-g, &#8211;hide-gui</code></p>
<dd> Hide all GUI windows (except the video window) on start. This is the same as pressing `<code>G</code>&#8216; within xine.</p>
<dt><code>-H, &#8211;hide-video</code></p>
<dd> Hide video output window.</p>
<dt><code>-L, &#8211;no-lirc</code></p>
<dd> Turn off LIRC support. This option is <i>only~available</i> if xine has been compiled with LIRC support.</p>
<dt><code>&#8211;visual&nbsp;<wbr></code><i>&lt;visual-class-or-id&gt;</i></p>
<dd> Try to use a specific X11 server visual for xine windows. The <i>&lt;visual-class-or-id&gt;</i> parameter is either the name of an X11 visual class (<code>StaticGray</code>, <code>GrayScale</code>, <code>StaticColor</code>, <code>PseudoColor</code>, <code>TrueColor</code> or <code>DirectColor</code>) or the <code>hexadecimal</code> value for a specific X11 visual. </p>
<p> When used with a visual class name, xine tries to find such a visual with depth <code>15</code> or <code>16</code>, <code>24</code>, <code>32</code> or <code>8</code> (in that order). The default visual class used by xine in absence of a <i>&#8211;visual</i> option is <code>TrueColor</code>. </p>
<p> If no usable visual is found, xine falls back to the default visual used on the X11 server&#8217;s root window.</p>
<dt><code>&#8211;install</code></p>
<dd> When using an X11 visual with changeable colors (colormaps), install a private colormap for xine. With a private colormap, xine can allocate more colors so that video output may look better.</p>
<dt><code>&#8211;keymap&nbsp;<wbr></code><i>[=option]</i></p>
<dd> Display keymap. Option are:<br />
 `<code>default</code>&#8216; display default keymap table,<br />
 `<code>lirc</code>&#8216; display draft of a <i>~/.lircrc</i> config file,<br />
 `<code>remapped</code>&#8216; user remapped keymap table,<br />
 `<code>file:&lt;file&gt;</code>&#8216; use <code>file</code> as keymap table,<br />
 If no option is given, `<code>default</code>&#8216; is selected.</p>
<dt><code>-n, &#8211;network</code></p>
<dd> Enable network remote control server. To use network remote control server, a password file is required. If xine cannot find it, the server is stopped. The syntax of the password file follows the (familiar) scheme &lt;<i>identification</i>&gt;:&lt;<i>password</i>&gt;. Since cryptography is subject to legal issues in some countries, the password is not encrypted and also transmitted unencrypted, so take care with remote connections. Two (optional) generic rules are available as well (one at a time) </p>
<pre>
<code>ALL:ALLOW</code> or <code>ALL:DENY</code>
</pre>
<p> In the first case, all clients are allowed to execute all available commands, without restriction. In the second case, no-one is allowed to execute any commands, except identified users (using &#8216;identify&#8217; command). </p>
<p> If a password entry begins with an asterisk `<code>*</code>&#8216;, the user is blocked. If a password entry is empty, the full entry is ignored. Here is an example of a small <i>~/.xine/passwd</i> file: </p>
<pre>
ALL:DENY
daniel:mypasswd
foo:*
</pre>
<p> This will allow only &#8216;daniel&#8217; to execute commands, after a successfully identifying stage. </p>
<p> The default port of the server is <code>6789</code>, this number is totally arbitrary. You can connect the server using a simple <i>telnet</i> command: </p>
<pre>
<code>telnet~localhost~6789</code>
</pre>
<p> To change the default port, you can (as root) edit your <i>/etc/services</i>, and add an entry like this: </p>
<pre>
xinectl    7890/tcp        # xine control
</pre>
<p> This will change the default port from 6789 to 7890, and create a &quot;human&quot; service called <i>xinectl</i>. </p>
<p> The server itself offers command help/syntax:<br />
 <code>help&nbsp;<wbr></code><i>[command]</i><br />
 Without <i>command</i> specified, all available commands will be displayed. If a command is specified, short text about the command functionality will be given.<br />
 <code>syntax&nbsp;<wbr></code><i>&lt;command&gt;</i><br />
 Display the <i>command</i> syntax.</p>
<dt><code>-R, &#8211;root</code></p>
<dd> Use root window as video window.</p>
<dt><code>-G, &#8211;geometry&nbsp;<wbr></code><i>&lt;WxH[+X+Y]&gt;</i></p>
<dd> You can set video output size and position using the X like geometry (see <code><a href="/docs/linux/man/7-x/">X</a></code>(7)). <code>X</code> and <code>Y</code> offset are optional.</p>
<dt><code>-B, &#8211;borderless</code></p>
<dd> Remove borders of video output window, in windowed mode.</p>
<dt><code>-N, &#8211;animation&nbsp;<wbr></code><i>&lt;mrl&gt;</i></p>
<dd> Specify one or more mrl to play with audio only streams.</p>
<dt><code>-P, &#8211;playlist&nbsp;<wbr></code><i>&lt;filename&gt;</i></p>
<dd> Use file as playlist. Known formats are: asx, toxine, m3u, pls, sfv and raw text file.</p>
<dt><code>-l, &#8211;loop&nbsp;<wbr></code><i>[=mode]</i></p>
<dd> Set playlist loop mode. If mode isn&#8217;t specified, mode <code>loop</code> is used. Possible modes are:<br />
 <code>loop</code>: loop entire playlist.<br />
 <code>repeat</code>: repeat current playlist entry.<br />
 <code>shuffle</code>: select randomly an entry in playlist from those not yet played.<br />
 <code>shuffle+</code>: same as shuffle, but indefinitely replay the playlist.</p>
<dt><code>&#8211;skin-server-url&nbsp;<wbr></code><i>&lt;url&gt;</i></p>
<dd> Define the skin server url.</p>
<dt><code>&#8211;enqueue&nbsp;<wbr></code><i>&lt;mrl&gt;</i><code>&#8230;</code></p>
<dd>
 Enqueue one or more mrl in a running session (session 0).<br />
 If you want to specify another session, use <code>-S session=</code><i>x</i> option.</p>
<dt><code>-S, &#8211;session&nbsp;<wbr></code><i>&lt;option1,option2,&#8230;&gt;</i></p>
<dd>
 Session managements. All options can be used more than one time, except <code>session</code>.<br />
 Options are:<br />
 <code>session=</code><i>n</i> specify session &lt;<i>n</i>&gt; number,<br />
 <code>mrl=</code><i>m</i> add mrl &lt;<i>m</i>&gt; to the playlist,<br />
 <code>audio=</code><i>c</i> select audio channel (&lt;<i>c</i>&gt;: <code>next</code> or <code>prev</code>),<br />
 <code>spu=</code><i>c</i> select spu channel (&lt;<i>c</i>&gt;: <code>next</code> or <code>prev</code>),<br />
 <code>volume=</code><i>v</i> set audio volume (&lt;<i>v</i>&gt;: 0 to 100),<br />
 <code>amp=</code><i>v</i> set audio amplification of instance (&lt;<i>v</i>&gt;: 0 to 200),<br />
 <code>loop=</code><i>m</i> set loop mode (&lt;<i>m</i>&gt;: <code>none</code> <code>loop</code> <code>repeat</code> <code>shuffle</code> or <code>shuffle+</code>),<br />
 <code>get_speed</code> get current speed status. Return values are:<br />
&nbsp;<wbr>&#8211; 1: error<br />
&nbsp;<wbr>&#8211; 2: stop<br />
&nbsp;<wbr>&#8211; 3: play<br />
&nbsp;<wbr>&#8211; 4: pause<br />
&nbsp;<wbr>&#8211; 5: slow4<br />
&nbsp;<wbr>&#8211; 6: slow2<br />
&nbsp;<wbr>&#8211; 7: fast2<br />
&nbsp;<wbr>&#8211; 8: fast4<br />
 <code>get_time[=p|pos]</code> get current position status in seconds, or in position in stream (0..65535).<br />
 (<code>playlist</code>|<code>pl</code>)<code>=</code><i>p</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;<i>p</i>&gt;&nbsp;<wbr>can be: </p>
<p>&nbsp;<wbr><code>clear</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>clear the playlist,<br />
&nbsp;<wbr><code>first</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>play first entry in the playlist,<br />
&nbsp;<wbr><code>prev</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>play previous playlist entry,<br />
&nbsp;<wbr><code>next</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>play next playlist entry,<br />
&nbsp;<wbr><code>last</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>play last entry in the playlist,<br />
&nbsp;<wbr><code>load:</code><i>s</i>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>load playlist file&nbsp;<wbr>&lt;<i>s</i>&gt;,<br />
&nbsp;<wbr><code>stop</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>stop playback at the end of the current playback,<br />
&nbsp;<wbr><code>cont</code>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>continue playback at the end of current playback.<br />
 There are also some self explanatory options.<br />
&nbsp;<wbr><code>play</code>,&nbsp;<wbr><code>slow2</code>,&nbsp;<wbr><code>slow4</code>,&nbsp;<wbr><code>pause</code>,&nbsp;<wbr><code>fast2</code>,&nbsp;<wbr><code>fast4</code>,&nbsp;<wbr><code>stop</code>,&nbsp;<wbr><code>quit</code>,&nbsp;<wbr><code>fullscreen</code>,&nbsp;<wbr><code>eject</code>.</p>
<dt><code>-Z</code></p>
<dd> Don&#8217;t automatically start playback, affect only auto-start when smart mode is used.</p>
<dt><code>-D, &#8211;deinterlace&nbsp;<wbr></code><i>[post[:..][;]]</i></p>
<dd> Deinterlace video output. You can override configuration option of post(s) used to deinterlace the output picture. See <i>&#8211;post</i> for syntax.</p>
<dt><code>-r, &#8211;aspect-ratio&nbsp;<wbr></code><i>&lt;mode&gt;</i></p>
<dd> Set aspect ratio of video output. &lt;<i>mode</i>&gt; can be: <code>auto</code>, <code>square</code>, <code>4:3</code>, <code>anamorphic</code>, <code>dvb</code>.</p>
<dt><code>&#8211;broadcast-port&nbsp;<wbr></code><i>&lt;port&gt;</i></p>
<dd> Set port of xine broadcaster (master side), slave is started with &#8216;xine <a href="slave://address:port'">slave://address:port&#8217;</a></p>
<dt><code>&#8211;no-logo</code></p>
<dd> Don&#8217;t display the logo.</p>
<dt><code>-E, &#8211;no-reload</code></p>
<dd> Don&#8217;t reload old playlist. Playlist is saved when you leave xine, then it is reloaded and played the next time you lanch xine. This feature can be disabled via setup window.</p>
<dt><code>&#8211;post&nbsp;<wbr></code><i>&lt;plugin&gt;[:parameter=value][,&#8230;][;&#8230;]</i></p>
<dd> Load one or more post plugin(s). Parameters are comma separated. This option can be used more than one time to chain two or more video postprocess plugins. You can specify two or more plugin, which may be separated by a semi-colon &#8216;;&#8217;.</p>
<dt><code>&#8211;disable-post</code></p>
<dd> Don&#8217;t enable post plugin(s). This way, you can specify one more plugin to use, using the &#8211;post command line option, but don&#8217;t enable those effects.</p>
<dt><code>&#8211;no-splash</code></p>
<dd> Don&#8217;t display the splash screen.</p>
<dt><code>&#8211;stdctl</code></p>
<dd> Turn on controlling xine over STDIN.</p>
<dt><code>-T, &#8211;tvout</code><i>&lt;backend&gt;</i></p>
<dd> Turn on TVout support. &lt;<i>backend</i>&gt; can be: nvtv, ati.</p>
<dt><code>&#8211;list-plugins</code><i>[=type]</i></p>
<dd> Display the list of available plugins. Optional &lt;<i>type</i>&gt; can be: audio_out, video_out, demux, input, sub, post, audio_decoder, video_decoder</p>
<dt><code>&#8211;bug-report</code><i>[=mrl]</i></p>
<dd> Enable bug report mode. This turns verbosity on, gathers all output messages and writes them to a file named BUG-REPORT.TXT. If &lt;<i>mrl</i>&gt; is given, xine will play that mrl then quit (like -pq does).
</dl>
<p> If you don&#8217;t specify any MRL, you&#8217;ll have to select a file by drag and drop. Dragging files from the <code>GNOME~Midnight~Commander</code> (gmc), <code>Nautilus</code> or <code>Konqueror</code> is known to work. </p>
<h2>MRL (media resource locator)</h2>
<p> MRLs are similar to URLs in your web browser. They describe the media to read from. <code><a href="/docs/linux/man/5-xine/">xine</a></code>(5) describes them in some detail. xine extends the syntax as follows:</p>
<dl>
<dt><code>&lt;mrl&gt;::&lt;subtitlefile&gt;</code></p>
<dd> This is the xine-ui specific way to define the subtitle file to use. The filename will be extracted by the frontend, that permit to change it, save it in a playlist, etc&#8230;
</dl>
<h2>STREAM OPTIONS</h2>
<p> After a delimiting <code>#</code> you can add several stream parameters:</p>
<dl>
<dt><code>novideo</code></p>
<dd> video will be ignored</p>
<dt><code>noaudio</code></p>
<dd> audio will be ignored</p>
<dt><code>nospu</code></p>
<dd> subpictures will be ignored</p>
<dt><code>demux:</code><i>&lt;demux name&gt;</i></p>
<dd> specify the demux plugin to use</p>
<dt><code>volume:</code><i>&lt;level&gt;</i></p>
<dd> set audio volume</p>
<dt><code>compression:</code><i>&lt;level&gt;</i></p>
<dd> set audio dynamic range compression</p>
<dt><code>&lt;config entry&gt;</code><i>:</i><code>&lt;config value&gt;</code></p>
<dd> assign a new value to any config entry</p>
<dt><code>change configuration option &#8216;on the fly&#8217;:</code></p>
<dd>
 You can change a configuration option at anytime, using the special cfg:/ mrl style. The syntax is:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cfg:/&lt;config entry&gt; : &lt;config value&gt;</p>
<p> Unlike stream config option, you can change anything <i>before</i> playing the stream.</dl>
<h2>CONTROL KEYS</h2>
<p> Many features can be controlled by pressing control keys. `<code>M-</code>&#8216; is the Meta key (`<code>Alt</code>&#8216; key on PC keyboard), `<code>C-</code>&#8216; is the Control `<code>CTRL</code>&#8216; key, other special keys are delimited by `<code>&lt;</code>&#8216; and `<code>&gt;</code>&#8216; characters, e.g. the `<code>HOME</code>&#8216; key is displayed as <code>&lt;home&gt;</code>. The default key bindings are:</p>
<dl>
<dt><code>&lt;Return&gt;</code></p>
<dd> Start playback</p>
<dt><code>&lt;space&gt;</code></p>
<dd> Playback pause toggle</p>
<dt><code>S</code></p>
<dd> Stop playback</p>
<dt><code>t</code></p>
<dd> Take a snapshot</p>
<dt><code>e</code></p>
<dd> Eject the current medium</p>
<dt><code>&lt;Next&gt;</code></p>
<dd> Select and play next MRL in the playlist</p>
<dt><code>&lt;Prior&gt;</code></p>
<dd> Select and play previous MRL in the playlist</p>
<dt><code>l</code></p>
<dd> Loop mode toggle</p>
<dt><code>C</code>&#8211;<code>s</code></p>
<dd> Scan playlist to grab stream infos</p>
<dt><code>C</code>&#8211;<code>a</code></p>
<dd> Add a mediamark from current playback</p>
<dt><code>C</code>&#8211;<code>e</code></p>
<dd> Edit selected mediamark</p>
<dt><code>&lt;Left&gt;</code></p>
<dd> Set position to -60 seconds in current stream</p>
<dt><code>&lt;Right&gt;</code></p>
<dd> Set position to +60 seconds in current stream</p>
<dt><code>M</code>&#8211;<code>&lt;Left&gt;</code></p>
<dd> Set position to -30 seconds in current stream</p>
<dt><code>M</code>&#8211;<code>&lt;Right&gt;</code></p>
<dd> Set position to +30 seconds in current stream</p>
<dt><code>C</code>&#8211;<code>&lt;Left&gt;</code></p>
<dd> Set position to -15 seconds in current stream</p>
<dt><code>C</code>&#8211;<code>&lt;Right&gt;</code></p>
<dd> Set position to +15 seconds in current stream</p>
<dt><code>M3</code>&#8211;<code>&lt;Left&gt;</code></p>
<dd> Set position to -7 seconds in current stream</p>
<dt><code>M3</code>&#8211;<code>&lt;Right&gt;</code></p>
<dd> Set position to +7 seconds in current stream</p>
<dt><code>C</code>&#8211;<code>0</code></p>
<dd> Set position to beginning of current stream</p>
<dt><code>C</code>&#8211;<code>1</code></p>
<dd> Set position to 10% of current stream</p>
<dt><code>C</code>&#8211;<code>2</code></p>
<dd> Set position to 20% of current stream</p>
<dt><code>C</code>&#8211;<code>3</code></p>
<dd> Set position to 30% of current stream</p>
<dt><code>C</code>&#8211;<code>4</code></p>
<dd> Set position to 40% of current stream</p>
<dt><code>C</code>&#8211;<code>5</code></p>
<dd> Set position to 50% of current stream</p>
<dt><code>C</code>&#8211;<code>6</code></p>
<dd> Set position to 60% of current stream</p>
<dt><code>C</code>&#8211;<code>7</code></p>
<dd> Set position to 70% of current stream</p>
<dt><code>C</code>&#8211;<code>8</code></p>
<dd> Set position to 80% of current stream</p>
<dt><code>C</code>&#8211;<code>9</code></p>
<dd> Set position to 90% of current stream</p>
<dt><code>&lt;Up&gt;</code></p>
<dd> Increment playback speed</p>
<dt><code>&lt;Down&gt;</code></p>
<dd> Decrement playback speed</p>
<dt><code>M</code>&#8211;<code>&lt;Down&gt;</code></p>
<dd> Reset playback speed</p>
<dt><code>V</code></p>
<dd> Increment audio volume</p>
<dt><code>v</code></p>
<dd> Decrement audio volume</p>
<dt><code>C</code>&#8211;<code>V</code></p>
<dd> Increment amplification level</p>
<dt><code>C</code>&#8211;<code>v</code></p>
<dd> Decrement amplification level</p>
<dt><code>C</code>&#8211;<code>A</code></p>
<dd> Reset amplification to default value</p>
<dt><code>C</code>&#8211;<code>m</code></p>
<dd> Audio muting toggle</p>
<dt><code>&lt;plus&gt;</code></p>
<dd> Select next audio channel</p>
<dt><code>&lt;minus&gt;</code></p>
<dd> Select previous audio channel</p>
<dt><code>&lt;period&gt;</code></p>
<dd> Select next sub picture (subtitle) channel</p>
<dt><code>&lt;comma&gt;</code></p>
<dd> Select previous sub picture (subtitle) channel</p>
<dt><code>i</code></p>
<dd> Interlaced mode toggle</p>
<dt><code>a</code></p>
<dd> Cycle aspect ratio values</p>
<dt><code>&lt;less&gt;</code></p>
<dd> Reduce the output window size by factor 1.2</p>
<dt><code>&lt;greater&gt;</code></p>
<dd> Enlarge the output window size by factor 1.2</p>
<dt><code>M</code>&#8211;<code>1</code></p>
<dd> Set video output window to 50%</p>
<dt><code>M</code>&#8211;<code>2</code></p>
<dd> Set video output window to 100%</p>
<dt><code>M</code>&#8211;<code>3</code></p>
<dd> Set video output window to 200%</p>
<dt><code>z</code></p>
<dd> Zoom in</p>
<dt><code>Z</code></p>
<dd> Zoom out</p>
<dt><code>C</code>&#8211;<code>z</code></p>
<dd> Zoom in horizontally</p>
<dt><code>C</code>&#8211;<code>Z</code></p>
<dd> Zoom out horizontally</p>
<dt><code>M</code>&#8211;<code>z</code></p>
<dd> Zoom in vertically</p>
<dt><code>M</code>&#8211;<code>Z</code></p>
<dd> Zoom out vertically</p>
<dt><code>C</code>&#8211;<code>M</code>&#8211;<code>z</code></p>
<dd> Reset zooming</p>
<dt><code>s</code></p>
<dd> Resize output window to stream size</p>
<dt><code>f</code></p>
<dd> Fullscreen toggle</p>
<dt><code>F</code></p>
<dd> Xinerama fullscreen toggle</p>
<dt><code>b</code></p>
<dd> Video window borders appearance toggle</p>
<dt><code>&lt;Escape&gt;</code></p>
<dd> Jump to media Menu</p>
<dt><code>&lt;F1&gt;</code></p>
<dd> Jump to Title Menu</p>
<dt><code>&lt;F2&gt;</code></p>
<dd> Jump to Root Menu</p>
<dt><code>&lt;F3&gt;</code></p>
<dd> Jump to Subpicture Menu</p>
<dt><code>&lt;F4&gt;</code></p>
<dd> Jump to Audio Menu</p>
<dt><code>&lt;F5&gt;</code></p>
<dd> Jump to Angle Menu</p>
<dt><code>&lt;F6&gt;</code></p>
<dd> Jump to Part Menu</p>
<dt><code>&lt;Keypad Up&gt;</code></p>
<dd> Menu navigate up</p>
<dt><code>&lt;Keypad Down&gt;</code></p>
<dd> Menu navigate down</p>
<dt><code>&lt;Keypad Left&gt;</code></p>
<dd> Menu navigate left</p>
<dt><code>&lt;Keypad Right&gt;</code></p>
<dd> Menu navigate right</p>
<dt><code>&lt;Keypad Enter&gt;</code></p>
<dd> Menu select</p>
<dt><code>&lt;Keypad Next&gt;</code></p>
<dd> Jump to next chapter</p>
<dt><code>&lt;Keypad Prior&gt;</code></p>
<dd> Jump to previous chapter</p>
<dt><code>&lt;Keypad Home&gt;</code></p>
<dd> Select next angle</p>
<dt><code>&lt;Keypad End&gt;</code></p>
<dd> Select previous angle</p>
<dt><code>M</code>&#8211;<code>h</code></p>
<dd> Visibility toggle of help window</p>
<dt><code>M</code>&#8211;<code>P</code></p>
<dd> Visibility toggle of video post effect window</p>
<dt><code>C</code>&#8211;<code>M</code>&#8211;<code>P</code></p>
<dd> Toggle post effect usage</p>
<dt><code>h</code></p>
<dd> Visibility toggle of output window</p>
<dt><code>g</code></p>
<dd> Visibility toggle of UI windows</p>
<dt><code>M</code>&#8211;<code>c</code></p>
<dd> Visibility toggle of control window</p>
<dt><code>M</code>&#8211;<code>m</code></p>
<dd> Visibility toggle of mrl browser window</p>
<dt><code>M</code>&#8211;<code>p</code></p>
<dd> Visibility toggle of playlist editor window</p>
<dt><code>M</code>&#8211;<code>s</code></p>
<dd> Visibility toggle of the setup window</p>
<dt><code>M</code>&#8211;<code>e</code></p>
<dd> Visibility toggle of the event sender window</p>
<dt><code>M</code>&#8211;<code>t</code></p>
<dd> Visibility toggle of analog TV window</p>
<dt><code>M</code>&#8211;<code>l</code></p>
<dd> Visibility toggle of log viewer</p>
<dt><code>M</code>&#8211;<code>i</code></p>
<dd> Visibility toggle of stream info window</p>
<dt><code>C</code>&#8211;<code>i</code></p>
<dd> Display stream information using OSD</p>
<dt><code>M</code>&#8211;<code>k</code></p>
<dd> Enter key binding editor</p>
<dt><code>C</code>&#8211;<code>o</code></p>
<dd> Open file selector</p>
<dt><code>C</code>&#8211;<code>S</code></p>
<dd> Select a subtitle file</p>
<dt><code>C</code>&#8211;<code>d</code></p>
<dd> Download a skin from the skin server</p>
<dt><code>C</code>&#8211;<code>t</code></p>
<dd> Display MRL/Ident toggle</p>
<dt><code>&lt;Insert&gt;</code></p>
<dd> Grab pointer toggle</p>
<dt><code>0</code></p>
<dd> Enter the number 0</p>
<dt><code>1</code></p>
<dd> Enter the number 1</p>
<dt><code>2</code></p>
<dd> Enter the number 2</p>
<dt><code>3</code></p>
<dd> Enter the number 3</p>
<dt><code>4</code></p>
<dd> Enter the number 4</p>
<dt><code>5</code></p>
<dd> Enter the number 5</p>
<dt><code>6</code></p>
<dd> Enter the number 6</p>
<dt><code>7</code></p>
<dd> Enter the number 7</p>
<dt><code>8</code></p>
<dd> Enter the number 8</p>
<dt><code>9</code></p>
<dd> Enter the number 9</p>
<dt><code>M3</code>&#8211;<code>&lt;plus&gt;</code></p>
<dd> Add 10 to the next entered number</p>
<dt><code>&lt;slash&gt;</code></p>
<dd> Set position in current stream to numeric percentage See the section on &quot;Numeric Input&quot; below.</p>
<dt><code>M</code>&#8211;<code>&lt;Up&gt;</code></p>
<dd> Set position forward by numeric argument in current stream</p>
<dt><code>M3</code>&#8211;<code>&lt;Up&gt;</code></p>
<dd> Set position back by numeric argument in current stream</p>
<dt><code>m</code></p>
<dd> Change audio video syncing (delay video)</p>
<dt><code>n</code></p>
<dd> Change audio video syncing (delay audio)</p>
<dt><code>&lt;Home&gt;</code></p>
<dd> Reset audio video syncing offset</p>
<dt><code>M</code></p>
<dd> Change subtitle syncing (delay video)</p>
<dt><code>N</code></p>
<dd> Change subtitle syncing (delay subtitles)</p>
<dt><code>C</code>&#8211;<code>M</code>&#8211;<code>o</code></p>
<dd> Toggle TV modes (on the DXR3)</p>
<dt><code>d</code></p>
<dd> Switch Monitor to DPMS standby mode</p>
<dt><code>C</code>&#8211;<code>l</code></p>
<dd> Stop playback after played stream</p>
<dt><code>q</code></p>
<dd> Quit the program
</dl>
<h3>Third party plugins</h3>
<p> Following shortcuts are used by third party plugins, generally for DVD navigation:</p>
<dl>
<dt><code>&lt;KeyPad Up&gt;</code></p>
<dd> Up event.</p>
<dt><code>&lt;KeyPad Down&gt;</code></p>
<dd> Down event.</p>
<dt><code>&lt;KeyPad Left&gt;</code></p>
<dd> Left event.</p>
<dt><code>&lt;KeyPad Right&gt;</code></p>
<dd> Right event.</p>
<dt><code>&lt;KeyPad Prior&gt;</code></p>
<dd> Prior event.</p>
<dt><code>&lt;KeyPad Next&gt;</code></p>
<dd> Next event.</p>
<dt><code>&lt;KeyPad End&gt;</code></p>
<dd> Previous angle event.</p>
<dt><code>&lt;KeyPad Home&gt;</code></p>
<dd> Next angle event.</p>
<dt><code>&lt;KeyPad Enter&gt;</code></p>
<dd> Select event </p>
</dl>
<h3>Synchronization fine tuning</h3>
<p> Some streams have bad timestamps, so synchronization fails. This can be tweaked using these keys:</p>
<dl>
<dt>n</p>
<dd> press if video lags behind audio</p>
<dt>m</p>
<dd> press if video runs ahead of audio</p>
<dt><code>&lt;home&gt;</code></p>
<dd> press to reset audio/video offset to <code>0</code>, so stream timestamps are unchanged. </p>
</dl>
<h3>Subtitle synchronization</h3>
<p> You can adjust subtitle synchronization by using these keys:</p>
<dl>
<dt>M / N</p>
<dd>
</dl>
<h3>Numeric Input</h3>
<p> You can specify a numeric argument to be applied to a command typing in a number and then entering a function key. For example entering &quot;99/&quot;, that is, the number-9 key twice and then the slash key, you should seek 99% of the current stream. </p>
<p> The new VCD/SVCD plugin allows some numeric input. Entering a number followed by the &quot;Select event&quot; (by default the keypad enter), one can go to a specific &quot;Chapter&quot; (track or entry) or selection number. As this is a relatively new feature, perhaps over time more plugins will make use of numeric selection. </p>
<p> Other commands that can be numeric prefaced by a numeric argument are next/previous MRL (<code>MRL_NEXT</code>, <code>MRL_PRIOR</code>), next/previous subtitle (<code>SPU_NEXT</code>, <code>SPU_PRIOR</code>), and next/previous audio channel (<code>AUDIOCHAN_NEXT</code>, <code>AUDIOCHAN_PRIOR</code>). With a numeric prefix, it is as though one entered that command the number of times. Here, the argument 0, since it would otherwise meaningless, is interpreted here to be 1 instead. </p>
<p> Admittedly the use of numeric input here is of limited value. Over time perhaps more useful commands like specifying a specific or absolute MRL, subtitle or audio channel number will be implemented. </p>
<h2>FILES</h2>
<dl>
<dt>~/.xine/config</p>
<dd> Main config file</p>
<dt>~/.xine/keymap</p>
<dd> Key bindings for xine-ui</p>
<dt>~/.xine/passwd</p>
<dd> Passwords file xine-ui</p>
<dt>~/.xine/xinerc</p>
<dd> Additional command line arguments<br />
 Each line specifies an additional command line argument (one argument per line): </p>
<pre>
--geometry 720x576+0+0
--network
-s DVD
-p
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xine-remote/">xine-remote</a></code>(1)<br />
 <code><a href="/docs/linux/man/5-xine/">xine</a></code>(5) for details of the MRL syntax </p>
<p> The programs are documented fully on the xine home page: <i><a rel="nofollow" href="http://www.xine-project.org/">http://www.xine-project.org/</a></i></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Siggi Langauf &lt;siggi [at] debian.org&gt;, for the xine project. Lots of additions by Guenter Bartsch &lt;guenter [at] users.sourceforge.net&gt;, Daniel Caujolle-Bert &lt;f1rmb [at] users.sourceforge.net&gt;, Rocky Bernstein &lt;rocky [at] panix.com&gt;, and Philipp Hahn &lt;pmhahn [at] users.sourceforge.net&gt;. </p>
<h2>Index</h2>
