---
title: "mhfixmsg(1)"
name: "mhfixmsg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhfixmsg/"
description: "mhfixmsg – rewrite MIME messages with various transformations"
---

<h2 class="name">NAME</h2>
<p> mhfixmsg &#8211; rewrite MIME messages with various transformations </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhfixmsg</code> [<i>+folder</i>] [<i>msgs</i> | <i>absolute pathname</i> | -file <i>file</i>] [<code>-decodetext</code></p>
<dd>8bit/7bit | <code>-nodecodetext</code>] [<code>-textcharset</code> <i>charset</i> | <code>-notextcharset</code>] [<code>-reformat</code> | <code>-noreformat</code>] [<code>-replacetextplain</code> | <code>-noreplacetextplain</code>] [<code>-fixboundary</code> | <code>-nofixboundary</code>] [<code>-fixcte</code> | <code>-nofixcte</code>] [<code>-outfile</code> <i>outfile</i>] [<code>-rmmproc</code> <i>program</i>] [<code>-normmproc</code>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mhfixmsg</code> rewrites MIME messages, applying specific transformations such as decoding of MIME-encoded message parts and repairing invalid MIME headers. </p>
<p> MIME messages are specified in RFC 2045 to RFC 2049 (see <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1)). The <code>mhlist</code> command is invaluable for viewing the content structure of MIME messages. <code>mhfixmsg</code> passes non-MIME messages through without any transformations. If no transformations apply to a MIME message, the original message or file is not modified or removed. </p>
<p> The <code>-decodetext</code> switch enables a transformation to decode each base64 and quoted-printable text message part to the selected 8bit or 7bit encoding. If 7bit is selected for a base64 part but it will only fit 8bit, as defined by RFC 2045, then it will be decoded to 8bit quoted-printable. Otherwise, if the decoded text would not fit the selected encoding, the part is not decoded (and a message will be displayed if <code>-verbose</code> is enabled). </p>
<p> When the <code>-decodetext</code> switch is enabled, each carriage return character that precedes a linefeed character is removed from text parts encoded in ASCII, ISO-8859-x, UTF-8, or Windows-12xx. </p>
<p> The <code>-textcharset</code> switch specifies that all text/plain parts of the message(s) should be converted to <i>charset</i>. Charset conversions require that <code>nmh</code> be built with <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3); see the <code><a href="/docs/linux/man/1-mhparam/">mhparam</a></code>(1) man page for how determine whether your <code>nmh</code> installation includes that. To convert text parts other than text/plain, an external program can be used, via the <code>-reformat</code> switch. </p>
<p> The <code>-reformat</code> switch enables a transformation for text parts in the message. For each text part that is not text/plain and that does not have a corresponding text/plain in a multipart/alternative part, <code>mhfixmsg</code> looks for a mhfixmsg-format-text/subtype profile entry that matches the subtype of the part. If one is found and can be used to successfully convert the part to text/plain, <code>mhfixmsg</code> inserts that text/plain part at the beginning of the containing multipart/alternative part, if present. If not, it creates a multipart/alternative part. </p>
<p> The <code>-replacetextplain</code> switch broadens the applicability of <code>-reformat</code> by always replacing a corresponding text/plain part, if one exists. If <code>-verbose</code> if enabled, the replacement will be shown as two steps: a removal of the text/plain part followed by the usual insertion of a new part. </p>
<p> <code>-reformat</code> requires a profile entry for each text part subtype to be reformatted. The mhfixmsg-format-text/subtype profile entries are based on external conversion programs, and are used the same way that <code>mhshow</code> uses its mhshow-show-text/subtype entries. When <code>nmh</code> is installed, it searches for a conversion program for text/html content, and if one is found, inserts a mhfixmsg-format-text/html entry in /etc/nmh/mhn.defaults. An entry of the same name in the user&#8217;s profile takes precedence. The user can add entries for other text subtypes to their profile. </p>
<p> The <code>-fixboundary</code> switch enables a transformation to repair the boundary portion of the Content-Type header field of the message to match the boundaries of the outermost multipart part of the message, if it does not. That condition is indicated by a &#8220;bogus multipart content in message&#8221; error message from <code>mhlist</code> and other <code>nmh</code> programs that parse MIME messages. </p>
<p> The <code>-fixcte</code> switch enables a transformation to change the Content-Transfer-Encoding from an invalid value to 8bit in message parts with a Content-Type of multipart, as required by RFC 2045, Section 6.4. That condition is indicated by a &#8220;must be encoded in 7bit, 8bit, or binary&#8221; error message from <code>mhlist</code> and other <code>nmh</code> programs that parse MIME messages. </p>
<p> The <code>-verbose</code> switch directs <code>mhfixmsg</code> to output informational message for each transformation applied. </p>
<p> The <code>-file</code> <i>file</i> switch directs <code>mhfixmsg</code> to use the specified file as the source message, rather than a message from a folder. Only one file argument may be provided. The <code>-file</code> switch is implied if <i>file</i> is an absolute pathname. If the file is &#8220;-&#8221;, then <code>mhfixmsg</code> accepts the source message on the standard input stream. If the <code>-outfile</code> switch is not enabled when using the standard input stream, <code>mhfixmsg</code> will not produce a transformed output message. </p>
<p> <code>mhfixmsg</code>, by default, transforms the message in place. If the <code>-outfile</code> switch is enabled, then <code>mhfixmsg</code> does not modify the input message or file, but instead places its output in the specified file. An outfile name of &#8220;-&#8221; specifies the standard output stream. </p>
<p> Combined with the <code>-verbose</code> switch, the <code>-outfile</code> switch can be used to show what transformations <code>mhfixmsg</code> would apply without actually applying them, e.g., </p>
<dl>
<dt>
<dd> mhfixmsg -outfile /dev/null -verbose</dl>
<p> As always, this usage obeys any <code>mhfixmsg</code> switches in the user&#8217;s profile. </p>
<p> <code>-outfile</code> can be combined with <code>rcvstore</code> to add a single transformed message to a different folder, e.g., </p>
<dl>
<dt>
<dd> mhfixmsg -outfile &#8211; | \</p>
<dl>
<dt>
<dd> /usr/libexec/nmh/rcvstore +folder</dl>
</dl>
<h3>Summary of Applicability</h3>
<p> The transformations apply to the parts of a message depending on content type and/or encoding as follows: </p>
<dl>
<dt>
<dd>
<pre>
-decodetext   base64 and quoted-printable encoded text parts
-textcharset  text/plain parts
-reformat     text parts that are not text/plain
-fixboundary  outermost multipart part
-fixcte       multipart part
</pre>
</dl>
<h3>Backup of Original Message/File</h3>
<p> If it applies any transformations to a message or file, and the <code>-outfile</code> switch is not used, <code>mhfixmsg</code> backs up the original the same way as <code>rmm</code>. That is, it uses the <i>rmmproc</i> profile component, if present. If not present, <code>mhfixmsg</code> moves the original message to a backup file. The <code>-rmmproc</code> switch may be used to override this profile component. The <code>-normmproc</code> switch disables the use of any <i>rmmproc</i> profile component and negates all prior <code>-rmmproc</code> switches. </p>
<h3>Integration with inc</h3>
<p> <code>mhfixmsg</code> can be used as an add-hook, as described in /usr/share/doc/nmh-1.6/README-HOOKS. Note that add-hooks are called from all <code>nmh</code> programs that add a message to a folder, not just <code>inc</code>. Alternatively, a simple shell alias or function can be used to call <code>mhfixmsg</code> immediately after a successful invocation of <code>inc</code>. For example, with bash: </p>
<dl>
<dt>
<dd> alias inc=&#8217;inc &amp;&amp; mhfixmsg&#8217;</dl>
<h3>Integration with procmail</h3>
<p> By way of example, here is an excerpt from a procmailrc file that filters messages through <code>mhfixmsg</code> before storing them in the user&#8217;s <i>nmh-workers</i> folder. It also stores the incoming message in the <i>Backups</i> folder in a filename generated by <code>mktemp</code>, which is a non-POSIX utility to generate a temporary file. If you do not have that utility, then the <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) function could form the basis for a substitute. Or, <code>mhfixmsg</code> could be called on the message after it is stored. </p>
<dl>
<dt>
<dd>
<pre>
PATH = /usr/bin:$PATH
MAILDIR = `mhparam path`
MKTEMP = 'mktemp Backups/mhfixmsg.XXXXXXXX'
MHFIXMSG = 'mhfixmsg -noverbose -file - -outfile -'
STORE = /usr/libexec/nmh/rcvstore
:0 w: nmh-worker/procmail.$LOCKEXT
* ^TOnmh-workers [at] nongnu.org
| tee `$MKTEMP` | $MHFIXMSG | $STORE +nmh-workers
</pre>
</dl>
<h2>FILES</h2>
<p> <code>mhfixmsg</code> looks for mhn.defaults in multiple locations: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<pre>
^$HOME/.mh_profile~^The user profile
^/etc/nmh/mhn.defaults~^Default mhfixmsg conversion entries
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^rmmproc:~^Program to delete original messages or files
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1), <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-mhlist/">mhlist</a></i>(1), <i><a href="/docs/linux/man/1-mhparam/">mhparam</a></i>(1), <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1), <i><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></i>(3), <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1), <i><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></i>(5), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1), <i><a href="/docs/linux/man/1-rmm/">rmm</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-decodetext 8bit'</code>
`<code>-notextcharset</code>'
`<code>-reformat</code>'
`<code>-noreplacetextplain</code>'
`<code>-fixboundary</code>'
`<code>-fixcte</code>'
`<code>-noverbose</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The last message selected from a folder will become the current message. If the <code>-file</code> switch or an absolute pathname is used, the context will not be modified. </p>
<h2>Index</h2>
