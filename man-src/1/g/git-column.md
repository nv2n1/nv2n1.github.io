---
title: "git-column(1)"
name: "git-column"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-column/"
description: "git-column – Display data in columns"
---

<h2 class="name">NAME</h2>
<p> git-column &#8211; Display data in columns </p>
<h2>SYNOPSIS</h2>
<pre><code>
git column[--command = &lt;name&gt;][--[raw - ] mode = &lt;mode&gt;][--width = &lt;width&gt;]
          [--indent = &lt;string&gt;][--nl = &lt;string&gt;][--padding = &lt;n&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command formats the lines of its standard input into a table with multiple columns. Each input line occupies one cell of the table. It is used internally by other git commands to format output into columns.</p>
<h2>OPTIONS</h2>
<p> &#8211;command=&lt;name&gt;</p>
<dl>
<dt>
<dd> Look up layout mode using configuration variable column.&lt;name&gt; and column.ui.</dl>
<p> &#8211;mode=&lt;mode&gt;</p>
<dl>
<dt>
<dd> Specify layout mode. See configuration variable column.ui for option syntax in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;raw-mode=&lt;n&gt;</p>
<dl>
<dt>
<dd> Same as &#8211;mode but take mode encoded as a number. This is mainly used by other commands that have already parsed layout mode.</dl>
<p> &#8211;width=&lt;width&gt;</p>
<dl>
<dt>
<dd> Specify the terminal width. By default <i>git column</i> will detect the terminal width, or fall back to 80 if it is unable to do so.</dl>
<p> &#8211;indent=&lt;string&gt;</p>
<dl>
<dt>
<dd> String to be printed at the beginning of each line.</dl>
<p> &#8211;nl=&lt;string&gt;</p>
<dl>
<dt>
<dd> String to be printed at the end of each line, including newline character.</dl>
<p> &#8211;padding=&lt;N&gt;</p>
<dl>
<dt>
<dd> The number of spaces between columns. One space by default.</dl>
<h2>EXAMPLES</h2>
<p> Format data by columns: </p>
<dl>
<dt>
<dd>
<pre>
$ seq 1 24 | git column --mode=column --padding=5
1      4      7      10     13     16     19     22
2      5      8      11     14     17     20     23
3      6      9      12     15     18     21     24
</pre>
</dl>
<p> Format data by rows: </p>
<dl>
<dt>
<dd>
<pre>
$ seq 1 21 | git column --mode=row --padding=5
1      2      3      4      5      6      7
8      9      10     11     12     13     14
15     16     17     18     19     20     21
</pre>
</dl>
<p> List some tags in a table with unequal column widths: </p>
<dl>
<dt>
<dd>
<pre>
$ git tag --list 'v2.4.*' --column=row,dense
v2.4.0  v2.4.0-rc0  v2.4.0-rc1  v2.4.0-rc2  v2.4.0-rc3
v2.4.1  v2.4.10     v2.4.11     v2.4.12     v2.4.2
v2.4.3  v2.4.4      v2.4.5      v2.4.6      v2.4.7
v2.4.8  v2.4.9
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
