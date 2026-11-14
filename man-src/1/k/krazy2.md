---
title: "krazy2(1)"
name: "krazy2"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krazy2/"
description: "krazy2 – Sanity checks KDE source code."
---

<h2 class="name">NAME</h2>
<p> krazy2 &#8211; Sanity checks KDE source code. </p>
<h2>SYNOPSIS</h2>
<p> krazy2 [<font SIZE="-1">OPTIONS</font>] [<font SIZE="-1">FILES</font>]</p>
<h2>DESCRIPTION</h2>
<p> krazy2 scans <font SIZE="-1">KDE</font> source code looking for issues that should be fixed for reasons of policy, good coding practice, optimization, or any other good reason. In typical use, krazy2 simply counts up the issues and provides the line numbers where those issues occurred in each file processed. With the verbose option, the offending content will be printed as well. </p>
<p> krazy2 uses &#8220;checker programs&#8221; which are small plugin programs to do the real work of the scanning. It is easy to write your own plugins (see <font SIZE="-1"><code>PLUGINS</code></font>) and tell krazy2 how to use them (see <font SIZE="-1"><code>ENVIRONMENT</code></font>). </p>
<p> A list of <font SIZE="-1">FILES</font> to process is either specified on the command line or read from standard input if the first file name is &#8220;-&#8221;, in which case 1 file per line is expected. Blank lines and lines starting with a &#8216;#&#8217; are ignored when reading the file list from standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>&#8211;list</code></p>
<dd> Print a list of all available checker programs and exit.</p>
<dt><code>&#8211;list-types</code></p>
<dd> Print a list of all the supported file types and exit.</p>
<dt><code>&#8211;list-sets</code></p>
<dd> Print a list of all the checker sets and exit.</p>
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
<dt><code>&#8211;explain</code></p>
<dd> For each checker program, if any issues are found, print an explanation of the problem along with solving instructions. May be used in conjunction with the <code>&#8211;list</code> option to provide a more detailed description of the checker programs.</p>
<dt><code>&#8211;ignorerc</code></p>
<dd> Ignore .krazy files.</p>
<dt><code>&#8211;config</code> &lt;krazyrc&gt;</p>
<dd> Read settings from the specified krazyrc configuration file only. All other configuration files will be ignored, including those found in the user&#8217;s home directory or in the current working directory.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> With this option the checker programs aren&#8217;t run; instead, the command line for each check that would be run is printed.</p>
<dt><code>&#8211;check</code> &lt;prog[,prog1,prog2,&#8230;,progN]&gt;</p>
<dd> Run the specified checker program(s) only. You may not combine this option with <code>&#8211;check-sets</code>. </p>
<p> Use the <code>&#8211;list</code> option to show the list of available checkers.</p>
<dt><code>&#8211;check-sets</code> &lt;set[,set1,set2,&#8230;,setN]&gt;</p>
<dd> Run the checker programs belonging to the specified set(s) only. You may not combine this option with <code>&#8211;check</code>. </p>
<p> Use the <code>&#8211;list-sets</code> option to see the list of available check sets and programs.</p>
<dt><code>&#8211;exclude</code> &lt;prog[,prog1,prog2,&#8230;,progN]&gt;</p>
<dd> Do <font SIZE="-1"><code>NOT</code></font> run the specified checker program(s). </p>
<p> Use the <code>&#8211;list</code> option to show the list of available checkers.</p>
<dt><code>&#8211;extra</code> &lt;prog[,prog1,prog2,&#8230;,progN]&gt;</p>
<dd> Add the specified &#8220;extra&#8221; program(s) to the list of checkers to run. </p>
<p> Use the <code>&#8211;list</code> option to show the list of available &#8220;extra&#8221; checkers; they will be marked with the tag [<font SIZE="-1">EXTRA</font>] by the checker description line.</p>
<dt><code>&#8211;types</code> &lt;type[,type1,type2,&#8230;,typeN]&gt;</p>
<dd> Check the specified file type(s) only.</p>
<dt><code>&#8211;exclude-types</code> &lt;type[,type1,type2,&#8230;,typeN]&gt;</p>
<dd> Do <font SIZE="-1">NOT</font> check the specified file type(s).</p>
<dt><code>&#8211;export</code> &lt;text|textlist|textedit|xml&gt;</p>
<dd> Output in one of the following formats:<br />
&nbsp;<wbr>&nbsp;<wbr>text&nbsp;<wbr>(default)<br />
&nbsp;<wbr>&nbsp;<wbr>textlist -&gt;&nbsp;<wbr>plain old text, 1 offending file-per-line<br />
&nbsp;<wbr>&nbsp;<wbr>textedit -&gt;&nbsp;<wbr>text formatted for IDEs, 1 issue-per-line<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the format is:&nbsp;<wbr>&nbsp;<wbr>file:line-number:issue<br />
&nbsp;<wbr>&nbsp;<wbr>xml -&gt;&nbsp;<wbr><font SIZE="-1">XML</font>&nbsp;<wbr>formatted</p>
<dt><code>&#8211;title</code></p>
<dd> Give the output report a project title.</p>
<dt><code>&#8211;cms</code></p>
<dd> An acronym for &#8220;component/module/subdir&#8221;. Used to write the breadcrumbs line in the xml export. Must be a slash-delimited triple containing the component, module, and subdir which is being scanned.</p>
<dt><code>&#8211;rev</code></p>
<dd> Subversion revision number to be printed on the output report, if provided.</p>
<dt><code>&#8211;brief</code></p>
<dd> Only print the output for checkers that have at least 1 issue.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress all output messages.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print the offending content for each file processed</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Print a list of all available checker programs along with a short description:</p>
<dd>
<pre><code>
 % krazy2 --list
 Available KDE source code sanitizer checks:
 For c++ file types ==
    captruefalse: Check for FALSE macro
          captrue: Check for TRUE macro
        copyright: Check for an acceptable copyright
 doublequote_char: Check for adding single char string to a QString
          license: Check for an acceptable license
    nullstrassign: Check for assignments to QString::null
   nullstrcompare: Check for compares to QString::null
             qmax: Check for QMAX macros
             qmin: Check for QMIN macros
</code></pre>
<p> For desktop file types ==<br />
contractions: Check for contractions in strings<br />
endswithnewline: Check that file ends with a newline </p>
<p> For designer file types ==<br />
endswithnewline: Check that file ends with a newline<br />
i18ncheckarg: Check validity of i18n calls<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>spelling: Check for spelling errors</p>
<dt>Run all checker programs on a file:</p>
<dd>
 % krazy2 fred.cc<br />
 =&gt;c++/captruefalse test in-progress.done<br />
 =&gt;c++/captrue test in-progress.done<br />
 =&gt;c++/copyright test in-progress.done<br />
 =&gt;c++/doublequote_chars test in-progress.done<br />
 =&gt;c++/license test in-progress.done<br />
 =&gt;c++/nullstrassign test in-progress.done<br />
 =&gt;c++/nullstrcompare test in-progress.done<br />
 =&gt;c++/qmax test in-progress.done<br />
 =&gt;c++/qmin test in-progress.done<br />
 No Issues Found!<br />
 1. Check for FALSE macro&#8230; okay!<br />
 2. Check for TRUE macro&#8230; okay!<br />
 3. Check for an acceptable copyright&#8230; okay!<br />
 4. Check for adding single char string to a QString&#8230; okay!<br />
 5. Check for an acceptable license&#8230; okay!<br />
 6. Check for assignments to QString::null&#8230; okay!<br />
 7. Check for compares to QString::null&#8230; okay!<br />
 8. Check for QMAX macros&#8230; okay!<br />
 9. Check for QMIN macros&#8230; okay!</p>
<dt>Run all checker programs <code>except</code> <i>license</i> and <i>copyright</i> the .cpp files in the current working directory:</p>
<dd>
<pre>
 % krazy2 --exclude license,copyright *.cpp
</pre>
<dt>Run the captruefalse checker programs on the *.cpp, *.cc, and *.h found in the current working directory tree, printing explanations if any issues are encountered:</p>
<dd>
 % find . -name &#8220;*.cpp&#8221; -o -name &#8220;*.cc&#8221; -o -name &#8220;*.h&#8221; | \<br />
 xargs krazy2 &#8211;check captruefalse &#8211;explain<br />
 =&gt;c++/captruefalse test in-progress&#8230;&#8230;..done<br />
 Total Issues = 10<br />
 1. Check for FALSE macro&#8230; OOPS! 232 issues found!<br />
        ./fred.h: line#176 (1)<br />
        ./fredmsg.h: line#41,54 (2)<br />
        ./fred.cpp.cpp: line#436,530,702,724,1030,1506,1525 (7)<br />
        The FALSE macro is obsolete and should be replaced by the<br />
        false (all lower case) macro.</p>
<dt>Run all the checker programs on desktop files only:</p>
<dd>
<pre>
 % krazy2 --types=desktop *
</pre>
</dl>
<h2>DIRECTIVES</h2>
<p> The Krazy plugins support the following list of in-code directives:</p>
<dl>
<dt>//krazy:skip</p>
<dd>
<pre>
 no krazy2 tests will run on this file.
</pre>
<dt>//krazy:excludeall=&lt;name1[,name2,&#8230;,nameN]&gt;</p>
<dd>
<pre>
 the krazy2 tests name1, etc will not be run on this file.
</pre>
<dt>//krazy:exclude=&lt;name1[,name2,&#8230;,nameN]&gt;</p>
<dd>
<pre>
 the krazy2 tests name1, etc. will not be run on the line where
 this directive is found.
</pre>
</dl>
<p> Note that these directives must be C<font SIZE="-2">++</font> style comments that can be put anywhere in the file desired (except embedded within C-style comments).</p>
<h2>PLUGINS</h2>
<p> Write your own plugin:</p>
<dl>
<dt> Copy <font SIZE="-1">TEMPLATE</font>.pl to your new file.</p>
<dd>
<dt> Make the new file executable chmod +x file.</p>
<dd>
<dt> Move the new file into the installed plugins directory, or create your own krazy-plugins directory and add it to the $KRAZY_PLUGIN_PATH environment (see <font SIZE="-1"><code>ENVIRONMENT</code></font><code>).</p>
<dd></dl>
<p> You may write the plugin in the language of your choice, but it must follow these rules:</p>
<dl>
<dt>1. must accept the following optional command line args:</p>
<dd> </code> </p>
<pre><code>
--help : print one - line help message and exit-- version : print one - line version information and exit-- priority : report issues of the specified priority only-- strict : report issues with the specified strictness level only-- explain : print an explanation with solving instructions-- installed file is to be installed-- quiet : suppress all output messages-- verbose : print the offending content
</code></pre>
<dt>2. must require one command line argument which is the file to test.</p>
<dd>
<dt>3. must exit with status 0, and print okay if the file passes the test.</p>
<dd>
<dt>4. must exit with non-zero status if issues are encountered.</p>
<dd>
<dt>5. if issues are encountered, the final line printed should be ISSUES=N, where N is the total number of issues found. Krazy2 assumes this is the last line of output, even if the plugin prints more information after the ISSUES=N line.</p>
<dd>
<dt>6. must print a string to standard output showing line number(s) that fail the test.</p>
<dd>
<dt>7. the plugin should be a quick test of a source code file.</p>
<dd>
<dt>8. the &#8211;explain option must print an explanation of why the offending code is a problem, along with instructions on how to fix the code.</p>
<dd>
<dt>9. <i>finally, and importantly, the plugin must eliminate false positives as much as possible.</i></p>
<dd></dl>
<h2>ENVIRONMENT</h2>
<p> <font SIZE="-1"><code>KRAZY_PLUGIN_PATH</code></font> &#8211; this is a colon-separated list of paths which is searched when locating plugins. By default, plugins are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-plugins:krazy-plugins</i>. </p>
<p> <font SIZE="-1"><code>KRAZY_EXTRA_PATH</code></font> &#8211; this is a colon-separated list of paths which is searched when locating &#8220;extra&#8221; plugins. By default, the &#8220;extras&#8221; are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-extras:krazy-extras</i>. </p>
<p> <font SIZE="-1"><code>KRAZY_SET_PATH</code></font> &#8211; this is a colon-separated list of paths which is searched when locating checker sets. By default, the sets are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-sets:krazy-sets</i>. </p>
<p> where <tt>$TOP</tt> is the top-level installation directory (eg. <i>/usr/local</i>, <i>/usr/local/Krazy2</i>) </p>
<p> <font SIZE="-1"><code>KRAZY_STYLE_CPPSTYLE</code></font> &#8211; tells the &#8220;style&#8221; checker to follow the guidelines of the specified C<font SIZE="-2">++</font>-style. <i>Note</i>: Krazy uses a heuristic to decide what type of C<font SIZE="-2">++</font>-style to check against. That heuristic isn&#8217;t very smart; so use this setting to enforce the C<font SIZE="-2">++</font>-style. </p>
<p> C<font SIZE="-2">++</font>-style must be one of the following: </p>
<dl>
<dt>
<dd> &#8220;kde&#8221; (default), see <a rel="nofollow" href="http://techbase.kde.org/Policies/Kdelibs_Coding_Style">http://techbase.kde.org/Policies/Kdelibs_Coding_Style</a> </p>
<p> &#8220;pim&#8221; kdepim style, see <a rel="nofollow" href="http://pim.kde.org/development/coding-korganizer.php">http://pim.kde.org/development/coding-korganizer.php</a></dl>
<p> <font SIZE="-1"><code>KRAZY_STYLE_OFFSET</code></font> &#8211; tells the &#8220;style&#8221; checker to check for a basic indentation level, usually a small integer like 2 or 4. This value overrides the offset provided as part of the C<font SIZE="-2">++</font>-style (see <font SIZE="-1"><code>KRAZY_STYLE_CPPSTYLE</code></font>). </p>
<p> <font SIZE="-1"><code>KRAZY_STYLE_LINEMAX</code></font> &#8211; tells the &#8220;style&#8221; checker to check for lines longer than this number of characters. The default is 100 characters.</p>
<h2>EXIT STATUS</h2>
<p> In normal operation, krazy2 exits with a status equal to the total number of issues encountered during processing. </p>
<p> If a command line option was incorrectly provided, krazy2 exits with status=1. </p>
<p> If krazy2 was envoked with the <code>&#8211;help</code>, <code>&#8211;version</code>, <code>&#8211;list</code>, <code>&#8211;list-types</code>, or <code>&#8211;list-sets</code> options it will exit with status=0.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2005-2010 by Allen Winter &lt;winter [at] kde.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA</font> 02110-1301, <font SIZE="-1">USA</font>.</p>
<h2>FILES</h2>
<p> <i>.krazy</i> (see <i><a href="/docs/linux/man/5-krazyrc/">krazyrc</a></i>(5)) </p>
<p> krazy2 first parses a <i>.krazy</i> file found in the user&#8217;s home directory, if such a file exists. </p>
<p> Next, krazy2 searches up the current working directory tree for a project specific <i>.krazy</i> file. If one is found, its settings are merged with (or override) those already found from <i></i>$HOME<i>/.krazy</i>. </p>
<p> [For example, if the current working dir is <i>/my/kde/trunk/KDE/kdepimlibs/kcal/versit</i>, then krazy2 will look for <i>/my/kde/trunk/KDE/kdepimlibs/kcal/.krazy</i>, since kcal is the project within the kdepimlibs module.] </p>
<p> If krazy2 determines that the current working directory is not located within the <font SIZE="-1">KDE</font> directory structure, then it simply reads the settings from the <i>.krazy</i> file found in the current working directory, if such a file exists. </p>
<p> If krazy2 determines that the current working directory is located within the <font SIZE="-1">KDE</font> directory structure but above a project subdir (eg. <i>trunk/KDE/kdepim</i>), then it assumes no project specific <i>/.krazy</i> file.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-krazyrc/">krazyrc</a></i>(5), <i><a href="/docs/linux/man/1-krazy2all/">krazy2all</a></i>(1), <i><a href="/docs/linux/man/1-krazy2xml/">krazy2xml</a></i>(1) </p>
<p> Ben Meyer&#8217;s kdetestscripts &#8211; Automated scripts are to catch problems in <font SIZE="-1">KDE</font>, &lt;<a rel="nofollow" href="http://websvn.kde.org/trunk/playground/base/kdetestscripts">http://websvn.kde.org/trunk/playground/base/kdetestscripts</a>&gt;. </p>
<p> flawfinder &#8211; Examines source code looking for security weaknesses, &lt;<a rel="nofollow" href="http://www.dwheeler.com/flawfinder">http://www.dwheeler.com/flawfinder</a>&gt;.</p>
<h2>AUTHORS</h2>
<p> Allen Winter, &lt;winter [at] kde.org&gt; </p>
<h2>Index</h2>
