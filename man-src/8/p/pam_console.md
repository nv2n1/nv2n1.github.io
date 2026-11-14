---
title: "pam_console(8)"
name: "pam_console"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_console/"
description: "pam_console – determine user owning the system console"
---

<p>pam_console &#8211; determine user owning the system console</p>
<h2>Synopsis</h2>
<p><code>session optional pam_console.so</code><br />
 <code>auth required pam_console.so</code></p>
<h2>Description</h2>
<p>pam_console.so is designed to give users at the physical console (virtual terminals and local xdm-managed X sessions by default, but that is configurable) capabilities that they would not otherwise have, and to take those capabilities away when the are no longer logged in at the console. It provides two main kinds of capabilities: file permissions and authentication. When a user logs in at the console and <code>no other user is currently logged in at the console</code>, pam_console.so will run handler programs specified in the file /etc/security/console.handlers such as pam_console_apply which changes permissions and ownership of files as described in the file /etc/security/console.perms. That user may then log in on other terminals that are considered part of the console, and as long as the user is still logged in at any one of those terminals, that user will own those devices. When the user logs out of the last terminal, the console may be taken by the next user to log in. Other users who have logged in at the console during the time that the first user was logged in will not be given ownership of the devices unless they log in on one of the terminals; having done so on any one terminal, the next user will own those devices until he or she has logged out of every terminal that is part of the physical console. Then the race can start for the next user. In practice, this is not a problem; the physical console is not generally in use by many people at the same time, and pam_console.so just tries to do the right thing in weird cases. When an application attempts to authenticate the user <code>and this user is already logged in at the console</code>, pam_console.so checks whether there is a file in /etc/security/console.apps/ directory with the same name as the application servicename, and if such a file exists, authentication succeeds. This way pam_console may be utilized to run some system applications (reboots, config tools) without root password, or to enter user password on the first system login only. </p>
<h2>Arguments</h2>
<dl>
<dt>debug</p>
<dd>turns on debugging</p>
<dt>allow_nonroot_tty</p>
<dd>gain console locks and change permissions even if the TTY&#8217;s owner is not root.</p>
<dt>handlersfile=<i>filename</i></p>
<dd>tells pam_console.so to get the list of the handlers from a different file than /etc/security/console.handlers</dl>
<h2>Example</h2>
<p><code>/etc/pam.d/some-system-tool</code>:<br />
 auth sufficient pam_rootok.so<br />
 auth required pam_console.so </p>
<p> <code>/etc/pam.d/some-login-service</code>:<br />
 auth sufficient pam_console.so<br />
 auth required pam_unix.so<br />
 session required pam_unix.so<br />
 session optional pam_console.so</p>
<h2>Files</h2>
<p><i>/var/run/console/</i><br />
 <i>/var/run/console/console.lock</i><br />
 <i>/etc/security/console.apps</i><br />
 <i>/etc/security/console.handlers</i></p>
<h2>Security Notes</h2>
<p>When pam_console &quot;auth&quot; is used for login services which provide possibility of remote login, it is necessary to make sure the application correctly sets PAM_RHOST variable, or to deny remote logins completely. Currently, /bin/login (invoked from telnetd) and gdm is OK, others may be not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-console-perms/">console.perms</a></code>(5)<br />
 <code><a href="/docs/linux/man/5-console-apps/">console.apps</a></code>(5)<br />
 <code><a href="/docs/linux/man/5-console-handlers/">console.handlers</a></code>(5)<br />
 <code><a href="/docs/linux/man/8-pam_console_apply/">pam_console_apply</a></code>(8)<br />
 <i>/usr/share/doc/pam*/html/index.html</i></p>
<h2>Bugs</h2>
<p>Let&#8217;s hope not, but if you find any, please report them via the &quot;Bug Track&quot; link at <a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a></p>
<h2>Authors</h2>
<p>Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;<br />
 Support of console.handlers and other improvements by Tomas Mraz &lt;tmraz [at] redhat.com&gt;</p>
