---
title: "ftnchek(1)"
name: "ftnchek"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftnchek/"
description: "ftnchek – Fortran 77 program checker"
---

<h2 class="name">NAME</h2>
<p> ftnchek &#8211; Fortran 77 program checker </p>
<h2>SYNOPSIS</h2>
<p> <code>ftnchek</code> [ <code>-arguments</code>[=<i>list</i>] ] [ <code>-array</code>[=<i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>brief</code> ] [ <code>-calltree</code>[=<i>list</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>check</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-columns</code>[=<i>num</i>] ] [ <code>-common</code>[=<i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>crossref</code>[=<i>list</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>declare</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>division</code> ] [ <code>-errors</code>[=<i>num</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>extern</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>f77</code>[<code>=</code><i>list</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>f90</code>[<code>=</code><i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>f95</code>[<code>=</code><i>list</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>help</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>identifier-chars</code>[<code>=</code><i>list</i>] ] [ <code>-include=</code><i>str</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-intrinsic</code>[=<i>list</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>library</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>list</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-makedcls</code>[=<i>list</i>] ] [ <code>-mkhtml</code>[=<i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>novice</code> ] [ <code>-output=</code><i>str</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-pointersize</code>[=<i>num</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>portability</code>[<code>=</code><i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>pretty</code>[<code>=</code><i>list</i>] ] [ <code>-project</code>[=<i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>pure</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>quiet</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>reference</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>resources</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>sixchar</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>sort</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-source</code>[=<i>list</i>] ] [ <code>-style</code>[=<i>list</i>] ] [ <code>&#8211;</code>[<code>no</code>]<code>symtab</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>truncation</code>[<code>=</code><i>list</i>] ] [ <code>-usage</code>[=<i>list</i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>&#8211;</code>[<code>no</code>]<code>vcg</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>version</code> ] [ <code>&#8211;</code>[<code>no</code>]<code>volatile</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-wordsize</code>[=<i>num</i>] ] [ <code>-wrap</code>[=<i>num</i>] ] [ <i>files &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ftnchek</code> (short for Fortran checker) is designed to detect certain errors in a Fortran program that a compiler usually does not. <code>ftnchek</code> is not primarily intended to detect syntax errors. Its purpose is to assist the user in finding semantic errors. Semantic errors are legal in the Fortran language but are wasteful or may cause incorrect operation. For example, variables which are never used may indicate some omission in the program; uninitialized variables contain garbage which may cause incorrect results to be calculated; and variables which are not declared may not have the intended type. <code>ftnchek</code> is intended to assist users in the debugging of their Fortran program. It is not intended to catch all syntax errors. This is the function of the compiler. Prior to using <code>ftnchek</code>, the user should verify that the program compiles correctly. </p>
<p> This document first summarizes how to invoke <code>ftnchek</code>. That section should be read before beginning to use <code>ftnchek</code>. Later sections describe <code>ftnchek</code>&#8216;s options in more detail, give an example of its use, and explain how to interpret the output. The final sections mention the limitations and known bugs in <code>ftnchek</code>.</p>
<h2>INVOKING FTNCHEK</h2>
<p> <code>ftnchek</code> is invoked through a command of the form: </p>
<p> <center> $ ftnchek [-option -option &#8230;] filename [filename &#8230;]<br />
 </center> </p>
<p> The brackets indicate something which is optional. The brackets themselves are not actually typed. Here options are command-line switches or settings, which control the operation of the program and the amount of information that will be printed out. If no option is specified, the default action is to print error messages, warnings, and informational messages, but not the program listing or symbol tables. </p>
<p> Each option begins with the &#8216;-&#8216; character. (On VAX/VMS or MS-DOS systems you may use either &#8216;/&#8217; or &#8216;-&#8216;.) For the sake of conformity with an increasingly common convention, options can also begin with &#8216;&#8211;&#8216;. The options are described at greater length in the next section. </p>
<p> <code>ftnchek</code> options fall into two categories: switches, which are either true or false, and settings, which have a numeric or string value. The name of a switch is prefixed by &#8216;no&#8217; or &#8216;no-&#8216; to turn it off: e.g. <code>-nopure</code> would turn off the warnings about impure functions. The &#8216;no&#8217; prefix can also be used with numeric settings, having the effect of turning off the corresponding warnings. Settings that control lists of warnings have a special syntax discussed below. Only the first 3 characters of an option name (not counting the &#8216;-&#8216;) need be provided. A colon may be used in place of an equals sign for numeric or string setting assignments; however, we show only the equals sign form below. </p>
<p> The switches and settings which <code>ftnchek</code> currently recognizes are listed below. For each option, the default is the value used if the option is not explicitly specified, while the turn-on is the value used if the option is given without assigning it a value.</p>
<dl>
<dt><code>-arguments=</code><i>list</i></p>
<dd> Control warnings about subprogram type and argument mismatches. Default = turn-on = all.</p>
<dt><code>-array=</code><i>list</i></p>
<dd> Control warnings in checking array arguments of subprograms. Default = turn-on = all.</p>
<dt><code>-brief</code></p>
<dd> Use shorter format for some error messages. Default = no.</p>
<dt><code>-calltree=</code><i>list</i></p>
<dd> Produce subprogram call hierarchy in one of 3 formats: text call-tree, who-calls-who and VCG. Default = none, turn-on = tree,prune,sort. </p>
<p> If the <code>-mkhtml</code> option is invoked <i>and</i> tree is the applied calltree option, a file named CallTree.html, will be produced depicting the tree in HTML format.</p>
<dt><code>-check</code></p>
<dd> Perform checking. Default = yes.</p>
<dt><code>-columns=</code><i>num</i></p>
<dd> Set maximum line length to <i>num</i> columns. (Beyond this is ignored.) Turn-on = max = 132. Default = 72.</p>
<dt><code>-common=</code><i>list</i></p>
<dd> Set degree of strictness in checking COMMON blocks. Default = turn-on = all.</p>
<dt><code>-crossref=</code><i>list</i></p>
<dd> Print cross-reference list of subprogram calls, label usage, and/or COMMON block use. Default = none.</p>
<dt><code>-declare</code></p>
<dd> Print a list of all identifiers whose datatype is not explicitly declared. Default = no.</p>
<dt><code>-division</code></p>
<dd> Warn wherever division is done (except division by a constant). Default = no.</p>
<dt><code>-errors=</code><i>num</i></p>
<dd> Set the maximum number of error messages per cascade. Default = turn-on = 3.</p>
<dt><code>-extern</code></p>
<dd> Warn if external subprograms which are invoked are never defined. Default = yes.</p>
<dt><code>-f77=</code><i>list</i></p>
<dd> Control specific warnings about supported extensions to the Fortran 77 Standard. Default = none, turn-on = all.</p>
<dt><code>-f90=</code><i>list</i></p>
<dd> Control specific warnings about supported extensions to the Fortran 77 Standard that were not adopted as part of the Fortran 90 Standard. Default = none, turn-on = all.</p>
<dt><code>-f95=</code><i>list</i></p>
<dd> Control specific warnings about standard Fortran 77 features that were deleted from the Fortran 95 Standard. Default = none, turn-on = all.</p>
<dt><code>-help</code></p>
<dd> Print command summary. Default = no.</p>
<dt><code>-identifier-chars=</code><i>list</i></p>
<dd> Define non-alphanumeric characters that may be used in identifiers. Default = turn-on = dollar sign and underscore.</p>
<dt><code>-include=</code><i>path</i></p>
<dd> Define a directory to search for INCLUDE files before searching in the system-wide directory. Cumulative. Default = turn-on = none.</p>
<dt><code>-intrinsic=</code><i>list</i></p>
<dd> Control treatment of nonstandard intrinsic functions. Default = all except <code>vms</code> for Unix version, all except <code>unix</code> for VMS version, all except <code>unix</code> and <code>vms</code> for other versions. Turn-on = all.</p>
<dt><code>-library</code></p>
<dd> Begin library mode: do not warn about subprograms in file that are defined but never used. Default = no.</p>
<dt><code>-list</code></p>
<dd> Print source listing of program. Default = no.</p>
<dt><code>-makedcls=</code><i>list</i></p>
<dd> Prepare a file of declarations. The <i>list</i> specifies options for the format of this file. Default = none, turn-on = declarations.</p>
<dt><code>-mkhtml=</code><i>list</i></p>
<dd> Create individual HTML document files from ftnchek analysis and code comments. Usually you will also want to specify <code>-call=tree</code> to create the root HTML file CallTree.html. Default = none, turn-on = documents.</p>
<dt><code>-novice</code></p>
<dd> Give output suitable for novice users. Default = yes.</p>
<dt><code>-output=</code><i>filename</i></p>
<dd> Send output to the given file. Default and turn-on sends output to the screen. (Default filename extension is <i>.lis</i>).</p>
<dt><code>-pointersize=</code><i>num</i></p>
<dd> Set the size of &#8220;Cray pointer&#8221; variables to <i>num</i> bytes. Min = 1, max = 16. Default = turn-on = 4</p>
<dt><code>-portability=</code><i>list</i></p>
<dd> Warn about non-portable usages. Default = none, turn-on = all.</p>
<dt><code>-pretty=</code><i>list</i></p>
<dd> Give warnings for possibly misleading appearance of source code. Default = turn-on = all.</p>
<dt><code>-project=</code><i>list</i></p>
<dd> Create project file (see explanation below). Default = no.</p>
<dt><code>-pure</code></p>
<dd> Assume functions are pure, i.e. have no side effects. Default = yes.</p>
<dt><code>-quiet</code></p>
<dd> Produce less verbose output. Default = no.</p>
<dt><code>-reference</code></p>
<dd> Print table of subprograms referenced by each subprogram. Default = no.</p>
<dt><code>-resources</code></p>
<dd> Print amount of resources used in analyzing the program. Default = no.</p>
<dt><code>-sixchar</code></p>
<dd> List any variable names which clash at 6 characters length. Default = no.</p>
<dt><code>-sort</code></p>
<dd> Print list of subprograms sorted in prerequisite order. Default = no.</p>
<dt><code>-source=</code><i>list</i></p>
<dd> Select source formatting options: fixed or free form, DEC Fortran tab-formatted lines, VMS-style INCLUDE statement, UNIX-style backslash escape sequences, and implicit typing of parameters. Default = none, turn-on = all.</p>
<dt><code>-style=</code><i>list</i></p>
<dd> Produce extra-picky warnings about obsolescent or old-fashioned programming constructions. Default = none, turn-on = all.</p>
<dt><code>-symtab</code></p>
<dd> Print symbol table and label table for each subprogram. Default = no.</p>
<dt><code>-truncation=</code><i>list</i></p>
<dd> Check for possible loss of accuracy by truncation. Default = turn-on = all.</p>
<dt><code>-usage=</code><i>list</i></p>
<dd> Control warnings about unused or uninitialized variables, common blocks, etc. Default = turn-on = all.</p>
<dt><code>-vcg</code></p>
<dd> Produce VCG format of call graph.</p>
<dt><code>-version</code></p>
<dd> Print version number. Default = no.</p>
<dt><code>-volatile</code></p>
<dd> Assume COMMON blocks lose definition between activations. Default = no. (Obsolete. Use <code>-common=volatile</code> instead.)</p>
<dt><code>-wordsize=</code><i>num</i></p>
<dd> Set the default word size for numeric quantities to <i>num</i> bytes. Default = turn-on = 4 bytes.</p>
<dt><code>-wrap=</code><i>num</i></p>
<dd> Set output column at which to wrap long error messages and warnings to the next line. If set to 0, turn off wrapping. Default = turn-on = 79.</dl>
<p> When more than one option is used, they should be separated by a blank space, except on systems such as VMS where options begin with slash ( / ). No blank spaces may be placed around the equals sign ( = ) in a setting. ftnchek &quot;?&quot; will produce a command summary listing all options and settings. </p>
<p> For settings that take a list of keywords, namely <code>-arguments</code>, <code>-array</code>, <code>-calltree</code>, <code>-common</code>, <code>-crossref</code>, <code>-f77</code>, <code>-f90</code>, <code>-f95</code>, <code>-intrinsic</code>, <code>-makedcls</code>, <code>-mkhtml</code>, <code>-portability</code>, <code>-pretty</code>, <code>-project</code>, <code>-source</code>, <code>-style</code>, <code>-truncation</code>, and <code>-usage</code>, the list consists of keywords separated by commas or colons. If the list of keywords is omitted, the effect is to set the option to its turn-on value (same as &#8220;all&#8221; in most cases). Also, if the list is omitted, the setting name can be prefixed with <code>no</code> or <code>no-</code> to turn off all the options it controls. For example, <code>-f77</code> turns on all warnings about nonstandard constructions, while <code>-nof77</code> turns them all off. Three special keywords are:</p>
<dl>
<dt><code>help</code></p>
<dd> Print out all the option keywords controlled by the setting, with a brief explanation of their meanings. This keyword cannot be given in a list with other keywords.</p>
<dt><code>all</code></p>
<dd> Set all options. This turns on all options controlled by the setting.</p>
<dt><code>none</code></p>
<dd> Clear all options. This turns off all options controlled by the setting.</dl>
<p> These three special keywords must be given in full. For all other keywords, only as many letters of the keyword as are necessary to identify it unambiguously need be given, or a wildcard pattern may be used. Including a keyword in the list turns the corresponding option on. For example, <code>-f77=intrinsic</code> would turn on only the warnings about use of nonstandard intrinsic functions. Prefixing a keyword by <code>no-</code> turns its option off. For example, <code>-pretty=no-long-line</code> turns off warnings about lines exceeding 72 columns in length while leaving all other warnings about misleading appearance in effect. If a setting has default <code>none</code>, you can turn on all options except one or two by using <code>all</code> first. For example, <code>-f77=all,no-include</code> enables warnings about all nonstandard extensions except INCLUDE statements. If a setting has default <code>all</code>, you can turn off all warnings except one or two by using <code>none</code> first. For example, <code>-truncation=none,demotion</code> would turn off all precision related warnings except about demotions. Wildcard patterns contain an asterisk to stand for any string of characters. If a wildcard pattern is used, all the warnings that match it are affected. If <code>no-</code> is prefixed to the pattern, all the matching warnings are turned off, otherwise they are all turned on. The minimum unambiguous length rule does not apply to wildcard matching. For example, use <code>-usage=no-*var*</code> to turn off all warnings relating to variable usage (both local and common). (Unix users may need to quote any options containing wildcards in order to prevent the shell from attempting to expand them.) Wildcards are recognized only in lists of warning keywords, not in the top-level options themselves. </p>
<p> When <code>ftnchek</code> starts up, it looks for environment variables and also for a preferences file. Any options defined in the environment or in the preferences file are used as defaults in place of the built-in defaults. They are over-ridden by any command line options. See the section on changing the defaults for details about the environment options and the preferences file. </p>
<p> When giving a name of an input file, the extension is optional. If no extension is given, <code>ftnchek</code> will first look for a project file with extension <i>.prj</i>, and will use that if it exists. If not, then <code>ftnchek</code> will look for a Fortran source file with the extension <i>.for</i> for VMS systems, <i>.f</i> for UNIX systems. More than one file name can be given to <code>ftnchek</code>, and it will process the modules in all files as if they were in a single file. </p>
<p> Wildcards are allowed in the specification of filenames on the command line for the VMS and MS-DOS versions, as also of course under UNIX and any other system that performs wildcard expansion in the command processor. </p>
<p> If no filename is given, <code>ftnchek</code> will read input from the standard input.</p>
<h2>OPTIONS</h2>
<p> This section provides a more detailed discussion of <code>ftnchek</code> command-line options. Options and filenames may be interspersed on a command line. Most options are positional: each option remains in effect from the point it is encountered until it is overridden by a later change. Thus for example, the listing may be suppressed for some files and not for others. Exceptions are: the <code>-intrinsic</code>, <code>-pointersize</code>, and <code>-wordsize</code> settings, which cannot be changed once processing of input files has started; the <code>-arguments</code>, <code>-array</code>, <code>-calltree</code>, <code>-common</code>, <code>-crossref</code>, <code>-extern</code>, <code>-reference</code>, <code>-resources</code>, <code>-sort</code>, <code>-vcg</code>, and <code>-volatile</code> options, where the action depends only on the value of the option after the processing of input files is finished; and the <code>-include</code> setting, which is cumulative. </p>
<p> The option names in the following list are in alphabetical order. </p>
<dl>
<dt><code>-arguments=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Controls warnings about mismatches between actual and dummy subprogram arguments, and also about mismatches between expected and actual subprogram type. (An actual argument is an argument passed to the subprogram by the caller; a dummy argument is an argument received by the subprogram.) By default, all warnings are turned on. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. Since all these warnings are on by default, include a keyword prefixed by <code>no-</code> to turn off a particular warning. There are three special keywords: <code>all</code> to turn on all the warnings about arguments, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-arguments</code> is equivalent to <code>-arguments=all</code>, and <code>-noarguments</code> is equivalent to <code>-arguments=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>arrayness</code>:</p>
<dd> warn about inconsistent use of arguments that are arrays. These warnings can be further controlled by the <code>-array</code> option.</p>
<dt><code>type</code>:</p>
<dd> warn about dummy arguments of a different data type from the actual arguments.</p>
<dt><code>function-type</code>:</p>
<dd> warn if the invocation assumes the function&#8217;s return value is a different type than it actually is. Also warns if a function is called as a subroutine, or vice-versa.</p>
<dt><code>number</code>:</p>
<dd> warn about invoking a subprogram with a different number of arguments than the subprogram expects.</dl>
<p> For compatibility with previous versions of <code>ftnchek</code>, a numeric form of this setting is also accepted: the <i>list</i> is replaced by a number from 0 to 3. A value of 0 turns all the warnings off, 1 turns on only <code>number</code>, 2 turns on all except <code>number</code>, and 3 turns all the warnings on. </p>
<p> This setting does not apply to checking invocations of intrinsic functions or statement functions, which can only be turned off by the <code>-nocheck</code> option. </p>
<p> See also: <code>-array</code>, <code>-library</code>, <code>-usage</code>.</dl>
<dt><code>-array=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Controls the degree of strictness in checking agreement between actual and dummy subprogram arguments that are arrays. The warnings controlled by this setting are for constructions that might legitimately be used by a knowledgeable programmer, but that often indicate programming errors. By default, all warnings are turned on. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. Since all these warnings are on by default, include a keyword prefixed by <code>no-</code> to turn off a particular warning. There are three special keywords: <code>all</code> to turn on all the warnings about array arguments, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-array</code> is equivalent to <code>-array=all</code>, and <code>-noarray</code> is equivalent to <code>-array=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>dimensions</code>:</p>
<dd> warn if the arguments differ in their number of dimensions, or if the actual argument is an array element while the dummy argument is a whole array.</p>
<dt><code>size</code>:</p>
<dd> warn if both arguments are arrays, but they differ in number of elements.</dl>
<p> For compatibility with previous versions of <code>ftnchek</code>, a numeric form of this setting is also accepted: the <i>list</i> is replaced by a number from 0 to 3. A value of 0 turns all the warnings off, 1 turns on only <code>dimensions</code>, 2 turns on only <code>size</code>, and 3 turns all the warnings on. </p>
<p> Note: A warning is always given regardless of this setting if the actual argument is an array while the dummy argument is a scalar variable, or if the actual argument is a scalar variable or expression while the dummy argument is an array. These cases are seldom intentional. (To turn off even these warnings, use <code>-arguments=no-arrayness</code>.) No warning is ever given if the actual argument is an array element while the dummy argument is a scalar variable. Variable-dimensioned arrays and arrays dimensioned with 1 or asterisk match any number of array elements. There is no check of whether multi-dimensional arrays agree in the size of each dimension separately. </p>
<p> See also: <code>-arguments</code>, <code>-library</code>, <code>-usage</code>.</dl>
<dt><code>-brief</code></p>
<dd>
<dl>
<dt>
<dd> Selects a shorter format for some warning messages. At present, the only warnings controlled by this flag are those that are printed at the end of processing each subprogram. These include warnings about variables that are set but not used or used before set, variable names that do not conform to the Fortran 77 standard, etc. (These warnings may be suppressed entirely depending on other flags, such as the <code>-usage</code> or <code>-f77</code> flags.) In the default format each variable is listed on a separate line, along with the line number where the variable is declared, set or used, according to the nature of the warning. The briefer format simply lists all variables to which the warning applies, with up to 4 variables per line. </p>
<p> See also: <code>-quiet</code>.</dl>
<dt><code>-calltree=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Causes <code>ftnchek</code> to print out the call structure of the complete program. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. There are two special keywords: <code>none</code> to turn off all the options, and <code>help</code> to print the list of all the keywords with a brief explanation of each. (The keyword <code>all</code> turns on all the options, but should not normally be used since only one format should be specified.) If <i>list</i> is omitted, <code>-calltree</code> is equivalent to <code>-calltree=tree</code>, and <code>-nocalltree</code> is equivalent to <code>-calltree=none</code>. By default no call graph is printed. </p>
<p> If the -mkhtml option is invoked <i>and</i> tree is the applied calltree option, a file named CallTree.html, will also be produced depicting the tree in HTML format. This file is useful as a starting point for browsing the HTML files describing each component of the program. </p>
<p> The keywords which control which format is used are as follows:</p>
<dl>
<dt><code>tree</code>:</p>
<dd> produce the call graph in tree format.</p>
<dt><code>reference</code>:</p>
<dd> produce the call graph in who-calls-who format (same as <code>-reference</code> switch).</p>
<dt><code>vcg</code>:</p>
<dd> produce the call graph in VCG format (same as <code>-vcg</code> switch).</dl>
<p> Only one of the formats <code>tree</code>, <code>reference</code>, or <code>vcg</code> may be specified. </p>
<p> The following keywords control options affecting the output:</p>
<dl>
<dt><code>prune</code>:</p>
<dd> prune repeated subtrees (applicable only with <code>tree</code>). This the default.</p>
<dt><code>sort</code>:</p>
<dd> sort children of each routine into alphabetical order. This is the default.</dl>
<p> See the discussion of the <code>-reference</code> and <code>-vcg</code> flags for details about these formats. </p>
<p> For <code>tree</code> format, The call graph is printed out starting from the main program, which is listed on the first line at the left margin. Then on the following lines, each routine called by the main program is listed, indented a few spaces, followed by the subtree starting at that routine. </p>
<p> In the default mode, if a routine is called by more than one other routine, its call subtree is printed only the first time it is encountered Later calls give only the routine name and the notice &#8220;(see above)&#8221;. To have the subtree printed for each occurrence of the routine, use option <code>no-prune</code>. </p>
<p> Note that the call tree will be incomplete if any of the input files are project files containing more than one module that were created in <code>-library</code> mode. See the discussion of project files below. </p>
<p> Technical points: Each list of routines called by a given routine is printed in alphabetical order unless the <code>no-sort</code> option is given. If multiple main programs are found, the call tree of each is printed separately. If no main program is found, a report to that effect is printed out, and the call trees of any top-level non-library routines are printed. This flag only controls the printing of the call tree: <code>ftnchek</code> constructs the call tree in any case because it is used to determine which library modules will be cross-checked. See the discussion of the <code>-library</code> flag. </p>
<p> For compatibility with previous versions of <code>ftnchek</code>, a numeric form of this setting is also accepted: the <i>list</i> is replaced by a number from 0 to 15. This number is formed from 1 for <code>tree</code> format, 2 for <code>reference</code> format, or 3 for <code>vcg</code> format, plus 4 for <code>no-prune</code>, and 8 for <code>no-sort</code>. </p>
<p> See also: <code>-crossref</code>, <code>-library</code>, <code>-reference</code>, <code>-sort</code>, <code>-symtab</code>, <code>-vcg</code>.</dl>
<dt><code>-check</code></p>
<dd>
<dl>
<dt>
<dd> This switch is provided so that errors and warning messages can be turned off when <code>ftnchek</code> is used for purposes other than finding bugs, such as making declarations or printing the call tree. It is positional, so after turning all checks off, selected checks can be turned back on. The effect of <code>-nocheck</code> is to put all switches, numeric settings, and settings controlling lists of warnings to their turn-off values, as if they had all been specified with the -no prefix. Switches and settings that specify options and modes of operation, rather than controlling warnings, are unaffected. These are <code>-columns</code>, <code>-crossref</code>, <code>-include</code>, <code>-intrinsic</code>, <code>-library</code>, <code>-list</code>, <code>-makedcls</code>, <code>-novice</code>, <code>-output</code>, <code>-pointersize</code>, <code>-project</code>, <code>-quiet</code>, <code>-reference</code>, <code>-resources</code>, <code>-sort</code>, <code>-source</code>, <code>-symtab</code>, <code>-vcg</code>, <code>-version</code>, <code>-wordsize</code>, and <code>-wrap</code>. Default = yes. </p>
<p> Parse errors (syntax errors due to unrecognized or malformed statements) are not suppressed by this switch, since the results may be incorrect if <code>ftnchek</code> has not parsed the program correctly. </p>
<p> There are some miscellaneous errors and warning messages that are not controlled by any other switch, and so can be turned off only by this switch. Note that using <code>-check</code> following <code>-nocheck</code> only has the effect of turning these special warnings back on, and does not restore all the checks it turned off. These warnings are:</p>
<dl>
<dt>o</p>
<dd> Module contains no executable statements.</p>
<dt>o</p>
<dd> In free source form, missing space where space is required (e.g. between a keyword and an identifier) or space present where none is allowed (e.g. within an identifier).</p>
<dt>o</p>
<dd> Zero or negative length specification in a data type declaration of the form type*len.</p>
<dt>o</p>
<dd> Invalid operand(s) in an expression.</p>
<dt>o</p>
<dd> Array assigned to scalar.</p>
<dt>o</p>
<dd> Type mismatch between DO index and bounds.</p>
<dt>o</p>
<dd> Undefined common block declared in SAVE statement.</p>
<dt>o</p>
<dd> Intrinsic function explicitly declared with an incompatible type.</p>
<dt>o</p>
<dd> Unknown intrinsic function explicitly declared in an INTRINSIC statement.</p>
<dt>o</p>
<dd> Intrinsic function passed as a subprogram argument is not declared in an INTRINSIC statement.</p>
<dt>o</p>
<dd> Intrinsic function or statement function invoked incorrectly.</p>
<dt>o</p>
<dd> Function does not set return value prior to RETURN statement.</p>
<dt>o</p>
<dd> Parameter constant value not evaluated (this is <code>ftnchek</code>&#8216;s fault, and it is just informing you of the fact).</p>
<dt>o</p>
<dd> Entry point of a subprogram is later used as a different subprogram&#8217;s name.</p>
<dt>o</p>
<dd> Unknown keyword used in an I/O statement.</p>
<dt>o</p>
<dd> Illegal label reference (e.g. GOTO refers to a non-executable statement; I/O statement refers to a non-format statement).</dl>
<p> See also: <code>-errors</code>.</dl>
<dt><code>-columns=</code><i>num</i></p>
<dd>
<dl>
<dt>
<dd> Set maximum statement length to <i>num</i> columns. (Beyond this is ignored.) This setting is provided to allow checking of programs which may violate the Fortran standard limit of 72 columns for the length of a statement. According to the standard, all characters past column 72 are ignored. If this setting is used when the <code>-f77=long-line</code> option is in effect, a warning will be given for any lines in which characters past column 72 are processed. Turn-on = max = 132. Default = 72. </p>
<p> This setting does not suppress warnings about the presence of characters beyond column 72. To process code with meaningful program text beyond column 72, use this setting and be sure the <code>-f77</code> <code>long-line</code> option is off. To process code with sequence numbers in columns 73 to 80, leave the the columns setting at the default value and use the <code>-pretty=no-long-line</code> flag. </p>
<p> See also: <code>-f77</code>, <code>-pretty</code>.</dl>
<dt><code>-common=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> This setting controls the strictness of checking of COMMON blocks. By default, all warnings except <code>volatile</code> are turned on. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. Since most of these warnings are on by default, include a keyword prefixed by <code>no-</code> to turn off a particular warning. There are three special keywords: <code>all</code> to turn on all the warnings, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-common</code> is equivalent to <code>-common=dimensions,exact,length,type</code>, and <code>-nocommon</code> is equivalent to <code>-common=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>dimensions</code>:</p>
<dd> corresponding arrays in each declaration of a block must agree in size and number of dimensions. This option only has an effect when used together with <code>exact</code>.</p>
<dt><code>exact</code>:</p>
<dd> the comparison of two blocks is done variable-by-variable rather than simply requiring agreement between corresponding storage locations. Use this if all declarations of a given COMMON block are supposed to be identical, which is a good programming practice.</p>
<dt><code>length</code>:</p>
<dd> warn if different declarations of the same block are not equal in total length. The Fortran 77 Standard requires each named common block, but not blank common, to be the same length in all modules of the program.</p>
<dt><code>type</code>:</p>
<dd> in each declaration of a given COMMON block, corresponding memory locations (words or bytes) must agree in data type. If used together with <code>exact</code>, this will require that corresponding variables agree in data type.</p>
<dt><code>volatile</code>:</p>
<dd> Assume that COMMON blocks are volatile.</dl>
<p> Many Fortran programmers assume that variables, whether local or in COMMON, are static, i.e. that once assigned a value, they retain that value permanently until assigned a different value by the program. However, in fact the Fortran 77 Standard does not require this to be the case. Local variables may become undefined between activations of a module in which they are declared. Similarly, COMMON blocks may become undefined if no module in which they are declared is active. (The technical term for entities with this behavior is &#8220;automatic&#8221;, but <code>ftnchek</code> uses the word &#8220;volatile&#8221; since it is clearer to the nonspecialist.) Only COMMON blocks declared in a SAVE statement, or declared in the main program or in a block data subprogram remain defined as long as the program is running. Variables and COMMON blocks that can become undefined at some point are called volatile. </p>
<p> If the <code>-common=volatile</code> flag is turned on, <code>ftnchek</code> will warn you if it finds a volatile COMMON block. If, at the same time, the <code>-usage=com-block-volatile </code> option is turned on (which is the default), <code>ftnchek</code> will try to check whether such a block can lose its defined status between activations of the modules where it is declared. <code>ftnchek</code> does not do a very good job of this: the rule used is to see whether the block is declared in two separated subtrees of the call tree. For instance, this would be the case if two modules, both called from the main program, shared a volatile COMMON block. A block can also become undefined between two successive calls of the same subprogram, but <code>ftnchek</code> is not smart enough to tell whether a subprogram can be called more than once, so this case is not checked for. </p>
<p> The <code>-common=volatile</code> flag does not affect the way <code>ftnchek</code> checks the usage of local variables. </p>
<p> For compatibility with previous versions of <code>ftnchek</code>, a numeric form of this setting is also accepted: the <i>list</i> is replaced by a number from 0 to 3. A value of 0 turns all the warnings off, 1 or greater turns on <code>type</code>, 2 or greater turns on <code>length</code>, and 3 turns on <code>dimensions</code> and <code>exact</code> also. The numeric form cannot turn on the <code>volatile</code> option. </p>
<p> See also: <code>-library</code>, <code>-usage</code>.</dl>
<dt><code>-crossref=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Prints cross-reference tables. Default = none. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. The keywords with their meanings are as follows:</p>
<dl>
<dt><code>calls</code>:</p>
<dd> table lists each subprogram followed by a list of routines that call it. This listing omits library modules that are not in the call tree of the main program. The list is alphabetized.</p>
<dt><code>common</code>:</p>
<dd> table lists each COMMON block followed by a list of the routines that access it. These listed routines are those in which some variables in the COMMON block are accessed, not simply those routines that declare the block. (To find out what routines declare a COMMON block but do not use it, see the <code>-usage</code> flag.)</p>
<dt><code>labels</code>:</p>
<dd> table lists each label followed by a list of all references to it. A label reference is denoted by the line number and statement type of the referring statement. The label list is in sequential order. The references are listed in the order they are encountered in the program.</dl>
<p> See also: <code>-calltree</code>, <code>-reference</code>, <code>-sort</code>, <code>-symtab</code>, <code>-vcg</code>.</dl>
<dt><code>-declare</code></p>
<dd>
<dl>
<dt>
<dd> If this flag is set, all identifiers whose datatype is not declared in each module will be listed. This flag is useful for helping to find misspelled variable names, etc. The same listing will be given if the module contains an IMPLICIT NONE statement. Default = no. </p>
<p> See also: <code>-sixchar</code>, <code>-usage</code>.</dl>
<dt><code>-division</code></p>
<dd>
<dl>
<dt>
<dd> This switch is provided to help users spot potential division by zero problems. If this switch is selected, every division except by a constant will be flagged. (It is assumed that the user is intelligent enough not to divide by a constant which is equal to zero!) Default = no. </p>
<p> See also: <code>-portability</code>, <code>-truncation</code>.</dl>
<dt><code>-errors=</code><i>num</i></p>
<dd>
<dl>
<dt>
<dd> Set the maximum number of error messages in a &#8220;cascade&#8221;. During checking of agreement of subprogram arguments, common block declarations, and so forth, sometimes a single case will generate a long string of warnings. Often this simply indicates some other cause than a genuine item-by-item mismatch, such as for example a varible missing from one list. So in such cases <code>ftnchek</code> stops printing the warnings after the cascade limit is reached, and the trailer &#8220;etc&#8230;&#8221; is printed to indicate that there were more errors not printed. If you think that these warnings are likely to be genuine, use this setting to see more of them. Turn-on = default = 3, max = 999. A value of 0 means no limit. </p>
<p> This setting does not set an overall limit on the number of error messages printed, only the number printed in any one cascade. Most types of warnings and error messages are not subject to the cascade effect and so are not affected by this setting. To turn off warnings generally, use the individual warning control options or the <code>-nocheck</code> option. </p>
<p> See also: <code>-check</code>.</dl>
<dt><code>-extern</code></p>
<dd>
<dl>
<dt>
<dd> Causes <code>ftnchek</code> to report whether any subprograms invoked by the program are never defined. Ordinarily, if <code>ftnchek</code> is being run on a complete program, each subprogram other than the intrinsic functions should be defined somewhere. Turn off this switch if you just want to check a subset of files which form part of a larger complete program. Subprogram arguments will still be checked for correctness. Default = yes. </p>
<p> The <code>-extern</code> flag is now superseded by the <code>-usage=ext-undefined</code> option. For the sake of convenience, the <code>-extern</code> flag is retained, so that <code>-noextern</code> is equivalent to <code>-usage=no-ext-undefined</code> option. The <code>-extern</code> switch may be retired eventually. </p>
<p> See also: <code>-library</code>.</dl>
<dt><code>-f77=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Use this setting to catch language extensions which violate the Fortran 77 Standard. Such extensions may cause your program not to be portable. Examples include the use of underscores in variable names; variable names longer than six characters; statement lines longer than 72 characters; and nonstandard statements such as the DO &#8230; ENDDO structure. <code>ftnchek</code> does not report on the use of lowercase letters. By default, all warnings are turned off. </p>
<p> This setting provides detailed control over the warnings about supported extensions to the Fortran 77 Standard. (Further details about the extensions themselves are given below in the section on Extensions.) The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the warnings about nonstandard extensions, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-f77</code> is equivalent to <code>-f77=all</code>, and <code>-nof77</code> is equivalent to <code>-f77=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>accept-type</code>:</p>
<dd> ACCEPT and TYPE I/O statements.</p>
<dt><code>array-bounds</code>:</p>
<dd> Expressions defining array bounds that contain array elements or function references.</p>
<dt><code>assignment-stmt</code>:</p>
<dd> Assignment statements involving arrays. In Fortran 90, an array can be assigned to another array of compatible shape, or a scalar can be assigned to an array. Neither of these assignments is permitted in Fortran 77.</p>
<dt>
<dd> A related warning occurs when an array is assigned to a scalar. Since this is illegal also in Fortran 90, it is always warned about regardless of the <code>-f77</code> setting (unless all checking is turned off with the <code>-nocheck</code> flag).</p>
<dt><code>attribute-based-decl</code>:</p>
<dd> Type declarations in the new Fortran 90 attribute-based style. This style of declaration is distinguished by the use of a double colon (::) between the list of attributes and the list of declared variables. This option also controls warnings for use of Fortran 90 length or kind specifiers in type declarations. (Although these specifiers can be used in non-attribute-based declarations, they are controlled by this option to avoid proliferation of <code>-f77</code> options.)</p>
<dt><code>automatic-array</code>:</p>
<dd> Local (not dummy) arrays which have variable size. These would correspond to arrays whose storage would have to be dynamically allocated at run time.</p>
<dt><code>backslash</code>:</p>
<dd> Unix backslash escape in strings. This warning will be given only if the <code>-source=unix-backslash</code> setting is specified to cause the escape interpretation of backslash..</p>
<dt><code>byte</code>:</p>
<dd> BYTE data type declaration.</p>
<dt><code>case-construct</code>:</p>
<dd> The SELECT CASE construct.</p>
<dt><code>character</code>:</p>
<dd> Extensions to the Fortran 77 standard regarding character data. At present, this only controls warnings about character variables declared with zero or negative length. In Fortran 77, all character variables must be of positive length. In Fortran 90, they can be zero length, and declarations that specify negative lengths are permitted, turning into zero for the declared length. Note: because negative length specifiers may indicate a programming error, the warning about them is given even if this option is turned off, and is suppressed only by the <code>-nocheck</code> flag.</p>
<dt><code>common-subprog-name</code>:</p>
<dd> Common block and subprogram having the same name.</p>
<dt><code>construct-name</code>:</p>
<dd> Use of a construct-name to label a control statement.</p>
<dt><code>continuation</code>:</p>
<dd> More than 19 successive continuation lines.</p>
<dt><code>cpp</code>:</p>
<dd> Unix C preprocessor directives in the source code.</p>
<dt><code>cray-pointer</code>:</p>
<dd> &#8220;Cray pointer&#8221; syntax.</p>
<dt><code>cycle-exit</code>:</p>
<dd> The CYCLE and EXIT statements.</p>
<dt><code>d-comment</code>:</p>
<dd> Debugging comments starting with D in the source code.</p>
<dt><code>dec-tab</code>:</p>
<dd> DEC Fortran style tab-formatted source code. This warning will be given only if the <code>-source=dec-tab</code> setting is specified to cause interpretation of tabs in this style.</p>
<dt><code>do-enddo</code>:</p>
<dd> DO loop extensions: terminal statement label omitted, END DO, and WHILE.</p>
<dt><code>double-complex</code>:</p>
<dd> Double precision complex datatype.</p>
<dt><code>format-dollarsign</code>:</p>
<dd> Dollar sign control code in FORMAT statements.</p>
<dt><code>format-edit-descr</code>:</p>
<dd> Nonstandard edit descriptors in FORMAT statements.</p>
<dt><code>function-noparen</code>:</p>
<dd> Function definition without parentheses.</p>
<dt><code>implicit-none</code>:</p>
<dd> IMPLICIT NONE statement.</p>
<dt><code>include</code>:</p>
<dd> INCLUDE statement.</p>
<dt><code>inline-comment</code>:</p>
<dd> Inline comments starting with an exclamation point.</p>
<dt><code>internal-list-io</code>:</p>
<dd> List-directed I/O to or from an internal file.</p>
<dt><code>intrinsic</code>:</p>
<dd> Nonstandard intrinsic functions.</p>
<dt><code>io-keywords</code></p>
<dd> Nonstandard keywords used in I/O statements. These fall into three groups. The first group includes keywords that are accepted in Fortran 90: <center></p>
<table>
<tr VALIGN=top>
<td>ACTION</td>
<td>PAD</td>
<td>READWRITE
</td>
</tr>
<tr VALIGN=top>
<td>ADVANCE</td>
<td>POSITION</td>
<td>SIZE
</td>
</tr>
<tr VALIGN=top>
<td>DELIM</td>
<td>READ</td>
<td>WRITE
</td>
</tr>
<tr VALIGN=top>
<td>EOR</td>
<td></td>
<td>
</td>
</tr>
</table>
<p></center> The second group comprises the following VMS Fortran keywords: <center></p>
<table>
<tr VALIGN=top>
<td>BLOCKSIZE</td>
<td>EXTENDSIZE</td>
<td>READONLY
</td>
</tr>
<tr VALIGN=top>
<td>BUFFERCOUNT</td>
<td>INITIALSIZE</td>
<td>RECORDSIZE
</td>
</tr>
<tr VALIGN=top>
<td>CARRIAGECONTROL</td>
<td>MAXREC</td>
<td>RECORDTYPE
</td>
</tr>
<tr VALIGN=top>
<td>DEFAULTFILE</td>
<td>NAME (in OPEN)</td>
<td>SHARED
</td>
</tr>
<tr VALIGN=top>
<td>DISP</td>
<td>NOSPANBLOCK</td>
<td>TYPE
</td>
</tr>
<tr VALIGN=top>
<td>DISPOSE</td>
<td>ORGANIZATION</td>
<td>
</td>
</tr>
</table>
<p></center> (The keyword NAME is standard only in the INQUIRE statement.) The third group consists of the following IBM/MVS keyword: <center></p>
<table>
<tr VALIGN=top>
<td>NUM</td>
<td></td>
<td>
</td>
</tr>
</table>
<p></center> This flag also controls a warning about use of ACCESS=&#8217;APPEND&#8217;, which is accepted by some compilers. The value of &#8216;APPEND&#8217; is not valid for any I/O specifier in standard Fortran 77, and in Fortran 90 &#8216;APPEND&#8217; should be used as a value of the POSITION specifier, not ACCESS.</p>
<dt><code>long-line</code>:</p>
<dd> Statements with meaningful code past 72 columns. This warning is given only if the <code>-columns</code> setting has been used to increase the statement field width.</p>
<dt><code>long-name</code>:</p>
<dd> Identifiers over 6 characters long.</p>
<dt><code>mixed-common</code>:</p>
<dd> Mixed character and noncharacter data in COMMON block.</p>
<dt><code>mixed-expr</code>:</p>
<dd> Nonstandard type combinations in expressions, for example DOUBLE PRECISION with COMPLEX, assigning hollerith to integer, logical operations on integers.</p>
<dt><code>name-dollarsign</code>:</p>
<dd> Dollar sign used as a character in identifiers.</p>
<dt><code>name-underscore</code>:</p>
<dd> Underscore used as a character in identifiers.</p>
<dt><code>namelist</code>:</p>
<dd> NAMELIST statement.</p>
<dt><code>param-implicit-type</code>:</p>
<dd> Implicit typing of a parameter by the data type of the value assigned. This warning can only occur if implicit parameter typing has been turned on by the <code>-source=param-implicit-type</code> option, or if the PARAMETER statement is of the nonstandard form without parentheses. If this option is turned on, then any instances where implicit parameter typing occurs will be warned about. If you want to be warned only in those instances where the implicit data type differs from the default type, use <code>-portability=param-implicit-type</code> instead. According to the Fortran 77 standard, the data type of a parameter is given by the same rules as for a variable, and if necessary a type conversion is done when the value is assigned.</p>
<dt><code>param-intrinsic</code>:</p>
<dd> Intrinsic function or exponentiation by a real used to define the value of a PARAMETER definition.</p>
<dt><code>param-noparen</code>:</p>
<dd> PARAMETER statement without parentheses. The user should be aware that the semantics of this form of the statement differs from that of the standard form: in this form, the parameter takes its data type from the value assigned, rather than having its default data type based on the first letter of the parameter name. (This form of the PARAMETER statement was introduced by DEC before the Fortran 77 standard was defined, and should be avoided.)</p>
<dt><code>pointer</code>:</p>
<dd> Fortran 90 standard pointer-related syntax, including POINTER, TARGET and ALLOCATABLE type declarations, ALLOCATE, DEALLOCATE, and NULLIFY statements, and pointer assignment using =&gt;.</p>
<dt><code>quad-constant</code>:</p>
<dd> Quad precision real constants, e.g. of the form 1.23Q4.</p>
<dt><code>quotemark</code>:</p>
<dd> Strings delimited by quote marks rather than apostrophes.</p>
<dt><code>relops</code>:</p>
<dd> Relational (comparison) operators composed of punctuation, namely: &lt; &lt;= == /= &gt; &gt;=.</p>
<dt><code>semicolon</code>:</p>
<dd> Semicolon used as statement separator.</p>
<dt><code>statement-order</code>:</p>
<dd> Statements out of the sequence mandated by the Standard. The allowed sequence is illustrated in Table 1 in the section on Interpreting the Output.</p>
<dt><code>typeless-constant</code>:</p>
<dd> Typeless constants, for example Z&#8217;19AF&#8217;.</p>
<dt><code>type-size</code>:</p>
<dd> Type declarations specifying a size, for example REAL*8.</p>
<dt><code>variable-format</code>:</p>
<dd> Variable repeat specification or field size in FORMAT. These are of the form &lt; <i>expr</i> &gt;.</p>
<dt><code>vms-io</code>:</p>
<dd> Obsolete. Now has the same meaning as the <code>io-keywords</code> keyword.</dl>
<p> See also: <code>-f90</code>, <code>-f95</code>, <code>-portability</code>, <code>-pretty</code>, <code>-style</code>, <code>-wordsize</code>.</dl>
<dt><code>-f90=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> This setting provides detailed control over the warnings about supported extensions to the Fortran 77 Standard that were not adopted as part of the Fortran 90 Standard. Note that <code>ftnchek</code> does not support the full Fortran 90 language. However, it does support some common extensions to Fortran 77 that were prevalent before Fortran 90 was defined. Some of these extensions became part of the Fortran 90 Standard, but others did not. The <code>-f90</code> setting warns only about the latter. That is, this flag covers things that are neither legal Fortran 77 nor legal Fortran 90. Therefore, the warnings controlled by this flag are basically a subset of the warnings controlled by <code>-f77</code>. There are a few cases, described below, where the circumstances in which the warning is given are slightly different for the two flags. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the warnings about nonstandard extensions, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-f90</code> is equivalent to <code>-f90=all</code>, and <code>-nof90</code> is equivalent to <code>-f90=none</code>. </p>
<p> The following keywords have identical meanings for <code>-f90</code> as for <code>-f77</code>. The reader is referred to the explanations under <code>-f77</code>. <center></p>
<table>
<tr VALIGN=top>
<td><code>accept-type</code></td>
<td><code>double-complex</code></td>
<td><code>param-noparen</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>backslash</code></td>
<td><code>format-dollarsign</code></td>
<td><code>cray-pointer</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>byte</code></td>
<td><code>format-edit-descr</code></td>
<td><code>quad-constant</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>cpp</code></td>
<td><code>function-noparen</code></td>
<td><code>type-size</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>d-comment</code></td>
<td><code>name-dollarsign</code></td>
<td><code>variable-format</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>dec-tab</code></td>
<td><code>param-implicit-type</code></td>
<td><code>vms-io</code>
</td>
</tr>
</table>
<p></center> </p>
<p> The keywords which differ somewhat from the corresponding <code>-f77</code> keywords are as follows.</p>
<dl>
<dt><code>continuation</code>:</p>
<dd> The limit on the number of continuation lines for a statement in fixed source form is the same, namely 19, in Fortran 90 as in Fortran 77. For free source form the limit is 39 continuation lines, and a line containing a continuation mark cannot be otherwise empty or contain only a comment.</p>
<dt><code>intrinsic</code>:</p>
<dd> This is the same as for <code>-f77</code> except for the intrinsic functions defined in MIL-STD 1753, which are all included in Fortran 90, and so are not warned about. (See <code>-intrinsic</code> for a list.)</p>
<dt><code>io-keywords</code>:</p>
<dd> This is the same as for <code>-f77</code> except that no warnings are given for the I/O keywords that are standard in Fortran 90.</p>
<dt><code>long-line</code>:</p>
<dd> Although the Fortran 90 Standard allows lines longer than 72 characters in free source form, this restriction still applies to fixed source form. In free source form the line length limit is 132 characters, and unlike fixed form, <code>ftnchek</code> does not allow this limit to be increased.</p>
<dt><code>mixed-expr</code>:</p>
<dd> This is the same as for <code>-f77</code> except for expressions mixing extended precision real with complex data types, which are permitted in Fortran 90.</p>
<dt><code>statement-order</code>:</p>
<dd> This is similar to the corresponding <code>-f77</code> warning, but applies the somewhat looser restrictions on statement order of the Fortran 90 Standard. In particular, Fortran 90 allows DATA statements and statement-function definitions to be intermixed with specification statements.</p>
<dt><code>typeless-constant</code>:</p>
<dd> In Fortran 90, binary, octal, and hexadecimal constants of the form B&#8217;ddd&#8217;, O&#8217;ddd&#8217;, and Z&#8217;ddd&#8217;, respectively, are permitted. Here &#8216;ddd&#8217; represents a string of digits. <code>ftnchek</code> recognizes these forms, as well as a variant of the form X&#8217;ddd&#8217; for a hexadecimal constant, and other variants in which the base indicator B, O, Z, or X follows the digit string. These variants were not adopted in Fortran 90, so only they are warned about when this flag is turned on.</dl>
<p> See also: <code>-f77</code>, <code>-f95</code>, <code>-portability</code>, <code>-pretty</code>, <code>-style</code>, <code>-wordsize</code>.</dl>
<dt><code>-f95=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> This setting provides detailed control over warnings about standard Fortran 77 features that were deleted from the Fortran 95 Standard. Unlike the <code>-f77</code> and <code>-f90</code> settings, these warnings apply to syntax which is legal Fortran 77. However, since these features have been deleted from the Standard, it is possible that programs containing them will be unacceptable to some newer compilers. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the warnings about nonstandard extensions, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-f95</code> is equivalent to <code>-f95=all</code>, and <code>-nof95</code> is equivalent to <code>-f95=none</code>. The warning keywords with their meanings are as follows.</p>
<dl>
<dt><code>real-do</code>:</p>
<dd> A DO variable of any real numeric type.</p>
<dt><code>pause</code>:</p>
<dd> The PAUSE statement.</p>
<dt><code>assign</code>:</p>
<dd> The ASSIGN statement, assigned GOTO, or assigned format.</p>
<dt><code>h-edit</code>:</p>
<dd> The H edit descriptor in a format.</dl>
<p> There is one other Fortran 77 syntax feature that was deleted in Fortran 95, namely branching to an ENDIF from outside the IF block. However, <code>ftnchek</code> is unable to analyze program flow, and so it does not provide a warning for this. </p>
<p> See also: <code>-f77</code>, <code>-f90</code>, <code>-portability</code>, <code>-pretty</code>, <code>-style</code>, <code>-wordsize</code>.</dl>
<dt><code>-help</code></p>
<dd>
<dl>
<dt>
<dd> Prints a list of all the command-line options with a short description of each along with its default value. This command is identical in function to the <code>&#8220;?&#8221;</code> argument, and is provided as a convenience for those systems in which the question mark has special meaning to the command interpreter. Default = no. </p>
<p> The help listing also prints the version number and patch level of <code>ftnchek</code> and a copyright notice. </p>
<p> Note: the &#8220;default&#8221; values printed in square brackets in the help listing are, strictly speaking, not the built-in defaults but the current values after any environment options and any command-line options preceding the <code>-help</code> option have been processed. </p>
<p> See also: <code>-novice</code>, <code>-version</code>, and <code>help</code> option of all settings that take a list of keywords.</dl>
<dt><code>-identifier-chars=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Define non-alphanumeric characters that may be used in identifiers. By default, <code>ftnchek</code> only accepts the dollar sign and underscore as non-alphanumeric characters in identifier names. The characters in the <i>list</i> replace whatever set of accepted non-alphanumeric characters was previously in effect. Thus, if dollar sign or underscore are not included in the list, they lose their status as acceptable characters. </p>
<p> This option is provided to enable <code>ftnchek</code> to handle source files containing non-standard identifer names that may be needed, for example, to access certain operating system services. See the section on Limitations and Extensions for the treatment of identifiers containing these characters in implicit typing. </p>
<p> Using <code>-noidentifer-chars</code> turns off acceptance of non-alphanumeric characters entirely. </p>
<p> See also: <code>-source</code>.</dl>
<dt><code>-include=</code><i>path</i></p>
<dd>
<dl>
<dt>
<dd> Specifies a directory to be searched for files specified by INCLUDE statements. Unlike other command-line options, this setting is cumulative; that is, if it is given more than once on the command line, all the directories so specified are placed on a list that will be searched in the same order as they are given. The order in which <code>ftnchek</code> searches for a file to be included is: the current directory; the directory specified by environment variable FTNCHEK_INCLUDE if any; the directories specified by any <code>-include</code> options; the directory specified by environment variable INCLUDE; and finally in a standard system-wide directory (/usr/include for UNIX, SYS$LIBRARY for VMS, and \include for MSDOS). </p>
<p> See also: <code>-f77</code>, <code>-source</code>.</dl>
<dt><code>-intrinsic=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Controls whether <code>ftnchek</code> recognizes certain nonstandard intrinsic functions as intrinsic. The <i>list</i> consists of keywords separated by commas or colons. Some of the keywords control whether to recognize certain groups of functions, and other keywords control the expected syntax for invoking some nonstandard intrinsics. Include a keyword to turn on recognition of the corresponding set of intrinsics or to allow the corresponding syntax. Include a keyword prefixed by <code>no-</code> to turn off that recognition. </p>
<p> There are three special keywords: <code>all</code> turns on recognition of all the nonstandard intrinsics (listed below) and accepts either syntax for those that have variations. Use <code>none</code> to turn off recognition of all nonstandard intrinsics except those noted below. Use <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-intrinsic</code> is equivalent to <code>-intrinsic=all</code>, and <code>-nointrinsic</code> is equivalent to <code>-intrinsic=none</code>. </p>
<p> The nonstandard intrinsic functions needed to support the nonstandard extended precision data types (double complex and quad precision) are always recognized. The intrinsics for the double complex data type are: <center></p>
<table>
<tr VALIGN=top>
<td>CDABS</td>
<td>CDSQRT</td>
<td>DREAL</td>
<td>ZLOG
</td>
</tr>
<tr VALIGN=top>
<td>CDCOS</td>
<td>DCMPLX</td>
<td>IMAG</td>
<td>ZSIN
</td>
</tr>
<tr VALIGN=top>
<td>CDEXP</td>
<td>DCONJG</td>
<td>ZABS</td>
<td>ZSQRT
</td>
</tr>
<tr VALIGN=top>
<td>CDLOG</td>
<td>DIMAG</td>
<td>ZEXP</td>
<td>ZCOS
</td>
</tr>
<tr VALIGN=top>
<td>CDSIN</td>
<td></td>
<td></td>
<td>
</td>
</tr>
</table>
<p></center> The intrinsics for the quad precision and quad complex types are: <center></p>
<table>
<tr VALIGN=top>
<td>CQABS</td>
<td>QARCOS</td>
<td>QEXT</td>
<td>QNINT
</td>
</tr>
<tr VALIGN=top>
<td>CQCOS</td>
<td>QARSIN</td>
<td>QEXTD</td>
<td>QPROD
</td>
</tr>
<tr VALIGN=top>
<td>CQEXP</td>
<td>QATAN</td>
<td>QFLOAT</td>
<td>QREAL
</td>
</tr>
<tr VALIGN=top>
<td>CQLOG</td>
<td>QATAN2</td>
<td>QIMAG</td>
<td>QSIGN
</td>
</tr>
<tr VALIGN=top>
<td>CQSIN</td>
<td>QCMPLX</td>
<td>QINT</td>
<td>QSIN
</td>
</tr>
<tr VALIGN=top>
<td>CQSQRT</td>
<td>QCONJG</td>
<td>QLOG</td>
<td>QSINH
</td>
</tr>
<tr VALIGN=top>
<td>DBLEQ</td>
<td>QCOS</td>
<td>QLOG10</td>
<td>QSQRT
</td>
</tr>
<tr VALIGN=top>
<td>IQINT</td>
<td>QCOSH</td>
<td>QMAX1</td>
<td>QTAN
</td>
</tr>
<tr VALIGN=top>
<td>IQNINT</td>
<td>QDIM</td>
<td>QMIN1</td>
<td>QTANH
</td>
</tr>
<tr VALIGN=top>
<td>QABS</td>
<td>QEXP</td>
<td>QMOD</td>
<td>SNGLQ
</td>
</tr>
</table>
<p></center> The keywords controlling recognition of other nonstandard intrinsic functions are as follows:</p>
<dl>
<dt><code>extra</code>:</p>
<dd> recognize the following commonly available nonstandard intrinsics (all except EXIT and LOC are defined in MIL-STD 1753): <center></p>
<table>
<tr VALIGN=top>
<td>BTEST</td>
<td>IBCLR</td>
<td>IEOR</td>
<td>ISHFTC
</td>
</tr>
<tr VALIGN=top>
<td>EXIT</td>
<td>IBITS</td>
<td>IOR</td>
<td>LOC
</td>
</tr>
<tr VALIGN=top>
<td>IAND</td>
<td>IBSET</td>
<td>ISHFT</td>
<td>NOT
</td>
</tr>
</table>
<p></center></p>
<dt><code>unix</code>:</p>
<dd> recognize these common Unix-specific intrinsic functions: <center></p>
<table>
<tr VALIGN=top>
<td>ABORT</td>
<td>GMTIME</td>
<td>LTIME</td>
<td>SRAND
</td>
</tr>
<tr VALIGN=top>
<td>AND</td>
<td>IARGC</td>
<td>OR</td>
<td>SYSTEM
</td>
</tr>
<tr VALIGN=top>
<td>GETARG</td>
<td>IRAND</td>
<td>RAND</td>
<td>TIME
</td>
</tr>
<tr VALIGN=top>
<td>GETENV</td>
<td>LSHIFT</td>
<td>RSHIFT</td>
<td>XOR
</td>
</tr>
</table>
<p></center></p>
<dt><code>vms</code>:</p>
<dd> recognize these common VMS-specific intrinsic functions: <center></p>
<table>
<tr VALIGN=top>
<td>DATE</td>
<td>IDATE</td>
<td>SECNDS</td>
<td>TIME
</td>
</tr>
<tr VALIGN=top>
<td>ERRSNS</td>
<td>RAN</td>
<td>SIZEOF</td>
<td>
</td>
</tr>
</table>
<p></center></p>
<dt><code>iargc-no-argument</code>:</p>
<dd> specify that IARGC may be invoked with no arguments.</p>
<dt><code>iargc-one-argument</code>:</p>
<dd> specify that IARGC may be invoked with one argument.</p>
<dt><code>rand-no-argument</code>:</p>
<dd> specify that RAND and IRAND may be invoked with no arguments.</p>
<dt><code>rand-one-argument</code>:</p>
<dd> specify that RAND and IRAND may be invoked with one argument.</dl>
<p> The <code>no-argument</code> and <code>one-argument</code> keywords work as follows: turning the option on causes <code>ftnchek</code> to accept the corresponding syntax for invocation of the function, without excluding the possibility of the alternative syntax. Turning the option off causes the corresponding syntax not to be accepted. If both options are turned on at once (the default), then either syntax is accepted. Turning both options off at once would not be meaningful. These options have no effect if recognition of Unix intrinsics has been turned off. </p>
<p> Note that this setting does not control whether non-standard warnings are issued about these functions. It controls whether the functions are assumed to be intrinsic or not, which determines how their usage is checked. When functions in any of these sets are included, their invocations will be checked according to the rules for the intrinsic functions; otherwise they will be checked as normal (user-written) external functions. The non-standard warnings are controlled by the <code>-f77=intrinsic</code> option. </p>
<p> The default value of this setting is equivalent to <code>-intrinsic=all</code> followed by <code>-intrinsic=no-vms</code> for the Unix version, <code>-intrinsic=no-unix</code> for the VMS version, and <code>-intrinsic=no-unix,no-vms</code> for other versions. </p>
<p> Note: In versions of <code>ftnchek</code> prior to 2.10, the <code>-intrinsic</code> flag took a numeric argument instead of a list of options. For the sake of users who may have written scripts invoking <code>ftnchek</code> in this way, the numeric form is still accepted. The numeric form of the setting consists of three digits. The ones digit selects the set of intrinsic functions to be supported. The digit 0 selects only Fortran 77 standard intrinsics plus those needed to support the nonstandard extended precision data types. The digit 1 is equivalent to <code>extra</code>, 2 is equivalent to <code>extra,unix</code>, and 3 is equivalent to <code>extra,vms</code>. The tens digit of this setting controls the syntax of the RAND intrinsic function, and the hundreds digit controls the syntax of the IARGC function. For these digits, specify 0 to require invocation with no argument, 1 to require one argument, and 2 to allow either form. </p>
<p> See also: <code>-f77</code>.</dl>
<dt><code>-library</code></p>
<dd>
<dl>
<dt>
<dd> This switch is used when a number of subprograms are contained in a file, but not all of them are used by the application. Normally, <code>ftnchek</code> warns you if any subprograms are defined but never used. This switch will suppress these warnings. Default = no. </p>
<p> This switch also controls which subprogram calls and COMMON block declarations are checked. If a file is read with the <code>-library</code> flag in effect, the subprogram calls and COMMON declarations contained in a routine in that file will be checked only if that routine is in the main program&#8217;s call tree. On the other hand, if the <code>-library</code> switch is turned off, then <code>ftnchek</code> checks the calls of every routine by every other routine, regardless of whether those routines could ever actually be invoked at run time, and likewise all COMMON block declarations are compared for agreement. </p>
<p> The difference between this switch and the <code>-usage=no-ext-unused</code> option for subprograms is that the latter suppresses only the warning about routines being declared but not used. The <code>-library</code> switch goes further and excludes unused routines processed while it is in effect from all cross-checking of arguments and COMMON block declarations as well. </p>
<p> (If there is no main program anywhere in the set of files that <code>ftnchek</code> has read, so that there is no call tree, then <code>ftnchek</code> will look for any non-library routines that are not called by any other routine, and use these as substitutes for the main program in constructing the call tree and deciding what to check. If no such top-level non-library routines are found, then all inter-module calls and all COMMON declarations will be checked.) </p>
<p> See also: <code>-arguments</code>, <code>-calltree</code>, <code>-common</code>, <code>-extern</code>, <code>-usage</code>.</dl>
<dt><code>-list</code></p>
<dd>
<dl>
<dt>
<dd> Specifies that a listing of the Fortran program is to be printed out with line numbers. If <code>ftnchek</code> detects an error, the error message follows the program line with a caret ( ^ ) specifying the location of the error. If no source listing was requested, <code>ftnchek</code> will still print out any line containing an error, to aid the user in determining where the error occurred. Default = no. </p>
<p> See also: <code>-output</code>, B-symtab, fB-quiet.</dl>
<dt><code>-makedcls=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Prepare a neatly-formatted file of declarations of variables, common blocks, and namelist lists, for possible merging into the source code. The declarations are stored in a file of the same name as the source code, but with the extension changed to <i>.dcl</i>. If no declarations are written to the file, it is deleted to reduce clutter from empty files. </p>
<p> If input comes from standard input, instead of a named file, then declarations are written to standard output. </p>
<p> Variables are declared in alphabetical order within each declaration class and type, with integer variables first, because of their later possible use in array dimensions. </p>
<p> PARAMETER statements are an exception to the alphabetical order rule, because the Fortran 77 Standard requires that the expressions defining parameter values refer only to constants and already-defined parameter names. This forces the original source file order of such statements to be preserved in the declaration files. </p>
<p> Explicit declaration of <i>all</i> variables is considered good modern programming practice. By using compiler options to reject undeclared variables, misspelled variable names (or names extending past column 72) can be caught at compile time. Explicit declarations also greatly facilitate changing floating-point precision with filters such as <code><a href="//www.systutorials.com/docs/linux/man/1L-dtoq/">dtoq</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-dtos/">dtos</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-fd2s/">fd2s</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-fs2d/">fs2d</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-qtod/">qtod</a></code>(1L), and <code><a href="//www.systutorials.com/docs/linux/man/1L-stod/">stod</a></code>(1L). These programs are capable of changing types of explicit floating-point type declarations, intrinsic functions, and constants, but because they do not carry out rigorous lexical and grammatical analysis of the Fortran source code, they cannot provide modified type declarations for undeclared variables. Default setting = 0, turn-on = 1. </p>
<p> Various options for the form of the declarations file are controlled by the <i>list</i>, which consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the options, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-makedcls</code> is equivalent to <code>-makedcls=declarations</code> (i.e. produce the declarations file using the default options), and <code>-nomakedcls</code> is equivalent to <code>-makedcls=none</code>. </p>
<p> For compatibility with previous versions of <code>ftnchek</code>, a numeric form of this setting is also accepted: the <i>list</i> is replaced by a number which is the sum of the numbers in parentheses beside the keywords in the following list. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>declarations</code> (1):</p>
<dd> Write a declaration file. (This is implied by any of the other options, and can be omitted if any other options are given.)</p>
<dt><code>undeclared-only</code> (2):</p>
<dd> By default, all variables are included in the declaration file. With this option, include only <i>undeclared</i> variables. This setting is useful if you want to check for undeclared variables, since Fortran source files with all variables properly declared will not result in a <i>.dcl</i> file. With this option, common blocks and namelist lists will not be included in the declaration file, since by their nature they cannot be undeclared.</p>
<dt><code>compact</code> (4):</p>
<dd> The declarations are normally prettyprinted to line up neatly in common columns, as in the declaration files output by the Extended PFORT Verifier, <code><a href="//www.systutorials.com/docs/linux/man/1L-pfort/">pfort</a></code>(1L). This option value selects instead compact output, without column alignment.</p>
<dt><code>use-continuation-lines</code> (8):</p>
<dd> Causes continuation lines to be used where permissible. The default is to begin a new declaration on each line. This option is appropriate to use together with <code>compact</code>.</p>
<dt><code>keywords-lowercase</code> (16):</p>
<dd> Output Fortran keywords in lowercase, instead of the default uppercase.</p>
<dt><code>vars-and-consts-lowercase</code> (32):</p>
<dd> Output variables and constants in lowercase, instead of the default uppercase. Character string constants are not affected by this option.</p>
<dt><code>exclude-sftran3</code> (64):</p>
<dd> Omit declarations of internal integer variables produced by the SFTRAN3 preprocessor, <code><a href="//www.systutorials.com/docs/linux/man/1L-xsf3/">xsf3</a></code>(1L), as part of the translation of structured Fortran statements to ordinary Fortran. These variables have six-character names of the form <i>NPRddd</i>, <i>NXdddd</i>, <i>N2dddd</i>, and <i>N3dddd</i>, where <i>d</i> is a decimal digit. Because they are invisible in the SFTRAN3 source code, and will change if the SFTRAN3 code is modified, such variables should not be explicitly declared. Instead, they should just assume the default Fortran INTEGER data type based on their initial letter, <i>N</i>.</p>
<dt><code>asterisk-comment</code> (128):</p>
<dd> Use an asterisk as the comment character; the default is otherwise &#8216;C&#8217;.</p>
<dt><code>comment-char-lowercase</code> (256):</p>
<dd> Use &#8216;c&#8217; instead of &#8216;C&#8217; or &#8216;*&#8217; as the comment character.</p>
<dt><code>suppress-array-dimensions</code> (512):</p>
<dd> Suppress dimensioning of arrays in the generated declarations. This option is for use with code lacking type declarations, to allow the declaration files to be inserted without change into the code. Since the code will have dimension statements already, dimensioning the array variables in the type statements of the declaration file is redundant. This option should be used only in conjunction with option 2 = undeclared-only because otherwise any arrays that were dimensioned in a type statement will lose their dimensioning.</p>
<dt><code>free-form</code> (1024):</p>
<dd> Produce declarations in free source form. This mode is automatically used if the input source is free form. Use this option to produce declarations in free form even if the input is in fixed form. Free form declarations are indented only 2 columns instead of 6, use the exclamation mark as the comment character, and indicate continuation lines by an ampersand at the end of the line to be continued.</dl>
<p> The declaration files contain distinctive comments that mark the start and end of declarations for each program unit, to facilitate using text editor macros for merging the declarations back into the source code. </p>
<p> The <code>ftnchek</code> distribution includes a program, <code>dcl2inc</code>, which processes declaration files to produce files containing declarations of all COMMON blocks, in a form suitable for use as INCLUDE files. See the <code><a href="//www.systutorials.com/docs/linux/man/1L-dcl2inc/">dcl2inc</a></code>(1L) man page for the details of its use. </p>
<p> See also: <code>-mkhtml</code>.</dl>
<dt><code>-mkhtml=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Produce HTML documentation from source. Creates individual HTML files from ftnchek analysis and code comments. All comments immediately preceding and following the function or subroutine definition are captured to the HTML file. No reformatting of source comments is performed other than stripping of FORTRAN comment characters. In addition, the HTML file lists the local variables declared, common block variables used, functions and subroutines called, I/O unit usage, and other information about each subprogram. Usually you will also want to specify <code>-call=tree</code> to create the root HTML file CallTree.html. (Perhaps this file should be named index.html.) </p>
<p> Various options for the form of the HTML files are controlled by the <i>list</i>, which consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the options, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-mkhtml</code> is equivalent to <code>-mkhtml=documents</code> (i.e. produce the HTML document files using the default options), and <code>-nomkhtmls</code> is equivalent to <code>-mkhtml=none</code>. </p>
<p> For the sake of simplicity, the options for <code>-mkhtml</code> are the same as those for <code>-makedcls</code> except for those that are inapplicable. Likewise, a numeric form of this setting can be used, formed as the sum of the numbers in parentheses in the list below. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>documents</code> (1):</p>
<dd> Create the HTML documents. (This is implied by any of the other options, and can be omitted if any other options are given.)</p>
<dt><code>compact</code> (4):</p>
<dd> The declarations are normally prettyprinted to line up neatly in common columns. This option value selects instead compact output, without column alignment.</p>
<dt><code>use-continuation-lines</code> (8):</p>
<dd> Causes continuation lines to be used instead of beginning a new declaration on each line. This option is appropriate to use together with <code>compact</code>.</p>
<dt><code>keywords-lowercase</code> (16):</p>
<dd> Output Fortran keywords in lowercase, instead of the default uppercase.</p>
<dt><code>vars-and-consts-lowercase</code> (32):</p>
<dd> Output variables and constants in lowercase, instead of the default uppercase. Character string constants are not affected by this option.</p>
<dt><code>exclude-sftran3</code> (64):</p>
<dd> Omit declarations of internal integer variables produced by the SFTRAN3 preprocessor, <code><a href="//www.systutorials.com/docs/linux/man/1L-xsf3/">xsf3</a></code>(1L). (See <code>-makedcls</code> for discussion.)</p>
<dt><code>suppress-array-dimensions</code> (512):</p>
<dd> Suppress dimensioning of arrays in the generated declarations. This is normally undesirable, but is available if for some reason you do not want the array dimensions to appear in the HTML.</p>
<dt><code>free-form</code> (1024):</p>
<dd> Produce variable declarations in free source form. This mode is automatically used if the input source is free form. This mainly affects the form of continuation lines if they are used.</dl>
<p> See also: <code>-calltree</code>, <code>-makedcls</code>.</dl>
<dt><code>-novice</code></p>
<dd>
<dl>
<dt>
<dd> This flag is intended to provide more helpful output for beginners. It has two effects:</p>
<dl>
<dt>(a)</p>
<dd> provides an extra message to the effect that a function that is used but not defined anywhere might be an array which the user forgot to declare in a DIMENSION statement (since the syntax of an array reference is the same as that of a function reference).</p>
<dt>(b)</p>
<dd> modifies the form of the error messages and warnings. If the flag is turned off by <code>-nonovice</code>, these messages are printed in a style more resembling UNIX <code>lint</code>.</dl>
<p> Default = yes.</dl>
<dt><code>-output=</code><i>filename</i></p>
<dd> This setting is provided for convenience on systems which do not allow easy redirection of output from programs. When this setting is given, the output which normally appears on the screen will be sent instead to the named file. Note, however, that operational errors of <code>ftnchek</code> itself (e.g. out of space or cannot open file) will still be sent to the screen. The extension for the filename is optional, and if no extension is given, the extension <i>.lis</i> will be used. </p>
<dt><code>-pointersize=</code><i>num</i></p>
<dd>
<dl>
<dt>
<dd> Specifies the size of a &#8220;Cray pointer&#8221; variable to be <i>num</i> bytes. Default = turn-on = 4 bytes. </p>
<p> The pointer size is used to inform precision mismatch warnings involving pointer variables, for example when a pointer is assigned a value from an allocation routine, or passed as a subprogram parameter. </p>
<p> See also: <code>-f77</code>, <code>-portability</code>, <code>-truncation</code>, <code>-wordsize</code>.</dl>
<dt><code>-portability=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> <code>ftnchek</code> will give warnings for a variety of non-portable usages. Examples include the use of tabs except in comments or inside strings, the use of Hollerith constants, and the equivalencing of variables of different data types. This option does not produce warnings for supported extensions to the Fortran 77 Standard, which may also cause portability problems. To catch those, use the <code>-f77</code> setting. By default, all warnings are turned off. </p>
<p> This setting provides detailed control over the warnings about possible portability problems. The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the warnings about nonportable usages, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-portability</code> is equivalent to <code>-portability=all</code>, and <code>-noportability</code> is equivalent to <code>-portability=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>backslash</code>:</p>
<dd> Backslash character in strings. Since some compilers treat the backslash as an escape character, its presence can cause problems even though it is used in a standard-conforming way.</p>
<dt><code>common-alignment</code>:</p>
<dd> COMMON block variables not in descending order of storage size. Some compilers require this ordering because of storage alignment requirements.</p>
<dt><code>hollerith</code>:</p>
<dd> Hollerith constants (other than within FORMAT specifications). The Hollerith data type is a feature of Fortran IV that has been deleted in the Fortran 77 standard. It is superseded by the character data type. Storing Hollerith data in variables of a numeric or logical data type is nonportable due to differing word sizes.</p>
<dt><code>long-string</code>:</p>
<dd> String constants, variables, or expressions over 255 chars long.</p>
<dt><code>mixed-equivalence</code>:</p>
<dd> Variables of different data types equivalenced.</p>
<dt><code>mixed-size</code>:</p>
<dd> Variables declared with default precision used with variables given explicit precision, in expressions, assignments, or as arguments. For example, if a variable declared as REAL*8 is treated as equivalent to DOUBLE PRECISION.</p>
<dt><code>real-do</code>:</p>
<dd> Non-integer DO loop index and bounds. These can cause a program&#8217;s results to depend on the hardware characteristics of the particular computer used.</p>
<dt><code>param-implicit-type</code>:</p>
<dd> Implicit typing of a parameter by the data type of the value assigned, if it differs from the default type. This warning can only occur if implicit parameter typing has been turned on by the <code>-source=param-implicit-type</code> option, or if the PARAMETER statement is of the nonstandard form without parentheses. If this option is turned on, then any instances where implicit parameter typing occurs and where the implicit type is different from the default type based on the first letter of the parameter name, will be warned about. Implicit parameter typing can change the semantics of statements where the parameter is used, causing portability problems.</p>
<dt><code>tab</code>:</p>
<dd> Tabs in source code. Tabs are interpreted differently by different compilers. This warning will be given only once, at the end of the file.</dl>
<p> See also: <code>-f77</code>, <code>-f90</code>, <code>-f95</code>, <code>-pretty</code>, <code>-style</code>, <code>-wordsize</code>.</dl>
<dt><code>-pretty=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Controls certain messages related to the appearance of the source code. These warn about things that might make a program less readable or be deceptive to the reader. By default, all warnings are turned on. </p>
<p> This setting provides detailed control over the warnings about appearance. The <i>list</i> consists of keywords separated by commas or colons. Since all warnings are on by default, include a keyword prefixed by <code>no-</code> to turn off a particular warning. There are three special keywords: <code>all</code> to turn on all the warnings about misleading appearances, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-pretty</code> is equivalent to <code>-pretty=all</code>, and <code>-nopretty</code> is equivalent to <code>-pretty=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>alternate-return</code>:</p>
<dd> A RETURN statement has a constant specifying an alternate return point that is not between 0 and the number of dummy arguments that are labels. This is legal, and has the same effect as a RETURN with no alternate return expression, but suggests that the programmer intended to use an alternate return label that is not provided.</p>
<dt><code>embedded-space</code>:</p>
<dd> Space embedded in variable names or in multi-character operators such as **.</p>
<dt><code>continuation</code>:</p>
<dd> Continuation mark following a comment line.</p>
<dt><code>long-line</code>:</p>
<dd> Lines (except comments) over 72 columns in width (beyond 72 is normally ignored by compiler).</p>
<dt><code>missing-space</code>:</p>
<dd> Lack of space between variable and a preceding keyword.</p>
<dt><code>multiple-common</code>:</p>
<dd> COMMON block declared in multiple statements. No warning is given if the statements are consecutive except for comment lines.</p>
<dt><code>multiple-namelist</code>:</p>
<dd> NAMELIST declared in multiple statements. No warning is given if the statements are consecutive except for comment lines.</p>
<dt><code>parentheses</code>:</p>
<dd> Parentheses around a variable by itself. As a subprogram argument, this makes the argument an expression, not modifiable by the subprogram.</dl>
<p> Note that in free source form, extra space and missing space are forbidden by the Fortran 90 Standard, and are not mere style violations. In this case the warnings are replaced by syntax error messages, and can be turned off only by using <code>-nocheck</code>. </p>
<p> See also: <code>-f77</code>, <code>-portability</code>, <code>-style</code>.</dl>
<dt><code>-project=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> <code>ftnchek</code> will create a project file from each source file that is input while this option is turned on. The project file will be given the same name as the input file, but with the extension <i>.f</i> or <i>.for</i> replaced by <i>.prj</i>. (If input is from standard input, the project file is named <i>ftnchek.prj</i>.) Default = none. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the options, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-project</code> is equivalent to <code>-project=all</code>, and <code>-noproject</code> is equivalent to <code>-project=none</code>. The keywords with their meanings are as follows:</p>
<dl>
<dt><code>create</code>:</p>
<dd> Produce a project file. The default is not to produce a project file. If this option is not turned on, the other options have no effect.</p>
<dt><code>trim-calls</code>:</p>
<dd> Trim the amount of information stored in the project file about subprogram declarations and calls. This is the default. Turn this option off only in rare situations. (See discussion below.) The amount of trimming varies depending on the <code>-library</code> flag. More information is trimmed if that flag is turned on.</p>
<dt><code>trim-common</code>:</p>
<dd> Trim the number of common block declarations stored in the project file. This is the default. Turn this option off only in rare situations. (See discussion below.) This option has no effect if the <code>-library</code> flag is turned off: when not in library mode, no trimming of common block declarations is done regardless of this option.</dl>
<p> A project file contains a summary of information from the source file, for use in checking agreement among FUNCTION, SUBROUTINE, and COMMON usages in other files. It allows incremental checking, which saves time whenever you have a large set of files containing shared subroutines, most of which seldom change. You can run <code>ftnchek</code> once on each file with the <code>-project</code> flag set, creating the project files. Usually you would also set the <code>-library</code> and <code>-noextern</code> flags at this time, to suppress messages relating to consistency with other files. Only error messages pertaining to each file by itself will be printed at this time. Thereafter, run <code>ftnchek</code> without these flags on all the project files together, to check consistency among the different files. All messages internal to the individual files will now be omitted. Only when a file is altered will a new project file need to be made for it. </p>
<p> Naturally, when the <code>-project</code> option is turned on, <code>ftnchek</code> will not read project files as input. </p>
<p> Ordinarily, the trim options should be left on when you intend to create project files for future input to <code>ftnchek</code>. Since trimming is on by default, this means that simply giving the command <code>-project</code> with no option list is the recommended mode. The trim options are provided only as a convenience for those who want to make use of project files for purposes other than checking the program with <code>ftnchek</code>. To use project files for their intended purpose, the trim options should not be turned off. </p>
<p> Project files contain only information needed for checking agreement between files. This means that a project file is of no use if all modules of the complete program are contained in a single file. </p>
<p> A more detailed discussion is given in the section on Using Project Files.</dl>
<dt><code>-pure</code></p>
<dd>
<dl>
<dt>
<dd> Assume functions are &#8220;pure&#8221;, i.e., they will not have side effects by modifying their arguments or variables in a COMMON block. When this flag is in effect, <code>ftnchek</code> will base its determination of set and used status of the actual arguments on the assumption that arguments passed to a function are not altered. It will also issue a warning if a function is found to modify any of its arguments or any COMMON variables. Default = yes. </p>
<p> When this flag is turned off, actual arguments passed to functions will be handled the same way as actual arguments passed to subroutines. This means that <code>ftnchek</code> will assume that arguments may be modified by the functions. No warnings will be given if a function is found to have side effects. Because stricter checking is possible if functions are assumed to be pure, you should turn this flag off only if your program actually uses functions with side effects.</dl>
<dt><code>-quiet</code></p>
<dd>
<dl>
<dt>
<dd> This option reduces the amount of output relating to normal operation, so that error messages are more apparent. This option is provided for the convenience of users who are checking large suites of files. The eliminated output includes the names of project files, and the message reporting that no syntax errors were found. It also eliminates some blank lines that are ordinarily included for clarity. (Some of this output is turned back on by the <code>-list</code> and <code>-symtab</code> options.) Default = no. </p>
<p> Note: the way to remember the difference between the <code>-quiet</code> and <code>-brief</code> is that <code>-quiet</code> doesn&#8217;t suppress any warning-related information, whereas <code>-brief</code> does. </p>
<p> See also: <code>-brief</code>.</dl>
<dt><code>-reference</code></p>
<dd>
<dl>
<dt>
<dd> Specifies that a who-calls-who table be printed. This table lists each subprogram followed by a list of the routines it calls. This switch is equivalent to <code>-calltree=reference</code>. Default = no. </p>
<p> The reference list omits routines called by unused library modules. Thus it contains the same information as for the call-tree format, namely the hierarchy of subprogram calls, but printed in a different way. This prints out a breadth-first traversal of the call tree whereas <code>-calltree=tree</code> prints out a depth-first traversal. </p>
<p> See also: <code>-calltree</code>, <code>-crossref</code>, <code>-library</code>, <code>-sort</code>, <code>-symtab</code>, <code>-vcg</code>.</dl>
<dt><code>-resources</code></p>
<dd>
<dl>
<dt>
<dd> Prints the amount of resources used by <code>ftnchek</code> in processing the program. This listing may be useful in analyzing the size and complexity of a program. It can also help in choosing larger sizes for <code>ftnchek</code>&#8216;s internal tables if they are too small to analyze a particular program. Default = no. </p>
<p> In this listing, the term &#8220;chunk size&#8221; is the size of the blocks of memory allocated to store the item in question, in units of the size of one item, not necessarily in bytes. When the initially allocated space is filled up, more memory is allocated in chunks of this size. The following is an explanation of the items printed:</p>
<dl>
<dt><i>Source lines processed:</i></p>
<dd> Total number of lines of code, with separate totals for statement lines and comment lines. Comment lines include lines with &#8216;C&#8217; or &#8216;*&#8217; in column 1 as well as blank lines and lines containing only an inline comment. Statement lines are all other lines, including lines that have an inline comment following some code. Continuation lines are counted as separate lines. Lines in include files are counted each time the file is included.</p>
<dt><i>Total executable statements:</i></p>
<dd> Number of statements in the program, other than specification, data, statement-function, FORMAT, ENTRY, and END statements.</p>
<dt><i>Total number of modules:</i></p>
<dd> A module is any external subprogram, including the main program, subroutines, functions, and block data units. This count is of modules defined within the source, not modules referenced. Statement functions are not included. A subprogram with multiple entry points is only counted once.</p>
<dt><i>Total statement labels defined</i></p>
<dd> Number of labels attached to statements (often called statement numbers). The total label count for the entire program is given, as well as the maximum number in any single subprogram.</p>
<dt><i>Max identifier name chars:</i></p>
<dd> Number of characters used for storing identifier names. An identifier is a variable, subprogram, or common block name. Local names are those of local variables in a subprogram, whereas global names refer to subprogram and common block names, as well as dummy argument names and common variable names. Actual argument text (up to 15 characters for each argument) is also included here. The space used for local names is not recovered at the end of each module, so this number, like global space, grows until the whole program is analyzed. Unfortunately, this figure may include some text stored more than once, although a heuristic is used that will avoid duplicates in many cases.</p>
<dt><i>Max token text chars:</i></p>
<dd> A token is the smallest syntactic unit of the FORTRAN language above the level of individual characters. For instance a token can be a variable name, a numerical constant, a quoted text string, or a punctuation character. Token text is stored while a module is being processed. For technical reasons, single-character tokens are not included in this total. Items that are not represented in the symbol table may be duplicated. The space for token text is recovered at the end of each module, so this figure represents the maximum for any one module.</p>
<dt><i>Max local symbols:</i></p>
<dd> This is the largest number of entries in the local symbol table for any module. Local symbol table entries include all variables and parameters, common block names, statement functions, external subprograms and intrinsic functions referenced by the module. Literal constants are not stored in the local symbol table.</p>
<dt><i>Max global symbols:</i></p>
<dd> This is the number of entries in the global symbol table at the end of processing. Global symbol table entries include external subprogram and common block names. Intrinsic functions and statement functions are not included.</p>
<dt><i>Max number of tokenlists:</i></p>
<dd> A token list is a sequence of tokens representing the actual or dummy argument list of a subprogram, or the list of variables in a common block or namelist. Therefore this number represents the largest sum of COMMON, CALL, NAMELIST and ENTRY statements and function invocations for any one module. The space is recovered at the end of each module.</p>
<dt><i>Max token list/tree space:</i></p>
<dd> This is the largest number of tokens in all the token lists and token trees of any one module. A token tree is formed when analyzing an expression: each operand is a leaf of the tree, and the operators are the nodes. Therefore this number is a measure of the maximum complexity of an individual module. For instance a module with many long arithmetic expressions will have a high number. Note that unlike token text described above, the number of tokens is independent of the length of the variable names or literal constants in the expressions.</p>
<dt><i>Number of subprogram invocations:</i></p>
<dd> This is the sum over all modules of the number of CALL statements and function invocations (except intrinsic functions and statement functions).</p>
<dt><i>Number of common block decls:</i></p>
<dd> This is the sum over all modules of the number of common block declarations. That is, each declaration of a block in a different module is counted separately. (The standard allows multiple declarations of a block within the same module; these are counted as only one declaration since they are equivalent to a single long declaration.)</p>
<dt><i>Number of array dim &amp; param ptrs:</i></p>
<dd> This is the sum over all modules of the number of array dimension and parameter definition text strings saved for use by the <code>-makedcls</code> option. The length of the text strings is not counted. Each dimension of a multidimensional array is counted separately.</dl>
<p> These numbers are obviously not the same when project files are used in place of the original source code. Even the numbers for global entities may be different, since some redundant information is eliminated in project files.</dl>
<dt><code>-sixchar</code></p>
<dd>
<dl>
<dt>
<dd> One of the goals of the <code>ftnchek</code> program is to help users to write portable Fortran programs. One potential source of nonportability is the use of variable names that are longer than six characters. Some compilers just ignore the extra characters. This behavior could potentially lead to two different variables being considered as the same. For instance, variables named AVERAGECOST and AVERAGEPRICE are the same in the first six characters. If you wish to catch such possible conflicts, use this flag. Default = no. </p>
<p> Use the <code>-f77=long-names</code> if you want to list <i>all</i> variables longer than six characters, not just those pairs that are the same in the first six. </p>
<p> See also: <code>-f77</code>, <code>-portability</code>.</dl>
<dt><code>-sort</code></p>
<dd>
<dl>
<dt>
<dd> Specifies that a sorted list of all modules used in the program be printed. This list is in &#8220;prerequisite&#8221; order, i.e. each module is printed only after all the modules from which it is called have been printed. This is also called a &#8220;topological sort&#8221; of the call tree. Each module is listed only once. Routines that are not in the call tree of the main program are omitted. If there are any cycles in the call graph (illegal in standard Fortran) they will be detected and diagnosed. Default = no. </p>
<p> See also: <code>-calltree</code>, <code>-crossref</code>, <code>-reference</code>, <code>-symtab</code>, <code>-vcg</code>.</dl>
<dt><code>-source=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> This setting controls certain options about the form of the Fortran source code. The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the options, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-source</code> is equivalent to <code>-source=all</code>, and <code>-nosource</code> is equivalent to <code>-source=none</code>. </p>
<p> For compatibility with previous versions of <code>ftnchek</code>, a numeric form of this setting is also accepted: the <i>list</i> is replaced by a number which is the sum of the numbers in parentheses beside the keywords in the following list. (The <code>fixed</code> and <code>free</code> options do not have numeric values.) The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>fixed</code>:</p>
<dd> Interpret the source as fixed form (with supported extensions such as exclamation mark for comments). Statements must be in columns 7 to 72 (unless the <code>-cols</code> setting has been used to change this), and blanks are not significant outside character context (but warned about under the <code>-pretty</code> option). This is the default mode unless the source file extension is <i>.f90</i> or <i>.F90</i>. this option cannot be given together with <code>-source=free</code>.</p>
<dt><code>free</code>:</p>
<dd> Interpret the source as free form. Statements may be anywhere in columns 1 to 132, comments can only begin with an exclamation mark, and blanks are required in some places such as between identifiers and keywords. This is the default mode if the source file extension is <i>.f90</i> or <i>.F90</i>. This option cannot be given together with <code>-source=fixed</code> or <code>-source=dec-tab</code></p>
<dt><code>dec-tab</code> (1):</p>
<dd> Accept DEC-style tab-formatted source. A line beginning with an initial tab will be treated as a new statement line unless the character after the tab is a nonzero digit, in which case it is treated as a continuation line. The next column after the tab or continuation mark is taken as column 7. A warning will be given in the case where the line is a continuation, if <code>-f77=dec-tab</code> is in effect.</p>
<dt><code>vms-include</code> (2):</p>
<dd> Accept VMS-style INCLUDE statements. These follow the normal syntax, but with the following additional features: (1) the file extension, if not given, defaults to the same as a normal source file extension; and (2) the option /LIST or /NOLIST can be appended to the include-file name, to control listing of its contents.</p>
<dt><code>unix-backslash</code> (4):</p>
<dd> Handle UNIX-style backslash escapes in character strings. The escape sequence following the backslash will be evaluated according to the ANSI standard for strings in C: up to three digits signify an octal value, an x signifies the start of a hexadecimal constant, any of the letters a b f n r t signify special control codes, and any other character (including newline) signifies the character itself. When this source code option is in effect, a warning will be given if the <code>-f77=backslash</code> setting is specified.</p>
<dt>
<dd> The default behavior is to treat the backslash like any other normal character, but a warning about portability will be generated if the <code>-portability</code> flag is set. Because of the fact that some compilers treat the backslash in a nonstandard way, it is possible for standard-conforming programs to be non-portable if they use the backslash character in strings.</p>
<dt>
<dd> Since <code>ftnchek</code> does not do much with the interpreted string, it is seldom necessary to use this option. It is needed in order to avoid spurious warnings only if (a) the program being checked uses backslash to embed an apostrophe or quote mark in a string instead of using the standard mechanism of doubling the delimiter; (b) the backslash is used to escape the end-of-line in order to continue a string across multiple source lines; or (c) a PARAMETER definition uses an intrinsic string function such as LEN with such a string as argument, and that value is later used to define array dimensions, etc.</p>
<dt><code>param-implicit-type</code> (8):</p>
<dd> Implicit typing of a parameter by the data type of the value assigned. Some non-standard compilers may allow the data type of the value to override the Fortran 77 default type of a parameter that is based on the first letter of the parameter name. This option only applies to PARAMETER statements of the standard form which has parentheses. A parameter that has been explicitly declared in a type statement prior to the PARAMETER statement is not affected by this option. A warning will be given under the <code>-f77=param-implicit-type</code> or <code>-portability=param-implicit-type</code> option.</p>
<dt>
<dd> Note that this implicit typing is treated as equivalent to an explicit type declaration for the parameter. Therefore, if you use <code>-makedcls=undeclared-only</code> to generate declarations only of undeclared variables, these parameters will <i>not</i> be included.</p>
<dt><code>dec-param-standard-type</code> (16):</p>
<dd> Follow the Fortran 77 rule for data typing of DEC Fortran style parameters. These are declared using a nonstandard form of the PARAMETER statement which lacks parentheses. According to DEC Fortran, parameters defined by this form of the statement have their data type given by the data type of the value assigned. Use this option to tell <code>ftnchek</code> not to follow this rule but instead to use the same rule as for standard PARAMETER statements. This option does not apply to PARAMETER statements of the standard form.</dl>
<p> By default, all these source code options are turned off, except for the <code>vms-include</code> option, which is on by default in the VMS version.. </p>
<p> See also: <code>-f77</code>, <code>-include</code>, <code>-portability</code>.</dl>
<dt><code>-style=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Provides extra-picky warnings about obsolescent or old-fashioned programming constructions. This option is helpful for efforts to follow a modern programming style. (Most of the things complained about under this option are forbidden in the <code>F</code> subset language.) By default, all warnings are turned off. </p>
<p> The <i>list</i> consists of keywords separated by commas or colons. There are three special keywords: <code>all</code> to turn on all the options, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-style</code> is equivalent to <code>-style=all</code>, and <code>-nostyle</code> is equivalent to <code>-style=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>block-if</code>:</p>
<dd> Complain about arithmetic IF statement. Accept block IF or logical IF (which controls a single statement).</p>
<dt><code>construct-name</code>:</p>
<dd> Complain about unnamed block constructs: IF, DO, and SELECT CASE. Note that if a construct name is present on the opening statement of a construct, then it is required to be present on all other component statements (ELSE, END IF, etc.) of the construct. In that case a missing construct name on those statements generates a syntax error regardless of this option. The purpose of this option is to warn if the construct completely lacks the optional name.</p>
<dt><code>distinct-do</code>:</p>
<dd> Complain if two DO loops share a common terminator statement.</p>
<dt><code>do-construct</code>:</p>
<dd> Complain if terminator of a DO loop is anything other than an END DO or CONTINUE statement. This is the requirement in order for the loop to meet the Fortran 90 definition of a do-construct.</p>
<dt><code>do-enddo</code>:</p>
<dd> Complain if terminator of a DO loop is anything other than an END DO statement. (This option overrides the <code>do-construct</code> option, being even stricter.)</p>
<dt><code>end-name</code>:</p>
<dd> Complain about the absence of the subprogram name on structured END statements.</p>
<dt><code>format-stmt</code>:</p>
<dd> Complain about the presence of FORMAT statements. Only the FORMAT statements themselves are flagged, not the references to them in I/O lists.</p>
<dt><code>goto</code>:</p>
<dd> Complain about the presence of unconditional, computed or assigned GOTO statements. Also complain about alternate returns (but not about labels as subprogram arguments).</p>
<dt><code>labeled-stmt</code>:</p>
<dd> Complain about the presence of labels (numbers) on statements other than FORMAT statements. (Since FORMAT statements are arguably convenient and not readily abused, complaints about them are controlled by the separate <code>format-stmt</code> keyword.)</p>
<dt><code>program-stmt</code>:</p>
<dd> Complain about the absence of a PROGRAM statement at the head of the main program.</p>
<dt><code>structured-end</code>:</p>
<dd> Complain about the use of a plain END statement to end a subprogram, rather than a structured END statement (END PROGRAM, END SUBROUTINE, END FUNCTION, or END BLOCK DATA).</dl>
<p> See also: <code>-f77</code>, <code>-f90</code>, <code>-f95</code>, <code>-pretty</code>, <code>-portability</code>.</dl>
<dt><code>-symtab</code></p>
<dd>
<dl>
<dt>
<dd> A symbol table will be printed out for each module, listing all identifiers mentioned in the module. This table gives the name of each variable, its datatype, and the number of dimensions for arrays. An asterisk (*) indicates that the variable has been implicitly typed, rather than being named in an explicit type declaration statement. The table also lists all subprograms invoked by the module, all COMMON blocks declared, etc. Default = no. </p>
<p> Also, for each module, a label table will be printed. The table lists each label defined in the module; the line on which said statement label is defined; and the statement type (executable, format, or specification). The labels are listed in sequential order. </p>
<p> Also printed is a table describing the I/O units used by the module, together with information about how they are used: what operations are performed, whether the access is sequential or direct, and whether the I/O is formatted or unformatted. </p>
<p> See also: <code>-calltree</code>, <code>-crossref</code>, <code>-list</code>, <code>-reference</code>, <code>-sort</code>, <code>-vcg</code>.</dl>
<dt><code>-truncation=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Warn about possible truncation (or roundoff) errors. Most of these are related to integer arithmetic. By default, all warnings are turned on. </p>
<p> This setting provides detailed control over the warnings about possible truncation errors. The <i>list</i> consists of keywords separated by commas or colons. Since all warnings are on by default, include a keyword prefixed by <code>no-</code> to turn off a particular warning. There are three special keywords: <code>all</code> to turn on all the warnings about truncation, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-truncation</code> is equivalent to <code>-truncation=all</code>, and <code>-notruncation</code> is equivalent to <code>-truncation=none</code>. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>int-div-exponent</code>:</p>
<dd> use of the result of integer division as an exponent. This suggests that a real quotient is intended. An example would be writing X**(1/3) to evaluate the cube root of X. The correct expression is X**(1./3.).</p>
<dt><code>int-div-real</code>:</p>
<dd> Conversion of an expression involving an integer division to real. This suggests that a real quotient is intended.</p>
<dt><code>int-div-zero</code>:</p>
<dd> division in an integer constant expression that yields a result of zero.</p>
<dt><code>int-neg-power</code>:</p>
<dd> exponentiation of an integer by a negative integer (which yields zero unless the base integer is 1 in magnitude). This suggests that a real base is intended.</p>
<dt><code>promotion</code>:</p>
<dd> automatic conversion of a lower precision quantity to one of higher precision. The loss of accuracy for real variables in this process is comparable to the corresponding demotion. No warning is given for promotion of integer quantities to real since this is ordinarily exact.</p>
<dt><code>real-do-index</code>:</p>
<dd> use of a non-integer DO index in a loop with integer bounds. An integer DO index with real bounds is always warned about regardless of this setting.</p>
<dt><code>real-subscript</code>:</p>
<dd> use of a non-integer array subscript.</p>
<dt><code>significant-figures</code>:</p>
<dd> overspecifying a single precision constant. This may indicate that a double precision constant was intended.</p>
<dt><code>size-demotion</code>:</p>
<dd> automatic conversion of a higher precision quantity to one of lower precision of the same type. This warning only occurs when an explicit size is used in declaring the type of one or both operands in an assignment. For example, a warning wil be issued where a REAL*8 variable is assigned to a REAL variable, if the default wordsize of 4 is in effect. A warning is also issued if a long integer is assigned to a shorter one, for example, if an INTEGER expression is assigned to an INTEGER*2 variable. There is one exception to this last case, namely if the right hand side of the assignment is a small literal constant (less than 128). <code>type-demotion</code>: automatic conversion of a higher precision quantity to one of lower precision of different type. This warning includes conversion of real quantities to integer, double precision to single precision real, and assignment of a longer character string to a shorter one.</dl>
<p> The warnings about promotion and demotion also apply to complex constants, considering the precision to be that of the real or imaginary part. Warnings about promotions and demotions are given only when the conversion is done automatically, e.g. in expressions of mixed precision or in an assignment statement. If intrinsic functions such as INT are used to perform the conversion, no warning is given. </p>
<p> See also: <code>-portability</code>, <code>-wordsize</code>.</dl>
<dt><code>-usage=</code><i>list</i></p>
<dd>
<dl>
<dt>
<dd> Warn about unused or possible uninitialized variables, unused common blocks, undefined or unused statement labels, and unused or undefined subprograms. By default, all warnings are turned on. </p>
<p> This setting provides detailed control over the warnings about possible usage errors. The <i>list</i> consists of keywords separated by commas or colons. Since all warnings are on by default, include a keyword prefixed by <code>no-</code> to turn off a particular warning. There are three special keywords: <code>all</code> to turn on all the warnings about usage, <code>none</code> to turn them all off, and <code>help</code> to print the list of all the keywords with a brief explanation of each. If <i>list</i> is omitted, <code>-usage</code> is equivalent to <code>-usage=all</code>, and <code>-nousage</code> is equivalent to <code>-usage=none</code>. These warnings cover four main categories of objects: subprogram dummy arguments, common blocks and variables, subprograms and functions, and local variables. Warnings include undefined items, multiply defined items, unused items, etc. The warning keywords with their meanings are as follows:</p>
<dl>
<dt><code>arg-alias</code>:</p>
<dd> a scalar dummy argument is actually the same as another and is (or may be) modified. The Fortran 77 standard (section 15.9.3.6) prohibits modifying an argument that is aliased to another.</p>
<dt><code>arg-array-alias</code>:</p>
<dd> a dummy argument which is an array or array element is in the same array as another and is modified. This flag is similar to <code>arg-alias</code> but provides separate control over array arguments. It is harder to tell if aliasing is occurring in the case of arrays, so if <code>ftnchek</code> gives too many false warnings, this flag allows the array-related ones to be turned off without suppressing the warnings for scalars.</p>
<dt><code>arg-common-alias</code>:</p>
<dd> a scalar dummy argument is the same as a common variable in the subprogram, and either is modified. This is also prohibited by the Fortran 77 standard. If common checking is not exact (see the <code>-common</code> setting), it is harder to tell if aliasing is occurring, so the warning is given if the variable is anywhere in a common block that is declared by the subprogram.</p>
<dt><code>arg-common-array-alias</code>:</p>
<dd> a dummy argument which is an array or array element is in the same array as a common variable, and either is modified. If common checking is not exact, the variable can be anywhere in a common block that is declared by the subprogram.</p>
<dt><code>arg-const-modified</code>:</p>
<dd> a subprogram modifies an argument which is a constant or an expression. Such an action could cause anomalous behavior of the program.</p>
<dt><code>arg-unused</code>:</p>
<dd> a dummy argument is declared but never used. This is similar to the <code>var-unused</code> keyword described below, but applies only to arguments.</p>
<dt><code>com-block-unused</code>:</p>
<dd> a common block is declared but none of the variables in it are used by any subprogram. This warning is suppressed if the common strictness setting is 0.</p>
<dt><code>com-block-volatile</code>:</p>
<dd> a common block may lose the definition of its contents if common blocks are volatile. This option only has an effect if the <code>-common=volatile</code> flag is in effect. See the discussion of the <code>-common</code> setting above.</p>
<dt><code>com-var-set-unused</code>:</p>
<dd> a common variable is assigned a value, but its value is not used by any subprogram. This warning is suppressed if the common strictness setting is 0.</p>
<dt><code>com-var-uninitialized</code>:</p>
<dd> a common variable&#8217;s value is used in some subprogram, but is not set anywhere. Unfortunately, <code>ftnchek</code> does not do a thorough enough analysis of the calling sequence to know which routines are called before others. So warnings about this type of error will only be given for cases in which a variable is used in some routine but not set in any other routine. Checking of individual COMMON variables is done only if the <code>-common</code> setting is 3 (variable by variable agreement). This warning is suppressed if the common strictness setting is 0.</p>
<dt><code>com-var-unused</code>:</p>
<dd> a common variable is declared but not used by any subprogram. This warning is suppressed if the common strictness setting is 0.</p>
<dt><code>do-index-modified</code>:</p>
<dd> a variable that is the index of a DO loop is modified by some statement within the range of the loop. The Standard permits an active DO variable to be modified only by the incrementation mechanism of the DO statement.</p>
<dt><code>ext-multiply-defined</code>:</p>
<dd> an external (a subroutine or function) is defined more than once. Definition of an external means providing the body of its source code.</p>
<dt><code>ext-declared-only</code>:</p>
<dd> a name is declared in an EXTERNAL statement in some module, but is not defined or used anywhere.</p>
<dt><code>ext-undefined</code>:</p>
<dd> an external is used (invoked) but not defined anywhere. This option is equivalent to the <code>-external</code> flag. If the subprogram is invoked more than once, those invocations will still be checked for consistency.</p>
<dt><code>ext-unused</code>:</p>
<dd> an external is defined (its subprogram body is present) but it is not used. A subprogram is considered unused even if it is invoked by some other subprogram, if it cannot be called from any thread of execution starting with the main program. The agreement of the subprogram&#8217;s arguments with its invocations is still checked even if this warning is turned off. If there is no main program, then this warning is issued only if the subprogram is not invoked anywhere. This warning is suppressed in library mode, but library mode has the additional effect of suppressing argument checking for unused routines.</p>
<dt><code>label-undefined</code>:</p>
<dd> a statement refers to a label that has not been defined.</p>
<dt><code>label-unused</code>:</p>
<dd> a statement label is defined, but never referred to.</p>
<dt><code>var-set-unused</code>:</p>
<dd> a local variable is assigned a value, but that value is not used.</p>
<dt><code>var-uninitialized</code>:</p>
<dd> a local variable&#8217;s value may be used before it is assigned. Sometimes <code>ftnchek</code> makes a mistake in the warnings about local variable usage. Usually it errs on the side of giving a warning where no problem exists, but in rare cases it may fail to warn where the problem does exist. See the section on Bugs for examples. If variables are equivalenced, the rule used by <code>ftnchek</code> is that a reference to any variable implies the same reference to all variables it is equivalenced to. For arrays, the rule is that a reference to any array element is treated as a reference to all elements of the array.</p>
<dt><code>var-unused</code>:</p>
<dd> a local variable is declared (for instance, in a type declaration) but is not used in the module. Does not apply to dummy arguments: warnings about them are controlled by the keyword <code>arg-unused</code> described above.</dl>
<p> Note: In versions of <code>ftnchek</code> prior to 2.10, the <code>-usage</code> flag took a numeric argument instead of a list of options. For the sake of users who may have written scripts invoking <code>ftnchek</code> in this way, the numeric form is still accepted. The numeric setting is composed of three digits. The first digit (hundreds place) controls warnings about subprograms (functions and subroutines), the second digit (tens place) warnings about common blocks and common variables,, and the third digit (ones place) warnings about local variables. Each digit controls warnings according to the convention that a 1 means warn about undefined items and variables that are used before set, a 2 means warn about items that are unused, and a 3 means warn about both types. These numbers are now converted to the appropriate values for the above-listed keywords, except for <code>com-block-volatile</code>, which is not affected by the numeric argument. </p>
<p> See also: <code>-common</code>, <code>-declare</code>, <code>-extern</code>, <code>-library</code>.</dl>
<dt><code>-vcg</code></p>
<dd>
<dl>
<dt>
<dd> Produce the call graph in the form of a VCG graph description. This description is written to a separate file, with the same stem as the file containing the main program, and suffix <i>.vcg</i>. This file is able to be given directly to <code><a href="//www.systutorials.com/docs/linux/man/1L-xvcg/">xvcg</a></code>(1L) to visualize the call graph. (If input is from the standard input, then the graph description is sent to standard output.) This switch is equivalent to <code>-calltree=vcg</code>. Default = no. </p>
<p> The VCG description as created is more complex than it need be. VCG allows graphs and nested subgraphs: each subroutine is created as a subgraph nested inside its calling routines. This allows you to interactively display subgraphs or summarise them. </p>
<p> The <code>-vcg</code> option for <code>ftnchek</code> was written by Dr. Philip Rubini of Cranfield University, UK. </p>
<p> <code>xvcg</code> is a graph visualisation tool which runs under the X windows system. It is freely available from <a href="ftp://ftp.cs.uni-sb.de">ftp.cs.uni-sb.de</a>. It was written by G. Sander of the University of Saarland, Germany. </p>
<p> See also: <code>-calltree</code>, <code>-crossref</code>, <code>-reference</code>, <code>-sort</code>.</dl>
<dt><code>-version</code></p>
<dd>
<dl>
<dt>
<dd> This option causes <code>ftnchek</code> to print a line giving the version number, release date, and patch level of the program. If no files are given, it then exits. If files are given, the effect of this option is to include the patch level (normally omitted) in the version information printed at the start of processing. Default = no. </p>
<p> See also: <code>-help</code>.</dl>
<dt><code>-volatile</code></p>
<dd>
<dl>
<dt>
<dd> Assume that COMMON blocks are volatile. Default = no. </p>
<p> This flag is superseded by <code>-common=volatile</code>, and should no longer be used. It may be eliminated in a future release of <code>ftnchek</code>. </p>
<p> See also: <code>-common</code>, <code>-usage</code>.</dl>
<dt><code>-wordsize=</code><i>num</i></p>
<dd>
<dl>
<dt>
<dd> Specifies the default word size to be <i>num</i> bytes. This is the size of logical and single-precision numeric variables that are not given explicit precisions. (Explicit precisions for non-character variables are an extension to the Fortran 77 Standard, and are given by type declarations such as REAL*8 X.) Double-precision and complex variables will be twice this value, and double complex variables four times. Quad-precision constants and intrinsic function results will be four times this value. Note that variables declared as REAL*16 will be regarded as quad precision only if the word size is 4 bytes. Default = turn-on = 4 bytes. </p>
<p> The word size value does not matter for checking standard-conforming programs that do not declare explicit precisions for non-character variables or store Hollerith data in variables. This setting also does not affect the default size of character variables, which is always 1 byte. Hollerith constants also are assumed to occupy 1 byte per character. </p>
<p> The word size is used to determine whether truncation occurs in assignment statements, and to catch precision mismatches in subprogram argument lists and common block lists. The exact warnings that are issued will depend on the status of other flags. Under both the <code>-portability=mixed-size</code> and the <code>-nowordsize</code> flag, any mixing of explicit with default precision objects (character expressions not included) is warned about. This applies to arithmetic expressions containing both types of objects, and to subprogram arguments and COMMON variables. Under control of the <code>-truncation=demotion</code> and <code>promotion</code> options, a warning is given for assignment of an expression to a shorter variable of the same type, or for promotion of a lower precision value to higher precision in an arithmetic expression or an assignment statement. </p>
<p> Giving a word size of 0, or equivalently, using <code>-nowordsize</code> means that no default value will be assumed. This is equivalent to specifying <code>-portability=mixed-size</code>. Use it to find cases of mixing default and explicit precision, for example to flag places where REAL*8 is treated as equivalent to DOUBLE PRECISION. </p>
<p> See also: <code>-pointersize</code>, <code>-portability</code>, <code>-truncation</code>.</dl>
<dt><code>-wrap=</code><i>col</i></p>
<dd> Controls the wrapping of error messages. Long error messages that would run past the specified column will be broken up into separate lines between the words of the message for better readability. If turned off with <code>-nowrap</code>, each separate error message will be printed on one line, leaving it up to the display to wrap the message or truncate it. Default = turn-on = 79. </p>
</dl>
<h2>CHANGING THE DEFAULTS</h2>
<p> <code>ftnchek</code> includes two mechanisms for changing the default values of all options: by defining environment variables or by creating a preferences file. When <code>ftnchek</code> starts up, it looks in its environment for any variables whose names are composed by prefixing the string FTNCHEK_ onto the uppercased version of the option name. If such a variable is found, its value is used to specify the default for the corresponding switch or setting. In the case of settings (for example, the <code>-common</code> strictness setting) the value of the environment variable is read as the default setting value. In the case of switches, the default switch will be taken as true or yes unless the environment variable has the value 0 or NO. </p>
<p> Note that the environment variable name must be constructed with the full-length option name, which must be in uppercase. For example, to make <code>ftnchek</code> print a source listing by default, set the environment variable FTNCHEK_LIST to 1 or YES or anything other than 0 or NO. The names FTNCHEK_LIS (not the full option name) or ftnchek_list (lower case) would not be recognized. </p>
<p> Here are some examples of how to set environment variables on various systems. For simplicity, all the examples set the default <code>-list</code> switch to YES. </p>
<p> &gt;1. UNIX, Bourne shell: &gt;$ FTNCHEK_LIST=YES<br />
 &gt; &gt;$ export FTNCHEK_LIST </p>
<p> &gt;2. UNIX, C shell: &gt;% setenv FTNCHEK_LIST YES </p>
<p> &gt;3. VAX/VMS: &gt;$ DEFINE FTNCHEK_LIST YES </p>
<p> &gt;4. MSDOS: &gt;$ SET FTNCHEK_LIST=YES </p>
<p> After processing any environment variables, ftnchek looks for a preferences file containing options and settings. It will search in the following order, using only the first file found: (1) <i>.ftnchekrc</i> in the current directory, (2) <i>ftnchek.ini</i> in the current directory, (3) <i>.ftnchekrc</i> in the user&#8217;s home directory, (4) <i>ftnchek.ini</i> in the home directory. If such a file is found, the options defined in it are used as defaults in place of the built-in defaults and overriding any defaults set in the environment.. </p>
<p> Each option or setting in the preferences file must be on a separate line. They are given in the same form as on the command line, except without the initial dash. The preferences file can contain blank lines and comments. Comments are introduced at any point in a line by a space character (blank or tab) or the &#8216;#&#8217; character, and are terminated by the end of the line. </p>
<p> Command-line options override the defaults set in the environment or in the preferences file, in the same way as they override the built-in defaults. </p>
<h2>USING PROJECT FILES</h2>
<p> This section contains detailed information on how to use project files most effectively, and how to avoid some pitfalls. </p>
<p> One can divide the checks <code>ftnchek</code> does into two categories, local and global. Local checking is restricted to within a single routine, and catches things like uninitialized variables, unintended loss of precision in arithmetic expressions, etc. This sort of checking can be done on each subprogram independently. Furthermore, local checking of a subprogram does not need to be repeated when some other subprogram is changed. Global checking catches things like calling a subroutine with the wrong argument types, or disagreeing in common block declarations. It requires looking at the whole set of subprograms interacting with each other. </p>
<p> The purpose of project files is to allow the local checking and global checking steps to be separated. Assuming that each subprogram is in its own source file, you can run <code>ftnchek</code> once on each one to do local checking while suppressing global checking. Then <code>ftnchek</code> can be run once on all the project files together to do the global checking. The sample makefile below shows how to automate this task. The &#8220;.f.prj&#8221; target updates a project file for a particular file any time the source file changes. The information needed for global checking is saved in the project file. The &#8220;check&#8221; target does the combined global checking. Typically &#8220;make check&#8221; would repeat the &#8220;ftnchek -project&#8221; step only on changed source files, then do the global check. This is obviously a big advantage for large programs, when many subprograms seldom if ever change. </p>
<p> It is best when using project files to place each subprogram in a separate source file. If each source file may contain more than one subprogram, it complicates the definition of &#8220;local&#8221; and &#8220;global&#8221; checking because there is some inter-module checking that is contained within a file. <code>ftnchek</code> tries to do the right thing in this case, but there are some complications (described below) due to the trade-off between avoiding re-doing cross-checks and preserving information about the program&#8217;s structure. </p>
<p> Ordinarily, to do the least amount of re-checking, project files should be created with the <code>-library</code> flag in effect and trimming turned on. In this mode, the information saved in the project file consists of all subprogram declarations, all subprogram invocations not resolved by declarations in the same file, and one instance of each COMMON block declaration. This is the minimum amount of information needed to check agreement between files. </p>
<p> If the source file contains more than one routine, there are some possible problems that can arise from creating the project file in library mode, because the calling hierarchy among routines defined within the file is lost. Also, if the routines in the file make use of COMMON blocks that are shared with routines in other files, there will not be enough information saved for the correct checking of set and used status of COMMON blocks and COMMON variables according to the <code>-usage</code> setting. Therefore if you plan to use project files when <code>-usage</code> checking is turned on (which is the default situation), and if multiple routines in one project file share COMMON blocks with routines in other files, the project files should be created with the <code>-library</code> flag turned off. In this mode, <code>ftnchek</code> saves, besides the information listed above, one invocation of each subprogram by any other subprogram in the same file, and all COMMON block declarations. This means that the project file will be larger than necessary, and that when it is read in, <code>ftnchek</code> may repeat some inter-module checks that it already did when the project file was created. If each project file contains only one module, there is no loss of information in creating the project files in library mode. </p>
<p> Because of the possible loss of information entailed by creating a project file with the <code>-library</code> flag in effect, whenever that project file is read in later, it will be treated as a library file regardless of the current setting of the <code>-library</code> flag. On the other hand, a project file created with library mode turned off can be read in later in either mode. </p>
<p> The foregoing discussion assumes that the trimming options of the <code>-project</code> setting are turned on when the project file is created. This is the normal situation. The <code>no-trim</code> options of the <code>-project</code> setting are provided in case one wants to use the project files for purposes other than checking the program with <code>ftnchek</code>. For instance, one could write a Perl script to analyze the project files for information about how the different subprograms are called. You should not use the <code>no-trim</code> options to deal with the issues of information loss discussed above, since they cause more information than necessary to be stored. This makes the project files bigger and causes <code>ftnchek</code> to do more work later when it reads them to check your complete program. Ordinarily, you should use the <code>-library</code> option to control how much information to store for later use by <code>ftnchek</code> in checking your program. </p>
<p> Here is an example of how to use the UNIX <code>make</code> utility to automatically create a new project file each time the corresponding source file is altered, and to check the set of files for consistency. Add these lines to your makefile. The example assumes that a macro OBJS has been defined which lists all the names of object files to be linked together to form the complete executable program. (In this makefile, the indented lines should each begin with a tab, not blanks.) If any source file contains multiple routines that share common blocks among themselves, then the no-com-\* option should be removed from NOGLOBAL, and/or drop the -library flag. </p>
<pre>
    # tell make what a project file suffix is
    .SUFFIXES: .prj
    # these options suppress global checks.
    NOGLOBAL=-usage=no-ext-undefined,no-com-\*
    # tell make how to create a .prj file from a .f file
    .f.prj:
            ftnchek -project $(NOGLOBAL) -library $&lt;
    # set up macro PRJS containing project filenames
    PRJS= $(OBJS:.o=.prj)
    # &quot;make check&quot; will check everything that has been changed.
    check: $(PRJS)
            ftnchek $(PRJS)
</pre>
<p> When a program uses many routines defined in a large number of different source files in different directories, it can be cumbersome to specify all the different project files needed to check the program properly. To deal with such cases, <code>ftnchek</code> allows project files to be concatenated into a single large file. This single file can then be given to <code>ftnchek</code> to provide the information for checking the use of any or all of the routines defined in the combined project files. When using such a &#8220;library&#8221; project file, you may want <code>ftnchek</code>&#8216;s error reports to document precisely the name of the file where the specific function is defined. If the various source files are in several directories, an error report that gives only the file name may be ambiguous, and rather should include the path to the file. The solution is to create each of the individual project files by giving the complete path to the source file. Then this complete path will appear in the error reports. For example, suppose that all of the library subprogram source files are in subdirectories of a directory named /util/lib. Then the individual project files could first be created by a command such as </p>
<pre>
find /util/lib -name '*.f' -exec ftnchek -project '{}' ';'
</pre>
<p> (Possibly other options would be provided to <code>ftnchek</code> as discussed above. Also, this step could be handled instead by a revised makefile rule that would provide the complete source file path instead of just the local name when invoking <code>ftnchek</code>.) Next, concatenate all of these project files manually. </p>
<pre>
find /util/lib -name '*.prj' -exec cat '{}' ';' &gt; ourlib.prj
</pre>
<p> Then a program source file can be checked by using the command </p>
<pre>
ftnchek prog.f ... -lib ourlib.prj
</pre>
<p> and an error message related to any library routine will include the full path to the routine&#8217;s source file. </p>
<p> At present, there is no archive utility like <code>ar</code> to manage the contents of a concatenated project file like the one in the illustration above. If changes are made to one of the library routines, the only way to update the combined project file is to concatenate all the individual project files once again. Such a utility would be quite easy to write. Someone should do so and contribute it to the <code>ftnchek</code> effort.</p>
<h2>AN EXAMPLE</h2>
<p> The following simple Fortran program illustrates the messages given by <code>ftnchek</code>. The program is intended to accept an array of test scores and then compute the average for the series. </p>
<pre><code>
C AUTHORS : MIKE MYERS AND LUCIA SPAGNUOLO
                C DATE : MAY 8,
                         1989 C Variables : C SCORE-&gt;an array of test scores
                                                C SUM-&gt;sum of the test scores
                                                    C COUNT-&gt;counter of scores read in
                                                        C I-&gt;loop counter
                                                            REAL FUNCTION
                                                            COMPAV(SCORE, COUNT)
INTEGER SUM, COUNT, J, SCORE(5) DO 30 I = 1, COUNT SUM = SUM + SCORE(I) 30 CONTINUE COMPAV = SUM / COUNT END PROGRAM AVENUM C C MAIN PROGRAM C C AUTHOR : LOIS BIGBIE C DATE : MAY 15, 1990 C C Variables : C MAXNOS-&gt;maximum number of input values C NUMS-&gt;an array of numbers C COUNT-&gt;exact number of input values C AVG-&gt;average returned by COMPAV C I-&gt;loop counter C PARAMETER(MAXNOS = 5) INTEGER I, COUNT REAL NUMS(MAXNOS), AVG COUNT = 0 DO 80 I = 1, MAXNOS READ(5, *, END = 100) NUMS(I) COUNT = COUNT + 1 80 CONTINUE 100 AVG = COMPAV(NUMS, COUNT) END
</code></pre>
<p> The compiler gives no error messages when this program is compiled. Yet here is what happens when it is run: </p>
<pre>
$ run average
70
90
85
&lt;EOF&gt;
$
</pre>
<p> What happened? Why didn&#8217;t the program do anything? The following is the output from <code>ftnchek</code> when it is used to debug the above program: </p>
<p>$ ftnchek &#8211; list &#8211; symtab average FTNCHEK Version 3.3 November 2004 File average.f : 1 C AUTHORS : MIKE MYERS AND LUCIA SPAGNUOLO 2 C DATE : MAY 8, 1989 3 4 C Variables : 5 C SCORE-&gt;an array of test scores 6 C SUM-&gt;sum of the test scores 7 C COUNT-&gt;counter of scores read in 8 C I-&gt;loop counter 9 10 REAL FUNCTION COMPAV(SCORE, COUNT) 11 INTEGER SUM, COUNT, J, SCORE(5) 12 13 DO 30 I = 1, COUNT 14 SUM = SUM + SCORE(I) 15 30 CONTINUE 16 COMPAV = SUM / COUNT ^ Warning near line 16 col 20 : integer quotient expr SUM / COUNT converted to real 17 END Module COMPAV : func : real Variables :</p>
<p>    Name Type Dims Name Type Dims Name Type Dims Name Type Dims COMPAV real COUNT intg I intg<br />
    *<br />
    J intg SCORE intg 1 SUM intg * Variable not declared.Type has been implicitly defined.Warning in module COMPAV : Variables declared but never referenced : J declared at line 11 Warning in module COMPAV : Variables may be used before set : SUM used at line 14 SUM set at line 14 Statement labels defined : Label Line StmtType&lt;30&gt; 15 exec 18 19 20 PROGRAM AVENUM 21 C 22 C MAIN PROGRAM 23 C 24 C AUTHOR : LOIS BIGBIE 25 C DATE : MAY 15,<br />
                                                                                                                                                                                                                                                                                                                                                                                              1990 26 C<br />
                                                                                                                                                                                                                                                                                                                                                                                              27 C Variables : 28 C MAXNOS-&gt;maximum number of input values<br />
                                                                                                                                                                                                                                                                                                                                                                                              29 C NUMS-&gt;an array of numbers<br />
                                                                                                                                                                                                                                                                                                                                                                                              30 C COUNT-&gt;exact number of input values<br />
                                                                                                                                                                                                                                                                                                                                                                                              31 C AVG-&gt;average returned by COMPAV<br />
                                                                                                                                                                                                                                                                                                                                                                                              32 C I-&gt;loop counter<br />
                                                                                                                                                                                                                                                                                                                                                                                              33 C<br />
                                                                                                                                                                                                                                                                                                                                                                                              34 35 PARAMETER(MAXNOS = 5) 36 INTEGER I,<br />
                                                                                                                                                                                                                                                                                                                                                                                              COUNT<br />
    37 REAL NUMS(MAXNOS),<br />
                                                                                                                                                                                                                                                                                                                                                                                              AVG<br />
                                                                                                                                                                                                                                                                                                                                                                                              38 COUNT = 0 39 DO 80 I = 1,<br />
                                                                                                                                                                                                                                                                                                                                                                                              MAXNOS<br />
                                                                                                                                                                                                                                                                                                                                                                                              40 READ(5, *, END = 100) NUMS(I) 41 COUNT = COUNT + 1 42 80 CONTINUE<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                          43 100 AVG = COMPAV(NUMS, COUNT) 44 END<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                       Module AVENUM : prog<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                       External subprograms referenced : COMPAV : real<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  *<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Variables :</p>
<p>    Name Type Dims Name Type Dims Name Type Dims Name Type Dims<br />
    AVG real COUNT intg I intg MAXNOS intg<br />
    *<br />
    NUMS real 1 * Variable not declared.Type has been implicitly defined.Warning in module AVENUM : Variables set but never used : AVG set at line 43 I / O Operations : Unit ID Unit No.Access Form Operation Line 5 SEQ FMTD READ 40 Statement labels defined : Label Line StmtType Label Line StmtType&lt;80&gt; 42 exec&lt;100&gt; 43 exec 0 syntax errors detected in file average.f 6 warnings issued in file average.f Warning : Subprogram COMPAV argument data type mismatch at position 1 : Dummy arg SCORE in module COMPAV line 10 file average.f is type intg Actual arg NUMS in module AVENUM line 43 file average.f is type real</p>
<p> According to <code>ftnchek</code>, the program contains variables which may be used before they are assigned an initial value, and variables which are not needed. <code>ftnchek</code> also warns the user that an integer quotient has been converted to a real. This may assist the user in catching an unintended roundoff error. Since the <code>-symtab</code> flag was given, <code>ftnchek</code> prints out a table containing identifiers from the local module and their corresponding datatype and number of dimensions. Finally, <code>ftnchek</code> warns that the function COMPAV is not used with the proper type of arguments. </p>
<p> With <code>ftnchek</code>&#8216;s help, we can debug the program. We can see that there were the following errors:</p>
<dl>
<dt>1.</p>
<dd> SUM and COUNT should have been converted to real before doing the division.</p>
<dt>2.</p>
<dd> SUM should have been initialized to 0 before entering the loop.</p>
<dt>3.</p>
<dd> AVG was never printed out after being calculated.</p>
<dt>4.</p>
<dd> NUMS should have been declared INTEGER instead of REAL.</dl>
<p> We also see that I, not J, should have been declared INTEGER in function COMPAV. Also, MAXNOS was not declared as INTEGER, nor COMPAV as REAL, in program AVENUM. These are not errors, but they may indicate carelessness. As it happened, the default type of these variables coincided with the intended type. </p>
<p> Here is the corrected program, and its output when run: </p>
<p>C AUTHORS : MIKE MYERS AND LUCIA SPAGNUOLO<br />
                C DATE : MAY 8,<br />
                         1989 C<br />
                             C Variables : C SCORE-&gt;an array of test scores<br />
                                               C SUM-&gt;sum of the test scores<br />
                                                   C COUNT-&gt;counter of scores read in<br />
                                                       C I-&gt;loop counter<br />
                                                           C<br />
                                                               REAL FUNCTION<br />
                                                               COMPAV(SCORE, COUNT)<br />
INTEGER SUM, COUNT, I, SCORE(5) C SUM = 0 DO 30 I = 1, COUNT SUM = SUM + SCORE(I) 30 CONTINUE COMPAV = FLOAT(SUM) / FLOAT(COUNT) END C C PROGRAM AVENUM C C MAIN PROGRAM C C AUTHOR : LOIS BIGBIE C DATE : MAY 15, 1990 C C Variables : C MAXNOS-&gt;maximum number of input values C NUMS-&gt;an array of numbers C COUNT-&gt;exact number of input values C AVG-&gt;average returned by COMPAV C I-&gt;loop counter C C INTEGER MAXNOS PARAMETER(MAXNOS = 5) INTEGER I, NUMS(MAXNOS), COUNT REAL AVG, COMPAV COUNT = 0 DO 80 I = 1, MAXNOS READ(5, *, END = 100) NUMS(I) COUNT = COUNT + 1 80 CONTINUE 100 AVG = COMPAV(NUMS, COUNT) WRITE(6, *) &#8216;AVERAGE =&#8217;, AVG END $ run average 70 90 85 &lt; EOF &gt; AVERAGE = 81.66666 $</p>
<p> With <code>ftnchek</code>&#8216;s help, our program is a success! </p>
<h2>INTERPRETING THE OUTPUT</h2>
<p> The messages given by <code>ftnchek</code> include not only syntax errors but also warnings and informational messages about things that are legal Fortran but that may indicate errors or carelessness. Most of these messages can be turned off by command-line options. Which option controls each message depends on the nature of the condition being warned about. See the descriptions of the command-line flags in the previous sections, and of individual messages below. Each message is prefixed with a word or phrase indicating the nature of the condition and its severity. </p>
<p> &#8220;Error&#8221; means a syntax error. The simplest kind of syntax errors are typographical errors, for example unbalanced parentheses or misspelling of a keyword. This type of error is caught by the parser and appears with the description &#8220;parse error&#8221; or &#8220;syntax error&#8221; (depending on the version of the parser generator and whether it is GNU <code>bison</code> or UNIX <code>yacc</code>). This type of error message cannot be suppressed. Be aware that this type of error often means that <code>ftnchek</code> has not properly interpreted the statement where the error occurs, so that its subsequent checking operations will be compromised. You should eliminate all syntax errors before proceeding to interpret the other messages <code>ftnchek</code> gives. </p>
<p> &#8220;Warning: Nonstandard syntax&#8221; indicates an extension to Fortran that <code>ftnchek</code> supports but that is not according to the Fortran 77 Standard. The extensions that <code>ftnchek</code> accepts are described in the section on Extensions below. One example is the DO &#8230; ENDDO construction. If a program uses these extensions, warnings will be given according to specifications under the <code>-f77</code> setting. The default behavior is to give no warnings. </p>
<p> &#8220;Warning&#8221; in other cases means a condition that is suspicious but that may or may not be a programming error. Frequently these conditions are legal under the standard. Some are illegal but do not fall under the heading of syntax errors. Usage errors are one example. These refer to the possibility that a variable may be used before it has been assigned a value (generally an error), or that a variable is declared but never used (harmless but may indicate carelessness). The amount of checking for usage errors is controlled by the <code>-usage</code> flag, which specifies the maximum amount of checking by default. </p>
<p> Truncation warnings cover situations in which accuracy may be lost unintentionally, for example when a double precision value is assigned to a real variable. These warnings are controlled by the <code>-truncation</code> setting, which is on by default. </p>
<p> &#8220;Nonportable usage&#8221; warns about some feature that may not be accepted by some compilers even though it is not contrary to the Fortran 77 Standard, or that may cause the program to perform differently on different platforms. For example, equivalencing real and integer variables is usually a non-portable practice. The use of extensions to the standard language is, of course, another source of non-portability, but this is handled as a separate case. To check a program for true portability, both the <code>-portability</code> and the <code>-f77</code> flags should be used. They are both turned off by default. The <code>-wordsize</code> setting is provided to check only those nonportable usages that depend on a particular machine wordsize. </p>
<p> &#8220;Possibly misleading appearance&#8221; is used for legal constructions that may not mean what they appear to mean at first glance. For example, Fortran is insensitive to blank space, so extraneous space within variable names or the lack of space between a keyword and a variable can convey the wrong impression to the reader. These messages can be suppressed by turning off the <code>-pretty</code> flag, which is on by default. </p>
<p> Other messages that are given after all the files are processed, and having to do with agreement between modules, do not use the word &#8220;warning&#8221; but generally fall into that category. Examples include type mismatches between corresponding variables in different COMMON block declarations, or between dummy and actual arguments of a subprogram. These warnings are controlled by the <code>-common</code> and <code>-arguments</code> settings respectively. By default both are set for maximum strictness of checking. </p>
<p> Another group of warnings about conditions that are often harmless refer to cases where the array properties of a variable passed as a subprogram argument differ between the two routines. For instance, an array element might be passed to a subroutine that expects a whole array. This is a commonly-used technique for processing single rows or columns of two-dimensional arrays. However, it could also indicate a programming error. The <code>-array</code> setting allows the user to adjust the degree of strictness to be used in checking this kind of agreement between actual and dummy array arguments. By default the strictness is maximum. </p>
<p> &#8220;Oops&#8221; indicates a technical problem, meaning either a bug in <code>ftnchek</code> or that its resources have been exceeded. </p>
<p> The syntax error messages and warnings include the filename along with the line number and column number. <code>ftnchek</code> has two different options for the appearance of these error messages. If <code>-novice</code> is in effect, which is the default, the messages are in a style approximating normal English. (In default style, the filename is not printed in messages within the body of the program if <code>-list</code> is in effect.) The other style of error messages is selected by the <code>-nonovice</code> option. In this style, the appearance of the messages is similar to that of the UNIX <code>lint</code> program. </p>
<p> <code>ftnchek</code> is still blind to some kinds of syntax errors. The two most important ones are detailed checking of FORMAT statements, and almost anything to do with control of execution flow by means of IF, DO, and GOTO statements: namely correct nesting of control structures, matching of opening statements such as IF &#8230; THEN with closing statements such as ENDIF, and the proper use of statement labels (numbers). Most compilers will catch these errors. See the section on Limitations for a more detailed discussion. </p>
<p> If <code>ftnchek</code> gives you a syntax error message when the compiler does not, it may be because your program contains an extension to standard Fortran which is accepted by the compiler but not by <code>ftnchek</code>. (See the section on Extensions.) On a VAX/VMS system, you can use the compiler option /STANDARD to cause the compiler to accept only standard Fortran. On most UNIX or UNIX-like systems, this can be accomplished by setting the flag <code>-ansi.</code> </p>
<p> Many of the messages given by <code>ftnchek</code> are self-explanatory. Those that need some additional explanation are listed below in alphabetical order.</p>
<dl>
<dt><i>Common block NAME: data type mismatch at position n</i></p>
<dd> The <i>n</i>-th variable in the COMMON block differs in data type in two different declarations of the COMMON block. By default (<code>-common</code> strictness level 3), <code>ftnchek</code> is very picky about COMMON blocks: the variables listed in them must match exactly by data type and array dimensions. That is, the legal pair of declarations in different modules: </p>
<pre>
     COMMON /COM1/ A,B
and
     COMMON /COM1/ <a href="//www.systutorials.com/docs/linux/man/2-A/">A</a>(2)
</pre>
<p> will cause <code>ftnchek</code> to give warnings at strictness level 3. These two declarations are legal in Fortran since they both declare two real variables. At strictness level 1 or 2, no warning would be given in this example, but the warning would be given if there were a data type mismatch, for instance, if B were declared INTEGER. Controlled by <code>-common</code> setting. </p>
<dt><i>Common block NAME has long data type following short data type</i></p>
<dd> Some compilers require alignment of multi-byte items so that each item begins at an address that is a multiple of the item size. Thus if a short (e.g. single-precision real) item is followed by a long (e.g. double precision real) item, the latter may not be aligned correctly. Controlled by <code>-portability=common-alignment</code> option. </p>
<dt><i>Common block NAME has mixed character and non-character variables</i></p>
<dd> The ANSI standard requires that if any variable in a COMMON block is of type CHARACTER, then all other variables in the same COMMON block must also be of type CHARACTER. Controlled by <code>-f77=mixed-common</code> option. </p>
<dt><i>Common block NAME: varying length</i></p>
<dd> For <code>-common</code> setting level 2, this message means that a COMMON block is declared to have different numbers of words in two different subprograms. A word is the amount of storage occupied by one integer or real variable. For <code>-common</code> setting level 3, it means that the two declarations have different numbers of variables, where an array of any size is considered one variable. This is not necessarily an error, but it may indicate that a variable is missing from one of the lists. Note that according to the Fortran 77 Standard, it is an error for named COMMON blocks (but not blank COMMON) to differ in number of words in declarations in different modules. Given for <code>-common</code> setting 2 or 3. </p>
<dt><i>Error: Badly formed logical/relational operator or constant</i></p>
<dd>
<dt><i>Error: Badly formed real constant</i></p>
<dd> The syntax analyzer has found the start of one of the special words that begin and end with a period (e.g. .EQ.), or the start of a numeric constant, but did not succeed in finding a complete item of that kind. </p>
<dt><i>Error: cannot be adjustable size in module NAME</i></p>
<dd> A character variable cannot be declared with a size that is an asterisk in parentheses unless it is a dummy argument, a parameter, or the name of the function defined in the module. </p>
<dt><i>Error: cannot be declared in SAVE statement in module NAME</i></p>
<dd> Only local variables and common blocks can be declared in a SAVE statement. </p>
<dt><i>Error: No path to this statement</i></p>
<dd> <code>ftnchek</code> will detect statements which are ignored or by-passed because there is no foreseeable route to the statement. For example, an unnumbered statement (a statement without a statement label), occurring immediately after a GOTO statement, cannot possibly be executed. </p>
<dt><i>Error: Parse error</i></p>
<dd> This means that the parser, which analyzes the Fortran program into expressions, statements, etc., has been unable to find a valid interpretation for some portion of a statement in the program. If your compiler does not report a syntax error at the same place, the most common explanations are: (1) use of an extension to ANSI standard Fortran that is not recognized by <code>ftnchek</code>, or (2) the statement requires more lookahead than <code>ftnchek</code> uses (see section on Bugs).</p>
<dt>
<dd> NOTE: This message means that the affected statement is not interpreted. Therefore, it is possible that <code>ftnchek</code>&#8216;s subsequent processing will be in error, if it depends on any matters affected by this statement (type declarations, etc.). </p>
<dt><i>Error: Syntax error</i></p>
<dd> This is the same as &#8220;Error: Parse error&#8221; (see above). It is generated if your version of <code>ftnchek</code> was built using the UNIX <code>yacc</code> parser generator rather than GNU <code>bison</code>. </p>
<dt><i>Identifiers which are not unique in first six chars</i></p>
<dd> Warns that two identifiers which are longer than 6 characters do not differ in the first 6 characters. This is for portability: they may not be considered distinct by some compilers. Controlled by <code>-sixchar</code> option. </p>
<dt><i>Nonportable usage: argument precision may not be correct for intrinsic function</i></p>
<dd> The precision of an argument passed to an intrinsic function may be incorrect on some computers. Issued when a numeric variable declared with explicit precision (e.g. REAL*8 X) is passed to a specific intrinsic function (e.g. DSQRT(X)). Controlled by <code>-portability=mixed-size</code> and <code>-wordsize</code>. </p>
<dt><i>Nonportable usage: character constant/variable length exceeds 255</i></p>
<dd> Some compilers do not support character strings more than 255 characters in length. Controlled by <code>-portability=long-string</code>. </p>
<dt><i>Nonportable usage: File contains tabs</i></p>
<dd> <code>ftnchek</code> expands tabs to be equivalent to spaces up to the next column which is a multiple of 8. Some compilers treat tabs differently, and also it is possible that files sent by electronic mail will have the tabs converted to blanks in some way. Therefore files containing tabs may not be compiled correctly after being transferred. <code>ftnchek</code> does not give this message if tabs only occur within comments or character constants. Controlled by <code>-portability=tab</code>. </p>
<dt><i>Nonportable usage: non-integer DO loop bounds</i></p>
<dd> This warning is only given when the DO index and bounds are non-integer. Use of non-integer quantities in a DO statement may cause unexpected errors, or different results on different machines, due to roundoff effects. Controlled by <code>-portability=real-do</code>. </p>
<dt><i>Possibly it is an array which was not declared</i></p>
<dd> This message is appended to warnings related to a function invocation or to an argument type mismatch, for which the possibility exists that what appears to be a function is actually meant to be an array. If the programmer forgot to dimension an array, references to the array will be interpreted as function invocations. This message will be suppressed if the name in question appears in an EXTERNAL or INTRINSIC statement. Controlled by the <code>-novice</code> option. </p>
<dt><i>Possibly misleading appearance: characters past 72 columns</i></p>
<dd> The program is being processed with the statement field width at its standard value of 72, and some nonblank characters have been found past column 72. In this case, <code>ftnchek</code> is not processing the characters past column 72, and is notifying the user that the statement may not have the meaning that it appears to have. These characters might be intended by the programmer to be significant, but they will be ignored by the compiler. Controlled by <code>-pretty=long-line</code>. </p>
<dt><i>Possibly misleading appearance: Common block declared in more than one statement</i></p>
<dd> Such multiple declarations are legal and have the same effect as a continuation of the original declaration of the block. This warning is only given if the two declarations are separated by one or more intervening statements. Controlled by <code>-pretty=multiple-common</code>. </p>
<dt><i>Possibly misleading appearance: Continuation follows comment or blank line</i></p>
<dd> <code>ftnchek</code> issues this warning message to alert the user that a continuation of a statement is interspersed with comments, making it easy to overlook. Controlled by <code>-pretty=continuation</code>. </p>
<dt><i>Possibly misleading appearance: Extraneous parentheses</i></p>
<dd> Warns about parentheses surrounding a variable by itself in an expression. When a parenthesized variable is passed as an argument to a subprogram, it is treated as an expression, not as a variable whose value can be modified by the called routine. Controlled by <code>-pretty=parentheses</code>. </p>
<dt><i>Subprogram NAME: argument data type mismatch at position n</i></p>
<dd> The subprogram&#8217;s <i>n</i>-th actual argument (in the CALL or the usage of a function) differs in datatype or precision from the <i>n</i>-th dummy argument (in the SUBROUTINE or FUNCTION declaration). For instance, if the user defines a subprogram by </p>
<pre>
     SUBROUTINE SUBA(X)
     REAL X
</pre>
<p> and elsewhere invokes SUBA by </p>
<pre>
     CALL <a href="//www.systutorials.com/docs/linux/man/2-SUBA/">SUBA</a>(2)
</pre>
<p> <code>ftnchek</code> will detect the error. The reason here is that the number 2 is integer, not real. The user should have written </p>
<pre>
     CALL SUBA(2.0)
</pre>
<dt>
<dd> When checking an argument which is a subprogram, <code>ftnchek</code> must be able to determine whether it is a function or a subroutine. The rules used by <code>ftnchek</code> to do this are as follows: If the subprogram, besides being passed as an actual argument, is also invoked directly elsewhere in the same module, then its type is determined by that usage. If not, then if the name of the subprogram does not appear in an explicit type declaration, it is assumed to be a subroutine; if it is explicitly typed it is taken as a function. Therefore, subroutines passed as actual arguments need only be declared by an EXTERNAL statement in the calling module, whereas functions must also be explicitly typed in order to avoid generating this error message. Controlled by <code>-arguments</code> setting. </p>
<dt><i>Subprogram NAME: argument arrayness mismatch at position n</i></p>
<dd> Similar to the preceding situation, but the subprogram dummy argument differs from the corresponding actual argument in its number of dimensions or number of elements. Controlled by <code>-array</code> together with <code>-arguments</code> settings. </p>
<dt><i>Subprogram NAME: argument mismatch at position n</i></p>
<dd> A character dummy argument is larger than the corresponding actual argument, or a Hollerith dummy argument is larger than the corresponding actual argument. Controlled by <code>-arguments</code> setting. </p>
<dt><i>Subprogram NAME: argument usage mismatch</i></p>
<dd> <code>ftnchek</code> detects a possible conflict between the way a subprogram uses an argument and the way in which the argument is supplied to the subprogram. The conflict can be one of two types, as outlined below. </p>
<dt>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd> <i>Dummy arg is modified, Actual arg is const or expr</i> A dummy argument is an argument as named in a SUBROUTINE or FUNCTION statement and used within the subprogram. An actual argument is an argument as passed to a subroutine or function by the caller. <code>ftnchek</code> is saying that a dummy argument is modified by the subprogram, implying that its value is changed in the calling module. The corresponding actual argument should not be a constant or expression, but rather a variable or array element which can be legitimately assigned to. Controlled by the <code>-usage=arg-const-modified</code> option. </p>
<dt>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd> <i>Dummy arg used before set, Actual arg not set</i> Here a dummy argument may be used in the subprogram before having a value assigned to it by the subprogram. The corresponding actual argument should have a value assigned to it by the caller prior to invoking the subprogram. Controlled by the <code>-usage=var-uninitialized</code> option.</p>
<dt>
<dd> This warning is not affected by the <code>-arguments</code> setting. </p>
<dt><i>Subprogram NAME invoked inconsistently</i></p>
<dd> Here the mismatch is between the datatype of the subprogram itself as used and as defined. For instance, if the user declares </p>
<pre>
     INTEGER FUNCTION COUNT(A)
</pre>
<p> and invokes COUNT in another module as </p>
<pre>
     N = COUNT(A)
</pre>
<p> without declaring its datatype, it will default to real type, based on the first letter of its name. The calling module should have included the declaration </p>
<pre>
     INTEGER COUNT
</pre>
<dt>
<dd> Given for <code>-arguments</code> setting 2 or 3. </p>
<dt><i>Subprogram NAME: varying length argument lists:</i></p>
<dd> An inconsistency has been found between the number of dummy arguments (parameters) a subprogram has and the number of actual arguments given it in an invocation. <code>ftnchek</code> keeps track of all invocations of subprograms (CALL statements and expressions using functions) and compares them with the definitions of the subprograms elsewhere in the source code. The Fortran compiler normally does not catch this type of error. Given for <code>-arguments</code> setting 1 or 3. </p>
<dt><i>Variable not declared. Type has been implicitly defined</i></p>
<dd> When printing the symbol table for a module, <code>ftnchek</code> will flag with an asterisk all identifiers that are not explicitly typed and will show the datatype that was assigned through implicit typing. This provides support for users who wish to declare all variables as is required in Pascal or some other languages. This message appears only when the <code>-symtab</code> option is in effect. Alternatively, use the <code>-declare</code> flag if you want to get a list of all undeclared variables. </p>
<dt><i>Variables declared but never referenced</i></p>
<dd> Detects any identifiers that were declared in your program but were never used, either to be assigned a value or to have their value accessed. Variables in COMMON are excluded. Controlled by the <code>-usage=var-unused</code> option. </p>
<dt><i>Variables set but never used</i></p>
<dd> <code>ftnchek</code> will notify the user when a variable has been assigned a value, but the variable is not otherwise used in the program. Usually this results from an oversight. Controlled by the <code>-usage=var-set-unused</code> option. </p>
<dt><i>Variables used before set</i></p>
<dd> This message indicates that an identifier is used to compute a value prior to its initialization. Such usage may lead to an incorrect value being computed, since its initial value is not controlled. Controlled by the <code>-usage=var-uninitialized</code> option. </p>
<dt><i>Variables may be used before set</i></p>
<dd> Similar to used before set except that <code>ftnchek</code> is not able to determine its status with certainty. <code>ftnchek</code> assumes a variable may be used before set if the first usage of the variable occurs prior in the program text to its assignment. Controlled by the <code>-usage=var-uninitialized</code> option. </p>
<dt><i>Warning: DO index is not integer</i></p>
<dd> This warning is only given when the DO bounds are integer, but the DO index is not. It may indicate a failure to declare the index to be an integer. Controlled by <code>-truncation=real-do</code> option. </p>
<dt><i>Warning: integer quotient expr &#8230; converted to real</i></p>
<dd> The quotient of two integers results in an integer type result, in which the fractional part is dropped. If such an integer expression involving division is later converted to a real datatype, it may be that a real type division had been intended. Controlled by <code>-truncation=int-div-real</code> option. </p>
<dt><i>Warning: Integer quotient expr &#8230; used in exponent</i></p>
<dd> The quotient of two integers results in an integer type result, in which the fractional part is dropped. If such an integer expression is used as an exponent, it is quite likely that a real type division was intended. Controlled by <code>-truncation=int-div-exponent</code> option. </p>
<dt><i>Warning: NAME not set when RETURN encountered</i></p>
<dd> The way that functions in Fortran return a value is by assigning the value to the name of the function. This message indicates that the function was not assigned a value before the point where a RETURN statement was found. Therefore it is possible that the function could return an undefined value. </p>
<dt><i>Warning: Nonstandard syntax: adjustable size cannot be concatenated here</i></p>
<dd> The Fortran 77 Standard (sec. 6.2.2) forbids concatenating character variables whose size is an asterisk in parentheses, except in an assignment statement. Controlled by <code>-f77=mixed-expr</code>. </p>
<dt><i>Warning: Nonstandard syntax : significant characters past 72 columns</i></p>
<dd> This warning is given under the <code>-f77=long-line</code> setting if the <code>-columns</code> setting has been used to increase the statement field width, and a statement has meaningful program text beyond column 72. Standard Fortran ignores all text in those columns, but some compilers do not. Thus the program may be treated differently by different compilers. </p>
<dt><i>Warning: Nonstandard syntax : Statement out of order.</i></p>
<dd> <code>ftnchek</code> will detect statements that are out of the sequence specified for ANSI standard Fortran 77. Table 1 illustrates the allowed sequence of statements in the Fortran language. Statements which are out of order are nonetheless interpreted by <code>ftnchek</code>, to prevent &#8220;cascades&#8221; of error messages. The sequence counter is also rolled back to prevent repetition of the error message for a block of similar statements. Controlled by the <code>-f77=statement-order</code> option.</p>
<dt>
<dd>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- | | implicit | parameter | -- -- -- -- -- -- -- -- -- -- - | | other specification format | -- -- -- -- -- -- -- - | -- -- -- -- -- -- -- -- -- -- -and | | statement - function entry | data | -- -- -- -- -- -- -- -- -- -- - | | executable-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --Table 1
</code></pre>
<dt><i>Warning: Possible division by zero</i></p>
<dd> This message is printed out wherever division is done (except division by a constant). Use it to help locate a runtime division by zero problem. Controlled by <code>-division</code> option. </p>
<dt><i>Warning: real truncated to intg</i></p>
<dd> <code>ftnchek</code> has detected an assignment statement which has a real expression on the right, but an integer variable on the left. The fractional part of the real value will be lost. If you explicitly convert the real expression to integer using the INT or NINT intrinsic function, no warning will be printed. A similar message is printed if a double precision expression is assigned to a single precision variable, etc. Controlled by <code>-truncation=demotion</code> option. </p>
<dt><i>Warning: subscript is not integer</i></p>
<dd> Since array subscripts are normally integer quantities, the use of a non-integer expression here may signal an error. Controlled by <code>-truncation=real-subscript</code> option. </p>
<dt><i>Warning: Unknown intrinsic function</i></p>
<dd> This message warns the user that a name declared in an INTRINSIC statement is unknown to <code>ftnchek</code>. Probably it is a nonstandard intrinsic function, and so the program will not be portable. The function will be treated by <code>ftnchek</code> as a user-defined function. This warning is not suppressed by any option, since it affects <code>ftnchek</code>&#8216;s analysis of the program. However, if the intrinsic function is in one of the supported sets of nonstandard intrinsics, you can use the <code>-intrinsic</code> setting to cause <code>ftnchek</code> to recognize it. </p>
</dl>
<h2>LIMITATIONS AND EXTENSIONS</h2>
<p> <code>ftnchek</code> accepts ANSI standard Fortran-77 programs with some minor limitations and numerous common extensions.</p>
<dl>
<dt><code>Limitations</code>:</p>
<dd>
<dl>
<dt>
<dd> The dummy arguments in statement functions are treated like ordinary variables of the program. That is, their scope is the entire subprogram, not just the statement function definition. </p>
<p> The checking of FORMAT statements is lax, tolerating missing separators (comma, etc.) between format descriptors in places where the Standard requires them, and allowing <i>.d</i> fields on descriptors that should not have them. It does warn under <code>-f77=format-edit-descr</code> about nonstandard descriptor types (like O), and supported extensions. </p>
<p> There are some syntactic extensions and Fortran 90 elements that <code>ftnchek</code> accepts but does very little checking. For instance, pointer usage (whether the nonstandard Cray syntax or the Fortran 90 syntax) is not checked other than for set and used status. It is hoped that some day more thorough checking will be implemented, but for now the user should regard the acceptance of these syntactic features simply as a convenience to enable checking of other aspects of code that contains them. See the section Extensions for specifics about what features are accepted but not fully checked. </p>
<p> If a user-supplied subprogram has the same name as one of the nonstandard intrinsic functions recognized by <code>ftnchek</code>, it must be declared in an EXTERNAL statement in any routine that invokes it. Otherwise it will be subject to the checking normally given to the intrinsic function. Since the nonstandard intrinsics are not standard, this EXTERNAL statement is not required by the Fortran 77 Standard. Using the <code>-intrinsic=none</code> setting, recognition of most nonstandard intrinsics (excepting only those needed to support the double complex data type) can be turned off. See the lists of supported nonstandard intrinsic functions under the discussion of the <code>-intrinsic</code> setting above.</dl>
<dt><code>Extensions</code>:</p>
<dd>
<dl>
<dt>
<dd> All of these extensions (except lower-case characters) will generate warnings if the relevant <code>-f77</code> option is set. Some of the extensions listed below are part of the Fortran-90 Standard. These are indicated by the notation (F90). </p>
<p> Tabs are permitted, and translated into equivalent blanks which correspond to tab stops every 8 columns. The standard does not recognize tabs. Note that some compilers allow tabs, but treat them differently. The treatment defined for DEC FORTRAN can be achieved using the <code>-source=dec-tab</code> setting. </p>
<p> Strings may be delimited by either quote marks or apostrophes. A sequence of two delimiter characters is interpreted as a single embedded delimiter character. (F90) </p>
<p> Strings may contain UNIX-style backslash escape sequences. They will be interpreted as such if the <code>-source=unix-backslash</code> setting is given. Otherwise the backslash character will be treated as a normal printing character. </p>
<p> Source code can be in either Fortran 90 free format or traditional fixed format. (F90) </p>
<p> A semicolon is allowed as a statement separator. (F90) </p>
<p> Lower case characters are permitted, and are converted internally to uppercase except in character strings. The standard specifies upper case only, except in comments and strings. (F90) </p>
<p> Hollerith constants are permitted, in accordance with the Fortran 77 Standard, appendix C. They should not be used in expressions, or confused with datatype CHARACTER. </p>
<p> The letter &#8216;D&#8217; (upper or lower case) in column 1 is treated as the beginning of a comment. There is no option to treat such lines as statements instead of comments. </p>
<p> Statements may be longer than 72 columns provided that the setting <code>-columns</code> was used to increase the limit. According to the standard, all text from columns 73 through 80 is ignored, and no line may be longer than 80 columns. </p>
<p> Variable names may be longer than six characters. The standard specifies six as the maximum. <code>ftnchek</code> permits names up to 31 characters long (F90). </p>
<p> Variable names may contain underscores and dollar signs (or other non-alphabetic characters as specified by the <code>-identifier-chars</code> option). These characters are are treated the same as alphabetic letters. The default type for variables beginning with these characters is REAL. In IMPLICIT type statements specifying a range of characters, the dollar sign follows Z and is followed by underscore. (Any other user-defined characters are treated the same as the dollar sign.) Fortran 90 permits underscores in variable names. </p>
<p> The UNIX version tolerates the presence of preprocessor directives, namely lines beginning with the pound sign (#). These are treated as comments, except for #line directives, which are interpreted, and are used to set the line number and source file name for warnings and error messages. Note that #include directives are not processed by <code>ftnchek</code>. Programs that use them for including source files should be passed through the preprocessor before being input to <code>ftnchek</code>. As noted below, <code>ftnchek</code> does process INCLUDE statements, which have a different syntax. An optional program, <code><a href="//www.systutorials.com/docs/linux/man/1L-ftnpp/">ftnpp</a></code>(1L) (available separately) provides preprocessing that properly handles INCLUDE files. </p>
<p> The Fortran 90 DO &#8230; ENDDO control structure is permitted. The CYCLE and EXIT statements are accepted. All of these may have an optional do-construct name, but construct names are not checked for consistency. (F90) </p>
<p> The Fortran 90 SELECT CASE construct is accepted. (F90) </p>
<p> Construct names are also accepted on IF, THEN, ELSE, ENDIF and SELECT CASE statements. (F90) </p>
<p> The ACCEPT and TYPE statements (for terminal I/O) are permitted, with the same syntax as PRINT. </p>
<p> The so-called &#8220;Cray pointer&#8221; syntax is tolerated. It is not the same as the Fortran 90 POINTER statement. There is no real checking of the statement other than basic syntax. The form of this statement is<br />
 POINTER (<i>pointer</i>, <i>pointee</i>) [,(<i>pointer</i>, <i>pointee</i>)]<br />
 The pointer variables are assigned a data type of INTEGER *4. Usage checking of the pointee variables is suppressed, since in practice they are accessed indirectly via the pointers. </p>
<p> The following Fortran 90 pointer related syntaxes are accepted: ALLOCATABLE, POINTER, and TARGET statements and the same attributes in type declarations; ALLOCATE, DEALLOCATE, and NULLIFY executable statements; pointer assignment using =&gt; operator; and the intrinsic functions ALLOCATED and ASSOCIATED. Little semantic checking of pointer variables and operations is done beyond basic set and used status. For instance, there is no checking for such errors as dangling pointers, or use of unallocated arrays. </p>
<p> Statements may have any number of continuation lines. The Fortran 77 and Fortran 90 standards allow a maximum of 19 in fixed source form. The Fortran 90 standard allows a maximum of 39 in free source form. </p>
<p> Relational (comparison) operators composed of punctuation, namely: &lt; &lt;= == /= &gt; &gt;= are allowed. (F90) </p>
<p> Inline comments, beginning with an exclamation mark, are permitted. (F90) </p>
<p> NAMELIST I/O is supported. The syntax is the same as in Fortran 90. </p>
<p> FORMAT statements can contain a dollar sign to indicate suppression of carriage-return. An integer expression enclosed in angle brackets can be used anywhere in a FORMAT statement where the Fortran 77 Standard allows an integer constant (except for the length of a Hollerith constant), to provide a run-time value for a repeat specification or field width. </p>
<p> Nonstandard keywords are allowed in I/O statements, corresponding to those in VMS Fortran. </p>
<p> The IMPLICIT NONE statement is supported. The meaning of this statement is that all variables must have their data types explicitly declared. Rather than flag the occurrences of such variables with syntax error messages, <code>ftnchek</code> waits till the end of the module, and then prints out a list of all undeclared variables, as it does for the <code>-declare</code> option. (F90) </p>
<p> Data types INTEGER, REAL, COMPLEX, and LOGICAL are allowed to have an optional precision specification in type declarations. For instance, REAL*8 means an 8-byte floating point data type. The REAL*8 datatype is not necessarily considered equivalent to DOUBLE PRECISION, depending on the <code>-wordsize</code> setting. The Fortran 77 Standard allows a length specification only for CHARACTER data. </p>
<p> <code>ftnchek</code> supports the DOUBLE COMPLEX type specification for a complex quantity whose real and imaginary parts are double precision. Mixed-mode arithmetic involving single-precision complex with double-precision real data, prohibited under the Standard, yields a double complex result. </p>
<p> Combined type declarations and data-statement-like initializers are accepted. These have the form of a standard Fortran 77 type declaration, followed by a slash-delimited list of constants like that used in a DATA statement. An example of the syntax is<br />
 INTEGER N / 100 /<br />
 This bastard form of initializing declaration was not adopted in Fortran 90. Such declarations should be written using the standard form described below, which is accepted by <code>ftnchek</code>. </p>
<p> There is limited support for Fortran 90 attribute-based type declarations. This style of declaration is distinguished by the use of a double colon (::) between the list of attributes and the list of declared variables. The features supported may be adequate for novice programmers, but are not yet sufficient for professional-quality Fortran 90 programs. I hope to add support for more features in future releases. I invite volunteers to assist in this task. See the ToDo file in the source code distribution for details. The attributes currently accepted, besides all the usual data types, are DIMENSION, EXTERNAL, INTRINSIC, PARAMETER, and SAVE. The new form of declaration also allows assignment of values to the variables declared. At present, the (LEN=<i>value</i>) form of specifying character lengths is also accepted. Kind specifications, using (KIND=<i>value</i>) are parsed but are not processed: all kinds are treated as default kind. Also, there is little checking of these declarations beyond basic syntax. </p>
<p> Many commonly found nonstandard intrinsic functions are provided. See the discussion of <code>-intrinsic</code> for a list of functions and how to control which ones are recognized. </p>
<p> Argument checking is not tight for those nonstandard intrinsics that take arrays or mixed argument types. </p>
<p> <code>ftnchek</code> permits the INCLUDE statement, which causes inclusion of the text of the given file. The syntax is<br />
 INCLUDE &#8216;<i>filename</i>&#8216;<br />
 This is compatible with Fortran 90. If the <code>-source=vms-include</code> option is given, <code>ftnchek</code> follows VMS conventions with respect to this statement: it assumes a default extension of <i>.for</i> if no filename extension is given, and allows the qualifier /[NO]LIST following the filename, to control the listing of the included file. There is no support for including VMS text modules. </p>
<p> In diagnostic output relating to items contained in include files, the location of the error is specified by both its location in the include file and the location in the parent file where the file was included. </p>
<p> <code>ftnchek</code> accepts PARAMETER statements which lack parentheses. These will be warned about if the <code>-f77=param-noparen</code> flag is given. </p>
<p> <code>ftnchek</code> accepts PARAMETER definitions that involve intrinsic functions and exponentiation by a non-integer exponent. Both of these cases are prohibited by the Fortran 77 Standard, and will be warned about if the <code>-f77=param-intrinsic</code> flag is given. If an intrinsic function value is a compile-time integer constant, <code>ftnchek</code> will evaluate it. This allows better checking if the parameter is used in declaring array sizes. Fortran 90 allows intrinsic functions in PARAMETER definitions. </p>
<p> The intrinsic functions that are evaluated are: <center></p>
<table>
<tr VALIGN=top>
<td>ABS</td>
<td>IABS</td>
<td>DIM</td>
<td>IDIM</td>
<td>MAX
</td>
</tr>
<tr VALIGN=top>
<td>MAX0</td>
<td>MIN</td>
<td>MIN0</td>
<td>MOD</td>
<td>SIGN
</td>
</tr>
<tr VALIGN=top>
<td>ISIGN</td>
<td>LEN</td>
<td>ICHAR</td>
<td>INDEX</td>
<td>
</td>
</tr>
</table>
<p></center><br />
 The functions of integer arguments are evaluated only if the arguments are integer constant expressions. (These may involve integer constants, parameters, and evaluated intrinsic functions.) The function LEN is evaluated if its argument is an expression involving only character constants and variables whose length is not adjustable. The functions ICHAR and INDEX are evaluated only if the arguments are character constants. <code>ftnchek</code> gives a warning if it needs the value of some intrinsic function that is not evaluated.</dl>
</dl>
<h2>NEW FEATURES</h2>
<p> Here are the changes from Version 3.2 to Version 3.3:</p>
<dl>
<dt>1.</p>
<dd> Front-end has been rewritten for unlimited lookahead, eliminating the longstanding bug that caused incorrect interpretation of statements whose ambiguity was not resolved in the first line.</p>
<dt>2.</p>
<dd> The <code>-mkhtml</code> option is now available in the MS-DOS version.</p>
<dt>3.</p>
<dd> Added support for Fortran 90 pointer related syntax: ALLOCATE, DEALLOCATE, and NULLIFY statements; the ALLOCATABLE, POINTER and TARGET attributes in type declarations; the pointer assigment operator =&gt; and intrinsic functions ALLOCATED and ASSOCIATED; and deferred-shape array declarations. At present these new syntax features are accepted but not properly checked. This feature was added by Robert Landrito.</p>
<dt>4.</p>
<dd> The <code>-f77</code> and <code>-f90</code> <code>pointer</code> option controlling warnings about &#8220;Cray pointers&#8221; has been renamed to <code>cray-pointer</code>. The <code>-f77=pointer</code> option now instead controls warnings for code containing Fortran 90 pointer-related syntax.</p>
<dt>5.</p>
<dd> Re-implemented <code>-mkhtml</code> processing so it is now much faster on source files containing many routines.</p>
<dt>6.</p>
<dd> Changed the arrangement of the test directory so there is no longer any need to modify the distribution in order to run the test suite (<i>check.bat</i>) under MS-DOS.</p>
<dt>7.</p>
<dd> Fixed bug in reading numeric settings on command line when setting name abbreviated to 3 characters.</p>
<dt>8.</p>
<dd> Fixed bug causing spurious warning for a GOTO referring to a labeled END statement when the statement before END was a FORMAT.</p>
<dt>9.</p>
<dd> New flag <code>-f77=character</code> to control warnings about extensions to the Fortran 77 character data type. Accompanying this new flag is support for Fortran 90 rules for character variable declarations that evaluate to zero or negative length, allowing them and treating negative length values as zero.</p>
<dt>10.</p>
<dd> Fixed minor bug in printing of comments and blank lines following last END statement in <code>-list</code> mode.</dl>
<h2>BUGS</h2>
<p> <code>ftnchek</code> still has much room for improvement. Your feedback is appreciated. We want to know about any bugs you notice. Bugs include not only cases in which <code>ftnchek</code> issues an error message where no error exists, but also if <code>ftnchek</code> fails to issue a warning when it ought to. Note, however, that <code>ftnchek</code> is not intended to catch all syntax errors (see section on Limitations). Also, it is not considered a bug for a variable to be reported as used before set, if the reason is that the usage of the variable occurs prior in the text to where the variable is set. For instance, this could occur when a GOTO causes execution to loop backward to some previously skipped statements. <code>ftnchek</code> does not analyze the program flow, but assumes that statements occurring earlier in the text are executed before the following ones. </p>
<p> We especially want to know if <code>ftnchek</code> crashes for any reason. It is not supposed to crash, even on programs with syntax errors. Suggestions are welcomed for additional features which you would find useful. Tell us if any of <code>ftnchek</code>&#8216;s messages are incomprehensible. Comments on the readability and accuracy of this document are also welcome. </p>
<p> You may also suggest support for additional extensions to the Fortran language. These will be included only if it is felt that the extensions are sufficiently widely accepted by compilers. </p>
<p> If you find a bug in <code>ftnchek</code>, first consult the list of known bugs below to see if it has already been reported. Also check the section entitled &#8220;Limitations and Extensions&#8221; above for restrictions that could be causing the problem. If you do not find the problem documented in either place, then send a report including</p>
<dl>
<dt>1.</p>
<dd> The operating system and CPU type on which <code>ftnchek</code> is running.</p>
<dt>2.</p>
<dd> The version of <code>ftnchek</code> and values of any environment options or settings defined in startup file. (Capturing the output of ftnchek -help is useful for this.)</p>
<dt>3.</p>
<dd> A brief description of the bug.</p>
<dt>4.</p>
<dd> If possible, a small sample program showing the bug.</dl>
<p> The report should be sent to Dr. Robert Moniot (see contact information in section entitled &#8220;Installation and Support&#8221;). </p>
<p> Highest priority will be given to bugs which cause <code>ftnchek</code> to crash. </p>
<p> Certain problems that arise when checking large programs can be fixed by increasing the sizes of the data areas in <code>ftnchek</code>. (These problems are generally signaled by error messages beginning with &#8220;Oops&#8221;.) The simplest way to increase the table sizes is by recompiling <code>ftnchek</code> with the LARGE_MACHINE macro name defined. Consult the makefile and README file for the method of doing this. </p>
<p> The following is a list of known bugs.</p>
<dl>
<dt>1.</p>
<dd> Bug: Used-before-set message is suppressed for any variable which is used as the loop index in an implied-do loop, even if it was in fact used before being set in some earlier statement. For example, consider J in the statement</p>
<dl>
<dt>
<dd>
<pre>
      WRITE(5,*) (A(J), J=1,10)
</pre>
<p> Here <code>ftnchek</code> parses the I/O expression, A(J), where J is used, before it parses the implied loop where J is set. Normally this would cause <code>ftnchek</code> to report a spurious used-before-set warning for J. Since this report is usually in error and occurs fairly commonly, <code>ftnchek</code> suppresses the warning for J altogether. </p>
<p> Prognosis: A future version of <code>ftnchek</code> is planned which will handle implied-do loops correctly.</dl>
<dt>2.</p>
<dd> Bug: Variables used (not as arguments) in statement-function subprograms do not have their usage status updated when the statement function is invoked.</p>
<dl>
<dt>
<dd>
<p> Prognosis: To be fixed in a future version of <code>ftnchek</code>.</dl>
<dt>3.</p>
<dd> Bug: VAX version does not expand wildcards in filenames on the command line if they are followed without space by an option, e.g. ftnchek *.f/calltree would not expand the *.f. This is because VMS-style options without intervening space are not supported by the GNU shell_mung routine that is used to expand wildcards.</p>
<dl>
<dt>
<dd>
<p> Prognosis: unlikely to be fixed.</dl>
<dt>4.</p>
<dd> Bug: checking for nonstandard format edit descriptors is done only in FORMAT statements, not in character strings used as formats.</p>
<dl>
<dt>
<dd>
<p> Prognosis: may be fixed someday.</dl>
</dl>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>ftnchek</code> was designed by Dr. Robert Moniot, professor at Fordham University. During the academic year of 1988-1989, Michael Myers and Lucia Spagnuolo developed the program to perform the variable usage checks. During the following year it was augmented by Lois Bigbie to check subprogram arguments and COMMON block declarations. Brian Downing assisted with the implementation of the INCLUDE statement. John Quinn wrote the common block usage checks. Heba Elsayed wrote the label table printout and label usage checks. Nelson H. F. Beebe of the University of Utah added most of the new code to implement the <code>-makedcls</code> feature and wrote the dcl2inc script. The <code>-mkhtml</code> feature was contributed by Mark McVeigh of Framatome ANP, Inc. The <code>-reference</code> feature was contributed by Gerome Emmanuel, Ecole des mines, U. Nancy (slightly modified). The <code>-vcg</code> option was contributed by Dr. Philip Rubini of Cranfield University, UK. The support for Cray pointer syntax was provided by John Dannenhoffer of United Technologies Research Center. John C. Bollinger of Indiana University added the parser syntax for the SELECT CASE construct. Robert Landrito added the parser syntax for F90 pointer-related features. Additional features will be added as time permits. As of Version 2.5, the name was changed from <code>forchek</code> to <code>ftnchek</code>, to avoid confusion with a similar program named <code>forcheck</code>, developed earlier at Leiden University. </p>
<p> We would like to thank John Amor of the University of British Columbia, Reg Clemens of the Air Force Phillips Lab in Albuquerque, Markus Draxler of the University of Stuttgart, Victor Eijkhout of the University of Tennessee at Knoxville, Greg Flint of Purdue University, Daniel P. Giesy of NASA Langley Research Center, Fritz Keinert of Iowa State University, Judah Milgram of the University of Maryland College Park, Hugh Nicholas of the Pittsburgh Supercomputing Center, Dan Severance of Yale University, Phil Sterne of Lawrence Livermore National Laboratory, Larry Weissman of the University of Washington, Warren J. Wiscombe of NASA Goddard, and Nelson H. F. Beebe of the University of Utah, for pointing out bugs and suggesting some improvements. Stefan A. Deutscher, Gunnar Duus, Clive Page of the University of Leicester, Stephan Wefing of Heidelberg University, and Bob Wells of Oxford University were extremely helpful as alpha testers. We also thank Jack Dongarra for putting <code>ftnchek</code> into the netlib library of publicly available software.</p>
<h2>INSTALLATION AND SUPPORT</h2>
<p> The <code>ftnchek</code> program is free software. It can be obtained by anonymous ftp from many software servers, including <a href="ftp://netlib.org/fortran">ftp://netlib.org/fortran</a> . Note that on Netlib the distribution is named <i>ftnchek.tar.gz</i> whereas on most other servers the file name includes the version number, e.g. <i>ftnchek-3.3.0.tar.gz</i>. If the file extension is <i>.Z</i>, uncompress with the Unix <code><a href="/docs/linux/man/1-uncompress/">uncompress</a></code>(1) utility. If the file extension is <i>.gz</i>, uncompress with the GNU <code><a href="//www.systutorials.com/docs/linux/man/1L-gunzip/">gunzip</a></code>(1L) program. Then use <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) to unpack the files into a subdirectory. </p>
<p> Installation requires a C compiler for your computer. See the INSTALL file provided with the distribution for instructions on installing <code>ftnchek</code> on your system. Executable binary for particular systems such as IBM PC or Macintosh, as available, can be obtained by anonymous ftp from <a href="ftp://ftp.dsm.fordham.edu/pub/ftnchek">ftp://ftp.dsm.fordham.edu/pub/ftnchek</a> . Assistance in preparing such executable binary forms is welcome. </p>
<p> The <code>nroff</code> version of this document is named <i>ftnchek.man</i>. On UNIX systems, this file can be used as the man page, but actually it is a multi-purpose source file which is used to produce the other forms of the documentation. The cleaned-up man page document, created during installation of <code>ftnchek</code>, is named <i>ftnchek.1</i>. The distribution also includes a plain ASCII version named <i>ftnchek.doc</i>, a PostScript version named <i>ftnchek.ps</i>, an HTML version in directory <i>html</i>, and a VMS HELP version named <i>ftnchek.hlp</i>. </p>
<p> Information about the latest version and the status of the project can be obtained by visiting <code>ftnchek</code>&#8216;s home page, <a rel="nofollow" href="http://www.dsm.fordham.edu/~ftnchek">http://www.dsm.fordham.edu/~ftnchek</a> . For further information and to report bugs, you may contact Dr. Robert Moniot, whose contact information can be found by a Web search for his name and Fordham University. (E-mail address is not provided here because it attracts unsolicited commercial e-mail, but it is easily constructed by combining his last name with the name of the university and the edu domain.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1L-dcl2inc/">dcl2inc</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-dtoq/">dtoq</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-dtos/">dtos</a></code>(1L), <code><a href="/docs/linux/man/1-f77/">f77</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/1L-fd2s/">fd2s</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-fs2d/">fs2d</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-ftnpp/">ftnpp</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-pfort/">pfort</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-qtod/">qtod</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-sf3/">sf3</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-stod/">stod</a></code>(1L). <code><a href="//www.systutorials.com/docs/linux/man/1L-xsf3/">xsf3</a></code>(1L), <code><a href="//www.systutorials.com/docs/linux/man/1L-xvcg/">xvcg</a></code>(1L). </p>
<h2>Index</h2>
