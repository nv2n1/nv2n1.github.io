---
title: "bwild(8)"
name: "bwild"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bwild/"
description: "bwild – Bacula’s ‘wildcard’ engine"
---

<p>&nbsp;<wbr>bwild &#8211; Bacula&#8217;s&nbsp;<wbr>&#8216;wildcard&#8217;&nbsp;<wbr>engine</p>
<h2>Synopsis</h2>
<p><code>bwild</code> [<i>options</i>] <i>-f &lt;data-file&gt;</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bwild</code> command.<br />
 This is a simple program that will allow you to test wild-card expressions against a file of data. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></dt>
<dd>Show version and usage of program.</dd>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></dt>
<dd>Set debug level to <i>nn</i>.</dd>
<dt><code>-dt</code></dt>
<dd>Print timestamp in debug output</dd>
<dt><code>-f&nbsp;<wbr>&lt;data-file&gt;</code></dt>
<dd>The data-file is a filename that contains lines of data to be matched (or not) against one or more patterns. When the program is run, it will prompt you for a wild-card pattern, then apply it one line at a time against the data in the file. Each line that matches will be printed preceded by its line number. You will then be prompted again for another pattern.<br />
 Enter an empty line for a pattern to terminate the program. You can print only lines that do not match by using the -n option, and you can suppress printing of line numbers with the -l option.</dd>
<dt><code>-n</code></dt>
<dd>Print lines that do not match</dd>
<dt><code>-l</code></dt>
<dd>Suppress lines numbers.</dd>
<dt><code>-i</code></dt>
<dd>use case insensitive match.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3)</code></p>
<h2>Author</h2>
<p>This manual page was written by Bruno Friedmann &lt;bruno [at] ioda-net.ch&gt;.</p>
