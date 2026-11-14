---
title: "gpac(1)"
name: "gpac"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpac/"
description: "GPAC – MPEG-4 Systems Framework and Software Development Kit"
---

<h2>NAME</h2>
<p> GPAC<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; MPEG-4 Systems Framework and Software Development Kit</p>
<h2>DESCRIPTION</h2>
<p> GPAC stands (does it ?) for GPAC Project on Advanced Content. It is an implementation of the MPEG-4 Systems standard written in ANSI C. GPAC provides tools for media playback, vector graphics and 3D rendering, MPEG-4 authoring and distribution. This man page is about configuration of the GPAC framework version 0.5.0.</p>
<h2>INTRODUCTION</h2>
<p> Some applications in the GPAC framework use a configuration file shared among modules and reloadable at run time. This file is located in the user home directory and called &quot;.gpacrc&quot;. </p>
<p> The configuration file is based on the win32 .ini file model, ordered by sections and keys. </p>
<p> A section is declared as <code>[SectionName]</code> , a key is declared as <code>keyName=value</code> , the key value is not interpreted and always handled as ASCII text. Plugins may use the configuration file as well (to avoid multiple files). </p>
<p> <code>Note on plugin names: </code> Plugin names as given in the configuration file are names exported by each interface and not name of the physical library file (.dll/.so &#8230;). The physical file name can however be used to identify a plugin, it will be replaced by the interface name if the plugin was successfully loaded.</p>
<h2>SECTION General</h2>
<p> The &quot;General&quot; section holds generic, OS and player specific options. This section is not used by the GPAC Framework.</p>
<dl>
<dt><code>ModulesDirectory (value: path)</code></p>
<dd> path to modules (plugins) location. The client cannot be loaded without modules. This option is used by all GPAC clients on all platforms</p>
<dt><code>CacheDirectory (value: path)</code></p>
<dd> specifies location of temp files. This must be the absolute path to a directory with write access. Although not used by applications, this is used by several plugins.</dl>
<p> The following options are defined for Osmo4/wxWidgets player.</p>
<dl>
<dt><code>Loop (value: yes, no)</code></p>
<dd> specifies whether the presentation has to be restarted when done playing.</p>
<dt><code>ConsoleOff (value: yes, no)</code></p>
<dd> specifies whether application messages (script, buffering, download progress) are displayed in the console or not.</p>
<dt><code>Browser (value: string)</code></p>
<dd> specifies prefered browser for WWW anchors and scene graph viewing &#8211; Only used by Osmo4/wxWidgets.</p>
<dt><code>LookForSubtitles (value: yes, no)</code></p>
<dd> specifies if Osmo4 shall look for subtitle files when opening a presentation.</p>
<dt><code>PLEntry (value: unsigned int)</code></p>
<dd> indicates active playlist entry when player was last closed. Playlist backup is &quot;.gpac_pl.m3u&quot;, stored in user home directory.</p>
<dt><code>StartupFile value: filename)</code></p>
<dd> specifies file to load upon startup of osmo4/MP4Client. If not specified, no file is loaded.</p>
<dt><code>NoMIMETypeFetch (value: yes, no)</code></p>
<dd> specifies if the player has to check for mime type when following hyperlinks, or only follow links of known extensions.</p>
<dt><code>LogFile (value: filename)</code></p>
<dd> specifies where to output GPAC&#8217;s log. By default, the logs are written to stdout. Note that GPAC may be compiled without log support. This is not used by MP4Client.</p>
<dt><code>LogLevel (value: none, error, warning, info, debug)</code></p>
<dd> specifies the level of the log. By default, no log is performed.</p>
<dt><code>LogTools (value: a &#8216;:&#8217;-separated list of the following values)</code></p>
<dd> specifies which set of tools from GPAC should be logged. Available tools are:<br />
 core: libgpac core events.<br />
 coding: bitstream formats (audio, video, scene).<br />
 container: container formats (ISO File, MPEG-2 TS, AVI, &#8230;).<br />
 network: network data exept RTP trafic.<br />
 rtp: rtp, rtcp and rtsp trafic.<br />
 author : authoring tools (hint, import, export).<br />
 sync: terminal sync layer.<br />
 codec: terminal codec messages.<br />
 parser: scene parsers (svg, xmt, bt) and other.<br />
 media: terminal media object management.<br />
 scene: scene graph and scene manager.<br />
 script: scripting engine messages.<br />
 compose: composition engine (events, etc).<br />
 render: renderng engine (2D, 3D, etc).<br />
 service: network service management.<br />
 mmio: Audio/Video HW I/O management.</dl>
<h2>SECTION RecentFiles</h2>
<p> The &quot;RecentFiles&quot; section of the config file holds last accessed files (hardcoded to no more than 20) in the last access order. The keys are the file names and no value is used. This section is only used by GUI clients.</p>
<h2>SECTION Systems</h2>
<p> The &quot;Systems&quot; section holds all configuration options for the MPEG-4 Systems engine. The following options are defined:</p>
<dl>
<dt><code>Language (value: 3-char code from ISO 639-2)</code></p>
<dd> specifies the user prefered language. This is used to select streams in case of alternate content in an audio object.</p>
<dt><code>AlwaysDrawBIFS (value: yes, no)</code></p>
<dd> if set, late BIFS frame will still be drawn. If not set, the scene won&#8217;t be redrawn until BIFS streams are back in sync. This is by default off to keep better sync, but may be changed when testing heavy content or slow renderers.</p>
<dt><code>ForceSingleClock (value: yes, no)</code></p>
<dd> One big problem with MP4 files is that the notion of &quot;duration&quot; has been unclear for a long time, and most content available (audio-video files) specifiy a wrong BIFS duration. In such a case the movie cannot be controled/seek into.<br />
 Another problem with ISMA streaming is that BIFS/OD don&#8217;t use the same clock as audio/video, thus seeking the main timeline does not seek AV media.<br />
 Setting the ForceSingleClock will handle both cases by using a single timeline for all media streams and setting the duration to the one of the longest stream.</p>
<dt><code>ThreadingPolicy (value: Free, Single, Multi)</code></p>
<dd> specifies how media decoders are to be threaded.<br />
 Free: lets decoders decide of their threading.<br />
 Single: means that all decoders are managed in a single thread performing scheduling and priority handling.<br />
 Multi: means that each decoder runs in its own thread.</p>
<dt><code>Priority (value: low, normal, high, real-time)</code></p>
<dd> specifies the priority of the decoders (priority is applied to decoder thread(s) regardless of threading mode).</p>
<dt><code>hardcoded_protos (value: list of strings separated by space)</code></p>
<dd> holds a list list of EXTERNPROTO URLs (NO OD_ID !!!) implemented in hard in the renderer &#8211; for development only.</p>
<dt><code>NoVisualThread (value: yes, no)</code></p>
<dd> specifies whether the visual rendering is done in the main codec manager or in a dedicated thread.</p>
<dt><code>DefAudioDec, DefVideoDec (value: string)</code></p>
<dd> Specifies which plugin to use by default for audio/video decoding. Example, &quot;DefVideoDec=name&quot;. The name given is the name of the plugin to be used (same considerations as other plugins, cf above).</p>
<dt><code>codec_XX_XX (value: string)</code></p>
<dd> Allows to specify default media plugin (audio/video) per stream type and object type. This is usefull if you have more than one decoder for a given type. The syntax is <code>codec_AA_BB=pluginname</code> where AA is the hexadecimal MPEG-4 streamType value for the codec (0x04=visual, 0x05=audio) and BB is the hexadecimal MPEG-4 objectTypeIndication of the media (0x20 = MPEG-4 video, 0x40=MPEG-4 Audio, &#8230;). The name given is the name of the plugin to be used (same considerations as other plugins, cf above).</dl>
<h2>SECTION Rendering</h2>
<p> The &quot;Rendering&quot; section holds all configuration options for the logical rendering engines, whether 2D or 3D. The following options are defined:</p>
<dl>
<dt><code>RendererName (value: string)</code></p>
<dd> specifies which renderer should be used. There are currently 2 renderers available in GPAC, &quot;GPAC 2D Renderer&quot; and &quot;GPAC 3D Renderer&quot;. Renderers cannot be reloaded at run-time, the complete system must be restarted.</p>
<dt><code>Raster2D (value: string)</code></p>
<dd> specifies the 2D rasterizer to use for vectorial drawing. Used by 2D renderer (for everything) and 3D renderer (for textured text and gradients).</p>
<dt><code>FrameRate (value: float)</code></p>
<dd> specifies the simulation frame-rate of the presentation &#8211; this value is also used by the MPEG-4 Systems engine to determine when a BIFS frame is mature for decoding.</p>
<dt><code>AntiAlias (value: None, All, Text)</code></p>
<dd> specifies antialiasing settings &#8211; whether the setting is applied or not depends on the graphics plugin/graphic card.<br />
 None: no anti-aliasing<br />
 Text: anti-aliasing for text only<br />
 All: complete anti-aliasing</p>
<dt><code>FastRender (value: yes, no)</code></p>
<dd> specifies whether rendering should target speed or quality &#8211; whether the setting is applied or not depends on the graphics plugin/graphic card.</p>
<dt><code>ForceSceneSize (value: yes, no)</code></p>
<dd> forces the scene to resize to the biggest bitmap available if no size info is given in the BIFS configuration.</p>
<dt><code>StressMode (value: yes, no)</code></p>
<dd> specifies that the renderer runs in worst case scenario, recomputing all vectorial paths, meshes, outlines and reloading textures (sending them to graphics card) at each frame.</p>
<dt><code>BoundingVolume (value: None, Box, AABB)</code></p>
<dd> specifies whether the bounding volume of an object shall be drawn or not. Note that the 2D renderer only uses rectangles as bounding volumes. The &quot;AABB&quot; value is used by the 3D renderer only, and specifies the object bounding-box tree shall be drawn.</dl>
<h2>SECTION Render2D</h2>
<p> The &quot;Render2D&quot; section holds all configuration options for the 2D tile rendering engine. The following options are defined:</p>
<dl>
<dt><code>DirectRender (value: yes, no)</code></p>
<dd> specifies whether direct rendering should be used or not. In direct rendering mode, the screen is completely redrawn at each frame. In indirect rendering object positioning is tracked from frame to frame and dirty rectangles info is collected in order to redraw the minimal amount of the screen buffer.Whether the setting is applied or not depends on the graphics plugin (currently all plugins handle both mode).</p>
<dt><code>ScalableZoom (value: yes, no)</code></p>
<dd> specifies whether scalable zoom should be used or not. When scalable zoom is enabled, resizing the output window will also recompute all vectorial objects. Otherwise only the final buffer is stretched.</dl>
<h2>SECTION Render3D</h2>
<p> The &quot;Render3D&quot; section holds all configuration options for the 3D openGL rendering engine. The following options are defined:</p>
<dl>
<dt><code>RasterOutlines (value: yes, no)</code></p>
<dd> specifies that outlining shall be done through openGL pen width rather than vectorial outlining.</p>
<dt><code>PolygonAA (value: yes, no)</code></p>
<dd> specifies whether polygon antialiasing should be used in full antialiasing mode. If not set, only lines and points antialiasing are used.</p>
<dt><code>Wireframe (value: WireNone, WireOnly, WireOnSolid)</code></p>
<dd> specifies wireframe drawing options:<br />
 WireNone: objects are drawn as solid<br />
 WireOnly: objects are drawn as wireframe only<br />
 WireOnSolid: objects are drawn as solid and wireframe is then drawn</p>
<dt><code>DisableRectExt (value: yes, no)</code></p>
<dd> specifies whether openGL rectangular texture extension (GL_EXT_texture_rectangle or GL_NV_texture_rectangle) shall be used or not.<br />
 If &quot;yes&quot;, textures whose dimensions are not power of two are rescaled except if hardware support non-power-of-two textures (GL_ARB_texture_non_power_of_two) natively<br />
 If &quot;no&quot; and extension is available, textures are used without rescaling. Note that in this case texture transformation are disabled.</p>
<dt><code>EmulatePOW2 (value: yes, no)</code></p>
<dd> enables power of 2 emulation. Ignored if openGL rectangular texture extension is enabled.<br />
 if set, video texture is not resized but emulated with padding. This usually speeds up video mapping on shapes but disables texture transformations.<br />
 if not set, video is resized to a power of 2 texture when mapping to a shape.</p>
<dt><code>BitmapCopyPixels (value: yes, no)</code></p>
<dd> specifies whether the bitmap node should be drawn with regular openGL texturing (&quot;no&quot;) or through pixel copy routines (&quot;yes&quot;). This greatly impacts video rendering through bitmap depending on the graphics card. Some cards will have faster pixel copy routines that texture transfer ones, some won&#8217;t.</dl>
<h2>SECTION Audio</h2>
<p> The &quot;Audio&quot; section holds all configuration options for the audio rendering engine and hardware. Note that most options depend on the driver used and may be ignored by the driver. The following options are defined:</p>
<dl>
<dt><code>ForceConfig (value: yes, no)</code></p>
<dd> Forces a given sound card configuration to be used. If not set the sound card will be setup to use 2 audio buffers of 1024 samples each. This may not work properly on some audio cards due to hardware latency, therefore forcing the config may be very usefull.</p>
<dt><code>NumBuffers (value: integer, 0 forbidden)</code></p>
<dd> When config is forced, specifies the number of audio buffers to allocate (audio buffers are played in ring if possible, otherwise a single audio buffer is allocated).</p>
<dt><code>TotalDuration (value: integer, 0 forbidden)</code></p>
<dd> When config is forced, specifies the total audio buffer size in milliseconds. Be aware that the longer the audio buffer is, the longer the audio latency will be when pausing an audio object. The quality of fast forward audio playback will also be degradated when using large audio buffers.<br />
 <code>Note:</code> The SDL audio plugin does not use the TotalDuration and num buffers in the same way, it just computes the desired audio buffer size with this settings and picks the next power of 2 size for audio buffer size. It does not use ring buffers either.</p>
<dt><code>NoResync (value: yes, no)</code></p>
<dd> Disables audio resynchronization: audio clock is never adjusted and A/V sync may get broken</p>
<dt><code>DisableMultiChannel (value: yes, no)</code></p>
<dd> Disables audio multichannel output and always downmix to stereo. This may be usefull if the multichannel output behaves weirdly.</p>
<dt><code>DisableNotification (value: yes, no)</code></p>
<dd> Disables usage of audio buffer notifications when supported (currently only DirectSound supports it). If DirectSound audio sounds weird try without notifications. Ignored on other platforms than Win32/DX.</p>
<dt><code>DriverName (value: string)</code></p>
<dd> specifies the driver to use for audio rendering.</p>
<dt><code>Volume (value: integer, range 0-100)</code></p>
<dd> specifies the default audio volume used when launching GPAC.</p>
<dt><code>Pan (value: integer, range 0-100)</code></p>
<dd> specifies the default audio stereo balance used when launching GPAC &#8211; 0 for full left, 100 for full right, 50 for balanced.</dl>
<h2>SECTION Video</h2>
<p> The &quot;Video&quot; section holds all configuration options for the video renderer and hardware. The following options are defined:</p>
<dl>
<dt><code>DisableYUV (value: yes, no) &#8211; used by 2D renderer only</code></p>
<dd> disables YUV hardware support (YUV hardware support may not be available for the current plugin).</p>
<dt><code>SwitchResolution (value: yes, no)</code></p>
<dd> if enabled, selects smallest video resolution larger than scene size, otherwise use current video resolution.</p>
<dt><code>DriverName (value: string)</code></p>
<dd> specifies the driver to use for video memory access.</dl>
<h2>SECTION Network</h2>
<p> The &quot;Network&quot; section holds all configuration options for the network used by plugins and systems engine. The following options are defined:</p>
<dl>
<dt><code>AutoReconfigUDP (value: yes, no)</code></p>
<dd> specifies if network manager shall reconnect a scene if UDP traffic is blocked.</p>
<dt><code>DataTimeout (value: unsigned int)</code></p>
<dd> specifies timeout in milliseconds befor initial buffering aborts. Default terminal value is 20000 (20 seconds).</p>
<dt><code>UDPNotAvailable (value: yes, no)</code></p>
<dd> specifies that UDP traffic is not available (usually set by GPAC)</p>
<dt><code>UDPTimeout (value: unsigned int)</code></p>
<dd> specifies timeout in milliseconds for initial UDP detection. Once a UDP packet is recieved the timeout is ignored.</p>
<dt><code>BufferLength (value: unsigned int)</code></p>
<dd> specifies the default length of the decoding buffer in milliseconds. The client will wait for the buffer to be filled before starting decoding. A plugin may decide to use a different value based on protocol and network jitters.</p>
<dt><code>RebufferLength (value: unsigned int)</code></p>
<dd> specifies rebuffering length of the decoding buffer in milliseconds. Whenever the decoding buffer fullness is less than this value, the object clock is paused and the stream rebuffered till BufferLength. Therefore a value of 0 means no rebuffering. A plugin may decide to use a different value based on protocol and network jitters.</dl>
<h2>SECTION FontEngine</h2>
<p> The &quot;FontEngine&quot; section holds all configuration options for the font handling. The GPAC rendering module handles text through vectorial outline, allowing graphics plugin development without having to integrate text rendering which is always heavy work. The following options are defined:</p>
<dl>
<dt><code>DriverName (value: string)</code></p>
<dd> specifies the driver to use for font handling.</p>
<dt><code>FontDirectory (value: path)</code></p>
<dd> specifies the directory where fonts are located &#8211; currently only one directory can be specified (however nothing stops a font plugin from using a private directory). If the directory is invalid or does not contain fonts, text may be unavailable in GPAC.</p>
<dt><code>TextureTextMode (value: Never, 3D, Always)</code></p>
<dd> specifies whether text shall be drawn to a texture and then rendered or directly rendered. Using textured text can improve text look in the 3D renderer and also improve text-on-video like content.</p>
<dt><code>FontSerif (value: string)</code></p>
<dd> specifies default SERIF font.</p>
<dt><code>FontSans (value: string)</code></p>
<dd> specifies default SANS font.</p>
<dt><code>FontFixed (value: string)</code></p>
<dd> specifies default FIXED font.</dl>
<p> <code>Note:</code> The freetype plugin uses this section to maintain associations between font names and truetype font file names. This greatly speeds up font selection at run-time.</p>
<h2>SECTION Downloader</h2>
<p> The &quot;Downloader&quot; section holds all configuration options for file downloading and caching.</p>
<dl>
<dt><code>CleanCache (value: yes, no)</code></p>
<dd> specifies whether downloaded files shall be removed once used.</p>
<dt><code>RestartFiles (value: yes, no)</code></p>
<dd> specifies whether incompletely downloaded files shall be removed before redownloading.</p>
<dt><code>MaxRate (value: positive integer)</code></p>
<dd> specifies a maximum data rate in kilo bits per seconds for file downloading. This is used for simulation purposes. A value of 0 means no rate restriction.</p>
<dt><code>UserAgent (value: string)</code></p>
<dd> specifies an alternate user agent (default one is &quot;GPAC $VERSION&quot;).</dl>
<h2>SECTION HTTPProxy</h2>
<p> The &quot;HTTPProxy&quot; section of the config file holds configuration option for HTTP proxy adressing. Currently only one proxy can be enabled, and no URI selection is done</p>
<dl>
<dt><code>Enabled (value: yes, no)</code></p>
<dd> specifies whether the proxy should be used or not when downloading files.</p>
<dt><code>Name (value: string)</code></p>
<dd> specifies the proxy name (IP address or resolved name) without protocol identifier (eg, no &quot;http://&quot;). If not present, the proxy is disabled.</p>
<dt><code>Port (value: positive integer)</code></p>
<dd> Specifies the port to use with the proxy. If no port is specified, the default HTTP port (80) is used.</dl>
<h2>SECTION Streaming</h2>
<p> The &quot;Streaming&quot; section holds all configuration options for real-time streaming using IETF SDP/RTSP/RTP/RTCP protocols.</p>
<dl>
<dt><code>DefaultPort (value: unsigned short)</code></p>
<dd> specifies the default port to use when connecting to a server (ignored if a port is specified in the url). If the port is 80 or 8080 (HTTP), the client will connect to the RTSP server through an HTTP tunnel, and transport will take place on the RTSP connection.</p>
<dt><code>ReorderSize (value: integer)</code></p>
<dd> size of the RTP reordering buffer &#8211; 0 means no reordering. Ignored when transport takes place on the RTSP connection</p>
<dt><code>RTPoverRTSP (value: yes, no)</code></p>
<dd> specifies whether RTP packets should be carried on the RTSP connection (TCP or UDP) when possible, or carried on UDP. If the connection port is an HTTP port, this value is assumed to be true</p>
<dt><code>RTSPTimeout (value: unsigned int)</code></p>
<dd> specifies connection timeout with the server: an RTSP request is considered as failed when the timeout expires.</p>
<dt><code>FirstPacketDrop (value: unsigned int)</code></p>
<dd> specifies the first SL packet to be droped &#8211; 0 means no packet drop. Used for packet drop simulation tests.</p>
<dt><code>PacketDropFrequency (value: unsigned int)</code></p>
<dd> specifies the frequency at which SL packets are droped. If value is 20, one packet every 20 recieved packets will be droped. Used for packet drop simulation tests.</dl>
<h2>SECTION MimeTypes</h2>
<p> This section is used to keep MIME types and file associations for GPAC plugins. The format of the key is:<br />
 The description is used for GUI purposes (open file dialogs). You may modify the file extension list to support your own extensions. MIME Type is always checked when processing a remote ressource (eg http file) in order to load the appropriated plugins. If MIME type is not available, provided extensions are first checked, then all input plugins are queried.</p>
<h2>SECTION MimeTypes</h2>
<p> The &quot;StreamingCache&quot; section of the config file holds all configuration options for the streaming cache. Streaming cache allows for recording of live sources such as RTP/RTSP sessions and internet radios. This is currently just an experimental feature in GPAC.<br />
 <code>RecordDirectory (value: path)</code> specifies path for recorded files. Cached data is written directly to disk (no re-interleaving or similar processes). If not specified, the default cache directory is used.</p>
<dl>
<dt><code>BaseFileName (value: string)</code></p>
<dd> specifies the base name for recorded files. If not present in configuration file, the service name (URL) is used.</p>
<dt><code>KeepExistingFiles (value: yes no)</code></p>
<dd> specifies if cached files with same name should be kept or not. If not, an integer number is added to the cached file name, the higest number for the latest file.</p>
<dt>
<dd></dl>
<h2>SECTION SAXLoader</h2>
<p> The &quot;SAXLoader&quot; section holds all configuration options for XML SAX parsing of SVG, XMT and X3D files.</p>
<dl>
<dt></dl>
<h2>Progressive (value: string)</h2>
<dd> specifies XML parsing mode used by the loader. Supported modes are:<br />
 yes: SAX parsing is used with progressive loading of the document.<br />
 no: SAX parsing is used, document will first be completely downloaded.<br />
 DOM: DOM parsing is used, document will first be completely downloaded. Only supported by libXML2 plugin, otherwise handled as &quot;no&quot;.</p>
<dl>
<dt><code>MaxDuration (value positive integer)</code></p>
<dd> specifies the maximum amount of time the SAX parser should spent loading a portion of the document. Only used in SAX Progressive mode.</dl>
<h2>SECTION XviD</h2>
<p> The &quot;XviD&quot; section holds all configuration options for the XviD codec.</p>
<dl>
<dt></dl>
<h2>PostProc (value: string)</h2>
<dd> specifies filters to apply when decoding video. The string is a list of filters separated with a space character. Filters supported are:<br />
 FilmEffect: xvid 1.0.0 filmEffect.<br />
 Deblock_Y: Y plane deblocking filter.<br />
 Deblock_UV: UV plane deblocking filter.</p>
<dl>
<dt><code>Threaded (value yes, no)</code></p>
<dd> specifies whether the decoder should run in its own thread or not.</dl>
<h2>Section FFMPEG</h2>
<p> The &quot;FFMPEG&quot; section holds all configuration options for the FFMPEG demuxer and codec.</p>
<dl>
<dt></dl>
<h2>DataBufferMS (value: unsigned int)</h2>
<dd> specifies the amount of video/audio data (in milliseconds) to be bufferer before starting decoding. For developpers only.</p>
<h2>Section ISOReader</h2>
<p> The &quot;ISOReader&quot; section holds all configuration options for the ISO Media file demuxer.</p>
<dl>
<dt></dl>
<h2>IgnoreMPEG-4ForBrands (value: Full 4CC or 4CC pattern (abc* ab*))</h2>
<dd> ignores all MPEG-4 systems tracks and IOD for files showing the listed brands in their compatible brand list.</p>
<h2>CREATING THE CONFIGURATION FILE</h2>
<dl>
<dt>If not found, a default configuration file is created when launching MP4Client or Osmo4. In this process the font directory and the cache directory must be entered at prompt. The file is located in the user home directory and called &quot;.gpacrc&quot;</p>
<dd></dl>
<h2>FILES</h2>
<p> <code>GPAC Configuration File:</code> ~/.gpacrc</p>
<h2>AUTHORS</h2>
<p> Jean Le Feuvre &lt;jeanlf [at] users.sourceforge.net&gt; &#8211; GPAC (c) 2000-2005</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mp4client/">MP4Client</a>(1), <a href="/docs/linux/man/1-mp4box/">MP4Box</a>(1) </p>
<h2>Index</h2>
