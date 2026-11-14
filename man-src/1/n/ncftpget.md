---
title: "ncftpget(1)"
name: "ncftpget"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftpget/"
description: "ncftpget – Internet file transfer program for scripts"
---

<h2>NAME</h2>
<p> ncftpget &#8211; Internet file transfer program for scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>ncftpget</code> [<i>options</i>] <i>remote-host local-directory remote-files&#8230;</i> </p>
<p> <code>ncftpget</code> [<i>options</i>] <i>bookmark-name local-directory remote-files&#8230;</i> </p>
<p> <code>ncftpget</code> -f login.cfg [<i>options</i>] <i>local-directory remote-files&#8230;</i> </p>
<p> <code>ncftpget</code> [<i>options</i>] <i><a href="ftp://url.style.host/path/name">ftp://url.style.host/path/name</a></i> </p>
<p> <code>ncftpget</code> -c [<i>options</i>] <i>remote-host remote-file</i> &gt; stdout </p>
<p> <code>ncftpget</code> -C [<i>options</i>] <i>remote-host remote-file local-path-name</i> </p>
<p> <code>ncftpget</code> -c [<i>options</i>] <i><a href="ftp://url.style.host/path/name">ftp://url.style.host/path/name</a></i> &gt; stdout</p>
<h2>OPTIONS</h2>
<h3>Command line flags:</h3>
<dl>
<dt><code>-u </code><i>XX</i></p>
<dd> Use username <i>XX</i> instead of anonymous.</p>
<dt><code>-p </code><i>XX</i></p>
<dd> Use password <i>XX</i> with the username.</p>
<dt><code>-P </code><i>XX</i></p>
<dd> Use port number <i>XX</i> instead of the default FTP service port (21).</p>
<dt><code>-j </code><i>XX</i></p>
<dd> Use account <i>XX</i> in supplement to the username and password (deprecated).</p>
<dt><code>-d </code><i>XX</i></p>
<dd> Use the file <i>XX</i> for debug logging.</p>
<dt><code>-a</code></p>
<dd> Use ASCII transfer type instead of binary.</p>
<dt><code>-t </code><i>XX</i></p>
<dd> Timeout after <i>XX</i> seconds.</p>
<dt><code>-v</code>/<code>-V</code></p>
<dd> Do (do not) use progress meters. The default is to use progress meters if the output stream is a TTY.</p>
<dt><code>-f </code><i>XX</i></p>
<dd> Read the file <i>XX</i> for host, user, and password information.</p>
<dt><code>-c</code></p>
<dd> Read from remote host and write locally to standard out.</p>
<dt><code>-C</code></p>
<dd> Read from remote host and write locally to specified pathname.</p>
<dt><code>-A</code></p>
<dd> Append to local files, instead of overwriting them.</p>
<dt><code>-z</code>/<code>-Z</code></p>
<dd> Do (do not) try to resume transfers. The default is to try to resume (-z).</p>
<dt><code>-E</code></p>
<dd> Use regular (PORT) data connections.</p>
<dt><code>-F</code></p>
<dd> Use passive (PASV) data connections. The default is to use passive, but to fallback to regular if the passive connection fails or times out.</p>
<dt><code>-DD</code></p>
<dd> Delete remote file after successfully downloading it.</p>
<dt><code>-R</code></p>
<dd> Recursive mode; copy whole directory trees.</p>
<dt><code>-T</code></p>
<dd> Do not use automatic on-the-fly TAR mode for downloading whole directory trees. <i>ncftpget</i> uses TAR whenever possible since this usually preserves symbolic links and file permissions. TAR mode can also result in faster transfers for directories containing many small files, since a single data connection can be used rather than an FTP data connection for each small file. The downside to using TAR is that it forces downloading of the whole directory, even if you had previously downloaded a portion of it earlier, so you may want to use this option if you want to resume downloading of a directory.</p>
<dt><code>-r </code><i>XX</i></p>
<dd> Redial a maximum of <i>XX</i> times until connected to the remote FTP server.</p>
<dt><code>-b</code></p>
<dd> Run in background (by submitting a batch job and then spawning <i>ncftpbatch</i>).</p>
<dt><code>-bb</code></p>
<dd> Similar to <code>-b</code> option, but only submits the batch job. You will need to run <i>ncftpbatch</i> for the batch job to be processed. This is useful if you already have a <i>ncftpbatch</i> process running, or wish to have better control of when batch jobs are processed.</p>
<dt>
<dd> For example, if you wanted to do background processing of three files all on the same remote server, it is more polite to use just one <i>ncftpbatch</i> process to process the three jobs sequentially, rather than having three <i>ncftpbatch</i> processes open three simultaneous FTP sessions to the same server.</p>
<dt><code>-B </code><i>XX</i></p>
<dd> Try setting the TCP/IP socket buffer size to <i>XX</i> bytes.</p>
<dt><code>-W </code><i>XX</i></p>
<dd> Send raw FTP command <i>XX</i> after logging in.</p>
<dt><code>-X </code><i>XX</i></p>
<dd> Send raw FTP command <i>XX</i> after each file transferred.</p>
<dt><code>-Y </code><i>XX</i></p>
<dd> Send raw FTP command <i>XX</i> before logging out.</p>
<dt>
<dd> The <code>-W</code>, <code>-X</code>, and <code>-Y</code> options are useful for advanced users who need to tweak behavior on some servers. For example, users accessing mainframes might need to send some special SITE commands to set blocksize and record format information.</p>
<dt>
<dd> For these options, you can use them multiple times each if you need to send multiple commands. For the <code>-X</code> option, you can use the cookie <code>%s</code> to expand into the name of the file that was transferred.</p>
<dt><code>-o </code><i>XX</i></p>
<dd> Set advanced option <i>XX</i>.</p>
<dt>
<dd> This option is used primarily for debugging. It sets the value of an internal variable to an integer value. An example usage would be: <code>-o </code><i>useFEAT=0,useCLNT=1</i> which in this case, disables use of the FEAT command and enables the CLNT command. The available variables include: usePASV, useSIZE, useMDTM, useREST, useNLST_a, useNLST_d, useFEAT, useMLSD, useMLST, useCLNT, useHELP_SITE, useSITE_UTIME, STATfileParamWorks, NLSTfileParamWorks, require20, allowProxyForPORT, doNotGetStartCWD.</dl>
<h2>DESCRIPTION</h2>
<p> The purpose of <i>ncftpget</i> is to do file transfers from the command-line without entering an interactive shell. This lets you write shell scripts or other unattended processes that can do FTP. It is also useful for advanced users who want to retrieve files from the shell command line without entering an interactive FTP program such as <i>ncftp</i>. </p>
<p> One particularly useful feature of this program is that you can give it a <i>uniform resource locator</i> as the only argument and the program will download that file. You can then copy and paste from your web browser or newsreader and use that URL. Example:</p>
<dl>
<dt>
<dd>
<p> $ cd /tmp<br />
 $ ncftpget <a href="ftp://ftp.ncftp.com/pub/ncftp/ncftp.tar.Z">ftp://ftp.ncftp.com/pub/ncftp/ncftp.tar.Z</a><br />
 $ zcat nc<a href="ftp://ftp.tar.Z">ftp.tar.Z</a> | tar xf &#8211;
</dl>
<p> By default the program tries to open the remote host and login anonymously, but you can specify a username and password information. The <code>-u</code> option is used to specify the username to login as, and the <code>-p</code> option is used to specify the password. If you are running the program from the shell, you may omit the <code>-p</code> option and the program will prompt you for the password. </p>
<p> Using the <code>-u</code> and <code>-p</code> options are not recommended, because your account information is exposed to anyone who can see your shell script or your process information. For example, someone using the <i>ps</i> program could see your password while the program runs. </p>
<p> You may use the <code>-f</code> option instead to specify a file with the account information. However, this is still not secure because anyone who has read access to the information file can see the account information. Nevertheless, if you choose to use the <code>-f</code> option the file should look something like this:</p>
<dl>
<dt>
<dd>
<p> host sphygmomanometer.nc<a href="ftp://ftp.com">ftp.com</a><br />
 user gleason<br />
 pass mypasswd </p>
</dl>
<p> Don&#8217;t forget to change the permissions on this file so no one else can read them. </p>
<p> The <code>-d</code> option is very useful when you are trying to diagnose why a file transfer is failing. It prints out the entire FTP conversation to the file you specify, so you can get an idea of what went wrong. If you specify the special name <i>stdout</i> as the name of the debugging output file, the output will instead print to the screen. Example:</p>
<dl>
<dt>
<dd>
<p> $ ncftpget -d stdout bowser.nintendo.co.jp . /pub/README<br />
 220: FTP server ready.<br />
 Connected to bowser.nintendo.co.jp.<br />
 Cmd: USER anonymous<br />
 331: Guest login ok, send your complete e-mail address as password.<br />
 Cmd: PASS xxxxxxxx<br />
 230: Welcome!<br />
 Logged in to bowser.nintendo.co.jp as anonymous.<br />
 Cmd: TYPE I<br />
 200: Type set to I.<br />
 Cmd: PORT 192,168,9,37,6,76<br />
 200: PORT command successful.<br />
 Cmd: RETR /pub/README<br />
 550: /pub/README: File in use.<br />
 Cmd: QUIT<br />
 221: Goodbye.
</dl>
<p> Using ASCII mode is helpful when the text format of your host differs from that of the remote host. For example, if you are retrieving a .TXT file from a Windows-based host to a UNIX system, you could use the <code>-a</code> flag which would use ASCII transfer mode so that the file created on the UNIX system would be in the UNIX text format instead of the MS-DOS text format. </p>
<p> You can retrieve an entire directory tree of files by using the <code>-R</code> flag. However, this will work only if the remote FTP server is a UNIX server, or emulates UNIX&#8217;s list output. Example:</p>
<dl>
<dt>
<dd>
<p> $ ncftpget -R <a href="ftp://ftp.ncftp.com">ftp.ncftp.com</a> /tmp /pub/ncftp </p>
</dl>
<p> This would create a /tmp/ncftp hierarchy.</p>
<h2>DIAGNOSTICS</h2>
<p> <i>ncftpget</i> returns the following exit values:</p>
<dl>
<dt>0</p>
<dd> Success.</p>
<dt>1</p>
<dd> Could not connect to remote host.</p>
<dt>2</p>
<dd> Could not connect to remote host &#8211; timed out.</p>
<dt>3</p>
<dd> Transfer failed.</p>
<dt>4</p>
<dd> Transfer failed &#8211; timed out.</p>
<dt>5</p>
<dd> Directory change failed.</p>
<dt>6</p>
<dd> Directory change failed &#8211; timed out.</p>
<dt>7</p>
<dd> Malformed URL.</p>
<dt>8</p>
<dd> Usage error.</p>
<dt>9</p>
<dd> Error in login configuration file.</p>
<dt>10</p>
<dd> Library initialization failed.</p>
<dt>11</p>
<dd> Session initialization failed.</dl>
<h2>AUTHOR</h2>
<p> Mike Gleason, NcFTP Software (<a rel="nofollow" href="http://www.ncftp.com">http://www.ncftp.com</a>).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ncftpput/">ncftpput</a></i>(1), <i><a href="/docs/linux/man/1-ncftp/">ncftp</a></i>(1), <i><a href="/docs/linux/man/1-ftp/">ftp</a></i>(1), <i><a href="/docs/linux/man/1-rcp/">rcp</a></i>(1), <i><a href="/docs/linux/man/1-tftp/">tftp</a></i>(1). </p>
<p> <i>LibNcFTP</i> (<a rel="nofollow" href="http://www.ncftp.com/libncftp/">http://www.ncftp.com/libncftp/</a>). </p>
<h2>Index</h2>
