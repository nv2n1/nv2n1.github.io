---
title: "rexec(1)"
name: "rexec"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rexec/"
description: "rexec — remote execution client for an exec server"
---

<h2>NAME</h2>
<p> rexec &#8212; remote execution client for an exec server</p>
<h2>SYNOPSIS</h2>
<p> <code>rexec </code> [ <code>-abcdhns -l </code> username <code>-p </code> password ] host command</p>
<h2>DESCRIPTION</h2>
<p> <code>Rexec</code> calls the <code><a href="/docs/linux/man/3-rexec/">rexec</a>(3)</code> routine to act as a client for the remote host&#8217;s <code><a href="/docs/linux/man/8-rexecd/">rexecd</a>(8)</code> server. </p>
<p> It asks that &#8220;command&#8221; be run on the host computer, using username/password authentication. See <code><a href="/docs/linux/man/3-rexec/">rexec</a>(3)</code> and <code><a href="/docs/linux/man/8-rexecd/">rexecd</a>(8)</code> for details of the protocol.</p>
<h2>OPTIONS</h2>
<p> <code>Rexec</code> accepts several options, but only three are likely to be very useful: </p>
<p> <code>-l username</code></p>
<dl>
<dt>
<dd> Set the log-in name on the remote host to username.</dl>
<p> <code>-p password</code></p>
<dl>
<dt>
<dd> Provide the password for the remote account. The command line argument will be blanked after being parsed, to prevent it from being seen with <code><a href="/docs/linux/man/1-ps/">ps</a>(1).</code> However, it is still not very secure to type the password on the command line. In particular, be sure that the shell&#8217;s history file is protected.</p>
<dt><code>-n</code></p>
<dd> Explicitly prompt for name and password, even if provided in the environment, in the $HOME/.netrc file, or in the environmental variables REXEC_USER and REXEC_PASS.</dl>
<p> Other options that might be useful with non-standard remote exec daemons, or to debug connections:</p>
<dl>
<dt><code>-a</code></p>
<dd> Do not set up an auxiliary channel for standard error from command; the remote standard error and output are then both returned on the local standard output. By default, <code>rexec</code> asks that a separate channel be set up for diagnostic output from the remote command.</p>
<dt><code>-b</code></p>
<dd> Use signal handling as in BSD <a href="/docs/linux/man/1-rsh/">rsh</a>(1). Only the signals SIGINT, SIGQUIT, and SIGTERM are echoed to the remote process. They do not remain raised locally, so rexec waits for the remote command to shutdown its side of the socket. Also, CNTRL-Z will only suspend execution locally&#8211;the remote command may continue to run.</p>
<dt><code>-c</code></p>
<dd> Do not close remote standard input when local standard input closes. Normally the standard input to the remote command is closed when the local standard input is closed.</p>
<dt><code>-d</code></p>
<dd> Turn on debugging information. In particular the command sent to the remote host will be echoed.</p>
<dt><code>-h</code></p>
<dd> Print a usage message.</p>
<dt><code>-s</code></p>
<dd> Do not echo signals received by the rexec onto the remote process. Normally, signals which can be trapped are passed on to the remote process; then, when you type CNTRL-C, the remote process terminates as well.</dl>
<h2>USERNAME AND PASSWORD</h2>
<p> <code><a href="/docs/linux/man/1-rexec/">Rexec</a>(1)</code> searches for the username and password in the following order:</p>
<dl>
<dt>
<dd> 1. If -n is given on the command line, the user will always be prompted for both, even if they are also given on the command line.</p>
<dt>
<dd> 2. The command line will be parsed</p>
<dt>
<dd> 3. If the environmental variables REXEC_USER or REXEC_PASS are defined, they will define the username or password.</p>
<dt>
<dd> 4. The $HOME/.netrc file will be searched. See <code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code> for a description of this file&#8217;s format.</p>
<dt>
<dd> 5. Finally, the user will be prompted if either the username or password remains undefined. </p>
</dl>
<h2>SECURITY</h2>
<p> Users of this command should be aware that <code><a href="/docs/linux/man/3-rexec/">rexec</a>(3)</code> transmits their password to the remote host clear text, not encrypted. If the network is not secure to the remote host, the password can be comprimised. </p>
<h2>SIGNALS</h2>
<p> Without the -b option, all signals which can be handled are echoed to the remote process. Afterwards, however, they remain raised in the local process. Typically, this means that <code><a href="/docs/linux/man/1-rexec/">rexec</a>(1)</code> will exit after receiving a fatal signal, even if the remote process has arranged to handle or ignore it. </p>
<p> Differing operating systems use differing signal numbers; for example AIX and SunOS use 18 for SIGTSTP (^Z), while Linux uses 20. Therefore, it may have a different effect remotely than locally. In particular, typing CNTL-Z may not suspend the execution of the remote process.</p>
<h2>EXAMPLE</h2>
<p> rexec othermachine cat &quot;&gt;remote_file; date&quot; &lt;local_file </p>
<p> will send local_file to the othermachine as remote_file. </p>
<h2>BUGS</h2>
<p> Please send bug reports, system incompatibilities, and job offers to the author.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-rexec/">rexec</a>(3), <a href="/docs/linux/man/8-rexecd/">rexecd</a>(8), <a href="/docs/linux/man/1-rsh/">rsh</a>(1)</p>
<h2>AUTHOR</h2>
<p> Michael Sadd<br />
 mas22 [at] cornell.edu<br />
 <a rel="nofollow" href="http://www.tc.cornell.edu/~sadd/">http://www.tc.cornell.edu/~sadd/</a> </p>
<p> Thanks to Orange Gopher (2/10/97) and Johannes Plass (plass [at] dipmza.physik.uni-mainz.de, Oct. 17 1996) for useful suggestions. </p>
<h2>Index</h2>
