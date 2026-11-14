---
title: "incm(1)"
name: "incm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-incm/"
description: "incm – Incorporating new mails for Mew"
---

<h2>NAME</h2>
<p> incm &#8211; Incorporating new mails for Mew</p>
<h2>SYNOPSIS</h2>
<p> incm [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>incm</code> utility incorporates new mails from the mbox or the maildir to Mew&#8217;s inbox folder. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-a</code></p>
<dd> Retrieve all mails from maildir/{cur,new} for maildir.</p>
<dt><code>-b</code></p>
<dd> Backup mails. mbox: No truncate mbox file. maildir: To maildir/cur directory.</p>
<dt><code>-c</code></p>
<dd> Use the Content-Length: field, instead of the &quot;From &quot; line, as a mail separator for mbox.</p>
<dt><code>-d</code><i> path</i></p>
<dd> Path to mbox/maildir. If <i>path</i> is a file, mbox is assumed. If <i>path</i> is a directory, maildir is assumed.</p>
<dt><code>-m</code><i> path</i></p>
<dd> The same as the <code>-d</code> option.</p>
<dt><code>-s</code></p>
<dd> Read one mail from stdin instead of mbox/maildir.</p>
<dt><code>-i</code><i> inboxdir</i></p>
<dd> A path to the inbox directory.</p>
<dt><code>-u</code></p>
<dd> Don&#8217;t touch &quot;.mew-mtime&quot;.</p>
<dt><code>-f</code></p>
<dd> Preserve Unix From (Envelope Sender) line in mbox case.</p>
<dt><code>-p</code><i> mode</i></p>
<dd> Specify file mode that creates in mbox case.</p>
<dt><code>-o</code></p>
<dd> Use the suffix when creating messages.</p>
<dt><code>-x</code><i> suffix</i></p>
<dd> Use this <i>suffix</i>.</p>
<dt><code>-h</code></p>
<dd> Display this help message.</p>
<dt><code>-v</code></p>
<dd> Display the version.</dl>
<h3>mbox</h3>
<p> For mbox, the mail separator is &quot;From &quot; in the beginning of lines. The <code>incm</code> utility does not convert &quot;&gt;From &quot; to &quot;From &quot; in the beginning of lines in the body. On Solaris, Content-Length: should be used with the <code>-c</code> option to tell the end of mail. </p>
<p> To lock mbox, a lock file(&quot;&lt;user&gt;.lock&quot;), flock() or lockf(), and open(O_EXLOCK) are used. </p>
<h3>maildir</h3>
<p> For maildir, no lock and no separator are necessary. </p>
<p> Consider the following situation: </p>
<pre><code>
cur /
{
    1, 2
}
new /
{
    3, 4
}
</code></pre>
<p> Executing <code>incm</code> without the options results in:<br />
cur /<br />
{<br />
    1, 2<br />
}<br />
new /<br />
{<br />
}<br />
to inbox:<br />
{<br />
    3, 4<br />
}</p>
<p> Executing <code>incm</code> with the <code>-a</code> option results in:<br />
cur /<br />
{<br />
}<br />
new /<br />
{<br />
}<br />
to inbox:<br />
{<br />
    1, 2, 3, 4<br />
}</p>
<p> Executing <code>incm</code> with the <code>-b</code> option results in:<br />
cur /<br />
{<br />
    1, 2, 3, 4<br />
}<br />
new /<br />
{<br />
}<br />
to inbox:<br />
{<br />
    3, 4<br />
}</p>
<p> Executing <code>incm</code> with the <code>-a</code> option and the <code>-b</code> option results in: </p>
<pre><code>
cur /
{
    1, 2, 3, 4
}
new /
{
}
to inbox:
{
    1, 2, 3, 4
}
</code></pre>
<p> So, if both options are specified, messages are retrieved multiple times. </p>
<h2>Index</h2>
