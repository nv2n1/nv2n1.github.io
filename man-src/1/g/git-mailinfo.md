---
title: "git-mailinfo(1)"
name: "git-mailinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mailinfo/"
description: "git-mailinfo – Extracts patch and authorship from a single e-mail message"
---

<h2 class="name">NAME</h2>
<p> git-mailinfo &#8211; Extracts patch and authorship from a single e-mail message </p>
<h2>SYNOPSIS</h2>
<pre><code>
git mailinfo[-k | -b][-u | --encoding = &lt;encoding&gt; | -n]
            [--[no - ] scissors][--quoted - cr = &lt;action&gt;]&lt;msg&gt;&lt;patch&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads a single e-mail message from the standard input, and writes the commit log message in &lt;msg&gt; file, and the patches in &lt;patch&gt; file. The author name, e-mail and e-mail subject are written out to the standard output to be used by <i>git am</i> to create a commit. It is usually not necessary to use this command directly. See <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1) instead.</p>
<h2>OPTIONS</h2>
<p> -k</p>
<dl>
<dt>
<dd> Usually the program removes email cruft from the Subject: header line to extract the title line for the commit log message. This option prevents this munging, and is most useful when used to read back <i>git format-patch -k</i> output. </p>
<p> Specifically, the following are removed until none of them remain: </p>
<dl>
<dt>
<dd> &bull; Leading and trailing whitespace.</dl>
<dl>
<dt>
<dd> &bull; Leading <code>Re:</code>, <code>re:</code>, and <code>:</code>.</dl>
<dl>
<dt>
<dd> &bull; Leading bracketed strings (between <code>[</code> and <code>]</code>, usually <code>[PATCH]</code>).</dl>
<p> Finally, runs of whitespace are normalized to a single ASCII space character.</dl>
<p> -b</p>
<dl>
<dt>
<dd> When -k is not in effect, all leading strings bracketed with <i>[</i> and <i>]</i> pairs are stripped. This option limits the stripping to only the pairs whose bracketed string contains the word &quot;PATCH&quot;.</dl>
<p> -u</p>
<dl>
<dt>
<dd> The commit log message, author name and author email are taken from the e-mail, and after minimally decoding MIME transfer encoding, re-coded in the charset specified by <code>i18n.commitEncoding</code> (defaulting to UTF-8) by transliterating them. This used to be optional but now it is the default. </p>
<p> Note that the patch is always used as-is without charset conversion, even with this flag.</dl>
<p> &#8211;encoding=&lt;encoding&gt;</p>
<dl>
<dt>
<dd> Similar to -u. But when re-coding, the charset specified here is used instead of the one specified by <code>i18n.commitEncoding</code> or UTF-8.</dl>
<p> -n</p>
<dl>
<dt>
<dd> Disable all charset re-coding of the metadata.</dl>
<p> -m, &#8211;message-id</p>
<dl>
<dt>
<dd> Copy the Message-ID header at the end of the commit message. This is useful in order to associate commits with mailing list discussions.</dl>
<p> &#8211;scissors</p>
<dl>
<dt>
<dd> Remove everything in body before a scissors line (e.g. &quot;&#8211; &gt;8 &#8211;&quot;). The line represents scissors and perforation marks, and is used to request the reader to cut the message at that line. If that line appears in the body of the message before the patch, everything before it (including the scissors line itself) is ignored when this option is used. </p>
<p> This is useful if you want to begin your message in a discussion thread with comments and suggestions on the message you are responding to, and to conclude it with a patch submission, separating the discussion and the beginning of the proposed commit log message with a scissors line. </p>
<p> This can be enabled by default with the configuration option mailinfo.scissors.</dl>
<p> &#8211;no-scissors</p>
<dl>
<dt>
<dd> Ignore scissors lines. Useful for overriding mailinfo.scissors settings.</dl>
<p> &#8211;quoted-cr=&lt;action&gt;</p>
<dl>
<dt>
<dd> Action when processes email messages sent with base64 or quoted-printable encoding, and the decoded lines end with a CRLF instead of a simple LF. </p>
<p> The valid actions are: </p>
<dl>
<dt>
<dd> &bull; <code>nowarn</code>: Git will do nothing when such a CRLF is found.</dl>
<dl>
<dt>
<dd> &bull; <code>warn</code>: Git will issue a warning for each message if such a CRLF is found.</dl>
<dl>
<dt>
<dd> &bull; <code>strip</code>: Git will convert those CRLF to LF.</dl>
<p> The default action could be set by configuration option <code>mailinfo.quotedCR</code>. If no such configuration option has been set, <code>warn</code> will be used.</dl>
<p> &lt;msg&gt;</p>
<dl>
<dt>
<dd> The commit log message extracted from e-mail, usually except the title line which comes from e-mail Subject.</dl>
<p> &lt;patch&gt;</p>
<dl>
<dt>
<dd> The patch extracted from e-mail.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
