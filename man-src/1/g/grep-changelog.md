---
title: "grep-changelog(1)"
name: "grep-changelog"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grep-changelog/"
description: "grep-changelog – print ChangeLog entries matching criteria"
---

<h2>NAME</h2>
<p> grep-changelog &#8211; print ChangeLog entries matching criteria</p>
<h2>SYNOPSIS</h2>
<p> <code>grep-changelog</code> [<i>options</i>] [<i>CHANGELOG</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>grep-changelog</code> searches the named <i>CHANGELOG</i>s (by default files matching the regular expressions <code>ChangeLog</code> and <code>ChangeLog\.[0-9]+</code>) for entries matching the specified criteria. At least one option or file must be specified. This program is distributed with <code>GNU Emacs</code>. </p>
<h2>OPTIONS</h2>
<p> The program accepts unambiguous abbreviations for option names.</p>
<dl>
<dt><code>&#8211;author=AUTHOR</code></p>
<dd> Print entries whose author matches regular expression <i>AUTHOR</i>.</p>
<dt><code>&#8211;text=TEXT</code></p>
<dd> Print entries whose text matches regular expression <i>TEXT</i>.</p>
<dt><code>&#8211;exclude=TEXT</code></p>
<dd> Exclude entries matching regular expression <i>TEXT</i>.</p>
<dt><code>&#8211;from-date=YYYY-MM-DD</code></p>
<dd> Only consider entries made on or after the given date. ChangeLog date entries not in the &#8220;YYYY-MM-DD&#8221; format are never matched.</p>
<dt><code>&#8211;to-date=YYYY-MM-DD</code></p>
<dd> Only consider entries made on or before the given date.</p>
<dt><code>&#8211;rcs-log</code></p>
<dd> Print output in a format suitable for RCS log entries. This format removes author lines, leading spaces, and file names.</p>
<dt><code>&#8211;with-date</code></p>
<dd> In RCS log format, print short dates.</p>
<dt><code>&#8211;reverse</code></p>
<dd> Show matches in reverse order.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>&#8211;help</code></p>
<dd> Display basic usage information.</dl>
<h2>COPYING</h2>
<p> Copyright (C) 2008-2013 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation. </p>
<h2>Index</h2>
