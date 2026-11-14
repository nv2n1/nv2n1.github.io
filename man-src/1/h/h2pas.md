---
title: "h2pas(1)"
name: "h2pas"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h2pas/"
description: "h2pas – The C header to pascal unit conversion program."
---

<h2>NAME</h2>
<p> h2pas &#8211; The C header to pascal unit conversion program. </p>
<h2>SYNOPSIS</h2>
<p> <code>h2pas</code> <i>[options] filename</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>h2pas</code> attempts to convert a C header file to a pascal unit. it can handle most C constructs that one finds in a C header file, and attempts to translate them to their pascal counterparts. see the <code>CONSTRUCTS</code> section for a full description of what the translator can handle. </p>
<h2>USAGE</h2>
<p> H2pas is a command-line tool that translates a C header file to a spascal unit. It reads the C header file and translates the C declarations to equivalent pascal declarations that can be used to access code written in C. </p>
<p> The output of the h2pas program is written to a file with the same name as the C header file that was used as input, but with the extension <i>.pp</i>. The output file that h2pas creates can be customized in a number of ways by means of many options. </p>
<h2>OPTIONS</h2>
<p> The output of <code>h2pas</code> can be controlled with the following options: </p>
<dl>
<dt><code>-d </code></p>
<dd> use <i>external;</i> for all procedure and function declarations.</p>
<dt><code>-D </code></p>
<dd> use <code>external</code> <i>libname </i> <code>name</code> <i>&#8216;func_name&#8217;</i> for function and procedure declarations.</p>
<dt><code>-e </code></p>
<dd> Emit a series of constants instead of an enumeration type for the C <i>enum</i> construct.</p>
<dt><code>-i</code></p>
<dd> create an include file instead of a unit (omits the unit header).</p>
<dt><code>-l</code><i> libname</i></p>
<dd> specify the library name for external function declarations.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> Specify the output file name. Default is the input file name with the extension replaced by <i>.pp</i> &quot;.&quot;</p>
<dt><code>-p</code></p>
<dd> use the letter <code>P</code> in front of pointer type parameters instead of &quot;^&quot;.</p>
<dt><code>-s</code></p>
<dd> Strip comments from the input file. By default comments are converted to comments, but they may be displaced, since a comment is handled by the scanner.</p>
<dt><code>-t</code></p>
<dd> prepend typedef type names with the letter <code>T</code> (used to follow Borland&#8217;s convention that all types should be defined with T).</p>
<dt><code>-v</code></p>
<dd> replace pointer parameters by call by reference parameters. Use with care because some calls can expect a NIL pointer.</p>
<dt><code>-w</code></p>
<dd> Header file is a win32 header file (adds support for some special macros).</p>
<dt><code>-x</code></p>
<dd> handle SYS_TRAP of the PalmOS header files. </p>
</dl>
<h2>CONSTRUCTS</h2>
<p> The following C declarations and statements are recognized: </p>
<dl>
<dt><code>defines</code></p>
<dd> defines are changed into pascal constants if they are simple defines. macros are changed &#8211; wherever possible to functions; however the arguments are all integers, so these must be changed manually. Simple expressions in define staments are recognized, as are most arithmetic operators: addition, substraction, multiplication, division, logical operators, comparision operators, shift operators. The C construct ( A ? B : C) is also recognized and translated to a pascal construct with an IF statement (this is buggy, however). </p>
<dt><code>preprocessor statements</code></p>
<dd> the conditional preprocessing commands are recognized and translated into equivalent pascal compiler directives. The special <code>#ifdef __cplusplus</code> is also recognized and removed. </p>
<dt><code>typedef</code></p>
<dd> A typedef statement is changed into a pascal type statement. The following basic types are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>char</i></p>
<dd> changed to char.</p>
<dt><i>float</i></p>
<dd> changed to real (=double in free pascal).</p>
<dt><i>int</i></p>
<dd> changed to longint.</p>
<dt><i>long</i></p>
<dd> changed to longint.</p>
<dt><i>long int</i></p>
<dd> changed to longint.</p>
<dt><i>short</i></p>
<dd> changed to integer.</p>
<dt><i>unsigned</i></p>
<dd> changed to cardinal.</p>
<dt><i>unsigned char</i></p>
<dd> changed to byte.</p>
<dt><i>unsigned int</i></p>
<dd> changed to cardinal.</p>
<dt><i>unsigned long int</i></p>
<dd> changed to cardinal.</p>
<dt><i>unsigned short</i></p>
<dd> changed to word.</p>
<dt><i>void</i></p>
<dd> ignored.</dl>
</dl>
<p> These types are also changed if they appear in the arguments of a function or procedure.</p>
<dt><code>functions and procedures</code></p>
<dd> functions and procedures are translated as well; pointer types may be changed to call by reference arguments (using the <code>var</code> argument) by using the <code>-p</code> command line argument. functions that have a variable number of arguments are changed to a function with an <code>array of const</code> argument.</p>
<dt><code>specifiers</code></p>
<dd> the <i>extern</i> specifier is recognized; however it is ignored. the <i>packed</i> specifier is also recognised and changed with the <i>PACKRECORDS</i> directive. The <i>const</i> specifier is also recognized, but is ignored. </p>
<dt><code>modifiers</code></p>
<dd> If the <code>-w </code> option is specified, then the following modifiers are recognized: <i>STDCALL</i> , <i>CDECL</i> , <i>CALLBACK</i> , <i>PASCAL</i> , <i>WINAPI</i> , <i>APIENTRY</i> , <i>WINGDIAPI</i> as defined in the win32 headers. If additionally the <code>-x</code> option is specified then the <i>SYS_TRAP</i> specifier is also recognized. </p>
<dt><code>enums</code></p>
<dd> enum constructs are changed into enumeration types; bear in mind that in C enumeration types can have values assigned to them; Free Pascal also allows this to a certain degree. If you know that values are assigned to enums, it is best to use the <code>-e</code> option to change the enus to a series of integer constants. </p>
<dt><code>unions</code></p>
<dd> unions are changed to variant records. </p>
<dt><code>structs</code></p>
<dd> are changed to pascal records, with <code>C</code> packing. </p>
<dt>
<dd>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) </p>
</dl>
<h2>Index</h2>
