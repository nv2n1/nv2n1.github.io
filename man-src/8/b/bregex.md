---
title: "bregex(8)"
name: "bregex"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bregex/"
description: "bregex – Bacula’s ‘regex’ engine"
---

<p>&nbsp;<wbr>bregex &#8211; Bacula&#8217;s&nbsp;<wbr>&#8216;regex&#8217;&nbsp;<wbr>engine</p>
<h2>Synopsis</h2>
<p><code>bregex</code> [<i>options</i>] <i>-f &lt;data-file&gt;</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bregex</code> command.<br />
 This program can be useful for testing regex expressions to be applied against a list of filenames. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></p>
<dd>Show version and usage of program.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd>Set debug level to <i>nn</i>.</p>
<dt><code>-dt</code></p>
<dd>Print timestamp in debug output</p>
<dt><code>-f&nbsp;<wbr>&lt;data-file&gt;</code></p>
<dd>The data-file is a filename that contains lines of data to be matched (or not) against one or more patterns. When the program is run, it will prompt you for a regular expression pattern, then apply it one line at a time against the data in the file. Each line that matches will be printed preceded by its line number. You will then be prompted again for another pattern.</p>
<dt><code>-n</code></p>
<dd>Print lines that do not match</p>
<dt><code>-l</code></p>
<dd>Suppress lines numbers.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code></p>
<h2>Author</h2>
<p>This manual page was written by Bruno Friedmann &lt;bruno [at] ioda-net.ch&gt;.</p>
