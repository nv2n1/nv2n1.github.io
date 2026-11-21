---

title: "lftp(1)"
name: "lftp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lftp/"
description: "lftp – Sophisticated file transfer program"
---

<p> lftp - Sophisticated file transfer program </p>
<h2>SYNTAX</h2>
<p> <code>lftp</code> [<code>-d</code>] [<code>-e </code><i>cmd</i>] [<code>-p </code><i>port</i>] [<code>-u </code><i>user</i>[<code>,</code><i>pass</i>]] [<i>site</i>] <br />
 <code>lftp -f </code><i>script_file</i> <br />
 <code>lftp -c </code><i>commands</i> <br />
 <code>lftp --version</code> <br />
 <code>lftp --help</code> </p>
<h2>VERSION</h2>
<p> This man page documents lftp version 4.8.1. </p>
<h2>DESCRIPTION</h2>
<p> <code>lftp</code> is a file transfer program that allows sophisticated FTP, HTTP and other connections to other hosts. If <i>site</i> is specified then lftp will connect to that site otherwise a connection has to be established with the open command. </p>
<p> <code>lftp</code> can handle several file access methods - FTP, FTPS, HTTP, HTTPS, HFTP, FISH, SFTP and file (HTTPS and FTPS are only available when lftp is compiled with GNU TLS or OpenSSL library). You can specify the method to use in `open URL&#8217; command, e.g. `open <a rel="nofollow" href="http://www.us.kernel.org/pub/linux'.">http://www.us.kernel.org/pub/linux&#8217;.</a> HFTP is ftp-over-http-proxy protocol. It can be used automatically instead of FTP if ftp:proxy is set to `<a rel="nofollow" href="http://proxy[:port]'.">http://proxy[:port]&#8216;.</a> Fish is a protocol working over an ssh connection to a unix account. SFtp is a protocol implemented in SSH2 as SFTP subsystem. </p>
<p> Besides FTP-like protocols, lftp has support for BitTorrent protocol as `torrent&#8217; command. Seeding is also supported. </p>
<p> Every operation in <code>lftp</code> is reliable, that is any non-fatal error is handled properly and the operation is repeated. So if downloading breaks, it will be restarted from the point automatically. Even if FTP server does not support the REST command, <code>lftp</code> will try to retrieve the file from the very beginning until the file is transferred completely. </p>
<p> <code>lftp</code> has shell-like command syntax allowing you to launch several commands in parallel in background (&amp;). It is also possible to group commands within () and execute them in background. All background jobs are executed in the same single process. You can bring a foreground job to background with ^Z (c-z) and back with command `wait&#8217; (or `fg&#8217; which is alias to `wait&#8217;). To list running jobs, use command `jobs&#8217;. Some commands allow redirecting their output (cat, ls, ...) to file or via pipe to external command. Commands can be executed conditionally based on termination status of previous command (&amp;&amp;, ||). </p>
<p> If you exit <code>lftp</code> before all jobs are not finished yet, <code>lftp</code> will move itself to nohup mode in background. The same thing happens with a real modem hangup or when you close an xterm. </p>
<p> <code>lftp</code> has built-in mirror which can download or update a whole directory tree. There is also reverse mirror (mirror -R) which uploads or updates a directory tree on server. Mirror can also synchronize directories between two remote servers, using FXP if available. </p>
<p> There is command `at&#8217; to launch a job at specified time in current context, command `queue&#8217; to queue commands for sequential execution for current server, and much more. </p>
<p> On startup, <code>lftp</code> executes <i>/etc/l <a href="ftp://ftp.conf">ftp.conf</a></i> and then <i>~/.lftprc</i> and <i>~/.lftp/rc</i> (or <i>~/.config/lftp/rc</i> if <i>~/.lftp</i> does not exist). You can place aliases and `set&#8217; commands there. Some people prefer to see full protocol debug, use `debug&#8217; to turn the debug on. Use `debug 3&#8217; to see only greeting messages and error messages. </p>
<p> <code>lftp</code> has a number of settable variables. You can use `set -a&#8217; to see all variables and their values or `set -d&#8217; to see list of defaults. Variable names can be abbreviated and prefix can be omitted unless the rest becomes ambiguous. </p>
<p> If lftp was compiled with OpenSSL (configure --with-openssl) it includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit. (<a rel="nofollow" href="http://www.openssl.org/)">http://www.openssl.org/)</a> </p>
<h3>Commands</h3>
<p> <code>!</code><i> shell command</i> </p>
<p> Launch shell or shell command. </p>
<pre><code>!ls
</code></pre>
<p> To do a directory listing of the local host. </p>
<p> <code>alias</code> [<i>name</i> [<i>value</i>]] </p>
<p> Define or undefine alias <i>name</i>. If <i>value</i> is omitted, the alias is undefined, else it takes the value <i>value</i>. If no argument is given the current aliases are listed. </p>
<pre><code>alias dir ls -lF
alias less zmore
</code></pre>
<p> <code>at</code> <i>time</i> [ -- <i>command</i> ] </p>
<p> Wait until the given time and execute given (optional) command. See also <code><a href="/docs/linux/man/1-at/">at</a></code>(1). </p>
<p> <code>attach</code> [<i>PID</i>] </p>
<p> Attach the terminal to specified backgrounded lftp process. </p>
<p> <code>bookmark</code> [<i>subcommand</i>] </p>
<p> The bookmark command controls bookmarks. </p>
<p> Site names can be used in the <i>open</i> command directly as-is or in any command that accepts input URLs using the <i>bm:site/path</i> format. </p>
<table>
<tr VALIGN=top>
<td>add &lt;name&gt; [&lt;loc&gt;]</td>
<td> add current place or given location to bookmarks and bind to given name 
</td>
</tr>
<tr VALIGN=top>
<td>del &lt;name&gt;</td>
<td>remove bookmark with name
</td>
</tr>
<tr VALIGN=top>
<td>edit</td>
<td>start editor on bookmarks file
</td>
</tr>
<tr VALIGN=top>
<td>import &lt;type&gt;</td>
<td>import foreign bookmarks
</td>
</tr>
<tr VALIGN=top>
<td>list</td>
<td>list bookmarks (default)
</td>
</tr>
</table>
<p> <code>cache</code> [<i>subcommand</i>] </p>
<p> The cache command controls local memory cache. The following subcommands are recognized: </p>
<table>
<tr VALIGN=top>
<td>stat</td>
<td>print cache status (default)
</td>
</tr>
<tr VALIGN=top>
<td>on|off</td>
<td>turn on/off caching
</td>
</tr>
<tr VALIGN=top>
<td>flush</td>
<td>flush cache
</td>
</tr>
<tr VALIGN=top>
<td>size <i>lim</i></td>
<td>set memory limit, -1 means unlimited
</td>
</tr>
<tr VALIGN=top>
<td>expire <i>Nx</i></td>
<td> set cache expiration time to <i>N</i> seconds (<i>x</i>=s) minutes (<i>x</i>=m) hours (<i>x</i>=h) or days (<i>x</i>=d) 
</td>
</tr>
</table>
<p> <code>cat</code> <i>files</i> </p>
<p> cat outputs the remote file(s) to stdout. (See also <code>more</code>, <code>zcat</code> and <code>zmore</code>) </p>
<p> <code>cd</code> rdir </p>
<p> Change current remote directory. The previous remote directory is stored as `-&#8216;. You can do `cd -&#8216; to change the directory back. The previous directory for each site is also stored on disk, so you can do `open site; cd -&#8216; even after lftp restart. </p>
<p> <code>chmod</code> [<code>OPTS</code>] <i>mode files...</i> </p>
<p> Change permission mask on remote files. The mode can be an octal number or a symbolic mode (see <a href="/docs/linux/man/1-chmod/">chmod</a>(1)). </p>
<table>
<tr VALIGN=top>
<td>-c,&nbsp;</td>
<td>--changes</td>
<td>like verbose but report only when a change is made
</td>
</tr>
<tr VALIGN=top>
<td>-f,&nbsp;</td>
<td>--quiet</td>
<td>suppress most error messages
</td>
</tr>
<tr VALIGN=top>
<td>-v,&nbsp;</td>
<td>--verbose</td>
<td>output a diagnostic for every file processed
</td>
</tr>
<tr VALIGN=top>
<td>-R,&nbsp;</td>
<td>--recursive</td>
<td>change files and directories recursively
</td>
</tr>
</table>
<p> <code>close</code> [<code>-a</code>] </p>
<p> Close idle connections. By default only with the current server, use -a to close all idle connections. </p>
<p> <code>cls</code> [<code>OPTS</code>] <i>files...</i> </p>
<p> `cls&#8217; tries to retrieve information about specified files or directories and outputs the information according to format options. The difference between `ls&#8217; and `cls&#8217; is that `ls&#8217; requests the server to format file listing, and `cls&#8217; formats it itself, after retrieving all the needed information. </p>
<table>
<tr VALIGN=top>
<td>-1&nbsp;</td>
<td></td>
<td>single-column output
</td>
</tr>
<tr VALIGN=top>
<td>-a,&nbsp;</td>
<td>--all</td>
<td>show dot files
</td>
</tr>
<tr VALIGN=top>
<td>-B,&nbsp;</td>
<td>--basename</td>
<td>show basename of files only
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--block-size=SIZ</td>
<td>use SIZ-byte blocks
</td>
</tr>
<tr VALIGN=top>
<td>-d,&nbsp;</td>
<td>--directory</td>
<td> list directory entries instead of contents 
</td>
</tr>
<tr VALIGN=top>
<td>-F,&nbsp;</td>
<td>--classify</td>
<td> append indicator (one of /@) to entries 
</td>
</tr>
<tr VALIGN=top>
<td>-h,&nbsp;</td>
<td>--human-readable</td>
<td> print sizes in human readable format (e.g., 1K) 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--si</td>
<td> likewise, but use powers of 1000 not 1024 
</td>
</tr>
<tr VALIGN=top>
<td>-k,&nbsp;</td>
<td>--kilobytes</td>
<td> like --block-size=1024 
</td>
</tr>
<tr VALIGN=top>
<td>-l,&nbsp;</td>
<td>--long</td>
<td> use a long listing format 
</td>
</tr>
<tr VALIGN=top>
<td>-q,&nbsp;</td>
<td>--quiet</td>
<td>don&#8217;t show status
</td>
</tr>
<tr VALIGN=top>
<td>-s,&nbsp;</td>
<td>--size</td>
<td>print size of each file
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--filesize</td>
<td> if printing size, only print size for files 
</td>
</tr>
<tr VALIGN=top>
<td>-i,&nbsp;</td>
<td>--nocase</td>
<td> case-insensitive pattern matching 
</td>
</tr>
<tr VALIGN=top>
<td>-I,&nbsp;</td>
<td>--sortnocase</td>
<td> sort names case-insensitively 
</td>
</tr>
<tr VALIGN=top>
<td>-D,&nbsp;</td>
<td>--dirsfirst</td>
<td> list directories first 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--sort=OPT</td>
<td> &quot;name&quot;, &quot;size&quot;, &quot;date&quot; 
</td>
</tr>
<tr VALIGN=top>
<td>-S&nbsp;</td>
<td></td>
<td>sort by file size
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--user, --group,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--perms, --date,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--linkcount, --links</td>
<td>show individual fields
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--time-style=STYLE</td>
<td> use specified time format 
</td>
</tr>
</table>
<p> <code>command</code> <i>cmd args...</i> </p>
<p> execute given command ignoring aliases. </p>
<p> <code>debug</code> [<code>OPTS</code>] <i>level</i>|<code>off</code> </p>
<p> Switch debugging to <i>level</i> or turn it off. Options: </p>
<table>
<tr VALIGN=top>
<td>-T&nbsp;</td>
<td>truncate output file</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-o &lt;file&gt;&nbsp;</td>
<td>redirect debug output to the file</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-c&nbsp;</td>
<td>show message context</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-p&nbsp;</td>
<td>show PID</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-t&nbsp;</td>
<td>show timestamps</td>
<td>
</td>
</tr>
</table>
<p> <code>echo</code> [<code>-n</code>] <i>string</i> </p>
<p> Prints (echos) the given string to the display. </p>
<p> <code>edit</code> [<code>OPTS</code>] <i>file</i> </p>
<p> Retrieve remote file to a temporary location, run a local editor on it and upload the file back if changed. Options: </p>
<table>
<tr VALIGN=top>
<td>-k&nbsp;</td>
<td>keep the temporary file</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-o &lt;temp&gt;&nbsp;</td>
<td>explicit temporary file location</td>
<td>
</td>
</tr>
</table>
<p> <code>eval</code> [<code>-f</code> <i>format</i> ] <i>args...</i> </p>
<p> without -f it executes given arguments as a command. With -f, arguments are transformed into a new command. The format can contain plain text and placeholders $0...$9 and $@, corresponding to the arguments. </p>
<p> <code>exit</code> [<code>bg</code>] [<code>top</code>] [<code>parent</code>] [<code>kill</code>] [<i>code</i>] </p>
<p> exit will exit from lftp or move to background if there are active jobs. If no job is active, <i>code</i> is passed to operating system as lftp&#8217;s termination status. If <i>code</i> is omitted, the exit code of last command is used. </p>
<p> `exit bg&#8217; forces moving to background when cmd:move-background is false. `exit top&#8217; makes top level `shell&#8217; (internal lftp command executor) terminate. `exit parent&#8217; terminates the parent shell when running a nested script. `exit kill&#8217; kills all numbered jobs before exiting. The options can be combined, e.g. `at 08:00 -- exit top kill &amp;&#8216; kills all jobs and makes lftp exit at specified time. </p>
<p> <code>fg</code> </p>
<p> Alias for `wait&#8217;. </p>
<p> <code>find</code> [<code>OPTS</code>] <i>directory...</i> </p>
<p> List files in the directory (current directory by default) recursively. This can help with servers lacking ls -R support. You can redirect output of this command. Options: </p>
<table>
<tr VALIGN=top>
<td>-d <i>MD</i>,&nbsp;</td>
<td>--max-depth=<i>MD</i></td>
<td>specify maximum scan depth
</td>
</tr>
<tr VALIGN=top>
<td>-l,&nbsp;</td>
<td>--ls </td>
<td>use long listing format
</td>
</tr>
</table>
<p> <code>ftpcopy</code> </p>
<p> Obsolete. Use one of the following instead: </p>
<pre><code>getftp://... -oftp://...get -Oftp://... file1 file2...
putftp://...mputftp://.../*mget -Oftp://...ftp://.../*
</code></pre>
<p> or other combinations to get FXP transfer (directly between two FTP servers). lftp would fallback to plain copy (via client) if FXP transfer cannot be initiated or ftp:use-fxp is false. </p>
<p> <code>get</code> [<code>-E</code>] [<code>-a</code>] [<code>-c</code>] [<code>-e</code>] [<code>-P</code> <i>N</i>] [<code>-O</code> <i>base</i>] <i>rfile</i> [<code>-o</code> <i>lfile</i>] ... </p>
<p> Retrieve the remote file <i>rfile</i> and store it as the local file <i>lfile</i>. If -o is omitted, the file is stored to local file named as base name of <i>rfile</i>. You can get multiple files by specifying multiple instances of <i>rfile</i> (and -o <i>lfile</i>). Does not expand wildcards, use <code>mget</code> for that. </p>
<table>
<tr VALIGN=top>
<td>-c</td>
<td>continue, reget
</td>
</tr>
<tr VALIGN=top>
<td>-E</td>
<td>delete source files after successful transfer
</td>
</tr>
<tr VALIGN=top>
<td>-e</td>
<td>delete target file before the transfer
</td>
</tr>
<tr VALIGN=top>
<td>-a</td>
<td>use ascii mode (binary is the default)
</td>
</tr>
<tr VALIGN=top>
<td>-P <i>N</i></td>
<td>download <i>N</i> files in parallel
</td>
</tr>
<tr VALIGN=top>
<td>-O &lt;base&gt;</td>
<td> specifies base directory or URL where files should be placed 
</td>
</tr>
</table>
<p> Examples: </p>
<pre><code>get README
get README -o debian.README
get README README.mirrors
get README -o debian.README README.mirrors -o debian.mirrors
get README -oftp://some.host.org/debian.READMEget README -oftp://some.host.org/debian-dir/ &nbsp;<wbr>&nbsp; (end slash is important) 
</code></pre>
<p> <code>get1</code> [<i>OPTS</i>] <i>rfile</i> </p>
<p> Transfer a single file. Options: </p>
<table>
<tr VALIGN=top>
<td>-o &lt;lfile&gt;</td>
<td> destination file name (default - basename of rfile) 
</td>
</tr>
<tr VALIGN=top>
<td>-c</td>
<td>continue, reget
</td>
</tr>
<tr VALIGN=top>
<td>-E</td>
<td> delete source files after successful transfer 
</td>
</tr>
<tr VALIGN=top>
<td>-a</td>
<td>use ascii mode (binary is the default)
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td>create the directory of the target file
</td>
</tr>
<tr VALIGN=top>
<td>--source-region=&lt;from-to&gt;</td>
<td> transfer specified region of source file 
</td>
</tr>
<tr VALIGN=top>
<td>--target-position=&lt;pos&gt;</td>
<td> position in target file to write data at 
</td>
</tr>
</table>
<p> <code>glob</code> [<i>OPTS</i>] [<i>command</i>] <i>patterns</i> </p>
<p> Glob given patterns containing metacharacters and pass result to given command or return appropriate exit code. </p>
<table>
<tr VALIGN=top>
<td>-f</td>
<td>plain files (default)
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td>directories
</td>
</tr>
<tr VALIGN=top>
<td>-a</td>
<td>all types
</td>
</tr>
<tr VALIGN=top>
<td>--exist</td>
<td>return zero exit code when the patterns expand to non-empty list
</td>
</tr>
<tr VALIGN=top>
<td>--not-exist</td>
<td>return zero exit code when the patterns expand to an empty list
</td>
</tr>
</table>
<p> Examples: </p>
<pre><code>glob echo *
glob --exist *.csv &amp;&amp; echo &quot;There are *.csv files&quot;
</code></pre>
<p> <code>help</code> [<i>cmd</i>] </p>
<p> Print help for <i>cmd</i> or if no <i>cmd</i> was specified print a list of available commands. </p>
<p> <code>jobs</code> [<i>OPTS</i>] [<i>job_no...</i>] </p>
<p> List running jobs. If <i>job_no</i> is specified, only list a job with that number. Options: </p>
<table>
<tr VALIGN=top>
<td>-v</td>
<td>verbose, several -v increase verbosity
</td>
</tr>
<tr VALIGN=top>
<td>-r</td>
<td>list just one specified job without recursion
</td>
</tr>
</table>
<p> <code>kill</code> all|<i>job_no</i> </p>
<p> Delete specified job with <i>job_no</i> or all jobs. (For <i>job_no</i> see <code>jobs</code>) </p>
<p> <code>lcd</code> <i>ldir</i> </p>
<p> Change current local directory <i>ldir</i>. The previous local directory is stored as `-&#8216;. You can do `lcd -&#8216; to change the directory back. </p>
<p> <code>ln</code> [<code>-s</code>] <i>existing-file</i> <i>new-link</i> </p>
<p> Make a hard/symbolic link to an existing file. Option -s selects creation of a symbolic link. </p>
<p> <code>local</code> <i>command</i> </p>
<p> Run specified command with local directory file:// session instead of remote session. Examples: </p>
<pre><code>local pwd
local ls
local mirror /dir1 /dir2
</code></pre>
<p> <code>lpwd</code> </p>
<p> Print current working directory on local machine. </p>
<p> <code>ls</code> <i>params</i> </p>
<p> List remote files. You can redirect output of this command to file or via pipe to external command. By default, ls output is cached, to see new listing use <code>rels</code> or <code>cache flush.</code> </p>
<p> <code>mget</code> [<code>-c</code>] [<code>-d</code>] [<code>-a</code>] [<code>-E</code>] [<code>-e</code>] [<code>-P</code> <i>N</i>] [<code>-O</code> <i>base</i>] <i>files</i> </p>
<p> Gets selected files with expanded wildcards. </p>
<table>
<tr VALIGN=top>
<td>-c</td>
<td>continue, reget.
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td> create directories the same as file names and get the files into them instead of current directory. 
</td>
</tr>
<tr VALIGN=top>
<td>-E</td>
<td>delete source files after successful transfer
</td>
</tr>
<tr VALIGN=top>
<td>-e</td>
<td>delete target file before the transfer
</td>
</tr>
<tr VALIGN=top>
<td>-a</td>
<td>use ascii mode (binary is the default)
</td>
</tr>
<tr VALIGN=top>
<td>-P <i>N</i></td>
<td>download <i>N</i> files in parallel
</td>
</tr>
<tr VALIGN=top>
<td>-O &lt;base&gt;</td>
<td> specifies base directory or URL where files should be placed 
</td>
</tr>
</table>
<p> <code>mirror</code> [<i>OPTS</i>] [<i>source</i> [<i>target</i>]] </p>
<p> Mirror specified source directory to the target directory. </p>
<p> By default the source is remote and the target is a local directory. When using -R, the source directory is local and the target is remote. If the target directory is omitted, base name of the source directory is used. If both directories are omitted, current local and remote directories are used. </p>
<p> The source and/or the target may be URLs pointing to directories. </p>
<p> If the target directory ends with a slash (except the root directory) then base name of the source directory is appended. </p>
<table>
<tr VALIGN=top>
<td>-c,&nbsp;</td>
<td>--continue</td>
<td> continue a mirror job if possible 
</td>
</tr>
<tr VALIGN=top>
<td>-e,&nbsp;</td>
<td>--delete</td>
<td> delete files not present at the source 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--delete-excluded</td>
<td> delete files excluded at the target 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--delete-first</td>
<td> delete old files before transferring new ones 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--depth-first</td>
<td> descend into subdirectories before transferring files 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--scan-all-first</td>
<td> scan all directories recursively before transferring files 
</td>
</tr>
<tr VALIGN=top>
<td>-s,&nbsp;</td>
<td>--allow-suid</td>
<td> set suid/sgid bits according to the source 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--allow-chown</td>
<td> try to set owner and group on files 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--ascii</td>
<td> use ascii mode transfers (implies --ignore-size) 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--ignore-time</td>
<td> ignore time when deciding whether to download 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--ignore-size</td>
<td> ignore size when deciding whether to download 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--only-missing</td>
<td> download only missing files 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--only-existing</td>
<td> download only files already existing at target 
</td>
</tr>
<tr VALIGN=top>
<td>-n,&nbsp;</td>
<td>--only-newer</td>
<td> download only newer files (-c won&#8217;t work) 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--upload-older</td>
<td> upload even files older than the target ones 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--transfer-all</td>
<td> transfer all files, even seemingly the same at the target site 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--no-empty-dirs</td>
<td> don&#8217;t create empty directories (implies --depth-first) 
</td>
</tr>
<tr VALIGN=top>
<td>-r,&nbsp;</td>
<td>--no-recursion</td>
<td> don&#8217;t go to subdirectories 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--recursion=<i>MODE</i></td>
<td> go to subdirectories on a condition 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--no-symlinks</td>
<td> don&#8217;t create symbolic links 
</td>
</tr>
<tr VALIGN=top>
<td>-p,&nbsp;</td>
<td>--no-perms</td>
<td> don&#8217;t set file permissions 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--no-umask</td>
<td> don&#8217;t apply umask to file modes 
</td>
</tr>
<tr VALIGN=top>
<td>-R,&nbsp;</td>
<td>--reverse</td>
<td> reverse mirror (put files) 
</td>
</tr>
<tr VALIGN=top>
<td>-L,&nbsp;</td>
<td>--dereference</td>
<td> download symbolic links as files 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--overwrite</td>
<td> overwrite plain files without removing them first 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--no-overwrite</td>
<td> remove and re-create plain files instead of overwriting 
</td>
</tr>
<tr VALIGN=top>
<td>-N,&nbsp;</td>
<td>--newer-than=<i>SPEC</i></td>
<td> download only files newer than specified time 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--older-than=<i>SPEC</i></td>
<td> download only files older than specified time 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--size-range=<i>RANGE</i></td>
<td> download only files with size in specified range 
</td>
</tr>
<tr VALIGN=top>
<td>-P,&nbsp;</td>
<td>--parallel[=<i>N</i>]</td>
<td> download N files in parallel 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--use-pget[-n=<i>N</i>]</td>
<td> use pget to transfer every single file 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--on-change=<i>CMD</i></td>
<td> execute the command if anything has been changed 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--loop</td>
<td> repeat mirror until no changes found 
</td>
</tr>
<tr VALIGN=top>
<td>-i <i>RX</i>,&nbsp;</td>
<td>--include=<i>RX</i></td>
<td> include matching files 
</td>
</tr>
<tr VALIGN=top>
<td>-x <i>RX</i>,&nbsp;</td>
<td>--exclude=<i>RX</i></td>
<td> exclude matching files 
</td>
</tr>
<tr VALIGN=top>
<td>-I <i>GP</i>,&nbsp;</td>
<td>--include-glob=<i>GP</i></td>
<td> include matching files 
</td>
</tr>
<tr VALIGN=top>
<td>-X <i>GP</i>,&nbsp;</td>
<td>--exclude-glob=<i>GP</i></td>
<td> exclude matching files 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--include-rx-from=<i>FILE</i></td>
<td> 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--exclude-rx-from=<i>FILE</i></td>
<td> 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--include-glob-from=<i>FILE</i></td>
<td> 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--exclude-glob-from=<i>FILE</i></td>
<td> load include/exclude patterns from the file, one per line 
</td>
</tr>
<tr VALIGN=top>
<td>-f <i>FILE</i>,&nbsp;</td>
<td>--file=<i>FILE</i></td>
<td> mirror a single file or globbed group (e.g. /path/to/*.txt) 
</td>
</tr>
<tr VALIGN=top>
<td>-F <i>DIR</i>,&nbsp;</td>
<td>--directory=<i>DIR</i></td>
<td> mirror a single directory or globbed group (e.g. /path/to/dir*) 
</td>
</tr>
<tr VALIGN=top>
<td>-O <i>DIR</i>,&nbsp;</td>
<td>--target-directory=<i>DIR</i></td>
<td> target base path or URL 
</td>
</tr>
<tr VALIGN=top>
<td>-v,&nbsp;</td>
<td>--verbose[=level]</td>
<td> verbose operation 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--log=<i>FILE</i></td>
<td> write lftp commands being executed to FILE 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--script=<i>FILE</i></td>
<td> write lftp commands to FILE, but don&#8217;t execute them 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--just-print, --dry-run</td>
<td> same as --script=- 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--max-errors=<i>N</i></td>
<td> stop after this number of errors 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--skip-noaccess</td>
<td> don&#8217;t try to transfer files with no read access. 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--use-cache</td>
<td> use cached directory listings 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--Remove-source-files</td>
<td> remove source files after transfer (use with caution) 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--Remove-source-dirs</td>
<td> remove source files and directories after transfer (use with caution). Top level directory is not removed if it&#8217;s name ends with a slash. 
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>--Move</td>
<td> same as --Remove-source-dirs 
</td>
</tr>
<tr VALIGN=top>
<td>-a&nbsp;</td>
<td></td>
<td> same as --allow-chown --allow-suid --no-umask 
</td>
</tr>
</table>
<p> <i>RX</i> is an extended regular expression, just like in <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1). </p>
<p> <i>GP</i> is a glob pattern, e.g. `*.zip&#8217;. </p>
<p> Include and exclude options can be specified multiple times. It means that a file or directory would be mirrored if it matches an include and does not match to excludes after the include, or does not match anything and the first check is exclude. Directories are matched with a slash appended. </p>
<p> Note that symbolic links are not created when uploading to remote server, because FTP protocol cannot do it. To upload files the links refer to, use `mirror -RL&#8217; command (treat symbolic links as files). </p>
<p> For options --newer-than and --older-than you can either specify a file or time specification like that used by <code><a href="/docs/linux/man/1-at/">at</a></code>(1) command, e.g. `now-7days&#8217; or `week ago&#8217;. If you specify a file, then modification time of that file will be used. </p>
<p> Verbosity level can be selected using --verbose=level option or by several -v options, e.g. -vvv. Levels are: </p>
<pre><code>0 - no output (default)
1 - print actions
2 - +print not deleted file names (when -e is not specified)
3 - +print directory names which are mirrored
</code></pre>
<p> --only-newer turns off file size comparison and uploads/downloads only newer files even if size is different. By default older files are transferred and replace newer ones. </p>
<p> --upload-older allows replacing newer remote files with older ones (when the target side is remote). Some remote back-ends cannot preserve timestamps so the default is to keep newer files. </p>
<p> Recursion mode can be one of `always&#8217;, `never&#8217;, `missing&#8217;, `newer&#8217;. With the option `newer&#8217; mirror compares timestamps of directories and enters a directory only if it is older or missing on the target side. Be aware that when a file changes the directory timestamp may stay the same, so mirror won&#8217;t process that directory. </p>
<p> The options --file and --directory may be used multiple times and even mixed provided that base directories of the paths are the same. </p>
<p> You can mirror between two servers if you specify URLs instead of directories. FXP is automatically used for transfers between FTP servers, if possible. </p>
<p> Some FTP servers hide dot-files by default (e.g. <i>.htaccess</i>), and show them only when LIST command is used with -a option. In such case try to use `set ftp:list-options -a&#8217;. </p>
<p> --depth-first, --no-empty-dirs and setting mirror:no-empty-dirs=true. </p>
<p> <code>mkdir</code> [<code>-p</code>] [<code>-f</code>] <i>dir(s)</i> </p>
<p> Make remote directories. If -p is used, make all components of paths. The -f option makes mkdir quiet and suppresses messages. </p>
<p> <code>module</code> <i>module </i>[<i> args </i>] </p>
<p> Load given module using <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) function. If module name does not contain a slash, it is searched in directories specified by module:path variable. Arguments are passed to module_init function. See README.modules for technical details. </p>
<p> <code>more</code> <i>files</i> </p>
<p> Same as `cat <i>files</i> | more&#8217;. if <code>PAGER</code> is set, it is used as filter. (See also <code>cat</code>, <code>zcat</code> and <code>zmore</code>) </p>
<p> <code>mput</code> [<code>-c</code>] [<code>-d</code>] [<code>-a</code>] [<code>-E</code>] [<code>-e</code>] [<code>-P</code> <i>N</i>] [<code>-O</code> <i>base</i>] <i>files</i> </p>
<p> Upload files with wildcard expansion. By default it uses the base name of local name as remote one. This can be changed by `-d&#8217; option. </p>
<table>
<tr VALIGN=top>
<td>-c</td>
<td>continue, reput
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td> create directories the same as in file names and put the files into them instead of current directory 
</td>
</tr>
<tr VALIGN=top>
<td>-E</td>
<td> delete source files after successful transfer (dangerous) 
</td>
</tr>
<tr VALIGN=top>
<td>-e</td>
<td>delete target file before the transfer
</td>
</tr>
<tr VALIGN=top>
<td>-a</td>
<td>use ascii mode (binary is the default)
</td>
</tr>
<tr VALIGN=top>
<td>-P <i>N</i></td>
<td>upload <i>N</i> files in parallel
</td>
</tr>
<tr VALIGN=top>
<td>-O &lt;base&gt;</td>
<td> specifies base directory or URL where files should be placed 
</td>
</tr>
</table>
<p> <code>mrm</code> <i>file(s)</i> </p>
<p> Same as `glob rm&#8217;. Removes specified file(s) with wildcard expansion. </p>
<p> <code>mmv</code> [<code>-O</code> <i>directory</i>] <i>file(s)</i> <i>directory</i> </p>
<p> Move specified files to a target directory. The target directory can be specified after -O option or as the last argument. </p>
<table>
<tr VALIGN=top>
<td>-O &lt;dir&gt;</td>
<td> specifies the target directory where files should be placed 
</td>
</tr>
</table>
<p> <code>mv</code> <i>file1</i> <i>file2</i> </p>
<p> Rename <i>file1</i> to <i>file2</i>. No wildcard exmapsion is performed. If you give more than two arguments, or the last argument ends with a slash, then <code>mmv</code> command is executed instead. </p>
<p> <code>nlist</code> [<i>args</i>] </p>
<p> List remote file names </p>
<p> <code>open</code> [<i>OPTS</i>] <i>site</i> </p>
<p> Select a server by host name, URL or bookmark. When an URL or bookmark is given, automatically change the current working directory to the directory of the URL. Options: </p>
<table>
<tr VALIGN=top>
<td>-e <i>cmd</i></td>
<td>execute the command just after selecting the server
</td>
</tr>
<tr VALIGN=top>
<td>-u <i>user</i>[,<i>pass</i>]</td>
<td>use the user/password for authentication
</td>
</tr>
<tr VALIGN=top>
<td>-p <i>port</i></td>
<td>use the port for connection
</td>
</tr>
<tr VALIGN=top>
<td>-s <i>slot</i></td>
<td>assign the connection to this slot
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td>enable debug
</td>
</tr>
<tr VALIGN=top>
<td>-B</td>
<td>don&#8217;t look up bookmarks
</td>
</tr>
<tr VALIGN=top>
<td>--user <i>user</i></td>
<td>use the user for authentication
</td>
</tr>
<tr VALIGN=top>
<td>--password <i>pass</i></td>
<td>use the password for authentication
</td>
</tr>
<tr VALIGN=top>
<td>--env-password</td>
<td>take password from <code>LFTP_PASSWORD</code> environment variable
</td>
</tr>
<tr VALIGN=top>
<td><i>site</i></td>
<td>host name, URL or bookmark name
</td>
</tr>
</table>
<p> <code>pget</code> [<i>OPTS</i>] <i>rfile</i> [<i></i><code>-o</code> lfile] </p>
<p> Gets the specified file using several connections. This can speed up transfer, but loads the net and server heavily impacting other users. Use only if you really have to transfer the file ASAP. Options: </p>
<table>
<tr VALIGN=top>
<td>-c</td>
<td> continue transfer. Requires <i>lfile.lftp-pget-status</i> file. 
</td>
</tr>
<tr VALIGN=top>
<td>-n <i>maxconn</i></td>
<td> set maximum number of connections (default is taken from <code>pget:default-n</code> setting) 
</td>
</tr>
</table>
<p> <code>put</code> [<code>-E</code>] [<code>-a</code>] [<code>-c</code>] [<code>-e</code>] [<code>-P</code> <i>N</i>] [<code>-O </code><i>base</i>] <i>lfile</i> [<code>-o </code><i>rfile</i>] </p>
<p> Upload <i>lfile</i> with remote name <i>rfile</i>. If -o omitted, the base name of <i>lfile</i> is used as remote name. Does not expand wildcards, use <code>mput</code> for that. </p>
<table>
<tr VALIGN=top>
<td>-o &lt;rfile&gt;</td>
<td> specifies remote file name (default - basename of lfile) 
</td>
</tr>
<tr VALIGN=top>
<td>-c</td>
<td> continue, reput. It requires permission to overwrite remote files 
</td>
</tr>
<tr VALIGN=top>
<td>-E</td>
<td> delete source files after successful transfer (dangerous) 
</td>
</tr>
<tr VALIGN=top>
<td>-e</td>
<td>delete target file before the transfer
</td>
</tr>
<tr VALIGN=top>
<td>-a</td>
<td>use ascii mode (binary is the default)
</td>
</tr>
<tr VALIGN=top>
<td>-P <i>N</i></td>
<td>upload <i>N</i> files in parallel
</td>
</tr>
<tr VALIGN=top>
<td>-O &lt;base&gt;</td>
<td> specifies base directory or URL where files should be placed 
</td>
</tr>
</table>
<p> <code>pwd</code> [<code>-p</code>] </p>
<p> Print current remote URL. Use `-p&#8217; option to show password in the URL. </p>
<p> <code>queue</code> [<code>-n</code> <i>num</i> ] <i>cmd</i> </p>
<p> Add the given command to queue for sequential execution. Each site has its own queue. `-n&#8217; adds the command before the given item in the queue. Don&#8217;t try to queue `cd&#8217; or `lcd&#8217; commands, it may confuse lftp. Instead do the cd/lcd before `queue&#8217; command, and it will remember the place in which the command is to be done. It is possible to queue up an already running job by `queue wait &lt;jobno&gt;&#8216;, but the job will continue execution even if it is not the first in queue. </p>
<p> `queue stop&#8217; will stop the queue, it will not execute any new commands, but already running jobs will continue to run. You can use `queue stop&#8217; to create an empty stopped queue. `queue start&#8217; will resume queue execution. When you exit lftp, it will start all stopped queues automatically. </p>
<p> `queue&#8217; with no arguments will either create a stopped queue or print queue status. </p>
<p> <code>queue</code> <code>--delete|-d </code>[<i>index or wildcard expression</i>] </p>
<p> Delete one or more items from the queue. If no argument is given, the last entry in the queue is deleted. </p>
<p> <code>queue</code> <code>--move|-m </code>&lt;<i>index or wildcard expression</i>&gt; [<i>index</i>] </p>
<p> Move the given items before the given queue index, or to the end if no destination is given. </p>
<table>
<tr VALIGN=top>
<td>-q</td>
<td>Be quiet.
</td>
</tr>
<tr VALIGN=top>
<td>-v</td>
<td>Be verbose.
</td>
</tr>
<tr VALIGN=top>
<td>-Q</td>
<td> Output in a format that can be used to re-queue. Useful with --delete. 
</td>
</tr>
</table>
<p> Examples: </p>
<pre><code>&gt; get file &amp;
[1] get file
&gt; queue wait 1
&gt; queue get another_file
&gt; cd a_directory
&gt; queue get yet_another_file
</code></pre>
<table>
<tr VALIGN=top>
<td>queue -d 3</td>
<td>Delete the third item in the queue.
</td>
</tr>
<tr VALIGN=top>
<td>queue -m 6 4</td>
<td> Move the sixth item in the queue before the fourth. 
</td>
</tr>
<tr VALIGN=top>
<td>queue -m &quot;get*zip&quot; 1</td>
<td> Move all commands matching &quot;get*zip&quot; to the beginning of the queue. (The order of the items is preserved.) 
</td>
</tr>
<tr VALIGN=top>
<td>queue -d &quot;get*zip&quot;</td>
<td> Delete all commands matching &quot;get*zip&quot;. 
</td>
</tr>
</table>
<p> <code>quote</code> <i>cmd</i> </p>
<p> For FTP - send the command uninterpreted. Use with caution - it can lead to unknown remote state and thus will cause reconnect. You cannot be sure that any change of remote state because of quoted command is solid - it can be reset by reconnect at any time. </p>
<p> For HTTP - specific to HTTP action. Syntax: ``quote &lt;command&gt; [&lt;args&gt;]&#8216;&#8216;. Command may be ``set-cookie&#8217;&#8216; or ``post&#8217;&#8216;. </p>
<pre><code>openhttp://www.site.netquote set-cookie &quot;variable=value; othervar=othervalue&quot;
set http:post-content-type application/x-www-form-urlencoded
quote post /cgi-bin/script.cgi &quot;var=value&amp;othervar=othervalue&quot; &gt; local_file
</code></pre>
<p> For FISH - send the command uninterpreted. This can be used to execute arbitrary commands on server. The command must not take input or print ### at new line beginning. If it does, the protocol will become out of sync. </p>
<pre><code>openfish://serverquote find -name \*.zip
</code></pre>
<p> <code>reget </code><i>rfile</i> [<code>-o</code> <i>lfile</i>] </p>
<p> Same as `get -c&#8217;. </p>
<p> <code>rels</code> [<i>args</i>] </p>
<p> Same as `ls&#8217;, but ignores the cache. </p>
<p> <code>renlist</code> [<i>args</i>] </p>
<p> Same as `nlist&#8217;, but ignores the cache. </p>
<p> <code>repeat</code> [<i>OPTS</i>] [[<code>-d</code>] <i>delay</i>] [<i>command</i>] </p>
<p> Repeat specified command with a delay between iterations. Default delay is one second, default command is empty. </p>
<table>
<tr VALIGN=top>
<td>-c &lt;count&gt;</td>
<td>maximum number of iterations
</td>
</tr>
<tr VALIGN=top>
<td>-d &lt;delay&gt;</td>
<td>delay between iterations
</td>
</tr>
<tr VALIGN=top>
<td>--while-ok</td>
<td>stop when command exits with non-zero code
</td>
</tr>
<tr VALIGN=top>
<td>--until-ok</td>
<td>stop when command exits with zero code
</td>
</tr>
<tr VALIGN=top>
<td>--weak </td>
<td>stop when lftp moves to background.
</td>
</tr>
</table>
<p> Examples: </p>
<pre><code>repeat at tomorrow -- mirror
repeat 1d mirror
</code></pre>
<p> <code>reput</code> <i>lfile</i> [<code>-o</code> <i>rfile</i>] </p>
<p> Same as `put -c&#8217;. </p>
<p> <code>rm</code> [<code>-r</code>] [<code>-f</code>] <i>files</i> </p>
<p> Remove remote files. Does not expand wildcards, use <code>mrm</code> for that. -r is for recursive directory remove. Be careful, if something goes wrong you can lose files. -f suppress error messages. </p>
<p> <code>rmdir</code> <i>dir(s)</i> </p>
<p> Remove remote directories. </p>
<p> <code>scache</code> [<i>session</i>] </p>
<p> List cached sessions or switch to specified session. </p>
<p> <code>set</code> [<i>var</i> [<i>val</i>]] </p>
<p> Set variable to given value. If the value is omitted, unset the variable. Variable name has format ``name/closure&#8217;&#8216;, where closure can specify exact application of the setting. See below for details. If set is called with no variable then only altered settings are listed. It can be changed by options: </p>
<table>
<tr VALIGN=top>
<td>-a</td>
<td>list all settings, including default values
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td>list only default values, not necessary current ones
</td>
</tr>
</table>
<p> <code>site</code> <i>site_cmd</i> </p>
<p> Execute site command <i>site_cmd</i> and output the result. You can redirect its output. </p>
<p> <code>sleep</code> <i>interval</i> </p>
<p> Sleep given time interval and exit. Interval is in seconds by default, but can be suffixed with &#8216;m&#8217;, &#8216;h&#8217;, &#8216;d&#8217; for minutes, hours and days respectively. See also <code>at</code>. </p>
<p> <code>slot</code> [<i>name</i>] </p>
<p> Select specified slot or list all slots allocated. A slot is a connection to a server, somewhat like a virtual console. You can create multiple slots connected to different servers and switch between them. You can also use <i>slot:name</i> as a pseudo-URL evaluating to that slot location. </p>
<p> Default readline binding allows quick switching between slots named 0-9 using Meta-0 - Meta-9 keys (often you can use Alt instead of Meta). </p>
<p> <code>source</code> <i>file</i> <br />
 <code>source -e</code> <i>command</i> </p>
<p> Execute commands recorded in file <i>file</i> or returned by specified external command. </p>
<pre><code>source ~/.lftp/rc
source -e echo help
</code></pre>
<p> <code>suspend</code> </p>
<p> Stop lftp process. Note that transfers will be also stopped until you continue the process with shell&#8217;s fg or bg commands. </p>
<p> <code>torrent</code> [<code>OPTS</code>] <i>torrent-files...</i> </p>
<p> Start BitTorrent process for the given <i>torrent-files</i>, which can be a local file, URL, magnet link or plain <i>info_hash</i> written in hex or base32. Local wildcards are expanded. Existing files are first validated unless <i>--force-valid</i> option is given. Missing pieces are downloaded. Files are stored in specified <i>directory</i> or current working directory by default. Seeding continues until ratio reaches <i>torrent:stop-on-ratio</i> setting or time of <i>torrent:seed-max-time</i> runs out. </p>
<p> Options: </p>
<table>
<tr VALIGN=top>
<td>-O &lt;directory&gt;</td>
<td> specifies base directory where files should be placed 
</td>
</tr>
<tr VALIGN=top>
<td>--force-valid</td>
<td> skip file validation (if you are sure they are ok). 
</td>
</tr>
<tr VALIGN=top>
<td>--only-new</td>
<td> stop if the metadata is known already or the torrent is complete. 
</td>
</tr>
<tr VALIGN=top>
<td>--only-incomplete</td>
<td> stop if the torrent is already complete. 
</td>
</tr>
<tr VALIGN=top>
<td>--dht-bootstrap=&lt;node&gt;</td>
<td> bootstrap DHT by sending a query to specified <i>node</i>. This option should be used just once to fill the local node cache. Port number may be given after colon, default is 6881. Here are some nodes for bootstrapping: dht.transmissionbt.com, router.utorrent.com, router.bittorrent.com. 
</td>
</tr>
<tr VALIGN=top>
<td>--share</td>
<td> share specified file or directory using BitTorrent protocol. Magnet link is printed when it&#8217;s ready. 
</td>
</tr>
</table>
<p> <code>user</code> <i>user</i> [<i>pass</i>] <br />
 <code>user</code> <i>URL</i> [<i>pass</i>] </p>
<p> Use specified info for remote login. If you specify an URL with user name, the entered password will be cached so that future URL references can use it. </p>
<p> <code>version</code> </p>
<p> Print <code>lftp</code> version. </p>
<p> <code>wait</code> [<i>jobno</i>] <br />
 <code>wait all</code> </p>
<p> Wait for specified job to terminate. If jobno is omitted, wait for last backgrounded job. </p>
<p> `wait all&#8217; waits for all jobs to terminate. </p>
<p> <code>zcat</code> <i>files</i> </p>
<p> Same as cat, but filter each file through zcat. (See also <code>cat</code>, <code>more</code> and <code>zmore</code>) </p>
<p> <code>zmore</code> <i>files</i> </p>
<p> Same as more, but filter each file through zcat. (See also <code>cat</code>, <code>zcat</code> and <code>more</code>) </p>
<h3>Settings</h3>
<p> On startup, lftp executes <i>~/.lftprc</i> and <i>~/.lftp/rc</i> (or <i>~/.config/lftp/rc</i> if <i>~/.lftp</i> does not exist). You can place aliases and `set&#8217; commands there. Some people prefer to see full protocol debug, use `debug&#8217; to turn the debug on. </p>
<p> There is also a system-wide startup file in <i>/etc/l <a href="ftp://ftp.conf">ftp.conf</a></i>. It can be in different directory, see FILES section. </p>
<p> <code>lftp</code> has the following settable variables (you can also use `set -a&#8217; to see all variables and their values): </p>
<dl>
<dt><code>bmk:save-passwords</code>&nbsp;(boolean) </dt>
<dd> <p> save plain text passwords in <i>~/.local/share/lftp/bookmarks</i> or <i>~/.lftp/bookmarks</i> on `bookmark add&#8217; command. Off by default. </p>
 </dd>
<dt><code>cache:cache-empty-listings</code>&nbsp;(boolean) </dt>
<dd> <p> When false, empty listings are not cached. </p>
 </dd>
<dt><code>cache:enable</code>&nbsp;(boolean) </dt>
<dd> <p> When false, cache is disabled. </p>
 </dd>
<dt><code>cache:expire</code> (time interval) </dt>
<dd> <p> Positive cache entries expire in this time interval. </p>
 </dd>
<dt><code>cache:expire-negative</code> (time interval) </dt>
<dd> <p> Negative cache entries expire in this time interval. </p>
 </dd>
<dt><code>cache:size</code> (number) </dt>
<dd> <p> Maximum cache size. When exceeded, oldest cache entries will be removed from cache. </p>
 </dd>
<dt><code>cmd:at-exit</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed before lftp exits or moves to background. </p>
 </dd>
<dt><code>cmd:at-exit-bg</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed before backgrounded lftp exits. </p>
 </dd>
<dt><code>cmd:at-exit-fg</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed before foreground lftp exits. </p>
 </dd>
<dt><code>cmd:at-background</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed before lftp moves to background. </p>
 </dd>
<dt><code>cmd:at-terminate</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed before lftp terminates (either backgrounded or foreground). </p>
 </dd>
<dt><code>cmd:at-finish</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed once when all jobs are done. </p>
 </dd>
<dt><code>cmd:at-queue-finish</code>&nbsp;(string) </dt>
<dd> <p> the commands in string are executed once when all jobs in a queue are done. </p>
 </dd>
<dt><code>cmd:cls-completion-default</code>&nbsp;(string) </dt>
<dd> <p> default <code>cls</code> options for displaying completion choices. For example, to make completion listings show file sizes, set cmd:cls-completion-default to `-s&#8217;. </p>
 </dd>
<dt><code>cmd:cls-default</code>&nbsp;(string) </dt>
<dd> <p> default <code>cls</code> command options. They can be overridden by explicitly given options. </p>
 </dd>
<dt><code>cmd:cls-exact-time</code>&nbsp;(boolean) </dt>
<dd> <p> when true, <code>cls</code> would try to get exact file modification time even if it means more requests to the server. </p>
 </dd>
<dt><code>cmd:csh-history</code>&nbsp;(boolean) </dt>
<dd> <p> enables csh-like history expansion. </p>
 </dd>
<dt><code>cmd:default-protocol</code>&nbsp;(string) </dt>
<dd> <p> The value is used when `open&#8217; is used with just host name without protocol. Default is `ftp&#8217;. </p>
 </dd>
<dt><code>cmd:fail-exit</code>&nbsp;(boolean) </dt>
<dd> <p> if true, exit when a command fails and the following command is unconditional (i.e. does not begin with || or &amp;&amp;). lftp exits after the unconditional command is issued without executing it. </p>
 </dd>
<dt><code>cmd:interactive</code>&nbsp;(tri-boolean) </dt>
<dd> <p> when true, lftp acts interactively, handles terminal signals and outputs some extra messages. Default is auto and depends on stdin being a terminal. </p>
 </dd>
<dt><code>cmd:long-running</code>&nbsp;(seconds) </dt>
<dd> <p> time of command execution, which is considered as `long&#8217; and a beep is done before next prompt. 0 means off. </p>
 </dd>
<dt><code>cmd:ls-default</code>&nbsp;(string) </dt>
<dd> <p> default ls argument </p>
 </dd>
<dt><code>cmd:move-background</code> (boolean) </dt>
<dd> <p> when false, lftp refuses to go to background when exiting. To force it, use `exit bg&#8217;. </p>
 </dd>
<dt><code>cmd:move-background-detach</code> (boolean) </dt>
<dd> <p> when true (default), lftp detaches itself from the control terminal when moving to background, it is possible to attach back using `attach&#8217; command; when false, lftp tricks the shell to move lftp to background process group and continues to run, then fg shell command brings lftp back to foreground unless it has done all jobs and terminated. </p>
 </dd>
<dt><code>cmd:prompt</code>&nbsp;(string) </dt>
<dd> <p> The prompt. lftp recognizes the following backslash-escaped special characters that are decoded as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>\@</code></dt>
<dd> <p> insert @ if the current remote site user is not default </p>
 </dd>
<dt><code>\a</code></dt>
<dd> <p> an ASCII bell character (07) </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> an ASCII escape character (033) </p>
 </dd>
<dt><code>\h</code></dt>
<dd> <p> the remote hostname you are connected to </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> newline </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> the name of the client (lftp) </p>
 </dd>
<dt><code>\S</code></dt>
<dd> <p> current slot name </p>
 </dd>
<dt><code>\u</code></dt>
<dd> <p> the username of the remote site user you are logged in as </p>
 </dd>
<dt><code>\U</code></dt>
<dd> <p> the URL of the remote site (e.g., <a href="ftp://g437.ub.gu.se/home/james/src/lftp)">ftp://g437.ub.gu.se/home/james/src/lftp)</a> </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> the version of <code>lftp</code> (e.g., 2.0.3) </p>
 </dd>
<dt><code>\w</code></dt>
<dd> <p> the current working directory at the remote site </p>
 </dd>
<dt><code>\W</code></dt>
<dd> <p> the base name of the current working directory at the remote site </p>
 </dd>
<dt><code>\l</code></dt>
<dd> <p> the current working directory at the local site </p>
 </dd>
<dt><code>\L</code></dt>
<dd> <p> the base name of the current working directory at the local site </p>
 </dd>
<dt><code>\</code><i>nnn</i></dt>
<dd> <p> the character corresponding to the octal number <i>nnn</i> </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> a backslash </p>
 </dd>
<dt><code>\?</code></dt>
<dd> <p> skips next character if previous substitution was empty. </p>
 </dd>
<dt><code>\[</code></dt>
<dd> <p> begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt </p>
 </dd>
<dt><code>\]</code></dt>
<dd> <p> end a sequence of non-printing characters </p>
 </dd></dl>
</dl>
<dt><code>cmd:parallel</code>&nbsp;(number) </dt>
<dd> <p> Number of jobs run in parallel in non-interactive mode. For example, this may be useful for scripts with multiple `get&#8217; commands. Note that setting this to a value greater than 1 changes conditional execution behaviour, basically makes it inconsistent. </p>
 </dd>
<dt><code>cmd:queue-parallel</code>&nbsp;(number) </dt>
<dd> <p> Number of jobs run in parallel in a queue. </p>
 </dd>
<dt><code>cmd:remote-completion</code>&nbsp;(boolean) </dt>
<dd> <p> a boolean to control whether or not lftp uses remote completion. When true, <code>Tab</code> key guesses if the word being completed should be a remote file name. <code>Meta-Tab</code> does remote completion always. So you can force remote completion with <code>Meta-Tab</code> when <code>cmd:remote-completion</code> is false or when the guess is wrong. </p>
 </dd>
<dt><code>cmd:save-cwd-history</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp saves last CWD of each site to <i>~/.local/share/lftp/cwd_history</i> or <i>~/.lftp/cwd_history</i>, allowing to do ``cd -&#8216;&#8216; after lftp restart. Default is true. </p>
 </dd>
<dt><code>cmd:save-rl-history</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp saves readline history to <i>~/.local/share/lftp/rl_history</i> or <i>~/.lftp/rl_history</i> on exit. Default is true. </p>
 </dd>
<dt><code>cmd:show-status</code>&nbsp;(boolean) </dt>
<dd> <p> when false, lftp does not show status line on terminal. Default is true. </p>
 </dd>
<dt><code>cmd:set-term-status</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp updates terminal status if supported (e.g. xterm). The closure for this setting is the terminal type from TERM environment variable. </p>
 </dd>
<dt><code>cmd:status-interval</code>&nbsp;(time <code>interval)</code></dt>
<dd> <p> the time interval between status updates. </p>
 </dd>
<dt><code>cmd:stifle-rl-history</code>&nbsp;(number) </dt>
<dd> <p> the number of lines to keep in readline history. </p>
 </dd>
<dt><code>cmd:term-status</code>&nbsp;(string) </dt>
<dd> <p> the format string to use to display terminal status. The closure for this setting is the terminal type from TERM environment variable. Default uses ``tsl&#8217;&#8216; and ``fsl&#8217;&#8216; termcap values. </p>
<p> The following escapes are supported: </p>
<table>
<tr VALIGN=top>
<td>\a</td>
<td>bell
</td>
</tr>
<tr VALIGN=top>
<td>\e</td>
<td>escape
</td>
</tr>
<tr VALIGN=top>
<td>\n</td>
<td>new line
</td>
</tr>
<tr VALIGN=top>
<td>\s</td>
<td>&quot;lftp&quot;
</td>
</tr>
<tr VALIGN=top>
<td>\v</td>
<td>lftp version
</td>
</tr>
<tr VALIGN=top>
<td>\T</td>
<td>the status string
</td>
</tr>
</table>
 </dd>
<dt><code>cmd:time-style</code>&nbsp;(string) </dt>
<dd> <p> This setting is the default value for cls --time-style option. </p>
 </dd>
<dt><code>cmd:trace</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp prints the commands it executes (like sh -x). </p>
 </dd>
<dt><code>cmd:verify-host</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp resolves host name immediately in `open&#8217; command. It is also possible to skip the check for a single `open&#8217; command if `&amp;&#8216; is given, or if ^Z is pressed during the check. </p>
 </dd>
<dt><code>cmd:verify-path</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp checks the path given in `cd&#8217; command. It is also possible to skip the check for a single `cd&#8217; command if `&amp;&#8216; is given, or if ^Z is pressed during the check. Examples: </p>
<pre><code>set cmd:verify-path/hftp://* false
cd directory &amp;
</code></pre>
 </dd>
<dt><code>cmd:verify-path-cached</code>&nbsp;(boolean) </dt>
<dd> <p> When false, `cd&#8217; to a directory known from cache as existent will succeed immediately. Otherwise the verification will depend on cmd:verify-path setting. </p>
 </dd>
<dt><code>color:use-color</code> (tri-boolean) </dt>
<dd> <p> when true, cls command and completion output colored file listings according to color:dir-colors setting. When set to auto, colors are used when output is a terminal. </p>
 </dd>
<dt><code>color:dir-colors</code> (string) </dt>
<dd> <p> file listing color description. By default the value of LS_COLORS environment variable is used. See <a href="/docs/linux/man/1-dircolors/">dircolors</a>(1). </p>
 </dd>
<dt><code>dns:SRV-query</code>&nbsp;(boolean) </dt>
<dd> <p> query for SRV records and use them before gethostbyname. The SRV records are only used if port is not explicitly specified. See RFC2052 for details. </p>
 </dd>
<dt><code>dns:cache-enable</code>&nbsp;(boolean) </dt>
<dd> <p> enable DNS cache. If it is off, lftp resolves host name each time it reconnects. </p>
 </dd>
<dt><code>dns:cache-expire</code> (time interval) </dt>
<dd> <p> time to live for DNS cache entries. It has format &lt;number&gt;&lt;unit&gt;+, e.g. 1d12h30m5s or just 36h. To disable expiration, set it to `inf&#8217; or `never&#8217;. </p>
 </dd>
<dt><code>dns:cache-size</code>&nbsp;(number) </dt>
<dd> <p> maximum number of DNS cache entries. </p>
 </dd>
<dt><code>dns:fatal-timeout</code> (time interval) </dt>
<dd> <p> limit the time for DNS queries. If DNS server is unavailable too long, lftp will fail to resolve a given host name. Set to `never&#8217; to disable. </p>
 </dd>
<dt><code>dns:order</code> (list of protocol names) </dt>
<dd> <p> sets the order of DNS queries. Default is ``inet6 inet&#8217;&#8216; which means first look up address in inet6 family, then inet and use them in that order. To disable inet6 (AAAA) lookup, set this variable to ``inet&#8217;&#8216;. </p>
 </dd>
<dt><code>dns:use-fork</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will fork before resolving host address. Default is true. </p>
 </dd>
<dt><code>dns:max-retries</code>&nbsp;(number) </dt>
<dd> <p> If zero, there is no limit on the number of times lftp will try to lookup an address. If &gt; 0, lftp will try only this number of times to look up an address of each address family in dns:order. </p>
 </dd>
<dt><code>dns:name</code>&nbsp;(string) </dt>
<dd> <p> This setting can be used to substitute a host name alias with another name or IP address. The host name alias is used as the setting closure, the substituted name or IP address is in the value. Multiple names or IP addresses can be separated by comma. </p>
 </dd>
<dt><code>file:charset</code>&nbsp;(string) </dt>
<dd> <p> local character set. It is set from current locale initially. </p>
 </dd>
<dt><code>file:use-lock</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp uses advisory locking on local files when opening them. </p>
 </dd>
<dt><code>file:use-fallocate</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp uses <a href="/docs/linux/man/2-fallocate/">fallocate</a>(2) or <a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a>(3) to pre-allocate storage space and reduce file fragmentation in pget and torrent commands. </p>
 </dd>
<dt><code>fish:auto-confirm</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp answers ``yes&#8217;&#8216; to all ssh questions, in particular to the question about a new host key. Otherwise it answers ``no&#8217;&#8216;. </p>
 </dd>
<dt><code>fish:charset</code>&nbsp;(string) </dt>
<dd> <p> the character set used by fish server in requests, replies and file listings. Default is empty which means the same as local. </p>
 </dd>
<dt><code>fish:connect-program</code>&nbsp;(string) </dt>
<dd> <p> the program to use for connecting to remote server. It should support `-l&#8217; option for user name, `-p&#8217; for port number. Default is `ssh -a -x&#8217;. You can set it to `rsh&#8217;, for example. For private key authentication add `-i&#8217; option with the key file. </p>
 </dd>
<dt><code>fish:shell</code>&nbsp;(string) </dt>
<dd> <p> use specified shell on server side. Default is /bin/sh. On some systems, /bin/sh exits when doing cd to a non-existent directory. lftp can handle that but it has to reconnect. Set it to /bin/bash for such systems if bash is installed. </p>
 </dd>
<dt><code>ftp:acct</code>&nbsp;(string) </dt>
<dd> <p> Send this string in ACCT command after login. The result is ignored. The closure for this setting has format <i>user [at] host</i>. </p>
 </dd>
<dt><code>ftp:anon-pass</code>&nbsp;(string) </dt>
<dd> <p> sets the password used for anonymous FTP access authentication. Default is &quot;lftp@&quot;. </p>
 </dd>
<dt><code>ftp:anon-user</code>&nbsp;(string) </dt>
<dd> <p> sets the user name used for anonymous FTP access authentication. Default is &quot;anonymous&quot;. </p>
 </dd>
<dt><code>ftp:auto-sync-mode</code>&nbsp;(regex) </dt>
<dd> <p> if first server message matches this regex, turn on sync mode for that host. </p>
 </dd>
<dt><code>ftp:catch-size</code>&nbsp;(boolean) </dt>
<dd> <p> when there is no support for SIZE command, try to catch file size from the &quot;150 Opening data connection&quot; reply. </p>
 </dd>
<dt><code>ftp:charset</code>&nbsp;(string) </dt>
<dd> <p> the character set used by FTP server in requests, replies and file listings. Default is empty which means the same as local. This setting is only used when the server does not support UTF8. </p>
 </dd>
<dt><code>ftp:client</code>&nbsp;(string) </dt>
<dd> <p> the name of FTP client to send with CLNT command, if supported by server. If it is empty, then no CLNT command will be sent. </p>
 </dd>
<dt><code>ftp:compressed-re</code>&nbsp;(regex) </dt>
<dd> <p> files with matching name will be considered compressed and &quot;MODE Z&quot; will not be used for them. </p>
 </dd>
<dt><code>ftp:bind-data-socket</code>&nbsp;(boolean) </dt>
<dd> <p> bind data socket to the interface of control connection (in passive mode). Default is true, exception is the loopback interface. </p>
 </dd>
<dt><code>ftp:fix-pasv-address</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will try to correct address returned by server for PASV command in case when server address is in public network and PASV returns an address from a private network. In this case lftp would substitute server address instead of the one returned by PASV command, port number would not be changed. Default is true. </p>
 </dd>
<dt><code>ftp:fxp-passive-source</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will try to set up source FTP server in passive mode first, otherwise destination one. If first attempt fails, lftp tries to set them up the other way. If the other disposition fails too, lftp falls back to plain copy. See also ftp:use-fxp. </p>
 </dd>
<dt><code>ftp:home</code>&nbsp;(string) </dt>
<dd> <p> Initial directory. Default is empty string which means auto. Set this to `/&#8216; if you don&#8217;t like the look of %2F in FTP URLs. The closure for this setting has format <i>user [at] host</i>. </p>
 </dd>
<dt><code>ftp:ignore-pasv-address</code>&nbsp;(boolean) </dt>
<dd> <p> If true, lftp uses control connection address instead of the one returned in PASV reply for data connection. This can be useful for broken NATs. Default is false. </p>
 </dd>
<dt><code>ftp:list-empty-ok</code>&nbsp;(boolean) </dt>
<dd> <p> if set to false, empty lists from LIST command will be treated as incorrect, and another method (NLST) will be used. </p>
 </dd>
<dt><code>ftp:list-options</code>&nbsp;(string) </dt>
<dd> <p> sets options which are always appended to LIST command. It can be useful to set this to `-a&#8217; if server does not show dot (hidden) files by default. Default is empty. </p>
 </dd>
<dt><code>ftp:mode-z-level</code>&nbsp;(number) </dt>
<dd> <p> compression level (0-9) for uploading with MODE Z. </p>
 </dd>
<dt><code>ftp:nop-interval</code>&nbsp;(seconds) </dt>
<dd> <p> delay between NOOP commands when downloading tail of a file. This is useful for FTP servers which send &quot;Transfer complete&quot; message before flushing data transfer. In such cases NOOP commands can prevent connection timeout. </p>
 </dd>
<dt><code>ftp:passive-mode</code>&nbsp;(boolean) </dt>
<dd> <p> sets passive FTP mode. This can be useful if you are behind a firewall or a dumb masquerading router. In passive mode lftp uses PASV command, not the PORT command which is used in active mode. In passive mode lftp itself makes the data connection to the server; in active mode the server connects to lftp for data transfer. Passive mode is the default. </p>
 </dd>
<dt><code>ftp:port-ipv4</code> (ipv4 address) </dt>
<dd> <p> specifies an IPv4 address to send with PORT command. Default is empty which means to send the address of local end of control connection. </p>
 </dd>
<dt><code>ftp:port-range</code>&nbsp;(from-to) </dt>
<dd> <p> allowed port range for the local side of the data connection. Format is min-max, or `full&#8217; or `any&#8217; to indicate any port. Default is `full&#8217;. </p>
 </dd>
<dt><code>ftp:prefer-epsv</code>&nbsp;(boolean) </dt>
<dd> <p> use EPSV as preferred passive mode. Default is `false&#8217;. </p>
 </dd>
<dt><code>ftp:proxy</code>&nbsp;(URL) </dt>
<dd> <p> specifies FTP proxy to use. To disable proxy set this to empty string. Note that it is a FTP proxy which uses FTP protocol, not FTP over HTTP. Default value is taken from environment variable <code>ftp_proxy</code> if it starts with ``<a href="ftp://''.">ftp://&#8216;&#8216;.</a> If your FTP proxy requires authentication, specify user name and password in the URL. If ftp:proxy starts with http:// then hftp protocol (FTP over HTTP proxy) is used instead of FTP automatically. </p>
 </dd>
<dt><code>ftp:proxy-auth-type</code>&nbsp;(string) </dt>
<dd> <p> When set to ``joined&#8217;&#8216;, lftp sends ``user [at] proxy_user@<a href="ftp://ftp.example.org">ftp.example.org</a>&#8216;&#8216; as user name to proxy, and ``password [at] proxy_password&#8217;&#8216; as password. </p>
 </dd>
<dd> <p> When set to ``joined-acct&#8217;&#8216;, lftp sends ``user [at] ftp.example.org proxy_user&#8217;&#8216; (with space) as user name to proxy. The site password is sent as usual and the proxy password is expected in the following ACCT command. </p>
 </dd>
<dd> <p> When set to ``open&#8217;&#8216;, lftp first sends proxy user and proxy password and then ``OPEN <a href="ftp://ftp.example.org">ftp.example.org</a>&#8216;&#8216; followed by ``USER user&#8217;&#8216;. The site password is then sent as usual. </p>
 </dd>
<dd> <p> When set to ``user&#8217;&#8216; (default), lftp first sends proxy user and proxy password and then ``user [at] ftp.example.org&#8217;&#8216; as user name. The site password is then sent as usual. </p>
 </dd>
<dd> <p> When set to ``proxy-user [at] host&#8217;&#8216;, lftp first sends ``USER proxy_user [at] ftp.example.org&#8217;&#8216;, then proxy password. The site user and password are then sent as usual. </p>
 </dd>
<dt><code>ftp:rest-list</code>&nbsp;(boolean) </dt>
<dd> <p> allow usage of REST command before LIST command. This might be useful for large directories, but some FTP servers silently ignore REST before LIST. </p>
 </dd>
<dt><code>ftp:rest-stor</code>&nbsp;(boolean) </dt>
<dd> <p> if false, lftp will not try to use REST before STOR. This can be useful for some buggy servers which corrupt (fill with zeros) the file if REST followed by STOR is used. </p>
 </dd>
<dt><code>ftp:retry-530</code>&nbsp;(regex) </dt>
<dd> <p> Retry on server reply 530 for PASS command if text matches this regular expression. This setting should be useful to distinguish between overloaded server (temporary condition) and incorrect password (permanent condition). </p>
 </dd>
<dt><code>ftp:retry-530-anonymous</code>&nbsp;(regex) </dt>
<dd> <p> Additional regular expression for anonymous login, like ftp:retry-530. </p>
 </dd>
<dt><code>ftp:site-group</code>&nbsp;(string) </dt>
<dd> <p> Send this string in SITE GROUP command after login. The result is ignored. The closure for this setting has format <i>user [at] host</i>. </p>
 </dd>
<dt><code>ftp:skey-allow</code>&nbsp;(boolean) </dt>
<dd> <p> allow sending skey/opie reply if server appears to support it. On by default. </p>
 </dd>
<dt><code>ftp:skey-force</code>&nbsp;(boolean) </dt>
<dd> <p> do not send plain text password over the network, use skey/opie instead. If skey/opie is not available, assume failed login. Off by default. </p>
 </dd>
<dt><code>ftp:ssl-allow</code>&nbsp;(boolean) </dt>
<dd> <p> if true, try to negotiate SSL connection with FTP server for non-anonymous access. Default is true. This and other SSL settings are only available if lftp was compiled with an ssl/tls library. </p>
 </dd>
<dt><code>ftp:ssl-auth</code>&nbsp;(string) </dt>
<dd> <p> the argument for AUTH command, can be one of SSL, TLS, TLS-P, TLS-C. See RFC4217 for explanations. By default TLS or SSL will be used, depending on FEAT reply. </p>
 </dd>
<dt><code>ftp:ssl-data-use-keys</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp loads ssl:key-file for protected data connection too. When false, it does not, and the server can match data and control connections by session ID. Default is true. </p>
 </dd>
<dt><code>ftp:ssl-force</code>&nbsp;(boolean) </dt>
<dd> <p> if true, refuse to send password in clear when server does not support SSL. Default is false. </p>
 </dd>
<dt><code>ftp:ssl-protect-data</code>&nbsp;(boolean) </dt>
<dd> <p> if true, request SSL connection for data transfers. This is cpu-intensive but provides privacy. Default is false. </p>
 </dd>
<dt><code>ftp:ssl-protect-fxp</code>&nbsp;(boolean) </dt>
<dd> <p> if true, request SSL connection for data transfer between two FTP servers in FXP mode. CPSV or SSCN command will be used in that case. If SSL connection fails for some reason, lftp would try unprotected FXP transfer unless ftp:ssl-force is set for any of the two servers. Default is false. </p>
 </dd>
<dt><code>ftp:ssl-protect-list</code>&nbsp;(boolean) </dt>
<dd> <p> if true, request SSL connection for file list transfers. Default is true. </p>
 </dd>
<dt><code>ftp:ssl-use-ccc</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp would issue CCC command after logon, thus disable ssl protection layer on control connection. </p>
 </dd>
<dt><code>ftp:stat-interval</code> (time interval) </dt>
<dd> <p> interval between STAT commands. Default is 1 second. </p>
 </dd>
<dt><code>ftp:strict-multiline</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp strictly checks for multiline reply format (expects it to end with the same code as it started with). When false, this check is relaxed. </p>
 </dd>
<dt><code>ftp:sync-mode</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will send one command at a time and wait for response. This might be useful if you are using a buggy FTP server or router. When it is off, lftp sends a pack of commands and waits for responses - it speeds up operation when round trip time is significant. Unfortunately it does not work with all FTP servers and some routers have troubles with it, so it is on by default. </p>
 </dd>
<dt><code>ftp:timezone</code>&nbsp;(string) </dt>
<dd> <p> Assume this timezone for time in listings returned by LIST command. This setting can be GMT offset [+|-]HH[:MM[:SS]] or any valid TZ value (e.g. Europe/Moscow or MSK-3MSD,M3.5.0,M10.5.0/3). The default is GMT. Set it to an empty value to assume local timezone specified by environment variable TZ. </p>
 </dd>
<dt><code>ftp:too-many-re</code>&nbsp;(regexp) </dt>
<dd> <p> Decrease the dynamic connection limit when 421 reply line matches this regular expression. </p>
 </dd>
<dt><code>ftp:trust-feat</code>&nbsp;(string) </dt>
<dd> <p> When true, assume that FEAT returned data are correct and don&#8217;t use common protocol extensions like SIZE, MDTM, REST if they are not listed. Default is false. </p>
 </dd>
<dt><code>ftp:use-abor</code>&nbsp;(boolean) </dt>
<dd> <p> if false, lftp does not send ABOR command but closes data connection immediately. </p>
 </dd>
<dt><code>ftp:use-allo</code>&nbsp;(boolean) </dt>
<dd> <p> when true (default), lftp sends ALLO command before uploading a file. </p>
 </dd>
<dt><code>ftp:use-feat</code>&nbsp;(boolean) </dt>
<dd> <p> when true (default), lftp uses FEAT command to determine extended features of ftp server. </p>
 </dd>
<dt><code>ftp:use-fxp</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will try to set up direct connection between two ftp servers. </p>
 </dd>
<dt><code>ftp:use-hftp</code>&nbsp;(boolean) </dt>
<dd> <p> when ftp:proxy points to an http proxy, this setting selects hftp method (GET, HEAD) when true, and CONNECT method when false. Default is true. </p>
 </dd>
<dt><code>ftp:use-ip-tos</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp uses IPTOS_LOWDELAY for control connection and IPTOS_THROUGHPUT for data connections. </p>
 </dd>
<dt><code>ftp:lang</code>&nbsp;(boolean) </dt>
<dd> <p> the language selected with LANG command, if supported as indicated by FEAT response. Default is empty which means server default. </p>
 </dd>
<dt><code>ftp:use-mdtm</code>&nbsp;(boolean) </dt>
<dd> <p> when true (default), lftp uses MDTM command to determine file modification time. </p>
 </dd>
<dt><code>ftp:use-mdtm-overloaded</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp uses two argument MDTM command to set file modification time on uploaded files. Default is false. </p>
 </dd>
<dt><code>ftp:use-mlsd</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp will use MLSD command for directory listing if supported by the server. </p>
 </dd>
<dt><code>ftp:use-mode-z</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp will use &quot;MODE Z&quot; if supported by the server to perform compressed transfers. </p>
 </dd>
<dt><code>ftp:use-site-idle</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp sends `SITE IDLE&#8217; command with net:idle argument. Default is false. </p>
 </dd>
<dt><code>ftp:use-site-utime</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp sends 5-argument `SITE UTIME&#8217; command to set file modification time on uploaded files. Default is true. </p>
 </dd>
<dt><code>ftp:use-site-utime2</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp sends 2-argument `SITE UTIME&#8217; command to set file modification time on uploaded files. Default is true. If 5-argument `SITE UTIME&#8217; is also enabled, 2-argument command is tried first. </p>
 </dd>
<dt><code>ftp:use-size</code>&nbsp;(boolean) </dt>
<dd> <p> when true (default), lftp uses SIZE command to determine file size. </p>
 </dd>
<dt><code>ftp:use-stat</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp sends STAT command in FXP mode transfer to know how much data has been transferred. See also ftp:stat-interval. Default is true. </p>
 </dd>
<dt><code>ftp:use-stat-for-list</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp uses STAT instead of LIST command. By default `.&#8216; is used as STAT argument. Using STAT, lftp avoids creating data connection for directory listing. Some servers require special options for STAT, use ftp:list-options to specify them (e.g. <code>-la</code>). </p>
 </dd>
<dt><code>ftp:use-telnet-iac</code>&nbsp;(boolean) </dt>
<dd> <p> when true (default), lftp uses TELNET IAC command and follows TELNET protocol as specified in RFC959. When false, it does not follow TELNET protocol and thus does not double 255 (0xFF, 0377) character and does not prefix ABOR and STAT commands with TELNET IP+SYNCH signal. </p>
 </dd>
<dt><code>ftp:use-tvfs</code> (tri-boolean) </dt>
<dd> <p> When set to auto, usage of TVFS feature depends on FEAT server reply. Otherwise this setting tells whether use it or not. In short, if a server supports TVFS feature then it uses unix-like paths. </p>
 </dd>
<dt><code>ftp:use-utf8</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp sends `OPTS UTF8 ON&#8217; to the server to activate UTF-8 encoding (if supported). Disable it if the file names have a different encoding and the server has a trouble with it. </p>
 </dd>
<dt><code>ftp:use-quit</code> (boolean) </dt>
<dd> <p> if true, lftp sends QUIT before disconnecting from ftp server. Default is true. </p>
 </dd>
<dt><code>ftp:verify-address</code>&nbsp;(boolean) </dt>
<dd> <p> verify that data connection comes from the network address of control connection peer. This can possibly prevent data connection spoofing which can lead to data corruption. Unfortunately, this can fail for certain ftp servers with several network interfaces, when they do not set outgoing address on data socket, so it is disabled by default. </p>
 </dd>
<dt><code>ftp:verify-port</code>&nbsp;(boolean) </dt>
<dd> <p> verify that data connection has port 20 (ftp-data) on its remote end. This can possibly prevent data connection spoofing by users of remote host. Unfortunately, too many windows and even unix ftp servers forget to set proper port on data connection, thus this check is off by default. </p>
 </dd>
<dt><code>ftp:web-mode</code>&nbsp;(boolean) </dt>
<dd> <p> disconnect after closing data connection. This can be useful for totally broken ftp servers. Default is false. </p>
 </dd>
<dt><code>ftps:initial-prot</code>&nbsp;(string) </dt>
<dd> <p> specifies initial PROT setting for FTPS connections. Should be one of: C, S, E, P, or empty. Default is empty which means unknown, so that lftp will use PROT command unconditionally. If PROT command turns out to be unsupported, then Clear mode would be assumed. </p>
 </dd>
<dt><code>hftp:cache</code>&nbsp;(boolean) </dt>
<dd> <p> allow server/proxy side caching for ftp-over-http protocol. </p>
 </dd>
<dt><code>hftp:cache-control</code>&nbsp;(string) </dt>
<dd> <p> specify corresponding HTTP request header. </p>
 </dd>
<dt><code>hftp:decode</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp automatically decodes the entity in hftp protocol when Content-Encoding header value matches deflate, gzip, compress, x-gzip or x-compress. </p>
 </dd>
<dt><code>hftp:proxy</code>&nbsp;(URL) </dt>
<dd> <p> specifies HTTP proxy for FTP-over-HTTP protocol (hftp). The protocol hftp cannot work without a HTTP proxy, obviously. Default value is taken from environment variable <code>ftp_proxy</code> if it starts with ``<a rel="nofollow" href="http://'',">http://&#8216;&#8216;,</a> otherwise from environment variable <code>http_proxy</code>. If your FTP proxy requires authentication, specify user name and password in the URL. </p>
 </dd>
<dt><code>hftp:use-allprop</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will send `&lt;allprop/&gt;&#8216; request body in `PROPFIND&#8217; requests, otherwise it will send an empty request body. </p>
 </dd>
<dt><code>hftp:use-authorization</code>&nbsp;(boolean) </dt>
<dd> <p> if set to off, lftp will send password as part of URL to the proxy. This may be required for some proxies (e.g. M-soft). Default is on, and lftp will send password as part of Authorization header. </p>
 </dd>
<dt><code>hftp:use-head</code>&nbsp;(boolean) </dt>
<dd> <p> if set to off, lftp will try to use `GET&#8217; instead of `HEAD&#8217; for hftp protocol. While this is slower, it may allow lftp to work with some proxies which don&#8217;t understand or mishandle ``HEAD <a href="ftp://''">ftp://&#8216;&#8216;</a> requests. </p>
 </dd>
<dt><code>hftp:use-mkcol</code>&nbsp;(boolean) </dt>
<dd> <p> if set to off, lftp will try to use `PUT&#8217; instead of `MKCOL&#8217; to create directories with hftp protocol. Default is off. </p>
 </dd>
<dt><code>hftp:use-propfind</code>&nbsp;(boolean) </dt>
<dd> <p> if set to off, lftp will not try to use `PROPFIND&#8217; to get directory contents with hftp protocol and use `GET&#8217; instead. Default is off. When enabled, lftp will also use PROPPATCH to set file modification time after uploading. </p>
 </dd>
<dt><code>hftp:use-range</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp will use Range header for transfer restart. </p>
 </dd>
<dt><code>hftp:use-type</code>&nbsp;(boolean) </dt>
<dd> <p> If set to off, lftp won&#8217;t try to append `;type=&#8216; to URLs passed to proxy. Some broken proxies don&#8217;t handle it correctly. Default is on. </p>
 </dd>
<dt><code>http:accept, http:accept-charset, http:accept-encoding, http:accept-language</code> (string) </dt>
<dd> <p> specify corresponding HTTP request headers. </p>
 </dd>
<dt><code>http:authorization</code>&nbsp;(string) </dt>
<dd> <p> the authorization to use by default, when no user is specified. The format is ``user:password&#8217;&#8216;. Default is empty which means no authorization. </p>
 </dd>
<dt><code>http:cache</code>&nbsp;(boolean) </dt>
<dd> <p> allow server/proxy side caching. </p>
 </dd>
<dt><code>http:cache-control</code>&nbsp;(string) </dt>
<dd> <p> specify corresponding HTTP request header. </p>
 </dd>
<dt><code>http:cookie</code>&nbsp;(string) </dt>
<dd> <p> send this cookie to server. A closure is useful here: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set cookie/<a rel="nofollow" href="http://www.somehost.com">www.somehost.com</a>&nbsp;&quot;param=value&quot; </p>
 </dd>
<dt><code>http:decode</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp automatically decodes the entity when Content-Encoding header value matches deflate, gzip, compress, x-gzip or x-compress. </p>
 </dd>
<dt><code>http:post-content-type</code> (string) </dt>
<dd> <p> specifies value of Content-Type HTTP request header for POST method. Default is ``application/x-www-form-urlencoded&#8217;&#8216;. </p>
 </dd>
<dt><code>http:proxy</code>&nbsp;(URL) </dt>
<dd> <p> specifies HTTP proxy. It is used when lftp works over HTTP protocol. Default value is taken from environment variable <code>http_proxy</code>. If your proxy requires authentication, specify user name and password in the URL. </p>
 </dd>
<dt><code>http:put-method</code> (PUT or POST) </dt>
<dd> <p> specifies which HTTP method to use on put. </p>
 </dd>
<dt><code>http:put-content-type</code> (string) </dt>
<dd> <p> specifies value of Content-Type HTTP request header for PUT method. </p>
 </dd>
<dt><code>http:referer</code> (string) </dt>
<dd> <p> specifies value for Referer HTTP request header. Single dot `.&#8216; expands to current directory URL. Default is `.&#8216;. Set to empty string to disable Referer header. </p>
 </dd>
<dt><code>http:set-cookies</code> (boolean) </dt>
<dd> <p> if true, lftp modifies http:cookie variables when Set-Cookie header is received. </p>
 </dd>
<dt><code>http:use-allprop</code>&nbsp;(boolean) </dt>
<dd> <p> if true, lftp will send `&lt;allprop/&gt;&#8216; request body in `PROPFIND&#8217; requests, otherwise it will send an empty request body. </p>
 </dd>
<dt><code>http:use-mkcol</code>&nbsp;(boolean) </dt>
<dd> <p> if set to off, lftp will try to use `PUT&#8217; instead of `MKCOL&#8217; to create directories with HTTP protocol. Default is on. </p>
 </dd>
<dt><code>http:use-propfind</code>&nbsp;(boolean) </dt>
<dd> <p> if set to off, lftp will not try to use `PROPFIND&#8217; to get directory contents with HTTP protocol and use `GET&#8217; instead. Default is off. When enabled, lftp will also use PROPPATCH to set `Last-Modified&#8217; property after a file upload. </p>
 </dd>
<dt><code>http:use-range</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp will use Range header for transfer restart. </p>
 </dd>
<dt><code>http:user-agent</code> (string) </dt>
<dd> <p> the string lftp sends in User-Agent header of HTTP request. </p>
 </dd>
<dt><code>https:proxy</code> (string) </dt>
<dd> <p> specifies https proxy. Default value is taken from environment variable <code>https_proxy</code>. </p>
 </dd>
<dt><code>log:enabled</code>&nbsp;(boolean) </dt>
<dd> <p> when true, the log messages are output. The closure for this and other `log:&#8216; variables is either `debug&#8217; for debug messages or `xfer&#8217; for transfer logging. </p>
 </dd>
<dt><code>log:file</code> (string) </dt>
<dd> <p> the target output file for logging. When empty, <code>stderr</code> is used. </p>
 </dd>
<dt><code>log:level</code> (number) </dt>
<dd> <p> the log verbosity level. Currently it&#8217;s only defined for `debug&#8217; closure. </p>
 </dd>
<dt><code>log:max-size</code> (number) </dt>
<dd> <p> maximum size of the log file. When the size is reached, the file is renamed and started anew. </p>
 </dd>
<dt><code>log:prefix-error</code> (string) </dt>
<dd>  </dd>
<dt><code>log:prefix-note</code> (string) </dt>
<dd>  </dd>
<dt><code>log:prefix-recv</code> (string) </dt>
<dd>  </dd>
<dt><code>log:prefix-send</code> (string) </dt>
<dd> <p> the prefixes for corresponding types of debug messages. </p>
 </dd>
<dt><code>log:show-ctx</code>&nbsp;(boolean) </dt>
<dd>  </dd>
<dt><code>log:show-pid</code>&nbsp;(boolean) </dt>
<dd>  </dd>
<dt><code>log:show-time</code>&nbsp;(boolean) </dt>
<dd> <p> select additional information in the log messages. </p>
 </dd>
<dt><code>mirror:dereference</code> (boolean) </dt>
<dd> <p> when true, mirror will dereference symbolic links by default. You can override it by --no-dereference option. Default if false. </p>
 </dd>
<dt><code>mirror:exclude-regex</code> (regex) </dt>
<dd> <p> specifies default exclusion pattern. You can override it by --include option. </p>
 </dd>
<dt><code>mirror:include-regex</code> (regex) </dt>
<dd> <p> specifies default inclusion pattern. It is used just after mirror:exclude-regex is applied. It is never used if mirror:exclude-regex is empty. </p>
 </dd>
<dt><code>mirror:no-empty-dirs</code> (boolean) </dt>
<dd> <p> when true, mirror doesn&#8217;t create empty directories (like --no-empty-dirs option). </p>
 </dd>
<dt><code>mirror:sort-by</code> (string) </dt>
<dd> <p> specifies order of file transfers. Valid values are: name, name-desc, size, size-desc, date, date-desc. When the value is name or name-desc, then mirror:order setting also affects the order or transfers. </p>
 </dd>
<dt><code>mirror:order</code> (list of patterns) </dt>
<dd> <p> specifies order of file transfers when sorting by name. E.g. setting this to &quot;*.sfv *.sum&quot; makes mirror to transfer files matching *.sfv first, then ones matching *.sum and then all other files. To process directories after other files, add &quot;*/&quot; to the end of pattern list. </p>
 </dd>
<dt><code>mirror:overwrite</code> (boolean) </dt>
<dd> <p> when true, mirror will overwrite plain files instead of removing and re-creating them. </p>
 </dd>
<dt><code>mirror:parallel-directories</code> (boolean) </dt>
<dd> <p> if true, mirror will start processing of several directories in parallel when it is in parallel mode. Otherwise, it will transfer files from a single directory before moving to other directories. </p>
 </dd>
<dt><code>mirror:parallel-transfer-count</code> (number) </dt>
<dd> <p> specifies number of parallel transfers mirror is allowed to start. You can override it with --parallel option. A closure can be matched against source or target host names, the minimum number greater than 0 is used. </p>
 </dd>
<dt><code>mirror:require-source</code>&nbsp;(boolean) </dt>
<dd> <p> When true, mirror requires a source directory to be specified explicitly, otherwise it is supposed to be the current directory. </p>
 </dd>
<dt><code>mirror:set-permissions</code>&nbsp;(boolean) </dt>
<dd> <p> When set to off, mirror won&#8217;t try to copy file and directory permissions. You can override it by --perms option. Default is on. </p>
 </dd>
<dt><code>mirror:skip-noaccess</code>&nbsp;(boolean) </dt>
<dd> <p> when true, mirror does not try to download files which are obviously inaccessible by the permission mask. Default is false. </p>
 </dd>
<dt><code>mirror:use-pget-n</code> (number) </dt>
<dd> <p> specifies -n option for pget command used to transfer every single file under mirror. A closure can be matched against source or target host names, the minimum number greater than 0 is used. When the value is less than 2, pget is not used. </p>
 </dd>
<dt><code>module:path</code>&nbsp;(string) </dt>
<dd> <p> colon separated list of directories to look for modules. Can be initialized by environment variable LFTP_MODULE_PATH. Default is `PKGLIBDIR/VERSION:PKGLIBDIR&#8217;. </p>
 </dd>
<dt><code>net:connection-limit</code>&nbsp;(number) </dt>
<dd> <p> maximum number of concurrent connections to the same site. 0 means unlimited. </p>
 </dd>
<dt><code>net:connection-limit-timer</code> (time interval) </dt>
<dd> <p> increase the dynamic connection limit after this time interval. </p>
 </dd>
<dt><code>net:connection-takeover</code>&nbsp;(boolean) </dt>
<dd> <p> if true, foreground connections have priority over background ones and can interrupt background transfers to complete a foreground operation. </p>
 </dd>
<dt><code>net:idle</code> (time interval) </dt>
<dd> <p> disconnect from server after this idle time. Default is 3 minutes. </p>
 </dd>
<dt><code>net:limit-rate</code> (bytes per second) </dt>
<dd> <p> limit transfer rate on data connection. 0 means unlimited. You can specify two numbers separated by colon to limit download and upload rate separately. Suffixes are supported, e.g. 100K means 102400. </p>
 </dd>
<dt><code>net:limit-max</code>&nbsp;(bytes) </dt>
<dd> <p> limit accumulating of unused limit-rate. 0 means twice of limit-rate. </p>
 </dd>
<dt><code>net:limit-total-rate</code> (bytes per second) </dt>
<dd> <p> limit transfer rate of all connections in sum. 0 means unlimited. You can specify two numbers separated by colon to limit download and upload rate separately. Note that sockets have receive buffers on them, this can lead to network link load higher than this rate limit just after transfer beginning. You can try to set net:socket-buffer to relatively small value to avoid this. </p>
 </dd></dl>
<p> If you specify a closure, then rate limitation will be applied to sum of connections to a single matching host. </p>
<dl>
<dt><code>net:limit-total-max</code>&nbsp;(bytes) </dt>
<dd> <p> limit accumulating of unused limit-total-rate. 0 means twice of limit-total-rate. </p>
 </dd>
<dt><code>net:max-retries</code>&nbsp;(number) </dt>
<dd> <p> the maximum number of sequential tries of an operation without success. 0 means unlimited. 1 means no retries. </p>
 </dd>
<dt><code>net:no-proxy</code>&nbsp;(string) </dt>
<dd> <p> contains comma separated list of domains for which proxy should not be used. Default is taken from environment variable <code>no_proxy</code>. </p>
 </dd>
<dt><code>net:persist-retries</code> (number) </dt>
<dd> <p> ignore this number of hard errors. Useful to login to buggy FTP servers which reply 5xx when there is too many users. </p>
 </dd>
<dt><code>net:reconnect-interval-base</code>&nbsp;(seconds) </dt>
<dd> <p> sets the base minimal time between reconnects. Actual interval depends on net:reconnect-interval-multiplier and number of attempts to perform an operation. </p>
 </dd>
<dt><code>net:reconnect-interval-max</code>&nbsp;(seconds) </dt>
<dd> <p> sets maximum reconnect interval. When current interval after multiplication by net:reconnect-interval-multiplier reaches this value (or exceeds it), it is reset back to net:reconnect-interval-base. </p>
 </dd>
<dt><code>net:reconnect-interval-multiplier</code>&nbsp;(real number) </dt>
<dd> <p> sets multiplier by which base interval is multiplied each time new attempt to perform an operation fails. When the interval reaches maximum, it is reset to base value. See net:reconnect-interval-base and net:reconnect-interval-max. </p>
 </dd>
<dt><code>net:socket-bind-ipv4</code> (ipv4 address) </dt>
<dd> <p> bind all IPv4 sockets to specified address. This can be useful to select a specific network interface to use. Default is empty which means not to bind IPv4 sockets, operating system will choose an address automatically using routing table. </p>
 </dd>
<dt><code>net:socket-bind-ipv6</code> (ipv6 address) </dt>
<dd> <p> the same for IPv6 sockets. </p>
 </dd>
<dt><code>net:socket-buffer</code>&nbsp;(bytes) </dt>
<dd> <p> use given size for SO_SNDBUF and SO_RCVBUF socket options. 0 means system default. </p>
 </dd>
<dt><code>net:socket-maxseg</code>&nbsp;(bytes) </dt>
<dd> <p> use given size for TCP_MAXSEG socket option. Not all operating systems support this option, but Linux does. </p>
 </dd>
<dt><code>net:timeout</code> (time interval) </dt>
<dd> <p> sets the network protocol timeout. </p>
 </dd>
<dt><code>pget:default-n</code>&nbsp;(number) </dt>
<dd> <p> default number of chunks to split the file to in pget. </p>
 </dd>
<dt><code>pget:min-chunk-size</code>&nbsp;(number) </dt>
<dd> <p> minimal chunk size to split the file to. </p>
 </dd>
<dt><code>pget:save-status</code> (time interval) </dt>
<dd> <p> save pget transfer status this often. Set to `never&#8217; to disable saving of the status file. The status is saved to a file with suffix <i>.lftp-pget-status</i>. </p>
 </dd>
<dt><code>sftp:auto-confirm</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp answers ``yes&#8217;&#8216; to all ssh questions, in particular to the question about a new host key. Otherwise it answers ``no&#8217;&#8216;. </p>
 </dd>
<dt><code>sftp:charset</code>&nbsp;(string) </dt>
<dd> <p> the character set used by SFTP server in file names and file listings. Default is empty which means the same as local. This setting is only used for SFTP protocol version prior to 4. Version 4 and later always use UTF-8. </p>
 </dd>
<dt><code>sftp:connect-program</code>&nbsp;(string) </dt>
<dd> <p> the program to use for connecting to remote server. It should support `-l&#8217; option for user name, `-p&#8217; for port number. Default is `ssh -a -x&#8217;. For private key authentication add `-i&#8217; option with the key file. </p>
 </dd>
<dt><code>sftp:max-packets-in-flight</code>&nbsp;(number) </dt>
<dd> <p> The maximum number of unreplied packets in flight. If round trip time is significant, you should increase this and size-read/size-write. Default is 16. </p>
 </dd>
<dt><code>sftp:protocol-version</code>&nbsp;(number) </dt>
<dd> <p> The protocol number to negotiate. Default is 6. The actual protocol version used depends on the server. </p>
 </dd>
<dt><code>sftp:server-program</code>&nbsp;(string) </dt>
<dd> <p> The server program implementing SFTP protocol. If it does not contain a slash `/&#8216;, it is considered a ssh2 subsystem and -s option is used when starting connect-program. Default is `sftp&#8217;. You can use rsh as transport level protocol like this: </p>
<pre><code>set sftp:connect-program rsh
set sftp:server-program /usr/libexec/openssh/sftp-server
</code></pre>
<p> Similarly you can run SFTP over SSH1. </p>
 </dd>
<dt><code>sftp:size-read</code>&nbsp;(number) </dt>
<dd> <p> Block size for reading. Default is 0x8000. </p>
 </dd>
<dt><code>sftp:size-write</code>&nbsp;(number) </dt>
<dd> <p> Block size for writing. Default is 0x8000. </p>
 </dd>
<dt><code>ssl:ca-file</code> (path to file) </dt>
<dd> <p> use specified file as Certificate Authority certificate. </p>
 </dd>
<dt><code>ssl:ca-path</code> (path to directory) </dt>
<dd> <p> use specified directory as Certificate Authority certificate repository (OpenSSL only). </p>
 </dd>
<dt><code>ssl:check-hostname</code> (boolean) </dt>
<dd> <p> when true, lftp checks if the host name used to connect to the server corresponds to the host name in its certificate. </p>
 </dd>
<dt><code>ssl:crl-file</code> (path to file) </dt>
<dd> <p> use specified file as Certificate Revocation List certificate. </p>
 </dd>
<dt><code>ssl:crl-path</code> (path to directory) </dt>
<dd> <p> use specified directory as Certificate Revocation List certificate repository (OpenSSL only). </p>
 </dd>
<dt><code>ssl:key-file</code> (path to file) </dt>
<dd> <p> use specified file as your private key. This setting is only used for ftps and https protocols. For sftp and fish protocols use sftp:connect-program and fish:connect-program respectively (add `-i&#8217; option to ssh). </p>
 </dd>
<dt><code>ssl:cert-file</code> (path to file) </dt>
<dd> <p> use specified file as your certificate. </p>
 </dd>
<dt><code>ssl:use-sni</code>&nbsp;(boolean) </dt>
<dd> <p> when true, use Server Name Indication (SNI) TLS extension. </p>
 </dd>
<dt><code>ssl:verify-certificate</code>&nbsp;(boolean) </dt>
<dd> <p> if set to yes, then verify server&#8217;s certificate to be signed by a known Certificate Authority and not be on Certificate Revocation List. You can specify either host name or certificate fingerprint in the closure. </p>
 </dd>
<dt><code>ssl:priority</code> (string) </dt>
<dd> <p> free form priority string for GnuTLS. If built with OpenSSL the understood values are <i>+</i> or <i>-</i> followed by SSL3.0, TLS1.0, TLS1.1 or TLS1.2, separated by <i>:</i>. Example: </p>
<pre><code>set ssl:priority &quot;NORMAL:-SSL3.0:-TLS1.0:-TLS1.1:+TLS1.2&quot;
</code></pre>
 </dd>
<dt><code>torrent:ip</code> (ipv4 address) </dt>
<dd> <p> IP address to send to the tracker. Specify it if you are using an HTTP proxy. </p>
 </dd>
<dt><code>torrent:ipv6</code> (ipv6 address) </dt>
<dd> <p> IPv6 address to send to the tracker. By default, first found global unicast address is used. </p>
 </dd>
<dt><code>torrent:max-peers</code>&nbsp;(number) </dt>
<dd> <p> maximum number of peers for a torrent. Least used peers are removed to maintain this limit. </p>
 </dd>
<dt><code>torrent:port-range</code>&nbsp;(from-to) </dt>
<dd> <p> port range to accept connections on. A single port is selected when a torrent starts. </p>
 </dd>
<dt><code>torrent:retracker</code>&nbsp;(URL) </dt>
<dd> <p> explicit retracker URL, e.g. `<a rel="nofollow" href="http://retracker.local/announce'.">http://retracker.local/announce&#8217;.</a> </p>
 </dd>
<dt><code>torrent:save-metadata</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp saves metadata of each torrent it works with to <i>~/.local/share/lftp/torrent/md</i> or <i>~/.lftp/torrent/md</i> directory and loads it from there if necessary. </p>
 </dd>
<dt><code>torrent:seed-max-time</code> (time interval) </dt>
<dd> <p> maximum seed time. After this period of time a complete torrent shuts down independently of ratio. It can be set to infinity if needed. </p>
 </dd>
<dt><code>torrent:seed-min-peers</code>&nbsp;(number) </dt>
<dd> <p> minimum number of peers when the torrent is complete. If there are less, new peers are actively searched for. </p>
 </dd>
<dt><code>torrent:stop-min-ppr</code> (real number) </dt>
<dd> <p> minimum per-piece-ratio to stop seeding. Use it to avoid a situation when a popular piece causes quick raise of the total ratio. </p>
 </dd>
<dt><code>torrent:stop-on-ratio</code> (real number) </dt>
<dd> <p> torrent stops when it&#8217;s complete and ratio reached this number. </p>
 </dd>
<dt><code>torrent:timeout</code> (time interval) </dt>
<dd> <p> maximum time without any progress. When it&#8217;s reached, the torrent shuts down. </p>
 </dd>
<dt><code>torrent:use-dht</code>&nbsp;(boolean) </dt>
<dd> <p> when true, DHT is used. </p>
 </dd>
<dt><code>xfer:auto-rename</code>(boolean) </dt>
<dd> <p> suggested filenames provided by the server are used if user explicitly sets this option to `on&#8217;. As this could be security risk, default is off. </p>
 </dd>
<dt><code>xfer:backup-suffix</code>&nbsp;(string) </dt>
<dd> <p> a time format string (see <a href="/docs/linux/man/3-strftime/">strftime</a>(3)) for backup file name when replacing an existing file. </p>
 </dd>
<dt><code>xfer:clobber</code>&nbsp;(boolean) </dt>
<dd> <p> if this setting is off, get commands will not overwrite existing files and generate an error instead. </p>
 </dd>
<dt><code>xfer:destination-directory</code> (path or URL to directory) </dt>
<dd> <p> This setting is used as default -O option for get and mget commands. Default is empty, which means current directory (no -O option). </p>
 </dd>
<dt><code>xfer:disk-full-fatal</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp aborts a transfer if it cannot write target file because of full disk or quota; when false, lftp waits for disk space to be freed. </p>
 </dd>
<dt><code>xfer:eta-period</code>&nbsp;(seconds) </dt>
<dd> <p> the period over which weighted average rate is calculated to produce ETA. </p>
 </dd>
<dt><code>xfer:eta-terse</code>&nbsp;(boolean) </dt>
<dd> <p> show terse ETA (only high order parts). Default is true. </p>
 </dd>
<dt><code>xfer:keep-backup</code>&nbsp;(boolean) </dt>
<dd> <p> when true, the backup file created before replacing an existing file is not removed after successful transfer. </p>
 </dd>
<dt><code>xfer:make-backup</code>&nbsp;(boolean) </dt>
<dd> <p> when true, lftp renames pre-existing file adding xfer:backup-suffix instead of overwriting it. </p>
 </dd>
<dt><code>xfer:max-redirections</code> (number) </dt>
<dd> <p> maximum number of redirections. This can be useful for downloading over HTTP. 0 prohibits redirections. </p>
 </dd>
<dt><code>xfer:parallel</code>&nbsp;(number) </dt>
<dd> <p> the default number of parallel transfers in a single get/put/mget/mput command. </p>
 </dd>
<dt><code>xfer:rate-period</code>&nbsp;(seconds) </dt>
<dd> <p> the period over which weighted average rate is calculated to be shown. </p>
 </dd>
<dt><code>xfer:temp-file-name</code>&nbsp;(string) </dt>
<dd> <p> temporary file name pattern, first asterisk is replaced by the original file name. </p>
 </dd>
<dt><code>xfer:timeout</code> (time interval) </dt>
<dd> <p> maximum time without any transfer progress. It can be used to limit maximum time to retry a transfer from a server not supporting transfer restart. </p>
 </dd>
<dt><code>xfer:use-temp-file</code>&nbsp;(boolean) </dt>
<dd> <p> when true, a file will be transferred to a temporary file in the same directory and then renamed. </p>
 </dd>
<dt><code>xfer:verify</code>&nbsp;(boolean) </dt>
<dd> <p> when true, verify-command is launched after successful transfer to validate file integrity. Zero exit code of that command should indicate correctness of the file. </p>
 </dd>
<dt><code>xfer:verify-command</code>&nbsp;(string) </dt>
<dd> <p> the command to validate file integrity. The only argument is the path to the file. </p>
 </dd></dl>
<p> The name of a variable can be abbreviated unless it becomes ambiguous. The prefix before `:&#8216; can be omitted too. You can set one variable several times for different closures, and thus you can get a particular settings for particular state. The closure is to be specified after variable name separated with slash `/&#8216;. </p>
<p> The closure for `dns:&#8216;, `net:&#8216;, `ftp:&#8216;, `http:&#8216;, `hftp:&#8216; domain variables is currently just the host name as you specify it in the `open&#8217; command (with some exceptions where closure is meaningless, e.g. dns:cache-size). For some `cmd:&#8216; domain variables the closure is current URL without path. For `log:&#8216; domain variables the closure is either `debug&#8217; or `xfer&#8217;. For other variables it is not currently used. See examples in the sample <i>l <a href="ftp://ftp.conf">ftp.conf</a></i>. </p>
<p> Certain commands and settings take a time interval parameter. It has the format Nx[Nx...], where N is time amount (floating point) and x is time unit: d - days, h - hours, m - minutes, s - seconds. Default unit is second. E.g. 5h30m or 5.5h. Also the interval can be `infinity&#8217;, `inf&#8217;, `never&#8217;, `forever&#8217; - it means infinite interval. E.g. `sleep forever&#8217; or `set dns:cache-expire never&#8217;. </p>
<p> Boolean settings can be one of (true, on, yes, 1, +) for a True value or one of (false, off, no, 0, -) for a False value. </p>
<p> Tri-boolean settings have either a boolean value or `auto&#8217;. </p>
<p> Integer settings can have a suffix: k - kibi, m - mebi, g - gigi, etc. They can also have a prefix: 0 - octal, 0x - hexadecimal. </p>
<h3>FTP asynchronous mode (pipelining)</h3>
<p> <code>Lftp</code> can speed up FTP operations by sending several commands at once and then checking all the responses. See ftp:sync-mode variable. Sometimes this does not work, thus synchronous mode is the default. You can try to turn synchronous mode off and see if it works for you. It is known that some network software dealing with address translation works incorrectly in the case of several FTP commands in one network packet. </p>
<p> RFC959 says: ``The user-process sending another command before the completion reply would be in violation of protocol; but server-FTP processes should queue any commands that arrive while a preceding command is in progress&#8217;&#8216;. Also, RFC1123 says: ``Implementors MUST NOT assume any correspondence between READ boundaries on the control connection and the Telnet EOL sequences (CR LF).&#8216;&#8216; and ``a single READ from the control connection may include more than one FTP command&#8217;&#8216;. </p>
<p> So it must be safe to send several commands at once, which speeds up operation a lot and seems to work with all Unix and VMS based ftp servers. Unfortunately, windows based servers often cannot handle several commands in one packet, and so cannot some broken routers. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></dt>
<dd> <p> Switch on debugging mode. </p>
 </dd>
<dt><code>-e</code><i> commands</i></dt>
<dd> <p> Execute given commands and don&#8217;t exit. </p>
 </dd>
<dt><code>-p</code><i> port</i></dt>
<dd> <p> Use the given port to connect. </p>
 </dd>
<dt><code>-u</code><i> user</i>[<code>,</code>pass] </dt>
<dd> <p> Use the given username and password to connect. Remember to quote the password properly in the shell. Also note that it is not secure to specify the password on command line, use <i>~/.netrc</i> file or <code>LFTP_PASSWORD</code> environment variable together with --env-password option. Alternatively you can use ssh-based protocols with authorized keys, so you don&#8217;t have to enter a password. </p>
 </dd></dl>
<dl>
<dt><code>--norc</code></dt>
<dd> <p> Don&#8217;t execute rc files from the home directory. </p>
 </dd>
<dt><code>--rcfile</code><i> file</i></dt>
<dd> <p> Execute commands from the file. May be specified multiple times. </p>
 </dd>
<dt><code>-f</code><i> script_file</i></dt>
<dd> <p> Execute commands in the file and exit. This option must be used alone without other arguments (except <code>--norc</code>). </p>
 </dd>
<dt><code>-c</code><i> commands</i></dt>
<dd> <p> Execute the given commands and exit. Commands can be separated with a semicolon, `&amp;&amp;&#8216; or `||&#8216;. Remember to quote the commands argument properly in the shell. This option must be used alone without other arguments (except <code>--norc</code>). </p>
 </dd>
<dt>Other <code>open</code> options may also be given on the <code>lftp</code> command line.</dt>
<dd>  </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables are processed by <code>lftp</code>: </p>
<dl>
<dt><code>EDITOR</code></dt>
<dd> <p> Used as local editor for the <code>edit</code> command. </p>
 </dd>
<dt><code>HOME</code></dt>
<dd> <p> Used for (local) tilde (`~&#8216;) expansion. </p>
 </dd>
<dt><code>SHELL</code></dt>
<dd> <p> Used by the <code>!</code> command to determine the shell to run. </p>
 </dd>
<dt><code>PAGER</code></dt>
<dd> <p> This should be the name of the pager to use. It&#8217;s used by the <code>more</code> and <code>zmore</code> commands. </p>
 </dd>
<dt><code>http_proxy</code>, <code>https_proxy</code></dt>
<dd> <p> Used to set initial http:proxy, hftp:proxy and https:proxy variables. </p>
 </dd>
<dt><code>ftp_proxy</code></dt>
<dd> <p> Used to set initial ftp:proxy or hftp:proxy variables, depending on URL protocol used in this environment variable. </p>
 </dd>
<dt><code>no_proxy</code></dt>
<dd> <p> Used to set initial net:no-proxy variable. </p>
 </dd>
<dt><code>LFTP_MODULE_PATH</code></dt>
<dd> <p> Used to set initial module:path variable. </p>
 </dd>
<dt><code>LFTP_HOME</code></dt>
<dd> <p> Used to locate the directory that stores user-specific configuration files. If unset, <i>~/.lftp</i> will be used. Please note that if this directory does not exist, then XDG directories will be used. </p>
 </dd>
<dt><code>LFTP_PASSWORD</code></dt>
<dd> <p> Used for --env-password <code>open</code> option. </p>
 </dd>
<dt><code>LS_COLORS</code></dt>
<dd> <p> used to set initial color:dir-colors variable. </p>
 </dd>
<dt><code>XDG_CONFIG_HOME</code>, <code>XDG_DATA_HOME</code>, <code>XDG_CACHE_HOME</code></dt>
<dd> <p> Used to locate the directories for user-specific files when <i>~/.lftp</i> (or <code>$LFTP_HOME</code> directory) does not exist. Defaults are <i>~/.config</i>, <i>~/.local/share</i> and <i>~/.cache</i> respectively. The suffix <i>/lftp</i> is appended to make the full path to the directories. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/l <a href="ftp://ftp.conf">ftp.conf</a></i></dt>
<dd> <p> system-wide startup file. Actual location depends on --sysconfdir configure option. It is <i>/etc</i> when prefix is <i>/usr</i>, <i>/usr/local/etc</i> by default. </p>
 </dd>
<dt><i>~/.config/lftp/rc </i>or <i> ~/.lftp/rc, ~/.lftprc</i></dt>
<dd> <p> These files are executed on lftp startup after <i>/etc/l <a href="ftp://ftp.conf">ftp.conf</a></i>. </p>
 </dd>
<dt><i>~/.local/share/lftp/log </i>or <i> ~/.lftp/log</i></dt>
<dd> <p> The file things are logged to when lftp moves into the background in nohup mode. </p>
 </dd>
<dt><i>~/.local/share/lftp/transfer_log </i>or <i> ~/.lftp/transfer_log</i></dt>
<dd> <p> The file transfers are logged to when log:enabled/xfer setting is set to `yes&#8217;. The location can be changed by log:file/xfer setting. </p>
 </dd>
<dt><i>~/.local/share/lftp/bookmarks </i>or <i> ~/.lftp/bookmarks</i></dt>
<dd> <p> The file is used to store lftp&#8217;s bookmarks. See the <code>bookmark</code> command. </p>
 </dd>
<dt><i>~/.local/share/lftp/cwd_history </i>or <i> ~/.lftp/cwd_history</i></dt>
<dd> <p> The file is used to store last working directories for each site visited. </p>
 </dd>
<dt><i>~/.local/share/lftp/bg/ </i>or <i> ~/.lftp/bg/</i></dt>
<dd> <p> The directory is used to store named sockets for backgrounded lftp processes. </p>
 </dd>
<dt><i>~/.cache/lftp/DHT/ </i>or <i> ~/.lftp/DHT/</i></dt>
<dd> <p> The directory is used to store DHT id and nodes cache for IPv4 and IPv6. File name suffix is the host name. </p>
 </dd>
<dt><i>~/.cache/lftp/edit/ </i>or <i> ~/.lftp/edit/</i></dt>
<dd> <p> The directory is used to store temporary files for <code>edit</code> command. </p>
 </dd>
<dt><i>~/.local/share/lftp/torrent/md/ </i>or <i> ~/.lftp/torrent/md/</i></dt>
<dd> <p> The directory is used to store torrent metadata. It is especially useful for magnet links, cached metadata can be loaded from the directory. It can also serve as torrent history, file names are the info_hash of torrents. </p>
 </dd>
<dt><i>~/.netrc</i></dt>
<dd> <p> The file is consulted to get default login and password to a server when it is specified without a protocol to the `open&#8217; command. Passwords are also searched here if an URL with user name but with no password is used. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code>ftpd</code>(8),&nbsp;<code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) <br />
 RFC854 (telnet), RFC959 (ftp), RFC1123, RFC1945 (http/1.0), RFC2052 (SRV RR), RFC2228 (ftp security extensions), RFC2389 (ftp FEAT), RFC2428 (ftp/ipv6), RFC2518 (WebDAV), RFC2616 (http/1.1), RFC2617 (http/1.1 authentication), RFC2640 (ftp i18n), RFC3659 (ftp extensions), RFC4217 (ftp over ssl), BEP0003 (BitTorrent Protocol), BEP0005 (DHT Protocol), BEP0006 (Fast Extension), BEP0007 (IPv6 Tracker Extension), BEP0009 (Extension for Peers to Send Metadata Files), BEP0010 (Extension Protocol), BEP0012 (Multitracker Metadata Extension), BEP0023 (Tracker Returns Compact Peer Lists), BEP0032 (DHT Extensions for IPv6). <br />
 <a rel="nofollow" href="https://tools.ietf.org/html/draft-preston-ftpext-deflate-04">https://tools.ietf.org/html/draft-preston-ftpext-deflate-04</a> (ftp deflate transmission mode), <br />
 <a rel="nofollow" href="https://tools.ietf.org/html/draft-ietf-secsh-filexfer-13">https://tools.ietf.org/html/draft-ietf-secsh-filexfer-13</a> (sftp). <br />
 <a rel="nofollow" href="http://wiki.theory.org/BitTorrentSpecification">http://wiki.theory.org/BitTorrentSpecification</a> <br />
 <a rel="nofollow" href="http://www.bittornado.com/docs/multitracker-spec.txt">http://www.bittornado.com/docs/multitracker-spec.txt</a> <br />
 <a rel="nofollow" href="http://www.rasterbar.com/products/libtorrent/dht_sec.html">http://www.rasterbar.com/products/libtorrent/dht_sec.html</a> (DHT security extension) <br />
 <a rel="nofollow" href="http://xbtt.sourceforge.net/udp_tracker_protocol.html">http://xbtt.sourceforge.net/udp_tracker_protocol.html</a> (UDP tracker) </p>
<h2>AUTHOR</h2>
<pre><code>Alexander V. Lukyanov
lav [at] yars.free.net
</code></pre>
<h2>ACKNOWLEDGMENTS</h2>
<p> This manual page was originally written by Christoph Lameter &lt;clameter [at] debian.org&gt;, for the Debian GNU/Linux system. The page was improved and updated later by Nicolas Lichtmaier &lt;nick [at] Feedback.com.ar&gt;, James Troup &lt;J.J.Troup [at] comp.brad.ac.uk&gt; and Alexander V. Lukyanov &lt;lav [at] yars.free.net&gt;. </p>
