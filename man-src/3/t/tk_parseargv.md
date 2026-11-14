---
title: "tk_parseargv(3)"
name: "tk_parseargv"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_parseargv/"
description: "Tk_ParseArgv – process command-line options"
---

<p>Tk_ParseArgv &#8211; process command-line options </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_ParseArgv</code>(<i>interp, tkwin, argcPtr, argv, argTable, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for returning error messages.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window to use when arguments specify Tk options. If NULL, then no Tk options will be processed.</p>
<dd>int <i>argcPtr</i> (in/out) Pointer to number of arguments in argv; gets modified to hold number of unprocessed arguments that remain after the call.</p>
<dd>const char <i>**argv</i> (in/out) Command line arguments passed to main program. Modified to hold unprocessed arguments that remain after the call.</p>
<dd>Tk_ArgvInfo <i>*argTable</i> (in) Array of argument descriptors, terminated by element with type <code>TK_ARGV_END</code>.</p>
<dd>int <i>flags</i> (in) If non-zero, then it specifies one or more flags that control the parsing of arguments. Different flags may be OR&#8217;ed together. The flags currently defined are <code>TK_ARGV_DONT_SKIP_FIRST_ARG</code>, <code>TK_ARGV_NO_ABBREV</code>, <code>TK_ARGV_NO_LEFTOVERS</code>, and <code>TK_ARGV_NO_DEFAULTS</code>.
</dl>
<h2>Description</h2>
<p><code>Tk_ParseArgv</code> processes an array of command-line arguments according to a table describing the kinds of arguments that are expected. Each of the arguments in <i>argv</i> is processed in turn: if it matches one of the entries in <i>argTable</i>, the argument is processed according to that entry and discarded. The arguments that do not match anything in <i>argTable</i> are copied down to the beginning of <i>argv</i> (retaining their original order) and returned to the caller. At the end of the call <code>Tk_ParseArgv</code> sets <i>*argcPtr</i> to hold the number of arguments that are left in <i>argv</i>, and <i>argv[*argcPtr]</i> will hold the value NULL. Normally, <code>Tk_ParseArgv</code> assumes that <i>argv[0]</i> is a command name, so it is treated like an argument that does not match <i>argTable</i> and returned to the caller; however, if the <code>TK_ARGV_DONT_SKIP_FIRST_ARG</code> bit is set in <i>flags</i> then <i>argv[0]</i> will be processed just like the other elements of <i>argv</i>. </p>
<p> <code>Tk_ParseArgv</code> normally returns the value <code>TCL_OK</code>. If an error occurs while parsing the arguments, then <code>TCL_ERROR</code> is returned and <code>Tk_ParseArgv</code> will leave an error message in <i>interp-&gt;result</i> in the standard Tcl fashion. In the event of an error return, <i>*argvPtr</i> will not have been modified, but <i>argv</i> could have been partially modified. The possible causes of errors are explained below. </p>
<p> The <i>argTable</i> array specifies the kinds of arguments that are expected; each of its entries has the following structure:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 char *<i>key</i>;
 int <i>type</i>;
 char *<i>src</i>;
 char *<i>dst</i>;
 char *<i>help</i>;
} Tk_ArgvInfo;</pre>
</dl>
<p> The <i>key</i> field is a string such as &#8220;-display&#8221; or &#8220;-bg&#8221; that is compared with the values in <i>argv</i>. <i>Type</i> indicates how to process an argument that matches <i>key</i> (more on this below). <i>Src</i> and <i>dst</i> are additional values used in processing the argument. Their exact usage depends on <i>type</i>, but typically <i>src</i> indicates a value and <i>dst</i> indicates where to store the value. The <code>char *</code> declarations for <i>src</i> and <i>dst</i> are placeholders: the actual types may be different. Lastly, <i>help</i> is a string giving a brief description of this option; this string is printed when users ask for help about command-line options. </p>
<p> When processing an argument in <i>argv</i>, <code>Tk_ParseArgv</code> compares the argument to each of the <i>key</i>&#8216;s in <i>argTable</i>. <code>Tk_ParseArgv</code> selects the first specifier whose <i>key</i> matches the argument exactly, if such a specifier exists. Otherwise <code>Tk_ParseArgv</code> selects a specifier for which the argument is a unique abbreviation. If the argument is a unique abbreviation for more than one specifier, then an error is returned. If there is no matching entry in <i>argTable</i>, then the argument is skipped and returned to the caller. </p>
<p> Once a matching argument specifier is found, <code>Tk_ParseArgv</code> processes the argument according to the <i>type</i> field of the specifier. The argument that matched <i>key</i> is called &#8220;the matching argument&#8221; in the descriptions below. As part of the processing, <code>Tk_ParseArgv</code> may also use the next argument in <i>argv</i> after the matching argument, which is called &#8220;the following argument&#8221;. The legal values for <i>type</i>, and the processing that they cause, are as follows:</p>
<dl COMPACT>
<dt><code>TK_ARGV_END</code></p>
<dd>Marks the end of the table. The last entry in <i>argTable</i> must have this type; all of its other fields are ignored and it will never match any arguments.</p>
<dt><code>TK_ARGV_CONSTANT</code></p>
<dd><i>Src</i> is treated as an integer and <i>dst</i> is treated as a pointer to an integer. <i>Src</i> is stored at <i>*dst</i>. The matching argument is discarded.</p>
<dt><code>TK_ARGV_INT</code></p>
<dd>The following argument must contain an integer string in the format accepted by <code>strtol</code> (e.g. &#8220;0&#8221; and &#8220;0x&#8221; prefixes may be used to specify octal or hexadecimal numbers, respectively). <i>Dst</i> is treated as a pointer to an integer; the following argument is converted to an integer value and stored at <i>*dst</i>. <i>Src</i> is ignored. The matching and following arguments are discarded from <i>argv</i>.</p>
<dt><code>TK_ARGV_FLOAT</code></p>
<dd>The following argument must contain a floating-point number in the format accepted by <code>strtol</code>. <i>Dst</i> is treated as the address of a double-precision floating point value; the following argument is converted to a double-precision value and stored at <i>*dst</i>. The matching and following arguments are discarded from <i>argv</i>.</p>
<dt><code>TK_ARGV_STRING</code></p>
<dd>In this form, <i>dst</i> is treated as a pointer to a (char *); <code>Tk_ParseArgv</code> stores at <i>*dst</i> a pointer to the following argument, and discards the matching and following arguments from <i>argv</i>. <i>Src</i> is ignored.</p>
<dt><code>TK_ARGV_UID</code></p>
<dd>This form is similar to <code>TK_ARGV_STRING</code>, except that the argument is turned into a Tk_Uid by calling <code>Tk_GetUid</code>. <i>Dst</i> is treated as a pointer to a Tk_Uid; <code>Tk_ParseArgv</code> stores at <i>*dst</i> the Tk_Uid corresponding to the following argument, and discards the matching and following arguments from <i>argv</i>. <i>Src</i> is ignored.</p>
<dt><code>TK_ARGV_CONST_OPTION</code></p>
<dd>This form causes a Tk option to be set (as if the <code>option</code> command had been invoked). The <i>src</i> field is treated as a pointer to a string giving the value of an option, and <i>dst</i> is treated as a pointer to the name of the option. The matching argument is discarded. If <i>tkwin</i> is NULL, then argument specifiers of this type are ignored (as if they did not exist).</p>
<dt><code>TK_ARGV_OPTION_VALUE</code></p>
<dd>This form is similar to <code>TK_ARGV_CONST_OPTION</code>, except that the value of the option is taken from the following argument instead of from <i>src</i>. <i>Dst</i> is used as the name of the option. <i>Src</i> is ignored. The matching and following arguments are discarded. If <i>tkwin</i> is NULL, then argument specifiers of this type are ignored (as if they did not exist).</p>
<dt><code>TK_ARGV_OPTION_NAME_VALUE</code></p>
<dd>In this case the following argument is taken as the name of a Tk option and the argument after that is taken as the value for that option. Both <i>src</i> and <i>dst</i> are ignored. All three arguments are discarded from <i>argv</i>. If <i>tkwin</i> is NULL, then argument specifiers of this type are ignored (as if they did not exist).</p>
<dt><code>TK_ARGV_HELP</code></p>
<dd>When this kind of option is encountered, <code>Tk_ParseArgv</code> uses the <i>help</i> fields of <i>argTable</i> to format a message describing all the valid arguments. The message is placed in <i>interp-&gt;result</i> and <code>Tk_ParseArgv</code> returns <code>TCL_ERROR</code>. When this happens, the caller normally prints the help message and aborts. If the <i>key</i> field of a <code>TK_ARGV_HELP</code> specifier is NULL, then the specifier will never match any arguments; in this case the specifier simply provides extra documentation, which will be included when some other <code>TK_ARGV_HELP</code> entry causes help information to be returned.</p>
<dt><code>TK_ARGV_REST</code></p>
<dd>This option is used by programs or commands that allow the last several of their options to be the name and/or options for some other program. If a <code>TK_ARGV_REST</code> argument is found, then <code>Tk_ParseArgv</code> does not process any of the remaining arguments; it returns them all at the beginning of <i>argv</i> (along with any other unprocessed arguments). In addition, <code>Tk_ParseArgv</code> treats <i>dst</i> as the address of an integer value, and stores at <i>*dst</i> the index of the first of the <code>TK_ARGV_REST</code> options in the returned <i>argv</i>. This allows the program to distinguish the <code>TK_ARGV_REST</code> options from other unprocessed options that preceded the <code>TK_ARGV_REST</code>.</p>
<dt><code>TK_ARGV_FUNC</code></p>
<dd>For this kind of argument, <i>src</i> is treated as the address of a procedure, which is invoked to process the following argument. The procedure should have the following structure:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>
<pre>int
<i>func</i>(<i>dst</i>, <i>key</i>, <i>nextArg</i>)
 char *<i>dst</i>;
 char *<i>key</i>;
 char *<i>nextArg</i>;
{
}</pre>
</dl>
<p> The <i>dst</i> and <i>key</i> parameters will contain the corresponding fields from the <i>argTable</i> entry, and <i>nextArg</i> will point to the following argument from <i>argv</i> (or NULL if there are not any more arguments left in <i>argv</i>). If <i>func</i> uses <i>nextArg</i> (so that <code>Tk_ParseArgv</code> should discard it), then it should return 1. Otherwise it should return 0 and <code>TkParseArgv</code> will process the following argument in the normal fashion. In either event the matching argument is discarded.</dl>
<dt><code>TK_ARGV_GENFUNC</code></p>
<dd>This form provides a more general procedural escape. It treats <i>src</i> as the address of a procedure, and passes that procedure all of the remaining arguments. The procedure should have the following form:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>
<pre>int
<i>genfunc</i>(dst, interp, key, argc, argv)
 char *<i>dst</i>;
 Tcl_Interp *<i>interp</i>;
 char *<i>key</i>;
 int <i>argc</i>;
 char **<i>argv</i>;
{
}</pre>
</dl>
<p> The <i>dst</i> and <i>key</i> parameters will contain the corresponding fields from the <i>argTable</i> entry. <i>Interp</i> will be the same as the <i>interp</i> argument to <code>Tcl_ParseArgv</code>. <i>Argc</i> and <i>argv</i> refer to all of the options after the matching one. <i>Genfunc</i> should behave in a fashion similar to <code>Tk_ParseArgv</code>: parse as many of the remaining arguments as it can, then return any that are left by compacting them to the beginning of <i>argv</i> (starting at <i>argv</i>[0]). <i>Genfunc</i> should return a count of how many arguments are left in <i>argv</i>; <code>Tk_ParseArgv</code> will process them. If <i>genfunc</i> encounters an error then it should leave an error message in <i>interp-&gt;result</i>, in the usual Tcl fashion, and return -1; when this happens <code>Tk_ParseArgv</code> will abort its processing and return <code>TCL_ERROR</code>.</dl>
</dl>
<h2>Flags</h2>
<dl COMPACT>
<dt><code>TK_ARGV_DONT_SKIP_FIRST_ARG</code></p>
<dd><code>Tk_ParseArgv</code> normally treats <i>argv[0]</i> as a program or command name, and returns it to the caller just as if it had not matched <i>argTable</i>. If this flag is given, then <i>argv[0]</i> is not given special treatment.</p>
<dt><code>TK_ARGV_NO_ABBREV</code></p>
<dd>Normally, <code>Tk_ParseArgv</code> accepts unique abbreviations for <i>key</i> values in <i>argTable</i>. If this flag is given then only exact matches will be acceptable.</p>
<dt><code>TK_ARGV_NO_LEFTOVERS</code></p>
<dd>Normally, <code>Tk_ParseArgv</code> returns unrecognized arguments to the caller. If this bit is set in <i>flags</i> then <code>Tk_ParseArgv</code> will return an error if it encounters any argument that does not match <i>argTable</i>. The only exception to this rule is <i>argv[0]</i>, which will be returned to the caller with no errors as long as <code>TK_ARGV_DONT_SKIP_FIRST_ARG</code> is not specified.</p>
<dt><code>TK_ARGV_NO_DEFAULTS</code></p>
<dd>Normally, <code>Tk_ParseArgv</code> searches an internal table of standard argument specifiers in addition to <i>argTable</i>. If this bit is set in <i>flags</i>, then <code>Tk_ParseArgv</code> will use only <i>argTable</i> and not its default table.</dl>
<h2>Example</h2>
<p>Here is an example definition of an <i>argTable</i> and some sample command lines that use the options. Note the effect on <i>argc</i> and <i>argv</i>; arguments processed by <code>Tk_ParseArgv</code> are eliminated from <i>argv</i>, and <i>argc</i> is updated to reflect reduced number of arguments.</p>
<dl COMPACT>
<dd>
<pre>/*
 * Define and set default values for globals.
 */
int debugFlag = 0;
int numReps = 100;
char defaultFileName[] = &quot;out&quot;;
char *fileName = defaultFileName;
Boolean exec = FALSE;
/*
 * Define option descriptions.
 */
Tk_ArgvInfo argTable[] = {
 {&quot;-X&quot;, TK_ARGV_CONSTANT, (char *) 1, (char *) &amp;debugFlag,
 &quot;Turn on debugging printfs&quot;},
 {&quot;-N&quot;, TK_ARGV_INT, (char *) NULL, (char *) &amp;numReps,
 &quot;Number of repetitions&quot;},
 {&quot;-of&quot;, TK_ARGV_STRING, (char *) NULL, (char *) &amp;fileName,
 &quot;Name of file for output&quot;},
 {&quot;x&quot;, TK_ARGV_REST, (char *) NULL, (char *) &amp;exec,
 &quot;File to exec, followed by any arguments (must be last argument).&quot;},
 {(char *) NULL, TK_ARGV_END, (char *) NULL, (char *) NULL,
 (char *) NULL}
};
main(argc, argv)
 int argc;
 char *argv[];
{
 ...
 if (Tk_ParseArgv(interp, tkwin, &amp;argc, argv, argTable, 0) != TCL_OK) {
 fprintf(stderr, &quot;%s
&quot;, interp-&gt;result);
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 }
 /*
 * Remainder of the program.
 */
}</pre>
</dl>
<p> Note that default values can be assigned to variables named in <i>argTable</i>: the variables will only be overwritten if the particular arguments are present in <i>argv</i>. Here are some example command lines and their effects.</p>
<dl COMPACT>
<dd>
<pre>prog -N 200 infile # just sets the numReps variable to 200
prog -of out200 infile # sets fileName to reference &quot;out200&quot;
prog -XN 10 infile # sets the debug flag, also sets numReps</pre>
</dl>
<p> In all of the above examples, <i>argc</i> will be set by <code>Tk_ParseArgv</code> to 2, <i>argv</i>[0] will be &#8220;prog&#8221;, <i>argv</i>[1] will be &#8220;infile&#8221;, and <i>argv</i>[2] will be NULL.</p>
<h2>Keywords</h2>
<p>arguments, command line, options</p>
