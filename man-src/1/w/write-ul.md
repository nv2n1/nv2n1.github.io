---
title: "write-ul(1)"
name: "write-ul"
section: "1"
letter: "w"
url: "/docs/linux/man/1-write-ul/"
description: "write – send a message to another user"
---

<p>write &#8211; send a message to another user </p>
<p> <code>write</code> <i>user</i> [<i>ttyname</i>] </p>
<h2>Description</h2>
<p><code>write</code> allows you to communicate with other users, by copying lines from your terminal to theirs. </p>
<p> When you run the <code>write</code> command, the user you are writing to gets a message of the form: </p>
<dl COMPACT>
<dd>
<pre>Message from yourname [at] yourhost on yourtty at hh:mm ...</pre>
</dl>
<p> Any further lines you enter will be copied to the specified user&#8217;s terminal. If the other user wants to reply, they must run <code>write</code> as well. </p>
<p> When you are done, type an end-of-file or interrupt character. The other user will see the message <code>EOF</code> indicating that the conversation is over. </p>
<p> You can prevent people (other than the superuser) from writing to you with the <code><a href="/docs/linux/man/1-mesg/">mesg</a></code>(1) command. Some commands, for example <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1) and <code><a href="/docs/linux/man/1-pr/">pr</a></code>(1), may automatically disallow writing, so that the output they produce isn&#8217;t overwritten. </p>
<p> If the user you want to write to is logged in on more than one terminal, you can specify which terminal to write to by giving the terminal name as the second operand to the <code>write</code> command. Alternatively, you can let <code>write</code> select one of the terminals &#8211; it will pick the one with the shortest idle time. This is so that if the user is logged in at work and also dialed up from home, the message will go to the right place. </p>
<p> The traditional protocol for writing to someone is that the string <i>-o</i>, either at the end of a line or on a line by itself, means that it&#8217;s the other person&#8217;s turn to talk. The string <i>oo</i> means that the person believes the conversation to be over.</p>
<h2>Options</h2>
<p><code>-V</code>, <code>&#8211;version</code></p>
<dl COMPACT>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl COMPACT>
<dd>Display help text and exit.</dl>
<h2>History</h2>
<p>A <code>write</code> command appeared in Version 6 AT&amp;T UNIX.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mesg/">mesg</a></code>(1), <code><a href="/docs/linux/man/1-talk/">talk</a></code>(1), <code><a href="/docs/linux/man/1-who/">who</a></code>(1)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>write</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
