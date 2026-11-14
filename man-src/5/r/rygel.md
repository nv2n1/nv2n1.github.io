---
title: "rygel(5)"
name: "rygel"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rygel/"
description: "rygel.conf – Rygel configuration file"
---

<p>rygel.conf &#8211; Rygel configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>$XDG_CONFIG_DIR/rygel.conf</code></p>
<dt> <code>/etc/rygel.conf</code></dl>
<h2>Description</h2>
<p><code>rygel</code></p>
<dd>reads its configuration values from the file $XDG_CONFIG_DIR/rygel.conf or a file given on command line with the <code>&#8211;config</code> option. If that file does not exist it uses the file /etc/rygel.conf. </p>
<p> Most of the options may be overriden by commandline arguments or envronment variables. See <code><a href="/docs/linux/man/1-rygel/">rygel</a></code>(1) for details on those.</p>
<h2>General Directives</h2>
<p>Lists in the configuration files are separated by a semicolon (<code>;</code>). Boolean values may be either <code>true</code> or <code>false</code>. </p>
<p> <code>upnp-enabled</code></p>
<dl>
<dd>Enable/disable UPnP sharing of the media files. If set to <code>false</code>, rygel will still offer HTTP proxy URLs for its media files but not actively advertise them via UPnP.</dl>
<p> <code>interface=</code><i>INTERFACE</i></p>
<dl>
<dd>A list of the network interfaces rygel listens on. May be an IP, an interface name or on Linux even the ESSID of a wireless network.</dl>
<p> <code>port=</code><i>PORT</i></p>
<dl>
<dd>Set the listen-port.</dl>
<p> <code>enable-transcoding</code></p>
<dl>
<dd>Set to <code>true</code> to enable transcoding in general.</dl>
<p> <code>log-level=</code><i>DOMAIN</i><code>:</code><i>LEVEL</i><code>[,</code><i>DOMAIN</i><code>:</code><i>LEVEL</i><code>,&#8230;]</code></p>
<dl>
<dd>Comma-separated list of <i>DOMAIN</i>:<i>LEVEL</i> pairs, allowing to set the log level individually for each domain, where <i>DOMAIN</i> is eiher <code>&quot;*&quot;</code>, &quot;<code>rygel</code>&quot; or the name of a plugin. Allowed log levels are 1=critical, 2=error, 3=warning, 4=message/info, 5=debug. Note that on recent versions of GLib (&gt;= 2.36) it is required to set the environment variable <code>G_MESSAGES_DEBUG</code> to <code>all</code> to get any debug output.</dl>
<p> <code>plugin-path=</code><i>PATH</i></p>
<dl>
<dd>Set the plugin search path.</dl>
<p> <code>engine-path=</code><i>PATH</i></p>
<dl>
<dd>Set the engine search path.</dl>
<p> <code>media-engine=</code><i>ENGINE</i></p>
<dl>
<dd>Name of the loadable module to use as media engine back-end.</dl>
<p> <code>allow-upload</code></p>
<dl>
<dd>Allow uploading of media files via UPnP.</dl>
<p> <code>allow-deletion</code></p>
<dl>
<dd>Allow remote media file deletion via UPnP.</dl>
<p> <code>video-upload-folder</code></p>
<dl>
<dd>If <code>allow-upload</code> is <code>true</code>, use this folder to store uploaded videos. It defaults to <code>@VIDEOS@</code> which expands to the default directory for video files (usually <code>$HOME</code>/Videos).</dl>
<p> <code>music-upload-folder</code></p>
<dl>
<dd>If <code>allow-upload</code> is <code>true</code>, use this folder to store uploaded music files. It defaults to <code>@MUSIC@</code> which expands to the default directory for music files (usually <code>$HOME</code>/Music).</dl>
<p> <code>picture-upload-folder</code></p>
<dl>
<dd>If <code>allow-upload</code> is <code>true</code>, use this folder to store uploaded pictures. It defaults to <code>@PICTURES@</code> which expands to the default directory for picture files (usually <code>$HOME</code>/Pictures).</dl>
<p> <code>force-downgrade-for</code></p>
<dl>
<dd>Semicolon-separated list of device user-agents (or parts thereof) which need a forced downgrade to <code>MediaServer:1</code> and/or <code>ContentDirectory:1</code>. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Only use this parameter if you know what your&#8217;re doing or are being told to do so; overriding the default value might cause incompatibilites. If you find that adding your device here enables its usage with Rygel, please m[blue]<code>file an IOP bug</code>m[]<font SIZE="-2">[1]</font> so we can include it into the default configuration. </p>
</dl>
</dl>
<h2>Gstreamer Media Engine Settings</h2>
<p>The settings in the [GstMediaEngine] section are specific to the Gstreamer media engine, which is the default media engine. See the media-engine setting. These following options are available for the m[blue]<code>GStreamer</code>m[]<font SIZE="-2">[2]</font> media engine. </p>
<p> <code>transcoders</code></p>
<dl>
<dd>A semicolon-separated list of the active transcoders. This setting has no effect if <code>enable-transcoding</code> is set to false. Possible values are: lpcm,mp3,mp2ts,aac,avc or wmv. Its default value is lpcm;mp3;mp2ts;aac;wmv.</dl>
<h2>Plugin-Specific Settings</h2>
<p>Sections for plugins are denoted with <code>[PluginName]</code> and can contain options specific to a plugin (see below) as well these common options: </p>
<p> <code>title</code>=<i>TITLE</i></p>
<dl>
<dd>Title of the device implemented by this plugin. There are some variables which will be replaced by rygel. <i>@REALNAME@</i> will be subsituted by the user&#8217;s real name, <i>@USERNAME@</i> by the user&#8217;s login id and <i>@HOSTNAME@</i> by the name of the machine rygel runs on.</dl>
<p> <code>enabled</code></p>
<dl>
<dd>You can individually enable or disable plugins by setting this to <code>true</code> or <code>false</code>.</dl>
<p> <code>diagnostics</code></p>
<dl>
<dd>Set to <code>true</code> if you would like the UPnP device to contain a BasicManagement:2 service that allows running tools like ping, nslookup and traceroute remotely.</dl>
<h2>Tracker Plugin</h2>
<p>The tracker plugin uses the centralized database of meta information from the tracker project. See the m[blue]<code>tracker project website</code>m[]<font SIZE="-2">[3]</font> for more information about tracker. </p>
<p> <code>share-pictures</code></p>
<dl>
<dd>Enable or disable sharing of all pictures in the Tracker database.</dl>
<p> <code>share-videos</code></p>
<dl>
<dd>Enable or disable sharing of all videos in the Tracker database.</dl>
<p> <code>share-music</code></p>
<dl>
<dd>Enable or disable sharing of all music in the Tracker database.</dl>
<h2>Mediaexport Plugin</h2>
<p>The MediaExport plugin is an alternative to the tracker-backed media export. It extracts meta-data by itself and stores it in a m[blue]<code>SQLite</code>m[]<font SIZE="-2">[4]</font> database in $XDG_CACHE_DIR/rygel/media-export.db on UNIX platforms. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If both plugins, Tracker as well as MediaExport are enabled, MediaExport will disable itself in favour of the Tracker plugin. </p>
</dl>
<p> There are several options supported by this plugin: </p>
<p> <code>uris</code></p>
<dl>
<dd>A list of URIS to expose via UPnP. May be files, folders or anything supported by GVFS. If left emtpy it defaults to export the user&#8217;s music, video and picture folders as defined per XDG special user directories spec. These default folders can be referenced by <code>@MUSIC@</code>, <code>@PICTURES@</code> and <code>@VIDEOS@</code>. Locations can be entered as either fully escaped URIS or normal paths. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If you enter a normal path that contains whitespace there is no need to escape them with either a backslash or putting the string in quotes. </p>
</dl>
<p> <code>Example 1. Possible values for uris</code> </p>
<p> <code>uris=@MUSIC@;/home/user/My Pictures;file:///home/user/My%20Videos</code></dl>
<p> <code>extract-metadata</code></p>
<dl>
<dd>Set to <code>false</code> if you do not care about duration or any other meta-data like artist. This speeds up the initial crawl of the media a lot. Use it to quickly share some files via UPnP. Make sure to define an <code>include-filter</code>, otherwise you will end up with a lot of files exposed which the client cannot display anyway.</dl>
<p> <code>monitor-changes</code></p>
<dl>
<dd>Set to <code>false</code> if you don&#8217;t want to have new files picked up automatically by rygel.</dl>
<p> <code>monitor-grace-timeout</code></p>
<dl>
<dd>Time in seconds to wait after a new file has been detected before trying to extract meta-data from it. Useful if you&#8217;re downloading to a directory watched by rygel. Default is 5 seconds.</dl>
<p> <code>virtual-folders</code></p>
<dl>
<dd>Set to <code>false</code> if you don&#8217;t need the virtual folder hierarchy.</dl>
<h2>Playbin Plugin</h2>
<p>The Playbin plugin implements a media renderer (Digtal Media Renderer, DMR in DLNA terms). This plugin was known as GstRenderer. </p>
<p> This plugin has no special options.</p>
<h2>Zdfmediathek</h2>
<p>The m[blue]<code>ZDF Mediathek</code>m[]<font SIZE="-2">[5]</font> is an online archive of broadcasts from the second german television. This plugin can be used to subscribes to the RSS feeds of this service and expose the broadcasts via UPnP. </p>
<p> <code>rss</code></p>
<dl>
<dd>A list of broadcast ids. How to get the broadcast ids from the web site is described in the file README.Mediathek (in german only).</dl>
<p> <code>update-interval</code></p>
<dl>
<dd>Time in seconds after which the plugin checks for new content. The default interval is 1800 seconds (30 minutes), the minimum interval 10 minutes.</dl>
<p> <code>video-format</code></p>
<dl>
<dd>The mediathek usually offers the videos in two formats, WMV and H.264. Possible values here are wmv and mp4. The default video format is wmv. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Proxying of general RTSP in rygel as used by the H.264 streams is currently not working very well. Please enable mp4 only if your renderer can handle RTSP by itself. </p>
</dl>
</dl>
<h2>Gstlaunch Plugin</h2>
<p>The GstLaunch plugin allows to expose GStreamer pipelines using the same syntax as the gst-launch utilty. You can configure several items in this plugins. </p>
<p> <code>launch-items</code></p>
<dl>
<dd>A list of of identifiers for the pipelines to be exposed.</dl>
<p> <code>identifier-title</code></p>
<dl>
<dd>Title of the device represented by this pipeline. Identifier is the identifier as set in launch-items</dl>
<p> <code>identifier-mime</code></p>
<dl>
<dd>Mime-type of the pipeline.</dl>
<p> <code>identifier-launch</code></p>
<dl>
<dd>Definition of the pipeline in gst-launch syntax. For some examples on writing pipelines see <code><a href="/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1).</dl>
<p> <code>identifier-dlnaprofile</code></p>
<dl>
<dd>DLNA profile for the stream.</dl>
<p> An example configuration is available in the distributed configuration file /etc/rygel.conf.</p>
<h2>External</h2>
<p>The External plugin is an consumer of the m[blue]<code>MediaServer2 DBus interface specification</code>m[]<font SIZE="-2">[6]</font>. This allows external programs to share their data via UPnP by implementing this DBus specification. The plugin picks up any implementation of this interface on the session bus and exposes the presented media via UPnP. Known implementors of this spec are m[blue]<code>gnome-dvb-daemon</code>m[]<font SIZE="-2">[7]</font>, m[blue]<code>Rhythmbox</code>m[]<font SIZE="-2">[8]</font> and m[blue]<code>Grilo</code>m[]<font SIZE="-2">[9]</font> via the grilo-ms2 project. </p>
<p> You can disable the whole functionality by setting <code>enabled=false</code> in the <code>[External]</code> section of the configuration file. </p>
<p> Individual peers may be enabled or disabled by creating sections corresponding to the D-Bus names of the peer: </p>
<dl>
<dd>
<pre>[org.gnome.UPnP.MediaServer2.Rhythmbox]
enabled=false</pre>
</dl>
<p> This plugin has no additional options.</p>
<h2>Mpris</h2>
<p>The MPRIS plugin is a consumer of the m[blue]<code>MPRIS2 DBus interface specification</code>m[]<font SIZE="-2">[10]</font>. The implementation conforms to version 2.0 of the standard. </p>
<p> rygel exposes media players that implement the provider side of this DBus specification as DLNA Digital Media Renderers (DMR) similar to the Playbin plugin. This means that you can easily turn your media player into a DMR by implementing this DBus specification. </p>
<p> Players that implement this spec and are known to work with rygel are m[blue]<code>Banshee</code>m[]<font SIZE="-2">[11]</font>, m[blue]<code>Rhythmbox</code>m[]<font SIZE="-2">[8]</font> and m[blue]<code>Totem</code>m[]<font SIZE="-2">[12]</font> </p>
<p> You can disable the whole functionality by setting <code>enabled=false</code> in the <code>[MRPIS]</code> section of the configuration file. </p>
<p> The configuration of this plugin is special. Plugin configuration is not done on the plugin but rather per peer that is found providing the MPRIS2 interface. See the following example to set the title for Banshee on MPRIS: </p>
<dl>
<dd>
<pre>[org.mpris.MediaPlayer2.banshee]
title=@REALNAME@'s Banshee on @HOSTNAME@</pre>
</dl>
<p> This plugin has no additional options.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rygel/">rygel</a></code>(1), README.Mediathek, <code><a href="/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1)</p>
<h2>Author</h2>
<p><code>Jens Georg</code> &lt;mail [at] jensge.org&gt;</p>
<dl>
<dd>Wrote this manpage.</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>file an IOP bug</p>
<dl>
<dd><a rel="nofollow" href="https://bugzilla.gnome.org/enter_bug.cgi?product=Rygel">https://bugzilla.gnome.org/enter_bug.cgi?product=Rygel</a>&amp;component=IOP</dl>
<dt> 2.</p>
<dd>GStreamer</p>
<dl>
<dd><a rel="nofollow" href="http://gstreamer.freedesktop.org">http://gstreamer.freedesktop.org</a></dl>
<dt> 3.</p>
<dd>tracker project website</p>
<dl>
<dd><a rel="nofollow" href="http://projects.gnome.org/tracker/">http://projects.gnome.org/tracker/</a></dl>
<dt> 4.</p>
<dd>SQLite</p>
<dl>
<dd><a rel="nofollow" href="http://sqlite.org">http://sqlite.org</a></dl>
<dt> 5.</p>
<dd>ZDF Mediathek</p>
<dl>
<dd><a rel="nofollow" href="http://www.zdf.de/ZDFmediathek">http://www.zdf.de/ZDFmediathek</a></dl>
<dt> 6.</p>
<dd>MediaServer2 DBus interface specification</p>
<dl>
<dd><a rel="nofollow" href="http://live.gnome.org/Rygel/MediaServer2Spec">http://live.gnome.org/Rygel/MediaServer2Spec</a></dl>
<dt> 7.</p>
<dd>gnome-dvb-daemon</p>
<dl>
<dd><a rel="nofollow" href="http://live.gnome.org/DVBDaemon">http://live.gnome.org/DVBDaemon</a></dl>
<dt> 8.</p>
<dd>Rhythmbox</p>
<dl>
<dd><a rel="nofollow" href="http://www.rhythmbox.org">http://www.rhythmbox.org</a></dl>
<dt> 9.</p>
<dd>Grilo</p>
<dl>
<dd><a rel="nofollow" href="http://live.gnome.org/Grilo">http://live.gnome.org/Grilo</a></dl>
<dt>10.</p>
<dd>MPRIS2 DBus interface specification</p>
<dl>
<dd><a rel="nofollow" href="http://www.mpris.org">http://www.mpris.org</a></dl>
<dt>11.</p>
<dd>Banshee</p>
<dl>
<dd><a rel="nofollow" href="http://banshee.fm">http://banshee.fm</a></dl>
<dt>12.</p>
<dd>Totem</p>
<dl>
<dd><a rel="nofollow" href="http://live.gnome.org/Totem">http://live.gnome.org/Totem</a></dl>
