---
title: "antlr3-_builddir_build_build_antlr-3(3)"
name: "antlr3-_builddir_build_build_antlr-3"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-_builddir_build_build_antlr-3/"
description: "src/ Directory Reference –"
---

<p>src/ Directory Reference &#8211; </p>
<h2>Synopsis</h2>
<h3>Files</h3>
<p>file <code>antlr3baserecognizer.c</code> </p>
<p> <i>Contains the base functions that all recognizers require. </i><br />
 file <code>antlr3basetree.c</code> </p>
<p> file <code>antlr3basetreeadaptor.c</code> </p>
<p> <i>Contains the base functions that all tree adaptors start with. </i><br />
 file <code>antlr3bitset.c</code> </p>
<p> <i>Contains the C implementation of ANTLR3 bitsets as adapted from Terence Parr&#8217;s Java implementation. </i><br />
 file <code>antlr3collections.c</code> </p>
<p> <i>Provides a number of useful functions that are roughly equivalent to java HashTable and List for the purposes of Antlr 3 C runtime. </i><br />
 file <code>antlr3commontoken.c</code> </p>
<p> file <code>antlr3commontree.c</code> </p>
<p> file <code>antlr3commontreeadaptor.c</code> </p>
<p> <i>This is the standard tree adaptor used by the C runtime unless the grammar source file says to use anything different. </i><br />
 file <code>antlr3commontreenodestream.c</code> </p>
<p> <i>Defines the implementation of the common node stream the default tree node stream used by ANTLR. </i><br />
 file <code>antlr3convertutf.c</code> </p>
<p> file <code>antlr3cyclicdfa.c</code> </p>
<p> file <code>antlr3debughandlers.c</code> </p>
<p> <i>Provides the debugging functions invoked by a recognizer built using the debug generator mode of the antlr tool. </i><br />
 file <code>antlr3encodings.c</code> </p>
<p> file <code>antlr3exception.c</code> </p>
<p> <i>Contains default functions for creating and destroying as well as otherwise handling ANTLR3 standard exception structures. </i><br />
 file <code>antlr3filestream.c</code> </p>
<p> <i>The ANTLR3 C filestream is used when the source character stream is a filesystem based input set and all the characters in the filestream can be loaded at once into memory and away the lexer goes. </i><br />
 file <code>antlr3inputstream.c</code> </p>
<p> <i>Base functions to initialize and manipulate any input stream. </i><br />
 file <code>antlr3intstream.c</code> </p>
<p> <i>Implementation of superclass elements of an ANTLR3 int stream. </i><br />
 file <code>antlr3lexer.c</code> </p>
<p> <i>Base implementation of an antlr 3 lexer. </i><br />
 file <code>antlr3parser.c</code> </p>
<p> <i>Implementation of the base functionality for an ANTLR3 parser. </i><br />
 file <code>antlr3rewritestreams.c</code> </p>
<p> <i>Implementation of token/tree streams that are used by the tree re-write rules to manipulate the tokens and trees produced by rules that are subject to rewrite directives. </i><br />
 file <code>antlr3string.c</code> </p>
<p> <i>Implementation of the ANTLR3 string and string factory classes. </i><br />
 file <code>antlr3stringstream.c</code> </p>
<p> <i>Provides implementations of string (or memory) streams as input for ANLTR3 lexers. </i><br />
 file <code>antlr3tokenstream.c</code> </p>
<p> <i>Default implementation of CommonTokenStream. </i><br />
 file <code>antlr3treeparser.c</code> </p>
<p> <i>Implementation of the tree parser and overrides for the base recognizer. </i><br />
 file <code>antlr3ucs2inputstream.c</code> </p>
<p> <i>Base functions to initialize and manipulate a UCS2 input stream. </i></p>
