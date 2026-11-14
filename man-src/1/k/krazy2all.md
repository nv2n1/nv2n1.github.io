---
title: "krazy2all(1)"
name: "krazy2all"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krazy2all/"
description: "krazy2all – Sanity checks KDE source code."
---

<h2 class="name">NAME</h2>
<p> krazy2all &#8211; Sanity checks KDE source code. </p>
<h2>SYNOPSIS</h2>
<p> krazy2all [options]</p>
<h2>DESCRIPTION</h2>
<p> krazy2all finds all supported files within the current directory tree and runs the krazy2 checker on all of them, producing 1 concise report in the specified export format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>&#8211;list</code></p>
<dd> Print a list of all available checker programs and exit.</p>
<dt><code>&#8211;list-types</code></p>
<dd> Print a list of the support file types and exit.</p>
<dt><code>&#8211;ignorerc</code></p>
<dd> Ignore .krazy files.</p>
<dt><code>&#8211;config</code> &lt;krazyrc&gt;</p>
<dd> Read settings from the specified krazyrc configuration file only. All other configuration files will be ignored, including those found in the user&#8217;s home directory or in the current working directory.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> With this option the checker programs aren&#8217;t run; instead, the command line for each check that would be run is printed.</p>
<dt><code>&#8211;priority</code> &lt;low|normal|high|important|all&gt;</p>
<dd> Tell each checker program to report issues with the specified priority only. This option is useful to help put issues into &#8220;fix-first&#8221; order. </p>
<p> Supported priorites are:<br />
&nbsp;<wbr>&nbsp;<wbr>low -&gt;&nbsp;<wbr>print low priority issues only<br />
&nbsp;<wbr>&nbsp;<wbr>normal -&gt;&nbsp;<wbr>print normal priority issues only<br />
&nbsp;<wbr>&nbsp;<wbr>high -&gt;&nbsp;<wbr>print high priority issues only<br />
&nbsp;<wbr>&nbsp;<wbr>important -&gt;&nbsp;<wbr>print issues with normal or high priority<br />
&nbsp;<wbr>&nbsp;<wbr>all -&gt;&nbsp;<wbr>print all issues&nbsp;<wbr>(default)</p>
<dt><code>&#8211;strict</code> &lt;normal|super|all&gt;</p>
<dd> Tell each checker program to report issues match the strictness level only. Use this option to help filter out issues of less importance. </p>
<p> Support strictness levels are:<br />
&nbsp;<wbr>&nbsp;<wbr>normal -&gt;&nbsp;<wbr>print non-super strict issues only<br />
&nbsp;<wbr>&nbsp;<wbr>super -&gt;&nbsp;<wbr>print super strict issues only<br />
&nbsp;<wbr>&nbsp;<wbr>all -&gt;&nbsp;<wbr>print all issues&nbsp;<wbr>(default)</p>
<dt><code>&#8211;check</code> &lt;prog[,prog1,prog2,&#8230;,progN]&gt;</p>
<dd> Run the specified checker program(s) only. You may not combine this option with <code>&#8211;check-sets</code>. </p>
<p> Use the <code>&#8211;list</code> option to show the list of available checkers.</p>
<dt><code>&#8211;check-sets</code> &lt;set[,set1,set2,&#8230;,setN]&gt;</p>
<dd> Run the checker programs belonging to the specified set(s) only. You may not combine this option with <code>&#8211;check</code>. </p>
<p> Use the <code>&#8211;list-sets</code> option to see the list of available check sets and programs.</p>
<dt><code>&#8211;exclude</code> &lt;prog[,prog1,prog2,&#8230;,progN]&gt;</p>
<dd> Do <font SIZE="-1"><code>NOT</code></font> run the specified checker program(s).</p>
<dt><code>&#8211;extra</code> &lt;prog[,prog1,prog2,&#8230;,progN]&gt;</p>
<dd> Add the specified &#8220;extra&#8221; program(s) to the list of checkers to run. Use the &#8211;list option to show the list of available &#8220;extra&#8221; checkers; they will be marked with the tag [<font SIZE="-1">EXTRA</font>] by the checker description line.</p>
<dt><code>&#8211;types</code> &lt;type[,type1,type2,&#8230;,typeN]&gt;</p>
<dd> Check the specified file type(s) only.</p>
<dt><code>&#8211;exclude-types</code> &lt;type[,type1,type2,&#8230;,typeN]&gt;</p>
<dd> Do <font SIZE="-1">NOT</font> check the specified file type(s).</p>
<dt><code>&#8211;export</code> &lt;text|textlist|textedit|xml&gt;</p>
<dd> Output in one of the following formats:<br />
&nbsp;<wbr>&nbsp;<wbr>text&nbsp;<wbr>(default)<br />
&nbsp;<wbr>&nbsp;<wbr>textlist -&gt;&nbsp;<wbr>plain old text, 1 offending file-per-line<br />
&nbsp;<wbr>&nbsp;<wbr>textedit -&gt;&nbsp;<wbr>text formatted for IDEs, 1 issue-per-line&nbsp;<wbr>(file:line:issue)<br />
&nbsp;<wbr>&nbsp;<wbr>xml -&gt;&nbsp;<wbr><font SIZE="-1">XML</font>&nbsp;<wbr>formatted</p>
<dt><code>&#8211;title</code></p>
<dd> Give the output report a project title.</p>
<dt><code>&#8211;cms</code></p>
<dd> An acronym for &#8220;component/module/subdir&#8221;. Used to write the breadcrumbs line in the <font SIZE="-1">XML</font> output. Must be a slash-delimited triple containing the component, module, and subdir which is being scanned.</p>
<dt><code>&#8211;brief</code></p>
<dd> Only print the output for checkers that have at least 1 issue.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress all output messages.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print the offending content for each file processed</dl>
<h2>ENVIRONMENT</h2>
<p> <font SIZE="-1">KRAZY_PLUGIN_PATH</font> &#8211; this is a colon-separated list of paths which is searched when locating plugins. By default, plugins are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-plugins:krazy-plugins</i>. </p>
<p> <font SIZE="-1">KRAZY_EXTRA_PATH</font> &#8211; this is a colon-separated list of paths which is searched when locating &#8220;extra&#8221; plugins. By default, the &#8220;extras&#8221; are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-extras:krazy-extras</i>. </p>
<p> <font SIZE="-1">KRAZY_SET_PATH</font> &#8211; this is a colon-separated list of paths which is searched when locating checker sets. By default, the sets are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-sets:krazy-sets</i>. </p>
<p> where <tt>$TOP</tt> is the top-level installation directory (eg. <i>/usr/local</i>, <i>/usr/local/Krazy2</i>)</p>
<h2>EXIT STATUS</h2>
<p> In normal operation, krazy2all exits with a status 0. </p>
<p> If a command line option was incorrectly provided, krazy2all exits with status=1. </p>
<p> If krazy2all was envoked with the <code>&#8211;help</code>, <code>&#8211;version</code> <code>&#8211;list</code> or <code>&#8211;list-types</code> options it will exit with status=0.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2005-2010 by Allen Winter &lt;winter [at] kde.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA</font> 02110-1301, <font SIZE="-1">USA</font>.</p>
<h2>FILES</h2>
<p> <i>.krazy</i> (see <i><a href="/docs/linux/man/5-krazyrc/">krazyrc</a></i>(5)) </p>
<p> krazy2all looks up the current working directory tree for a <i>.krazy</i> file in the project subdirectory. Only <i>.krazy</i> files found at the project subdirectory level are read. </p>
<p> For example, if the current working dir is <i>/my/kde/trunk/KDE/kdepimlibs/kcal/versit</i>, then krazy2all will look for <i>/my/kde/trunk/KDE/kdepimlibs/kcal/.krazy</i>, since kcal is the project within the kdepimlibs module. </p>
<p> If the current working dir is not within a <font SIZE="-1">KDE</font> module, or if the current working dir is above a project subdir, then a <i>.krazy</i> file will not be read.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-krazyrc/">krazyrc</a></i>(5), <i><a href="/docs/linux/man/1-krazy2/">krazy2</a></i>(1), <i><a href="/docs/linux/man/1-krazy2xml/">krazy2xml</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> Allen Winter, &lt;winter [at] kde.org&gt; </p>
<h2>Index</h2>
