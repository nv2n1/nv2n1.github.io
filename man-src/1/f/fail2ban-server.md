---
title: "fail2ban-server(1)"
name: "fail2ban-server"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fail2ban-server/"
description: "fail2ban-server – start the server"
---

<h2>NAME</h2>
<p> fail2ban-server &#8211; start the server</p>
<h2>SYNOPSIS</h2>
<p> <code>fail2ban-server</code> [<i>,OPTIONS/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Fail2Ban v0.9.6 reads log file that contains password failure report and bans the corresponding IP addresses using firewall rules. </p>
<p> Only use this command for debugging purpose. Start the server with fail2ban-client instead. The default behaviour is to start the server in background.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> start in background</dd>
<dt><code>-f</code></dt>
<dd> start in foreground</dd>
<dt><code>-s</code> &lt;FILE&gt;</dt>
<dd> socket path</dd>
<dt><code>-p</code> &lt;FILE&gt;</dt>
<dd> pidfile path</dd>
<dt><code>-x</code></dt>
<dd> force execution of the server (remove socket file)</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print the version</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Cyril Jaquier &lt;cyril.jaquier [at] fail2ban.org&gt;. Many contributions by Yaroslav O. Halchenko &lt;debian [at] onerussian.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/fail2ban/fail2ban/issues">https://github.com/fail2ban/fail2ban/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2008 Cyril Jaquier, 2008- Fail2Ban Contributors<br />
 Copyright of modifications held by their respective authors. Licensed under the GNU General Public License v2 (GPL).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fail2ban-client/">fail2ban-client</a>(1) </p>
<h2>Index</h2>
