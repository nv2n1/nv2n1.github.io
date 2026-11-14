---
title: "cscope(1)"
name: "cscope"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cscope/"
description: "cscope – interactively examine a C program"
---

<h2>NAME</h2>
<p> cscope &#8211; interactively examine a C program</p>
<h2>SYNOPSIS</h2>
<p> <code>cscope</code> <code>[-bCcdehkLlqRTUuVv]</code> <code>[-F</code><i>symfile</i><code>]</code> <code>[-f</code><i>reffile</i><code>]</code> <code>[-I</code><i>incdir</i><code>]</code> <code>[-i</code><i>namefile</i><code>]</code> <code>[-0123456789</code><i>pattern</i><code>]</code> <code>[-p</code><i>n</i><code>]</code> <code>[-s</code><i>dir</i><code>]</code> <code>[</code><i>files</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>cscope</i> is an interactive, screen-oriented tool that allows the user to browse through C source files for specified elements of code. </p>
<p> By default, <i>cscope</i> examines the C (.c and .h), lex (.l), and yacc (.y) source files in the current directory. <i>cscope</i> may also be invoked for source files named on the command line. In either case, <i>cscope</i> searches the standard directories for #include files that it does not find in the current directory. <i>cscope</i> uses a symbol cross-reference, called cscope.out by default, to locate functions, function calls, macros, variables, and preprocessor symbols in the files. </p>
<p> <i>cscope</i> builds the symbol cross-reference the first time it is used on the source files for the program being browsed. On a subsequent invocation, <i>cscope</i> rebuilds the cross-reference only if a source file has changed or the list of source files is different. When the cross-reference is rebuilt, the data for the unchanged files are copied from the old cross-reference, which makes rebuilding faster than the initial build.</p>
<h2>OPTIONS</h2>
<p> Some command line arguments can only occur as the only argument in the execution of cscope. They cause the program to just print out some output and exit immediately:</p>
<dl>
<dt><code>-h</code></p>
<dd> View the long usage help display.</p>
<dt><code>-V</code></p>
<dd> Print on the first line of screen the version number of cscope.</p>
<dt><code>&#8211;help</code></p>
<dd> Same as <code>-h</code></p>
<dt><code>&#8211;version</code></p>
<dd> Same as <code>-V</code> </p>
</dl>
<p> The following options can appear in any combination:</p>
<dl>
<dt><code>-b</code></p>
<dd> Build the cross-reference only.</p>
<dt><code>-C</code></p>
<dd> Ignore letter case when searching.</p>
<dt><code>-c</code></p>
<dd> Use only ASCII characters in the cross-reference file, that is, do not compress the data.</p>
<dt><code>-d</code></p>
<dd> Do not update the cross-reference.</p>
<dt><code>-e</code></p>
<dd> Suppress the &lt;Ctrl&gt;-e command prompt between files.</p>
<dt><code>-F</code><i>symfile</i></p>
<dd> Read symbol reference lines from <i>symfile. </i> (A symbol reference file is created by &gt; and &gt;&gt;, and can also be read using the &lt; command, described under &#8220;Issuing Subsequent Requests&#8221;, below.)</p>
<dt><code>-f</code><i>reffile</i></p>
<dd> Use <i>reffile </i> as the cross-reference file name instead of the default &quot;cscope.out&quot;.</p>
<dt><code>-I</code><i>incdir</i></p>
<dd> Look in <i>incdir </i> (before looking in $INCDIR, the standard place for header files, normally /usr/include) for any #include files whose names do not begin with &#8220;/&#8221; and that are not specified on the command line or in <i>namefile </i> below. (The #include files may be specified with either double quotes or angle brackets.) The incdir directory is searched in addition to the current directory (which is searched first) and the standard list (which is searched last). If more than one occurrence of -I appears, the directories are searched in the order they appear on the command line.</p>
<dt><code>-i</code><i>namefile</i></p>
<dd> Browse through all source files whose names are listed in <i>namefile</i> (file names separated by spaces, tabs, or new-lines) instead of the default name list file, which is called cscope.files. If this option is specified, cscope ignores any file names appearing on the command line. The argument namefile can be set to &#8220;-&#8221; to accept a list of files from the standard input. Filenames in the namefile that contain whitespace have to be enclosed in &quot;double quotes&quot;. Inside such quoted filenames, any double-quote and backslash characters have to be escaped by backslashes.</p>
<dt><code>-k</code></p>
<dd> &#8220;Kernel Mode&#8221;, turns off the use of the default include dir (usually /usr/include) when building the database, since kernel source trees generally do not use it.</p>
<dt><code>-L</code></p>
<dd> Do a single search with line-oriented output when used with the -num pattern option.</p>
<dt><code>-l</code></p>
<dd> Line-oriented interface (see &#8220;Line-Oriented Interface&#8221; below).</p>
<dt><code>-[</code><i>0-9</i><code>]</code><i>pattern</i></p>
<dd> Go to input field <i>num </i> (counting from 0) and find <i>pattern.</i></p>
<dt><code>-P</code><i>path</i></p>
<dd> Prepend <i>path </i> to relative file names in a pre-built cross-reference file so you do not have to change to the directory where the cross-reference file was built. This option is only valid with the -d option.</p>
<dt><code>-p</code><i>n</i></p>
<dd> Display the last <i>n </i> file path components instead of the default (1). Use <i>0 </i> not to display the file name at all.</p>
<dt><code>-q</code></p>
<dd> Enable fast symbol lookup via an inverted index. This option causes cscope to create 2 more files (default names &#8220;cscope.in.out&#8221; and &#8220;cscope.po.out&#8221;) in addition to the normal database. This allows a faster symbol search algorithm that provides noticeably faster lookup performance for large projects.</p>
<dt><code>-R</code></p>
<dd> Recurse subdirectories during search for source files.</p>
<dt><code>-s</code><i>dir</i></p>
<dd> Look in <i>dir</i> for additional source files. This option is ignored if source files are given on the command line.</p>
<dt><code>-T</code></p>
<dd> Use only the first eight characters to match against C symbols. A regular expression containing special characters other than a period (.) will not match any symbol if its minimum length is greater than eight characters.</p>
<dt><code>-U</code></p>
<dd> Check file time stamps. This option will update the time stamp on the database even if no files have changed.</p>
<dt><code>-u</code></p>
<dd> Unconditionally build the cross-reference file (assume that all files have changed).</p>
<dt><code>-v</code></p>
<dd> Be more verbose in line-oriented mode. Output progress updates during database building and searches.</p>
<dt><i>files</i></p>
<dd> A list of file names to operate on.</dl>
<p> The -I, -c, -k, -p, -q, and -T options can also be in the cscope.files file. </p>
<h3>Requesting the initial search</h3>
<p> After the cross-reference is ready, cscope will display this menu: </p>
<p> <code>Find this C symbol:</code></p>
<dl>
<dt><code>Find this function definition:</code></p>
<dd>
<dt><code>Find functions called by this function:</code></p>
<dd>
<dt><code>Find functions calling this function:</code></p>
<dd>
<dt><code>Find this text string:</code></p>
<dd>
<dt><code>Change this text string:</code></p>
<dd>
<dt><code>Find this egrep pattern:</code></p>
<dd>
<dt><code>Find this file:</code></p>
<dd>
<dt><code>Find files #including this file:</code></p>
<dd></dl>
<p> Press the &lt;Up&gt; or &lt;Down&gt; keys repeatedly to move to the desired input field, type the text to search for, and then press the &lt;Return&gt; key. </p>
<h3>Issuing subsequent requests</h3>
<p> If the search is successful, any of these single-character commands can be used:</p>
<dl>
<dt><code>0-9a-zA-Z</code></p>
<dd> Edit the file referenced by the given line number.</p>
<dt><code>&lt;Space&gt;</code></p>
<dd> Display next set of matching lines.</p>
<dt><code>&lt;Tab&gt;</code></p>
<dd> Alternate between the menu and the list of matching lines</p>
<dt><code>&lt;Up&gt;</code></p>
<dd> Move to the previous menu item (if the cursor is in the menu) or move to the previous matching line (if the cursor is in the matching line list.)</p>
<dt><code>&lt;Down&gt;</code></p>
<dd> Move to the next menu item (if the cursor is in the menu) or move to the next matching line (if the cursor is in the matching line list.)</p>
<dt><code>+</code></p>
<dd> Display next set of matching lines.</p>
<dt><code>&#8211; </code></p>
<dd> Display previous set of matching lines.</p>
<dt><code>^e</code></p>
<dd> Edit displayed files in order.</p>
<dt><code>&gt;</code></p>
<dd> Write the displayed list of lines to a file.</p>
<dt><code>&gt;&gt;</code></p>
<dd> Append the displayed list of lines to a file.</p>
<dt><code>&lt;</code></p>
<dd> Read lines from a file that is in symbol reference format (created by &gt; or &gt;&gt;), just like the -F option.</p>
<dt><code>^</code></p>
<dd> Filter all lines through a shell command and display the resulting lines, replacing the lines that were already there.</p>
<dt><code>|</code></p>
<dd> Pipe all lines to a shell command and display them without changing them.</dl>
<p> At any time these single-character commands can also be used:</p>
<dl>
<dt><code>&lt;Return&gt;</code></p>
<dd> Move to next input field.</p>
<dt><code>^n</code></p>
<dd> Move to next input field.</p>
<dt><code>^p</code></p>
<dd> Move to previous input field.</p>
<dt><code>^y</code></p>
<dd> Search with the last text typed.</p>
<dt><code>^b</code></p>
<dd> Move to previous input field and search pattern.</p>
<dt><code>^f</code></p>
<dd> Move to next input field and search pattern.</p>
<dt><code>^c</code></p>
<dd> Toggle ignore/use letter case when searching. (When ignoring letter case, search for &#8220;FILE&#8221; will match &#8220;File&#8221; and &#8220;file&#8221;.)</p>
<dt><code>^r</code></p>
<dd> Rebuild the cross-reference.</p>
<dt><code>!</code></p>
<dd> Start an interactive shell (type ^d to return to cscope).</p>
<dt><code>^l</code></p>
<dd> Redraw the screen.</p>
<dt><code>?</code></p>
<dd> Give help information about cscope commands.</p>
<dt><code>^d</code></p>
<dd> Exit cscope.</dl>
<p> <code>NOTE: If the first character of the text to be searched for matches</code> <code>one of the above commands, escape it by typing a (backslash) first.</code> </p>
<p> <code>Substituting new text for old text</code> </p>
<p> After the text to be changed has been typed, cscope will prompt for the new text, and then it will display the lines containing the old text. Select the lines to be changed with these single-character commands: </p>
<dl>
<dt><code>0-9a-zA-Z</code></p>
<dd> Mark or unmark the line to be changed.</p>
<dt><code>* </code></p>
<dd> Mark or unmark all displayed lines to be changed.</p>
<dt><code>&lt;Space&gt;</code></p>
<dd> Display next set of lines.</p>
<dt><code>+</code></p>
<dd> Display next set of lines.</p>
<dt><code>&#8211; </code></p>
<dd> Display previous set of lines.</p>
<dt><code>a</code></p>
<dd> Mark or unmark all lines to be changed.</p>
<dt><code>^d</code></p>
<dd> Change the marked lines and exit.</p>
<dt><code>&lt;Esc&gt;</code></p>
<dd> Exit without changing the marked lines.</p>
<dt><code>!</code></p>
<dd> Start an interactive shell (type ^d to return to cscope).</p>
<dt><code>^l</code></p>
<dd> Redraw the screen.</p>
<dt><code>?</code></p>
<dd> Give help information about cscope commands.</p>
<dt><code>Special keys</code></p>
<dd> If your terminal has arrow keys that work in vi, you can use them to move around the input fields. The up-arrow key is useful to move to the previous input field instead of using the &lt;Tab&gt; key repeatedly. If you have &lt;CLEAR&gt;, &lt;NEXT&gt;, or &lt;PREV&gt; keys they will act as the ^l, +, and &#8211; commands, respectively.</dl>
<h3>Line-Oriented interface</h3>
<p> The -l option lets you use cscope where a screen-oriented interface would not be useful, for example, from another screen-oriented program. </p>
<p> cscope will prompt with &gt;&gt; when it is ready for an input line starting with the field number (counting from 0) immediately followed by the search pattern, for example, &#8220;lmain&#8221; finds the definition of the main function. </p>
<p> If you just want a single search, instead of the -l option use the -L and -num pattern options, and you won&#8217;t get the &gt;&gt; prompt. </p>
<p> For -l, cscope outputs the number of reference lines cscope: 2 lines </p>
<p> For each reference found, cscope outputs a line consisting of the file name, function name, line number, and line text, separated by spaces, for example, main.c main 161 main(argc, argv) </p>
<p> Note that the editor is not called to display a single reference, unlike the screen-oriented interface. </p>
<p> You can use the c command to toggle ignore/use letter case when searching. (When ignoring letter case, search for &#8220;FILE&#8221; will match &#8220;File&#8221; and &#8220;file&#8221;.) </p>
<p> You can use the r command to rebuild the database. </p>
<p> cscope will quit when it detects end-of-file, or when the first character of an input line is &#8220;^d&#8221; or &#8220;q&#8221;. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CSCOPE_EDITOR</code></p>
<dd> Overrides the EDITOR and VIEWER variables. Use this if you wish to use a different editor with cscope than that specified by your EDITOR/VIEWER variables.</p>
<dt><code>CSCOPE_LINEFLAG</code></p>
<dd> Format of the line number flag for your editor. By default, cscope invokes your editor via the equivalent of &#8220;editor +N file&#8221;, where &#8220;N&#8221; is the line number that the editor should jump to. This format is used by both emacs and vi. If your editor needs something different, specify it in this variable, with &#8220;%s&#8221; as a placeholder for the line number. Ex: if your editor needs to be invoked as &#8220;editor -#103 file&#8221; to go to line 103, set this variable to &#8220;-#%s&#8221;.</p>
<dt><code>CSCOPE_LINEFLAG_AFTER_FILE</code></p>
<dd> Set this variable to &#8220;yes&#8221; if your editor needs to be invoked with the line number option after the filename to be edited. To continue the example from CSCOPE_LINEFLAG, above: if your editor needs to see &#8220;editor file -#number&#8221;, set this environment variable. Users of most standard editors (vi, emacs) do not need to set this variable.</p>
<dt><code>EDITOR</code></p>
<dd> Preferred editor, which defaults to vi.</p>
<dt><code>HOME</code></p>
<dd> Home directory, which is automatically set at login.</p>
<dt><code>INCLUDEDIRS</code></p>
<dd> Colon-separated list of directories to search for #include files.</p>
<dt><code>SHELL</code></p>
<dd> Preferred shell, which defaults to sh.</p>
<dt><code>SOURCEDIRS</code></p>
<dd> Colon-separated list of directories to search for additional source files.</p>
<dt><code>TERM</code></p>
<dd> Terminal type, which must be a screen terminal.</p>
<dt><code>TERMINFO</code></p>
<dd> Terminal information directory full path name. If your terminal is not in the standard terminfo directory, see curses and terminfo for how to make your own terminal description.</p>
<dt><code>TMPDIR</code></p>
<dd> Temporary file directory, which defaults to /var/tmp.</p>
<dt><code>VIEWER</code></p>
<dd> Preferred file display program (such as less), which overrides EDITOR (see above).</p>
<dt><code>VPATH</code></p>
<dd> A colon-separated list of directories, each of which has the same directory structure below it. If VPATH is set, cscope searches for source files in the directories specified; if it is not set, cscope searches only in the current directory.</dl>
<h2>FILES</h2>
<dl>
<dt><code>cscope.files</code></p>
<dd> Default files containing -I, -p, -q, and -T options and the list of source files (overridden by the -i option).</p>
<dt><code>cscope.out</code></p>
<dd> Symbol cross-reference file (overridden by the -f option), which is put in the home directory if it cannot be created in the current directory.</p>
<dt>
<dd> <code>cscope.in.out</code></p>
<dt><code>cscope.po.out</code></p>
<dd> Default files containing the inverted index used for quick symbol searching (-q option). If you use the -f option to rename the cross-reference file (so it&#8217;s not cscope.out), the names for these inverted index files will be created by adding<br />
&nbsp;<wbr>.in and .po to the name you supply with -f. For example, if you indicated -f xyz, then these files would be named xyz.in and xyz.po.</p>
<dt><code>INCDIR</code></p>
<dd> Standard directory for #include files (usually /usr/include).</dl>
<h2>Notices</h2>
<p> <i>cscope</i> recognizes function definitions of the form:</p>
<dl>
<dt>fname blank ( args ) white arg_decs white {</p>
<dd>
<dt>where:</p>
<dd> <i>fname</i> is the function name</p>
<dt><i>blank</i></p>
<dd> is zero or more spaces, tabs, vtabs, form feeds or carriage returns, not including newlines</p>
<dt><i>args</i></p>
<dd> is any string that does not contain a &#8220;&quot;&#8221; or a newline</p>
<dt><i>white</i></p>
<dd> is zero or more spaces, tabs, vtabs, form feeds, carriage returns or newlines</p>
<dt><i>arg_decs</i></p>
<dd> are zero or more argument declarations (arg_decs may include comments and white space)</dl>
<p> It is not necessary for a function declaration to start at the beginning of a line. The return type may precede the function name; cscope will still recognize the declaration. Function definitions that deviate from this form will not be recognized by cscope. </p>
<p> The &#8220;Function&#8221; column of the search output for the menu option Find functions called by this function: input field will only display the first function called in the line, that is, for this function </p>
<p>&nbsp;<wbr>e()<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>return&nbsp;<wbr>(f()&nbsp;<wbr>+&nbsp;<wbr>g());<br />
&nbsp;<wbr>} </p>
<p> the display would be </p>
<p>Functions called by this function: e<br />
File Function Line<br />
a.c f 3 return(f()&nbsp;<wbr>+&nbsp;<wbr>g()); </p>
<p> Occasionally, a function definition or call may not be recognized because of braces inside #if statements. Similarly, the use of a variable may be incorrectly recognized as a definition. </p>
<p> A <code>typedef</code> name preceding a preprocessor statement will be incorrectly recognized as a global definition, for example, </p>
<p>&nbsp;<wbr>LDFILE&nbsp;<wbr>&nbsp;<wbr>*<br />
&nbsp;<wbr>#if AR16WR </p>
<p> Preprocessor statements can also prevent the recognition of a global definition, for example, </p>
<p>&nbsp;<wbr>char flag<br />
&nbsp;<wbr>#ifdef ALLOCATE_STORAGE<br />
=&nbsp;<wbr>-1<br />
&nbsp;<wbr>#endif<br />
&nbsp;<wbr>; </p>
<p> A function declaration inside a function is incorrectly recognized as a function call, for example, </p>
<p>&nbsp;<wbr>f()<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>void g();<br />
&nbsp;<wbr>} </p>
<p> is incorrectly recognized as a call to g. </p>
<p> <i>cscope</i> recognizes C++ classes by looking for the class keyword, but doesn&#8217;t recognize that a struct is also a class, so it doesn&#8217;t recognize inline member function definitions in a structure. It also doesn&#8217;t expect the class keyword in a <i>typedef</i> , so it incorrectly recognizes X as a definition in </p>
<p>&nbsp;<wbr>typedef class X&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>Y; </p>
<p> It also doesn&#8217;t recognize operator function definitions </p>
<p>&nbsp;<wbr>Bool Feature::operator==(const Feature&nbsp;<wbr>&amp;&nbsp;<wbr>other)<br />
&nbsp;<wbr>{<br />
&#8230;<br />
&nbsp;<wbr>} </p>
<p> Nor does it recognize function definitions with a function pointer argument </p>
<p>&nbsp;<wbr>ParseTable::Recognize(int startState, char&nbsp;<wbr>*pattern,<br />
int finishState, void&nbsp;<wbr>(*FinalAction)(char&nbsp;<wbr>*))<br />
&nbsp;<wbr>{<br />
&#8230;<br />
&nbsp;<wbr>} </p>
<h2>Index</h2>
