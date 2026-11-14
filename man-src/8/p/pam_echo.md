---
title: "pam_echo(8)"
name: "pam_echo"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_echo/"
description: "pam_echo – PAM module for printing text messages"
---

<p>pam_echo &#8211; PAM module for printing text messages</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_echo.so</code> [file=<i>/path/message</i>]</dl>
<h2>Description</h2>
<dd>The <i>pam_echo</i> PAM module is for printing text messages to inform user about special things. Sequences starting with the <i>%</i> character are interpreted in the following way: </p>
<p> <i>%H</i></p>
<dl>
<dd>The name of the remote host (PAM_RHOST).</dl>
<p> <i>%h</i></p>
<dl>
<dd>The name of the local host.</dl>
<p> <i>%s</i></p>
<dl>
<dd>The service name (PAM_SERVICE).</dl>
<p> <i>%t</i></p>
<dl>
<dd>The name of the controlling terminal (PAM_TTY).</dl>
<p> <i>%U</i></p>
<dl>
<dd>The remote user name (PAM_RUSER).</dl>
<p> <i>%u</i></p>
<dl>
<dd>The local user name (PAM_USER).</dl>
<p> All other sequences beginning with <i>%</i> expands to the characters following the <i>%</i> character.</p>
<h2>Options</h2>
<p><code>file=</code><i>/path/message</i></p>
<dl>
<dd>The content of the file /path/message will be printed with the PAM conversion function as PAM_TEXT_INFO.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Message was successful printed.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>PAM_SILENT flag was given or message file does not exist, no message printed.</dl>
<h2>Examples</h2>
<p>For an example of the use of this module, we show how it may be used to print information about good passwords:</p>
<dl>
<dd>
<pre>password optional pam_echo.so file=/usr/share/doc/good-password.txt
password required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam-conf/">pam.conf</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;</p>
