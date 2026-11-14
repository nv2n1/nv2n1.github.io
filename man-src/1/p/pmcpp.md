---
title: "pmcpp(1)"
name: "pmcpp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmcpp/"
description: "pmcpp – simple preprocessor for the Performance Co-Pilot"
---

<h2>NAME</h2>
<p> <code>pmcpp</code> &#8211; simple preprocessor for the Performance Co-Pilot</p>
<h2>SYNOPSIS</h2>
<p> <code>pmcpp</code> [<code>-Prs</code>] [<code>-D</code> <i>name</i>[=<i>value</i>] &#8230;] [<code>-I</code> <i>dir</i> &#8230;] [<i>infile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmcpp</code> provides a very simple pre-processor originally designed for manipulating Performance Metric Name Space (PMNS) files for the Performance Co-Pilot (PCP), but later generalized to provide conditional blocks, include file processing, in-line shell command execution and macro substitution for arbitrary files. It is most commonly used internally to process the PMNS file(s) after <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) is called and to pre-process the configuration files for <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Input lines are read from <i>infile</i> (or standard input if <i>infile</i> is not specified), processed and written to standard output. </p>
<p> All C-style comments of the form /* &#8230; */ are stripped from the input stream. </p>
<p> There are no predefined macros for <code>pmcpp</code> although macros may be defined on the command line using the <code>-D</code> option, where <i>name</i> and <i>value</i> must follow the same rules as described below for the <code>#define</code> directive. </p>
<p> <code>pmcpp</code> accepts the following directives in the input stream (like <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1)):</p>
<dl>
<dt>&bull;</p>
<dd> <code>#include &quot;</code><i>filename</i><code>&quot;</code><br />
 or<br />
 <code>#include &lt;</code><i>filename</i><code>&gt;</code><br />
 In either case the directory search path for <i>filename</i> tries <i>filename</i> first, then the directory for the command line <i>infile</i> (if any), followed by any directories named in <code>-I</code> command line arguments, and finally the <code>$PCP_VAR_DIR/pmns</code> directory (the latter is for backwards compatibility with earlier versions of <code>pmcpp</code> and the implied used from <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3)). <code>#include</code> directives may be nested, up to a maximum depth of 5.</p>
<dt>&bull;</p>
<dd> <code>#shell &quot;</code><i>command</i><code>&quot;</code><br />
 or<br />
 <code>#shell &#8216;</code><i>command</i><code>&#8216;<br />
 The shell </code><i>command</i> will be executed and the standard output is inserted into the stream of data to be processed by <code>pmcpp</code>. Functionally this is similar to a <code>#include</code> directive, except input lines are read from a <i>command</i> rather than a file. The <code>#shell</code> directive is most useful for including or excluding <code>#define</code> or <code>#undef</code> directives based on run-time logic in the <i>command</i>.</p>
<dt>&bull;</p>
<dd> <code>#define </code><i>name value</i><br />
 or<br />
 <code>#define </code><i>name </i><code>&quot;</code><i>value</i><code>&quot;</code><br />
 or<br />
 <code>#define </code><i>name </i><code>&#8216;</code><i>value</i><code>&#8216;</code><br />
 Defines a value for the macro <i>name</i> which must be a valid C-style name, so leading alphabetic or underscore followed by zero or more alphanumerics or underscores. <i>value</i> is optional (and defaults to an empty string). There is no character escape mechanism, but either single quotes or double quotes may be used to define a <i>value</i> with special characters or embedded horizontal white space (no newlines).</p>
<dt>&bull;</p>
<dd> <code>#undef </code><i>name</i><br />
 Removes the macro definition, if any, for <i>name</i>.</p>
<dt>&bull;</p>
<dd> <code>#ifdef </code><i>name</i><br />
 &#8230;<br />
 <code>#endif</code><br />
 or<br />
 <code>#ifndef </code><i>name</i><br />
 &#8230;<br />
 <code>#endif</code><br />
 The enclosing lines will be stripped or included, depending if the macro <i>name</i> is defined or not.</p>
<dt>&bull;</p>
<dd> <code>#else</code><br />
 Within a <code>#ifdef</code> or <code>#ifndef</code> block, <code>#else</code> may be used to delimit lines to be included if the preceding &#8220;if&#8221; condition is false.</dl>
<p> Macro substitution is achieved by breaking the input stream into words separated by white space or characters that are not valid in a macro name, i.e. not alphanumeric and not underscore. Each word is checked and if it matches a macro name, the word is replaced by the macro value, otherwise the word is unchanged. </p>
<p> There is generally one output line for each input line, although the line may be empty if the text has been stripped due to the handling of comments or conditional directives. When there is a change in the input stream, an additional output line is generated of the form: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> # lineno &quot;filename&quot; </p>
<p> to indicate the <i>following</i> line of output corresponds to line number <i>lineno</i> of the input file <i>filename</i>. </p>
<p> The <code>-P</code> argument suppresses the generation of these linemarker lines. </p>
<p> The <code>-s</code> argument changes the expected input style from C-like to shell-like (where # is a comment prefix). This forces the following changes in <code>pmcpp</code> behaviour:</p>
<dl>
<dt>&bull;</p>
<dd> The control prefix character changes from <code>#</code> to <code>%</code>, so <code>%include</code> for example.</p>
<dt>&bull;</p>
<dd> No comment stripping is performed.</dl>
<p> To provide finer control of macro expansion, the <code>-r</code> option restricts macro substitution to words that match the patterns <code>#</code>name or <code>#{</code>name<code>}</code> or if <code>-s</code> is specified, then <code>%</code>name or <code>%{</code>name<code>}</code>. In this mode, the macro <i>name</i> alone in the input stream will never be expanded, however in control lines (like <code>#ifdef</code>) the macro <i>name</i> should appear alone with out the prefix character or the curly braces (refer to the EXAMPLES below). </p>
<p> Important <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) features that are <code>not</code> supported by <code>pmcpp</code> include:</p>
<dl>
<dt>&bull;</p>
<dd> Macros with parameters &#8211; the <code>pmcpp</code> macros support only parameterless string substitution.</p>
<dt>&bull;</p>
<dd> <code>#if </code><i>expr</i><br />
 &#8230;<br />
 <code>#endif</code></p>
<dt>&bull;</p>
<dd> Nested use of <code>#ifdef</code> or <code>#ifndef</code>.</p>
<dt>&bull;</p>
<dd> Stripping C++ style comments, as in // comment.</p>
<dt>&bull;</p>
<dd> Error recovery &#8211; the first error encountered by <code>pmcpp</code> will be fatal.</p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) command line options like <code>-o</code>, <code>-W</code>, <code>-U</code>, and <code>-x</code>.</dl>
<h2>EXAMPLES</h2>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Command: <code>pmcpp</code></td>
<td ALIGN=right COLSPAN=2>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Input</code></td>
<td><code>Output</code></td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># 1 &quot;&lt;stdin&gt;&quot;</td>
</tr>
<tr VALIGN=top>
<td>#define MYDOMAIN 27</td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
</tr>
<tr VALIGN=top>
<td>root {</td>
<td>root {</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MYDOMAIN:0:0</td>
<td> foo 27:0:0</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>}</td>
</tr>
</table>
</table>
<p> For the following examples, the file <i>frequencies</i> contains the lines: </p>
<pre>
%define dk_freq 1minute
%define cpu_freq '15 sec'
</pre>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Command: <code>pmcpp -rs</code></td>
<td ALIGN=right COLSPAN=2>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Input</code></td>
<td><code>Output</code></td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td># get logging frequencies</td>
<td># get logging frequencies</td>
</tr>
<tr VALIGN=top>
<td># e.g. dk_freq macro</td>
<td># e.g. dk_freq macro</td>
</tr>
<tr VALIGN=top>
<td>%include &quot;frequencies&quot;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
</tr>
<tr VALIGN=top>
<td>log mandatory on %dk_freq {</td>
<td>log mandatory on 1minute {</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disk.dev</td>
<td> disk.dev</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>}</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
</tr>
<tr VALIGN=top>
<td># note no % for want_cpu here</td>
<td># note no % for want_cpu here</td>
</tr>
<tr VALIGN=top>
<td>%ifdef want_cpu</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>%define cpu_pfx &#8216;kernel.all.cpu.&#8217;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>log mandatory on %cpu_freq {</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%{cpu_pfx}user</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%{cpu_pfx}sys</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>%endif</td>
<td></td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Command: <code>pmcpp -rs -Dwant_cpu</code></td>
<td ALIGN=right COLSPAN=2>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Input</code></td>
<td><code>Output</code></td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td># get logging frequencies</td>
<td># get logging frequencies</td>
</tr>
<tr VALIGN=top>
<td># e.g. dk_freq macro</td>
<td># e.g. dk_freq macro</td>
</tr>
<tr VALIGN=top>
<td>%include &quot;frequencies&quot;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
</tr>
<tr VALIGN=top>
<td>log mandatory on %dk_freq {</td>
<td>log mandatory on 1minute {</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disk.dev</td>
<td> disk.dev</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>}</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
</tr>
<tr VALIGN=top>
<td># note no % for want_cpu here</td>
<td># note no % for want_cpu here</td>
</tr>
<tr VALIGN=top>
<td>%ifdef want_cpu</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>%define cpu_pfx &#8216;kernel.all.cpu.&#8217;</td>
<td></td>
</tr>
<tr VALIGN=top>
<td>log mandatory on %cpu_freq {</td>
<td>log mandatory on 15 sec {</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%{cpu_pfx}user</td>
<td> kernel.all.cpu.user</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%{cpu_pfx}sys</td>
<td> kernel.all.cpu.sys</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>}</td>
</tr>
<tr VALIGN=top>
<td>%endif</td>
<td></td>
</tr>
</table>
</table>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
