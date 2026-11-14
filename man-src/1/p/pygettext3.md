---
title: "pygettext3(1)"
name: "pygettext3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pygettext3/"
description: "pygettext – Python equivalent of"
---

<h2 class="name">NAME</h2>
<p> pygettext &#8211; Python equivalent of </p>
<p> <a href="/docs/linux/man/1-xgettext/">xgettext</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>pygettext</code> [<i>OPTIONS</i>] <i>INPUTFILE </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> pygettext is deprecated. The current version of xgettext supports many languages, including Python. </p>
<p> pygettext uses Python&#8217;s standard tokenize module to scan Python source code, generating .pot files identical to what GNU xgettext generates for C and C++ code. From there, the standard GNU tools can be used. </p>
<p> pygettext searches only for _() by default, even though GNU xgettext recognizes the following keywords: gettext, dgettext, dcgettext, and gettext_noop. See the <code>-k</code>/<code>&#8211;keyword</code> flag below for how to augment this. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;extract-all</code></p>
<dd> Extract all strings.</p>
<dt><code>-d</code>, <code>&#8211;default-domain</code>=<i>NAME</i></p>
<dd> Rename the default output file from messages.pot to name.pot.</p>
<dt><code>-E</code>, <code>&#8211;escape</code></p>
<dd> Replace non-ASCII characters with octal escape sequences.</p>
<dt><code>-D</code>, <code>&#8211;docstrings</code></p>
<dd> Extract module, class, method, and function docstrings. These do not need to be wrapped in _() markers, and in fact cannot be for Python to consider them docstrings. (See also the <code>-X</code> option).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print this help message and exit.</p>
<dt><code>-k</code>, <code>&#8211;keyword</code>=<i>WORD</i></p>
<dd> Keywords to look for in addition to the default set, which are: _</p>
<dt>
<dd> You can have multiple <code>-k</code> flags on the command line.</p>
<dt><code>-K</code>, <code>&#8211;no-default-keywords</code></p>
<dd> Disable the default set of keywords (see above). Any keywords explicitly added with the <code>-k</code>/<code>&#8211;keyword</code> option are still recognized.</p>
<dt><code>&#8211;no-location</code></p>
<dd> Do not write filename/lineno location comments.</p>
<dt><code>-n</code>, <code>&#8211;add-location</code></p>
<dd> Write filename/lineno location comments indicating where each extracted string is found in the source. These lines appear before each msgid. The style of comments is controlled by the <code>-S</code>/<code>&#8211;style</code> option. This is the default.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILENAME</i></p>
<dd> Rename the default output file from messages.pot to FILENAME. If FILENAME is `-&#8216; then the output is sent to standard out.</p>
<dt><code>-p</code>, <code>&#8211;output-dir</code>=<i>DIR</i></p>
<dd> Output files will be placed in directory DIR.</p>
<dt><code>-S</code>, <code>&#8211;style</code>=<i>STYLENAME</i></p>
<dd> Specify which style to use for location comments. Two styles are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Solaris<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># File: filename, line: line-number</p>
<dt>&bull;</p>
<dd> GNU<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>#: filename:line
</dl>
</dl>
<dt>
<dd> The style name is case insensitive. GNU style is the default.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print the names of the files being processed.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of pygettext and exit.</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>COLUMNS</i></p>
<dd> Set width of output to columns.</p>
<dt><code>-x</code>, <code>&#8211;exclude-file</code>=<i>FILENAME</i></p>
<dd> Specify a file that contains a list of strings that are not be extracted from the input files. Each string to be excluded must appear on a line by itself in the file.</p>
<dt><code>-X</code>, <code>&#8211;no-docstrings</code>=<i>FILENAME</i></p>
<dd> Specify a file that contains a list of files (one per line) that should not have their docstrings extracted. This is only useful in conjunction with the <code>-D</code> option above.</dl>
<p> If `INPUTFILE&#8217; is -, standard input is read.</p>
<h2>BUGS</h2>
<p> pygettext attempts to be option and feature compatible with GNU xgettext where ever possible. However some options are still missing or are not fully implemented. Also, xgettext&#8217;s use of command line switches with option arguments is broken, and in these cases, pygettext just defines additional switches.</p>
<h2>AUTHOR</h2>
<p> pygettext is written by Barry Warsaw &lt;barry [at] zope.com&gt;. </p>
<p> Joonas Paalasmaa &lt;joonas.paalasmaa [at] iki.fi&gt; put this manual page together based on &quot;pygettext &#8211;help&quot;. </p>
<h2>Index</h2>
