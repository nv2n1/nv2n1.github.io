---
title: "denyhosts(8)"
name: "denyhosts"
section: "8"
letter: "d"
url: "/docs/linux/man/8-denyhosts/"
description: "DenyHosts – version: 2.8"
---

<p>DenyHosts &#8211; version: 2.8</p>
<h2>Description</h2>
<p><code>DenyHosts</code> is a python program that automatically blocks ssh attacks by adding entries to /etc/hosts.deny. <code>DenyHosts</code> will also inform system administrators about offending hosts, attacked users and suspicious logins. Usage: /usr/sbin/denyhosts [-f logfile | <code>&#8211;file</code>=<i>logfile]</i> [ <code>-c</code> configfile | <code>&#8211;config</code>=<i>configfile]</i> [-i | <code>&#8211;ignore]</code> [-n | <code>&#8211;noemail]</code> [&#8211;purge] [&#8211;migrate] [&#8211;daemon] [&#8211;sync] [&#8211;version]</p>
<dl>
<dt><code>&#8211;file</code>:</p>
<dd>The name of log file to parse</p>
<dt> <code>&#8211;config</code>: The configuration file to use, typically /etc/denyhosts.conf</p>
<dt> <code>&#8211;ignore</code>: Ignore last processed offset (start processing from beginning)</p>
<dt> <code>&#8211;noemail</code>: Do not send an email report</p>
<dt> <code>&#8211;unlock</code>: if lockfile exists, remove it and run as normal</p>
<dt> <code>&#8211;migrate</code>: migrate your HOSTS_DENY file so that it is suitable for <code>&#8211;purge</code></p>
<dt> <code>&#8211;purge</code>: expire entries older than your PURGE_DENY setting</p>
<dt> <code>&#8211;purge-all</code>: expire all entries immediately</p>
<dt> <code>&#8211;purgeip</code>: remove specified IP address from blocked list</p>
<dt> <code>&#8211;daemon</code>: run DenyHosts in daemon mode</p>
<dt> <code>&#8211;foreground</code>: run DenyHosts in foreground mode</p>
<dt> <code>&#8211;sync</code>: run DenyHosts synchronization mode</p>
<dt> <code>&#8211;version</code>: Prints the version of DenyHosts and exits</dl>
<dd>Note: multiple <code>&#8211;file</code> args can be processed. If multiple files are provided, <code>&#8211;ignore</code> is implied Note: in a Debian system, the default running mode is <code>daemon mode</code> and the configuration file is <code>/etc/denyhosts.conf</code></p>
<h3>When run in &#8211;daemon mode the following flags are ignored:</h3>
<dl>
<dt> <code>&#8211;file</code>, <code>&#8211;purge</code>, <code>&#8211;migrate</code>, <code>&#8211;sync</code>, <code>&#8211;verbose</code> </p>
<h2>See Also</h2>
<dd>Please refer to <a rel="nofollow" href="http://denyhost.sourceforge.net/faq.html">http://denyhost.sourceforge.net/faq.html</a> for full documentation.</p>
<h2>Author</h2>
<p><code>DenyHosts</code> was written by Phil Schwartz &lt;phil_schwartz [at] users.sourceforge.net&gt; </p>
<p> This manual page was written by Marco Bertorello &lt;marco [at] bertorello.ns0.it&gt; for the Debian project (but may be used by others).</p>
