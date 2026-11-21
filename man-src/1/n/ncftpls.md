---

title: "ncftpls(1)"
name: "ncftpls"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftpls/"
description: "ncftpls – Internet file transfer program for scripts"
---

<p> ncftpls &#8211; Internet file transfer program for scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>ncftpls</code> [<i>options</i>] <i><a href="ftp://url.style/host/path/name/">ftp://url.style/host/path/name/</a></i></p>
<h2>OPTIONS</h2>
<h3>Command line flags:</h3>
<dl>
<dt><code>-m</code></dt>
<dd> Use a machine readable list format, if the server supports it. This requires that the server software support the MLSD extensions, and many implementations do not have these features.</dd>
<dt><code>-1</code></dt>
<dd> Most basic format, one item per line.</dd>
<dt><code>-l</code></dt>
<dd> Long list format.</dd>
<dt><code>-C</code></dt>
<dd> Columnized list format. This is the default list format.</dd>
<dt><code>-R</code></dt>
<dd> Recurse all subdirectories while listing.</dd>
<dt><code>-a</code></dt>
<dd> Show all files, if server allows it (as in &quot;/bin/ls -a&quot;).</dd>
<dt><code>-i </code><i>XX</i></dt>
<dd> Filter the listing (if server supports it) with the wildcard <i>XX</i>.</dd>
<dt><code>-x &#8211;</code><i>XX</i></dt>
<dd> Set the <i>ls</i> flags to use on the server.</dd>
<dt><code>-u </code><i>XX</i></dt>
<dd> Use username <i>XX</i> instead of anonymous.</dd>
<dt><code>-p </code><i>XX</i></dt>
<dd> Use password <i>XX</i> with the username.</dd>
<dt><code>-P </code><i>XX</i></dt>
<dd> Use port number <i>XX</i> instead of the default FTP service port (21).</dd>
<dt><code>-d </code><i>XX</i></dt>
<dd> Use the file <i>XX</i> for debug logging.</dd>
<dt><code>-t </code><i>XX</i></dt>
<dd> Timeout after <i>XX</i> seconds.</dd>
<dt><code>-E</code></dt>
<dd> Use regular (PORT) data connections.</dd>
<dt><code>-F</code></dt>
<dd> Use passive (PASV) data connections. The default is to use passive, but to fallback to regular if the passive connection fails or times out.</dd>
<dt><code>-r </code><i>XX</i></dt>
<dd> Redial a maximum of <i>XX</i> times until connected to the remote FTP server.</dd>
<dt><code>-W </code><i>XX</i></dt>
<dd> Send raw FTP command <i>XX</i> after logging in.</dd>
<dt><code>-X </code><i>XX</i></dt>
<dd> Send raw FTP command <i>XX</i> after each file transferred.</dd>
<dt><code>-Y </code><i>XX</i></dt>
<dd> Send raw FTP command <i>XX</i> before logging out.</dd>
<dt>
</dt><dd> The <code>-W</code>, <code>-X</code>, and <code>-Y</code> options are useful for advanced users who need to tweak behavior on some servers. For example, users accessing mainframes might need to send some special SITE commands to set blocksize and record format information.</dd>
<dt>
</dt><dd> For these options, you can use them multiple times each if you need to send multiple commands. For the <code>-X</code> option, you can use the cookie <code>%s</code> to expand into the name of the file that was transferred.</dd>
<dt><code>-o </code><i>XX</i></dt>
<dd> Set advanced option <i>XX</i>.</dd>
<dt>
</dt><dd> This option is used primarily for debugging. It sets the value of an internal variable to an integer value. An example usage would be: <code>-o </code><i>useFEAT=0,useCLNT=1</i> which in this case, disables use of the FEAT command and enables the CLNT command. The available variables include: usePASV, useSIZE, useMDTM, useREST, useNLST_a, useNLST_d, useFEAT, useMLSD, useMLST, useCLNT, useHELP_SITE, useSITE_UTIME, STATfileParamWorks, NLSTfileParamWorks, require20, allowProxyForPORT, doNotGetStartCWD.</dd></dl>
<h2>DESCRIPTION</h2>
<p> The purpose of <i>ncftpls</i> is to do remote directory listings using the File Transfer Protocol without entering an interactive shell. This lets you write shell scripts or other unattended processes that can do FTP. </p>
<p> The default behavior is to print the directory listing in columnized format (i.e. ls -CF), but that is not very useful for scripting. This example uses the <code>-1</code> flag, to print one file per line:</p>
<dl>
<dt>
</dt><dd>
<p> $ ncftpls -1 <a href="ftp://ftp.ncftp.com/pub/ncftp/">ftp://ftp.ncftp.com/pub/ncftp/</a></dd></dl>
<p> You can also do a remote &quot;ls -l&quot;, by using &quot;ncftpls -l&quot;. If you want to try other flags, you have to use them with the <code>-x</code> flag. For example, if you wanted to do a remote &quot;ls -lrt&quot;, you could do this:</p>
<dl>
<dt>
</dt><dd>
<p> $ ncftpls -x &quot;-lrt&quot; <a href="ftp://ftp.ncftp.com/pub/ncftp/">ftp://ftp.ncftp.com/pub/ncftp/</a></dd></dl>
<p> By default the program tries to open the remote host and login anonymously, but you can specify a username and password information like you can with <i>ncftpget</i> or <i>ncftpput</i>. </p>
<p> Note that the standard specifies that URL pathnames are are relative pathnames. For FTP, this means that URLs specify relative pathnames from the start directory, which for user logins, are typically the user&#8217;s home directory. If you want to use absolute pathnames, you need to include a literal slash, using the &quot;%2F&quot; code for a &quot;/&quot; character. Examples:</p>
<dl>
<dt>
</dt><dd>
<p> $ ncftpls -u linus <a href="ftp://ftp.kernel.org/%2Fusr/src/">ftp://ftp.kernel.org/%2Fusr/src/</a><br />
 $ ncftpls <a href="ftp://steve@ftp.apple.com/%2Fetc/">ftp://steve@ftp.apple.com/%2Fetc/</a></dd></dl>
<h2>DIAGNOSTICS</h2>
<p> <i>ncftpls</i> returns the following exit values:</p>
<dl>
<dt>0</dt>
<dd> Success.</dd>
<dt>1</dt>
<dd> Could not connect to remote host.</dd>
<dt>2</dt>
<dd> Could not connect to remote host &#8211; timed out.</dd>
<dt>3</dt>
<dd> Transfer failed.</dd>
<dt>4</dt>
<dd> Transfer failed &#8211; timed out.</dd>
<dt>5</dt>
<dd> Directory change failed.</dd>
<dt>6</dt>
<dd> Directory change failed &#8211; timed out.</dd>
<dt>7</dt>
<dd> Malformed URL.</dd>
<dt>8</dt>
<dd> Usage error.</dd>
<dt>9</dt>
<dd> Error in login configuration file.</dd>
<dt>10</dt>
<dd> Library initialization failed.</dd>
<dt>11</dt>
<dd> Session initialization failed.</dd></dl>
<h2>AUTHOR</h2>
<p> Mike Gleason, NcFTP Software (<a rel="nofollow" href="http://www.ncftp.com">http://www.ncftp.com</a>).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ncftpput/">ncftpput</a></i>(1), <i><a href="/docs/linux/man/1-ncftpget/">ncftpget</a>(1),</i> <i><a href="/docs/linux/man/1-ncftp/">ncftp</a></i>(1), <i><a href="/docs/linux/man/1-ftp/">ftp</a></i>(1), <i><a href="/docs/linux/man/1-rcp/">rcp</a></i>(1), <i><a href="/docs/linux/man/1-tftp/">tftp</a></i>(1). </p>
<p> <i>LibNcFTP</i> (<a rel="nofollow" href="http://www.ncftp.com/libncftp/">http://www.ncftp.com/libncftp/</a>). </p>
