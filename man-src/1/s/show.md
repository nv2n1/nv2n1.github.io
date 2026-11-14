---
title: "show(1)"
name: "show"
section: "1"
letter: "s"
url: "/docs/linux/man/1-show/"
description: "show – show (display) messages"
---

<h2 class="name">NAME</h2>
<p> show &#8211; show (display) messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>show</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-draft</code>] [-showproc <i>program</i>] [<code>-showmimeproc</code> <i>program</i>] [<code>-header</code> | <code>-noheader</code>] [<code>-checkmime</code> | <code>-nocheckmime</code>] [switches for <i>showproc</i></p>
<dd>or <i>showmimeproc</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Show</code> lists each of the specified messages to the standard output (typically, the terminal). </p>
<p> By default, text (non-MIME) messages are filtered and displayed by the <code>nmh</code> command <code>mhl</code>. This command will display text messages in a nice, uniform format. It also allows you to configure the format of the displayed messages and which headers fields are shown. See the <i><a href="/docs/linux/man/1-mhl/">mhl</a></i>(1) manual page for the details about this command. This default can be changed by defining the <i>showproc</i> profile component. Any switches not recognized by <code>show</code> are passed along to that program. To override the default and the <i>showproc</i> profile component, use the <code>-showproc</code> <i>program</i> switch. For example, <code>-showproc</code> <i>more</i> will cause the <code>more</code> program to list the messages with no reformatting. Normally, this program is specified as the <i>showproc</i> in the user&#8217;s <i>.mh_profile</i>, rather than using a command line switch. </p>
<p> By default, non-text messages (MIME messages with multi-media contents) are processed and displayed by the <code>nmh</code> command <code>mhshow</code>. See the <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1) manual page for details about this command. This default can changed by defining the <i>showmimeproc</i> profile component. Any switches not recognized by <code>show</code> are passed along to that program. To override this default and the <code>showmimeproc</code> profile component, use the <code>-showmimeproc</code> <i>program</i> switch. </p>
<p> Note that in some cases, <code>show</code> may invoke the <i>showmimeproc</i> even for textual contents. This will happen for text messages that specify a transfer encoding (such as MIME quoted-printable or base64) or specify a character set that <code>show</code> doesn&#8217;t believe can be displayed natively. The appropriate <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) environment variables should be set to the terminal&#8217;s native character set to avoid gratuitous invocations of the <i>showmimeproc</i>. See the <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) man page for details about these environment variables. </p>
<p> The option <code>-checkmime</code> (set by default) instructs <code>show</code> to test if any of the messages to be displayed are non-text (MIME) messages. If any are non-text, they are displayed by the program <i>showmimeproc</i>, else they are displayed by the program <i>showproc</i>. The option <code>-nocheckmime</code> disables this test and instructs <code>show</code> to use <i>showproc</i>, regardless of whether any of the messages are non-text (MIME) messages. </p>
<p> The <code>-noshowproc</code> switch will disable any formatting or paging of messages. It is equivalent to <code>-nocheckmime</code> <code>-showproc</code> <i>cat</i>. It is still accepted, but should be considered (somewhat) obsolete. </p>
<p> The <code>-header</code> switch tells <code>show</code> to display a one-line description of the message being shown. This description includes the folder and the message number. </p>
<p> If no `msgs&#8217; are specified, the current message is used. Although it depends on the specific <i>showproc</i> or <i>showmimeproc</i>, in the default setup when more than one message is specified, you will be prompted for a &lt;RETURN&gt; prior to listing each message. Each message will be listed a page at a time, and when the end of page is reached, the program will wait for a &lt;SPACE&gt; or &lt;RETURN&gt;. If a &lt;RETURN&gt; is entered, it will print the next line, whereas &lt;SPACE&gt; will print the next screenful. </p>
<p> If the standard output is not a terminal, no queries are made, and each file is listed with a one-line header and two lines of separation. </p>
<p> &#8220;<code>show -draft</code>&#8221; will list the file &lt;mh-dir&gt;/draft if it exists. </p>
<p> If the profile entry &#8220;Unseen-Sequence&#8221; is present and non-empty, then <code>show</code> will remove each of the messages shown from each sequence named by the profile entry.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Unseen-Sequence:~^To name sequences denoting unseen messages
^showproc:~^Program to show text (non-MIME) messages
^showmimeproc:~^Program to show non-text (MIME) messages
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mhl/">mhl</a></i>(1), <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1), <i><a href="/docs/linux/man/1-next/">next</a></i>(1), <i><a href="/docs/linux/man/1-prev/">prev</a></i>(1), <i><a href="/docs/linux/man/1-scan/">scan</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-checkmime</code>'
`<code>-header</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The last message selected will become the current message.</p>
<h2>BUGS</h2>
<p> The <code>-header</code> switch doesn&#8217;t work when `msgs&#8217; expands to more than one message. If the <i>showproc</i> is <code>mhl</code>, then this problem can be circumvented by referencing the &#8220;messagename&#8221; field in the <code>mhl</code> format file. </p>
<p> <code>Show</code> updates the user&#8217;s context before showing the message. Hence <code>show</code> will mark messages as seen prior to the user actually seeing them. This is generally not a problem, unless the user relies on the &#8220;unseen&#8221; messages mechanism, and interrupts <code>show</code> while it is showing &#8220;unseen&#8221; messages. </p>
<p> If your <i>showproc</i> is <code>mhl</code> (the default), then <code>show</code> uses a built-in <code>mhl</code>: it does not actually run the <code>mhl</code> program. Hence, if you define your own <code>showproc ,</code> don&#8217;t call it <code>mhl</code> since <code>show</code> won&#8217;t run it. </p>
<p> If your <i>showproc</i> is the pager <code>more</code>, then avoid running <code>show</code> in the background with only its standard output piped to another process, as in </p>
<dl>
<dt>
<dd> show | imprint &amp;</dl>
<p> Due to a bug in <code>more</code>, show will go into a &#8220;tty input&#8221; state. To avoid this problem, re-direct <code>show</code>&#8216;s diagnostic output as well. For users of <code>csh</code>: </p>
<dl>
<dt>
<dd> show |&amp; imprint &amp;</dl>
<p> For users of <code>sh</code>: </p>
<dl>
<dt>
<dd> show 2&gt;&amp;1 | imprint &amp;</dl>
<h2>Index</h2>
