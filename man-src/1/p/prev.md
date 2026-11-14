---
title: "prev(1)"
name: "prev"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prev/"
description: "prev – show the previous message"
---

<h2 class="name">NAME</h2>
<p> prev &#8211; show the previous message </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>prev </code> [<i>+folder</i>] [-showproc <i>program</i>] [<code>-showmimeproc</code> <i>program</i>] [<code>-header</code> | <code>-noheader</code>] [<code>-checkmime</code> | <code>-nocheckmime</code>] [switches for <i>showproc</i></p>
<dd>or <i>showmimeproc</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Prev</code> performs a <code>show</code> on the previous message in the specified (or current) folder. Like <code>show</code>, it passes any switches on to the program named by <i>showproc</i> or <i>showmimeproc</i>, which is called to list the message. This command is almost exactly equivalent to &#8220;<code>show prev</code>&#8221;. Consult the manual entry for <i><a href="/docs/linux/man/1-show/">show</a></i>(1) for all the details.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^showproc:~^Program to show non-MIME messages
^showmimeproc:~^Program to show MIME messages
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-next/">next</a></i>(1), <i><a href="/docs/linux/man/1-show/">show</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>-checkmime</code>'
`<code>-header</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is specified, it will become the current folder. The message that is shown (i.e., the previous message in sequence) will become the current message.</p>
<h2>BUGS</h2>
<p> <code>prev</code> is really a link to the <code>show</code> program. As a result, if you make a link to <code>prev</code> and that link is not called <code>prev</code>, your link will act like <code>show</code> instead. To circumvent this, add a profile-entry for the link to your <code>nmh</code> profile and add the argument <code>prev</code> to the entry. </p>
<h2>Index</h2>
