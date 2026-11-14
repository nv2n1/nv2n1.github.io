---
title: "doveadm-config(1)"
name: "doveadm-config"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-config/"
description: "doveconf – Dovecot’s configuration dumping utility"
---

<h2>NAME</h2>
<p> doveconf &#8211; Dovecot&#8217;s configuration dumping utility</p>
<h2>SYNOPSIS</h2>
<p> <code>doveconf</code> [<code>-adnNSx</code>] [<code>-c</code> <i>config-file</i>] [<code>-f</code> <i>filter</i>] [<code>-m</code> <i>module</i>]<br />
 <code>doveconf</code> [<code>-n</code>] [<code>-c</code> <i>config-file</i>] <i>section_name</i>&nbsp;<wbr>&#8230;<br />
 <code>doveconf</code> [<code>-h</code>] [<code>-c</code> <i>config-file</i>] [<code>-f</code> <i>filter</i>] <i>setting_name</i>&nbsp;<wbr>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>doveconf</code> reads and parses Dovecot&#8217;s configuration files and converts them into a simpler format used by the rest of Dovecot. All standalone programs, such as <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) and <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), will first get their settings by executing doveconf. </p>
<p> For system administrators, <code>doveconf</code> is mainly useful for dumping the configuration in easy human readable output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Show all settings with their currently configured values.</p>
<dt><code>-c</code><i>&nbsp;<wbr>config-file</i></p>
<dd> read configuration from the given <i>config-file</i>. By default <i>/etc/dovecot/dovecot.conf</i> will be used.</p>
<dt><code>-d</code></p>
<dd> Show the setting&#8217;s default value instead of the one currently configured.</p>
<dt><code>-f</code><i>&nbsp;<wbr>filter</i></p>
<dd> Show the matching configuration for the specified <i>filter</i> condition. The <i>filter</i> option string has to be given as <i>name</i><code>=</code><i>value</i> pair. For multiple filter conditions the <code>-f</code> option can be supplied multiple times.<br />
 Possible names for the <i>filter</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>lname</code></p>
<dd> The local hostname, e.g. mail.example.com. This will only match hostnames which were configured like:<br />
 <code>local_name mail.example.com { # special settings }</code></p>
<dt><code>local</code></p>
<dd> The server&#8217;s hostname or IP address. This will also match hostnames which were configured like:<br />
 <code>local imap.example.net { # special settings }</code></p>
<dt><code>protocol, service</code></p>
<dd> The protocol, e.g. imap or pop3</p>
<dt><code>remote</code></p>
<dd> The client&#8217;s hostname or IP address.</dl>
</dl>
<dt><code>-h</code></p>
<dd> Hide the setting&#8217;s name, show only the setting&#8217;s value.</p>
<dt><code>-m&nbsp;<wbr></code><i>module</i></p>
<dd> Show only settings for the given <i>module</i>.</p>
<dl>
<dt>
<dd> e.g. <code>imap</code>, <code>imap-login</code>, <code>lmtp</code>, <code>pop3&nbsp;<wbr></code>or <code>pop3-login</code></dl>
<dt><code>-n</code></p>
<dd> Show only settings with non-default values.</p>
<dt><code>-N</code></p>
<dd> Show settings with non-default values and explicitly set default values.</p>
<dt><code>-S</code></p>
<dd> Dump settings in simplified machine parsable/readable format.</p>
<dt><code>-x</code></p>
<dd> Expand configuration variables (e.g. $mail_plugins &rArr; quota) and show file contents (from e.g. ssl_cert = &lt;/etc/ssl/certs/dovecot.pem).</p>
<dt><i>section_name</i></p>
<dd> Show only the current configuration of one or more specified sections.</p>
<dt><i>setting_name</i></p>
<dd> Show only the setting of one or more <i>setting_name</i>(s) with the currently configured value. You can show a setting inside a section using &#8216;/&#8217; as the section separator, e.g. service/imap/executable.</dl>
<h2>EXAMPLE</h2>
<p> When Dovecot was configured to use different settings for some networks/subnets it is possible to show which settings will be applied for a specific connection. </p>
<pre>
<code>doveconf -f local=10.0.0.110 -f remote=10.11.1.2 -f service=pop3 -n</code>
</pre>
<p> <code>doveconf</code> can be also used to convert v1.x configuration files into v2.x format. </p>
<pre>
<code>doveconf -n -c /oldpath/dovecot.conf &gt; /etc/dovecot/dovecot.conf.new</code>
</pre>
<p> This example shows how to ask <code>doveconf</code> for a global setting and a protocol specific setting. The second command uses also the <code>-h</code> option, in order to hide the setting&#8217;s name. </p>
<pre>
<code>doveconf mail_plugins</code>
mail_plugins = quota
<code>doveconf  -h -f protocol=imap mail_plugins</code>
quota imap_quota
</pre>
<p> This example demonstrates how to dump a whole configuration section. </p>
<pre>
<code>doveconf dict</code>
dict {
  quota = pgsql:/etc/dovecot/dovecot-dict-sql.conf.ext
}
</pre>
<p> Or how to dump only the quota dict: </p>
<pre>
<code>doveconf dict/quota</code>
dict/quota = pgsql:/etc/dovecot/dovecot-dict-sql.conf.ext
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-dsync/">dsync</a></code>(1) </p>
<h2>Index</h2>
