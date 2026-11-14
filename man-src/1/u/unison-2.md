---
title: "unison-2(1)"
name: "unison-2"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unison-2/"
description: "unison-2.40.102 – a file-synchronization tool for Unix and Windows"
---

<h2 class="name">NAME</h2>
<p> unison-2.40.102 &#8211; a file-synchronization tool for Unix and Windows </p>
<h2>SYNOPSIS</h2>
<p> <code>unison-2.40.102</code> [<i>options</i>]<br />
 <code>unison-2.40.102</code> root1 root2 [<i>options</i>]<br />
 <code>unison-2.40.102</code> profilename [<i>options</i>]<br />
 <code>unison-2.40.102-gtk</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents Unison, and was written for the Debian GNU/Linux distribution because the original program does not have a manual page. For a full description, please refer to the inbuilt documentation or the manuals in /usr/share/doc/unison/. The unison-2.40.102-gtk binary has similar command-line options, but allows the user to select and create profiles and configure options from within the program. </p>
<p> Unison is a file-synchronization tool for Unix and Windows. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other. </p>
<p> Unison offers several advantages over various synchronization methods such as CVS, Coda, rsync, Intellisync, etc. Unison can run on and synchronize between Windows and many UNIX platforms. Unison requires no root privileges, system access or kernel changes to function. Unison can synchronize changes to files and directories in both directions, on the same machine, or across a network using ssh or a direct socket connection. </p>
<p> Transfers are optimised using a version of the rsync protocol, making it ideal for slower links. Unison has a clear and precise specification, and is resilient to failure due to its careful handling of the replicas and its private structures. </p>
<p> The two roots can be specified using an URI or a path. The URI must follow the convention: protocol://[user@][host][:port][/path]. The protocol part can be file, socket, ssh or rsh.</p>
<h2>OPTIONS</h2>
<p> All Unison options are long, starting with one dash (`-&#8216;) only. A summary of options is included here. For a complete description, see the inbuilt documentation or the manuals in /usr/share/doc/unison/.</p>
<dl>
<dt><code>-auto</code></p>
<dd> automatically accept default (nonconflicting) actions</p>
<dt><code>-batch</code></p>
<dd> batch mode: ask no questions at all</p>
<dt><code>-doc xxx</code></p>
<dd> show documentation (&#8216;-doc topics&#8217; lists topics)</p>
<dt><code>-fat</code></p>
<dd> use appropriate options for FAT filesystems</p>
<dt><code>-group</code></p>
<dd> synchronize group attributes</p>
<dt><code>-ignore xxx</code></p>
<dd> add a pattern to the ignore list</p>
<dt><code>-ignorenot xxx</code></p>
<dd> add a pattern to the ignorenot list</p>
<dt><code>-nocreation xxx</code></p>
<dd> prevent file creations on one replica</p>
<dt><code>-nodeletion xxx</code></p>
<dd> prevent file deletions on one replica</p>
<dt><code>-noupdate xxx</code></p>
<dd> prevent file updates and deletions on one replica</p>
<dt><code>-owner</code></p>
<dd> synchronize owner</p>
<dt><code>-path xxx</code></p>
<dd> path to synchronize</p>
<dt><code>-perms n</code></p>
<dd> part of the permissions which is synchronized</p>
<dt><code>-root xxx</code></p>
<dd> root of a replica (should be used exactly twice)</p>
<dt><code>-silent</code></p>
<dd> print nothing except error messages</p>
<dt><code>-terse</code></p>
<dd> suppress status messages</p>
<dt><code>-testserver</code></p>
<dd> exit immediately after the connection to the server</p>
<dt><code>-times</code></p>
<dd> synchronize modification times</p>
<dt><code>-version</code></p>
<dd> print version and exit</p>
<dt><code>-addprefsto xxx</code></p>
<dd> file to add new prefs to</p>
<dt><code>-addversionno</code></p>
<dd> add version number to name of unison on server</p>
<dt><code>-backup xxx</code></p>
<dd> add a pattern to the backup list</p>
<dt><code>-backupcurr xxx</code></p>
<dd> add a pattern to the backupcurr list</p>
<dt><code>-backupcurrnot xxx</code></p>
<dd> add a pattern to the backupcurrnot list</p>
<dt><code>-backupdir xxx</code></p>
<dd> directory for storing centralized backups</p>
<dt><code>-backuploc xxx</code></p>
<dd> where backups are stored (&#8216;local&#8217; or &#8216;central&#8217;)</p>
<dt><code>-backupnot xxx</code></p>
<dd> add a pattern to the backupnot list</p>
<dt><code>-backupprefix xxx</code></p>
<dd> prefix for the names of backup files</p>
<dt><code>-backups</code></p>
<dd> keep backup copies of all files (see also &#8216;backup&#8217;)</p>
<dt><code>-backupsuffix xxx</code></p>
<dd> a suffix to be added to names of backup files</p>
<dt><code>-confirmbigdel</code></p>
<dd> ask about whole-replica (or path) deletes (default true)</p>
<dt><code>-confirmmerge</code></p>
<dd> ask for confirmation before committing results of a merge</p>
<dt><code>-contactquietly</code></p>
<dd> suppress the &#8216;contacting server&#8217; message during startup</p>
<dt><code>-copymax n</code></p>
<dd> maximum number of simultaneous copyprog transfers</p>
<dt><code>-copyprog xxx</code></p>
<dd> external program for copying large files</p>
<dt><code>-copyprogrest xxx</code></p>
<dd> variant of copyprog for resuming partial transfers</p>
<dt><code>-copyquoterem xxx</code></p>
<dd> add quotes to remote file name for copyprog (true/false/default)</p>
<dt><code>-copythreshold n</code></p>
<dd> use copyprog on files bigger than this (if &gt;=0, in Kb)</p>
<dt><code>-debug xxx</code></p>
<dd> debug module xxx (&#8216;all&#8217; -&gt; everything, &#8216;verbose&#8217; -&gt; more)</p>
<dt><code>-diff xxx</code></p>
<dd> set command for showing differences between files</p>
<dt><code>-dontchmod</code></p>
<dd> when set, never use the chmod system call</p>
<dt><code>-dumbtty</code></p>
<dd> do not change terminal settings in text UI</p>
<dt><code>-fastcheck xxx</code></p>
<dd> do fast update detection (true/false/default)</p>
<dt><code>-follow xxx</code></p>
<dd> add a pattern to the follow list</p>
<dt><code>-force xxx</code></p>
<dd> force changes from this replica to the other</p>
<dt><code>-forcepartial xxx</code></p>
<dd> add a pattern to the forcepartial list</p>
<dt><code>-halfduplex</code></p>
<dd> force half-duplex communication with the server</p>
<dt><code>-height n</code></p>
<dd> height (in lines) of main window in graphical interface</p>
<dt><code>-host xxx</code></p>
<dd> bind the socket to this host name in server socket mode</p>
<dt><code>-ignorearchives</code></p>
<dd> ignore existing archive files</p>
<dt><code>-ignorecase xxx</code></p>
<dd> identify upper/lowercase filenames (true/false/default)</p>
<dt><code>-ignoreinodenumbers</code></p>
<dd> ignore inode number changes when detecting updates</p>
<dt><code>-ignorelocks</code></p>
<dd> ignore locks left over from previous run (dangerous!)</p>
<dt><code>-immutable xxx</code></p>
<dd> add a pattern to the immutable list</p>
<dt><code>-immutablenot xxx</code></p>
<dd> add a pattern to the immutablenot list</p>
<dt><code>-key xxx</code></p>
<dd> define a keyboard shortcut for this profile (in some UIs)</p>
<dt><code>-killserver</code></p>
<dd> kill server when done (even when using sockets)</p>
<dt><code>-label xxx</code></p>
<dd> provide a descriptive string label for this profile</p>
<dt><code>-links xxx</code></p>
<dd> allow the synchronization of symbolic links (true/false/default)</p>
<dt><code>-log</code></p>
<dd> record actions in logfile (default true)</p>
<dt><code>-logfile xxx</code></p>
<dd> logfile name</p>
<dt><code>-maxbackups n</code></p>
<dd> number of backed up versions of a file</p>
<dt><code>-maxerrors n</code></p>
<dd> maximum number of errors before a directory transfer is aborted</p>
<dt><code>-maxthreads n</code></p>
<dd> maximum number of simultaneous file transfers</p>
<dt><code>-merge xxx</code></p>
<dd> add a pattern to the merge list</p>
<dt><code>-mountpoint xxx</code></p>
<dd> abort if this path does not exist</p>
<dt><code>-nocreationpartial xxx</code></p>
<dd> add a pattern to the nocreationpartial list</p>
<dt><code>-nodeletionpartial xxx</code></p>
<dd> add a pattern to the nodeletionpartial list</p>
<dt><code>-noupdatepartial xxx</code></p>
<dd> add a pattern to the noupdatepartial list</p>
<dt><code>-numericids</code></p>
<dd> don&#8217;t map uid/gid values by user/group names</p>
<dt><code>-prefer xxx</code></p>
<dd> choose this replica&#8217;s version for conflicting changes</p>
<dt><code>-preferpartial xxx</code></p>
<dd> add a pattern to the preferpartial list</p>
<dt><code>-repeat xxx</code></p>
<dd> synchronize repeatedly (text interface only)</p>
<dt><code>-retry n</code></p>
<dd> re-try failed synchronizations N times (text ui only)</p>
<dt><code>-rootalias xxx</code></p>
<dd> register alias for canonical root names</p>
<dt><code>-rsrc xxx</code></p>
<dd> synchronize resource forks (true/false/default)</p>
<dt><code>-rsync</code></p>
<dd> activate the rsync transfer mode (default true)</p>
<dt><code>-selftest</code></p>
<dd> run internal tests and exit</p>
<dt><code>-servercmd xxx</code></p>
<dd> name of unison executable on remote server</p>
<dt><code>-showarchive</code></p>
<dd> show &#8216;true names&#8217; (for rootalias) of roots and archive</p>
<dt><code>-socket xxx</code></p>
<dd> act as a server on a socket</p>
<dt><code>-sortbysize</code></p>
<dd> list changed files by size, not name</p>
<dt><code>-sortfirst xxx</code></p>
<dd> add a pattern to the sortfirst list</p>
<dt><code>-sortlast xxx</code></p>
<dd> add a pattern to the sortlast list</p>
<dt><code>-sortnewfirst</code></p>
<dd> list new before changed files</p>
<dt><code>-sshargs xxx</code></p>
<dd> other arguments (if any) for remote shell command</p>
<dt><code>-sshcmd xxx</code></p>
<dd> path to the ssh executable</p>
<dt><code>-stream</code></p>
<dd> use a streaming protocol for transferring file contents (default true)</p>
<dt><code>-ui xxx</code></p>
<dd> select UI (&#8216;text&#8217; or &#8216;graphic&#8217;); command-line only</p>
<dt><code>-unicode xxx</code></p>
<dd> assume Unicode encoding in case insensitive mode</p>
<dt><code>-xferbycopying</code></p>
<dd> optimize transfers using local copies (default true)</dl>
<p> Some preferences are just boolean flags. Others take numeric or string arguments, indicated in the preferences list by n or xxx. Most of the string preferences can be given several times; the arguments are accumulated into a list internally.</p>
<h2>SEE ALSO</h2>
<p> The program is documented fully in the in-built documentation and the manual, available as text in /usr/share/doc/unison/.</p>
<h2>AUTHOR</h2>
<p> Options are automatically extracted from `unison -help&#8217;. The rest of this manual page was written by Robert McQueen &lt;robot101 [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
