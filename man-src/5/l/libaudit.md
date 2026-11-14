---
title: "libaudit(5)"
name: "libaudit"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libaudit/"
description: "libaudit.conf – libaudit configuration file"
---

<p>libaudit.conf &#8211; libaudit configuration file</p>
<h2>Description</h2>
<p>The file <i>/etc/libaudit.conf</i> contains configuration information for user space applications that link to libaudit. The applications are responsible for querrying the settings in this file and obeying the admin&#8217;s preferences. This file contains one configuration keyword per line, an equal sign, and then followed by appropriate configuration information. The keywords recognized are: <i>failure_action</i>. These keywords are described below.</p>
<dl>
<dt><i>failure_action</i></p>
<dd>This keyword specifies what action the admin wishes a user space application to take when there is a failure to send an audit event to the kernel. The possible values are: <i>IGNORE</i><br />
&nbsp;<wbr>&#8211; meaning do nothing, <i>LOG</i> &#8211; write to syslog the inability to send an audit event, and <i>TERMINATE</i> &#8211; the user space application should exit. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_auditfail_action/">get_auditfail_action</a></code>(3). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
