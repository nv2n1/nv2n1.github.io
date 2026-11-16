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
<dt><code>-Ca</code>, <code>&#8211;align</code></dt>
<dd> trade off larger tables for better memory alignment</dd>
<dt><code>-Ce</code>, <code>&#8211;ecs</code></dt>
<dd> construct equivalence classes</dd>
<dt><code>-Cf</code></dt>
<dd> do not compress tables; use <code>-f</code> representation</dd>
<dt><code>-CF</code></dt>
<dd> do not compress tables; use <code>-F</code> representation</dd>
<dt><code>-Cm</code>, <code>&#8211;meta-ecs</code></dt>
<dd> construct meta-equivalence classes</dd>
<dt><code>-Cr</code>, <code>&#8211;read</code></dt>
<dd> use read() instead of stdio for scanner input</dd>
<dt><code>-f</code>, <code>&#8211;full</code></dt>
<dd> generate fast, large scanner. Same as <code>-Cfr</code></dd>
<dt><code>-F</code>, <code>&#8211;fast</code></dt>
<dd> use alternate table representation. Same as <code>-CFr</code></dd>
<dt><code>-Cem</code></dt>
<dd> default compression (same as <code>&#8211;ecs</code> <code>&#8211;meta-ecs</code>)</dd></dl>
<h3>Debugging:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> enable debug mode in scanner</dd>
<dt><code>-b</code>, <code>&#8211;backup</code></dt>
<dd> write backing-up information to lex.backup</dd>
<dt><code>-p</code>, <code>&#8211;perf-report</code></dt>
<dd> write performance report to stderr</dd>
<dt><code>-s</code>, <code>&#8211;nodefault</code></dt>
<dd> suppress default rule to ECHO unmatched text</dd>
<dt><code>-T</code>, <code>&#8211;trace</code></dt>
<dd> flex should run in trace mode</dd>
<dt><code>-w</code>, <code>&#8211;nowarn</code></dt>
<dd> do not generate warnings</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> write summary of scanner statistics to stdout</dd></dl>
<h3>Files:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;outfile</code>=<i>FILE</i></dt>
<dd> specify output filename</dd>
<dt><code>-S</code>, <code>&#8211;skel</code>=<i>FILE</i></dt>
<dd> specify skeleton file</dd>
<dt><code>-t</code>, <code>&#8211;stdout</code></dt>
<dd> write scanner on stdout instead of lex.yy.c</dd>
<dt><code>&#8211;yyclass</code>=<i>NAME</i></dt>
<dd> name of C++ class</dd>
<dt><code>&#8211;header-file</code>=<i>FILE</i></dt>
<dd> create a C header file in addition to the scanner</dd>
<dt> <code>&#8211;tables-file</code>[=<i>FILE</i>] write tables to FILE</dt></dl>
<h3>Scanner behavior:</h3>
<dl>
<dt><code>-7</code>, <code>&#8211;7bit</code></dt>
<dd>
</dd><dd>generate 7-bit scanner</dd>
<dt><code>-8</code>, <code>&#8211;8bit</code></dt>
<dd> generate 8-bit scanner</dd>
<dt><code>-B</code>, <code>&#8211;batch</code></dt>
<dd> generate batch scanner (opposite of <code>-I</code>)</dd>
<dt><code>-i</code>, <code>&#8211;case-insensitive</code></dt>
<dd> ignore case in patterns</dd>
<dt><code>-l</code>, <code>&#8211;lex-compat</code></dt>
<dd> maximal compatibility with original lex</dd>
<dt><code>-X</code>, <code>&#8211;posix-compat</code></dt>
<dd> maximal compatibility with POSIX lex</dd>
<dt><code>-I</code>, <code>&#8211;interactive</code></dt>
<dd> generate interactive scanner (opposite of <code>-B</code>)</dd>
<dt><code>&#8211;yylineno</code></dt>
<dd> track line count in yylineno</dd></dl>
<h3>Generated code:</h3>
<dl>
<dt>-+, <code>&#8211;c</code>++</dt>
<dd> generate C++ scanner class</dd>
<dt><code>-Dmacro</code>[=<i>defn</i>]</dt>
<dd> #define macro defn (default defn is &#8216;1&#8217;)</dd>
<dt><code>-L</code>, <code>&#8211;noline</code></dt>
<dd> suppress #line directives in scanner</dd>
<dt><code>-P</code>, <code>&#8211;prefix</code>=<i>STRING</i></dt>
<dd> use STRING as prefix instead of &quot;yy&quot;</dd>
<dt><code>-R</code>, <code>&#8211;reentrant</code></dt>
<dd> generate a reentrant C scanner</dd>
<dt><code>&#8211;bison-bridge</code></dt>
<dd> scanner for bison pure parser.</dd>
<dt><code>&#8211;bison-locations</code></dt>
<dd> include yylloc support.</dd>
<dt><code>&#8211;stdinit</code></dt>
<dd> initialize yyin/yyout to stdin/stdout</dd>
<dt> <code>&#8211;noansi-definitions</code> old-style function definitions</dt>
<dt><code>&#8211;noansi-prototypes</code></dt>
<dd>
</dd><dd>empty parameter list in prototypes</dd>
<dt><code>&#8211;nounistd</code></dt>
<dd> do not include &lt;unistd.h&gt;</dd>
<dt><code>&#8211;noFUNCTION</code></dt>
<dd> do not generate a particular FUNCTION</dd></dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-c</code></dt>
<dd> do-nothing POSIX option</dd>
<dt><code>-n</code></dt>
<dd> do-nothing POSIX option</dd>
<dt> -?</dt>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
</dd><dd>produce this help message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> report flex version</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>flex</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>flex</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info flex</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
