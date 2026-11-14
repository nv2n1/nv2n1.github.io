---
title: "service(8)"
name: "service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-service/"
description: "service – run a System V init script"
---

<p>service &#8211; run a System V init script</p>
<h2>Synopsis</h2>
<p><code>service</code> <i>SCRIPT</i> <i>COMMAND</i> [<i>OPTIONS</i>] </p>
<p> <code>service</code> <code>&#8211;status-all</code> </p>
<p> <code>service</code> <code>&#8211;help</code> | <code>-h</code> | <code>&#8211;version</code></p>
<h2>Description</h2>
<p><code>service</code> runs a System V init script or systemd unit in as predictable an environment as possible, removing most environment variables and with the current working directory set to <code>/</code>. </p>
<p> The <i>SCRIPT</i> parameter specifies a System V init script, located in <i>/etc/init.d/SCRIPT</i>, or the name of a systemd unit. The existence of a systemd unit of the same name as a script in <code>/etc/init.d</code> will cause the unit to take precedence over the init.d script. The supported values of <i>COMMAND</i> depend on the invoked script. <code>service</code> passes <i>COMMAND</i> and <i>OPTIONS</i> to the init script unmodified. For systemd units, start, stop, status, and reload are passed through to their systemctl/initctl equivalents. </p>
<p> All scripts should support at least the <code>start</code> and <code>stop</code> commands. As a special case, if <i>COMMAND</i> is <code>&#8211;full-restart</code>, the script is run twice, first with the <code>stop</code> command, then with the <code>start</code> command. Note, that unlike <code><a href="/docs/linux/man/8-update-rc-d/">update-rc.d</a></code>(8), <code>service</code> does not check <code>/usr/sbin/policy-rc.d</code>. </p>
<p> <code>service &#8211;status-all</code> runs all init scripts, in alphabetical order, with the <code>status</code> command. The status is [ + ] for running services, [ &#8211; ] for stopped services and [ ? ] for services without a <code>status</code> command. This option only calls status for sysvinit jobs.</p>
<h2>Exit Codes</h2>
<p><code>service</code> calls the init script and returns the status returned by it.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/init.d</code></p>
<dd>The directory containing System V init scripts.</p>
<dt><code>/{lib,run,etc}/systemd/system</code></p>
<dd>The directories containing systemd units.</dl>
<h2>Environment</h2>
<dl>
<dt><code>LANG</code>, <code>LANGUAGE</code>, <code>LC_CTYPE</code>, <code>LC_NUMERIC</code>, <code>LC_TIME</code>, <code>LC_COLLATE</code>, <code>LC_MONETARY</code>, <code>LC_MESSAGES</code>, <code>LC_PAPER</code>, <code>LC_NAME</code>, <code>LC_ADDRESS</code>, <code>LC_TELEPHONE</code>, <code>LC_MEASUREMENT</code>, <code>LC_IDENTIFICATION</code>, <code>LC_ALL</code>, <code>TERM</code>, <code>PATH</code></p>
<dd>The only environment variables passed to the init scripts.</dl>
<h2>See Also</h2>
<pre><i>/etc/init.d/skeleton</i>
<code><a href="//www.systutorials.com/docs/linux/man/8-update-rc.d/">update-rc.d</a></code>(8)
<code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a></code>(8)
<code><a href="//www.systutorials.com/docs/linux/man/8-invoke-rc.d/">invoke-rc.d</a></code>(8)
<code><a href="//www.systutorials.com/docs/linux/man/1-systemctl/">systemctl</a></code>(1)</pre>
<h2>Author</h2>
<p>Miloslav Trmac &lt;mitr [at] redhat.com&gt;, Petter Reinholdtsen &lt;pere [at] hungry.com&gt; </p>
<p> License: GNU General Public License v2 (GPLv2)</p>
<h2>Copyright</h2>
<p>2006 Red Hat, Inc., Petter Reinholdtsen &lt;pere [at] hungry.com&gt;</p>
