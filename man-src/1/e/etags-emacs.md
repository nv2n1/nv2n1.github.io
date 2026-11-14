---
title: "etags-emacs(1)"
name: "etags-emacs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-etags-emacs/"
description: "etags, ctags – generate tag file for Emacs, vi"
---

<p>etags, ctags &#8211; generate tag file for Emacs, vi </p>
<h2>Synopsis</h2>
<p><code>etags</code> [-aCDGIQRVh] [-i <i>file</i>] [-l <i>language</i>]<br />
 [-o <i>tagfile</i>] [-r <i>regexp</i>] [&#8211;parse-stdin=<i>file</i>]<br />
 [&#8211;append] [&#8211;no-defines] [&#8211;globals] [&#8211;no-globals] [&#8211;no-line-directive] [&#8211;include=<i>file</i>] [&#8211;ignore-indentation] [&#8211;language=<i>language</i>] [&#8211;members] [&#8211;no-members] [&#8211;output=<i>tagfile</i>] [&#8211;class-qualify] [&#8211;regex=<i>regexp</i>] [&#8211;no-regex] [&#8211;help] [&#8211;version] <i>file</i> &#8230; </p>
<p> <code>ctags</code> [-aCdgIQRVh] [-BtTuvwx] [-l <i>language</i>]<br />
 [-o <i>tagfile</i>] [-r <i>regexp</i>] [&#8211;parse-stdin=<i>file</i>]<br />
 [&#8211;append] [&#8211;backward-search] [&#8211;cxref] [&#8211;no-defines] [&#8211;globals] [&#8211;no-globals] [&#8211;no-line-directive] [&#8211;ignore-indentation] [&#8211;language=<i>language</i>] [&#8211;members] [&#8211;no-members] [&#8211;class-qualify] [&#8211;output=<i>tagfile</i>] [&#8211;regex=<i>regexp</i>] [&#8211;update] [&#8211;help] [&#8211;version] <i>file</i> &#8230;</p>
<h2>Description</h2>
<p>The <code>etags</code> program is used to create a tag table file, in a format understood by <code>emacs</code>(<code>1</code>); the <code>ctags</code> program is used to create a similar table in a format understood by <code>vi</code>(<code>1</code>). Both forms of the program understand the syntax of C, Objective C, C++, Java, Fortran, Ada, Cobol, Erlang, Forth, Go, HTML, LaTeX, Emacs Lisp/Common Lisp, Lua, Makefile, Pascal, Perl, Ruby, PHP, PostScript, Python, Prolog, Scheme and most assembler-like syntaxes. Both forms read the files specified on the command line, and write a tag table (defaults: <code>TAGS</code> for <code>etags</code>, <code>tags</code> for <code>ctags</code>) in the current working directory. Files specified with relative file names will be recorded in the tag table with file names relative to the directory where the tag table resides. If the tag table is in /dev or is the standard output, however, the file names are made relative to the working directory. Files specified with absolute file names will be recorded with absolute file names. Files generated from a source file&#8211;like a C file generated from a source Cweb file&#8211;will be recorded with the name of the source file. Compressed files are supported using gzip, bzip2, and xz. The programs recognize the language used in an input file based on its file name and contents. The <code>&#8211;language</code> switch can be used to force parsing of the file names following the switch according to the given language, overriding guesses based on filename extensions.</p>
<h2>Options</h2>
<p>Some options make sense only for the <code>vi</code> style tag files produced by ctags; <code>etags</code> does not recognize them. The programs accept unambiguous abbreviations for long option names.</p>
<dl>
<dt><code>-a, &#8211;append</code></p>
<dd>Append to existing tag file. (For <code>vi</code>-format tag files, see also <code>&#8211;update</code>.)</p>
<dt><code>-B, &#8211;backward-search</code></p>
<dd>Tag files written in the format expected by <code>vi</code> contain regular expression search instructions; the <code>-B</code> option writes them using the delimiter &quot;<code>?</code>&quot;, to search <i>backwards</i> through files. The default is to use the delimiter &quot;<code>/</code>&quot;, to search <i>forwards</i> through files. Only <code>ctags</code> accepts this option.</p>
<dt><code>&#8211;declarations</code></p>
<dd>In C and derived languages, create tags for function declarations, and create tags for extern variables unless &#8211;no-globals is used. In Lisp, create tags for (defvar foo) declarations.</p>
<dt><code>-D, &#8211;no-defines</code></p>
<dd>Do not create tag entries for C preprocessor constant definitions and enum constants. This may make the tags file much smaller if many header files are tagged.</p>
<dt><code>&#8211;globals</code></p>
<dd>Create tag entries for global variables in Perl and Makefile. This is the default in C and derived languages.</p>
<dt><code>&#8211;no-globals</code></p>
<dd>Do not tag global variables in C and derived languages. Typically this reduces the file size by one fourth.</p>
<dt><code>&#8211;no-line-directive</code></p>
<dd>Ignore <code>#line</code> preprocessor directives in C and derived languages. The default is to honor those directives, and record the tags as if the file scanned was the one named in the <code>#line</code> directive. This switch is useful when the original file named by <code>#line</code> is no longer available.</p>
<dt><code>-i</code> <i>file</i>, <code>&#8211;include=</code><i>file</i></p>
<dd>Include a note in the tag file indicating that, when searching for a tag, one should also consult the tags file <i>file</i> after checking the current file. Only <code>etags</code> accepts this option.</p>
<dt><code>-I, &#8211;ignore-indentation</code></p>
<dd>Don&#8217;t rely on indentation as much as we normally do. Currently, this means not to assume that a closing brace in the first column is the final brace of a function or structure definition in C and C++.</p>
<dt><code>-l</code> <i>language</i>, <code>&#8211;language=</code><i>language</i></p>
<dd>Parse the following files according to the given language. More than one such options may be intermixed with filenames. Use <code>&#8211;help</code> to get a list of the available languages and their default filename extensions. The &quot;auto&quot; language can be used to restore automatic detection of language based on the file name. The &quot;none&quot; language may be used to disable language parsing altogether; only regexp matching is done in this case (see the <code>&#8211;regex</code> option).</p>
<dt><code>&#8211;members</code></p>
<dd>Create tag entries for variables that are members of structure-like constructs in PHP. This is the default for C and derived languages.</p>
<dt><code>&#8211;no-members</code></p>
<dd>Do not tag member variables.</p>
<dt><code>&#8211;packages-only</code></p>
<dd>Only tag packages in Ada files.</p>
<dt><code>&#8211;parse-stdin=</code><i>file</i></p>
<dd>May be used (only once) in place of a file name on the command line. <code>etags</code> will read from standard input and mark the produced tags as belonging to the file <code>FILE</code>.</p>
<dt><code> -Q, &#8211;class-qualify</code></p>
<dd>Qualify tag names with their class name in C++, ObjC, Java, and Perl. This produces tag names of the form <i>class</i><code>::</code><i>member</i> for C++ and Perl, <i>class</i><code>(</code><i>category</i><code>)</code> for Objective C, and <i>class</i><code>.</code><i>member</i> for Java. For Objective C, this also produces class methods qualified with their arguments, as in <i>foo</i><code>:</code><i>bar</i><code>:</code><i>baz</i><code>:</code><i>more</i>.</p>
<dt><code>-o</code> <i>tagfile</i>, <code>&#8211;output=</code><i>tagfile</i></p>
<dd>Explicit name of file for tag table; for <code>etags</code> only, a file name of &#8211; means standard output; overrides default <code>TAGS</code> or <code>tags</code>. (But ignored with <code>-v</code> or <code>-x</code>.)</p>
<dt><code>-r</code> <i>regexp</i>, <code>&#8211;regex=</code><i>regexp</i></p>
<dd>Make tags based on regexp matching for the files following this option, in addition to the tags made with the standard parsing based on language. May be freely intermixed with filenames and the <code>-R</code> option. The regexps are cumulative, i.e., each such option will add to the previous ones. The regexps are of one of the forms:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[<code>{</code><i>language</i><code>}</code>]<code>/</code><i>tagregexp/</i>[<i>nameregexp</i><code>/</code>]<i>modifiers</i></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><code>@</code><i>regexfile</i></p>
<p> where <i>tagregexp</i> is used to match the tag. It should not match useless characters. If the match is such that more characters than needed are unavoidably matched by <i>tagregexp</i>, it may be useful to add a <i>nameregexp</i>, to narrow down the tag scope. <code>ctags</code> ignores regexps without a <i>nameregexp</i>. The syntax of regexps is the same as in emacs. The following character escape sequences are supported: , , \d, , , 
, , 	, , which respectively stand for the ASCII characters BEL, BS, DEL, ESC, FF, NL, CR, TAB, VT.<br />
 The <i>modifiers</i> are a sequence of 0 or more characters among <i>i</i>, which means to ignore case when matching; <i>m</i>, which means that the <i>tagregexp</i> will be matched against the whole file contents at once, rather than line by line, and the matching sequence can match multiple lines; and <i>s</i>, which implies <i>m</i> and means that the dot character in <i>tagregexp</i> matches the newline char as well.<br />
 The separator, which is <code>/</code> in the examples, can be any character different from space, tab, braces and <code>@</code>. If the separator character is needed inside the regular expression, it must be quoted by preceding it with <code>\</code>.<br />
 The optional <code>{</code><i>language</i><code>}</code> prefix means that the tag should be created only for files of language <i>language</i>, and ignored otherwise. This is particularly useful when storing many predefined regexps in a file.<br />
 In its second form, <i>regexfile</i> is the name of a file that contains a number of arguments to the <i>&#8211;regex=</i> option, one per line. Lines beginning with a space or tab are assumed to be comments, and ignored. </p>
<p> Here are some examples. All the regexps are quoted to protect them from shell interpretation. </p>
<p> Tag the DEFVAR macros in the emacs source files:<br />
 <i>&#8211;regex=&#8217;/[ 	]*DEFVAR_[A-Z_ 	(]+&quot;\([^&quot;]+\)&quot;/&#8217;</i> </p>
<p> Tag VHDL files (this example is a single long line, broken here for formatting reasons):<br />
 <i>&#8211;language=none &#8211;regex=&#8217;/[&nbsp;	]*\(ARCHITECTURE\|\ CONFIGURATION\)&nbsp;+[^&nbsp;]*&nbsp;+OF/&#8217;&nbsp;&#8211;regex=&#8217;/[&nbsp;	]*\ \(ATTRIBUTE\|ENTITY\|FUNCTION\|PACKAGE\(&nbsp;BODY\)?\ \|PROCEDURE\|PROCESS\|TYPE\)[&nbsp;	]+\([^&nbsp;	(]+\)/\3/&#8217;</i> </p>
<p> Tag TCL files (this last example shows the usage of a <i>tagregexp</i>):<br />
 <i>&#8211;lang=none &#8211;regex=&#8217;/proc[&nbsp;	]+\([^&nbsp;	]+\)/\1/&#8217;</i> </p>
<p> A regexp can be preceded by {<i>lang</i>}, thus restricting it to match lines of files of the specified language. Use <code>etags &#8211;help</code> to obtain a list of the recognized languages. This feature is particularly useful inside <code>regex files</code>. A regex file contains one regex per line. Empty lines, and those lines beginning with space or tab are ignored. Lines beginning with @ are references to regex files whose name follows the @ sign. Other lines are considered regular expressions like those following <code>&#8211;regex</code>.<br />
 For example, the command<br />
 <i>etags &#8211;regex=@regex.file *.c</i><br />
 reads the regexes contained in the file regex.file.</p>
<dt><code>-R, &#8211;no-regex</code></p>
<dd>Don&#8217;t do any more regexp matching on the following files. May be freely intermixed with filenames and the <code>&#8211;regex</code> option.</p>
<dt><code>-u, &#8211;update</code></p>
<dd>Update tag entries for <i>files</i> specified on command line, leaving tag entries for other files in place. Currently, this is implemented by deleting the existing entries for the given files and then rewriting the new entries at the end of the tags file. It is often faster to simply rebuild the entire tag file than to use this. Only <code>ctags</code> accepts this option.</p>
<dt><code>-v, &#8211;vgrind</code></p>
<dd>Instead of generating a tag file, write index (in <code>vgrind</code> format) to standard output. Only <code>ctags</code> accepts this option.</p>
<dt><code>-x, &#8211;cxref</code></p>
<dd>Instead of generating a tag file, write a cross reference (in <code>cxref</code> format) to standard output. Only <code>ctags</code> accepts this option.</p>
<dt><code>-h, -H, &#8211;help</code></p>
<dd>Print usage information. Followed by one or more &#8211;language=LANG prints detailed information about how tags are created for LANG.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the current version of the program (same as the version of the emacs <code>etags</code> is shipped with). </p>
</dl>
<h2>See Also</h2>
<p>&quot;<code>emacs</code>&quot; entry in <code>info</code>; <i>GNU Emacs Manual</i>, Richard Stallman.<br />
 <code>cxref</code>(<code>1</code>), <code>emacs</code>(<code>1</code>), <code>vgrind</code>(<code>1</code>), <code>vi</code>(<code>1</code>). </p>
<h2>Copying</h2>
<p>Copyright 1992, 1999, 2001-2019 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation.</p>
