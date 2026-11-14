---
title: "pki-server-nuxwdog(8)"
name: "pki-server-nuxwdog"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-server-nuxwdog/"
description: "pki-server-nuxwdog – Command-Line Interface for enabling CS instances to start using nuxwdog."
---

<p>pki-server-nuxwdog &#8211; Command-Line Interface for enabling CS instances to start using <code>nuxwdog</code>.</p>
<h2>Synopsis</h2>
<pre><code>pki-server [CLI options] nuxwdog</code>
<code>pki-server [CLI options] nuxwdog-enable</code>
<code>pki-server [CLI options] nuxwdog-disable</code></pre>
<h2>Description</h2>
<p>When a Certificate System (CS) instance starts, it reads a plain text configuration file (<code> /etc/pki/&lt;instance_name&gt;/password.conf</code>) to obtain passwords needed to initialize the server. This could include passwords needed to access server keys in hardware or software cryptographic modules, or passwords to establish database connections. While this file is protected by file and SELinux permissions, it is even more secure to remove this file entirely, and have the server prompt for these passwords on startup. This means of course that it will not be possible to start the CS instance unattended, including on server reboots. <code>nuxwdog</code> is a daemon that will launch the CS instance and prompt the administrator for the relevant passwords. These passwords will be cached securely in the kernel keyring. If the CS instance crashes unexpectedly, <code>nuxwdog</code> will attempt to restart the instance using the cached passwords. CS instances need to be reconfigured to use <code>nuxwdog</code> to start. Not only are changes required in instance configuration files, but instances need to use a different systemd unit file to start. See details in the <code>Operations</code> section. <code>pki-server nuxwdog</code> commands provide a mechanism to reconfigure instances to either start or not start with <code>nuxwdog</code>. <code>pki-server [CLI options] nuxwdog</code></p>
<dl>
<dd>This command is to list available <code>nuxwdog</code> commands.</dl>
<p> <code>pki-server [CLI options] nuxwdog-enable</code></p>
<dl>
<dd>This command is to reconfigure ALL local CS instances to start using <code>nuxwdog</code>. To reconfigure a particular CS instance only, use <code>pki-server instance-nuxwdog-enable</code>.</dl>
<p> <code>pki-server [CLI options] nuxwdog-disable</code></p>
<dl>
<dd>This command is to reconfigure ALL local CS instances to start without using <code>nuxwdog</code>. To reconfigure a particular CS instance only, use <code>pki-server instance-nuxwdog-disable</code>. Once this operation is complete, instances will need to read a <code>password.conf</code> file in order to start up.</dl>
<h2>Options</h2>
<p>The CLI options are described in <code><a href="/docs/linux/man/8-pki-server/">pki-server</a></code>(8).</p>
<h2>Operations</h2>
<p>Configuring a CS instance to start using <code>nuxwdog</code> requires changes to instance configuration files such as <code>server.xml</code>. These changes are performed by <code>pki-server</code>. </p>
<p> Once a subsystem has been converted to using <code>nuxwdog</code>, the <code>password.conf</code> file is no longer needed. It can be removed from the filesystem. Be sure, of course, to note all passwords contained therein &#8211; some of which may be randomly generated during the install. </p>
<p> An instance that is started by <code>nuxwdog</code> is started by a different systemd unit file (<code>pki-tomcatd-nuxwdog</code>). Therefore, to start/stop/restart an instance using the following: </p>
<p> <code>systemctl start/stop/restart pki-tomcatd-nuxwdog@&lt;instance_id&gt;.service</code> </p>
<p> If the CS instance is converted back to not using <code>nuxwdog</code> to start, then the usual systemd unit scripts can be invoked: </p>
<p> <code>systemctl start/stop/restart pki-tomcatd@&lt;instance_id&gt;.service</code> </p>
<p> All <code>pki-server</code> commands must be executed as the system administrator.</p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
