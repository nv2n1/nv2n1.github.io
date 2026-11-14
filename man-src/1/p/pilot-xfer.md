---
title: "pilot-xfer(1)"
name: "pilot-xfer"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot-xfer/"
description: "pilot-xfer – Backup, sync, and restore databases from a Palm handheld device."
---

<h2>NAME</h2>
<p> pilot-xfer &#8211; Backup, sync, and restore databases from a Palm handheld device.</p>
<h2>SECTION</h2>
<p> pilot-link: Userland conduits </p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr><i>pilot-xfer</i>&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>-e</code>&nbsp;<wbr>&lt;<i>file</i>&gt;]&nbsp;<wbr>[<code>-b</code>]&nbsp;<wbr>[<code>-u</code>]&nbsp;<wbr>[<code>-s</code>]&nbsp;<wbr>&lt;<i>directory</i>&gt; </p>
<p> or </p>
<p>&nbsp;<wbr><i>pilot-xfer</i>&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>&lt;<code>port</code>&gt;]&nbsp;<wbr>[<code>-r</code>&nbsp;<wbr>&lt;<code>directory</code>&gt;]&nbsp;<wbr>[<code>-l</code>]&nbsp;<wbr>[<code>-L</code>]&nbsp;<wbr>[<code>-P</code>]&nbsp;<wbr>[<code>-f</code>&nbsp;<wbr>&lt;<code>dbname</code>&gt;]&nbsp;<wbr>[<code>-d</code>&nbsp;<wbr>&lt;<code>dbname</code>&gt;]&nbsp;<wbr>[<code>-i</code>&nbsp;<wbr>&lt;<code>dbname</code>&gt;]&nbsp;<wbr>[<code>-m</code>&nbsp;<wbr>&lt;<i>file</i>&gt;]&nbsp;<wbr>&#8230; </p>
<p> Use exactly one of -brsudfimlI; mix in -aexDPv, &#8211;rom and with-os. </p>
<h2>DESCRIPTION</h2>
<p> This is the swiss-army-knife of the entire pilot-link suite. </p>
<p>&nbsp;<wbr><i>pilot-xfer</i>&nbsp;<wbr>allows the user to install databases contained in the standard .prc&nbsp;<wbr>(Palm Resource Database), .pdb&nbsp;<wbr>(Palm Record Database), and .pqa&nbsp;<wbr>(Palm Query Application)&nbsp;<wbr>formats onto a Palm, retrieve databases from the Palm, list the databases contained in a Palm, backup or restore all of the databases at once as well as many other powerful operations performed on a Palm handheld device. </p>
<h2>OPTIONS</h2>
<h3>pilot-xfer options</h3>
<p> Archive files which have been removed from the Palm to &lt;<i>dir</i>&gt; instead of just deleting (unlinking) them. </p>
<pre>
   <code>-a</code>, <code>--archive</code>
   &lt;<i>dir</i>&gt;
                        
</pre>
<p> Back up the Palm into the specified directory (which will be created if it does not already exist). </p>
<pre>
   <code>-b</code>, <code>--backup</code>
   &lt;<i>dir</i>&gt;
</pre>
<p> Show information on available cards </p>
<pre>
   <code>-C</code>, <code>--cardinfo</code>
</pre>
<p> Permanently delete the specified database(s) by name (without extension). Obviously, be very careful with this one. </p>
<pre>
   --delete &lt;<code>dbname</code>&gt;
</pre>
<p> Modify <code>-l</code>, <code>-i</code> or <code>-f</code> to use VFS <i>dir</i> instead of internal storage (see examples section for usage) </p>
<pre>
   <code>-D</code>,
   <code>--vfsdir</code>=<i>dir</i>
</pre>
<p> Reads a list of databases from &lt;<i>file</i>&gt; and prevents <code>&#8211;backup</code>, <code>&#8211;sync</code>, or <code>&#8211;update</code> from operating on the listed database(s). A maximum of 100 databases can be excluded. Databases should be specified by name without the extension, as displayed with &#8211;list, in any order. </p>
<pre>
   <code>-e</code>, --exclude=
   <i>&lt;</i><code>file</code>&gt;
</pre>
<p> Fetch each specified database out of the Palm into the current directory. </p>
<p> Obsolete. Replaced by <code>&#8211;rom</code> in v0.12. </p>
<pre>
   <code>-F</code>, <code>--Flash</code>
</pre>
<p> Install each specified file into the Palm. Wildcards are valid with this syntax and multiple files may be listed at once. </p>
<pre>
   <code>-i</code>, --install
   &lt;<i>file</i>&gt; [...]
</pre>
<p> Note: the behavior of list has changed in version 0.12 and later </p>
<p> List all the databases in the Palm, including OS-specific native databases. </p>
<pre>
   <code>-l</code>, <code>--list</code>
</pre>
<p> Unsupported in 0.12 &#8211; see <code>-l</code> </p>
<pre>
   <code>-L</code>, <code>--Listall</code>
</pre>
<p> Adds the records in each specified file into the corresponding Palm database. </p>
<pre>
   <code>-m</code>, <code>--merge</code>
   &lt;<i>file1</i>&gt; &lt;file2&gt; [...]
</pre>
<p> Obsolete. Replaced by <code>&#8211;with-os</code> in v0.12 and later </p>
<pre>
   <code>-O</code>, --<code>Osflash</code>
</pre>
<p> Purge any deleted data that haven&#8217;t been cleaned up by a full synchronization (this is a safe operation, and will prevent your Palm from accumulating unused data if you delete records but aren&#8217;t syncing with a PIM.) The only information you can lose is archived but un-synchronized records. </p>
<pre>
   <code>-P</code>, <code>--Purge</code>
</pre>
<p> Installs all files contained in the named directory to the Palm. (Use this to restore your Palm after a hard reset has cleared and wiped its memory, using your backup directory as a baseline). </p>
<pre>
   <code>-r</code>, <code>--restore</code>
   &lt;<i>dir</i>&gt;
</pre>
<p> Modifies <code>-b</code>, <code>-u</code>, and <code> s </code>, to back up non-OS dbs from the internal Flash ROM </p>
<pre>
   <code>--rom</code>
</pre>
<p> Backs up the Palm into the specified directory (which will be created if it does not already exist). Any Palm databases which have not been modified or created since the versions stored in the specified directory will not be backed up. </p>
<p>&nbsp;<wbr><i>NOTE</i>: Any Palm databases which have been deleted will have their corresponding backup file removed. </p>
<pre>
   <code>-s</code>, <code>--sync</code>
   &lt;<i>dir</i>&gt;
</pre>
<p> Not supported in v0.12. No replacement. </p>
<pre>
   <code>-S</code>, <code>--novsf</code>
</pre>
<p> Modifies <code>-b</code>, <code>-u</code>, and <code> s </code>, to back up OS databases from internal Flash ROM. </p>
<pre>
   <code>--with-os</code>
</pre>
<p> Backs up the Palm into the specified directory (which will be created if it does not already exist). Any Palm databases which have not been modified or created since the versions stored in the specified directory will not be backed up. </p>
<pre>
   <code>-u</code>, <code>--update</code>
</pre>
<p> This will back up the UnsavedPreferences.prc file from the Palm. Normally this file is not backed up by normal means (Palm recommends that you do not restore this file upon restoration of your device using <code>&#8211;restore</code>. </p>
<p> This also modifies the behavior of <code>&#8211;backup</code>, <code>&#8211;sync</code>, and <code>&#8211;update</code>. </p>
<pre>
   <code>-I</code>, <code>--Illegal</code>
</pre>
<p> Execute a shell command for intermediate processing. All commands will be done, from left to right on the command-line, before the connection to the Palm device is made. </p>
<pre>
   <code>-x</code>, <code>--exec=command</code>
</pre>
<h3>Conduit Options</h3>
<p> Use device file &lt;<i>port</i>&gt; to communicate with the Palm handheld. If this is not specified, <i>pilot-xfer</i> will look for the <i>$PILOTPORT</i> environment variable. If neither are found, <i> pilot-xfer </i> will print the usage information. </p>
<pre>
   <code>-p</code>, <code>--port</code>
   &lt;<code>port</code>&gt;
</pre>
<p> Display version of <i>pilot-xfer</i> and exit without connecting. </p>
<pre>
   <code>-v</code>, <code>--version</code>
</pre>
<h3>Help Options</h3>
<p> Display the help synopsis for <i>pilot-xfer</i> and exit without connecting. </p>
<pre>
   <code>-h</code>, <code>--help</code>
</pre>
<p> Display a brief usage message and exit without connecting. </p>
<pre>
   <code>--usage</code>
</pre>
<h2>USAGE</h2>
<p> The program will attempt to connect to a target Palm handheld device and specified port and perform the requested options specified by the user on the commandline. </p>
<h2>EXAMPLES</h2>
<p> To perform a full backup of your Palm handheld: </p>
<p> # using long options </p>
<p>&nbsp;<wbr> </p>
<pre>
   <i>pilot-xfer</i> <code>--port</code> <i>/dev/pilot</i> <code>--backup</code> <i>$HOME/pilot/Backup</i>
            
</pre>
<p>&nbsp;<wbr> </p>
<p> # or over IrDA, using short options </p>
<p>&nbsp;<wbr> </p>
<pre>
   <i>pilot-xfer</i> <code>-p</code> <i>/dev/ircomm0</i> <code>-b</code> <i>$HOME/pilot/Backup</i>
            
</pre>
<p>&nbsp;<wbr> </p>
<p> To restore that backup to a non-standard serial port (for example, to a xcopilot or POSE session, assuming you have xcopilot or POSE configured properly for this operation, see the appropriate man pages for details on configuring your emulator): </p>
<p>&nbsp;<wbr> </p>
<pre>
   <i>pilot-xfer</i> <code>-p</code> <i>/dev/ttyqe</i> <code>--restore</code> <i>$HOME/pilot/Backup</i>
            
</pre>
<p>&nbsp;<wbr> </p>
<p> To fetch a file that is on your Palm handheld, such as the Palm Address Book database, you could do the following. This will connect to /dev/pilot and retrieve the records found in AddressDB and place them in a local file called AddressDB.pdb (Palm Record Database). </p>
<p>&nbsp;<wbr> </p>
<pre>
   <i>pilot-xfer</i> <code>-p</code> <i>/dev/pilot</i> <code>--fetch</code> <code>AddressDB</code> 
            
</pre>
<p>&nbsp;<wbr> </p>
<p> This will connect to your Palm device and install the application Foo (in Foo.prc) to your external storage card (typically an SD or MMC card) in the directory /Palm/Launcher on that card, using VFS. </p>
<p>&nbsp;<wbr> </p>
<pre>
   <i>pilot-xfer</i> <code>-p</code> <i>/dev/pilot</i> <code>-i Foo.prc -D /Palm/Launcher</code>
            
</pre>
<p>&nbsp;<wbr> </p>
<h2>AUTHOR</h2>
<p>&nbsp;<wbr><i>pilot-xfer</i>&nbsp;<wbr>written by Kenneth Albanowski. This manual page was originally written by Kenneth Albanowski and David H. Silber. Completely rewritten by David A. Desrosiers. Updated for 0.12 by Neil Williams&nbsp;<wbr>&lt;&nbsp;<wbr>linux [at] codehelp.co.uk&nbsp;<wbr>&gt;&nbsp;<wbr>. </p>
<h2>BUGS</h2>
<h3>Known Bugs</h3>
<p>&nbsp;<wbr><code>&#8211;backup</code>&nbsp;<wbr>will currently truncate/corrupt pdb/prc files if the communication to the device is interrupted during sync&nbsp;<wbr>(such as removing the Palm from the cradle, or a temporary network hiccup during a NetSync). Ideally, this should restore the original file, or delete the corrupted version and restore the original version back into place, but presently.. it does not. </p>
<h3>Reporting Bugs</h3>
<p> We have an online bug tracker. Using this is the only way to ensure that your bugs are recorded and that we can track them until they are resolved or closed. Reporting bugs via email, while easy, is not very useful in terms of accountability. Please point your browser to <a rel="nofollow" href="http://bugs.pilot-link.org:">http://bugs.pilot-link.org:</a> <i><a href="http://bugs.pilot-link.org">http://bugs.pilot-link.org</a></i> and report your bugs and issues there. </p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><i><a href="/docs/linux/man/7-pilot-link/">pilot-link</a></i>(7) </p>
<h2>Index</h2>
