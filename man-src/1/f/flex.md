---
title: "flex(1)"
name: "flex"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flex/"
description: "flex – the fast lexical analyser generator"
---

<h2>NAME</h2>
<p> flex &#8211; the fast lexical analyser generator</p>
<h2>SYNOPSIS</h2>
<p> <code>flex</code> [<i>OPTIONS</i>] [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Generates programs that perform pattern-matching on text.</p>
<h3>Table Compression:</h3>
<dl>
<dt><code>-Ca</code>, <code>&#8211;align</code></p>
<dd> trade off larger tables for better memory alignment</p>
<dt><code>-Ce</code>, <code>&#8211;ecs</code></p>
<dd> construct equivalence classes</p>
<dt><code>-Cf</code></p>
<dd> do not compress tables; use <code>-f</code> representation</p>
<dt><code>-CF</code></p>
<dd> do not compress tables; use <code>-F</code> representation</p>
<dt><code>-Cm</code>, <code>&#8211;meta-ecs</code></p>
<dd> construct meta-equivalence classes</p>
<dt><code>-Cr</code>, <code>&#8211;read</code></p>
<dd> use read() instead of stdio for scanner input</p>
<dt><code>-f</code>, <code>&#8211;full</code></p>
<dd> generate fast, large scanner. Same as <code>-Cfr</code></p>
<dt><code>-F</code>, <code>&#8211;fast</code></p>
<dd> use alternate table representation. Same as <code>-CFr</code></p>
<dt><code>-Cem</code></p>
<dd> default compression (same as <code>&#8211;ecs</code> <code>&#8211;meta-ecs</code>)</dl>
<h3>Debugging:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> enable debug mode in scanner</p>
<dt><code>-b</code>, <code>&#8211;backup</code></p>
<dd> write backing-up information to lex.backup</p>
<dt><code>-p</code>, <code>&#8211;perf-report</code></p>
<dd> write performance report to stderr</p>
<dt><code>-s</code>, <code>&#8211;nodefault</code></p>
<dd> suppress default rule to ECHO unmatched text</p>
<dt><code>-T</code>, <code>&#8211;trace</code></p>
<dd> flex should run in trace mode</p>
<dt><code>-w</code>, <code>&#8211;nowarn</code></p>
<dd> do not generate warnings</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> write summary of scanner statistics to stdout</dl>
<h3>Files:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;outfile</code>=<i>FILE</i></p>
<dd> specify output filename</p>
<dt><code>-S</code>, <code>&#8211;skel</code>=<i>FILE</i></p>
<dd> specify skeleton file</p>
<dt><code>-t</code>, <code>&#8211;stdout</code></p>
<dd> write scanner on stdout instead of lex.yy.c</p>
<dt><code>&#8211;yyclass</code>=<i>NAME</i></p>
<dd> name of C++ class</p>
<dt><code>&#8211;header-file</code>=<i>FILE</i></p>
<dd> create a C header file in addition to the scanner</p>
<dt> <code>&#8211;tables-file</code>[=<i>FILE</i>] write tables to FILE</dl>
<h3>Scanner behavior:</h3>
<dl>
<dt><code>-7</code>, <code>&#8211;7bit</code></p>
<dd>
<dd>generate 7-bit scanner</p>
<dt><code>-8</code>, <code>&#8211;8bit</code></p>
<dd> generate 8-bit scanner</p>
<dt><code>-B</code>, <code>&#8211;batch</code></p>
<dd> generate batch scanner (opposite of <code>-I</code>)</p>
<dt><code>-i</code>, <code>&#8211;case-insensitive</code></p>
<dd> ignore case in patterns</p>
<dt><code>-l</code>, <code>&#8211;lex-compat</code></p>
<dd> maximal compatibility with original lex</p>
<dt><code>-X</code>, <code>&#8211;posix-compat</code></p>
<dd> maximal compatibility with POSIX lex</p>
<dt><code>-I</code>, <code>&#8211;interactive</code></p>
<dd> generate interactive scanner (opposite of <code>-B</code>)</p>
<dt><code>&#8211;yylineno</code></p>
<dd> track line count in yylineno</dl>
<h3>Generated code:</h3>
<dl>
<dt>-+, <code>&#8211;c</code>++</p>
<dd> generate C++ scanner class</p>
<dt><code>-Dmacro</code>[=<i>defn</i>]</p>
<dd> #define macro defn (default defn is &#8216;1&#8217;)</p>
<dt><code>-L</code>, <code>&#8211;noline</code></p>
<dd> suppress #line directives in scanner</p>
<dt><code>-P</code>, <code>&#8211;prefix</code>=<i>STRING</i></p>
<dd> use STRING as prefix instead of &quot;yy&quot;</p>
<dt><code>-R</code>, <code>&#8211;reentrant</code></p>
<dd> generate a reentrant C scanner</p>
<dt><code>&#8211;bison-bridge</code></p>
<dd> scanner for bison pure parser.</p>
<dt><code>&#8211;bison-locations</code></p>
<dd> include yylloc support.</p>
<dt><code>&#8211;stdinit</code></p>
<dd> initialize yyin/yyout to stdin/stdout</p>
<dt> <code>&#8211;noansi-definitions</code> old-style function definitions</p>
<dt><code>&#8211;noansi-prototypes</code></p>
<dd>
<dd>empty parameter list in prototypes</p>
<dt><code>&#8211;nounistd</code></p>
<dd> do not include &lt;unistd.h&gt;</p>
<dt><code>&#8211;noFUNCTION</code></p>
<dd> do not generate a particular FUNCTION</dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-c</code></p>
<dd> do-nothing POSIX option</p>
<dt><code>-n</code></p>
<dd> do-nothing POSIX option</p>
<dt> -?</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
<dd>produce this help message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> report flex version</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>flex</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>flex</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info flex</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
