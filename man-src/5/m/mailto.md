---
title: "mailto(5)"
name: "mailto"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mailto/"
---

mailto.conf - configuration file for cups email notifier

<h2>Description</h2>

The <i>mailto.conf</i> file defines the local mail server and email notification preferences for CUPS. 

 Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character.

<h2>Directives</h2>

<dl><dt>Cc <i>cc-address [at] domain.com</i>
<dd>Specifies an additional recipient for all email notifications.
<dt>From <i>from-address [at] domain.com</i>
<dd>Specifies the sender of email notifications.
<dt>Sendmail <i>sendmail command and options</i>
<dd>Specifies the sendmail command to use when sending email notifications. Only one <i>Sendmail</i> or <i>SMTPServer</i> line may be present in the <i>mailto.conf</i> file. If multiple lines are present, only the last one is used.
<dt>SMTPServer <i>servername</i>
<dd>Specifies a SMTP server to send email notifications to. Only one <i>Sendmail</i> or <i>SMTPServer</i> line may be present in the <i>mailto.conf</i> file. If multiple lines are present, only the last one is used.
<dt>Subject <i>subject-prefix</i>
<dd>Specifies a prefix string for the subject line of an email notification.</dl>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-classes-conf/">classes.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a HREF="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-types/">mime.types</a>(5)</i>, <i><a HREF="/docs/linux/man/5-printers-conf/">printers.conf</a>(5)</i>, 
 <a rel="nofollow" HREF="http://localhost:631/help">http://localhost:631/help</a>

<h2>Copyright</h2>

Copyright 2007-2013 by Apple Inc.
