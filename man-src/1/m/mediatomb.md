---
title: "mediatomb(1)"
name: "mediatomb"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mediatomb/"
description: "mediatomb – UPnP MediaServer"
---

<h2 class="name">NAME</h2>
<p> mediatomb &#8211; UPnP MediaServer </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mediatomb</code> [<code>-i&nbsp;<wbr></code><i>IP address</i><code>&nbsp;<wbr></code>] [<code>-e&nbsp;<wbr></code><i>interface</i><code>&nbsp;<wbr></code>] [<code>-p&nbsp;<wbr></code><i>port</i><code>&nbsp;<wbr></code>] [<code>-c&nbsp;<wbr></code><i>config file</i><code>&nbsp;<wbr></code>] [<code>-d</code>] [<code>-m&nbsp;<wbr></code><i>home dir</i><code>&nbsp;<wbr></code>] [<code>-f&nbsp;<wbr></code><i>config dir</i><code>&nbsp;<wbr></code>] [<code>-P&nbsp;<wbr></code><i>PID file</i><code>&nbsp;<wbr></code>] [<code>-u&nbsp;<wbr></code><i>user</i><code>&nbsp;<wbr></code>] [<code>-g&nbsp;<wbr></code><i>group</i><code>&nbsp;<wbr></code>] [<code>-a&nbsp;<wbr></code><i>path</i><code>&nbsp;<wbr></code>] [<code>-l&nbsp;<wbr></code><i>logfile</i><code>&nbsp;<wbr></code>] [<code>-D</code>] [<code>&#8211;compile-info</code>] [<code>&#8211;version</code>] [<code>-h</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page describes the command line parameters for MediaTomb. For a detailed documentation please see the README file which is distributed with MediaTomb or visit <a rel="nofollow" href="http://mediatomb.cc/.">http://mediatomb.cc/.</a></p>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>&#8211;ip</code></p>
<dl>
<dt>
<dd> The server will bind to the given IP address, currently we can not bind to multiple interfaces so binding to 0.0.0.0 will not be possible.</dl>
<p> <code>-e</code>, <code>&#8211;interface</code></p>
<dl>
<dt>
<dd> The server will bind to the given network interface, currently we can only bind to one interface at a time.</dl>
<p> <code>-p</code>, <code>&#8211;port</code></p>
<dl>
<dt>
<dd> Specify the server port that will be used for the web user interface, for serving media and for UPnP requests, minimum allowed value is 49152. If this option is omitted a default port will be chosen, however, in this case it is possible that the port will change upon server restart.</dl>
<p> <code>-c</code>, <code>&#8211;config</code></p>
<dl>
<dt>
<dd> By default MediaTomb will search for a file named &quot;config.xml&quot; in the ~/.mediatomb directory. This option allows you to specify a config file by the name and location of your choice. The file name must be absolute.</dl>
<p> <code>-d</code>, <code>&#8211;daemon</code></p>
<dl>
<dt>
<dd> Run the server in background, MediaTomb will shutdown on SIGTERM, SIGINT and restart on SIGHUP.</dl>
<p> <code>-m</code>, <code>&#8211;home</code></p>
<dl>
<dt>
<dd> Specify an alternative home directory. By default MediaTomb will try to retrieve the users home directory from the environment, then it will look for a .mediatomb directory in users home. If .mediatomb was found we will try to find the default configuration file (config.xml), if not found we will create both, the .mediatomb directory and the default config file. </p>
<p> This option is useful in two cases: when the home directory can not be retrieved from the environment (in this case you could also use -c to point MediaTomb to your configuration file or when you want to create a new configuration in a non standard location (for example, when setting up daemon mode). In the latter case you can combine this parameter with the parameter described in Section 5.6, &quot;Config Directory&quot;</dl>
<p> <code>-f</code>, <code>&#8211;cfgdir</code></p>
<dl>
<dt>
<dd> The default configuration directory is combined out of the users home and the default that equals to .mediatomb, this option allows you to override the default directory naming. This is useful when you want to setup the server in a nonstandard location, but want that the default configuration to be written by the server.</dl>
<p> <code>-P</code>, <code>&#8211;pidfile</code></p>
<dl>
<dt>
<dd> Specify a file that will hold the server process ID, the filename must be absolute.</dl>
<p> <code>-u</code>, <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Run MediaTomb under the specified user name, this is especially useful in combination with the daemon mode.</dl>
<p> <code>-g</code>, <code>&#8211;group</code></p>
<dl>
<dt>
<dd> Run MediaTomb under the specified group, this is especially useful in combination with the daemon mode.</dl>
<p> <code>-a</code>, <code>&#8211;add</code></p>
<dl>
<dt>
<dd> Add the specified directory or file name to the database without UI interaction. The path must be absolute, if path is a directory then it will be added recursively. If path is a file, then only the given file will be imported.</dl>
<p> <code>-l</code>, <code>&#8211;logfile</code></p>
<dl>
<dt>
<dd> Do not output log messages to stdout, but redirect everything to a specified file.</dl>
<p> <code>-D</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Enable debug log output.</dl>
<p> <code>&#8211;compile-info</code></p>
<dl>
<dt>
<dd> Print the configuration summary (used libraried and enabled features) and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a summary about the available command line options.</dl>
<h2>AUTHORS</h2>
<p> <code>Sergey Bostandzhyan</code> </p>
<p> <code>Leonhard Wimmer</code></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Gena Batsyan, Sergey Bostandzhyan<br />
 Copyright &#169; 2006-2008 Gena Batsyan, Sergey Bostandzhyan, Leonhard Wimmer </p>
<p> This manual page is part of MediaTomb. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License version 2 as published by the Free Software Foundation. </p>
<h2>Index</h2>
