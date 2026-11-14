---
title: "pycodestyle(1)"
name: "pycodestyle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pycodestyle/"
description: "pycodestyle – pycodestyle documentation"
---

<h2>NAME</h2>
<p> pycodestyle &#8211; pycodestyle documentation </p>
<p> <i>Python style guide checker</i> </p>
<p> pycodestyle (formerly pep8) is a tool to check your Python code against some of the style conventions in <i>PEP 8</i>. </p>
<p> Contents:</p>
<h2>INTRODUCTION</h2>
<p> pycodestyle is a tool to check your Python code against some of the style conventions in <i>PEP 8</i>.</p>
<dl>
<dt>&bull;</p>
<dd> <i>Features</i></p>
<dt>&bull;</p>
<dd> <i>Disclaimer</i></p>
<dt>&bull;</p>
<dd> <i>Installation</i></p>
<dt>&bull;</p>
<dd> <i>Example usage and output</i></p>
<dt>&bull;</p>
<dd> <i>Configuration</i></p>
<dt>&bull;</p>
<dd> <i>Error codes</i></p>
<dt>&bull;</p>
<dd> <i>Related tools</i></dl>
<h3>Features</h3>
<dl>
<dt>&bull;</p>
<dd> Plugin architecture: Adding new checks is easy.</p>
<dt>&bull;</p>
<dd> Parseable output: Jump to error location in your editor.</p>
<dt>&bull;</p>
<dd> Small: Just one Python file, requires only stdlib. You can use just the <code>pycodestyle.py</code> file for this purpose.</p>
<dt>&bull;</p>
<dd> Comes with a comprehensive test suite.</dl>
<h3>Disclaimer</h3>
<p> This utility does not enforce every single rule of PEP 8. It helps to verify that some coding conventions are applied but it does not intend to be exhaustive. Some rules cannot be expressed with a simple algorithm, and other rules are only guidelines which you could circumvent when you need to. </p>
<p> Always remember this statement from <i>PEP 8</i>: <i>A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is most important.</i> </p>
<p> Among other things, these features are currently not in the scope of the <code>pycodestyle</code> library:</p>
<dl>
<dt>&bull;</p>
<dd> <code>naming conventions</code>: this kind of feature is supported through plugins. Install <i>flake8</i> and the <i>pep8-naming extension</i> to use this feature.</p>
<dt>&bull;</p>
<dd> <code>docstring conventions</code>: they are not in the scope of this library; see the <i>pydocstyle project</i>.</p>
<dt>&bull;</p>
<dd> <code>automatic fixing</code>: see the section <i>PEP8 Fixers</i> in the <i>related tools</i> page.</dl>
<h3>Installation</h3>
<p> You can install, upgrade, uninstall <code>pycodestyle.py</code> with these commands: </p>
<pre>
$ pip install pycodestyle
$ pip install --upgrade pycodestyle
$ pip uninstall pycodestyle
</pre>
<h3>Example usage and output</h3>
<pre>
$ pycodestyle --first optparse.py
optparse.py:69:11: E401 multiple imports on one line
optparse.py:77:1: E302 expected 2 blank lines, found 1
optparse.py:88:5: E301 expected 1 blank line, found 0
optparse.py:222:34: W602 deprecated form of raising exception
optparse.py:347:31: E211 whitespace before '('
optparse.py:357:17: E201 whitespace after '{'
optparse.py:472:29: E221 multiple spaces before operator
optparse.py:544:21: W601 .has_key() is deprecated, use 'in'
</pre>
<p> You can also make <code>pycodestyle.py</code> show the source code for each error, and even the relevant text from PEP 8: </p>
<pre>
$ pycodestyle --show-source --show-pep8 testsuite/E40.py
testsuite/E40.py:2:10: E401 multiple imports on one line
import os, sys
         ^
    Imports should usually be on separate lines.
    Okay: import os
import sys
    E401: import sys, os
</pre>
<p> Or you can display how often each error was found: </p>
<pre>
$ pycodestyle --statistics -qq Python-2.5/Lib
232     E201 whitespace after '['
599     E202 whitespace before ')'
631     E203 whitespace before ','
842     E211 whitespace before '('
2531    E221 multiple spaces before operator
4473    E301 expected 1 blank line, found 0
4006    E302 expected 2 blank lines, found 1
165     E303 too many blank lines (4)
325     E401 multiple imports on one line
3615    E501 line too long (82 characters)
612     W601 .has_key() is deprecated, use 'in'
1188    W602 deprecated form of raising exception
</pre>
<p> You can also make <code>pycodestyle.py</code> show the error text in different formats by using <code>&#8211;format</code> having options default/pylint/custom: </p>
<pre><code>
$ pycodestyle testsuite / E40.py-- format = default testsuite / E40.py : 2 : 10 : E401 multiple imports on one line $ pycodestyle testsuite / E40.py-- format = pylint
                                                                                                                                                                    testsuite /
                                                                                                                                                                E40.py : 2 : [E401] multiple imports on one line
                                                                                                                                                                                 $ pycodestyle testsuite /
                                                                                                                                                                E40.py-- format = '%(path)s|%(row)d|%(col)d| %(code)s %(text)s' testsuite / E40.py | 2 | 10 | E401 multiple imports on one line
</code></pre>
<p> Variables in the <code>custom</code> format option <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Variable </td>
<td> Significance
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>path</code> </td>
<td> File name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>row</code> </td>
<td> Row number
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>col</code> </td>
<td> Column number
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>code</code> </td>
<td> Error code
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>text</code> </td>
<td> Error text
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Quick help is available on the command line: </p>
<p>$ pycodestyle -h<br />
Usage: pycodestyle [options] input &#8230;<br />
Options:<br />
  &#8211;version            show program&#8217;s version number and exit<br />
  -h, &#8211;help           show this help message and exit<br />
  -v, &#8211;verbose        print status messages, or debug with -vv<br />
  -q, &#8211;quiet          report only file names, or nothing with -qq<br />
  &#8211;first              show first occurrence of each error<br />
  &#8211;exclude=patterns   exclude files or directories which match these comma<br />
                       separated patterns (default: .svn,CVS,.bzr,.hg,.git)<br />
  &#8211;filename=patterns  when parsing directories, only check filenames matching<br />
                       these comma separated patterns (default: *.py)<br />
  &#8211;select=errors      select errors and warnings (e.g. E,W6)<br />
  &#8211;ignore=errors      skip errors and warnings (e.g. E4,W)<br />
  &#8211;show-source        show source code for each error<br />
  &#8211;show-pep8          show text of PEP 8 for each error (implies &#8211;first)<br />
  &#8211;statistics         count errors and warnings<br />
  &#8211;count              print total number of errors and warnings to standard<br />
                       error and set exit code to 1 if total is not null<br />
  &#8211;max-line-length=n  set maximum allowed line length (default: 79)<br />
  &#8211;hang-closing       hang closing bracket instead of matching indentation of<br />
                       opening bracket&#8217;s line<br />
  &#8211;format=format      set the error format [default|pylint|&lt;custom&gt;]<br />
  &#8211;diff               report only lines changed according to the unified diff<br />
                       received on STDIN<br />
  Testing Options:<br />
    &#8211;benchmark        measure processing speed<br />
  Configuration:<br />
    The project options are read from the [pep8] section of the tox.ini<br />
    file or the setup.cfg file located in any parent folder of the path(s)<br />
being processed.Allowed options are : exclude, filename, select,<br />
    ignore, max &#8211; line &#8211; length, hang &#8211; closing, count, format, quiet, show &#8211; pep8,<br />
    show &#8211; source, statistics, verbose.&#8211;config = path user config file location(default<br />
                                                                                 : ~ /.config / pep8)</p>
<h3>Configuration</h3>
<p> The behaviour may be configured at two levels, the user and project levels. </p>
<p> At the user level, settings are read from the following locations:</p>
<dl>
<dt><code>If on Windows:</code></p>
<dd> <code>~\.pep8</code></p>
<dt><code>Otherwise, if the XDG_CONFIG_HOME</code> environment variable is defined:</p>
<dd> <code>XDG_CONFIG_HOME/pep8</code></p>
<dt><code>Else if XDG_CONFIG_HOME</code> is not defined:</p>
<dd> <code>~/.config/pep8</code> </p>
<p> Example: </p>
<pre>
[pep8]
ignore = E226,E302,E41
max-line-length = 160
</pre>
<p> At the project level, a <code>setup.cfg</code> file or a <code>tox.ini</code> file is read if present. If none of these files have a <code>[pep8]</code> section, no project specific configuration is loaded.</dl>
<h3>Error codes</h3>
<p> This is the current list of error and warning codes: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> code </td>
<td> sample message
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E1</code> </td>
<td> <i>Indentation</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E101 </td>
<td> indentation contains mixed spaces and tabs
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E111 </td>
<td> indentation is not a multiple of four
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E112 </td>
<td> expected an indented block
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E113 </td>
<td> unexpected indentation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E114 </td>
<td> indentation is not a multiple of four (comment)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E115 </td>
<td> expected an indented block (comment)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E116 </td>
<td> unexpected indentation (comment)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E121 (*^) </td>
<td> continuation line under-indented for hanging indent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E122 (^) </td>
<td> continuation line missing indentation or outdented
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E123 (*) </td>
<td> closing bracket does not match indentation of opening bracket&#8217;s line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E124 (^) </td>
<td> closing bracket does not match visual indentation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E125 (^) </td>
<td> continuation line with same indent as next logical line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E126 (*^) </td>
<td> continuation line over-indented for hanging indent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E127 (^) </td>
<td> continuation line over-indented for visual indent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E128 (^) </td>
<td> continuation line under-indented for visual indent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E129 (^) </td>
<td> visually indented line with same indent as next logical line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E131 (^) </td>
<td> continuation line unaligned for hanging indent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E133 (*) </td>
<td> closing bracket is missing indentation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E2</code> </td>
<td> <i>Whitespace</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E201 </td>
<td> whitespace after &#8216;(&#8216;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E202 </td>
<td> whitespace before &#8216;)&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E203 </td>
<td> whitespace before &#8216;:&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E211 </td>
<td> whitespace before &#8216;(&#8216;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E221 </td>
<td> multiple spaces before operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E222 </td>
<td> multiple spaces after operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E223 </td>
<td> tab before operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E224 </td>
<td> tab after operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E225 </td>
<td> missing whitespace around operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E226 (*) </td>
<td> missing whitespace around arithmetic operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E227 </td>
<td> missing whitespace around bitwise or shift operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E228 </td>
<td> missing whitespace around modulo operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E231 </td>
<td> missing whitespace after &#8216;,&#8217;, &#8216;;&#8217;, or &#8216;:&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E241 (*) </td>
<td> multiple spaces after &#8216;,&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E242 (*) </td>
<td> tab after &#8216;,&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E251 </td>
<td> unexpected spaces around keyword / parameter equals
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E261 </td>
<td> at least two spaces before inline comment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E262 </td>
<td> inline comment should start with &#8216;# &#8216;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E265 </td>
<td> block comment should start with &#8216;# &#8216;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E266 </td>
<td> too many leading &#8216;#&#8217; for block comment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E271 </td>
<td> multiple spaces after keyword
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E272 </td>
<td> multiple spaces before keyword
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E273 </td>
<td> tab after keyword
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E274 </td>
<td> tab before keyword
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E275 </td>
<td> missing whitespace after keyword
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E3</code> </td>
<td> <i>Blank line</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E301 </td>
<td> expected 1 blank line, found 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E302 </td>
<td> expected 2 blank lines, found 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E303 </td>
<td> too many blank lines (3)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E304 </td>
<td> blank lines found after function decorator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E4</code> </td>
<td> <i>Import</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E401 </td>
<td> multiple imports on one line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E402 </td>
<td> module level import not at top of file
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E5</code> </td>
<td> <i>Line length</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E501 (^) </td>
<td> line too long (82 &gt; 79 characters)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E502 </td>
<td> the backslash is redundant between brackets
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E7</code> </td>
<td> <i>Statement</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E701 </td>
<td> multiple statements on one line (colon)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E702 </td>
<td> multiple statements on one line (semicolon)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E703 </td>
<td> statement ends with a semicolon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E704 (*) </td>
<td> multiple statements on one line (def)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E711 (^) </td>
<td> comparison to None should be &#8216;if cond is None:&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E712 (^) </td>
<td> comparison to True should be &#8216;if cond is True:&#8217; or &#8216;if cond:&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E713 </td>
<td> test for membership should be &#8216;not in&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E714 </td>
<td> test for object identity should be &#8216;is not&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E721 (^) </td>
<td> do not compare types, use &#8216;isinstance()&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E731 </td>
<td> do not assign a lambda expression, use a def
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>E9</code> </td>
<td> <i>Runtime</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E901 </td>
<td> SyntaxError or IndentationError
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> E902 </td>
<td> IOError
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>W1</code> </td>
<td> <i>Indentation warning</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W191 </td>
<td> indentation contains tabs
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>W2</code> </td>
<td> <i>Whitespace warning</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W291 </td>
<td> trailing whitespace
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W292 </td>
<td> no newline at end of file
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W293 </td>
<td> blank line contains whitespace
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>W3</code> </td>
<td> <i>Blank line warning</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W391 </td>
<td> blank line at end of file
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>W5</code> </td>
<td> <i>Line break warning</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W503 (*) </td>
<td> line break occurred before a binary operator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>W6</code> </td>
<td> <i>Deprecation warning</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W601 </td>
<td> .has_key() is deprecated, use &#8216;in&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W602 </td>
<td> deprecated form of raising exception
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W603 </td>
<td> &#8216;&lt;&gt;&#8217; is deprecated, use &#8216;!=&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> W604 </td>
<td> backticks are deprecated, use &#8216;repr()&#8217;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <code>(*)</code> In the default configuration, the checks <code>E121</code>, <code>E123</code>, <code>E126</code>, <code>E133</code>, <code>E226</code>, <code>E241</code>, <code>E242</code>, <code>E704</code> and <code>W503</code> are ignored because they are not rules unanimously accepted, and <i>PEP 8</i> does not enforce them. The check <code>E133</code> is mutually exclusive with check <code>E123</code>. Use switch <code>&#8211;hang- closing</code> to report <code>E133</code> instead of <code>E123</code>. </p>
<p> <code>(^)</code> These checks can be disabled at the line level using the <code># noqa</code> special comment. This possibility should be reserved for special cases. <i>Special cases aren&#8217;t special enough to break the rules.</i> </p>
<p> Note: most errors can be listed with such one-liner: </p>
<pre>
$ python pycodestyle.py --first --select E,W testsuite/ --format '%(code)s: %(text)s'
</pre>
<h3>Related tools</h3>
<p> The <i>flake8 checker</i> is a wrapper around <code>pycodestyle</code> and similar tools. It supports plugins. </p>
<p> Other tools which use <code>pycodestyle</code> are referenced in the Wiki: <i>list of related tools</i>.</p>
<h2>ADVANCED USAGE</h2>
<h3>Automated tests</h3>
<p> You can also execute <code>pycodestyle</code> tests from Python code. For example, this can be highly useful for automated testing of coding style conformance in your project: </p>
<pre>
import unittest
import pycodestyle
class TestCodeFormat(unittest.TestCase):
    def test_conformance(self):
        &quot;&quot;&quot;Test that we conform to PEP-8.&quot;&quot;&quot;
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['file1.py', 'file2.py'])
        self.assertEqual(result.total_errors, 0,
                         &quot;Found code style errors (and warnings).&quot;)
</pre>
<p> If you are using <code>nosetests</code> for running tests, remove <code>quiet=True</code> since Nose suppresses stdout. </p>
<p> There&#8217;s also a shortcut for checking a single file: </p>
<pre>
import pycodestyle
fchecker = pycodestyle.Checker('testsuite/E27.py', show_source=True)
file_errors = fchecker.check_all()
print(&quot;Found %s errors (and warnings)&quot; % file_errors)
</pre>
<h3>Configuring tests</h3>
<p> You can configure automated <code>pycodestyle</code> tests in a variety of ways. </p>
<p> For example, you can pass in a path to a configuration file that <code>pycodestyle</code> should use: </p>
<pre>
import pycodestyle
style = pycodestyle.StyleGuide(config_file='/path/to/tox.ini')
</pre>
<p> You can also set specific options explicitly: </p>
<pre>
style = pycodestyle.StyleGuide(ignore=['E501'])
</pre>
<h3>Skip file header</h3>
<p> Another example is related to the <i>feature request #143</i>: skip a number of lines at the beginning and the end of a file. This use case is easy to implement through a custom wrapper for the PEP 8 library: </p>
<p>#!python<br />
import pycodestyle LINES_SLICE = slice(14, &#8211; 20) class StyleGuide(pycodestyle.StyleGuide) : &#8220;&#8221;<br />
                                                                                            &#8220;This subclass of pycodestyle.StyleGuide will skip the first and last lines<br />
                                                                  of each file.&#8221;&#8221;<br />
                                                                               &#8221;<br />
                                                                  def input_file(self, filename, lines = None, expected = None, line_offset = 0) : if lines is None:assert line_offset == 0 line_offset = LINES_SLICE.start or 0 lines = pycodestyle.readlines(filename)[LINES_SLICE] return super(StyleGuide, self).input_file(filename, lines = lines, expected = expected, line_offset = line_offset) if __name__ == &#8216;__main__&#8217; :style = StyleGuide(parse_argv = True, config_file = True) report = style.check_files() if report.total_errors:raise SystemExit(1)</p>
<p> This module declares a lines&#8217; window which skips 14 lines at the beginning and 20 lines at the end. If there&#8217;s no line to skip at the end, it could be changed with <code>LINES_SLICE = slice(14, None)</code> for example. </p>
<p> You can save it in a file and use it with the same options as the original <code>pycodestyle</code>.</p>
<h2>PYCODESTYLE API</h2>
<p> The library provides classes which are usable by third party tools.</p>
<dl>
<dt>&bull;</p>
<dd> <i>Checker Classes</i></p>
<dt>&bull;</p>
<dd> <i>Report Classes</i></p>
<dt>&bull;</p>
<dd> <i>Utilities</i></dl>
<h3>Checker Classes</h3>
<p> The <code>StyleGuide</code> class is used to configure a style guide checker instance to check multiple files. </p>
<p> The <code>Checker</code> class can be used to check a single file.</p>
<dl>
<dt><code>class pycodestyle.StyleGuide(parse_argv=False, config_file=None, parser=None, paths=None, report=None, **kwargs)</code></p>
<dd> Initialize a PEP-8 instance with few options.</p>
<dt><code>init_report(reporter=None)</code></p>
<dd> Initialize the report instance.</p>
<dt><code>check_files(paths=None)</code></p>
<dd> Run all checks on the paths.</p>
<dt><code>input_file(filename, lines=None, expected=None, line_offset=0)</code></p>
<dd> Run all checks on a Python source file.</p>
<dt><code>input_dir(dirname)</code></p>
<dd> Check all files in this directory and all subdirectories.</p>
<dt><code>excluded(filename, parent=None)</code></p>
<dd> Check if the file should be excluded. </p>
<p> Check if &#8216;options.exclude&#8217; contains a pattern that matches filename.</p>
<dt><code>ignore_code(code)</code></p>
<dd> Check if the error code should be ignored. </p>
<p> If &#8216;options.select&#8217; contains a prefix of the error code, return False. Else, if &#8216;options.ignore&#8217; contains a prefix of the error code, return True.</p>
<dt><code>get_checks(argument_name)</code></p>
<dd> Get all the checks for this category. </p>
<p> Find all globally visible functions where the first argument name starts with argument_name and which contain selected tests.</p>
<dt><code>class pycodestyle.Checker(filename=None, lines=None, report=None, **kwargs)</code></p>
<dd> Load a Python source file, tokenize it, check coding style.</p>
<dt><code>readline()</code></p>
<dd> Get the next line from the input buffer.</p>
<dt><code>run_check(check, argument_names)</code></p>
<dd> Run a check plugin.</p>
<dt><code>check_physical(line)</code></p>
<dd> Run all physical checks on a raw input line.</p>
<dt><code>build_tokens_line()</code></p>
<dd> Build a logical line from tokens.</p>
<dt><code>check_logical()</code></p>
<dd> Build a line from tokens and run all logical checks on it.</p>
<dt><code>check_ast()</code></p>
<dd> Build the file&#8217;s AST and run all AST checks.</p>
<dt><code>generate_tokens()</code></p>
<dd> Tokenize the file, run physical line checks and yield tokens.</p>
<dt><code>check_all(expected=None, line_offset=0)</code></p>
<dd> Run all checks on the input file.</dl>
<h3>Report Classes</h3>
<dl>
<dt><code>class pycodestyle.BaseReport(options)</code></p>
<dd> Collect the results of the checks.</p>
<dt><code>start()</code></p>
<dd> Start the timer.</p>
<dt><code>stop()</code></p>
<dd> Stop the timer.</p>
<dt><code>init_file(filename, lines, expected, line_offset)</code></p>
<dd> Signal a new file.</p>
<dt><code>increment_logical_line()</code></p>
<dd> Signal a new logical line.</p>
<dt><code>error(line_number, offset, text, check)</code></p>
<dd> Report an error, according to options.</p>
<dt><code>get_file_results()</code></p>
<dd> Return the count of errors and warnings for this file.</p>
<dt><code>get_count(prefix=&#8221;)</code></p>
<dd> Return the total count of errors and warnings.</p>
<dt><code>get_statistics(prefix=&#8221;)</code></p>
<dd> Get statistics for message codes that start with the prefix. </p>
<p> prefix=&#8221; matches all errors and warnings prefix=&#8217;E&#8217; matches all errors prefix=&#8217;W&#8217; matches all warnings prefix=&#8217;E4&#8242; matches all errors that have to do with imports</p>
<dt><code>print_statistics(prefix=&#8221;)</code></p>
<dd> Print overall statistics (number of errors and warnings).</p>
<dt><code>print_benchmark()</code></p>
<dd> Print benchmark numbers.</p>
<dt><code>class pycodestyle.FileReport(options)</code></p>
<dd> Collect the results of the checks and print only the filenames.</p>
<dt><code>class pycodestyle.StandardReport(options)</code></p>
<dd> Collect and print the results of the checks.</p>
<dt><code>class pycodestyle.DiffReport(options)</code></p>
<dd> Collect and print the results for the changed lines only.</dl>
<h3>Utilities</h3>
<dl>
<dt><code>pycodestyle.expand_indent(line)</code></p>
<dd> Return the amount of indentation. </p>
<p> Tabs are expanded to the next multiple of 8. </p>
<pre>
&gt;&gt;&gt; expand_indent('    ')
4
&gt;&gt;&gt; expand_indent('	')
8
&gt;&gt;&gt; expand_indent('       	')
8
&gt;&gt;&gt; expand_indent('        	')
16
</pre>
<dt><code>pycodestyle.mute_string(text)</code></p>
<dd> Replace contents with &#8216;xxx&#8217; to prevent syntax matching. </p>
<pre>
&gt;&gt;&gt; mute_string('&quot;abc&quot;')
'&quot;xxx&quot;'
&gt;&gt;&gt; mute_string(&quot;'''abc'''&quot;)
&quot;'''xxx'''&quot;
&gt;&gt;&gt; mute_string(&quot;r'abc'&quot;)
&quot;r'xxx'&quot;
</pre>
<dt><code>pycodestyle.read_config(options, args, arglist, parser)</code></p>
<dd> Read and parse configurations. </p>
<p> If a config file is specified on the command line with the &quot;&#8211;config&quot; option, then only it is used for configuration. </p>
<p> Otherwise, the user configuration (~/.config/pep8) and any local configurations in the current directory or above will be merged together (in that order) using the read method of ConfigParser.</p>
<dt><code>pycodestyle.process_options(arglist=None, parse_argv=False, config_file=None)</code></p>
<dd> Process options passed either via arglist or via command line args. </p>
<p> Passing in the <code>config_file</code> parameter allows other tools, such as flake8 to specify their own options to be processed in pep8.</p>
<dt><code>pycodestyle.register_check(func_or_cls, codes=None)</code></p>
<dd> Register a new check object.</dl>
<h2>DEVELOPER&#8217;S NOTES</h2>
<h3>Source code</h3>
<p> The source code is currently <i>available on GitHub</i> under the terms and conditions of the <i>Expat license</i>. Fork away!</p>
<dl>
<dt>&bull;</p>
<dd> <i>Source code</i> and <i>issue tracker</i> on GitHub.</p>
<dt>&bull;</p>
<dd> <i>Continuous tests</i> against Python 2.6 through 3.4 and PyPy, on <i>Travis-CI platform</i>.</dl>
<h3>Direction</h3>
<p> Some high-level aims and directions to bear in mind for contributions:</p>
<dl>
<dt>&bull;</p>
<dd> <code>pycodestyle</code> is intended to be as fast as possible. Using the <code>ast</code> module defeats that purpose. The <i>pep8-naming</i> plugin exists for this sort of functionality.</p>
<dt>&bull;</p>
<dd> If you want to provide extensibility / plugins, please see <i>flake8</i> &#8211; <code>pycodestyle</code> doesn&#8217;t want or need a plugin architecture.</p>
<dt>&bull;</p>
<dd> Python 2.6 support is still deemed important.</p>
<dt>&bull;</p>
<dd> <code>pycodestyle</code> aims to have no external dependencies.</dl>
<h3>Contribute</h3>
<p> You can add checks to this program by writing plugins. Each plugin is a simple function that is called for each line of source code, either physical or logical. </p>
<p> Physical line:</p>
<dl>
<dt>&bull;</p>
<dd> Raw line of text from the input file. </p>
<p> Logical line:</p>
<dt>&bull;</p>
<dd> Multi-line statements converted to a single line.</p>
<dt>&bull;</p>
<dd> Stripped left and right.</p>
<dt>&bull;</p>
<dd> Contents of strings replaced with <code>&quot;xxx&quot;</code> of same length.</p>
<dt>&bull;</p>
<dd> Comments removed. </p>
<p> The check function requests physical or logical lines by the name of the first argument: </p>
<pre>
def maximum_line_length(physical_line)
def extraneous_whitespace(logical_line)
def blank_lines(logical_line, blank_lines, indent_level, line_number)
</pre>
<p> The last example above demonstrates how check plugins can request additional information with extra arguments. All attributes of the <code>Checker</code> object are available. Some examples:</p>
<dt>&bull;</p>
<dd> <code>lines</code>: a list of the raw lines from the input file</p>
<dt>&bull;</p>
<dd> <code>tokens</code>: the tokens that contribute to this logical line</p>
<dt>&bull;</p>
<dd> <code>line_number</code>: line number in the input file</p>
<dt>&bull;</p>
<dd> <code>total_lines</code>: number of lines in the input file</p>
<dt>&bull;</p>
<dd> <code>blank_lines</code>: blank lines before this one</p>
<dt>&bull;</p>
<dd> <code>indent_char</code>: indentation character in this file (<code>&quot; &quot;</code> or <code>&quot;	&quot;</code>)</p>
<dt>&bull;</p>
<dd> <code>indent_level</code>: indentation (with tabs expanded to multiples of 8)</p>
<dt>&bull;</p>
<dd> <code>previous_indent_level</code>: indentation on previous line</p>
<dt>&bull;</p>
<dd> <code>previous_logical</code>: previous logical line </p>
<p> Check plugins can also maintain per-file state. If you need this, declare a parameter named <code>checker_state</code>. You will be passed a dict, which will be the same one for all lines in the same file but a different one for different files. Each check plugin gets its own dict, so you don&#8217;t need to worry about clobbering the state of other plugins. </p>
<p> The docstring of each check function shall be the relevant part of text from <i>PEP 8</i>. It is printed if the user enables <code>&#8211;show-pep8</code>. Several docstrings contain examples directly from the <i>PEP 8</i> document. </p>
<pre><code>
Okay : spam(ham[1], {eggs : 2})
           E201 : spam(ham[1], {eggs : 2})
</code></pre>
<p> These examples are verified automatically when <code>pycodestyle.py</code> is run with the <code>&#8211;doctest</code> option. You can add examples for your own check functions. The format is simple: <code>&quot;Okay&quot;</code> or error/warning code followed by colon and space, the rest of the line is example source code. If you put <code>&#8216;r&#8217;</code> before the docstring, you can use <code>
</code> for newline and <code>	</code> for tab. </p>
<p> Then be sure to pass the tests: </p>
<pre>
$ python pycodestyle.py --testsuite testsuite
$ python pycodestyle.py --doctest
$ python pycodestyle.py --verbose pycodestyle.py
</pre>
<p> When contributing to pycodestyle, please observe our <i>Code of Conduct</i>.</dl>
<h3>Changes</h3>
<h3>2.0.0 (2016-05-31)</h3>
<p> Announcements:</p>
<dl>
<dt>&bull;</p>
<dd> Repository renamed to <i>pycodestyle</i>; Issue #466 / #481.</p>
<dt>&bull;</p>
<dd> Added joint Code of Conduct as member of PyCQA; #483 </p>
<p> Changes:</p>
<dt>&bull;</p>
<dd> Added tox test support for Python 3.5 and pypy3</p>
<dt>&bull;</p>
<dd> Added check E275 for whitespace on <i>from &#8230; import &#8230;</i> lines; #489 / #491</p>
<dt>&bull;</p>
<dd> Added W503 to the list of codes ignored by default ignore list; #498</p>
<dt>&bull;</p>
<dd> Removed use of project level <i>.pep8</i> configuration file; #364 </p>
<p> Bugs:</p>
<dt>&bull;</p>
<dd> Fixed bug with treating <i>~</i> operator as binary; #383 / #384</p>
<dt>&bull;</p>
<dd> Identify binary operators as unary; #484 / #485</dl>
<h3>1.7.0 (2016-01-12)</h3>
<p> Announcements:</p>
<dl>
<dt>&bull;</p>
<dd> Repository moved to PyCQA Organization on GitHub: <i><a rel="nofollow" href="https://github.com/pycqa/pep8">https://github.com/pycqa/pep8</a></i> </p>
<p> Changes:</p>
<dt>&bull;</p>
<dd> Reverted the fix in #368, &quot;options passed on command line are only ones accepted&quot; feature. This has many unintended consequences in pep8 and flake8 and needs to be reworked when I have more time.</p>
<dt>&bull;</p>
<dd> Added support for Python 3.5. (Issue #420 &amp; #459)</p>
<dt>&bull;</p>
<dd> Added support for multi-line config_file option parsing. (Issue #429)</p>
<dt>&bull;</p>
<dd> Improved parameter parsing. (Issues #420 &amp; #456) </p>
<p> Bugs:</p>
<dt>&bull;</p>
<dd> Fixed BytesWarning on Python 3. (Issue #459)</dl>
<h3>1.6.2 (2015-02-15)</h3>
<p> Changes:</p>
<dl>
<dt>&bull;</p>
<dd> Added check for breaking around a binary operator. (Issue #197, Pull #305) </p>
<p> Bugs:</p>
<dt>&bull;</p>
<dd> Restored config_file parameter in process_options(). (Issue #380)</dl>
<h3>1.6.1 (2015-02-08)</h3>
<p> Changes:</p>
<dl>
<dt>&bull;</p>
<dd> Assign variables before referenced. (Issue #287) </p>
<p> Bugs:</p>
<dt>&bull;</p>
<dd> Exception thrown due to unassigned <code>local_dir</code> variable. (Issue #377)</dl>
<h3>1.6.0 (2015-02-06)</h3>
<p> News:</p>
<dl>
<dt>&bull;</p>
<dd> Ian Lee &lt;<i>ianlee1521 [at] gmail.com</i>&gt; joined the project as a maintainer. </p>
<p> Changes:</p>
<dt>&bull;</p>
<dd> Report E731 for lambda assignment. (Issue #277)</p>
<dt>&bull;</p>
<dd> Report E704 for one-liner def instead of E701. Do not report this error in the default configuration. (Issue #277)</p>
<dt>&bull;</p>
<dd> Replace codes E111, E112 and E113 with codes E114, E115 and E116 for bad indentation of comments. (Issue #274)</p>
<dt>&bull;</p>
<dd> Report E266 instead of E265 when the block comment starts with multiple <code>#</code>. (Issue #270)</p>
<dt>&bull;</p>
<dd> Report E402 for import statements not at the top of the file. (Issue #264)</p>
<dt>&bull;</p>
<dd> Do not enforce whitespaces around <code>**</code> operator. (Issue #292)</p>
<dt>&bull;</p>
<dd> Strip whitespace from around paths during normalization. (Issue #339 / #343)</p>
<dt>&bull;</p>
<dd> Update <code>&#8211;format</code> documentation. (Issue #198 / Pull Request #310)</p>
<dt>&bull;</p>
<dd> Add <code>.tox/</code> to default excludes. (Issue #335)</p>
<dt>&bull;</p>
<dd> Do not report E121 or E126 in the default configuration. (Issues #256 / #316)</p>
<dt>&bull;</p>
<dd> Allow spaces around the equals sign in an annotated function. (Issue #357)</p>
<dt>&bull;</p>
<dd> Allow trailing backslash if in an inline comment. (Issue #374)</p>
<dt>&bull;</p>
<dd> If <code>&#8211;config</code> is used, only that configuration is processed. Otherwise, merge the user and local configurations are merged. (Issue #368 / #369) </p>
<p> Bug fixes:</p>
<dt>&bull;</p>
<dd> Don&#8217;t crash if Checker.build_tokens_line() returns None. (Issue #306)</p>
<dt>&bull;</p>
<dd> Don&#8217;t crash if os.path.expanduser() throws an ImportError. (Issue #297)</p>
<dt>&bull;</p>
<dd> Missing space around keyword parameter equal not always reported, E251. (Issue #323)</p>
<dt>&bull;</p>
<dd> Fix false positive E711/E712/E713. (Issues #330 and #336)</p>
<dt>&bull;</p>
<dd> Do not skip physical checks if the newline is escaped. (Issue #319)</p>
<dt>&bull;</p>
<dd> Flush sys.stdout to avoid race conditions with printing. See flake8 bug: <i><a rel="nofollow" href="https://gitlab.com/pycqa/flake8/issues/17">https://gitlab.com/pycqa/flake8/issues/17</a></i> for more details. (Issue #363)</dl>
<h3>1.5.7 (2014-05-29)</h3>
<p> Bug fixes:</p>
<dl>
<dt>&bull;</p>
<dd> Skip the traceback on &quot;Broken pipe&quot; signal. (Issue #275)</p>
<dt>&bull;</p>
<dd> Do not exit when an option in <code>setup.cfg</code> or <code>tox.ini</code> is not recognized.</p>
<dt>&bull;</p>
<dd> Check the last line even if it does not end with a newline. (Issue #286)</p>
<dt>&bull;</p>
<dd> Always open files in universal newlines mode in Python 2. (Issue #288)</dl>
<h3>1.5.6 (2014-04-14)</h3>
<p> Bug fixes:</p>
<dl>
<dt>&bull;</p>
<dd> Check the last line even if it has no end-of-line. (Issue #273)</dl>
<h3>1.5.5 (2014-04-10)</h3>
<p> Bug fixes:</p>
<dl>
<dt>&bull;</p>
<dd> Fix regression with E22 checks and inline comments. (Issue #271)</dl>
<h3>1.5.4 (2014-04-07)</h3>
<p> Bug fixes:</p>
<dl>
<dt>&bull;</p>
<dd> Fix negative offset with E303 before a multi-line docstring. (Issue #269)</dl>
<h3>1.5.3 (2014-04-04)</h3>
<p> Bug fixes:</p>
<dl>
<dt>&bull;</p>
<dd> Fix wrong offset computation when error is on the last char of a physical line. (Issue #268)</dl>
<h3>1.5.2 (2014-04-04)</h3>
<p> Changes:</p>
<dl>
<dt>&bull;</p>
<dd> Distribute a universal wheel file. </p>
<p> Bug fixes:</p>
<dt>&bull;</p>
<dd> Report correct line number for E303 with comments. (Issue #60)</p>
<dt>&bull;</p>
<dd> Do not allow newline after parameter equal. (Issue #252)</p>
<dt>&bull;</p>
<dd> Fix line number reported for multi-line strings. (Issue #220)</p>
<dt>&bull;</p>
<dd> Fix false positive E121/E126 with multi-line strings. (Issue #265)</p>
<dt>&bull;</p>
<dd> Fix E501 not detected in comments with Python 2.5.</p>
<dt>&bull;</p>
<dd> Fix caret position with <code>&#8211;show-source</code> when line contains tabs.</dl>
<h3>1.5.1 (2014-03-27)</h3>
<p> Bug fixes:</p>
<dl>
<dt>&bull;</p>
<dd> Fix a crash with E125 on multi-line strings. (Issue #263)</dl>
<h3>1.5 (2014-03-26)</h3>
<p> Changes:</p>
<dl>
<dt>&bull;</p>
<dd> Report E129 instead of E125 for visually indented line with same indent as next logical line. (Issue #126)</p>
<dt>&bull;</p>
<dd> Report E265 for space before block comment. (Issue #190)</p>
<dt>&bull;</p>
<dd> Report E713 and E714 when operators <code>not in</code> and <code>is not</code> are recommended. (Issue #236)</p>
<dt>&bull;</p>
<dd> Allow long lines in multiline strings and comments if they cannot be wrapped. (Issue #224).</p>
<dt>&bull;</p>
<dd> Optionally disable physical line checks inside multiline strings, using <code># noqa</code>. (Issue #242)</p>
<dt>&bull;</p>
<dd> Change text for E121 to report &quot;continuation line under-indented for hanging indent&quot; instead of indentation not being a multiple of 4.</p>
<dt>&bull;</p>
<dd> Report E131 instead of E121 / E126 if the hanging indent is not consistent within the same continuation block. It helps when error E121 or E126 is in the <code>ignore</code> list.</p>
<dt>&bull;</p>
<dd> Report E126 instead of E121 when the continuation line is hanging with extra indentation, even if indentation is not a multiple of 4. </p>
<p> Bug fixes:</p>
<dt>&bull;</p>
<dd> Allow the checkers to report errors on empty files. (Issue #240)</p>
<dt>&bull;</p>
<dd> Fix ignoring too many checks when <code>&#8211;select</code> is used with codes declared in a flake8 extension. (Issue #216)</p>
<dt>&bull;</p>
<dd> Fix regression with multiple brackets. (Issue #214)</p>
<dt>&bull;</p>
<dd> Fix <code>StyleGuide</code> to parse the local configuration if the keyword argument <code>paths</code> is specified. (Issue #246)</p>
<dt>&bull;</p>
<dd> Fix a false positive E124 for hanging indent. (Issue #254)</p>
<dt>&bull;</p>
<dd> Fix a false positive E126 with embedded colon. (Issue #144)</p>
<dt>&bull;</p>
<dd> Fix a false positive E126 when indenting with tabs. (Issue #204)</p>
<dt>&bull;</p>
<dd> Fix behaviour when <code>exclude</code> is in the configuration file and the current directory is not the project directory. (Issue #247)</p>
<dt>&bull;</p>
<dd> The logical checks can return <code>None</code> instead of an empty iterator. (Issue #250)</p>
<dt>&bull;</p>
<dd> Do not report multiple E101 if only the first indentation starts with a tab. (Issue #237)</p>
<dt>&bull;</p>
<dd> Fix a rare false positive W602. (Issue #34)</dl>
<h3>1.4.6 (2013-07-02)</h3>
<p> Changes:</p>
<dl>
<dt>&bull;</p>
<dd> Honor <code># noqa</code> for errors E711 and E712. (Issue #180)</p>
<dt>&bull;</p>
<dd> When both a <code>tox.ini</code> and a <code>setup.cfg</code> are present in the project directory, merge their contents. The <code>tox.ini</code> file takes precedence (same as before). (Issue #182)</p>
<dt>&bull;</p>
<dd> Give priority to <code>&#8211;select</code> over <code>&#8211;ignore</code>. (Issue #188)</p>
<dt>&bull;</p>
<dd> Compare full path when excluding a file. (Issue #186)</p>
<dt>&bull;</p>
<dd> New option <code>&#8211;hang-closing</code> to switch to the alternative style of closing bracket indentation for hanging indent. Add error E133 for closing bracket which is missing indentation. (Issue #103)</p>
<dt>&bull;</p>
<dd> Accept both styles of closing bracket indentation for hanging indent. Do not report error E123 in the default configuration. (Issue #103) </p>
<p> Bug fixes:</p>
<dt>&bull;</p>
<dd> Do not crash when running AST checks and the document contains null bytes. (Issue #184)</p>
<dt>&bull;</p>
<dd> Correctly report other E12 errors when E123 is ignored. (Issue #103)</p>
<dt>&bull;</p>
<dd> Fix false positive E261/E262 when the file contains a BOM. (Issue #193)</p>
<dt>&bull;</p>
<dd> Fix E701, E702 and E703 not detected sometimes. (Issue #196)</p>
<dt>&bull;</p>
<dd> Fix E122 not detected in some cases. (Issue #201 and #208)</p>
<dt>&bull;</p>
<dd> Fix false positive E121 with multiple brackets. (Issue #203)</dl>
<h3>1.4.5 (2013-03-06)</h3>
<dl>
<dt>&bull;</p>
<dd> When no path is specified, do not try to read from stdin. The feature was added in 1.4.3, but it is not supported on Windows. Use <code>&#8211;</code> filename argument to read from stdin. This usage is supported since 1.3.4. (Issue #170)</p>
<dt>&bull;</p>
<dd> Do not require <code>setuptools</code> in setup.py. It works around an issue with <code>pip</code> and Python 3. (Issue #172)</p>
<dt>&bull;</p>
<dd> Add <code>__pycache__</code> to the ignore list.</p>
<dt>&bull;</p>
<dd> Change misleading message for E251. (Issue #171)</p>
<dt>&bull;</p>
<dd> Do not report false E302 when the source file has a coding cookie or a comment on the first line. (Issue #174)</p>
<dt>&bull;</p>
<dd> Reorganize the tests and add tests for the API and for the command line usage and options. (Issues #161 and #162)</p>
<dt>&bull;</p>
<dd> Ignore all checks which are not explicitly selected when <code>select</code> is passed to the <code>StyleGuide</code> constructor.</dl>
<h3>1.4.4 (2013-02-24)</h3>
<dl>
<dt>&bull;</p>
<dd> Report E227 or E228 instead of E225 for whitespace around bitwise, shift or modulo operators. (Issue #166)</p>
<dt>&bull;</p>
<dd> Change the message for E226 to make clear that it is about arithmetic operators.</p>
<dt>&bull;</p>
<dd> Fix a false positive E128 for continuation line indentation with tabs.</p>
<dt>&bull;</p>
<dd> Fix regression with the <code>&#8211;diff</code> option. (Issue #169)</p>
<dt>&bull;</p>
<dd> Fix the <code>TestReport</code> class to print the unexpected warnings and errors.</dl>
<h3>1.4.3 (2013-02-22)</h3>
<dl>
<dt>&bull;</p>
<dd> Hide the <code>&#8211;doctest</code> and <code>&#8211;testsuite</code> options when installed.</p>
<dt>&bull;</p>
<dd> Fix crash with AST checkers when the syntax is invalid. (Issue #160)</p>
<dt>&bull;</p>
<dd> Read from standard input if no path is specified.</p>
<dt>&bull;</p>
<dd> Initiate a graceful shutdown on <code>Control+C</code>.</p>
<dt>&bull;</p>
<dd> Allow changing the <code>checker_class</code> for the <code>StyleGuide</code>.</dl>
<h3>1.4.2 (2013-02-10)</h3>
<dl>
<dt>&bull;</p>
<dd> Support AST checkers provided by third-party applications.</p>
<dt>&bull;</p>
<dd> Register new checkers with <code>register_check(func_or_cls, codes)</code>.</p>
<dt>&bull;</p>
<dd> Allow constructing a <code>StyleGuide</code> with a custom parser.</p>
<dt>&bull;</p>
<dd> Accept visual indentation without parenthesis after the <code>if</code> statement. (Issue #151)</p>
<dt>&bull;</p>
<dd> Fix UnboundLocalError when using <code># noqa</code> with continued lines. (Issue #158)</p>
<dt>&bull;</p>
<dd> Re-order the lines for the <code>StandardReport</code>.</p>
<dt>&bull;</p>
<dd> Expand tabs when checking E12 continuation lines. (Issue #155)</p>
<dt>&bull;</p>
<dd> Refactor the testing class <code>TestReport</code> and the specific test functions into a separate test module.</dl>
<h3>1.4.1 (2013-01-18)</h3>
<dl>
<dt>&bull;</p>
<dd> Allow sphinx.ext.autodoc syntax for comments. (Issue #110)</p>
<dt>&bull;</p>
<dd> Report E703 instead of E702 for the trailing semicolon. (Issue #117)</p>
<dt>&bull;</p>
<dd> Honor <code># noqa</code> in addition to <code># nopep8</code>. (Issue #149)</p>
<dt>&bull;</p>
<dd> Expose the <code>OptionParser</code> factory for better extensibility.</dl>
<h3>1.4 (2012-12-22)</h3>
<dl>
<dt>&bull;</p>
<dd> Report E226 instead of E225 for optional whitespace around common operators (<code>*</code>, <code>**</code>, <code>/</code>, <code>+</code> and <code>&#8211;</code>). This new error code is ignored in the default configuration because PEP 8 recommends to &quot;use your own judgement&quot;. (Issue #96)</p>
<dt>&bull;</p>
<dd> Lines with a <code># nopep8</code> at the end will not issue errors on line length E501 or continuation line indentation E12*. (Issue #27)</p>
<dt>&bull;</p>
<dd> Fix AssertionError when the source file contains an invalid line ending <code>&quot;
&quot;</code>. (Issue #119)</p>
<dt>&bull;</p>
<dd> Read the <code>[pep8]</code> section of <code>tox.ini</code> or <code>setup.cfg</code> if present. (Issue #93 and #141)</p>
<dt>&bull;</p>
<dd> Add the Sphinx-based documentation, and publish it on <i><a rel="nofollow" href="https://pycodestyle.readthedocs.io/">https://pycodestyle.readthedocs.io/</a></i>. (Issue #105)</dl>
<h3>1.3.4 (2012-12-18)</h3>
<dl>
<dt>&bull;</p>
<dd> Fix false positive E124 and E128 with comments. (Issue #100)</p>
<dt>&bull;</p>
<dd> Fix error on stdin when running with bpython. (Issue #101)</p>
<dt>&bull;</p>
<dd> Fix false positive E401. (Issue #104)</p>
<dt>&bull;</p>
<dd> Report E231 for nested dictionary in list. (Issue #142)</p>
<dt>&bull;</p>
<dd> Catch E271 at the beginning of the line. (Issue #133)</p>
<dt>&bull;</p>
<dd> Fix false positive E126 for multi-line comments. (Issue #138)</p>
<dt>&bull;</p>
<dd> Fix false positive E221 when operator is preceded by a comma. (Issue #135)</p>
<dt>&bull;</p>
<dd> Fix <code>&#8211;diff</code> failing on one-line hunk. (Issue #137)</p>
<dt>&bull;</p>
<dd> Fix the <code>&#8211;exclude</code> switch for directory paths. (Issue #111)</p>
<dt>&bull;</p>
<dd> Use <code>&#8211;</code> filename to read from standard input. (Issue #128)</dl>
<h3>1.3.3 (2012-06-27)</h3>
<dl>
<dt>&bull;</p>
<dd> Fix regression with continuation line checker. (Issue #98)</dl>
<h3>1.3.2 (2012-06-26)</h3>
<dl>
<dt>&bull;</p>
<dd> Revert to the previous behaviour for <code>&#8211;show-pep8</code>: do not imply <code>&#8211;first</code>. (Issue #89)</p>
<dt>&bull;</p>
<dd> Add E902 for IO errors. (Issue #87)</p>
<dt>&bull;</p>
<dd> Fix false positive for E121, and missed E124. (Issue #92)</p>
<dt>&bull;</p>
<dd> Set a sensible default path for config file on Windows. (Issue #95)</p>
<dt>&bull;</p>
<dd> Allow <code>verbose</code> in the configuration file. (Issue #91)</p>
<dt>&bull;</p>
<dd> Show the enforced <code>max-line-length</code> in the error message. (Issue #86)</dl>
<h3>1.3.1 (2012-06-18)</h3>
<dl>
<dt>&bull;</p>
<dd> Explain which configuration options are expected. Accept and recommend the options names with hyphen instead of underscore. (Issue #82)</p>
<dt>&bull;</p>
<dd> Do not read the user configuration when used as a module (except if <code>config_file=True</code> is passed to the <code>StyleGuide</code> constructor).</p>
<dt>&bull;</p>
<dd> Fix wrong or missing cases for the E12 series.</p>
<dt>&bull;</p>
<dd> Fix cases where E122 was missed. (Issue #81)</dl>
<h3>1.3 (2012-06-15)</h3>
<p> <code>WARNING:</code> The internal API is backwards incompatible.</p>
<dl>
<dt>&bull;</p>
<dd> Remove global configuration and refactor the library around a <code>StyleGuide</code> class; add the ability to configure various reporters. (Issue #35 and #66)</p>
<dt>&bull;</p>
<dd> Read user configuration from <code>~/.config/pep8</code> and local configuration from <code>./.pep8</code>. (Issue #22)</p>
<dt>&bull;</p>
<dd> Fix E502 for backslash embedded in multi-line string. (Issue #68)</p>
<dt>&bull;</p>
<dd> Fix E225 for Python 3 iterable unpacking (PEP 3132). (Issue #72)</p>
<dt>&bull;</p>
<dd> Enable the new checkers from the E12 series in the default configuration.</p>
<dt>&bull;</p>
<dd> Suggest less error-prone alternatives for E712 errors.</p>
<dt>&bull;</p>
<dd> Rewrite checkers to run faster (E22, E251, E27).</p>
<dt>&bull;</p>
<dd> Fixed a crash when parsed code is invalid (too many closing brackets).</p>
<dt>&bull;</p>
<dd> Fix E127 and E128 for continuation line indentation. (Issue #74)</p>
<dt>&bull;</p>
<dd> New option <code>&#8211;format</code> to customize the error format. (Issue #23)</p>
<dt>&bull;</p>
<dd> New option <code>&#8211;diff</code> to check only modified code. The unified diff is read from STDIN. Example: <code>hg diff | pep8 &#8211;diff</code> (Issue #39)</p>
<dt>&bull;</p>
<dd> Correctly report the count of failures and set the exit code to 1 when the <code>&#8211;doctest</code> or the <code>&#8211;testsuite</code> fails.</p>
<dt>&bull;</p>
<dd> Correctly detect the encoding in Python 3. (Issue #69)</p>
<dt>&bull;</p>
<dd> Drop support for Python 2.3, 2.4 and 3.0. (Issue #78)</dl>
<h3>1.2 (2012-06-01)</h3>
<dl>
<dt>&bull;</p>
<dd> Add E121 through E128 for continuation line indentation. These checks are disabled by default. If you want to force all checks, use switch <code>&#8211;select=E,W</code>. Patch by Sam Vilain. (Issue #64)</p>
<dt>&bull;</p>
<dd> Add E721 for direct type comparisons. (Issue #47)</p>
<dt>&bull;</p>
<dd> Add E711 and E712 for comparisons to singletons. (Issue #46)</p>
<dt>&bull;</p>
<dd> Fix spurious E225 and E701 for function annotations. (Issue #29)</p>
<dt>&bull;</p>
<dd> Add E502 for explicit line join between brackets.</p>
<dt>&bull;</p>
<dd> Fix E901 when printing source with <code>&#8211;show-source</code>.</p>
<dt>&bull;</p>
<dd> Report all errors for each checker, instead of reporting only the first occurrence for each line.</p>
<dt>&bull;</p>
<dd> Option <code>&#8211;show-pep8</code> implies <code>&#8211;first</code>.</dl>
<h3>1.1 (2012-05-24)</h3>
<dl>
<dt>&bull;</p>
<dd> Add E901 for syntax errors. (Issues #63 and #30)</p>
<dt>&bull;</p>
<dd> Add E271, E272, E273 and E274 for extraneous whitespace around keywords. (Issue #57)</p>
<dt>&bull;</p>
<dd> Add <code>tox.ini</code> configuration file for tests. (Issue #61)</p>
<dt>&bull;</p>
<dd> Add <code>.travis.yml</code> configuration file for continuous integration. (Issue #62)</dl>
<h3>1.0.1 (2012-04-06)</h3>
<dl>
<dt>&bull;</p>
<dd> Fix inconsistent version numbers.</dl>
<h3>1.0 (2012-04-04)</h3>
<dl>
<dt>&bull;</p>
<dd> Fix W602 <code>raise</code> to handle multi-char names. (Issue #53)</dl>
<h3>0.7.0 (2012-03-26)</h3>
<dl>
<dt>&bull;</p>
<dd> Now <code>&#8211;first</code> prints only the first occurrence of each error. The <code>&#8211;repeat</code> flag becomes obsolete because it is the default behaviour. (Issue #6)</p>
<dt>&bull;</p>
<dd> Allow specifying <code>&#8211;max-line-length</code>. (Issue #36)</p>
<dt>&bull;</p>
<dd> Make the shebang more flexible. (Issue #26)</p>
<dt>&bull;</p>
<dd> Add testsuite to the bundle. (Issue #25)</p>
<dt>&bull;</p>
<dd> Fixes for Jython. (Issue #49)</p>
<dt>&bull;</p>
<dd> Add PyPI classifiers. (Issue #43)</p>
<dt>&bull;</p>
<dd> Fix the <code>&#8211;exclude</code> option. (Issue #48)</p>
<dt>&bull;</p>
<dd> Fix W602, accept <code>raise</code> with 3 arguments. (Issue #34)</p>
<dt>&bull;</p>
<dd> Correctly select all tests if <code>DEFAULT_IGNORE == &#8221;</code>.</dl>
<h3>0.6.1 (2010-10-03)</h3>
<dl>
<dt>&bull;</p>
<dd> Fix inconsistent version numbers. (Issue #21)</dl>
<h3>0.6.0 (2010-09-19)</h3>
<dl>
<dt>&bull;</p>
<dd> Test suite reorganized and enhanced in order to check more failures with fewer test files. Read the <code>run_tests</code> docstring for details about the syntax.</p>
<dt>&bull;</p>
<dd> Fix E225: accept <code>print &gt;&gt;sys.stderr, &quot;&#8230;&quot;</code> syntax.</p>
<dt>&bull;</p>
<dd> Fix E501 for lines containing multibyte encoded characters. (Issue #7)</p>
<dt>&bull;</p>
<dd> Fix E221, E222, E223, E224 not detected in some cases. (Issue #16)</p>
<dt>&bull;</p>
<dd> Fix E211 to reject <code>v = dic[&#8216;a&#8217;] [&#8216;b&#8217;]</code>. (Issue #17)</p>
<dt>&bull;</p>
<dd> Exit code is always 1 if any error or warning is found. (Issue #10)</p>
<dt>&bull;</p>
<dd> <code>&#8211;ignore</code> checks are now really ignored, especially in conjunction with <code>&#8211;count</code>. (Issue #8)</p>
<dt>&bull;</p>
<dd> Blank lines with spaces yield W293 instead of W291: some developers want to ignore this warning and indent the blank lines to paste their code easily in the Python interpreter.</p>
<dt>&bull;</p>
<dd> Fix E301: do not require a blank line before an indented block. (Issue #14)</p>
<dt>&bull;</p>
<dd> Fix E203 to accept NumPy slice notation <code>a[0, :]</code>. (Issue #13)</p>
<dt>&bull;</p>
<dd> Performance improvements.</p>
<dt>&bull;</p>
<dd> Fix decoding and checking non-UTF8 files in Python 3.</p>
<dt>&bull;</p>
<dd> Fix E225: reject <code>True+False</code> when running on Python 3.</p>
<dt>&bull;</p>
<dd> Fix an exception when the line starts with an operator.</p>
<dt>&bull;</p>
<dd> Allow a new line before closing <code>)</code>, <code>}</code> or <code>]</code>. (Issue #5)</dl>
<h3>0.5.0 (2010-02-17)</h3>
<dl>
<dt>&bull;</p>
<dd> Changed the <code>&#8211;count</code> switch to print to sys.stderr and set exit code to 1 if any error or warning is found.</p>
<dt>&bull;</p>
<dd> E241 and E242 are removed from the standard checks. If you want to include these checks, use switch <code>&#8211;select=E,W</code>. (Issue #4)</p>
<dt>&bull;</p>
<dd> Blank line is not mandatory before the first class method or nested function definition, even if there&#8217;s a docstring. (Issue #1)</p>
<dt>&bull;</p>
<dd> Add the switch <code>&#8211;version</code>.</p>
<dt>&bull;</p>
<dd> Fix decoding errors with Python 3. (Issue #13 [1])</p>
<dt>&bull;</p>
<dd> Add <code>&#8211;select</code> option which is mirror of <code>&#8211;ignore</code>.</p>
<dt>&bull;</p>
<dd> Add checks E261 and E262 for spaces before inline comments.</p>
<dt>&bull;</p>
<dd> New check W604 warns about deprecated usage of backticks.</p>
<dt>&bull;</p>
<dd> New check W603 warns about the deprecated operator <code>&lt;&gt;</code>.</p>
<dt>&bull;</p>
<dd> Performance improvement, due to rewriting of E225.</p>
<dt>&bull;</p>
<dd> E225 now accepts:</p>
<dt>&bull;</p>
<dd> no whitespace after unary operator or similar. (Issue #9 [1])</p>
<dt>&bull;</p>
<dd> lambda function with argument unpacking or keyword defaults.</p>
<dt>&bull;</p>
<dd> Reserve &quot;2 blank lines&quot; for module-level logical blocks. (E303)</p>
<dt>&bull;</p>
<dd> Allow multi-line comments. (E302, issue #10 [1])</dl>
<h3>0.4.2 (2009-10-22)</h3>
<dl>
<dt>&bull;</p>
<dd> Decorators on classes and class methods are OK now.</dl>
<h3>0.4 (2009-10-20)</h3>
<dl>
<dt>&bull;</p>
<dd> Support for all versions of Python from 2.3 to 3.1.</p>
<dt>&bull;</p>
<dd> New and greatly expanded self tests.</p>
<dt>&bull;</p>
<dd> Added <code>&#8211;count</code> option to print the total number of errors and warnings.</p>
<dt>&bull;</p>
<dd> Further improvements to the handling of comments and blank lines. (Issue #1 [1] and others changes.)</p>
<dt>&bull;</p>
<dd> Check all py files in directory when passed a directory (Issue #2 [1]). This also prevents an exception when traversing directories with non <code>*.py</code> files.</p>
<dt>&bull;</p>
<dd> E231 should allow commas to be followed by <code>)</code>. (Issue #3 [1])</p>
<dt>&bull;</p>
<dd> Spaces are no longer required around the equals sign for keyword arguments or default parameter values.</p>
<dt>[1]</p>
<dd> These issues refer to the <i>previous issue tracker</i>.</dl>
<h3>0.3.1 (2009-09-14)</h3>
<dl>
<dt>&bull;</p>
<dd> Fixes for comments: do not count them when checking for blank lines between items.</p>
<dt>&bull;</p>
<dd> Added setup.py for pypi upload and easy_installability.</dl>
<h3>0.2 (2007-10-16)</h3>
<dl>
<dt>&bull;</p>
<dd> Loads of fixes and improvements.</dl>
<h3>0.1 (2006-10-01)</h3>
<dl>
<dt>&bull;</p>
<dd> First release.</p>
<dt>&bull;</p>
<dd> Online documentation: <i><a rel="nofollow" href="https://pycodestyle.readthedocs.io/">https://pycodestyle.readthedocs.io/</a></i></p>
<dt>&bull;</p>
<dd> Source code and issue tracker: <i><a rel="nofollow" href="https://github.com/pycqa/pycodestyle">https://github.com/pycqa/pycodestyle</a></i></p>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i> </p>
<p> Created by Johann C. Rocholl. </p>
<p> Maintained by Florent Xicluna and Ian Lee. </p>
<p> The <code>pycodestyle</code> library is provided under the terms and conditions of the Expat license: </p>
<pre>
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the &quot;Software&quot;), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Johann C. Rocholl, Florent Xicluna, Ian Lee</p>
<h2>COPYRIGHT</h2>
<p> 2006-2016, Johann C. Rocholl, Florent Xicluna, Ian Lee </p>
<h2>Index</h2>
