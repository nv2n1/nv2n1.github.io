---
title: "slocal(1)"
name: "slocal"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slocal/"
description: "slocal – asynchronously filter and deliver new mail"
---

<h2 class="name">NAME</h2>
<p> slocal &#8211; asynchronously filter and deliver new mail </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/slocal</code> [<code>-addr</code> <i>address</i>] [<code>-info</code> <i>data</i>] [<code>-sender</code> <i>sender</i>] [<code>-user</code> <i>username</i>] [<code>-mailbox</code> <i>mbox</i>] [<code>-file</code> <i>file</i>] [<code>-maildelivery</code> <i>deliveryfile</i>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-suppressdup</code> | <code>-nosuppressdup</code>] [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Slocal</code></p>
<dd>is a program designed to allow you to have your inbound mail processed according to a complex set of selection criteria. You do not normally invoke <code>slocal</code> yourself, rather <code>slocal</code> is invoked on your behalf by your system&#8217;s Message Transfer Agent (such as <code>sendmail</code>) when the message arrives. </p>
<p> The message selection criteria used by <code>slocal is specified</code> in the file &#8220;<i>.maildelivery</i>&#8221; in the user&#8217;s home directory. You can specify an alternate file with the <code>-maildelivery</code> <i>file</i> option. The syntax of this file is specified below. </p>
<p> The message delivery address and message sender are determined from the Message Transfer Agent envelope information, if possible. Under <code>sendmail</code>, the sender will obtained from the UUCP &#8220;From:&#8221; line, if present. The user may override these values with the <code>-addr</code> and <code>-sender</code> switches. </p>
<p> The message is normally read from the standard input. The <code>-file</code> switch sets the name of the file from which the message should be read, instead of reading stdin. This is useful when debugging a &#8220;<i>.maildelivery</i>&#8221; file. </p>
<p> The <code>-user</code> switch tells <code>slocal</code> the name of the user for whom it is delivering mail. The <code>-mailbox</code> switch tells <code>slocal</code> the name of the user&#8217;s maildrop file. </p>
<p> <code>slocal</code> is able to detect and suppress duplicate messages. To enable this, use the option <code>-suppressdup</code>. <code>slocal</code> will keep a database containing the Message-ID&#8217;s of incoming messages, in order to detect duplicates. Depending on your configuration, this database will be in either ndbm or Berkeley db format. </p>
<p> The <code>-info</code> switch may be used to pass an arbitrary argument to sub-processes which <code>slocal</code> may invoke on your behalf. </p>
<p> The <code>-verbose</code> switch causes <code>slocal</code> to give information on stdout about its progress. The <code>-debug</code> switch produces more verbose debugging output on stderr. These flags are useful when creating and debugging your &#8220;<i>.maildelivery</i>&#8221; file, as they allow you to see the decisions and actions that <code>slocal</code> is taking, as well as check for syntax errors in your &#8220;<i>.maildelivery</i>&#8221; file.</p>
<h3>Message Transfer Agents</h3>
<p> Most modern MTAs including <code>sendmail</code>, <code>postfix</code> and <code>exim</code> support a .forward file for directing incoming mail. You should include the line </p>
<p> <center> &#8220;|&nbsp;<wbr>/usr/libexec/nmh/slocal -user username&#8221;<br />
 </center> </p>
<p> in your .forward file in your home directory. This will cause your MTA to invoke <code>slocal</code> on your behalf when a message arrives.</p>
<h3>The Maildelivery File</h3>
<p> The &#8220;<i>.maildelivery</i>&#8221; file controls how <code>slocal</code> filters and delivers incoming mail. Each line of this file consists of five fields, separated by whitespace or comma. Since double-quotes are honored, these characters may be included in a single argument by enclosing the entire argument in double-quotes. A double-quote can be included by preceding it with a backslash. Lines beginning with `#&#8217; and blank lines are ignored. </p>
<p> The format of each line in the &#8220;<i>.maildelivery</i>&#8221; file is: </p>
<dl>
<dt>
<dd> <code>header<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pattern<tt>&nbsp;<wbr></tt>action<tt>&nbsp;<wbr>&nbsp;<wbr></tt>result<tt>&nbsp;<wbr>&nbsp;<wbr></tt>string</code></dl>
<p> <code>header</code>:</p>
<dl>
<dt>
<dd> The name of a header field (such as To, Cc, or From) that is to<br />
 be searched for a pattern. This is any field in the headers of the message that might be present. </p>
<p> The following special fields are also defined:</p>
<dl>
<dt><i>source</i></p>
<dd> the out-of-band sender information</p>
<dt><i>addr</i></p>
<dd> the address that was used to cause delivery to the recipient</p>
<dt><i>default</i></p>
<dd> this matches <code>only</code> if the message hasn&#8217;t been delivered yet</p>
<dt><i>*</i></p>
<dd> this always matches</dl>
</dl>
<p> <code>pattern</code>:</p>
<dl>
<dt>
<dd> The sequence of characters to match in the specified header field. Matching is case-insensitive, but does not use regular expressions.</dl>
<p> <code>action</code>:</p>
<dl>
<dt>
<dd> The action to take to deliver the message. When a message is delivered, a &#8220;Delivery-Date: date&#8221; header is added which indicates the date and time that message was delivered.</p>
<dl>
<dt><i>destroy</i></p>
<dd> This action always succeeds.</p>
<dt><i>file</i>, <i>mbox</i>, or <i>&gt;</i></p>
<dd> Append the message to the file named by <i>string</i>. The message is appended to the file in mbox (uucp) format. This is the format used by most other mail clients (such as mailx, elm). If the message can be appended to the file, then this action succeeds.</p>
<dt><i>mmdf</i></p>
<dd> Identical to <i>file</i>, but always appends the message using the MMDF mailbox format.</p>
<dt><i>pipe</i> or <i>|</i></p>
<dd> Pipe the message as the standard input to the command named by <i>string</i>, using the Bourne shell <code>sh</code> to interpret the string. Prior to giving the string to the shell, it is expanded with the following built-in variables:</p>
<dl>
<dt>
<dd>
<dl>
<dt>$(sender)</p>
<dd> the out-of-band sender information</p>
<dt>$(address)</p>
<dd> the address that was used to cause delivery to the recipient</p>
<dt>$(size)</p>
<dd> the size of the message in bytes</p>
<dt>$(reply-to)</p>
<dd> either the &#8220;Reply-To:&#8221; or &#8220;From:&#8221; field of the message</p>
<dt>$(info)</p>
<dd> the out-of-band information specified</dl>
</dl>
<dt><i>qpipe</i> or <i>^</i></p>
<dd> Similar to <i>pipe</i>, but executes the command directly, after built-in variable expansion, without assistance from the shell. This action can be used to avoid quoting special characters which your shell might interpret.</p>
<dt><i>folder</i> or <i>+</i></p>
<dd> Store the message in the <code>nmh</code> folder named by <i>string</i>. Currently this is handled by piping the message to the <code>nmh</code> program <code>rcvstore</code>, although this may change in the future.</dl>
</dl>
<p> <code>result</code>:</p>
<dl>
<dt>
<dd> Indicates how the action should be performed:</p>
<dl>
<dt><i>A</i></p>
<dd> Perform the action. If the action succeeds, then the message is considered delivered.</p>
<dt><i>R</i></p>
<dd> Perform the action. Regardless of the outcome of the action, the message is not considered delivered.</p>
<dt><i>?</i></p>
<dd> Perform the action only if the message has not been delivered. If the action succeeds, then the message is considered delivered.</p>
<dt><i>N</i></p>
<dd> Perform the action only if the message has not been delivered and the previous action succeeded. If this action succeeds, then the message is considered delivered.</dl>
<p> The delivery file is always read completely, so that several matches can be made and several actions can be taken.</dl>
<h3>Security of Delivery Files</h3>
<p> In order to prevent security problems, the &#8220;<i>.maildelivery</i>&#8221; file must be owned either by the user or by root, and must be writable only by the owner. If this is not the case, the file is not read. </p>
<p> If the &#8220;<i>.maildelivery</i>&#8221; file cannot be found, or does not perform an action which delivers the message, then <code>slocal</code> will check for a global delivery file at <i>/etc/nmh/maildelivery</i>. This file is read according to the same rules. This file must be owned by root and must be writable only by root. </p>
<p> If a global delivery file cannot be found or does not perform an action which delivers the message, then standard delivery to the user&#8217;s maildrop is performed.</p>
<h3>Example Delivery File</h3>
<p> To summarize, here&#8217;s an example delivery file: </p>
<pre>
#
# .maildelivery file for nmh's slocal
#
# Blank lines and lines beginning with a '#' are ignored
#
# FIELD   PATTERN   ACTION  RESULT  STRING
#
# File mail with foobar in the ``To:'' line into file foobar.log
To        foobar    file    A       foobar.log
# Pipe messages from coleman to the program message-archive
From      coleman   pipe    A       /bin/message-archive
# Anything to the ``nmh-workers'' mailing list is put in
# its own folder, if not filed already
To        nmh-workers  folder ?     nmh-workers
# Anything with Unix in the subject is put into
# the file unix-mail
Subject   unix      file    A       unix-mail
# I don't want to read mail from Steve, so destroy it
From      steve     destroy A       -
# Put anything not matched yet into mailbox
default   -        file    ?       mailbox
# always run rcvtty
*         -        pipe    R       /usr/libexec/nmh/rcvtty
</pre>
<h3>Sub-process environment</h3>
<p> When a process is invoked, its environment is: the user/group-ids are set to recipient&#8217;s ids; the working directory is the recipient&#8217;s home directory; the umask is 0077; the process has no /dev/tty; the standard input is set to the message; the standard output and diagnostic output are set to /dev/null; all other file-descriptors are closed; the environment variables <code>$USER</code>, <code>$HOME</code>, <code>$SHELL</code> are set appropriately, and no other environment variables exist. </p>
<p> The process is given a certain amount of time to execute. If the process does not exit within this limit, the process will be terminated with extreme prejudice. The amount of time is calculated as ((size / 60) + 300) seconds, where size is the number of bytes in the message (with 30 minutes the maximum time allowed). </p>
<p> The exit status of the process is consulted in determining the success of the action. An exit status of zero means that the action succeeded. Any other exit status (or abnormal termination) means that the action failed. </p>
<p> In order to avoid any time limitations, you might implement a process that began by <i>fork</i>()-ing. The parent would return the appropriate value immediately, and the child could continue on, doing whatever it wanted for as long as it wanted. This approach is somewhat risky if the parent is going to return an exit status of zero. If the parent is going to return a non-zero exit status, then this approach can lead to quicker delivery into your maildrop.</p>
<h2>FILES</h2>
<pre>
^/etc/nmh/mts.conf~^nmh mts configuration file
^$HOME/.maildelivery~^The file controlling local delivery
^/etc/nmh/maildelivery~^Rather than the standard file
^/var/mail/$USER~^The default maildrop
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rcvdist/">rcvdist</a></i>(1), <i><a href="/docs/linux/man/1-rcvpack/">rcvpack</a></i>(1), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1), <i><a href="/docs/linux/man/1-rcvtty/">rcvtty</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-noverbose</code>'
`<code>-nosuppressdup</code>'
`<code>-maildelivery</code>' defaults to $HOME/.maildelivery
`<code>-mailbox</code>' deaults to /var/mail/$USER
`<code>-file</code>' defaults to stdin
`<code>-user</code>' defaults to the current user
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>HISTORY</h2>
<p> <code>Slocal</code> was originally designed to be backward-compatible with the <code>maildelivery</code> facility provided by <code>MMDF-II</code>. Thus, the &#8220;<i>.maildelivery</i>&#8221; file syntax is somewhat limited. But <code>slocal</code> has been modified and extended, so that is it no longer compatible with <code>MMDF-II</code>. </p>
<p> In addition to an exit status of zero, the <code>MMDF</code> values <code>RP_MOK</code> (32) and <code>RP_OK</code> (9) mean that the message has been fully delivered. Any other non-zero exit status, including abnormal termination, is interpreted as the <code>MMDF</code> value <code>RP_MECH</code> (200), which means &#8220;use an alternate route&#8221; (deliver the message to the maildrop).</p>
<h2>BUGS</h2>
<p> Only two return codes are meaningful, others should be. </p>
<p> <code>Slocal</code> was originally designed to be backwards-compatible with the <code>maildelivery</code> functionality provided by <code>MMDF-II</code>. </p>
<h2>Index</h2>
