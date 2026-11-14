---
title: "xrmparsecommand(3)"
name: "xrmparsecommand"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmparsecommand/"
description: "XrmInitialize, XrmParseCommand, XrmValue, XrmOptionKind, XrmOptionDescRec – initialize the Resource Manager, Resource Manager structures, and parse the command line"
---

<p>XrmInitialize, XrmParseCommand, XrmValue, XrmOptionKind, XrmOptionDescRec &#8211; initialize the Resource Manager, Resource Manager structures, and parse the command line </p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt;</p>
<dd>void XrmInitialize(void);</p>
<dd>void XrmParseCommand(XrmDatabase *<i>database</i>, XrmOptionDescList <i>table</i>, int <i>table_count</i>, char *<i>name</i>, int *<i>argc_in_out</i>, char **<i>argv_in_out</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>argc_in_out</i></p>
<dd>Specifies the number of arguments and returns the number of remaining arguments.</p>
<dt><i>argv_in_out</i></p>
<dd>Specifies the command line arguments and returns the remaining arguments.</p>
<dt><i>database</i></p>
<dd>Specifies the resource database.</p>
<dt><i>name</i></p>
<dd>Specifies the application name.</p>
<dt><i>table</i></p>
<dd>Specifies the table of command line arguments to be parsed.</p>
<dt><i>table_count</i></p>
<dd>Specifies the number of entries in the table.</dl>
<h2>Description</h2>
<p>The <code>XrmInitialize</code> function initialize the resource manager. It must be called before any other Xrm functions are used. </p>
<p> The <code>XrmParseCommand</code> function parses an (argc, argv) pair according to the specified option table, loads recognized options into the specified database with type &#8220;String,&#8221; and modifies the (argc, argv) pair to remove all recognized options. If database contains NULL, <code>XrmParseCommand</code> creates a new database and returns a pointer to it. Otherwise, entries are added to the database specified. If a database is created, it is created in the current locale. </p>
<p> The specified table is used to parse the command line. Recognized options in the table are removed from argv, and entries are added to the specified resource database in the order they occur in argv. The table entries contain information on the option string, the option name, the style of option, and a value to provide if the option kind is <code>XrmoptionNoArg</code>. The option names are compared byte-for-byte to arguments in argv, independent of any locale. The resource values given in the table are stored in the resource database without modification. All resource database entries are created using a &#8220;String&#8221; representation type. The argc argument specifies the number of arguments in argv and is set on return to the remaining number of arguments that were not parsed. The name argument should be the name of your application for use in building the database entry. The name argument is prefixed to the resourceName in the option table before storing a database entry. The name argument is treated as a single component, even if it has embedded periods. No separating (binding) character is inserted, so the table must contain either a period (.) or an asterisk (*) as the first character in each resourceName entry. To specify a more completely qualified resource name, the resourceName entry can contain multiple components. If the name argument and the resourceNames are not in the Host Portable Character Encoding, the result is implementation-dependent.</p>
<h2>Structures</h2>
<p>The <code>XrmValue</code>, <code>XrmOptionKind</code>, and <code>XrmOptionDescRec</code> structures contain: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XPointer addr; } XrmValue, *XrmValuePtr; </p>
<p> typedef enum {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionNoArg,&nbsp;/*&nbsp;Value is specified in XrmOptionDescRec.value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionIsArg,&nbsp;/*&nbsp;Value is the option string itself&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionStickyArg,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Value is characters immediately following option&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionSepArg,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Value is next argument in argv&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionResArg,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Resource and value in next argument in argv&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionSkipArg,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ignore this option and the next argument in argv&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionSkipLine,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ignore this option and the rest of argv&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionSkipNArgs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ignore this option and the next<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmOptionDescRec.value arguments in argv&nbsp;*/ } XrmOptionKind; </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*option;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Option specification string in argv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*specifier;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Binding and resource name&nbsp;(sans application name)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmOptionKind argKind;&nbsp;<wbr>&nbsp;/*&nbsp;Which style of option it is&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XPointer value;&nbsp;/*&nbsp;Value to provide if XrmoptionNoArg or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmoptionSkipNArgs&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ } XrmOptionDescRec, *XrmOptionDescList;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrmgetresource/">XrmGetResource</a>(3), <a href="/docs/linux/man/3-xrmmergedatabases/">XrmMergeDatabases</a>(3), <a href="/docs/linux/man/3-xrmputresource/">XrmPutResource</a>(3), <a href="/docs/linux/man/3-xrmuniquequark/">XrmUniqueQuark</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
