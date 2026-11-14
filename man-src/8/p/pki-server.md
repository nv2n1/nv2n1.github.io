---
title: "pki-server(8)"
name: "pki-server"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-server/"
description: "pki-server – Command-Line Interface for performing administrative tasks on Certificate System subsystems."
---

<p>pki-server &#8211; Command-Line Interface for performing administrative tasks on Certificate System subsystems.</p>
<h2>Synopsis</h2>
<p><code>pki-server</code> [CLI options] &lt;command&gt; [command arguments] </p>
<h2>Description</h2>
<p>The <code>pki-server</code> command provides a command-line interface allowing administrators to perform various administrative operations on the Certificate System instances. These services include starting/stopping instances, enabling/disabling subsystems, performing certain migrations and enabling/disabling startup using <code>nuxwdog</code>. Operations are performed using file system utilities, and can only be performed by an administrative user on the local host. This utility does not connect to any of the subsystem&#8217;s WEB or REST interfaces. </p>
<h2>Cli Options</h2>
<p><code>&#8211;help</code> Prints additional help information.</p>
<dl>
<dt><code>-d</code></p>
<dd>Displays debug information.</p>
<dt><code>-v</code></p>
<dd>Displays verbose information. </p>
</dl>
<h2>Operations</h2>
<p>To view available commands and options, simply type <code>pki-server</code>. </p>
<p> Some commands have sub-commands. To view the sub-commands, type <code>pki-server &lt;command&gt;</code>. To view each command&#8217;s usage, type <code> pki-server &lt;command&gt; &#8211;help</code>.</p>
<h2>Files</h2>
<p><i>/usr/sbin/pki-server</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki-server-instance/">pki-server-instance</a></code>(1)</p>
<dl>
<dd>Certificate Server instance management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-server-subsystem/">pki-server-subsystem</a></code>(1)</p>
<dl>
<dd>Certificate Server subsystem management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-server-migrate/">pki-server-migrate</a></code>(1)</p>
<dl>
<dd>Certificate server migration script management commands</dl>
<p> <code><a href="/docs/linux/man/1-pki-server-nuxwdog/">pki-server-nuxwdog</a></code>(1)</p>
<dl>
<dd>Commands to enable/disable startup using <code>nuxwdog</code>.</dl>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
