---
title: "rcvstore(1)"
name: "rcvstore"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcvstore/"
description: "rcvstore – asynchronously incorporate mail into a folder"
---

<h2 class="name">NAME</h2>
<p> rcvstore &#8211; asynchronously incorporate mail into a folder </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/rcvstore</code> [<i>+folder</i>] [<code>-create</code> | <code>-nocreate</code>] [<code>-unseen</code> | <code>-nounseen</code>] [<code>-zero</code> | <code>-nozero</code>] [<code>-sequence</code> <i>name</i> &#8230;] [<code>-public</code> | <code>-nopublic</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Rcvstore</code></p>
<dd>incorporates a message from the standard input into an <code>nmh</code> folder. This command is typically used in conjunction with mail filtering programs such as <code>slocal</code> and <code>procmail</code>, to filter your mail into different folders. </p>
<p> You may specify which folder to use with <i>+folder</i>. If no folder is specified, <code>rcvstore</code> will use the folder given by a non-empty &#8220;Inbox:&#8221; entry in the user&#8217;s profile, else it will use the folder named &#8220;inbox&#8221;. </p>
<p> If the switch <code>-create</code> is given (it is the default) and if the specified (or default) folder does not exist, then it will be created. You may disable this with the <code>-nocreate</code> option. In this case <code>rcvstore</code> will exit if the specified folder does not exist. </p>
<p> When the new message is incorporated into the folder, it is assigned the next highest number for that folder. </p>
<p> <code>Rcvstore</code> will incorporate anything except zero length messages into the user&#8217;s <code>nmh</code> folder. It will not change the message in any way. </p>
<p> If the user&#8217;s profile contains a &#8220;<i>Msg-Protect: nnn</i>&#8221; entry, it will be used as the protection on the newly created message, otherwise the <code>nmh</code> default of 0600 will be used (on filesystems that support it). For all subsequent operations on this message, this initially assigned protection will be preserved. </p>
<p> If the switch <code>-unseen</code> is given (it is on by default), and if the profile entry &#8220;Unseen-Sequence&#8221; is present and non-empty, then <code>rcvstore</code> will add the newly incorporated message to each sequence named by this profile entry. You may use the switch <code>-nounseen</code> to disable this. These sequences will not be zero&#8217;ed by <code>rcvstore</code> prior to adding the new message. </p>
<p> Furthermore, the incoming message may be added to additional sequences as they arrive by the use of the <code>-sequence</code> switch. As with the commands <code>pick</code> and <code>mark</code>, you may also use the switches <code>-zero</code> and <code>-nozero</code> to specify whether to zero old sequences or not. Similarly, use of the <code>-public</code> and <code>-nopublic</code> switches may be used to force these sequences to be public or private sequences.</p>
<h3>LOCKING AND -unseen</h3>
<p> If you use the &#8220;Unseen-Sequence&#8221; profile entry, rcvstore could try to read and update its sequence state while another <code>nmh</code> process is also trying to do so. This can cause the sequence state to lose track. To avoid this just between asynchronous invocations of <code>rcvstore</code>, do not use it without an external locking mechanism, for example, a <i><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></i>(5) local lockfile, if you use the &#8220;Unseen-Sequence&#8221; profile entry.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Folder-Protect:~^To set mode when creating a new folder
^Inbox:~^To find the default inbox
^Msg-Protect:~^To set mode when creating a new message
^Unseen-Sequence:~^To name sequences denoting unseen messages
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rcvdist/">rcvdist</a></i>(1), <i><a href="/docs/linux/man/1-rcvpack/">rcvpack</a></i>(1), <i><a href="/docs/linux/man/1-rcvtty/">rcvtty</a></i>(1), <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5), <i><a href="/docs/linux/man/5-procmailex/">procmailex</a></i>(5), <i><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></i>(5)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to ``Inbox'' profile entry
`<code>-create</code>'
`<code>-unseen</code>'
`<code>-nozero</code>'
</pre>
<h2>CONTEXT</h2>
<p> No context changes will be attempted, with the exception of sequence manipulation. </p>
<h2>Index</h2>
