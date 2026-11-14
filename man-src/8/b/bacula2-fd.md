---
title: "bacula2-fd(8)"
name: "bacula2-fd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bacula2-fd/"
description: "bacula-fd – Bacula’s File Daemon"
---

<p><code>bacula-fd</code> &#8211; Bacula&#8217;s File Daemon</p>
<h2>Synopsis</h2>
<p><code>bacula-fd</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bacula</code> command.<br />
 Bacula&#8217;s File Daemon acts as the interface between the Bacula network backup system and the filesystems to be backed up: it is responsible for reading/writing/verifying the files to be backup&#8217;d/verified/restored. Network transfer can optionally be compressed.</p>
<h2>Options</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>config</i></p>
<dd>Change location to read <i>bacula-fd.conf</i> from (default $CWD)</p>
<dt><code>-u&nbsp;<wbr></code><i>user</i></p>
<dd>Set the username/uid to run as.</p>
<dt><code>-g&nbsp;<wbr></code><i>group</i></p>
<dd>Set the group/gid to run as.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bacula-dir/">bacula-dir</a></code>(8), <code><a href="/docs/linux/man/8-bacula-sd/">bacula-sd</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;joseluis [at] DarkCube.adv-solutions.net&gt;.</p>
