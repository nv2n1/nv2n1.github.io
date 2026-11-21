---
title: "xmms2d(1)"
name: "xmms2d"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms2d/"
description: "xmms2d – XMMS2 daemon which handles the playback of music and storage of music metadata"
---

<h2>NAME</h2>
<p> xmms2d &#8211; XMMS2 daemon which handles the playback of music and storage of music metadata</p>
<h2>SYNOPSIS</h2>
<p> <i>xmms2d</i> [ <code>-vqn</code> ] [ <code>-? / &#8211;help</code> ] [ <code>-V / &#8211;version</code> ] [ <code>-p</code> plugin_path / <code>&#8211;plugindir=</code> plugin_path ] [ <code>-o</code> output_plugin / <code>&#8211;output=</code> output_plugin ] [ <code>-c </code> path_to_config_file / <code>&#8211;conf=</code> path_to_config_file ] [ <code>-s </code> fd / <code>&#8211;status-fd=</code> fd ]</p>
<h2>DESCRIPTION</h2>
<p> <code>XMMS2 </code> is a redesign of the XMMS (<a rel="nofollow" href="http://www.xmms.org)">http://www.xmms.org)</a> music player. It features a client-server model, allowing multiple (even simultaneous!) user interfaces, both textual and graphical. All common audio formats are supported using plugins. On top of this, there is a flexible media library to organise your music. </p>
<p> <i>xmms2d</i> is the daemon through which <code>XMMS2</code> clients playback and manage music. A client library provided allows third parties to easily write <code>XMMS2</code> clients, especially using the Python and Ruby bindings. </p>
<p> <i>xmms2d</i> uses a three part method to playback music. Music is accessed from disk or network using a transport plugin, the data is then passed on to a decoder plugin which decodes the audio into a form that can be played back by an output plugin. </p>
<p> <i>xmms2d </i> includes command line options to change the way in which the daemon functions.</p>
<dl>
<dt><code>These</code>options<code>are</code>currently<code>recognised:</code></dt>
<dd>
</dd><dt><i>-v </i></dt>
<dd> Increases the vebosity of <i>xmms2d</i></dd>
<dt><i>-q</i></dt>
<dd> Decrease the verbosity of <i>xmms2d</i></dd>
<dt><i>-V | &#8211;version </i></dt>
<dd> Returns the <code>XMMS2</code> version</dd>
<dt><i>-? | &#8211;help</i></dt>
<dd> Displays basic help information for <i>xmms2d</i></dd>
<dt><i>-n | &#8211;no-logging</i></dt>
<dd> Disables logging</dd>
<dt><i>-o output_plugin | &#8211;output=output_plugin</i></dt>
<dd> Specifies a different output plugin to use in place of the default</dd>
<dt><i>-p plugin_path | &#8211;plugindir=plugin_path</i></dt>
<dd> Specifies a different plugin directory path than the default</dd>
<dt><i>-c path_to_config_file | &#8211;conf=path_to_config_file</i></dt>
<dd> Specifies a path to an alternative configuration file</dd>
<dt><i>-s fd | &#8211;status-fd=fd</i></dt>
<dd> Specifies a file descriptor to write to when started</dd></dl>
<h2>IPC SOCKET</h2>
<p> <code>XMMS2</code> clients uses IPC sockets to communicate with <i>xmms2d. </i> These IPC sockets are specified in a URL based format with three possible transport methods: unix, tcp, and tcp6. </p>
<p> The TCP methods allow clients to connect over IPv4 and IPv6 to <i>xmms2d</i> and therefore allow remote control of <code>XMMS2.</code></p>
<dl>
<dt>A typical IPC socket path using TCP would be:</dt>
<dd> <code><a href="tcp://127.0.0.1:9667">tcp://127.0.0.1:9667</a> </code></dd></dl>
<p> The UNIX transport method is for local clients only and creates a file through which <code>XMMS2</code> clients can access <i>xmms2d.</i></p>
<dl>
<dt>A typical IPC socket path using the UNIX transport would be:</dt>
<dd> <code><a href="unix:///tmp/xmms-ipc-foobar">unix:///tmp/xmms-ipc-foobar</a> </code></dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.config/xmms2/medialib.db or $XDG_CONFIG_HOME/xmms2/medialib.db</i></dt>
<dd> An sqlite3 database that includes information about each song that has been added to the <code>XMMS2</code> media library</dd>
<dt><i>$HOME/.config/xmms2/xmms2.conf or $XDG_CONFIG_HOME/xmms2/xmms2.conf</i></dt>
<dd> An XML formatted configuration file that allows you to change the default settings of <i>xmms2d</i></dd>
<dt><i>$HOME/.config/xmms2/startup.d or $XDG_CONFIG_HOME/xmms2/startup.d</i></dt>
<dd> A directory populated with programs that run when <i>xmms2d</i> is executed</dd>
<dt><i>$HOME/.config/xmms2/shutdown.d or $XDG_CONFIG_HOME/xmms2/shutdown.d</i></dt>
<dd> A directory populated with programs that run when <i>xmms2d</i> is shutdown correctly</dd>
<dt><i>/tmp/xmms-ipc-USER</i></dt>
<dd> The typical location for the UNIX IPC Socket. USER is the name of the user that executed <i>xmms2d.</i></dd></dl>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><i>XDG_CONFIG_HOME</i></dt>
<dd> The path where the xmms2 configuration files and resources are located</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xmms2/">xmms2</a>(1), <a href="/docs/linux/man/1-xmms2-launcher/">xmms2-launcher</a>(1), <a rel="nofollow" href="http://xmms2.xmms.org">http://xmms2.xmms.org</a></p>
<h2>HISTORY</h2>
<p> The <code>XMMS2</code> Project was started by Tobias Rundström and Anders Gustafsson. It is developed with their lead by a small group of contributers from all over the world.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alexander Botero-Lowry &lt;alex [at] foxybanana.com&gt; </p>
