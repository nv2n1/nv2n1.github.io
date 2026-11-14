---
title: "lftp(1)"
name: "lftp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lftp/"
description: "lftp – Sophisticated file transfer program"
---

<h2 class="name">NAME</h2>
<p> lftp &#8211; Sophisticated file transfer program </p>
<h2>SYNTAX</h2>
<p> <code>lftp</code> [<code>-d</code>] [<code>-e </code><i>cmd</i>] [<code>-p </code><i>port</i>] [<code>-u </code><i>user</i>[<code>,</code><i>pass</i>]] [<i>site</i>]<br />
 <code>lftp -f </code><i>script_file</i><br />
 <code>lftp -c </code><i>commands</i><br />
 <code>lftp &#8211;version</code><br />
 <code>lftp &#8211;help</code> </p>
<h2>VERSION</h2>
<p> This man page documents lftp version 4.8.1. </p>
<h2>DESCRIPTION</h2>
<p> <code>lftp</code> is a file transfer program that allows sophisticated FTP, HTTP and other connections to other hosts. If <i>site</i> is specified then lftp will connect to that site otherwise a connection has to be established with the open command. </p>
<p> <code>lftp</code> can handle several file access methods &#8211; FTP, FTPS, HTTP, HTTPS, HFTP, FISH, SFTP and file (HTTPS and FTPS are only available when lftp is compiled with GNU TLS or OpenSSL library). You can specify the method to use in `open URL&#8217; command, e.g. `open <a rel="nofollow" href="http://www.us.kernel.org/pub/linux'.">http://www.us.kernel.org/pub/linux&#8217;.</a> HFTP is ftp-over-http-proxy protocol. It can be used automatically instead of FTP if ftp:proxy is set to `<a rel="nofollow" href="http://proxy[:port]'.">http://proxy[:port]&#8217;.</a> Fish is a protocol working over an ssh connection to a unix account. SFtp is a protocol implemented in SSH2 as SFTP subsystem. </p>
<p> Besides FTP-like protocols, lftp has support for BitTorrent protocol as `torrent&#8217; command. Seeding is also supported. </p>
<p> Every operation in <code>lftp</code> is reliable, that is any non-fatal error is handled properly and the operation is repeated. So if downloading breaks, it will be restarted from the point automatically. Even if FTP server does not support the REST command, <code>lftp</code> will try to retrieve the file from the very beginning until the file is transferred completely. </p>
<p> <code>lftp</code> has shell-like command syntax allowing you to launch several commands in parallel in background (&amp;). It is also possible to group commands within () and execute them in background. All background jobs are executed in the same single process. You can bring a foreground job to background with ^Z (c-z) and back with command `wait&#8217; (or `fg&#8217; which is alias to `wait&#8217;). To list running jobs, use command `jobs&#8217;. Some commands allow redirecting their output (cat, ls, &#8230;) to file or via pipe to external command. Commands can be executed conditionally based on termination status of previous command (&amp;&amp;, ||). </p>
<p> If you exit <code>lftp</code> before all jobs are not finished yet, <code>lftp</code> will move itself to nohup mode in background. The same thing happens with a real modem hangup or when you close an xterm. </p>
<p> <code>lftp</code> has built-in mirror which can download or update a whole directory tree. There is also reverse mirror (mirror -R) which uploads or updates a directory tree on server. Mirror can also synchronize directories between two remote servers, using FXP if available. </p>
<p> There is command `at&#8217; to launch a job at specified time in current context, command `queue&#8217; to queue commands for sequential execution for current server, and much more. </p>
<p> On startup, <code>lftp</code> executes <i>/etc/l<a href="ftp://ftp.conf">ftp.conf</a></i> and then <i>~/.lftprc</i> and <i>~/.lftp/rc</i> (or <i>~/.config/lftp/rc</i> if <i>~/.lftp</i> does not exist). You can place aliases and `set&#8217; commands there. Some people prefer to see full protocol debug, use `debug&#8217; to turn the debug on. Use `debug 3&#8242; to see only greeting messages and error messages. </p>
<p> <code>lftp</code> has a number of settable variables. You can use `set -a&#8217; to see all variables and their values or `set -d&#8217; to see list of defaults. Variable names can be abbreviated and prefix can be omitted unless the rest becomes ambiguous. </p>
<p> If lftp was compiled with OpenSSL (configure &#8211;with-openssl) it includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit. (<a rel="nofollow" href="http://www.openssl.org/)">http://www.openssl.org/)</a> </p>
<h3>Commands</h3>
<p> <code>!</code><i> shell command</i> </p>
<p> Launch shell or shell command. </p>
<pre>
!ls
</pre>
<p> To do a directory listing of the local host. </p>
<p> <code>alias</code> [<i>name</i> [<i>value</i>]] </p>
<p> Define or undefine alias <i>name</i>. If <i>value</i> is omitted, the alias is undefined, else it takes the value <i>value</i>. If no argument is given the current aliases are listed. </p>
<pre>
alias dir ls -lF
alias less zmore
</pre>
<p> <code>at</code> <i>time</i> [ &#8212; <i>command</i> ] </p>
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
<p> <code>chmod</code> [<code>OPTS</code>] <i>mode files&#8230;</i> </p>
<p> Change permission mask on remote files. The mode can be an octal number or a symbolic mode (see <a href="/docs/linux/man/1-chmod/">chmod</a>(1)). </p>
<table>
<tr VALIGN=top>
<td>-c,&nbsp;</td>
<td>&#8211;changes</td>
<td>like verbose but report only when a change is made
</td>
</tr>
<tr VALIGN=top>
<td>-f,&nbsp;</td>
<td>&#8211;quiet</td>
<td>suppress most error messages
</td>
</tr>
<tr VALIGN=top>
<td>-v,&nbsp;</td>
<td>&#8211;verbose</td>
<td>output a diagnostic for every file processed
</td>
</tr>
<tr VALIGN=top>
<td>-R,&nbsp;</td>
<td>&#8211;recursive</td>
<td>change files and directories recursively
</td>
</tr>
</table>
<p> <code>close</code> [<code>-a</code>] </p>
<p> Close idle connections. By default only with the current server, use -a to close all idle connections. </p>
<p> <code>cls</code> [<code>OPTS</code>] <i>files&#8230;</i> </p>
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
<td>&#8211;all</td>
<td>show dot files
</td>
</tr>
<tr VALIGN=top>
<td>-B,&nbsp;</td>
<td>&#8211;basename</td>
<td>show basename of files only
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;block-size=SIZ</td>
<td>use SIZ-byte blocks
</td>
</tr>
<tr VALIGN=top>
<td>-d,&nbsp;</td>
<td>&#8211;directory</td>
<td> list directory entries instead of contents
</td>
</tr>
<tr VALIGN=top>
<td>-F,&nbsp;</td>
<td>&#8211;classify</td>
<td> append indicator (one of /@) to entries
</td>
</tr>
<tr VALIGN=top>
<td>-h,&nbsp;</td>
<td>&#8211;human-readable</td>
<td> print sizes in human readable format (e.g., 1K)
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;si</td>
<td> likewise, but use powers of 1000 not 1024
</td>
</tr>
<tr VALIGN=top>
<td>-k,&nbsp;</td>
<td>&#8211;kilobytes</td>
<td> like &#8211;block-size=1024
</td>
</tr>
<tr VALIGN=top>
<td>-l,&nbsp;</td>
<td>&#8211;long</td>
<td> use a long listing format
</td>
</tr>
<tr VALIGN=top>
<td>-q,&nbsp;</td>
<td>&#8211;quiet</td>
<td>don&#8217;t show status
</td>
</tr>
<tr VALIGN=top>
<td>-s,&nbsp;</td>
<td>&#8211;size</td>
<td>print size of each file
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;filesize</td>
<td> if printing size, only print size for files
</td>
</tr>
<tr VALIGN=top>
<td>-i,&nbsp;</td>
<td>&#8211;nocase</td>
<td> case-insensitive pattern matching
</td>
</tr>
<tr VALIGN=top>
<td>-I,&nbsp;</td>
<td>&#8211;sortnocase</td>
<td> sort names case-insensitively
</td>
</tr>
<tr VALIGN=top>
<td>-D,&nbsp;</td>
<td>&#8211;dirsfirst</td>
<td> list directories first
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;sort=OPT</td>
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
<td>&#8211;user, &#8211;group,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;perms, &#8211;date,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;linkcount, &#8211;links</td>
<td>show individual fields
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;time-style=STYLE</td>
<td> use specified time format
</td>
</tr>
</table>
<p> <code>command</code> <i>cmd args&#8230;</i> </p>
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
<p> <code>eval</code> [<code>-f</code> <i>format</i> ] <i>args&#8230;</i> </p>
<p> without -f it executes given arguments as a command. With -f, arguments are transformed into a new command. The format can contain plain text and placeholders $0&#8230;$9 and $@, corresponding to the arguments. </p>
<p> <code>exit</code> [<code>bg</code>] [<code>top</code>] [<code>parent</code>] [<code>kill</code>] [<i>code</i>] </p>
<p> exit will exit from lftp or move to background if there are active jobs. If no job is active, <i>code</i> is passed to operating system as lftp&#8217;s termination status. If <i>code</i> is omitted, the exit code of last command is used. </p>
<p> `exit bg&#8217; forces moving to background when cmd:move-background is false. `exit top&#8217; makes top level `shell&#8217; (internal lftp command executor) terminate. `exit parent&#8217; terminates the parent shell when running a nested script. `exit kill&#8217; kills all numbered jobs before exiting. The options can be combined, e.g. `at 08:00 &#8212; exit top kill &amp;&#8217; kills all jobs and makes lftp exit at specified time. </p>
<p> <code>fg</code> </p>
<p> Alias for `wait&#8217;. </p>
<p> <code>find</code> [<code>OPTS</code>] <i>directory&#8230;</i> </p>
<p> List files in the directory (current directory by default) recursively. This can help with servers lacking ls -R support. You can redirect output of this command. Options: </p>
<table>
<tr VALIGN=top>
<td>-d <i>MD</i>,&nbsp;</td>
<td>&#8211;max-depth=<i>MD</i></td>
<td>specify maximum scan depth
</td>
</tr>
<tr VALIGN=top>
<td>-l,&nbsp;</td>
<td>&#8211;ls </td>
<td>use long listing format
</td>
</tr>
</table>
<p> <code>ftpcopy</code> </p>
<p> Obsolete. Use one of the following instead: </p>
<pre>
get <a href="ftp://...">ftp://...</a> -o <a href="ftp://...">ftp://...</a>
get -O <a href="ftp://...">ftp://...</a> file1 file2...
put <a href="ftp://...">ftp://...</a>
mput <a href="ftp://.../*">ftp://.../*</a>
mget -O <a href="ftp://...">ftp://...</a> <a href="ftp://.../*">ftp://.../*</a>
</pre>
<p> or other combinations to get FXP transfer (directly between two FTP servers). lftp would fallback to plain copy (via client) if FXP transfer cannot be initiated or ftp:use-fxp is false. </p>
<p> <code>get</code> [<code>-E</code>] [<code>-a</code>] [<code>-c</code>] [<code>-e</code>] [<code>-P</code> <i>N</i>] [<code>-O</code> <i>base</i>] <i>rfile</i> [<code>-o</code> <i>lfile</i>] &#8230; </p>
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
<pre>
get README
get README -o debian.README
get README README.mirrors
get README -o debian.README README.mirrors -o debian.mirrors
get README -o <a href="ftp://some.host.org/debian.README">ftp://some.host.org/debian.README</a>
get README -o <a href="ftp://some.host.org/debian-dir/">ftp://some.host.org/debian-dir/</a> &nbsp;<wbr>&nbsp;<code>(end slash is important)</code>
</pre>
<p> <code>get1</code> [<i>OPTS</i>] <i>rfile</i> </p>
<p> Transfer a single file. Options: </p>
<table>
<tr VALIGN=top>
<td>-o &lt;lfile&gt;</td>
<td> destination file name (default &#8211; basename of rfile)
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
<td>&#8211;source-region=&lt;from-to&gt;</td>
<td> transfer specified region of source file
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;target-position=&lt;pos&gt;</td>
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
<td>&#8211;exist</td>
<td>return zero exit code when the patterns expand to non-empty list
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;not-exist</td>
<td>return zero exit code when the patterns expand to an empty list
</td>
</tr>
</table>
<p> Examples: </p>
<pre>
glob echo *
glob --exist *.csv &amp;&amp; echo &quot;There are *.csv files&quot;
</pre>
<p> <code>help</code> [<i>cmd</i>] </p>
<p> Print help for <i>cmd</i> or if no <i>cmd</i> was specified print a list of available commands. </p>
<p> <code>jobs</code> [<i>OPTS</i>] [<i>job_no&#8230;</i>] </p>
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
<pre>
local pwd
local ls
local mirror /dir1 /dir2
</pre>
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
<td>&#8211;continue</td>
<td> continue a mirror job if possible
</td>
</tr>
<tr VALIGN=top>
<td>-e,&nbsp;</td>
<td>&#8211;delete</td>
<td> delete files not present at the source
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;delete-excluded</td>
<td> delete files excluded at the target
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;delete-first</td>
<td> delete old files before transferring new ones
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;depth-first</td>
<td> descend into subdirectories before transferring files
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;scan-all-first</td>
<td> scan all directories recursively before transferring files
</td>
</tr>
<tr VALIGN=top>
<td>-s,&nbsp;</td>
<td>&#8211;allow-suid</td>
<td> set suid/sgid bits according to the source
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;allow-chown</td>
<td> try to set owner and group on files
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;ascii</td>
<td> use ascii mode transfers (implies &#8211;ignore-size)
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;ignore-time</td>
<td> ignore time when deciding whether to download
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;ignore-size</td>
<td> ignore size when deciding whether to download
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;only-missing</td>
<td> download only missing files
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;only-existing</td>
<td> download only files already existing at target
</td>
</tr>
<tr VALIGN=top>
<td>-n,&nbsp;</td>
<td>&#8211;only-newer</td>
<td> download only newer files (-c won&#8217;t work)
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;upload-older</td>
<td> upload even files older than the target ones
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;transfer-all</td>
<td> transfer all files, even seemingly the same at the target site
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;no-empty-dirs</td>
<td> don&#8217;t create empty directories (implies &#8211;depth-first)
</td>
</tr>
<tr VALIGN=top>
<td>-r,&nbsp;</td>
<td>&#8211;no-recursion</td>
<td> don&#8217;t go to subdirectories
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;recursion=<i>MODE</i></td>
<td> go to subdirectories on a condition
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;no-symlinks</td>
<td> don&#8217;t create symbolic links
</td>
</tr>
<tr VALIGN=top>
<td>-p,&nbsp;</td>
<td>&#8211;no-perms</td>
<td> don&#8217;t set file permissions
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;no-umask</td>
<td> don&#8217;t apply umask to file modes
</td>
</tr>
<tr VALIGN=top>
<td>-R,&nbsp;</td>
<td>&#8211;reverse</td>
<td> reverse mirror (put files)
</td>
</tr>
<tr VALIGN=top>
<td>-L,&nbsp;</td>
<td>&#8211;dereference</td>
<td> download symbolic links as files
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;overwrite</td>
<td> overwrite plain files without removing them first
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;no-overwrite</td>
<td> remove and re-create plain files instead of overwriting
</td>
</tr>
<tr VALIGN=top>
<td>-N,&nbsp;</td>
<td>&#8211;newer-than=<i>SPEC</i></td>
<td> download only files newer than specified time
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;older-than=<i>SPEC</i></td>
<td> download only files older than specified time
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;size-range=<i>RANGE</i></td>
<td> download only files with size in specified range
</td>
</tr>
<tr VALIGN=top>
<td>-P,&nbsp;</td>
<td>&#8211;parallel[=<i>N</i>]</td>
<td> download N files in parallel
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;use-pget[-n=<i>N</i>]</td>
<td> use pget to transfer every single file
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;on-change=<i>CMD</i></td>
<td> execute the command if anything has been changed
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;loop</td>
<td> repeat mirror until no changes found
</td>
</tr>
<tr VALIGN=top>
<td>-i <i>RX</i>,&nbsp;</td>
<td>&#8211;include=<i>RX</i></td>
<td> include matching files
</td>
</tr>
<tr VALIGN=top>
<td>-x <i>RX</i>,&nbsp;</td>
<td>&#8211;exclude=<i>RX</i></td>
<td> exclude matching files
</td>
</tr>
<tr VALIGN=top>
<td>-I <i>GP</i>,&nbsp;</td>
<td>&#8211;include-glob=<i>GP</i></td>
<td> include matching files
</td>
</tr>
<tr VALIGN=top>
<td>-X <i>GP</i>,&nbsp;</td>
<td>&#8211;exclude-glob=<i>GP</i></td>
<td> exclude matching files
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;include-rx-from=<i>FILE</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;exclude-rx-from=<i>FILE</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;include-glob-from=<i>FILE</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;exclude-glob-from=<i>FILE</i></td>
<td> load include/exclude patterns from the file, one per line
</td>
</tr>
<tr VALIGN=top>
<td>-f <i>FILE</i>,&nbsp;</td>
<td>&#8211;file=<i>FILE</i></td>
<td> mirror a single file or globbed group (e.g. /path/to/*.txt)
</td>
</tr>
<tr VALIGN=top>
<td>-F <i>DIR</i>,&nbsp;</td>
<td>&#8211;directory=<i>DIR</i></td>
<td> mirror a single directory or globbed group (e.g. /path/to/dir*)
</td>
</tr>
<tr VALIGN=top>
<td>-O <i>DIR</i>,&nbsp;</td>
<td>&#8211;target-directory=<i>DIR</i></td>
<td> target base path or URL
</td>
</tr>
<tr VALIGN=top>
<td>-v,&nbsp;</td>
<td>&#8211;verbose[=level]</td>
<td> verbose operation
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;log=<i>FILE</i></td>
<td> write lftp commands being executed to FILE
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;script=<i>FILE</i></td>
<td> write lftp commands to FILE, but don&#8217;t execute them
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;just-print, &#8211;dry-run</td>
<td> same as &#8211;script=-
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;max-errors=<i>N</i></td>
<td> stop after this number of errors
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;skip-noaccess</td>
<td> don&#8217;t try to transfer files with no read access.
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;use-cache</td>
<td> use cached directory listings
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;Remove-source-files</td>
<td> remove source files after transfer (use with caution)
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;Remove-source-dirs</td>
<td> remove source files and directories after transfer (use with caution). Top level directory is not removed if it&#8217;s name ends with a slash.
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;</td>
<td>&#8211;Move</td>
<td> same as &#8211;Remove-source-dirs
</td>
</tr>
<tr VALIGN=top>
<td>-a&nbsp;</td>
<td></td>
<td> same as &#8211;allow-chown &#8211;allow-suid &#8211;no-umask
</td>
</tr>
</table>
<p> <i>RX</i> is an extended regular expression, just like in <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1). </p>
<p> <i>GP</i> is a glob pattern, e.g. `*.zip&#8217;. </p>
<p> Include and exclude options can be specified multiple times. It means that a file or directory would be mirrored if it matches an include and does not match to excludes after the include, or does not match anything and the first check is exclude. Directories are matched with a slash appended. </p>
<p> Note that symbolic links are not created when uploading to remote server, because FTP protocol cannot do it. To upload files the links refer to, use `mirror -RL&#8217; command (treat symbolic links as files). </p>
<p> For options &#8211;newer-than and &#8211;older-than you can either specify a file or time specification like that used by <code><a href="/docs/linux/man/1-at/">at</a></code>(1) command, e.g. `now-7days&#8217; or `week ago&#8217;. If you specify a file, then modification time of that file will be used. </p>
<p> Verbosity level can be selected using &#8211;verbose=level option or by several -v options, e.g. -vvv. Levels are: </p>
<pre>
0 - no output (default)
1 - print actions
2 - +print not deleted file names (when -e is not specified)
3 - +print directory names which are mirrored
</pre>
<p> &#8211;only-newer turns off file size comparison and uploads/downloads only newer files even if size is different. By default older files are transferred and replace newer ones. </p>
<p> &#8211;upload-older allows replacing newer remote files with older ones (when the target side is remote). Some remote back-ends cannot preserve timestamps so the default is to keep newer files. </p>
<p> Recursion mode can be one of `always&#8217;, `never&#8217;, `missing&#8217;, `newer&#8217;. With the option `newer&#8217; mirror compares timestamps of directories and enters a directory only if it is older or missing on the target side. Be aware that when a file changes the directory timestamp may stay the same, so mirror won&#8217;t process that directory. </p>
<p> The options &#8211;file and &#8211;directory may be used multiple times and even mixed provided that base directories of the paths are the same. </p>
<p> You can mirror between two servers if you specify URLs instead of directories. FXP is automatically used for transfers between FTP servers, if possible. </p>
<p> Some FTP servers hide dot-files by default (e.g. <i>.htaccess</i>), and show them only when LIST command is used with -a option. In such case try to use `set ftp:list-options -a&#8217;. </p>
<p> &#8211;depth-first, &#8211;no-empty-dirs and setting mirror:no-empty-dirs=true. </p>
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
<td>&#8211;user <i>user</i></td>
<td>use the user for authentication
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;password <i>pass</i></td>
<td>use the password for authentication
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;env-password</td>
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
<td> specifies remote file name (default &#8211; basename of lfile)
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
<p> Add the given command to queue for sequential execution. Each site has its own queue. `-n&#8217; adds the command before the given item in the queue. Don&#8217;t try to queue `cd&#8217; or `lcd&#8217; commands, it may confuse lftp. Instead do the cd/lcd before `queue&#8217; command, and it will remember the place in which the command is to be done. It is possible to queue up an already running job by `queue wait &lt;jobno&gt;&#8217;, but the job will continue execution even if it is not the first in queue. </p>
<p> `queue stop&#8217; will stop the queue, it will not execute any new commands, but already running jobs will continue to run. You can use `queue stop&#8217; to create an empty stopped queue. `queue start&#8217; will resume queue execution. When you exit lftp, it will start all stopped queues automatically. </p>
<p> `queue&#8217; with no arguments will either create a stopped queue or print queue status. </p>
<p> <code>queue</code> <code>&#8211;delete|-d </code>[<i>index or wildcard expression</i>] </p>
<p> Delete one or more items from the queue. If no argument is given, the last entry in the queue is deleted. </p>
<p> <code>queue</code> <code>&#8211;move|-m </code>&lt;<i>index or wildcard expression</i>&gt; [<i>index</i>] </p>
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
<td> Output in a format that can be used to re-queue. Useful with &#8211;delete.
</td>
</tr>
</table>
<p> Examples: </p>
<pre>
&gt; get file &amp;
[1] get file
&gt; queue wait 1
&gt; queue get another_file
&gt; cd a_directory
&gt; queue get yet_another_file
</pre>
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
<p> For FTP &#8211; send the command uninterpreted. Use with caution &#8211; it can lead to unknown remote state and thus will cause reconnect. You cannot be sure that any change of remote state because of quoted command is solid &#8211; it can be reset by reconnect at any time. </p>
<p> For HTTP &#8211; specific to HTTP action. Syntax: &#8220;quote &lt;command&gt; [&lt;args&gt;]&#8221;. Command may be &#8220;set-cookie&#8221; or &#8220;post&#8221;. </p>
<pre>
open <a rel="nofollow" href="http://www.site.net">http://www.site.net</a>
quote set-cookie &quot;variable=value; othervar=othervalue&quot;
set http:post-content-type application/x-www-form-urlencoded
quote post /cgi-bin/script.cgi &quot;var=value&amp;othervar=othervalue&quot; &gt; local_file
</pre>
<p> For FISH &#8211; send the command uninterpreted. This can be used to execute arbitrary commands on server. The command must not take input or print ### at new line beginning. If it does, the protocol will become out of sync. </p>
<pre>
open <a href="fish://server">fish://server</a>
quote find -name \*.zip
</pre>
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
<td>&#8211;while-ok</td>
<td>stop when command exits with non-zero code
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;until-ok</td>
<td>stop when command exits with zero code
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;weak </td>
<td>stop when lftp moves to background.
</td>
</tr>
</table>
<p> Examples: </p>
<pre>
repeat at tomorrow -- mirror
repeat 1d mirror
</pre>
<p> <code>reput</code> <i>lfile</i> [<code>-o</code> <i>rfile</i>] </p>
<p> Same as `put -c&#8217;. </p>
<p> <code>rm</code> [<code>-r</code>] [<code>-f</code>] <i>files</i> </p>
<p> Remove remote files. Does not expand wildcards, use <code>mrm</code> for that. -r is for recursive directory remove. Be careful, if something goes wrong you can lose files. -f suppress error messages. </p>
<p> <code>rmdir</code> <i>dir(s)</i> </p>
<p> Remove remote directories. </p>
<p> <code>scache</code> [<i>session</i>] </p>
<p> List cached sessions or switch to specified session. </p>
<p> <code>set</code> [<i>var</i> [<i>val</i>]] </p>
<p> Set variable to given value. If the value is omitted, unset the variable. Variable name has format &#8220;name/closure&#8221;, where closure can specify exact application of the setting. See below for details. If set is called with no variable then only altered settings are listed. It can be changed by options: </p>
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
<p> Default readline binding allows quick switching between slots named 0-9 using Meta-0 &#8211; Meta-9 keys (often you can use Alt instead of Meta). </p>
<p> <code>source</code> <i>file</i><br />
 <code>source -e</code> <i>command</i> </p>
<p> Execute commands recorded in file <i>file</i> or returned by specified external command. </p>
<pre>
source ~/.lftp/rc
source -e echo help
</pre>
<p> <code>suspend</code> </p>
<p> Stop lftp process. Note that transfers will be also stopped until you continue the process with shell&#8217;s fg or bg commands. </p>
<p> <code>torrent</code> [<code>OPTS</code>] <i>torrent-files&#8230;</i> </p>
<p> Start BitTorrent process for the given <i>torrent-files</i>, which can be a local file, URL, magnet link or plain <i>info_hash</i> written in hex or base32. Local wildcards are expanded. Existing files are first validated unless <i>&#8211;force-valid</i> option is given. Missing pieces are downloaded. Files are stored in specified <i>directory</i> or current working directory by default. Seeding continues until ratio reaches <i>torrent:stop-on-ratio</i> setting or time of <i>torrent:seed-max-time</i> runs out. </p>
<p> Options: </p>
<table>
<tr VALIGN=top>
<td>-O &lt;directory&gt;</td>
<td> specifies base directory where files should be placed
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;force-valid</td>
<td> skip file validation (if you are sure they are ok).
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;only-new</td>
<td> stop if the metadata is known already or the torrent is complete.
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;only-incomplete</td>
<td> stop if the torrent is already complete.
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;dht-bootstrap=&lt;node&gt;</td>
<td> bootstrap DHT by sending a query to specified <i>node</i>. This option should be used just once to fill the local node cache. Port number may be given after colon, default is 6881. Here are some nodes for bootstrapping: dht.transmissionbt.com, router.utorrent.com, router.bittorrent.com.
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;share</td>
<td> share specified file or directory using BitTorrent protocol. Magnet link is printed when it&#8217;s ready.
</td>
</tr>
</table>
<p> <code>user</code> <i>user</i> [<i>pass</i>]<br />
 <code>user</code> <i>URL</i> [<i>pass</i>] </p>
<p> Use specified info for remote login. If you specify an URL with user name, the entered password will be cached so that future URL references can use it. </p>
<p> <code>version</code> </p>
<p> Print <code>lftp</code> version. </p>
<p> <code>wait</code> [<i>jobno</i>]<br />
 <code>wait all</code> </p>
<p> Wait for specified job to terminate. If jobno is omitted, wait for last backgrounded job. </p>
<p> `wait all&#8217; waits for all jobs to terminate. </p>
<p> <code>zcat</code> <i>files</i> </p>
<p> Same as cat, but filter each file through zcat. (See also <code>cat</code>, <code>more</code> and <code>zmore</code>) </p>
<p> <code>zmore</code> <i>files</i> </p>
<p> Same as more, but filter each file through zcat. (See also <code>cat</code>, <code>zcat</code> and <code>more</code>) </p>
<h3>Settings</h3>
<p> On startup, lftp executes <i>~/.lftprc</i> and <i>~/.lftp/rc</i> (or <i>~/.config/lftp/rc</i> if <i>~/.lftp</i> does not exist). You can place aliases and `set&#8217; commands there. Some people prefer to see full protocol debug, use `debug&#8217; to turn the debug on. </p>
<p> There is also a system-wide startup file in <i>/etc/l<a href="ftp://ftp.conf">ftp.conf</a></i>. It can be in different directory, see FILES section. </p>
<p> <code>lftp</code> has the following settable variables (you can also use `set -a&#8217; to see all variables and their values):</p>
<dl>
<dt><code>bmk:save-passwords</code>&nbsp;(boolean)</p>
<dd> save plain text passwords in <i>~/.local/share/lftp/bookmarks</i> or <i>~/.lftp/bookmarks</i> on `bookmark add&#8217; command. Off by default.</p>
<dt><code>cache:cache-empty-listings</code>&nbsp;(boolean)</p>
<dd> When false, empty listings are not cached.</p>
<dt><code>cache:enable</code>&nbsp;(boolean)</p>
<dd> When false, cache is disabled.</p>
<dt><code>cache:expire</code> (time interval)</p>
<dd> Positive cache entries expire in this time interval.</p>
<dt><code>cache:expire-negative</code> (time interval)</p>
<dd> Negative cache entries expire in this time interval.</p>
<dt><code>cache:size</code> (number)</p>
<dd> Maximum cache size. When exceeded, oldest cache entries will be removed from cache.</p>
<dt><code>cmd:at-exit</code>&nbsp;(string)</p>
<dd> the commands in string are executed before lftp exits or moves to background.</p>
<dt><code>cmd:at-exit-bg</code>&nbsp;(string)</p>
<dd> the commands in string are executed before backgrounded lftp exits.</p>
<dt><code>cmd:at-exit-fg</code>&nbsp;(string)</p>
<dd> the commands in string are executed before foreground lftp exits.</p>
<dt><code>cmd:at-background</code>&nbsp;(string)</p>
<dd> the commands in string are executed before lftp moves to background.</p>
<dt><code>cmd:at-terminate</code>&nbsp;(string)</p>
<dd> the commands in string are executed before lftp terminates (either backgrounded or foreground).</p>
<dt><code>cmd:at-finish</code>&nbsp;(string)</p>
<dd> the commands in string are executed once when all jobs are done.</p>
<dt><code>cmd:at-queue-finish</code>&nbsp;(string)</p>
<dd> the commands in string are executed once when all jobs in a queue are done.</p>
<dt><code>cmd:cls-completion-default</code>&nbsp;(string)</p>
<dd> default <code>cls</code> options for displaying completion choices. For example, to make completion listings show file sizes, set cmd:cls-completion-default to `-s&#8217;.</p>
<dt><code>cmd:cls-default</code>&nbsp;(string)</p>
<dd> default <code>cls</code> command options. They can be overridden by explicitly given options.</p>
<dt><code>cmd:cls-exact-time</code>&nbsp;(boolean)</p>
<dd> when true, <code>cls</code> would try to get exact file modification time even if it means more requests to the server.</p>
<dt><code>cmd:csh-history</code>&nbsp;(boolean)</p>
<dd> enables csh-like history expansion.</p>
<dt><code>cmd:default-protocol</code>&nbsp;(string)</p>
<dd> The value is used when `open&#8217; is used with just host name without protocol. Default is `ftp&#8217;.</p>
<dt><code>cmd:fail-exit</code>&nbsp;(boolean)</p>
<dd> if true, exit when a command fails and the following command is unconditional (i.e. does not begin with || or &amp;&amp;). lftp exits after the unconditional command is issued without executing it.</p>
<dt><code>cmd:interactive</code>&nbsp;(tri-boolean)</p>
<dd> when true, lftp acts interactively, handles terminal signals and outputs some extra messages. Default is auto and depends on stdin being a terminal.</p>
<dt><code>cmd:long-running</code>&nbsp;(seconds)</p>
<dd> time of command execution, which is considered as `long&#8217; and a beep is done before next prompt. 0 means off.</p>
<dt><code>cmd:ls-default</code>&nbsp;(string)</p>
<dd> default ls argument</p>
<dt><code>cmd:move-background</code> (boolean)</p>
<dd> when false, lftp refuses to go to background when exiting. To force it, use `exit bg&#8217;.</p>
<dt><code>cmd:move-background-detach</code> (boolean)</p>
<dd> when true (default), lftp detaches itself from the control terminal when moving to background, it is possible to attach back using `attach&#8217; command; when false, lftp tricks the shell to move lftp to background process group and continues to run, then fg shell command brings lftp back to foreground unless it has done all jobs and terminated.</p>
<dt><code>cmd:prompt</code>&nbsp;(string)</p>
<dd> The prompt. lftp recognizes the following backslash-escaped special characters that are decoded as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>\@</code></p>
<dd> insert @ if the current remote site user is not default</p>
<dt><code></code></p>
<dd> an ASCII bell character (07)</p>
<dt><code></code></p>
<dd> an ASCII escape character (033)</p>
<dt><code>\h</code></p>
<dd> the remote hostname you are connected to</p>
<dt><code>
</code></p>
<dd> newline</p>
<dt><code>\s</code></p>
<dd> the name of the client (lftp)</p>
<dt><code>\S</code></p>
<dd> current slot name</p>
<dt><code>
