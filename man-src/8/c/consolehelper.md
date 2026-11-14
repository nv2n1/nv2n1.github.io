---
title: "consolehelper(8)"
name: "consolehelper"
section: "8"
letter: "c"
url: "/docs/linux/man/8-consolehelper/"
description: "consolehelper – A wrapper that helps console users run system programs"
---

<p>consolehelper &#8211; A wrapper that helps console users run system programs</p>
<h2>Synopsis</h2>
<p><i>progname</i> [ <i>options</i> ]</p>
<h2>Description</h2>
<p><code>consolehelper</code> is a tool that makes it easy for console users to run system programs, doing authentication via PAM (which can be set up to trust all console users or to ask for a password at the system administrator&#8217;s discretion). When possible, the authentication is done graphically; otherwise, it is done within the text console from which consolehelper was started. </p>
<p> It is intended to be completely transparent. This means that the user will never run the consolehelper program directly. Instead, programs like /sbin/shutdown are paired with a link from /usr/bin/shutdown to /usr/bin/consolehelper. Then when non-root users (specifically, users without /sbin in their path, or /sbin after /usr/bin) call the &quot;shutdown&quot; program, consolehelper will be invoked to authenticate the action and then invoke /sbin/shutdown. (consolehelper itself has no priviledges; it calls the <i><a href="/docs/linux/man/8-userhelper/">userhelper</a></i>(8) program do the real work.) </p>
<p> consolehelper requires that a PAM configuration for every managed program exist. So to make /sbin/<i>foo</i> or /usr/sbin/<i>foo</i> managed, you need to create a link from /usr/bin/<i>foo</i> to /usr/bin/consolehelper and create the file /etc/pam.d/<i>foo</i>, normally using the <i><a href="/docs/linux/man/8-pam_console/">pam_console</a></i>(8) PAM module.</p>
<h2>Options</h2>
<p>This program has no command line options of its own; it passes all command line options on to the program it is calling.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-userhelper/">userhelper</a></i>(8)</p>
<h2>Author</h2>
<p>Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;</p>
