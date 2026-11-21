---

title: "sg(1)"
name: "sg"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sg/"
description: "sg – execute command as different group ID"
---

<dl>
<dt> <code>sg</code> [-] [group&nbsp;[-c&nbsp;]&nbsp;command]</dt></dl>
<dd>The <code>sg</code> command works similar to <code>newgrp</code> but accepts a command. The command will be executed with the /bin/sh shell. With most shells you may run <code>sg</code> from, you need to enclose multi-word commands in quotes. Another difference between <code>newgrp</code> and <code>sg</code> is that some shells treat <code>newgrp</code> specially, replacing themselves with a new instance of a shell that <code>newgrp</code> creates. This doesn&#8217;t happen with <code>sg</code>, so upon exit from a <code>sg</code> command you are returned to your previous group ID.</dd>
<h2>CONFIGURATION</h2>
<p> The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>SYSLOG_SG_ENAB</code> (boolean)</p>
<dl>
<dt>
</dt><dd> Enable &quot;syslog&quot; logging of <code>sg</code> activity.</dd></dl>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
</dt><dd> User account information.</dd></dl>
<p> /etc/shadow</p>
<dl>
<dt>
</dt><dd> Secure user account information.</dd></dl>
<p> /etc/group</p>
<dl>
<dt>
</dt><dd> Group account information.</dd></dl>
<p> /etc/gshadow</p>
<dl>
<dt>
</dt><dd> Secure group account information.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-id/">id</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/1-gpasswd/">gpasswd</a></code>(1), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5). </p>
