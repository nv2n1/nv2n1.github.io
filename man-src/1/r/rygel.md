---
title: "rygel(1)"
name: "rygel"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rygel/"
description: "rygel – a collection of DLNA/UPnP AV services"
---

<h2 class="name">NAME</h2>
<p> rygel &#8211; a collection of DLNA/UPnP AV services </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>rygel</code> [<code>options</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>rygel</code></p>
<dd>is a home media solution that allows you to easily share audio, video and pictures, and control of media player on your home network. In technical terms it is both a UPnP AV MediaServer and MediaRenderer implemented through a plug-in mechanism. Interoperability with other devices in the market is achieved by conformance to very strict requirements of DLNA and on the fly conversion of media to format that client devices are capable of handling.</p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version of program.</dl>
<p> <code>-n</code>, <code>&#8211;network-interface=</code><i>INTERFACE</i></p>
<dl>
<dt>
<dd> Set the network interfaces rygel listens on. Can be used multiple times for to configure multiple interfaces. <code>INTERFACE</code> can be an IP, a device name or an ESSID (Linux only).</dl>
<p> <code>-p</code>, <code>&#8211;port=</code><i>PORT</i></p>
<dl>
<dt>
<dd> Set the listen-port.</dl>
<p> <code>-t</code>, <code>&#8211;disable-transcoding</code></p>
<dl>
<dt>
<dd> Disable any transcoding.</dl>
<p> <code>-U</code>, <code>&#8211;disallow-upload</code></p>
<dl>
<dt>
<dd> Disable uploading of media files via UPnP.</dl>
<p> <code>-D</code>, <code>&#8211;disallow-deletion</code></p>
<dl>
<dt>
<dd> UPnP clients are not allowed to delete media files on the server.</dl>
<p> <code>-g</code>, <code>&#8211;log-level=</code><i>LEVEL</i></p>
<dl>
<dt>
<dd> Comma-separated list of <i>DOMAIN</i>:<i>LEVEL</i> pairs, allowing to set the log level individually for each domain, where <i>DOMAIN</i> is eiher <code>&quot;*&quot;</code>, &quot;<code>rygel</code>&quot; or the name of a plugin. Allowed log levels are 1=critical, 2=error, 3=warning, 4=message/info, 5=debug.</dl>
<p> <code>-u</code>, <code>&#8211;plugin-path=</code><i>PATH</i></p>
<dl>
<dt>
<dd> Set the plugin search path.</dl>
<p> <code>-e</code>, <code>&#8211;engine-path=</code><i>ENGINE_PATH</i></p>
<dl>
<dt>
<dd> Set the media streaming and transcoding engine search path.</dl>
<p> <code>-d</code>, <code>&#8211;disable-plugin=</code><i>PLUGIN_NAME</i></p>
<dl>
<dt>
<dd> Disable the plugin <i>PLUGIN_NAME</i>.</dl>
<p> <code>-i</code>, <code>&#8211;title=</code><i>PLUGIN_NAME</i><code>:</code><i>TITLE</i></p>
<dl>
<dt>
<dd> Set the title of plugin <i>PLUGIN_NAME</i> to <i>TITLE</i> You can use this option more than once for every plugin you want to set the name of.</dl>
<p> <code>-o</code>, <code>&#8211;plugin-option=</code><i>PLUGIN_NAME</i><code>:</code> <i>OPTION</i><code>:</code><i>VALUE1[,VALUE2,&#8230;]</i></p>
<dl>
<dt>
<dd> Set options for a plugin.</dl>
<p> <code>-P</code>, <code>&#8211;disable-upnp</code></p>
<dl>
<dt>
<dd> Disable advertisement via UPnP and set rygel into streaming-only mode.</dl>
<p> <code>-c</code>, <code>&#8211;config=</code><i>CONFIG_FILE</i></p>
<dl>
<dt>
<dd> Use <i>CONFIG_FILE</i> instead of ${XDG_CONFIG_DIR}/rygel.conf.</dl>
<p> <code>-s</code>, <code>&#8211;shutdown</code></p>
<dl>
<dt>
<dd> Shutdown a currently running instance of rygel</dl>
<p> <code>-r</code>, <code>&#8211;replace</code></p>
<dl>
<dt>
<dd> Replace the currently running instance of rygel with this instance. Short for <code>rygel -s &amp;&amp; rygel</code></dl>
<h2>FILES</h2>
<p> /etc/rygel.conf</p>
<dl>
<dt>
<dd> The system-wide configuration file to control the behaviour of rygel. See <code><a href="/docs/linux/man/5-rygel-conf/">rygel.conf</a></code>(5) for further details.</dl>
<p> ${XDG_CONFIG_DIR}/rygel.conf</p>
<dl>
<dt>
<dd> The per-user configuration file to control the behaviour of rygel. See <code><a href="/docs/linux/man/5-rygel-conf/">rygel.conf</a></code>(5) for further details.</dl>
<p> ${XDG_CONFIG_DIR}/Rygel/*.xml</p>
<dl>
<dt>
<dd> Cached UPnP device description files.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>RYGEL_DISABLE_UPNP</code></p>
<dl>
<dt>
<dd> Disable advertisement via UPnP and set rygel into streaming-only mode.</dl>
<p> <code>RYGEL_IFACE</code></p>
<dl>
<dt>
<dd> Set the network interfaces to bind to.</dl>
<p> <code>RYGEL_PORT</code></p>
<dl>
<dt>
<dd> Define the network port to bind to.</dl>
<p> <code>RYGEL_DISABLE_TRANSCODING</code></p>
<dl>
<dt>
<dd> Disable transcoding globally.</dl>
<p> <code>RYGEL_LOG</code></p>
<dl>
<dt>
<dd> Set the log level of rygel.</dl>
<p> <code>RYGEL_PLUGIN_PATH</code></p>
<dl>
<dt>
<dd> Set the plugin search path of rygel.</dl>
<p> <code>RYGEL_ENGINE_PATH</code></p>
<dl>
<dt>
<dd> Set the media streaming and transcoding engine search path for rygel.</dl>
<p> <code>RYGEL_MEDIA_ENGINE</code></p>
<dl>
<dt>
<dd> Set a specific media streaming engine to pick up from the media engine search path.</dl>
<p> <code>RYGEL_DISABLE_UPLOAD</code></p>
<dl>
<dt>
<dd> Disable media file upload via UPnP.</dl>
<p> <code>RYGEL_DISABLE_DELETION</code></p>
<dl>
<dt>
<dd> Disable remote file deletion via UPnP.</dl>
<p> <code>RYGEL_PLUGIN_TIMEOUT</code></p>
<dl>
<dt>
<dd> Set the time-out for finding the plugins. Useful to increase when running inside valgrind.</dl>
<p> <code>RYGEL_DATABASE_DEBUG</code></p>
<dl>
<dt>
<dd> If set to 1, the database library will print the used SQL statements.</dl>
<p> Also for every plugin you can set the following environment variables: </p>
<p> <code>RYGEL_PLUGIN_NAME_TITLE</code></p>
<dl>
<dt>
<dd> Set the title of the plugin.</dl>
<p> <code>RYGEL_PLUGIN_NAME_ENABLED</code></p>
<dl>
<dt>
<dd> Enable or disable the plugin.</dl>
<h2>BUGS</h2>
<p> The BTS can be found at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/rygel/issues">https://gitlab.gnome.org/GNOME/rygel/issues</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-rygel-conf/">rygel.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <code>Jens Georg</code> &lt;mail [at] jensge.org&gt;</p>
<dl>
<dt>
<dd> Wrote this manpage.</dl>
<h2>Index</h2>
