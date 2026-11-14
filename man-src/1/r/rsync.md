---
title: "rsync(1)"
name: "rsync"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsync/"
description: "rsync – a fast, versatile, remote (and local) file-copying tool"
---

<h2 class="name">NAME</h2>
<p> rsync &#8211; a fast, versatile, remote (and local) file-copying tool</p>
<h2>SYNOPSIS</h2>
<pre><code>
Local : rsync[OPTION...] SRC...[DEST] Access via remote shell : Pull : rsync[OPTION...][USER @] HOST : SRC...[DEST] Push : rsync[OPTION...] SRC...[USER @] HOST : DEST
                                                                                                                                                                      Access via rsync daemon : Pull : rsync[OPTION...][USER @] HOST::SRC...[DEST] rsync[OPTION...] rsync : //[USER@]HOST[:PORT]/SRC... [DEST]
                                                                                                                                                                                                                                                                            Push : rsync[OPTION...] SRC...[USER @] HOST::DEST
                                                                                                                                                                                                                                                                                       rsync[OPTION...] SRC... rsync: //[USER@]HOST[:PORT]/DEST)
</code></pre>
<p> Usages with just one SRC arg and no DEST arg will list the source files instead of copying. </p>
<p> The online version of this manpage (that includes cross-linking of topics) is available at <a rel="nofollow" href="https://download.samba.org/pub/rsync/rsync.1.">https://download.samba.org/pub/rsync/rsync.1.</a> </p>
<h2>DESCRIPTION</h2>
<p> Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from another host over any remote shell, or to/from a remote rsync daemon. It offers a large number of options that control every aspect of its behavior and permit very flexible specification of the set of files to be copied. It is famous for its delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the differences between the source files and the existing files in the destination. Rsync is widely used for backups and mirroring and as an improved copy command for everyday use. </p>
<p> Rsync finds files that need to be transferred using a &quot;quick check&quot; algorithm (by default) that looks for files that have changed in size or in last-modified time. Any changes in the other preserved attributes (as requested by options) are made on the destination file directly when the quick check indicates that the file&#8217;s data does not need to be updated. </p>
<p> Some of the additional features of rsync are: </p>
<dl>
<dt>o</p>
<dd> support for copying links, devices, owners, groups, and permissions</p>
<dt>o</p>
<dd> exclude and exclude-from options similar to GNU tar</p>
<dt>o</p>
<dd> a CVS exclude mode for ignoring the same files that CVS would ignore</p>
<dt>o</p>
<dd> can use any transparent remote shell, including ssh or rsh</p>
<dt>o</p>
<dd> does not require super-user privileges</p>
<dt>o</p>
<dd> pipelining of file transfers to minimize latency costs</p>
<dt>o</p>
<dd> support for anonymous or authenticated rsync daemons (ideal for mirroring)</dl>
<h2>GENERAL</h2>
<p> Rsync copies files either to or from a remote host, or locally on the current host (it does not support copying files between two remote hosts). </p>
<p> There are two different ways for rsync to contact a remote system: using a remote-shell program as the transport (such as ssh or rsh) or contacting an rsync daemon directly via TCP. The remote-shell transport is used whenever the source or destination path contains a single colon (:) separator after a host specification. Contacting an rsync daemon directly happens when the source or destination path contains a double colon (::) separator after a host specification, OR when an rsync:// URL is specified (see also the USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION section for an exception to this latter rule). </p>
<p> As a special case, if a single source arg is specified without a destination, the files are listed in an output format similar to &quot;<code>ls -l</code>&quot;. </p>
<p> As expected, if neither the source or destination path specify a remote host, the copy occurs locally (see also the <code>&#8211;list-only</code> option). </p>
<p> Rsync refers to the local side as the client and the remote side as the server. Don&#8217;t confuse server with an rsync daemon. A daemon is always a server, but a server can be either a daemon or a remote-shell spawned process. </p>
<h2>SETUP</h2>
<p> See the file README.md for installation instructions. </p>
<p> Once installed, you can use rsync to any machine that you can access via a remote shell (as well as some that you can access using the rsync daemon-mode protocol). For remote transfers, a modern rsync uses ssh for its communications, but it may have been configured to use a different remote shell by default, such as rsh or remsh. </p>
<p> You can also specify any remote shell you like, either by using the <code>-e</code> command line option, or by setting the <code>RSYNC_RSH</code> environment variable. </p>
<p> Note that rsync must be installed on both the source and destination machines. </p>
<h2>USAGE</h2>
<p> You use rsync in the same way you use rcp. You must specify a source and a destination, one of which may be remote. </p>
<p> Perhaps the best way to explain the syntax is with some examples:</p>
<dl>
<dt>
<dd>
<pre>
rsync -t *.c foo:src/
</pre>
</dl>
<p> This would transfer all files matching the pattern <code>*.c</code> from the current directory to the directory src on the machine foo. If any of the files already exist on the remote system then the rsync remote-update protocol is used to update the file by sending only the differences in the data. Note that the expansion of wildcards on the command-line (<code>*.c</code>) into a list of files is handled by the shell before it runs rsync and not by rsync itself (exactly the same as all other Posix-style programs).</p>
<dl>
<dt>
<dd>
<pre>
rsync -avz foo:src/bar /data/tmp
</pre>
</dl>
<p> This would recursively transfer all files from the directory src/bar on the machine foo into the /data/tmp/bar directory on the local machine. The files are transferred in archive mode, which ensures that symbolic links, devices, attributes, permissions, ownerships, etc. are preserved in the transfer. Additionally, compression will be used to reduce the size of data portions of the transfer.</p>
<dl>
<dt>
<dd>
<pre>
rsync -avz foo:src/bar/ /data/tmp
</pre>
</dl>
<p> A trailing slash on the source changes this behavior to avoid creating an additional directory level at the destination. You can think of a trailing / on a source as meaning &quot;copy the contents of this directory&quot; as opposed to &quot;copy the directory by name&quot;, but in both cases the attributes of the containing directory are transferred to the containing directory on the destination. In other words, each of the following commands copies the files in the same way, including their setting of the attributes of /dest/foo:</p>
<dl>
<dt>
<dd>
<pre>
rsync -av /src/foo /dest
rsync -av /src/foo/ /dest/foo
</pre>
</dl>
<p> Note also that host and module references don&#8217;t require a trailing slash to copy the contents of the default directory. For example, both of these copy the remote directory&#8217;s contents into &quot;/dest&quot;:</p>
<dl>
<dt>
<dd>
<pre>
rsync -av host: /dest
rsync -av host::module /dest
</pre>
</dl>
<p> You can also use rsync in local-only mode, where both the source and destination don&#8217;t have a &#8216;:&#8217; in the name. In this case it behaves like an improved copy command. </p>
<p> Finally, you can list all the (listable) modules available from a particular rsync daemon by leaving off the module name:</p>
<dl>
<dt>
<dd>
<pre>
rsync somehost.mydomain.com::
</pre>
</dl>
<h2>COPYING TO A DIFFERENT NAME</h2>
<p> When you want to copy a directory to a different name, use a trailing slash on the source directory to put the contents of the directory into any destination directory you like:</p>
<dl>
<dt>
<dd>
<pre>
rsync -ai foo/ bar/
</pre>
</dl>
<p> Rsync also has the ability to customize a destination file&#8217;s name when copying a single item. The rules for this are: </p>
<dl>
<dt>o</p>
<dd> The transfer list must consist of a single item (either a file or an empty directory)</p>
<dt>o</p>
<dd> The final element of the destination path must not exist as a directory</p>
<dt>o</p>
<dd> The destination path must not have been specified with a trailing slash</dl>
<p> Under those circumstances, rsync will set the name of the destination&#8217;s single item to the last element of the destination path. Keep in mind that it is best to only use this idiom when copying a file and use the above trailing-slash idiom when copying a directory. </p>
<p> The following example copies the <code>foo.c</code> file as <code>bar.c</code> in the <code>save</code> dir (assuming that <code>bar.c</code> isn&#8217;t a directory):</p>
<dl>
<dt>
<dd>
<pre>
rsync -ai src/foo.c save/bar.c
</pre>
</dl>
<p> The single-item copy rule might accidentally bite you if you unknowingly copy a single item and specify a destination dir that doesn&#8217;t exist (without using a trailing slash). For example, if <code>src/*.c</code> matches one file and <code>save/dir</code> doesn&#8217;t exist, this will confuse you by naming the destination file <code>save/dir</code>:</p>
<dl>
<dt>
<dd>
<pre>
rsync -ai src/*.c save/dir
</pre>
</dl>
<p> To prevent such an accident, either make sure the destination dir exists or specify the destination path with a trailing slash:</p>
<dl>
<dt>
<dd>
<pre>
rsync -ai src/*.c save/dir/
</pre>
</dl>
<h2>SORTED TRANSFER ORDER</h2>
<p> Rsync always sorts the specified filenames into its internal transfer list. This handles the merging together of the contents of identically named directories, makes it easy to remove duplicate filenames. It can, however, confuse someone when the files are transferred in a different order than what was given on the command-line. </p>
<p> If you need a particular file to be transferred prior to another, either separate the files into different rsync calls, or consider using <code>&#8211;delay-updates</code> (which doesn&#8217;t affect the sorted transfer order, but does make the final file-updating phase happen much more rapidly). </p>
<h2>MULTI-HOST SECURITY</h2>
<p> Rsync takes steps to ensure that the file requests that are shared in a transfer are protected against various security issues. Most of the potential problems arise on the receiving side where rsync takes steps to ensure that the list of files being transferred remains within the bounds of what was requested. </p>
<p> Toward this end, rsync 3.1.2 and later have aborted when a file list contains an absolute or relative path that tries to escape out of the top of the transfer. Also, beginning with version 3.2.5, rsync does two more safety checks of the file list to (1) ensure that no extra source arguments were added into the transfer other than those that the client requested and (2) ensure that the file list obeys the exclude rules that were sent to the sender. </p>
<p> For those that don&#8217;t yet have a 3.2.5 client rsync (or those that want to be extra careful), it is safest to do a copy into a dedicated destination directory for the remote files when you don&#8217;t trust the remote host. For example, instead of doing an rsync copy into your home directory:</p>
<dl>
<dt>
<dd>
<pre>
rsync -aiv host1:dir1 ~
</pre>
</dl>
<p> Dedicate a &quot;host1-files&quot; dir to the remote content:</p>
<dl>
<dt>
<dd>
<pre>
rsync -aiv host1:dir1 ~/host1-files
</pre>
</dl>
<p> See the <code>&#8211;trust-sender</code> option for additional details. </p>
<p> CAUTION: it is not particularly safe to use rsync to copy files from a case-preserving filesystem to a case-ignoring filesystem. If you must perform such a copy, you should either disable symlinks via <code>&#8211;no-links</code> or enable the munging of symlinks via <code>&#8211;munge-links</code> (and make sure you use the right local or remote option). This will prevent rsync from doing potentially dangerous things if a symlink name overlaps with a file or directory. It does not, however, ensure that you get a full copy of all the files (since that may not be possible when the names overlap). A potentially better solution is to list all the source files and create a safe list of filenames that you pass to the <code>&#8211;files-from</code> option. Any files that conflict in name would need to be copied to different destination directories using more than one copy. </p>
<p> While a copy of a case-ignoring filesystem to a case-ignoring filesystem can work out fairly well, if no <code>&#8211;delete-during</code> or <code>&#8211;delete-before</code> option is active, rsync can potentially update an existing file on the receiveing side without noticing that the upper-/lower-case of the filename should be changed to match the sender. </p>
<h2>ADVANCED USAGE</h2>
<p> The syntax for requesting multiple files from a remote host is done by specifying additional remote-host args in the same style as the first, or with the hostname omitted. For instance, all these work:</p>
<dl>
<dt>
<dd>
<p>rsync &#8211; aiv host : file1 : file2 host : file{3, 4} / dest / rsync &#8211; aiv host::modname / file{1, 2} host::modname / extra / dest / rsync &#8211; aiv host::modname / first ::extra &#8211; file{1, 2} / dest /
</dl>
<p> Note that a daemon connection only supports accessing one module per copy command, so if the start of a follow-up path doesn&#8217;t begin with the modname of the first path, it is assumed to be a path in the module (such as the extra-file1 &amp; extra-file2 that are grabbed above). </p>
<p> Really old versions of rsync (2.6.9 and before) only allowed specifying one remote-source arg, so some people have instead relied on the remote-shell performing space splitting to break up an arg into multiple paths. Such unintuitive behavior is no longer supported by default (though you can request it, as described below). </p>
<p> Starting in 3.2.4, filenames are passed to a remote shell in such a way as to preserve the characters you give it. Thus, if you ask for a file with spaces in the name, that&#8217;s what the remote rsync looks for:</p>
<dl>
<dt>
<dd>
<pre>
rsync -aiv host:'a simple file.pdf' /dest/
</pre>
</dl>
<p> If you use scripts that have been written to manually apply extra quoting to the remote rsync args (or to require remote arg splitting), you can ask rsync to let your script handle the extra escaping. This is done by either adding the <code>&#8211;old-args</code> option to the rsync runs in the script (which requires a new rsync) or exporting RSYNC_OLD_ARGS=1 and RSYNC_PROTECT_ARGS=0 (which works with old or new rsync versions). </p>
<h2>CONNECTING TO AN RSYNC DAEMON</h2>
<p> It is also possible to use rsync without a remote shell as the transport. In this case you will directly connect to a remote rsync daemon, typically using TCP port 873. (This obviously requires the daemon to be running on the remote system, so refer to the STARTING AN RSYNC DAEMON TO ACCEPT CONNECTIONS section below for information on that.) </p>
<p> Using rsync in this way is the same as using it with a remote shell except that: </p>
<dl>
<dt>o</p>
<dd> Use either double-colon syntax or rsync:// URL syntax instead of the single-colon (remote shell) syntax.</p>
<dt>o</p>
<dd> The first element of the &quot;path&quot; is actually a module name.</p>
<dt>o</p>
<dd> Additional remote source args can use an abbreviated syntax that omits the hostname and/or the module name, as discussed in ADVANCED USAGE.</p>
<dt>o</p>
<dd> The remote daemon may print a &quot;message of the day&quot; when you connect.</p>
<dt>o</p>
<dd> If you specify only the host (with no module or path) then a list of accessible modules on the daemon is output.</p>
<dt>o</p>
<dd> If you specify a remote source path but no destination, a listing of the matching files on the remote daemon is output.</p>
<dt>o</p>
<dd> The <code>&#8211;rsh</code> (<code>-e</code>) option must be omitted to avoid changing the connection style from using a socket connection to USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION.</dl>
<p> An example that copies all the files in a remote module named &quot;src&quot;:</p>
<dl>
<dt>
<dd>
<pre>
rsync -av host::src /dest
</pre>
</dl>
<p> Some modules on the remote daemon may require authentication. If so, you will receive a password prompt when you connect. You can avoid the password prompt by setting the environment variable <code>RSYNC_PASSWORD</code> to the password you want to use or using the <code>&#8211;password-file</code> option. This may be useful when scripting rsync. </p>
<p> WARNING: On some systems environment variables are visible to all users. On those systems using <code>&#8211;password-file</code> is recommended. </p>
<p> You may establish the connection via a web proxy by setting the environment variable <code>RSYNC_PROXY</code> to a hostname:port pair pointing to your web proxy. Note that your web proxy&#8217;s configuration must support proxy connections to port 873. </p>
<p> You may also establish a daemon connection using a program as a proxy by setting the environment variable <code>RSYNC_CONNECT_PROG</code> to the commands you wish to run in place of making a direct socket connection. The string may contain the escape &quot;%H&quot; to represent the hostname specified in the rsync command (so use &quot;%%&quot; if you need a single &quot;%&quot; in your string). For example:</p>
<dl>
<dt>
<dd>
<pre>
export RSYNC_CONNECT_PROG='ssh proxyhost nc %H 873'
rsync -av targethost1::module/src/ /dest/
rsync -av <a href="rsync://targethost2/module/src/">rsync://targethost2/module/src/</a> /dest/
</pre>
</dl>
<p> The command specified above uses ssh to run nc (netcat) on a proxyhost, which forwards all data to port 873 (the rsync daemon) on the targethost (%H). </p>
<p> Note also that if the <code>RSYNC_SHELL</code> environment variable is set, that program will be used to run the <code>RSYNC_CONNECT_PROG</code> command instead of using the default shell of the <code>system()</code> call. </p>
<h2>USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION</h2>
<p> It is sometimes useful to use various features of an rsync daemon (such as named modules) without actually allowing any new socket connections into a system (other than what is already required to allow remote-shell access). Rsync supports connecting to a host using a remote shell and then spawning a single-use &quot;daemon&quot; server that expects to read its config file in the home dir of the remote user. This can be useful if you want to encrypt a daemon-style transfer&#8217;s data, but since the daemon is started up fresh by the remote user, you may not be able to use features such as chroot or change the uid used by the daemon. (For another way to encrypt a daemon transfer, consider using ssh to tunnel a local port to a remote machine and configure a normal rsync daemon on that remote host to only allow connections from &quot;localhost&quot;.) </p>
<p> From the user&#8217;s perspective, a daemon transfer via a remote-shell connection uses nearly the same command-line syntax as a normal rsync-daemon transfer, with the only exception being that you must explicitly set the remote shell program on the command-line with the <code>&#8211;rsh=COMMAND</code> option. (Setting the RSYNC_RSH in the environment will not turn on this functionality.) For example:</p>
<dl>
<dt>
<dd>
<pre>
rsync -av --rsh=ssh host::module /dest
</pre>
</dl>
<p> If you need to specify a different remote-shell user, keep in mind that the user@ prefix in front of the host is specifying the rsync-user value (for a module that requires user-based authentication). This means that you must give the &#8216;-l user&#8217; option to ssh when specifying the remote-shell, as in this example that uses the short version of the <code>&#8211;rsh</code> option:</p>
<dl>
<dt>
<dd>
<pre>
rsync -av -e &quot;ssh -l ssh-user&quot; rsync-user [at] host::module /dest
</pre>
</dl>
<p> The &quot;ssh-user&quot; will be used at the ssh level; the &quot;rsync-user&quot; will be used to log-in to the &quot;module&quot;. </p>
<p> In this setup, the daemon is started by the ssh command that is accessing the system (which can be forced via the <code>~/.ssh/authorized_keys</code> file, if desired). However, when accessing a daemon directly, it needs to be started beforehand. </p>
<h2>STARTING AN RSYNC DAEMON TO ACCEPT CONNECTIONS</h2>
<p> In order to connect to an rsync daemon, the remote system needs to have a daemon already running (or it needs to have configured something like inetd to spawn an rsync daemon for incoming connections on a particular port). For full information on how to start a daemon that will handling incoming socket connections, see the <code><a href="/docs/linux/man/5-rsyncd-conf/">rsyncd.conf</a></code>(5) manpage &#8212; that is the config file for the daemon, and it contains the full details for how to run the daemon (including stand-alone and inetd configurations). </p>
<p> If you&#8217;re using one of the remote-shell transports for the transfer, there is no need to manually start an rsync daemon. </p>
<h2>EXAMPLES</h2>
<p> Here are some examples of how rsync can be used. </p>
<p> To backup a home directory, which consists of large MS Word files and mail folders, a per-user cron job can be used that runs this each day:</p>
<dl>
<dt>
<dd>
<pre>
rsync -aiz . bkhost:backup/joe/
</pre>
</dl>
<p> To move some files from a remote host to the local host, you could run:</p>
<dl>
<dt>
<dd>
<pre>
rsync -aiv --remove-source-files rhost:/tmp/{file1,file2}.c ~/src/
</pre>
</dl>
<h2>OPTION SUMMARY</h2>
<p> Here is a short summary of the options available in rsync. Each option also has its own detailed description later in this manpage. </p>
<p>&#8211;verbose, -v            increase verbosity<br />
&#8211;info=FLAGS             fine-grained informational verbosity<br />
&#8211;debug=FLAGS            fine-grained debug verbosity<br />
&#8211;stderr=e|a|c           change stderr output mode (default: errors)<br />
&#8211;quiet, -q              suppress non-error messages<br />
&#8211;no-motd                suppress daemon-mode MOTD<br />
&#8211;checksum, -c           skip based on checksum, not mod-time &amp; size<br />
&#8211;archive, -a            archive mode is -rlptgoD (no -A,-X,-U,-N,-H)<br />
&#8211;no-OPTION              turn off an implied OPTION (e.g. &#8211;no-D)<br />
&#8211;recursive, -r          recurse into directories<br />
&#8211;relative, -R           use relative path names<br />
&#8211;no-implied-dirs        don&#8217;t send implied dirs with &#8211;relative<br />
&#8211;backup, -b             make backups (see &#8211;suffix &amp; &#8211;backup-dir)<br />
&#8211;backup-dir=DIR         make backups into hierarchy based in DIR<br />
&#8211;suffix=SUFFIX          backup suffix (default ~ w/o &#8211;backup-dir)<br />
&#8211;update, -u             skip files that are newer on the receiver<br />
&#8211;inplace                update destination files in-place<br />
&#8211;append                 append data onto shorter files<br />
&#8211;append-verify          &#8211;append w/old data in file checksum<br />
&#8211;dirs, -d               transfer directories without recursing<br />
&#8211;old-dirs, &#8211;old-d      works like &#8211;dirs when talking to old rsync<br />
&#8211;mkpath                 create destination&#8217;s missing path components<br />
&#8211;links, -l              copy symlinks as symlinks<br />
&#8211;copy-links, -L         transform symlink into referent file/dir<br />
&#8211;copy-unsafe-links      only &#8220;unsafe&#8221; symlinks are transformed<br />
&#8211;safe-links             ignore symlinks that point outside the tree<br />
&#8211;munge-links            munge symlinks to make them safe &amp; unusable<br />
&#8211;copy-dirlinks, -k      transform symlink to dir into referent dir<br />
&#8211;keep-dirlinks, -K      treat symlinked dir on receiver as dir<br />
&#8211;hard-links, -H         preserve hard links<br />
&#8211;perms, -p              preserve permissions<br />
&#8211;executability, -E      preserve executability<br />
&#8211;chmod=CHMOD            affect file and/or directory permissions<br />
&#8211;acls, -A               preserve ACLs (implies &#8211;perms)<br />
&#8211;xattrs, -X             preserve extended attributes<br />
&#8211;owner, -o              preserve owner (super-user only)<br />
&#8211;group, -g              preserve group<br />
&#8211;devices                preserve device files (super-user only)<br />
&#8211;copy-devices           copy device contents as a regular file<br />
&#8211;write-devices          write to devices as files (implies &#8211;inplace)<br />
&#8211;specials               preserve special files<br />
-D                       same as &#8211;devices &#8211;specials<br />
&#8211;times, -t              preserve modification times<br />
&#8211;atimes, -U             preserve access (use) times<br />
&#8211;open-noatime           avoid changing the atime on opened files<br />
&#8211;crtimes, -N            preserve create times (newness)<br />
&#8211;omit-dir-times, -O     omit directories from &#8211;times<br />
&#8211;omit-link-times, -J    omit symlinks from &#8211;times<br />
&#8211;super                  receiver attempts super-user activities<br />
&#8211;fake-super             store/recover privileged attrs using xattrs<br />
&#8211;sparse, -S             turn sequences of nulls into sparse blocks<br />
&#8211;preallocate            allocate dest files before writing them<br />
&#8211;dry-run, -n            perform a trial run with no changes made<br />
&#8211;whole-file, -W         copy files whole (w/o delta-xfer algorithm)<br />
&#8211;checksum-choice=STR    choose the checksum algorithm (aka &#8211;cc)<br />
&#8211;one-file-system, -x    don&#8217;t cross filesystem boundaries<br />
&#8211;block-size=SIZE, -B    force a fixed checksum block-size<br />
&#8211;rsh=COMMAND, -e        specify the remote shell to use<br />
&#8211;rsync-path=PROGRAM     specify the rsync to run on remote machine<br />
&#8211;existing               skip creating new files on receiver<br />
&#8211;ignore-existing        skip updating files that exist on receiver<br />
&#8211;remove-source-files    sender removes synchronized files (non-dir)<br />
&#8211;del                    an alias for &#8211;delete-during<br />
&#8211;delete                 delete extraneous files from dest dirs<br />
&#8211;delete-before          receiver deletes before xfer, not during<br />
&#8211;delete-during          receiver deletes during the transfer<br />
&#8211;delete-delay           find deletions during, delete after<br />
&#8211;delete-after           receiver deletes after transfer, not during<br />
&#8211;delete-excluded        also delete excluded files from dest dirs<br />
&#8211;ignore-missing-args    ignore missing source args without error<br />
&#8211;delete-missing-args    delete missing source args from destination<br />
&#8211;ignore-errors          delete even if there are I/O errors<br />
&#8211;force                  force deletion of dirs even if not empty<br />
&#8211;max-delete=NUM         don&#8217;t delete more than NUM files<br />
&#8211;max-size=SIZE          don&#8217;t transfer any file larger than SIZE<br />
&#8211;min-size=SIZE          don&#8217;t transfer any file smaller than SIZE<br />
&#8211;max-alloc=SIZE         change a limit relating to memory alloc<br />
&#8211;partial                keep partially transferred files<br />
&#8211;partial-dir=DIR        put a partially transferred file into DIR<br />
&#8211;delay-updates          put all updated files into place at end<br />
&#8211;prune-empty-dirs, -m   prune empty directory chains from file-list<br />
&#8211;numeric-ids            don&#8217;t map uid/gid values by user/group name<br />
&#8211;usermap=STRING         custom username mapping<br />
&#8211;groupmap=STRING        custom groupname mapping<br />
&#8211;chown=USER:GROUP       simple username/groupname mapping<br />
&#8211;timeout=SECONDS        set I/O timeout in seconds<br />
&#8211;contimeout=SECONDS     set daemon connection timeout in seconds<br />
&#8211;ignore-times, -I       don&#8217;t skip files that match size and time<br />
&#8211;size-only              skip files that match in size<br />
&#8211;modify-window=NUM, -@  set the accuracy for mod-time comparisons<br />
&#8211;temp-dir=DIR, -T       create temporary files in directory DIR<br />
&#8211;fuzzy, -y              find similar file for basis if no dest file<br />
&#8211;compare-dest=DIR       also compare destination files relative to DIR<br />
&#8211;copy-dest=DIR          &#8230; and include copies of unchanged files<br />
&#8211;link-dest=DIR          hardlink to files in DIR when unchanged<br />
&#8211;compress, -z           compress file data during the transfer<br />
&#8211;compress-choice=STR    choose the compression algorithm (aka &#8211;zc)<br />
&#8211;compress-level=NUM     explicitly set compression level (aka &#8211;zl)<br />
&#8211;skip-compress=LIST     skip compressing files with suffix in LIST<br />
&#8211;cvs-exclude, -C        auto-ignore files in the same way CVS does<br />
&#8211;filter=RULE, -f        add a file-filtering RULE<br />
-F                       same as &#8211;filter=&#8217;dir-merge /.rsync-filter&#8217;<br />
                         repeated: &#8211;filter=&#8217;- .rsync-filter&#8217;<br />
&#8211;exclude=PATTERN        exclude files matching PATTERN<br />
&#8211;exclude-from=FILE      read exclude patterns from FILE<br />
&#8211;include=PATTERN        don&#8217;t exclude files matching PATTERN<br />
&#8211;include-from=FILE      read include patterns from FILE<br />
&#8211;files-from=FILE        read list of source-file names from FILE<br />
&#8211;from0, -0              all *-from/filter files are delimited by 0s<br />
&#8211;old-args               disable the modern arg-protection idiom<br />
&#8211;secluded-args, -s      use the protocol to safely send the args<br />
&#8211;trust-sender           trust the remote sender&#8217;s file list<br />
&#8211;copy-as=USER[:GROUP]   specify user &amp; optional group for the copy<br />
&#8211;address=ADDRESS        bind address for outgoing socket to daemon<br />
&#8211;port=PORT              specify double-colon alternate port number<br />
&#8211;sockopts=OPTIONS       specify custom TCP options<br />
&#8211;blocking-io            use blocking I/O for the remote shell<br />
&#8211;outbuf=N|L|B           set out buffering to None, Line, or Block<br />
&#8211;stats                  give some file-transfer stats<br />
&#8211;8-bit-output, -8       leave high-bit chars unescaped in output<br />
&#8211;human-readable, -h     output numbers in a human-readable format<br />
&#8211;progress               show progress during transfer<br />
-P                       same as &#8211;partial &#8211;progress<br />
&#8211;itemize-changes, -i    output a change-summary for all updates<br />
&#8211;remote-option=OPT, -M  send OPTION to the remote side only<br />
&#8211;out-format=FORMAT      output updates using the specified FORMAT<br />
&#8211;log-file=FILE          log what we&#8217;re doing to the specified FILE<br />
&#8211;log-file-format=FMT    log updates using the specified FMT<br />
&#8211;password-file=FILE     read daemon-access password from FILE<br />
&#8211;early-input=FILE       use FILE for daemon&#8217;s early exec input<br />
&#8211;list-only              list the files instead of copying them<br />
&#8211;bwlimit=RATE           limit socket I/O bandwidth<br />
&#8211;stop-after=MINS        Stop rsync after MINS minutes have elapsed<br />
&#8211;stop-at=y-m-dTh:m      Stop rsync at the specified point in time<br />
&#8211;fsync                  fsync every written file<br />
&#8211;write-batch=FILE       write a batched update to FILE<br />
&#8211;only-write-batch=FILE  like &#8211;write-batch but w/o updating dest<br />
&#8211;read-batch=FILE        read a batched update from FILE<br />
&#8211;protocol=NUM           force an older protocol version to be used<br />
&#8211;iconv=CONVERT_SPEC     request charset conversion of filenames<br />
&#8211;checksum-seed=NUM      set block/file checksum seed (advanced)<br />
&#8211;ipv4, -4               prefer IPv4<br />
&#8211;ipv6, -6               prefer IPv6<br />
&#8211;version, -V            print the version + other info and exit<br />
&#8211;help, -h (*)           show this help (* -h is help only on its own)</p>
<p> Rsync can also be run as a daemon, in which case the following options are accepted: </p>
<p>&#8211;daemon run as an rsync daemon&#8211; address = ADDRESS bind to the specified address&#8211; bwlimit = RATE limit socket I / O bandwidth&#8211; config = FILE specify alternate rsyncd.conf file&#8211; dparam = OVERRIDE, -M override global daemon config parameter&#8211; no &#8211; detach do not detach from the parent&#8211; port = PORT listen on alternate port number&#8211; log &#8211; file = FILE override the &#8220;log file&#8221; setting&#8211; log &#8211; file &#8211; format = FMT override the &#8220;log format&#8221; setting&#8211; sockopts = OPTIONS specify custom TCP options&#8211; verbose, -v increase verbosity&#8211; ipv4, -4 prefer IPv4&#8211; ipv6, -6 prefer IPv6&#8211; help, -h show this help(when used with&#8211; daemon)</p>
<h2>OPTIONS</h2>
<p> Rsync accepts both long (double-dash + word) and short (single-dash + letter) options. The full list of the available options are described below. If an option can be specified in more than one way, the choices are comma-separated. Some options only have a long variant, not a short. </p>
<p> If the option takes a parameter, the parameter is only listed after the long variant, even though it must also be specified for the short. When specifying a parameter, you can either use the form <code>&#8211;option=param</code>, <code>&#8211;option param</code>, <code>-o=param</code>, <code>-o param</code>, or <code>-oparam</code> (the latter choices assume that your option has a short variant). </p>
<p> The parameter may need to be quoted in some manner for it to survive the shell&#8217;s command-line parsing. Also keep in mind that a leading tilde (<code>~</code>) in a pathname is substituted by your shell, so make sure that you separate the option name from the pathname using a space if you want the local shell to expand it. </p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print a short help page describing the options available in rsync and exit. You can also use <code>-h</code> for <code>&#8211;help</code> when it is used without any other options (since it normally means <code>&#8211;human-readable</code>).</p>
<dt><code>&#8211;version</code>, <code>-V</code></p>
<dd> Print the rsync version plus other info and exit. When repeated, the information is output is a JSON format that is still fairly readable (client side only).</p>
<dt>
<dd> The output includes a list of compiled-in capabilities, a list of optimizations, the default list of checksum algorithms, the default list of compression algorithms, the default list of daemon auth digests, a link to the rsync web site, and a few other items.</p>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> This option increases the amount of information you are given during the transfer. By default, rsync works silently. A single <code>-v</code> will give you information about what files are being transferred and a brief summary at the end. Two <code>-v</code> options will give you information on what files are being skipped and slightly more information at the end. More than two <code>-v</code> options should only be used if you are debugging rsync.</p>
<dt>
<dd> The end-of-run summary tells you the number of bytes sent to the remote rsync (which is the receiving side on a local copy), the number of bytes received from the remote host, and the average bytes per second of the transferred data computed over the entire length of the rsync run. The second line shows the total size (in bytes), which is the sum of all the file sizes that rsync considered transferring. It also shows a &quot;speedup&quot; value, which is a ratio of the total file size divided by the sum of the sent and received bytes (which is really just a feel-good bigger-is-better number). Note that these byte values can be made more (or less) human-readable by using the <code>&#8211;human-readable</code> (or <code>&#8211;no-human-readable</code>) options.</p>
<dt>
<dd> In a modern rsync, the <code>-v</code> option is equivalent to the setting of groups of <code>&#8211;info</code> and <code>&#8211;debug</code> options. You can choose to use these newer options in addition to, or in place of using <code>&#8211;verbose</code>, as any fine-grained settings override the implied settings of <code>-v</code>. Both <code>&#8211;info</code> and <code>&#8211;debug</code> have a way to ask for help that tells you exactly what flags are set for each increase in verbosity.</p>
<dt>
<dd> However, do keep in mind that a daemon&#8217;s &quot;<code>max verbosity</code>&quot; setting will limit how high of a level the various individual flags can be set on the daemon side. For instance, if the max is 2, then any info and/or debug flag that is set to a higher value than what would be set by <code>-vv</code> will be downgraded to the <code>-vv</code> level in the daemon&#8217;s logging.</p>
<dt><code>&#8211;info=FLAGS</code></p>
<dd> This option lets you have fine-grained control over the information output you want to see. An individual flag name may be followed by a level number, with 0 meaning to silence that output, 1 being the default output level, and higher numbers increasing the output of that flag (for those that support higher levels). Use <code>&#8211;info=help</code> to see all the available flag names, what they output, and what flag names are added for each increase in the verbose level. Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -a --info=progress2 src/ dest/
rsync -avv --info=stats2,misc1,flist0 src/ dest/
</pre>
</dl>
</dl>
<dt>
<dd> Note that <code>&#8211;info=name</code>&#8216;s output is affected by the <code>&#8211;out-format</code> and <code>&#8211;itemize-changes</code> (<code>-i</code>) options. See those options for more information on what is output and when.</p>
<dt>
<dd> This option was added to 3.1.0, so an older rsync on the server side might reject your attempts at fine-grained control (if one or more flags needed to be send to the server and the server was too old to understand them). See also the &quot;<code>max verbosity</code>&quot; caveat above when dealing with a daemon.</p>
<dt><code>&#8211;debug=FLAGS</code></p>
<dd> This option lets you have fine-grained control over the debug output you want to see. An individual flag name may be followed by a level number, with 0 meaning to silence that output, 1 being the default output level, and higher numbers increasing the output of that flag (for those that support higher levels). Use <code>&#8211;debug=help</code> to see all the available flag names, what they output, and what flag names are added for each increase in the verbose level. Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -avvv --debug=none src/ dest/
rsync -avA --del --debug=del2,acl src/ dest/
</pre>
</dl>
</dl>
<dt>
<dd> Note that some debug messages will only be output when the <code>&#8211;stderr=all</code> option is specified, especially those pertaining to I/O and buffer debugging.</p>
<dt>
<dd> Beginning in 3.2.0, this option is no longer auto-forwarded to the server side in order to allow you to specify different debug values for each side of the transfer, as well as to specify a new debug option that is only present in one of the rsync versions. If you want to duplicate the same option on both sides, using brace expansion is an easy way to save you some typing. This works in zsh and bash:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -aiv {-M,}--debug=del2 src/ dest/
</pre>
</dl>
</dl>
<dt><code>&#8211;stderr=errors|all|client</code></p>
<dd> This option controls which processes output to stderr and if info messages are also changed to stderr. The mode strings can be abbreviated, so feel free to use a single letter value. The 3 possible choices are:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>errors</code> &#8211; (the default) causes all the rsync processes to send an error directly to stderr, even if the process is on the remote side of the transfer. Info messages are sent to the client side via the protocol stream. If stderr is not available (i.e. when directly connecting with a daemon via a socket) errors fall back to being sent via the protocol stream.</p>
<dt>o</p>
<dd> <code>all</code> &#8211; causes all rsync messages (info and error) to get written directly to stderr from all (possible) processes. This causes stderr to become line-buffered (instead of raw) and eliminates the ability to divide up the info and error messages by file handle. For those doing debugging or using several levels of verbosity, this option can help to avoid clogging up the transfer stream (which should prevent any chance of a deadlock bug hanging things up). It also allows <code>&#8211;debug</code> to enable some extra I/O related messages.</p>
<dt>o</p>
<dd> <code>client</code> &#8211; causes all rsync messages to be sent to the client side via the protocol stream. One client process outputs all messages, with errors on stderr and info messages on stdout. This <code>was</code> the default in older rsync versions, but can cause error delays when a lot of transfer data is ahead of the messages. If you&#8217;re pushing files to an older rsync, you may want to use <code>&#8211;stderr=all</code> since that idiom has been around for several releases.</dl>
</dl>
<dt>
<dd> This option was added in rsync 3.2.3. This version also began the forwarding of a non-default setting to the remote side, though rsync uses the backward-compatible options <code>&#8211;msgs2stderr</code> and <code>&#8211;no-msgs2stderr</code> to represent the <code>all</code> and <code>client</code> settings, respectively. A newer rsync will continue to accept these older option names to maintain compatibility.</p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd> This option decreases the amount of information you are given during the transfer, notably suppressing information messages from the remote server. This option is useful when invoking rsync from cron.</p>
<dt><code>&#8211;no-motd</code></p>
<dd> This option affects the information that is output by the client at the start of a daemon transfer. This suppresses the message-of-the-day (MOTD) text, but it also affects the list of modules that the daemon sends in response to the &quot;rsync host::&quot; request (due to a limitation in the rsync protocol), so omit this option if you want to request the list of modules from the daemon.</p>
<dt><code>&#8211;ignore-times</code>, <code>-I</code></p>
<dd> Normally rsync will skip any files that are already the same size and have the same modification timestamp. This option turns off this &quot;quick check&quot; behavior, causing all files to be updated.</p>
<dt>
<dd> This option can be confusing compared to <code>&#8211;ignore-existing</code> and <code>&#8211;ignore-non-existing</code> in that that they cause rsync to transfer fewer files, while this option causes rsync to transfer more files.</p>
<dt><code>&#8211;size-only</code></p>
<dd> This modifies rsync&#8217;s &quot;quick check&quot; algorithm for finding files that need to be transferred, changing it from the default of transferring files with either a changed size or a changed last-modified time to just looking for files that have changed in size. This is useful when starting to use rsync after using another mirroring system which may not preserve timestamps exactly.</p>
<dt><code>&#8211;modify-window=NUM</code>, <code>-@</code></p>
<dd> When comparing two timestamps, rsync treats the timestamps as being equal if they differ by no more than the modify-window value. The default is 0, which matches just integer seconds. If you specify a negative value (and the receiver is at least version 3.1.3) then nanoseconds will also be taken into account. Specifying 1 is useful for copies to/from MS Windows FAT filesystems, because FAT represents times with a 2-second resolution (allowing times to differ from the original by up to 1 second).</p>
<dt>
<dd> If you want all your transfers to default to comparing nanoseconds, you can create a <code>~/.popt</code> file and put these lines in it:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync alias -a -a@-1
rsync alias -t -t@-1
</pre>
</dl>
</dl>
<dt>
<dd> With that as the default, you&#8217;d need to specify <code>&#8211;modify-window=0</code> (aka <code>-@0</code>) to override it and ignore nanoseconds, e.g. if you&#8217;re copying between ext3 and ext4, or if the receiving rsync is older than 3.1.3.</p>
<dt><code>&#8211;checksum</code>, <code>-c</code></p>
<dd> This changes the way rsync checks if the files have been changed and are in need of a transfer. Without this option, rsync uses a &quot;quick check&quot; that (by default) checks if each file&#8217;s size and time of last modification match between the sender and receiver. This option changes this to compare a 128-bit checksum for each file that has a matching size. Generating the checksums means that both sides will expend a lot of disk I/O reading all the data in the files in the transfer, so this can slow things down significantly (and this is prior to any reading that will be done to transfer changed files)</p>
<dt>
<dd> The sending side generates its checksums while it is doing the file-system scan that builds the list of the available files. The receiver generates its checksums when it is scanning for changed files, and will checksum any file that has the same size as the corresponding sender&#8217;s file: files with either a changed size or a changed checksum are selected for transfer.</p>
<dt>
<dd> Note that rsync always verifies that each <i>transferred</i> file was correctly reconstructed on the receiving side by checking a whole-file checksum that is generated as the file is transferred, but that automatic after-the-transfer verification has nothing to do with this option&#8217;s before-the-transfer &quot;Does this file need to be updated?&quot; check.</p>
<dt>
<dd> The checksum used is auto-negotiated between the client and the server, but can be overridden using either the <code>&#8211;checksum-choice</code> (<code>&#8211;cc</code>) option or an environment variable that is discussed in that option&#8217;s section.</p>
<dt><code>&#8211;archive</code>, <code>-a</code></p>
<dd> This is equivalent to <code>-rlptgoD</code>. It is a quick way of saying you want recursion and want to preserve almost everything. Be aware that it does <code>not</code> include preserving ACLs (<code>-A</code>), xattrs (<code>-X</code>), atimes (<code>-U</code>), crtimes (<code>-N</code>), nor the finding and preserving of hardlinks (<code>-H</code>).</p>
<dt>
<dd> The only exception to the above equivalence is when <code>&#8211;files-from</code> is specified, in which case <code>-r</code> is not implied.</p>
<dt><code>&#8211;no-OPTION</code></p>
<dd> You may turn off one or more implied options by prefixing the option name with &quot;no-&quot;. Not all positive options have a negated opposite, but a lot do, including those that can be used to disable an implied option (e.g. <code>&#8211;no-D</code>, <code>&#8211;no-perms</code>) or have different defaults in various circumstances (e.g. <code>&#8211;no-whole-file</code>, <code>&#8211;no-blocking-io</code>, <code>&#8211;no-dirs</code>). Every valid negated option accepts both the short and the long option name after the &quot;no-&quot; prefix (e.g. <code>&#8211;no-R</code> is the same as <code>&#8211;no-relative</code>).</p>
<dt>
<dd> As an example, if you want to use <code>&#8211;archive</code> (<code>-a</code>) but don&#8217;t want <code>&#8211;owner</code> (<code>-o</code>), instead of converting <code>-a</code> into <code>-rlptgD</code>, you can specify <code>-a &#8211;no-o</code> (aka <code>&#8211;archive &#8211;no-owner</code>).</p>
<dt>
<dd> The order of the options is important: if you specify <code>&#8211;no-r -a</code>, the <code>-r</code> option would end up being turned on, the opposite of <code>-a &#8211;no-r</code>. Note also that the side-effects of the <code>&#8211;files-from</code> option are NOT positional, as it affects the default state of several options and slightly changes the meaning of <code>-a</code> (see the <code>&#8211;files-from</code> option for more details).</p>
<dt><code>&#8211;recursive</code>, <code>-r</code></p>
<dd> This tells rsync to copy directories recursively. See also <code>&#8211;dirs</code> (<code>-d</code>) for an option that allows the scanning of a single directory.</p>
<dt>
<dd> See the <code>&#8211;inc-recursive</code> option for a discussion of the incremental recursion for creating the list of files to transfer.</p>
<dt><code>&#8211;inc-recursive</code>, <code>&#8211;i-r</code></p>
<dd> This option explicitly enables on incremental recursion when scanning for files, which is enabled by default when using the <code>&#8211;recursive</code> option and both sides of the transfer are running rsync 3.0.0 or newer.</p>
<dt>
<dd> Incremental recursion uses much less memory than non-incremental, while also beginning the transfer more quickly (since it doesn&#8217;t need to scan the entire transfer hierarchy before it starts transferring files). If no recursion is enabled in the source files, this option has no effect.</p>
<dt>
<dd> Some options require rsync to know the full file list, so these options disable the incremental recursion mode. These include:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>&#8211;delete-before</code> (the old default of <code>&#8211;delete</code>)</p>
<dt>o</p>
<dd> <code>&#8211;delete-after</code></p>
<dt>o</p>
<dd> <code>&#8211;prune-empty-dirs</code></p>
<dt>o</p>
<dd> <code>&#8211;delay-updates</code></dl>
</dl>
<dt>
<dd> In order to make <code>&#8211;delete</code> compatible with incremental recursion, rsync 3.0.0 made <code>&#8211;delete-during</code> the default delete mode (which was first added in 2.6.4).</p>
<dt>
<dd> One side-effect of incremental recursion is that any missing sub-directories inside a recursively-scanned directory are (by default) created prior to recursing into the sub-dirs. This earlier creation point (compared to a non-incremental recursion) allows rsync to then set the modify time of the finished directory right away (without having to delay that until a bunch of recursive copying has finished). However, these early directories don&#8217;t yet have their completed mode, mtime, or ownership set &#8212; they have more restrictive rights until the subdirectory&#8217;s copying actually begins. This early-creation idiom can be avoided by using the <code>&#8211;omit-dir-times</code> option.</p>
<dt>
<dd> Incremental recursion can be disabled using the <code>&#8211;no-inc-recursive</code> (<code>&#8211;no-i-r</code>) option.</p>
<dt><code>&#8211;no-inc-recursive</code>, <code>&#8211;no-i-r</code></p>
<dd> Disables the new incremental recursion algorithm of the <code>&#8211;recursive</code> option. This makes rsync scan the full file list before it begins to transfer files. See <code>&#8211;inc-recursive</code> for more info.</p>
<dt><code>&#8211;relative</code>, <code>-R</code></p>
<dd> Use relative paths. This means that the full path names specified on the command line are sent to the server rather than just the last parts of the filenames. This is particularly useful when you want to send several different directories at the same time. For example, if you used this command:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -av /foo/bar/baz.c remote:/tmp/
</pre>
</dl>
</dl>
<dt>
<dd> would create a file named baz.c in /tmp/ on the remote machine. If instead you used</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -avR /foo/bar/baz.c remote:/tmp/
</pre>
</dl>
</dl>
<dt>
<dd> then a file named /tmp/foo/bar/baz.c would be created on the remote machine, preserving its full path. These extra path elements are called &quot;implied directories&quot; (i.e. the &quot;foo&quot; and the &quot;foo/bar&quot; directories in the above example).</p>
<dt>
<dd> Beginning with rsync 3.0.0, rsync always sends these implied directories as real directories in the file list, even if a path element is really a symlink on the sending side. This prevents some really unexpected behaviors when copying the full path of a file that you didn&#8217;t realize had a symlink in its path. If you want to duplicate a server-side symlink, include both the symlink via its path, and referent directory via its real path. If you&#8217;re dealing with an older rsync on the sending side, you may need to use the <code>&#8211;no-implied-dirs</code> option.</p>
<dt>
<dd> It is also possible to limit the amount of path information that is sent as implied directories for each path you specify. With a modern rsync on the sending side (beginning with 2.6.7), you can insert a dot and a slash into the source path, like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -avR /foo/./bar/baz.c remote:/tmp/
</pre>
</dl>
</dl>
<dt>
<dd> That would create /tmp/bar/baz.c on the remote machine. (Note that the dot must be followed by a slash, so &quot;/foo/.&quot; would not be abbreviated.) For older rsync versions, you would need to use a chdir to limit the source path. For example, when pushing files:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
(cd /foo; rsync -avR bar/baz.c remote:/tmp/)
</pre>
</dl>
</dl>
<dt>
<dd> (Note that the parens put the two commands into a sub-shell, so that the &quot;cd&quot; command doesn&#8217;t remain in effect for future commands.) If you&#8217;re pulling files from an older rsync, use this idiom (but only for a non-daemon transfer):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -avR --rsync-path=&quot;cd /foo; rsync&quot; \
     remote:bar/baz.c /tmp/
</pre>
</dl>
</dl>
<dt><code>&#8211;no-implied-dirs</code></p>
<dd> This option affects the default behavior of the <code>&#8211;relative</code> option. When it is specified, the attributes of the implied directories from the source names are not included in the transfer. This means that the corresponding path elements on the destination system are left unchanged if they exist, and any missing implied directories are created with default attributes. This even allows these implied path elements to have big differences, such as being a symlink to a directory on the receiving side.</p>
<dt>
<dd> For instance, if a command-line arg or a files-from entry told rsync to transfer the file &quot;path/foo/file&quot;, the directories &quot;path&quot; and &quot;path/foo&quot; are implied when <code>&#8211;relative</code> is used. If &quot;path/foo&quot; is a symlink to &quot;bar&quot; on the destination system, the receiving rsync would ordinarily delete &quot;path/foo&quot;, recreate it as a directory, and receive the file into the new directory. With <code>&#8211;no-implied-dirs</code>, the receiving rsync updates &quot;path/foo/file&quot; using the existing path elements, which means that the file ends up being created in &quot;path/bar&quot;. Another way to accomplish this link preservation is to use the <code>&#8211;keep-dirlinks</code> option (which will also affect symlinks to directories in the rest of the transfer).</p>
<dt>
<dd> When pulling files from an rsync older than 3.0.0, you may need to use this option if the sending side has a symlink in the path you request and you wish the implied directories to be transferred as normal directories.</p>
<dt><code>&#8211;backup</code>, <code>-b</code></p>
<dd> With this option, preexisting destination files are renamed as each file is transferred or deleted. You can control where the backup file goes and what (if any) suffix gets appended using the <code>&#8211;backup-dir</code> and <code>&#8211;suffix</code> options.</p>
<dt>
<dd> If you don&#8217;t specify <code>&#8211;backup-dir</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dt>1.</p>
<dd> the <code>&#8211;omit-dir-times</code> option will be forced on</p>
<dt>2.</p>
<dd> the use of <code>&#8211;delete</code> (without <code>&#8211;delete-excluded</code>), causes rsync to add a &quot;protect&quot; filter-rule for the backup suffix to the end of all your existing filters that looks like this: <code>-f&nbsp;&quot;P&nbsp;*~&quot;</code>. This rule prevents previously backed-up files from being deleted.</dl>
</dl>
<dt>
<dd> Note that if you are supplying your own filter rules, you may need to manually insert your own exclude/protect rule somewhere higher up in the list so that it has a high enough priority to be effective (e.g. if your rules specify a trailing inclusion/exclusion of <code>*</code>, the auto-added rule would never be reached).</p>
<dt><code>&#8211;backup-dir=DIR</code></p>
<dd> This implies the <code>&#8211;backup</code> option, and tells rsync to store all backups in the specified directory on the receiving side. This can be used for incremental backups. You can additionally specify a backup suffix using the <code>&#8211;suffix</code> option (otherwise the files backed up in the specified directory will keep their original filenames).</p>
<dt>
<dd> Note that if you specify a relative path, the backup directory will be relative to the destination directory, so you probably want to specify either an absolute path or a path that starts with &quot;../&quot;. If an rsync daemon is the receiver, the backup dir cannot go outside the module&#8217;s path hierarchy, so take extra care not to delete it or copy into it.</p>
<dt><code>&#8211;suffix=SUFFIX</code></p>
<dd> This option allows you to override the default backup suffix used with the <code>&#8211;backup</code> (<code>-b</code>) option. The default suffix is a <code>~</code> if no <code>&#8211;backup-dir</code> was specified, otherwise it is an empty string.</p>
<dt><code>&#8211;update</code>, <code>-u</code></p>
<dd> This forces rsync to skip any files which exist on the destination and have a modified time that is newer than the source file. (If an existing destination file has a modification time equal to the source file&#8217;s, it will be updated if the sizes are different.)</p>
<dt>
<dd> Note that this does not affect the copying of dirs, symlinks, or other special files. Also, a difference of file format between the sender and receiver is always considered to be important enough for an update, no matter what date is on the objects. In other words, if the source has a directory where the destination has a file, the transfer would occur regardless of the timestamps.</p>
<dt>
<dd> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects.</p>
<dt>
<dd> A caution for those that choose to combine <code>&#8211;inplace</code> with <code>&#8211;update</code>: an interrupted transfer will leave behind a partial file on the receiving side that has a very recent modified time, so re-running the transfer will probably <code>not</code> continue the interrupted file. As such, it is usually best to avoid combining this with <code>&#8211;inplace</code> unless you have implemented manual steps to handle any interrupted in-progress files.</p>
<dt><code>&#8211;inplace</code></p>
<dd> This option changes how rsync transfers a file when its data needs to be updated: instead of the default method of creating a new copy of the file and moving it into place when it is complete, rsync instead writes the updated data directly to the destination file.</p>
<dt>
<dd> This has several effects:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Hard links are not broken. This means the new data will be visible through other hard links to the destination file. Moreover, attempts to copy differing source files onto a multiply-linked destination file will result in a &quot;tug of war&quot; with the destination data changing back and forth.</p>
<dt>o</p>
<dd> In-use binaries cannot be updated (either the OS will prevent this from happening, or binaries that attempt to swap-in their data will misbehave or crash).</p>
<dt>o</p>
<dd> The file&#8217;s data will be in an inconsistent state during the transfer and will be left that way if the transfer is interrupted or if an update fails.</p>
<dt>o</p>
<dd> A file that rsync cannot write to cannot be updated. While a super user can update any file, a normal user needs to be granted write permission for the open of the file for writing to be successful.</p>
<dt>o</p>
<dd> The efficiency of rsync&#8217;s delta-transfer algorithm may be reduced if some data in the destination file is overwritten before it can be copied to a position later in the file. This does not apply if you use <code>&#8211;backup</code>, since rsync is smart enough to use the backup file as the basis file for the transfer.</dl>
</dl>
<dt>
<dd> WARNING: you should not use this option to update files that are being accessed by others, so be careful when choosing to use this for a copy.</p>
<dt>
<dd> This option is useful for transferring large files with block-based changes or appended data, and also on systems that are disk bound, not network bound. It can also help keep a copy-on-write filesystem snapshot from diverging the entire contents of a file that only has minor changes.</p>
<dt>
<dd> The option implies <code>&#8211;partial</code> (since an interrupted transfer does not delete the file), but conflicts with <code>&#8211;partial-dir</code> and <code>&#8211;delay-updates</code>. Prior to rsync 2.6.4 <code>&#8211;inplace</code> was also incompatible with <code>&#8211;compare-dest</code> and <code>&#8211;link-dest</code>.</p>
<dt><code>&#8211;append</code></p>
<dd> This special copy mode only works to efficiently update files that are known to be growing larger where any existing content on the receiving side is also known to be the same as the content on the sender. The use of <code>&#8211;append</code> <code>can be dangerous</code> if you aren&#8217;t 100% sure that all the files in the transfer are shared, growing files. You should thus use filter rules to ensure that you weed out any files that do not fit this criteria.</p>
<dt>
<dd> Rsync updates these growing file in-place without verifying any of the existing content in the file (it only verifies the content that it is appending). Rsync skips any files that exist on the receiving side that are not shorter than the associated file on the sending side (which means that new files are transferred). It also skips any files whose size on the sending side gets shorter during the send negotiations (rsync warns about a &quot;diminished&quot; file when this happens).</p>
<dt>
<dd> This does not interfere with the updating of a file&#8217;s non-content attributes (e.g. permissions, ownership, etc.) when the file does not need to be transferred, nor does it affect the updating of any directories or non-regular files.</p>
<dt><code>&#8211;append-verify</code></p>
<dd> This special copy mode works like <code>&#8211;append</code> except that all the data in the file is included in the checksum verification (making it less efficient but also potentially safer). This option <code>can be dangerous</code> if you aren&#8217;t 100% sure that all the files in the transfer are shared, growing files. See the <code>&#8211;append</code> option for more details.</p>
<dt>
<dd> Note: prior to rsync 3.0.0, the <code>&#8211;append</code> option worked like <code>&#8211;append-verify</code>, so if you are interacting with an older rsync (or the transfer is using a protocol prior to 30), specifying either append option will initiate an <code>&#8211;append-verify</code> transfer.</p>
<dt><code>&#8211;dirs</code>, <code>-d</code></p>
<dd> Tell the sending side to include any directories that are encountered. Unlike <code>&#8211;recursive</code>, a directory&#8217;s contents are not copied unless the directory name specified is &quot;.&quot; or ends with a trailing slash (e.g. &quot;.&quot;, &quot;dir/.&quot;, &quot;dir/&quot;, etc.). Without this option or the <code>&#8211;recursive</code> option, rsync will skip all directories it encounters (and output a message to that effect for each one). If you specify both <code>&#8211;dirs</code> and <code>&#8211;recursive</code>, <code>&#8211;recursive</code> takes precedence.</p>
<dt>
<dd> The <code>&#8211;dirs</code> option is implied by the <code>&#8211;files-from</code> option or the <code>&#8211;list-only</code> option (including an implied <code>&#8211;list-only</code> usage) if <code>&#8211;recursive</code> wasn&#8217;t specified (so that directories are seen in the listing). Specify <code>&#8211;no-dirs</code> (or <code>&#8211;no-d</code>) if you want to turn this off.</p>
<dt>
<dd> There is also a backward-compatibility helper option, <code>&#8211;old-dirs</code> (<code>&#8211;old-d</code>) that tells rsync to use a hack of <code>-r &#8211;exclude=&#8217;/*/*&#8217;</code> to get an older rsync to list a single directory without recursing.</p>
<dt><code>&#8211;mkpath</code></p>
<dd> Create all missing path components of the destination path.</p>
<dt>
<dd> By default, rsync allows only the final component of the destination path to not exist, which is an attempt to help you to validate your destination path. With this option, rsync creates all the missing destination-path components, just as if <code>mkdir -p&nbsp;$DEST_PATH</code> had been run on the receiving side.</p>
<dt>
<dd> When specifying a destination path, including a trailing slash ensures that the whole path is treated as directory names to be created, even when the file list has a single item. See the COPYING TO A DIFFERENT NAME section for full details on how rsync decides if a final destination-path component should be created as a directory or not.</p>
<dt>
<dd> If you would like the newly-created destination dirs to match the dirs on the sending side, you should be using <code>&#8211;relative</code> (<code>-R</code>) instead of <code>&#8211;mkpath</code>. For instance, the following two commands result in the same destination tree, but only the second command ensures that the &quot;some/extra/path&quot; components match the dirs on the sending side:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -ai --mkpath host:some/extra/path/*.c some/extra/path/
rsync -aiR host:some/extra/path/*.c ./
</pre>
</dl>
</dl>
<dt><code>&#8211;links</code>, <code>-l</code></p>
<dd> Add symlinks to the transferred files instead of noisily ignoring them with a &quot;non-regular file&quot; warning for each symlink encountered. You can alternately silence the warning by specifying <code>&#8211;info=nonreg0</code>.</p>
<dt>
<dd> The default handling of symlinks is to recreate each symlink&#8217;s unchanged value on the receiving side.</p>
<dt>
<dd> See the SYMBOLIC LINKS section for multi-option info.</p>
<dt><code>&#8211;copy-links</code>, <code>-L</code></p>
<dd> The sender transforms each symlink encountered in the transfer into the referent item, following the symlink chain to the file or directory that it references. If a symlink chain is broken, an error is output and the file is dropped from the transfer.</p>
<dt>
<dd> This option supersedes any other options that affect symlinks in the transfer, since there are no symlinks left in the transfer.</p>
<dt>
<dd> This option does not change the handling of existing symlinks on the receiving side, unlike versions of rsync prior to 2.6.3 which had the side-effect of telling the receiving side to also follow symlinks. A modern rsync won&#8217;t forward this option to a remote receiver (since only the sender needs to know about it), so this caveat should only affect someone using an rsync client older than 2.6.7 (which is when <code>-L</code> stopped being forwarded to the receiver).</p>
<dt>
<dd> See the <code>&#8211;keep-dirlinks</code> (<code>-K</code>) if you need a symlink to a directory to be treated as a real directory on the receiving side.</p>
<dt>
<dd> See the SYMBOLIC LINKS section for multi-option info.</p>
<dt><code>&#8211;copy-unsafe-links</code></p>
<dd> This tells rsync to copy the referent of symbolic links that point outside the copied tree. Absolute symlinks are also treated like ordinary files, and so are any symlinks in the source path itself when <code>&#8211;relative</code> is used.</p>
<dt>
<dd> Note that the cut-off point is the top of the transfer, which is the part of the path that rsync isn&#8217;t mentioning in the verbose output. If you copy &quot;/src/subdir&quot; to &quot;/dest/&quot; then the &quot;subdir&quot; directory is a name inside the transfer tree, not the top of the transfer (which is /src) so it is legal for created relative symlinks to refer to other names inside the /src and /dest directories. If you instead copy &quot;/src/subdir/&quot; (with a trailing slash) to &quot;/dest/subdir&quot; that would not allow symlinks to any files outside of &quot;subdir&quot;.</p>
<dt>
<dd> Note that safe symlinks are only copied if <code>&#8211;links</code> was also specified or implied. The <code>&#8211;copy-unsafe-links</code> option has no extra effect when combined with <code>&#8211;copy-links</code>.</p>
<dt>
<dd> See the SYMBOLIC LINKS section for multi-option info.</p>
<dt><code>&#8211;safe-links</code></p>
<dd> This tells the receiving rsync to ignore any symbolic links in the transfer which point outside the copied tree. All absolute symlinks are also ignored.</p>
<dt>
<dd> Since this ignoring is happening on the receiving side, it will still be effective even when the sending side has munged symlinks (when it is using <code>&#8211;munge-links</code>). It also affects deletions, since the file being present in the transfer prevents any matching file on the receiver from being deleted when the symlink is deemed to be unsafe and is skipped.</p>
<dt>
<dd> This option must be combined with <code>&#8211;links</code> (or <code>&#8211;archive</code>) to have any symlinks in the transfer to conditionally ignore. Its effect is superseded by <code>&#8211;copy-unsafe-links</code>.</p>
<dt>
<dd> Using this option in conjunction with <code>&#8211;relative</code> may give unexpected results.</p>
<dt>
<dd> See the SYMBOLIC LINKS section for multi-option info.</p>
<dt><code>&#8211;munge-links</code></p>
<dd> This option affects just one side of the transfer and tells rsync to munge symlink values when it is receiving files or unmunge symlink values when it is sending files. The munged values make the symlinks unusable on disk but allows the original contents of the symlinks to be recovered.</p>
<dt>
<dd> The server-side rsync often enables this option without the client&#8217;s knowledge, such as in an rsync daemon&#8217;s configuration file or by an option given to the rrsync (restricted rsync) script. When specified on the client side, specify the option normally if it is the client side that has/needs the munged symlinks, or use <code>-M&#8211;munge-links</code> to give the option to the server when it has/needs the munged symlinks. Note that on a local transfer, the client is the sender, so specifying the option directly unmunges symlinks while specifying it as a remote option munges symlinks.</p>
<dt>
<dd> This option has no effect when sent to a daemon via <code>&#8211;remote-option</code> because the daemon configures whether it wants munged symlinks via its &quot;<code>munge symlinks</code>&quot; parameter.</p>
<dt>
<dd> The symlink value is munged/unmunged once it is in the transfer, so any option that transforms symlinks into non-symlinks occurs prior to the munging/unmunging <code>except</code> for <code>&#8211;safe-links</code>, which is a choice that the receiver makes, so it bases its decision on the munged/unmunged value. This does mean that if a receiver has munging enabled, that using <code>&#8211;safe-links</code> will cause all symlinks to be ignored (since they are all absolute).</p>
<dt>
<dd> The method that rsync uses to munge the symlinks is to prefix each one&#8217;s value with the string &quot;/rsyncd-munged/&quot;. This prevents the links from being used as long as the directory does not exist. When this option is enabled, rsync will refuse to run if that path is a directory or a symlink to a directory (though it only checks at startup). See also the &quot;munge-symlinks&quot; python script in the support directory of the source code for a way to munge/unmunge one or more symlinks in-place.</p>
<dt><code>&#8211;copy-dirlinks</code>, <code>-k</code></p>
<dd> This option causes the sending side to treat a symlink to a directory as though it were a real directory. This is useful if you don&#8217;t want symlinks to non-directories to be affected, as they would be using <code>&#8211;copy-links</code>.</p>
<dt>
<dd> Without this option, if the sending side has replaced a directory with a symlink to a directory, the receiving side will delete anything that is in the way of the new symlink, including a directory hierarchy (as long as <code>&#8211;force</code> or <code>&#8211;delete</code> is in effect).</p>
<dt>
<dd> See also <code>&#8211;keep-dirlinks</code> for an analogous option for the receiving side.</p>
<dt>
<dd> <code>&#8211;copy-dirlinks</code> applies to all symlinks to directories in the source. If you want to follow only a few specified symlinks, a trick you can use is to pass them as additional source args with a trailing slash, using <code>&#8211;relative</code> to make the paths match up right. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -r --relative src/./ src/./follow-me/ dest/
</pre>
</dl>
</dl>
<dt>
<dd> This works because rsync calls <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) on the source arg as given, and the trailing slash makes <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) follow the symlink, giving rise to a directory in the file-list which overrides the symlink found during the scan of &quot;src/./&quot;.</p>
<dt>
<dd> See the SYMBOLIC LINKS section for multi-option info.</p>
<dt><code>&#8211;keep-dirlinks</code>, <code>-K</code></p>
<dd> This option causes the receiving side to treat a symlink to a directory as though it were a real directory, but only if it matches a real directory from the sender. Without this option, the receiver&#8217;s symlink would be deleted and replaced with a real directory.</p>
<dt>
<dd> For example, suppose you transfer a directory &quot;foo&quot; that contains a file &quot;file&quot;, but &quot;foo&quot; is a symlink to directory &quot;bar&quot; on the receiver. Without <code>&#8211;keep-dirlinks</code>, the receiver deletes symlink &quot;foo&quot;, recreates it as a directory, and receives the file into the new directory. With <code>&#8211;keep-dirlinks</code>, the receiver keeps the symlink and &quot;file&quot; ends up in &quot;bar&quot;.</p>
<dt>
<dd> One note of caution: if you use <code>&#8211;keep-dirlinks</code>, you must trust all the symlinks in the copy or enable the <code>&#8211;munge-links</code> option on the receiving side! If it is possible for an untrusted user to create their own symlink to any real directory, the user could then (on a subsequent copy) replace the symlink with a real directory and affect the content of whatever directory the symlink references. For backup copies, you are better off using something like a bind mount instead of a symlink to modify your receiving hierarchy.</p>
<dt>
<dd> See also <code>&#8211;copy-dirlinks</code> for an analogous option for the sending side.</p>
<dt>
<dd> See the SYMBOLIC LINKS section for multi-option info.</p>
<dt><code>&#8211;hard-links</code>, <code>-H</code></p>
<dd> This tells rsync to look for hard-linked files in the source and link together the corresponding files on the destination. Without this option, hard-linked files in the source are treated as though they were separate files.</p>
<dt>
<dd> This option does NOT necessarily ensure that the pattern of hard links on the destination exactly matches that on the source. Cases in which the destination may end up with extra hard links include the following:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> If the destination contains extraneous hard-links (more linking than what is present in the source file list), the copying algorithm will not break them explicitly. However, if one or more of the paths have content differences, the normal file-update process will break those extra links (unless you are using the <code>&#8211;inplace</code> option).</p>
<dt>o</p>
<dd> If you specify a <code>&#8211;link-dest</code> directory that contains hard links, the linking of the destination files against the <code>&#8211;link-dest</code> files can cause some paths in the destination to become linked together due to the <code>&#8211;link-dest</code> associations.</dl>
</dl>
<dt>
<dd> Note that rsync can only detect hard links between files that are inside the transfer set. If rsync updates a file that has extra hard-link connections to files outside the transfer, that linkage will be broken. If you are tempted to use the <code>&#8211;inplace</code> option to avoid this breakage, be very careful that you know how your files are being updated so that you are certain that no unintended changes happen due to lingering hard links (and see the <code>&#8211;inplace</code> option for more caveats).</p>
<dt>
<dd> If incremental recursion is active (see <code>&#8211;inc-recursive</code>), rsync may transfer a missing hard-linked file before it finds that another link for that contents exists elsewhere in the hierarchy. This does not affect the accuracy of the transfer (i.e. which files are hard-linked together), just its efficiency (i.e. copying the data for a new, early copy of a hard-linked file that could have been found later in the transfer in another member of the hard-linked set of files). One way to avoid this inefficiency is to disable incremental recursion using the <code>&#8211;no-inc-recursive</code> option.</p>
<dt><code>&#8211;perms</code>, <code>-p</code></p>
<dd> This option causes the receiving rsync to set the destination permissions to be the same as the source permissions. (See also the <code>&#8211;chmod</code> option for a way to modify what rsync considers to be the source permissions.)</p>
<dt>
<dd> When this option is <i>off</i>, permissions are set as follows:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Existing files (including updated files) retain their existing permissions, though the <code>&#8211;executability</code> option might change just the execute permission for the file.</p>
<dt>o</p>
<dd> New files get their &quot;normal&quot; permission bits set to the source file&#8217;s permissions masked with the receiving directory&#8217;s default permissions (either the receiving process&#8217;s umask, or the permissions specified via the destination directory&#8217;s default ACL), and their special permission bits disabled except in the case where a new directory inherits a setgid bit from its parent directory.</dl>
</dl>
<dt>
<dd> Thus, when <code>&#8211;perms</code> and <code>&#8211;executability</code> are both disabled, rsync&#8217;s behavior is the same as that of other file-copy utilities, such as <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) and <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1).</p>
<dt>
<dd> In summary: to give destination files (both old and new) the source permissions, use <code>&#8211;perms</code>. To give new files the destination-default permissions (while leaving existing files unchanged), make sure that the <code>&#8211;perms</code> option is off and use <code>&#8211;chmod=ugo=rwX</code> (which ensures that all non-masked bits get enabled). If you&#8217;d care to make this latter behavior easier to type, you could define a popt alias for it, such as putting this line in the file <code>~/.popt</code> (the following defines the <code>-Z</code> option, and includes <code>&#8211;no-g</code> to use the default group of the destination dir):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync alias -Z --no-p --no-g --chmod=ugo=rwX
</pre>
</dl>
</dl>
<dt>
<dd> You could then use this new option in a command such as this one:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -avZ src/ dest/
</pre>
</dl>
</dl>
<dt>
<dd> (Caveat: make sure that <code>-a</code> does not follow <code>-Z</code>, or it will re-enable the two <code>&#8211;no-*</code> options mentioned above.)</p>
<dt>
<dd> The preservation of the destination&#8217;s setgid bit on newly-created directories when <code>&#8211;perms</code> is off was added in rsync 2.6.7. Older rsync versions erroneously preserved the three special permission bits for newly-created files when <code>&#8211;perms</code> was off, while overriding the destination&#8217;s setgid bit setting on a newly-created directory. Default ACL observance was added to the ACL patch for rsync 2.6.7, so older (or non-ACL-enabled) rsyncs use the umask even if default ACLs are present. (Keep in mind that it is the version of the receiving rsync that affects these behaviors.)</p>
<dt><code>&#8211;executability</code>, <code>-E</code></p>
<dd> This option causes rsync to preserve the executability (or non-executability) of regular files when <code>&#8211;perms</code> is not enabled. A regular file is considered to be executable if at least one &#8216;x&#8217; is turned on in its permissions. When an existing destination file&#8217;s executability differs from that of the corresponding source file, rsync modifies the destination file&#8217;s permissions as follows:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> To make a file non-executable, rsync turns off all its &#8216;x&#8217; permissions.</p>
<dt>o</p>
<dd> To make a file executable, rsync turns on each &#8216;x&#8217; permission that has a corresponding &#8216;r&#8217; permission enabled.</dl>
</dl>
<dt>
<dd> If <code>&#8211;perms</code> is enabled, this option is ignored.</p>
<dt><code>&#8211;acls</code>, <code>-A</code></p>
<dd> This option causes rsync to update the destination ACLs to be the same as the source ACLs. The option also implies <code>&#8211;perms</code>.</p>
<dt>
<dd> The source and destination systems must have compatible ACL entries for this option to work properly. See the <code>&#8211;fake-super</code> option for a way to backup and restore ACLs that are not compatible.</p>
<dt><code>&#8211;xattrs</code>, <code>-X</code></p>
<dd> This option causes rsync to update the destination extended attributes to be the same as the source ones.</p>
<dt>
<dd> For systems that support extended-attribute namespaces, a copy being done by a super-user copies all namespaces except system.*. A normal user only copies the user.* namespace. To be able to backup and restore non-user namespaces as a normal user, see the <code>&#8211;fake-super</code> option.</p>
<dt>
<dd> The above name filtering can be overridden by using one or more filter options with the <code>x</code> modifier. When you specify an xattr-affecting filter rule, rsync requires that you do your own system/user filtering, as well as any additional filtering for what xattr names are copied and what names are allowed to be deleted. For example, to skip the system namespace, you could specify:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--filter='-x system.*'
</pre>
</dl>
</dl>
<dt>
<dd> To skip all namespaces except the user namespace, you could specify a negated-user match:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--filter='-x! user.*'
</pre>
</dl>
</dl>
<dt>
<dd> To prevent any attributes from being deleted, you could specify a receiver-only rule that excludes all names:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--filter='-xr *'
</pre>
</dl>
</dl>
<dt>
<dd> Note that the <code>-X</code> option does not copy rsync&#8217;s special xattr values (e.g. those used by <code>&#8211;fake-super</code>) unless you repeat the option (e.g. <code>-XX</code>). This &quot;copy all xattrs&quot; mode cannot be used with <code>&#8211;fake-super</code>.</p>
<dt><code>&#8211;chmod=CHMOD</code></p>
<dd> This option tells rsync to apply one or more comma-separated &quot;chmod&quot; modes to the permission of the files in the transfer. The resulting value is treated as though it were the permissions that the sending side supplied for the file, which means that this option can seem to have no effect on existing files if <code>&#8211;perms</code> is not enabled.</p>
<dt>
<dd> In addition to the normal parsing rules specified in the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) manpage, you can specify an item that should only apply to a directory by prefixing it with a &#8216;D&#8217;, or specify an item that should only apply to a file by prefixing it with a &#8216;F&#8217;. For example, the following will ensure that all directories get marked set-gid, that no files are other-writable, that both are user-writable and group-writable, and that both have consistent executability across all bits:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--chmod=Dg+s,ug+w,Fo-w,+X
</pre>
</dl>
</dl>
<dt>
<dd> Using octal mode numbers is also allowed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--chmod=D2775,F664
</pre>
</dl>
</dl>
<dt>
<dd> It is also legal to specify multiple <code>&#8211;chmod</code> options, as each additional option is just appended to the list of changes to make.</p>
<dt>
<dd> See the <code>&#8211;perms</code> and <code>&#8211;executability</code> options for how the resulting permission value can be applied to the files in the transfer.</p>
<dt><code>&#8211;owner</code>, <code>-o</code></p>
<dd> This option causes rsync to set the owner of the destination file to be the same as the source file, but only if the receiving rsync is being run as the super-user (see also the <code>&#8211;super</code> and <code>&#8211;fake-super</code> options). Without this option, the owner of new and/or transferred files are set to the invoking user on the receiving side.</p>
<dt>
<dd> The preservation of ownership will associate matching names by default, but may fall back to using the ID number in some circumstances (see also the <code>&#8211;numeric-ids</code> option for a full discussion).</p>
<dt><code>&#8211;group</code>, <code>-g</code></p>
<dd> This option causes rsync to set the group of the destination file to be the same as the source file. If the receiving program is not running as the super-user (or if <code>&#8211;no-super</code> was specified), only groups that the invoking user on the receiving side is a member of will be preserved. Without this option, the group is set to the default group of the invoking user on the receiving side.</p>
<dt>
<dd> The preservation of group information will associate matching names by default, but may fall back to using the ID number in some circumstances (see also the <code>&#8211;numeric-ids</code> option for a full discussion).</p>
<dt><code>&#8211;devices</code></p>
<dd> This option causes rsync to transfer character and block device files to the remote system to recreate these devices. If the receiving rsync is not being run as the super-user, rsync silently skips creating the device files (see also the <code>&#8211;super</code> and <code>&#8211;fake-super</code> options).</p>
<dt>
<dd> By default, rsync generates a &quot;non-regular file&quot; warning for each device file encountered when this option is not set. You can silence the warning by specifying <code>&#8211;info=nonreg0</code>.</p>
<dt><code>&#8211;specials</code></p>
<dd> This option causes rsync to transfer special files, such as named sockets and fifos. If the receiving rsync is not being run as the super-user, rsync silently skips creating the special files (see also the <code>&#8211;super</code> and <code>&#8211;fake-super</code> options).</p>
<dt>
<dd> By default, rsync generates a &quot;non-regular file&quot; warning for each special file encountered when this option is not set. You can silence the warning by specifying <code>&#8211;info=nonreg0</code>.</p>
<dt><code>-D</code></p>
<dd> The <code>-D</code> option is equivalent to &quot;<code>&#8211;devices</code> <code>&#8211;specials</code>&quot;.</p>
<dt><code>&#8211;copy-devices</code></p>
<dd> This tells rsync to treat a device on the sending side as a regular file, allowing it to be copied to a normal destination file (or another device if <code>&#8211;write-devices</code> was also specified).</p>
<dt>
<dd> This option is refused by default by an rsync daemon.</p>
<dt><code>&#8211;write-devices</code></p>
<dd> This tells rsync to treat a device on the receiving side as a regular file, allowing the writing of file data into a device.</p>
<dt>
<dd> This option implies the <code>&#8211;inplace</code> option.</p>
<dt>
<dd> Be careful using this, as you should know what devices are present on the receiving side of the transfer, especially when running rsync as root.</p>
<dt>
<dd> This option is refused by default by an rsync daemon.</p>
<dt><code>&#8211;times</code>, <code>-t</code></p>
<dd> This tells rsync to transfer modification times along with the files and update them on the remote system. Note that if this option is not used, the optimization that excludes files that have not been modified cannot be effective; in other words, a missing <code>-t</code> (or <code>-a</code>) will cause the next transfer to behave as if it used <code>&#8211;ignore-times</code> (<code>-I</code>), causing all files to be updated (though rsync&#8217;s delta-transfer algorithm will make the update fairly efficient if the files haven&#8217;t actually changed, you&#8217;re much better off using <code>-t</code>).</p>
<dt>
<dd> A modern rsync that is using transfer protocol 30 or 31 conveys a modify time using up to 8-bytes. If rsync is forced to speak an older protocol (perhaps due to the remote rsync being older than 3.0.0) a modify time is conveyed using 4-bytes. Prior to 3.2.7, these shorter values could convey a date range of 13-Dec-1901 to 19-Jan-2038. Beginning with 3.2.7, these 4-byte values now convey a date range of 1-Jan-1970 to 7-Feb-2106. If you have files dated older than 1970, make sure your rsync executables are upgraded so that the full range of dates can be conveyed.</p>
<dt><code>&#8211;atimes</code>, <code>-U</code></p>
<dd> This tells rsync to set the access (use) times of the destination files to the same value as the source files.</p>
<dt>
<dd> If repeated, it also sets the <code>&#8211;open-noatime</code> option, which can help you to make the sending and receiving systems have the same access times on the transferred files without needing to run rsync an extra time after a file is transferred.</p>
<dt>
<dd> Note that some older rsync versions (prior to 3.2.0) may have been built with a pre-release <code>&#8211;atimes</code> patch that does not imply <code>&#8211;open-noatime</code> when this option is repeated.</p>
<dt><code>&#8211;open-noatime</code></p>
<dd> This tells rsync to open files with the O_NOATIME flag (on systems that support it) to avoid changing the access time of the files that are being transferred. If your OS does not support the O_NOATIME flag then rsync will silently ignore this option. Note also that some filesystems are mounted to avoid updating the atime on read access even without the O_NOATIME flag being set.</p>
<dt><code>&#8211;crtimes</code>, <code>-N,</code></p>
<dd> This tells rsync to set the create times (newness) of the destination files to the same value as the source files.</p>
<dt><code>&#8211;omit-dir-times</code>, <code>-O</code></p>
<dd> This tells rsync to omit directories when it is preserving modification, access, and create times. If NFS is sharing the directories on the receiving side, it is a good idea to use <code>-O</code>. This option is inferred if you use <code>&#8211;backup</code> without <code>&#8211;backup-dir</code>.</p>
<dt>
<dd> This option also has the side-effect of avoiding early creation of missing sub-directories when incremental recursion is enabled, as discussed in the <code>&#8211;inc-recursive</code> section.</p>
<dt><code>&#8211;omit-link-times</code>, <code>-J</code></p>
<dd> This tells rsync to omit symlinks when it is preserving modification, access, and create times.</p>
<dt><code>&#8211;super</code></p>
<dd> This tells the receiving side to attempt super-user activities even if the receiving rsync wasn&#8217;t run by the super-user. These activities include: preserving users via the <code>&#8211;owner</code> option, preserving all groups (not just the current user&#8217;s groups) via the <code>&#8211;group</code> option, and copying devices via the <code>&#8211;devices</code> option. This is useful for systems that allow such activities without being the super-user, and also for ensuring that you will get errors if the receiving side isn&#8217;t being run as the super-user. To turn off super-user activities, the super-user can use <code>&#8211;no-super</code>.</p>
<dt><code>&#8211;fake-super</code></p>
<dd> When this option is enabled, rsync simulates super-user activities by saving/restoring the privileged attributes via special extended attributes that are attached to each file (as needed). This includes the file&#8217;s owner and group (if it is not the default), the file&#8217;s device info (device &amp; special files are created as empty text files), and any permission bits that we won&#8217;t allow to be set on the real file (e.g. the real file gets u-s,g-s,o-t for safety) or that would limit the owner&#8217;s access (since the real super-user can always access/change a file, the files we create can always be accessed/changed by the creating user). This option also handles ACLs (if <code>&#8211;acls</code> was specified) and non-user extended attributes (if <code>&#8211;xattrs</code> was specified).</p>
<dt>
<dd> This is a good way to backup data without using a super-user, and to store ACLs from incompatible systems.</p>
<dt>
<dd> The <code>&#8211;fake-super</code> option only affects the side where the option is used. To affect the remote side of a remote-shell connection, use the <code>&#8211;remote-option</code> (<code>-M</code>) option:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -av -M--fake-super /src/ host:/dest/
</pre>
</dl>
</dl>
<dt>
<dd> For a local copy, this option affects both the source and the destination. If you wish a local copy to enable this option just for the destination files, specify <code>-M&#8211;fake-super</code>. If you wish a local copy to enable this option just for the source files, combine <code>&#8211;fake-super</code> with <code>-M&#8211;super</code>.</p>
<dt>
<dd> This option is overridden by both <code>&#8211;super</code> and <code>&#8211;no-super</code>.</p>
<dt>
<dd> See also the <code>fake super</code> setting in the daemon&#8217;s rsyncd.conf file.</p>
<dt><code>&#8211;sparse</code>, <code>-S</code></p>
<dd> Try to handle sparse files efficiently so they take up less space on the destination. If combined with <code>&#8211;inplace</code> the file created might not end up with sparse blocks with some combinations of kernel version and/or filesystem type. If <code>&#8211;whole-file</code> is in effect (e.g. for a local copy) then it will always work because rsync truncates the file prior to writing out the updated version.</p>
<dt>
<dd> Note that versions of rsync older than 3.1.3 will reject the combination of <code>&#8211;sparse</code> and <code>&#8211;inplace</code>.</p>
<dt><code>&#8211;preallocate</code></p>
<dd> This tells the receiver to allocate each destination file to its eventual size before writing data to the file. Rsync will only use the real filesystem-level preallocation support provided by Linux&#8217;s <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) system call or Cygwin&#8217;s <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3), not the slow glibc implementation that writes a null byte into each block.</p>
<dt>
<dd> Without this option, larger files may not be entirely contiguous on the filesystem, but with this option rsync will probably copy more slowly. If the destination is not an extent-supporting filesystem (such as ext4, xfs, NTFS, etc.), this option may have no positive effect at all.</p>
<dt>
<dd> If combined with <code>&#8211;sparse</code>, the file will only have sparse blocks (as opposed to allocated sequences of null bytes) if the kernel version and filesystem type support creating holes in the allocated data.</p>
<dt><code>&#8211;dry-run</code>, <code>-n</code></p>
<dd> This makes rsync perform a trial run that doesn&#8217;t make any changes (and produces mostly the same output as a real run). It is most commonly used in combination with the <code>&#8211;verbose</code> (<code>-v</code>) and/or <code>&#8211;itemize-changes</code> (<code>-i</code>) options to see what an rsync command is going to do before one actually runs it.</p>
<dt>
<dd> The output of <code>&#8211;itemize-changes</code> is supposed to be exactly the same on a dry run and a subsequent real run (barring intentional trickery and system call failures); if it isn&#8217;t, that&#8217;s a bug. Other output should be mostly unchanged, but may differ in some areas. Notably, a dry run does not send the actual data for file transfers, so <code>&#8211;progress</code> has no effect, the &quot;bytes sent&quot;, &quot;bytes received&quot;, &quot;literal data&quot;, and &quot;matched data&quot; statistics are too small, and the &quot;speedup&quot; value is equivalent to a run where no file transfers were needed.</p>
<dt><code>&#8211;whole-file</code>, <code>-W</code></p>
<dd> This option disables rsync&#8217;s delta-transfer algorithm, which causes all transferred files to be sent whole. The transfer may be faster if this option is used when the bandwidth between the source and destination machines is higher than the bandwidth to disk (especially when the &quot;disk&quot; is actually a networked filesystem). This is the default when both the source and destination are specified as local paths, but only if no batch-writing option is in effect.</p>
<dt><code>&#8211;no-whole-file</code>, <code>&#8211;no-W</code></p>
<dd> Disable whole-file updating when it is enabled by default for a local transfer. This usually slows rsync down, but it can be useful if you are trying to minimize the writes to the destination file (if combined with <code>&#8211;inplace</code>) or for testing the checksum-based update algorithm.</p>
<dt>
<dd> See also the <code>&#8211;whole-file</code> option.</p>
<dt><code>&#8211;checksum-choice=STR</code>, <code>&#8211;cc=STR</code></p>
<dd> This option overrides the checksum algorithms. If one algorithm name is specified, it is used for both the transfer checksums and (assuming <code>&#8211;checksum</code> is specified) the pre-transfer checksums. If two comma-separated names are supplied, the first name affects the transfer checksums, and the second name affects the pre-transfer checksums (<code>-c</code>).</p>
<dt>
<dd> The checksum options that you may be able to use are:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>auto</code> (the default automatic choice)</p>
<dt>o</p>
<dd> <code>xxh128</code></p>
<dt>o</p>
<dd> <code>xxh3</code></p>
<dt>o</p>
<dd> <code>xxh64</code> (aka <code>xxhash</code>)</p>
<dt>o</p>
<dd> <code>md5</code></p>
<dt>o</p>
<dd> <code>md4</code></p>
<dt>o</p>
<dd> <code>sha1</code></p>
<dt>o</p>
<dd> <code>none</code></dl>
</dl>
<dt>
<dd> Run <code>rsync &#8211;version</code> to see the default checksum list compiled into your version (which may differ from the list above).</p>
<dt>
<dd> If &quot;none&quot; is specified for the first (or only) name, the <code>&#8211;whole-file</code> option is forced on and no checksum verification is performed on the transferred data. If &quot;none&quot; is specified for the second (or only) name, the <code>&#8211;checksum</code> option cannot be used.</p>
<dt>
<dd> The &quot;auto&quot; option is the default, where rsync bases its algorithm choice on a negotiation between the client and the server as follows:</p>
<dt>
<dd> When both sides of the transfer are at least 3.2.0, rsync chooses the first algorithm in the client&#8217;s list of choices that is also in the server&#8217;s list of choices. If no common checksum choice is found, rsync exits with an error. If the remote rsync is too old to support checksum negotiation, a value is chosen based on the protocol version (which chooses between MD5 and various flavors of MD4 based on protocol age).</p>
<dt>
<dd> The default order can be customized by setting the environment variable <code>RSYNC_CHECKSUM_LIST</code> to a space-separated list of acceptable checksum names. If the string contains a &quot;<code>&amp;</code>&quot; character, it is separated into the &quot;client string &amp; server string&quot;, otherwise the same string applies to both. If the string (or string portion) contains no non-whitespace characters, the default checksum list is used. This method does not allow you to specify the transfer checksum separately from the pre-transfer checksum, and it discards &quot;auto&quot; and all unknown checksum names. A list with only invalid names results in a failed negotiation.</p>
<dt>
<dd> The use of the <code>&#8211;checksum-choice</code> option overrides this environment list.</p>
<dt><code>&#8211;one-file-system</code>, <code>-x</code></p>
<dd> This tells rsync to avoid crossing a filesystem boundary when recursing. This does not limit the user&#8217;s ability to specify items to copy from multiple filesystems, just rsync&#8217;s recursion through the hierarchy of each directory that the user specified, and also the analogous recursion on the receiving side during deletion. Also keep in mind that rsync treats a &quot;bind&quot; mount to the same device as being on the same filesystem.</p>
<dt>
<dd> If this option is repeated, rsync omits all mount-point directories from the copy. Otherwise, it includes an empty directory at each mount-point it encounters (using the attributes of the mounted directory because those of the underlying mount-point directory are inaccessible).</p>
<dt>
<dd> If rsync has been told to collapse symlinks (via <code>&#8211;copy-links</code> or <code>&#8211;copy-unsafe-links</code>), a symlink to a directory on another device is treated like a mount-point. Symlinks to non-directories are unaffected by this option.</p>
<dt><code>&#8211;ignore-non-existing</code>, <code>&#8211;existing</code></p>
<dd> This tells rsync to skip creating files (including directories) that do not exist yet on the destination. If this option is combined with the <code>&#8211;ignore-existing</code> option, no files will be updated (which can be useful if all you want to do is delete extraneous files).</p>
<dt>
<dd> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects.</p>
<dt><code>&#8211;ignore-existing</code></p>
<dd> This tells rsync to skip updating files that already exist on the destination (this does <i>not</i> ignore existing directories, or nothing would get done). See also <code>&#8211;ignore-non-existing</code>.</p>
<dt>
<dd> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects.</p>
<dt>
<dd> This option can be useful for those doing backups using the <code>&#8211;link-dest</code> option when they need to continue a backup run that got interrupted. Since a <code>&#8211;link-dest</code> run is copied into a new directory hierarchy (when it is used properly), using [<code>&#8211;ignore-existing</code> will ensure that the already-handled files don&#8217;t get tweaked (which avoids a change in permissions on the hard-linked files). This does mean that this option is only looking at the existing files in the destination hierarchy itself.</p>
<dt>
<dd> When <code>&#8211;info=skip2</code> is used rsync will output &quot;FILENAME exists (INFO)&quot; messages where the INFO indicates one of &quot;type change&quot;, &quot;sum change&quot; (requires <code>-c</code>), &quot;file change&quot; (based on the quick check), &quot;attr change&quot;, or &quot;uptodate&quot;. Using <code>&#8211;info=skip1</code> (which is also implied by 2 <code>-v</code> options) outputs the exists message without the INFO suffix.</p>
<dt><code>&#8211;remove-source-files</code></p>
<dd> This tells rsync to remove from the sending side the files (meaning non-directories) that are a part of the transfer and have been successfully duplicated on the receiving side.</p>
<dt>
<dd> Note that you should only use this option on source files that are quiescent. If you are using this to move files that show up in a particular directory over to another host, make sure that the finished files get renamed into the source directory, not directly written into it, so that rsync can&#8217;t possibly transfer a file that is not yet fully written. If you can&#8217;t first write the files into a different directory, you should use a naming idiom that lets rsync avoid transferring files that are not yet finished (e.g. name the file &quot;foo.new&quot; when it is written, rename it to &quot;foo&quot; when it is done, and then use the option <code>&#8211;exclude=&#8217;*.new&#8217;</code> for the rsync transfer).</p>
<dt>
<dd> Starting with 3.1.0, rsync will skip the sender-side removal (and output an error) if the file&#8217;s size or modify time has not stayed unchanged.</p>
<dt>
<dd> Starting with 3.2.6, a local rsync copy will ensure that the sender does not remove a file the receiver just verified, such as when the user accidentally makes the source and destination directory the same path.</p>
<dt><code>&#8211;delete</code></p>
<dd> This tells rsync to delete extraneous files from the receiving side (ones that aren&#8217;t on the sending side), but only for the directories that are being synchronized. You must have asked rsync to send the whole directory (e.g. &quot;<code>dir</code>&quot; or &quot;<code>dir/</code>&quot;) without using a wildcard for the directory&#8217;s contents (e.g. &quot;<code>dir/*</code>&quot;) since the wildcard is expanded by the shell and rsync thus gets a request to transfer individual files, not the files&#8217; parent directory. Files that are excluded from the transfer are also excluded from being deleted unless you use the <code>&#8211;delete-excluded</code> option or mark the rules as only matching on the sending side (see the include/exclude modifiers in the FILTER RULES section).</p>
<dt>
<dd> Prior to rsync 2.6.7, this option would have no effect unless <code>&#8211;recursive</code> was enabled. Beginning with 2.6.7, deletions will also occur when <code>&#8211;dirs</code> (<code>-d</code>) is enabled, but only for directories whose contents are being copied.</p>
<dt>
<dd> This option can be dangerous if used incorrectly! It is a very good idea to first try a run using the <code>&#8211;dry-run</code> (<code>-n</code>) option to see what files are going to be deleted.</p>
<dt>
<dd> If the sending side detects any I/O errors, then the deletion of any files at the destination will be automatically disabled. This is to prevent temporary filesystem failures (such as NFS errors) on the sending side from causing a massive deletion of files on the destination. You can override this with the <code>&#8211;ignore-errors</code> option.</p>
<dt>
<dd> The <code>&#8211;delete</code> option may be combined with one of the &#8211;delete-WHEN options without conflict, as well as <code>&#8211;delete-excluded</code>. However, if none of the <code>&#8211;delete-WHEN</code> options are specified, rsync will choose the <code>&#8211;delete-during</code> algorithm when talking to rsync 3.0.0 or newer, or the <code>&#8211;delete-before</code> algorithm when talking to an older rsync. See also <code>&#8211;delete-delay</code> and <code>&#8211;delete-after</code>.</p>
<dt><code>&#8211;delete-before</code></p>
<dd> Request that the file-deletions on the receiving side be done before the transfer starts. See <code>&#8211;delete</code> (which is implied) for more details on file-deletion.</p>
<dt>
<dd> Deleting before the transfer is helpful if the filesystem is tight for space and removing extraneous files would help to make the transfer possible. However, it does introduce a delay before the start of the transfer, and this delay might cause the transfer to timeout (if <code>&#8211;timeout</code> was specified). It also forces rsync to use the old, non-incremental recursion algorithm that requires rsync to scan all the files in the transfer into memory at once (see <code>&#8211;recursive</code>).</p>
<dt><code>&#8211;delete-during</code>, <code>&#8211;del</code></p>
<dd> Request that the file-deletions on the receiving side be done incrementally as the transfer happens. The per-directory delete scan is done right before each directory is checked for updates, so it behaves like a more efficient <code>&#8211;delete-before</code>, including doing the deletions prior to any per-directory filter files being updated. This option was first added in rsync version 2.6.4. See <code>&#8211;delete</code> (which is implied) for more details on file-deletion.</p>
<dt><code>&#8211;delete-delay</code></p>
<dd> Request that the file-deletions on the receiving side be computed during the transfer (like <code>&#8211;delete-during</code>), and then removed after the transfer completes. This is useful when combined with <code>&#8211;delay-updates</code> and/or <code>&#8211;fuzzy</code>, and is more efficient than using <code>&#8211;delete-after</code> (but can behave differently, since <code>&#8211;delete-after</code> computes the deletions in a separate pass after all updates are done). If the number of removed files overflows an internal buffer, a temporary file will be created on the receiving side to hold the names (it is removed while open, so you shouldn&#8217;t see it during the transfer). If the creation of the temporary file fails, rsync will try to fall back to using <code>&#8211;delete-after</code> (which it cannot do if <code>&#8211;recursive</code> is doing an incremental scan). See <code>&#8211;delete</code> (which is implied) for more details on file-deletion.</p>
<dt><code>&#8211;delete-after</code></p>
<dd> Request that the file-deletions on the receiving side be done after the transfer has completed. This is useful if you are sending new per-directory merge files as a part of the transfer and you want their exclusions to take effect for the delete phase of the current transfer. It also forces rsync to use the old, non-incremental recursion algorithm that requires rsync to scan all the files in the transfer into memory at once (see <code>&#8211;recursive</code>). See <code>&#8211;delete</code> (which is implied) for more details on file-deletion.</p>
<dt>
<dd> See also the <code>&#8211;delete-delay</code> option that might be a faster choice for those that just want the deletions to occur at the end of the transfer.</p>
<dt><code>&#8211;delete-excluded</code></p>
<dd> This option turns any unqualified exclude/include rules into server-side rules that do not affect the receiver&#8217;s deletions.</p>
<dt>
<dd> By default, an exclude or include has both a server-side effect (to &quot;hide&quot; and &quot;show&quot; files when building the server&#8217;s file list) and a receiver-side effect (to &quot;protect&quot; and &quot;risk&quot; files when deletions are occurring). Any rule that has no modifier to specify what sides it is executed on will be instead treated as if it were a server-side rule only, avoiding any &quot;protect&quot; effects of the rules.</p>
<dt>
<dd> A rule can still apply to both sides even with this option specified if the rule is given both the sender &amp; receiver modifier letters (e.g., <code>-f&#8217;-sr foo&#8217;</code>). Receiver-side protect/risk rules can also be explicitly specified to limit the deletions. This saves you from having to edit a bunch of <code>-f&#8217;- foo&#8217;</code> rules into <code>-f&#8217;-s foo&#8217;</code> (aka <code>-f&#8217;H foo&#8217;</code>) rules (not to mention the corresponding includes).</p>
<dt>
<dd> See the FILTER RULES section for more information. See <code>&#8211;delete</code> (which is implied) for more details on deletion.</p>
<dt><code>&#8211;ignore-missing-args</code></p>
<dd> When rsync is first processing the explicitly requested source files (e.g. command-line arguments or <code>&#8211;files-from</code> entries), it is normally an error if the file cannot be found. This option suppresses that error, and does not try to transfer the file. This does not affect subsequent vanished-file errors if a file was initially found to be present and later is no longer there.</p>
<dt><code>&#8211;delete-missing-args</code></p>
<dd> This option takes the behavior of the (implied) <code>&#8211;ignore-missing-args</code> option a step farther: each missing arg will become a deletion request of the corresponding destination file on the receiving side (should it exist). If the destination file is a non-empty directory, it will only be successfully deleted if <code>&#8211;force</code> or <code>&#8211;delete</code> are in effect. Other than that, this option is independent of any other type of delete processing.</p>
<dt>
<dd> The missing source files are represented by special file-list entries which display as a &quot;<code>*missing</code>&quot; entry in the <code>&#8211;list-only</code> output.</p>
<dt><code>&#8211;ignore-errors</code></p>
<dd> Tells <code>&#8211;delete</code> to go ahead and delete files even when there are I/O errors.</p>
<dt><code>&#8211;force</code></p>
<dd> This option tells rsync to delete a non-empty directory when it is to be replaced by a non-directory. This is only relevant if deletions are not active (see <code>&#8211;delete</code> for details).</p>
<dt>
<dd> Note for older rsync versions: <code>&#8211;force</code> used to still be required when using <code>&#8211;delete-after</code>, and it used to be non-functional unless the <code>&#8211;recursive</code> option was also enabled.</p>
<dt><code>&#8211;max-delete=NUM</code></p>
<dd> This tells rsync not to delete more than NUM files or directories. If that limit is exceeded, all further deletions are skipped through the end of the transfer. At the end, rsync outputs a warning (including a count of the skipped deletions) and exits with an error code of 25 (unless some more important error condition also occurred).</p>
<dt>
<dd> Beginning with version 3.0.0, you may specify <code>&#8211;max-delete=0</code> to be warned about any extraneous files in the destination without removing any of them. Older clients interpreted this as &quot;unlimited&quot;, so if you don&#8217;t know what version the client is, you can use the less obvious <code>&#8211;max-delete=-1</code> as a backward-compatible way to specify that no deletions be allowed (though really old versions didn&#8217;t warn when the limit was exceeded).</p>
<dt><code>&#8211;max-size=SIZE</code></p>
<dd> This tells rsync to avoid transferring any file that is larger than the specified SIZE. A numeric value can be suffixed with a string to indicate the numeric units or left unqualified to specify bytes. Feel free to use a fractional value along with the units, such as <code>&#8211;max-size=1.5m</code>.</p>
<dt>
<dd> This option is a TRANSFER RULE, so don&#8217;t expect any exclude side effects.</p>
<dt>
<dd> The first letter of a units string can be <code>B</code> (bytes), <code>K</code> (kilo), <code>M</code> (mega), <code>G</code> (giga), <code>T</code> (tera), or <code>P</code> (peta). If the string is a single char or has &quot;ib&quot; added to it (e.g. &quot;G&quot; or &quot;GiB&quot;) then the units are multiples of 1024. If you use a two-letter suffix that ends with a &quot;B&quot; (e.g. &quot;kb&quot;) then you get units that are multiples of 1000. The string&#8217;s letters can be any mix of upper and lower-case that you want to use.</p>
<dt>
<dd> Finally, if the string ends with either &quot;+1&quot; or &quot;-1&quot;, it is offset by one byte in the indicated direction. The largest possible value is usually <code>8192P-1</code>.</p>
<dt>
<dd> Examples: <code>&#8211;max-size=1.5mb-1</code> is 1499999 bytes, and <code>&#8211;max-size=2g+1</code> is 2147483649 bytes.</p>
<dt>
<dd> Note that rsync versions prior to 3.1.0 did not allow <code>&#8211;max-size=0</code>.</p>
<dt><code>&#8211;min-size=SIZE</code></p>
<dd> This tells rsync to avoid transferring any file that is smaller than the specified SIZE, which can help in not transferring small, junk files. See the <code>&#8211;max-size</code> option for a description of SIZE and other info.</p>
<dt>
<dd> Note that rsync versions prior to 3.1.0 did not allow <code>&#8211;min-size=0</code>.</p>
<dt><code>&#8211;max-alloc=SIZE</code></p>
<dd> By default rsync limits an individual malloc/realloc to about 1GB in size. For most people this limit works just fine and prevents a protocol error causing rsync to request massive amounts of memory. However, if you have many millions of files in a transfer, a large amount of server memory, and you don&#8217;t want to split up your transfer into multiple parts, you can increase the per-allocation limit to something larger and rsync will consume more memory.</p>
<dt>
<dd> Keep in mind that this is not a limit on the total size of allocated memory. It is a sanity-check value for each individual allocation.</p>
<dt>
<dd> See the <code>&#8211;max-size</code> option for a description of how SIZE can be specified. The default suffix if none is given is bytes.</p>
<dt>
<dd> Beginning in 3.2.3, a value of 0 specifies no limit.</p>
<dt>
<dd> You can set a default value using the environment variable <code>RSYNC_MAX_ALLOC</code> using the same SIZE values as supported by this option. If the remote rsync doesn&#8217;t understand the <code>&#8211;max-alloc</code> option, you can override an environmental value by specifying <code>&#8211;max-alloc=1g</code>, which will make rsync avoid sending the option to the remote side (because &quot;1G&quot; is the default).</p>
<dt><code>&#8211;block-size=SIZE</code>, <code>-B</code></p>
<dd> This forces the block size used in rsync&#8217;s delta-transfer algorithm to a fixed value. It is normally selected based on the size of each file being updated. See the technical report for details.</p>
<dt>
<dd> Beginning in 3.2.3 the SIZE can be specified with a suffix as detailed in the <code>&#8211;max-size</code> option. Older versions only accepted a byte count.</p>
<dt><code>&#8211;rsh=COMMAND</code>, <code>-e</code></p>
<dd> This option allows you to choose an alternative remote shell program to use for communication between the local and remote copies of rsync. Typically, rsync is configured to use ssh by default, but you may prefer to use rsh on a local network.</p>
<dt>
<dd> If this option is used with <code>[user@]host::module/path</code>, then the remote shell <i>COMMAND</i> will be used to run an rsync daemon on the remote host, and all data will be transmitted through that remote shell connection, rather than through a direct socket connection to a running rsync daemon on the remote host. See the USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION section above.</p>
<dt>
<dd> Beginning with rsync 3.2.0, the <code>RSYNC_PORT</code> environment variable will be set when a daemon connection is being made via a remote-shell connection. It is set to 0 if the default daemon port is being assumed, or it is set to the value of the rsync port that was specified via either the <code>&#8211;port</code> option or a non-empty port value in an <code>rsync://</code> URL. This allows the script to discern if a non-default port is being requested, allowing for things such as an SSL or stunnel helper script to connect to a default or alternate port.</p>
<dt>
<dd> Command-line arguments are permitted in COMMAND provided that COMMAND is presented to rsync as a single argument. You must use spaces (not tabs or other whitespace) to separate the command and args from each other, and you can use single- and/or double-quotes to preserve spaces in an argument (but not backslashes). Note that doubling a single-quote inside a single-quoted string gives you a single-quote; likewise for double-quotes (though you need to pay attention to which quotes your shell is parsing and which quotes rsync is parsing). Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
-e 'ssh -p 2234'
-e 'ssh -o &quot;ProxyCommand nohup ssh firewall nc -w1 %h %p&quot;'
</pre>
</dl>
</dl>
<dt>
<dd> (Note that ssh users can alternately customize site-specific connect options in their .ssh/config file.)</p>
<dt>
<dd> You can also choose the remote shell program using the <code>RSYNC_RSH</code> environment variable, which accepts the same range of values as <code>-e</code>.</p>
<dt>
<dd> See also the <code>&#8211;blocking-io</code> option which is affected by this option.</p>
<dt><code>&#8211;rsync-path=PROGRAM</code></p>
<dd> Use this to specify what program is to be run on the remote machine to start-up rsync. Often used when rsync is not in the default remote-shell&#8217;s path (e.g. <code>&#8211;rsync-path=/usr/local/bin/rsync</code>). Note that PROGRAM is run with the help of a shell, so it can be any program, script, or command sequence you&#8217;d care to run, so long as it does not corrupt the standard-in &amp; standard-out that rsync is using to communicate.</p>
<dt>
<dd> One tricky example is to set a different default directory on the remote machine for use with the <code>&#8211;relative</code> option. For instance:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -avR --rsync-path=&quot;cd /a/b &amp;&amp; rsync&quot; host:c/d /e/
</pre>
</dl>
</dl>
<dt><code>&#8211;remote-option=OPTION</code>, <code>-M</code></p>
<dd> This option is used for more advanced situations where you want certain effects to be limited to one side of the transfer only. For instance, if you want to pass <code>&#8211;log-file=FILE</code> and <code>&#8211;fake-super</code> to the remote system, specify it like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -av -M --log-file=foo -M--fake-super src/ dest/
</pre>
</dl>
</dl>
<dt>
<dd> If you want to have an option affect only the local side of a transfer when it normally affects both sides, send its negation to the remote side. Like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -av -x -M--no-x src/ dest/
</pre>
</dl>
</dl>
<dt>
<dd> Be cautious using this, as it is possible to toggle an option that will cause rsync to have a different idea about what data to expect next over the socket, and that will make it fail in a cryptic fashion.</p>
<dt>
<dd> Note that you should use a separate <code>-M</code> option for each remote option you want to pass. On older rsync versions, the presence of any spaces in the remote-option arg could cause it to be split into separate remote args, but this requires the use of <code>&#8211;old-args</code> in a modern rsync.</p>
<dt>
<dd> When performing a local transfer, the &quot;local&quot; side is the sender and the &quot;remote&quot; side is the receiver.</p>
<dt>
<dd> Note some versions of the popt option-parsing library have a bug in them that prevents you from using an adjacent arg with an equal in it next to a short option letter (e.g. <code>-M&#8211;log-file=/tmp/foo</code>). If this bug affects your version of popt, you can use the version of popt that is included with rsync.</p>
<dt><code>&#8211;cvs-exclude</code>, <code>-C</code></p>
<dd> This is a useful shorthand for excluding a broad range of files that you often don&#8217;t want to transfer between systems. It uses a similar algorithm to CVS to determine if a file should be ignored.</p>
<dt>
<dd> The exclude list is initialized to exclude the following items (these initial items are marked as perishable &#8212; see the FILTER RULES section):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>RCS</code> <code>SCCS</code> <code>CVS</code> <code>CVS.adm</code> <code>RCSLOG</code> <code>cvslog.*</code> <code>tags</code> <code>TAGS</code> <code>.make.state</code> <code>.nse_depinfo</code> <code>*~</code> <code>#*</code> <code>.#*</code> <code>,*</code> <code>_$*</code> <code>*$</code> <code>*.old</code> <code>*.bak</code> <code>*.BAK</code> <code>*.orig</code> <code>*.rej</code> <code>.del-*</code> <code>*.a</code> <code>*.olb</code> <code>*.o</code> <code>*.obj</code> <code>*.so</code> <code>*.exe</code> <code>*.Z</code> <code>*.elc</code> <code>*.ln</code> <code>core</code> <code>.svn/</code> <code>.git/</code> <code>.hg/</code> <code>.bzr/</code></dl>
</dl>
<dt>
<dd> then, files listed in a $HOME/.cvsignore are added to the list and any files listed in the CVSIGNORE environment variable (all cvsignore names are delimited by whitespace).</p>
<dt>
<dd> Finally, any file is ignored if it is in the same directory as a .cvsignore file and matches one of the patterns listed therein. Unlike rsync&#8217;s filter/exclude files, these patterns are split on whitespace. See the <code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1) manual for more information.</p>
<dt>
<dd> If you&#8217;re combining <code>-C</code> with your own <code>&#8211;filter</code> rules, you should note that these CVS excludes are appended at the end of your own rules, regardless of where the <code>-C</code> was placed on the command-line. This makes them a lower priority than any rules you specified explicitly. If you want to control where these CVS excludes get inserted into your filter rules, you should omit the <code>-C</code> as a command-line option and use a combination of <code>&#8211;filter=:C</code> and <code>&#8211;filter=-C</code> (either on your command-line or by putting the &quot;:C&quot; and &quot;-C&quot; rules into a filter file with your other rules). The first option turns on the per-directory scanning for the .cvsignore file. The second option does a one-time import of the CVS excludes mentioned above.</p>
<dt><code>&#8211;filter=RULE</code>, <code>-f</code></p>
<dd> This option allows you to add rules to selectively exclude certain files from the list of files to be transferred. This is most useful in combination with a recursive transfer.</p>
<dt>
<dd> You may use as many <code>&#8211;filter</code> options on the command line as you like to build up the list of files to exclude. If the filter contains whitespace, be sure to quote it so that the shell gives the rule to rsync as a single argument. The text below also mentions that you can use an underscore to replace the space that separates a rule from its arg.</p>
<dt>
<dd> See the FILTER RULES section for detailed information on this option.</p>
<dt><code>-F</code></p>
<dd> The <code>-F</code> option is a shorthand for adding two <code>&#8211;filter</code> rules to your command. The first time it is used is a shorthand for this rule:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--filter='dir-merge /.rsync-filter'
</pre>
</dl>
</dl>
<dt>
<dd> This tells rsync to look for per-directory .rsync-filter files that have been sprinkled through the hierarchy and use their rules to filter the files in the transfer. If <code>-F</code> is repeated, it is a shorthand for this rule:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--filter='exclude .rsync-filter'
</pre>
</dl>
</dl>
<dt>
<dd> This filters out the .rsync-filter files themselves from the transfer.</p>
<dt>
<dd> See the FILTER RULES section for detailed information on how these options work.</p>
<dt><code>&#8211;exclude=PATTERN</code></p>
<dd> This option is a simplified form of the <code>&#8211;filter</code> option that specifies an exclude rule and does not allow the full rule-parsing syntax of normal filter rules. This is equivalent to specifying <code>-f&#8217;- PATTERN&#8217;</code>.</p>
<dt>
<dd> See the FILTER RULES section for detailed information on this option.</p>
<dt><code>&#8211;exclude-from=FILE</code></p>
<dd> This option is related to the <code>&#8211;exclude</code> option, but it specifies a FILE that contains exclude patterns (one per line). Blank lines in the file are ignored, as are whole-line comments that start with &#8216;<code>;</code>&#8216; or &#8216;<code>#</code>&#8216; (filename rules that contain those characters are unaffected).</p>
<dt>
<dd> If a line begins with &quot;<code>&#8211;&nbsp;</code>&quot; (dash, space) or &quot;<code>+&nbsp;</code>&quot; (plus, space), then the type of rule is being explicitly specified as an exclude or an include (respectively). Any rules without such a prefix are taken to be an exclude.</p>
<dt>
<dd> If a line consists of just &quot;<code>!</code>&quot;, then the current filter rules are cleared before adding any further rules.</p>
<dt>
<dd> If <i>FILE</i> is &#8216;<code>&#8211;</code>&#8216;, the list will be read from standard input.</p>
<dt><code>&#8211;include=PATTERN</code></p>
<dd> This option is a simplified form of the <code>&#8211;filter</code> option that specifies an include rule and does not allow the full rule-parsing syntax of normal filter rules. This is equivalent to specifying <code>-f&#8217;+&nbsp;PATTERN&#8217;</code>.</p>
<dt>
<dd> See the FILTER RULES section for detailed information on this option.</p>
<dt><code>&#8211;include-from=FILE</code></p>
<dd> This option is related to the <code>&#8211;include</code> option, but it specifies a FILE that contains include patterns (one per line). Blank lines in the file are ignored, as are whole-line comments that start with &#8216;<code>;</code>&#8216; or &#8216;<code>#</code>&#8216; (filename rules that contain those characters are unaffected).</p>
<dt>
<dd> If a line begins with &quot;<code>&#8211;&nbsp;</code>&quot; (dash, space) or &quot;<code>+&nbsp;</code>&quot; (plus, space), then the type of rule is being explicitly specified as an exclude or an include (respectively). Any rules without such a prefix are taken to be an include.</p>
<dt>
<dd> If a line consists of just &quot;<code>!</code>&quot;, then the current filter rules are cleared before adding any further rules.</p>
<dt>
<dd> If <i>FILE</i> is &#8216;<code>&#8211;</code>&#8216;, the list will be read from standard input.</p>
<dt><code>&#8211;files-from=FILE</code></p>
<dd> Using this option allows you to specify the exact list of files to transfer (as read from the specified FILE or &#8216;<code>&#8211;</code>&#8216; for standard input). It also tweaks the default behavior of rsync to make transferring just the specified files and directories easier:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> The <code>&#8211;relative</code> (<code>-R</code>) option is implied, which preserves the path information that is specified for each item in the file (use <code>&#8211;no-relative</code> or <code>&#8211;no-R</code> if you want to turn that off).</p>
<dt>o</p>
<dd> The <code>&#8211;dirs</code> (<code>-d</code>) option is implied, which will create directories specified in the list on the destination rather than noisily skipping them (use <code>&#8211;no-dirs</code> or <code>&#8211;no-d</code> if you want to turn that off).</p>
<dt>o</p>
<dd> The <code>&#8211;archive</code> (<code>-a</code>) option&#8217;s behavior does not imply <code>&#8211;recursive</code> (<code>-r</code>), so specify it explicitly, if you want it.</p>
<dt>o</p>
<dd> These side-effects change the default state of rsync, so the position of the <code>&#8211;files-from</code> option on the command-line has no bearing on how other options are parsed (e.g. <code>-a</code> works the same before or after <code>&#8211;files-from</code>, as does <code>&#8211;no-R</code> and all other options).</dl>
</dl>
<dt>
<dd> The filenames that are read from the FILE are all relative to the source dir &#8212; any leading slashes are removed and no &quot;..&quot; references are allowed to go higher than the source dir. For example, take this command:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -a --files-from=/tmp/foo /usr remote:/backup
</pre>
</dl>
</dl>
<dt>
<dd> If /tmp/foo contains the string &quot;bin&quot; (or even &quot;/bin&quot;), the /usr/bin directory will be created as /backup/bin on the remote host. If it contains &quot;bin/&quot; (note the trailing slash), the immediate contents of the directory would also be sent (without needing to be explicitly mentioned in the file &#8212; this began in version 2.6.4). In both cases, if the <code>-r</code> option was enabled, that dir&#8217;s entire hierarchy would also be transferred (keep in mind that <code>-r</code> needs to be specified explicitly with <code>&#8211;files-from</code>, since it is not implied by <code>-a</code>. Also note that the effect of the (enabled by default) <code>-r</code> option is to duplicate only the path info that is read from the file &#8212; it does not force the duplication of the source-spec path (/usr in this case).</p>
<dt>
<dd> In addition, the <code>&#8211;files-from</code> file can be read from the remote host instead of the local host if you specify a &quot;host:&quot; in front of the file (the host must match one end of the transfer). As a short-cut, you can specify just a prefix of &quot;:&quot; to mean &quot;use the remote end of the transfer&quot;. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
rsync -a --files-from=:/path/file-list src:/ /tmp/copy
</pre>
</dl>
</dl>
<dt>
<dd> This would copy all the files specified in the /path/file-list file that was located on the remote &quot;src&quot; host.</p>
<dt>
<dd> If the <code>&#8211;iconv</code> and <code>&#8211;secluded-args</code> options are specified and the <code>&#8211;files-from</code> filenames are being sent from one host to another, the filenames will be translated from the sending host&#8217;s charset to the receiving host&#8217;s charset.</p>
<dt>
<dd> NOTE: sorting the list of files in the <code>&#8211;files-from</code> input helps rsync to be more efficient, as it will avoid re-visiting the path elements that are shared between adjacent entries. If the input is not sorted, some path elements (implied directories) may end up being scanned multiple times, and rsync will eventually unduplicate them after they get turned into file-list elements.</p>
<dt><code>&#8211;from0</code>, <code>-0</code></p>
<dd> This tells rsync that the rules/filenames it reads from a file are terminated by a null (&#8216;
