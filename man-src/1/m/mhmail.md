---
title: "mhmail(1)"
name: "mhmail"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhmail/"
description: "mhmail – send or read mail"
---

<h2 class="name">NAME</h2>
<p> mhmail &#8211; send or read mail </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhmail</code> [<code>-to</code>] addrs &#8230; [<code>-attach</code> <i>file</i>] [<code>-body</code> <i>text</i>] [<code>-cc</code> <i>addrs</i> &#8230;] [<code>-from</code> <i>addr</i>] [<code>-headerfield</code> <i>name:value</i>] [<code>-subject</code> <i>subject</i>] [<code>-resent</code>] [switches for <i>post</i> &#8230; | -profile [switches for <i>send</i> &#8230;]] [<code>-send</code> | <code>-nosend</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<dl>
<dt> <code>mhmail</code></p>
<dd>with no arguments is equivalent to <code>inc</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>mhmail</code> is intended as a replacement for the standard Berkeley mail program (<code>mail</code> or <code>mailx</code>), which is compatible with <code>nmh</code>. This program is intended for the use of programs such as <code>cron</code>, which expect to send mail automatically to various addresses. It is also used by various <code>nmh</code> commands to mail various error notifications. Although <code>mhmail</code> can be used interactively, it is recommended that <code>comp</code> and <code>send</code> be used instead to send messages. </p>
<p> When invoked without arguments, it simply invokes <code>inc</code> to incorporate new messages from the user&#8217;s maildrop. </p>
<p> When one or more addresses are specified, a message is read from the standard input and spooled to a temporary file. <code>mhmail</code> then invokes <code>post</code>, by default, with the name of the temporary file as its argument to deliver the message to the specified address. </p>
<p> The <code>-subject</code> <i>subject</i> switch can be used to specify the &#8220;Subject:&#8221; field of the message. </p>
<p> The <code>-resent</code> switch indicates that the message body is a fully formed message that will be resent, as <code>dist</code> would do. For example: </p>
<dl>
<dt>
<dd>
<pre>
mhmail u2 [at] example.com -resent &lt; `mhpath cur`
</pre>
</dl>
<p> By default, <code>mhmail</code> will read the message to be sent from the standard input. You can specify the text of the message at the command line with the <code>-body</code> <i>text</i> switch. If the standard input has zero length, <code>mhmail</code> will not send the message and return with status 1. You can use the switch <code>-body</code> &#8220;&#8221; to force an empty message. </p>
<p> Normally, addresses appearing as arguments are put in the &#8220;To:&#8221; field. At least one such address is required when sending a message, i.e., if any other switches are supplied. If the <code>-cc</code> switch is used, all addresses following it, even if there are intervening switches other than <code>-to</code>, are placed in the &#8220;cc:&#8221; field. The optional <code>-to</code> switch can appear in front of any addresses to signify their placement in the &#8220;To:&#8221; field. The <code>-to</code> and <code>-cc</code> switches may be given multiple times. </p>
<p> By using <code>-from</code> <i>addr</i>, you can specify the &#8220;From:&#8221; header of the draft. If no <code>-from</code> switch is used when sending, <code>mhmail</code> will supply a &#8220;From:&#8221; header field using the sender&#8217;s local mailbox, see <i>localmbox</i> in <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5). Naturally, <code>post</code> will fill-in the &#8220;Sender:&#8221; header correctly. </p>
<p> The <code>-headerfield</code> <i>name:value</i> switch adds a header field with the specified name and value to the message. (The <i>value</i> is called the <i>field body</i> in RFC 2822, but that&#8217;s too easily confused with the message body.) There need not be a space after the colon that separates the name and value in the argument to this switch. It is usually best to enclose the argument in quotes to protect it from the shell. The <code>-headerfield</code> switch may be given multiple times to add multiple header fields, for example, </p>
<dl>
<dt>
<dd>
<pre><code>
mhmail - from sender[at] example.com - headerfield 'MIME-Version:1.0' - headerfield 'Content-Type:text/plain; charset=utf-8' - headerfield 'Content-Transfer-Encoding:8bit' recipient[at] example.com
</code></pre>
</dl>
<p> Note about this example: the <code>-attach</code> switch causes <i>MIME-Version</i> and <i>Content-Type</i> headers to be added to the message. </p>
<p> The <code>-profile</code> switch instructs <code>mhmail</code> to use <code>send</code> instead of <code>post</code> to send the message. This allows use of the user&#8217;s context and aliases. </p>
<p> The <code>-attach</code> <i>file</i> switch attaches the specified file to the message. Use of <code>-attach</code> enables <code>-profile</code> because <code>mhmail</code> uses <code>send</code> to handle the attachment. It is usually best to enclose the argument in quotes to protect it from the shell. The <code>-attach</code> switch may be given multiple times to add multiple attachments. </p>
<p> The <code>-nosend</code> option shows the draft file that would be posted/sent on the command&#8217;s standard output but does not post or send it. <code>-send</code> provides the default behavior of posting or sending the message. It can be used to disable <code>-nosend</code>, for example, when using a shell alias. </p>
<p> All other switches are passed on to <code>post</code> if <code>-profile</code> is not used, or <code>send</code> if <code>-profile</code> is used.</p>
<h2>FILES</h2>
<pre>
^/usr/bin/inc~^Program to incorporate maildrop into folder
^/usr/libexec/nmh/post~^Program to deliver a message
^/tmp/mhmail*~^Temporary copy of message
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dist/">dist</a></i>(1), <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5), <i><a href="/docs/linux/man/8-post/">post</a></i>(8)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-from localmbox</code>'
`<code>-profile</code>' is enabled by default only with <code>-attach</code>
`<code>-send</code>'
</pre>
<h2>CONTEXT</h2>
<p> If <code>inc</code> is invoked, then <code>inc</code>&#8216;s context changes occur. With the <code>-profile</code> switch, the context of <code>send</code> is used. <code>mhmail</code> does not read the context file itself, so an entry for it will be ignored. </p>
<h2>Index</h2>
