---
title: "mboxgrep(1)"
name: "mboxgrep"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mboxgrep/"
description: "mboxgrep – displays email messages matching a pattern"
---

<h2>NAME</h2>
<p> mboxgrep &#8211; displays email messages matching a pattern</p>
<h2>SYNOPSIS</h2>
<p> <code>mboxgrep</code> [<i>OPTIONS</i>] PATTERN [<i>MAILBOX</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page refers to <code>mboxgrep</code> version <code>0.7.9</code>. </p>
<p> <code>mboxgrep</code> scans a <i>MAILBOX</i> and displays messages matching <i>PATTERN.</i> </p>
<p> If a mailbox name is ommited, or a single dash (-) is given instead, it reads from standard input. It can read mbox folders or output from another <code>mboxgrep</code> process from standard input. </p>
<p> <code>mboxgrep</code> understands POSIX regular expressions, as well as Perl compatible regular expressions (if enabled at compile time). <i>MAILBOX</i> can be either a:</p>
<dl>
<dt>*</p>
<dd> mbox folder (either plain or compressed)</p>
<dt>*</p>
<dd> MH folder</p>
<dt>*</p>
<dd> Gnus nnmh or nnml folder</p>
<dt>*</p>
<dd> qmail-style maildir folder</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display a help screen and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Display version and copyright information and exit.</p>
<dt>-r, &#8211;recursive</p>
<dd> Descend into directories recursively.</p>
<dt>-E, &#8211;extended-regexp</p>
<dd> PATTERN is an extended regular expression. This is default.</p>
<dt>-G, &#8211;basic-regexp</p>
<dd> PATTERN is a basic regular expression.</p>
<dt>-P, &#8211;perl-regexp</p>
<dd> PATTERN is a Perl regular expression. Works only if enabled at compile time.</p>
<dt>-e, &#8211;regexp=PATTERN</p>
<dd> Use PATTERN as a regular expression.</p>
<dt>-i, &#8211;ignore-case</p>
<dd> Ignore case distinctions.</p>
<dt>-v, &#8211;invert-match</p>
<dd> Select messages which don&#8217;t match PATTERN.</p>
<dt>-H, &#8211;headers</p>
<dd> Match PATTERN against message headers.</p>
<dt>-B, &#8211;body</p>
<dd> Match PATTERN against message body.</p>
<dt>-l, &#8211;file-lock=METHOD</p>
<dd> Select file locking METHOD. METHOD is `fcntl&#8217;, `flock&#8217;, or `none&#8217;.</p>
<dt>-nl, &#8211;no-file-lock</p>
<dd> Do not lock files. This option is meaningful only if a mbox folder (see below) is scanned.</p>
<dt>-c, &#8211;count</p>
<dd> Suppress normal output and print a count of matching messages.</p>
<dt>-o, &#8211;output=FOLDER</p>
<dd> Suppress normal output and write messages to destination folder FOLDER instead.</p>
<dt>-p, &#8211;pipe=COMMAND</p>
<dd> Pipe each found message to COMMAND</p>
<dt>-d, &#8211;delete</p>
<dd> Suppress normal output and delete selected messages instead. Use with caution.</p>
<dt>-nd, &#8211;no-duplicates</p>
<dd> Ignore duplicate messages.</p>
<dt>-m, &#8211;mailbox-format=TYPE</p>
<dd> Select input and output mailbox TYPE. TYPE can be either `mbox&#8217; (default), `zmbox&#8217; (meaning `gzip compressed mbox&#8217;), `bz2mbox&#8217; (meaning `bzip2 compressed mbox&#8217;), `mh&#8217;, `nnml&#8217;, `nnmh&#8217; or `maildir&#8217;.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>*</p>
<dd> Search $MAIL for messages from Dirty Harry:</dl>
<p> mboxgrep &#8216;^From:.*callahan [at] homicide\.SFPD\.gov&#8217; $MAIL</p>
<dl>
<dt>*</p>
<dd> Display all messages contained in folder ~/Mail/incoming, except those that appear to originate from AOL:</dl>
<p> mboxgrep -v &#8216;Received:.*aol\.com&#8217; ~/Mail/incoming</p>
<h2>BUGS</h2>
<p> Report them to address below.</p>
<h2>NOTICE</h2>
<p> Mboxgrep was alomost completely rewritten since version 0.5.3. Additionally, there was no stable 0.6.x branch between 0.5.3 and 0.7.0.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/7-regex/">regex</a>(7), <a href="/docs/linux/man/1-perlre/">perlre</a>(1), <a href="/docs/linux/man/5-mbox/">mbox</a>(5), RFC 2822</p>
<h2>DEDICATION</h2>
<p> Mboxgrep is dedicated in loving memory of Vicky, my cat who died of tumor on Sep 12, 2002. </p>
<p> You haven&#8217;t been long with us, but you gave us a lot of joy and all your big heart that stopped ticking too early. I will never forget you. Sleep well, little friend.</p>
<h2>URL</h2>
<p> <a rel="nofollow" href="http://www.mboxgrep.org/">http://www.mboxgrep.org/</a></p>
<h2>AUTHOR</h2>
<p> Daniel Spiljar &lt;dspiljar [at] world.std.com&gt; </p>
<h2>Index</h2>
