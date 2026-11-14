---
title: "borg(1)"
name: "borg"
section: "1"
letter: "b"
url: "/docs/linux/man/1-borg/"
description: "borg – BorgBackup is a deduplicating backup program with optional compression and authenticated encryption."
---

<h2>NAME</h2>
<p> borg &#8211; BorgBackup is a deduplicating backup program with optional compression and authenticated encryption. </p>
<p> Borg consists of a number of commands. Each command accepts a number of arguments and options. The following sections will describe each command in detail.</p>
<h2>GENERAL</h2>
<h3>Repository URLs</h3>
<p> <code>Local filesystem</code> (or locally mounted network filesystem): </p>
<p> <code>/path/to/repo</code> &#8211; filesystem path to repo directory, absolute path </p>
<p> <code>path/to/repo</code> &#8211; filesystem path to repo directory, relative path </p>
<p> Also, stuff like <code>~/path/to/repo</code> or <code>~other/path/to/repo</code> works (this is expanded by your shell). </p>
<p> Note: you may also prepend a <code>file://</code> to a filesystem path to get URL style. </p>
<p> <code>Remote repositories</code> accessed via ssh <i>user [at] host</i>: </p>
<p> <code>user [at] host:/path/to/repo</code> &#8211; remote repo, absolute path </p>
<p> <code><a href="ssh://user@host:port/path/to/repo">ssh://user@host:port/path/to/repo</a></code> &#8211; same, alternative syntax, port can be given </p>
<p> <code>Remote repositories with relative pathes</code> can be given using this syntax: </p>
<p> <code>user [at] host:path/to/repo</code> &#8211; path relative to current directory </p>
<p> <code>user [at] host:~/path/to/repo</code> &#8211; path relative to user&#8217;s home directory </p>
<p> <code>user [at] host:~other/path/to/repo</code> &#8211; path relative to other&#8217;s home directory </p>
<p> Note: giving <code>user [at] host:/./path/to/repo</code> or <code>user [at] host:/~/path/to/repo</code> or <code>user [at] host:/~other/path/to/repo</code> is also supported, but not required here. </p>
<p> <code>Remote repositories with relative pathes, alternative syntax with port</code>: </p>
<p> <code><a href="ssh://user@host:port/./path/to/repo">ssh://user@host:port/./path/to/repo</a></code> &#8211; path relative to current directory </p>
<p> <code><a href="ssh://user@host:port/~/path/to/repo">ssh://user@host:port/~/path/to/repo</a></code> &#8211; path relative to user&#8217;s home directory </p>
<p> <code><a href="ssh://user@host:port/~other/path/to/repo">ssh://user@host:port/~other/path/to/repo</a></code> &#8211; path relative to other&#8217;s home directory </p>
<p> If you frequently need the same repo URL, it is a good idea to set the <code>BORG_REPO</code> environment variable to set a default for the repo URL: </p>
<pre>
export BORG_REPO='<a href="ssh://user@host:port/path/to/repo'">ssh://user@host:port/path/to/repo'</a>
</pre>
<p> Then just leave away the repo URL if only a repo URL is needed and you want to use the default &#8211; it will be read from BORG_REPO then. </p>
<p> Use <code>::</code> syntax to give the repo URL when syntax requires giving a positional argument for the repo (e.g. <code>borg mount :: /mnt</code>).</p>
<h3>Repository / Archive Locations</h3>
<p> Many commands want either a repository (just give the repo URL, see above) or an archive location, which is a repo URL followed by <code>::archive_name</code>. </p>
<p> Archive names must not contain the <code>/</code> (slash) character. For simplicity, maybe also avoid blanks or other characters that have special meaning on the shell or in a filesystem (borg mount will use the archive name as directory name). </p>
<p> If you have set BORG_REPO (see above) and an archive location is needed, use <code>::archive_name</code> &#8211; the repo URL part is then read from BORG_REPO.</p>
<h3>Type of log output</h3>
<p> The log level of the builtin logging configuration defaults to WARNING. This is because we want Borg to be mostly silent and only output warnings, errors and critical messages. </p>
<p> Log levels: DEBUG &lt; INFO &lt; WARNING &lt; ERROR &lt; CRITICAL </p>
<p> Use <code>&#8211;debug</code> to set DEBUG log level &#8211; to get debug, info, warning, error and critical level output. </p>
<p> Use <code>&#8211;info</code> (or <code>-v</code> or <code>&#8211;verbose</code>) to set INFO log level &#8211; to get info, warning, error and critical level output. </p>
<p> Use <code>&#8211;warning</code> (default) to set WARNING log level &#8211; to get warning, error and critical level output. </p>
<p> Use <code>&#8211;error</code> to set ERROR log level &#8211; to get error and critical level output. </p>
<p> Use <code>&#8211;critical</code> to set CRITICAL log level &#8211; to get critical level output. </p>
<p> While you can set misc. log levels, do not expect that every command will give different output on different log levels &#8211; it&#8217;s just a possibility. </p>
<p> <code>WARNING:</code> Options &#8211;critical and &#8211;error are provided for completeness, their usage is not recommended as you might miss important information. </p>
<p> <code>WARNING:</code> While some options (like <code>&#8211;stats</code> or <code>&#8211;list</code>) will emit more informational messages, you have to use INFO (or lower) log level to make them show up in log output. Use <code>-v</code> or a logging configuration.</p>
<h3>Return codes</h3>
<p> Borg can exit with the following return codes (rc): </p>
<pre>
0 = success (logged as INFO)
1 = warning (operation reached its normal end, but there were warnings -
    you should check the log, logged as WARNING)
2 = error (like a fatal error, a local or remote exception, the operation
    did not reach its normal end, logged as ERROR)
128+N = killed by signal N (e.g. 137 == kill -9)
</pre>
<p> If you use <code>&#8211;show-rc</code>, the return code is also logged at the indicated level as the last log entry.</p>
<h3>Environment Variables</h3>
<p> Borg uses some environment variables for automation:</p>
<dl>
<dt><code>General:</code></p>
<dd>
<dt><code>BORG_REPO</code></p>
<dd> When set, use the value to give the default repository location. If a command needs an archive parameter, you can abbreviate as <i>::archive</i>. If a command needs a repository parameter, you can either leave it away or abbreviate as <i>::</i>, if a positional parameter is required.</p>
<dt><code>BORG_PASSPHRASE</code></p>
<dd> When set, use the value to answer the passphrase question for encrypted repositories.</p>
<dt><code>BORG_DISPLAY_PASSPHRASE</code></p>
<dd> When set, use the value to answer the &quot;display the passphrase for verification&quot; question when defining a new passphrase for encrypted repositories.</p>
<dt><code>BORG_LOGGING_CONF</code></p>
<dd> When set, use the given filename as <i>INI</i>-style logging configuration.</p>
<dt><code>BORG_RSH</code></p>
<dd> When set, use this command instead of <code>ssh</code>. This can be used to specify ssh options, such as a custom identity file <code>ssh -i /path/to/private/key</code>. See <code>man ssh</code> for other options.</p>
<dt><code>BORG_REMOTE_PATH</code></p>
<dd> When set, use the given path/filename as remote path (default is &quot;borg&quot;). Using <code>&#8211;remote-path PATH</code> commandline option overrides the environment variable.</p>
<dt><code>BORG_FILES_CACHE_TTL</code></p>
<dd> When set to a numeric value, this determines the maximum &quot;time to live&quot; for the files cache entries (default: 20). The files cache is used to quickly determine whether a file is unchanged. The FAQ explains this more detailed in: <i>always_chunking</i></p>
<dt><code>TMPDIR</code></p>
<dd> where temporary files are stored (might need a lot of temporary space for some operations)</p>
<dt><code>Some automatic answerers (if set, they automatically answer confirmation questions):</code></p>
<dd>
<dt><code>BORG_UNKNOWN_UNENCRYPTED_REPO_ACCESS_IS_OK=no (or =yes)</code></p>
<dd> For &quot;Warning: Attempting to access a previously unknown unencrypted repository&quot;</p>
<dt><code>BORG_RELOCATED_REPO_ACCESS_IS_OK=no (or =yes)</code></p>
<dd> For &quot;Warning: The repository at location &#8230; was previously located at &#8230;&quot;</p>
<dt><code>BORG_CHECK_I_KNOW_WHAT_I_AM_DOING=NO (or =YES)</code></p>
<dd> For &quot;Warning: &#8216;check &#8211;repair&#8217; is an experimental feature that might result in data loss.&quot;</p>
<dt><code>BORG_DELETE_I_KNOW_WHAT_I_AM_DOING=NO (or =YES)</code></p>
<dd> For &quot;You requested to completely DELETE the repository <i>including</i> all archives it contains:&quot; </p>
<p> Note: answers are case sensitive. setting an invalid answer value might either give the default answer or ask you interactively, depending on whether retries are allowed (they by default are allowed). So please test your scripts interactively before making them a non-interactive script.</p>
<dt><code>Directories:</code></p>
<dd>
<dt><code>BORG_KEYS_DIR</code></p>
<dd> Default to &#8216;~/.config/borg/keys&#8217;. This directory contains keys for encrypted repositories.</p>
<dt><code>BORG_SECURITY_DIR</code></p>
<dd> Default to &#8216;~/.config/borg/security&#8217;. This directory is used by Borg to track various pieces of security-related data.</p>
<dt><code>BORG_CACHE_DIR</code></p>
<dd> Default to &#8216;~/.cache/borg&#8217;. This directory contains the local cache and might need a lot of space for dealing with big repositories).</p>
<dt><code>Building:</code></p>
<dd>
<dt><code>BORG_OPENSSL_PREFIX</code></p>
<dd> Adds given OpenSSL header file directory to the default locations (setup.py).</p>
<dt><code>BORG_LZ4_PREFIX</code></p>
<dd> Adds given LZ4 header file directory to the default locations (setup.py). </p>
<p> Please note:</p>
<dt>&bull;</p>
<dd> be very careful when using the &quot;yes&quot; sayers, the warnings with prompt exist for your / your data&#8217;s security/safety</p>
<dt>&bull;</p>
<dd> also be very careful when putting your passphrase into a script, make sure it has appropriate file permissions (e.g. mode 600, root:root).</dl>
<h3>Resource Usage</h3>
<p> Borg might use a lot of resources depending on the size of the data set it is dealing with. </p>
<p> If one uses Borg in a client/server way (with a ssh: repository), the resource usage occurs in part on the client and in another part on the server. </p>
<p> If one uses Borg as a single process (with a filesystem repo), all the resource usage occurs in that one process, so just add up client + server to get the approximate resource usage.</p>
<dl>
<dt><code>CPU client:</code></p>
<dd> borg create: does chunking, hashing, compression, crypto (high CPU usage) chunks cache sync: quite heavy on CPU, doing lots of hashtable operations. borg extract: crypto, decompression (medium to high CPU usage) borg check: similar to extract, but depends on options given. borg prune / borg delete archive: low to medium CPU usage borg delete repo: done on the server It won&#8217;t go beyond 100% of 1 core as the code is currently single-threaded. Especially higher zlib and lzma compression levels use significant amounts of CPU cycles. Crypto might be cheap on the CPU (if hardware accelerated) or expensive (if not).</p>
<dt><code>CPU server:</code></p>
<dd> It usually doesn&#8217;t need much CPU, it just deals with the key/value store (repository) and uses the repository index for that. </p>
<p> borg check: the repository check computes the checksums of all chunks (medium CPU usage) borg delete repo: low CPU usage</p>
<dt><code>CPU (only for client/server operation):</code></p>
<dd> When using borg in a client/server way with a <i>ssh:-type</i> repo, the ssh processes used for the transport layer will need some CPU on the client and on the server due to the crypto they are doing &#8211; esp. if you are pumping big amounts of data.</p>
<dt><code>Memory (RAM) client:</code></p>
<dd> The chunks index and the files index are read into memory for performance reasons. Might need big amounts of memory (see below). Compression, esp. lzma compression with high levels might need substantial amounts of memory.</p>
<dt><code>Memory (RAM) server:</code></p>
<dd> The server process will load the repository index into memory. Might need considerable amounts of memory, but less than on the client (see below).</p>
<dt><code>Chunks index (client only):</code></p>
<dd> Proportional to the amount of data chunks in your repo. Lots of chunks in your repo imply a big chunks index. It is possible to tweak the chunker params (see create options).</p>
<dt><code>Files index (client only):</code></p>
<dd> Proportional to the amount of files in your last backups. Can be switched off (see create options), but next backup might be much slower if you do. The speed benefit of using the files cache is proportional to file size.</p>
<dt><code>Repository index (server only):</code></p>
<dd> Proportional to the amount of data chunks in your repo. Lots of chunks in your repo imply a big repository index. It is possible to tweak the chunker params (see create options) to influence the amount of chunks being created.</p>
<dt><code>Temporary files (client):</code></p>
<dd> Reading data and metadata from a FUSE mounted repository will consume up to the size of all deduplicated, small chunks in the repository. Big chunks won&#8217;t be locally cached.</p>
<dt><code>Temporary files (server):</code></p>
<dd> None.</p>
<dt><code>Cache files (client only):</code></p>
<dd> Contains the chunks index and files index (plus a collection of single- archive chunk indexes which might need huge amounts of disk space, depending on archive count and size &#8211; see FAQ about how to reduce).</p>
<dt><code>Network (only for client/server operation):</code></p>
<dd> If your repository is remote, all deduplicated (and optionally compressed/ encrypted) data of course has to go over the connection (ssh: repo url). If you use a locally mounted network filesystem, additionally some copy operations used for transaction support also go over the connection. If you backup multiple sources to one target repository, additional traffic happens for cache resynchronization. </p>
<p> In case you are interested in more details (like formulas), please see <i>internals</i>.</dl>
<h3>Units</h3>
<p> To display quantities, Borg takes care of respecting the usual conventions of scale. Disk sizes are displayed in <i>decimal</i>, using powers of ten (so <code>kB</code> means 1000 bytes). For memory usage, <i>binary prefixes</i> are used, and are indicated using the <i>IEC binary prefixes</i>, using powers of two (so <code>KiB</code> means 1024 bytes).</p>
<h3>Date and Time</h3>
<p> We format date and time conforming to ISO-8601, that is: YYYY-MM-DD and HH:MM:SS (24h clock). </p>
<p> For more information about that, see: <i><a rel="nofollow" href="https://xkcd.com/1179/">https://xkcd.com/1179/</a></i> </p>
<p> Unless otherwise noted, we display local date and time. Internally, we store and process date and time as UTC.</p>
<h2>BORG INIT</h2>
<pre><code>
usage: borg init [-h] [--critical] [--error] [--warning] [--info] [--debug]
                 [--lock-wait N] [--show-rc] [--no-files-cache] [--umask M]
                 [--remote-path PATH] [-e {none,keyfile,repokey}] [-a]
                 [REPOSITORY]
Initialize an empty repository
positional arguments:
  REPOSITORY            repository to create
optional arguments:
  -h, --help            show this help message and exit
  --critical            work on log level CRITICAL
  --error               work on log level ERROR
  --warning             work on log level WARNING (default)
  --info, -v, --verbose
                        work on log level INFO
  --debug               work on log level DEBUG
  --lock-wait N         wait for the lock, but max. N seconds (default: 1).
  --show-rc             show/log the return code (rc)
  --no-files-cache      do not load/update the file metadata cache used to
                        detect unchanged files
  --umask M             set umask to M (local and remote, default: 0077)
  --remote-path PATH    set remote path to executable (default: "borg")
  -e {none,keyfile,repokey}, --encryption {none,keyfile,repokey}
                        select encryption key mode (default: "repokey")
  -a, --append-only     create an append-only mode repository
</code></pre>
<h3>Description</h3>
<p> This command initializes an empty repository. A repository is a filesystem directory containing the deduplicated data from zero or more archives. Encryption can be enabled at repository init time.</p>
<h3>Examples</h3>
<p>#Local repository(default is to use encryption in repokey mode)<br />
$ borg init / path / to / repo<br />
#Local repository(no encryption)<br />
                              $ borg init&#8211; encryption = none / path / to / repo<br />
#Remote repository(accesses a remote borg via ssh)<br />
                                                                                $ borg init user[at] hostname : backup<br />
#Remote repository(store the key your home dir)<br />
                                                                                                                    $ borg init&#8211; encryption = keyfile user[at] hostname : backup</p>
<p> Important notes about encryption: </p>
<p> It is not recommended to disable encryption. Repository encryption protects you e.g. against the case that an attacker has access to your backup repository. </p>
<p> But be careful with the key / the passphrase: </p>
<p> If you want &quot;passphrase-only&quot; security, use the <code>repokey</code> mode. The key will be stored inside the repository (in its &quot;config&quot; file). In above mentioned attack scenario, the attacker will have the key (but not the passphrase). </p>
<p> If you want &quot;passphrase and having-the-key&quot; security, use the <code>keyfile</code> mode. The key will be stored in your home directory (in <code>.config/borg/keys</code>). In the attack scenario, the attacker who has just access to your repo won&#8217;t have the key (and also not the passphrase). </p>
<p> Make a backup copy of the key file (<code>keyfile</code> mode) or repo config file (<code>repokey</code> mode) and keep it at a safe place, so you still have the key in case it gets corrupted or lost. Also keep the passphrase at a safe place. The backup that is encrypted with that key won&#8217;t help you with that, of course. </p>
<p> Make sure you use a good passphrase. Not too short, not too simple. The real encryption / decryption key is encrypted with / locked by your passphrase. If an attacker gets your key, he can&#8217;t unlock and use it without knowing the passphrase. </p>
<p> Be careful with special or non-ascii characters in your passphrase:</p>
<dl>
<dt>&bull;</p>
<dd> Borg processes the passphrase as unicode (and encodes it as utf-8), so it does not have problems dealing with even the strangest characters.</p>
<dt>&bull;</p>
<dd> BUT: that does not necessarily apply to your OS / VM / keyboard configuration. </p>
<p> So better use a long passphrase made from simple ascii chars than one that includes non-ascii stuff or characters that are hard/impossible to enter on a different keyboard layout. </p>
<p> You can change your passphrase for existing repos at any time, it won&#8217;t affect the encryption/decryption key or other secrets.</dl>
<h2>BORG CREATE</h2>
<p>usage: borg create [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                   [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                   [&#8211;remote-path PATH] [-s] [-p] [&#8211;list]<br />
                   [&#8211;filter STATUSCHARS] [-e PATTERN]<br />
                   [&#8211;exclude-from EXCLUDEFILE] [&#8211;exclude-caches]<br />
                   [&#8211;exclude-if-present FILENAME] [&#8211;keep-tag-files]<br />
                   [-c SECONDS] [-x] [&#8211;numeric-owner] [&#8211;noatime] [&#8211;noctime]<br />
                   [&#8211;timestamp yyyy-mm-ddThh:mm:ss]<br />
                   [&#8211;chunker-params CHUNK_MIN_EXP,CHUNK_MAX_EXP,HASH_MASK_BITS,HASH_WINDOW_SIZE]<br />
                   [&#8211;ignore-inode] [-C COMPRESSION] [&#8211;read-special] [-n]<br />
                   ARCHIVE PATH [PATH &#8230;]<br />
Create new archive<br />
positional arguments:<br />
  ARCHIVE               name of archive to create (must be also a valid<br />
                        directory name)<br />
  PATH                  paths to archive<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  -s, &#8211;stats           print statistics for the created archive<br />
  -p, &#8211;progress        show progress display while creating the archive,<br />
                        showing Original, Compressed and Deduplicated sizes,<br />
                        followed by the Number of files seen and the path<br />
                        being processed, default: False<br />
  &#8211;list                output verbose list of items (files, dirs, &#8230;)<br />
  &#8211;filter STATUSCHARS  only display items with the given status characters<br />
  -e PATTERN, &#8211;exclude PATTERN<br />
                        exclude paths matching PATTERN<br />
  &#8211;exclude-from EXCLUDEFILE<br />
                        read exclude patterns from EXCLUDEFILE, one per line<br />
  &#8211;exclude-caches      exclude directories that contain a CACHEDIR.TAG file<br />
                        (http://www.brynosaurus.com/cachedir/spec.html)<br />
  &#8211;exclude-if-present FILENAME<br />
                        exclude directories that contain the specified file<br />
  &#8211;keep-tag-files      keep tag files of excluded caches/directories<br />
  -c SECONDS, &#8211;checkpoint-interval SECONDS<br />
                        write checkpoint every SECONDS seconds (Default: 300)<br />
  -x, &#8211;one-file-system<br />
                        stay in same file system<br />
  &#8211;numeric-owner       only store numeric user and group identifiers<br />
  &#8211;noatime             do not store atime into archive<br />
  &#8211;noctime             do not store ctime into archive<br />
  &#8211;timestamp yyyy-mm-ddThh:mm:ss<br />
                        manually specify the archive creation date/time (UTC).<br />
                        alternatively, give a reference file/directory.<br />
  &#8211;chunker-params CHUNK_MIN_EXP,CHUNK_MAX_EXP,HASH_MASK_BITS,HASH_WINDOW_SIZE<br />
                        specify the chunker parameters. default: 19,23,21,4095<br />
  &#8211;ignore-inode        ignore inode data in the file metadata cache used to<br />
                        detect unchanged files.<br />
  -C COMPRESSION, &#8211;compression COMPRESSION<br />
                        select compression algorithm (and level): none == no<br />
                        compression (default), lz4 == lz4, zlib == zlib<br />
                        (default level 6), zlib,0 .. zlib,9 == zlib (with<br />
                        level 0..9), lzma == lzma (default level 6), lzma,0 ..<br />
                        lzma,9 == lzma (with level 0..9).<br />
  &#8211;read-special        open and read block and char device files as well as<br />
                        FIFOs as if they were regular files. Also follows<br />
                        symlinks pointing to these kinds of files.<br />
  -n, &#8211;dry-run         do not create a backup archive</p>
<h3>Description</h3>
<p> This command creates a backup archive containing all files found while recursively traversing all paths specified. When giving &#8216;-&#8216; as path, borg will read data from standard input and create a file &#8216;stdin&#8217; in the created archive from that data. </p>
<p> The archive will consume almost no disk space for files or parts of files that have already been stored in other archives. </p>
<p> The archive name needs to be unique. It must not end in &#8216;.checkpoint&#8217; or &#8216;.checkpoint.N&#8217; (with N being a number), because these names are used for checkpoints and treated in special ways. </p>
<p> In the archive name, you may use the following placeholders: {now}, {utcnow}, {fqdn}, {hostname}, {user} and some others. </p>
<p> To speed up pulling backups over sshfs and similar network file systems which do not provide correct inode information the &#8211;ignore-inode flag can be used. This potentially decreases reliability of change detection, while avoiding always reading all files on these file systems. </p>
<p> See the output of the &quot;borg help patterns&quot; command for more help on exclude patterns. See the output of the &quot;borg help placeholders&quot; command for more help on placeholders.</p>
<h3>Examples</h3>
<p>#Backup ~ / Documents into an archive named &#8220;my-documents&#8221;<br />
$ borg create / path / to / repo::my &#8211; documents ~ / Documents<br />
#same, but verbosely list all files as we process them<br />
                                                         $ borg create &#8211;<br />
    v&#8211; list / path / to / repo::my &#8211; documents ~ / Documents<br />
#Backup ~ / Documents and ~ / src but exclude pyc files<br />
                                                        $ borg create /<br />
                                          path / to / repo::my &#8211;<br />
    files ~ / Documents ~ / src&#8211; exclude &#8216;*.pyc&#8217;<br />
#Backup home directories excluding image thumbnails(i.e.only<br />
#/ home /*/.thumbnails is excluded, not /home/*/ * /.thumbnails)<br />
        $ borg create /<br />
        path / to / repo::my &#8211;<br />
    files / home&#8211; exclude &#8216;re:^/home/[^/]+/\.thumbnails/&#8217;<br />
#Do the same using a shell &#8211; style pattern<br />
        $ borg create /<br />
        path / to / repo::my &#8211;<br />
    files / home&#8211; exclude &#8216;sh:/home/*/.thumbnails&#8217;<br />
#Backup the root filesystem into an archive named &#8220;root-YYYY-MM-DD&#8221;<br />
#use zlib compression(good, but slow) &#8211; default is no compression<br />
        $ borg create &#8211;<br />
    C zlib,<br />
    6 / path / to / repo::root &#8211; {now : % Y &#8211; % m &#8211; % d} / &#8211;one &#8211; file &#8211; system<br />
#Make a big effort in fine granular deduplication(big chunk management<br />
#overhead, needs a lot of RAM and disk space, see formula in internals<br />
#docs &#8211; same parameters as borg &lt; 1.0 or attic):<br />
                                                                              $ borg create&#8211; chunker &#8211;<br />
        params 10,<br />
    23, 16, 4095 / path / to / repo::small / smallstuff<br />
#Backup a raw device(must not be active / in use / mounted at that time)<br />
                                                 $ dd if = / dev / sdx bs = 10M | borg create / path / to / repo::my &#8211; sdx &#8211;<br />
#No compression(default)<br />
                                                                                      $ borg create / path / to / repo::arch ~<br />
#Super fast, low compression<br />
                                                                                          $ borg create&#8211; compression lz4 /<br />
                                                                                          path / to / repo::arch ~<br />
#Less fast, higher compression(N = 0..9)<br />
                                                                                          $ borg create&#8211; compression zlib,<br />
                                                      N / path / to / repo::arch ~<br />
#Even slower, even higher compression(N = 0..9)<br />
                                                          $ borg create&#8211; compression lzma,<br />
                                                      N / path / to / repo::arch ~<br />
#Use short hostname, user name and current time in archive name<br />
                                                              $ borg create /<br />
                                                              path / to / repo::{hostname} &#8211;<br />
                                                          {user} &#8211;<br />
{<br />
    now<br />
}<br />
~<br />
#Similar, use the same datetime format as borg 1.1 will have as default<br />
        $ borg create /<br />
        path / to / repo::{hostname} &#8211;<br />
    {user} &#8211;<br />
{<br />
now:<br />
    % Y &#8211; % m &#8211; % dT % H : % M : % S<br />
}<br />
~<br />
#As above, but add nanoseconds<br />
        $ borg create /<br />
        path / to / repo::{hostname} &#8211;<br />
    {user} &#8211;<br />
{<br />
now:<br />
    % Y &#8211; % m &#8211; % dT % H : % M : % S.% f<br />
}<br />
~</p>
<h3>Notes</h3>
<dl>
<dt>&bull;</p>
<dd> the &#8211;exclude patterns are not like tar. In tar &#8211;exclude .bundler/gems will exclude foo/.bundler/gems. In borg it will not, you need to use &#8211;exclude &#8216;*/.bundler/gems&#8217; to get the same effect. See <code>borg help patterns</code> for more information.</dl>
<h2>BORG EXTRACT</h2>
<p>usage : borg extract[-h][&#8211;critical][&#8211;error][&#8211;warning][&#8211;info][&#8211;debug]<br />
                    [&#8211;lock &#8211; wait N][&#8211;show &#8211; rc][&#8211;no &#8211; files &#8211; cache][&#8211;umask M]<br />
                    [&#8211;remote &#8211; path PATH][&#8211;list][-n][-e PATTERN]<br />
                    [&#8211;exclude &#8211; from EXCLUDEFILE][&#8211;numeric &#8211; owner]<br />
                    [&#8211;strip &#8211; components NUMBER][&#8211;stdout][&#8211;sparse] ARCHIVE[PATH[PATH&#8230;]] Extract archive contents<br />
                        positional arguments : ARCHIVE archive to extract<br />
                                                   PATH paths to extract; patterns are supported<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  &#8211;list                output verbose list of items (files, dirs, &#8230;)<br />
  -n, &#8211;dry-run         do not actually change any files<br />
  -e PATTERN, &#8211;exclude PATTERN<br />
                        exclude paths matching PATTERN<br />
  &#8211;exclude-from EXCLUDEFILE<br />
                        read exclude patterns from EXCLUDEFILE, one per line<br />
  &#8211;numeric-owner       only obey numeric user and group identifiers<br />
  &#8211;strip-components NUMBER<br />
                        Remove the specified number of leading path elements.<br />
                        Pathnames with fewer elements will be silently<br />
                        skipped.<br />
  &#8211;stdout              write all extracted data to stdout<br />
  &#8211;sparse              create holes in output sparse file from all-zero<br />
                        chunks</p>
<h3>Description</h3>
<p> This command extracts the contents of an archive. By default the entire archive is extracted but a subset of files and directories can be selected by passing a list of <code>PATHs</code> as arguments. The file selection can further be restricted by using the <code>&#8211;exclude</code> option. </p>
<p> See the output of the &quot;borg help patterns&quot; command for more help on exclude patterns.</p>
<h3>Examples</h3>
<p>#Extract entire archive<br />
$ borg extract / path / to / repo::my &#8211; files<br />
#Extract entire archive and list files while processing<br />
                                            $ borg extract &#8211;<br />
        v&#8211; list / path / to / repo::my &#8211; files<br />
#Extract the &#8220;src&#8221; directory<br />
                                                  $ borg extract /<br />
                                              path / to / repo::my &#8211;<br />
        files home / USERNAME / src<br />
#Extract the &#8220;src&#8221; directory but exclude object files<br />
                                    $ borg extract /<br />
            path / to / repo::my &#8211;<br />
        files home / USERNAME / src&#8211; exclude &#8216;*.o&#8217;<br />
#Restore a raw device(must not be active / in use / mounted at that time)<br />
            $ borg extract&#8211; stdout /<br />
            path / to / repo::my &#8211;<br />
        sdx |<br />
    dd of = / dev / sdx bs = 10M</p>
<dl>
<dt><code>Note: currently, extract always writes into the current working directory (.),</code></p>
<dd> so make sure you <code>cd</code> to the right place before calling <code>borg extract</code>.</dl>
<h2>BORG CHECK</h2>
<p>usage: borg check [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                  [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                  [&#8211;remote-path PATH] [&#8211;repository-only] [&#8211;archives-only]<br />
                  [&#8211;repair] [&#8211;save-space] [&#8211;last N] [-P PREFIX]<br />
                  [REPOSITORY_OR_ARCHIVE]<br />
Check repository consistency<br />
positional arguments:<br />
  REPOSITORY_OR_ARCHIVE<br />
                        repository or archive to check consistency of<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  &#8211;repository-only     only perform repository checks<br />
  &#8211;archives-only       only perform archives checks<br />
  &#8211;repair              attempt to repair any inconsistencies found<br />
  &#8211;save-space          work slower, but using less space<br />
  &#8211;last N              only check last N archives (Default: all)<br />
  -P PREFIX, &#8211;prefix PREFIX<br />
                        only consider archive names starting with this prefix</p>
<h3>Description</h3>
<p> The check command verifies the consistency of a repository and the corresponding archives. </p>
<p> First, the underlying repository data files are checked:</p>
<dl>
<dt>&bull;</p>
<dd> For all segments the segment magic (header) is checked</p>
<dt>&bull;</p>
<dd> For all objects stored in the segments, all metadata (e.g. crc and size) and all data is read. The read data is checked by size and CRC. Bit rot and other types of accidental damage can be detected this way.</p>
<dt>&bull;</p>
<dd> If we are in repair mode and a integrity error is detected for a segment, we try to recover as many objects from the segment as possible.</p>
<dt>&bull;</p>
<dd> In repair mode, it makes sure that the index is consistent with the data stored in the segments.</p>
<dt>&bull;</p>
<dd> If you use a remote repo server via ssh:, the repo check is executed on the repo server without causing significant network traffic.</p>
<dt>&bull;</p>
<dd> The repository check can be skipped using the &#8211;archives-only option. </p>
<p> Second, the consistency and correctness of the archive metadata is verified:</p>
<dt>&bull;</p>
<dd> Is the repo manifest present? If not, it is rebuilt from archive metadata chunks (this requires reading and decrypting of all metadata and data).</p>
<dt>&bull;</p>
<dd> Check if archive metadata chunk is present. if not, remove archive from manifest.</p>
<dt>&bull;</p>
<dd> For all files (items) in the archive, for all chunks referenced by these files, check if chunk is present. If a chunk is not present and we are in repair mode, replace it with a same-size replacement chunk of zeros. If a previously lost chunk reappears (e.g. via a later backup) and we are in repair mode, the all-zero replacement chunk will be replaced by the correct chunk. This requires reading of archive and file metadata, but not data.</p>
<dt>&bull;</p>
<dd> If we are in repair mode and we checked all the archives: delete orphaned chunks from the repo.</p>
<dt>&bull;</p>
<dd> if you use a remote repo server via ssh:, the archive check is executed on the client machine (because if encryption is enabled, the checks will require decryption and this is always done client-side, because key access will be required).</p>
<dt>&bull;</p>
<dd> The archive checks can be time consuming, they can be skipped using the &#8211;repository-only option.</dl>
<h2>BORG RENAME</h2>
<p>usage: borg rename [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                   [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                   [&#8211;remote-path PATH]<br />
                   ARCHIVE NEWNAME<br />
Rename an existing archive<br />
positional arguments:<br />
  ARCHIVE               archive to rename<br />
  NEWNAME               the new archive name to use<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)</p>
<h3>Description</h3>
<p> This command renames an archive in the repository.</p>
<h3>Examples</h3>
<pre>
$ borg create /path/to/repo::archivename ~
$ borg list /path/to/repo
archivename                          Mon, 2016-02-15 19:50:19
$ borg rename /path/to/repo::archivename newname
$ borg list /path/to/repo
newname                              Mon, 2016-02-15 19:50:19
</pre>
<h2>BORG LIST</h2>
<p>usage: borg list [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                 [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                 [&#8211;remote-path PATH] [&#8211;short] [&#8211;list-format LISTFORMAT]<br />
                 [-P PREFIX]<br />
                 [REPOSITORY_OR_ARCHIVE]<br />
List archive or repository contents<br />
positional arguments:<br />
  REPOSITORY_OR_ARCHIVE<br />
                        repository/archive to list contents of<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  &#8211;short               only print file/directory names, nothing else<br />
  &#8211;list-format LISTFORMAT<br />
                        specify format for archive file listing (default:<br />
                        &#8220;{mode} {user:6} {group:6} {size:8d} {isomtime}<br />
                        {path}{extra}{<br />
    NEWLINE}&#8221;) Special &#8220;{<br />
    formatkeys}&#8221; exists<br />
                        to list available keys<br />
  -P PREFIX, &#8211;prefix PREFIX<br />
                        only consider archive names starting with this prefix</p>
<h3>Description</h3>
<p> This command lists the contents of a repository or an archive.</p>
<h3>Examples</h3>
<p>$ borg list / path / to / repo Monday Mon, 2016 &#8211; 02 &#8211; 15 19 : 15 : 11 repo Mon, 2016 &#8211; 02 &#8211; 15 19 : 26 : 54 root &#8211; 2016 &#8211; 02 &#8211; 15 Mon, 2016 &#8211; 02 &#8211; 15 19 : 36 : 29 newname Mon, 2016 &#8211; 02 &#8211; 15 19 : 50 : 19 &#8230; $ borg list / path / to / repo::root &#8211; 2016 &#8211; 02 &#8211; 15 drwxr &#8211; xr &#8211; x root root 0 Mon, 2016 &#8211; 02 &#8211; 15 17 : 44 : 27.drwxrwxr &#8211; x root root 0 Mon, 2016 &#8211; 02 &#8211; 15 19 : 04 : 49 bin &#8211; rwxr &#8211; xr &#8211; x root root 1029624 Thu, 2014 &#8211; 11 &#8211; 13 00 : 08 : 51 bin / bash lrwxrwxrwx root root 0 Fri, 2015 &#8211; 03 &#8211; 27 20 : 24 : 26 bin / bzcmp-&gt;bzdiff &#8211; rwxr &#8211; xr &#8211; x root root 2140 Fri, 2015 &#8211; 03 &#8211; 27 20 : 24 : 22 bin / bzdiff&#8230; $ borg list / path / to / repo::archiveA&#8211; list &#8211; format = &#8220;{mode} {user:6} {group:6} {size:8d} {isomtime} {path}{extra}{NEWLINE}&#8221; drwxrwxr &#8211; x user user 0 Sun, 2015 &#8211; 02 &#8211; 01 11 : 00 : 00.drwxrwxr &#8211; x user user 0 Sun, 2015 &#8211; 02 &#8211; 01 11 : 00 : 00 code drwxrwxr &#8211; x user user 0 Sun, 2015 &#8211; 02 &#8211; 01 11 : 00 : 00 code / myproject &#8211; rw &#8211; rw &#8211; r&#8211; user user 1416192 Sun, 2015 &#8211; 02 &#8211; 01 11 : 00 : 00 code / myproject / file.ext&#8230;<br />
#see what is changed between archives, based on file modification time, size and file path<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        $ borg list /<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         path / to / repo::archiveA&#8211; list &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             format = &#8220;{mtime:%s}{TAB}{size}{TAB}{path}{LF}&#8221; | sort &#8211; n &gt; / tmp / list.archiveA $ borg list / path / to / repo::archiveB&#8211; list &#8211; format = &#8220;{mtime:%s}{TAB}{size}{TAB}{path}{LF}&#8221; | sort &#8211; n &gt; / tmp / list.archiveB $ diff &#8211; y / tmp / list.archiveA / tmp / list.archiveB 1422781200 0.1422781200 0.1422781200 0 code 1422781200 0 code 1422781200 0 code / myproject 1422781200 0 code / myproject 1422781200 1416192 code / myproject / file.ext | 1454664653 1416192 code / myproject / file.ext&#8230;</p>
<h2>BORG DELETE</h2>
<p>usage: borg delete [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                   [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                   [&#8211;remote-path PATH] [-p] [-s] [-c] [&#8211;force]<br />
                   [&#8211;save-space]<br />
                   [TARGET]<br />
Delete an existing repository or archive<br />
positional arguments:<br />
  TARGET                archive or repository to delete<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  -p, &#8211;progress        show progress display while deleting a single archive<br />
  -s, &#8211;stats           print statistics for the deleted archive<br />
  -c, &#8211;cache-only      delete only the local cache for the given repository<br />
  &#8211;force               force deletion of corrupted archives<br />
  &#8211;save-space          work slower, but using less space</p>
<h3>Description</h3>
<p> This command deletes an archive from the repository or the complete repository. Disk space is reclaimed accordingly. If you delete the complete repository, the local cache for it (if any) is also deleted.</p>
<h3>Examples</h3>
<pre>
# delete a single backup archive:
$ borg delete /path/to/repo::Monday
# delete the whole repository and the related local cache:
$ borg delete /path/to/repo
You requested to completely DELETE the repository *including* all archives it contains:
repo                                 Mon, 2016-02-15 19:26:54
root-2016-02-15                      Mon, 2016-02-15 19:36:29
newname                              Mon, 2016-02-15 19:50:19
Type 'YES' if you understand this and want to continue: YES
</pre>
<h2>BORG PRUNE</h2>
<p>usage: borg prune [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                  [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                  [&#8211;remote-path PATH] [-n] [&#8211;force] [-s] [&#8211;list]<br />
                  [&#8211;keep-within WITHIN] [-H HOURLY] [-d DAILY] [-w WEEKLY]<br />
                  [-m MONTHLY] [-y YEARLY] [-P PREFIX] [&#8211;save-space]<br />
                  [REPOSITORY]<br />
Prune repository archives according to specified rules<br />
positional arguments:<br />
  REPOSITORY            repository to prune<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  -n, &#8211;dry-run         do not change repository<br />
  &#8211;force               force pruning of corrupted archives<br />
  -s, &#8211;stats           print statistics for the deleted archive<br />
  &#8211;list                output verbose list of archives it keeps/prunes<br />
  &#8211;keep-within WITHIN  keep all archives within this time interval<br />
  -H HOURLY, &#8211;keep-hourly HOURLY<br />
                        number of hourly archives to keep<br />
  -d DAILY, &#8211;keep-daily DAILY<br />
                        number of daily archives to keep<br />
  -w WEEKLY, &#8211;keep-weekly WEEKLY<br />
                        number of weekly archives to keep<br />
  -m MONTHLY, &#8211;keep-monthly MONTHLY<br />
                        number of monthly archives to keep<br />
  -y YEARLY, &#8211;keep-yearly YEARLY<br />
                        number of yearly archives to keep<br />
  -P PREFIX, &#8211;prefix PREFIX<br />
                        only consider archive names starting with this prefix<br />
  &#8211;save-space          work slower, but using less space</p>
<h3>Description</h3>
<p> The prune command prunes a repository by deleting all archives not matching any of the specified retention options. This command is normally used by automated backup scripts wanting to keep a certain number of historic backups. </p>
<p> As an example, &quot;-d 7&quot; means to keep the latest backup on each day, up to 7 most recent days with backups (days without backups do not count). The rules are applied from hourly to yearly, and backups selected by previous rules do not count towards those of later rules. The time that each backup starts is used for pruning purposes. Dates and times are interpreted in the local timezone, and weeks go from Monday to Sunday. Specifying a negative number of archives to keep means that there is no limit. </p>
<p> The &quot;&#8211;keep-within&quot; option takes an argument of the form &quot;&lt;int&gt;&lt;char&gt;&quot;, where char is &quot;H&quot;, &quot;d&quot;, &quot;w&quot;, &quot;m&quot;, &quot;y&quot;. For example, &quot;&#8211;keep-within 2d&quot; means to keep all archives that were created within the past 48 hours. &quot;1m&quot; is taken to mean &quot;31d&quot;. The archives kept with this option do not count towards the totals specified by any other options. </p>
<p> If a prefix is set with -P, then only archives that start with the prefix are considered for deletion and only those archives count towards the totals specified by the rules. Otherwise, <i>all</i> archives in the repository are candidates for deletion! There is no automatic distinction between archives representing different contents. These need to be distinguished by specifying matching prefixes.</p>
<h3>Examples</h3>
<p> Be careful, prune is a potentially dangerous command, it will remove backup archives. </p>
<p> The default of prune is to apply to <code>all archives in the repository</code> unless you restrict its operation to a subset of the archives using <code>&#8211;prefix</code>. When using <code>&#8211;prefix</code>, be careful to choose a good prefix &#8211; e.g. do not use a prefix &quot;foo&quot; if you do not also want to match &quot;foobar&quot;. </p>
<p> It is strongly recommended to always run <code>prune -v &#8211;list &#8211;dry-run &#8230;</code> first so you will see what it would do without it actually doing anything. </p>
<p> There is also a visualized prune example in <code>docs/misc/prune-example.txt</code>. </p>
<p>#Keep 7 end of day and 4 additional end of week archives.<br />
#Do a dry &#8211; run without actually deleting anything.<br />
$ borg prune &#8211; v&#8211; list&#8211; dry &#8211; run&#8211; keep &#8211; daily = 7 &#8211;keep &#8211; weekly = 4 / path / to / repo<br />
#Same as above but only apply to archive names starting with the hostname<br />
#of the machine followed by a &#8220;-&#8221; character:<br />
                                                                                             $ borg prune &#8211;<br />
                                                                         v&#8211; list&#8211; keep &#8211; daily = 7 &#8211;keep &#8211; weekly = 4 &#8211;prefix = &#8216;{hostname}-&#8216; / path / to / repo<br />
#Keep 7 end of day, 4 additional end of week archives,<br />
#and an end of month archive for every month:<br />
                                                                                                                                                                    $ borg prune &#8211;<br />
                                                                                                                                    v&#8211; list&#8211; keep &#8211; daily = 7 &#8211;keep &#8211; weekly = 4 &#8211;keep &#8211; monthly = -1 / path / to / repo<br />
#Keep all backups in the last 10 days, 4 additional end of week archives,<br />
#and an end of month archive for every month:<br />
                                                                                                                                                                                                                            $ borg prune &#8211;<br />
                                                                                                                                                                                                       v&#8211; list&#8211; keep &#8211; within = 10d &#8211;keep &#8211; weekly = 4 &#8211;keep &#8211; monthly = -1 / path / to / repo</p>
<h2>BORG INFO</h2>
<p>usage: borg info [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                 [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                 [&#8211;remote-path PATH]<br />
                 ARCHIVE<br />
Show archive details such as disk space used<br />
positional arguments:<br />
  ARCHIVE               archive to display information about<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)</p>
<h3>Description</h3>
<p> This command displays some detailed information about the specified archive. </p>
<p> Please note that the deduplicated sizes of the individual archives do not add up to the deduplicated size of the repository (&quot;all archives&quot;), because the two are meaning different things:</p>
<dl>
<dt><code>This archive / deduplicated size = amount of data stored ONLY for this archive</code></p>
<dd> = unique chunks of this archive.</p>
<dt><code>All archives / deduplicated size = amount of data stored in the repo</code></p>
<dd> = all chunks in the repository.</dl>
<h3>Examples</h3>
<pre>
$ borg info /path/to/repo::root-2016-02-15
Name: root-2016-02-15
Fingerprint: 57c827621f21b000a8d363c1e163cc55983822b3afff3a96df595077a660be50
Hostname: myhostname
Username: root
Time (start): Mon, 2016-02-15 19:36:29
Time (end):   Mon, 2016-02-15 19:39:26
Command line: /usr/local/bin/borg create -v --list -C zlib,6 /path/to/repo::root-2016-02-15 / --one-file-system
Number of files: 38100
                       Original size      Compressed size    Deduplicated size
This archive:                1.33 GB            613.25 MB            571.64 MB
All archives:                1.63 GB            853.66 MB            584.12 MB
                       Unique chunks         Total chunks
Chunk index:                   36858                48844
</pre>
<h2>BORG MOUNT</h2>
<p>usage: borg mount [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                  [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                  [&#8211;remote-path PATH] [-f] [-o OPTIONS]<br />
                  REPOSITORY_OR_ARCHIVE MOUNTPOINT<br />
Mount archive or an entire repository as a FUSE filesystem<br />
positional arguments:<br />
  REPOSITORY_OR_ARCHIVE<br />
                        repository/archive to mount<br />
  MOUNTPOINT            where to mount filesystem<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  -f, &#8211;foreground      stay in foreground, do not daemonize<br />
  -o OPTIONS            Extra mount options</p>
<h3>Description</h3>
<p> This command mounts an archive as a FUSE filesystem. This can be useful for browsing an archive or restoring individual files. Unless the <code>&#8211;foreground</code> option is given the command will run in the background until the filesystem is <code>umounted</code>. </p>
<p> The BORG_MOUNT_DATA_CACHE_ENTRIES environment variable is meant for advanced users to tweak the performance. It sets the number of cached data chunks; additional memory usage can be up to ~8 MiB times this number. The default is the number of CPU cores. </p>
<p> For mount options, see the <a href="/docs/linux/man/8-fuse/">fuse</a>(8) manual page. Additional mount options supported by borg:</p>
<dl>
<dt>&bull;</p>
<dd> allow_damaged_files: by default damaged files (where missing chunks were replaced with runs of zeros by borg check &#8211;repair) are not readable and return EIO (I/O error). Set this option to read such files. </p>
<p> When the daemonized process receives a signal or crashes, it does not unmount. Unmounting in these cases could cause an active rsync or similar process to unintentionally delete data. </p>
<p> When running in the foreground ^C/SIGINT unmounts cleanly, but other signals or crashes do not.</dl>
<h2>BORG UMOUNT</h2>
<p>usage: borg umount [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                   [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                   [&#8211;remote-path PATH]<br />
                   MOUNTPOINT<br />
un-mount the FUSE filesystem<br />
positional arguments:<br />
  MOUNTPOINT            mountpoint of the filesystem to umount<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)</p>
<h3>Description</h3>
<p> This command un-mounts a FUSE filesystem that was mounted with <code>borg mount</code>. </p>
<p> This is a convenience wrapper that just calls the platform-specific shell command &#8211; usually this is either umount or fusermount -u.</p>
<h3>Examples</h3>
<pre>
$ borg mount /path/to/repo::root-2016-02-15 /tmp/mymountpoint
$ ls /tmp/mymountpoint
bin  boot  etc      home  lib  lib64  lost+found  media  mnt  opt  root  sbin  srv  tmp  usr  var
$ borg umount /tmp/mymountpoint
</pre>
<h2>BORG KEY EXPORT</h2>
<p>usage: borg key export [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info]<br />
                       [&#8211;debug] [&#8211;lock-wait N] [&#8211;show-rc]<br />
                       [&#8211;no-files-cache] [&#8211;umask M] [&#8211;remote-path PATH]<br />
                       [&#8211;paper] [&#8211;qr-html]<br />
                       [REPOSITORY] [PATH]<br />
Export the repository key for backup<br />
positional arguments:<br />
  REPOSITORY<br />
  PATH                  where to store the backup<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  &#8211;paper               Create an export suitable for printing and later type-<br />
                        in<br />
  &#8211;qr-html             Create an html file suitable for printing and later<br />
                        type-in or qr scan</p>
<h3>Description</h3>
<p> If repository encryption is used, the repository is inaccessible without the key. This command allows to backup this essential key. </p>
<p> There are two backup formats. The normal backup format is suitable for digital storage as a file. The <code>&#8211;paper</code> backup format is optimized for printing and typing in while importing, with per line checks to reduce problems with manual input. </p>
<p> For repositories using keyfile encryption the key is saved locally on the system that is capable of doing backups. To guard against loss of this key, the key needs to be backed up independently of the main data backup. </p>
<p> For repositories using the repokey encryption the key is saved in the repository in the config file. A backup is thus not strictly needed, but guards against the repository becoming inaccessible if the file is damaged for some reason.</p>
<h2>BORG KEY IMPORT</h2>
<p>usage: borg key import [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info]<br />
                       [&#8211;debug] [&#8211;lock-wait N] [&#8211;show-rc]<br />
                       [&#8211;no-files-cache] [&#8211;umask M] [&#8211;remote-path PATH]<br />
                       [&#8211;paper]<br />
                       [REPOSITORY] [PATH]<br />
Import the repository key from backup<br />
positional arguments:<br />
  REPOSITORY<br />
  PATH                  path to the backup<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  &#8211;paper               interactively import from a backup done with &#8211;paper</p>
<h3>Description</h3>
<p> This command allows to restore a key previously backed up with the export command. </p>
<p> If the <code>&#8211;paper</code> option is given, the import will be an interactive process in which each line is checked for plausibility before proceeding to the next line. For this format PATH must not be given.</p>
<h2>BORG CHANGE-PASSPHRASE</h2>
<p>usage: borg change-passphrase [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info]<br />
                              [&#8211;debug] [&#8211;lock-wait N] [&#8211;show-rc]<br />
                              [&#8211;no-files-cache] [&#8211;umask M]<br />
                              [&#8211;remote-path PATH]<br />
                              [REPOSITORY]<br />
Change repository key file passphrase<br />
positional arguments:<br />
  REPOSITORY<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)</p>
<h3>Description</h3>
<p> The key files used for repository encryption are optionally passphrase protected. This command can be used to change this passphrase.</p>
<h3>Examples</h3>
<pre>
# Create a key file protected repository
$ borg init --encryption=keyfile -v /path/to/repo
Initializing repository at &quot;/path/to/repo&quot;
Enter new passphrase:
Enter same passphrase again:
Remember your passphrase. Your data will be inaccessible without it.
Key in &quot;/root/.config/borg/keys/mnt_backup&quot; created.
Keep this key safe. Your data will be inaccessible without it.
Synchronizing chunks cache...
Archives: 0, w/ cached Idx: 0, w/ outdated Idx: 0, w/o cached Idx: 0.
Done.
# Change key file passphrase
$ borg change-passphrase -v /path/to/repo
Enter passphrase for key /root/.config/borg/keys/mnt_backup:
Enter new passphrase:
Enter same passphrase again:
Remember your passphrase. Your data will be inaccessible without it.
Key updated
</pre>
<h2>BORG SERVE</h2>
<p>usage: borg serve [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                  [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                  [&#8211;remote-path PATH] [&#8211;restrict-to-path PATH]<br />
                  [&#8211;append-only]<br />
Start in server mode. This command is usually not used manually.<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  &#8211;restrict-to-path PATH<br />
                        restrict repository access to PATH. Can be specified<br />
                        multiple times to allow the client access to several<br />
                        directories. Access to all sub-directories is granted<br />
                        implicitly;<br />
PATH doesn&#8217;t need to directly point to a repository.&#8211;append &#8211; only only allow appending to repository segment files</p>
<h3>Description</h3>
<p> This command starts a repository server process. This command is usually not used manually.</p>
<h3>Examples</h3>
<p> borg serve has special support for ssh forced commands (see <code>authorized_keys</code> example below): it will detect that you use such a forced command and extract the value of the <code>&#8211;restrict-to-path</code> option(s). It will then parse the original command that came from the client, makes sure that it is also <code>borg serve</code> and enforce path restriction(s) as given by the forced command. That way, other options given by the client (like <code>&#8211;info</code> or <code>&#8211;umask</code>) are preserved (and are not fixed by the forced command). </p>
<pre>
# Allow an SSH keypair to only run borg, and only have access to /path/to/repo.
# Use key options to disable unneeded and potentially dangerous SSH functionality.
# This will help to secure an automated remote backup system.
$ cat ~/.ssh/authorized_keys
command=&quot;borg serve --restrict-to-path /path/to/repo&quot;,no-pty,no-agent-forwarding,no-port-forwarding,no-X11-forwarding,no-user-rc ssh-rsa AAAAB3[...]
</pre>
<h2>BORG UPGRADE</h2>
<p>usage: borg upgrade [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info] [&#8211;debug]<br />
                    [&#8211;lock-wait N] [&#8211;show-rc] [&#8211;no-files-cache] [&#8211;umask M]<br />
                    [&#8211;remote-path PATH] [-p] [-n] [-i] [&#8211;force] [&#8211;tam]<br />
                    [&#8211;disable-tam]<br />
                    [REPOSITORY]<br />
upgrade a repository from a previous version<br />
positional arguments:<br />
  REPOSITORY            path to the repository to be upgraded<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)<br />
  -p, &#8211;progress        show progress display while upgrading the repository<br />
  -n, &#8211;dry-run         do not change repository<br />
  -i, &#8211;inplace         rewrite repository in place, with no chance of going<br />
                        back to older versions of the repository.<br />
  &#8211;force               Force upgrade<br />
  &#8211;tam                 Enable manifest authentication (in key and cache)<br />
                        (Borg 1.0.9 and later)<br />
  &#8211;disable-tam         Disable manifest authentication (in key and cache)</p>
<h3>Description</h3>
<p> Upgrade an existing Borg repository.</p>
<h3>Borg 1.x.y upgrades</h3>
<p> Use <code>borg upgrade &#8211;tam REPO</code> to require manifest authentication introduced with Borg 1.0.9 to address security issues. This means that modifying the repository after doing this with a version prior to 1.0.9 will raise a validation error, so only perform this upgrade after updating all clients using the repository to 1.0.9 or newer. </p>
<p> This upgrade should be done on each client for safety reasons. </p>
<p> If a repository is accidentally modified with a pre-1.0.9 client after this upgrade, use <code>borg upgrade &#8211;tam &#8211;force REPO</code> to remedy it. </p>
<p> If you routinely do this you might not want to enable this upgrade (which will leave you exposed to the security issue). You can reverse the upgrade by issuing <code>borg upgrade &#8211;disable-tam REPO</code>. </p>
<p> See <i><a rel="nofollow" href="https://borgbackup.readthedocs.io/en/stable/changes.html#pre-1-0-9-manifest-spoofing-vulnerability">https://borgbackup.readthedocs.io/en/stable/changes.html#pre-1-0-9-manifest-spoofing-vulnerability</a></i> for details.</p>
<h3>Attic and Borg 0.xx to Borg 1.x</h3>
<p> This currently supports converting an Attic repository to Borg and also helps with converting Borg 0.xx to 1.0. </p>
<p> Currently, only LOCAL repositories can be upgraded (issue #465). </p>
<p> It will change the magic strings in the repository&#8217;s segments to match the new Borg magic strings. The keyfiles found in $ATTIC_KEYS_DIR or ~/.attic/keys/ will also be converted and copied to $BORG_KEYS_DIR or ~/.config/borg/keys. </p>
<p> The cache files are converted, from $ATTIC_CACHE_DIR or ~/.cache/attic to $BORG_CACHE_DIR or ~/.cache/borg, but the cache layout between Borg and Attic changed, so it is possible the first backup after the conversion takes longer than expected due to the cache resync. </p>
<p> Upgrade should be able to resume if interrupted, although it will still iterate over all segments. If you want to start from scratch, use <i>borg delete</i> over the copied repository to make sure the cache files are also removed: borg delete borg </p>
<p> Unless <code>&#8211;inplace</code> is specified, the upgrade process first creates a backup copy of the repository, in REPOSITORY.upgrade-DATETIME, using hardlinks. This takes longer than in place upgrades, but is much safer and gives progress information (as opposed to <code>cp -al</code>). Once you are satisfied with the conversion, you can safely destroy the backup copy. </p>
<p> WARNING: Running the upgrade in place will make the current copy unusable with older version, with no way of going back to previous versions. This can PERMANENTLY DAMAGE YOUR REPOSITORY! Attic CAN NOT READ BORG REPOSITORIES, as the magic strings have changed. You have been warned.</p>
<h3>Examples</h3>
<pre>
# Upgrade the borg repository to the most recent version.
$ borg upgrade -v /path/to/repo
making a hardlink copy in /path/to/repo.upgrade-2016-02-15-20:51:55
opening attic repository with borg and converting
no key file found for repository
converting repo index /path/to/repo/index.0
converting 1 segments...
converting borg 0.xx to borg current
no key file found for repository
</pre>
<h3>Upgrading a passphrase encrypted attic repo</h3>
<p> attic offered a &quot;passphrase&quot; encryption mode, but this was removed in borg 1.0 and replaced by the &quot;repokey&quot; mode (which stores the passphrase-protected encryption key into the repository config). </p>
<p> Thus, to upgrade a &quot;passphrase&quot; attic repo to a &quot;repokey&quot; borg repo, 2 steps are needed, in this order:</p>
<dl>
<dt>&bull;</p>
<dd> borg upgrade repo</p>
<dt>&bull;</p>
<dd> borg migrate-to-repokey repo</dl>
<h2>BORG BREAK-LOCK</h2>
<p>usage: borg break-lock [-h] [&#8211;critical] [&#8211;error] [&#8211;warning] [&#8211;info]<br />
                       [&#8211;debug] [&#8211;lock-wait N] [&#8211;show-rc]<br />
                       [&#8211;no-files-cache] [&#8211;umask M] [&#8211;remote-path PATH]<br />
                       [REPOSITORY]<br />
Break the repository lock (e.g. in case it was left by a dead borg.<br />
positional arguments:<br />
  REPOSITORY            repository for which to break the locks<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;critical            work on log level CRITICAL<br />
  &#8211;error               work on log level ERROR<br />
  &#8211;warning             work on log level WARNING (default)<br />
  &#8211;info, -v, &#8211;verbose<br />
                        work on log level INFO<br />
  &#8211;debug               work on log level DEBUG<br />
  &#8211;lock-wait N         wait for the lock, but max. N seconds (default: 1).<br />
  &#8211;show-rc             show/log the return code (rc)<br />
  &#8211;no-files-cache      do not load/update the file metadata cache used to<br />
                        detect unchanged files<br />
  &#8211;umask M             set umask to M (local and remote, default: 0077)<br />
  &#8211;remote-path PATH    set remote path to executable (default: &#8220;borg&#8221;)</p>
<h3>Description</h3>
<p> This command breaks the repository and cache locks. Please use carefully and only while no borg process (on any machine) is trying to access the Cache or the Repository.</p>
<h2>MISCELLANEOUS HELP</h2>
<h3>borg help patterns</h3>
<p> Exclusion patterns support four separate styles, fnmatch, shell, regular expressions and path prefixes. By default, fnmatch is used. If followed by a colon (&#8216;:&#8217;) the first two characters of a pattern are used as a style selector. Explicit style selection is necessary when a non-default style is desired or when the desired pattern starts with two alphanumeric characters followed by a colon (i.e. <i>aa:something/*</i>). </p>
<p> <i>Fnmatch</i>, selector <i>fm:</i> This is the default style. These patterns use a variant of shell pattern syntax, with &#8216;*&#8217; matching any number of characters, &#8216;?&#8217; matching any single character, &#8216;[&#8230;]&#8217; matching any single character specified, including ranges, and &#8216;[!&#8230;]&#8217; matching any character not specified. For the purpose of these patterns, the path separator (&#8221; for Windows and &#8216;/&#8217; on other systems) is not treated specially. Wrap meta-characters in brackets for a literal match (i.e. <i>[?]</i> to match the literal character <i>?</i>). For a path to match a pattern, it must completely match from start to end, or must match from the start to just before a path separator. Except for the root path, paths will never end in the path separator when matching is attempted. Thus, if a given pattern ends in a path separator, a &#8216;*&#8217; is appended before matching is attempted. </p>
<p> Shell-style patterns, selector <i>sh:</i> Like fnmatch patterns these are similar to shell patterns. The difference is that the pattern may include <i>**/</i> for matching zero or more directory levels, <i>*</i> for matching zero or more arbitrary characters with the exception of any path separator. </p>
<p> Regular expressions, selector <i>re:</i> Regular expressions similar to those found in Perl are supported. Unlike shell patterns regular expressions are not required to match the complete path and any substring match is sufficient. It is strongly recommended to anchor patterns to the start (&#8216;^&#8217;), to the end (&#8216;$&#8217;) or both. Path separators (&#8221; for Windows and &#8216;/&#8217; on other systems) in paths are always normalized to a forward slash (&#8216;/&#8217;) before applying a pattern. The regular expression syntax is described in the <i>Python documentation for the re module</i>. </p>
<p> Prefix path, selector <i>pp:</i> This pattern style is useful to match whole sub-directories. The pattern <i>pp:/data/bar</i> matches <i>/data/bar</i> and everything therein. </p>
<p> Exclusions can be passed via the command line option <i>&#8211;exclude</i>. When used from within a shell the patterns should be quoted to protect them from expansion. </p>
<p> The <i>&#8211;exclude-from</i> option permits loading exclusion patterns from a text file with one pattern per line. Lines empty or starting with the number sign (&#8216;#&#8217;) after removing whitespace on both ends are ignored. The optional style selector prefix is also supported for patterns loaded from a file. Due to whitespace removal paths with whitespace at the beginning or end can only be excluded using regular expressions. </p>
<p> Examples: </p>
<p>#Exclude &#8216;/home/user/file.o&#8217; but not &#8216;/home/user/file.odt&#8217;:<br />
$ borg create &#8211; e &#8216;*.o&#8217; backup /<br />
#Exclude &#8216;/home/user/junk&#8217; and &#8216;/home/user/subdir/junk&#8217; but<br />
#not &#8216;/home/user/importantjunk&#8217; or &#8216;/etc/junk&#8217;:<br />
                    $ borg create &#8211;<br />
        e &#8216;/home/*/junk&#8217; backup /<br />
#Exclude the contents of &#8216;/home/user/cache&#8217; but not the directory itself:<br />
            $ borg create &#8211;<br />
        e / home / user / cache / backup /<br />
#The file &#8216;/home/user/cache/important&#8217; is * not *backed up:<br />
            $ borg create &#8211;<br />
        e / home / user / cache / backup / / home / user / cache / important<br />
#The contents of directories in &#8216;/home&#8217; are not backed up when their name<br />
#ends in &#8216;.tmp&#8217;<br />
                                                                       $ borg create&#8211; exclude &#8216;re:^/home/[^/]+\.tmp/&#8217; backup /<br />
#Load exclusions from file<br />
            $ cat &gt;<br />
    exclude.txt &lt;&lt; EOF<br />
#Comment line<br />
                           / home /*/junk<br />
                             *.tmp<br />
                             fm:aa:something/*<br />
                             re:^/home/[^/]\.tmp/<br />
                             sh:/home/*/<br />
                                 .thumbnails<br />
                                     EOF<br />
                                         $ borg create&#8211; exclude &#8211;<br />
                       from exclude.txt backup /</p>
<h3>borg help placeholders</h3>
<p> Repository (or Archive) URLs, &#8211;prefix and &#8211;remote-path values support these placeholders: </p>
<p> {hostname} The (short) hostname of the machine. </p>
<p> {fqdn} The full name of the machine. </p>
<p> {now} The current local date and time. </p>
<p> {utcnow} The current UTC date and time. </p>
<p> {user} The user name (or UID, if no name is available) of the user running borg. </p>
<p> {pid} The current process ID. </p>
<p> {borgversion} The version of borg, e.g.: 1.0.8rc1 </p>
<p> {borgmajor} The version of borg, only the major version, e.g.: 1 </p>
<p> {borgminor} The version of borg, only major and minor version, e.g.: 1.0 </p>
<p> {borgpatch} The version of borg, only major, minor and patch version, e.g.: 1.0.8 </p>
<p> Examples: </p>
<pre><code>
borg create / path / to / repo::{hostname} - {user} - {utcnow}... borg create / path / to / repo::{hostname} - {now : % Y - % m - % d_ % H : % M : % S}... borg prune-- prefix '{hostname}-' ...
</code></pre>
<h2>DEBUG COMMANDS</h2>
<p> There are some more commands (all starting with &quot;debug-&quot;) which are all <code>not intended for normal use</code> and <code>potentially very dangerous</code> if used incorrectly. </p>
<p> For example, <code>borg debug-put-obj</code> and <code>borg debug-delete-obj</code> will only do what their name suggests: put objects into repo / delete objects from repo. </p>
<p> Please note:</p>
<dl>
<dt>&bull;</p>
<dd> they will not update the chunks cache (chunks index) about the object</p>
<dt>&bull;</p>
<dd> they will not update the manifest (so no automatic chunks index resync is triggered)</p>
<dt>&bull;</p>
<dd> they will not check whether the object is in use (e.g. before delete-obj)</p>
<dt>&bull;</p>
<dd> they will not update any metadata which may point to the object </p>
<p> They exist to improve debugging capabilities without direct system access, e.g. in case you ever run into some severe malfunction. Use them only if you know what you are doing or if a trusted Borg developer tells you what to do.</dl>
<h2>ADDITIONAL NOTES</h2>
<p> Here are misc. notes about topics that are maybe not covered in enough detail in the usage section.</p>
<h3>Item flags</h3>
<p> <code>borg create -v &#8211;list</code> outputs a verbose list of all files, directories and other file system items it considered (no matter whether they had content changes or not). For each item, it prefixes a single-letter flag that indicates type and/or status of the item. </p>
<p> If you are interested only in a subset of that output, you can give e.g. <code>&#8211;filter=AME</code> and it will only show regular files with A, M or E status (see below). </p>
<p> A uppercase character represents the status of a regular file relative to the &quot;files&quot; cache (not relative to the repo &#8212; this is an issue if the files cache is not used). Metadata is stored in any case and for &#8216;A&#8217; and &#8216;M&#8217; also new data chunks are stored. For &#8216;U&#8217; all data chunks refer to already existing chunks.</p>
<dl>
<dt>&bull;</p>
<dd> &#8216;A&#8217; = regular file, added (see also <i>a_status_oddity</i> in the FAQ)</p>
<dt>&bull;</p>
<dd> &#8216;M&#8217; = regular file, modified</p>
<dt>&bull;</p>
<dd> &#8216;U&#8217; = regular file, unchanged</p>
<dt>&bull;</p>
<dd> &#8216;E&#8217; = regular file, an error happened while accessing/reading <i>this</i> file </p>
<p> A lowercase character means a file type other than a regular file, borg usually just stores their metadata:</p>
<dt>&bull;</p>
<dd> &#8216;d&#8217; = directory</p>
<dt>&bull;</p>
<dd> &#8216;b&#8217; = block device</p>
<dt>&bull;</p>
<dd> &#8216;c&#8217; = char device</p>
<dt>&bull;</p>
<dd> &#8216;h&#8217; = regular file, hardlink (to already seen inodes)</p>
<dt>&bull;</p>
<dd> &#8216;s&#8217; = symlink</p>
<dt>&bull;</p>
<dd> &#8216;f&#8217; = fifo </p>
<p> Other flags used include:</p>
<dt>&bull;</p>
<dd> &#8216;i&#8217; = backup data was read from standard input (stdin)</p>
<dt>&bull;</p>
<dd> &#8216;-&#8216; = dry run, item was <i>not</i> backed up</p>
<dt>&bull;</p>
<dd> &#8216;?&#8217; = missing status code (if you see this, please file a bug report!)</dl>
<h3>&#8211;chunker-params</h3>
<p> The chunker params influence how input files are cut into pieces (chunks) which are then considered for deduplication. They also have a big impact on resource usage (RAM and disk space) as the amount of resources needed is (also) determined by the total amount of chunks in the repository (see <i>Indexes / Caches memory usage</i> for details). </p>
<p> <code>&#8211;chunker-params=10,23,16,4095</code> results in a fine-grained deduplication and creates a big amount of chunks and thus uses a lot of resources to manage them. This is good for relatively small data volumes and if the machine has a good amount of free RAM and disk space. </p>
<p> <code>&#8211;chunker-params=19,23,21,4095</code> (default) results in a coarse-grained deduplication and creates a much smaller amount of chunks and thus uses less resources. This is good for relatively big data volumes and if the machine has a relatively low amount of free RAM and disk space. </p>
<p> If you already have made some archives in a repository and you then change chunker params, this of course impacts deduplication as the chunks will be cut differently. </p>
<p> In the worst case (all files are big and were touched in between backups), this will store all content into the repository again. </p>
<p> Usually, it is not that bad though:</p>
<dl>
<dt>&bull;</p>
<dd> usually most files are not touched, so it will just re-use the old chunks it already has in the repo</p>
<dt>&bull;</p>
<dd> files smaller than the (both old and new) minimum chunksize result in only one chunk anyway, so the resulting chunks are same and deduplication will apply </p>
<p> If you switch chunker params to save resources for an existing repo that already has some backup archives, you will see an increasing effect over time, when more and more files have been touched and stored again using the bigger chunksize <code>and</code> all references to the smaller older chunks have been removed (by deleting / pruning archives). </p>
<p> If you want to see an immediate big effect on resource usage, you better start a new repository when changing chunker params. </p>
<p> For more details, see <i>chunker_details</i>.</dl>
<h3>&#8211;umask</h3>
<p> If you use <code>&#8211;umask</code>, make sure that all repository-modifying borg commands (create, delete, prune) that access the repository in question use the same <code>&#8211;umask</code> value. </p>
<p> If multiple machines access the same repository, this should hold true for all of them.</p>
<h3>&#8211;read-special</h3>
<p> The &#8211;read-special option is special &#8211; you do not want to use it for normal full-filesystem backups, but rather after carefully picking some targets for it. </p>
<p> The option <code>&#8211;read-special</code> triggers special treatment for block and char device files as well as FIFOs. Instead of storing them as such a device (or FIFO), they will get opened, their content will be read and in the backup archive they will show up like a regular file. </p>
<p> Symlinks will also get special treatment if (and only if) they point to such a special file: instead of storing them as a symlink, the target special file will get processed as described above. </p>
<p> One intended use case of this is backing up the contents of one or multiple block devices, like e.g. LVM snapshots or inactive LVs or disk partitions. </p>
<p> You need to be careful about what you include when using <code>&#8211;read-special</code>, e.g. if you include <code>/dev/zero</code>, your backup will never terminate. </p>
<p> Restoring such files&#8217; content is currently only supported one at a time via <code>&#8211;stdout</code> option (and you have to redirect stdout to where ever it shall go, maybe directly into an existing device file of your choice or indirectly via <code>dd</code>). </p>
<p> To some extent, mounting a backup archive with the backups of special files via <code>borg mount</code> and then loop-mounting the image files from inside the mount point will work. If you plan to access a lot of data in there, it likely will scale and perform better if you do not work via the FUSE mount.</p>
<h3>Example</h3>
<p> Imagine you have made some snapshots of logical volumes (LVs) you want to backup. </p>
<p> <code>NOTE:</code> For some scenarios, this is a good method to get &quot;crash-like&quot; consistency (I call it crash-like because it is the same as you would get if you just hit the reset button or your machine would abrubtly and completely crash). This is better than no consistency at all and a good method for some use cases, but likely not good enough if you have databases running. </p>
<p> Then you create a backup archive of all these snapshots. The backup process will see a &quot;frozen&quot; state of the logical volumes, while the processes working in the original volumes continue changing the data stored there. </p>
<p> You also add the output of <code>lvdisplay</code> to your backup, so you can see the LV sizes in case you ever need to recreate and restore them. </p>
<p> After the backup has completed, you remove the snapshots again. </p>
<pre>
$ # create snapshots here
$ lvdisplay &gt; lvdisplay.txt
$ borg create --read-special /path/to/repo::arch lvdisplay.txt /dev/vg0/*-snapshot
$ # remove snapshots here
</pre>
<p> Now, let&#8217;s see how to restore some LVs from such a backup. </p>
<pre>
$ borg extract /path/to/repo::arch lvdisplay.txt
$ # create empty LVs with correct sizes here (look into lvdisplay.txt).
$ # we assume that you created an empty root and home LV and overwrite it now:
$ borg extract --stdout /path/to/repo::arch dev/vg0/root-snapshot &gt; /dev/vg0/root
$ borg extract --stdout /path/to/repo::arch dev/vg0/home-snapshot &gt; /dev/vg0/home
</pre>
<h3>Append-only mode</h3>
<p> A repository can be made &quot;append-only&quot;, which means that Borg will never overwrite or delete committed data. This is useful for scenarios where multiple machines back up to a central backup server using <code>borg serve</code>, since a hacked machine cannot delete backups permanently. </p>
<p> To activate append-only mode, edit the repository <code>config</code> file and add a line <code>append_only=1</code> to the <code>[repository]</code> section (or edit the line if it exists). </p>
<p> In append-only mode Borg will create a transaction log in the <code>transactions</code> file, where each line is a transaction and a UTC timestamp. </p>
<p> In addition, <code>borg serve</code> can act as if a repository is in append-only mode with its option <code>&#8211;append-only</code>. This can be very useful for fine-tuning access control in <code>.ssh/authorized_keys</code> </p>
<pre>
command=&quot;borg serve --append-only ...&quot; ssh-rsa &lt;key used for not-always-trustable backup clients&gt;
command=&quot;borg serve ...&quot; ssh-rsa &lt;key used for backup management&gt;
</pre>
<h3>Example</h3>
<p> Suppose an attacker remotely deleted all backups, but your repository was in append-only mode. A transaction log in this situation might look like this: </p>
<pre>
transaction 1, UTC time 2016-03-31T15:53:27.383532
transaction 5, UTC time 2016-03-31T15:53:52.588922
transaction 11, UTC time 2016-03-31T15:54:23.887256
transaction 12, UTC time 2016-03-31T15:55:54.022540
transaction 13, UTC time 2016-03-31T15:55:55.472564
</pre>
<p> From your security logs you conclude the attacker gained access at 15:54:00 and all the backups where deleted or replaced by compromised backups. From the log you know that transactions 11 and later are compromised. Note that the transaction ID is the name of the <i>last</i> file in the transaction. For example, transaction 11 spans files 6 to 11. </p>
<p> In a real attack you&#8217;ll likely want to keep the compromised repository intact to analyze what the attacker tried to achieve. It&#8217;s also a good idea to make this copy just in case something goes wrong during the recovery. Since recovery is done by deleting some files, a hard link copy (<code>cp -al</code>) is sufficient. </p>
<p> The first step to reset the repository to transaction 5, the last uncompromised transaction, is to remove the <code>hints.N</code> and <code>index.N</code> files in the repository (these two files are always expendable). In this example N is 13. </p>
<p> Then remove or move all segment files from the segment directories in <code>data/</code> starting with file 6: </p>
<pre>
rm data/**/{6..13}
</pre>
<p> That&#8217;s all to it.</p>
<h3>Drawbacks</h3>
<p> As data is only appended, and nothing removed, commands like <code>prune</code> or <code>delete</code> won&#8217;t free disk space, they merely tag data as deleted in a new transaction. </p>
<p> Be aware that as soon as you write to the repo in non-append-only mode (e.g. prune, delete or create archives from an admin machine), it will remove the deleted objects permanently (including the ones that were already marked as deleted, but not removed, in append-only mode). </p>
<p> Note that you can go back-and-forth between normal and append-only operation by editing the configuration file, it&#8217;s not a &quot;one way trip&quot;.</p>
<h3>Further considerations</h3>
<p> Append-only mode is not respected by tools other than Borg. <code>rm</code> still works on the repository. Make sure that backup client machines only get to access the repository via <code>borg serve</code>. </p>
<p> Ensure that no remote access is possible if the repository is temporarily set to normal mode for e.g. regular pruning. </p>
<p> Further protections can be implemented, but are outside of Borgs scope. For example, file system snapshots or wrapping <code>borg serve</code> to set special permissions or ACLs on new data files.</p>
<h2>AUTHOR</h2>
<p> The Borg Collective (see AUTHORS file)</p>
<h2>COPYRIGHT</h2>
<p> 2010-2014 Jonas Borgström, 2015-2016 The Borg Collective (see AUTHORS file) </p>
<h2>Index</h2>
