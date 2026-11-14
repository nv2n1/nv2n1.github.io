---
title: "cons(8)"
name: "cons"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cons/"
description: "cons.saver – general-purpose Linux console screen save and restore server"
---

<p>cons.saver &#8211; general-purpose Linux console screen save and restore server</p>
<h2>Synopsis</h2>
<pre>cons.saver <i>TTY</i></pre>
<h2>Description</h2>
<dl>
<dt>Invoke this helper program with the Ctrl-o key combination to save and restore the user session on the screen.</p>
<dd></dl>
<h2>Options</h2>
<p>cons.saver takes only one argument, the <i>TTY</i> <i>NAME</i> from which the system will save and restore.</p>
<h2>Security</h2>
<p>Cons.saver does not need to be invoked by root. It only needs read and write access to /dev/vcsa*, which is a priviledged operation. You should create an unprivileged user, make cons.saver setuid to that user, and assure that all the vcsa* are owned by that user too.</p>
<h2>Author</h2>
<p>Manpage written by Rodrigo Rubira Branco &lt;rrbranco [at] br.ibm.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mc/">mc</a></code>(1), <code><a href="/docs/linux/man/8-mcserv/">mcserv</a></code>(8) </p>
