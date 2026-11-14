---
title: "plex(1)"
name: "plex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plex/"
---

<h2>NAME</h2>

 plex - The Pascal Lex lexical analyzer generator. 

 

<h2>USAGE</h2>

 

 <b>lex [options] lex-file[.l] [output-file[.pas]]</b> 

 

<h2>OPTIONS</h2>

 

<dl>
<dt><b>-v</b>
<dd> <i>Verbose:</i> Lex generates a readable description of the generated lexical analyzer, written to lex-file with new extension <i>.lst</i>
<dt><b>-o </b>
<dd> <i>Optimize:</i> Lex optimizes DFA tables to produce a minimal DFA. 

</dl>

<h2>DESCRIPTION</h2>

 

 TP Lex is a program generator that is used to generate the Turbo Pascal source code for a lexical analyzer subroutine from the specification of an input language by a regular expression grammar. 

 TP Lex parses the source grammar contained in lex-file (with default suffix output-file (with default suffix .pas); if no output file is specified, output goes to lex-file with new suffix .pas. If any errors are found during compilation, error messages are written to the list file (lex-file with new suffix .lst). 

 The generated output file contains a lexical analyzer routine, yylex, implemented as: 

<dl>
<dt>
<dd> 
&nbsp;<wbr>&nbsp;<wbr>function yylex : Integer;</dl>
 

 This routine has to be called by your main program to execute the lexical analyzer. The return value of the yylex routine usually denotes the number of a token recognized by the lexical analyzer (see the return routine in the LexLib unit). At end-of-file the yylex routine normally returns 0. 

 The code template for the yylex routine may be found in the yylex.cod file. This file is needed by TP Lex when it constructs the output file. It must be present either in the current directory or in the directory from which TP Lex was executed (TP Lex searches these directories in the indicated order). (NB: For the Linux/Free Pascal version, the code template is searched in some directory defined at compile-time instead of the execution path, usually /usr/lib/fpc/lexyacc.) 

 The TP Lex library (LexLib) unit is required by programs using Lex-generated lexical analyzers; you will therefore have to put an appropriate uses clause into your program or unit that contains the lexical analyzer routine. The LexLib unit also provides various useful utility routines; see the file lexlib.pas for further information. 

 

<h2>MORE INFORMATION</h2>

 

 For more information, see the documentation that comes with TP lex and yacc. 

<h2>AUTHOR</h2>

 Albert Graeff (&lt;ag [at] muwiinfa.geschichte.uni-mainz.de&gt;, &lt;Dr.Graef [at] t-online.de&gt;) 

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-ppc386/">ppc386</a></b>(1) <b><a HREF="/docs/linux/man/1-pyacc/">pyacc</a></b>(1) 

<h2>Index</h2>


