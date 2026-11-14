---
title: "bsd-write(1)"
name: "bsd-write"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsd-write/"
description: "write – send a message to another user"
---

<h2 class="name">NAME</h2>
<p> <code>write</code> &#8211; send a message to another user </p>
<h2>SYNOPSIS</h2>
<p> <i>user</i> [<i>tty</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility allows you to communicate with other users, by copying lines from your terminal to theirs. </p>
<p> When you run the command, the user you are writing to gets a message of the form: </p>
<blockquote><p><tt>Message from yourname [at] yourhost on yourtty at hh:mm ...</tt></p></blockquote>
<p> Any further lines you enter will be copied to the specified user&#8217;s terminal. If the other user wants to reply, they must run as well. </p>
<p> When you are done, type an end-of-file or interrupt character. The other user will see the message `EOF&#8217; indicating that the conversation is over. </p>
<p> You can prevent people (other than the super-user) from writing to you with the <a href="/docs/linux/man/1-mesg/">mesg</a>(1) command. </p>
<p> If the user you want to write to is logged in on more than one terminal, you can specify which terminal to write to by specifying the terminal name as the second operand to the command. Alternatively, you can let select one of the terminals &#8211; it will pick the one with the shortest idle time. This is so that if the user is logged in at work and also dialed up from home, the message will go to the right place. </p>
<p> The traditional protocol for writing to someone is that the string `-o&#8217; , either at the end of a line or on a line by itself, means that it is the other person&#8217;s turn to talk. The string `oo&#8217; means that the person believes the conversation to be over.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mesg/">mesg</a>(1), <a href="/docs/linux/man/1-talk/">talk</a>(1), <a href="/docs/linux/man/1-wall/">wall</a>(1), <a href="/docs/linux/man/1-who/">who</a>(1)</p>
<h2>HISTORY</h2>
<p> A command appeared in AT&amp;T System v1 .</p>
<h2>BUGS</h2>
<p> The sender&#8217;s <code>LC_CTYPE</code> setting is used to determine which characters are safe to write to a terminal, not the receiver&#8217;s (which has no way of knowing). </p>
<h2>Index</h2>
