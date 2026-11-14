---
title: "mh-mail(5)"
name: "mh-mail"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-mail/"
description: "mh-mail – message format for nmh message system"
---

<p>mh-mail &#8211; message format for nmh message system</p>
<h2>Description</h2>
<p><code>nmh</code> processes messages in a particular format. It should be noted that although neither Bell nor Berkeley mailers produce message files in the format that <code>nmh</code> prefers, <code>nmh</code> can read message files in that antiquated format. </p>
<p> Each user possesses a mail drop box which initially receives all messages processed by <code>post</code>. <code>Inc</code> will read from that drop box and incorporate the new messages found there into the user&#8217;s own mail folders (typically &#8220;<i>+inbox</i>&#8221;). The mail drop box consists of one or more messages. </p>
<p> Messages are expected to consist of lines of text. Graphics and binary data are not handled. No data compression is accepted. All text is clear ASCII 7-bit data. </p>
<p> The general &#8220;memo&#8221; framework of RFC 822 is used. A message consists of a block of information in a rigid format, followed by general text with no specified format. The rigidly formatted first part of a message is called the header, and the free-format portion is called the body. The header must always exist, but the body is optional. These parts are separated by an empty line, i.e., two consecutive newline characters. Within <code>nmh</code>, the header and body may be separated by a line consisting of dashes: </p>
<dl>
<dd>
<pre>From: Local Mailbox &lt;user [at] example.com&gt;
To:
cc:
Fcc: +outbox
Subject:</pre>
</dl>
<p> The header is composed of one or more header items. Each header item can be viewed as a single logical line of ASCII characters. If the text of a header item extends across several real lines, the continuation lines are indicated by leading spaces or tabs. </p>
<p> Each header item is called a component and is composed of a keyword or name, along with associated text. The keyword begins at the left margin, may NOT contain spaces or tabs, may not exceed 63 characters (as specified by RFC 822), and is terminated by a colon (`:&#8217;). Certain components (as identified by their keywords) must follow rigidly defined formats in their text portions. </p>
<p> The text for most formatted components (e.g., &#8220;Date:&#8221; and &#8220;Message-Id:&#8221;) is produced automatically. The only ones entered by the user are address fields such as &#8220;To:&#8221;, &#8220;cc:&#8221;, etc. Internet addresses are assigned mailbox names and host computer specifications. The rough format is &#8220;local [at] domain&#8221;, such as &#8220;MH@UCI&#8221;, or &#8220;MH [at] UCI-ICSA.ARPA&#8221;. Multiple addresses are separated by commas. A missing host/domain is assumed to be the local host/domain. </p>
<p> As mentioned above, a blank line (or a line of dashes) signals that all following text up to the end of the file is the body. No formatting is expected or enforced within the body. </p>
<p> Following is a list of header components that are considered meaningful to various <code>nmh</code> programs. </p>
<p> <code>Date</code>:</p>
<dl>
<dd>Added by <code>post</code>, contains date and time of the message&#8217;s entry into the mail transport system.</dl>
<p> <code>From</code>:</p>
<dl>
<dd>This header is filled in by default with the system&#8217;s idea of the user&#8217;s local mailbox. This can be changed with the <code>Local-Mailbox</code> profile entry. It contains the address of the author or authors (may be more than one if a &#8220;Sender:&#8221; field is present). For a standard reply (using <code>repl</code>), the reply address is constructed by checking the following headers (in this order): &#8220;Mail-Reply-To:&#8221;, &#8220;Reply-To:&#8221;, &#8220;From:&#8221;, &#8220;Sender:&#8221;. A &#8220;From:&#8221; header MUST exist when the message is sent to <code>post,</code> otherwise the message will be rejected.</dl>
<p> <code>Envelope-From</code>:</p>
<dl>
<dd>Used by <code>post</code> to specify a value for the sender&#8217;s envelope address to the mail transport system. If omitted, <code>post</code> will use the value of the &#8220;Sender:&#8221; or the &#8220;From:&#8221; header. See <i><a href="/docs/linux/man/1-send/">send</a></i>(1) for more details.</dl>
<p> <code>Mail-Reply-To</code>:</p>
<dl>
<dd>For a standard reply (using <code>repl</code>), the reply address is constructed by checking the following headers (in this order): &#8220;Mail-Reply-To:&#8221;, &#8220;Reply-To:&#8221;, &#8220;From:&#8221;, &#8220;Sender:&#8221;.</dl>
<p> <code>Mail-Followup-To</code>:</p>
<dl>
<dd>When making a &#8220;group&#8221; reply (using <code>repl</code> <code>-group</code>), any addresses in this field will take precedence, and no other reply address will be added to the draft. If this header is not available, then the return addresses will be constructed from the &#8220;Mail-Reply-To:&#8221;, or &#8220;Reply-To:&#8221;, or &#8220;From:&#8221;, along with adding the addresses from the headers &#8220;To:&#8221;, &#8220;cc:&#8221;, as well as adding your personal address.</dl>
<p> <code>Reply-To</code>:</p>
<dl>
<dd>For a standard reply (using <code>repl</code>), the reply address is constructed by checking the following headers (in this order): &#8220;Mail-Reply-To:&#8221;, &#8220;Reply-To:&#8221;, &#8220;From:&#8221;, &#8220;Sender:&#8221;.</dl>
<p> <code>Sender</code>:</p>
<dl>
<dd>Required by <code>post</code> in the event that the message has multiple addresses on the &#8220;From:&#8221; line. It is otherwise optional. This line should contain the address of the actual sender.</dl>
<p> <code>To</code>:</p>
<dl>
<dd>Contains addresses of primary recipients.</dl>
<p> <code>cc</code>:</p>
<dl>
<dd>Contains addresses of secondary recipients.</dl>
<p> <code>Bcc</code>:</p>
<dl>
<dd>Still more recipients. However, the &#8220;Bcc:&#8221; line is not copied onto the message as delivered, so these recipients are not listed. <code>nmh</code> uses an encapsulation method for blind copies, see <i><a href="/docs/linux/man/1-send/">send</a></i>(1).</dl>
<p> <code>Dcc</code>:</p>
<dl>
<dd>Still more recipients. However, the &#8220;Dcc:&#8221; line is not copied onto the messages as delivered. Recipients on the &#8220;Dcc:&#8221; line receive the same messsage as recipients on the &#8220;To:&#8221; and &#8220;cc:&#8221; lines. See <i><a href="/docs/linux/man/1-send/">send</a></i>(1) for more details. <code>Dcc</code> is not supported with the <code>sendmail/pipe</code> mail transport method.</dl>
<p> <code>Fcc</code>:</p>
<dl>
<dd>Causes <code>post</code> to copy the message into the specified folder for the sender, if the message was successfully given to the transport system.</dl>
<p> <code>Message-ID</code>:</p>
<dl>
<dd>A unique message identifier added by <code>post</code> if the <code>-msgid</code> flag is set.</dl>
<p> <code>Subject</code>:</p>
<dl>
<dd>Sender&#8217;s commentary. It is displayed by <code>scan</code>.</dl>
<p> <code>In-Reply-To</code>:</p>
<dl>
<dd>A commentary line added by <code>repl</code> when replying to a message.</dl>
<p> <code>Resent-Date</code>:</p>
<dl>
<dd>Added when redistributing a message by <code>post</code>.</dl>
<p> <code>Resent-From</code>:</p>
<dl>
<dd>Used instead of the &#8220;From:&#8221; header when <code>post </code> redistributes a message. See &#8220;From:&#8221; for more information about this header is used.</dl>
<p> <code>Resent-To:</code></p>
<dl>
<dd>New recipients for a message resent by <code>dist</code>.</dl>
<p> <code>Resent-cc</code>:</p>
<dl>
<dd>Still more recipients. See &#8220;cc:&#8221; and &#8220;Resent-To:&#8221;.</dl>
<p> <code>Resent-Bcc</code>:</p>
<dl>
<dd>Even more recipients. See &#8220;Bcc:&#8221; and &#8220;Resent-To:&#8221;.</dl>
<p> <code>Resent-Fcc</code>:</p>
<dl>
<dd>Copy resent message into a folder. See &#8220;Fcc:&#8221; and &#8220;Resent-To:&#8221;.</dl>
<p> <code>Resent-Message-Id</code>:</p>
<dl>
<dd>A unique identifier glued on by <code>post</code> if the <code>-msgid</code> flag is set. See &#8220;Message-Id:&#8221; and &#8220;Resent-To:&#8221;.</dl>
<p> <code>Resent</code>:</p>
<dl>
<dd>Annotation for <code>dist</code> under the <code>-annotate</code> option.</dl>
<p> <code>Forwarded</code>:</p>
<dl>
<dd>Annotation for <code>forw</code> under the <code>-annotate</code> option.</dl>
<p> <code>Replied</code>:</p>
<dl>
<dd>Annotation for <code>repl</code> under the <code>-annotate</code> option.</dl>
<p> <code>Attach</code>:</p>
<dl>
<dd>Used by <code>mhbuild</code> to specify a filename to attach to this message. See <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1) for more information.</dl>
<h2>Files</h2>
<pre>^/var/mail/$USER~^Location of mail drop</pre>
<h2>See Also</h2>
<p><i>Standard for the Format of ARPA Internet Text Messages</i> (RFC 822)</p>
<h2>Context</h2>
<p>None</p>
