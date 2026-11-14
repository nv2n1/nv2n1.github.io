---
title: "pyacc(1)"
name: "pyacc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pyacc/"
description: "pyacc – Pascal Yacc compiler compiler."
---

<h2>NAME</h2>
<p> pyacc &#8211; Pascal Yacc compiler compiler. </p>
<h2>USAGE</h2>
<p> <code>yacc [options] yacc-file[.y] [output-file[.pas]]</code> </p>
<p> SH OPTIONS </p>
<dl>
<dt><code>-v</code></p>
<dd> <i>Verbose:</i> Pascal Yacc generates a readable description of the generated parser, written to yacc-file with new extension <i>.lst.</i></p>
<dt><code>-d</code></p>
<dd> <i>Debug:</i> TP Yacc generates a parser with debugging output. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>TP Yacc</code> is a program that lets you prepare parsers from the description of input languages by BNF-like grammars. You simply specify the grammar for your target language, augmented with the Turbo Pascal code necessary to process the syntactic constructs, and TP Yacc translates your grammar into the Turbo Pascal code for a corresponding parser subroutine named yyparse. </p>
<p> TP Yacc parses the source grammar contained in yacc-file (with default suffix .y) and writes the constructed parser subroutine to the specified output-file (with default suffix .pas); if no output file is specified, output goes to yacc-file with new suffix .pas. If any errors are found during compilation, error messages are written to the list file (yacc-file with new suffix .lst). </p>
<p> The generated parser routine, yyparse, is declared as: </p>
<p>function yyparse : Integer; </p>
<p> This routine may be called by your main program to execute the parser. The return value of the yyparse routine denotes success or failure of the parser (possible return values: 0 = success, 1 = unrecoverable syntax error or parse stack overflow). </p>
<p> Similar to TP Lex, the code template for the yyparse routine may be found in the yyparse.cod file. The rules for locating this file are analogous to those of TP Lex (see Section `TP Lex&#8217;). </p>
<p> The TP Yacc library (YaccLib) unit is required by programs using Yacc- generated parsers; you will therefore have to put an appropriate uses clause into your program or unit that contains the parser routine. The YaccLib unit also provides some routines which may be used to control the actions of the parser. See the file yacclib.pas for further information. </p>
<h2>More information</h2>
<p> For more information, see the documentation that comes with TP lex and yacc. </p>
<h2>AUTHOR</h2>
<p> Albert Graeff (&lt;ag [at] muwiinfa.geschichte.uni-mainz.de&gt;, &lt;Dr.Graef [at] t-online.de&gt;) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-plex/">plex</a></code>(1) </p>
<h2>Index</h2>
