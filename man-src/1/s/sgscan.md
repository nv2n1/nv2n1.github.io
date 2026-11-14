---
title: "sgscan(1)"
name: "sgscan"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgscan/"
description: "sgscan – scan an file or mailbox for viruses/spams"
---

<h2>NAME</h2>
<p> sgscan &#8211; scan an file or mailbox for viruses/spams</p>
<h2>SYNOPSIS</h2>
<p> <code>sgscan</code> [&#8211;help] [&#8211;config filename] [&#8211;debug level] [&#8211;clean] [&#8211;verbose] [&#8211;quiet] [&#8211;av-only] files&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This command is a part of sagator. It can be used to scan files or mailboxes for viruses/spams. It also can be used to clean mailboxes (if some viruses passes through sagator).</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;help</p>
<dd> Display a short help text.</p>
<dt>&#8211;config filename</p>
<dd> Load &quot;filename&quot; as alternate config. This filename must be without &quot;.py&quot; extension.</p>
<dt>&#8211;debug level</p>
<dd> Set debug level to &quot;level&quot;. You can specifi level from 0 to 9.</p>
<dt>&#8211;clean</p>
<dd> Clean all known viruses from mailboxes.</p>
<dt>&#8211;quiet</p>
<dd> Quiet output. If an infection/spam will be found, only increment an counter and do not display anything.</p>
<dt>&#8211;verbose</p>
<dd> Verbose output. Also clean emails are shown. Virus name &quot;CLEAN&quot; will be shown.</p>
<dt>&#8211;progress</p>
<dd> Show progress indicator. Shows total number of emails in mailbox, email counter, infection/spam count and estimation time.</p>
<dt>&#8211;av-only</p>
<dd> Use only antivirus scanners and do not use antispam scanners.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Scan all mailboxes for viruses.</p>
<dd> <code>sgscan</code> &#8211;av-only /var/mail/*</p>
<dt>Scan and clean all mailboxes:</p>
<dd> <code>sgscan</code> &#8211;clean /var/mail/*</dl>
<h2>AUTHOR</h2>
<p> Jan ONDREJ (SAL) &lt;ondrejj (at) salstar.sk&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sgfilter/">sgfilter</a>(1), <a href="/docs/linux/man/8-sagator/">sagator</a>(8), <a href="/docs/linux/man/8-sqback/">sqback</a>(8) </p>
<h2>Index</h2>
