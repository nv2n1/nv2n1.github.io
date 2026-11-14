---
title: "afpcmd(1)"
name: "afpcmd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afpcmd/"
description: "afpcmd – Transfer files over the networking using the Apple Filing Protocol (AFP)"
---

<h2>NAME</h2>
<p> afpcmd &#8211; Transfer files over the networking using the Apple Filing Protocol (AFP)</p>
<h2>SYNOPSIS</h2>
<p> <i>afpcmd</i> [<code>-r</code> [<code>afp url</code>] </p>
<h2>DESCRIPTION</h2>
<p> afpcmd is a command-line tool to help transfer files to and from a server using AFP. This is typically either Netatalk or Mac OS or Mac OS X. </p>
<p> This can be done as a non-root user. It offers either an interactive command-line (like a traditional FTP client) or for batch retrievals. </p>
<p> Do not confuse this with the FUSE mounting tools (mount_afp, afpfsd, afp_client), which offer the ability to mount an entire filesystem. </p>
<h2>OPTIONS</h2>
<p> <code>-r</code> sets the recursive flag. </p>
<p> <code>afp url</code> uses the standard AFP URL format. </p>
<h2>AFP version support</h2>
<p> Look at the afpfs-ng documentation for more information on specific AFP version compatibility information. </p>
<h2>Batch mode</h2>
<p> Batch file transfers can be done in one of two ways: </p>
<p> <i>afpcmd -r [</i><code>afp url to directory</code>] </p>
<p> This does a recursive transfer of all subdirectories and files locally. </p>
<p> <i>afpcmd [</i><code>afp url to file</code>] </p>
<p> This transfers just the file locally. </p>
<p> After either of these is finished, the command exits. </p>
<h2>Interactive mode</h2>
<p> If a URL is provided on the command line, afpcmd connects and enters the volume and directory specified. </p>
<p> Standard readline keystrokes are enabled. Command line competion (using tab) and history (using up and down arrows) is provided. Local filename completion is enabled. </p>
<p> <code>Most common commands</code> </p>
<p> <i>connect</i> &lt;afp URL&gt;: Connect to server, change to volume and directory </p>
<p> <i>cd</i>: Change directories on the server </p>
<p> <i>get</i> &lt;filename&gt;: retrieve file </p>
<p> <i>get</i> -r &lt;directory&gt;: Recursively retrieve the directory </p>
<p> <i>put</i> &lt;filename&gt;: Upload file </p>
<p> <i>quit</i>: Quit </p>
<p> <code>Conect/disconnect commands</code> </p>
<p> <i>disconnect</i>: Disconnect from current server </p>
<p> <i>passwd</i>: Prompts for a new password without showing on screen </p>
<p> <i>user</i> &lt;user&gt;: Set the user </p>
<p> <i>passwd</i>: change the password on the server. Does not work. </p>
<p> <code>Remote directory commands</code> </p>
<p> <i>pwd</i>: Show current directory on server </p>
<p> <i>mkdir</i> &lt;directory&gt;: create new directory </p>
<p> <i>rmdir</i> &lt;directory: remove directory </p>
<p> <i>ls</i> or <i>dir</i>: show files in current directory </p>
<p> <code>Remote file commands</code> </p>
<p> <i>mv</i> or <i>rename</i> old_file new_file: Rename &lt;old file&gt; to &lt;new file&gt; </p>
<p> <i>touch</i> &lt;filename&gt;: Create a blank file </p>
<p> <i>view</i> &lt;filename&gt;: Show file </p>
<p> <i>chmod</i>: &lt;file&gt; &lt;mode&gt;: Change the mode of a file on the server </p>
<p> <i>delete</i> of <i>rm</i>: &lt;file&gt;: Remove file from the server </p>
<p> <code>Status commands</code> </p>
<p> <i>status</i>: Show status of the connection and details. For debugging. </p>
<p> <i>df</i>: Show the disk size and available blocks. </p>
<p> <code>Local commands</code> </p>
<p> <i>lpwd</i>: Show current local </p>
<p> <i>lcd</i>: Change local directory </p>
<p> <code>Other commands</code> </p>
<p> <i>help</i> or <i>?</i>: show help </p>
<p> <i>testafp</i>: various tests for developers </p>
<h2>AFP URLs</h2>
<p> A typical usage of afpcmd is: </p>
<p> <i>afpcmd</i> <a href="afp://username:password@servername/volume">afp://username:password@servername/volume</a> </p>
<p> The complete syntax of a URL is: </p>
<p> <a href="afp://username;AUTH=authtype:password@server:port/volume/path">afp://username;AUTH=authtype:password@server:port/volume/path</a> </p>
<p> If a password of &quot;-&quot; is provided, the user is prompted for a password. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the afpfs-ng-devel [at] sf.net mailing list.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-afpgetstatus/">afpgetstatus</a></code>(1) </p>
<h2>Index</h2>
