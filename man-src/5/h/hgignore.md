---
title: "hgignore(5)"
name: "hgignore"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hgignore/"
description: "hgignore – syntax for Mercurial ignore files"
---

<p>hgignore &#8211; syntax for Mercurial ignore files</p>
<h2>Synopsis</h2>
<p>The Mercurial system uses a file called <code>.hgignore</code> in the root directory of a repository to control its behavior when it searches for files that it is not currently tracking.</p>
<h2>Description</h2>
<p>The working directory of a Mercurial repository will often contain files that should not be tracked by Mercurial. These include backup files created by editors and build products created by compilers. These files can be ignored by listing them in a <code>.hgignore</code> file in the root of the working directory. The <code>.hgignore</code> file must be created manually. It is typically put under version control, so that the settings will propagate to other repositories with push and pull. </p>
<p> An untracked file is ignored if its path relative to the repository root directory, or any prefix path of that path, is matched against any pattern in <code>.hgignore</code>. </p>
<p> For example, say we have an untracked file, <code>file.c</code>, at <code>a/b/file.c</code> inside our repository. Mercurial will ignore <code>file.c</code> if any pattern in <code>.hgignore</code> matches <code>a/b/file.c</code>, <code>a/b</code> or <code>a</code>. </p>
<p> In addition, a Mercurial configuration file can reference a set of per-user or global ignore files. See the <code>ignore</code> configuration key on the <code>[ui]</code> section of <code>hg help config</code>: for details of how to configure these files. </p>
<p> To control Mercurial&#8217;s handling of files that it manages, many commands support the <code>-I</code> and <code>-X</code> options; see <code>hg help &lt;command&gt;</code>: and <code>hg help patterns</code>: for details. </p>
<p> Files that are already tracked are not affected by .hgignore, even if they appear in .hgignore. An untracked file X can be explicitly added with <code>hg add X</code>:, even if X would be excluded by a pattern in .hgignore.</p>
<h2>Syntax</h2>
<p>An ignore file is a plain text file consisting of a list of patterns, with one pattern per line. Empty lines are skipped. The <code>#</code> character is treated as a comment character, and the <code>\</code> character is treated as an escape character. </p>
<p> Mercurial supports several pattern syntaxes. The default syntax used is Python/Perl-style regular expressions. </p>
<p> To change the syntax used, use a line of the following form: </p>
<pre>syntax: NAME</pre>
<p>where <code>NAME</code> is one of the following:</p>
<dl>
<dt><code>regexp</code></p>
<dd>Regular expression, Python/Perl syntax.</p>
<dt><code>glob</code></p>
<dd>Shell-style glob. </p>
<p> The chosen syntax stays in effect when parsing all patterns that follow, until another syntax is selected. </p>
<p> Neither glob nor regexp patterns are rooted. A glob-syntax pattern of the form <code>*.c</code> will match a file ending in <code>.c</code> in any directory, and a regexp pattern of the form <code>\.c$</code> will do the same. To root a regexp pattern, start it with <code>^</code>.</p>
<dt>Note</p>
<dd>Patterns specified in other than <code>.hgignore</code> are always rooted. Please see <code>hg help patterns</code>: for details.</dl>
<h2>Example</h2>
<p>Here is an example ignore file. </p>
<pre># use glob syntax.
syntax: glob
*.elc
*.pyc
*~
# switch to regexp syntax.
syntax: regexp
^\.pc/</pre>
<h2>Author</h2>
<p>Vadim Gelfer &lt;vadim.gelfer [at] gmail.com:&gt; </p>
<p> Mercurial was written by Matt Mackall &lt;mpm [at] selenic.com:&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-hg/">hg</a></code>(1):, <code><a href="/docs/linux/man/5-hgrc/">hgrc</a></code>(5):</p>
<h2>Copying</h2>
<p>This manual page is copyright 2006 Vadim Gelfer. Mercurial is copyright 2005-2012 Matt Mackall. Free use of this software is granted under the terms of the GNU General Public License version 2 or any later version.</p>
<h2>Author</h2>
<p>Vadim Gelfer &lt;vadim.gelfer [at] gmail.com&gt; </p>
<p> Organization: Mercurial</p>
