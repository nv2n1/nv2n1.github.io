---
title: "praliases(8)"
name: "praliases"
section: "8"
letter: "p"
url: "/docs/linux/man/8-praliases/"
description: "praliases – display system mail aliases"
---

<p>praliases &#8211; display system mail aliases</p>
<h2>Synopsis</h2>
<p><code>praliases</code> [<code>-C</code> <i>file</i>] [<code>-f</code> <i>file</i>] [<i>key</i> <i>&#8230;</i>]</p>
<h2>Description</h2>
<p>The <code>praliases</code> utility displays the current system aliases, one per line, in no particular order. The special internal @:@ alias will be displayed if present. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-C </code><i>file</i></p>
<dd>Read the specified sendmail configuration file instead of the default <code>sendmail</code> configuration file.</p>
<dt><code>-f </code><i>file</i></p>
<dd>Read the specified file instead of the configured <code>sendmail</code> system aliases file(s).</dl>
<p> If one or more keys are specified on the command line, only entries which match those keys are displayed. </p>
<p> The <code>praliases</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>Files</h2>
<dl>
<dt>/etc/mail/sendmail.cf</p>
<dd>The default <code>sendmail</code> configuration file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mailq/">mailq</a>(1), <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) </p>
