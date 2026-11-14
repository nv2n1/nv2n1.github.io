---
title: "reformime(1)"
name: "reformime"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reformime/"
description: "reformime – MIME E-mail reformatting tool"
---

<h2 class="name">NAME</h2>
<p> reformime &#8211; MIME E-mail reformatting tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>reformime</code> [<i>options</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>reformime</code></p>
<dd>is a utility for reformatting MIME messages. </p>
<p> Generally, <code>reformime</code> expects to see an m[blue]<code>RFC 2045</code>m[]<font SIZE="-2">[1]</font> compliant message on standard input, except in few cases such as the <code>-m</code> option. </p>
<p> If no options are given, <code>reformime</code> prints the MIME structure of the message. The output consists of so-called &quot;MIME reference tags&quot;, one per line. For example: </p>
<dl>
<dt>
<dd>
<pre>
1
1.1
1.2
</pre>
</dl>
<p> This shows that the message contains two different MIME sections. The first line of the MIME structure output will always contain &quot;1&quot;, which refers to the entire message. In this case it happens to be a multipart/mixed message. &quot;1.1&quot; refers to the first section of the multipart message, which happens to be a text/plain section. &quot;1.2&quot; refers to the second section of the message, which happens to be an application/octet-stream section. </p>
<p> If the message is not a MIME message, or it does not contain any attachments, <code>reformime</code> prints only &quot;1&quot;, that refers to the entire message itself: </p>
<dl>
<dt>
<dd>
<pre>
1
</pre>
</dl>
<p> Here&#8217;s the output from <code>reformime</code> when the first part of the message was itself a multipart/alternative section: </p>
<dl>
<dt>
<dd>
<pre>
1
1.1
1.1.1
1.1.2
1.2
</pre>
</dl>
<p> Arbitrarily complex MIME constructs are possible.</p>
<h2>OPTIONS</h2>
<p> -d</p>
<dl>
<dt>
<dd> Parse a delivery status notification MIME message (m[blue]<code>RFC 1894</code>m[]<font SIZE="-2">[2]</font>). <code>reformime</code> expects to see on standard input a MIME message that consists of a delivery status notification, as defined by RFC 1894. <code>reformime</code> reads the message and prints on standard output a list of addresses and their corresponding delivery status, as specified in the delivery status notification. Each line printed by <code>reformime</code> consists of a delivery status, a space, and the address. <code>reformime</code> then terminates with a 0 exit status. <code>reformime</code> produces no output and terminates with an exit status of 1 if the standard input does not contain a delivery status notification.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Like the <code>-d</code> except that <code>reformime</code> lists the address found in the Original-Recipient: header, if it exists.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Extract the contents of the indicated MIME section, and display it on standard output. The <code>-s</code> option is required when <code>-e</code> is specified. If the specified section or sections use either the base64 or quoted-printable encoding method, <code>reformime</code> automatically decodes it. In this case you&#8217;re better off redirecting the standard output into a file.</dl>
<p> -i</p>
<dl>
<dt>
<dd> Display MIME information for each section. <code>reformime</code> displays the contents of the Content-Type: header, any encoding used, and the character set. <code>reformime</code> also displays the byte offset in the message where each section starts and ends (and where the actual contents of the section start, after skipping all the headers).</dl>
<p> -m</p>
<dl>
<dt>
<dd> Create a multipart/digest MIME message digest.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Rewrite message, adding or standardizing m[blue]<code>RFC 2045</code>m[]<font SIZE="-2">[1]</font> MIME headers.</dl>
<p> -r7</p>
<dl>
<dt>
<dd> Like <code>-r</code> but also convert 8bit-encoded MIME sections to quoted-printable.</dl>
<p> -r8</p>
<dl>
<dt>
<dd> Like <code>-r</code> but also convert quoted-printable-encoded MIME sections to 8bit.</dl>
<p> -s <i>section</i></p>
<dl>
<dt>
<dd> Display MIME information for this section only. <i>section</i> is a MIME specification tag. The <code>-s</code> option is required if <code>-e</code> is also specified, and is optional with <code>-i</code>. </p>
<p> Multiple sections may be specified by separating them with commas. <code>reformime</code> processes each section using the other options that were specified.</dl>
<p> -x</p>
<dl>
<dt>
<dd> Extract the contents of the indicated MIME section to a file.</dl>
<p> -X</p>
<dl>
<dt>
<dd> Pipe the contents of the indicated MIME section to a program.</dl>
<h3>Extracting RFC 2045 MIME section(s) to file(s)</h3>
<p> The <code>-x</code> and <code>-X</code> options extract a specific MIME section to a file or to a pipe to an external program. Use the <code>-s</code> option to identify the MIME section to extract. If the <code>-s</code> option is not specified, every MIME section in the message is extracted, one at a time. If <code>-s</code> lists multiple sections, each section gets extracted separately. quoted-printable and base64 encoding are automatically decoded. </p>
<p> -x</p>
<dl>
<dt>
<dd> Interactive extraction. <code>reformime</code> prints the MIME content type of each section. Answer with &#8216;y&#8217; or &#8216;Y&#8217; to extract the MIME section. Specify the filename at the next prompt. <code>reformime</code> prompts with a default filename. <code>reformime</code> tries to choose the default filename based on the MIME headers, if possible. If not, the default filename will be attachment1.dat (if the -s option is not specified, the next filename will be attachment2.dat, and so on).</dl>
<p> -x<i>PREFIX</i></p>
<dl>
<dt>
<dd> Automatic extraction. <code>reformime</code> automatically extracts one or more MIME sections, and saves them to a file. The filename is formed by taking <i>PREFIX</i>, and appending the default filename to it. Note that there&#8217;s no space between &quot;-x&quot; and &quot;PREFIX&quot;. For example: </p>
<dl>
<dt>
<dd>
<pre>
reformime -xfiles-
</pre>
</dl>
<p> This command saves MIME sections as files-attachment1.dat, then files-attachment2.dat, etc. <code>reformime</code> tries to append the filename specified in the MIME headers for each section, where possible. <code>reformime</code> replaces all suspect characters with the underscore character.</dl>
<p> -X prog arg1 arg2 &#8230;</p>
<dl>
<dt>
<dd> The <code>-X</code> option must be the last option to <code>reformime</code>. <code>reformime</code> runs an external program <code>prog</code>, and pipes the contents of the MIME section to the program. <code>reformime</code> sets the environment variable <code>CONTENT_TYPE</code> to the MIME content type. The environment variable <code>FILENAME</code> gets set to the default filename of <code>reformime</code>&#8216;s liking. If the <code>-s</code> option is not specified, the program runs once for every MIME section in the message. The external program, <code>prog</code> must terminate with a zero exit status in order for <code>reformime</code> to proceed to the next MIME section in the message (or the next section specified by <code>-s</code>). In any case, if <code>prog</code> terminates with a non-zero exit status, <code>reformime</code> terminates with the exit status of 20 plus <code>prog</code>&#8216;s exit status.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> <code>reformime</code> extracts every MIME section in the message unless the <code>-s</code> option is specified. This includes even the text/plain MIME content that usually precedes a binary attachment. </p>
</dl>
<h3>Adding RFC 2045 MIME headers</h3>
<p> The <code>-r</code> option performs the following actions: </p>
<p> If there is no Mime-Version:, Content-Type:, or Content-Transfer-Encoding: header, <code>reformime</code> adds one. </p>
<p> If the Content-Transfer-Encoding: header contains 8bit or raw, but only seven-bit data is found, <code>reformime</code> changes the Content-Transfer-Encoding header to 7bit. </p>
<p> <code>-r7</code> does the same thing, but also converts 8bit-encoded content that contains eight-bit characters to quoted-printable encoding. </p>
<p> <code>-r8</code> does the same thing, but also converts quoted-printable-encoded content to 8bit, except in some situations.</p>
<h3>Creating multipart/digest MIME digests</h3>
<p> The <code>-m</code> option creates a MIME digest. <code>reformime</code> reads a list of filenames on standard input. Each line read from standard input contains the name of a file that is presumed to contain an RFC 2822-formatted message. <code>reformime</code> splices all files into a <code>multipart/digest</code> MIME section, and writes it to standard output.</p>
<h3>Translating MIME headers</h3>
<p> The following options do not read a message from standard input. These options process MIME headers via the command line, and are designed to be conveniently used by mail-handling scripts. </p>
<p> -h &quot;<i>header</i>&quot;</p>
<dl>
<dt>
<dd> Decode a MIME-encoded &quot;<i>header</i>&quot; and print the decoded 8-bit content on standard output. The decoding gets carried out as if the contents occurred in the &#8220;Subject&#8221; header. Example: </p>
<dl>
<dt>
<dd>
<pre>
$ reformime -h '=?iso-8859-1?Q?H=F3la!?='
Hóla!
</pre>
</dl>
</dl>
<p> -H &quot;<i>header</i>&quot;</p>
<dl>
<dt>
<dd> Like <code>-h</code> except that <i>header</i> is parsed as a list of email addresses, like &#8220;From&#8221; or &#8220;To&#8221;.</dl>
<p> -o &quot;<i>text</i>&quot;</p>
<dl>
<dt>
<dd> MIME-encode &quot;<i>text</i>&quot;, and print the results on standard output.</dl>
<p> -O &quot;<i>text</i>&quot;</p>
<dl>
<dt>
<dd> Like the <code>-o option</code>, except that <i>text</i> is a structured header with RFC 2822 addresses.</dl>
<p> -c &quot;<i>charset</i>&quot;</p>
<dl>
<dt>
<dd> Use <i>charset</i> as the character set setting, by the <code>-h</code>, <code>-H</code>, <code>-o</code> and <code>-O</code> options.</dl>
<p> -u</p>
<dl>
<dt>
<dd> This &#8220;undocumented&#8221; option reads a MIME message on standard input, and converts its contents to an UTF-8-encoded character stream, which is written to standard output. </p>
<p> The standard output receives a concatenated amalgam of the headers and &#8220;text&#8221; MIME object data. It is meant to be used as part of a generic search function. This option decodes various kinds of header MIME encoding, the quoted-printable and base64 transfer encodings of &#8220;text&#8221; MIME objects.</dl>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a href="/docs/linux/man/1-reformail/">reformail</a></code>(1)m[]<font SIZE="-2">[3]</font>, <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), m[blue]<code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)m[]<font SIZE="-2">[4]</font>, m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[5]</font>, m[blue]<code><a href="/docs/linux/man/5-maildropfilter/">maildropfilter</a></code>(5)m[]<font SIZE="-2">[6]</font>, <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd> Author</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> RFC 2045</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.rfc-editor.org/rfc/rfc2045.txt">http://www.rfc-editor.org/rfc/rfc2045.txt</a></dl>
<dt> 2.</p>
<dd> RFC 1894</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.rfc-editor.org/rfc/rfc1894.txt">http://www.rfc-editor.org/rfc/rfc1894.txt</a></dl>
<dt> 3.</p>
<dd> <code><a href="/docs/linux/man/1-reformail/">reformail</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/reformail.html</dl>
<dt> 4.</p>
<dd> <code><a href="/docs/linux/man/1-mailbot/">mailbot</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/mailbot.html</dl>
<dt> 5.</p>
<dd> <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildrop.html</dl>
<dt> 6.</p>
<dd> <code><a href="/docs/linux/man/5-maildropfilter/">maildropfilter</a></code>(5)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildropfilter.html</dl>
</dl>
<h2>Index</h2>
