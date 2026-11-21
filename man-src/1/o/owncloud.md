---
title: "owncloud(1)"
name: "owncloud"
section: "1"
letter: "o"
url: "/docs/linux/man/1-owncloud/"
description: "owncloud – File synchronisation desktop utility."
---

<h2>NAME</h2>
<p> owncloud &#8211; File synchronisation desktop utility.</p>
<h2>SYNOPSIS</h2>
<p> <i>owncloud</i> [<i>OPTIONS</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The ownCloud Client is a file synchronization desktop utility. It synchronizes files on your local computer, tablet, or handheld device with an ownCloud Server. If you make a change to the files on one device, the change is propagated to all other synchronized devices using the desktop synchronization clients. </p>
<p> Normally, you start the client by clicking on the desktop icon or by starting it from the client application menu. After starting, an ownCloud icon appears in the computer system tray or on your tablet or handheld device.</p>
<h2>OPTIONS</h2>
<p> You have the option of starting your ownCloud desktop client with the <code>owncloud</code> command. The following options are supported:</p>
<dl>
<dt><code>owncloud -h</code> or <code>owncloud &#8211;help</code></dt>
<dd> Displays all command options. </dd>
<p> The other options are:</p>
<dt><code>&#8211;logwindow</code></dt>
<dd> Opens a window displaying log output.</dd>
<dt><code>&#8211;logfile</code> <i>&lt;filename&gt;</i></dt>
<dd> Write log output to the file specified. To write to stdout, specify <i>&#8211;</i> as the filename.</dd>
<dt><code>&#8211;logdir</code> <i>&lt;name&gt;</i></dt>
<dd> Writes each synchronization log output in a new file in the specified directory.</dd>
<dt><code>&#8211;logexpire</code> <i>&lt;hours&gt;</i></dt>
<dd> Removes logs older than the value specified (in hours). This command is used with <code>&#8211;logdir</code>.</dd>
<dt><code>&#8211;logflush</code></dt>
<dd> Clears (flushes) the log file after each write action.</dd>
<dt><code>&#8211;confdir</code> <i>&lt;dirname&gt;</i></dt>
<dd> Uses the specified configuration directory.</dd></dl>
<h2>CONFIG FILE</h2>
<p> The ownCloud Client reads a configuration file. You can locate this configuration file as follows:</p>
<dl>
<dt><code>On Linux distributions:</code></dt>
<dd> <code>$HOME/.local/share/data/ownCloud/owncloud.cfg</code></dd>
<dt><code>On Microsoft Windows systems:</code></dt>
<dd> <code>%LOCALAPPDATA%\ownCloud\owncloud.cfg</code></dd>
<dt><code>On MAC OS X systems:</code></dt>
<dd> <code>$HOME/Library/Application Support/ownCloud/owncloud.cfg</code> </dd>
<p> The configuration file contains settings using the Microsoft Windows .ini file format. You can overwrite changes using the ownCloud configuration dialog. </p>
<p> <code>NOTE:</code> Use caution when making changes to the ownCloud Client configuration file. Incorrect settings can produce unintended results. </p>
<p> You can change the following configuration settings in the <code>[ownCloud]</code> section:</p>
<dt>&bull;</dt>
<dd> <code>remotePollInterval</code> (default: <code>30000</code>) &#8212; Specifies the poll time for the remote repository in milliseconds.</dd>
<dt>&bull;</dt>
<dd> <code>forceSyncInterval</code> (default: <code>7200000</code>) &#8212; The duration of no activity after which a synchronization run shall be triggered automatically.</dd>
<dt>&bull;</dt>
<dd> <code>notificationRefreshInterval</code> (default: <code>300000</code>) &#8212; Specifies the default interval of checking for new server notifications in milliseconds. </dd>
<p> You can change the following configuration settings in the <code>[General]</code> section:</p>
<dt>&bull;</dt>
<dd> <code>chunkSize</code> (default: <code>5242880</code>) &#8212; Specifies the chunk size of uploaded files in bytes.</dd>
<dt>&bull;</dt>
<dd> <code>promptDeleteAllFiles</code> (default: <code>true</code>) &#8212; If a UI prompt should ask for confirmation if it was detected that all files and folders were deleted.</dd>
<dt>&bull;</dt>
<dd> <code>maxLogLines</code> (default: <code>20000</code>) &#8212; Specifies the maximum number of log lines displayed in the log window.</dd>
<dt>&bull;</dt>
<dd> <code>timeout</code> (default: <code>300</code>) &#8212; The timeout for network connections in seconds.</dd></dl>
<h2>BUGS</h2>
<p> Please report bugs at <i><a rel="nofollow" href="https://github.com/owncloud/client/issues">https://github.com/owncloud/client/issues</a></i>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-owncloudcmd/">owncloudcmd</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> The ownCloud developers</p>
<h2>COPYRIGHT</h2>
<p> 2013-2016, The ownCloud developers </p>
