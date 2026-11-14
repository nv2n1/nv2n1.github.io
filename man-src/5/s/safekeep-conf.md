---
title: "safekeep-conf(5)"
name: "safekeep-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-safekeep-conf/"
description: "safekeep.conf – Configuration file for ‘"
---

<p>safekeep.conf &#8211; Configuration file for &#8216;</p>
<p><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1)&#8217;</p>
<h2>Synopsis</h2>
<p>This file resides in /etc/safekeep/, or optionally in ~/.safekeep/ for non-root users, from where it will be automatically picked up by <i><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1)</i>.</p>
<h2>Description</h2>
<p>This configuration file holds safekeep global settings. The format of the file is a simple key-value pair similar to Java properties files: lines starting with <i>#</i> are ignored as comments, keys are separated from values by <i>=</i>, and leading and trailing spaces are ignored.</p>
<h2>Parameters</h2>
<p>backup.user</p>
<dl>
<dd>The Unix user under which the server will run. If not specified, safekeep will just run under the current user.</dl>
<p> base.dir</p>
<dl>
<dd>The base directory for date repository relative paths. If not specified, it defaults to the home directory of the backup user.</dl>
<p> client.user</p>
<dl>
<dd>The default Unix user which will be used on the client. This can be overridden on a host by host basis in the .backup file. If not specified, it defaults to root.</dl>
<p> email.format</p>
<dl>
<dd>If specified generate multipart MIME email messages. If not specified then a non-MIME message is created. The format options are <i>text</i> or <i>html</i> to generate parts of that type. NB: The log of safekeep is always sent as <i>text</i>.</dl>
<p> email.from</p>
<dl>
<dd>The email address to be used as sender when sending the logs. If not specified safekeep will use SafeKeep@&lt;hostname fqdn&gt;.</dl>
<p> email.to</p>
<dl>
<dd>In addition to writing the session logs on the standard output, safekeep can also send the logs via email to a number of recipients. This comma-separated list of emails designates the recipients of the logs. If not specified, safekeep will not attempt to email the logs.</dl>
<p> email.smtp.port</p>
<dl>
<dd>Specifies the port to use to connect to the SMTP server. If not specified, safekeep will use the system default value, normally port 25/tcp.</dl>
<p> email.smtp.server</p>
<dl>
<dd>Specifies the SMTP server used for sending mails if the email.to specifies any recipients. If not specified, safekeep will just use /usr/sbin/sendmail to deliver the mail.</dl>
<p> email.summary</p>
<dl>
<dd>Generate a summary part at the start of the email. Possible options are <i>true</i>, <i>yes</i> or <i>1</i>. Anything elses as taken as <i>false</i>. NB: This requires <i>email.format</i> set and currently only used for <i>server</i> and <i>list</i> run types.</dl>
<p> nice.adjustment</p>
<dl>
<dd>The default nice level adjustment for safekeep. It specifies an integer to be added to the current nice level. Nicenesses range from -20 (most favorable scheduling) to 19 (least favorable). To disable nice, set this value to 0. If no nice level is specified, safekeep is niced at +10.</dl>
<p> nice.adjustment.server</p>
<dl>
<dd>The nice level adjustment for safekeep, used on the server side. It overrides the generic setting in nice.adjustment.</dl>
<p> nice.adjustment.client</p>
<dl>
<dd>The default nice adjustment for the client. This settings is normally not all that important, as most of the load is on the server side. You can also set the remove nice level on a per-client basis in the .backup file (see /backup/host/@nice). NB: if you change this value, you will have to re-deploy the auth keys.</dl>
<p> ionice.adjustment</p>
<dl>
<dd>The default IO nice level adjustment for safekeep. It can be either <i>none</i>, <i>idle</i>, or an integer between 0-7 (with 0 being higher priority). See <a href="/docs/linux/man/1-ionice/">ionice</a>(1) for more information. This is currently being used only on the server side, where IO load tends to be a problem. NB: this depends on the availability of <i><a href="/docs/linux/man/1-ionice/">ionice</a>(1)</i> on the system where the server is running. If ionice cannot be found, this setting is ignored. If no level is specified, it defaults to <i>idle</i>.</dl>
<p> bandwidth.overall</p>
<dl>
<dd>This is the default bandwidth limit for both upload and download for all the clients. It is an integer number of KB/s (see NOTES section for more information). This value is optional.</dl>
<p> bandwidth.download</p>
<dl>
<dd>This is the default bandwidth limit for download across all clients. If specified (with a value greater than 0) it will override the value set in bandwidth.overall (refer to it for more informatio). This value is optional.</dl>
<p> bandwidth.upload</p>
<dl>
<dd>This is the default bandwidth limit for upload across all clients. If specified (with a value greater than 0) it will override the value set in bandwidth.overall (refer to it for more information). This value is optional.</dl>
<p> snapshot.size</p>
<dl>
<dd>This is the default size to be used for any snapshots without a size value specified. It is passed to <i><a href="/docs/linux/man/8-lvcreate/">lvcreate</a>(8)</i> (LVM2), including the specification of a percentage (%). If not otherwise specified, the percentage is based on unallocated space (i.e. LVM2 <i>%FREE</i>), which is different to the interpretation within the &lt;snapshot&gt; option. This value is optional, it defaults to <i>20%FREE</i>.</dl>
<p> ssh.keygen.type</p>
<dl>
<dd>The SSH private key type to generate when <i>safekeep &#8211;keys</i> is used. This is passed to <i><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1)</i> and not all valid types may be accepted on all systems. Only SSH protocol version 2 keys are accepted. This value is optional, it defaults to <i>rsa</i>.</dl>
<p> ssh.keygen.bits</p>
<dl>
<dd>Specifies the number of bits in the SSH private key to create. This is passed to <i><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1)</i> and only certain sizes are accepted, depending of the key type. If no value is required, e.g. for <i>ecdsa</i> key type, give this option with no corresponding bit size. This value is optional, it defaults to <i>4096</i>.</dl>
<h2>Notes</h2>
<p>Safekeep uses trickle to implement bandwidth throttling (see m[blue]<code><a rel="nofollow" href="http://monkey.org/~marius/pages/?page=trickle">http://monkey.org/~marius/pages/?page=trickle</a></code>m[] for more information). You will need to install it separately to use this feature (most Linux distributions have it packaged as trickle). </p>
<p> The bandwidth is calculated as an average over a 256KB window, and it is expressed as an integer number of kilo-bytes per second (e.g. 100, meaning 100KB/s). Bandwidth limits of zero are ignored. </p>
<p> The bandwidth throtlling can be customized for both download and upload (see bandwidth.download and bandwidth.upload) as well as on a per-client basis (see <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5) for more information).</p>
<h2>Files</h2>
<dl>
<dd>
<pre>/etc/safekeep/safekeep.conf
~/.safekeep/safekeep.conf</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-safekeep/">safekeep</a>(1), <a href="/docs/linux/man/5-safekeep-backup/">safekeep.backup</a>(5), <a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a>(1), <a href="/docs/linux/man/1-trickle/">trickle</a>(1), <a href="/docs/linux/man/8-lvcreate/">lvcreate</a>(8), <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1)</p>
<h2>Author</h2>
<p>This man page was originally written by Dimi Paun &lt;m[blue]<code>dimi [at] lattica.com</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>dimi [at] lattica.com</p>
<dl>
<dd>mailto:dimi [at] lattica.com</dl>
