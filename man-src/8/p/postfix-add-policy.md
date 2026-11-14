---
title: "postfix-add-policy(8)"
name: "postfix-add-policy"
section: "8"
letter: "p"
url: "/docs/linux/man/8-postfix-add-policy/"
description: "postfix-add-policy – add policy service to Postfix master.cf"
---

<p>postfix-add-policy &#8211; add policy service to Postfix master.cf</p>
<h2>Synopsis</h2>
<pre><code>postfix-add-policy</code> [<i>policy name</i>...] [<i>username</i>...] [<i>argv</i>...]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-postfix-add-policy/">postfix-add-policy</a></code>(8) command adds an smtp policy server named <i>policy name</i> running using <i>username</i> and called as <i>argv</i> to /etc/postfix/master.cf to facilitate integration of SMTP policy servers such as postgrey or postfix-policyd-spf-perl. The configuration is based on the Postfix SMTPD_POLICY_README. Adminstrators should verify it is appropriate for their requirements. The original file is copied prior to modification and left in /etc/postfix to make it possible to revert changes easily. Available in the Debian package for Postfix version 2.5.3 and later. </p>
<h2>Diagnostics</h2>
<p>If the given <i>policy name</i> already appears in the master.cf, a message will be printed to standard out and master.cf will not be modified.</p>
<h2>Environment</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd>Directory with Postfix configuration files. </p>
<p> The <code><a href="/docs/linux/man/8-postfix-add-policy/">postfix-add-policy</a></code>(8) command should use this, but it currently doesn&#8217;t. It is hard coded to /etc/postfix. This should be changed.</dl>
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
