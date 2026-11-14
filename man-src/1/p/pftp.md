---
title: "pftp(1)"
name: "pftp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pftp/"
description: "ftp – Internet file transfer program"
---

<p>Linux NetKit (0.17)</p>
<h2 class="name">NAME</h2>
<p> <code>ftp</code> &#8211; <code>Internet</code> file transfer program </p>
<h2>SYNOPSIS</h2>
<p> <code>ftp</code> [-<code>46pinegvd</code> ] [<i>host </i>[<i>port</i> ] ]<br />
<code>pftp</code> [-<code>46inegvd</code> ] [<i>host </i>[<i>port</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ftp</code> is the user interface to the <code>Internet</code> standard File Transfer Protocol. The program allows a user to transfer files to and from a remote network site. </p>
<p> Options may be specified at the command line, or to the command interpreter.</p>
<dl>
<dt><code>-4</code></p>
<dd> Use only IPv4 to contact any host.</p>
<dt><code>-6</code></p>
<dd> Use IPv6 only.</p>
<dt><code>-p</code></p>
<dd> Use passive mode for data transfers. Allows use of ftp in environments where a firewall prevents connections from the outside world back to the client machine. Requires that the ftp server support the PASV command. This is the default if invoked as <code>pftp.</code></p>
<dt><code>-i</code></p>
<dd> Turns off interactive prompting during multiple file transfers.</p>
<dt><code>-n</code></p>
<dd> Restrains <code>ftp</code> from attempting &ldquo;auto-login&rdquo; upon initial connection. If auto-login is enabled, <code>ftp</code> will check the .netrc (see <a href="/docs/linux/man/5-netrc/">netrc</a>(5)) file in the user&#8217;s home directory for an entry describing an account on the remote machine. If no entry exists, <code>ftp</code> will prompt for the remote machine login name (default is the user identity on the local machine), and, if necessary, prompt for a password and an account with which to login.</p>
<dt><code>-e</code></p>
<dd> Disables command editing and history support, if it was compiled into the <code>ftp</code> executable. Otherwise, does nothing.</p>
<dt><code>-g</code></p>
<dd> Disables file name globbing.</p>
<dt><code>-v</code></p>
<dd> Verbose option forces <code>ftp</code> to show all responses from the remote server, as well as report on data transfer statistics.</p>
<dt><code>-d</code></p>
<dd> Enables debugging.</dl>
<p> The client host and an optional port number with which <code>ftp</code> is to communicate may be specified on the command line. If this is done, <code>ftp</code> will immediately attempt to establish a connection to an <code>FTP</code> server on that host; otherwise, <code>ftp</code> will enter its command interpreter and await instructions from the user. When <code>ftp</code> is awaiting commands from the user the prompt `ftp&gt;&#8217; is provided to the user. The following commands are recognized by <code>ftp </code></p>
<dl>
<dt><code>! </code>[<i>command </i>[<i>args</i> ] ]</p>
<dd> Invoke an interactive shell on the local machine. If there are arguments, the first is taken to be a command to execute directly, with the rest of the arguments as its arguments.</p>
<dt><code>$ </code><i>macro-name </i>[<i>args</i> ]</p>
<dd> Execute the macro <i>macro-name</i> that was defined with the <code>macdef</code> command. Arguments are passed to the macro unglobbed.</p>
<dt><code>account </code>[<i>passwd</i> ]</p>
<dd> Supply a supplemental password required by a remote system for access to resources once a login has been successfully completed. If no argument is included, the user will be prompted for an account password in a non-echoing input mode.</p>
<dt><code>append </code><i>local-file </i>[<i>remote-file</i> ]</p>
<dd> Append a local file to a file on the remote machine. If <i>remote-file</i> is left unspecified, the local file name is used in naming the remote file after being altered by any <code>ntrans</code> or <code>nmap</code> setting. File transfer uses the current settings for <code>type </code> <code>format</code> <code>mode </code> and <code>structure</code></p>
<dt><code>ascii</code></p>
<dd> Set the file transfer <code>type</code> to network <code>ASCII</code> This is the default type.</p>
<dt><code>bell</code></p>
<dd> Arrange that a bell be sounded after each file transfer command is completed.</p>
<dt><code>binary</code></p>
<dd> Set the file transfer <code>type</code> to support binary image transfer.</p>
<dt><code>bye</code></p>
<dd> Terminate the <code>FTP</code> session with the remote server and exit <code>ftp </code> An end of file will also terminate the session and exit.</p>
<dt><code>case</code></p>
<dd> Toggle remote computer file name case mapping during <code>mget</code> commands. When <code>case</code> is on (default is off), remote computer file names with all letters in upper case are written in the local directory with the letters mapped to lower case.</p>
<dt><code>cd </code><i>remote-directory</i></p>
<dd> Change the working directory on the remote machine to <i>remote-directory </i></p>
<dt><code>cdup</code></p>
<dd> Change the remote machine working directory to the parent of the current remote machine working directory.</p>
<dt><code>chmod </code><i>mode file-name</i></p>
<dd> Change the permission modes of the file <i>file-name</i> on the remote system to <i>mode </i></p>
<dt><code>close</code></p>
<dd> Terminate the <code>FTP</code> session with the remote server, and return to the command interpreter. Any defined macros are erased.</p>
<dt><code>cr</code></p>
<dd> Toggle carriage return stripping during ascii type file retrieval. Records are denoted by a carriage return/linefeed sequence during ascii type file transfer. When <code>cr</code> is on (the default), carriage returns are stripped from this sequence to conform with the UNIX single linefeed record delimiter. Records on non- <code>UNIX </code> remote systems may contain single linefeeds; when an ascii type transfer is made, these linefeeds may be distinguished from a record delimiter only when <code>cr</code> is off.</p>
<dt><code>qc</code></p>
<dd> Toggle the printing of control characters in the output of <code>ASCII</code> type commands. When this is turned on, control characters are replaced with a question mark if the output file is the standard output. This is the default when the standard output is a tty.</p>
<dt><code>delete </code><i>remote-file</i></p>
<dd> Delete the file <i>remote-file</i> on the remote machine.</p>
<dt><code>debug </code>[<i>debug-value</i> ]</p>
<dd> Toggle debugging mode. If an optional <i>debug-value</i> is specified it is used to set the debugging level. When debugging is on, <code>ftp</code> prints each command sent to the remote machine, preceded by the string `&#8211;&gt;&#8217;</p>
<dt> <code>dir</code> [<i>remote-directory</i> ] [<i>local-file</i> ]</p>
<dd>
<dd>Print a listing of the directory contents in the directory, <i>remote-directory </i> and, optionally, placing the output in <i>local-file </i> If interactive prompting is on, <code>ftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>dir</code> output. If no directory is specified, the current working directory on the remote machine is used. If no local file is specified, or <i>local-file</i> is &#8211;<code>,</code> output comes to the terminal.</p>
<dt><code>disconnect</code></p>
<dd> A synonym for <i>close </i></p>
<dt><code>form </code><i>format</i></p>
<dd> Set the file transfer <code>form</code> to <i>format </i> The default format is &ldquo;file&rdquo;.</p>
<dt><code>get </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> Retrieve the <i>remote-file</i> and store it on the local machine. If the local file name is not specified, it is given the same name it has on the remote machine, subject to alteration by the current <code>case </code> <code>ntrans</code> and <code>nmap</code> settings. The current settings for <code>type </code> <code>form</code> <code>mode </code> and <code>structure</code> are used while transferring the file.</p>
<dt><code>glob</code></p>
<dd> Toggle filename expansion for <code>mdelete </code> <code>mget</code> and <code>mput </code> If globbing is turned off with <code>glob </code> the file name arguments are taken literally and not expanded. Globbing for <code>mput</code> is done as in <a href="/docs/linux/man/1-csh/">csh</a>(1). For <code>mdelete</code> and <code>mget </code> each remote file name is expanded separately on the remote machine and the lists are not merged. Expansion of a directory name is likely to be different from expansion of the name of an ordinary file: the exact result depends on the foreign operating system and ftp server, and can be previewed by doing `mls&#8217; remote-files &#8211; Note: <code>mget</code> and <code>mput</code> are not meant to transfer entire directory subtrees of files. That can be done by transferring a <a href="/docs/linux/man/1-tar/">tar</a>(1) archive of the subtree (in binary mode).</p>
<dt><code>hash </code>[<i>increment</i> ]</p>
<dd> Toggle hash-sign (&#8220;#&#8221;) printing for each transferred data block, but only in the absence of an argument. The size of a data block is set to 1024 bytes by default, but can be changed by the argument <i>increment</i> which also accepts the suffixed multipliers &#8216;k&#8217; and &#8216;K&#8217; for kilobytes, &#8216;m&#8217; and &#8216;M&#8217; for Megabytes, and finally &#8216;g&#8217; and &#8216;G&#8217; for Gigabytes. Setting a size activates hash printing unconditionally.</p>
<dt><code>help </code>[<i>command</i> ]</p>
<dd> Print an informative message about the meaning of <i>command </i> If no argument is given, <code>ftp</code> prints a list of the known commands.</p>
<dt><code>idle </code>[<i>seconds</i> ]</p>
<dd> Set the inactivity timer on the remote server to <i>seconds</i> seconds. If <i>seconds</i> is omitted, the current inactivity timer is printed.</p>
<dt><code>ipany</code></p>
<dd> Allow the address resolver to return any address family.</p>
<dt><code>ipv4</code></p>
<dd> Restrict the address resolver to look only for IPv4 addresses.</p>
<dt><code>ipv6</code></p>
<dd> Restrict host adressing to IPv6 only.</p>
<dt><code>lcd </code>[<i>directory</i> ]</p>
<dd> Change the working directory on the local machine. If no <i>directory</i> is specified, the user&#8217;s home directory is used.</p>
<dt> <code>ls</code> [<i>remote-directory</i> ] [<i>local-file</i> ]</p>
<dd>
<dd>Print a listing of the contents of a directory on the remote machine. The listing includes any system-dependent information that the server chooses to include; for example, most UNIX systems will produce output from the command `ls&#8217; -l . (See also <code>nlist .</code> If <i>remote-directory</i> is left unspecified, the current working directory is used. If interactive prompting is on, <code>ftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>ls</code> output. If no local file is specified, or if <i>local-file</i> is `- &#8216; the output is sent to the terminal.</p>
<dt><code>macdef </code><i>macro-name</i></p>
<dd> Define a macro. Subsequent lines are stored as the macro <i>macro-name </i> a null line (consecutive newline characters in a file or carriage returns from the terminal) terminates macro input mode. There is a limit of 16 macros and 4096 total characters in all defined macros. Macros remain defined until a <code>close</code> command is executed. The macro processor interprets `$&#8217; and `\&#8217; as special characters. A `$&#8217; followed by a number (or numbers) is replaced by the corresponding argument on the macro invocation command line. A `$&#8217; followed by an `i&#8217; signals that macro processor that the executing macro is to be looped. On the first pass `$i&#8217; is replaced by the first argument on the macro invocation command line, on the second pass it is replaced by the second argument, and so on. A `\&#8217; followed by any character is replaced by that character. Use the `\&#8217; to prevent special treatment of the `$&#8217;.</p>
<dt><code>mdelete </code>[<i>remote-files</i> ]</p>
<dd> Delete the <i>remote-files</i> on the remote machine.</p>
<dt><code>mdir </code><i>remote-files local-file</i></p>
<dd> Like <code>dir </code> except multiple remote files may be specified. If interactive prompting is on, <code>ftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>mdir</code> output.</p>
<dt><code>mget </code><i>remote-files</i></p>
<dd> Expand the <i>remote-files</i> on the remote machine and do a <code>get</code> for each file name thus produced. See <code>glob</code> for details on the filename expansion. Resulting file names will then be processed according to <code>case </code> <code>ntrans</code> and <code>nmap</code> settings. Files are transferred into the local working directory, which can be changed with `lcd&#8217; directory ; new local directories can be created with `!&#8217; mkdir directory .</p>
<dt><code>mkdir </code><i>directory-name</i></p>
<dd> Make a directory on the remote machine.</p>
<dt><code>mls </code><i>remote-files local-file</i></p>
<dd> Like <code>nlist </code> except multiple remote files may be specified, and the <i>local-file</i> must be specified. If interactive prompting is on, <code>ftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>mls</code> output.</p>
<dt><code>mode </code>[<i>mode-name</i> ]</p>
<dd> Set the file transfer <code>mode</code> to <i>mode-name </i> The default mode is &ldquo;stream&rdquo; mode.</p>
<dt><code>modtime </code><i>file-name</i></p>
<dd> Show the last modification time of the file on the remote machine.</p>
<dt><code>mput </code><i>local-files</i></p>
<dd> Expand wild cards in the list of local files given as arguments and do a <code>put</code> for each file in the resulting list. See <code>glob</code> for details of filename expansion. Resulting file names will then be processed according to <code>ntrans</code> and <code>nmap</code> settings.</p>
<dt><code>newer </code><i>file-name </i>[<i>local-file</i> ]</p>
<dd> Get the file only if the modification time of the remote file is more recent that the file on the current system. If the file does not exist on the current system, the remote file is considered <code>newer </code> Otherwise, this command is identical to <i>get </i></p>
<dt> <code>nlist</code> [<i>remote-directory</i> ] [<i>local-file</i> ]</p>
<dd>
<dd>Print a list of the files in a directory on the remote machine. If <i>remote-directory</i> is left unspecified, the current working directory is used. If interactive prompting is on, <code>ftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>nlist</code> output. If no local file is specified, or if <i>local-file</i> is &#8211;<code>,</code> the output is sent to the terminal.</p>
<dt><code>nmap </code>[<i>inpattern outpattern</i> ]</p>
<dd> Set or unset the filename mapping mechanism. If no arguments are specified, the filename mapping mechanism is unset. If arguments are specified, remote filenames are mapped during <code>mput</code> commands and <code>put</code> commands issued without a specified remote target filename. If arguments are specified, local filenames are mapped during <code>mget</code> commands and <code>get</code> commands issued without a specified local target filename. This command is useful when connecting to a <code>non- UNIX </code> remote computer with different file naming conventions or practices. The mapping follows the pattern set by <i>inpattern</i> and <i>outpattern </i> [<i>Inpattern</i> ] is a template for incoming filenames (which may have already been processed according to the <code>ntrans</code> and <code>case</code> settings). Variable templating is accomplished by including the sequences `$1&#8242;, `$2&#8242;, &#8230;, `$9&#8242; in <i>inpattern </i> Use `\&#8217; to prevent this special treatment of the `$&#8217; character. All other characters are treated literally, and are used to determine the <code>nmap</code> [<i>inpattern</i> ] variable values. For example, given <i>inpattern</i> $1.$2 and the remote file name &quot;mydata.data&quot;, $1 would have the value &quot;mydata&quot;, and $2 would have the value &quot;data&quot;. The <i>outpattern</i> determines the resulting mapped filename. The sequences `$1&#8242;, `$2&#8242;, &#8230;., `$9&#8242; are replaced by any value resulting from the <i>inpattern</i> template. The sequence `$0&#8242; is replace by the original filename. Additionally, the sequence `[<i>seq1</i> ] &#8216; , Ar seq2 is replaced by [<i>seq1</i> ] if <i>seq1</i> is not a null string; otherwise it is replaced by <i>seq2</i> For example, the command </p>
<blockquote>
<pre><code>
nmap $1.$2.$3[$1, $2].[$2, file]
</code></pre>
</blockquote>
<p> would yield the output filename &quot;myfile.data&quot; for input filenames &quot;myfile.data&quot; and &quot;myfile.data.old&quot;, &quot;myfile.file&quot; for the input filename &quot;myfile&quot;, and &quot;myfile.myfile&quot; for the input filename &quot;.myfile&quot;. Spaces may be included in <i>outpattern </i> as in the example: `nmap $1 sed &quot;s/ *$//&quot; &gt; $1&#8242; . Use the `\&#8217; character to prevent special treatment of the `$&#8217;,'[&#8216;,'[&#8216;, and `,&#8217; characters.</p>
<dt><code>ntrans </code>[<i>inchars </i>[<i>outchars</i> ] ]</p>
<dd> Set or unset the filename character translation mechanism. If no arguments are specified, the filename character translation mechanism is unset. If arguments are specified, characters in remote filenames are translated during <code>mput</code> commands and <code>put</code> commands issued without a specified remote target filename. If arguments are specified, characters in local filenames are translated during <code>mget</code> commands and <code>get</code> commands issued without a specified local target filename. This command is useful when connecting to a <code>non- UNIX </code> remote computer with different file naming conventions or practices. Characters in a filename matching a character in <i>inchars</i> are replaced with the corresponding character in <i>outchars </i> If the character&#8217;s position in <i>inchars</i> is longer than the length of <i>outchars </i> the character is deleted from the file name.</p>
<dt><code>open </code><i>host </i>[<i>port</i> ]</p>
<dd> Establish a connection to the specified <i>host</i> <code>FTP</code> server. An optional port number may be supplied, in which case, <code>ftp</code> will attempt to contact an <code>FTP</code> server at that port. If the <code>auto-login</code> option is on (default), <code>ftp</code> will also attempt to automatically log the user in to the <code>FTP</code> server (see below).</p>
<dt><code>prompt</code></p>
<dd> Toggle interactive prompting. Interactive prompting occurs during multiple file transfers to allow the user to selectively retrieve or store files. If prompting is turned off (default is on), any <code>mget</code> or <code>mput</code> will transfer all files, and any <code>mdelete</code> will delete all files.</p>
<dt><code>proxy </code><i>ftp-command</i></p>
<dd> Execute an ftp command on a secondary control connection. This command allows simultaneous connection to two remote ftp servers for transferring files between the two servers. The first <code>proxy</code> command should be an <code>open </code> to establish the secondary control connection. Enter the command &quot;proxy ?&quot; to see other ftp commands executable on the secondary connection. The following commands behave differently when prefaced by <code>proxy </code> <code>open</code> will not define new macros during the auto-login process, <code>close</code> will not erase existing macro definitions, <code>get</code> and <code>mget</code> transfer files from the host on the primary control connection to the host on the secondary control connection, and <code>put </code> <code>mput</code> and <code>append</code> transfer files from the host on the secondary control connection to the host on the primary control connection. Third party file transfers depend upon support of the ftp protocol <code>PASV</code> command by the server on the secondary control connection.</p>
<dt><code>put </code><i>local-file </i>[<i>remote-file</i> ]</p>
<dd> Store a local file on the remote machine. If <i>remote-file</i> is left unspecified, the local file name is used after processing according to any <code>ntrans</code> or <code>nmap</code> settings in naming the remote file. File transfer uses the current settings for <code>type </code> <code>format</code> <code>mode </code> and <code>structure </code></p>
<dt><code>pwd</code></p>
<dd> Print the name of the current working directory on the remote machine.</p>
<dt><code>quit</code></p>
<dd> A synonym for <code>bye </code></p>
<dt><code>quote </code><i>arg1 arg2 &#8230;</i></p>
<dd> The arguments specified are sent, verbatim, to the remote <code>FTP</code> server.</p>
<dt><code>recv </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> A synonym for get.</p>
<dt><code>reget </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> Reget acts like get, except that if <i>local-file</i> exists and is smaller than <i>remote-file </i> <i>local-file</i> is presumed to be a partially transferred copy of <i>remote-file</i> and the transfer is continued from the apparent point of failure. If <i>local-file</i> does not exist ftp won&#8217;t fetch the file. This command is useful when transferring very large files over networks that are prone to dropping connections.</p>
<dt><code>remotehelp </code>[<i>command-name</i> ]</p>
<dd> Request help from the remote <code>FTP</code> server. If a <i>command-name</i> is specified it is supplied to the server as well.</p>
<dt><code>remotestatus </code>[<i>file-name</i> ]</p>
<dd> With no arguments, show status of remote machine. If <i>file-name</i> is specified, show status of <i>file-name</i> on remote machine.</p>
<dt> <code>rename</code> [<i>from</i> ] [<i>to</i> ]</p>
<dd>
<dd>Rename the file <i>from</i> on the remote machine, to the file <i>to </i></p>
<dt><code>reset</code></p>
<dd> Clear reply queue. This command re-synchronizes command/reply sequencing with the remote ftp server. Resynchronization may be necessary following a violation of the ftp protocol by the remote server.</p>
<dt><code>restart </code><i>marker</i></p>
<dd> Restart the immediately following <code>get</code> or <code>put</code> at the indicated <i>marker </i> On UNIX systems, marker is usually a byte offset into the file.</p>
<dt><code>rmdir </code><i>directory-name</i></p>
<dd> Delete a directory on the remote machine.</p>
<dt><code>runique</code></p>
<dd> Toggle storing of files on the local system with unique filenames. If a file already exists with a name equal to the target local filename for a <code>get</code> or <code>mget</code> command, a &quot;.1&quot; is appended to the name. If the resulting name matches another existing file, a &quot;.2&quot; is appended to the original name. If this process continues up to &quot;.99&quot;, an error message is printed, and the transfer does not take place. The generated unique filename will be reported. Note that <code>runique</code> will not affect local files generated from a shell command (see below). The default value is off.</p>
<dt><code>send </code><i>local-file </i>[<i>remote-file</i> ]</p>
<dd> A synonym for put.</p>
<dt><code>sendport</code></p>
<dd> Toggle the use of <code>PORT</code> commands. By default, <code>ftp</code> will attempt to use a <code>PORT</code> command when establishing a connection for each data transfer. The use of <code>PORT</code> commands can prevent delays when performing multiple file transfers. If the <code>PORT</code> command fails, <code>ftp</code> will use the default data port. When the use of <code>PORT</code> commands is disabled, no attempt will be made to use <code>PORT</code> commands for each data transfer. This is useful for certain <code>FTP</code> implementations which do ignore <code>PORT</code> commands but, incorrectly, indicate they&#8217;ve been accepted.</p>
<dt><code>site </code><i>arg1 arg2 &#8230;</i></p>
<dd> The arguments specified are sent, verbatim, to the remote <code>FTP</code> server as a <code>SITE</code> command.</p>
<dt><code>size </code><i>file-name</i></p>
<dd> Return size of <i>file-name</i> on remote machine.</p>
<dt><code>status</code></p>
<dd> Show the current status of <code>ftp </code></p>
<dt><code>struct </code>[<i>struct-name</i> ]</p>
<dd> Set the file transfer <i>structure</i> to <i>struct-name</i> By default &ldquo;stream&rdquo; structure is used.</p>
<dt><code>sunique</code></p>
<dd> Toggle storing of files on remote machine under unique file names. Remote ftp server must support ftp protocol <code>STOU</code> command for successful completion. The remote server will report unique name. Default value is off.</p>
<dt><code>system</code></p>
<dd> Show the type of operating system running on the remote machine.</p>
<dt><code>tenex</code></p>
<dd> Set the file transfer type to that needed to talk to <code>TENEX</code> machines.</p>
<dt><code>trace</code></p>
<dd> Toggle packet tracing.</p>
<dt><code>type </code>[<i>type-name</i> ]</p>
<dd> Set the file transfer <code>type</code> to <i>type-name </i> If no type is specified, the current type is printed. The default type is network <code>ASCII</code></p>
<dt><code>umask </code>[<i>newmask</i> ]</p>
<dd> Set the default umask on the remote server to <i>newmask </i> If <i>newmask</i> is omitted, the current umask is printed.</p>
<dt> <code>user </code><i>user-name</i> [<i>password</i> ] [<i>account</i> ]</p>
<dd>
<dd>Identify yourself to the remote <code>FTP</code> server. If the <i>password</i> is not specified and the server requires it, <code>ftp</code> will prompt the user for it (after disabling local echo). If an <i>account</i> field is not specified, and the <code>FTP</code> server requires it, the user will be prompted for it. If an <i>account</i> field is specified, an account command will be relayed to the remote server after the login sequence is completed if the remote server did not require it for logging in. Unless <code>ftp</code> is invoked with &ldquo;auto-login&rdquo; disabled, this process is done automatically on initial connection to the <code>FTP</code> server.</p>
<dt><code>verbose</code></p>
<dd> Toggle verbose mode. In verbose mode, all responses from the <code>FTP</code> server are displayed to the user. In addition, if verbose is on, when a file transfer completes, statistics regarding the efficiency of the transfer are reported. By default, verbose is on.</p>
<dt><code>? </code>[<i>command</i> ]</p>
<dd> A synonym for help.</dl>
<p> Command arguments which have embedded spaces may be quoted with quote `&quot;&#8217; marks.</p>
<h2>ABORTING A FILE TRANSFER</h2>
<p> To abort a file transfer, use the terminal interrupt key (usually Ctrl-C). Sending transfers will be immediately halted. Receiving transfers will be halted by sending a ftp protocol <code>ABOR</code> command to the remote server, and discarding any further data received. The speed at which this is accomplished depends upon the remote server&#8217;s support for <code>ABOR</code> processing. If the remote server does not support the <code>ABOR</code> command, an `ftp&gt;&#8217; prompt will not appear until the remote server has completed sending the requested file. </p>
<p> The terminal interrupt key sequence will be ignored when <code>ftp</code> has completed any local processing and is awaiting a reply from the remote server. A long delay in this mode may result from the ABOR processing described above, or from unexpected behavior by the remote server, including violations of the ftp protocol. If the delay results from unexpected remote server behavior, the local <code>ftp</code> program must be killed by hand.</p>
<h2>FILE NAMING CONVENTIONS</h2>
<p> Files specified as arguments to <code>ftp</code> commands are processed according to the following rules. </p>
<ol>
<li> If the file name `- &#8216; is specified, the <i>stdin</i> (for reading) or <i>stdout</i> (for writing) is used.
<li> If the first character of the file name is `|&#8217; the remainder of the argument is interpreted as a shell command. <code>Ftp</code> then forks a shell, using <a href="/docs/linux/man/3-popen/">popen</a>(3) with the argument supplied, and reads (writes) from the stdout (stdin). If the shell command includes spaces, the argument must be quoted; e.g. &ldquo;&quot; ls -lt&quot;&rdquo;. A particularly useful example of this mechanism is: &ldquo;dir more&rdquo;.
<li> Failing the above checks, if &#8220;globbing&#8221; is enabled, local file names are expanded according to the rules used in the <a href="/docs/linux/man/1-csh/">csh</a>(1); c.f. the <code>glob</code> command. If the <code>ftp</code> command expects a single local file (.e.g. <code>put )</code> only the first filename generated by the &quot;globbing&quot; operation is used.
<li> For <code>mget</code> commands and <code>get</code> commands with unspecified local file names, the local filename is the remote filename, which may be altered by a <code>case </code> <code>ntrans</code> or <code>nmap</code> setting. The resulting filename may then be altered if <code>runique</code> is on.
<li> For <code>mput</code> commands and <code>put</code> commands with unspecified remote file names, the remote filename is the local filename, which may be altered by a <code>ntrans</code> or <code>nmap</code> setting. The resulting filename may then be altered by the remote server if <code>sunique</code> is on. </ol>
<h2>FILE TRANSFER PARAMETERS</h2>
<p> The FTP specification specifies many parameters which may affect a file transfer. The <code>type</code> may be one of &ldquo;ascii&rdquo;, &ldquo;image&rdquo; (binary), &ldquo;ebcdic&rdquo;, and &ldquo;local byte size&rdquo; (for <code>PDP -10&#8217;s</code> and <code>PDP -20&#8217;s</code> mostly). <code>Ftp</code> supports the ascii and image types of file transfer, plus local byte size 8 for <code>tenex</code> mode transfers. </p>
<p> <code>Ftp</code> supports only the default values for the remaining file transfer parameters: <code>mode </code> <code>form</code> and <code>struct </code></p>
<h2>ENVIRONMENT</h2>
<p> <code>Ftp</code> utilizes the following environment variables.</p>
<dl>
<dt><code>HOME</code></p>
<dd> For default location of a .netrc file, if one exists.</p>
<dt><code>SHELL</code></p>
<dd> For default shell.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ftpd/">ftpd</a>(8), <a href="/docs/linux/man/5-netrc/">netrc</a>(5), RFC 959</p>
<h2>HISTORY</h2>
<p> The <code>ftp</code> command appeared in BSD 4.2</p>
<h2>BUGS</h2>
<p> Correct execution of many commands depends upon proper behavior by the remote server. </p>
<p> An error in the treatment of carriage returns in the BSD 4.2 ascii-mode transfer code has been corrected. This correction may result in incorrect transfers of binary files to and from BSD 4.2 servers using the ascii type. Avoid this problem by using the binary image type. </p>
<h2>Index</h2>
