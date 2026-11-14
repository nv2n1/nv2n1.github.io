---
title: "mailto-conf(5)"
name: "mailto-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mailto-conf/"
description: "mailto.conf – configuration file for cups email notifier"
---

<p>mailto.conf &#8211; configuration file for cups email notifier</p>
<h2>Description</h2>
<p>The <code>mailto.conf</code> file defines the local mail server and email notification preferences for CUPS. </p>
<p> Each line in the file can be a configuration directive, a blank line, or a comment. Configuration directives typically consist of a name and zero or more values separated by whitespace. The configuration directive name and values are case-insensitive. Comment lines start with the # character.</p>
<h3>Directives</h3>
<dl>
<dt><code>Cc </code><i>cc-address [at] domain.com</i></p>
<dd>Specifies an additional recipient for all email notifications.</p>
<dt><code>From </code><i>from-address [at] domain.com</i></p>
<dd>Specifies the sender of email notifications.</p>
<dt><code>Sendmail </code><i>sendmail command and options</i></p>
<dd>Specifies the sendmail command to use when sending email notifications. Only one <i>Sendmail</i> or <i>SMTPServer</i> line may be present in the <code>mailto.conf</code> file. If multiple lines are present, only the last one is used.</p>
<dt><code>SMTPServer </code><i>servername</i></p>
<dd>Specifies a SMTP server to send email notifications to. Only one <i>Sendmail</i> or <i>SMTPServer</i> line may be present in the <code>mailto.conf</code> file. If multiple lines are present, only the last one is used.</p>
<dt><code>Subject </code><i>subject-prefix</i></p>
<dd>Specifies a prefix string for the subject line of an email notification.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
