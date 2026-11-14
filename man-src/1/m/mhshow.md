---
title: "mhshow(1)"
name: "mhshow"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhshow/"
description: "mhshow – display MIME messages"
---

<h2 class="name">NAME</h2>
<p> mhshow &#8211; display MIME messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhshow</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-file</code> <i>file</i>] [<code>-part</code> <i>number</i>] &#8230; [<code>-type</code> <i>content</i>] &#8230; [<code>-concat</code> | <code>-noconcat</code>] [<code>-textonly</code> | <code>-notextonly</code>] [<code>-inlineonly</code> | <code>-noinlineonly</code>] [<code>-form</code> <i>formfile</i>] [<code>-markform</code> <i>formfile</i>] [<code>-rcache</code> <i>policy</i>] [<code>-wcache</code> <i>policy</i>] [<code>-check</code> | <code>-nocheck</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mhshow</code> command display contents of a MIME (multi-media) message or collection of messages. </p>
<p> <code>mhshow</code> manipulates multi-media messages as specified in RFC 2045 to RFC 2049. Currently <code>mhshow</code> only supports encodings in message bodies, and does not support the encoding of message headers as specified in RFC 2047. </p>
<p> By default <code>mhshow</code> will display only text parts of a message that are not marked as attachments. This behavior can be changed by the <code>-notextonly</code> and <code>-noinlineonly</code> switches. In addition, by using the <code>-part</code> and <code>-type</code> switches, you may further limit the scope of <code>mhshow</code> to particular subparts (of a multipart content) and/or particular content types. The inclusion of any <code>-part</code> or <code>-type</code> switches will override the default settings of <code>-textonly</code> and <code>-inlineonly.</code> </p>
<p> By default <code>mhshow</code> will concatenate all content under one pager. If you which each part to displayed separately, you can override the default behavior with <code>-noconcat.</code> </p>
<p> The option <code>-file</code> <i>file</i> directs <code>mhshow</code> to use the specified file as the source message, rather than a message from a folder. If you specify this file as &#8220;-&#8221;, then <code>mhshow</code> will accept the source message on the standard input. Note that the file, or input from standard input should be a validly formatted message, just like any other <code>nmh</code> message. It should <code>NOT</code> be in mail drop format (to convert a file in mail drop format to a folder of <code>nmh</code> messages, see <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1)). </p>
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
<p> To specify a content, regardless of its subtype, just use the name of the content, e.g., &#8220;audio&#8221;. To specify a specific subtype, separate the two with a slash, e.g., &#8220;audio/basic&#8221;. Note that regardless of the values given to the `-type&#8217; switch, a multipart content (of any subtype listed above) is always acted upon. Further note that if the `-type&#8217; switch is used, and it is desirable to act on a message/external-body content, then the `-type&#8217; switch must be used twice: once for message/external-body and once for the content externally referenced.</p>
<h3>Unseen Sequence</h3>
<p> If the profile entry &#8220;Unseen-Sequence&#8221; is present and non-empty, then <code>mhshow</code> will remove each of the messages shown from each sequence named by the profile entry.</p>
<h3>Checking the Contents</h3>
<p> The <code>-check</code> switch tells <code>mhshow</code> to check each content for an integrity checksum. If a content has such a checksum (specified as a Content-MD5 header field), then <code>mhshow</code> will attempt to verify the integrity of the content.</p>
<h3>Showing the Contents</h3>
<p> The headers of each message are displayed with the <i>mhlproc</i> (usually <code>mhl</code>), using the standard format file <i>mhl.headers</i>. You may specify an alternate format file with the <code>-form</code> <i>formfile</i> switch. If the format file <i>mhl.null</i> is specified, then the display of the message headers is suppressed. </p>
<p> Next, the contents are extracted from the message and are stored in a temporary file. Usually, the name of the temporary file is the word &#8220;mhshow&#8221; followed by a string of characters. Occasionally, the method used to display a content (described next), requires that the file end in a specific suffix. For example, the <code>soffice</code> command (part of the StarOffice package) can be used to display Microsoft Word content, but it uses the suffix to determine how to display the file. If no suffix is present, the file is not correctly loaded. Similarily, older versions of the <code>gs</code> command append a &#8220;.ps&#8221; suffix to the filename if one was missing. As a result, these cannot be used to read the default temporary file. </p>
<p> To get around this, your profile can contain lines of the form: </p>
<dl>
<dt>
<dd> mhshow-suffix-&lt;type&gt;/&lt;subtype&gt;: &lt;suffix&gt;</dl>
<p> or </p>
<dl>
<dt>
<dd> mhshow-suffix-&lt;type&gt;: &lt;suffix&gt;</dl>
<p> to specify a suffix which can be automatically added to the temporary file created for a specific content type. For example, the following lines might appear in your profile: </p>
<dl>
<dt>
<dd>
<pre>
mhshow-suffix-text: .txt
mhshow-suffix-application/msword: .doc
mhshow-suffix-application/PostScript: .ps
</pre>
</dl>
<p> to automatically append a suffix to the temporary files. </p>
<p> The method used to display the different contents in the messages bodies will be determined by a &#8220;display string&#8221;. To find the display string, <code>mhshow</code> will first search your profile for an entry of the form: </p>
<dl>
<dt>
<dd> mhshow-show-&lt;type&gt;/&lt;subtype&gt;</dl>
<p> to determine the display string. If this isn&#8217;t found, <code>mhshow</code> will search for an entry of the form: </p>
<dl>
<dt>
<dd> mhshow-show-&lt;type&gt;</dl>
<p> to determine the display string. </p>
<p> If a display string is found, any escapes (given below) will be expanded. The result will be executed under &#8220;/bin/sh&#8221;, with the standard input set to the content. </p>
<p> The display string may contain the following escapes: </p>
<dl>
<dt>
<dd>
<pre>
%a           Insert parameters from Content-Type field
%{parameter} Insert the parameter value from the Content-Type field
%f           Insert filename containing content
%F           %f, and stdin is terminal not content
%l           display listing prior to displaying content
%s           Insert content subtype
%d           Insert content description
%%           Insert the character %
</pre>
</dl>
<p> <code>Mhshow</code> will execute at most one display string at any given time, and wait for the current display string to finish execution before executing the next display string. </p>
<p> The {parameter} escape is typically used in a command line argument that should only be present if it has a non-null value. Its value will be wrapped with single quotes if the escape is not so wrapped. Shell parameter expansion can construct the argument only when it is non-null, e.g., </p>
<dl>
<dt>
<dd>
<pre><code>
mhshow - show - text / html : charset = % {charset};
w3m ${charset : +-I $charset} - T text / html % F
</code></pre>
</dl>
<p> That example also shows the use of indentation to signify continuation: the two text lines combine to form a single entry. Note that when dealing with text that has been converted internally by <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3), the &#8220;charset&#8221; parameter will reflect the target character set of the text, rather than the original character set in the message. </p>
<p> Note that if the content being displayed is multipart, but not one of the subtypes listed above, then the f- and F-escapes expand to multiple filenames, one for each subordinate content. Further, stdin is not redirected from the terminal to the content. </p>
<p> If a display string is not found, <code>mhshow</code> behaves as if these profile entries were supplied and supported: </p>
<dl>
<dt>
<dd>
<pre>
mhshow-show-text/plain: %lmoreproc %F
mhshow-show-message/rfc822: %lshow -file %F
</pre>
</dl>
<p> Note that &#8220;moreproc&#8221; is not supported in user profile display strings. </p>
<p> If a subtype of type text doesn&#8217;t have a profile entry, it will be treated as text/plain. </p>
<p> <code>mhshow</code> has default methods for handling multipart messages of subtype mixed, alternative, parallel, and digest. Any unknown subtype of type multipart (without a profile entry), will be treated as multipart/mixed. </p>
<p> If none of these apply, then <code>mhshow</code> will check to see if the message has an application/octet-stream content with parameter &#8220;type=tar&#8221;. If so, <code>mhshow</code> will use an appropriate command. If not, <code>mhshow</code> will complain. </p>
<p> Example entries might be: </p>
<dl>
<dt>
<dd>
<pre>
mhshow-show-audio/basic: raw2audio 2&gt;/dev/null | play
mhshow-show-image: xv %f
mhshow-show-application/PostScript: lpr -Pps
</pre>
</dl>
<p> If an f- or F-escape is not quoted with single quotes, its expansion will be wrapped with single quotes. </p>
<p> Finally, <code>mhshow</code> will process each message serially &#8212; it won&#8217;t start showing the next message until all the commands executed to display the current message have terminated.</p>
<h3>Showing Alternate Character Sets</h3>
<p> If <code>mhshow</code> was built with <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3), then all text/plain parts of the message(s) will be displayed using the character set of the current locale. See the <code><a href="/docs/linux/man/1-mhparam/">mhparam</a></code>(1) man page for how determine whether your <code>nmh</code> installation includes <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3) support. To convert text parts other than text/plain, or if <code>mhshow</code> was not built with <i>iconv</i>, an external program can be used, as described next. </p>
<p> Because a content of type text might be in a non-ASCII character set, when <code>mhshow</code> encounters a &#8220;charset&#8221; parameter for this content, it checks if your terminal can display this character set natively. <code>mhshow</code> checks this by examining the current character set defined by the <i><a href="/docs/linux/man/1-locale/">locale</a></i>(1) environment variables. If the value of the locale character set is equal to the value of the charset parameter, then <code>mhshow</code> assumes it can display this content without any additional setup. If the locale is not set properly, <code>mhshow</code> will assume a value of &#8220;US-ASCII&#8221;. If the character set cannot be displayed natively, then <code>mhshow</code> will look for an entry of the form: </p>
<dl>
<dt>
<dd> mhshow-charset-&lt;charset&gt;</dl>
<p> which should contain a command creating an environment to render the character set. This command string should containing a single &#8220;%s&#8221;, which will be filled-in with the command to display the content. </p>
<p> Example entries might be: </p>
<dl>
<dt>
<dd> mhshow-charset-iso-8859-1: xterm -fn &#8216;-*-*-medium-r-normal-*-*-120-*-*-c-*-iso8859-*&#8217; -e %s</dl>
<p> or </p>
<dl>
<dt>
<dd> mhshow-charset-iso-8859-1: &#8216;%s&#8217;</dl>
<p> The first example tells <code>mhshow</code> to start <code>xterm</code> and load the appropriate character set for that message content. The second example tells <code>mhshow</code> that your pager (or other program handling that content type) can handle that character set, and that no special processing is needed beforehand. </p>
<p> Note that many pagers strip off the high-order bit or have problems displaying text with the high-order bit set. However, the pager <code>less</code> has support for single-octet character sets. For example, messages encoded in the ISO-8859-1 character set can be view using <code>less</code>, with these environment variable settings: </p>
<dl>
<dt>
<dd>
<pre>
LESSCHARSET latin1
LESS        -f
</pre>
</dl>
<p> The first setting tells <code>less</code> to use the ISO-8859-1 definition for determining whether a character is &#8220;normal&#8221;, &#8220;control&#8220;, or &#8220;binary&#8221;. The second setting tells <code>less</code> not to warn you if it encounters a file that has non-ASCII characters. Then, simply set the <i>moreproc</i> profile entry to <code>less</code>, and it will get called automatically. (To handle other single-octet character sets, look at the <i><a href="/docs/linux/man/1-less/">less</a></i>(1) manual entry for information about the <code>$LESSCHARDEF</code> environment variable.)</p>
<h3>Messages of Type message/partial</h3>
<p> <code>mhshow</code> cannot directly display messages of type partial. You must reassemble them first into a normal message using <code>mhstore</code>. Check the man page for <i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1) for details.</p>
<h3>External Access</h3>
<p> For contents of type message/external-body, <code>mhshow</code> supports these access-types: </p>
<dl>
<dt>&bull;</p>
<dd> afs</p>
<dt>&bull;</p>
<dd> anon-ftp</p>
<dt>&bull;</p>
<dd> ftp</p>
<dt>&bull;</p>
<dd> local-file</p>
<dt>&bull;</p>
<dd> mail-server</p>
<dt>&bull;</p>
<dd> url</dl>
<p> For the &#8220;anon-ftp&#8221; and &#8220;ftp&#8221; access types, <code>mhshow</code> will look for the &#8220;nmh-access-ftp&#8221; profile entry, e.g., </p>
<dl>
<dt>
<dd> nmh-access-ftp: my<a href="ftp://ftp.sh">ftp.sh</a></dl>
<p> to determine the pathname of a program to perform the FTP retrieval. </p>
<p> This program is invoked with these arguments: </p>
<dl>
<dt>
<dd>
<pre>
domain name of FTP-site
username
password
remote directory
remote filename
local filename
``ascii'' or ``binary''
</pre>
</dl>
<p> The program should terminate with an exit status of zero if the retrieval is successful, and a non-zero exit status otherwise. </p>
<p> For the &#8220;url&#8221; access-type, <code>mhshow</code> will look for the &#8220;nmh-access-url&#8221; profile entry. See <i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1) for more details. </p>
<h3>The Content Cache</h3>
<p> When <code>mhshow</code> encounters an external content containing a &#8220;Content-ID:&#8221; field, and if the content allows caching, then depending on the caching behavior of <code>mhshow</code>, the content might be read from or written to a cache. </p>
<p> The caching behavior of <code>mhshow</code> is controlled with the <code>-rcache</code> and <code>-wcache</code> switches, which define the policy for reading from, and writing to, the cache, respectively. One of four policies may be specified: &#8220;public&#8221;, indicating that <code>mhshow</code> should make use of a publically-accessible content cache; &#8220;private&#8221;, indicating that <code>mhshow</code> should make use of the user&#8217;s private content cache; &#8220;never&#8221;, indicating that <code>mhshow</code> should never make use of caching; and, &#8220;ask&#8221;, indicating that <code>mhshow</code> should ask the user. </p>
<p> There are two directories where contents may be cached: the profile entry &#8220;nmh-cache&#8221; names a directory containing world-readable contents, and, the profile entry &#8220;nmh-private-cache&#8221; names a directory containing private contents. The former should be an absolute (rooted) directory name. </p>
<p> For example, </p>
<dl>
<dt>
<dd> nmh-cache: /tmp</dl>
<p> might be used if you didn&#8217;t care that the cache got wiped after each reboot of the system. The latter is interpreted relative to the user&#8217;s nmh directory, if not rooted, e.g., </p>
<dl>
<dt>
<dd> nmh-private-cache: .cache</dl>
<p> (which is the default value).</p>
<h3>User Environment</h3>
<p> Because the display environment in which <code>mhshow</code> operates may vary for different machines, <code>mhshow</code> will look for the environment variable <code>$MHSHOW</code>. If present, this specifies the name of an additional user profile which should be read. Hence, when a user logs in on a particular display device, this environment variable should be set to refer to a file containing definitions useful for the given display device. Normally, only entries that deal with the methods to display different content type and subtypes </p>
<dl>
<dt>
<dd>
<pre>
mhshow-show-&lt;type&gt;/&lt;subtype&gt;
mhshow-show-&lt;type&gt;
</pre>
</dl>
<p> need be present in this additional profile. Finally, <code>mhshow</code> will attempt to consult </p>
<dl>
<dt>
<dd> /etc/nmh/mhn.defaults</dl>
<p> which is created automatically during <code>nmh</code> installation. </p>
<p> See &quot;Profile Lookup&quot; in <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) for the profile search order, and for how duplicate entries are treated.</p>
<h3>Content-Type Marker</h3>
<p> If <code>mhshow</code> decides to not display a particular part due to the switches of <code>-textonly</code> or <code>-inlineonly</code> it will display a marker containing information about the part. This marker is processed via <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) and can be changed by the use of the <code>-markform</code> switch to specify a file containing the <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) instructions to use when displaying the content marker. In addition to the normal set of <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) instructions, the following <i>component</i> escapes are supported: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape         Returns   Description</i>
part            string    MIME part number
content-type    string    MIME Content-Type of part
description     string    Content-Description header
disposition     string    Content disposition (attachment or inline)
ctype-&lt;PARAM&gt;   string    Value of &lt;PARAM&gt; from Content-Type header
cdispo-&lt;PARAM&gt;  string    Value of &lt;PARAM&gt; from
                          Content-Disposition header
</pre>
</dl>
<p> All MIME parameters and the &#8220;Content-Description&#8221; header will have RFC 2231 decoding applied and be converted to the local character set. </p>
<h2>FILES</h2>
<p> <code>mhshow</code> looks for all format files and mhn.defaults in multiple locations: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<pre>
^$HOME/.mh_profile~^The user profile
^$MHSHOW~^Additional profile entries
^/etc/nmh/mhn.defaults~^System default MIME profile entries
^/etc/nmh/mhl.headers~^The headers template
^/etc/nmh/mhshow.marker~^Example content marker
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Unseen-Sequence:~^To name sequences denoting unseen messages
^mhlproc:~^Default program to display message headers
^nmh-access-ftp:~^Program to retrieve contents via FTP
^nmh-access-url:~^Program to retrieve contents via HTTP
^nmh-cache~^Public directory to store cached external contents
^nmh-private-cache~^Personal directory to store cached external contents
^mhshow-charset-&lt;charset&gt;~^Template for environment to render character sets
^mhshow-show-&lt;type&gt;*~^Template for displaying contents
^moreproc:~^Default program to display text/plain content
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3), <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-mhl/">mhl</a></i>(1), <i><a href="/docs/linux/man/1-mhlist/">mhlist</a></i>(1), <i><a href="/docs/linux/man/1-mhparam/">mhparam</a></i>(1), <i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1), <i><a href="/docs/linux/man/1-sendfiles/">sendfiles</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-nocheck</code>'
`<code>-concat</code>'
`<code>-textonly</code>'
`<code>-inlineonly</code>'
`<code>-form mhl.headers</code>'
`<code>-rcache ask</code>'
`<code>-wcache ask</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The last message selected will become the current message. </p>
<h2>Index</h2>
