---
title: "talk(1)"
name: "talk"
section: "1"
letter: "t"
url: "/docs/linux/man/1-talk/"
description: "talk – talk to another user"
---

<h2 class="name">NAME</h2>
<p> <code>talk</code> &#8211; talk to another user </p>
<h2>SYNOPSIS</h2>
<p> <code>talk</code> <i>person</i> [<i>-x</i> ] [<i>ttyname</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Talk</code> is a visual communication program which copies lines from your terminal to that of another user. </p>
<p> Options available:</p>
<dl>
<dt><i>person</i></p>
<dd> If you wish to talk to someone on your own machine, then <i>person</i> is just the person&#8217;s login name. If you wish to talk to a user on another host, then <i>person</i> is of the form `user [at] host&#8217; ( or `host.user&#8217; or `host!user&#8217; or `host:user&#8217; ).</p>
<dt><i>-x</i></p>
<dd> If you wish to talk to a user who has dot character in username, the <i>-x</i> argument will force `user [at] host&#8217; form of the <i>person</i> and talk will take dots as part of user name.</p>
<dt><i>ttyname</i></p>
<dd> If you wish to talk to a user who is logged in more than once, the <i>ttyname</i> argument may be used to indicate the appropriate terminal name, where <i>ttyname</i> is of the form `ttyXX&#8217; or `pts/X&#8217;</dl>
<p> When first called, <code>talk</code> contacts the talk daemon on the other user&#8217;s machine, which sends the message </p>
<blockquote>
<pre><code>
Message from TalkDaemon[at] his_machine... talk : connection requested by your_name[at] your_machine.talk : respond with : talk your_name[at] your_machine
</code></pre>
</blockquote>
<p> to that user. At this point, he then replies by typing </p>
<blockquote><p><tt>talk &nbsp;<wbr>your_name [at] your_machine</tt></p></blockquote>
<p> It doesn&#8217;t matter from which machine the recipient replies, as long as his login name is the same. Once communication is established, the two parties may type simultaneously; their output will appear in separate windows. Typing control-L (^L) will cause the screen to be reprinted. The erase, kill line, and word erase characters (normally ^H, ^U, and ^W respectively) will behave normally. To exit, just type the interrupt character (normally ^C); <code>talk</code> then moves the cursor to the bottom of the screen and restores the terminal to its previous state. </p>
<p> As of netkit-ntalk 0.15 <code>talk</code> supports scrollback; use esc-p and esc-n to scroll your window, and ctrl-p and ctrl-n to scroll the other window. These keys are now opposite from the way they were in 0.16; while this will probably be confusing at first, the rationale is that the key combinations with escape are harder to type and should therefore be used to scroll one&#8217;s own screen, since one needs to do that much less often. </p>
<p> If you do not want to receive talk requests, you may block them using the <a href="/docs/linux/man/1-mesg/">mesg</a>(1) command. By default, talk requests are normally not blocked. Certain commands, in particular <a href="/docs/linux/man/1-nroff/">nroff</a>(1), <a href="/docs/linux/man/1-pine/">pine</a>(1), and <a href="/docs/linux/man/1-pr/">pr</a>(1), may block messages temporarily in order to prevent messy output. </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/hosts </code></p>
<dd> to find the recipient&#8217;s machine</p>
<dt><code>/var/run/utmp </code></p>
<dd> to find the recipient&#8217;s tty</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mail/">mail</a>(1), <a href="/docs/linux/man/1-mesg/">mesg</a>(1), <a href="/docs/linux/man/1-who/">who</a>(1), <a href="/docs/linux/man/1-write/">write</a>(1), <a href="/docs/linux/man/8-talkd/">talkd</a>(8)</p>
<h2>BUGS</h2>
<p> The protocol used to communicate with the talk daemon is braindead. </p>
<p> Also, the version of <a href="/docs/linux/man/1-talk/">talk</a>(1) released with BSD 4.2 uses a different and even more braindead protocol that is completely incompatible. Some vendor Unixes (particularly those from Sun) have been found to use this old protocol. </p>
<p> Old versions of <code>talk</code> may have trouble running on machines with more than one IP address, such as machines with dynamic SLIP or PPP connections. This problem is fixed as of netkit-ntalk 0.11, but may affect people you are trying to communicate with.</p>
<h2>HISTORY</h2>
<p> The <code>talk</code> command appeared in BSD 4.2 </p>
<h2>Index</h2>
