---
title: "header_checks(5)"
name: "header_checks"
section: "5"
letter: "h"
url: "/docs/linux/man/5-header_checks/"
description: "header_checks – Postfix built-in content inspection"
---

<p>header_checks &#8211; Postfix built-in content inspection</p>
<h2>Synopsis</h2>
<pre><code>header_checks = pcre:/etc/postfix/header_checks</code>
<code>mime_header_checks = pcre:/etc/postfix/mime_header_checks</code>
<code>nested_header_checks = pcre:/etc/postfix/nested_header_checks</code>
<code>body_checks = pcre:/etc/postfix/body_checks</code>
<code>milter_header_checks = pcre:/etc/postfix/milter_header_checks</code>
<code>smtp_header_checks = pcre:/etc/postfix/smtp_header_checks</code>
<code>smtp_mime_header_checks = pcre:/etc/postfix/smtp_mime_header_checks</code>
<code>smtp_nested_header_checks = pcre:/etc/postfix/smtp_nested_header_checks</code>
<code>smtp_body_checks = pcre:/etc/postfix/smtp_body_checks</code>
<code>postmap -q &quot;</code><i>string</i><code>&quot; pcre:/etc/postfix/</code><i>filename</i>
<code>postmap -q - pcre:/etc/postfix/</code><i>filename</i> &lt;<i>inputfile</i></pre>
<h2>Description</h2>
<p>This document describes access control on the content of message headers and message body lines; it is implemented by the Postfix <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) server before mail is queued. See <code><a href="/docs/linux/man/5-access/">access</a></code>(5) for access control on remote SMTP client information. </p>
<p> Each message header or message body line is compared against a list of patterns. When a match is found the corresponding action is executed, and the matching process is repeated for the next message header or message body line. </p>
<p> Note: message headers are examined one logical header at a time, even when a message header spans multiple lines. Body lines are always examined one line at a time. </p>
<p> For examples, see the EXAMPLES section at the end of this manual page. </p>
<p> Postfix header or body_checks are designed to stop a flood of mail from worms or viruses; they do not decode attachments, and they do not unzip archives. See the documents referenced below in the README FILES section if you need more sophisticated content analysis.</p>
<h2>Filters While Receiving Mail</h2>
<p>Postfix implements the following four built-in content inspection classes while receiving mail:</p>
<dl>
<dt><code>header_checks</code> (default: empty)</p>
<dd>These are applied to initial message headers (except for the headers that are processed with <code>mime_header_checks</code>).</p>
<dt><code>mime_header_checks</code> (default: <code>$header_checks</code>)</p>
<dd>These are applied to MIME related message headers only. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>nested_header_checks</code> (default: <code>$header_checks</code>)</p>
<dd>These are applied to message headers of attached email messages (except for the headers that are processed with <code>mime_header_checks</code>). </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>body_checks</code></p>
<dd>These are applied to all other content, including multi-part message boundaries. </p>
<p> With Postfix versions before 2.0, all content after the initial message headers is treated as body content.</dl>
<h2>Filters After Receiving Mail</h2>
<p>Postfix supports a subset of the built-in content inspection classes after the message is received:</p>
<dl>
<dt><code>milter_header_checks</code> (default: empty)</p>
<dd>These are applied to headers that are added with Milter applications. </p>
<p> This feature is available in Postfix 2.7 and later.</dl>
<h2>Filters While Delivering Mail</h2>
<p>Postfix supports all four content inspection classes while delivering mail via SMTP.</p>
<dl>
<dt><code>smtp_header_checks</code> (default: empty)</p>
<dd>
<dt><code>smtp_mime_header_checks</code> (default: empty)</p>
<dd>
<dt><code>smtp_nested_header_checks</code> (default: empty)</p>
<dd>
<dt><code>smtp_body_checks</code> (default: empty)</p>
<dd>These features are available in Postfix 2.5 and later.</dl>
<h2>Compatibility</h2>
<p>With Postfix version 2.2 and earlier specify &quot;<code>postmap -fq</code>&quot; to query a table that contains case sensitive patterns. By default, regexp: and pcre: patterns are case insensitive.</p>
<h2>Table Format</h2>
<p>This document assumes that header and body_checks rules are specified in the form of Postfix regular expression lookup tables. Usually the best performance is obtained with <code>pcre</code> (Perl Compatible Regular Expression) tables. The <code>regexp</code> (POSIX regular expressions) tables are usually slower, but more widely available. Use the command &quot;<code>postconf -m</code>&quot; to find out what lookup table types your Postfix system supports. </p>
<p> The general format of Postfix regular expression tables is given below. For a discussion of specific pattern or flags syntax, see <code><a href="/docs/linux/man/5-pcre_table/">pcre_table</a></code>(5) or <code><a href="/docs/linux/man/5-regexp_table/">regexp_table</a></code>(5), respectively.</p>
<dl>
<dt><code>/</code><i>pattern</i><code>/</code><i>flags action</i></p>
<dd>When /<i>pattern</i>/ matches the input string, execute the corresponding <i>action</i>. See below for a list of possible actions.</p>
<dt><code>!/</code><i>pattern</i><code>/</code><i>flags action</i></p>
<dd>When /<i>pattern</i>/ does <code>not</code> match the input string, execute the corresponding <i>action</i>.</p>
<dt><code>if /</code><i>pattern</i><code>/</code><i>flags</i></p>
<dd>
<dt><code>endif</code></p>
<dd>If the input string matches /<i>pattern</i>/, then match that input string against the patterns between <code>if</code> and <code>endif</code>. The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to patterns inside <code>if</code>..<code>endif</code>.</p>
<dt><code>if !/</code><i>pattern</i><code>/</code><i>flags</i></p>
<dd>
<dt><code>endif</code></p>
<dd>If the input string does not match /<i>pattern</i>/, then match that input string against the patterns between <code>if</code> and <code>endif</code>. The <code>if</code>..<code>endif</code> can nest.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A pattern/action line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Table Search Order</h2>
<p>For each line of message input, the patterns are applied in the order as specified in the table. When a pattern is found that matches the input line, the corresponding action is executed and then the next input line is inspected.</p>
<h2>Text Substitution</h2>
<p>Substitution of substrings from the matched expression into the <i>action</i> string is possible using the conventional Perl syntax (<code>$1</code>, <code>$2</code>, etc.). The macros in the result string may need to be written as <code>${n}</code> or <code>$(n)</code> if they aren&#8217;t followed by whitespace. </p>
<p> Note: since negated patterns (those preceded by <code>!</code>) return a result when the expression does not match, substitutions are not available for negated patterns.</p>
<h2>Actions</h2>
<p>Action names are case insensitive. They are shown in upper case for consistency with other Postfix documentation.</p>
<dl>
<dt><code>BCC </code><i>user [at] domain</i></p>
<dd>Add the specified address as a BCC recipient, and inspect the next input line. The address must have a local part and domain part. The number of BCC addresses that can be added is limited only by the amount of available storage space. </p>
<p> Note 1: the BCC address is added as if it was specified with NOTIFY=NONE. The sender will not be notified when the BCC address is undeliverable, as long as all down-stream software implements RFC 3461. </p>
<p> Note 2: this ignores duplicate addresses (with the same delivery status notification options). </p>
<p> This feature is available in Postfix 3.0 and later. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>DISCARD </code><i>optional text&#8230;</i></p>
<dd>Claim successful delivery and silently discard the message. Do not inspect the remainder of the input message. Log the optional text if specified, otherwise log a generic message. </p>
<p> Note: this action disables further header or body_checks inspection of the current message and affects all recipients. To discard only one recipient without discarding the entire message, use the <a href="/docs/linux/man/5-transport/">transport</a>(5) table to direct mail to the <a href="/docs/linux/man/8-discard/">discard</a>(8) service. </p>
<p> This feature is available in Postfix 2.0 and later. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>DUNNO</code></p>
<dd>Pretend that the input line did not match any pattern, and inspect the next input line. This action can be used to shorten the table search. </p>
<p> For backwards compatibility reasons, Postfix also accepts <code>OK</code> but it is (and always has been) treated as <code>DUNNO</code>. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt><code>FILTER </code><i>transport:destination</i></p>
<dd>Override the content_filter parameter setting, and inspect the next input line. After the message is queued, send the entire message through the specified external content filter. The <i>transport</i> name specifies the first field of a mail delivery agent definition in master.cf; the syntax of the next-hop <i>destination</i> is described in the manual page of the corresponding delivery agent. More information about external content filters is in the Postfix FILTER_README file. </p>
<p> Note 1: do not use $<i>number</i> regular expression substitutions for <i>transport</i> or <i>destination</i> unless you know that the information has a trusted origin. </p>
<p> Note 2: this action overrides the main.cf <code>content_filter</code> setting, and affects all recipients of the message. In the case that multiple <code>FILTER</code> actions fire, only the last one is executed. </p>
<p> Note 3: the purpose of the FILTER command is to override message routing. To override the recipient&#8217;s <i>transport</i> but not the next-hop <i>destination</i>, specify an empty filter <i>destination</i> (Postfix 2.7 and later), or specify a <i>transport:destination</i> that delivers through a different Postfix instance (Postfix 2.6 and earlier). Other options are using the recipient-dependent <code>transport_maps</code> or the sender-dependent <code>sender_dependent_default_transport_maps</code> features. </p>
<p> This feature is available in Postfix 2.0 and later. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>HOLD </code><i>optional text&#8230;</i></p>
<dd>Arrange for the message to be placed on the <code>hold</code> queue, and inspect the next input line. The message remains on <code>hold</code> until someone either deletes it or releases it for delivery. Log the optional text if specified, otherwise log a generic message. </p>
<p> Mail that is placed on hold can be examined with the <code><a href="/docs/linux/man/1-postcat/">postcat</a></code>(1) command, and can be destroyed or released with the <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) command. </p>
<p> Note: use &quot;<code>postsuper -r</code>&quot; to release mail that was kept on hold for a significant fraction of <code>$maximal_queue_lifetime</code> or <code>$bounce_queue_lifetime</code>, or longer. Use &quot;<code>postsuper -H</code>&quot; only for mail that will not expire within a few delivery attempts. </p>
<p> Note: this action affects all recipients of the message. </p>
<p> This feature is available in Postfix 2.0 and later. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>IGNORE</code></p>
<dd>Delete the current line from the input, and inspect the next input line. See <code>STRIP</code> for an alternative that logs the action.</p>
<dt><code>INFO </code><i>optional text&#8230;</i></p>
<dd>Log an &quot;info:&quot; record with the <i>optional text&#8230;</i> (or log a generic text), and inspect the next input line. This action is useful for routine logging or for debugging. </p>
<p> This feature is available in Postfix 2.8 and later.</p>
<dt><code>PASS </code><i>optional text&#8230;</i></p>
<dd>Log a &quot;pass:&quot; record with the <i>optional text&#8230;</i> (or log a generic text), and turn off header, body, and Milter inspection for the remainder of this message. </p>
<p> Note: this feature relies on trust in information that is easy to forge. </p>
<p> This feature is available in Postfix 3.2 and later. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>PREPEND </code><i>text&#8230;</i></p>
<dd>Prepend one line with the specified text, and inspect the next input line. </p>
<p> Notes:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>The prepended text is output on a separate line, immediately before the input that triggered the <code>PREPEND</code> action.</p>
<dt>&bull;</p>
<dd>The prepended text is not considered part of the input stream: it is not subject to header/body checks or address rewriting, and it does not affect the way that Postfix adds missing message headers.</p>
<dt>&bull;</p>
<dd>When prepending text before a message header line, the prepended text must begin with a valid message header label.</p>
<dt>&bull;</p>
<dd>This action cannot be used to prepend multi-line text.</dl>
</dl>
<dd>This feature is available in Postfix 2.1 and later. </p>
<p> This feature is not supported with milter_header_checks.</p>
<dt><code>REDIRECT </code><i>user [at] domain</i></p>
<dd>Write a message redirection request to the queue file, and inspect the next input line. After the message is queued, it will be sent to the specified address instead of the intended recipient(s). </p>
<p> Note: this action overrides the <code>FILTER</code> action, and affects all recipients of the message. If multiple <code>REDIRECT</code> actions fire, only the last one is executed. </p>
<p> This feature is available in Postfix 2.1 and later. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>REPLACE </code><i>text&#8230;</i></p>
<dd>Replace the current line with the specified text, and inspect the next input line. </p>
<p> This feature is available in Postfix 2.2 and later. The description below applies to Postfix 2.2.2 and later. </p>
<p> Notes:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>When replacing a message header line, the replacement text must begin with a valid header label.</p>
<dt>&bull;</p>
<dd>The replaced text remains part of the input stream. Unlike the result from the <code>PREPEND</code> action, a replaced message header may be subject to address rewriting and may affect the way that Postfix adds missing message headers.</dl>
</dl>
<dt><code>REJECT </code><i>optional text&#8230;</i></p>
<dd>Reject the entire message. Do not inspect the remainder of the input message. Reply with <i>optional text&#8230;</i> when the optional text is specified, otherwise reply with a generic error message. </p>
<p> Note: this action disables further header or body_checks inspection of the current message and affects all recipients. </p>
<p> Postfix version 2.3 and later support enhanced status codes. When no code is specified at the beginning of <i>optional text&#8230;</i>, Postfix inserts a default enhanced status code of &quot;5.7.1&quot;. </p>
<p> This feature is not supported with smtp header/body checks.</p>
<dt><code>STRIP </code><i>optional text&#8230;</i></p>
<dd>Log a &quot;strip:&quot; record with the <i>optional text&#8230;</i> (or log a generic text), delete the input line from the input, and inspect the next input line. See <code>IGNORE</code> for a silent alternative. </p>
<p> This feature is available in Postfix 3.2 and later.</p>
<dt><code>WARN </code><i>optional text&#8230;</i></p>
<dd>Log a &quot;warning:&quot; record with the <i>optional text&#8230;</i> (or log a generic text), and inspect the next input line. This action is useful for debugging and for testing a pattern before applying more drastic actions.</dl>
<h2>Bugs</h2>
<p>Empty lines never match, because some map types mis-behave when given a zero-length search string. This limitation may be removed for regular expression tables in a future release. </p>
<p> Many people overlook the main limitations of header and body_checks rules.</p>
<dl>
<dt>&bull;</p>
<dd>These rules operate on one logical message header or one body line at a time. A decision made for one line is not carried over to the next line.</p>
<dt>&bull;</p>
<dd>If text in the message body is encoded (RFC 2045) then the rules need to be specified for the encoded form.</p>
<dt>&bull;</p>
<dd>Likewise, when message headers are encoded (RFC 2047) then the rules need to be specified for the encoded form.</dl>
<p> Message headers added by the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon itself are excluded from inspection. Examples of such message headers are <code>From:</code>, <code>To:</code>, <code>Message-ID:</code>, <code>Date:</code>. </p>
<p> Message headers deleted by the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon will be examined before they are deleted. Examples are: <code>Bcc:</code>, <code>Content-Length:</code>, <code>Return-Path:</code>.</p>
<h2>Configuration Parameters</h2>
<dl>
<dt><code>body_checks</code></p>
<dd>Lookup tables with content filter rules for message body lines. These filters see one physical line at a time, in chunks of at most <code>$line_length_limit</code> bytes.</p>
<dt><code>body_checks_size_limit</code></p>
<dd>The amount of content per message body segment (attachment) that is subjected to <code>$body_checks</code> filtering.</p>
<dt><code>header_checks</code></p>
<dd>
<dt><code>mime_header_checks</code> (default: <code>$header_checks</code>)</p>
<dd>
<dt><code>nested_header_checks</code> (default: <code>$header_checks</code>)</p>
<dd>Lookup tables with content filter rules for message header lines: respectively, these are applied to the initial message headers (not including MIME headers), to the MIME headers anywhere in the message, and to the initial headers of attached messages. </p>
<p> Note: these filters see one logical message header at a time, even when a message header spans multiple lines. Message headers that are longer than <code>$header_size_limit</code> characters are truncated.</p>
<dt><code>disable_mime_input_processing</code></p>
<dd>While receiving mail, give no special treatment to MIME related message headers; all text after the initial message headers is considered to be part of the message body. This means that <code>header_checks</code> is applied to all the initial message headers, and that <code>body_checks</code> is applied to the remainder of the message. </p>
<p> Note: when used in this manner, <code>body_checks</code> will process a multi-line message header one line at a time.</dl>
<h2>Examples</h2>
<p>Header pattern to block attachments with bad file name extensions. For convenience, the PCRE /x flag is specified, so that there is no need to collapse the pattern into a single line of text. The purpose of the [[:xdigit:]] sub-expressions is to recognize Windows CLSID strings. </p>
<pre><code>/etc/postfix/main.cf:
header_checks = pcre:/etc/postfix/header_checks.pcre

/etc/postfix/header_checks.pcre:
/^Content-(Disposition|Type).*name\s*=\s*&quot;?([^;]*(\.|=2E)(
ade|adp|asp|bas|bat|chm|cmd|com|cpl|crt|dll|exe|
hlp|ht[at]|
inf|ins|isp|jse?|lnk|md[betw]|ms[cipt]|nws|
\{[[:xdigit:]]{8}(?:-[[:xdigit:]]{4}){3}-[[:xdigit:]]{12}\}|
ops|pcd|pif|prf|reg|sc[frt]|sh[bsm]|swf|
vb[esx]?|vxd|ws[cfh]))(\?=)?&quot;?\s*(;|$)/x
REJECT Attachment name &quot;$2&quot; may not end with &quot;.$4&quot;</code></pre>
<p> Body pattern to stop a specific HTML browser vulnerability exploit. </p>
<pre>/etc/postfix/main.cf:
 body_checks = regexp:/etc/postfix/body_checks
/etc/postfix/body_checks:
 /^&lt;iframe src=(3D)?cid:.* height=(3D)?0 width=(3D)?0&gt;$/
 REJECT IFRAME vulnerability exploit</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), canonicalize and enqueue Postfix message
<a href="//www.systutorials.com/docs/linux/man/5-pcre_table/">pcre_table</a>(5), format of PCRE lookup tables
<a href="//www.systutorials.com/docs/linux/man/5-regexp_table/">regexp_table</a>(5), format of POSIX regular expression tables
<a href="//www.systutorials.com/docs/linux/man/1-postconf/">postconf</a>(1), Postfix configuration utility
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table management
<a href="//www.systutorials.com/docs/linux/man/1-postsuper/">postsuper</a>(1), Postfix janitor
<a href="//www.systutorials.com/docs/linux/man/1-postcat/">postcat</a>(1), show Postfix queue file contents
RFC 2045, base64 and quoted-printable encoding rules
RFC 2047, message header encoding for non-ASCII text</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview
CONTENT_INSPECTION_README, Postfix content inspection overview
BUILTIN_FILTER_README, Postfix built-in content inspection
BACKSCATTER_README, blocking returned forged mail</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
