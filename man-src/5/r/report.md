---
title: "report(5)"
name: "report"
section: "5"
letter: "r"
url: "/docs/linux/man/5-report/"
description: "report.conf – Configuration file for report."
---

<p><code>report.conf</code> &#8211; Configuration file for report.</p>
<h2>Description</h2>
<p>Report uses a configuration file at <code>/etc/report.conf</code>. Additional configuration files are also read from <code>/etc/report.d</code>. </p>
<h2>Parameters</h2>
<p>There are two levels of configuration in the report configuration file(s): global and plugin specific. Global is sets any configuration option presented from the plugins as well as any additional non-plugin specific parameters. Any plugin that is shipped with report will have its parameters defined here, however, any 3rd party plugins will need additional documentation provided by its maintainer.</p>
<h2>[main] OPTIONS</h2>
<dl>
<dd><code>plugin</code> Default plugin to be used.</p>
<dd><code>description</code> Short description of what the plugin does.</p>
<dd><code>loglevel</code> Set a syslog priority and facility when logging </p>
</dl>
<h2>plugin OPTIONS</h2>
<dl>
<dd><code>SCP</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>host</code>&nbsp;<wbr>remote scp/ssh server to connect to </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>path</code>&nbsp;<wbr>remote storage directory </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>username</code>&nbsp;<wbr>define a ssh user. </p>
<dd><code>FTP</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>urldir</code>&nbsp;<wbr>ftp server to store report. This also allows </p>
<p>&nbsp;<wbr>&nbsp;<wbr>passing a username/password in the form of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;<a href="ftp://username:password@ftp.server.com">ftp://username:password@ftp.server.com</a>&quot; </p>
<dd><code>LOCALSAVE</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>path</code>&nbsp;<wbr>path on local filesystem where to store report files. </p>
<dd><code>BUGZILLA</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>bugzilla_host</code>&nbsp;<wbr>URL of a bugzilla instance </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>username</code>&nbsp;<wbr>login for bugzilla instance </p>
</dl>
<h2>Files</h2>
<pre>/etc/report.conf
/etc/report.d/</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-report/">report</a>(1) </p>
