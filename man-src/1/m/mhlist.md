---
title: "mhlist(1)"
name: "mhlist"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhlist/"
description: "mhlist – list information about MIME messages"
---

<h2 class="name">NAME</h2>
<p> mhlist &#8211; list information about MIME messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhlist</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-file</code> <i>file</i>] [<code>-part</code> <i>number</i>] &#8230; [<code>-type</code> <i>content</i>] &#8230; [<code>-headers</code> | <code>-noheaders</code>] [<code>-realsize</code> | <code>-norealsize</code>] [<code>-rcache</code> <i>policy</i>] [<code>-wcache</code> <i>policy</i>] [<code>-check</code> | <code>-nocheck</code>] [<code>-changecur</code> | <code>-nochangecur</code>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-disposition</code> | <code>-nodisposition</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mhlist</code> command allows you to list information (essentially a table of contents) about the various parts of a collection of MIME (multi-media) messages. </p>
<p> <code>mhlist</code> manipulates MIME (multi-media messages) as specified in RFC 2045 to RFC 2049 (See <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1)). </p>
<p> The <code>-headers</code> switch indicates that a one-line banner should be displayed above the listing. </p>
<p> The <code>-realsize</code> switch tells <code>mhlist</code> to evaluate the &#8220;native&#8221; (decoded) format of each content prior to listing. This provides an accurate count at the expense of a small delay. </p>
<p> If the <code>-verbose</code> switch is present, then the listing will show any &#8220;extra&#8221; information that is present in the message, such as comments in the &#8220;Content-Type&#8221; header. </p>
<p> If the <code>-disposition</code> switch is present, then the listing will show any relevant information from the &#8220;Content-Disposition&#8221; header. </p>
<p> The option <code>-file</code> <i>file</i> directs <code>mhlist</code> to use the specified file as the source message, rather than a message from a folder. If you specify this file as &#8220;-&#8221;, then <code>mhlist</code> will accept the source message on the standard input. Note that the file, or input from standard input should be a validly formatted message, just like any other <code>nmh</code> message. It should <code>NOT</code> be in mail drop format (to convert a file in mail drop format to a folder of <code>nmh</code> messages, see <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1)). </p>
<p> By default, <code>mhlist</code> will list information about the entire message (all of its parts). By using the <code>-part</code> and <code>-type</code> switches, you may limit the scope of this command to particular subparts (of a multipart content) and/or particular content types. </p>
<p> A part specification consists of a series of numbers separated by dots. For example, in a multipart content containing three parts, these would be named as 1, 2, and 3, respectively. If part 2 was also a multipart content containing two parts, these would be named as 2.1 and 2.2, respectively. Note that the <code>-part</code> switch is effective for only messages containing a multipart content. If a message has some other kind of content, or if the part is itself another multipart content, the <code>-part</code> switch will not prevent the content from being acted upon. </p>
<p> A content specification consists of a content type and a subtype. The initial list of &#8220;standard&#8221; content types and subtypes can be found in RFC 2046. </p>
<p> A list of commonly used contents is briefly reproduced here: </p>
<dl>
<dt>
<dd>
<pre><code>
Type Subtypes-- -- -- -- -- --text plain, enriched multipart mixed, alternative, digest, parallel message rfc822, partial, external - body application octet - stream, postscript image jpeg, gif, png audio basic video mpeg
</code></pre>
</dl>
<p> A legal MIME message must contain a subtype specification. </p>
<p> To specify a content, regardless of its subtype, just use the name of the content, e.g., &#8220;audio&#8221;. To specify a specific subtype, separate the two with a slash, e.g., &#8220;audio/basic&#8221;. Note that regardless of the values given to the <code>-type</code> switch, a multipart content (of any subtype listed above) is always acted upon. Further note that if the <code>-type</code> switch is used, and it is desirable to act on a message/external-body content, then the <code>-type</code> switch must be used twice: once for message/external-body and once for the content externally referenced. </p>
<p> The parts of a multipart/alternative part are listed in the reverse order of their placement in the message. The listing therefore is in decreasing order of preference, as defined in RFC 1521.</p>
<h3>Checking the Contents</h3>
<p> The <code>-check</code> switch tells <code>mhlist</code> to check each content for an integrity checksum. If a content has such a checksum (specified as a Content-MD5 header field), then <code>mhlist</code> will attempt to verify the integrity of the content.</p>
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
<p> <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1), <i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-nocheck</code>'
`<code>-headers</code>'
`<code>-realsize</code>'
`<code>-rcache ask</code>'
`<code>-wcache ask</code>'
`<code>-changecur</code>'
`<code>-noverbose</code>'
`<code>-nodisposition</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The last message selected will become the current message, unless the <code>-nochangecur</code> option is specified. </p>
<h2>Index</h2>
