---
title: "bison(1)"
name: "bison"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bison/"
description: "bison – GNU Project parser generator (yacc replacement)"
---

<h2>NAME</h2>
<p> bison &#8211; GNU Project parser generator (yacc replacement)</p>
<h2>SYNOPSIS</h2>
<p> <code>bison</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Bison</i> is a parser generator in the style of <i><a href="/docs/linux/man/1-yacc/">yacc</a></i>(1). It should be upwardly compatible with input files designed for <i>yacc</i>. </p>
<p> Input files should follow the <i>yacc</i> convention of ending in <code>.y</code>. Unlike <i>yacc</i>, the generated files do not have fixed names, but instead use the prefix of the input file. Moreover, if you need to put <i>C++</i> code in the input file, you can end his name by a C++-like extension (.ypp or .y++), then bison will follow your extension to name the output file (.cpp or .c++). For instance, a grammar description file named <code>parse.yxx</code> would produce the generated parser in a file named <code>parse.tab.cxx</code>, instead of <i>yacc</i>&#8216;s <code>y.tab.c</code> or old <i>Bison</i> version&#8217;s <code>parse.tab.c</code>. </p>
<p> This description of the options that can be given to <i>bison</i> is adapted from the node <code>Invocation</code> in the <code>bison.texi</code> manual, which should be taken as authoritative. </p>
<p> <i>Bison</i> supports both traditional single-letter options and mnemonic long option names. Long option names are indicated with <code>&#8212;</code> instead of <code>&#8211;</code>. Abbreviations for option names are allowed as long as they are unique. When a long option takes an argument, like <code>&#8211;file-prefix</code>, connect the option name and the argument with <code>=</code>. </p>
<p> Generate a deterministic LR or generalized LR (GLR) parser employing LALR(1), IELR(1), or canonical LR(1) parser tables. IELR(1) and canonical LR(1) support is experimental. </p>
<p> Mandatory arguments to long options are mandatory for short options too. The same is true for optional arguments.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>&#8211;print-localedir</code></dt>
<dd> output directory containing locale-dependent data</dd>
<dt><code>&#8211;print-datadir</code></dt>
<dd> output directory containing skeletons and XSLT</dd>
<dt><code>-y</code>, <code>&#8211;yacc</code></dt>
<dd> emulate POSIX Yacc</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>[=<i>,CATEGORY/</i>]</dt>
<dd> report the warnings falling in CATEGORY</dd>
<dt><code>-f</code>, <code>&#8211;feature</code>[=<i>,FEATURE/</i>]</dt>
<dd> activate miscellaneous features</dd></dl>
<h3>Parser:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;language</code>=<i>,LANGUAGE/</i></dt>
<dd> specify the output programming language</dd>
<dt><code>-S</code>, <code>&#8211;skeleton</code>=<i>,FILE/</i></dt>
<dd> specify the skeleton to use</dd>
<dt><code>-t</code>, <code>&#8211;debug</code></dt>
<dd> instrument the parser for tracing same as &#8216;-Dparse.trace&#8217;</dd>
<dt><code>&#8211;locations</code></dt>
<dd> enable location support</dd>
<dt><code>-D</code>, <code>&#8211;define=NAME</code>[=<i>,VALUE/</i>]</dt>
<dd> similar to &#8216;%define NAME &quot;VALUE&quot;&#8217;</dd>
<dt><code>-F</code>, <code>&#8211;force-define=NAME</code>[=<i>,VALUE/</i>]</dt>
<dd> override &#8216;%define NAME &quot;VALUE&quot;&#8217;</dd>
<dt><code>-p</code>, <code>&#8211;name-prefix</code>=<i>,PREFIX/</i></dt>
<dd> prepend PREFIX to the external symbols deprecated by &#8216;-Dapi.prefix=PREFIX&#8217;</dd>
<dt><code>-l</code>, <code>&#8211;no-lines</code></dt>
<dd> don&#8217;t generate &#8216;#line&#8217; directives</dd>
<dt><code>-k</code>, <code>&#8211;token-table</code></dt>
<dd> include a table of token names</dd></dl>
<h3>Output:</h3>
<dl>
<dt><code>&#8211;defines</code>[=<i>,FILE/</i>]</dt>
<dd> also produce a header file</dd>
<dt><code>-d</code></dt>
<dd> likewise but cannot specify FILE (for POSIX Yacc)</dd>
<dt><code>-r</code>, <code>&#8211;report</code>=<i>,THINGS/</i></dt>
<dd> also produce details on the automaton</dd>
<dt><code>&#8211;report-file</code>=<i>,FILE/</i></dt>
<dd> write report to FILE</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> same as &#8216;&#8211;report=state&#8217;</dd>
<dt><code>-b</code>, <code>&#8211;file-prefix</code>=<i>,PREFIX/</i></dt>
<dd> specify a PREFIX for output files</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> leave output to FILE</dd>
<dt><code>-g</code>, <code>&#8211;graph</code>[=<i>,FILE/</i>]</dt>
<dd> also output a graph of the automaton</dd>
<dt><code>-x</code>, <code>&#8211;xml</code>[=<i>,FILE/</i>]</dt>
<dd> also output an XML report of the automaton (the XML schema is experimental)</dd></dl>
<h3>Warning categories include:</h3>
<dl>
<dt>&#8216;midrule-values&#8217;</dt>
<dd> unset or unused midrule values</dd>
<dt>&#8216;yacc&#8217;</dt>
<dd> incompatibilities with POSIX Yacc</dd>
<dt>&#8216;conflicts-sr&#8217;</dt>
<dd> S/R conflicts (enabled by default)</dd>
<dt>&#8216;conflicts-rr&#8217;</dt>
<dd> R/R conflicts (enabled by default)</dd>
<dt>&#8216;deprecated&#8217;</dt>
<dd> obsolete constructs</dd>
<dt>&#8217;empty-rule&#8217;</dt>
<dd> empty rules without %empty</dd>
<dt>&#8216;precedence&#8217;</dt>
<dd> useless precedence and associativity</dd>
<dt>&#8216;other&#8217;</dt>
<dd> all other warnings (enabled by default)</dd>
<dt>&#8216;all&#8217;</dt>
<dd> all the warnings except &#8216;yacc&#8217;</dd>
<dt>&#8216;no-CATEGORY&#8217;</dt>
<dd> turn off warnings in CATEGORY</dd>
<dt>&#8216;none&#8217;</dt>
<dd> turn off all the warnings</dd>
<dt>&#8216;error[=CATEGORY]&#8217;</dt>
<dd> treat warnings as errors</dd></dl>
<h3>THINGS is a list of comma separated words that can include:</h3>
<dl>
<dt>&#8216;state&#8217;</dt>
<dd> describe the states</dd>
<dt>&#8216;itemset&#8217;</dt>
<dd> complete the core item sets with their closure</dd>
<dt>&#8216;lookahead&#8217;</dt>
<dd> explicitly associate lookahead tokens to items</dd>
<dt>&#8216;solved&#8217;</dt>
<dd> describe shift/reduce conflicts solving</dd>
<dt>&#8216;all&#8217;</dt>
<dd> include all the above information</dd>
<dt>&#8216;none&#8217;</dt>
<dd> disable the report</dd></dl>
<h3>FEATURE is a list of comma separated words that can include:</h3>
<dl>
<dt>&#8216;caret&#8217;</dt>
<dd> show errors with carets</dd>
<dt>&#8216;all&#8217;</dt>
<dd> all of the above</dd>
<dt>&#8216;none&#8217;</dt>
<dd> disable all of the above</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Robert Corbett and Richard Stallman.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-bison [at] gnu.org&gt;.<br />
 GNU Bison home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/bison/">http://www.gnu.org/software/bison/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;. </p>
<p> Report translation bugs to &lt;<a rel="nofollow" href="http://translationproject.org/team/">http://translationproject.org/team/</a>&gt;.<br />
 For complete documentation, run: info bison.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code>lex</code>(1), <code><a href="/docs/linux/man/1-flex/">flex</a></code>(1), <code><a href="/docs/linux/man/1-yacc/">yacc</a></code>(1). </p>
<p> The full documentation for <code>bison</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>bison</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info bison</code></dd></dl>
<p> should give you access to the complete manual. </p>
