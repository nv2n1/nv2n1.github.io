---
title: "ipa-replica-conncheck(1)"
name: "ipa-replica-conncheck"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-replica-conncheck/"
description: "ipa-replica-conncheck – Check a replica-master network connection before installation"
---

<h2>NAME</h2>
<p> ipa-replica-conncheck &#8211; Check a replica-master network connection before installation</p>
<h2>SYNOPSIS</h2>
<p> ipa-replica-conncheck [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> When an IPA replica is being installed a network connection between a replica machine and a replicated IPA master machine has to be prepared for master-replica communication. In case of a flawed connection the installation may fail with inconvenient error messages. A common connection problem is a misconfigured firewall with closed required port on a replica or master machine. </p>
<p> The connection is checked by running a set of tests from both master and replica machines. The program is incorporated to <a href="/docs/linux/man/1-ipa-replica-install/">ipa-replica-install</a>(1) but can be also run separately. </p>
<h2>OPTIONS</h2>
<h3>REPLICA MACHINE OPTIONS</h3>
<p> This set of options is used when the connection check is run on a prepared IPA replica machine.</p>
<dl>
<dt><code>-m</code> <i>MASTER</i>, <code>&#8211;master</code>=<i>MASTER</i></p>
<dd> Remote master machine address</p>
<dt><code>-a</code>, <code>&#8211;auto-master-check</code></p>
<dd> Automatically log in to master machine and execute the master machine part of the connection check. The following options for replica part are only evaluated when this option is set</p>
<dt><code>-r</code> <i>REALM</i>, <code>&#8211;realm</code>=<i>REALM</i></p>
<dd> The Kerberos realm name for the IPA server</p>
<dt><code>-k</code> <i>KDC</i>, <code>&#8211;kdc</code>=<i>KDC</i></p>
<dd> KDC server address. Defaults t <i>MASTER</i></p>
<dt><code>-p</code> <i>PRINCIPAL</i>, <code>&#8211;principal</code>=<i>PRINCIPAL</i></p>
<dd> Authorized Kerberos principal to use to log in to master machine. Defaults to <i>admin</i></p>
<dt><code>-w</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd> Password for given principal. The password will be prompted interactively when this option is missing </p>
</dl>
<h3>MASTER MACHINE OPTIONS</h3>
<p> This set of options is used when the connection check is run on a master machine against a running <a href="/docs/linux/man/1-ipa-replica-conncheck/">ipa-replica-conncheck</a>(1) on a replica machine.</p>
<dl>
<dt><code>-R</code> <i>REPLICA</i>, <code>&#8211;replica</code>=<i>REPLICA</i></p>
<dd> Remote replica machine address </p>
</dl>
<h3>COMMON OPTIONS</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;check-ca</code></p>
<dd> Include in a check also a set of dogtag connection requirements. Only needed when the master was installed with Dogtag 9 or lower.</p>
<dt><code>-h</code> <i>HOSTNAME</i>, <code>&#8211;hostname</code>=<i>HOSTNAME</i></p>
<dd> The hostname of this server (FQDN). By default a nodename from <a href="/docs/linux/man/2-uname/">uname</a>(2) is used</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Output only errors </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ipa-replica-conncheck -m master.example.com</code></p>
<dd> Run a replica machine connection check against a remote master <i>master.example.com</i>. If the connection to the remote master machine is successful the program will switch to listening mode and prompt for running the master machine part. The second part check the connection from master to replica.</p>
<dt><code>ipa-replica-conncheck -R replica.example.com</code></p>
<dd> Run a master machine connection check part. This is either run automatically by replica part of the connection check program (when <i>-a</i> option is set) or manually by the user. A running <a href="/docs/linux/man/1-ipa-replica-conncheck/">ipa-replica-conncheck</a>(1) in a listening mode must be already running on a replica machine.</p>
<dt><code>ipa-replica-conncheck -m master.example.com -a -r EXAMPLE.COM -w password</code></p>
<dd> Run a replica-master connection check. In case of a success switch to listening mode, automatically log to <i>master.example.com</i> in a realm <i>EXAMPLE.COM</i> with a password <i>password</i> and run the second part of the connection check. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the connection check was successful </p>
<p> 1 if an error occurred</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipa-replica-install/">ipa-replica-install</a></code>(1) </p>
<h2>Index</h2>
