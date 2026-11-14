---
title: "amrecover(8)"
name: "amrecover"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amrecover/"
description: "amrecover – Amanda index database browser"
---

<p>amrecover &#8211; Amanda index database browser</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amrecover</code> [-s&nbsp;<wbr><i>index-server</i>] [-t&nbsp;<wbr><i>tape-server</i>] [-d&nbsp;<wbr><i>tape-device</i>] [-h&nbsp;<wbr><i>hostname</i>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [-C&nbsp;<wbr><i>config</i>]</dl>
<h2>Description</h2>
<p><code>Amrecover</code></p>
<dd>browses the database of Amanda index files to determine which tapes contain files to recover. Furthermore, it is able to recover files. </p>
<p> In order to restore files in place, you must invoke <code>amrecover</code> from the root of the backed up filesystem, or use <code>lcd</code> to move into that directory, otherwise a directory tree that resembles the backed up filesystem will be created in the current directory. See the examples below for details. </p>
<p> Amrecover will read the <code>amanda-client.conf</code> file and the <i>config</i><code>/amanda-client.conf</code> file. If no configuration name is supplied on the command line, Amrecover will try the compiled-in default configuration ,usually <code>DailySet1</code>. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The Default values are those set at compile-time. Use <code>amrestore</code> to recover client-encrypted or client-custom-compressed tapes. </p>
</dl>
<p> <code>[ -C ] config</code></p>
<dl>
<dd>Amanda configuration.</dl>
<p> <code>-s index-server</code></p>
<dl>
<dd>Host that runs the index daemon.</dl>
<p> <code>-t tape-server</code></p>
<dl>
<dd>Host that runs the tape server daemon.</dl>
<p> <code>-d tape-device</code></p>
<dl>
<dd>Tape device to use on the tape server host.</dl>
<p> <code>-h hostname</code></p>
<dl>
<dd>Hostname to begin restoring; defaults to the system&#8217;s hostname.</dl>
<p> <code>-o</code> <i>clientconfigoption</i></p>
<dl>
<dd>See the &quot;<code>CONFIGURATION OVERRIDE</code>&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Auth</h2>
<p>The default <code>auth</code> is &#8216;BSDTCP&#8217;, you can set a different auth in the <code>amanda-client.conf</code> file or by specifying the &#8216;-oauth=bsd&#8217; command line argument.</p>
<h2>Commands</h2>
<p><code>Amrecover</code> connects to the index server and then presents a command line prompt. Usage is similar to an ftp client. The GNU readline library is used to provide command line history and editing if it was built in to <code>amrecover</code>. </p>
<p> The purpose of browsing the database is to build up a <i>restore list</i> of files to be extracted from the backup system. The following commands are available: </p>
<p> <code>sethost hostname</code></p>
<dl>
<dd>Specifies which host to look at backup files for (default: the local host).</dl>
<p> <code>setdate YYYY-MM-DD-HH-MM[-SS] | YYYY-MM-DD</code></p>
<dl>
<dd>Set the restore time (default: now). File listing commands only return information on backup images for this day, for the day before with the next lower dump level, and so on, until the most recent level 0 backup on or before the specified date is encountered. </p>
<p> For example, if: </p>
<dl>
<dd>
<pre>1996-07-01 was a level 0 backup
1996-07-02 through 1996-07-05 were level 1 backups
1996-07-06 through 1997-07-08 were level 2 backups</pre>
</dl>
<p> then the command <code>setdate 1997-07-08-00</code> would yield files from the following days: </p>
<dl>
<dd>
<pre>1997-07-08 (the latest level 2 backup)
1997-07-05 (the latest level 1 backup)
1997-07-01 (the latest level 0 backup)</pre>
</dl>
<p> Only the most recent version of a file will be presented. </p>
<p> The following abbreviated date specifications are accepted: </p>
<p> <code>&#8211;MM-DD</code></p>
<dl>
<dd>dates in the current year</dl>
<p> <code>&#8212;DD</code></p>
<dl>
<dd>dates in the current month of the current year</dl>
</dl>
<p> <code>setdisk</code> <i>diskname</i> [<i>mountpoint</i>]</p>
<dl>
<dd>Specifies which disk to consider (default: the disk holding the working directory where <code>amrecover</code> is started). It can only be set after the host is set with <code>sethost</code>. <i>Diskname</i> is the device name specified in the <i>amanda.conf</i> or <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5). The disk must be local to the host. If <i>mountpoint</i> is not specified, all pathnames will be relative to the (unknown) mount point instead of full pathnames.</dl>
<p> <code>listhost</code> [<i>diskdevice</i>]</p>
<dl>
<dd>List all <code>host</code></dl>
<p> <code>listdisk</code> [<i>diskdevice</i>]</p>
<dl>
<dd>List all <code>diskname</code></dl>
<p> <code>listproperty</code></p>
<dl>
<dd>List all <code>property</code></dl>
<p> <code>setproperty</code> [<code>append</code>] [<code>priority</code>] <i>name</i> [<i>value</i> &#8230;]</p>
<dl>
<dd>Set the property <i>name</i> to the value <i>value</i>. The <code>append</code> keyword appends the <i>value</i> to the values already set for this property. Without <i>value</i>, the property is unset. The <code>priority</code> keyword is unused, it is present for ease of copy/paste from application definition.</dl>
<p> <code>setdevice</code> [[-h <i>tape-server</i>] <i>tapedev</i>]</p>
<dl>
<dd>Specifies the host to use as the tape server, and which of its tape devices to use. If the server is omitted, the server name reverts to the configure-time default. If the tape device is omitted, the default is used. </p>
<p> If you want amrecover to use your changer, the <i>tapedev</i> must be equal to the <code>amrecover-changer</code> setting on the server. </p>
<p> Since device names contain colons, you must always specify the hostname. </p>
<pre>settape 192.168.0.10:file:/file1</pre>
<p>You can change the tape device when amrecover ask you to load the tape: </p>
<pre>Load tape DMP014 now
Continue? [Y/n/t]: t
Tape device: server2:/dev/nst2
Continue? [Y/n/t]: Y
Using tape /dev/nst2 from server server2.</pre>
</dl>
<p> <code>setmode</code> <i>mode</i></p>
<dl>
<dd>Set the extraction mode for Samba shares. If <i>mode</i> is <code>smb</code>, shares are sent to the Samba server to be restored back onto the PC. If <i>mode</i> is <code>tar</code>, they are extracted on the local machine the same way tar volumes are extracted.</dl>
<p> <code>settranslate</code> [<code>on</code>|<code>off</code>]</p>
<dl>
<dd>Default: on. Translate escaped octal value (&#8216;
