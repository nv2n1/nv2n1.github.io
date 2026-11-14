---
title: "formail(1)"
name: "formail"
section: "1"
letter: "f"
url: "/docs/linux/man/1-formail/"
description: "formail – mail (re)formatter"
---

<h2 class="name">NAME</h2>
<p> formail &#8211; mail (re)formatter </p>
<h2>SYNOPSIS</h2>
<p> <code>formail</code> [<i></i><code>+</code>skip] [<i></i><code>&#8211;</code>total] [<code>-bczfrktedqBY</code>] [<code>-p</code> <i>prefix</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-D</code> <i>maxlen idcache</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-l</code> <i>folder</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-x</code> <i>headerfield</i>] [<code>-X</code> <i>headerfield</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-a</code> <i>headerfield</i>] [<code>-A</code> <i>headerfield</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-i</code> <i>headerfield</i>] [<code>-I</code> <i>headerfield</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-u</code> <i>headerfield</i>] [<code>-U</code> <i>headerfield</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-R</code> <i>oldfield</i> <i>newfield</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-n</code> [<i>maxprocs</i> ]] [<code>-m</code> <i>minfields</i>] [<code>-s</code> [<i>command</i> [<i>arg</i> &#8230;]]]<br />
 <code>formail</code> <code>-v</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>formail</code> is a filter that can be used to force mail into mailbox format, perform `From &#8216; escaping, generate auto-replying headers, do simple header munging/extracting or split up a mailbox/digest/articles file. The mail/mailbox/article contents will be expected on stdin. </p>
<p> If formail is supposed to determine the sender of the mail, but is unable to find any, it will substitute `foo@bar&#8217;. </p>
<p> If formail is started without any command line options, it will force any mail coming from stdin into mailbox format and will escape <code>all</code> bogus `From &#8216; lines with a `&gt;&#8217;. </p>
<h2>OPTIONS</h2>
<p> Tp 0.5i <code>-v</code> Formail will print its version number and exit.<br />
 Tp <code>-b</code> Don&#8217;t escape any bogus mailbox headers (i.e., lines starting with `From &#8216;).<br />
 Tp <i></i><code>-p</code> prefix Define a different quotation prefix. If unspecified it defaults to `&gt;&#8217;.<br />
 Tp <code>-Y</code> Assume traditional Berkeley mailbox format, ignoring any <code>Content-Length:</code> fields.<br />
 Tp <code>-c</code> Concatenate continued fields in the header. Might be convenient when postprocessing mail with standard (line oriented) text utilities.<br />
 Tp <code>-z</code> Ensure a whitespace exists between field name and content. Zap fields which contain only a single whitespace character. Zap leading and trailing whitespace on fields extracted with <code>-x</code>.<br />
 Tp <code>-f</code> Force formail to simply pass along any non-mailbox format (i.e., don&#8217;t generate a `From &#8216; line as the first line).<br />
 Tp <code>-r</code> Generate an auto-reply header. This will normally throw away all the existing fields (except X-Loop:) in the original message, fields you wish to preserve need to be named using the <code>-i</code> option. If you use this option in conjunction with <code>-k</code>, you can prevent the body from being `escaped&#8217; by also specifying <code>-b</code>.<br />
 Tp <code>-k</code> When generating the auto-reply header or when extracting fields, keep the body as well.<br />
 Tp <code>-t</code> Trust the sender to have used a valid return address in his header. This causes formail to select the <i>header sender</i> instead of the <i>envelope sender</i> for the reply. This option should be used when generating auto-reply headers from news articles or when the sender of the message is expecting a reply.<br />
 Tp <code>-s</code> The input will be split up into separate mail messages, and piped into a program one by one (a new program is started for every part). <code>-s</code> has to be the last option specified, the first argument following it is expected to be the name of a program, any other arguments will be passed along to it. If you omit the program, then formail will simply concatenate the split mails on stdout again. See <code>FILENO</code>.<br />
 Tp <i></i><code>-n</code> [maxprocs] Tell formail not to wait for every program to finish before starting the next (causes splits to be processed in parallel). <i>Maxprocs</i> optionally specifies an upper limit on the number of concurrently running processes.<br />
 Tp <code>-e</code> Do not require empty lines to be preceding the header of a new message (i.e., the messages could start on every line).<br />
 Tp <code>-d</code> Tell formail that the messages it is supposed to split need not be in strict mailbox format (i.e., allows you to split digests/articles or non-standard mailbox formats). This disables recognition of the <code>Content-Length:</code> field.<br />
 Tp <code>-l folder</code> Generate a log summary in the same style as procmail. This includes the entire &quot;From &quot; line, the Subject: header field, the folder, and the size of the message in bytes. The mailstat command can be used to summarize logs in this format.<br />
 Tp <code>-B</code> Makes formail assume that it is splitting up a BABYL rmail file.<br />
 Tp <i></i><code>-m</code> minfields Allows you to specify the number of consecutive headerfields formail needs to find before it decides it found the start of a new message, it defaults to 2.<br />
 Tp <code>-q</code> Tells formail to (still detect but) be quiet about write errors, duplicate messages and mismatched <code>Content-Length:</code> fields. This option is on by default, to make it display the messages use <code>-q-</code>.<br />
 Tp <i></i><code>-D</code> maxlen idcache Formail will detect if the Message-ID of the current message has already been seen using an <i>idcache</i> file of approximately <i>maxlen</i> size. If not splitting, it will return success if a duplicate has been found. If splitting, it will not output duplicate messages. If used in conjunction with <code>-r</code>, formail will look at the <i>mail address</i> of the envelope sender <i>instead</i> at the Message-ID.<br />
 Tp <i></i><code>-x</code> headerfield Extract the contents of this <i>headerfield</i> from the header. Line continuations will be left intact; if you want the value on a single line then you&#8217;ll also need the <code>-c</code> option.<br />
 Tp <i></i><code>-X</code> headerfield Same as <code>-x</code>, but also preserves/includes the field name.<br />
 Tp <i></i><code>-a</code> headerfield Append a custom <i>headerfield</i> onto the header; but only if a similar field does not exist yet. If you specify either one of the field names <code>Message-ID:</code> or <code>Resent-Message-ID:</code> with no field contents, then formail will generate a unique message-ID for you.<br />
 Tp <i></i><code>-A</code> headerfield Append a custom <i>headerfield</i> onto the header in any case.<br />
 Tp <i></i><code>-i</code> headerfield Same as <code>-A</code>, except that any existing similar fields are renamed by prepending an &#8220;Old-&#8221; prefix. If <i>headerfield</i> consists only of a field-name, it will not be appended.<br />
 Tp <i></i><code>-I</code> headerfield Same as <code>-i</code>, except that any existing similar fields are simply removed. If <i>headerfield</i> consists only of a field-name, it effectively deletes the field.<br />
 Tp <i></i><code>-u</code> headerfield Make the first occurrence of this field unique, and thus delete all subsequent occurrences of it.<br />
 Tp <i></i><code>-U</code> headerfield Make the last occurrence of this field unique, and thus delete all preceding occurrences of it.<br />
 Tp <i></i><code>-R</code> oldfield newfield Renames all occurrences of the fieldname <i>oldfield</i> into <i>newfield</i>.<br />
 Tp <i></i><code>+</code>skip Skip the first <i>skip</i> messages while splitting.<br />
 Tp <i></i><code>&#8211;</code>total Output at most <i>total</i> messages while splitting. </p>
<h2>NOTES</h2>
<p> When renaming, removing, or extracting fields, partial fieldnames may be used to specify all fields that start with the specified value. </p>
<p> By default, when generating an auto-reply header procmail selects the envelope sender from the input message. This is correct for vacation messages and other automatic replies regarding the routing or delivery of the original message. If the sender is expecting a reply or the reply is being generated in response to the contents of the original message then the -t option should be used. </p>
<p> <code>RFC822</code>, the original standard governing the format of Internet mail messages, did not specify whether Resent header fields (those that begin with `Resent-&#8216;, such as `Resent-From:&#8217;) should be considered when generating a reply. Since then, the recommended usage of the Resent headers has evolved to consider them as purely informational and not for use when generating a reply. This has been codified in <code>RFC2822</code>, the new Internet Message Format standard, which states in part:</p>
<dl>
<dt>
<dd> Resent fields are used to identify a message as having been reintroduced into the transport system by a user. The purpose of using resent fields is to have the message appear to the final recipient as if it were sent directly by the original sender, with all of the original fields remaining the same&#8230;.They MUST NOT be used in the normal processing of replies or other such automatic actions on messages.</dl>
<p> While formail now ignores Resent headers when generating header replies, versions of formail prior to 3.14 gave such headers a high precedence. If the old behavior is needed for established applications it can be specified by calling formail with the option `-a Resent-&#8216; in addition to the -r and -t options. This usage is deprecated and should not be used in new applications. </p>
<h2>ENVIRONMENT</h2>
<p> Tp .B FILENO <code>FILENO</code> While splitting, formail assigns the message number currently being output to this variable. By presetting FILENO, you can change the initial message number being used and the width of the zero-padded output. If FILENO is unset it will default to 000. If FILENO is non-empty and does not contain a number, FILENO generation is disabled. </p>
<h2>EXAMPLES</h2>
<p> To split up a digest one usually uses: </p>
<pre>
<dl><dt><dd>formail +1 -ds &gt;&gt;the_mailbox_of_your_choice
</dl>
</pre>
<p> or </p>
<pre>
<dl><dt><dd>formail +1 -ds procmail
</dl>
</pre>
<p> To remove all Received: fields from the header: </p>
<pre>
<dl><dt><dd>formail -I Received:
</dl>
</pre>
<p> To remove all fields except From: and Subject: from the header: </p>
<pre>
<dl><dt><dd>formail -k -X From: -X Subject:
</dl>
</pre>
<p> To supersede the Reply-To: field in a header you could use: </p>
<pre>
<dl><dt><dd>formail -i &quot;Reply-To: foo@bar&quot;
</dl>
</pre>
<p> To convert a non-standard mailbox file into a standard mailbox file you can use: </p>
<pre>
<dl><dt><dd>formail -ds &lt;old_mailbox &gt;&gt;new_mailbox
</dl>
</pre>
<p> Or, if you have a very tolerant mailer: </p>
<pre>
<dl><dt><dd>formail -a Date: -ds &lt;old_mailbox &gt;&gt;new_mailbox
</dl>
</pre>
<p> To extract the header from a message: </p>
<pre>
<dl><dt><dd>formail -X &quot;&quot;
</dl>
</pre>
<p> or </p>
<pre>
<dl><dt><dd>sed -e '/^$/ q'
</dl>
</pre>
<p> To extract the body from a message: </p>
<pre>
<dl><dt><dd>formail -I &quot;&quot;
</dl>
</pre>
<p> or </p>
<pre>
<dl><dt><dd>sed -e '1,/^$/ d'
</dl>
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1), <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code>RFC822</code>, <code>RFC2822</code>, <code>RFC1123</code> </p>
<h2>DIAGNOSTICS</h2>
<p> Tp 2.3i Can&#8217;t fork Too many processes on this machine.<br />
 Tp Content-Length: field exceeds actual length by nnn bytes The Content-Length: field in the header specified a length that was longer than the actual body. This causes this message to absorb a number of subsequent messages following it in the same mailbox.<br />
 Tp Couldn&#8217;t write to stdout The program that formail was trying to pipe into didn&#8217;t accept all the data formail sent to it; this diagnostic can be suppressed by the <code>-q</code> option.<br />
 Tp Duplicate key found: x The Message-ID or sender x in this message was found in the idcache; this diagnostic can be suppressed by the <code>-q</code> option.<br />
 Tp Failed to execute &quot;x&quot; Program not in path, or not executable.<br />
 Tp File table full Too many open files on this machine.<br />
 Tp Invalid field-name: &quot;x&quot; The specified field-name &quot;x&quot; contains control characters, or cannot be a partial field-name for this option. </p>
<h2>WARNINGS</h2>
<p> You can save yourself and others a lot of grief if you try to avoid using this autoreply feature on mails coming through mailinglists. Depending on the format of the incoming mail (which in turn depends on both the original sender&#8217;s mail agent and the mailinglist setup) formail could decide to generate an autoreply header that replies to the list. </p>
<p> In the tradition of UN*X utilities, formail will do exactly what you ask it to, even if it results in a non-<code>RFC822</code> compliant message. In particular, formail will let you generate header fields whose name ends in a space instead of a colon. While this is correct for the leading `From &#8216; line, that line is not a header field so much as the message separator for the mbox mailbox format. Multiple occurrences of such a line or any other colonless header field will be considered by many mail programs, including formail itself, as the beginning of a new message. Others will consider the message to be corrupt. Because of this, you should not use the <code>-i</code> option with the `From &#8216; line as the resulting renamed line, `Old-From &#8216;, will probably not do what you want it to. If you want to save the original `From &#8216; line, rename it with the <code>-R</code> option to a legal header field such as `X-From_:&#8217;. </p>
<h2>BUGS</h2>
<p> When formail has to generate a leading `From &#8216; line it normally will contain the current date. If formail is given the option `-a Date:&#8217;, it will use the date from the `Date:&#8217; field in the header (if present). However, since formail copies it verbatim, the format will differ from that expected by most mail readers. </p>
<p> If formail is instructed to delete or rename the leading `From &#8216; line, it will not automatically regenerate it as usual. To force formail to regenerate it in this case, include <code>-a &#8216;From &#8216;</code>. </p>
<p> If formail is not called as the first program in a pipe and it is told to split up the input in several messages, then formail will not terminate until the program it receives the input from closes its output or terminates itself. </p>
<p> If formail is instructed to generate an autoreply mail, it will <code>never</code> put more than one address in the `To:&#8217; field. </p>
<h2>MISCELLANEOUS</h2>
<p> Formail is eight-bit clean. </p>
<p> When formail has to determine the sender&#8217;s address, every <code>RFC822</code> conforming mail address is allowed. Formail will always strip down the address to its minimal form (deleting excessive comments and whitespace). </p>
<p> The regular expression that is used to find `real&#8217; postmarks is: </p>
<pre><code>
"

From [	 ]*[^	
 ]+[	 ]+[^
	 ]"
</code></pre>
<p> If a <code>Content-Length:</code> field is found in a header, formail will copy the number of specified bytes in the body verbatim before resuming the regular scanning for message boundaries (except when splitting digests or Berkeley mailbox format is assumed). </p>
<p> Any header lines immediately following the leading `From &#8216; line that start with `&gt;From &#8216; are considered to be a continuation of the `From &#8216; line. If instructed to rename the `From &#8216; line, formail will change each leading `&gt;&#8217; into a space, thereby transforming those lines into normal <code>RFC822</code> continuations. </p>
<h2>NOTES</h2>
<p> Calling up formail with the -h or -? options will cause it to display a command-line help page.</p>
<h2>SOURCE</h2>
<p> This program is part of the <i>procmail mail-processing-package</i> (v3.23pre) available at <a rel="nofollow" href="http://www.procmail.org/">http://www.procmail.org/</a> or <a href="ftp://ftp.procmail.org">ftp.procmail.org</a> in <code>pub/procmail/</code>.</p>
<h2>MAILINGLIST</h2>
<p> There exists a mailinglist for questions relating to any program in the procmail package: </p>
<pre>
<dl><dt><dd>&lt;procmail-users [at] procmail.org&gt;
<dl><dt><dd>for submitting questions/answers.
</dl>
</pre>
<p> &lt;procmail-users-request [at] procmail.org&gt; </p>
<pre>
<dl><dt><dd>for subscription requests.
</dl>
</pre>
</dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to </p>
<pre>
<dl><dt><dd>procmail-announce-request [at] procmail.org
</dl>
</pre>
<p> (this is a readonly list). </p>
<h2>AUTHORS</h2>
<p> Stephen R. van den Berg </p>
<pre>
<dl><dt><dd>&lt;srb [at] cuci.nl&gt;
</dl>
</pre>
<p> Philip A. Guenther </p>
<pre>
<dl><dt><dd>&lt;guenther [at] sendmail.com&gt;
</dl>
</pre>
<h2>Index</h2>
