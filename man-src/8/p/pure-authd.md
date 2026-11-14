---
title: "pure-authd(8)"
name: "pure-authd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-authd/"
description: "pure-authd – External authentication agent for Pure-FTPd."
---

<p>pure-authd &#8211; External authentication agent for Pure-FTPd.</p>
<h2>Syntax</h2>
<p>pure-authd [<i>-p</i> &lt;<i>/path/to/pidfile</i>&gt;] [<i>-u</i> uid] [<i>-g</i> gid] [<i>-B</i>] &lt;<i>-s</i> /path/to/socket&gt; <i>-r</i> /program/to/run</p>
<h2>Description</h2>
<p>pure-authd is a daemon that forks an authentication program, waits for an authentication reply, and feed them to an application server. </p>
<p> pure-authd listens to a local Unix socket. A new connection to that socket should feed pure-authd the following structure :</p>
<dl>
<dd>account:xxx </p>
<p> password:xxx </p>
<p> localhost:xxx </p>
<p> localport:xxx </p>
<p> peer:xxx </p>
<p> end</dl>
<p> (replace xxx with appropriate values) . localhost, localport and peer are numeric IP addresses and ports. peer is the IP address of the remote client. </p>
<p> These arguments are passed to the authentication program, as environment variables :</p>
<dl>
<dd>AUTHD_ACCOUNT </p>
<p> AUTHD_PASSWORD </p>
<p> AUTHD_LOCAL_IP </p>
<p> AUTHD_LOCAL_PORT </p>
<p> AUTHD_REMOTE_IP </p>
<p> AUTHD_ENCRYPTED</dl>
<p> The authentication program should take appropriate actions to fetch account info according to these arguments, and reply to the standard output a structure like the following one :</p>
<dl>
<dd>auth_ok:1 </p>
<p> uid:42 </p>
<p> gid:21 </p>
<p> dir:/home/j </p>
<p> end </p>
<dt><code>auth_ok:</code>xxx</p>
<dd>If xxx is 0, the user was not found (the next authentication method passed to pure-ftpd will be tried) . If xxx is -1, the user was found, but there was a fatal authentication error : user is root, password is wrong, account has expired, etc (next authentication methods will not be tried) . If xxx is 1, the user was found and successfully authenticated.</p>
<dt><code>uid:</code>xxx</p>
<dd>The system uid to be assigned to that user. Must be &gt; 0.</p>
<dt><code>gid:</code>xxx</p>
<dd>The primary system gid. Must be &gt; 0.</p>
<dt><code>dir:</code>xxx</p>
<dd>The absolute path to the home directory. Can contain /./ for a chroot jail.</p>
<dt><code>slow_tilde_expansion:</code>xxx <i>(optional, default is 1)</i></p>
<dd>When the command &#8216;cd ~user&#8217; is issued, it&#8217;s handy to go to that user&#8217;s home directory, as expected in a shell environment. But fetching account info can be an expensive operation for non-system accounts. If xxx is 0, &#8216;cd ~user&#8217; will expand to the system user home directory. If xxx is 1, &#8216;cd ~user&#8217; won&#8217;t expand. You should use 1 in most cases with external authentication, when your FTP users don&#8217;t match system users. You can also set xxx to 1 if you&#8217;re using slow nss_* system authentication modules.</p>
<dt><code>throttling_bandwidth_ul:</code>xxx <i>(optional)</i></p>
<dd>The allocated bandwidth for uploads, in bytes per second.</p>
<dt><code>throttling_bandwidth_dl:</code>xxx <i>(optional)</i></p>
<dd>The allocated bandwidth for downloads, in bytes per second.</p>
<dt><code>user_quota_size:</code>xxx <i>(optional)</i></p>
<dd>The maximal total size for this account, in bytes.</p>
<dt><code>user_quota_files:</code>xxx <i>(optional)</i></p>
<dd>The maximal number of files for this account.</p>
<dt><code>ratio_upload:</code>xxx <i>(optional)</i></p>
<dd>
<dt><code>radio_download:</code>xxx <i>(optional)</i></p>
<dd>The user must match a ratio_upload:ratio_download ratio.</dl>
<p> <i>Only one authentication program is forked at a time. It must return quickly.</i></p>
<h2>Options</h2>
<dl>
<dt><code>-u</code> &lt;<i>uid</i>&gt;</p>
<dd>Have the daemon run with that uid.</p>
<dt><code>-g</code> &lt;<i>gid</i>&gt;</p>
<dd>Have the daemon run with that gid.</p>
<dt><code>-B</code></p>
<dd>Fork in background (daemonization).</p>
<dt><code>-s</code> &lt;<i>/path/to/socket</i>&gt;</p>
<dd>Set the full path to the local Unix socket.</p>
<dt><code>-R</code> &lt;<i>/path/to/program</i>&gt;</p>
<dd>Set the full path to the authentication program.</p>
<dt><code>-h</code></p>
<dd>Output help information and exit.</dl>
<h2>Examples</h2>
<p>To run this program the standard way type: </p>
<p> pure-authd -s /var/run/ftpd.sock -r /usr/bin/my-auth-program &amp; </p>
<p> pure-ftpd -lextauth:/var/run/ftpd.sock &amp;</p>
<dl>
<dt>/usr/bin/my-auth-program can be as simple as :</p>
<dd>#! /bin/sh </p>
<p> echo &#8216;auth_ok:1&#8217; </p>
<p> echo &#8216;uid:42&#8217; </p>
<p> echo &#8216;gid:21&#8217; </p>
<p> echo &#8216;dir:/home/j&#8217; </p>
<p> echo &#8216;end&#8217;</dl>
<h2>Authors</h2>
<p>Frank DENIS &lt;j at pureftpd dot org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959,</code> <code>RFC 2389,</code> <code>RFC 2228</code> and <code>RFC 2428.</code> </p>
