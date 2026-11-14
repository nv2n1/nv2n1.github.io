---
title: "uberftp(1)"
name: "uberftp"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uberftp/"
description: "uberftp – GridFTP-enabled client"
---

<h2>NAME</h2>
<p> uberftp &#8211; GridFTP-enabled client</p>
<h2>SYNOPSIS</h2>
<p> <code>uberftp</code> [options] [host options] [<i>host</i>] </p>
<p> <code>uberftp</code> [options] [host options] host &#8220;<i>cmd</i>&#8221; </p>
<p> <code>uberftp</code> [options] <i>srcurl</i> <i>dsturl</i> </p>
<p> <code>uberftp</code> [options] -f <i>urlfile</i> </p>
<p> <code>uberftp</code> [options] -cmd <i>url</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>uberftp </code> is a GridFTP-enabled client that supports both interactive use and FTP commands on the <code>uberftp</code> command line to transfer files between two computers. It is intended for use with computers that have a GridFTP server installed. <code>Uberftp</code> supports GSI authentication, parallel data channels and striping. For more information about GridFTP, see the GridFTP URL in the &quot;SEE ALSO&quot; section below. </p>
<p> Only the first usage shown above will create an interactive session. If <i>host</i> is specified, <code>uberftp</code> immediately attempts to establish a connection to the <font SIZE="-1">GridFTP</font> server on <i>host</i>, enters its command interpreter and awaits commands from the user. If <i>host</i> is not specified, <code>uberftp</code> immediately drops into the command interpreter without connecting to any <font SIZE="-1">GridFTP</font> server. </p>
<p> The second usage option denotes a non interactive session in which &#8220;<i>cmd</i>&#8221; is a series of one or more commands as described in the <code>COMMANDS</code> section below to run once the control connection is established. These commands are run exactly as if they had been entered from the interactive prompt. This list must be enclosed in quotes. Multiple commands are semicolon or comma delimited. uberftp will execute these commands and then exit. <code>Uberftp</code> will exit upon the first error encountered. </p>
<p> The third and forth usage statements use the URL style format for specifying the source and destination for the files to transfer. The third usage statement places these URLs on the command line. The forth usage allows the user to specify multiple URL pairs in a separate file for <code>Uberftp</code> to transfer one at a time. The supported URL syntaxes are <a href="gsiftp://[user@]host[:port]/file,">gsiftp://[user@]host[:port]/file,</a> <a href="ftp://[user[:pass]@]host[:port]/file">ftp://[user[:pass]@]host[:port]/file</a> and file://path. </p>
<p> The fifth usage statement allows for commands that take pathnames to accept URLs instead. The allowable commands are listed in the <code>-cmds</code> section below. </p>
<h2>HOST OPTIONS</h2>
<dl>
<dt><code>-P </code><i>port</i></p>
<dd> Connect to <i>port</i> instead of the default. The default for GSI authentication is 2811. The default for password authentication is 21.</p>
<dt><code>-u </code><i>user</i></p>
<dd> Connect as <i>user</i>. This is useful for both password and GSI authentication mechanisms.</p>
<dt><code>-p </code><i>pass</i></p>
<dd> Use <i>pass</i> when authenticating. If <i>pass</i> equals X, UberFTP will prompt for the password with character echoing turned off. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-active</code></p>
<dd> Use ACTIVE mode for data transfers.</p>
<dt><code>-ascii</code></p>
<dd> Use ASCII mode for data transfers.</p>
<dt><code>-binary</code></p>
<dd> Use BINARY mode for data transfers.</p>
<dt><code>-blksize </code><i>n</i></p>
<dd> Set the internal buffer size to <i>n</i>.</p>
<dt><code>-cksum [</code><i>on</i>|<i>off</i>]</p>
<dd> Enable/Disable CRC checks after file transfers.</p>
<dt><code>-cos </code><i>name</i></p>
<dd> Set the storage class of service to <i>name</i>. Used with HPSS installations. Use the class of service name <i>default</i> to allow the remote server to decide which class of service to use.</p>
<dt><code>-d</code></p>
<dd> Enable debugging. Same as &#8216;-debug 3&#8217;. Deprecated.</p>
<dt><code>-debug </code><i>n</i></p>
<dd> Set the debug level to <i>n</i>.</p>
<dt><code>-family </code><i>name</i></p>
<dd> Set the storage family to <i>name</i>. Use the family name <i>default</i> to allow the remote server to decide which family to use.</p>
<dt><code>-glob [</code><i>on</i>|<i>off</i>]</p>
<dd> Enable/Disable filename expansion.</p>
<dt><code>-hash</code></p>
<dd> Enable printing of hash marks during transfers.</p>
<dt><code>-keepalive </code><i>n</i></p>
<dd> Send control channel keepalive messages every <i>n</i> seconds during data transfers.</p>
<dt><code>-mode [</code><i>E</i>|<i>S</i>]</p>
<dd> Switch the transfer mode to extended block (<i>E</i>) or streams mode (<i>S</i>).</p>
<dt><code>-parallel </code><i>n</i></p>
<dd> Use <i>n</i> parallel data channels during extended block transfers.</p>
<dt><code>-passive</code></p>
<dd> Use PASSIVE mode for data transfers.</p>
<dt><code>-pbsz </code><i>n</i></p>
<dd> Set the data protection buffer size to <i>n</i> n bytes.</p>
<dt><code>-prot [</code><i>C</i>|<i>S</i>|<i>E</i>|<i>P</i>]</p>
<dd> Set the data protection lelvel to clear (<i>C</i>), safe (<i>S</i>), confidential (<i>E</i>) or private (<i>P</i>).</p>
<dt><code>-retry </code><i>n</i></p>
<dd> Retry commands that fail with transient errors <i>n</i> times.</p>
<dt><code>-resume </code><i>path</i></p>
<dd> Retry the recursive transfer starting at <i>path</i>.</p>
<dt><code>-tcpbuf </code><i>n</i></p>
<dd> Set the TCP read/write buffers to <i>n</i> bytes.</p>
<dt><code>-wait</code></p>
<dd> This will cause the client to wait for remote files to stage before attempting to transfer them.</p>
<dt><code>-v</code></p>
<dd> Print UberFTP version information and exit.</p>
<dt><code>-version</code></p>
<dd> Print UberFTP version information and exit.</p>
<dt><code>-versions</code></p>
<dd> Print version information about all used globus modules and exit. </p>
</dl>
<h2>Supported -cmds</h2>
<dl>
<dt><code>-cat </code><i>url</i></p>
<dd> Print to stdout the contents of the remote file.</p>
<dt><code>-chgrp [</code><i>-r</i>] <i>group</i> <i>url</i></p>
<dd> Set the group ownership of the remote object(s).</p>
<dt><code>-chmod [</code><i>-r</i>] <i>perms</i> <i>url</i></p>
<dd> Set the permissions of the remote object(s).</p>
<dt><code>-dir [</code><i>-r</i>] <i>url</i></p>
<dd> List the contents of the remote object.</p>
<dt><code>-link </code><i>url</i> <i>path</i></p>
<dd> Create a hardlink named &lt;path&gt; to the remote object.</p>
<dt><code>-ls [</code><i>-r</i>] <i>url</i></p>
<dd> List the contents of the remote object.</p>
<dt><code>-mkdir </code><i>url</i></p>
<dd> Create the remote directory.</p>
<dt><code>-rename </code><i>url</i> <i>path</i></p>
<dd> Rename the remote object to the given path.</p>
<dt><code>-rm [</code><i>-r</i>] <i>url</i></p>
<dd> Remove the remote object(s).</p>
<dt><code>-rmdir </code><i>url</i></p>
<dd> Remove the remote directory.</p>
<dt><code>-size </code><i>url</i></p>
<dd> Return the size of the remote object.</p>
<dt><code>-stage [</code><i>-r</i>] <i>seconds</i> <i>url</i></p>
<dd> Attempt to stage the remote object(s) over the time period given in seconds.</p>
<dt><code>-symlink </code><i>url</i> <i>path</i></p>
<dd> Create a symlink named &lt;path&gt; to the remote object. </p>
</dl>
<h2>DEFAULT TRANSFER MODE</h2>
<p> By default, without any special environment variables, command line options or commands, <code>uberftp</code> will transfer files in PASSIVE STREAMS mode. PASSIVE means that the client will initiate the data connection which is useful for users behind firewalls. STREAMS mode implies that GRIDFTP features including striping and parallel data connections are not used. In order to take advantage of these features with GridFTP capable servers, you must either change the mode directly using -m command line switch or the <code>mode</code> interactive command, or you can change the mode indirectly by specifying more than one parallel data connection using the -c command line switch or by using the <code>parallel</code> interactive command. </p>
<h2>GETTING YOUR GSI PROXY</h2>
<p> <code>By default, uberftp</code> requires a GSI certificate. If you do not already have a certificate, see the following web page to learn how to get one: </p>
<p> <a rel="nofollow" href="http://www.ncsa.uiuc.edu/UserInfo/Grid/Security/GetUserCert.html">http://www.ncsa.uiuc.edu/UserInfo/Grid/Security/GetUserCert.html</a> </p>
<p> Once you have a certificate, use the <code>grid-proxy-init</code> command to get a valid proxy. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>! [</code><i>command</i>]</p>
<dd> Run the command using a shell on the local machine. If no command is given, invoke an interactive shell.</p>
<dt><code>? [</code><i>command</i>]</p>
<dd> If <i>command</i> is given, print a (hopefully) helpful blurb about it. Otherwise, list all commands.</p>
<dt><code>active</code></p>
<dd> Change to ACTIVE mode which causes the server to initiate the data connection. The default is PASSIVE mode unless the variable UBERFTP_ACTIVE_MODE is set in the environment. If you are behind a firewall you must use PASSIVE mode.</p>
<dt><code>ascii</code></p>
<dd> Change the data transfer type to ASCII which causes the server to do some simple transformations to the file being transferred. This is mostly useful for changing EOL (end of line) in text files when moving between platforms. This option is almost never necessary today. The default is BINARY mode also known as IMAGE mode.</p>
<dt><code>binary</code></p>
<dd> Change the data transfer type to BINARY (aka IMAGE) which causes the server to not perform transformations to the file being transferred. This is the default and is faster than an ASCII transfer.</p>
<dt><code>blksize </code><i>size</i></p>
<dd> Change the size of the memory buffer used to read and write data to disks to <i>size</i> bytes. The default block size is 1024*1024 (1048576) bytes but it can be changed at compile time. The block size can be increased to improve file transfer performance. This is not related to the extended block mode block size used to determine the ratio of data to header for data transferred on the data channel.</p>
<dt><code>bugs</code></p>
<dd> Prints information regarding bug reporting and feature requests.</p>
<dt><code>bye</code></p>
<dd> Close all control and data connections and exit.</p>
<dt><code>cat </code><i>file1</i> [<i>file2</i> &#8230; <i>filen</i>]</p>
<dd> Print the contents of the remote file(s) to stdout.</p>
<dt><code>cdup</code></p>
<dd> Change the remote working directory up one level.</p>
<dt><code>cd [</code><i>dir</i>]</p>
<dd> Change the remote working directory to <i>dir</i>. If <i>dir</i> is not given, the client will make every attempt to change to the user&#8217;s home directory. </p>
<dt><code>chgrp [</code><i>-r</i>] <i>group</i> <i>object</i> [<i>object2</i> &#8230; <i>objectn</i>]</p>
<dd> Change group ownership on the remote object(s).<br />
 <i>-r</i> Recursively chgrp everything in the given directory. </p>
<dt><code>chmod [</code><i>-r</i>] <i>perms</i> <i>object</i> [<i>object2</i> &#8230; <i>objectn</i>]</p>
<dd> Change permissions on the remote object(s).<br />
 <i>-r</i> Recursively chmod everything in the given directory.</p>
<dt><code>close</code></p>
<dd> Close the control connection to the remote host.</p>
<dt><code>cksum [</code><i>on</i>|<i>off</i>]</p>
<dd> Enable file cksum comparison after each file transfer. This only works with NCSA&#8217;s mass storage system.<br />
 <i>on</i> Enable checksum comparison<br />
 <i>off</i> Disable checksum comparison</p>
<dt><code>cos </code><i>name</i></p>
<dd> Sets the HPSS class of service to <i>name</i> on the FTP service if the service supports it. If <i>name</i> is omitted, the current class of service is printed. Use the class of service name <i>default</i> to allow the remote server to decide which class of service to use.</p>
<dt><code>dcau [</code><i>N</i>|<i>A</i>|<i>S</i> <i>subject</i>]</p>
<dd> Change the data channel authentication settings. If the service does not support DCAU, these settings are ignored.<br />
 <i>N</i> Disabled dcau.<br />
 <i>A</i> Expect the remote identity to be mine. (Default)<br />
 <i>S</i> <i>subject</i> Expect the remote identity to be <i>subject</i>.</p>
<dt><code>debug [</code><i>0-3</i>]</p>
<dd> Turn debug statements on/off. If no value is given, this command will toggle between <a href="/docs/linux/man/2-debug/">debug</a>(2) and non <a href="/docs/linux/man/1-debug/">debug</a>(1) mode. Otherwise the debug level is set to the given level.<br />
 0 Only errors are printed<br />
 1 Default. Errors and some helpful messages are printed<br />
 2 Print useful control channel information<br />
 3 Print all information</p>
<dt><code>family </code><i>name</i></p>
<dd> Sets the tape family to <i>name</i> on the FTP service if the service supports it. If <i>name</i> is omitted, the current family is printed. Use the family name <i>default</i> to allow the remote server to decide which family to use.</p>
<dt><code>glob [</code><i>on</i>|<i>off</i>]</p>
<dd> Enable or disable filename globbing. If no option is given, this command will toggle the current setting.<br />
 <i>on</i> Enable filename globbing<br />
 <i>off</i> Disable filename globbing</p>
<dt><code>dir [</code><i>-r</i>] [<i>target</i>]</p>
<dd> List the contents of the remote target directory. If <i>target</i> is not given, then the current working directory is used.<br />
 <i>-r</i> Recursively list <i>target</i>.<br />
 <i>target</i> Directory or file to list. &#8216;.&#8217; is used by default.</p>
<dt><code>get [</code><i>-r</i>] <i>source</i> [<i>destination</i>]</p>
<dd> Retrieve file(s) from the remote service. If <i>source</i> implies multiple transfers, either through regular expressions or by using the recursive feature, then <i>destination</i> must be a directory. If <i>destination</i> is not specified, <i>source</i> is used.<br />
 <i>-r</i> Recursively transfer the given directory.</p>
<dt><code>hash</code></p>
<dd> Print hash marks during data transfers. This does not work during third party transfers.</p>
<dt><code>help [</code><i>command</i>]</p>
<dd> If <i>command</i> is given, print a helpful blurb about <i>command</i>. Otherwise, list all commands.</p>
<dt><code>keepalive [</code><i>seconds</i>]</p>
<dd> Attempts to keep the control channel from being blocked by firewalls during long data channel operations. UberFTP sends a NOOP command to the service at intervals equal to the specified number of <i>seconds</i>. Setting it to zero will disable keepalive. If <i>seconds</i> are not given, the current timeout is displayed. This feature is disabled by default.<br />
 seconds number of seconds between NOOPs. Disabled if zero.</p>
<dt><code>lcat </code><i>file1</i> [<i>file2</i> &#8230; <i>filen</i>]</p>
<dd> Print the contents of the local file(s) to stdout.</p>
<dt><code>lcd [</code><i>dir</i>]</p>
<dd> Change the local working directory to <i>dir</i>. If <i>dir</i> is not given, the client will make every attempt to change to the user&#8217;s home directory.</p>
<dt><code>lcdup</code></p>
<dd> Change the local working directory up one level.</p>
<dt><code>lchgrp [</code><i>-r</i>] <i>group</i> <i>object</i> [<i>object2</i> &#8230; <i>objectn</i>]</p>
<dd> Change group ownership on the local object(s).<br />
 <i>-r</i> Recursively chgrp everything in the given directory. </p>
<dt><code>lchmod [</code><i>-r</i>] <i>perms</i> <i>object</i> [<i>object2</i> &#8230; <i>objectn</i>]</p>
<dd> Change permissions on the local object(s).<br />
 <i>-r</i> Recursively chmod everything in the given directory.</p>
<dt><code>lclose</code></p>
<dd> Close the control connection to the local host.</p>
<dt><code>ldir [</code><i>-r</i>] [<i>target</i>]</p>
<dd> List the contents of the local <i>target</i> directory. If <i>target</i> is not given, then the current working directory is used.<br />
 <i>-r</i> Recursively list <i>target</i>.<br />
 target Directory or file to list. &#8216;.&#8217; is used by default.</p>
<dt><code>link [</code><i>oldfile</i>] [<i>newfile</i>]</p>
<dd> Create a hardlink to oldfile named newfile on the remote service.</p>
<dt><code>llink [</code><i>oldfile</i>] [<i>newfile</i>]</p>
<dd> Create a hardlink to oldfile named newfile on the local service.</p>
<dt><code>lls [</code><i>-r</i>] [<i>target</i>]</p>
<dd> List the contents of the local <i>target</i> directory. If <i>target</i> is not given, then the current working directory is used.<br />
 <i>-r</i> Recursively list <i>target</i>.<br />
 target Directory or file to list. &#8216;.&#8217; is used by default.</p>
<dt><code>llscos</code></p>
<dd> List the available class of services on the local server (HPSS only).</p>
<dt><code>llsfam</code></p>
<dd> List the available tape families on the local server (HPSS only).</p>
<dt><code>lmkdir </code><i>dir1</i> [<i>dir2</i> &#8230; <i>dirn</i>]</p>
<dd> Create the local directory(ies).</p>
<dt><code>lopen [</code><i>-P port</i>] [<i>-u user</i>] [<i>-p pass</i> | <i>X</i>] <i>host</i></p>
<dd> Opens a control channel to <i>host</i> and that host becomes the &#8216;local&#8217; machine. After using lopen, all local (l*) commands perform their respective operations on <i>host</i> rather than the local machine. This is how third party transfers are accomplished. GSI authentication is used unless the <i>-p</i> option is used.<br />
 <i>-P port</i> Connect to port (Default 2811 for GSI, 21 for password).<br />
 <i>-u user</i> Connect as alternate user.<br />
 <i>-p pass</i> | <i>X</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use password&nbsp;<wbr><i>pass</i>&nbsp;<wbr>when authenticating with&nbsp;<wbr><i>host</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr><i>pass</i>&nbsp;<wbr>equals&nbsp;<wbr><i>X</i>, read the password from STDIN with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>character echoing turned off.<br />
 <i>host</i> Connect to <i>host</i>.</p>
<dt><code>lpwd</code></p>
<dd> Prints the current local working directory.</p>
<dt><code>lrename </code><i>src</i> <i>dst</i></p>
<dd> Rename the local object <i>src</i> to <i>dst</i>.</p>
<dt><code>lrm [</code><i>-r</i>] <i>object1</i> [<i>object1</i>&#8230;<i>objectn</i>]</p>
<dd> Removes the local file system object(s).<br />
 <i>-r</i> Recursively remove the given directory.</p>
<dt><code>lrmdir </code><i>dir1</i> [<i>dir2</i>&#8230;<i>dirn</i>]</p>
<dd> Removes the given directories from the local service.</p>
<dt><code>lquote </code><i>cmd</i></p>
<dd> Pass <i>cmd</i> to the local FTP service. This allows the user to use server-specific commands that are not available through the uberftp interface.</p>
<dt><code>ls [</code><i>-r</i>] [<i>target</i>]</p>
<dd> List the contents of the remote target directory. If [<i>target</i>] is not given, then the current working directory is used.<br />
 <i>-r</i> Recursively list <i>target</i>.<br />
 <i>target</i> Directory or file to list. &#8216;.&#8217; is used by default.</p>
<dt><code>lscos</code></p>
<dd> List the available class of services on the remote server (HPSS only).</p>
<dt><code>lsfam</code></p>
<dd> List the available tape families on the remote server (HPSS only).</p>
<dt><code>lsize </code><i>file1</i> [<i>file2</i>&#8230;<i>filen</i>]</p>
<dd> Prints the size of the given object(s).</p>
<dt><code>lstage [</code><i>-r</i>] <i>seconds</i> <i>object1</i> [<i>object2</i>&#8230;<i>objectn</i>]</p>
<dd> Attempt to stage all matching files within the given number of <i>seconds</i> on the local service.<br />
 seconds number of seconds to attempt staging<br />
 <i>-r</i> Recursively stage all files in the given subdirectory.</p>
<dt><code>lsymlink [</code><i>oldfile</i>] [<i>newfile</i>]</p>
<dd> Create a symlink to oldfile named newfile on the local service.</p>
<dt><code>mput [</code><i>-r</i>] <i>object1</i> [<i>object2</i>&#8230;<i>objectn</i>]</p>
<dd> Retrieve file(s) from the remote service. This is similiar to making multiple calls to get without specifying a destination.<br />
 <i>-r</i> Recursively transfer the given directory.</p>
<dt><code>mkdir </code><i>dir</i></p>
<dd> Create the remote directory.</p>
<dt><code>mode [</code><i>E</i>|<i>S</i>]</p>
<dd> Toggle the data transfer mode between Streams mode and Extended Block mode. The default is Streams mode. If no option is given, it will display the current mode.<br />
 E Extended block mode<br />
 S Streams mode</p>
<dt><code>mput [</code><i>-r</i>] <i>object1</i> [<i>object2</i>&#8230;<i>objectn</i>]</p>
<dd> Store file(s) to the remote service. This is similiar to making multiple calls to put without specifying a destination.<br />
 <i>-r</i> Recursively transfer the given directory.</p>
<dt><code>open [</code><i>-P port</i>] [<i>-u user</i>] [<i>-p pass</i> | <i>X</i>] <i>host</i></p>
<dd> Opens a control channel to <i>host</i> and that host becomes the &#8216;remote&#8217; machine. GSI authentication is used unless the -p option is used.<br />
 <i>-P port</i> Connect to <i>port</i> (Default 2811 for GSI, 21 for password).<br />
 <i>-u user</i> Connect as <i>user</i>.<br />
 <i>-p pass</i> | <i>X</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use password&nbsp;<wbr><i>pass</i>&nbsp;<wbr>when authenticating with&nbsp;<wbr><i>host</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr><i>pass</i>&nbsp;<wbr>equals&nbsp;<wbr><i>X</i>, read the password from STDIN with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>character echoing turned off.<br />
 <i>host</i> Connect to <i>host</i>.</p>
<dt><code>order [</code><i>type</i>]</p>
<dd> Changes the order of lists returned from ls and lls to the given scheme. If <i>type</i> is not given, the current order is displayed.<br />
 <i>type</i> Ordering scheme to use. Value options are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>none&nbsp;<wbr>&nbsp;<wbr>Do not order listings </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>name&nbsp;<wbr>&nbsp;<wbr>Order listings by name </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size&nbsp;<wbr>&nbsp;<wbr>Order listings by size </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>type&nbsp;<wbr>&nbsp;<wbr>Order listings by type</p>
<dt><code>parallel [</code><i>number</i>]</p>
<dd> Set the number of parallel data connections to <i>number</i>. This is only useful for extended block mode transfers. The default number of data connections is one. If no number is given, the current setting for the number of parallel connects is printed.</p>
<dt><code>passive</code></p>
<dd> Change to PASSIVE mode which causes the client to initiate the data connection. This is the default mode unless the variable UBERFTP_ACTIVE_MODE is set in the environment. If you are behind a firewall you must use PASSIVE mode.</p>
<dt><code>pbsz [</code><i>size</i>]</p>
<dd> Change the length of the protection buffer. The protection buffer is used to encrypt data on the data channel. The length of the protection buffer represents the largest encoded message that is allowed on the data channel. By default, the protection buffer is grown to match the internal buffer used. For efficient transfers, pbsz should be sufficiently larger than blksize so that the wrapped buffer fits within the protection buffer. Otherwise, the blksize buffer is broken into multiple pieces so that each write is less than pbsz when wrapped. If <i>pbsz</i> is not given, the current size is displayed.<br />
 <i>size</i> length of protection buffer. 0 will set it to its default.</p>
<dt><code>pget </code><i>offset</i> <i>size</i> <i>srcfile</i> [<i>destfile</i>]</p>
<dd> Retrieve only the specified portion of the file(s). If srcfile is a regular expression and expands to multiple files, and destination is given, destination must refer to a directory.<br />
 <i>offset</i> Offset within the file<br />
 <i>size</i> Amount of data to retrieve<br />
 <i>srcfile</i> Name of remote file<br />
 <i>destfile</i> Name of local file. srcfile is used if destfile<br />
 is not specified</p>
<dt><code>pput </code><i>offset</i> <i>size</i> <i>srcfile</i> [<i>destfile</i>]</p>
<dd> Store only the specified portion of the file(s). If srcfile is a regular expression and expands to multiple files, and destination is given, destination must refer to a directory.<br />
 <i>offset</i> Offset within the file<br />
 <i>size</i> Amount of data to retrieve<br />
 <i>srcfile</i> Name of local file<br />
 <i>destfile</i> Name of remote file. srcfile is used if destfile </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is not specified</p>
<dt><code>prot [</code><i>C</i>|<i>S</i>|<i>E</i>|<i>P</i>]</p>
<dd> This command configures the level of security on the data channel after data channel authentication has completed. Clear means that the data will not be protected. Safe means that the data will be integrity protected meaning that altered data will be detected. Confidential means that the data will be unreadable to third parties. Private mode means the data will be confidential and safe.<br />
 <i>C</i> Set protection level to clear.<br />
 <i>S</i> Set protection level to safe.<br />
 <i>E</i> Set protection level to confidential.<br />
 <i>P</i> Set protection level to private.</p>
<dt><code>put [</code><i>-r</i>] <i>source</i> [<i>destination</i>]</p>
<dd> Store file(s) to the remote service. If <i>source</i> implies multiple transfers, either through regular expressions or by using the recursive feature, then <i>destination</i> must be a directory. If <i>destination</i> is not specified, <i>source</i> is used.<br />
 <i>-r</i> Recursively transfer the given directory.</p>
<dt><code>pwd</code></p>
<dd> Prints the current working directory.</p>
<dt><code>quit</code></p>
<dd> Close all control and data connections and exit.</p>
<dt><code>quote </code><i>cmd</i></p>
<dd> Pass <i>cmd</i> to the remote FTP service. This allows the user to use server-specific commands that are not available through the uberftp interface.</p>
<dt><code>rename </code><i>src</i> <i>dst</i></p>
<dd> Rename the remote object <i>src</i> to <i>dst</i>.</p>
<dt><code>retry [</code><i>cnt</i>]</p>
<dd> Configures retry on failed commands that have transient errors. <i>cnt</i> represents the number of times a failed command is retried. A value of zero effectively disables retry. Zero is the default. If no value is given the current setting is displayed.<br />
 <i>cnt</i> Number of times a failed command is retried.</p>
<dt><code>resume [</code><i>-d</i>] <i>path</i></p>
<dd> Sets a restart point for recursive transfers. If a long recursive transfer fails, you can set resume to the path that failed and UberFTP will skip all file and directory creations up to the given path.<br />
 <i>path</i> Path to resume transfer at. If <i>path</i> is not given, print the current </p>
<p>&nbsp;<wbr>resume target.<br />
 <i>-d</i> Remove the current resume path.</p>
<dt><code>rm [</code><i>-r</i>] <i>object1</i> [<i>object1</i>&#8230;<i>objectn</i>]</p>
<dd> Removes the remote file system object(s).<br />
 <i>-r</i> Recursively remove the given directory.</p>
<dt><code>rmdir </code><i>dir1</i> [<i>dir2</i>&#8230;<i>dirn</i>]</p>
<dd> Removes the given directories from the remote service.</p>
<dt><code>runique</code></p>
<dd> Toggles the client to store files using unique names during put operations.</p>
<dt><code>size </code><i>file1</i> [<i>file2</i>&#8230;<i>filen</i>]</p>
<dd> Prints the size of the given object(s).</p>
<dt><code>stage [</code><i>-r</i>] <i>seconds</i> <i>object1</i> [<i>object2</i>&#8230;<i>objectn</i>]</p>
<dd> Attempt to stage all matching files within the given number of seconds on the remote service.<br />
 <i>seconds</i> number of seconds to attempt staging<br />
 <i>-r</i> Recursively stage all files in the given subdirectory.</p>
<dt><code>sunique</code></p>
<dd> Toggles the client to store files using unique names during get operations.</p>
<dt><code>symlink [</code><i>oldfile</i>] [<i>newfile</i>]</p>
<dd> Create a symlink to oldfile named newfile on the remote service.</p>
<dt><code>tcpbuf [</code><i>size</i>]</p>
<dd> Set the data channel TCP buffer size to <i>size</i> bytes. If <i>size</i> is not given, the current TCP buffer size will be printed.</p>
<dt><code>versions</code></p>
<dd> Prints the versions of all Globus modules being used.</p>
<dt><code>wait</code></p>
<dd> Toggles whether the client should wait for files to stage before attempting to retrieve them. </p>
</dl>
<h2>IMPROVING FILE TRANSFER PERFORMANCE</h2>
<p> Use the <code>active</code> command to enable <i>active</i> mode FTP when using NCSA&#8217;s UniTree mass storage system if possible since it will give much better file transfer performance. When tranferring files over long distances, use a large value (for example, 16777216) for <code>tcpbuf</code>. When there is high network traffic, you may be able to improve performance using the <code>parallel</code> command to increase the number of parallel data connections to 2-4.</p>
<h2>THIRD-PARTY TRANSFERS</h2>
<p> In order to perform a third-party transfer, you must log into two <code>FTP</code> servers. Typically, you connect to a single <code>FTP</code> service to &quot;get&quot; files to the local machine and &quot;put&quot; files to the remote service. For third-party transfers, you must connect to a second service thereby replacing the former local machine. In <code>UberFTP</code> terminology, it is referred to as &quot;opening a new local service&quot; since, from the perspective of the user, the new local service will appear as though the user initiated the FTP session from that machine. </p>
<p> All remote service commands have &quot;l*&quot; counterparts that allow you to specify that the command is to be performed on the local service, whether that service is the local machine or a new local service. So to open a new local service, use the &quot;l*&quot; version of the open command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>UberFTP&gt;&nbsp;<wbr>lopen mss.ncsa.teragrid.org<br />
&nbsp;<wbr>&nbsp;<wbr>UberFTP&gt;&nbsp;<wbr>lclose<br />
 Once you have connected to both services, files can be transferred as before with the change that files you &quot;get&quot; go to the new local service and files you &quot;put&quot; are sent from the new local service.</p>
<h2>CONTROLLING EPHEMERAL PORT SELECTION</h2>
<p> By default, local port selection is managed by the operating system. However, you may wish to specify which ports UberFTP should use for incoming and out going connections. This is useful when dealing with firewalls. </p>
<p> Setting UBERFTP_TCP_PORT_RANGE in your environment will cause all inbound connections to use the specified port range. Likewise, setting UBERFTP_TCP_SOURCE_RANGE in your environment will cause all outbound connections to use the specified port range. </p>
<p> The environment variables GLOBUS_TCP_PORT_RANGE and GLOBUS_TCP_SOURCE_RANGE will also control the ephemeral port selection. These variables behave exactly as their UBERFTP counterparts and are available for backwards compatibility with older versions. The UBERFTP variables take precedence over the GLOBUS variables. </p>
<p> The values of the variables specify a port range, a minimum port number and a maximum port number, separated by either a comma or a space. For example, to set the inbound port range, you would set: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>UBERFTP_TCP_PORT_RANGE=40000,50000 </p>
<p> Using the space delimiter, this format is also acceptable: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>UBERFTP_TCP_PORT_RANGE=&quot;40000 50000&quot; </p>
<p> See your shell documentation for the proper syntax for settings variables within your environment. </p>
<p> Setting the ephemeral port range to an unusable range will cause UberFTP connections to fail. For instance, setting a port range from 10 to 100 with a non root process will fail on most operating systems. </p>
<h2>EXIT VALUES</h2>
<p> UberFTP will exit with a value of 0 if no errors occurred during the session, otherwise it will exit with a value of 1. In non interactive, commandline mode, it will exit after the first error occurs.</p>
<h2>EXAMPLES</h2>
<p> Set the environment variable to set <i>active</i> mode FTP (improves file transfer performance to the mass storage system). Connect to NCSA&#8217;s UniTree mass storage system interactively from NCSA&#8217;s TeraGrid cluster: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>setenv UBERFTP_ACTIVE_MODE on<br />
&nbsp;<wbr>&nbsp;<wbr>%&nbsp;<wbr>uberftp mss.ncsa.teragrid.org<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>220 UNIX Archive FTP server ready.<br />
&nbsp;<wbr>&nbsp;<wbr>230 User consult logged in.<br />
&nbsp;<wbr>&nbsp;<wbr>UberFTP&gt; </p>
<p> Use the command-line interface to copy a file from NCSA&#8217;s TeraGrid cluster to the UniTree mass storage system. (There is no need to set <code>tcpbuf</code> since it is over a LAN but <i>active</i> mode is turned on to improve file transfer performance to the mass storage system.): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>uberftp mss.ncsa.teragrid.org&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;active;&nbsp;<wbr>cd work;&nbsp;<wbr>get file.tar&quot; </p>
<p> Copy a file from SDSC&#8217;s TeraGrid cluster to NCSA&#8217;s TeraGrid cluster. (Note that <code>tcpbuf</code> is set to 16777216 since there is a long network latency between NCSA and SDSC): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>uberftp tg-grid<a href="ftp://ftp.sdsc.teragrid.org">ftp.sdsc.teragrid.org</a>&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;tcpbuf 16777216;&nbsp;<wbr>cd scr;&nbsp;<wbr>put file.tar&quot;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mssftp/">mssftp</a></code>(1), <code><a href="/docs/linux/man/1-msscmd/">msscmd</a></code>(1), <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1),<br />
 GridFTP: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.globus.org/datagrid/gridftp.html">http://www.globus.org/datagrid/gridftp.html</a><br />
 TCP Window Size: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://dast.nlanr.net/Articles/GettingStarted/TCP_window_size.html">http://dast.nlanr.net/Articles/GettingStarted/TCP_window_size.html</a><br />
 Active vs. Passive FTP: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://slacksite.com/other/ftp.html">http://slacksite.com/other/ftp.html</a> </p>
<p> <code>Note: The links above are not under NCSA&#8217;s control so they may become obsolete.</code> </p>
<h2>Index</h2>
