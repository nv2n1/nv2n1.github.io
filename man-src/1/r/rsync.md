---
title: "rsync(1)"
name: "rsync"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsync/"
description: "rsync – a fast, versatile, remote (and local) file-copying tool"
---
<h2 class="name">NAME</h2>
<p> rsync - a fast, versatile, remote (and local) file-copying tool  </p>
<h2>SYNOPSIS</h2>
<pre><code>Local:
    rsync [OPTION...] SRC... [DEST]
Access via remote shell:
    Pull:
        rsync [OPTION...] [USER@]HOST:SRC... [DEST]
    Push:
        rsync [OPTION...] SRC... [USER@]HOST:DEST
Access via rsync daemon:
    Pull:
        rsync [OPTION...] [USER@]HOST::SRC... [DEST]
        rsync [OPTION...]rsync://[USER@]HOST[:PORT]/SRC... [DEST]
    Push:
        rsync [OPTION...] SRC... [USER@]HOST::DEST
        rsync [OPTION...] SRC...rsync://[USER@]HOST[:PORT]/DEST)
</code></pre>
<p> Usages with just one SRC arg and no DEST arg will list the source files instead of copying. </p>
<p> The online version of this manpage (that includes cross-linking of topics) is available at <a rel="nofollow" href="https://download.samba.org/pub/rsync/rsync.1.">https://download.samba.org/pub/rsync/rsync.1.</a> </p>
<h2>DESCRIPTION</h2>
<p> Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from another host over any remote shell, or to/from a remote rsync daemon. It offers a large number of options that control every aspect of its behavior and permit very flexible specification of the set of files to be copied. It is famous for its delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the differences between the source files and the existing files in the destination. Rsync is widely used for backups and mirroring and as an improved copy command for everyday use. </p>
<p> Rsync finds files that need to be transferred using a &quot;quick check&quot; algorithm (by default) that looks for files that have changed in size or in last-modified time. Any changes in the other preserved attributes (as requested by options) are made on the destination file directly when the quick check indicates that the file&#8217;s data does not need to be updated. </p>
<p> Some of the additional features of rsync are: </p>
<dl>
<dt>o</dt>
<dd> <p> support for copying links, devices, owners, groups, and permissions </p>
 </dd>
<dt>o</dt>
<dd> <p> exclude and exclude-from options similar to GNU tar </p>
 </dd>
<dt>o</dt>
<dd> <p> a CVS exclude mode for ignoring the same files that CVS would ignore </p>
 </dd>
<dt>o</dt>
<dd> <p> can use any transparent remote shell, including ssh or rsh </p>
 </dd>
<dt>o</dt>
<dd> <p> does not require super-user privileges </p>
 </dd>
<dt>o</dt>
<dd> <p> pipelining of file transfers to minimize latency costs </p>
 </dd>
<dt>o</dt>
<dd> <p> support for anonymous or authenticated rsync daemons (ideal for mirroring) </p>
 </dd></dl>
<h2>GENERAL</h2>
<p> Rsync copies files either to or from a remote host, or locally on the current host (it does not support copying files between two remote hosts). </p>
<p> There are two different ways for rsync to contact a remote system: using a remote-shell program as the transport (such as ssh or rsh) or contacting an rsync daemon directly via TCP. The remote-shell transport is used whenever the source or destination path contains a single colon (:) separator after a host specification. Contacting an rsync daemon directly happens when the source or destination path contains a double colon (::) separator after a host specification, OR when an rsync:// URL is specified (see also the USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION section for an exception to this latter rule). </p>
<p> As a special case, if a single source arg is specified without a destination, the files are listed in an output format similar to &quot;<code>ls -l</code>&quot;. </p>
<p> As expected, if neither the source or destination path specify a remote host, the copy occurs locally (see also the <code>--list-only</code> option). </p>
<p> Rsync refers to the local side as the client and the remote side as the server. Don&#8217;t confuse server with an rsync daemon. A daemon is always a server, but a server can be either a daemon or a remote-shell spawned process. </p>
<h2>SETUP</h2>
<p> See the file README.md for installation instructions. </p>
<p> Once installed, you can use rsync to any machine that you can access via a remote shell (as well as some that you can access using the rsync daemon-mode protocol). For remote transfers, a modern rsync uses ssh for its communications, but it may have been configured to use a different remote shell by default, such as rsh or remsh. </p>
<p> You can also specify any remote shell you like, either by using the <code>-e</code> command line option, or by setting the <code>RSYNC_RSH</code> environment variable. </p>
<p> Note that rsync must be installed on both the source and destination machines. </p>
<h2>USAGE</h2>
<p> You use rsync in the same way you use rcp. You must specify a source and a destination, one of which may be remote. </p>
<p> Perhaps the best way to explain the syntax is with some examples: </p>
<dl>
<dd> <pre><code>rsync -t *.c foo:src/
</code></pre>
 </dd></dl>
<p> This would transfer all files matching the pattern <code>*.c</code> from the current directory to the directory src on the machine foo. If any of the files already exist on the remote system then the rsync remote-update protocol is used to update the file by sending only the differences in the data. Note that the expansion of wildcards on the command-line (<code>*.c</code>) into a list of files is handled by the shell before it runs rsync and not by rsync itself (exactly the same as all other Posix-style programs). </p>
<dl>
<dd> <pre><code>rsync -avz foo:src/bar /data/tmp
</code></pre>
 </dd></dl>
<p> This would recursively transfer all files from the directory src/bar on the machine foo into the /data/tmp/bar directory on the local machine. The files are transferred in archive mode, which ensures that symbolic links, devices, attributes, permissions, ownerships, etc. are preserved in the transfer. Additionally, compression will be used to reduce the size of data portions of the transfer. </p>
<dl>
<dd> <pre><code>rsync -avz foo:src/bar/ /data/tmp
</code></pre>
 </dd></dl>
<p> A trailing slash on the source changes this behavior to avoid creating an additional directory level at the destination. You can think of a trailing / on a source as meaning &quot;copy the contents of this directory&quot; as opposed to &quot;copy the directory by name&quot;, but in both cases the attributes of the containing directory are transferred to the containing directory on the destination. In other words, each of the following commands copies the files in the same way, including their setting of the attributes of /dest/foo: </p>
<dl>
<dd> <pre><code>rsync -av /src/foo /dest
rsync -av /src/foo/ /dest/foo
</code></pre>
 </dd></dl>
<p> Note also that host and module references don&#8217;t require a trailing slash to copy the contents of the default directory. For example, both of these copy the remote directory&#8217;s contents into &quot;/dest&quot;: </p>
<dl>
<dd> <pre><code>rsync -av host: /dest
rsync -av host::module /dest
</code></pre>
 </dd></dl>
<p> You can also use rsync in local-only mode, where both the source and destination don&#8217;t have a &#8216;:&#8216; in the name. In this case it behaves like an improved copy command. </p>
<p> Finally, you can list all the (listable) modules available from a particular rsync daemon by leaving off the module name: </p>
<dl>
<dd> <pre><code>rsync somehost.mydomain.com::
</code></pre>
 </dd></dl>
<h2>COPYING TO A DIFFERENT NAME</h2>
<p> When you want to copy a directory to a different name, use a trailing slash on the source directory to put the contents of the directory into any destination directory you like: </p>
<dl>
<dd> <pre><code>rsync -ai foo/ bar/
</code></pre>
 </dd></dl>
<p> Rsync also has the ability to customize a destination file&#8217;s name when copying a single item. The rules for this are: </p>
<dl>
<dt>o</dt>
<dd> <p> The transfer list must consist of a single item (either a file or an empty directory) </p>
 </dd>
<dt>o</dt>
<dd> <p> The final element of the destination path must not exist as a directory </p>
 </dd>
<dt>o</dt>
<dd> <p> The destination path must not have been specified with a trailing slash </p>
 </dd></dl>
<p> Under those circumstances, rsync will set the name of the destination&#8217;s single item to the last element of the destination path. Keep in mind that it is best to only use this idiom when copying a file and use the above trailing-slash idiom when copying a directory. </p>
<p> The following example copies the <code>foo.c</code> file as <code>bar.c</code> in the <code>save</code> dir (assuming that <code>bar.c</code> isn&#8217;t a directory): </p>
<dl>
<dd> <pre><code>rsync -ai src/foo.c save/bar.c
</code></pre>
 </dd></dl>
<p> The single-item copy rule might accidentally bite you if you unknowingly copy a single item and specify a destination dir that doesn&#8217;t exist (without using a trailing slash). For example, if <code>src/*.c</code> matches one file and <code>save/dir</code> doesn&#8217;t exist, this will confuse you by naming the destination file <code>save/dir</code>: </p>
<dl>
<dd> <pre><code>rsync -ai src/*.c save/dir
</code></pre>
 </dd></dl>
<p> To prevent such an accident, either make sure the destination dir exists or specify the destination path with a trailing slash: </p>
<dl>
<dd> <pre><code>rsync -ai src/*.c save/dir/
</code></pre>
 </dd></dl>
<h2>SORTED TRANSFER ORDER</h2>
<p> Rsync always sorts the specified filenames into its internal transfer list. This handles the merging together of the contents of identically named directories, makes it easy to remove duplicate filenames. It can, however, confuse someone when the files are transferred in a different order than what was given on the command-line. </p>
<p> If you need a particular file to be transferred prior to another, either separate the files into different rsync calls, or consider using <code>--delay-updates</code> (which doesn&#8217;t affect the sorted transfer order, but does make the final file-updating phase happen much more rapidly). </p>
<h2>MULTI-HOST SECURITY</h2>
<p> Rsync takes steps to ensure that the file requests that are shared in a transfer are protected against various security issues. Most of the potential problems arise on the receiving side where rsync takes steps to ensure that the list of files being transferred remains within the bounds of what was requested. </p>
<p> Toward this end, rsync 3.1.2 and later have aborted when a file list contains an absolute or relative path that tries to escape out of the top of the transfer. Also, beginning with version 3.2.5, rsync does two more safety checks of the file list to (1) ensure that no extra source arguments were added into the transfer other than those that the client requested and (2) ensure that the file list obeys the exclude rules that were sent to the sender. </p>
<p> For those that don&#8217;t yet have a 3.2.5 client rsync (or those that want to be extra careful), it is safest to do a copy into a dedicated destination directory for the remote files when you don&#8217;t trust the remote host. For example, instead of doing an rsync copy into your home directory: </p>
<dl>
<dd> <pre><code>rsync -aiv host1:dir1 ~
</code></pre>
 </dd></dl>
<p> Dedicate a &quot;host1-files&quot; dir to the remote content: </p>
<dl>
<dd> <pre><code>rsync -aiv host1:dir1 ~/host1-files
</code></pre>
 </dd></dl>
<p> See the <code>--trust-sender</code> option for additional details. </p>
<p> CAUTION: it is not particularly safe to use rsync to copy files from a case-preserving filesystem to a case-ignoring filesystem. If you must perform such a copy, you should either disable symlinks via <code>--no-links</code> or enable the munging of symlinks via <code>--munge-links</code> (and make sure you use the right local or remote option). This will prevent rsync from doing potentially dangerous things if a symlink name overlaps with a file or directory. It does not, however, ensure that you get a full copy of all the files (since that may not be possible when the names overlap). A potentially better solution is to list all the source files and create a safe list of filenames that you pass to the <code>--files-from</code> option. Any files that conflict in name would need to be copied to different destination directories using more than one copy. </p>
<p> While a copy of a case-ignoring filesystem to a case-ignoring filesystem can work out fairly well, if no <code>--delete-during</code> or <code>--delete-before</code> option is active, rsync can potentially update an existing file on the receiveing side without noticing that the upper-/lower-case of the filename should be changed to match the sender. </p>
<h2>ADVANCED USAGE</h2>
<p> The syntax for requesting multiple files from a remote host is done by specifying additional remote-host args in the same style as the first, or with the hostname omitted. For instance, all these work: </p>
<dl>
<dd> <pre><code>rsync -aiv host:file1 :file2 host:file{3,4} /dest/
rsync -aiv host::modname/file{1,2} host::modname/extra /dest/
rsync -aiv host::modname/first ::extra-file{1,2} /dest/
</code></pre>
 </dd></dl>
<p> Note that a daemon connection only supports accessing one module per copy command, so if the start of a follow-up path doesn&#8217;t begin with the modname of the first path, it is assumed to be a path in the module (such as the extra-file1 &amp; extra-file2 that are grabbed above). </p>
<p> Really old versions of rsync (2.6.9 and before) only allowed specifying one remote-source arg, so some people have instead relied on the remote-shell performing space splitting to break up an arg into multiple paths. Such unintuitive behavior is no longer supported by default (though you can request it, as described below). </p>
<p> Starting in 3.2.4, filenames are passed to a remote shell in such a way as to preserve the characters you give it. Thus, if you ask for a file with spaces in the name, that&#8217;s what the remote rsync looks for: </p>
<dl>
<dd> <pre><code>rsync -aiv host:'a simple file.pdf' /dest/
</code></pre>
 </dd></dl>
<p> If you use scripts that have been written to manually apply extra quoting to the remote rsync args (or to require remote arg splitting), you can ask rsync to let your script handle the extra escaping. This is done by either adding the <code>--old-args</code> option to the rsync runs in the script (which requires a new rsync) or exporting RSYNC_OLD_ARGS=1 and RSYNC_PROTECT_ARGS=0 (which works with old or new rsync versions). </p>
<h2>CONNECTING TO AN RSYNC DAEMON</h2>
<p> It is also possible to use rsync without a remote shell as the transport. In this case you will directly connect to a remote rsync daemon, typically using TCP port 873. (This obviously requires the daemon to be running on the remote system, so refer to the STARTING AN RSYNC DAEMON TO ACCEPT CONNECTIONS section below for information on that.) </p>
<p> Using rsync in this way is the same as using it with a remote shell except that: </p>
<dl>
<dt>o</dt>
<dd> <p> Use either double-colon syntax or rsync:// URL syntax instead of the single-colon (remote shell) syntax. </p>
 </dd>
<dt>o</dt>
<dd> <p> The first element of the &quot;path&quot; is actually a module name. </p>
 </dd>
<dt>o</dt>
<dd> <p> Additional remote source args can use an abbreviated syntax that omits the hostname and/or the module name, as discussed in ADVANCED USAGE. </p>
 </dd>
<dt>o</dt>
<dd> <p> The remote daemon may print a &quot;message of the day&quot; when you connect. </p>
 </dd>
<dt>o</dt>
<dd> <p> If you specify only the host (with no module or path) then a list of accessible modules on the daemon is output. </p>
 </dd>
<dt>o</dt>
<dd> <p> If you specify a remote source path but no destination, a listing of the matching files on the remote daemon is output. </p>
 </dd>
<dt>o</dt>
<dd> <p> The <code>--rsh</code> (<code>-e</code>) option must be omitted to avoid changing the connection style from using a socket connection to USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION. </p>
 </dd></dl>
<p> An example that copies all the files in a remote module named &quot;src&quot;: </p>
<dl>
<dd> <pre><code>rsync -av host::src /dest
</code></pre>
 </dd></dl>
<p> Some modules on the remote daemon may require authentication. If so, you will receive a password prompt when you connect. You can avoid the password prompt by setting the environment variable <code>RSYNC_PASSWORD</code> to the password you want to use or using the <code>--password-file</code> option. This may be useful when scripting rsync. </p>
<p> WARNING: On some systems environment variables are visible to all users. On those systems using <code>--password-file</code> is recommended. </p>
<p> You may establish the connection via a web proxy by setting the environment variable <code>RSYNC_PROXY</code> to a hostname:port pair pointing to your web proxy. Note that your web proxy&#8217;s configuration must support proxy connections to port 873. </p>
<p> You may also establish a daemon connection using a program as a proxy by setting the environment variable <code>RSYNC_CONNECT_PROG</code> to the commands you wish to run in place of making a direct socket connection. The string may contain the escape &quot;%H&quot; to represent the hostname specified in the rsync command (so use &quot;%%&quot; if you need a single &quot;%&quot; in your string). For example: </p>
<dl>
<dd> <pre><code>export RSYNC_CONNECT_PROG='ssh proxyhost nc %H 873'
rsync -av targethost1::module/src/ /dest/
rsync -avrsync://targethost2/module/src/ /dest/
</code></pre>
 </dd></dl>
<p> The command specified above uses ssh to run nc (netcat) on a proxyhost, which forwards all data to port 873 (the rsync daemon) on the targethost (%H). </p>
<p> Note also that if the <code>RSYNC_SHELL</code> environment variable is set, that program will be used to run the <code>RSYNC_CONNECT_PROG</code> command instead of using the default shell of the <code>system()</code> call. </p>
<h2>USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION</h2>
<p> It is sometimes useful to use various features of an rsync daemon (such as named modules) without actually allowing any new socket connections into a system (other than what is already required to allow remote-shell access). Rsync supports connecting to a host using a remote shell and then spawning a single-use &quot;daemon&quot; server that expects to read its config file in the home dir of the remote user. This can be useful if you want to encrypt a daemon-style transfer&#8217;s data, but since the daemon is started up fresh by the remote user, you may not be able to use features such as chroot or change the uid used by the daemon. (For another way to encrypt a daemon transfer, consider using ssh to tunnel a local port to a remote machine and configure a normal rsync daemon on that remote host to only allow connections from &quot;localhost&quot;.) </p>
<p> From the user&#8217;s perspective, a daemon transfer via a remote-shell connection uses nearly the same command-line syntax as a normal rsync-daemon transfer, with the only exception being that you must explicitly set the remote shell program on the command-line with the <code>--rsh=COMMAND</code> option. (Setting the RSYNC_RSH in the environment will not turn on this functionality.) For example: </p>
<dl>
<dd> <pre><code>rsync -av --rsh=ssh host::module /dest
</code></pre>
 </dd></dl>
<p> If you need to specify a different remote-shell user, keep in mind that the user@ prefix in front of the host is specifying the rsync-user value (for a module that requires user-based authentication). This means that you must give the &#8216;-l user&#8217; option to ssh when specifying the remote-shell, as in this example that uses the short version of the <code>--rsh</code> option: </p>
<dl>
<dd> <pre><code>rsync -av -e &quot;ssh -l ssh-user&quot; rsync-user [at] host::module /dest
</code></pre>
 </dd></dl>
<p> The &quot;ssh-user&quot; will be used at the ssh level; the &quot;rsync-user&quot; will be used to log-in to the &quot;module&quot;. </p>
<p> In this setup, the daemon is started by the ssh command that is accessing the system (which can be forced via the <code>~/.ssh/authorized_keys</code> file, if desired). However, when accessing a daemon directly, it needs to be started beforehand. </p>
<h2>STARTING AN RSYNC DAEMON TO ACCEPT CONNECTIONS</h2>
<p> In order to connect to an rsync daemon, the remote system needs to have a daemon already running (or it needs to have configured something like inetd to spawn an rsync daemon for incoming connections on a particular port). For full information on how to start a daemon that will handling incoming socket connections, see the <code>rsyncd.conf</code>(5) manpage -- that is the config file for the daemon, and it contains the full details for how to run the daemon (including stand-alone and inetd configurations). </p>
<p> If you&#8217;re using one of the remote-shell transports for the transfer, there is no need to manually start an rsync daemon. </p>
<h2>EXAMPLES</h2>
<p> Here are some examples of how rsync can be used. </p>
<p> To backup a home directory, which consists of large MS Word files and mail folders, a per-user cron job can be used that runs this each day: </p>
<dl>
<dd> <pre><code>rsync -aiz . bkhost:backup/joe/
</code></pre>
 </dd></dl>
<p> To move some files from a remote host to the local host, you could run: </p>
<dl>
<dd> <pre><code>rsync -aiv --remove-source-files rhost:/tmp/{file1,file2}.c ~/src/
</code></pre>
 </dd></dl>
<h2>OPTION SUMMARY</h2>
<p> Here is a short summary of the options available in rsync. Each option also has its own detailed description later in this manpage. </p>
<pre><code>--verbose, -v increase verbosity
--info=FLAGS fine-grained informational verbosity
--debug=FLAGS fine-grained debug verbosity
--stderr=e|a|c change stderr output mode (default: errors)
--quiet, -q suppress non-error messages
--no-motd suppress daemon-mode MOTD
--checksum, -c skip based on checksum, not mod-time &amp; size
--archive, -a archive mode is -rlptgoD (no -A,-X,-U,-N,-H)
--no-OPTION turn off an implied OPTION (e.g. --no-D)
--recursive, -r recurse into directories
--relative, -R use relative path names
--no-implied-dirs don't send implied dirs with --relative
--backup, -b make backups (see --suffix &amp; --backup-dir)
--backup-dir=DIR make backups into hierarchy based in DIR
--suffix=SUFFIX backup suffix (default ~ w/o --backup-dir)
--update, -u skip files that are newer on the receiver
--inplace update destination files in-place
--append append data onto shorter files
--append-verify --append w/old data in file checksum
--dirs, -d transfer directories without recursing
--old-dirs, --old-d works like --dirs when talking to old rsync
--mkpath create destination's missing path components
--links, -l copy symlinks as symlinks
--copy-links, -L transform symlink into referent file/dir
--copy-unsafe-links only &quot;unsafe&quot; symlinks are transformed
--safe-links ignore symlinks that point outside the tree
--munge-links munge symlinks to make them safe &amp; unusable
--copy-dirlinks, -k transform symlink to dir into referent dir
--keep-dirlinks, -K treat symlinked dir on receiver as dir
--hard-links, -H preserve hard links
--perms, -p preserve permissions
--executability, -E preserve executability
--chmod=CHMOD affect file and/or directory permissions
--acls, -A preserve ACLs (implies --perms)
--xattrs, -X preserve extended attributes
--owner, -o preserve owner (super-user only)
--group, -g preserve group
--devices preserve device files (super-user only)
--copy-devices copy device contents as a regular file
--write-devices write to devices as files (implies --inplace)
--specials preserve special files
-D same as --devices --specials
--times, -t preserve modification times
--atimes, -U preserve access (use) times
--open-noatime avoid changing the atime on opened files
--crtimes, -N preserve create times (newness)
--omit-dir-times, -O omit directories from --times
--omit-link-times, -J omit symlinks from --times
--super receiver attempts super-user activities
--fake-super store/recover privileged attrs using xattrs
--sparse, -S turn sequences of nulls into sparse blocks
--preallocate allocate dest files before writing them
--dry-run, -n perform a trial run with no changes made
--whole-file, -W copy files whole (w/o delta-xfer algorithm)
--checksum-choice=STR choose the checksum algorithm (aka --cc)
--one-file-system, -x don't cross filesystem boundaries
--block-size=SIZE, -B force a fixed checksum block-size
--rsh=COMMAND, -e specify the remote shell to use
--rsync-path=PROGRAM specify the rsync to run on remote machine
--existing skip creating new files on receiver
--ignore-existing skip updating files that exist on receiver
--remove-source-files sender removes synchronized files (non-dir)
--del an alias for --delete-during
--delete delete extraneous files from dest dirs
--delete-before receiver deletes before xfer, not during
--delete-during receiver deletes during the transfer
--delete-delay find deletions during, delete after
--delete-after receiver deletes after transfer, not during
--delete-excluded also delete excluded files from dest dirs
--ignore-missing-args ignore missing source args without error
--delete-missing-args delete missing source args from destination
--ignore-errors delete even if there are I/O errors
--force force deletion of dirs even if not empty
--max-delete=NUM don't delete more than NUM files
--max-size=SIZE don't transfer any file larger than SIZE
--min-size=SIZE don't transfer any file smaller than SIZE
--max-alloc=SIZE change a limit relating to memory alloc
--partial keep partially transferred files
--partial-dir=DIR put a partially transferred file into DIR
--delay-updates put all updated files into place at end
--prune-empty-dirs, -m prune empty directory chains from file-list
--numeric-ids don't map uid/gid values by user/group name
--usermap=STRING custom username mapping
--groupmap=STRING custom groupname mapping
--chown=USER:GROUP simple username/groupname mapping
--timeout=SECONDS set I/O timeout in seconds
--contimeout=SECONDS set daemon connection timeout in seconds
--ignore-times, -I don't skip files that match size and time
--size-only skip files that match in size
--modify-window=NUM, -@ set the accuracy for mod-time comparisons
--temp-dir=DIR, -T create temporary files in directory DIR
--fuzzy, -y find similar file for basis if no dest file
--compare-dest=DIR also compare destination files relative to DIR
--copy-dest=DIR ... and include copies of unchanged files
--link-dest=DIR hardlink to files in DIR when unchanged
--compress, -z compress file data during the transfer
--compress-choice=STR choose the compression algorithm (aka --zc)
--compress-level=NUM explicitly set compression level (aka --zl)
--skip-compress=LIST skip compressing files with suffix in LIST
--cvs-exclude, -C auto-ignore files in the same way CVS does
--filter=RULE, -f add a file-filtering RULE
-F same as --filter='dir-merge /.rsync-filter'
                         repeated: --filter='- .rsync-filter'
--exclude=PATTERN exclude files matching PATTERN
--exclude-from=FILE read exclude patterns from FILE
--include=PATTERN don't exclude files matching PATTERN
--include-from=FILE read include patterns from FILE
--files-from=FILE read list of source-file names from FILE
--from0, -0 all *-from/filter files are delimited by 0s
--old-args disable the modern arg-protection idiom
--secluded-args, -s use the protocol to safely send the args
--trust-sender trust the remote sender's file list
--copy-as=USER[:GROUP] specify user &amp; optional group for the copy
--address=ADDRESS bind address for outgoing socket to daemon
--port=PORT specify double-colon alternate port number
--sockopts=OPTIONS specify custom TCP options
--blocking-io use blocking I/O for the remote shell
--outbuf=N|L|B set out buffering to None, Line, or Block
--stats give some file-transfer stats
--8-bit-output, -8 leave high-bit chars unescaped in output
--human-readable, -h output numbers in a human-readable format
--progress show progress during transfer
-P same as --partial --progress
--itemize-changes, -i output a change-summary for all updates
--remote-option=OPT, -M send OPTION to the remote side only
--out-format=FORMAT output updates using the specified FORMAT
--log-file=FILE log what we're doing to the specified FILE
--log-file-format=FMT log updates using the specified FMT
--password-file=FILE read daemon-access password from FILE
--early-input=FILE use FILE for daemon's early exec input
--list-only list the files instead of copying them
--bwlimit=RATE limit socket I/O bandwidth
--stop-after=MINS Stop rsync after MINS minutes have elapsed
--stop-at=y-m-dTh:m Stop rsync at the specified point in time
--fsync fsync every written file
--write-batch=FILE write a batched update to FILE
--only-write-batch=FILE like --write-batch but w/o updating dest
--read-batch=FILE read a batched update from FILE
--protocol=NUM force an older protocol version to be used
--iconv=CONVERT_SPEC request charset conversion of filenames
--checksum-seed=NUM set block/file checksum seed (advanced)
--ipv4, -4 prefer IPv4
--ipv6, -6 prefer IPv6
--version, -V print the version + other info and exit
--help, -h (*) show this help (* -h is help only on its own)
</code></pre>
<p> Rsync can also be run as a daemon, in which case the following options are accepted: </p>
<pre><code>--daemon run as an rsync daemon
--address=ADDRESS bind to the specified address
--bwlimit=RATE limit socket I/O bandwidth
--config=FILE specify alternate rsyncd.conf file
--dparam=OVERRIDE, -M override global daemon config parameter
--no-detach do not detach from the parent
--port=PORT listen on alternate port number
--log-file=FILE override the &quot;log file&quot; setting
--log-file-format=FMT override the &quot;log format&quot; setting
--sockopts=OPTIONS specify custom TCP options
--verbose, -v increase verbosity
--ipv4, -4 prefer IPv4
--ipv6, -6 prefer IPv6
--help, -h show this help (when used with --daemon)
</code></pre>
<h2>OPTIONS</h2>
<p> Rsync accepts both long (double-dash + word) and short (single-dash + letter) options. The full list of the available options are described below. If an option can be specified in more than one way, the choices are comma-separated. Some options only have a long variant, not a short. </p>
<p> If the option takes a parameter, the parameter is only listed after the long variant, even though it must also be specified for the short. When specifying a parameter, you can either use the form <code>--option=param</code>, <code>--option param</code>, <code>-o=param</code>, <code>-o param</code>, or <code>-oparam</code> (the latter choices assume that your option has a short variant). </p>
<p> The parameter may need to be quoted in some manner for it to survive the shell&#8217;s command-line parsing. Also keep in mind that a leading tilde (<code>~</code>) in a pathname is substituted by your shell, so make sure that you separate the option name from the pathname using a space if you want the local shell to expand it. </p>
<dl>
<dt><code>--help</code></dt>
<dd> <p> Print a short help page describing the options available in rsync and exit. You can also use <code>-h</code> for <code>--help</code> when it is used without any other options (since it normally means <code>--human-readable</code>). </p>
 </dd>
<dt><code>--version</code>, <code>-V</code></dt>
<dd> <p> Print the rsync version plus other info and exit. When repeated, the information is output is a JSON format that is still fairly readable (client side only). </p>
 </dd>
<dd> <p> The output includes a list of compiled-in capabilities, a list of optimizations, the default list of checksum algorithms, the default list of compression algorithms, the default list of daemon auth digests, a link to the rsync web site, and a few other items. </p>
 </dd>
<dt><code>--verbose</code>, <code>-v</code></dt>
<dd> <p> This option increases the amount of information you are given during the transfer. By default, rsync works silently. A single <code>-v</code> will give you information about what files are being transferred and a brief summary at the end. Two <code>-v</code> options will give you information on what files are being skipped and slightly more information at the end. More than two <code>-v</code> options should only be used if you are debugging rsync. </p>
 </dd>
<dd> <p> The end-of-run summary tells you the number of bytes sent to the remote rsync (which is the receiving side on a local copy), the number of bytes received from the remote host, and the average bytes per second of the transferred data computed over the entire length of the rsync run. The second line shows the total size (in bytes), which is the sum of all the file sizes that rsync considered transferring. It also shows a &quot;speedup&quot; value, which is a ratio of the total file size divided by the sum of the sent and received bytes (which is really just a feel-good bigger-is-better number). Note that these byte values can be made more (or less) human-readable by using the <code>--human-readable</code> (or <code>--no-human-readable</code>) options. </p>
 </dd>
<dd> <p> In a modern rsync, the <code>-v</code> option is equivalent to the setting of groups of <code>--info</code> and <code>--debug</code> options. You can choose to use these newer options in addition to, or in place of using <code>--verbose</code>, as any fine-grained settings override the implied settings of <code>-v</code>. Both <code>--info</code> and <code>--debug</code> have a way to ask for help that tells you exactly what flags are set for each increase in verbosity. </p>
 </dd>
<dd> <p> However, do keep in mind that a daemon&#8217;s &quot;<code>max verbosity</code>&quot; setting will limit how high of a level the various individual flags can be set on the daemon side. For instance, if the max is 2, then any info and/or debug flag that is set to a higher value than what would be set by <code>-vv</code> will be downgraded to the <code>-vv</code> level in the daemon&#8217;s logging. </p>
 </dd>
<dt><code>--info=FLAGS</code></dt>
<dd> <p> This option lets you have fine-grained control over the information output you want to see. An individual flag name may be followed by a level number, with 0 meaning to silence that output, 1 being the default output level, and higher numbers increasing the output of that flag (for those that support higher levels). Use <code>--info=help</code> to see all the available flag names, what they output, and what flag names are added for each increase in the verbose level. Some examples: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -a --info=progress2 src/ dest/
rsync -avv --info=stats2,misc1,flist0 src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Note that <code>--info=name</code>&#8216;s output is affected by the <code>--out-format</code> and <code>--itemize-changes</code> (<code>-i</code>) options. See those options for more information on what is output and when. </p>
 </dd>
<dd> <p> This option was added to 3.1.0, so an older rsync on the server side might reject your attempts at fine-grained control (if one or more flags needed to be send to the server and the server was too old to understand them). See also the &quot;<code>max verbosity</code>&quot; caveat above when dealing with a daemon. </p>
 </dd>
<dt><code>--debug=FLAGS</code></dt>
<dd> <p> This option lets you have fine-grained control over the debug output you want to see. An individual flag name may be followed by a level number, with 0 meaning to silence that output, 1 being the default output level, and higher numbers increasing the output of that flag (for those that support higher levels). Use <code>--debug=help</code> to see all the available flag names, what they output, and what flag names are added for each increase in the verbose level. Some examples: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avvv --debug=none src/ dest/
rsync -avA --del --debug=del2,acl src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Note that some debug messages will only be output when the <code>--stderr=all</code> option is specified, especially those pertaining to I/O and buffer debugging. </p>
 </dd>
<dd> <p> Beginning in 3.2.0, this option is no longer auto-forwarded to the server side in order to allow you to specify different debug values for each side of the transfer, as well as to specify a new debug option that is only present in one of the rsync versions. If you want to duplicate the same option on both sides, using brace expansion is an easy way to save you some typing. This works in zsh and bash: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -aiv {-M,}--debug=del2 src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dt><code>--stderr=errors|all|client</code></dt>
<dd> <p> This option controls which processes output to stderr and if info messages are also changed to stderr. The mode strings can be abbreviated, so feel free to use a single letter value. The 3 possible choices are: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <code>errors</code> - (the default) causes all the rsync processes to send an error directly to stderr, even if the process is on the remote side of the transfer. Info messages are sent to the client side via the protocol stream. If stderr is not available (i.e. when directly connecting with a daemon via a socket) errors fall back to being sent via the protocol stream. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>all</code> - causes all rsync messages (info and error) to get written directly to stderr from all (possible) processes. This causes stderr to become line-buffered (instead of raw) and eliminates the ability to divide up the info and error messages by file handle. For those doing debugging or using several levels of verbosity, this option can help to avoid clogging up the transfer stream (which should prevent any chance of a deadlock bug hanging things up). It also allows <code>--debug</code> to enable some extra I/O related messages. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>client</code> - causes all rsync messages to be sent to the client side via the protocol stream. One client process outputs all messages, with errors on stderr and info messages on stdout. This <code>was</code> the default in older rsync versions, but can cause error delays when a lot of transfer data is ahead of the messages. If you&#8217;re pushing files to an older rsync, you may want to use <code>--stderr=all</code> since that idiom has been around for several releases. </p>
 </dd></dl>
</dl>
<dd> <p> This option was added in rsync 3.2.3. This version also began the forwarding of a non-default setting to the remote side, though rsync uses the backward-compatible options <code>--msgs2stderr</code> and <code>--no-msgs2stderr</code> to represent the <code>all</code> and <code>client</code> settings, respectively. A newer rsync will continue to accept these older option names to maintain compatibility. </p>
 </dd>
<dt><code>--quiet</code>, <code>-q</code></dt>
<dd> <p> This option decreases the amount of information you are given during the transfer, notably suppressing information messages from the remote server. This option is useful when invoking rsync from cron. </p>
 </dd>
<dt><code>--no-motd</code></dt>
<dd> <p> This option affects the information that is output by the client at the start of a daemon transfer. This suppresses the message-of-the-day (MOTD) text, but it also affects the list of modules that the daemon sends in response to the &quot;rsync host::&quot; request (due to a limitation in the rsync protocol), so omit this option if you want to request the list of modules from the daemon. </p>
 </dd>
<dt><code>--ignore-times</code>, <code>-I</code></dt>
<dd> <p> Normally rsync will skip any files that are already the same size and have the same modification timestamp. This option turns off this &quot;quick check&quot; behavior, causing all files to be updated. </p>
 </dd>
<dd> <p> This option can be confusing compared to <code>--ignore-existing</code> and <code>--ignore-non-existing</code> in that that they cause rsync to transfer fewer files, while this option causes rsync to transfer more files. </p>
 </dd>
<dt><code>--size-only</code></dt>
<dd> <p> This modifies rsync&#8217;s &quot;quick check&quot; algorithm for finding files that need to be transferred, changing it from the default of transferring files with either a changed size or a changed last-modified time to just looking for files that have changed in size. This is useful when starting to use rsync after using another mirroring system which may not preserve timestamps exactly. </p>
 </dd>
<dt><code>--modify-window=NUM</code>, <code>-@</code></dt>
<dd> <p> When comparing two timestamps, rsync treats the timestamps as being equal if they differ by no more than the modify-window value. The default is 0, which matches just integer seconds. If you specify a negative value (and the receiver is at least version 3.1.3) then nanoseconds will also be taken into account. Specifying 1 is useful for copies to/from MS Windows FAT filesystems, because FAT represents times with a 2-second resolution (allowing times to differ from the original by up to 1 second). </p>
 </dd>
<dd> <p> If you want all your transfers to default to comparing nanoseconds, you can create a <code>~/.popt</code> file and put these lines in it: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync alias -a -a@-1
rsync alias -t -t@-1
</code></pre>
 </dd></dl>
</dl>
<dd> <p> With that as the default, you&#8217;d need to specify <code>--modify-window=0</code> (aka <code>-@0</code>) to override it and ignore nanoseconds, e.g. if you&#8217;re copying between ext3 and ext4, or if the receiving rsync is older than 3.1.3. </p>
 </dd>
<dt><code>--checksum</code>, <code>-c</code></dt>
<dd> <p> This changes the way rsync checks if the files have been changed and are in need of a transfer. Without this option, rsync uses a &quot;quick check&quot; that (by default) checks if each file&#8217;s size and time of last modification match between the sender and receiver. This option changes this to compare a 128-bit checksum for each file that has a matching size. Generating the checksums means that both sides will expend a lot of disk I/O reading all the data in the files in the transfer, so this can slow things down significantly (and this is prior to any reading that will be done to transfer changed files) </p>
 </dd>
<dd> <p> The sending side generates its checksums while it is doing the file-system scan that builds the list of the available files. The receiver generates its checksums when it is scanning for changed files, and will checksum any file that has the same size as the corresponding sender&#8217;s file: files with either a changed size or a changed checksum are selected for transfer. </p>
 </dd>
<dd> <p> Note that rsync always verifies that each <i>transferred</i> file was correctly reconstructed on the receiving side by checking a whole-file checksum that is generated as the file is transferred, but that automatic after-the-transfer verification has nothing to do with this option&#8217;s before-the-transfer &quot;Does this file need to be updated?&quot; check. </p>
 </dd>
<dd> <p> The checksum used is auto-negotiated between the client and the server, but can be overridden using either the <code>--checksum-choice</code> (<code>--cc</code>) option or an environment variable that is discussed in that option&#8217;s section. </p>
 </dd>
<dt><code>--archive</code>, <code>-a</code></dt>
<dd> <p> This is equivalent to <code>-rlptgoD</code>. It is a quick way of saying you want recursion and want to preserve almost everything. Be aware that it does <code>not</code> include preserving ACLs (<code>-A</code>), xattrs (<code>-X</code>), atimes (<code>-U</code>), crtimes (<code>-N</code>), nor the finding and preserving of hardlinks (<code>-H</code>). </p>
 </dd>
<dd> <p> The only exception to the above equivalence is when <code>--files-from</code> is specified, in which case <code>-r</code> is not implied. </p>
 </dd>
<dt><code>--no-OPTION</code></dt>
<dd> <p> You may turn off one or more implied options by prefixing the option name with &quot;no-&quot;. Not all positive options have a negated opposite, but a lot do, including those that can be used to disable an implied option (e.g. <code>--no-D</code>, <code>--no-perms</code>) or have different defaults in various circumstances (e.g. <code>--no-whole-file</code>, <code>--no-blocking-io</code>, <code>--no-dirs</code>). Every valid negated option accepts both the short and the long option name after the &quot;no-&quot; prefix (e.g. <code>--no-R</code> is the same as <code>--no-relative</code>). </p>
 </dd>
<dd> <p> As an example, if you want to use <code>--archive</code> (<code>-a</code>) but don&#8217;t want <code>--owner</code> (<code>-o</code>), instead of converting <code>-a</code> into <code>-rlptgD</code>, you can specify <code>-a --no-o</code> (aka <code>--archive --no-owner</code>). </p>
 </dd>
<dd> <p> The order of the options is important: if you specify <code>--no-r -a</code>, the <code>-r</code> option would end up being turned on, the opposite of <code>-a --no-r</code>. Note also that the side-effects of the <code>--files-from</code> option are NOT positional, as it affects the default state of several options and slightly changes the meaning of <code>-a</code> (see the <code>--files-from</code> option for more details). </p>
 </dd>
<dt><code>--recursive</code>, <code>-r</code></dt>
<dd> <p> This tells rsync to copy directories recursively. See also <code>--dirs</code> (<code>-d</code>) for an option that allows the scanning of a single directory. </p>
 </dd>
<dd> <p> See the <code>--inc-recursive</code> option for a discussion of the incremental recursion for creating the list of files to transfer. </p>
 </dd>
<dt><code>--inc-recursive</code>, <code>--i-r</code></dt>
<dd> <p> This option explicitly enables on incremental recursion when scanning for files, which is enabled by default when using the <code>--recursive</code> option and both sides of the transfer are running rsync 3.0.0 or newer. </p>
 </dd>
<dd> <p> Incremental recursion uses much less memory than non-incremental, while also beginning the transfer more quickly (since it doesn&#8217;t need to scan the entire transfer hierarchy before it starts transferring files). If no recursion is enabled in the source files, this option has no effect. </p>
 </dd>
<dd> <p> Some options require rsync to know the full file list, so these options disable the incremental recursion mode. These include: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <code>--delete-before</code> (the old default of <code>--delete</code>) </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>--delete-after</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>--prune-empty-dirs</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>--delay-updates</code> </p>
 </dd></dl>
</dl>
<dd> <p> In order to make <code>--delete</code> compatible with incremental recursion, rsync 3.0.0 made <code>--delete-during</code> the default delete mode (which was first added in 2.6.4). </p>
 </dd>
<dd> <p> One side-effect of incremental recursion is that any missing sub-directories inside a recursively-scanned directory are (by default) created prior to recursing into the sub-dirs. This earlier creation point (compared to a non-incremental recursion) allows rsync to then set the modify time of the finished directory right away (without having to delay that until a bunch of recursive copying has finished). However, these early directories don&#8217;t yet have their completed mode, mtime, or ownership set -- they have more restrictive rights until the subdirectory&#8217;s copying actually begins. This early-creation idiom can be avoided by using the <code>--omit-dir-times</code> option. </p>
 </dd>
<dd> <p> Incremental recursion can be disabled using the <code>--no-inc-recursive</code> (<code>--no-i-r</code>) option. </p>
 </dd>
<dt><code>--no-inc-recursive</code>, <code>--no-i-r</code></dt>
<dd> <p> Disables the new incremental recursion algorithm of the <code>--recursive</code> option. This makes rsync scan the full file list before it begins to transfer files. See <code>--inc-recursive</code> for more info. </p>
 </dd>
<dt><code>--relative</code>, <code>-R</code></dt>
<dd> <p> Use relative paths. This means that the full path names specified on the command line are sent to the server rather than just the last parts of the filenames. This is particularly useful when you want to send several different directories at the same time. For example, if you used this command: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av /foo/bar/baz.c remote:/tmp/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> would create a file named baz.c in /tmp/ on the remote machine. If instead you used </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avR /foo/bar/baz.c remote:/tmp/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> then a file named /tmp/foo/bar/baz.c would be created on the remote machine, preserving its full path. These extra path elements are called &quot;implied directories&quot; (i.e. the &quot;foo&quot; and the &quot;foo/bar&quot; directories in the above example). </p>
 </dd>
<dd> <p> Beginning with rsync 3.0.0, rsync always sends these implied directories as real directories in the file list, even if a path element is really a symlink on the sending side. This prevents some really unexpected behaviors when copying the full path of a file that you didn&#8217;t realize had a symlink in its path. If you want to duplicate a server-side symlink, include both the symlink via its path, and referent directory via its real path. If you&#8217;re dealing with an older rsync on the sending side, you may need to use the <code>--no-implied-dirs</code> option. </p>
 </dd>
<dd> <p> It is also possible to limit the amount of path information that is sent as implied directories for each path you specify. With a modern rsync on the sending side (beginning with 2.6.7), you can insert a dot and a slash into the source path, like this: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avR /foo/./bar/baz.c remote:/tmp/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> That would create /tmp/bar/baz.c on the remote machine. (Note that the dot must be followed by a slash, so &quot;/foo/.&quot; would not be abbreviated.) For older rsync versions, you would need to use a chdir to limit the source path. For example, when pushing files: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>(cd /foo; rsync -avR bar/baz.c remote:/tmp/)
</code></pre>
 </dd></dl>
</dl>
<dd> <p> (Note that the parens put the two commands into a sub-shell, so that the &quot;cd&quot; command doesn&#8217;t remain in effect for future commands.) If you&#8217;re pulling files from an older rsync, use this idiom (but only for a non-daemon transfer): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avR --rsync-path=&quot;cd /foo; rsync&quot; \
     remote:bar/baz.c /tmp/
</code></pre>
 </dd></dl>
</dl>
<dt><code>--no-implied-dirs</code></dt>
<dd> <p> This option affects the default behavior of the <code>--relative</code> option. When it is specified, the attributes of the implied directories from the source names are not included in the transfer. This means that the corresponding path elements on the destination system are left unchanged if they exist, and any missing implied directories are created with default attributes. This even allows these implied path elements to have big differences, such as being a symlink to a directory on the receiving side. </p>
 </dd>
<dd> <p> For instance, if a command-line arg or a files-from entry told rsync to transfer the file &quot;path/foo/file&quot;, the directories &quot;path&quot; and &quot;path/foo&quot; are implied when <code>--relative</code> is used. If &quot;path/foo&quot; is a symlink to &quot;bar&quot; on the destination system, the receiving rsync would ordinarily delete &quot;path/foo&quot;, recreate it as a directory, and receive the file into the new directory. With <code>--no-implied-dirs</code>, the receiving rsync updates &quot;path/foo/file&quot; using the existing path elements, which means that the file ends up being created in &quot;path/bar&quot;. Another way to accomplish this link preservation is to use the <code>--keep-dirlinks</code> option (which will also affect symlinks to directories in the rest of the transfer). </p>
 </dd>
<dd> <p> When pulling files from an rsync older than 3.0.0, you may need to use this option if the sending side has a symlink in the path you request and you wish the implied directories to be transferred as normal directories. </p>
 </dd>
<dt><code>--backup</code>, <code>-b</code></dt>
<dd> <p> With this option, preexisting destination files are renamed as each file is transferred or deleted. You can control where the backup file goes and what (if any) suffix gets appended using the <code>--backup-dir</code> and <code>--suffix</code> options. </p>
 </dd>
<dd> <p> If you don&#8217;t specify <code>--backup-dir</code>: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd>
<dt>1.</dt>
<dd> <p> the <code>--omit-dir-times</code> option will be forced on </p>
 </dd>
<dt>2.</dt>
<dd> <p> the use of <code>--delete</code> (without <code>--delete-excluded</code>), causes rsync to add a &quot;protect&quot; filter-rule for the backup suffix to the end of all your existing filters that looks like this: <code>-f&nbsp;&quot;P&nbsp;*~&quot;</code>. This rule prevents previously backed-up files from being deleted. </p>
 </dd></dl>
</dl>
<dd> <p> Note that if you are supplying your own filter rules, you may need to manually insert your own exclude/protect rule somewhere higher up in the list so that it has a high enough priority to be effective (e.g. if your rules specify a trailing inclusion/exclusion of <code>*</code>, the auto-added rule would never be reached). </p>
 </dd>
<dt><code>--backup-dir=DIR</code></dt>
<dd> <p> This implies the <code>--backup</code> option, and tells rsync to store all backups in the specified directory on the receiving side. This can be used for incremental backups. You can additionally specify a backup suffix using the <code>--suffix</code> option (otherwise the files backed up in the specified directory will keep their original filenames). </p>
 </dd>
<dd> <p> Note that if you specify a relative path, the backup directory will be relative to the destination directory, so you probably want to specify either an absolute path or a path that starts with &quot;../&quot;. If an rsync daemon is the receiver, the backup dir cannot go outside the module&#8217;s path hierarchy, so take extra care not to delete it or copy into it. </p>
 </dd>
<dt><code>--suffix=SUFFIX</code></dt>
<dd> <p> This option allows you to override the default backup suffix used with the <code>--backup</code> (<code>-b</code>) option. The default suffix is a <code>~</code> if no <code>--backup-dir</code> was specified, otherwise it is an empty string. </p>
 </dd>
<dt><code>--update</code>, <code>-u</code></dt>
<dd> <p> This forces rsync to skip any files which exist on the destination and have a modified time that is newer than the source file. (If an existing destination file has a modification time equal to the source file&#8217;s, it will be updated if the sizes are different.) </p>
 </dd>
<dd> <p> Note that this does not affect the copying of dirs, symlinks, or other special files. Also, a difference of file format between the sender and receiver is always considered to be important enough for an update, no matter what date is on the objects. In other words, if the source has a directory where the destination has a file, the transfer would occur regardless of the timestamps. </p>
 </dd>
<dd> <p> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects. </p>
 </dd>
<dd> <p> A caution for those that choose to combine <code>--inplace</code> with <code>--update</code>: an interrupted transfer will leave behind a partial file on the receiving side that has a very recent modified time, so re-running the transfer will probably <code>not</code> continue the interrupted file. As such, it is usually best to avoid combining this with <code>--inplace</code> unless you have implemented manual steps to handle any interrupted in-progress files. </p>
 </dd>
<dt><code>--inplace</code></dt>
<dd> <p> This option changes how rsync transfers a file when its data needs to be updated: instead of the default method of creating a new copy of the file and moving it into place when it is complete, rsync instead writes the updated data directly to the destination file. </p>
 </dd>
<dd> <p> This has several effects: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> Hard links are not broken. This means the new data will be visible through other hard links to the destination file. Moreover, attempts to copy differing source files onto a multiply-linked destination file will result in a &quot;tug of war&quot; with the destination data changing back and forth. </p>
 </dd>
<dt>o</dt>
<dd> <p> In-use binaries cannot be updated (either the OS will prevent this from happening, or binaries that attempt to swap-in their data will misbehave or crash). </p>
 </dd>
<dt>o</dt>
<dd> <p> The file&#8217;s data will be in an inconsistent state during the transfer and will be left that way if the transfer is interrupted or if an update fails. </p>
 </dd>
<dt>o</dt>
<dd> <p> A file that rsync cannot write to cannot be updated. While a super user can update any file, a normal user needs to be granted write permission for the open of the file for writing to be successful. </p>
 </dd>
<dt>o</dt>
<dd> <p> The efficiency of rsync&#8217;s delta-transfer algorithm may be reduced if some data in the destination file is overwritten before it can be copied to a position later in the file. This does not apply if you use <code>--backup</code>, since rsync is smart enough to use the backup file as the basis file for the transfer. </p>
 </dd></dl>
</dl>
<dd> <p> WARNING: you should not use this option to update files that are being accessed by others, so be careful when choosing to use this for a copy. </p>
 </dd>
<dd> <p> This option is useful for transferring large files with block-based changes or appended data, and also on systems that are disk bound, not network bound. It can also help keep a copy-on-write filesystem snapshot from diverging the entire contents of a file that only has minor changes. </p>
 </dd>
<dd> <p> The option implies <code>--partial</code> (since an interrupted transfer does not delete the file), but conflicts with <code>--partial-dir</code> and <code>--delay-updates</code>. Prior to rsync 2.6.4 <code>--inplace</code> was also incompatible with <code>--compare-dest</code> and <code>--link-dest</code>. </p>
 </dd>
<dt><code>--append</code></dt>
<dd> <p> This special copy mode only works to efficiently update files that are known to be growing larger where any existing content on the receiving side is also known to be the same as the content on the sender. The use of <code>--append</code> <code>can be dangerous</code> if you aren&#8217;t 100% sure that all the files in the transfer are shared, growing files. You should thus use filter rules to ensure that you weed out any files that do not fit this criteria. </p>
 </dd>
<dd> <p> Rsync updates these growing file in-place without verifying any of the existing content in the file (it only verifies the content that it is appending). Rsync skips any files that exist on the receiving side that are not shorter than the associated file on the sending side (which means that new files are transferred). It also skips any files whose size on the sending side gets shorter during the send negotiations (rsync warns about a &quot;diminished&quot; file when this happens). </p>
 </dd>
<dd> <p> This does not interfere with the updating of a file&#8217;s non-content attributes (e.g. permissions, ownership, etc.) when the file does not need to be transferred, nor does it affect the updating of any directories or non-regular files. </p>
 </dd>
<dt><code>--append-verify</code></dt>
<dd> <p> This special copy mode works like <code>--append</code> except that all the data in the file is included in the checksum verification (making it less efficient but also potentially safer). This option <code>can be dangerous</code> if you aren&#8217;t 100% sure that all the files in the transfer are shared, growing files. See the <code>--append</code> option for more details. </p>
 </dd>
<dd> <p> Note: prior to rsync 3.0.0, the <code>--append</code> option worked like <code>--append-verify</code>, so if you are interacting with an older rsync (or the transfer is using a protocol prior to 30), specifying either append option will initiate an <code>--append-verify</code> transfer. </p>
 </dd>
<dt><code>--dirs</code>, <code>-d</code></dt>
<dd> <p> Tell the sending side to include any directories that are encountered. Unlike <code>--recursive</code>, a directory&#8217;s contents are not copied unless the directory name specified is &quot;.&quot; or ends with a trailing slash (e.g. &quot;.&quot;, &quot;dir/.&quot;, &quot;dir/&quot;, etc.). Without this option or the <code>--recursive</code> option, rsync will skip all directories it encounters (and output a message to that effect for each one). If you specify both <code>--dirs</code> and <code>--recursive</code>, <code>--recursive</code> takes precedence. </p>
 </dd>
<dd> <p> The <code>--dirs</code> option is implied by the <code>--files-from</code> option or the <code>--list-only</code> option (including an implied <code>--list-only</code> usage) if <code>--recursive</code> wasn&#8217;t specified (so that directories are seen in the listing). Specify <code>--no-dirs</code> (or <code>--no-d</code>) if you want to turn this off. </p>
 </dd>
<dd> <p> There is also a backward-compatibility helper option, <code>--old-dirs</code> (<code>--old-d</code>) that tells rsync to use a hack of <code>-r --exclude=&#8216;/*/*&#8216;</code> to get an older rsync to list a single directory without recursing. </p>
 </dd>
<dt><code>--mkpath</code></dt>
<dd> <p> Create all missing path components of the destination path. </p>
 </dd>
<dd> <p> By default, rsync allows only the final component of the destination path to not exist, which is an attempt to help you to validate your destination path. With this option, rsync creates all the missing destination-path components, just as if <code>mkdir -p&nbsp;$DEST_PATH</code> had been run on the receiving side. </p>
 </dd>
<dd> <p> When specifying a destination path, including a trailing slash ensures that the whole path is treated as directory names to be created, even when the file list has a single item. See the COPYING TO A DIFFERENT NAME section for full details on how rsync decides if a final destination-path component should be created as a directory or not. </p>
 </dd>
<dd> <p> If you would like the newly-created destination dirs to match the dirs on the sending side, you should be using <code>--relative</code> (<code>-R</code>) instead of <code>--mkpath</code>. For instance, the following two commands result in the same destination tree, but only the second command ensures that the &quot;some/extra/path&quot; components match the dirs on the sending side: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -ai --mkpath host:some/extra/path/*.c some/extra/path/
rsync -aiR host:some/extra/path/*.c ./
</code></pre>
 </dd></dl>
</dl>
<dt><code>--links</code>, <code>-l</code></dt>
<dd> <p> Add symlinks to the transferred files instead of noisily ignoring them with a &quot;non-regular file&quot; warning for each symlink encountered. You can alternately silence the warning by specifying <code>--info=nonreg0</code>. </p>
 </dd>
<dd> <p> The default handling of symlinks is to recreate each symlink&#8217;s unchanged value on the receiving side. </p>
 </dd>
<dd> <p> See the SYMBOLIC LINKS section for multi-option info. </p>
 </dd>
<dt><code>--copy-links</code>, <code>-L</code></dt>
<dd> <p> The sender transforms each symlink encountered in the transfer into the referent item, following the symlink chain to the file or directory that it references. If a symlink chain is broken, an error is output and the file is dropped from the transfer. </p>
 </dd>
<dd> <p> This option supersedes any other options that affect symlinks in the transfer, since there are no symlinks left in the transfer. </p>
 </dd>
<dd> <p> This option does not change the handling of existing symlinks on the receiving side, unlike versions of rsync prior to 2.6.3 which had the side-effect of telling the receiving side to also follow symlinks. A modern rsync won&#8217;t forward this option to a remote receiver (since only the sender needs to know about it), so this caveat should only affect someone using an rsync client older than 2.6.7 (which is when <code>-L</code> stopped being forwarded to the receiver). </p>
 </dd>
<dd> <p> See the <code>--keep-dirlinks</code> (<code>-K</code>) if you need a symlink to a directory to be treated as a real directory on the receiving side. </p>
 </dd>
<dd> <p> See the SYMBOLIC LINKS section for multi-option info. </p>
 </dd>
<dt><code>--copy-unsafe-links</code></dt>
<dd> <p> This tells rsync to copy the referent of symbolic links that point outside the copied tree. Absolute symlinks are also treated like ordinary files, and so are any symlinks in the source path itself when <code>--relative</code> is used. </p>
 </dd>
<dd> <p> Note that the cut-off point is the top of the transfer, which is the part of the path that rsync isn&#8217;t mentioning in the verbose output. If you copy &quot;/src/subdir&quot; to &quot;/dest/&quot; then the &quot;subdir&quot; directory is a name inside the transfer tree, not the top of the transfer (which is /src) so it is legal for created relative symlinks to refer to other names inside the /src and /dest directories. If you instead copy &quot;/src/subdir/&quot; (with a trailing slash) to &quot;/dest/subdir&quot; that would not allow symlinks to any files outside of &quot;subdir&quot;. </p>
 </dd>
<dd> <p> Note that safe symlinks are only copied if <code>--links</code> was also specified or implied. The <code>--copy-unsafe-links</code> option has no extra effect when combined with <code>--copy-links</code>. </p>
 </dd>
<dd> <p> See the SYMBOLIC LINKS section for multi-option info. </p>
 </dd>
<dt><code>--safe-links</code></dt>
<dd> <p> This tells the receiving rsync to ignore any symbolic links in the transfer which point outside the copied tree. All absolute symlinks are also ignored. </p>
 </dd>
<dd> <p> Since this ignoring is happening on the receiving side, it will still be effective even when the sending side has munged symlinks (when it is using <code>--munge-links</code>). It also affects deletions, since the file being present in the transfer prevents any matching file on the receiver from being deleted when the symlink is deemed to be unsafe and is skipped. </p>
 </dd>
<dd> <p> This option must be combined with <code>--links</code> (or <code>--archive</code>) to have any symlinks in the transfer to conditionally ignore. Its effect is superseded by <code>--copy-unsafe-links</code>. </p>
 </dd>
<dd> <p> Using this option in conjunction with <code>--relative</code> may give unexpected results. </p>
 </dd>
<dd> <p> See the SYMBOLIC LINKS section for multi-option info. </p>
 </dd>
<dt><code>--munge-links</code></dt>
<dd> <p> This option affects just one side of the transfer and tells rsync to munge symlink values when it is receiving files or unmunge symlink values when it is sending files. The munged values make the symlinks unusable on disk but allows the original contents of the symlinks to be recovered. </p>
 </dd>
<dd> <p> The server-side rsync often enables this option without the client&#8217;s knowledge, such as in an rsync daemon&#8217;s configuration file or by an option given to the rrsync (restricted rsync) script. When specified on the client side, specify the option normally if it is the client side that has/needs the munged symlinks, or use <code>-M--munge-links</code> to give the option to the server when it has/needs the munged symlinks. Note that on a local transfer, the client is the sender, so specifying the option directly unmunges symlinks while specifying it as a remote option munges symlinks. </p>
 </dd>
<dd> <p> This option has no effect when sent to a daemon via <code>--remote-option</code> because the daemon configures whether it wants munged symlinks via its &quot;<code>munge symlinks</code>&quot; parameter. </p>
 </dd>
<dd> <p> The symlink value is munged/unmunged once it is in the transfer, so any option that transforms symlinks into non-symlinks occurs prior to the munging/unmunging <code>except</code> for <code>--safe-links</code>, which is a choice that the receiver makes, so it bases its decision on the munged/unmunged value. This does mean that if a receiver has munging enabled, that using <code>--safe-links</code> will cause all symlinks to be ignored (since they are all absolute). </p>
 </dd>
<dd> <p> The method that rsync uses to munge the symlinks is to prefix each one&#8217;s value with the string &quot;/rsyncd-munged/&quot;. This prevents the links from being used as long as the directory does not exist. When this option is enabled, rsync will refuse to run if that path is a directory or a symlink to a directory (though it only checks at startup). See also the &quot;munge-symlinks&quot; python script in the support directory of the source code for a way to munge/unmunge one or more symlinks in-place. </p>
 </dd>
<dt><code>--copy-dirlinks</code>, <code>-k</code></dt>
<dd> <p> This option causes the sending side to treat a symlink to a directory as though it were a real directory. This is useful if you don&#8217;t want symlinks to non-directories to be affected, as they would be using <code>--copy-links</code>. </p>
 </dd>
<dd> <p> Without this option, if the sending side has replaced a directory with a symlink to a directory, the receiving side will delete anything that is in the way of the new symlink, including a directory hierarchy (as long as <code>--force</code> or <code>--delete</code> is in effect). </p>
 </dd>
<dd> <p> See also <code>--keep-dirlinks</code> for an analogous option for the receiving side. </p>
 </dd>
<dd> <p> <code>--copy-dirlinks</code> applies to all symlinks to directories in the source. If you want to follow only a few specified symlinks, a trick you can use is to pass them as additional source args with a trailing slash, using <code>--relative</code> to make the paths match up right. For example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -r --relative src/./ src/./follow-me/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This works because rsync calls <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) on the source arg as given, and the trailing slash makes <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) follow the symlink, giving rise to a directory in the file-list which overrides the symlink found during the scan of &quot;src/./&quot;. </p>
 </dd>
<dd> <p> See the SYMBOLIC LINKS section for multi-option info. </p>
 </dd>
<dt><code>--keep-dirlinks</code>, <code>-K</code></dt>
<dd> <p> This option causes the receiving side to treat a symlink to a directory as though it were a real directory, but only if it matches a real directory from the sender. Without this option, the receiver&#8217;s symlink would be deleted and replaced with a real directory. </p>
 </dd>
<dd> <p> For example, suppose you transfer a directory &quot;foo&quot; that contains a file &quot;file&quot;, but &quot;foo&quot; is a symlink to directory &quot;bar&quot; on the receiver. Without <code>--keep-dirlinks</code>, the receiver deletes symlink &quot;foo&quot;, recreates it as a directory, and receives the file into the new directory. With <code>--keep-dirlinks</code>, the receiver keeps the symlink and &quot;file&quot; ends up in &quot;bar&quot;. </p>
 </dd>
<dd> <p> One note of caution: if you use <code>--keep-dirlinks</code>, you must trust all the symlinks in the copy or enable the <code>--munge-links</code> option on the receiving side! If it is possible for an untrusted user to create their own symlink to any real directory, the user could then (on a subsequent copy) replace the symlink with a real directory and affect the content of whatever directory the symlink references. For backup copies, you are better off using something like a bind mount instead of a symlink to modify your receiving hierarchy. </p>
 </dd>
<dd> <p> See also <code>--copy-dirlinks</code> for an analogous option for the sending side. </p>
 </dd>
<dd> <p> See the SYMBOLIC LINKS section for multi-option info. </p>
 </dd>
<dt><code>--hard-links</code>, <code>-H</code></dt>
<dd> <p> This tells rsync to look for hard-linked files in the source and link together the corresponding files on the destination. Without this option, hard-linked files in the source are treated as though they were separate files. </p>
 </dd>
<dd> <p> This option does NOT necessarily ensure that the pattern of hard links on the destination exactly matches that on the source. Cases in which the destination may end up with extra hard links include the following: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> If the destination contains extraneous hard-links (more linking than what is present in the source file list), the copying algorithm will not break them explicitly. However, if one or more of the paths have content differences, the normal file-update process will break those extra links (unless you are using the <code>--inplace</code> option). </p>
 </dd>
<dt>o</dt>
<dd> <p> If you specify a <code>--link-dest</code> directory that contains hard links, the linking of the destination files against the <code>--link-dest</code> files can cause some paths in the destination to become linked together due to the <code>--link-dest</code> associations. </p>
 </dd></dl>
</dl>
<dd> <p> Note that rsync can only detect hard links between files that are inside the transfer set. If rsync updates a file that has extra hard-link connections to files outside the transfer, that linkage will be broken. If you are tempted to use the <code>--inplace</code> option to avoid this breakage, be very careful that you know how your files are being updated so that you are certain that no unintended changes happen due to lingering hard links (and see the <code>--inplace</code> option for more caveats). </p>
 </dd>
<dd> <p> If incremental recursion is active (see <code>--inc-recursive</code>), rsync may transfer a missing hard-linked file before it finds that another link for that contents exists elsewhere in the hierarchy. This does not affect the accuracy of the transfer (i.e. which files are hard-linked together), just its efficiency (i.e. copying the data for a new, early copy of a hard-linked file that could have been found later in the transfer in another member of the hard-linked set of files). One way to avoid this inefficiency is to disable incremental recursion using the <code>--no-inc-recursive</code> option. </p>
 </dd>
<dt><code>--perms</code>, <code>-p</code></dt>
<dd> <p> This option causes the receiving rsync to set the destination permissions to be the same as the source permissions. (See also the <code>--chmod</code> option for a way to modify what rsync considers to be the source permissions.) </p>
 </dd>
<dd> <p> When this option is <i>off</i>, permissions are set as follows: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> Existing files (including updated files) retain their existing permissions, though the <code>--executability</code> option might change just the execute permission for the file. </p>
 </dd>
<dt>o</dt>
<dd> <p> New files get their &quot;normal&quot; permission bits set to the source file&#8217;s permissions masked with the receiving directory&#8217;s default permissions (either the receiving process&#8217;s umask, or the permissions specified via the destination directory&#8217;s default ACL), and their special permission bits disabled except in the case where a new directory inherits a setgid bit from its parent directory. </p>
 </dd></dl>
</dl>
<dd> <p> Thus, when <code>--perms</code> and <code>--executability</code> are both disabled, rsync&#8217;s behavior is the same as that of other file-copy utilities, such as <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) and <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1). </p>
 </dd>
<dd> <p> In summary: to give destination files (both old and new) the source permissions, use <code>--perms</code>. To give new files the destination-default permissions (while leaving existing files unchanged), make sure that the <code>--perms</code> option is off and use <code>--chmod=ugo=rwX</code> (which ensures that all non-masked bits get enabled). If you&#8217;d care to make this latter behavior easier to type, you could define a popt alias for it, such as putting this line in the file <code>~/.popt</code> (the following defines the <code>-Z</code> option, and includes <code>--no-g</code> to use the default group of the destination dir): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync alias -Z --no-p --no-g --chmod=ugo=rwX
</code></pre>
 </dd></dl>
</dl>
<dd> <p> You could then use this new option in a command such as this one: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avZ src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> (Caveat: make sure that <code>-a</code> does not follow <code>-Z</code>, or it will re-enable the two <code>--no-*</code> options mentioned above.) </p>
 </dd>
<dd> <p> The preservation of the destination&#8217;s setgid bit on newly-created directories when <code>--perms</code> is off was added in rsync 2.6.7. Older rsync versions erroneously preserved the three special permission bits for newly-created files when <code>--perms</code> was off, while overriding the destination&#8217;s setgid bit setting on a newly-created directory. Default ACL observance was added to the ACL patch for rsync 2.6.7, so older (or non-ACL-enabled) rsyncs use the umask even if default ACLs are present. (Keep in mind that it is the version of the receiving rsync that affects these behaviors.) </p>
 </dd>
<dt><code>--executability</code>, <code>-E</code></dt>
<dd> <p> This option causes rsync to preserve the executability (or non-executability) of regular files when <code>--perms</code> is not enabled. A regular file is considered to be executable if at least one &#8216;x&#8217; is turned on in its permissions. When an existing destination file&#8217;s executability differs from that of the corresponding source file, rsync modifies the destination file&#8217;s permissions as follows: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> To make a file non-executable, rsync turns off all its &#8216;x&#8217; permissions. </p>
 </dd>
<dt>o</dt>
<dd> <p> To make a file executable, rsync turns on each &#8216;x&#8217; permission that has a corresponding &#8216;r&#8217; permission enabled. </p>
 </dd></dl>
</dl>
<dd> <p> If <code>--perms</code> is enabled, this option is ignored. </p>
 </dd>
<dt><code>--acls</code>, <code>-A</code></dt>
<dd> <p> This option causes rsync to update the destination ACLs to be the same as the source ACLs. The option also implies <code>--perms</code>. </p>
 </dd>
<dd> <p> The source and destination systems must have compatible ACL entries for this option to work properly. See the <code>--fake-super</code> option for a way to backup and restore ACLs that are not compatible. </p>
 </dd>
<dt><code>--xattrs</code>, <code>-X</code></dt>
<dd> <p> This option causes rsync to update the destination extended attributes to be the same as the source ones. </p>
 </dd>
<dd> <p> For systems that support extended-attribute namespaces, a copy being done by a super-user copies all namespaces except system.*. A normal user only copies the user.* namespace. To be able to backup and restore non-user namespaces as a normal user, see the <code>--fake-super</code> option. </p>
 </dd>
<dd> <p> The above name filtering can be overridden by using one or more filter options with the <code>x</code> modifier. When you specify an xattr-affecting filter rule, rsync requires that you do your own system/user filtering, as well as any additional filtering for what xattr names are copied and what names are allowed to be deleted. For example, to skip the system namespace, you could specify: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--filter='-x system.*'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> To skip all namespaces except the user namespace, you could specify a negated-user match: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--filter='-x! user.*'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> To prevent any attributes from being deleted, you could specify a receiver-only rule that excludes all names: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--filter='-xr *'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Note that the <code>-X</code> option does not copy rsync&#8217;s special xattr values (e.g. those used by <code>--fake-super</code>) unless you repeat the option (e.g. <code>-XX</code>). This &quot;copy all xattrs&quot; mode cannot be used with <code>--fake-super</code>. </p>
 </dd>
<dt><code>--chmod=CHMOD</code></dt>
<dd> <p> This option tells rsync to apply one or more comma-separated &quot;chmod&quot; modes to the permission of the files in the transfer. The resulting value is treated as though it were the permissions that the sending side supplied for the file, which means that this option can seem to have no effect on existing files if <code>--perms</code> is not enabled. </p>
 </dd>
<dd> <p> In addition to the normal parsing rules specified in the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) manpage, you can specify an item that should only apply to a directory by prefixing it with a &#8216;D&#8217;, or specify an item that should only apply to a file by prefixing it with a &#8216;F&#8217;. For example, the following will ensure that all directories get marked set-gid, that no files are other-writable, that both are user-writable and group-writable, and that both have consistent executability across all bits: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--chmod=Dg+s,ug+w,Fo-w,+X
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Using octal mode numbers is also allowed: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--chmod=D2775,F664
</code></pre>
 </dd></dl>
</dl>
<dd> <p> It is also legal to specify multiple <code>--chmod</code> options, as each additional option is just appended to the list of changes to make. </p>
 </dd>
<dd> <p> See the <code>--perms</code> and <code>--executability</code> options for how the resulting permission value can be applied to the files in the transfer. </p>
 </dd>
<dt><code>--owner</code>, <code>-o</code></dt>
<dd> <p> This option causes rsync to set the owner of the destination file to be the same as the source file, but only if the receiving rsync is being run as the super-user (see also the <code>--super</code> and <code>--fake-super</code> options). Without this option, the owner of new and/or transferred files are set to the invoking user on the receiving side. </p>
 </dd>
<dd> <p> The preservation of ownership will associate matching names by default, but may fall back to using the ID number in some circumstances (see also the <code>--numeric-ids</code> option for a full discussion). </p>
 </dd>
<dt><code>--group</code>, <code>-g</code></dt>
<dd> <p> This option causes rsync to set the group of the destination file to be the same as the source file. If the receiving program is not running as the super-user (or if <code>--no-super</code> was specified), only groups that the invoking user on the receiving side is a member of will be preserved. Without this option, the group is set to the default group of the invoking user on the receiving side. </p>
 </dd>
<dd> <p> The preservation of group information will associate matching names by default, but may fall back to using the ID number in some circumstances (see also the <code>--numeric-ids</code> option for a full discussion). </p>
 </dd>
<dt><code>--devices</code></dt>
<dd> <p> This option causes rsync to transfer character and block device files to the remote system to recreate these devices. If the receiving rsync is not being run as the super-user, rsync silently skips creating the device files (see also the <code>--super</code> and <code>--fake-super</code> options). </p>
 </dd>
<dd> <p> By default, rsync generates a &quot;non-regular file&quot; warning for each device file encountered when this option is not set. You can silence the warning by specifying <code>--info=nonreg0</code>. </p>
 </dd>
<dt><code>--specials</code></dt>
<dd> <p> This option causes rsync to transfer special files, such as named sockets and fifos. If the receiving rsync is not being run as the super-user, rsync silently skips creating the special files (see also the <code>--super</code> and <code>--fake-super</code> options). </p>
 </dd>
<dd> <p> By default, rsync generates a &quot;non-regular file&quot; warning for each special file encountered when this option is not set. You can silence the warning by specifying <code>--info=nonreg0</code>. </p>
 </dd>
<dt><code>-D</code></dt>
<dd> <p> The <code>-D</code> option is equivalent to &quot;<code>--devices</code> <code>--specials</code>&quot;. </p>
 </dd>
<dt><code>--copy-devices</code></dt>
<dd> <p> This tells rsync to treat a device on the sending side as a regular file, allowing it to be copied to a normal destination file (or another device if <code>--write-devices</code> was also specified). </p>
 </dd>
<dd> <p> This option is refused by default by an rsync daemon. </p>
 </dd>
<dt><code>--write-devices</code></dt>
<dd> <p> This tells rsync to treat a device on the receiving side as a regular file, allowing the writing of file data into a device. </p>
 </dd>
<dd> <p> This option implies the <code>--inplace</code> option. </p>
 </dd>
<dd> <p> Be careful using this, as you should know what devices are present on the receiving side of the transfer, especially when running rsync as root. </p>
 </dd>
<dd> <p> This option is refused by default by an rsync daemon. </p>
 </dd>
<dt><code>--times</code>, <code>-t</code></dt>
<dd> <p> This tells rsync to transfer modification times along with the files and update them on the remote system. Note that if this option is not used, the optimization that excludes files that have not been modified cannot be effective; in other words, a missing <code>-t</code> (or <code>-a</code>) will cause the next transfer to behave as if it used <code>--ignore-times</code> (<code>-I</code>), causing all files to be updated (though rsync&#8217;s delta-transfer algorithm will make the update fairly efficient if the files haven&#8217;t actually changed, you&#8217;re much better off using <code>-t</code>). </p>
 </dd>
<dd> <p> A modern rsync that is using transfer protocol 30 or 31 conveys a modify time using up to 8-bytes. If rsync is forced to speak an older protocol (perhaps due to the remote rsync being older than 3.0.0) a modify time is conveyed using 4-bytes. Prior to 3.2.7, these shorter values could convey a date range of 13-Dec-1901 to 19-Jan-2038. Beginning with 3.2.7, these 4-byte values now convey a date range of 1-Jan-1970 to 7-Feb-2106. If you have files dated older than 1970, make sure your rsync executables are upgraded so that the full range of dates can be conveyed. </p>
 </dd>
<dt><code>--atimes</code>, <code>-U</code></dt>
<dd> <p> This tells rsync to set the access (use) times of the destination files to the same value as the source files. </p>
 </dd>
<dd> <p> If repeated, it also sets the <code>--open-noatime</code> option, which can help you to make the sending and receiving systems have the same access times on the transferred files without needing to run rsync an extra time after a file is transferred. </p>
 </dd>
<dd> <p> Note that some older rsync versions (prior to 3.2.0) may have been built with a pre-release <code>--atimes</code> patch that does not imply <code>--open-noatime</code> when this option is repeated. </p>
 </dd>
<dt><code>--open-noatime</code></dt>
<dd> <p> This tells rsync to open files with the O_NOATIME flag (on systems that support it) to avoid changing the access time of the files that are being transferred. If your OS does not support the O_NOATIME flag then rsync will silently ignore this option. Note also that some filesystems are mounted to avoid updating the atime on read access even without the O_NOATIME flag being set. </p>
 </dd>
<dt><code>--crtimes</code>, <code>-N,</code></dt>
<dd> <p> This tells rsync to set the create times (newness) of the destination files to the same value as the source files. </p>
 </dd>
<dt><code>--omit-dir-times</code>, <code>-O</code></dt>
<dd> <p> This tells rsync to omit directories when it is preserving modification, access, and create times. If NFS is sharing the directories on the receiving side, it is a good idea to use <code>-O</code>. This option is inferred if you use <code>--backup</code> without <code>--backup-dir</code>. </p>
 </dd>
<dd> <p> This option also has the side-effect of avoiding early creation of missing sub-directories when incremental recursion is enabled, as discussed in the <code>--inc-recursive</code> section. </p>
 </dd>
<dt><code>--omit-link-times</code>, <code>-J</code></dt>
<dd> <p> This tells rsync to omit symlinks when it is preserving modification, access, and create times. </p>
 </dd>
<dt><code>--super</code></dt>
<dd> <p> This tells the receiving side to attempt super-user activities even if the receiving rsync wasn&#8217;t run by the super-user. These activities include: preserving users via the <code>--owner</code> option, preserving all groups (not just the current user&#8217;s groups) via the <code>--group</code> option, and copying devices via the <code>--devices</code> option. This is useful for systems that allow such activities without being the super-user, and also for ensuring that you will get errors if the receiving side isn&#8217;t being run as the super-user. To turn off super-user activities, the super-user can use <code>--no-super</code>. </p>
 </dd>
<dt><code>--fake-super</code></dt>
<dd> <p> When this option is enabled, rsync simulates super-user activities by saving/restoring the privileged attributes via special extended attributes that are attached to each file (as needed). This includes the file&#8217;s owner and group (if it is not the default), the file&#8217;s device info (device &amp; special files are created as empty text files), and any permission bits that we won&#8217;t allow to be set on the real file (e.g. the real file gets u-s,g-s,o-t for safety) or that would limit the owner&#8217;s access (since the real super-user can always access/change a file, the files we create can always be accessed/changed by the creating user). This option also handles ACLs (if <code>--acls</code> was specified) and non-user extended attributes (if <code>--xattrs</code> was specified). </p>
 </dd>
<dd> <p> This is a good way to backup data without using a super-user, and to store ACLs from incompatible systems. </p>
 </dd>
<dd> <p> The <code>--fake-super</code> option only affects the side where the option is used. To affect the remote side of a remote-shell connection, use the <code>--remote-option</code> (<code>-M</code>) option: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av -M--fake-super /src/ host:/dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> For a local copy, this option affects both the source and the destination. If you wish a local copy to enable this option just for the destination files, specify <code>-M--fake-super</code>. If you wish a local copy to enable this option just for the source files, combine <code>--fake-super</code> with <code>-M--super</code>. </p>
 </dd>
<dd> <p> This option is overridden by both <code>--super</code> and <code>--no-super</code>. </p>
 </dd>
<dd> <p> See also the <code>fake super</code> setting in the daemon&#8217;s rsyncd.conf file. </p>
 </dd>
<dt><code>--sparse</code>, <code>-S</code></dt>
<dd> <p> Try to handle sparse files efficiently so they take up less space on the destination. If combined with <code>--inplace</code> the file created might not end up with sparse blocks with some combinations of kernel version and/or filesystem type. If <code>--whole-file</code> is in effect (e.g. for a local copy) then it will always work because rsync truncates the file prior to writing out the updated version. </p>
 </dd>
<dd> <p> Note that versions of rsync older than 3.1.3 will reject the combination of <code>--sparse</code> and <code>--inplace</code>. </p>
 </dd>
<dt><code>--preallocate</code></dt>
<dd> <p> This tells the receiver to allocate each destination file to its eventual size before writing data to the file. Rsync will only use the real filesystem-level preallocation support provided by Linux&#8217;s <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) system call or Cygwin&#8217;s <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3), not the slow glibc implementation that writes a null byte into each block. </p>
 </dd>
<dd> <p> Without this option, larger files may not be entirely contiguous on the filesystem, but with this option rsync will probably copy more slowly. If the destination is not an extent-supporting filesystem (such as ext4, xfs, NTFS, etc.), this option may have no positive effect at all. </p>
 </dd>
<dd> <p> If combined with <code>--sparse</code>, the file will only have sparse blocks (as opposed to allocated sequences of null bytes) if the kernel version and filesystem type support creating holes in the allocated data. </p>
 </dd>
<dt><code>--dry-run</code>, <code>-n</code></dt>
<dd> <p> This makes rsync perform a trial run that doesn&#8217;t make any changes (and produces mostly the same output as a real run). It is most commonly used in combination with the <code>--verbose</code> (<code>-v</code>) and/or <code>--itemize-changes</code> (<code>-i</code>) options to see what an rsync command is going to do before one actually runs it. </p>
 </dd>
<dd> <p> The output of <code>--itemize-changes</code> is supposed to be exactly the same on a dry run and a subsequent real run (barring intentional trickery and system call failures); if it isn&#8217;t, that&#8217;s a bug. Other output should be mostly unchanged, but may differ in some areas. Notably, a dry run does not send the actual data for file transfers, so <code>--progress</code> has no effect, the &quot;bytes sent&quot;, &quot;bytes received&quot;, &quot;literal data&quot;, and &quot;matched data&quot; statistics are too small, and the &quot;speedup&quot; value is equivalent to a run where no file transfers were needed. </p>
 </dd>
<dt><code>--whole-file</code>, <code>-W</code></dt>
<dd> <p> This option disables rsync&#8217;s delta-transfer algorithm, which causes all transferred files to be sent whole. The transfer may be faster if this option is used when the bandwidth between the source and destination machines is higher than the bandwidth to disk (especially when the &quot;disk&quot; is actually a networked filesystem). This is the default when both the source and destination are specified as local paths, but only if no batch-writing option is in effect. </p>
 </dd>
<dt><code>--no-whole-file</code>, <code>--no-W</code></dt>
<dd> <p> Disable whole-file updating when it is enabled by default for a local transfer. This usually slows rsync down, but it can be useful if you are trying to minimize the writes to the destination file (if combined with <code>--inplace</code>) or for testing the checksum-based update algorithm. </p>
 </dd>
<dd> <p> See also the <code>--whole-file</code> option. </p>
 </dd>
<dt><code>--checksum-choice=STR</code>, <code>--cc=STR</code></dt>
<dd> <p> This option overrides the checksum algorithms. If one algorithm name is specified, it is used for both the transfer checksums and (assuming <code>--checksum</code> is specified) the pre-transfer checksums. If two comma-separated names are supplied, the first name affects the transfer checksums, and the second name affects the pre-transfer checksums (<code>-c</code>). </p>
 </dd>
<dd> <p> The checksum options that you may be able to use are: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <code>auto</code> (the default automatic choice) </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>xxh128</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>xxh3</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>xxh64</code> (aka <code>xxhash</code>) </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>md5</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>md4</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>sha1</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>none</code> </p>
 </dd></dl>
</dl>
<dd> <p> Run <code>rsync --version</code> to see the default checksum list compiled into your version (which may differ from the list above). </p>
 </dd>
<dd> <p> If &quot;none&quot; is specified for the first (or only) name, the <code>--whole-file</code> option is forced on and no checksum verification is performed on the transferred data. If &quot;none&quot; is specified for the second (or only) name, the <code>--checksum</code> option cannot be used. </p>
 </dd>
<dd> <p> The &quot;auto&quot; option is the default, where rsync bases its algorithm choice on a negotiation between the client and the server as follows: </p>
 </dd>
<dd> <p> When both sides of the transfer are at least 3.2.0, rsync chooses the first algorithm in the client&#8217;s list of choices that is also in the server&#8217;s list of choices. If no common checksum choice is found, rsync exits with an error. If the remote rsync is too old to support checksum negotiation, a value is chosen based on the protocol version (which chooses between MD5 and various flavors of MD4 based on protocol age). </p>
 </dd>
<dd> <p> The default order can be customized by setting the environment variable <code>RSYNC_CHECKSUM_LIST</code> to a space-separated list of acceptable checksum names. If the string contains a &quot;<code>&amp;</code>&quot; character, it is separated into the &quot;client string &amp; server string&quot;, otherwise the same string applies to both. If the string (or string portion) contains no non-whitespace characters, the default checksum list is used. This method does not allow you to specify the transfer checksum separately from the pre-transfer checksum, and it discards &quot;auto&quot; and all unknown checksum names. A list with only invalid names results in a failed negotiation. </p>
 </dd>
<dd> <p> The use of the <code>--checksum-choice</code> option overrides this environment list. </p>
 </dd>
<dt><code>--one-file-system</code>, <code>-x</code></dt>
<dd> <p> This tells rsync to avoid crossing a filesystem boundary when recursing. This does not limit the user&#8217;s ability to specify items to copy from multiple filesystems, just rsync&#8217;s recursion through the hierarchy of each directory that the user specified, and also the analogous recursion on the receiving side during deletion. Also keep in mind that rsync treats a &quot;bind&quot; mount to the same device as being on the same filesystem. </p>
 </dd>
<dd> <p> If this option is repeated, rsync omits all mount-point directories from the copy. Otherwise, it includes an empty directory at each mount-point it encounters (using the attributes of the mounted directory because those of the underlying mount-point directory are inaccessible). </p>
 </dd>
<dd> <p> If rsync has been told to collapse symlinks (via <code>--copy-links</code> or <code>--copy-unsafe-links</code>), a symlink to a directory on another device is treated like a mount-point. Symlinks to non-directories are unaffected by this option. </p>
 </dd>
<dt><code>--ignore-non-existing</code>, <code>--existing</code></dt>
<dd> <p> This tells rsync to skip creating files (including directories) that do not exist yet on the destination. If this option is combined with the <code>--ignore-existing</code> option, no files will be updated (which can be useful if all you want to do is delete extraneous files). </p>
 </dd>
<dd> <p> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects. </p>
 </dd>
<dt><code>--ignore-existing</code></dt>
<dd> <p> This tells rsync to skip updating files that already exist on the destination (this does <i>not</i> ignore existing directories, or nothing would get done). See also <code>--ignore-non-existing</code>. </p>
 </dd>
<dd> <p> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects. </p>
 </dd>
<dd> <p> This option can be useful for those doing backups using the <code>--link-dest</code> option when they need to continue a backup run that got interrupted. Since a <code>--link-dest</code> run is copied into a new directory hierarchy (when it is used properly), using [<code>--ignore-existing</code> will ensure that the already-handled files don&#8217;t get tweaked (which avoids a change in permissions on the hard-linked files). This does mean that this option is only looking at the existing files in the destination hierarchy itself. </p>
 </dd>
<dd> <p> When <code>--info=skip2</code> is used rsync will output &quot;FILENAME exists (INFO)&quot; messages where the INFO indicates one of &quot;type change&quot;, &quot;sum change&quot; (requires <code>-c</code>), &quot;file change&quot; (based on the quick check), &quot;attr change&quot;, or &quot;uptodate&quot;. Using <code>--info=skip1</code> (which is also implied by 2 <code>-v</code> options) outputs the exists message without the INFO suffix. </p>
 </dd>
<dt><code>--remove-source-files</code></dt>
<dd> <p> This tells rsync to remove from the sending side the files (meaning non-directories) that are a part of the transfer and have been successfully duplicated on the receiving side. </p>
 </dd>
<dd> <p> Note that you should only use this option on source files that are quiescent. If you are using this to move files that show up in a particular directory over to another host, make sure that the finished files get renamed into the source directory, not directly written into it, so that rsync can&#8217;t possibly transfer a file that is not yet fully written. If you can&#8217;t first write the files into a different directory, you should use a naming idiom that lets rsync avoid transferring files that are not yet finished (e.g. name the file &quot;foo.new&quot; when it is written, rename it to &quot;foo&quot; when it is done, and then use the option <code>--exclude=&#8216;*.new&#8217;</code> for the rsync transfer). </p>
 </dd>
<dd> <p> Starting with 3.1.0, rsync will skip the sender-side removal (and output an error) if the file&#8217;s size or modify time has not stayed unchanged. </p>
 </dd>
<dd> <p> Starting with 3.2.6, a local rsync copy will ensure that the sender does not remove a file the receiver just verified, such as when the user accidentally makes the source and destination directory the same path. </p>
 </dd>
<dt><code>--delete</code></dt>
<dd> <p> This tells rsync to delete extraneous files from the receiving side (ones that aren&#8217;t on the sending side), but only for the directories that are being synchronized. You must have asked rsync to send the whole directory (e.g. &quot;<code>dir</code>&quot; or &quot;<code>dir/</code>&quot;) without using a wildcard for the directory&#8217;s contents (e.g. &quot;<code>dir/*</code>&quot;) since the wildcard is expanded by the shell and rsync thus gets a request to transfer individual files, not the files&#8217; parent directory. Files that are excluded from the transfer are also excluded from being deleted unless you use the <code>--delete-excluded</code> option or mark the rules as only matching on the sending side (see the include/exclude modifiers in the FILTER RULES section). </p>
 </dd>
<dd> <p> Prior to rsync 2.6.7, this option would have no effect unless <code>--recursive</code> was enabled. Beginning with 2.6.7, deletions will also occur when <code>--dirs</code> (<code>-d</code>) is enabled, but only for directories whose contents are being copied. </p>
 </dd>
<dd> <p> This option can be dangerous if used incorrectly! It is a very good idea to first try a run using the <code>--dry-run</code> (<code>-n</code>) option to see what files are going to be deleted. </p>
 </dd>
<dd> <p> If the sending side detects any I/O errors, then the deletion of any files at the destination will be automatically disabled. This is to prevent temporary filesystem failures (such as NFS errors) on the sending side from causing a massive deletion of files on the destination. You can override this with the <code>--ignore-errors</code> option. </p>
 </dd>
<dd> <p> The <code>--delete</code> option may be combined with one of the --delete-WHEN options without conflict, as well as <code>--delete-excluded</code>. However, if none of the <code>--delete-WHEN</code> options are specified, rsync will choose the <code>--delete-during</code> algorithm when talking to rsync 3.0.0 or newer, or the <code>--delete-before</code> algorithm when talking to an older rsync. See also <code>--delete-delay</code> and <code>--delete-after</code>. </p>
 </dd>
<dt><code>--delete-before</code></dt>
<dd> <p> Request that the file-deletions on the receiving side be done before the transfer starts. See <code>--delete</code> (which is implied) for more details on file-deletion. </p>
 </dd>
<dd> <p> Deleting before the transfer is helpful if the filesystem is tight for space and removing extraneous files would help to make the transfer possible. However, it does introduce a delay before the start of the transfer, and this delay might cause the transfer to timeout (if <code>--timeout</code> was specified). It also forces rsync to use the old, non-incremental recursion algorithm that requires rsync to scan all the files in the transfer into memory at once (see <code>--recursive</code>). </p>
 </dd>
<dt><code>--delete-during</code>, <code>--del</code></dt>
<dd> <p> Request that the file-deletions on the receiving side be done incrementally as the transfer happens. The per-directory delete scan is done right before each directory is checked for updates, so it behaves like a more efficient <code>--delete-before</code>, including doing the deletions prior to any per-directory filter files being updated. This option was first added in rsync version 2.6.4. See <code>--delete</code> (which is implied) for more details on file-deletion. </p>
 </dd>
<dt><code>--delete-delay</code></dt>
<dd> <p> Request that the file-deletions on the receiving side be computed during the transfer (like <code>--delete-during</code>), and then removed after the transfer completes. This is useful when combined with <code>--delay-updates</code> and/or <code>--fuzzy</code>, and is more efficient than using <code>--delete-after</code> (but can behave differently, since <code>--delete-after</code> computes the deletions in a separate pass after all updates are done). If the number of removed files overflows an internal buffer, a temporary file will be created on the receiving side to hold the names (it is removed while open, so you shouldn&#8217;t see it during the transfer). If the creation of the temporary file fails, rsync will try to fall back to using <code>--delete-after</code> (which it cannot do if <code>--recursive</code> is doing an incremental scan). See <code>--delete</code> (which is implied) for more details on file-deletion. </p>
 </dd>
<dt><code>--delete-after</code></dt>
<dd> <p> Request that the file-deletions on the receiving side be done after the transfer has completed. This is useful if you are sending new per-directory merge files as a part of the transfer and you want their exclusions to take effect for the delete phase of the current transfer. It also forces rsync to use the old, non-incremental recursion algorithm that requires rsync to scan all the files in the transfer into memory at once (see <code>--recursive</code>). See <code>--delete</code> (which is implied) for more details on file-deletion. </p>
 </dd>
<dd> <p> See also the <code>--delete-delay</code> option that might be a faster choice for those that just want the deletions to occur at the end of the transfer. </p>
 </dd>
<dt><code>--delete-excluded</code></dt>
<dd> <p> This option turns any unqualified exclude/include rules into server-side rules that do not affect the receiver&#8217;s deletions. </p>
 </dd>
<dd> <p> By default, an exclude or include has both a server-side effect (to &quot;hide&quot; and &quot;show&quot; files when building the server&#8217;s file list) and a receiver-side effect (to &quot;protect&quot; and &quot;risk&quot; files when deletions are occurring). Any rule that has no modifier to specify what sides it is executed on will be instead treated as if it were a server-side rule only, avoiding any &quot;protect&quot; effects of the rules. </p>
 </dd>
<dd> <p> A rule can still apply to both sides even with this option specified if the rule is given both the sender &amp; receiver modifier letters (e.g., <code>-f&#8217;-sr foo&#8217;</code>). Receiver-side protect/risk rules can also be explicitly specified to limit the deletions. This saves you from having to edit a bunch of <code>-f&#8217;- foo&#8217;</code> rules into <code>-f&#8217;-s foo&#8217;</code> (aka <code>-f&#8217;H foo&#8217;</code>) rules (not to mention the corresponding includes). </p>
 </dd>
<dd> <p> See the FILTER RULES section for more information. See <code>--delete</code> (which is implied) for more details on deletion. </p>
 </dd>
<dt><code>--ignore-missing-args</code></dt>
<dd> <p> When rsync is first processing the explicitly requested source files (e.g. command-line arguments or <code>--files-from</code> entries), it is normally an error if the file cannot be found. This option suppresses that error, and does not try to transfer the file. This does not affect subsequent vanished-file errors if a file was initially found to be present and later is no longer there. </p>
 </dd>
<dt><code>--delete-missing-args</code></dt>
<dd> <p> This option takes the behavior of the (implied) <code>--ignore-missing-args</code> option a step farther: each missing arg will become a deletion request of the corresponding destination file on the receiving side (should it exist). If the destination file is a non-empty directory, it will only be successfully deleted if <code>--force</code> or <code>--delete</code> are in effect. Other than that, this option is independent of any other type of delete processing. </p>
 </dd>
<dd> <p> The missing source files are represented by special file-list entries which display as a &quot;<code>*missing</code>&quot; entry in the <code>--list-only</code> output. </p>
 </dd>
<dt><code>--ignore-errors</code></dt>
<dd> <p> Tells <code>--delete</code> to go ahead and delete files even when there are I/O errors. </p>
 </dd>
<dt><code>--force</code></dt>
<dd> <p> This option tells rsync to delete a non-empty directory when it is to be replaced by a non-directory. This is only relevant if deletions are not active (see <code>--delete</code> for details). </p>
 </dd>
<dd> <p> Note for older rsync versions: <code>--force</code> used to still be required when using <code>--delete-after</code>, and it used to be non-functional unless the <code>--recursive</code> option was also enabled. </p>
 </dd>
<dt><code>--max-delete=NUM</code></dt>
<dd> <p> This tells rsync not to delete more than NUM files or directories. If that limit is exceeded, all further deletions are skipped through the end of the transfer. At the end, rsync outputs a warning (including a count of the skipped deletions) and exits with an error code of 25 (unless some more important error condition also occurred). </p>
 </dd>
<dd> <p> Beginning with version 3.0.0, you may specify <code>--max-delete=0</code> to be warned about any extraneous files in the destination without removing any of them. Older clients interpreted this as &quot;unlimited&quot;, so if you don&#8217;t know what version the client is, you can use the less obvious <code>--max-delete=-1</code> as a backward-compatible way to specify that no deletions be allowed (though really old versions didn&#8217;t warn when the limit was exceeded). </p>
 </dd>
<dt><code>--max-size=SIZE</code></dt>
<dd> <p> This tells rsync to avoid transferring any file that is larger than the specified SIZE. A numeric value can be suffixed with a string to indicate the numeric units or left unqualified to specify bytes. Feel free to use a fractional value along with the units, such as <code>--max-size=1.5m</code>. </p>
 </dd>
<dd> <p> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects. </p>
 </dd>
<dd> <p> The first letter of a units string can be <code>B</code> (bytes), <code>K</code> (kilo), <code>M</code> (mega), <code>G</code> (giga), <code>T</code> (tera), or <code>P</code> (peta). If the string is a single char or has &quot;ib&quot; added to it (e.g. &quot;G&quot; or &quot;GiB&quot;) then the units are multiples of 1024. If you use a two-letter suffix that ends with a &quot;B&quot; (e.g. &quot;kb&quot;) then you get units that are multiples of 1000. The string&#8217;s letters can be any mix of upper and lower-case that you want to use. </p>
 </dd>
<dd> <p> Finally, if the string ends with either &quot;+1&quot; or &quot;-1&quot;, it is offset by one byte in the indicated direction. The largest possible value is usually <code>8192P-1</code>. </p>
 </dd>
<dd> <p> Examples: <code>--max-size=1.5mb-1</code> is 1499999 bytes, and <code>--max-size=2g+1</code> is 2147483649 bytes. </p>
 </dd>
<dd> <p> Note that rsync versions prior to 3.1.0 did not allow <code>--max-size=0</code>. </p>
 </dd>
<dt><code>--min-size=SIZE</code></dt>
<dd> <p> This tells rsync to avoid transferring any file that is smaller than the specified SIZE, which can help in not transferring small, junk files. See the <code>--max-size</code> option for a description of SIZE and other info. </p>
 </dd>
<dd> <p> Note that rsync versions prior to 3.1.0 did not allow <code>--min-size=0</code>. </p>
 </dd>
<dt><code>--max-alloc=SIZE</code></dt>
<dd> <p> By default rsync limits an individual malloc/realloc to about 1GB in size. For most people this limit works just fine and prevents a protocol error causing rsync to request massive amounts of memory. However, if you have many millions of files in a transfer, a large amount of server memory, and you don&#8217;t want to split up your transfer into multiple parts, you can increase the per-allocation limit to something larger and rsync will consume more memory. </p>
 </dd>
<dd> <p> Keep in mind that this is not a limit on the total size of allocated memory. It is a sanity-check value for each individual allocation. </p>
 </dd>
<dd> <p> See the <code>--max-size</code> option for a description of how SIZE can be specified. The default suffix if none is given is bytes. </p>
 </dd>
<dd> <p> Beginning in 3.2.3, a value of 0 specifies no limit. </p>
 </dd>
<dd> <p> You can set a default value using the environment variable <code>RSYNC_MAX_ALLOC</code> using the same SIZE values as supported by this option. If the remote rsync doesn&#8217;t understand the <code>--max-alloc</code> option, you can override an environmental value by specifying <code>--max-alloc=1g</code>, which will make rsync avoid sending the option to the remote side (because &quot;1G&quot; is the default). </p>
 </dd>
<dt><code>--block-size=SIZE</code>, <code>-B</code></dt>
<dd> <p> This forces the block size used in rsync&#8217;s delta-transfer algorithm to a fixed value. It is normally selected based on the size of each file being updated. See the technical report for details. </p>
 </dd>
<dd> <p> Beginning in 3.2.3 the SIZE can be specified with a suffix as detailed in the <code>--max-size</code> option. Older versions only accepted a byte count. </p>
 </dd>
<dt><code>--rsh=COMMAND</code>, <code>-e</code></dt>
<dd> <p> This option allows you to choose an alternative remote shell program to use for communication between the local and remote copies of rsync. Typically, rsync is configured to use ssh by default, but you may prefer to use rsh on a local network. </p>
 </dd>
<dd> <p> If this option is used with <code>[user@]host::module/path</code>, then the remote shell <i>COMMAND</i> will be used to run an rsync daemon on the remote host, and all data will be transmitted through that remote shell connection, rather than through a direct socket connection to a running rsync daemon on the remote host. See the USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION section above. </p>
 </dd>
<dd> <p> Beginning with rsync 3.2.0, the <code>RSYNC_PORT</code> environment variable will be set when a daemon connection is being made via a remote-shell connection. It is set to 0 if the default daemon port is being assumed, or it is set to the value of the rsync port that was specified via either the <code>--port</code> option or a non-empty port value in an <code>rsync://</code> URL. This allows the script to discern if a non-default port is being requested, allowing for things such as an SSL or stunnel helper script to connect to a default or alternate port. </p>
 </dd>
<dd> <p> Command-line arguments are permitted in COMMAND provided that COMMAND is presented to rsync as a single argument. You must use spaces (not tabs or other whitespace) to separate the command and args from each other, and you can use single- and/or double-quotes to preserve spaces in an argument (but not backslashes). Note that doubling a single-quote inside a single-quoted string gives you a single-quote; likewise for double-quotes (though you need to pay attention to which quotes your shell is parsing and which quotes rsync is parsing). Some examples: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>-e 'ssh -p 2234'
-e 'ssh -o &quot;ProxyCommand nohup ssh firewall nc -w1 %h %p&quot;'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> (Note that ssh users can alternately customize site-specific connect options in their .ssh/config file.) </p>
 </dd>
<dd> <p> You can also choose the remote shell program using the <code>RSYNC_RSH</code> environment variable, which accepts the same range of values as <code>-e</code>. </p>
 </dd>
<dd> <p> See also the <code>--blocking-io</code> option which is affected by this option. </p>
 </dd>
<dt><code>--rsync-path=PROGRAM</code></dt>
<dd> <p> Use this to specify what program is to be run on the remote machine to start-up rsync. Often used when rsync is not in the default remote-shell&#8217;s path (e.g. <code>--rsync-path=/usr/local/bin/rsync</code>). Note that PROGRAM is run with the help of a shell, so it can be any program, script, or command sequence you&#8217;d care to run, so long as it does not corrupt the standard-in &amp; standard-out that rsync is using to communicate. </p>
 </dd>
<dd> <p> One tricky example is to set a different default directory on the remote machine for use with the <code>--relative</code> option. For instance: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avR --rsync-path=&quot;cd /a/b &amp;&amp; rsync&quot; host:c/d /e/
</code></pre>
 </dd></dl>
</dl>
<dt><code>--remote-option=OPTION</code>, <code>-M</code></dt>
<dd> <p> This option is used for more advanced situations where you want certain effects to be limited to one side of the transfer only. For instance, if you want to pass <code>--log-file=FILE</code> and <code>--fake-super</code> to the remote system, specify it like this: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av -M --log-file=foo -M--fake-super src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> If you want to have an option affect only the local side of a transfer when it normally affects both sides, send its negation to the remote side. Like this: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av -x -M--no-x src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Be cautious using this, as it is possible to toggle an option that will cause rsync to have a different idea about what data to expect next over the socket, and that will make it fail in a cryptic fashion. </p>
 </dd>
<dd> <p> Note that you should use a separate <code>-M</code> option for each remote option you want to pass. On older rsync versions, the presence of any spaces in the remote-option arg could cause it to be split into separate remote args, but this requires the use of <code>--old-args</code> in a modern rsync. </p>
 </dd>
<dd> <p> When performing a local transfer, the &quot;local&quot; side is the sender and the &quot;remote&quot; side is the receiver. </p>
 </dd>
<dd> <p> Note some versions of the popt option-parsing library have a bug in them that prevents you from using an adjacent arg with an equal in it next to a short option letter (e.g. <code>-M--log-file=/tmp/foo</code>). If this bug affects your version of popt, you can use the version of popt that is included with rsync. </p>
 </dd>
<dt><code>--cvs-exclude</code>, <code>-C</code></dt>
<dd> <p> This is a useful shorthand for excluding a broad range of files that you often don&#8217;t want to transfer between systems. It uses a similar algorithm to CVS to determine if a file should be ignored. </p>
 </dd>
<dd> <p> The exclude list is initialized to exclude the following items (these initial items are marked as perishable -- see the FILTER RULES section): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>RCS</code> <code>SCCS</code> <code>CVS</code> <code>CVS.adm</code> <code>RCSLOG</code> <code>cvslog.*</code> <code>tags</code> <code>TAGS</code> <code>.make.state</code> <code>.nse_depinfo</code> <code>*~</code> <code>#*</code> <code>.#*</code> <code>,*</code> <code>_$*</code> <code>*$</code> <code>*.old</code> <code>*.bak</code> <code>*.BAK</code> <code>*.orig</code> <code>*.rej</code> <code>.del-*</code> <code>*.a</code> <code>*.olb</code> <code>*.o</code> <code>*.obj</code> <code>*.so</code> <code>*.exe</code> <code>*.Z</code> <code>*.elc</code> <code>*.ln</code> <code>core</code> <code>.svn/</code> <code>.git/</code> <code>.hg/</code> <code>.bzr/</code> </p>
 </dd></dl>
</dl>
<dd> <p> then, files listed in a $HOME/.cvsignore are added to the list and any files listed in the CVSIGNORE environment variable (all cvsignore names are delimited by whitespace). </p>
 </dd>
<dd> <p> Finally, any file is ignored if it is in the same directory as a .cvsignore file and matches one of the patterns listed therein. Unlike rsync&#8217;s filter/exclude files, these patterns are split on whitespace. See the <code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1) manual for more information. </p>
 </dd>
<dd> <p> If you&#8217;re combining <code>-C</code> with your own <code>--filter</code> rules, you should note that these CVS excludes are appended at the end of your own rules, regardless of where the <code>-C</code> was placed on the command-line. This makes them a lower priority than any rules you specified explicitly. If you want to control where these CVS excludes get inserted into your filter rules, you should omit the <code>-C</code> as a command-line option and use a combination of <code>--filter=:C</code> and <code>--filter=-C</code> (either on your command-line or by putting the &quot;:C&quot; and &quot;-C&quot; rules into a filter file with your other rules). The first option turns on the per-directory scanning for the .cvsignore file. The second option does a one-time import of the CVS excludes mentioned above. </p>
 </dd>
<dt><code>--filter=RULE</code>, <code>-f</code></dt>
<dd> <p> This option allows you to add rules to selectively exclude certain files from the list of files to be transferred. This is most useful in combination with a recursive transfer. </p>
 </dd>
<dd> <p> You may use as many <code>--filter</code> options on the command line as you like to build up the list of files to exclude. If the filter contains whitespace, be sure to quote it so that the shell gives the rule to rsync as a single argument. The text below also mentions that you can use an underscore to replace the space that separates a rule from its arg. </p>
 </dd>
<dd> <p> See the FILTER RULES section for detailed information on this option. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> The <code>-F</code> option is a shorthand for adding two <code>--filter</code> rules to your command. The first time it is used is a shorthand for this rule: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--filter='dir-merge /.rsync-filter'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This tells rsync to look for per-directory .rsync-filter files that have been sprinkled through the hierarchy and use their rules to filter the files in the transfer. If <code>-F</code> is repeated, it is a shorthand for this rule: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--filter='exclude .rsync-filter'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This filters out the .rsync-filter files themselves from the transfer. </p>
 </dd>
<dd> <p> See the FILTER RULES section for detailed information on how these options work. </p>
 </dd>
<dt><code>--exclude=PATTERN</code></dt>
<dd> <p> This option is a simplified form of the <code>--filter</code> option that specifies an exclude rule and does not allow the full rule-parsing syntax of normal filter rules. This is equivalent to specifying <code>-f&#8217;- PATTERN&#8217;</code>. </p>
 </dd>
<dd> <p> See the FILTER RULES section for detailed information on this option. </p>
 </dd>
<dt><code>--exclude-from=FILE</code></dt>
<dd> <p> This option is related to the <code>--exclude</code> option, but it specifies a FILE that contains exclude patterns (one per line). Blank lines in the file are ignored, as are whole-line comments that start with &#8216;<code>;</code>&#8216; or &#8216;<code>#</code>&#8216; (filename rules that contain those characters are unaffected). </p>
 </dd>
<dd> <p> If a line begins with &quot;<code>-&nbsp;</code>&quot; (dash, space) or &quot;<code>+&nbsp;</code>&quot; (plus, space), then the type of rule is being explicitly specified as an exclude or an include (respectively). Any rules without such a prefix are taken to be an exclude. </p>
 </dd>
<dd> <p> If a line consists of just &quot;<code>!</code>&quot;, then the current filter rules are cleared before adding any further rules. </p>
 </dd>
<dd> <p> If <i>FILE</i> is &#8216;<code>-</code>&#8216;, the list will be read from standard input. </p>
 </dd>
<dt><code>--include=PATTERN</code></dt>
<dd> <p> This option is a simplified form of the <code>--filter</code> option that specifies an include rule and does not allow the full rule-parsing syntax of normal filter rules. This is equivalent to specifying <code>-f&#8217;+&nbsp;PATTERN&#8217;</code>. </p>
 </dd>
<dd> <p> See the FILTER RULES section for detailed information on this option. </p>
 </dd>
<dt><code>--include-from=FILE</code></dt>
<dd> <p> This option is related to the <code>--include</code> option, but it specifies a FILE that contains include patterns (one per line). Blank lines in the file are ignored, as are whole-line comments that start with &#8216;<code>;</code>&#8216; or &#8216;<code>#</code>&#8216; (filename rules that contain those characters are unaffected). </p>
 </dd>
<dd> <p> If a line begins with &quot;<code>-&nbsp;</code>&quot; (dash, space) or &quot;<code>+&nbsp;</code>&quot; (plus, space), then the type of rule is being explicitly specified as an exclude or an include (respectively). Any rules without such a prefix are taken to be an include. </p>
 </dd>
<dd> <p> If a line consists of just &quot;<code>!</code>&quot;, then the current filter rules are cleared before adding any further rules. </p>
 </dd>
<dd> <p> If <i>FILE</i> is &#8216;<code>-</code>&#8216;, the list will be read from standard input. </p>
 </dd>
<dt><code>--files-from=FILE</code></dt>
<dd> <p> Using this option allows you to specify the exact list of files to transfer (as read from the specified FILE or &#8216;<code>-</code>&#8216; for standard input). It also tweaks the default behavior of rsync to make transferring just the specified files and directories easier: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> The <code>--relative</code> (<code>-R</code>) option is implied, which preserves the path information that is specified for each item in the file (use <code>--no-relative</code> or <code>--no-R</code> if you want to turn that off). </p>
 </dd>
<dt>o</dt>
<dd> <p> The <code>--dirs</code> (<code>-d</code>) option is implied, which will create directories specified in the list on the destination rather than noisily skipping them (use <code>--no-dirs</code> or <code>--no-d</code> if you want to turn that off). </p>
 </dd>
<dt>o</dt>
<dd> <p> The <code>--archive</code> (<code>-a</code>) option&#8217;s behavior does not imply <code>--recursive</code> (<code>-r</code>), so specify it explicitly, if you want it. </p>
 </dd>
<dt>o</dt>
<dd> <p> These side-effects change the default state of rsync, so the position of the <code>--files-from</code> option on the command-line has no bearing on how other options are parsed (e.g. <code>-a</code> works the same before or after <code>--files-from</code>, as does <code>--no-R</code> and all other options). </p>
 </dd></dl>
</dl>
<dd> <p> The filenames that are read from the FILE are all relative to the source dir -- any leading slashes are removed and no &quot;..&quot; references are allowed to go higher than the source dir. For example, take this command: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -a --files-from=/tmp/foo /usr remote:/backup
</code></pre>
 </dd></dl>
</dl>
<dd> <p> If /tmp/foo contains the string &quot;bin&quot; (or even &quot;/bin&quot;), the /usr/bin directory will be created as /backup/bin on the remote host. If it contains &quot;bin/&quot; (note the trailing slash), the immediate contents of the directory would also be sent (without needing to be explicitly mentioned in the file -- this began in version 2.6.4). In both cases, if the <code>-r</code> option was enabled, that dir&#8217;s entire hierarchy would also be transferred (keep in mind that <code>-r</code> needs to be specified explicitly with <code>--files-from</code>, since it is not implied by <code>-a</code>. Also note that the effect of the (enabled by default) <code>-r</code> option is to duplicate only the path info that is read from the file -- it does not force the duplication of the source-spec path (/usr in this case). </p>
 </dd>
<dd> <p> In addition, the <code>--files-from</code> file can be read from the remote host instead of the local host if you specify a &quot;host:&quot; in front of the file (the host must match one end of the transfer). As a short-cut, you can specify just a prefix of &quot;:&quot; to mean &quot;use the remote end of the transfer&quot;. For example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -a --files-from=:/path/file-list src:/ /tmp/copy
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This would copy all the files specified in the /path/file-list file that was located on the remote &quot;src&quot; host. </p>
 </dd>
<dd> <p> If the <code>--iconv</code> and <code>--secluded-args</code> options are specified and the <code>--files-from</code> filenames are being sent from one host to another, the filenames will be translated from the sending host&#8217;s charset to the receiving host&#8217;s charset. </p>
 </dd>
<dd> <p> NOTE: sorting the list of files in the <code>--files-from</code> input helps rsync to be more efficient, as it will avoid re-visiting the path elements that are shared between adjacent entries. If the input is not sorted, some path elements (implied directories) may end up being scanned multiple times, and rsync will eventually unduplicate them after they get turned into file-list elements. </p>
 </dd>
<dt><code>--from0</code>, <code>-0</code></dt>
<dd> <p> This tells rsync that the rules/filenames it reads from a file are terminated by a null (&#8216;\0&#8217;) character, not a NL, CR, or CR+LF. This affects <code>--exclude-from</code>, <code>--include-from</code>, <code>--files-from</code>, and any merged files specified in a <code>--filter</code> rule. It does not affect <code>--cvs-exclude</code> (since all names read from a .cvsignore file are split on whitespace). </p>
 </dd>
<dt><code>--old-args</code></dt>
<dd> <p> This option tells rsync to stop trying to protect the arg values on the remote side from unintended word-splitting or other misinterpretation. It also allows the client to treat an empty arg as a &quot;.&quot; instead of generating an error. </p>
 </dd>
<dd> <p> The default in a modern rsync is for &quot;shell-active&quot; characters (including spaces) to be backslash-escaped in the args that are sent to the remote shell. The wildcard characters <code>*</code>, <code>?</code>, <code>[</code>, &amp; <code>]</code> are not escaped in filename args (allowing them to expand into multiple filenames) while being protected in option args, such as <code>--usermap</code>. </p>
 </dd>
<dd> <p> If you have a script that wants to use old-style arg splitting in its filenames, specify this option once. If the remote shell has a problem with any backslash escapes at all, specify this option twice. </p>
 </dd>
<dd> <p> You may also control this setting via the <code>RSYNC_OLD_ARGS</code> environment variable. If it has the value &quot;1&quot;, rsync will default to a single-option setting. If it has the value &quot;2&quot; (or more), rsync will default to a repeated-option setting. If it is &quot;0&quot;, you&#8217;ll get the default escaping behavior. The environment is always overridden by manually specified positive or negative options (the negative is <code>--no-old-args</code>). </p>
 </dd>
<dd> <p> Note that this option also disables the extra safety check added in 3.2.5 that ensures that a remote sender isn&#8217;t including extra top-level items in the file-list that you didn&#8217;t request. This side-effect is necessary because we can&#8217;t know for sure what names to expect when the remote shell is interpreting the args. </p>
 </dd>
<dd> <p> This option conflicts with the <code>--secluded-args</code> option. </p>
 </dd>
<dt><code>--secluded-args</code>, <code>-s</code></dt>
<dd> <p> This option sends all filenames and most options to the remote rsync via the protocol (not the remote shell command line) which avoids letting the remote shell modify them. Wildcards are expanded on the remote host by rsync instead of a shell. </p>
 </dd>
<dd> <p> This is similar to the default backslash-escaping of args that was added in 3.2.4 (see <code>--old-args</code>) in that it prevents things like space splitting and unwanted special-character side-effects. However, it has the drawbacks of being incompatible with older rsync versions (prior to 3.0.0) and of being refused by restricted shells that want to be able to inspect all the option values for safety. </p>
 </dd>
<dd> <p> This option is useful for those times that you need the argument&#8217;s character set to be converted for the remote host, if the remote shell is incompatible with the default backslash-escpaing method, or there is some other reason that you want the majority of the options and arguments to bypass the command-line of the remote shell. </p>
 </dd>
<dd> <p> If you combine this option with <code>--iconv</code>, the args related to the remote side will be translated from the local to the remote character-set. The translation happens before wild-cards are expanded. See also the <code>--files-from</code> option. </p>
 </dd>
<dd> <p> You may also control this setting via the <code>RSYNC_PROTECT_ARGS</code> environment variable. If it has a non-zero value, this setting will be enabled by default, otherwise it will be disabled by default. Either state is overridden by a manually specified positive or negative version of this option (note that <code>--no-s</code> and <code>--no-secluded-args</code> are the negative versions). This environment variable is also superseded by a non-zero <code>RSYNC_OLD_ARGS</code> export. </p>
 </dd>
<dd> <p> This option conflicts with the <code>--old-args</code> option. </p>
 </dd>
<dd> <p> This option used to be called <code>--protect-args</code> (before 3.2.6) and that older name can still be used (though specifying it as <code>-s</code> is always the easiest and most compatible choice). </p>
 </dd>
<dt><code>--trust-sender</code></dt>
<dd> <p> This option disables two extra validation checks that a local client performs on the file list generated by a remote sender. This option should only be used if you trust the sender to not put something malicious in the file list (something that could possibly be done via a modified rsync, a modified shell, or some other similar manipulation). </p>
 </dd>
<dd> <p> Normally, the rsync client (as of version 3.2.5) runs two extra validation checks when pulling files from a remote rsync: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> It verifies that additional arg items didn&#8217;t get added at the top of the transfer. </p>
 </dd>
<dt>o</dt>
<dd> <p> It verifies that none of the items in the file list are names that should have been excluded (if filter rules were specified). </p>
 </dd></dl>
</dl>
<dd> <p> Note that various options can turn off one or both of these checks if the option interferes with the validation. For instance: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> Using a per-directory filter file reads filter rules that only the server knows about, so the filter checking is disabled. </p>
 </dd>
<dt>o</dt>
<dd> <p> Using the <code>--old-args</code> option allows the sender to manipulate the requested args, so the arg checking is disabled. </p>
 </dd>
<dt>o</dt>
<dd> <p> Reading the files-from list from the server side means that the client doesn&#8217;t know the arg list, so the arg checking is disabled. </p>
 </dd>
<dt>o</dt>
<dd> <p> Using <code>--read-batch</code> disables both checks since the batch file&#8217;s contents will have been verified when it was created. </p>
 </dd></dl>
</dl>
<dd> <p> This option may help an under-powered client server if the extra pattern matching is slowing things down on a huge transfer. It can also be used to work around a currently-unknown bug in the verification logic for a transfer from a trusted sender. </p>
 </dd>
<dd> <p> When using this option it is a good idea to specify a dedicated destination directory, as discussed in the MULTI-HOST SECURITY section. </p>
 </dd>
<dt><code>--copy-as=USER[:GROUP]</code></dt>
<dd> <p> This option instructs rsync to use the USER and (if specified after a colon) the GROUP for the copy operations. This only works if the user that is running rsync has the ability to change users. If the group is not specified then the user&#8217;s default groups are used. </p>
 </dd>
<dd> <p> This option can help to reduce the risk of an rsync being run as root into or out of a directory that might have live changes happening to it and you want to make sure that root-level read or write actions of system files are not possible. While you could alternatively run all of rsync as the specified user, sometimes you need the root-level host-access credentials to be used, so this allows rsync to drop root for the copying part of the operation after the remote-shell or daemon connection is established. </p>
 </dd>
<dd> <p> The option only affects one side of the transfer unless the transfer is local, in which case it affects both sides. Use the <code>--remote-option</code> to affect the remote side, such as <code>-M--copy-as=joe</code>. For a local transfer, the lsh (or lsh.sh) support file provides a local-shell helper script that can be used to allow a &quot;localhost:&quot; or &quot;lh:&quot; host-spec to be specified without needing to setup any remote shells, allowing you to specify remote options that affect the side of the transfer that is using the host-spec (and using hostname &quot;lh&quot; avoids the overriding of the remote directory to the user&#8217;s home dir). </p>
 </dd>
<dd> <p> For example, the following rsync writes the local files as user &quot;joe&quot;: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>sudo rsync -aiv --copy-as=joe host1:backups/joe/ /home/joe/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This makes all files owned by user &quot;joe&quot;, limits the groups to those that are available to that user, and makes it impossible for the joe user to do a timed exploit of the path to induce a change to a file that the joe user has no permissions to change. </p>
 </dd>
<dd> <p> The following command does a local copy into the &quot;dest/&quot; dir as user &quot;joe&quot; (assuming you&#8217;ve installed support/lsh into a dir on your $PATH): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>sudo rsync -aive lsh -M--copy-as=joe src/ lh:dest/
</code></pre>
 </dd></dl>
</dl>
<dt><code>--temp-dir=DIR</code>, <code>-T</code></dt>
<dd> <p> This option instructs rsync to use DIR as a scratch directory when creating temporary copies of the files transferred on the receiving side. The default behavior is to create each temporary file in the same directory as the associated destination file. Beginning with rsync 3.1.1, the temp-file names inside the specified DIR will not be prefixed with an extra dot (though they will still have a random suffix added). </p>
 </dd>
<dd> <p> This option is most often used when the receiving disk partition does not have enough free space to hold a copy of the largest file in the transfer. In this case (i.e. when the scratch directory is on a different disk partition), rsync will not be able to rename each received temporary file over the top of the associated destination file, but instead must copy it into place. Rsync does this by copying the file over the top of the destination file, which means that the destination file will contain truncated data during this copy. If this were not done this way (even if the destination file were first removed, the data locally copied to a temporary file in the destination directory, and then renamed into place) it would be possible for the old file to continue taking up disk space (if someone had it open), and thus there might not be enough room to fit the new version on the disk at the same time. </p>
 </dd>
<dd> <p> If you are using this option for reasons other than a shortage of disk space, you may wish to combine it with the <code>--delay-updates</code> option, which will ensure that all copied files get put into subdirectories in the destination hierarchy, awaiting the end of the transfer. If you don&#8217;t have enough room to duplicate all the arriving files on the destination partition, another way to tell rsync that you aren&#8217;t overly concerned about disk space is to use the <code>--partial-dir</code> option with a relative path; because this tells rsync that it is OK to stash off a copy of a single file in a subdir in the destination hierarchy, rsync will use the partial-dir as a staging area to bring over the copied file, and then rename it into place from there. (Specifying a <code>--partial-dir</code> with an absolute path does not have this side-effect.) </p>
 </dd>
<dt><code>--fuzzy</code>, <code>-y</code></dt>
<dd> <p> This option tells rsync that it should look for a basis file for any destination file that is missing. The current algorithm looks in the same directory as the destination file for either a file that has an identical size and modified-time, or a similarly-named file. If found, rsync uses the fuzzy basis file to try to speed up the transfer. </p>
 </dd>
<dd> <p> If the option is repeated, the fuzzy scan will also be done in any matching alternate destination directories that are specified via <code>--compare-dest</code>, <code>--copy-dest</code>, or <code>--link-dest</code>. </p>
 </dd>
<dd> <p> Note that the use of the <code>--delete</code> option might get rid of any potential fuzzy-match files, so either use <code>--delete-after</code> or specify some filename exclusions if you need to prevent this. </p>
 </dd>
<dt><code>--compare-dest=DIR</code></dt>
<dd> <p> This option instructs rsync to use <i>DIR</i> on the destination machine as an additional hierarchy to compare destination files against doing transfers (if the files are missing in the destination directory). If a file is found in <i>DIR</i> that is identical to the sender&#8217;s file, the file will NOT be transferred to the destination directory. This is useful for creating a sparse backup of just files that have changed from an earlier backup. This option is typically used to copy into an empty (or newly created) directory. </p>
 </dd>
<dd> <p> Beginning in version 2.6.4, multiple <code>--compare-dest</code> directories may be provided, which will cause rsync to search the list in the order specified for an exact match. If a match is found that differs only in attributes, a local copy is made and the attributes updated. If a match is not found, a basis file from one of the <i>DIRs</i> will be selected to try to speed up the transfer. </p>
 </dd>
<dd> <p> If <i>DIR</i> is a relative path, it is relative to the destination directory. See also <code>--copy-dest</code> and <code>--link-dest</code>. </p>
 </dd>
<dd> <p> NOTE: beginning with version 3.1.0, rsync will remove a file from a non-empty destination hierarchy if an exact match is found in one of the compare-dest hierarchies (making the end result more closely match a fresh copy). </p>
 </dd>
<dt><code>--copy-dest=DIR</code></dt>
<dd> <p> This option behaves like <code>--compare-dest</code>, but rsync will also copy unchanged files found in <i>DIR</i> to the destination directory using a local copy. This is useful for doing transfers to a new destination while leaving existing files intact, and then doing a flash-cutover when all files have been successfully transferred. </p>
 </dd>
<dd> <p> Multiple <code>--copy-dest</code> directories may be provided, which will cause rsync to search the list in the order specified for an unchanged file. If a match is not found, a basis file from one of the <i>DIRs</i> will be selected to try to speed up the transfer. </p>
 </dd>
<dd> <p> If <i>DIR</i> is a relative path, it is relative to the destination directory. See also <code>--compare-dest</code> and <code>--link-dest</code>. </p>
 </dd>
<dt><code>--link-dest=DIR</code></dt>
<dd> <p> This option behaves like <code>--copy-dest</code>, but unchanged files are hard linked from <i>DIR</i> to the destination directory. The files must be identical in all preserved attributes (e.g. permissions, possibly ownership) in order for the files to be linked together. An example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av --link-dest=$PWD/prior_dir host:src_dir/ new_dir/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> If files aren&#8217;t linking, double-check their attributes. Also check if some attributes are getting forced outside of rsync&#8217;s control, such a mount option that squishes root to a single user, or mounts a removable drive with generic ownership (such as OS X&#8217;s &quot;Ignore ownership on this volume&quot; option). </p>
 </dd>
<dd> <p> Beginning in version 2.6.4, multiple <code>--link-dest</code> directories may be provided, which will cause rsync to search the list in the order specified for an exact match (there is a limit of 20 such directories). If a match is found that differs only in attributes, a local copy is made and the attributes updated. If a match is not found, a basis file from one of the <i>DIRs</i> will be selected to try to speed up the transfer. </p>
 </dd>
<dd> <p> This option works best when copying into an empty destination hierarchy, as existing files may get their attributes tweaked, and that can affect alternate destination files via hard-links. Also, itemizing of changes can get a bit muddled. Note that prior to version 3.1.0, an alternate-directory exact match would never be found (nor linked into the destination) when a destination file already exists. </p>
 </dd>
<dd> <p> Note that if you combine this option with <code>--ignore-times</code>, rsync will not link any files together because it only links identical files together as a substitute for transferring the file, never as an additional check after the file is updated. </p>
 </dd>
<dd> <p> If <i>DIR</i> is a relative path, it is relative to the destination directory. See also <code>--compare-dest</code> and <code>--copy-dest</code>. </p>
 </dd>
<dd> <p> Note that rsync versions prior to 2.6.1 had a bug that could prevent <code>--link-dest</code> from working properly for a non-super-user when <code>--owner</code> (<code>-o</code>) was specified (or implied). You can work-around this bug by avoiding the <code>-o</code> option (or using <code>--no-o</code>) when sending to an old rsync. </p>
 </dd>
<dt><code>--compress</code>, <code>-z</code></dt>
<dd> <p> With this option, rsync compresses the file data as it is sent to the destination machine, which reduces the amount of data being transmitted -- something that is useful over a slow connection. </p>
 </dd>
<dd> <p> Rsync supports multiple compression methods and will choose one for you unless you force the choice using the <code>--compress-choice</code> (<code>--zc</code>) option. </p>
 </dd>
<dd> <p> Run <code>rsync --version</code> to see the default compress list compiled into your version. </p>
 </dd>
<dd> <p> When both sides of the transfer are at least 3.2.0, rsync chooses the first algorithm in the client&#8217;s list of choices that is also in the server&#8217;s list of choices. If no common compress choice is found, rsync exits with an error. If the remote rsync is too old to support checksum negotiation, its list is assumed to be &quot;zlib&quot;. </p>
 </dd>
<dd> <p> The default order can be customized by setting the environment variable <code>RSYNC_COMPRESS_LIST</code> to a space-separated list of acceptable compression names. If the string contains a &quot;<code>&amp;</code>&quot; character, it is separated into the &quot;client string &amp; server string&quot;, otherwise the same string applies to both. If the string (or string portion) contains no non-whitespace characters, the default compress list is used. Any unknown compression names are discarded from the list, but a list with only invalid names results in a failed negotiation. </p>
 </dd>
<dd> <p> There are some older rsync versions that were configured to reject a <code>-z</code> option and require the use of <code>-zz</code> because their compression library was not compatible with the default zlib compression method. You can usually ignore this weirdness unless the rsync server complains and tells you to specify <code>-zz</code>. </p>
 </dd>
<dt><code>--compress-choice=STR</code>, <code>--zc=STR</code></dt>
<dd> <p> This option can be used to override the automatic negotiation of the compression algorithm that occurs when <code>--compress</code> is used. The option implies <code>--compress</code> unless &quot;none&quot; was specified, which instead implies <code>--no-compress</code>. </p>
 </dd>
<dd> <p> The compression options that you may be able to use are: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <code>zstd</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>lz4</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>zlibx</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>zlib</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>none</code> </p>
 </dd></dl>
</dl>
<dd> <p> Run <code>rsync --version</code> to see the default compress list compiled into your version (which may differ from the list above). </p>
 </dd>
<dd> <p> Note that if you see an error about an option named <code>--old-compress</code> or <code>--new-compress</code>, this is rsync trying to send the <code>--compress-choice=zlib</code> or <code>--compress-choice=zlibx</code> option in a backward-compatible manner that more rsync versions understand. This error indicates that the older rsync version on the server will not allow you to force the compression type. </p>
 </dd>
<dd> <p> Note that the &quot;zlibx&quot; compression algorithm is just the &quot;zlib&quot; algorithm with matched data excluded from the compression stream (to try to make it more compatible with an external zlib implementation). </p>
 </dd>
<dt><code>--compress-level=NUM</code>, <code>--zl=NUM</code></dt>
<dd> <p> Explicitly set the compression level to use (see <code>--compress</code>, <code>-z</code>) instead of letting it default. The <code>--compress</code> option is implied as long as the level chosen is not a &quot;don&#8217;t compress&quot; level for the compression algorithm that is in effect (e.g. zlib compression treats level 0 as &quot;off&quot;). </p>
 </dd>
<dd> <p> The level values vary depending on the checksum in effect. Because rsync will negotiate a checksum choice by default (when the remote rsync is new enough), it can be good to combine this option with a <code>--compress-choice</code> (<code>--zc</code>) option unless you&#8217;re sure of the choice in effect. For example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -aiv --zc=zstd --zl=22 host:src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> For zlib &amp; zlibx compression the valid values are from 1 to 9 with 6 being the default. Specifying <code>--zl=0</code> turns compression off, and specifying <code>--zl=-1</code> chooses the default level of 6. </p>
 </dd>
<dd> <p> For zstd compression the valid values are from -131072 to 22 with 3 being the default. Specifying 0 chooses the default of 3. </p>
 </dd>
<dd> <p> For lz4 compression there are no levels, so the value is always 0. </p>
 </dd>
<dd> <p> If you specify a too-large or too-small value, the number is silently limited to a valid value. This allows you to specify something like <code>--zl=999999999</code> and be assured that you&#8217;ll end up with the maximum compression level no matter what algorithm was chosen. </p>
 </dd>
<dd> <p> If you want to know the compression level that is in effect, specify <code>--debug=nstr</code> to see the &quot;negotiated string&quot; results. This will report something like &quot;<code>Client compress: zstd&nbsp;(level 3)</code>&quot; (along with the checksum choice in effect). </p>
 </dd>
<dt><code>--skip-compress=LIST</code></dt>
<dd> <p> <code>NOTE:</code> no compression method currently supports per-file compression changes, so this option has no effect. </p>
 </dd>
<dd> <p> Override the list of file suffixes that will be compressed as little as possible. Rsync sets the compression level on a per-file basis based on the file&#8217;s suffix. If the compression algorithm has an &quot;off&quot; level, then no compression occurs for those files. Other algorithms that support changing the streaming level on-the-fly will have the level minimized to reduces the CPU usage as much as possible for a matching file. </p>
 </dd>
<dd> <p> The <code>LIST</code> should be one or more file suffixes (without the dot) separated by slashes (<code>/</code>). You may specify an empty string to indicate that no files should be skipped. </p>
 </dd>
<dd> <p> Simple character-class matching is supported: each must consist of a list of letters inside the square brackets (e.g. no special classes, such as &quot;[:alpha:]&quot;, are supported, and &#8216;-&#8216; has no special meaning). </p>
 </dd>
<dd> <p> The characters asterisk (<code>*</code>) and question-mark (<code>?</code>) have no special meaning. </p>
 </dd>
<dd> <p> Here&#8217;s an example that specifies 6 suffixes to skip (since 1 of the 5 rules matches 2 suffixes): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--skip-compress=gz/jpg/mp[34]/7z/bz2
</code></pre>
 </dd></dl>
</dl>
<dd> <p> The default file suffixes in the skip-compress list in this version of rsync are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> 3g2 3gp 7z aac ace apk avi bz2 deb dmg ear f4v flac flv gpg gz iso jar jpeg jpg lrz lz lz4 lzma lzo m1a m1v m2a m2ts m2v m4a m4b m4p m4r m4v mka mkv mov mp1 mp2 mp3 mp4 mpa mpeg mpg mpv mts odb odf odg odi odm odp ods odt oga ogg ogm ogv ogx opus otg oth otp ots ott oxt png qt rar rpm rz rzip spx squashfs sxc sxd sxg sxm sxw sz tbz tbz2 tgz tlz ts txz tzo vob war webm webp xz z zip zst </p>
 </dd></dl>
</dl>
<dd> <p> This list will be replaced by your <code>--skip-compress</code> list in all but one situation: a copy from a daemon rsync will add your skipped suffixes to its list of non-compressing files (and its list may be configured to a different default). </p>
 </dd>
<dt><code>--numeric-ids</code></dt>
<dd> <p> With this option rsync will transfer numeric group and user IDs rather than using user and group names and mapping them at both ends. </p>
 </dd>
<dd> <p> By default rsync will use the username and groupname to determine what ownership to give files. The special uid 0 and the special group 0 are never mapped via user/group names even if the <code>--numeric-ids</code> option is not specified. </p>
 </dd>
<dd> <p> If a user or group has no name on the source system or it has no match on the destination system, then the numeric ID from the source system is used instead. See also the <code>use chroot</code> setting in the rsyncd.conf manpage for some comments on how the chroot setting affects rsync&#8217;s ability to look up the names of the users and groups and what you can do about it. </p>
 </dd>
<dt><code>--usermap=STRING</code>, <code>--groupmap=STRING</code></dt>
<dd> <p> These options allow you to specify users and groups that should be mapped to other values by the receiving side. The <code>STRING</code> is one or more <code>FROM</code>:<code>TO</code> pairs of values separated by commas. Any matching <code>FROM</code> value from the sender is replaced with a <code>TO</code> value from the receiver. You may specify usernames or user IDs for the <code>FROM</code> and <code>TO</code> values, and the <code>FROM</code> value may also be a wild-card string, which will be matched against the sender&#8217;s names (wild-cards do NOT match against ID numbers, though see below for why a &#8216;<code>*</code>&#8216; matches everything). You may instead specify a range of ID numbers via an inclusive range: LOW-HIGH. For example: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--usermap=0-99:nobody,wayne:admin,*:normal --groupmap=usr:1,1:usr
</code></pre>
 </dd></dl>
</dl>
<dd> <p> The first match in the list is the one that is used. You should specify all your user mappings using a single <code>--usermap</code> option, and/or all your group mappings using a single <code>--groupmap</code> option. </p>
 </dd>
<dd> <p> Note that the sender&#8217;s name for the 0 user and group are not transmitted to the receiver, so you should either match these values using a 0, or use the names in effect on the receiving side (typically &quot;root&quot;). All other <code>FROM</code> names match those in use on the sending side. All <code>TO</code> names match those in use on the receiving side. </p>
 </dd>
<dd> <p> Any IDs that do not have a name on the sending side are treated as having an empty name for the purpose of matching. This allows them to be matched via a &quot;<code>*</code>&quot; or using an empty name. For instance: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--usermap=:nobody --groupmap=*:nobody
</code></pre>
 </dd></dl>
</dl>
<dd> <p> When the <code>--numeric-ids</code> option is used, the sender does not send any names, so all the IDs are treated as having an empty name. This means that you will need to specify numeric <code>FROM</code> values if you want to map these nameless IDs to different values. </p>
 </dd>
<dd> <p> For the <code>--usermap</code> option to work, the receiver will need to be running as a super-user (see also the <code>--super</code> and <code>--fake-super</code> options). For the <code>--groupmap</code> option to work, the receiver will need to have permissions to set that group. </p>
 </dd>
<dd> <p> Starting with rsync 3.2.4, the <code>--usermap</code> option implies the <code>--owner</code> (<code>-o</code>) option while the <code>--groupmap</code> option implies the <code>--group</code> (<code>-g</code>) option (since rsync needs to have those options enabled for the mapping options to work). </p>
 </dd>
<dd> <p> An older rsync client may need to use <code>-s</code> to avoid a complaint about wildcard characters, but a modern rsync handles this automatically. </p>
 </dd>
<dt><code>--chown=USER:GROUP</code></dt>
<dd> <p> This option forces all files to be owned by USER with group GROUP. This is a simpler interface than using <code>--usermap</code> &amp; <code>--groupmap</code> directly, but it is implemented using those options internally so they cannot be mixed. If either the USER or GROUP is empty, no mapping for the omitted user/group will occur. If GROUP is empty, the trailing colon may be omitted, but if USER is empty, a leading colon must be supplied. </p>
 </dd>
<dd> <p> If you specify &quot;<code>--chown=foo:bar</code>&quot;, this is exactly the same as specifying &quot;<code>--usermap=*:foo --groupmap=*:bar</code>&quot;, only easier (and with the same implied <code>--owner</code> and/or <code>--group</code> options). </p>
 </dd>
<dd> <p> An older rsync client may need to use <code>-s</code> to avoid a complaint about wildcard characters, but a modern rsync handles this automatically. </p>
 </dd>
<dt><code>--timeout=SECONDS</code></dt>
<dd> <p> This option allows you to set a maximum I/O timeout in seconds. If no data is transferred for the specified time then rsync will exit. The default is 0, which means no timeout. </p>
 </dd>
<dt><code>--contimeout=SECONDS</code></dt>
<dd> <p> This option allows you to set the amount of time that rsync will wait for its connection to an rsync daemon to succeed. If the timeout is reached, rsync exits with an error. </p>
 </dd>
<dt><code>--address=ADDRESS</code></dt>
<dd> <p> By default rsync will bind to the wildcard address when connecting to an rsync daemon. The <code>--address</code> option allows you to specify a specific IP address (or hostname) to bind to. </p>
 </dd>
<dd> <p> See also the daemon version of the <code>--address</code> option. </p>
 </dd>
<dt><code>--port=PORT</code></dt>
<dd> <p> This specifies an alternate TCP port number to use rather than the default of 873. This is only needed if you are using the double-colon (::) syntax to connect with an rsync daemon (since the URL syntax has a way to specify the port as a part of the URL). </p>
 </dd>
<dd> <p> See also the daemon version of the <code>--port</code> option. </p>
 </dd>
<dt><code>--sockopts=OPTIONS</code></dt>
<dd> <p> This option can provide endless fun for people who like to tune their systems to the utmost degree. You can set all sorts of socket options which may make transfers faster (or slower!). Read the manpage for the <code>setsockopt()</code> system call for details on some of the options you may be able to set. By default no special socket options are set. This only affects direct socket connections to a remote rsync daemon. </p>
 </dd>
<dd> <p> See also the daemon version of the <code>--sockopts</code> option. </p>
 </dd>
<dt><code>--blocking-io</code></dt>
<dd> <p> This tells rsync to use blocking I/O when launching a remote shell transport. If the remote shell is either rsh or remsh, rsync defaults to using blocking I/O, otherwise it defaults to using non-blocking I/O. (Note that ssh prefers non-blocking I/O.) </p>
 </dd>
<dt><code>--outbuf=MODE</code></dt>
<dd> <p> This sets the output buffering mode. The mode can be None (aka Unbuffered), Line, or Block (aka Full). You may specify as little as a single letter for the mode, and use upper or lower case. </p>
 </dd>
<dd> <p> The main use of this option is to change Full buffering to Line buffering when rsync&#8217;s output is going to a file or pipe. </p>
 </dd>
<dt><code>--itemize-changes</code>, <code>-i</code></dt>
<dd> <p> Requests a simple itemized list of the changes that are being made to each file, including attribute changes. This is exactly the same as specifying <code>--out-format=&#8216;%i&nbsp;%n%L&#8217;</code>. If you repeat the option, unchanged files will also be output, but only if the receiving rsync is at least version 2.6.7 (you can use <code>-vv</code> with older versions of rsync, but that also turns on the output of other verbose messages). </p>
 </dd>
<dd> <p> The &quot;%i&quot; escape has a cryptic output that is 11 letters long. The general format is like the string <code>YXcstpoguax</code>, where <code>Y</code> is replaced by the type of update being done, <code>X</code> is replaced by the file-type, and the other letters represent attributes that may be output if they are being modified. </p>
 </dd>
<dd> <p> The update types that replace the <code>Y</code> are as follows: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> A <code>&lt;</code> means that a file is being transferred to the remote host (sent). </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>&gt;</code> means that a file is being transferred to the local host (received). </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>c</code> means that a local change/creation is occurring for the item (such as the creation of a directory or the changing of a symlink, etc.). </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>h</code> means that the item is a hard link to another item (requires <code>--hard-links</code>). </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>.</code> means that the item is not being updated (though it might have attributes that are being modified). </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>*</code> means that the rest of the itemized-output area contains a message (e.g. &quot;deleting&quot;). </p>
 </dd></dl>
</dl>
<dd> <p> The file-types that replace the <code>X</code> are: <code>f</code> for a file, a <code>d</code> for a directory, an <code>L</code> for a symlink, a <code>D</code> for a device, and a <code>S</code> for a special file (e.g. named sockets and fifos). </p>
 </dd>
<dd> <p> The other letters in the string indicate if some attributes of the file have changed, as follows: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> &quot;<code>.</code>&quot; - the attribute is unchanged. </p>
 </dd>
<dt>o</dt>
<dd> <p> &quot;<code>+</code>&quot; - the file is newly created. </p>
 </dd>
<dt>o</dt>
<dd> <p> &quot;<code>&nbsp;</code>&quot; - all the attributes are unchanged (all dots turn to spaces). </p>
 </dd>
<dt>o</dt>
<dd> <p> &quot;<code>?</code>&quot; - the change is unknown (when the remote rsync is old). </p>
 </dd>
<dt>o</dt>
<dd> <p> A letter indicates an attribute is being updated. </p>
 </dd></dl>
</dl>
<dd> <p> The attribute that is associated with each letter is as follows: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> A <code>c</code> means either that a regular file has a different checksum (requires <code>--checksum</code>) or that a symlink, device, or special file has a changed value. Note that if you are sending files to an rsync prior to 3.0.1, this change flag will be present only for checksum-differing regular files. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>s</code> means the size of a regular file is different and will be updated by the file transfer. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>t</code> means the modification time is different and is being updated to the sender&#8217;s value (requires <code>--times</code>). An alternate value of <code>T</code> means that the modification time will be set to the transfer time, which happens when a file/symlink/device is updated without <code>--times</code> and when a symlink is changed and the receiver can&#8217;t set its time. (Note: when using an rsync 3.0.0 client, you might see the <code>s</code> flag combined with <code>t</code> instead of the proper <code>T</code> flag for this time-setting failure.) </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>p</code> means the permissions are different and are being updated to the sender&#8217;s value (requires <code>--perms</code>). </p>
 </dd>
<dt>o</dt>
<dd> <p> An <code>o</code> means the owner is different and is being updated to the sender&#8217;s value (requires <code>--owner</code> and super-user privileges). </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>g</code> means the group is different and is being updated to the sender&#8217;s value (requires <code>--group</code> and the authority to set the group). </p>
 </dd>
<dt>o</dt>
<dd>  </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> A <code>u</code>|<code>n</code>|<code>b</code> indicates the following information: </p>
<p> <code>u</code> means the access (use) time is different and is being updated to the sender&#8217;s value (requires <code>--atimes</code>) </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>n</code> means the create time (newness) is different and is being updated to the sender&#8217;s value (requires <code>--crtimes</code>) </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>b</code> means that both the access and create times are being updated </p>
 </dd></dl>
</dl>
<dt>o</dt>
<dd> <p> The <code>a</code> means that the ACL information is being changed. </p>
 </dd>
<dt>o</dt>
<dd> <p> The <code>x</code> means that the extended attribute information is being changed. </p>
 </dd></dl>
</dl>
<dd> <p> One other output is possible: when deleting files, the &quot;%i&quot; will output the string &quot;<code>*deleting</code>&quot; for each item that is being removed (assuming that you are talking to a recent enough rsync that it logs deletions instead of outputting them as a verbose message). </p>
 </dd>
<dt><code>--out-format=FORMAT</code></dt>
<dd> <p> This allows you to specify exactly what the rsync client outputs to the user on a per-update basis. The format is a text string containing embedded single-character escape sequences prefixed with a percent (%) character. A default format of &quot;%n%L&quot; is assumed if either <code>--info=name</code> or <code>-v</code> is specified (this tells you just the name of the file and, if the item is a link, where it points). For a full list of the possible escape characters, see the <code>log format</code> setting in the rsyncd.conf manpage. </p>
 </dd>
<dd> <p> Specifying the <code>--out-format</code> option implies the <code>--info=name</code> option, which will mention each file, dir, etc. that gets updated in a significant way (a transferred file, a recreated symlink/device, or a touched directory). In addition, if the itemize-changes escape (%i) is included in the string (e.g. if the <code>--itemize-changes</code> option was used), the logging of names increases to mention any item that is changed in any way (as long as the receiving side is at least 2.6.4). See the <code>--itemize-changes</code> option for a description of the output of &quot;%i&quot;. </p>
 </dd>
<dd> <p> Rsync will output the out-format string prior to a file&#8217;s transfer unless one of the transfer-statistic escapes is requested, in which case the logging is done at the end of the file&#8217;s transfer. When this late logging is in effect and <code>--progress</code> is also specified, rsync will also output the name of the file being transferred prior to its progress information (followed, of course, by the out-format output). </p>
 </dd>
<dt><code>--log-file=FILE</code></dt>
<dd> <p> This option causes rsync to log what it is doing to a file. This is similar to the logging that a daemon does, but can be requested for the client side and/or the server side of a non-daemon transfer. If specified as a client option, transfer logging will be enabled with a default format of &quot;%i %n%L&quot;. See the <code>--log-file-format</code> option if you wish to override this. </p>
 </dd>
<dd> <p> Here&#8217;s an example command that requests the remote side to log what is happening: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av --remote-option=--log-file=/tmp/rlog src/ dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This is very useful if you need to debug why a connection is closing unexpectedly. </p>
 </dd>
<dd> <p> See also the daemon version of the <code>--log-file</code> option. </p>
 </dd>
<dt><code>--log-file-format=FORMAT</code></dt>
<dd> <p> This allows you to specify exactly what per-update logging is put into the file specified by the <code>--log-file</code> option (which must also be specified for this option to have any effect). If you specify an empty string, updated files will not be mentioned in the log file. For a list of the possible escape characters, see the <code>log format</code> setting in the rsyncd.conf manpage. </p>
 </dd>
<dd> <p> The default FORMAT used if <code>--log-file</code> is specified and this option is not is &#8216;%i %n%L&#8217;. </p>
 </dd>
<dd> <p> See also the daemon version of the <code>--log-file-format</code> option. </p>
 </dd>
<dt><code>--stats</code></dt>
<dd> <p> This tells rsync to print a verbose set of statistics on the file transfer, allowing you to tell how effective rsync&#8217;s delta-transfer algorithm is for your data. This option is equivalent to <code>--info=stats2</code> if combined with 0 or 1 <code>-v</code> options, or <code>--info=stats3</code> if combined with 2 or more <code>-v</code> options. </p>
 </dd>
<dd> <p> The current statistics are as follows: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <code>Number of files</code> is the count of all &quot;files&quot; (in the generic sense), which includes directories, symlinks, etc. The total count will be followed by a list of counts by filetype (if the total is non-zero). For example: &quot;(reg: 5, dir: 3, link: 2, dev: 1, special: 1)&quot; lists the totals for regular files, directories, symlinks, devices, and special files. If any of value is 0, it is completely omitted from the list. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Number of created files</code> is the count of how many &quot;files&quot; (generic sense) were created (as opposed to updated). The total count will be followed by a list of counts by filetype (if the total is non-zero). </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Number of deleted files</code> is the count of how many &quot;files&quot; (generic sense) were deleted. The total count will be followed by a list of counts by filetype (if the total is non-zero). Note that this line is only output if deletions are in effect, and only if protocol 31 is being used (the default for rsync 3.1.x). </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Number of regular files transferred</code> is the count of normal files that were updated via rsync&#8217;s delta-transfer algorithm, which does not include dirs, symlinks, etc. Note that rsync 3.1.0 added the word &quot;regular&quot; into this heading. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Total file size</code> is the total sum of all file sizes in the transfer. This does not count any size for directories or special files, but does include the size of symlinks. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Total transferred file size</code> is the total sum of all files sizes for just the transferred files. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Literal data</code> is how much unmatched file-update data we had to send to the receiver for it to recreate the updated files. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Matched data</code> is how much data the receiver got locally when recreating the updated files. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>File list size</code> is how big the file-list data was when the sender sent it to the receiver. This is smaller than the in-memory size for the file list due to some compressing of duplicated data when rsync sends the list. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>File list generation time</code> is the number of seconds that the sender spent creating the file list. This requires a modern rsync on the sending side for this to be present. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>File list transfer time</code> is the number of seconds that the sender spent sending the file list to the receiver. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Total bytes sent</code> is the count of all the bytes that rsync sent from the client side to the server side. </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>Total bytes received</code> is the count of all non-message bytes that rsync received by the client side from the server side. &quot;Non-message&quot; bytes means that we don&#8217;t count the bytes for a verbose message that the server sent to us, which makes the stats more consistent. </p>
 </dd></dl>
</dl>
<dt><code>--8-bit-output</code>, <code>-8</code></dt>
<dd> <p> This tells rsync to leave all high-bit characters unescaped in the output instead of trying to test them to see if they&#8217;re valid in the current locale and escaping the invalid ones. All control characters (but never tabs) are always escaped, regardless of this option&#8217;s setting. </p>
 </dd>
<dd> <p> The escape idiom that started in 2.6.7 is to output a literal backslash (<code>\</code>) and a hash (<code>#</code>), followed by exactly 3 octal digits. For example, a newline would output as &quot;<code>\#012</code>&quot;. A literal backslash that is in a filename is not escaped unless it is followed by a hash and 3 digits (0-9). </p>
 </dd>
<dt><code>--human-readable</code>, <code>-h</code></dt>
<dd> <p> Output numbers in a more human-readable format. There are 3 possible levels: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd>
<dt>1.</dt>
<dd> <p> output numbers with a separator between each set of 3 digits (either a comma or a period, depending on if the decimal point is represented by a period or a comma). </p>
 </dd>
<dt>2.</dt>
<dd> <p> output numbers in units of 1000 (with a character suffix for larger units -- see below). </p>
 </dd>
<dt>3.</dt>
<dd> <p> output numbers in units of 1024. </p>
 </dd></dl>
</dl>
<dd> <p> The default is human-readable level 1. Each <code>-h</code> option increases the level by one. You can take the level down to 0 (to output numbers as pure digits) by specifying the <code>--no-human-readable</code> (<code>--no-h</code>) option. </p>
 </dd>
<dd> <p> The unit letters that are appended in levels 2 and 3 are: <code>K</code> (kilo), <code>M</code> (mega), <code>G</code> (giga), <code>T</code> (tera), or <code>P</code> (peta). For example, a 1234567-byte file would output as 1.23M in level-2 (assuming that a period is your local decimal point). </p>
 </dd>
<dd> <p> Backward compatibility note: versions of rsync prior to 3.1.0 do not support human-readable level 1, and they default to level 0. Thus, specifying one or two <code>-h</code> options will behave in a comparable manner in old and new versions as long as you didn&#8217;t specify a <code>--no-h</code> option prior to one or more <code>-h</code> options. See the <code>--list-only</code> option for one difference. </p>
 </dd>
<dt><code>--partial</code></dt>
<dd> <p> By default, rsync will delete any partially transferred file if the transfer is interrupted. In some circumstances it is more desirable to keep partially transferred files. Using the <code>--partial</code> option tells rsync to keep the partial file which should make a subsequent transfer of the rest of the file much faster. </p>
 </dd>
<dt><code>--partial-dir=DIR</code></dt>
<dd> <p> This option modifies the behavior of the <code>--partial</code> option while also implying that it be enabled. This enhanced partial-file method puts any partially transferred files into the specified <i>DIR</i> instead of writing the partial file out to the destination file. On the next transfer, rsync will use a file found in this dir as data to speed up the resumption of the transfer and then delete it after it has served its purpose. </p>
 </dd>
<dd> <p> Note that if <code>--whole-file</code> is specified (or implied), any partial-dir files that are found for a file that is being updated will simply be removed (since rsync is sending files without using rsync&#8217;s delta-transfer algorithm). </p>
 </dd>
<dd> <p> Rsync will create the <i>DIR</i> if it is missing, but just the last dir -- not the whole path. This makes it easy to use a relative path (such as &quot;<code>--partial-dir=.rsync-partial</code>&quot;) to have rsync create the partial-directory in the destination file&#8217;s directory when it is needed, and then remove it again when the partial file is deleted. Note that this directory removal is only done for a relative pathname, as it is expected that an absolute path is to a directory that is reserved for partial-dir work. </p>
 </dd>
<dd> <p> If the partial-dir value is not an absolute path, rsync will add an exclude rule at the end of all your existing excludes. This will prevent the sending of any partial-dir files that may exist on the sending side, and will also prevent the untimely deletion of partial-dir items on the receiving side. An example: the above <code>--partial-dir</code> option would add the equivalent of this &quot;perishable&quot; exclude at the end of any other filter rules: <code>-f&nbsp;&#8216;-p .rsync-partial/&#8216;</code> </p>
 </dd>
<dd> <p> If you are supplying your own exclude rules, you may need to add your own exclude/hide/protect rule for the partial-dir because: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd>
<dt>1.</dt>
<dd> <p> the auto-added rule may be ineffective at the end of your other rules, or </p>
 </dd>
<dt>2.</dt>
<dd> <p> you may wish to override rsync&#8217;s exclude choice. </p>
 </dd></dl>
</dl>
<dd> <p> For instance, if you want to make rsync clean-up any left-over partial-dirs that may be lying around, you should specify <code>--delete-after</code> and add a &quot;risk&quot; filter rule, e.g. <code>-f&nbsp;&#8216;R .rsync-partial/&#8216;</code>. Avoid using <code>--delete-before</code> or <code>--delete-during</code> unless you don&#8217;t need rsync to use any of the left-over partial-dir data during the current run. </p>
 </dd>
<dd> <p> IMPORTANT: the <code>--partial-dir</code> should not be writable by other users or it is a security risk! E.g. AVOID &quot;/tmp&quot;! </p>
 </dd>
<dd> <p> You can also set the partial-dir value the <code>RSYNC_PARTIAL_DIR</code> environment variable. Setting this in the environment does not force <code>--partial</code> to be enabled, but rather it affects where partial files go when <code>--partial</code> is specified. For instance, instead of using <code>--partial-dir=.rsync-tmp</code> along with <code>--progress</code>, you could set <code>RSYNC_PARTIAL_DIR=.rsync-tmp</code> in your environment and then use the <code>-P</code> option to turn on the use of the .rsync-tmp dir for partial transfers. The only times that the <code>--partial</code> option does not look for this environment value are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd>
<dt>1.</dt>
<dd> <p> when <code>--inplace</code> was specified (since <code>--inplace</code> conflicts with <code>--partial-dir</code>), and </p>
 </dd>
<dt>2.</dt>
<dd> <p> when <code>--delay-updates</code> was specified (see below). </p>
 </dd></dl>
</dl>
<dd> <p> When a modern rsync resumes the transfer of a file in the partial-dir, that partial file is now updated in-place instead of creating yet another tmp-file copy (so it maxes out at dest + tmp instead of dest + partial + tmp). This requires both ends of the transfer to be at least version 3.2.0. </p>
 </dd>
<dd> <p> For the purposes of the daemon-config&#8217;s &quot;<code>refuse options</code>&quot; setting, <code>--partial-dir</code> does <i>not</i> imply <code>--partial</code>. This is so that a refusal of the <code>--partial</code> option can be used to disallow the overwriting of destination files with a partial transfer, while still allowing the safer idiom provided by <code>--partial-dir</code>. </p>
 </dd>
<dt><code>--delay-updates</code></dt>
<dd> <p> This option puts the temporary file from each updated file into a holding directory until the end of the transfer, at which time all the files are renamed into place in rapid succession. This attempts to make the updating of the files a little more atomic. By default the files are placed into a directory named <code>.~tmp~</code> in each file&#8217;s destination directory, but if you&#8217;ve specified the <code>--partial-dir</code> option, that directory will be used instead. See the comments in the <code>--partial-dir</code> section for a discussion of how this <code>.~tmp~</code> dir will be excluded from the transfer, and what you can do if you want rsync to cleanup old <code>.~tmp~</code> dirs that might be lying around. Conflicts with <code>--inplace</code> and <code>--append</code>. </p>
 </dd>
<dd> <p> This option implies <code>--no-inc-recursive</code> since it needs the full file list in memory in order to be able to iterate over it at the end. </p>
 </dd>
<dd> <p> This option uses more memory on the receiving side (one bit per file transferred) and also requires enough free disk space on the receiving side to hold an additional copy of all the updated files. Note also that you should not use an absolute path to <code>--partial-dir</code> unless: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd>
<dt>1.</dt>
<dd> <p> there is no chance of any of the files in the transfer having the same name (since all the updated files will be put into a single directory if the path is absolute), and </p>
 </dd>
<dt>2.</dt>
<dd> <p> there are no mount points in the hierarchy (since the delayed updates will fail if they can&#8217;t be renamed into place). </p>
 </dd></dl>
</dl>
<dd> <p> See also the &quot;atomic-rsync&quot; python script in the &quot;support&quot; subdir for an update algorithm that is even more atomic (it uses <code>--link-dest</code> and a parallel hierarchy of files). </p>
 </dd>
<dt><code>--prune-empty-dirs</code>, <code>-m</code></dt>
<dd> <p> This option tells the receiving rsync to get rid of empty directories from the file-list, including nested directories that have no non-directory children. This is useful for avoiding the creation of a bunch of useless directories when the sending rsync is recursively scanning a hierarchy of files using include/exclude/filter rules. </p>
 </dd>
<dd> <p> This option can still leave empty directories on the receiving side if you make use of TRANSFER_RULES. </p>
 </dd>
<dd> <p> Because the file-list is actually being pruned, this option also affects what directories get deleted when a delete is active. However, keep in mind that excluded files and directories can prevent existing items from being deleted due to an exclude both hiding source files and protecting destination files. See the perishable filter-rule option for how to avoid this. </p>
 </dd>
<dd> <p> You can prevent the pruning of certain empty directories from the file-list by using a global &quot;protect&quot; filter. For instance, this option would ensure that the directory &quot;emptydir&quot; was kept in the file-list: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>--filter 'protect emptydir/'
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Here&#8217;s an example that copies all .pdf files in a hierarchy, only creating the necessary destination directories to hold the .pdf files, and ensures that any superfluous files and directories in the destination are removed (note the hide filter of non-directories being used instead of an exclude): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -avm --del --include='*.pdf' -f 'hide,! */' src/ dest
</code></pre>
 </dd></dl>
</dl>
<dd> <p> If you didn&#8217;t want to remove superfluous destination files, the more time-honored options of <code>--include=&#8216;*/&#8216;&nbsp;--exclude=&#8216;*&#8216;</code> would work fine in place of the hide-filter (if that is more natural to you). </p>
 </dd>
<dt><code>--progress</code></dt>
<dd> <p> This option tells rsync to print information showing the progress of the transfer. This gives a bored user something to watch. With a modern rsync this is the same as specifying <code>--info=flist2,name,progress</code>, but any user-supplied settings for those info flags takes precedence (e.g. <code>--info=flist0 --progress</code>). </p>
 </dd>
<dd> <p> While rsync is transferring a regular file, it updates a progress line that looks like this: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>782448 63% 110.64kB/s 0:00:04
</code></pre>
 </dd></dl>
</dl>
<dd> <p> In this example, the receiver has reconstructed 782448 bytes or 63% of the sender&#8217;s file, which is being reconstructed at a rate of 110.64 kilobytes per second, and the transfer will finish in 4 seconds if the current rate is maintained until the end. </p>
 </dd>
<dd> <p> These statistics can be misleading if rsync&#8217;s delta-transfer algorithm is in use. For example, if the sender&#8217;s file consists of the basis file followed by additional data, the reported rate will probably drop dramatically when the receiver gets to the literal data, and the transfer will probably take much longer to finish than the receiver estimated as it was finishing the matched part of the file. </p>
 </dd>
<dd> <p> When the file transfer finishes, rsync replaces the progress line with a summary line that looks like this: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>1,238,099 100% 146.38kB/s 0:00:08 (xfr#5, to-chk=169/396)
</code></pre>
 </dd></dl>
</dl>
<dd> <p> In this example, the file was 1,238,099 bytes long in total, the average rate of transfer for the whole file was 146.38 kilobytes per second over the 8 seconds that it took to complete, it was the 5th transfer of a regular file during the current rsync session, and there are 169 more files for the receiver to check (to see if they are up-to-date or not) remaining out of the 396 total files in the file-list. </p>
 </dd>
<dd> <p> In an incremental recursion scan, rsync won&#8217;t know the total number of files in the file-list until it reaches the ends of the scan, but since it starts to transfer files during the scan, it will display a line with the text &quot;ir-chk&quot; (for incremental recursion check) instead of &quot;to-chk&quot; until the point that it knows the full size of the list, at which point it will switch to using &quot;to-chk&quot;. Thus, seeing &quot;ir-chk&quot; lets you know that the total count of files in the file list is still going to increase (and each time it does, the count of files left to check will increase by the number of the files added to the list). </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> The <code>-P</code> option is equivalent to &quot;<code>--partial</code> <code>--progress</code>&quot;. Its purpose is to make it much easier to specify these two options for a long transfer that may be interrupted. </p>
 </dd>
<dd> <p> There is also a <code>--info=progress2</code> option that outputs statistics based on the whole transfer, rather than individual files. Use this flag without outputting a filename (e.g. avoid <code>-v</code> or specify <code>--info=name0</code>) if you want to see how the transfer is doing without scrolling the screen with a lot of names. (You don&#8217;t need to specify the <code>--progress</code> option in order to use <code>--info=progress2</code>.) </p>
 </dd>
<dd> <p> Finally, you can get an instant progress report by sending rsync a signal of either SIGINFO or SIGVTALRM. On BSD systems, a SIGINFO is generated by typing a Ctrl+T (Linux doesn&#8217;t currently support a SIGINFO signal). When the client-side process receives one of those signals, it sets a flag to output a single progress report which is output when the current file transfer finishes (so it may take a little time if a big file is being handled when the signal arrives). A filename is output (if needed) followed by the <code>--info=progress2</code> format of progress info. If you don&#8217;t know which of the 3 rsync processes is the client process, it&#8217;s OK to signal all of them (since the non-client processes ignore the signal). </p>
 </dd>
<dd> <p> CAUTION: sending SIGVTALRM to an older rsync (pre-3.2.0) will kill it. </p>
 </dd>
<dt><code>--password-file=FILE</code></dt>
<dd> <p> This option allows you to provide a password for accessing an rsync daemon via a file or via standard input if <code>FILE</code> is <code>-</code>. The file should contain just the password on the first line (all other lines are ignored). Rsync will exit with an error if <code>FILE</code> is world readable or if a root-run rsync command finds a non-root-owned file. </p>
 </dd>
<dd> <p> This option does not supply a password to a remote shell transport such as ssh; to learn how to do that, consult the remote shell&#8217;s documentation. When accessing an rsync daemon using a remote shell as the transport, this option only comes into effect after the remote shell finishes its authentication (i.e. if you have also specified a password in the daemon&#8217;s config file). </p>
 </dd>
<dt><code>--early-input=FILE</code></dt>
<dd> <p> This option allows rsync to send up to 5K of data to the &quot;early exec&quot; script on its stdin. One possible use of this data is to give the script a secret that can be used to mount an encrypted filesystem (which you should unmount in the the &quot;post-xfer exec&quot; script). </p>
 </dd>
<dd> <p> The daemon must be at least version 3.2.1. </p>
 </dd>
<dt><code>--list-only</code></dt>
<dd> <p> This option will cause the source files to be listed instead of transferred. This option is inferred if there is a single source arg and no destination specified, so its main uses are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd>
<dt>1.</dt>
<dd> <p> to turn a copy command that includes a destination arg into a file-listing command, or </p>
 </dd>
<dt>2.</dt>
<dd> <p> to be able to specify more than one source arg. Note: be sure to include the destination. </p>
 </dd></dl>
</dl>
<dd> <p> CAUTION: keep in mind that a source arg with a wild-card is expanded by the shell into multiple args, so it is never safe to try to specify a single wild-card arg to try to infer this option. A safe example is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync -av --list-only foo* dest/
</code></pre>
 </dd></dl>
</dl>
<dd> <p> This option always uses an output format that looks similar to this: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>drwxrwxr-x 4,096 2022/09/30 12:53:11 support
-rw-rw-r-- 80 2005/01/11 10:37:37 support/Makefile
</code></pre>
 </dd></dl>
</dl>
<dd> <p> The only option that affects this output style is (as of 3.1.0) the <code>--human-readable</code> (<code>-h</code>) option. The default is to output sizes as byte counts with digit separators (in a 14-character-width column). Specifying at least one <code>-h</code> option makes the sizes output with unit suffixes. If you want old-style bytecount sizes without digit separators (and an 11-character-width column) use <code>--no-h</code>. </p>
 </dd>
<dd> <p> Compatibility note: when requesting a remote listing of files from an rsync that is version 2.6.3 or older, you may encounter an error if you ask for a non-recursive listing. This is because a file listing implies the <code>--dirs</code> option w/o <code>--recursive</code>, and older rsyncs don&#8217;t have that option. To avoid this problem, either specify the <code>--no-dirs</code> option (if you don&#8217;t need to expand a directory&#8217;s content), or turn on recursion and exclude the content of subdirectories: <code>-r --exclude=&#8216;/*/*&#8216;</code>. </p>
 </dd>
<dt><code>--bwlimit=RATE</code></dt>
<dd> <p> This option allows you to specify the maximum transfer rate for the data sent over the socket, specified in units per second. The RATE value can be suffixed with a string to indicate a size multiplier, and may be a fractional value (e.g. <code>--bwlimit=1.5m</code>). If no suffix is specified, the value will be assumed to be in units of 1024 bytes (as if &quot;K&quot; or &quot;KiB&quot; had been appended). See the <code>--max-size</code> option for a description of all the available suffixes. A value of 0 specifies no limit. </p>
 </dd>
<dd> <p> For backward-compatibility reasons, the rate limit will be rounded to the nearest KiB unit, so no rate smaller than 1024 bytes per second is possible. </p>
 </dd>
<dd> <p> Rsync writes data over the socket in blocks, and this option both limits the size of the blocks that rsync writes, and tries to keep the average transfer rate at the requested limit. Some burstiness may be seen where rsync writes out a block of data and then sleeps to bring the average rate into compliance. </p>
 </dd>
<dd> <p> Due to the internal buffering of data, the <code>--progress</code> option may not be an accurate reflection on how fast the data is being sent. This is because some files can show up as being rapidly sent when the data is quickly buffered, while other can show up as very slow when the flushing of the output buffer occurs. This may be fixed in a future version. </p>
 </dd>
<dd> <p> See also the daemon version of the <code>--bwlimit</code> option. </p>
 </dd>
<dt><code>--stop-after=MINS</code>, (<code>--time-limit=MINS</code>)</dt>
<dd> <p> This option tells rsync to stop copying when the specified number of minutes has elapsed. </p>
 </dd>
<dd> <p> For maximal flexibility, rsync does not communicate this option to the remote rsync since it is usually enough that one side of the connection quits as specified. This allows the option&#8217;s use even when only one side of the connection supports it. You can tell the remote side about the time limit using <code>--remote-option</code> (<code>-M</code>), should the need arise. </p>
 </dd>
<dd> <p> The <code>--time-limit</code> version of this option is deprecated. </p>
 </dd>
<dt><code>--stop-at=y-m-dTh:m</code></dt>
<dd> <p> This option tells rsync to stop copying when the specified point in time has been reached. The date &amp; time can be fully specified in a numeric format of year-month-dayThour:minute (e.g. 2000-12-31T23:59) in the local timezone. You may choose to separate the date numbers using slashes instead of dashes. </p>
 </dd>
<dd> <p> The value can also be abbreviated in a variety of ways, such as specifying a 2-digit year and/or leaving off various values. In all cases, the value will be taken to be the next possible point in time where the supplied information matches. If the value specifies the current time or a past time, rsync exits with an error. </p>
 </dd>
<dd> <p> For example, &quot;1-30&quot; specifies the next January 30th (at midnight local time), &quot;14:00&quot; specifies the next 2 P.M., &quot;1&quot; specifies the next 1st of the month at midnight, &quot;31&quot; specifies the next month where we can stop on its 31st day, and &quot;:59&quot; specifies the next 59th minute after the hour. </p>
 </dd>
<dd> <p> For maximal flexibility, rsync does not communicate this option to the remote rsync since it is usually enough that one side of the connection quits as specified. This allows the option&#8217;s use even when only one side of the connection supports it. You can tell the remote side about the time limit using <code>--remote-option</code> (<code>-M</code>), should the need arise. Do keep in mind that the remote host may have a different default timezone than your local host. </p>
 </dd>
<dt><code>--fsync</code></dt>
<dd> <p> Cause the receiving side to fsync each finished file. This may slow down the transfer, but can help to provide peace of mind when updating critical files. </p>
 </dd>
<dt><code>--write-batch=FILE</code></dt>
<dd> <p> Record a file that can later be applied to another identical destination with <code>--read-batch</code>. See the &quot;BATCH MODE&quot; section for details, and also the <code>--only-write-batch</code> option. </p>
 </dd>
<dd> <p> This option overrides the negotiated checksum &amp; compress lists and always negotiates a choice based on old-school md5/md4/zlib choices. If you want a more modern choice, use the <code>--checksum-choice</code> (<code>--cc</code>) and/or <code>--compress-choice</code> (<code>--zc</code>) options. </p>
 </dd>
<dt><code>--only-write-batch=FILE</code></dt>
<dd> <p> Works like <code>--write-batch</code>, except that no updates are made on the destination system when creating the batch. This lets you transport the changes to the destination system via some other means and then apply the changes via <code>--read-batch</code>. </p>
 </dd>
<dd> <p> Note that you can feel free to write the batch directly to some portable media: if this media fills to capacity before the end of the transfer, you can just apply that partial transfer to the destination and repeat the whole process to get the rest of the changes (as long as you don&#8217;t mind a partially updated destination system while the multi-update cycle is happening). </p>
 </dd>
<dd> <p> Also note that you only save bandwidth when pushing changes to a remote system because this allows the batched data to be diverted from the sender into the batch file without having to flow over the wire to the receiver (when pulling, the sender is remote, and thus can&#8217;t write the batch). </p>
 </dd>
<dt><code>--read-batch=FILE</code></dt>
<dd> <p> Apply all of the changes stored in FILE, a file previously generated by <code>--write-batch</code>. If <i>FILE</i> is <code>-</code>, the batch data will be read from standard input. See the &quot;BATCH MODE&quot; section for details. </p>
 </dd>
<dt><code>--protocol=NUM</code></dt>
<dd> <p> Force an older protocol version to be used. This is useful for creating a batch file that is compatible with an older version of rsync. For instance, if rsync 2.6.4 is being used with the <code>--write-batch</code> option, but rsync 2.6.3 is what will be used to run the <code>--read-batch</code> option, you should use &quot;--protocol=28&quot; when creating the batch file to force the older protocol version to be used in the batch file (assuming you can&#8217;t upgrade the rsync on the reading system). </p>
 </dd>
<dt><code>--iconv=CONVERT_SPEC</code></dt>
<dd> <p> Rsync can convert filenames between character sets using this option. Using a CONVERT_SPEC of &quot;.&quot; tells rsync to look up the default character-set via the locale setting. Alternately, you can fully specify what conversion to do by giving a local and a remote charset separated by a comma in the order <code>--iconv=LOCAL,REMOTE</code>, e.g. <code>--iconv=utf8,iso88591</code>. This order ensures that the option will stay the same whether you&#8217;re pushing or pulling files. Finally, you can specify either <code>--no-iconv</code> or a CONVERT_SPEC of &quot;-&quot; to turn off any conversion. The default setting of this option is site-specific, and can also be affected via the <code>RSYNC_ICONV</code> environment variable. </p>
 </dd>
<dd> <p> For a list of what charset names your local iconv library supports, you can run &quot;<code>iconv --list</code>&quot;. </p>
 </dd>
<dd> <p> If you specify the <code>--secluded-args</code> (<code>-s</code>) option, rsync will translate the filenames you specify on the command-line that are being sent to the remote host. See also the <code>--files-from</code> option. </p>
 </dd>
<dd> <p> Note that rsync does not do any conversion of names in filter files (including include/exclude files). It is up to you to ensure that you&#8217;re specifying matching rules that can match on both sides of the transfer. For instance, you can specify extra include/exclude rules if there are filename differences on the two sides that need to be accounted for. </p>
 </dd>
<dd> <p> When you pass an <code>--iconv</code> option to an rsync daemon that allows it, the daemon uses the charset specified in its &quot;charset&quot; configuration parameter regardless of the remote charset you actually pass. Thus, you may feel free to specify just the local charset for a daemon transfer (e.g. <code>--iconv=utf8</code>). </p>
 </dd>
<dt><code>--ipv4</code>, <code>-4</code> or <code>--ipv6</code>, <code>-6</code></dt>
<dd> <p> Tells rsync to prefer IPv4/IPv6 when creating sockets or running ssh. This affects sockets that rsync has direct control over, such as the outgoing socket when directly contacting an rsync daemon, as well as the forwarding of the <code>-4</code> or <code>-6</code> option to ssh when rsync can deduce that ssh is being used as the remote shell. For other remote shells you&#8217;ll need to specify the &quot;<code>--rsh SHELL -4</code>&quot; option directly (or whatever IPv4/IPv6 hint options it uses). </p>
 </dd>
<dd> <p> See also the daemon version of these options. </p>
 </dd>
<dd> <p> If rsync was compiled without support for IPv6, the <code>--ipv6</code> option will have no effect. The <code>rsync --version</code> output will contain &quot;<code>no IPv6</code>&quot; if is the case. </p>
 </dd>
<dt><code>--checksum-seed=NUM</code></dt>
<dd> <p> Set the checksum seed to the integer NUM. This 4 byte checksum seed is included in each block and MD4 file checksum calculation (the more modern MD5 file checksums don&#8217;t use a seed). By default the checksum seed is generated by the server and defaults to the current <code>time</code>(). This option is used to set a specific checksum seed, which is useful for applications that want repeatable block checksums, or in the case where the user wants a more random checksum seed. Setting NUM to 0 causes rsync to use the default of <code>time</code>() for checksum seed. </p>
 </dd></dl>
<h2>DAEMON OPTIONS</h2>
<p> The options allowed when starting an rsync daemon are as follows: </p>
<dl>
<dt><code>--daemon</code></dt>
<dd> <p> This tells rsync that it is to run as a daemon. The daemon you start running may be accessed using an rsync client using the <code>host::module</code> or <code><a href="rsync://host/module/">rsync://host/module/</a></code> syntax. </p>
 </dd>
<dd> <p> If standard input is a socket then rsync will assume that it is being run via inetd, otherwise it will detach from the current terminal and become a background daemon. The daemon will read the config file (rsyncd.conf) on each connect made by a client and respond to requests accordingly. </p>
 </dd>
<dd> <p> See the <code>rsyncd.conf</code>(5) manpage for more details. </p>
 </dd>
<dt><code>--address=ADDRESS</code></dt>
<dd> <p> By default rsync will bind to the wildcard address when run as a daemon with the <code>--daemon</code> option. The <code>--address</code> option allows you to specify a specific IP address (or hostname) to bind to. This makes virtual hosting possible in conjunction with the <code>--config</code> option. </p>
 </dd>
<dd> <p> See also the address global option in the rsyncd.conf manpage and the client version of the <code>--address</code> option. </p>
 </dd>
<dt><code>--bwlimit=RATE</code></dt>
<dd> <p> This option allows you to specify the maximum transfer rate for the data the daemon sends over the socket. The client can still specify a smaller <code>--bwlimit</code> value, but no larger value will be allowed. </p>
 </dd>
<dd> <p> See the client version of the <code>--bwlimit</code> option for some extra details. </p>
 </dd>
<dt><code>--config=FILE</code></dt>
<dd> <p> This specifies an alternate config file than the default. This is only relevant when <code>--daemon</code> is specified. The default is /etc/rsyncd.conf unless the daemon is running over a remote shell program and the remote user is not the super-user; in that case the default is rsyncd.conf in the current directory (typically $HOME). </p>
 </dd>
<dt><code>--dparam=OVERRIDE</code>, <code>-M</code></dt>
<dd> <p> This option can be used to set a daemon-config parameter when starting up rsync in daemon mode. It is equivalent to adding the parameter at the end of the global settings prior to the first module&#8217;s definition. The parameter names can be specified without spaces, if you so desire. For instance: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>rsync --daemon -M pidfile=/path/rsync.pid
</code></pre>
 </dd></dl>
</dl>
<dt><code>--no-detach</code></dt>
<dd> <p> When running as a daemon, this option instructs rsync to not detach itself and become a background process. This option is required when running as a service on Cygwin, and may also be useful when rsync is supervised by a program such as <code>daemontools</code> or AIX&#8217;s <code>System Resource Controller</code>. <code>--no-detach</code> is also recommended when rsync is run under a debugger. This option has no effect if rsync is run from inetd or sshd. </p>
 </dd>
<dt><code>--port=PORT</code></dt>
<dd> <p> This specifies an alternate TCP port number for the daemon to listen on rather than the default of 873. </p>
 </dd>
<dd> <p> See also the client version of the <code>--port</code> option and the port global setting in the rsyncd.conf manpage. </p>
 </dd>
<dt><code>--log-file=FILE</code></dt>
<dd> <p> This option tells the rsync daemon to use the given log-file name instead of using the &quot;<code>log file</code>&quot; setting in the config file. </p>
 </dd>
<dd> <p> See also the client version of the <code>--log-file</code> option. </p>
 </dd>
<dt><code>--log-file-format=FORMAT</code></dt>
<dd> <p> This option tells the rsync daemon to use the given FORMAT string instead of using the &quot;<code>log format</code>&quot; setting in the config file. It also enables &quot;<code>transfer logging</code>&quot; unless the string is empty, in which case transfer logging is turned off. </p>
 </dd>
<dd> <p> See also the client version of the <code>--log-file-format</code> option. </p>
 </dd>
<dt><code>--sockopts</code></dt>
<dd> <p> This overrides the <code>socket options</code> setting in the rsyncd.conf file and has the same syntax. </p>
 </dd>
<dd> <p> See also the client version of the <code>--sockopts</code> option. </p>
 </dd>
<dt><code>--verbose</code>, <code>-v</code></dt>
<dd> <p> This option increases the amount of information the daemon logs during its startup phase. After the client connects, the daemon&#8217;s verbosity level will be controlled by the options that the client used and the &quot;<code>max verbosity</code>&quot; setting in the module&#8217;s config section. </p>
 </dd>
<dd> <p> See also the client version of the <code>--verbose</code> option. </p>
 </dd>
<dt><code>--ipv4</code>, <code>-4</code> or <code>--ipv6</code>, <code>-6</code></dt>
<dd> <p> Tells rsync to prefer IPv4/IPv6 when creating the incoming sockets that the rsync daemon will use to listen for connections. One of these options may be required in older versions of Linux to work around an IPv6 bug in the kernel (if you see an &quot;address already in use&quot; error when nothing else is using the port, try specifying <code>--ipv6</code> or <code>--ipv4</code> when starting the daemon). </p>
 </dd>
<dd> <p> See also the client version of these options. </p>
 </dd>
<dd> <p> If rsync was compiled without support for IPv6, the <code>--ipv6</code> option will have no effect. The <code>rsync --version</code> output will contain &quot;<code>no IPv6</code>&quot; if is the case. </p>
 </dd>
<dt><code>--help</code>, <code>-h</code></dt>
<dd> <p> When specified after <code>--daemon</code>, print a short help page describing the options available for starting an rsync daemon. </p>
 </dd></dl>
<h2>FILTER RULES</h2>
<p> The filter rules allow for custom control of several aspects of how files are handled: </p>
<dl>
<dt>o</dt>
<dd> <p> Control which files the sending side puts into the file list that describes the transfer hierarchy </p>
 </dd>
<dt>o</dt>
<dd> <p> Control which files the receiving side protects from deletion when the file is not in the sender&#8217;s file list </p>
 </dd>
<dt>o</dt>
<dd> <p> Control which extended attribute names are skipped when copying xattrs </p>
 </dd></dl>
<p> The rules are either directly specified via option arguments or they can be read in from one or more files. The filter-rule files can even be a part of the hierarchy of files being copied, affecting different parts of the tree in different ways. </p>
<h3>SIMPLE INCLUDE/EXCLUDE RULES</h3>
<p> We will first cover the basics of how include &amp; exclude rules affect what files are transferred, ignoring any deletion side-effects. Filter rules mainly affect the contents of directories that rsync is &quot;recursing&quot; into, but they can also affect a top-level item in the transfer that was specified as a argument. </p>
<p> The default for any unmatched file/dir is for it to be included in the transfer, which puts the file/dir into the sender&#8217;s file list. The use of an exclude rule causes one or more matching files/dirs to be left out of the sender&#8217;s file list. An include rule can be used to limit the effect of an exclude rule that is matching too many files. </p>
<p> The order of the rules is important because the first rule that matches is the one that takes effect. Thus, if an early rule excludes a file, no include rule that comes after it can have any effect. This means that you must place any include overrides somewhere prior to the exclude that it is intended to limit. </p>
<p> When a directory is excluded, all its contents and sub-contents are also excluded. The sender doesn&#8217;t scan through any of it at all, which can save a lot of time when skipping large unneeded sub-trees. </p>
<p> It is also important to understand that the include/exclude rules are applied to every file and directory that the sender is recursing into. Thus, if you want a particular deep file to be included, you have to make sure that none of the directories that must be traversed on the way down to that file are excluded or else the file will never be discovered to be included. As an example, if the directory &quot;<code>a/path</code>&quot; was given as a transfer argument and you want to ensure that the file &quot;<code>a/path/down/deep/wanted.txt</code>&quot; is a part of the transfer, then the sender must not exclude the directories &quot;<code>a/path</code>&quot;, &quot;<code>a/path/down</code>&quot;, or &quot;<code>a/path/down/deep</code>&quot; as it makes it way scanning through the file tree. </p>
<p> When you are working on the rules, it can be helpful to ask rsync to tell you what is being excluded/included and why. Specifying <code>--debug=FILTER</code> or (when pulling files) <code>-M--debug=FILTER</code> turns on level 1 of the FILTER debug information that will output a message any time that a file or directory is included or excluded and which rule it matched. Beginning in 3.2.4 it will also warn if a filter rule has trailing whitespace, since an exclude of &quot;foo&nbsp;&quot; (with a trailing space) will not exclude a file named &quot;foo&quot;. </p>
<p> Exclude and include rules can specify wildcard PATTERN MATCHING RULES (similar to shell wildcards) that allow you to match things like a file suffix or a portion of a filename. </p>
<p> A rule can be limited to only affecting a directory by putting a trailing slash onto the filename. </p>
<h3>SIMPLE INCLUDE/EXCLUDE EXAMPLE</h3>
<p> With the following file tree created on the sending side: </p>
<dl>
<dd> <pre><code>mkdir x/
touch x/file.txt
mkdir x/y/
touch x/y/file.txt
touch x/y/zzz.txt
mkdir x/z/
touch x/z/file.txt
</code></pre>
 </dd></dl>
<p> Then the following rsync command will transfer the file &quot;<code>x/y/file.txt</code>&quot; and the directories needed to hold it, resulting in the path &quot;<code>/tmp/x/y/file.txt</code>&quot; existing on the remote host: </p>
<dl>
<dd> <pre><code>rsync -ai -f'+ x/' -f'+ x/y/' -f'+ x/y/file.txt' -f'- *' x host:/tmp/
</code></pre>
 </dd></dl>
<p> Aside: this copy could also have been accomplished using the <code>-R</code> option (though the 2 commands behave differently if deletions are enabled): </p>
<dl>
<dd> <pre><code>rsync -aiR x/y/file.txt host:/tmp/
</code></pre>
 </dd></dl>
<p> The following command does not need an include of the &quot;x&quot; directory because it is not a part of the transfer (note the traililng slash). Running this command would copy just &quot;<code>/tmp/x/file.txt</code>&quot; because the &quot;y&quot; and &quot;z&quot; dirs get excluded: </p>
<dl>
<dd> <pre><code>rsync -ai -f'+ file.txt' -f'- *' x/ host:/tmp/x/
</code></pre>
 </dd></dl>
<p> This command would omit the zzz.txt file while copying &quot;x&quot; and everything else it contains: </p>
<dl>
<dd> <pre><code>rsync -ai -f'- zzz.txt' x host:/tmp/
</code></pre>
 </dd></dl>
<h3>FILTER RULES WHEN DELETING</h3>
<p> By default the include &amp; exclude filter rules affect both the sender (as it creates its file list) and the receiver (as it creates its file lists for calculating deletions). If no delete option is in effect, the receiver skips creating the delete-related file lists. This two-sided default can be manually overridden so that you are only specifying sender rules or receiver rules, as described in the FILTER RULES IN DEPTH section. </p>
<p> When deleting, an exclude protects a file from being removed on the receiving side while an include overrides that protection (putting the file at risk of deletion). The default is for a file to be at risk -- its safety depends on it matching a corresponding file from the sender. </p>
<p> An example of the two-sided exclude effect can be illustrated by the copying of a C development directory between 2 systems. When doing a touch-up copy, you might want to skip copying the built executable and the <code>.o</code> files (sender hide) so that the receiving side can build their own and not lose any object files that are already correct (receiver protect). For instance: </p>
<dl>
<dd> <pre><code>rsync -ai --del -f'- *.o' -f'- cmd' src host:/dest/
</code></pre>
 </dd></dl>
<p> Note that using <code>-f&#8217;-p&nbsp;*.o&#8217;</code> is even better than <code>-f&#8217;-&nbsp;*.o&#8217;</code> if there is a chance that the directory structure may have changed. The &quot;p&quot; modifier is discussed in FILTER RULE MODIFIERS. </p>
<p> One final note, if your shell doesn&#8217;t mind unexpanded wildcards, you could simplify the typing of the filter options by using an underscore in place of the space and leaving off the quotes. For instance, <code>-f -_*.o -f -_cmd</code> (and similar) could be used instead of the filter options above. </p>
<h3>FILTER RULES IN DEPTH</h3>
<p> Rsync supports old-style include/exclude rules and new-style filter rules. The older rules are specified using <code>--include</code> and <code>--exclude</code> as well as the <code>--include-from</code> and <code>--exclude-from</code>. These are limited in behavior but they don&#8217;t require a &quot;-&quot; or &quot;+&quot; prefix. An old-style exclude rule is turned into a &quot;<code>- name</code>&quot; filter rule (with no modifiers) and an old-style include rule is turned into a &quot;<code>+&nbsp;name</code>&quot; filter rule (with no modifiers). </p>
<p> Rsync builds an ordered list of filter rules as specified on the command-line and/or read-in from files. New style filter rules have the following syntax: </p>
<dl>
<dd> <pre><code>RULE [PATTERN_OR_FILENAME]
RULE,MODIFIERS [PATTERN_OR_FILENAME]
</code></pre>
 </dd></dl>
<p> You have your choice of using either short or long RULE names, as described below. If you use a short-named rule, the &#8216;,&#8216; separating the RULE from the MODIFIERS is optional. The PATTERN or FILENAME that follows (when present) must come after either a single space or an underscore (_). Any additional spaces and/or underscores are considered to be a part of the pattern name. Here are the available rule prefixes: </p>
<dl>
<dt><code>exclude,&nbsp;&#8216;-&#8216;</code></dt>
<dd> <p> specifies an exclude pattern that (by default) is both a <code>hide</code> and a <code>protect</code>. </p>
 </dd>
<dt><code>include,&nbsp;&#8216;+&#8216;</code></dt>
<dd> <p> specifies an include pattern that (by default) is both a <code>show</code> and a <code>risk</code>. </p>
 </dd>
<dt><code>merge,&nbsp;&#8216;.&#8216;</code></dt>
<dd> <p> specifies a merge-file on the client side to read for more rules. </p>
 </dd>
<dt><code>dir-merge,&nbsp;&#8216;:&#8216;</code></dt>
<dd> <p> specifies a per-directory merge-file. Using this kind of filter rule requires that you trust the sending side&#8217;s filter checking, so it has the side-effect mentioned under the <code>--trust-sender</code> option. </p>
 </dd>
<dt><code>hide,&nbsp;&#8216;H&#8217;</code></dt>
<dd> <p> specifies a pattern for hiding files from the transfer. Equivalent to a sender-only exclude, so <code>-f&#8217;H foo&#8217;</code> could also be specified as <code>-f&#8217;-s foo&#8217;</code>. </p>
 </dd>
<dt><code>show,&nbsp;&#8216;S&#8217;</code></dt>
<dd> <p> files that match the pattern are not hidden. Equivalent to a sender-only include, so <code>-f&#8217;S foo&#8217;</code> could also be specified as <code>-f&#8217;+s foo&#8217;</code>. </p>
 </dd>
<dt><code>protect,&nbsp;&#8216;P&#8217;</code></dt>
<dd> <p> specifies a pattern for protecting files from deletion. Equivalent to a receiver-only exclude, so <code>-f&#8217;P foo&#8217;</code> could also be specified as <code>-f&#8217;-r foo&#8217;</code>. </p>
 </dd>
<dt><code>risk,&nbsp;&#8216;R&#8217;</code></dt>
<dd> <p> files that match the pattern are not protected. Equivalent to a receiver-only include, so <code>-f&#8217;R foo&#8217;</code> could also be specified as <code>-f&#8217;+r foo&#8217;</code>. </p>
 </dd>
<dt><code>clear,&nbsp;&#8216;!&#8216;</code></dt>
<dd> <p> clears the current include/exclude list (takes no arg) </p>
 </dd></dl>
<p> When rules are being read from a file (using merge or dir-merge), empty lines are ignored, as are whole-line comments that start with a &#8216;<code>#</code>&#8216; (filename rules that contain a hash character are unaffected). </p>
<p> Note also that the <code>--filter</code>, <code>--include</code>, and <code>--exclude</code> options take one rule/pattern each. To add multiple ones, you can repeat the options on the command-line, use the merge-file syntax of the <code>--filter</code> option, or the <code>--include-from</code> / <code>--exclude-from</code> options. </p>
<h3>PATTERN MATCHING RULES</h3>
<p> Most of the rules mentioned above take an argument that specifies what the rule should match. If rsync is recursing through a directory hierarchy, keep in mind that each pattern is matched against the name of every directory in the descent path as rsync finds the filenames to send. </p>
<p> The matching rules for the pattern argument take several forms: </p>
<dl>
<dt>o</dt>
<dd> <p> If a pattern contains a <code>/</code> (not counting a trailing slash) or a &quot;<code>**</code>&quot; (which can match a slash), then the pattern is matched against the full pathname, including any leading directories within the transfer. If the pattern doesn&#8217;t contain a (non-trailing) <code>/</code> or a &quot;<code>**</code>&quot;, then it is matched only against the final component of the filename or pathname. For example, <code>foo</code> means that the final path component must be &quot;foo&quot; while <code>foo/bar</code> would match the last 2 elements of the path (as long as both elements are within the transfer). </p>
 </dd>
<dt>o</dt>
<dd> <p> A pattern that ends with a <code>/</code> only matches a directory, not a regular file, symlink, or device. </p>
 </dd>
<dt>o</dt>
<dd> <p> A pattern that starts with a <code>/</code> is anchored to the start of the transfer path instead of the end. For example, <code>/foo/**</code> or <code>/foo/bar/**</code> match only leading elements in the path. If the rule is read from a per-directory filter file, the transfer path being matched will begin at the level of the filter file instead of the top of the transfer. See the section on ANCHORING INCLUDE/EXCLUDE PATTERNS for a full discussion of how to specify a pattern that matches at the root of the transfer. </p>
 </dd></dl>
<p> Rsync chooses between doing a simple string match and wildcard matching by checking if the pattern contains one of these three wildcard characters: &#8216;<code>*</code>&#8216;, &#8216;<code>?</code>&#8216;, and &#8216;<code>[</code>&#8216; : </p>
<dl>
<dt>o</dt>
<dd> <p> a &#8216;<code>?</code>&#8216; matches any single character except a slash (<code>/</code>). </p>
 </dd>
<dt>o</dt>
<dd> <p> a &#8216;<code>*</code>&#8216; matches zero or more non-slash characters. </p>
 </dd>
<dt>o</dt>
<dd> <p> a &#8216;<code>**</code>&#8216; matches zero or more characters, including slashes. </p>
 </dd>
<dt>o</dt>
<dd> <p> a &#8216;<code>[</code>&#8216; introduces a character class, such as <code>[a-z]</code> or <code>[[:alpha:]]</code>, that must match one character. </p>
 </dd>
<dt>o</dt>
<dd> <p> a trailing <code>***</code> in the pattern is a shorthand that allows you to match a directory and all its contents using a single rule. For example, specifying &quot;<code>dir_name/***</code>&quot; will match both the &quot;dir_name&quot; directory (as if &quot;<code>dir_name/</code>&quot; had been specified) and everything in the directory (as if &quot;<code>dir_name/**</code>&quot; had been specified). </p>
 </dd>
<dt>o</dt>
<dd> <p> a backslash can be used to escape a wildcard character, but it is only interpreted as an escape character if at least one wildcard character is present in the match pattern. For instance, the pattern &quot;<code>foo\bar</code>&quot; matches that single backslash literally, while the pattern &quot;<code>foo\bar*</code>&quot; would need to be changed to &quot;<code>foo\\bar*</code>&quot; to avoid the &quot;<code>\b</code>&quot; becoming just &quot;b&quot;. </p>
 </dd></dl>
<p> Here are some examples of exclude/include matching: </p>
<dl>
<dt>o</dt>
<dd> <p> Option <code>-f&#8217;-&nbsp;*.o&#8217;</code> would exclude all filenames ending with <code>.o</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> Option <code>-f&#8217;-&nbsp;/foo&#8217;</code> would exclude a file (or directory) named foo in the transfer-root directory </p>
 </dd>
<dt>o</dt>
<dd> <p> Option <code>-f&#8217;- foo/&#8216;</code> would exclude any directory named foo </p>
 </dd>
<dt>o</dt>
<dd> <p> Option <code>-f&#8217;- foo/*/bar&#8217;</code> would exclude any file/dir named bar which is at two levels below a directory named foo (if foo is in the transfer) </p>
 </dd>
<dt>o</dt>
<dd> <p> Option <code>-f&#8217;-&nbsp;/foo/**/bar&#8217;</code> would exclude any file/dir named bar that was two or more levels below a top-level directory named foo (note that /foo/bar is <code>not</code> excluded by this) </p>
 </dd>
<dt>o</dt>
<dd> <p> Options <code>-f&#8217;+&nbsp;*/&#8216;&nbsp;-f&#8217;+&nbsp;*.c&#8217;&nbsp;-f&#8217;-&nbsp;*&#8216;</code> would include all directories and .c source files but nothing else </p>
 </dd>
<dt>o</dt>
<dd> <p> Options <code>-f&#8217;+&nbsp;foo/&#8216;&nbsp;-f&#8217;+&nbsp;foo/bar.c&#8217;&nbsp;-f&#8217;-&nbsp;*&#8216;</code> would include only the foo directory and foo/bar.c (the foo directory must be explicitly included or it would be excluded by the &quot;<code>-&nbsp;*</code>&quot;) </p>
 </dd></dl>
<h3>FILTER RULE MODIFIERS</h3>
<p> The following modifiers are accepted after an include (+) or exclude (-) rule: </p>
<dl>
<dt>o</dt>
<dd> <p> A <code>/</code> specifies that the include/exclude rule should be matched against the absolute pathname of the current item. For example, <code>-f&#8217;-/&nbsp;/etc/passwd&#8217;</code> would exclude the passwd file any time the transfer was sending files from the &quot;/etc&quot; directory, and &quot;-/ subdir/foo&quot; would always exclude &quot;foo&quot; when it is in a dir named &quot;subdir&quot;, even if &quot;foo&quot; is at the root of the current transfer. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>!</code> specifies that the include/exclude should take effect if the pattern fails to match. For instance, <code>-f&#8217;-!&nbsp;*/&#8216;</code> would exclude all non-directories. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>C</code> is used to indicate that all the global CVS-exclude rules should be inserted as excludes in place of the &quot;-C&quot;. No arg should follow. </p>
 </dd>
<dt>o</dt>
<dd> <p> An <code>s</code> is used to indicate that the rule applies to the sending side. When a rule affects the sending side, it affects what files are put into the sender&#8217;s file list. The default is for a rule to affect both sides unless <code>--delete-excluded</code> was specified, in which case default rules become sender-side only. See also the hide (H) and show (S) rules, which are an alternate way to specify sending-side includes/excludes. </p>
 </dd>
<dt>o</dt>
<dd> <p> An <code>r</code> is used to indicate that the rule applies to the receiving side. When a rule affects the receiving side, it prevents files from being deleted. See the <code>s</code> modifier for more info. See also the protect (P) and risk (R) rules, which are an alternate way to specify receiver-side includes/excludes. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>p</code> indicates that a rule is perishable, meaning that it is ignored in directories that are being deleted. For instance, the <code>--cvs-exclude</code> (<code>-C</code>) option&#8217;s default rules that exclude things like &quot;CVS&quot; and &quot;<code>*.o</code>&quot; are marked as perishable, and will not prevent a directory that was removed on the source from being deleted on the destination. </p>
 </dd>
<dt>o</dt>
<dd> <p> An <code>x</code> indicates that a rule affects xattr names in xattr copy/delete operations (and is thus ignored when matching file/dir names). If no xattr-matching rules are specified, a default xattr filtering rule is used (see the <code>--xattrs</code> option). </p>
 </dd></dl>
<h3>MERGE-FILE FILTER RULES</h3>
<p> You can merge whole files into your filter rules by specifying either a merge (.) or a dir-merge (:) filter rule (as introduced in the FILTER RULES section above). </p>
<p> There are two kinds of merged files -- single-instance (&#8216;.&#8216;) and per-directory (&#8216;:&#8216;). A single-instance merge file is read one time, and its rules are incorporated into the filter list in the place of the &quot;.&quot; rule. For per-directory merge files, rsync will scan every directory that it traverses for the named file, merging its contents when the file exists into the current list of inherited rules. These per-directory rule files must be created on the sending side because it is the sending side that is being scanned for the available files to transfer. These rule files may also need to be transferred to the receiving side if you want them to affect what files don&#8217;t get deleted (see PER-DIRECTORY RULES AND DELETE below). </p>
<p> Some examples: </p>
<dl>
<dd> <pre><code>merge /etc/rsync/default.rules
. /etc/rsync/default.rules
dir-merge .per-dir-filter
dir-merge,n- .non-inherited-per-dir-excludes
:n- .non-inherited-per-dir-excludes
</code></pre>
 </dd></dl>
<p> The following modifiers are accepted after a merge or dir-merge rule: </p>
<dl>
<dt>o</dt>
<dd> <p> A <code>-</code> specifies that the file should consist of only exclude patterns, with no other rule-parsing except for in-file comments. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>+</code> specifies that the file should consist of only include patterns, with no other rule-parsing except for in-file comments. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>C</code> is a way to specify that the file should be read in a CVS-compatible manner. This turns on &#8216;n&#8217;, &#8216;w&#8217;, and &#8216;-&#8216;, but also allows the list-clearing token (!) to be specified. If no filename is provided, &quot;.cvsignore&quot; is assumed. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>e</code> will exclude the merge-file name from the transfer; e.g. &quot;dir-merge,e .rules&quot; is like &quot;dir-merge .rules&quot; and &quot;- .rules&quot;. </p>
 </dd>
<dt>o</dt>
<dd> <p> An <code>n</code> specifies that the rules are not inherited by subdirectories. </p>
 </dd>
<dt>o</dt>
<dd> <p> A <code>w</code> specifies that the rules are word-split on whitespace instead of the normal line-splitting. This also turns off comments. Note: the space that separates the prefix from the rule is treated specially, so &quot;- foo + bar&quot; is parsed as two rules (assuming that prefix-parsing wasn&#8217;t also disabled). </p>
 </dd>
<dt>o</dt>
<dd> <p> You may also specify any of the modifiers for the &quot;+&quot; or &quot;-&quot; rules (above) in order to have the rules that are read in from the file default to having that modifier set (except for the <code>!</code> modifier, which would not be useful). For instance, &quot;merge,-/ .excl&quot; would treat the contents of .excl as absolute-path excludes, while &quot;dir-merge,s .filt&quot; and &quot;:sC&quot; would each make all their per-directory rules apply only on the sending side. If the merge rule specifies sides to affect (via the <code>s</code> or <code>r</code> modifier or both), then the rules in the file must not specify sides (via a modifier or a rule prefix such as <code>hide</code>). </p>
 </dd></dl>
<p> Per-directory rules are inherited in all subdirectories of the directory where the merge-file was found unless the &#8216;n&#8217; modifier was used. Each subdirectory&#8217;s rules are prefixed to the inherited per-directory rules from its parents, which gives the newest rules a higher priority than the inherited rules. The entire set of dir-merge rules are grouped together in the spot where the merge-file was specified, so it is possible to override dir-merge rules via a rule that got specified earlier in the list of global rules. When the list-clearing rule (&quot;!&quot;) is read from a per-directory file, it only clears the inherited rules for the current merge file. </p>
<p> Another way to prevent a single rule from a dir-merge file from being inherited is to anchor it with a leading slash. Anchored rules in a per-directory merge-file are relative to the merge-file&#8217;s directory, so a pattern &quot;/foo&quot; would only match the file &quot;foo&quot; in the directory where the dir-merge filter file was found. </p>
<p> Here&#8217;s an example filter file which you&#8217;d specify via <code>--filter=&quot;. file&quot;:</code> </p>
<dl>
<dd> <pre><code>merge /home/user/.global-filter
- *.gz
dir-merge .rules
+ *.[ch]
- *.o
- foo*
</code></pre>
 </dd></dl>
<p> This will merge the contents of the /home/user/.global-filter file at the start of the list and also turns the &quot;.rules&quot; filename into a per-directory filter file. All rules read in prior to the start of the directory scan follow the global anchoring rules (i.e. a leading slash matches at the root of the transfer). </p>
<p> If a per-directory merge-file is specified with a path that is a parent directory of the first transfer directory, rsync will scan all the parent dirs from that starting point to the transfer directory for the indicated per-directory file. For instance, here is a common filter (see <code>-F</code>): </p>
<dl>
<dd> <pre><code>--filter=': /.rsync-filter'
</code></pre>
 </dd></dl>
<p> That rule tells rsync to scan for the file .rsync-filter in all directories from the root down through the parent directory of the transfer prior to the start of the normal directory scan of the file in the directories that are sent as a part of the transfer. (Note: for an rsync daemon, the root is always the same as the module&#8217;s &quot;path&quot;.) </p>
<p> Some examples of this pre-scanning for per-directory files: </p>
<dl>
<dd> <pre><code>rsync -avF /src/path/ /dest/dir
rsync -av --filter=': ../../.rsync-filter' /src/path/ /dest/dir
rsync -av --filter=': .rsync-filter' /src/path/ /dest/dir
</code></pre>
 </dd></dl>
<p> The first two commands above will look for &quot;.rsync-filter&quot; in &quot;/&quot; and &quot;/src&quot; before the normal scan begins looking for the file in &quot;/src/path&quot; and its subdirectories. The last command avoids the parent-dir scan and only looks for the &quot;.rsync-filter&quot; files in each directory that is a part of the transfer. </p>
<p> If you want to include the contents of a &quot;.cvsignore&quot; in your patterns, you should use the rule &quot;:C&quot;, which creates a dir-merge of the .cvsignore file, but parsed in a CVS-compatible manner. You can use this to affect where the <code>--cvs-exclude</code> (<code>-C</code>) option&#8217;s inclusion of the per-directory .cvsignore file gets placed into your rules by putting the &quot;:C&quot; wherever you like in your filter rules. Without this, rsync would add the dir-merge rule for the .cvsignore file at the end of all your other rules (giving it a lower priority than your command-line rules). For example: </p>
<dl>
<dd> <pre><code>cat &lt;&lt;EOT | rsync -avC --filter='. -' a/ b
+ foo.o
:C
- *.old
EOT
rsync -avC --include=foo.o -f :C --exclude='*.old' a/ b
</code></pre>
 </dd></dl>
<p> Both of the above rsync commands are identical. Each one will merge all the per-directory .cvsignore rules in the middle of the list rather than at the end. This allows their dir-specific rules to supersede the rules that follow the :C instead of being subservient to all your rules. To affect the other CVS exclude rules (i.e. the default list of exclusions, the contents of $HOME/.cvsignore, and the value of $CVSIGNORE) you should omit the <code>-C</code> command-line option and instead insert a &quot;-C&quot; rule into your filter rules; e.g. &quot;<code>--filter=-C</code>&quot;. </p>
<h3>LIST-CLEARING FILTER RULE</h3>
<p> You can clear the current include/exclude list by using the &quot;!&quot; filter rule (as introduced in the FILTER RULES section above). The &quot;current&quot; list is either the global list of rules (if the rule is encountered while parsing the filter options) or a set of per-directory rules (which are inherited in their own sub-list, so a subdirectory can use this to clear out the parent&#8217;s rules). </p>
<h3>ANCHORING INCLUDE/EXCLUDE PATTERNS</h3>
<p> As mentioned earlier, global include/exclude patterns are anchored at the &quot;root of the transfer&quot; (as opposed to per-directory patterns, which are anchored at the merge-file&#8217;s directory). If you think of the transfer as a subtree of names that are being sent from sender to receiver, the transfer-root is where the tree starts to be duplicated in the destination directory. This root governs where patterns that start with a / match. </p>
<p> Because the matching is relative to the transfer-root, changing the trailing slash on a source path or changing your use of the <code>--relative</code> option affects the path you need to use in your matching (in addition to changing how much of the file tree is duplicated on the destination host). The following examples demonstrate this. </p>
<p> Let&#8217;s say that we want to match two source files, one with an absolute path of &quot;/home/me/foo/bar&quot;, and one with a path of &quot;/home/you/bar/baz&quot;. Here is how the various command choices differ for a 2-source transfer: </p>
<dl>
<dd> <pre><code>Example cmd: rsync -a /home/me /home/you /dest
+/- pattern: /me/foo/bar
+/- pattern: /you/bar/baz
Target file: /dest/me/foo/bar
Target file: /dest/you/bar/baz
</code></pre>
 </dd></dl>
<dl>
<dd> <pre><code>Example cmd: rsync -a /home/me/ /home/you/ /dest
+/- pattern: /foo/bar (note missing &quot;me&quot;)
+/- pattern: /bar/baz (note missing &quot;you&quot;)
Target file: /dest/foo/bar
Target file: /dest/bar/baz
</code></pre>
 </dd></dl>
<dl>
<dd> <pre><code>Example cmd: rsync -a --relative /home/me/ /home/you /dest
+/- pattern: /home/me/foo/bar (note full path)
+/- pattern: /home/you/bar/baz (ditto)
Target file: /dest/home/me/foo/bar
Target file: /dest/home/you/bar/baz
</code></pre>
 </dd></dl>
<dl>
<dd> <pre><code>Example cmd: cd /home; rsync -a --relative me/foo you/ /dest
+/- pattern: /me/foo/bar (starts at specified path)
+/- pattern: /you/bar/baz (ditto)
Target file: /dest/me/foo/bar
Target file: /dest/you/bar/baz
</code></pre>
 </dd></dl>
<p> The easiest way to see what name you should filter is to just look at the output when using <code>--verbose</code> and put a / in front of the name (use the <code>--dry-run</code> option if you&#8217;re not yet ready to copy any files). </p>
<h3>PER-DIRECTORY RULES AND DELETE</h3>
<p> Without a delete option, per-directory rules are only relevant on the sending side, so you can feel free to exclude the merge files themselves without affecting the transfer. To make this easy, the &#8216;e&#8217; modifier adds this exclude for you, as seen in these two equivalent commands: </p>
<dl>
<dd> <pre><code>rsync -av --filter=': .excl' --exclude=.excl host:src/dir /dest
rsync -av --filter=':e .excl' host:src/dir /dest
</code></pre>
 </dd></dl>
<p> However, if you want to do a delete on the receiving side AND you want some files to be excluded from being deleted, you&#8217;ll need to be sure that the receiving side knows what files to exclude. The easiest way is to include the per-directory merge files in the transfer and use <code>--delete-after</code>, because this ensures that the receiving side gets all the same exclude rules as the sending side before it tries to delete anything: </p>
<dl>
<dd> <pre><code>rsync -avF --delete-after host:src/dir /dest
</code></pre>
 </dd></dl>
<p> However, if the merge files are not a part of the transfer, you&#8217;ll need to either specify some global exclude rules (i.e. specified on the command line), or you&#8217;ll need to maintain your own per-directory merge files on the receiving side. An example of the first is this (assume that the remote .rules files exclude themselves): </p>
<dl>
<dd> <pre><code>rsync -av --filter=': .rules' --filter='. /my/extra.rules'
   --delete host:src/dir /dest
</code></pre>
 </dd></dl>
<p> In the above example the extra.rules file can affect both sides of the transfer, but (on the sending side) the rules are subservient to the rules merged from the .rules files because they were specified after the per-directory merge rule. </p>
<p> In one final example, the remote side is excluding the .rsync-filter files from the transfer, but we want to use our own .rsync-filter files to control what gets deleted on the receiving side. To do this we must specifically exclude the per-directory merge files (so that they don&#8217;t get deleted) and then put rules into the local files to control what else should not get deleted. Like one of these commands: </p>
<dl>
<dd> <pre><code>rsync -av --filter=':e /.rsync-filter' --delete \
    host:src/dir /dest
rsync -avFF --delete host:src/dir /dest
</code></pre>
 </dd></dl>
<h2>TRANSFER RULES</h2>
<p> In addition to the FILTER RULES that affect the recursive file scans that generate the file list on the sending and (when deleting) receiving sides, there are transfer rules. These rules affect which files the generator decides need to be transferred without the side effects of an exclude filter rule. Transfer rules affect only files and never directories. </p>
<p> Because a transfer rule does not affect what goes into the sender&#8217;s (and receiver&#8217;s) file list, it cannot have any effect on which files get deleted on the receiving side. For example, if the file &quot;foo&quot; is present in the sender&#8217;s list but its size is such that it is omitted due to a transfer rule, the receiving side does not request the file. However, its presence in the file list means that a delete pass will not remove a matching file named &quot;foo&quot; on the receiving side. On the other hand, a server-side exclude (hide) of the file &quot;foo&quot; leaves the file out of the server&#8217;s file list, and absent a receiver-side exclude (protect) the receiver will remove a matching file named &quot;foo&quot; if deletions are requested. </p>
<p> Given that the files are still in the sender&#8217;s file list, the <code>--prune-empty-dirs</code> option will not judge a directory as being empty even if it contains only files that the transfer rules omitted. </p>
<p> Similarly, a transfer rule does not have any extra effect on which files are deleted on the receiving side, so setting a maximum file size for the transfer does not prevent big files from being deleted. </p>
<p> Examples of transfer rules include the default &quot;quick check&quot; algorithm (which compares size &amp; modify time), the <code>--update</code> option, the <code>--max-size</code> option, the <code>--ignore-non-existing</code> option, and a few others. </p>
<h2>BATCH MODE</h2>
<p> Batch mode can be used to apply the same set of updates to many identical systems. Suppose one has a tree which is replicated on a number of hosts. Now suppose some changes have been made to this source tree and those changes need to be propagated to the other hosts. In order to do this using batch mode, rsync is run with the write-batch option to apply the changes made to the source tree to one of the destination trees. The write-batch option causes the rsync client to store in a &quot;batch file&quot; all the information needed to repeat this operation against other, identical destination trees. </p>
<p> Generating the batch file once saves having to perform the file status, checksum, and data block generation more than once when updating multiple destination trees. Multicast transport protocols can be used to transfer the batch update files in parallel to many hosts at once, instead of sending the same data to every host individually. </p>
<p> To apply the recorded changes to another destination tree, run rsync with the read-batch option, specifying the name of the same batch file, and the destination tree. Rsync updates the destination tree using the information stored in the batch file. </p>
<p> For your convenience, a script file is also created when the write-batch option is used: it will be named the same as the batch file with &quot;.sh&quot; appended. This script file contains a command-line suitable for updating a destination tree using the associated batch file. It can be executed using a Bourne (or Bourne-like) shell, optionally passing in an alternate destination tree pathname which is then used instead of the original destination path. This is useful when the destination tree path on the current host differs from the one used to create the batch file. </p>
<p> Examples: </p>
<dl>
<dd> <pre><code>$ rsync --write-batch=foo -a host:/source/dir/ /adest/dir/
$ scp foo* remote:
$ ssh remote ./foo.sh /bdest/dir/
</code></pre>
 </dd></dl>
<dl>
<dd> <pre><code>$ rsync --write-batch=foo -a /source/dir/ /adest/dir/
$ ssh remote rsync --read-batch=- -a /bdest/dir/ &lt;foo
</code></pre>
 </dd></dl>
<p> In these examples, rsync is used to update /adest/dir/ from /source/dir/ and the information to repeat this operation is stored in &quot;foo&quot; and &quot;foo.sh&quot;. The host &quot;remote&quot; is then updated with the batched data going into the directory /bdest/dir. The differences between the two examples reveals some of the flexibility you have in how you deal with batches: </p>
<dl>
<dt>o</dt>
<dd> <p> The first example shows that the initial copy doesn&#8217;t have to be local -- you can push or pull data to/from a remote host using either the remote-shell syntax or rsync daemon syntax, as desired. </p>
 </dd>
<dt>o</dt>
<dd> <p> The first example uses the created &quot;foo.sh&quot; file to get the right rsync options when running the read-batch command on the remote host. </p>
 </dd>
<dt>o</dt>
<dd> <p> The second example reads the batch data via standard input so that the batch file doesn&#8217;t need to be copied to the remote machine first. This example avoids the foo.sh script because it needed to use a modified <code>--read-batch</code> option, but you could edit the script file if you wished to make use of it (just be sure that no other option is trying to use standard input, such as the <code>--exclude-from=-</code> option). </p>
 </dd></dl>
<p> Caveats: </p>
<p> The read-batch option expects the destination tree that it is updating to be identical to the destination tree that was used to create the batch update fileset. When a difference between the destination trees is encountered the update might be discarded with a warning (if the file appears to be up-to-date already) or the file-update may be attempted and then, if the file fails to verify, the update discarded with an error. This means that it should be safe to re-run a read-batch operation if the command got interrupted. If you wish to force the batched-update to always be attempted regardless of the file&#8217;s size and date, use the <code>-I</code> option (when reading the batch). If an error occurs, the destination tree will probably be in a partially updated state. In that case, rsync can be used in its regular (non-batch) mode of operation to fix up the destination tree. </p>
<p> The rsync version used on all destinations must be at least as new as the one used to generate the batch file. Rsync will die with an error if the protocol version in the batch file is too new for the batch-reading rsync to handle. See also the <code>--protocol</code> option for a way to have the creating rsync generate a batch file that an older rsync can understand. (Note that batch files changed format in version 2.6.3, so mixing versions older than that with newer versions will not work.) </p>
<p> When reading a batch file, rsync will force the value of certain options to match the data in the batch file if you didn&#8217;t set them to the same as the batch-writing command. Other options can (and should) be changed. For instance <code>--write-batch</code> changes to <code>--read-batch</code>, <code>--files-from</code> is dropped, and the <code>--filter</code> / <code>--include</code> / <code>--exclude</code> options are not needed unless one of the <code>--delete</code> options is specified. </p>
<p> The code that creates the BATCH.sh file transforms any filter/include/exclude options into a single list that is appended as a &quot;here&quot; document to the shell script file. An advanced user can use this to modify the exclude list if a change in what gets deleted by <code>--delete</code> is desired. A normal user can ignore this detail and just use the shell script as an easy way to run the appropriate <code>--read-batch</code> command for the batched data. </p>
<p> The original batch mode in rsync was based on &quot;rsync+&quot;, but the latest version uses a new implementation. </p>
<h2>SYMBOLIC LINKS</h2>
<p> Three basic behaviors are possible when rsync encounters a symbolic link in the source directory. </p>
<p> By default, symbolic links are not transferred at all. A message &quot;skipping non-regular&quot; file is emitted for any symlinks that exist. </p>
<p> If <code>--links</code> is specified, then symlinks are added to the transfer (instead of being noisily ignored), and the default handling is to recreate them with the same target on the destination. Note that <code>--archive</code> implies <code>--links</code>. </p>
<p> If <code>--copy-links</code> is specified, then symlinks are &quot;collapsed&quot; by copying their referent, rather than the symlink. </p>
<p> Rsync can also distinguish &quot;safe&quot; and &quot;unsafe&quot; symbolic links. An example where this might be used is a web site mirror that wishes to ensure that the rsync module that is copied does not include symbolic links to <code>/etc/passwd</code> in the public section of the site. Using <code>--copy-unsafe-links</code> will cause any links to be copied as the file they point to on the destination. Using <code>--safe-links</code> will cause unsafe links to be omitted by the receiver. (Note that you must specify or imply <code>--links</code> for <code>--safe-links</code> to have any effect.) </p>
<p> Symbolic links are considered unsafe if they are absolute symlinks (start with <code>/</code>), empty, or if they contain enough &quot;..&quot; components to ascend from the top of the transfer. </p>
<p> Here&#8217;s a summary of how the symlink options are interpreted. The list is in order of precedence, so if your combination of options isn&#8217;t mentioned, use the first line that is a complete subset of your options: </p>
<dl>
<dt><code>--copy-links</code></dt>
<dd> <p> Turn all symlinks into normal files and directories (leaving no symlinks in the transfer for any other options to affect). </p>
 </dd>
<dt><code>--copy-dirlinks</code></dt>
<dd> <p> Turn just symlinks to directories into real directories, leaving all other symlinks to be handled as described below. </p>
 </dd>
<dt><code>--links --copy-unsafe-links</code></dt>
<dd> <p> Turn all unsafe symlinks into files and create all safe symlinks. </p>
 </dd>
<dt><code>--copy-unsafe-links</code></dt>
<dd> <p> Turn all unsafe symlinks into files, noisily skip all safe symlinks. </p>
 </dd>
<dt><code>--links --safe-links</code></dt>
<dd> <p> The receiver skips creating unsafe symlinks found in the transfer and creates the safe ones. </p>
 </dd>
<dt><code>--links</code></dt>
<dd> <p> Create all symlinks. </p>
 </dd></dl>
<p> For the effect of <code>--munge-links</code>, see the discussion in that option&#8217;s section. </p>
<p> Note that the <code>--keep-dirlinks</code> option does not effect symlinks in the transfer but instead affects how rsync treats a symlink to a directory that already exists on the receiving side. See that option&#8217;s section for a warning. </p>
<h2>DIAGNOSTICS</h2>
<p> Rsync occasionally produces error messages that may seem a little cryptic. The one that seems to cause the most confusion is &quot;protocol version mismatch -- is your shell clean?&quot;. </p>
<p> This message is usually caused by your startup scripts or remote shell facility producing unwanted garbage on the stream that rsync is using for its transport. The way to diagnose this problem is to run your remote shell like this: </p>
<dl>
<dd> <pre><code>ssh remotehost /bin/true &gt; out.dat
</code></pre>
 </dd></dl>
<p> then look at out.dat. If everything is working correctly then out.dat should be a zero length file. If you are getting the above error from rsync then you will probably find that out.dat contains some text or data. Look at the contents and try to work out what is producing it. The most common cause is incorrectly configured shell startup scripts (such as .cshrc or .profile) that contain output statements for non-interactive logins. </p>
<p> If you are having trouble debugging filter patterns, then try specifying the <code>-vv</code> option. At this level of verbosity rsync will show why each individual file is included or excluded. </p>
<h2>EXIT VALUES</h2>
<dl>
<dt>o</dt>
<dd> <p> <code>0</code> - Success </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>1</code> - Syntax or usage error </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>2</code> - Protocol incompatibility </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>3</code> - Errors selecting input/output files, dirs </p>
 </dd>
<dt>o</dt>
<dd>  </dd></dl>
<dl>
<dd>  </dd>
<dl>
<dt>o</dt>
<dd> <p> <code>4</code> - Requested action not supported. Either: </p>
<p> an attempt was made to manipulate 64-bit files on a platform that cannot support them </p>
 </dd>
<dt>o</dt>
<dd> <p> an option was specified that is supported by the client and not by the server </p>
 </dd></dl>
</dl>
<dl>
<dt>o</dt>
<dd> <p> <code>5</code> - Error starting client-server protocol </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>6</code> - Daemon unable to append to log-file </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>10</code> - Error in socket I/O </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>11</code> - Error in file I/O </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>12</code> - Error in rsync protocol data stream </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>13</code> - Errors with program diagnostics </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>14</code> - Error in IPC code </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>20</code> - Received SIGUSR1 or SIGINT </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>21</code> - Some error returned by <code>waitpid()</code> </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>22</code> - Error allocating core memory buffers </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>23</code> - Partial transfer due to error </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>24</code> - Partial transfer due to vanished source files </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>25</code> - The --max-delete limit stopped deletions </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>30</code> - Timeout in data send/receive </p>
 </dd>
<dt>o</dt>
<dd> <p> <code>35</code> - Timeout waiting for daemon connection </p>
 </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CVSIGNORE</code></dt>
<dd> <p> The CVSIGNORE environment variable supplements any ignore patterns in .cvsignore files. See the <code>--cvs-exclude</code> option for more details. </p>
 </dd>
<dt><code>RSYNC_ICONV</code></dt>
<dd> <p> Specify a default <code>--iconv</code> setting using this environment variable. First supported in 3.0.0. </p>
 </dd>
<dt><code>RSYNC_OLD_ARGS</code></dt>
<dd> <p> Specify a &quot;1&quot; if you want the <code>--old-args</code> option to be enabled by default, a &quot;2&quot; (or more) if you want it to be enabled in the repeated-option state, or a &quot;0&quot; to make sure that it is disabled by default. When this environment variable is set to a non-zero value, it supersedes the <code>RSYNC_PROTECT_ARGS</code> variable. </p>
 </dd>
<dd> <p> This variable is ignored if <code>--old-args</code>, <code>--no-old-args</code>, or <code>--secluded-args</code> is specified on the command line. </p>
 </dd>
<dd> <p> First supported in 3.2.4. </p>
 </dd>
<dt><code>RSYNC_PROTECT_ARGS</code></dt>
<dd> <p> Specify a non-zero numeric value if you want the <code>--secluded-args</code> option to be enabled by default, or a zero value to make sure that it is disabled by default. </p>
 </dd>
<dd> <p> This variable is ignored if <code>--secluded-args</code>, <code>--no-secluded-args</code>, or <code>--old-args</code> is specified on the command line. </p>
 </dd>
<dd> <p> First supported in 3.1.0. Starting in 3.2.4, this variable is ignored if <code>RSYNC_OLD_ARGS</code> is set to a non-zero value. </p>
 </dd>
<dt><code>RSYNC_RSH</code></dt>
<dd> <p> This environment variable allows you to override the default shell used as the transport for rsync. Command line options are permitted after the command name, just as in the <code>--rsh</code> (<code>-e</code>) option. </p>
 </dd>
<dt><code>RSYNC_PROXY</code></dt>
<dd> <p> This environment variable allows you to redirect your rsync client to use a web proxy when connecting to an rsync daemon. You should set <code>RSYNC_PROXY</code> to a hostname:port pair. </p>
 </dd>
<dt><code>RSYNC_PASSWORD</code></dt>
<dd> <p> This environment variable allows you to set the password for an rsync <code>daemon</code> connection, which avoids the password prompt. Note that this does <code>not</code> supply a password to a remote shell transport such as ssh (consult its documentation for how to do that). </p>
 </dd>
<dt><code>USER</code> or <code>LOGNAME</code></dt>
<dd> <p> The USER or LOGNAME environment variables are used to determine the default username sent to an rsync daemon. If neither is set, the username defaults to &quot;nobody&quot;. If both are set, <code>USER</code> takes precedence. </p>
 </dd>
<dt><code>RSYNC_PARTIAL_DIR</code></dt>
<dd> <p> This environment variable specifies the directory to use for a <code>--partial</code> transfer without implying that partial transfers be enabled. See the <code>--partial-dir</code> option for full details. </p>
 </dd>
<dt><code>RSYNC_COMPRESS_LIST</code></dt>
<dd> <p> This environment variable allows you to customize the negotiation of the compression algorithm by specifying an alternate order or a reduced list of names. Use the command <code>rsync --version</code> to see the available compression names. See the <code>--compress</code> option for full details. </p>
 </dd>
<dt><code>RSYNC_CHECKSUM_LIST</code></dt>
<dd> <p> This environment variable allows you to customize the negotiation of the checksum algorithm by specifying an alternate order or a reduced list of names. Use the command <code>rsync --version</code> to see the available checksum names. See the <code>--checksum-choice</code> option for full details. </p>
 </dd>
<dt><code>RSYNC_MAX_ALLOC</code></dt>
<dd> <p> This environment variable sets an allocation maximum as if you had used the <code>--max-alloc</code> option. </p>
 </dd>
<dt><code>RSYNC_PORT</code></dt>
<dd> <p> This environment variable is not read by rsync, but is instead set in its sub-environment when rsync is running the remote shell in combination with a daemon connection. This allows a script such as <code>rsync-ssl</code> to be able to know the port number that the user specified on the command line. </p>
 </dd>
<dt><code>HOME</code></dt>
<dd> <p> This environment variable is used to find the user&#8217;s default .cvsignore file. </p>
 </dd>
<dt><code>RSYNC_CONNECT_PROG</code></dt>
<dd> <p> This environment variable is mainly used in debug setups to set the program to use when making a daemon connection. See CONNECTING TO AN RSYNC DAEMON for full details. </p>
 </dd>
<dt><code>RSYNC_SHELL</code></dt>
<dd> <p> This environment variable is mainly used in debug setups to set the program to use to run the program specified by <code>RSYNC_CONNECT_PROG</code>. See CONNECTING TO AN RSYNC DAEMON for full details. </p>
 </dd></dl>
<h2>FILES</h2>
<p> /etc/rsyncd.conf or rsyncd.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rsync-ssl/">rsync-ssl</a></code>(1), <code>rsyncd.conf</code>(5), <code><a href="/docs/linux/man/1-rrsync/">rrsync</a></code>(1) </p>
<h2>BUGS</h2>
<dl>
<dt>o</dt>
<dd> <p> Times are transferred as *nix time_t values. </p>
 </dd>
<dt>o</dt>
<dd> <p> When transferring to FAT filesystems rsync may re-sync unmodified files. See the comments on the <code>--modify-window</code> option. </p>
 </dd>
<dt>o</dt>
<dd> <p> File permissions, devices, etc. are transferred as native numerical values. </p>
 </dd>
<dt>o</dt>
<dd> <p> See also the comments on the <code>--delete</code> option. </p>
 </dd></dl>
<p> Please report bugs! See the web site at <a rel="nofollow" href="https://rsync.samba.org/.">https://rsync.samba.org/.</a> </p>
<h2>VERSION</h2>
<p> This manpage is current for version 3.2.7 of rsync. </p>
<h2>INTERNAL OPTIONS</h2>
<p> The options <code>--server</code> and <code>--sender</code> are used internally by rsync, and should never be typed by a user under normal circumstances. Some awareness of these options may be needed in certain scenarios, such as when setting up a login that can only run an rsync command. For instance, the support directory of the rsync distribution has an example script named rrsync (for restricted rsync) that can be used with a restricted ssh login. </p>
<h2>CREDITS</h2>
<p> Rsync is distributed under the GNU General Public License. See the file COPYING for details. </p>
<p> An rsync web site is available at <a rel="nofollow" href="https://rsync.samba.org/.">https://rsync.samba.org/.</a> The site includes an FAQ-O-Matic which may cover questions unanswered by this manual page. </p>
<p> The rsync github project is <a rel="nofollow" href="https://github.com/WayneD/rsync.">https://github.com/WayneD/rsync.</a> </p>
<p> We would be delighted to hear from you if you like this program. Please contact the mailing-list at rsync [at] lists.samba.org. </p>
<p> This program uses the excellent zlib compression library written by Jean-loup Gailly and Mark Adler. </p>
<h2>THANKS</h2>
<p> Special thanks go out to: John Van Essen, Matt McCutchen, Wesley W. Terpstra, David Dykstra, Jos Backus, Sebastian Krahmer, Martin Pool, and our gone-but-not-forgotten compadre, J.W. Schultz. </p>
<p> Thanks also to Richard Brent, Brendan Mackay, Bill Waite, Stephen Rothwell and David Bell. I&#8217;ve probably missed some people, my apologies if I have. </p>
<h2>AUTHOR</h2>
<p> Rsync was originally written by Andrew Tridgell and Paul Mackerras. Many people have later contributed to it. It is currently maintained by Wayne Davison. </p>
<p> Mailing lists for support and development are available at <a rel="nofollow" href="https://lists.samba.org/.">https://lists.samba.org/.</a> </p>
