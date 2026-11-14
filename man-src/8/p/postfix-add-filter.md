---
title: "postfix-add-filter(8)"
name: "postfix-add-filter"
section: "8"
letter: "p"
url: "/docs/linux/man/8-postfix-add-filter/"
description: "postfix-add-filter – add filter service to Postfix master.cf"
---

<p>postfix-add-filter &#8211; add filter service to Postfix master.cf</p>
<h2>Synopsis</h2>
<pre><code>postfix-add-filter</code> [<i>smtp service name</i>...] [<i>smtpd port</i>...]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-postfix-add-filter/">postfix-add-filter</a></code>(8) command adds an smtp service named <i>smtp service name</i> and and smtpd server listening on <i>smtpd port</i> to /etc/postfix/master.cf to facilitate integration of SMTP filters such as amavisd-new or clamsmtp. The configuration is based on the upstream recommendations for amavisd-new 2.6.0. Adminstrators should verify it is appropriate for their requirements. The original file is copied prior to modification and left in /etc/postfix to make it possible to revert changes easily. Available in the Debian package for Postfix version 2.5.3 and later. </p>
<h2>Diagnostics</h2>
<p>If the given <i>smtp service name</i> or <i>smtpd port</i> already appear in the master.cf, a message will be printed to standard out and master.cf will not be modified.</p>
<h2>Environment</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd>Directory with Postfix configuration files. </p>
<p> The <code><a href="/docs/linux/man/8-postfix-add-filter/">postfix-add-filter</a></code>(8) command should use this, but it currently doesn&#8217;t. It is hard coded to /etc/postfix. This should be changed.</dl>
<h2>Configuration Parameters</h2>
<p>None</p>
<h2>Files</h2>
<pre>/etc/postfix/master.cf</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), Postfix configuration</pre>
<h2>License</h2>
<p>This software is licensed under the MIT open source license.</p>
<h2>Author(S)</h2>
<pre>Scott Kitterman
&lt;scott [at] kitterman.com&gt;</pre>
