---
title: "ftp(1)"
name: "ftp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftp/"
description: "tnftp – Internet file transfer program"
---

<h2 class="name">NAME</h2>
<p> <code>tnftp</code> &#8211; Internet file transfer program </p>
<h2>SYNOPSIS</h2>
<p> <code>tnftp</code> [-<code>46AadefginpRtVv?</code> ] [-<code>N </code><i>netrc</i> ] [-<code>o </code><i>output</i> ] [-<code>P </code><i>port</i> ] [-<code>q </code><i>quittime</i> ] [-<code>r </code><i>retry</i> ] [-<code>s </code><i>srcaddr</i> ] [-<code>T </code> <i>dir</i> <i>max</i> [, <i>inc</i> ] ] [-<code>x </code><i>xfersize</i> ] [[<i>user </i><code>@ </code><i>host </i>[<i>port </i>] ] ] [[<i>user </i><code>@</code> ] <i>host </i><code>:</code> [<i>path</i> ] [<code>/</code> ] ] [<code>file:/// </code><i>path</i> ] [<code>ftp://</code> [<i>user</i> [<code>: </code><i>password</i> ] <code>@ </code>] <i>host </i>[<code>: </code><i>port </i>] <code>/ </code><i>path</i> [<code>/</code> ] [<code>;type= </code><i>type</i> ] ] [<code>http://</code> [<i>user</i> [<code>: </code><i>password</i> ] <code>@ </code>] <i>host </i>[<code>: </code><i>port </i>] <code>/ </code><i>path</i> ] [<code>https://</code> [<i>user</i> [<code>: </code><i>password</i> ] <code>@ </code>] <i>host </i>[<code>: </code><i>port </i>] <code>/ </code><i>path</i> ] <i>&#8230;</i><br />
<code>tnftp</code> &#8211;<code>u </code><i>url file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tnftp</code> is the user interface to the Internet standard File Transfer Protocol. The program allows a user to transfer files to and from a remote network site. </p>
<p> The last five arguments will fetch a file using the <code>FTP</code> or <code>HTTP</code> protocols, or by direct copying, into the current directory. This is ideal for scripts. Refer to Sx AUTO-FETCHING FILES below for more information. </p>
<p> Options may be specified at the command line, or to the command interpreter.</p>
<dl>
<dt><code>-4</code></p>
<dd> Forces <code>tnftp</code> to only use IPv4 addresses.</p>
<dt><code>-6</code></p>
<dd> Forces <code>tnftp</code> to only use IPv6 addresses.</p>
<dt><code>-A</code></p>
<dd> Force active mode <code>FTP</code> By default, <code>tnftp</code> will try to use passive mode <code>FTP</code> and fall back to active mode if passive is not supported by the server. This option causes <code>tnftp</code> to always use an active connection. It is only useful for connecting to very old servers that do not implement passive mode properly.</p>
<dt><code>-a</code></p>
<dd> Causes <code>tnftp</code> to bypass normal login procedure, and use an anonymous login instead.</p>
<dt><code>-d</code></p>
<dd> Enables debugging.</p>
<dt><code>-e</code></p>
<dd> Disables command line editing. This is useful for Emacs ange-ftp mode.</p>
<dt><code>-f</code></p>
<dd> Forces a cache reload for transfers that go through the <code>FTP</code> or <code>HTTP</code> proxies.</p>
<dt><code>-g</code></p>
<dd> Disables file name globbing.</p>
<dt><code>-i</code></p>
<dd> Turns off interactive prompting during multiple file transfers.</p>
<dt><code>-N </code><i>netrc</i></p>
<dd> Use <i>netrc</i> instead of ~/.netrc Refer to Sx THE .netrc FILE for more information.</p>
<dt><code>-n</code></p>
<dd> Restrains <code>tnftp</code> from attempting &#8220;auto-login&#8221; upon initial connection for non auto-fetch transfers. If auto-login is enabled, <code>tnftp</code> will check the .netrc (see below) file in the user&#8217;s home directory for an entry describing an account on the remote machine. If no entry exists, <code>tnftp</code> will prompt for the remote machine login name (default is the user identity on the local machine), and, if necessary, prompt for a password and an account with which to login. To override the auto-login for auto-fetch transfers, specify the username (and optionally, password) as appropriate.</p>
<dt><code>-o </code><i>output</i></p>
<dd> When auto-fetching files, save the contents in <i>output</i> <i>output</i> is parsed according to the Sx FILE NAMING CONVENTIONS below. If <i>output</i> is not `-&#8216; or doesn&#8217;t start with `|&#8217; then only the first file specified will be retrieved into <i>output</i> all other files will be retrieved into the basename of their remote name.</p>
<dt><code>-P </code><i>port</i></p>
<dd> Sets the port number to <i>port</i></p>
<dt><code>-p</code></p>
<dd> Enable passive mode operation for use behind connection filtering firewalls. This option has been deprecated as <code>tnftp</code> now tries to use passive mode by default, falling back to active mode if the server does not support passive connections.</p>
<dt><code>-q </code><i>quittime</i></p>
<dd> Quit if the connection has stalled for <i>quittime</i> seconds.</p>
<dt><code>-R</code></p>
<dd> Restart all non-proxied auto-fetches.</p>
<dt><code>-r </code><i>wait</i></p>
<dd> Retry the connection attempt if it failed, pausing for <i>wait</i> seconds.</p>
<dt><code>-s </code><i>srcaddr</i></p>
<dd> Uses <i>srcaddr</i> as the local IP address for all connections.</p>
<dt><code>-t</code></p>
<dd> Enables packet tracing.</p>
<dt><code>-T </code><i>direction </i><code>, </code><i>maximum </i>[, <i>increment </i>]</p>
<dd> Set the maximum transfer rate for <i>direction</i> to <i>maximum</i> bytes/second, and if specified, the increment to <i>increment</i> bytes/second. Refer to <code>rate</code> for more information.</p>
<dt><code>-u </code><i>url file &#8230;</i></p>
<dd> Upload files on the command line to <i>url</i> where <i>url</i> is one of the `<code>ftp://</code> &#8216; URL types as supported by auto-fetch (with an optional target filename for single file uploads), and <i>file</i> is one or more local files to be uploaded.</p>
<dt><code>-V</code></p>
<dd> Disable <code>verbose</code> and <code>progress</code> overriding the default of enabled when output is to a terminal.</p>
<dt><code>-v</code></p>
<dd> Enable <code>verbose</code> and <code>progress</code> This is the default if output is to a terminal (and in the case of <code>progress</code> <code>tnftp</code> is the foreground process). Forces <code>tnftp</code> to show all responses from the remote server, as well as report on data transfer statistics.</p>
<dt><code>-x </code><i>xfersize</i></p>
<dd> Set the size of the socket send and receive buffers to <i>xfersize</i> Refer to <code>xferbuf</code> for more information.</p>
<dt><code>&#8211; </code></p>
<dd> Display help to stdout, and exit.</dl>
<p> The client host with which <code>tnftp</code> is to communicate may be specified on the command line. If this is done, <code>tnftp</code> will immediately attempt to establish a connection to an <code>FTP</code> server on that host; otherwise, <code>tnftp</code> will enter its command interpreter and await instructions from the user. When <code>tnftp</code> is awaiting commands from the user the prompt `ftp&gt;&#8217; is provided to the user. The following commands are recognized by <code>tnftp</code></p>
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
<dd> Terminate the <code>FTP</code> session with the remote server and exit <code>tnftp</code> An end of file will also terminate the session and exit.</p>
<dt><code>case</code></p>
<dd> Toggle remote computer file name case mapping during <code>get</code> <code>mget</code> and <code>mput</code> commands. When <code>case</code> is on (default is off), remote computer file names with all letters in upper case are written in the local directory with the letters mapped to lower case.</p>
<dt><code>cd </code><i>remote-directory</i></p>
<dd> Change the working directory on the remote machine to <i>remote-directory</i></p>
<dt><code>cdup</code></p>
<dd> Change the remote machine working directory to the parent of the current remote machine working directory.</p>
<dt><code>chmod </code><i>mode remote-file</i></p>
<dd> Change the permission modes of the file <i>remote-file</i> on the remote system to <i>mode</i></p>
<dt><code>close</code></p>
<dd> Terminate the <code>FTP</code> session with the remote server, and return to the command interpreter. Any defined macros are erased.</p>
<dt><code>cr</code></p>
<dd> Toggle carriage return stripping during ascii type file retrieval. Records are denoted by a carriage return/linefeed sequence during ascii type file transfer. When <code>cr</code> is on (the default), carriage returns are stripped from this sequence to conform with the UNIX single linefeed record delimiter. Records on non- <code>UNIX </code> remote systems may contain single linefeeds; when an ascii type transfer is made, these linefeeds may be distinguished from a record delimiter only when <code>cr</code> is off.</p>
<dt><code>debug </code>[<i>debug-value</i> ]</p>
<dd> Toggle debugging mode. If an optional <i>debug-value</i> is specified it is used to set the debugging level. When debugging is on, <code>tnftp</code> prints each command sent to the remote machine, preceded by the string `&#8211;&gt;&#8217;</p>
<dt><code>delete </code><i>remote-file</i></p>
<dd> Delete the file <i>remote-file</i> on the remote machine.</p>
<dt><code>dir </code>[<i>remote-path </i>[<i>local-file</i> ] ]</p>
<dd> Print a listing of the contents of a directory on the remote machine. The listing includes any system-dependent information that the server chooses to include; for example, most UNIX systems will produce output from the command `ls&#8217; -l . If <i>remote-path</i> is left unspecified, the current working directory is used. If interactive prompting is on, <code>tnftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>dir</code> output. If no local file is specified, or if <i>local-file</i> is `- &#8216; the output is sent to the terminal.</p>
<dt><code>disconnect</code></p>
<dd> A synonym for <code>close</code></p>
<dt><code>edit</code></p>
<dd> Toggle command line editing, and context sensitive command and file completion. This is automatically enabled if input is from a terminal, and disabled otherwise.</p>
<dt><code>epsv , epsv4 , epsv6</code></p>
<dd> Toggle the use of the extended <code>EPSV</code> and <code>EPRT</code> commands on all IP, IPv4, and IPv6 connections respectively. First try <code>EPSV / EPRT</code> and then <code>PASV / PORT</code> This is enabled by default. If an extended command fails then this option will be temporarily disabled for the duration of the current connection, or until <code>epsv</code> <code>epsv4</code> or <code>epsv6</code> is executed again.</p>
<dt><code>exit</code></p>
<dd> A synonym for <code>bye</code></p>
<dt><code>features</code></p>
<dd> Display what features the remote server supports (using the <code>FEAT</code> command).</p>
<dt><code>fget </code><i>localfile</i></p>
<dd> Retrieve the files listed in <i>localfile</i> which has one line per filename.</p>
<dt><code>form </code><i>format</i></p>
<dd> Set the file transfer <code>form</code> to <i>format</i> The default (and only supported) format is &#8220;non-print&#8221;</p>
<dt><code>ftp </code><i>host </i>[<i>port</i> ]</p>
<dd> A synonym for <code>open</code></p>
<dt><code>gate </code>[<i>host </i>[<i>port</i> ] ]</p>
<dd> Toggle gate-ftp mode, which used to connect through the TIS FWTK and Gauntlet <code>FTP</code> proxies. This will not be permitted if the gate-ftp server hasn&#8217;t been set (either explicitly by the user, or from the <code>FTPSERVER</code> environment variable). If <i>host</i> is given, then gate-ftp mode will be enabled, and the gate-ftp server will be set to <i>host</i> If <i>port</i> is also given, that will be used as the port to connect to on the gate-ftp server.</p>
<dt><code>get </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> Retrieve the <i>remote-file</i> and store it on the local machine. If the local file name is not specified, it is given the same name it has on the remote machine, subject to alteration by the current <code>case </code> <code>ntrans</code> and <code>nmap</code> settings. The current settings for <code>type </code> <code>form</code> <code>mode </code> and <code>structure</code> are used while transferring the file.</p>
<dt><code>glob</code></p>
<dd> Toggle filename expansion for <code>mdelete </code> <code>mget</code> <code>mput</code> and <code>mreget</code> If globbing is turned off with <code>glob </code> the file name arguments are taken literally and not expanded. Globbing for <code>mput</code> is done as in <a href="/docs/linux/man/1-csh/">csh</a>(1). For <code>mdelete</code> <code>mget</code> and <code>mreget</code> each remote file name is expanded separately on the remote machine and the lists are not merged. Expansion of a directory name is likely to be different from expansion of the name of an ordinary file: the exact result depends on the foreign operating system and <code>FTP</code> server, and can be previewed by doing `<code>mls remote-files &#8211;</code> &#8216; Note: <code>mget</code> <code>mput</code> and <code>mreget</code> are not meant to transfer entire directory subtrees of files. That can be done by transferring a <a href="/docs/linux/man/1-tar/">tar</a>(1) archive of the subtree (in binary mode).</p>
<dt><code>hash </code>[<i>size</i> ]</p>
<dd> Toggle hash-sign (`#&#8217; ) printing for each data block transferred. The size of a data block defaults to 1024 bytes. This can be changed by specifying <i>size</i> in bytes. Enabling <code>hash</code> disables <code>progress</code></p>
<dt><code>help </code>[<i>command</i> ]</p>
<dd> Print an informative message about the meaning of <i>command</i> If no argument is given, <code>tnftp</code> prints a list of the known commands.</p>
<dt><code>idle </code>[<i>seconds</i> ]</p>
<dd> Set the inactivity timer on the remote server to <i>seconds</i> seconds. If <i>seconds</i> is omitted, the current inactivity timer is printed.</p>
<dt><code>image</code></p>
<dd> A synonym for <code>binary</code></p>
<dt><code>lcd </code>[<i>directory</i> ]</p>
<dd> Change the working directory on the local machine. If no <i>directory</i> is specified, the user&#8217;s home directory is used.</p>
<dt><code>less </code><i>file</i></p>
<dd> A synonym for <code>page</code></p>
<dt><code>lpage </code><i>local-file</i></p>
<dd> Display <i>local-file</i> with the program specified by the <code>set pager</code> option.</p>
<dt><code>lpwd</code></p>
<dd> Print the working directory on the local machine.</p>
<dt><code>ls </code>[<i>remote-path </i>[<i>local-file</i> ] ]</p>
<dd> A synonym for <code>dir</code></p>
<dt><code>macdef </code><i>macro-name</i></p>
<dd> Define a macro. Subsequent lines are stored as the macro <i>macro-name </i> a null line (consecutive newline characters in a file or carriage returns from the terminal) terminates macro input mode. There is a limit of 16 macros and 4096 total characters in all defined macros. Macro names can be a maximum of 8 characters. Macros are only applicable to the current session they are defined within (or if defined outside a session, to the session invoked with the next <code>open</code> command), and remain defined until a <code>close</code> command is executed. To invoke a macro, use the <code>$</code> command (see above). </p>
<p> The macro processor interprets `$&#8217; and `\&#8217; as special characters. A `$&#8217; followed by a number (or numbers) is replaced by the corresponding argument on the macro invocation command line. A `$&#8217; followed by an `i&#8217; signals the macro processor that the executing macro is to be looped. On the first pass `$i&#8217; is replaced by the first argument on the macro invocation command line, on the second pass it is replaced by the second argument, and so on. A `\&#8217; followed by any character is replaced by that character. Use the `\&#8217; to prevent special treatment of the `$&#8217;</p>
<dt><code>mdelete </code>[<i>remote-files</i> ]</p>
<dd> Delete the <i>remote-files</i> on the remote machine.</p>
<dt><code>mdir </code><i>remote-files local-file</i></p>
<dd> Like <code>dir </code> except multiple remote files may be specified. If interactive prompting is on, <code>tnftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>mdir</code> output.</p>
<dt><code>mget </code><i>remote-files</i></p>
<dd> Expand the <i>remote-files</i> on the remote machine and do a <code>get</code> for each file name thus produced. See <code>glob</code> for details on the filename expansion. Resulting file names will then be processed according to <code>case </code> <code>ntrans</code> and <code>nmap</code> settings. Files are transferred into the local working directory, which can be changed with `lcd&#8217; directory ; new local directories can be created with `<code>! mkdir directory</code> &#8216;</p>
<dt><code>mkdir </code><i>directory-name</i></p>
<dd> Make a directory on the remote machine.</p>
<dt><code>mls </code><i>remote-files local-file</i></p>
<dd> Like <code>ls </code> except multiple remote files may be specified, and the <i>local-file</i> must be specified. If interactive prompting is on, <code>tnftp</code> will prompt the user to verify that the last argument is indeed the target local file for receiving <code>mls</code> output.</p>
<dt><code>mlsd </code>[<i>remote-path</i> ]</p>
<dd> Display the contents of <i>remote-path</i> (which should default to the current directory if not given) in a machine-parsable form, using <code>MLSD</code> The format of display can be changed with `<code>remopts mlst &#8230;</code> &#8216;</p>
<dt><code>mlst </code>[<i>remote-path</i> ]</p>
<dd> Display the details about <i>remote-path</i> (which should default to the current directory if not given) in a machine-parsable form, using <code>MLST</code> The format of display can be changed with `<code>remopts mlst &#8230;</code> &#8216;</p>
<dt><code>mode </code><i>mode-name</i></p>
<dd> Set the file transfer <code>mode</code> to <i>mode-name</i> The default (and only supported) mode is &#8220;stream&#8221;</p>
<dt><code>modtime </code><i>remote-file</i></p>
<dd> Show the last modification time of the file on the remote machine, in <code>RFC 2822</code> format.</p>
<dt><code>more </code><i>file</i></p>
<dd> A synonym for <code>page</code></p>
<dt><code>mput </code><i>local-files</i></p>
<dd> Expand wild cards in the list of local files given as arguments and do a <code>put</code> for each file in the resulting list. See <code>glob</code> for details of filename expansion. Resulting file names will then be processed according to <code>ntrans</code> and <code>nmap</code> settings.</p>
<dt><code>mreget </code><i>remote-files</i></p>
<dd> As per <code>mget</code> but performs a <code>reget</code> instead of <code>get</code></p>
<dt><code>msend </code><i>local-files</i></p>
<dd> A synonym for <code>mput</code></p>
<dt><code>newer </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> Get the file only if the modification time of the remote file is more recent that the file on the current system. If the file does not exist on the current system, the remote file is considered <code>newer</code> Otherwise, this command is identical to <code>get</code></p>
<dt><code>nlist </code>[<i>remote-path </i>[<i>local-file</i> ] ]</p>
<dd> A synonym for <code>ls</code></p>
<dt><code>nmap </code>[<i>inpattern outpattern</i> ]</p>
<dd> Set or unset the filename mapping mechanism. If no arguments are specified, the filename mapping mechanism is unset. If arguments are specified, remote filenames are mapped during <code>mput</code> commands and <code>put</code> commands issued without a specified remote target filename. If arguments are specified, local filenames are mapped during <code>mget</code> commands and <code>get</code> commands issued without a specified local target filename. This command is useful when connecting to a <code>non- UNIX </code> remote computer with different file naming conventions or practices. The mapping follows the pattern set by <i>inpattern</i> and <i>outpattern</i> </p>
<p> <i>inpattern</i> is a template for incoming filenames (which may have already been processed according to the <code>ntrans</code> and <code>case</code> settings). Variable templating is accomplished by including the sequences `$1&#8242; , `$2&#8242; , &#8230;, `$9&#8242; in <i>inpattern</i> Use `\&#8217; to prevent this special treatment of the `$&#8217; character. All other characters are treated literally, and are used to determine the <code>nmap</code> [<i>inpattern</i> ] variable values. For example, given <i>inpattern</i> `<code>$1.$2</code> &#8216; and the remote file name `<code>mydata.data</code> &#8216; `$1&#8217; would have the value `<code>mydata</code> &#8216; and `$2&#8217; would have the value `<code>data</code> &#8216; </p>
<p> The <i>outpattern</i> determines the resulting mapped filename. The sequences `$1&#8242; , `$2&#8242; , &#8230;, `$9&#8242; are replaced by any value resulting from the <i>inpattern</i> template. The sequence `$0&#8242; is replaced by the original filename. Additionally, the sequence &#8220;[<i>seq1 , seq2</i> ] &#8221; is replaced by <i>seq1</i> if <i>seq1</i> is not a null string; otherwise it is replaced by <i>seq2</i> For example, the command </p>
<blockquote><p><tt>nmap $1.$2.$3 [$1,$2].[$2,file]</tt></p></blockquote>
<p> would yield the output filename `<code>myfile.data</code> &#8216; for input filenames `<code>myfile.data</code> &#8216; and `<code>myfile.data.old</code> &#8216; `<code>myfile.file</code> &#8216; for the input filename `<code>myfile</code> &#8216; and `<code>myfile.myfile</code> &#8216; for the input filename `<code>.myfile</code> &#8216; Spaces may be included in <i>outpattern </i> as in the example: </p>
<blockquote><p><tt>nmap $1 sed &quot;s/ *$//&quot; &gt; $1</tt></p></blockquote>
<p> Use the `\&#8217; character to prevent special treatment of the `$&#8217; , `[&#8216; , `]&#8217; , and `,&#8217; characters.</p>
<dt><code>ntrans </code>[<i>inchars </i>[<i>outchars</i> ] ]</p>
<dd> Set or unset the filename character translation mechanism. If no arguments are specified, the filename character translation mechanism is unset. If arguments are specified, characters in remote filenames are translated during <code>mput</code> commands and <code>put</code> commands issued without a specified remote target filename. If arguments are specified, characters in local filenames are translated during <code>mget</code> commands and <code>get</code> commands issued without a specified local target filename. This command is useful when connecting to a <code>non- UNIX </code> remote computer with different file naming conventions or practices. Characters in a filename matching a character in <i>inchars</i> are replaced with the corresponding character in <i>outchars</i> If the character&#8217;s position in <i>inchars</i> is longer than the length of <i>outchars </i> the character is deleted from the file name.</p>
<dt><code>open </code><i>host </i>[<i>port</i> ]</p>
<dd> Establish a connection to the specified <i>host</i> <code>FTP</code> server. An optional port number may be supplied, in which case, <code>tnftp</code> will attempt to contact an <code>FTP</code> server at that port. If the <code>set auto-login</code> option is on (default), <code>tnftp</code> will also attempt to automatically log the user in to the <code>FTP</code> server (see below).</p>
<dt><code>page </code><i>file</i></p>
<dd> Retrieve <code>file</code> and display with the program specified by the <code>set pager</code> option.</p>
<dt><code>passive </code>[<code>auto</code> ]</p>
<dd> Toggle passive mode (if no arguments are given). If <code>auto</code> is given, act as if <code>FTPMODE</code> is set to `auto&#8217; If passive mode is turned on (default), <code>tnftp</code> will send a <code>PASV</code> command for all data connections instead of a <code>PORT</code> command. The <code>PASV</code> command requests that the remote server open a port for the data connection and return the address of that port. The remote server listens on that port and the client connects to it. When using the more traditional <code>PORT</code> command, the client listens on a port and sends that address to the remote server, who connects back to it. Passive mode is useful when using <code>tnftp</code> through a gateway router or host that controls the directionality of traffic. (Note that though <code>FTP</code> servers are required to support the <code>PASV</code> command by <code>RFC 1123</code> some do not.)</p>
<dt><code>pdir </code>[<i>remote-path</i> ]</p>
<dd> Perform <code>dir</code> [<i>remote-path</i> ] and display the result with the program specified by the <code>set pager</code> option.</p>
<dt><code>pls </code>[<i>remote-path</i> ]</p>
<dd> Perform <code>ls</code> [<i>remote-path</i> ] and display the result with the program specified by the <code>set pager</code> option.</p>
<dt><code>pmlsd </code>[<i>remote-path</i> ]</p>
<dd> Perform <code>mlsd</code> [<i>remote-path</i> ] and display the result with the program specified by the <code>set pager</code> option.</p>
<dt><code>preserve</code></p>
<dd> Toggle preservation of modification times on retrieved files.</p>
<dt><code>progress</code></p>
<dd> Toggle display of transfer progress bar. The progress bar will be disabled for a transfer that has <i>local-file</i> as `- &#8216; or a command that starts with `|&#8217; Refer to Sx FILE NAMING CONVENTIONS for more information. Enabling <code>progress</code> disables <code>hash</code></p>
<dt><code>prompt</code></p>
<dd> Toggle interactive prompting. Interactive prompting occurs during multiple file transfers to allow the user to selectively retrieve or store files. If prompting is turned off (default is on), any <code>mget</code> or <code>mput</code> will transfer all files, and any <code>mdelete</code> will delete all files. </p>
<p> When prompting is on, the following commands are available at a prompt:</p>
<dl>
<dt><code>a</code></p>
<dd> Answer `yes&#8217; to the current file, and automatically answer `yes&#8217; to any remaining files for the current command.</p>
<dt><code>n</code></p>
<dd> Answer `no&#8217; and do not transfer the file.</p>
<dt><code>p</code></p>
<dd> Answer `yes&#8217; to the current file, and turn off prompt mode (as is &#8220;prompt off&#8221; had been given).</p>
<dt><code>q</code></p>
<dd> Terminate the current operation.</p>
<dt><code>y</code></p>
<dd> Answer `yes&#8217; and transfer the file.</p>
<dt><code>?</code></p>
<dd> Display a help message.</dl>
<p> Any other response will answer `yes&#8217; to the current file.</p>
<dt><code>proxy </code><i>ftp-command</i></p>
<dd> Execute an <code>FTP</code> command on a secondary control connection. This command allows simultaneous connection to two remote <code>FTP</code> servers for transferring files between the two servers. The first <code>proxy</code> command should be an <code>open </code> to establish the secondary control connection. Enter the command `<code>proxy ?</code> &#8216; to see other <code>FTP</code> commands executable on the secondary connection. The following commands behave differently when prefaced by <code>proxy </code> <code>open</code> will not define new macros during the auto-login process, <code>close</code> will not erase existing macro definitions, <code>get</code> and <code>mget</code> transfer files from the host on the primary control connection to the host on the secondary control connection, and <code>put </code> <code>mput</code> and <code>append</code> transfer files from the host on the secondary control connection to the host on the primary control connection. Third party file transfers depend upon support of the <code>FTP</code> protocol <code>PASV</code> command by the server on the secondary control connection.</p>
<dt><code>put </code><i>local-file </i>[<i>remote-file</i> ]</p>
<dd> Store a local file on the remote machine. If <i>remote-file</i> is left unspecified, the local file name is used after processing according to any <code>ntrans</code> or <code>nmap</code> settings in naming the remote file. File transfer uses the current settings for <code>type </code> <code>format</code> <code>mode </code> and <code>structure</code></p>
<dt><code>pwd</code></p>
<dd> Print the name of the current working directory on the remote machine.</p>
<dt><code>quit</code></p>
<dd> A synonym for <code>bye</code></p>
<dt><code>quote </code>[<i>arg &#8230;</i> ]</p>
<dd> The arguments specified are sent, verbatim, to the remote <code>FTP</code> server.</p>
<dt><code>rate </code><i>direction </i>[<i>maximum </i>[<i>increment </i>] ]</p>
<dd> Throttle the maximum transfer rate to <i>maximum</i> bytes/second. If <i>maximum</i> is 0, disable the throttle. </p>
<p> <i>direction</i> may be one of:</p>
<dl>
<dt><code>all</code></p>
<dd> Both directions.</p>
<dt><code>get</code></p>
<dd> Incoming transfers.</p>
<dt><code>put</code></p>
<dd> Outgoing transfers.</dl>
<p> <i>maximum</i> can be modified on the fly by <i>increment</i> bytes (default: 1024) each time a given signal is received:</p>
<dl>
<dt><code>SIGUSR1</code></p>
<dd> Increment <i>maximum</i> by <i>increment</i> bytes.</p>
<dt><code>SIGUSR2</code></p>
<dd> Decrement <i>maximum</i> by <i>increment</i> bytes. The result must be a positive number.</dl>
<p> If <i>maximum</i> is not supplied, the current throttle rates are displayed. </p>
<p> Note: <code>rate</code> is not yet implemented for ascii mode transfers.</p>
<dt><code>rcvbuf </code><i>size</i></p>
<dd> Set the size of the socket receive buffer to <i>size</i></p>
<dt><code>recv </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> A synonym for <code>get</code></p>
<dt><code>reget </code><i>remote-file </i>[<i>local-file</i> ]</p>
<dd> <code>reget</code> acts like <code>get</code> except that if <i>local-file</i> exists and is smaller than <i>remote-file </i> <i>local-file</i> is presumed to be a partially transferred copy of <i>remote-file</i> and the transfer is continued from the apparent point of failure. This command is useful when transferring very large files over networks that are prone to dropping connections.</p>
<dt><code>remopts </code><i>command </i>[<i>command-options</i> ]</p>
<dd> Set options on the remote <code>FTP</code> server for <i>command</i> to <i>command-options</i> (whose absence is handled on a command-specific basis). Remote <code>FTP</code> commands known to support options include: <code>MLST</code> (used for <code>MLSD</code> and <code>MLST )</code></p>
<dt><code>rename </code>[<i>from </i>[<i>to</i> ] ]</p>
<dd> Rename the file <i>from</i> on the remote machine, to the file <i>to</i></p>
<dt><code>reset</code></p>
<dd> Clear reply queue. This command re-synchronizes command/reply sequencing with the remote <code>FTP</code> server. Resynchronization may be necessary following a violation of the <code>FTP</code> protocol by the remote server.</p>
<dt><code>restart </code><i>marker</i></p>
<dd> Restart the immediately following <code>get</code> or <code>put</code> at the indicated <i>marker</i> On UNIX systems, marker is usually a byte offset into the file.</p>
<dt><code>rhelp </code>[<i>command-name</i> ]</p>
<dd> Request help from the remote <code>FTP</code> server. If a <i>command-name</i> is specified it is supplied to the server as well.</p>
<dt><code>rmdir </code><i>directory-name</i></p>
<dd> Delete a directory on the remote machine.</p>
<dt><code>rstatus </code>[<i>remote-file</i> ]</p>
<dd> With no arguments, show status of remote machine. If <i>remote-file</i> is specified, show status of <i>remote-file</i> on remote machine.</p>
<dt><code>runique</code></p>
<dd> Toggle storing of files on the local system with unique filenames. If a file already exists with a name equal to the target local filename for a <code>get</code> or <code>mget</code> command, a `.1&#8242; is appended to the name. If the resulting name matches another existing file, a `.2&#8242; is appended to the original name. If this process continues up to `.99&#8242; , an error message is printed, and the transfer does not take place. The generated unique filename will be reported. Note that <code>runique</code> will not affect local files generated from a shell command (see below). The default value is off.</p>
<dt><code>send </code><i>local-file </i>[<i>remote-file</i> ]</p>
<dd> A synonym for <code>put</code></p>
<dt><code>sendport</code></p>
<dd> Toggle the use of <code>PORT</code> commands. By default, <code>tnftp</code> will attempt to use a <code>PORT</code> command when establishing a connection for each data transfer. The use of <code>PORT</code> commands can prevent delays when performing multiple file transfers. If the <code>PORT</code> command fails, <code>tnftp</code> will use the default data port. When the use of <code>PORT</code> commands is disabled, no attempt will be made to use <code>PORT</code> commands for each data transfer. This is useful for certain <code>FTP</code> implementations which do ignore <code>PORT</code> commands but, incorrectly, indicate they&#8217;ve been accepted.</p>
<dt><code>set </code>[<i>option value</i> ]</p>
<dd> Set <i>option</i> to <i>value</i> If <i>option</i> and <i>value</i> are not given, display all of the options and their values. The currently supported options are:</p>
<dl>
<dt><code>anonpass</code></p>
<dd> Defaults to <code>$FTPANONPASS</code></p>
<dt><code>ftp_proxy</code></p>
<dd> Defaults to <code>$ftp_proxy</code></p>
<dt><code>http_proxy</code></p>
<dd> Defaults to <code>$http_proxy</code></p>
<dt><code>https_proxy</code></p>
<dd> Defaults to <code>$https_proxy</code></p>
<dt><code>no_proxy</code></p>
<dd> Defaults to <code>$no_proxy</code></p>
<dt><code>pager</code></p>
<dd> Defaults to <code>$PAGER</code></p>
<dt><code>prompt</code></p>
<dd> Defaults to <code>$FTPPROMPT</code></p>
<dt><code>rprompt</code></p>
<dd> Defaults to <code>$FTPRPROMPT</code></dl>
<dt><code>site </code>[<i>arg &#8230;</i> ]</p>
<dd> The arguments specified are sent, verbatim, to the remote <code>FTP</code> server as a <code>SITE</code> command.</p>
<dt><code>size </code><i>remote-file</i></p>
<dd> Return size of <i>remote-file</i> on remote machine.</p>
<dt><code>sndbuf </code><i>size</i></p>
<dd> Set the size of the socket send buffer to <i>size</i></p>
<dt><code>status</code></p>
<dd> Show the current status of <code>tnftp</code></p>
<dt><code>struct </code><i>struct-name</i></p>
<dd> Set the file transfer <i>structure</i> to <i>struct-name</i> The default (and only supported) structure is &#8220;file&#8221;</p>
<dt><code>sunique</code></p>
<dd> Toggle storing of files on remote machine under unique file names. The remote <code>FTP</code> server must support <code>FTP</code> protocol <code>STOU</code> command for successful completion. The remote server will report unique name. Default value is off.</p>
<dt><code>system</code></p>
<dd> Show the type of operating system running on the remote machine.</p>
<dt><code>tenex</code></p>
<dd> Set the file transfer type to that needed to talk to <code>TENEX</code> machines.</p>
<dt><code>throttle</code></p>
<dd> A synonym for <code>rate</code></p>
<dt><code>trace</code></p>
<dd> Toggle packet tracing.</p>
<dt><code>type </code>[<i>type-name</i> ]</p>
<dd> Set the file transfer <code>type</code> to <i>type-name</i> If no type is specified, the current type is printed. The default type is network <code>ASCII</code></p>
<dt><code>umask </code>[<i>newmask</i> ]</p>
<dd> Set the default umask on the remote server to <i>newmask</i> If <i>newmask</i> is omitted, the current umask is printed.</p>
<dt><code>unset </code><i>option</i></p>
<dd> Unset <i>option</i> Refer to <code>set</code> for more information.</p>
<dt><code>usage </code><i>command</i></p>
<dd> Print the usage message for <i>command</i></p>
<dt><code>user </code><i>user-name </i>[<i>password </i>[<i>account </i>] ]</p>
<dd> Identify yourself to the remote <code>FTP</code> server. If the <i>password</i> is not specified and the server requires it, <code>tnftp</code> will prompt the user for it (after disabling local echo). If an <i>account</i> field is not specified, and the <code>FTP</code> server requires it, the user will be prompted for it. If an <i>account</i> field is specified, an account command will be relayed to the remote server after the login sequence is completed if the remote server did not require it for logging in. Unless <code>tnftp</code> is invoked with &#8220;auto-login&#8221; disabled, this process is done automatically on initial connection to the <code>FTP</code> server.</p>
<dt><code>verbose</code></p>
<dd> Toggle verbose mode. In verbose mode, all responses from the <code>FTP</code> server are displayed to the user. In addition, if verbose is on, when a file transfer completes, statistics regarding the efficiency of the transfer are reported. By default, verbose is on.</p>
<dt><code>xferbuf </code><i>size</i></p>
<dd> Set the size of the socket send and receive buffers to <i>size</i></p>
<dt><code>? </code>[<i>command</i> ]</p>
<dd> A synonym for <code>help</code></dl>
<p> Command arguments which have embedded spaces may be quoted with quote `&quot;&#8217; marks. </p>
<p> Commands which toggle settings can take an explicit <code>on</code> or <code>off</code> argument to force the setting appropriately. </p>
<p> Commands which take a byte count as an argument (e.g., <code>hash</code> <code>rate</code> and <code>xferbuf</code> support an optional suffix on the argument which changes the interpretation of the argument. Supported suffixes are:</p>
<dl>
<dt><code>b</code></p>
<dd> Causes no modification. (Optional)</p>
<dt><code>k</code></p>
<dd> Kilo; multiply the argument by 1024</p>
<dt><code>m</code></p>
<dd> Mega; multiply the argument by 1048576</p>
<dt><code>g</code></p>
<dd> Giga; multiply the argument by 1073741824</dl>
<p> If <code>tnftp</code> receives a <code>SIGINFO</code> (see the <code>status</code> argument of <a href="/docs/linux/man/1-stty/">stty</a>(1)) or <code>SIGQUIT</code> signal whilst a transfer is in progress, the current transfer rate statistics will be written to the standard error output, in the same format as the standard completion message.</p>
<h2>AUTO-FETCHING FILES</h2>
<p> In addition to standard commands, this version of <code>tnftp</code> supports an auto-fetch feature. To enable auto-fetch, simply pass the list of hostnames/files on the command line. </p>
<p> The following formats are valid syntax for an auto-fetch element:</p>
<dl>
<dt>[<i>user </i><code>@ </code><i>host </i><code>: </code>[<i>path </i>] ]</p>
<dd> Ns Oo Li / Oc &#8220;Classic&#8221; <code>FTP</code> format. </p>
<p> If <i>path</i> contains a glob character and globbing is enabled, (see <code>glob )</code> then the equivalent of `<code>mget path</code> &#8216; is performed. </p>
<p> If the directory component of <i>path</i> contains no globbing characters, it is stored locally with the name basename (see <a href="/docs/linux/man/1-basename/">basename</a>(1)) of <code>path</code> in the current directory. Otherwise, the full remote name is used as the local name, relative to the local root directory.</p>
<dt><code>ftp:// </code>[<i>user </i>[<code>: </code><i>password </i><code>@ </code>] ]</p>
<dd> Ns Ar host Ns Oo Li : Ns Ar port Oc Ns Li / Ns Ar path Ns Oo Li / Oc Ns Oo Li ;type= Ns Ar type Oc An <code>FTP</code> URL, retrieved using the <code>FTP</code> protocol if <code>set ftp_proxy</code> isn&#8217;t defined. Otherwise, transfer the URL using <code>HTTP</code> via the proxy defined in <code>set ftp_proxy</code> If <code>set ftp_proxy</code> isn&#8217;t defined and <i>user</i> is given, login as <i>user</i> In this case, use <i>password</i> if supplied, otherwise prompt the user for one. </p>
<p> If a suffix of `<code>;type=A</code> &#8216; or `<code>;type=I</code> &#8216; is supplied, then the transfer type will take place as ascii or binary (respectively). The default transfer type is binary. </p>
<p> In order to be compliant with <code>RFC 3986</code> <code>tnftp</code> interprets the <i>path</i> part of an `<code>ftp://</code> &#8216; auto-fetch URL as follows: </p>
<ul>
<li> The `<code>/</code> &#8216; immediately after the <i>host </i>[<code>: </code><i>port </i>] is interpreted as a separator before the <i>path</i> and not as part of the <i>path</i> itself.
<li> The <i>path</i> is interpreted as a So Li / Sc Ns -separated list of name components. For all but the last such component, <code>tnftp</code> performs the equivalent of a <code>cd</code> command. For the last path component, <code>tnftp</code> performs the equivalent of a <code>get</code> command.
<li> Empty name components, which result from `<code>//</code> &#8216; within the <i>path</i> or from an extra `<code>/</code> &#8216; at the beginning of the <i>path</i> will cause the equivalent of a <code>cd</code> command without a directory name. This is unlikely to be useful.
<li> Any `<code>% </code><i>XX</i> &#8216; codes (per <code>RFC 3986</code> within the path components are decoded, with <i>XX</i> representing a character code in hexadecimal. This decoding takes place after the <i>path</i> has been split into components, but before each component is used in the equivalent of a <code>cd</code> or <code>get</code> command. Some often-used codes are `<code>%2F</code> &#8216; (which represents `<code>/</code> &#8216; and `<code>%7E</code> &#8216; (which represents `<code>~</code> &#8216; </ul>
<p> The above interpretation has the following consequences: </p>
<ul>
<li> The path is interpreted relative to the default login directory of the specified user or of the `anonymous&#8217; user. If the / directory is required, use a leading path of `<code>%2F</code> &#8216; If a user&#8217;s home directory is required (and the remote server supports the syntax), use a leading path of `<code>%7E </code><i>user </i><code>/</code> &#8216; For example, to retrieve /etc/motd from `<code>localhost</code> &#8216; as the user `<code>myname</code> &#8216; with the password `<code>mypass</code> &#8216; use `<code><a href="ftp://myname:mypass@localhost/%2fetc/motd">ftp://myname:mypass@localhost/%2fetc/motd</a></code> &#8216;
<li> The exact <code>cd</code> and <code>get</code> commands can be controlled by careful choice of where to use `<code>/</code> &#8216; and where to use `<code>%2F</code> &#8216; (or `<code>%2f</code> &#8216; For example, the following URLs correspond to the equivalents of the indicated commands:
<dl>
<dt><code><a href="ftp://host/dir1/dir2/file">ftp://host/dir1/dir2/file</a></code></p>
<dd> &#8220;cd dir1&#8221; &#8220;cd dir2&#8221; &#8220;get file&#8221;</p>
<dt><code><a href="ftp://host/%2Fdir1/dir2/file">ftp://host/%2Fdir1/dir2/file</a></code></p>
<dd> &#8220;cd /dir1&#8221; &#8220;cd dir2&#8221; &#8220;get file&#8221;</p>
<dt><code><a href="ftp://host/dir1%2Fdir2/file">ftp://host/dir1%2Fdir2/file</a></code></p>
<dd> &#8220;cd dir1/dir2&#8221; &#8220;get file&#8221;</p>
<dt><code><a href="ftp://host/%2Fdir1%2Fdir2/file">ftp://host/%2Fdir1%2Fdir2/file</a></code></p>
<dd> &#8220;cd /dir1/dir2&#8221; &#8220;get file&#8221;</p>
<dt><code><a href="ftp://host/dir1%2Fdir2%2Ffile">ftp://host/dir1%2Fdir2%2Ffile</a></code></p>
<dd> &#8220;get dir1/dir2/file&#8221;</p>
<dt><code><a href="ftp://host/%2Fdir1%2Fdir2%2Ffile">ftp://host/%2Fdir1%2Fdir2%2Ffile</a></code></p>
<dd> &#8220;get /dir1/dir2/file&#8221;</dl>
<li> You must have appropriate access permission for each of the intermediate directories that is used in the equivalent of a <code>cd</code> command. </ul>
<dt><code>http:// </code>[<i>user </i>[<code>: </code><i>password </i><code>@ </code>] ]</p>
<dd> Ns Ar host Ns Oo Li : Ns Ar port Oc Ns Li / Ns Ar path An <code>HTTP</code> URL, retrieved using the <code>HTTP</code> protocol. If <code>set http_proxy</code> is defined, it is used as a URL to an <code>HTTP</code> proxy server. If <code>HTTP</code> authorization is required to retrieve <i>path</i> and <i>user</i> (and optionally <i>password</i> is in the URL, use them for the first attempt to authenticate.</p>
<dt><code>https:// </code>[<i>user </i>[<code>: </code><i>password </i><code>@ </code>] ]</p>
<dd> Ns Ar host Ns Oo Li : Ns Ar port Oc Ns Li / Ns Ar path An <code>HTTPS</code> URL, retrieved using the <code>HTTPS</code> protocol. If <code>set https_proxy</code> is defined, it is used as a URL to an <code>HTTPS</code> proxy server. If <code>HTTPS</code> authorization is required to retrieve <i>path</i> and <i>user</i> (and optionally <i>password</i> is in the URL, use them for the first attempt to authenticate. There is currently no certificate validation and verification.</p>
<dt><code>file:/// </code><i>path</i></p>
<dd> A local URL, copied from / <i>path</i> on the local host.</p>
<dt><code>about: </code><i>topic</i></p>
<dd> Display information regarding <i>topic</i> no file is retrieved for this auto-fetched element. Supported values include:</p>
<dl>
<dt><code>about:ftp</code></p>
<dd> Information about <code>tnftp</code></p>
<dt><code>about:version</code></p>
<dd> The version of <code>tnftp</code> Useful to provide when reporting problems.</dl>
</dl>
<p> Unless noted otherwise above, and &#8211;<code>o </code><i>output</i> is not given, the file is stored in the current directory as the <a href="/docs/linux/man/1-basename/">basename</a>(1) of <i>path</i> Note that if a <code>HTTP</code> redirect is received, the fetch is retried using the new target URL supplied by the server, with a corresponding new <i>path</i> Using an explicit &#8211;<code>o </code><i>output</i> is recommended, to avoid writing to unexpected file names. </p>
<p> If a classic format or an <code>FTP</code> URL format has a trailing `/&#8217; or an empty <i>path</i> component, then <code>tnftp</code> will connect to the site and <code>cd</code> to the directory given as the path, and leave the user in interactive mode ready for further input. This will not work if <code>set ftp_proxy</code> is being used. </p>
<p> Direct <code>HTTP</code> transfers use HTTP 1.1. Proxied <code>FTP</code> and <code>HTTP</code> transfers use HTTP 1.0. </p>
<p> If &#8211;<code>R</code> is given, all auto-fetches that don&#8217;t go via the <code>FTP</code> or <code>HTTP</code> proxies will be restarted. For <code>FTP</code> this is implemented by using <code>reget</code> instead of <code>get</code> For <code>HTTP</code> this is implemented by using the `Range: bytes=&#8217; <code>HTTP/1.1</code> directive. </p>
<p> If WWW or proxy WWW authentication is required, you will be prompted to enter a username and password to authenticate with. </p>
<p> When specifying IPv6 numeric addresses in a URL, you need to surround the address in square brackets. E.g.: `<code><a href="ftp://[::1]:21/">ftp://[::1]:21/</a></code> &#8216; This is because colons are used in IPv6 numeric address as well as being the separator for the port number.</p>
<h2>ABORTING A FILE TRANSFER</h2>
<p> To abort a file transfer, use the terminal interrupt key (usually Ctrl-C). Sending transfers will be immediately halted. Receiving transfers will be halted by sending an <code>FTP</code> protocol <code>ABOR</code> command to the remote server, and discarding any further data received. The speed at which this is accomplished depends upon the remote server&#8217;s support for <code>ABOR</code> processing. If the remote server does not support the <code>ABOR</code> command, the prompt will not appear until the remote server has completed sending the requested file. </p>
<p> If the terminal interrupt key sequence is used whilst <code>tnftp</code> is awaiting a reply from the remote server for the <code>ABOR</code> processing, then the connection will be closed. This is different from the traditional behaviour (which ignores the terminal interrupt during this phase), but is considered more useful.</p>
<h2>FILE NAMING CONVENTIONS</h2>
<p> Files specified as arguments to <code>tnftp</code> commands are processed according to the following rules. </p>
<ol>
<li> If the file name `- &#8216; is specified, the <i>stdin</i> (for reading) or <i>stdout</i> (for writing) is used.
<li> If the first character of the file name is `|&#8217; , the remainder of the argument is interpreted as a shell command. <code>tnftp</code> then forks a shell, using <a href="/docs/linux/man/3-popen/">popen</a>(3) with the argument supplied, and reads (writes) from the stdout (stdin). If the shell command includes spaces, the argument must be quoted; e.g. `<code>&quot;|~ls~-lt&quot;</code> &#8216; A particularly useful example of this mechanism is: `<code>dir~&quot;&quot;~|more</code> &#8216;
<li> Failing the above checks, if globbing is enabled, local file names are expanded according to the rules used in the <a href="/docs/linux/man/1-csh/">csh</a>(1); see the <code>glob</code> command. If the <code>tnftp</code> command expects a single local file (e.g. <code>put )</code> only the first filename generated by the globbing operation is used.
<li> For <code>mget</code> commands and <code>get</code> commands with unspecified local file names, the local filename is the remote filename, which may be altered by a <code>case </code> <code>ntrans</code> or <code>nmap</code> setting. The resulting filename may then be altered if <code>runique</code> is on.
<li> For <code>mput</code> commands and <code>put</code> commands with unspecified remote file names, the remote filename is the local filename, which may be altered by a <code>ntrans</code> or <code>nmap</code> setting. The resulting filename may then be altered by the remote server if <code>sunique</code> is on. </ol>
<h2>FILE TRANSFER PARAMETERS</h2>
<p> The <code>FTP</code> specification specifies many parameters which may affect a file transfer. The <code>type</code> may be one of &#8220;ascii&#8221; &#8220;image&#8221; (binary), &#8220;ebcdic&#8221; and &#8220;local byte size&#8221; (for <code>PDP -10&#8217;s</code> and <code>PDP -20&#8217;s</code> mostly). <code>tnftp</code> supports the ascii and image types of file transfer, plus local byte size 8 for <code>tenex</code> mode transfers. </p>
<p> <code>tnftp</code> supports only the default values for the remaining file transfer parameters: <code>mode</code> <code>form</code> and <code>struct</code></p>
<h2>THE .netrc FILE</h2>
<p> The .netrc file contains login and initialization information used by the auto-login process. It resides in the user&#8217;s home directory, unless overridden with the &#8211;<code>N </code><i>netrc</i> option, or specified in the <code>NETRC</code> environment variable. The following tokens are recognized; they may be separated by spaces, tabs, or new-lines:</p>
<dl>
<dt><code>machine </code><i>name</i></p>
<dd> Identify a remote machine <i>name</i> The auto-login process searches the .netrc file for a <code>machine</code> token that matches the remote machine specified on the <code>tnftp</code> command line or as an <code>open</code> command argument. Once a match is made, the subsequent .netrc tokens are processed, stopping when the end of file is reached or another <code>machine</code> or a <code>default</code> token is encountered.</p>
<dt><code>default</code></p>
<dd> This is the same as <code>machine</code> <i>name</i> except that <code>default</code> matches any name. There can be only one <code>default</code> token, and it must be after all <code>machine</code> tokens. This is normally used as: </p>
<blockquote><p><tt>default login anonymous password user [at] site</tt></p></blockquote>
<p> thereby giving the user an automatic anonymous <code>FTP</code> login to machines not specified in .netrc This can be overridden by using the &#8211;<code>n</code> flag to disable auto-login.</p>
<dt><code>login </code><i>name</i></p>
<dd> Identify a user on the remote machine. If this token is present, the auto-login process will initiate a login using the specified <i>name</i></p>
<dt><code>password </code><i>string</i></p>
<dd> Supply a password. If this token is present, the auto-login process will supply the specified string if the remote server requires a password as part of the login process. Note that if this token is present in the .netrc file for any user other than <i>anonymous </i> <code>tnftp</code> will abort the auto-login process if the .netrc is readable by anyone besides the user.</p>
<dt><code>account </code><i>string</i></p>
<dd> Supply an additional account password. If this token is present, the auto-login process will supply the specified string if the remote server requires an additional account password, or the auto-login process will initiate an <code>ACCT</code> command if it does not.</p>
<dt><code>macdef </code><i>name</i></p>
<dd> Define a macro. This token functions like the <code>tnftp</code> <code>macdef</code> command functions. A macro is defined with the specified name; its contents begin with the next .netrc line and continue until a blank line (consecutive new-line characters) is encountered. Like the other tokens in the .netrc file, a <code>macdef</code> is applicable only to the <code>machine</code> definition preceding it. A <code>macdef</code> entry cannot be used by multiple <code>machine</code> definitions; rather, it must be defined following each <code>machine</code> it is intended to be used with. If a macro named <code>init</code> is defined, it is automatically executed as the last step in the auto-login process. For example, </p>
<blockquote>
<pre>
default
macdef init
epsv4 off
</pre>
</blockquote>
<p> followed by a blank line.</dl>
<h2>COMMAND LINE EDITING</h2>
<p> <code>tnftp</code> supports interactive command line editing, via the <a href="/docs/linux/man/3-editline/">editline</a>(3) library. It is enabled with the <code>edit</code> command, and is enabled by default if input is from a tty. Previous lines can be recalled and edited with the arrow keys, and other GNU Emacs-style editing keys may be used as well. </p>
<p> The <a href="/docs/linux/man/3-editline/">editline</a>(3) library is configured with a .editrc file &#8212; refer to <a href="/docs/linux/man/5-editrc/">editrc</a>(5) for more information. </p>
<p> An extra key binding is available to <code>tnftp</code> to provide context sensitive command and filename completion (including remote file completion). To use this, bind a key to the <a href="/docs/linux/man/3-editline/">editline</a>(3) command <code>ftp-complete</code> By default, this is bound to the TAB key.</p>
<h2>COMMAND LINE PROMPT</h2>
<p> By default, <code>tnftp</code> displays a command line prompt of `<code>ftp&gt;~</code> &#8216; to the user. This can be changed with the <code>set prompt</code> command. </p>
<p> A prompt can be displayed on the right side of the screen (after the command input) with the <code>set rprompt</code> command. </p>
<p> The following formatting sequences are replaced by the given information:</p>
<dl>
<dt><code>%/</code></p>
<dd> The current remote working directory.</p>
<dt><code>%c </code>[[<code>0 </code><i>n , </i><code>%. </code>[[<code>0 </code><i>n </i>] ] ] ]</p>
<dd> The trailing component of the current remote working directory, or <i>n</i> trailing components if a digit <i>n</i> is given. If <i>n</i> begins with `0&#8242; , the number of skipped components precede the trailing component(s) in the format Do <code>/ &lt; </code><i>number </i><code>&gt;</code> <i>trailing</i> Dc (for `%c&#8217; ) or &#8220;<code>&#8230; </code><i>trailing</i> &#8221; (for `%.&#8217; ) .</p>
<dt><code>%M</code></p>
<dd> The remote host name.</p>
<dt><code>%m</code></p>
<dd> The remote host name, up to the first dot `.&#8217;</p>
<dt><code>%n</code></p>
<dd> The remote user name.</p>
<dt><code>%%</code></p>
<dd> A single percent character `%&#8217;</dl>
<h2>ENVIRONMENT</h2>
<p> <code>tnftp</code> uses the following environment variables.</p>
<dl>
<dt><code>FTPANONPASS</code></p>
<dd> Password to send in an anonymous <code>FTP</code> transfer. Defaults to &#8220;<code>`whoami`@</code> &#8221;</p>
<dt><code>FTPMODE</code></p>
<dd> Overrides the default operation mode. Support values are:</p>
<dl>
<dt><code>active</code></p>
<dd> active mode <code>FTP</code> only</p>
<dt><code>auto</code></p>
<dd> automatic determination of passive or active (this is the default)</p>
<dt><code>gate</code></p>
<dd> gate-ftp mode</p>
<dt><code>passive</code></p>
<dd> passive mode <code>FTP</code> only</dl>
<dt><code>FTPPROMPT</code></p>
<dd> Command-line prompt to use. Defaults to `<code>ftp&gt;~</code> &#8216; Refer to Sx COMMAND LINE PROMPT for more information.</p>
<dt><code>FTPRPROMPT</code></p>
<dd> Command-line right side prompt to use. Defaults to empty string. Refer to Sx COMMAND LINE PROMPT for more information.</p>
<dt><code>FTPSERVER</code></p>
<dd> Host to use as gate-ftp server when <code>gate</code> is enabled.</p>
<dt><code>FTPSERVERPORT</code></p>
<dd> Port to use when connecting to gate-ftp server when <code>gate</code> is enabled. Default is port returned by a <a href="/docs/linux/man/3-getservbyname/">getservbyname</a>(3) lookup of &#8220;<code>ftpgate/tcp</code> &#8221;</p>
<dt><code>FTPUSERAGENT</code></p>
<dd> The value to send for the <code>HTTP</code> User-Agent header.</p>
<dt><code>HOME</code></p>
<dd> For default location of a .netrc file, if one exists.</p>
<dt><code>NETRC</code></p>
<dd> An alternate location of the .netrc file.</p>
<dt><code>PAGER</code></p>
<dd> Used by various commands to display files. Defaults to <a href="/docs/linux/man/1-more/">more</a>(1) if empty or not set.</p>
<dt><code>SHELL</code></p>
<dd> For default shell.</p>
<dt><code>ftp_proxy</code></p>
<dd> URL of <code>FTP</code> proxy to use when making <code>FTP</code> URL requests (if not defined, use the standard <code>FTP</code> protocol). </p>
<p> See <code>http_proxy</code> for further notes about proxy use.</p>
<dt><code>http_proxy</code></p>
<dd> URL of <code>HTTP</code> proxy to use when making <code>HTTP</code> URL requests. If proxy authentication is required and there is a username and password in this URL, they will automatically be used in the first attempt to authenticate to the proxy. </p>
<p> If &#8220;unsafe&#8221; URL characters are required in the username or password (for example `@&#8217; or `/&#8217; ) , encode them with <code>RFC 3986</code> `<code>% </code><i>XX</i> &#8216; encoding. </p>
<p> Note that the use of a username and password in <code>ftp_proxy</code> and <code>http_proxy</code> may be incompatible with other programs that use it (such as <a href="/docs/linux/man/1-lynx/">lynx</a>(1)). </p>
<p> <i>NOTE</i> this is not used for interactive sessions, only for command-line fetches.</p>
<dt><code>https_proxy</code></p>
<dd> URL of <code>HTTPS</code> proxy to use when making <code>HTTPS</code> URL requests. </p>
<p> See <code>http_proxy</code> for further notes about proxy use.</p>
<dt><code>no_proxy</code></p>
<dd> A space or comma separated list of hosts (or domains) for which proxying is not to be used. Each entry may have an optional trailing `<code>: </code><i>port</i> &#8216; which restricts the matching to connections to that port.</dl>
<h2>EXTENDED PASSIVE MODE AND FIREWALLS</h2>
<p> Some firewall configurations do not allow <code>tnftp</code> to use extended passive mode. If you find that even a simple <code>ls</code> appears to hang after printing a message such as this: </p>
<blockquote><p><tt>229 Entering Extended Passive Mode (|||58551|)</tt></p></blockquote>
<p> then you will need to disable extended passive mode with <code>epsv4 off</code> See the above section Sx The .netrc File for an example of how to make this automatic.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-getservbyname/">getservbyname</a>(3), <a href="/docs/linux/man/5-editrc/">editrc</a>(5), <a href="/docs/linux/man/5-services/">services</a>(5), <a href="/docs/linux/man/8-ftpd/">ftpd</a>(8)</p>
<h2>STANDARDS</h2>
<p> <code>tnftp</code> attempts to be compliant with:</p>
<dl>
<dt><code>RFC 959</code></p>
<dd> <i>File Transfer Protocol</i></p>
<dt><code>RFC 1123</code></p>
<dd> <i>Requirements for Internet Hosts &#8211; Application and Support</i></p>
<dt><code>RFC 1635</code></p>
<dd> <i>How to Use Anonymous FTP</i></p>
<dt><code>RFC 2389</code></p>
<dd> <i>Feature negotiation mechanism for the File Transfer Protocol</i></p>
<dt><code>RFC 2428</code></p>
<dd> <i>FTP Extensions for IPv6 and NATs </i></p>
<dt><code>RFC 2616</code></p>
<dd> <i>Hypertext Transfer Protocol &#8212; HTTP/1.1</i></p>
<dt><code>RFC 2822</code></p>
<dd> <i>Internet Message Format</i></p>
<dt><code>RFC 3659</code></p>
<dd> <i>Extensions to FTP</i></p>
<dt><code>RFC 3986</code></p>
<dd> <i>Uniform Resource Identifier (URI)</i></dl>
<h2>HISTORY</h2>
<p> The <code>tnftp</code> command appeared in BSD 4.2 </p>
<p> Various features such as command line editing, context sensitive command and file completion, dynamic progress bar, automatic fetching of files and URLs, modification time preservation, transfer rate throttling, configurable command line prompt, and other enhancements over the standard BSD <code>tnftp</code> were implemented in Nx 1.3 and later releases by An Luke Mewburn Aq lukem [at] NetBSD.org . </p>
<p> IPv6 support was added by the WIDE/KAME project (but may not be present in all non-NetBSD versions of this program, depending if the operating system supports IPv6 in a similar manner to KAME).</p>
<h2>BUGS</h2>
<p> Correct execution of many commands depends upon proper behavior by the remote server. </p>
<p> An error in the treatment of carriage returns in the BSD 4.2 ascii-mode transfer code has been corrected. This correction may result in incorrect transfers of binary files to and from BSD 4.2 servers using the ascii type. Avoid this problem by using the binary image type. </p>
<p> <code>tnftp</code> assumes that all IPv4 mapped addresses Po IPv6 addresses with a form like <code>::ffff:10.1.1.1</code> Pc indicate IPv4 destinations which can be handled by <code>AF_INET</code> sockets. However, in certain IPv6 network configurations, this assumption is not true. In such an environment, IPv4 mapped addresses must be passed to <code>AF_INET6</code> sockets directly. For example, if your site uses a SIIT translator for IPv6-to-IPv4 translation, <code>tnftp</code> is unable to support your configuration. </p>
<h2>Index</h2>
