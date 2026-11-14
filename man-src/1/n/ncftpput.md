---
title: "ncftpput(1)"
name: "ncftpput"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftpput/"
description: "ncftpput – Internet file transfer program for scripts"
---

<h2>NAME</h2>
<p> ncftpput &#8211; Internet file transfer program for scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>ncftpput</code> [<i>options</i>] <i>remote-host remote-directory local-files&#8230;</i> </p>
<p> <code>ncftpput</code> [<i>options</i>] <i>bookmark-name remote-directory local-files&#8230;</i> </p>
<p> <code>ncftpput</code> -f <i>login.cfg</i> [<i>options</i>] <i>remote-directory local-files&#8230;</i> </p>
<p> <code>ncftpput</code> -c <i>remote-host remote-path-name</i> &lt; <i>stdin</i> </p>
<p> <code>ncftpput</code> -C <i>remote-host local-path-name remote-path-name</i></p>
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
<dt><code>-m</code></p>
<dd> Attempt to make the remote destination directory before copying.</p>
<dt><code>-t </code><i>XX</i></p>
<dd> Timeout after <i>XX</i> seconds.</p>
<dt><code>-U </code><i>XX</i></p>
<dd> Use value <i>XX</i> for the umask.</p>
<dt><code>-v</code>/<code>-V</code></p>
<dd> Do (do not) use progress meters. The default is to use progress meters if the output stream is a TTY.</p>
<dt><code>-f </code><i>XX</i></p>
<dd> Read the file <i>XX</i> for host, user, and password information.</p>
<dt><code>-c</code></p>
<dd> Read locally from standard input and write remotely to specified pathname.</p>
<dt><code>-C</code></p>
<dd> Similar to <code>-c</code>, except a local pathname is specified.</p>
<dt><code>-A</code></p>
<dd> Append to remote files, instead of overwriting them.</p>
<dt><code>-T </code><i>XX</i></p>
<dd> Upload into temporary files prefixed by <i>XX</i>.</p>
<dt><code>-S </code><i>XX</i></p>
<dd> Upload into temporary files suffixed by <i>XX</i>.</p>
<dt><code>-R</code></p>
<dd> Recursive mode; copy whole directory trees.</p>
<dt><code>-r </code><i>XX</i></p>
<dd> Redial a maximum of <i>XX</i> times until connected to the remote FTP server.</p>
<dt><code>-z</code>/<code>-Z</code></p>
<dd> Do (do not) try to resume transfers. The default is to <i>not</i> try to resume (-Z).</p>
<dt><code>-E</code></p>
<dd> Use regular (PORT) data connections.</p>
<dt><code>-F</code></p>
<dd> Use passive (PASV) data connections. The default is to use passive, but to fallback to regular if the passive connection fails or times out.</p>
<dt><code>-DD</code></p>
<dd> Delete local file after successfully uploading it.</p>
<dt><code>-y</code></p>
<dd> Try using &quot;SITE UTIME&quot; to preserve timestamps on remote host. Not many remote FTP servers support this, so it may not work.</p>
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
<p> The purpose of <i>ncftpput</i> is to do file transfers from the command-line without entering an interactive shell. This lets you write shell scripts or other unattended processes that can do FTP. It is also useful for advanced users who want to send files from the shell command line without entering an interactive FTP program such as <i>ncftp</i>. </p>
<p> By default the program tries to open the remote host and login anonymously, but you can specify a username and password information. The <code>-u</code> option is used to specify the username to login as, and the <code>-p</code> option is used to specify the password. If you are running the program from the shell, you may omit the <code>-p</code> option and the program will prompt you for the password. </p>
<p> Using the <code>-u</code> and <code>-p</code> options are not recommended, because your account information is exposed to anyone who can see your shell script or your process information. For example, someone using the <i>ps</i> program could see your password while the program runs. </p>
<p> You may use the <code>-f</code> option instead to specify a file with the account information. However, this is still not secure because anyone who has read access to the information file can see the account information. Nevertheless, if you choose to use the <code>-f</code> option the file should look something like this:</p>
<dl>
<dt>
<dd>
<p> host sphygmomanometer.nc<a href="ftp://ftp.com">ftp.com</a><br />
 user gleason<br />
 pass mypassword </p>
</dl>
<p> Don&#8217;t forget to change the permissions on this file so no one else can read them. </p>
<p> The <code>-d</code> option is very useful when you are trying to diagnose why a file transfer is failing. It prints out the entire FTP conversation to the file you specify, so you can get an idea of what went wrong. If you specify the special name <i>stdout</i> as the name of the debugging output file, the output will instead print to the screen. </p>
<p> Using ASCII mode is helpful when the text format of your host differs from that of the remote host. For example, if you are sending a text file from a UNIX system to a Windows-based host, you could use the <code>-a</code> flag which would use ASCII transfer mode so that the file created on the Windows machine would be in its native text format instead of the UNIX text format. </p>
<p> You can upload an entire directory tree of files by using the <code>-R</code> flag. Example:</p>
<dl>
<dt>
<dd>
<p> $ ncftpput -R pikachu.nintendo.co.jp /incoming /tmp/stuff </p>
</dl>
<p> This would create a /incoming/stuff hierarchy on the remote host. </p>
<p> The <code>-T</code> and <code>-S</code> options are useful when you want to upload file to the remote host, but you don&#8217;t want to use the destination pathname until the file is complete. Using these options, you will not destroy a remote file by the same name until your file is finished. These options are also useful when a remote process on the remote host polls a specific filename, and you don&#8217;t want that process to see that file until you know the file is finished sending. Here is an example that uploads to the file /pub/incoming/README, using the filename /pub/incoming/README.tmp as a temporary filename:</p>
<dl>
<dt>
<dd>
<p> $ ncftpput -S .tmp bowser.nintendo.co.jp /pub/incoming /a/README</dl>
<p> A neat way to pipe the output from any local command into a remote file is to use the <code>-c</code> option, which denotes that you&#8217;re using <i>stdin</i> as input. The following example shows how to make a backup and store it on a remote machine:</p>
<dl>
<dt>
<dd>
<p> $ tar cf &#8211; / | ncftpput -c sonic.sega.co.jp /usr/local/backup.tar</dl>
<h2>DIAGNOSTICS</h2>
<p> <i>ncftpput</i> returns the following exit values:</p>
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
<p> <i><a href="/docs/linux/man/1-ncftpget/">ncftpget</a></i>(1), <i><a href="/docs/linux/man/1-ncftp/">ncftp</a></i>(1), <i><a href="/docs/linux/man/1-ftp/">ftp</a></i>(1), <i><a href="/docs/linux/man/1-rcp/">rcp</a></i>(1), <i><a href="/docs/linux/man/1-tftp/">tftp</a></i>(1). </p>
<p> <i>LibNcFTP</i> (<a rel="nofollow" href="http://www.ncftp.com/libncftp/">http://www.ncftp.com/libncftp/</a>). </p>
<h2>Index</h2>
