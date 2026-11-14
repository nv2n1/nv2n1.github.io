---
title: "makestrs(1)"
name: "makestrs"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makestrs/"
description: "makestrs – makes string table C source and header(s)"
---

<h2>NAME</h2>
<p> makestrs &#8211; makes string table C source and header(s)</p>
<h2>SYNOPSIS</h2>
<p> <code>makestrs [-f source] [-i includedir] [-abioptions &#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>makestrs</i> command creates string table C source files and headers. If <i>-f</i> <i>source</i> is not specified <i>makestrs</i> will read from <i>stdin</i>. The C source file is always written to <i>stdout</i>. <i>makestrs</i> creates one or more C header files as specified in the source file. The following options may be specified: <i>-sparcabi</i>, <i>-intelabi</i>, <i>-functionabi</i>, <i>-arrayperabi</i>, and <i>-defaultabi.</i> </p>
<p> <i>-sparcabi </i> is used on SPARC platforms conforming to the SPARC Compliance Definition, i.e. SVR4/Solaris. </p>
<p> <i>-intelabi </i> is used on Intel platforms conforming to the System V Application Binary Interface, i.e. SVR4. </p>
<p> <i>-earlyR6abi </i> may be used in addition to <i>-intelabi </i> for situations where the vendor wishes to maintain binary compatibility between X11R6 public-patch 11 (and earlier) and X11R6 public-patch 12 (and later). </p>
<p> <i>-functionabi </i> generates a functional abi to the string table. This mechanism imposes a severe performance penalty and it&#8217;s recommended that you not use it. </p>
<p> <i>-arrayperabi </i> results in a separate array for each string. This is the default behavior if makestrs was compiled with -DARRAYPERSTR (it almost never is). </p>
<p> <i>-defaultabi </i> forces the generation of the &quot;normal&quot; string table even if makestrs was compiled with -DARRAYPERSTR. Since makestrs is almost never compiled with -DARRAYPERSTR this is the default behavior if no abioptions are specified. </p>
<p> <i>-i includedir</i> forces the reading of templates from the includedir instead of the local directory. This is useful to have separate source and build directories.</p>
<h2>SYNTAX</h2>
<p> The syntax for string-list file is (items in square brackets are optional):</p>
<dl>
<dt>
<dd> #prefix &lt;text&gt;</dl>
<dl>
<dt>
<dd> #feature &lt;text&gt;</dl>
<dl>
<dt>
<dd> #externref &lt;text&gt;</dl>
<dl>
<dt>
<dd> #externdef [&lt;text&gt;]</dl>
<dl>
<dt>
<dd> [#ctempl &lt;text&gt;]</dl>
<dl>
<dt>
<dd> #file &lt;filename&gt;</dl>
<dl>
<dt>
<dd> #table &lt;tablename&gt;</dl>
<dl>
<dt>
<dd> [#htempl]</dl>
<dl>
<dt>
<dd> &lt;text&gt;</dl>
<dl>
<dt>
<dd> &#8230;</dl>
<dl>
<dt>
<dd> &lt;text&gt;</dl>
<dl>
<dt>
<dd> [#table &lt;tablename&gt;</dl>
<dl>
<dt>
<dd> &lt;text&gt;</dl>
<dl>
<dt>
<dd> &#8230;</dl>
<dl>
<dt>
<dd> &lt;text&gt;</dl>
<dl>
<dt>
<dd> &#8230;</dl>
<dl>
<dt>
<dd> #table &lt;tablename&gt;</dl>
<dl>
<dt>
<dd> &#8230;]</dl>
<dl>
<dt>
<dd> [#file &lt;filename&gt;</dl>
<dl>
<dt>
<dd> &#8230;]</dl>
<p> In words you may have one or more #file directives. Each #file may have one or more #table directives. </p>
<p> The #prefix directive determines the string that makestr will prefix to each definition. </p>
<p> The #feature directive determines the string that makestr will use for the feature-test macro, e.g. X[TM]STRINGDEFINES. </p>
<p> The #externref directive determines the string that makestr will use for the extern clause, typically this will be &quot;extern&quot; but Motif wants it to be &quot;externalref&quot; </p>
<p> The #externdef directive determines the string that makestr will use for the declaration, typically this will be the null string (note that makestrs requires a trailing space in this case, i.e. &quot;#externdef &quot;), and Motif will use &quot;externaldef(_xmstrings). </p>
<p> The #ctmpl directive determines the name of the file used as a template for the C source file that is generated </p>
<p> Each #file &lt;filename&gt; directive will result in a corresponding header file by that name containing the appropriate definitions as specified by command line options. A single C source file containing the declarations for the definitions in all the headers will be printed to stdout. </p>
<p> The #htmpl directive determines the name of the file used as a template for the C header file that is generated. </p>
<p> Each #table &lt;tablename&gt; directive will be processed in accordance with the ABI. On most platforms all tables will be catenated into a single table with the name of the first table for that file. To conform to the Intel ABI separate tables will be generated with the names indicated. </p>
<p> The template files specified by the #ctmpl and #htmpl directives are processed by copying line for line from the template file to the appropriate output file. The line containing the string <i>&lt;&lt;&lt;STRING_TABLE_GOES_HERE&gt;&gt;&gt;</i> is not copied to the output file. The appropriate data is then copied to the output file and then the remainder of the template file is copied to the output file.</p>
<h2>BUGS</h2>
<p> makestrs is not very forgiving of syntax errors. Sometimes you need a trailing space after # directives, other times they will mess you up. No warning messages are emitted.</p>
<h2>SEE ALSO</h2>
<p> SPARC Compliance Definition 2.2., SPARC International Inc., 535 Middlefield Road, Suite 210, Menlo Park, CA 94025 </p>
<p> System V Application Binary Interface, Third Edition, ISBN 0-13-100439-5 UNIX Press, PTR Prentice Hall, 113 Sylvan Avenue, Englewood Cliffs, NJ 07632 </p>
<p> System V Application Binary Interface, Third Edition, Intel386 Architecture Processor Supplement ISBN 0-13-104670-5 UNIX Press, PTR Prentice Hall, 113 Sylvan Avenue, Englewood Cliffs, NJ 07632 </p>
<p> System V Application Binary Interface, Third Edition, SPARC Architecture Processor Supplement ISBN 0-13-104696-9 UNIX Press, PTR Prentice Hall, 113 Sylvan Avenue, Englewood Cliffs, NJ 07632 </p>
<h2>Index</h2>
