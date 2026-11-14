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
<p> Generate a deterministic LR or generalized LR (GLR) parser employing <a href="/docs/linux/man/1-lalr/">LALR</a>(1), <a href="/docs/linux/man/1-ielr/">IELR</a>(1), or canonical <a href="/docs/linux/man/1-lr/">LR</a>(1) parser tables. <a href="/docs/linux/man/1-ielr/">IELR</a>(1) and canonical <a href="/docs/linux/man/1-lr/">LR</a>(1) support is experimental. </p>
<p> Mandatory arguments to long options are mandatory for short options too. The same is true for optional arguments.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>&#8211;print-localedir</code></p>
<dd> output directory containing locale-dependent data</p>
<dt><code>&#8211;print-datadir</code></p>
<dd> output directory containing skeletons and XSLT</p>
<dt><code>-y</code>, <code>&#8211;yacc</code></p>
<dd> emulate POSIX Yacc</p>
<dt><code>-W</code>, <code>&#8211;warnings</code>[=<i>,CATEGORY/</i>]</p>
<dd> report the warnings falling in CATEGORY</p>
<dt><code>-f</code>, <code>&#8211;feature</code>[=<i>,FEATURE/</i>]</p>
<dd> activate miscellaneous features</dl>
<h3>Parser:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;language</code>=<i>,LANGUAGE/</i></p>
<dd> specify the output programming language</p>
<dt><code>-S</code>, <code>&#8211;skeleton</code>=<i>,FILE/</i></p>
<dd> specify the skeleton to use</p>
<dt><code>-t</code>, <code>&#8211;debug</code></p>
<dd> instrument the parser for tracing same as &#8216;-Dparse.trace&#8217;</p>
<dt><code>&#8211;locations</code></p>
<dd> enable location support</p>
<dt><code>-D</code>, <code>&#8211;define=NAME</code>[=<i>,VALUE/</i>]</p>
<dd> similar to &#8216;%define NAME &quot;VALUE&quot;&#8217;</p>
<dt><code>-F</code>, <code>&#8211;force-define=NAME</code>[=<i>,VALUE/</i>]</p>
<dd> override &#8216;%define NAME &quot;VALUE&quot;&#8217;</p>
<dt><code>-p</code>, <code>&#8211;name-prefix</code>=<i>,PREFIX/</i></p>
<dd> prepend PREFIX to the external symbols deprecated by &#8216;-Dapi.prefix=PREFIX&#8217;</p>
<dt><code>-l</code>, <code>&#8211;no-lines</code></p>
<dd> don&#8217;t generate &#8216;#line&#8217; directives</p>
<dt><code>-k</code>, <code>&#8211;token-table</code></p>
<dd> include a table of token names</dl>
<h3>Output:</h3>
<dl>
<dt><code>&#8211;defines</code>[=<i>,FILE/</i>]</p>
<dd> also produce a header file</p>
<dt><code>-d</code></p>
<dd> likewise but cannot specify FILE (for POSIX Yacc)</p>
<dt><code>-r</code>, <code>&#8211;report</code>=<i>,THINGS/</i></p>
<dd> also produce details on the automaton</p>
<dt><code>&#8211;report-file</code>=<i>,FILE/</i></p>
<dd> write report to FILE</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> same as &#8216;&#8211;report=state&#8217;</p>
<dt><code>-b</code>, <code>&#8211;file-prefix</code>=<i>,PREFIX/</i></p>
<dd> specify a PREFIX for output files</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> leave output to FILE</p>
<dt><code>-g</code>, <code>&#8211;graph</code>[=<i>,FILE/</i>]</p>
<dd> also output a graph of the automaton</p>
<dt><code>-x</code>, <code>&#8211;xml</code>[=<i>,FILE/</i>]</p>
<dd> also output an XML report of the automaton (the XML schema is experimental)</dl>
<h3>Warning categories include:</h3>
<dl>
<dt>&#8216;midrule-values&#8217;</p>
<dd> unset or unused midrule values</p>
<dt>&#8216;yacc&#8217;</p>
<dd> incompatibilities with POSIX Yacc</p>
<dt>&#8216;conflicts-sr&#8217;</p>
<dd> S/R conflicts (enabled by default)</p>
<dt>&#8216;conflicts-rr&#8217;</p>
<dd> R/R conflicts (enabled by default)</p>
<dt>&#8216;deprecated&#8217;</p>
<dd> obsolete constructs</p>
<dt>&#8217;empty-rule&#8217;</p>
<dd> empty rules without %empty</p>
<dt>&#8216;precedence&#8217;</p>
<dd> useless precedence and associativity</p>
<dt>&#8216;other&#8217;</p>
<dd> all other warnings (enabled by default)</p>
<dt>&#8216;all&#8217;</p>
<dd> all the warnings except &#8216;yacc&#8217;</p>
<dt>&#8216;no-CATEGORY&#8217;</p>
<dd> turn off warnings in CATEGORY</p>
<dt>&#8216;none&#8217;</p>
<dd> turn off all the warnings</p>
<dt>&#8216;error[=CATEGORY]&#8217;</p>
<dd> treat warnings as errors</dl>
<h3>THINGS is a list of comma separated words that can include:</h3>
<dl>
<dt>&#8216;state&#8217;</p>
<dd> describe the states</p>
<dt>&#8216;itemset&#8217;</p>
<dd> complete the core item sets with their closure</p>
<dt>&#8216;lookahead&#8217;</p>
<dd> explicitly associate lookahead tokens to items</p>
<dt>&#8216;solved&#8217;</p>
<dd> describe shift/reduce conflicts solving</p>
<dt>&#8216;all&#8217;</p>
<dd> include all the above information</p>
<dt>&#8216;none&#8217;</p>
<dd> disable the report</dl>
<h3>FEATURE is a list of comma separated words that can include:</h3>
<dl>
<dt>&#8216;caret&#8217;</p>
<dd> show errors with carets</p>
<dt>&#8216;all&#8217;</p>
<dd> all of the above</p>
<dt>&#8216;none&#8217;</p>
<dd> disable all of the above</dl>
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
<p> <code><a href="/docs/linux/man/1-lex/">lex</a></code>(1), <code><a href="/docs/linux/man/1-flex/">flex</a></code>(1), <code><a href="/docs/linux/man/1-yacc/">yacc</a></code>(1). </p>
<p> The full documentation for <code>bison</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>bison</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info bison</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
