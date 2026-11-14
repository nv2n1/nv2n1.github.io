---
title: "rmt(1)"
name: "rmt"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmt/"
description: "rmt – remote magnetic tape protocol server"
---

<h2>NAME</h2>
<p> rmt &#8211; remote magnetic tape protocol server</p>
<h2>SYNOPSIS</h2>
<p> <code>/opt/schily/sbin/rmt</code><br />
 <code>/etc/rmt</code> </p>
<h2>DESCRIPTION</h2>
<p> This is the description of the enhanced <code>Schily</code> version of the <code>rmt</code> remote tape server program. <code>rmt</code> is a program used by programs like <code>star </code> and <code>ufsdump </code> that like to access remote magnetic tape drives and files through an interprocess communication connection. <code>rmt</code> is normally started up with an <code><a href="/docs/linux/man/3-rexec/">rexec</a></code>(3) or <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) call. </p>
<p> The <code>rmt</code> program accepts <code>open</code>, <code>close</code>, <code>read</code>, <code>write </code> and <code>seek</code> requests as well as requests that are specific to magnetic tapes. <code>rmt</code> performs the commands and then responds with a status indication. </p>
<p> This version of the rmt server gives full compatibility to the original BSD version, the enhanced Sun version and the enhanced GNU version. In addition to the Sun and GNU enhancements, it implements further abstractions for better cross platform compliance. It supports best speed and best compliance even when server and client code are running on different platforms. It is prepared to be installed as a user shell in the passwd file to create remote tape specific logins and security checking. To use the enhanced compatibility features, you need to either use the remote tape client code from <code>star</code> which is available in <code>librmt</code> or reimplement its features. </p>
<p> All responses are send back in <font SIZE="-1">ASCII.</font> They are in one of the following two forms. </p>
<p> Successful commands have responses of</p>
<dl>
<dt>
<dd> <code>A</code><i>number
</i></dl>
<p> where <i>number</i> is the <font SIZE="-1">ASCII</font> representation of a decimal number that usually is the return code of the corresponding system call. Unsuccessful commands are responded to with</p>
<dl>
<dt>
<dd> <code>E</code><i>error-number</i><code>
</code><i>error-message</i><code>
</code></dl>
<p> where <i>error-number</i> is one of the possible error numbers described in <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2), and <i>error-message</i> is the corresponding error string as retrieved by <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3). Note that the error number is valid on the remote system where the <code>rmt</code> code runs and may have a different meaning on the local system. </p>
<p> The protocol implements the following commands:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>O</code><i>device</i><code>
</code><i>mode</i><code>
</code></p>
<dd>
<dt><code>O</code><i>device</i><code>
</code><i>mode symbolic_mode</i><code>
</code></p>
<dd> Open the specified <i>device</i> or file using the indicated <i>mode</i>. <i>device</i> is a full path name, and <i>mode</i> is an <font SIZE="-1">ASCII</font> representation of a decimal number suitable for being passed as second parameter to <code><a href="/docs/linux/man/2-open/">open</a></code>(2). A variant of the <code>open </code> command includes the <code>symbolic_mode</code> string which is a <code>GNU</code> extension. If both, <i>mode</i> and <i>symbolic_mode</i> are present, they are separated by a space character; <i>symbolic_mode</i> appears on the same line as the numeric mode. It is send using the same notation as used in a C source (e.g. <code>O_RDWR|O_CREAT</code>). If the <i>symbolic_mode</i> is send to the server, the numeric <code>mode</code> is ignored. The symbolic notation allows to send the expected open mode over the wire, using a system independent method. This is needed because different operating systems usually define all bits in a different way. An exception are the lowest two bits. The lowest two bits allow to code <i>O_RDONLY</i>,<i>O_WRONLY</i> and <i>O_RDWR</i>. To prevent unexpected behavior, <code>rmt</code> masks the numeric open mode with <code>0x03 </code> before using it as argument to the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) call. If you need more bits in the second parameter ot <code><a href="/docs/linux/man/2-open/">open</a></code>(2), you need to use the symbolic mode. </p>
<p> If no file <i>/etc/default/rmt</i> exists, only filenames starting with /dev/ are accepted for security reasons. </p>
<p> If a device is already open, it is closed before a new open is performed. </p>
<p> A <code>RMT protocol VERSION 1 </code> client should issue a<br />
 <code>I</code><i>-1</i><code>
</code><i>0
</i><br />
 command just after opening a file or device. This is needed to tell the server that the client is aware of the official order of the <i>mt_op</i> codes in the range 0..7 and that is maps deviating values to the official ones. </p>
<dt><code>C</code><i>device</i><code>
</code></p>
<dd> Close the currently open device or file. The argument <i>device</i> is ignored. </p>
<dt><code>R</code><i>count</i><code>
</code></p>
<dd> Read <i>count</i> bytes of data from the open device or file. <code>rmt</code> performs the requested <code><a href="/docs/linux/man/2-read/">read</a></code>(2) operation and responds with <code>A</code><i>count-read
</i> if the read operation was successful; otherwise an error in standard format is returned. If the read operation was successful, the data read is sent directly after the response described above. </p>
<dt><code>W</code><i>count</i><code>
</code></p>
<dd> Write data to the open device or file. After reading the command specification, <code>rmt</code> reads <i>count</i> bytes from the network connection and aborts if a premature <font SIZE="-1">EOF</font> is encountered. The return value from the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) operation is returned as reply. </p>
<dt><code>L</code><i>whence</i><code>
</code><i>offset</i><code>
</code></p>
<dd> Perform an <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) operation on the open device or file using the specified parameters. The return value from the <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) operation is returned as reply. </p>
<p> On large file aware operating systems, <code>rmt</code> will correctly handle large <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) requests.</p>
<dl>
<dt>
<dd>
<p> The following whence values are supported:</p>
<dl>
<dt>0</p>
<dd> Mapped to <code>SEEK_SET</code>.</p>
<dt>1</p>
<dd> Mapped to <code>SEEK_CUR</code>.</p>
<dt>2</p>
<dd> Mapped to <code>SEEK_END</code>.</p>
<dt>3</p>
<dd> Mapped to <code>SEEK_DATA</code> If avalable on the remote system.</p>
<dt>4</p>
<dd> Mapped to <code>SEEK_HOLE</code> If avalable on the remote system.</dl>
</dl>
<dt><code>S</code></p>
<dd> The old non-portable status call. This call should not be used anymore, it has been replaced by the new <code>RMT protocol version 1</code> extended status call below. If the currently open device is a magnetic tape, return the magnetic tape status, as obtained with a <font SIZE="-1"><code>MTIOCGET</code></font> <code>ioctl</code> call. If the open device is not a magnetic tape, an error is returned. If the <font SIZE="-1"><code>MTIOCGET</code></font> operation was successful, an &#8220;ack&#8221; is sent with the size of the status buffer, then the status buffer is sent. As the status buffer is sent in binary, this command it considered outdated. Please use the extended status command instead. This command is not terminated by a new-line. </p>
<dt><code>s</code><i>sub-command</i></p>
<dd> The new portable status call. This command is part of the <code>RMT protocol version 1</code>. If the currently open device is a magnetic tape, return a single specified member of the magnetic tape status structure, as obtained with a <font SIZE="-1"><code>MTIOCGET</code></font> <code>ioctl</code> call. If the open device is not a magnetic tape, an error is returned. If the <font SIZE="-1"><code>MTIOCGET</code></font> operation was successful, the numerical value of the structure member is returned in decimal. The following sub commands are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>T</p>
<dd> return the content of the structure member <code>mt_type</code> which contains the type of the magnetic tape device. </p>
<dt>D</p>
<dd> return the content of the structure member <code>mt_dsreg</code> which contains the &#8220;drive status register&#8221;. </p>
<dt>E</p>
<dd> return the content of the structure member <code>mt_erreg</code> which contains the &#8220;error register&#8221;. </p>
<p> This structure member must be retrieved first because it is cleared after each <font SIZE="-1"><code>MTIOCGET</code></font> <code>ioctl</code> call. The <code>librmt</code> will always retrieve the member <code>mt_erreg</code> first when it is told to retrieve a complete status structure. </p>
<dt>R</p>
<dd> return the content of the structure member <code>mt_resid</code> which contains the residual count of the last I/O. </p>
<dt>F</p>
<dd> return the content of the structure member <code>mt_fileno</code> which contains the block number of the current tape position. </p>
<dt>B</p>
<dd> return the content of the structure member <code>mt_blkno</code> which contains the block number of the current tape position. </p>
<dt>f</p>
<dd> return the content of the structure member <code>mt_flags</code> which contains MTF_ flags from the driver. </p>
<dt>b</p>
<dd> return the content of the structure member <code>mt_bf</code> which contains the optimum blocking factor.</dl>
<p> This command is not terminated with a new-line.</dl>
<dt><code>I</code><i>operation</i><code>
</code><i>count</i><code>
</code></p>
<dd> Perform a <font SIZE="-1"><code>MTIOCOP</code></font> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) command using the specified parameters. The parameters are interpreted as the <font SIZE="-1">ASCII</font> representations of the decimal values to place in the <i>mt_op</i> and <i>mt_count</i> fields of the structure used in the <code>ioctl</code> call. When the operation is successful the return value is the <i>count</i> parameter. Only Opcodes 0..7 are unique across different architectures. In many cases <code>Linux</code> does not even follow this rule. If we know that we have been called by a <code>RMT protocol VERSION 1 </code> client, we may safely assume that the client is not using <code>Linux</code> mapping over the wire but the standard mapping described below:</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> Retrieve the version number of the <code>rmt</code> server and tell the server that the client is aware of the official order of the <font SIZE="-1"><code>MTIOCOP</code></font> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) opcodes in the range 0..7. Local <i>mt_op</i> codes must be remapped to the official values before sending them over the wire. </p>
<p> The answer of the current version of <code>rmt</code> is 1. Old <code>rmt</code> implementations send an error code back when this command is used. Future <code>rmt</code> implementations with further enhancements will send an answer with a value &gt; 1.</p>
<dt>0</p>
<dd> Issue a <code>MTWEOF</code> command (write <i>count</i> end-of-file records).</p>
<dt>1</p>
<dd> Issue a <code>MTFSF</code> command (forward space over <i>count</i> file marks).</p>
<dt>2</p>
<dd> Issue a <code>MTBSF</code> command (backward space over <i>count</i> file marks).</p>
<dt>3</p>
<dd> Issue a <code>MTFSR</code> command (forward space <i>count</i> inter-record gaps).</p>
<dt>4</p>
<dd> Issue a <code>MTBSR</code> command (backward space <i>count</i> inter-record gaps).</p>
<dt>5</p>
<dd> Issue a <code>MTREW</code> command (rewind).</p>
<dt>6</p>
<dd> Issue a <code>MTOFFL</code> command (rewind and put the drive off-line).</p>
<dt>7</p>
<dd> Issue a <code>MTNOP</code> command (no operation, set status only).</dl>
</dl>
<dt><code>i</code><i>operation</i><code>
</code><i>count</i><code>
</code></p>
<dd> Perform a <font SIZE="-1"><code>MTIOCOP</code></font> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) command using the specified parameters. This command is a <code>RMT protocol VERSION 1 </code> extension and implements support for commands beyond MTWEOF..MTNOP (0..7). The parameters are interpreted as the <font SIZE="-1">ASCII</font> representations of the decimal values described below. They are converted into the local values <i>mt_op</i> and <i>mt_count</i> fields of the structure used in the <code>ioctl</code> call according to the actual values found in &lt;sys/mtio.h&gt;. When the operation is successful the return value is the <i>count</i> parameter.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Issue a <code>MTCACHE</code> command (switch cache on).</p>
<dt>1</p>
<dd> Issue a <code>MTNOCACHE</code> command (switch cache off).</p>
<dt>2</p>
<dd> Issue a <code>MTRETEN</code> command (retension the tape).</p>
<dt>3</p>
<dd> Issue a <code>MTERASE</code> command (erase the entire tape).</p>
<dt>4</p>
<dd> Issue a <code>MTEOM</code> command (position to end of media).</p>
<dt>5</p>
<dd> Issue a <code>MTNBSF</code> command (backward space <i>count</i> files to BOF).</dl>
</dl>
<dt><code>v</code><i>
</i></p>
<dd> Return the version of the <code>rmt</code> server. This is currently the decimal number 1.</dl>
</dl>
<p> Any other command causes <code>rmt</code> to exit.</p>
<h2>FILES</h2>
<dl>
<dt>/etc/default/rmt</p>
<dd> The file <code>/etc/default/rmt</code> allows to set up rules to limit the accessibility of files based on rules. This feature is typically used when the rmt run from a non personal but task specific login. </p>
<p> Default values can be set for the following options in /etc/default/rmt. For example: </p>
<p> <code>DEBUG=</code>/tmp/rmt.debug<br />
 <code>USER=</code>tape<br />
 <code>ACCESS=</code>tape<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myhost.mydomain.org<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/rmt/* </p>
<p> All keywords must be on the beginning of a line.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>DEBUG</code></p>
<dd> If you like to get debug information, set this to a file name where <code>rmt</code> should put debug information.</p>
<dt><code>USER</code></p>
<dd> The name of a user (local to the magnetic tape server) that may use the services of the <code>rmt</code> server. More than one <code>USER=</code><i>name</i> line is possible. A line <code>USER=</code>* grants access to all users.</p>
<dt><code>ACCESS</code></p>
<dd> This keyword is followed by three parameters separated by a TAB. The name of a user (local to the magnetic tape server host) that may use the services of the <code>rmt</code> server followed by the name of a host from where operation is granted and a file specifier pattern for a file or file sub tree that may be accessed if this <code>ACCESS</code> line matches. More than one <code>ACCESS=</code><i>name host path</i> line is possible. </p>
<p> If standard input of <code>rmt</code> is not a socket from a remote host, <code>rmt</code> will compare the host entry from <code>/etc/default/rmt</code> with the following strings:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PIPE</code></p>
<dd> If <code>stdin</code> is a <font SIZE="-1">UNIX </font> pipe. </p>
<p> If you like to allow remote connections that use the <code>ssh</code> protocol, you need to use the word <code>PIPE</code> instead of the real hostname in the matching <code>ACCESS=</code> line.</p>
<dt><code>ILLEGAL_SOCKET</code></p>
<dd> If <code>getpeername()</code> does not work for <code>stdin</code>.</p>
<dt><code>NOT_IP</code></p>
<dd> If <code>getpeername()</code> works for <code>stdin</code> but is not connected to an internet socket.</dl>
</dl>
</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-star/">star</a></code>(1), <code><a href="/docs/linux/man/1-ufsdump/">ufsdump</a></code>(1), <code><a href="/docs/linux/man/1-ufsrestore/">ufsrestore</a></code>(1), <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/3-getpeername/">getpeername</a></code>(3), <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3), <code><a href="/docs/linux/man/3-rexec/">rexec</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3), <code><a href="/docs/linux/man/7-mtio/">mtio</a></code>(7), <code><a href="/docs/linux/man/3-rmtopen/">rmtopen</a></code>(3), <code><a href="/docs/linux/man/3-rmtclose/">rmtclose</a></code>(3), <code><a href="/docs/linux/man/3-rmtread/">rmtread</a></code>(3), <code><a href="/docs/linux/man/3-rmtwrite/">rmtwrite</a></code>(3), <code><a href="/docs/linux/man/3-rmtseek/">rmtseek</a></code>(3), <code><a href="/docs/linux/man/3-rmtioctl/">rmtioctl</a></code>(3), <code><a href="/docs/linux/man/3-rmtstatus/">rmtstatus</a></code>(3) </p>
<h2>DIAGNOSTICS</h2>
<p> All responses are send to the network connection. They use the form described above.</p>
<h2>NOTES</h2>
<p> To use <code>rmt</code> as a remote file access protocol you need to use the symbolic open modes as e.g. the <i>O_CREAT</i> flag is not unique between different architectures. </p>
<p> In order to allow this implementation to be used as a remote file access protocol, it accepts file names up to 4096 bytes with the open command. Other <code>rmt</code> implementations allow no more than 64 bytes. </p>
<p> The possibility to create a debug file by calling <code>rmt</code><i> file</i> has been disabled for security reasons. If you like to debug <code>rmt</code> edit <code>/etc/default/rmt</code> and insert a <code>DEBUG</code> entry. </p>
<p> This implementation of <code>rmt</code> adds some security features to the server that make it behave slightly different from older implementations. Read the above documentation about the file /etc/default/rmt to make sure your local installation is configured for your needs. </p>
<p> To grant the same permissions as with old <code>rmt</code> servers, create a file /etc/default/rmt and add the following lines to this file: </p>
<p> <code>USER=</code>*<br />
 <code>ACCESS=</code>* * * </p>
<p> Note that the three fields in the <code>ACCESS=</code> line need to be separated by a TAB character. </p>
<p> Be very careful when designing patterns to match path names that may be accepted for <i>open</i>. If a pattern would allow to include <i>/../</i> in the path, a possible intruder could virtually access any path on your system. For this reason, <i>/../</i> is not allowed to appear in a path regardless of the pattern.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>HISTORY</h2>
<p> The <code>rmt</code> command first appeared on BSD in march 1981. This <code>rmt</code> server is a new implementation that tries to be compatible to all existing implementations. It is the only known implementation that in addition tries to fix the data exchange problems between different architectures. </p>
<h2>AUTHOR</h2>
<pre>
Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</pre>
<p> Mail bugs and suggestions to: </p>
<p> <code>joerg.schilling [at] fokus.fraunhofer.de</code> or <code>js [at] cs.tu-berlin.de</code> or <code>joerg [at] schily.isdn.cs.tu-berlin.de</code> </p>
<h2>Index</h2>
