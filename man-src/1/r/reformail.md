---
title: "reformail(1)"
name: "reformail"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reformail/"
description: "reformail – E-mail reformatting tool"
---

<h2 class="name">NAME</h2>
<p> reformail &#8211; E-mail reformatting tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>reformail</code> -s command [option&#8230;]</p>
<dt> <code>reformail</code> -D len <i>filename</i></p>
<dt> <code>reformail</code> -x&nbsp;<wbr><i>header:</i>&#8230;</p>
<dt> <code>reformail</code> -X&nbsp;<wbr><i>header:</i>&#8230;</p>
<dt> <code>reformail</code> [<i>options</i>&#8230;] </p>
<dd>See below for additional options</dl>
<h2>DESCRIPTION</h2>
<p> The <code>reformail</code> program reads a message on standard input, reformats it in some way, and writes the message to standard output:</p>
<h3>Splitting mailboxes into individual messages</h3>
<p> The <code>-s</code> option splits the mbox-formatted mailbox file on standard input into individual messages. An external program is executed for each message. The contents of each individual message will be provided to the external program on standard input. </p>
<p> If the <code>FILENO</code> environment variable is set to a number, <code>reformail</code> will consecutively increment <code>FILENO</code> each time the program is executed for each individual message. </p>
<p> If <code>FILENO</code> is not set, it&#8217;s initial value will be &quot;000&quot;. If <code>FILENO</code> is set to a non-numeric value, <code>FILENO</code> will remain unchanged.</p>
<h3>Detecting duplicate messages</h3>
<p> The <code>-D</code> option implements a simple way to delete duplicate messages in incoming mail. <i>filename</i> is a file that will be approximately &#8216;<i>len</i>&#8216; bytes long. This file will be used by <code>reformail</code> to save message IDs seen in recent mail. <code>reformail</code> reads the message on standard input. If the message has a Message-ID: header that&#8217;s already in the cache file, <code>reformail</code> terminates with the exit code set to 0. Otherwise, <code>reformail</code> terminates with the exit code set to 1. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Unlike a similar feature in the <code>formail</code> command, <code>reformail</code> takes care of locking the file, so it&#8217;s not necessary to implement your own locking mechanism for this option. </p>
</dl>
<h3>Extracting headers</h3>
<p> The <code>-x</code> and <code>-X</code> options extract the indicated headers from the message, and print them to standard output. Multiple <code>-x</code> and <code>-X</code> options can be specified at the same time, and may be intermixed. </p>
<p> The <code>-x</code> option extracts and prints the contents of the header. The <code>-X</code> option prints the name of the header as well. </p>
<p> In all other situations, <code>reformail</code> copies the message on its standard input to its standard output, reformatting the message as follows:</p>
<h2>OPTIONS</h2>
<p> -a&#8217;header: value&#8217;</p>
<dl>
<dt>
<dd> Append a custom header to the message if this header does not already exist. If the header is either Message-ID: or Resent-Message-ID: and the value is empty, <code>reformail</code> generates a (hopefully) unique message ID for you.</dl>
<p> -A&#8217;header: value&#8217;</p>
<dl>
<dt>
<dd> Append a custom header to the message even if this header already exists. If the header is either Message-ID: or Resent-Message-ID: and the value is empty, <code>reformail</code> generates a (hopefully) unique message ID for you.</dl>
<p> -c</p>
<dl>
<dt>
<dd> Concatenate multi-line headers. Headers split on multiple lines are combined into a single line.</dl>
<p> -d<i>n</i></p>
<dl>
<dt>
<dd> If n is 1, each line will be terminated with CRLF. If n is 0 (default), each line will be terminated with LF. <code>reformail</code> reads a message with either line terminator, and will force the message to have the specified line termination.</dl>
<p> -f0</p>
<dl>
<dt>
<dd> Any initial blank lines are removed. If the first non-blank line is a &quot;From_&quot; line, it gets converted to a &quot;Return-Path:&quot; header, and any existing &quot;Return-Path:&quot; header gets removed. If the message does not start with a &quot;From_&quot; line, the message remains unchanged.</dl>
<p> -f1</p>
<dl>
<dt>
<dd> Add the &quot;From_&quot; line to the message, if it&#8217;s not there. <code>reformail</code> will attempt to generate the &quot;From_&quot; line from any Errors-To:, Return-Path:, or From: headers in the message. &quot;root&quot; will be used if <code>reformail</code> is unable to determine the return address.</dl>
<p> -i&#8217;<i>header: value</i>&#8216;</p>
<dl>
<dt>
<dd> Appends a custom header to the message. If this header already exists it is renamed by prepending &quot;Old-&quot; to the name of the header.</dl>
<p> -I&#8217;<i>header: value</i>&#8216;</p>
<dl>
<dt>
<dd> Append a custom header to the message. If this header already exists in the message, the old header is completely removed. If the value is empty, any existing header is completely removed, and nothing gets appended.</dl>
<p> -R oldheader: newheader:</p>
<dl>
<dt>
<dd> Rename the indicated header.</dl>
<p> -u&#8217;header:&#8217;</p>
<dl>
<dt>
<dd> If this header occurs multiple times in the message, remove all occurrences except the first one.</dl>
<p> -U&#8217;header:&#8217;</p>
<dl>
<dt>
<dd> If this header occurs multiple times in the message, remove all occurrences except the last one.</dl>
<h2>AUTOREPLIES</h2>
<p> The autoreply options from earlier versions of <code>mailbot</code> have been moved into m[blue]<code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)m[]<font SIZE="-2">[1]</font>.</p>
<h2>BUGS</h2>
<p> For the <code>-a</code>, <code>-A</code>, and <code>-I</code> options, a space after the header name and the colon is considered to be a non-empty field. </p>
<p> Do not provide the same header to more than one family of header-modifying options, such as <code>-u</code>/<code>-U</code> and <code>-a</code>/<code>-A</code>. Doing so yields unpredictable results. It&#8217;s better to run <code>reformail</code> several times (use a pipe, perhaps).</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a href="/docs/linux/man/8-courier/">courier</a></code>(8)m[]<font SIZE="-2">[2]</font>, <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), m[blue]<code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)m[]<font SIZE="-2">[1]</font>, m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[3]</font>.</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd> Author</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/mailbot.html">http://www.courier-mta.org/maildrop/mailbot.html</a></dl>
<dt> 2.</p>
<dd> <code><a href="/docs/linux/man/8-courier/">courier</a></code>(8)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/courier.html">http://www.courier-mta.org/maildrop/courier.html</a></dl>
<dt> 3.</p>
<dd> <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildrop.html">http://www.courier-mta.org/maildrop/maildrop.html</a></dl>
</dl>
<h2>Index</h2>
