---
title: "console-handlers(5)"
name: "console-handlers"
section: "5"
letter: "c"
url: "/docs/linux/man/5-console-handlers/"
description: "console.handlers – file specifying handlers of console lock and unlock events"
---

<p>console.handlers &#8211; file specifying handlers of console lock and unlock events</p>
<h2>Description</h2>
<p>/etc/security/console.handlers determines which programs will be run when an user obtains the console lock at login time, and when the user loses it on log out. It is read by the pam_console module. The format is: <code>handler-filename</code> <code>lock</code><i>|</i><code>unlock</code> <i>[</i><code>flag &#8230;</code><i>]</i> Where <code>handler-filename</code> is a name of the executable to be run, <code>lock</code> or <code>unlock</code> specifies on which event it should be run, and flags specify how should pam_console call it. Additionally there should be a line which specifies glob patterns of console devices. The format of this line is: <code>console-name</code> <code>consoledevs</code> <code>regex</code> <i>[</i><code>regex &#8230;</code><i>]</i> Where <code>console-name</code> is a name of the console class &#8211; currently ignored &#8211; and regexes are regular expression patterns which specify the name of the tty device. Only the first such line is consulted. </p>
<h2>Flags</h2>
<dl>
<dt>logfail</p>
<dd>The pam_console module should log error to the system log if the return value of the handler is not zero or if the handler can not be executed.</p>
<dt>wait</p>
<dd>The pam_console should wait for the handler to exit before continuing.</p>
<dt>setuid</p>
<dd>The handler should be executed with uid/gid of the user which obtained the console lock.</p>
<dt>tty</p>
<dd>The handler will get a tty name as obtained from PAM as a parameter.</p>
<dt>user</p>
<dd>The handler will get an user name as obtained from PAM as a parameter.</dl>
<p> Anything else will be added directly as a parameter to the handler executable.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_console/">pam_console</a></code>(8)</p>
<h2>Author</h2>
<p>Tomas Mraz &lt;tmraz [at] redhat.com&gt;</p>
