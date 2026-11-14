---
title: "captest(8)"
name: "captest"
section: "8"
letter: "c"
url: "/docs/linux/man/8-captest/"
description: "captest – a program to demonstrate capabilities"
---

<p>captest &#8211; a program to demonstrate capabilities</p>
<h2>Synopsis</h2>
<p><code>captest [ &#8211;drop-all | &#8211;drop-caps | &#8211;id ] [ &#8211;lock ] [ &#8211;text ]</code></p>
<h2>Description</h2>
<p><code>captest</code> is a program that demonstrates and prints out the current process capabilities. Each option prints the same report. It will output current capabilities. then it will try to access /etc/shadow directly to show if that can be done. Then it creates a child process that attempts to read /etc/shadow and outputs the results of that. Then it outputs the capabilities that a child process would have. You can also apply file system capabilities to this program to study how they work. For example, filecap /usr/bin/captest chown. Then run captest as a normal user. Another interesting test is to make captest suid root so that you can see what the interaction is between root&#8217;s credentials and capabilities. For example, chmod 4755 /usr/bin/captest. When run as a normal user, the program will see if privilege escalation is possible. But do not leave this app setuid root after you are don testing so that an attacker cannot take advantage of it. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;drop-all</code></p>
<dd>This drops all capabilities and clears the bounding set.</p>
<dt><code>&#8211;drop-caps</code></p>
<dd>This drops just traditional capabilities.</p>
<dt><code>&#8211;id</code></p>
<dd>This changes to uid and gid 99, drops supplemental groups, and clears the bounding set.</p>
<dt><code>&#8211;text</code></p>
<dd>This option outputs the effective capabilities in text rather than numerically.</p>
<dt><code>&#8211;lock</code></p>
<dd>This prevents the ability for child processes to regain privileges if the uid is 0. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-filecap/">filecap</a></code>(8), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Author</h2>
<p>Steve Grubb</p>
