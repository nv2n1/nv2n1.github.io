---
title: "sendfiles(1)"
name: "sendfiles"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sendfiles/"
description: "sendfiles – send multiple files via a MIME message"
---

<h2 class="name">NAME</h2>
<p> sendfiles &#8211; send multiple files via a MIME message </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>sendfiles</code> [<code>-compress</code> <i>bzip2</i> | <i>compress</i> | <i>gzip</i> | <i>lzma</i> | <i>none</i>]</p>
<dd> [<code>-from</code> <i>sender</i>] [<i>-delay n</i> | <i>-n</i>] [<code>-version</code>] [<code>-help</code>]</p>
<dd> <code>-to</code> <i>recipient</i> <code>-subject</code> <i>subject</i> | <i>recipient</i> <i>subject</i></p>
<dd> <i>file/directory1</i> [<i>file/directory2</i> &#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>The shell script <code>sendfiles</code> is used to send a collection of files and directories via electronic mail. </p>
<p> <code>sendfiles</code> will archive the files and directories you name with the <code>tar</code> command, and then mail the compressed archive to the &#8220;recipient&#8221; with the given &#8220;subject&#8221;. The archive will be automatically split up into as many messages as necessary in order to get past most mailers. </p>
<p> The <code>-to</code> switch specifies the recipient. The <code>-subject</code> switch specifies the subject. Alternatively, these two required values can be provided without their corresponding switch names. </p>
<p> The <code>-from</code> switch can, and should, be used to specify the sender&#8217;s mailbox (name and email address). Alternatively, the <code>PERSON</code> environment variable can be used for the same purpose. If neither is used, <code>sendfiles</code> will supply a &#8220;From:&#8221; header field using the sender&#8217;s local mailbox, see <i>localmbox</i> in <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5). </p>
<p> The <code>-compress</code> command line switch can be used to override the run-time determination of the compression program by <code>sendfiles</code>. <code>-compress</code> <i>none</i> (alternatively, <code>-none</code>) disables compression. </p>
<p> Sometimes you want <code>sendfiles</code> to pause after posting a partial message. This is usually the case when you are running <code>sendmail</code> and expect to generate a lot of partial messages. The <code>-delay</code> switch specifies the number of seconds to pause in between postings, e.g., </p>
<dl>
<dt>
<dd> sendfiles -delay 30 -to recipient -subject &#8220;subject&#8221; files &#8230;</dl>
<p> will pause 30 seconds in between each posting. An alternate form of the switch with just the delay time, <code>-30</code>, for example, is also supported. </p>
<h3>Extracting the Received Files</h3>
<p> When these messages are received, invoke <code>mhstore</code> once for the list of messages. The default is for <code>mhstore</code> to store the combined parts as a new message in the current folder, although this can be changed using storage formatting strings. You can then use <code>mhlist</code> to find out what&#8217;s inside; possibly followed by <code>mhstore</code> again to write the archive to a file where you can subsequently uncompress and untar it. For instance: </p>
<dl>
<dt>
<dd>
<pre>
% mhlist 5-8
 msg part  type/subtype             size description
   5       message/partial           47K part 1 of 4
   6       message/partial           47K part 2 of 4
   7       message/partial           47K part 3 of 4
   8       message/partial           18K part 4 of 4
% mhstore 5-8
reassembling partials 5,6,7,8 to folder inbox as message 9
% mhlist -verbose 9
 msg part  type/subtype             size description
   9       application/octet-stream 118K
             (extract with uncompress | tar xvpf -)
             type=tar
             conversions=compress
% mhstore 9
% uncompress &lt; 9.tar.Z | tar xvpf -
</pre>
</dl>
<p> Alternately, by using the <code>-auto</code> switch, <code>mhstore</code> will automatically do the extraction for you: </p>
<dl>
<dt>
<dd>
<pre>
% mhlist 5-8
 msg part  type/subtype             size description
   5       message/partial           47K part 1 of 4
   6       message/partial           47K part 2 of 4
   7       message/partial           47K part 3 of 4
   8       message/partial           18K part 4 of 4
% mhstore 5-8
reassembling partials 5,6,7,8 to folder inbox as message 9
% mhlist -verbose 9
 msg part  type/subtype             size description
   9       application/octet-stream 118K
             (extract with uncompress | tar xvpf -)
             type=tar
             conversions=compress
% mhstore -auto 9
-- tar listing appears here as files are extracted
</pre>
</dl>
<p> As the second <code>tar</code> listing is generated, the files are extracted. A prudent user will never put <code>-auto</code> in the <i>.mh_profile</i> file. The correct procedure is to first use <code>mhlist</code> to find out what will be extracted. Then <code>mhstore</code> can be invoked with <code>-auto</code> to perform the extraction.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-mhlist/">mhlist</a></i>(1), <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1), <i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) </p>
<p> <i>Proposed Standard for Message Encapsulation</i> (RFC 934)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-delay 0</code>'
`<code>-from localmbox</code>'
</pre>
<h2>CONTEXT</h2>
<p> None </p>
<h2>Index</h2>
