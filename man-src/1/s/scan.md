---
title: "scan(1)"
name: "scan"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scan/"
description: "scan – produce a one line per message scan listing"
---

<h2 class="name">NAME</h2>
<p> scan &#8211; produce a one line per message scan listing </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>scan</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-clear</code> | <code>-noclear</code>] [<code>-form</code> <i>formatfile</i>] [<code>-format</code> <i>string</i>] [<code>-header</code> | <code>-noheader</code>] [<code>-width</code> <i>columns</i>] [<code>-reverse</code> | <code>-noreverse</code>] [<code>-file</code> <i>filename</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Scan</code></p>
<dd>produces a one-line-per-message listing of the specified folder or messages. Each <code>scan</code> line contains the message number (name), the date, the &#8220;From:&#8221; field, the &#8220;Subject&#8221; field, and, if room allows, some of the body of the message. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
15 + 10 / 05 crocker nned &amp;nbsp;
&amp;nbsp;
&lt;&lt; Last week I asked some of 16 - 10 / 05 crocker message id format &amp; nbsp;
&amp;nbsp;
&lt;&lt; I recommend 18 10 / 06 brien Re : Exit status from mkdir 19 10 / 07 * brien       ``scan'' listing format in nmh
</code></pre>
</dl>
<p> The `+&#8217; on message 15 indicates that it is the current message. </p>
<p> The `-&#8216; on message 16 indicates that it has been replied to, as indicated by a &#8220;Replied:&#8221; component (produced by the <code>-annotate</code> switch to the <code>repl</code> command). </p>
<p> The `*&#8217; on message 19 indicates that no &#8220;Date:&#8221; header was present. The time of last modification of the message is given instead. </p>
<p> If there is sufficient room left on the <code>scan</code> line after the subject, the line will be filled with text from the body, preceded by &#8220;&lt;&lt;&#8221;, and terminated by &#8220;&gt;&gt;&#8221; if the body is sufficiently short. <code>Scan</code> actually reads each of the specified messages and parses them to extract the desired fields. During parsing, appropriate error messages will be produced if there are format errors in any of the messages. </p>
<p> By default, <code>scan</code> will decode RFC 2047 (MIME) encoding in these scan listings. <code>Scan</code> will only decode these fields if your terminal can natively display the character set used in the encoding. You should set the appropriate <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) environment variables to your native character set, if it is not US-ASCII. See <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) for more details on the appropriate environment variables. </p>
<p> The switch <code>-reverse</code>, makes <code>scan</code> list the messages in reverse order. </p>
<p> The <code>-file</code> <i>filename</i> switch allows the user to obtain a <code>scan</code> listing of a maildrop file as produced by <code>packf</code>. This listing includes every message in the file (you can&#8217;t scan individual messages). The switch <code>-reverse</code> is ignored with this option. </p>
<p> The switch <code>-width</code> <i>columns</i> may be used to specify the width of the scan line. The default is to use the width of the terminal. </p>
<p> The <code>-header</code> switch produces a header line prior to the <code>scan</code> listing. Currently, the name of the folder and the current date and time are output (see the <code>HISTORY</code> section for more information). </p>
<p> If the <code>-clear</code> switch is used and <code>scan</code>&#8216;s output is directed to a terminal, then <code>scan</code> will consult the environment variables <code>$TERM</code> and <code>$TERMCAP</code> to determine your terminal type in order to find out how to clear the screen prior to exiting. If the <code>-clear</code> switch is used and <code>scan</code>&#8216;s output is not directed to a terminal (e.g., a pipe or a file), then <code>scan</code> will send a formfeed prior to exiting. </p>
<p> For example, the command: </p>
<dl>
<dt>
<dd> (scan -clear -header; show all -show pr -f) | lpr</dl>
<p> produces a scan listing of the current folder, followed by a formfeed, followed by a formatted listing of all messages in the folder, one per page. Omitting &#8220;<code>-show pr -f</code>&#8221; will cause the messages to be concatenated, separated by a one-line header and two blank lines. </p>
<p> To override the output format used by <code>scan</code>, the <code>-format</code> <i>string</i> or <code>-form</code> <i>file</i> switches are used. This permits individual fields of the scan listing to be extracted with ease. The string is simply a format string and the file is simply a format file. See <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for the details. </p>
<p> In addition to the standard <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) escapes, <code>scan</code> also recognizes the following additional <i>component</i> escapes: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape   Returns  Description</i>
body      string   the (compressed) first part of the body
dtimenow  date     the current date
folder    string   the name of the current folder
</pre>
</dl>
<p> If no date header is present in the message, the <i>function</i> escapes which operate on {<code>date</code>} will return values for the date of last modification of the message file itself. This feature is handy for scanning a draft folder, as message drafts usually aren&#8217;t allowed to have dates in them. </p>
<p> The <code>/etc/nmh</code> directory contains several format files as examples of customized <code>scan</code> output. </p>
<p> <code>scan</code> will update the <code>nmh</code> context prior to starting the listing, so interrupting a long <code>scan</code> listing preserves the new context. <code>nmh</code> purists hate this idea.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Alternate-Mailboxes:~^To determine the user's mailboxes
^Current-Folder:~^To find the default current folder
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pick/">pick</a></i>(1), <i><a href="/docs/linux/man/1-show/">show</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to all
`<code>-format</code>' defaulted as described above
`<code>-noheader</code>'
`<code>-width</code>' defaulted to the width of the terminal
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder.</p>
<h2>HISTORY</h2>
<p> Prior to using the format string mechanism, <code>-header</code> used to generate a heading saying what each column in the listing was. Format strings prevent this from happening.</p>
<h2>BUGS</h2>
<p> The value of each <i>component</i> escape is set by <code>scan</code> to the contents of the first message header <code>scan</code> encounters with the corresponding component name; any following headers with the same component name are ignored. </p>
<h2>Index</h2>
