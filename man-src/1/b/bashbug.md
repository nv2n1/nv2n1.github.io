---

title: "bashbug(1)"
name: "bashbug"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bashbug/"
description: "bashbug – report a bug in bash"
---

<p> bashbug &#8211; report a bug in bash </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bashbug</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<i>bug-report-email-addresses</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>bashbug</code></p>
<dd>is a utility for reporting bugs in Bash to the maintainers. </dd>
<p> <code>bashbug</code> will start up your preferred editor with a preformatted bug report template for you to fill in. Save the file and quit the editor once you have completed the missing fields. <code>bashbug</code> will notify you of any problems with the report and ask for confirmation before sending it. By default the bug report is mailed to both the GNU developers and the Debian Bash maintainers. The recipients can be changed by giving a comma separated list of <i>bug-report-email-addresses</i>. </p>
<p> If you invoke <code>bashbug</code> by accident, just quit your editor. You will always be asked for confirmation before a bug report is sent.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show a brief usage message and exit.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show the version of <code>bashbug</code> and exit.</dd></dl>
<p> <code>bug-report-email-addresses</code></p>
<dl>
<dt>
</dt><dd> Comma separated list of recipients&#8217; email addresses. By default the report is mailed to both the GNU developers and the Debian Bash maintainers.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>DEFEDITOR</code></p>
<dl>
<dt>
</dt><dd> Editor to use for editing the bug report.</dd></dl>
<p> <code>EDITOR</code></p>
<dl>
<dt>
</dt><dd> Editor to use for editing the bug report (overridden by <code>DEFEDITOR</code>).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code>reportbug</code>(1), <code>update-alternatives</code>(8) for preferred editor.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christer Andersson &lt;klamm [at] comhem.se&gt; for the Debian project (but may be used by others). </p>
