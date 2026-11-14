---
title: "ucpp(1)"
name: "ucpp"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ucpp/"
description: "ucpp – C preprocessor"
---

<h2>NAME</h2>
<p> ucpp &#8211; C preprocessor</p>
<h2>SYNOPSIS</h2>
<p> <code>ucpp </code> [ <i>options</i> ] [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ucpp</code> is a C preprocessor mostly compatible with ISO-C99. It is rather strict and uses only a small amount of memory. It uses standard input as primary input if no file argument is given.</p>
<h2>OPTIONS</h2>
<p> There are several classes of options.</p>
<dl>
<dt><code>Language Options</code></p>
<dd>
<dt><code>-C</code></p>
<dd> keep comments in the output.</p>
<dt><code>-s</code></p>
<dd> if a rogue &#8216;#&#8217; is encountered, do not emit an error and keep it in the output.</p>
<dt><code>-l</code></p>
<dd> supress the emission of &#8216;#line&#8217; directives in the output.</p>
<dt><code>-lg</code></p>
<dd> convert the &#8216;#line&#8217; to the gcc-style equivalent.</p>
<dt><code>-CC</code></p>
<dd> disable C++-like comments (a &#8216;//&#8217; begins a comment, up to the end of the line). Use this option to get closer to C90 behaviour.</p>
<dt><code>-a, -na</code></p>
<dd> handle assertions (defined with #assert); <code>-a</code> also defines the standard assertions <i>#machine</i> , <i>#cpu</i> and <i>#system</i> (see <code>-e</code> to get the local definition of such assertions).</p>
<dt><code>-a0</code></p>
<dd> disable assertion support.</p>
<dt><code>-V</code></p>
<dd> disable support for macros with a variable number of arguments: in C99, a macro may be declared with <i>&#8230;</i> as the last argument; inside the replacement list, <i>__VA_ARGS__</i> is replaced with the optional extra arguments given in the call to the macro. Use this option to get closer to C90 behaviour.</p>
<dt><code>-u</code></p>
<dd> enable UTF-8 support: with this option, the source is considered as an ISO/10646 source, encoded in UTF-8. Characters represented as two bytes or more are considered as alphabetic characters, like letters, and therefore usable in identifiers. These characters hold the same syntactic value than the corresponding Universal Character Names.</p>
<dt><code>-X</code></p>
<dd> enable <code>-a, -u</code> and <code>-Y.</code> This should make <code>ucpp</code> behave closer to what is requested from a &quot;modern&quot; C preprocessor.</p>
<dt><code>-c90</code></p>
<dd> enable <code>-V</code> and <code>-CC,</code> and do not define <code>__STDC_VERSION__.</code> This should make <code>ucpp</code> mimic older C90 behaviour.</p>
<dt><code>-t</code></p>
<dd> disable trigraph support; this seems to be required for some legacy code.</p>
<dt><code>Warning Options</code></p>
<dd>
<dt><code>-wt</code></p>
<dd> emit a final warning when trigraphs are encountered.</p>
<dt><code>-wtt</code></p>
<dd> emit warnings for each trigraph encountered.</p>
<dt><code>-wa</code></p>
<dd> emit annoying warnings (these are usually useless).</p>
<dt><code>-w0</code></p>
<dd> supress standard warnings.</p>
<dt><code>Directory Options</code></p>
<dd>
<dt><code>-I</code><i>directory</i></p>
<dd>
<dt><code>-I </code><i>directory</i></p>
<dd> add <i>directory</i> to the include path, before the standard include path.</p>
<dt><code>-J</code><i>directory</i></p>
<dd>
<dt><code>-J </code><i>directory</i></p>
<dd> add <i>directory</i> to the include path, after the standard include path.</p>
<dt><code>-zI</code></p>
<dd> do not use the standard (compile-time) include path.</p>
<dt><code>-M</code></p>
<dd> emit only the names of encountered files, separated by spaces; this is intended for automatic generation of Makefile dependencies.</p>
<dt><code>-Ma</code></p>
<dd> do the same as <code>-M</code> but also for system files.</p>
<dt><code>-o </code><i>file</i></p>
<dd> direct the ouput to <i>file</i> instead of standard output.</p>
<dt><code>Macro Options</code></p>
<dd>
<dt><code>-D</code><i>macro</i></p>
<dd> predefine <i>macro</i> with content <code>1.</code></p>
<dt><code>-D</code><i>macro=def</i></p>
<dd> predefine <i>macro</i> with the content <i>def.</i></p>
<dt><code>-U</code><i>macro</i></p>
<dd> undefine <i>macro.</i></p>
<dt><code>-Y</code></p>
<dd> predefine system-dependant macros.</p>
<dt><code>-Z</code></p>
<dd> do not predefine special macros such as <code>__TIME__.</code></p>
<dt><code>-A</code><i>foo(bar)</i></p>
<dd> add <i>foo(bar)</i> to the list of assertions.</p>
<dt><code>-B</code><i>foo(bar)</i></p>
<dd> remove <i>foo(bar)</i> of the list of assertions; you may also use <code>-B</code><i>foo</i> to remove all <code>-B</code><i>foo(xxx)</i> from the list of assertions.</p>
<dt><code>-d</code></p>
<dd> instead of normal output, emit &#8216;#define&#8217; directives representing all macros defined during processing.</p>
<dt><code>-e</code></p>
<dd> instead of normal output, emit &#8216;#assert&#8217; directives representing all assertions defined during processing.</p>
<dt><code>Miscellaneous Options</code></p>
<dd>
<dt><code>-v</code></p>
<dd> print version number, include path and (optionaly) defined assertions.</p>
<dt><code>-h</code></p>
<dd> print some help.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>ucpp</code> is not itself affected by environment variables. However, it uses library functions that might be affected, depending on the system.</p>
<h2>AUTHOR</h2>
<p> Thomas Pornin &lt;pornin [at] bolet.org&gt;</p>
<h2>BUGS</h2>
<p> <code>ucpp</code> is considered stable software. However improbable it is, please report bugs to the author (possibly with a file that exhibits the problem) if the latest version, available from this site:</p>
<dl>
<dt><a rel="nofollow" href="http://pornin.nerim.net/ucpp/">http://pornin.nerim.net/ucpp/</a></p>
<dd></dl>
<p> has the bug. </p>
<h2>Index</h2>
