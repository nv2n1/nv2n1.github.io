---
title: "indent(1)"
name: "indent"
section: "1"
letter: "i"
url: "/docs/linux/man/1-indent/"
description: "indent – changes the appearance of a C program by inserting or deleting whitespace."
---

<h2>NAME</h2>
<p> indent &#8211; changes the appearance of a C program by inserting or deleting whitespace.</p>
<h2>SYNOPSIS</h2>
<p> <code>indent </code> [options] [input-files] </p>
<p> <code>indent </code> [options] [single-input-file] [-o output-file] </p>
<p> <code>indent </code> &#8211;version</p>
<h2>DESCRIPTION</h2>
<p> This man page is generated from the file <i>indent.texinfo</i>. This is Edition of &quot;The <code>indent</code> Manual&quot;, for Indent Version , last updated . </p>
<p> The <code>indent</code> program can be used to make code easier to read. It can also convert from one style of writing C to another. </p>
<p> <code>indent</code> understands a substantial amount about the syntax of C, but it also attempts to cope with incomplete and misformed syntax. </p>
<p> In version 1.2 and more recent versions, the GNU style of indenting is the default.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-bad</code>, <code>&#8211;blank-lines-after-declarations</code></p>
<dd> Force blank lines after the declarations.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-bap</code>, <code>&#8211;blank-lines-after-procedures</code></p>
<dd> Force blank lines after procedure bodies.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-bbb</code>, <code>&#8211;blank-lines-before-block-comments</code></p>
<dd> Force blank lines before block comments.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-bbo</code>, <code>&#8211;break-before-boolean-operator</code></p>
<dd> Prefer to break long lines before boolean operators.<br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>.</p>
<dt><code>-bc</code>, <code>&#8211;blank-lines-after-commas</code></p>
<dd> Force newline after comma in declaration.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-bl</code>, <code>&#8211;braces-after-if-line</code></p>
<dd> Put braces on line after <code>if</code>, etc.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-blf</code>, <code>&#8211;braces-after-func-def-line</code></p>
<dd> Put braces on line following function definition line.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-bli</code><i>n</i>, <code>&#8211;brace-indent</code><i>n</i></p>
<dd> Indent braces <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-bls</code>, <code>&#8211;braces-after-struct-decl-line</code></p>
<dd> Put braces on the line after <code>struct</code> declaration lines.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-br</code>, <code>&#8211;braces-on-if-line</code></p>
<dd> Put braces on line with <code>if</code>, etc.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-brf</code>, <code>&#8211;braces-on-func-def-line</code></p>
<dd> Put braces on function definition line.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-brs</code>, <code>&#8211;braces-on-struct-decl-line</code></p>
<dd> Put braces on <code>struct</code> declaration line.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-bs</code>, <code>&#8211;Bill-Shannon</code>, <code>&#8211;blank-before-sizeof</code></p>
<dd> Put a space between <code>sizeof</code> and its argument.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-c</code><i>n</i>, <code>&#8211;comment-indentation</code><i>n</i></p>
<dd> Put comments to the right of code in column <i>n</i>.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-cbi</code><i>n</i>, <code>&#8211;case-brace-indentation</code><i>n</i></p>
<dd> Indent braces after a case label N spaces.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-cd</code><i>n</i>, <code>&#8211;declaration-comment-column</code><i>n</i></p>
<dd> Put comments to the right of the declarations in column <i>n</i>.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-cdb</code>, <code>&#8211;comment-delimiters-on-blank-lines</code></p>
<dd> Put comment delimiters on blank lines.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-cdw</code>, <code>&#8211;cuddle-do-while</code></p>
<dd> Cuddle while of <code>do {} while;</code> and preceding &#8216;}&#8217;.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-ce</code>, <code>&#8211;cuddle-else</code></p>
<dd> Cuddle else and preceding &#8216;}&#8217;.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-ci</code><i>n</i>, <code>&#8211;continuation-indentation</code><i>n</i></p>
<dd> Continuation indent of <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-cli</code><i>n</i>, <code>&#8211;case-indentation</code><i>n</i></p>
<dd> Case label indent of <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-cp</code><i>n</i>, <code>&#8211;else-endif-column</code><i>n</i></p>
<dd> Put comments to the right of <code>#else</code> and <code> #endif</code> statements in column <i>n</i>.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-cs</code>, <code>&#8211;space-after-cast</code></p>
<dd> Put a space after a cast operator.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-d</code><i>n</i>, <code>&#8211;line-comments-indentation</code><i>n</i></p>
<dd> Set indentation of comments not to the right of code to <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-bfda</code>, <code>&#8211;break-function-decl-args</code></p>
<dd> Break the line before all arguments in a declaration.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-bfde</code>, <code>&#8211;break-function-decl-args-end</code></p>
<dd> Break the line after the last argument in a declaration.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-dj</code><i>n</i>, <code>&#8211;left-justify-declarations</code></p>
<dd> If -cd 0 is used then comments after declarations are left justified behind the declaration.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-di</code><i>n</i>, <code>&#8211;declaration-indentation</code><i>n</i></p>
<dd> Put variables in column <i>n</i>.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-fc1</code>, <code>&#8211;format-first-column-comments</code></p>
<dd> Format comments in the first column.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-fca</code>, <code>&#8211;format-all-comments</code></p>
<dd> Do not disable all formatting of comments.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-gnu</code>, <code>&#8211;gnu-style</code></p>
<dd> Use GNU coding style. This is the default.<br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>.</p>
<dt><code>-hnl</code>, <code>&#8211;honour-newlines</code></p>
<dd> Prefer to break long lines at the position of newlines in the input.<br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>.</p>
<dt><code>-i</code><i>n</i>, <code>&#8211;indent-level</code><i>n</i></p>
<dd> Set indentation level to <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-il</code><i>n</i>, <code>&#8211;indent-label</code><i>n</i></p>
<dd> Set offset for labels to column <i>n</i>.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-ip</code><i>n</i>, <code>&#8211;parameter-indentation</code><i>n</i></p>
<dd> Indent parameter types in old-style function definitions by <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-kr</code>, <code>&#8211;k-and-r-style</code></p>
<dd> Use Kernighan &amp; Ritchie coding style.<br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>.</p>
<dt><code>-l</code><i>n</i>, <code>&#8211;line-length</code><i>n</i></p>
<dd> Set maximum line length for non-comment lines to <i>n</i>.<br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>.</p>
<dt><code>-lc</code><i>n</i>, <code>&#8211;comment-line-length</code><i>n</i></p>
<dd> Set maximum line length for comment formatting to <i>n</i>.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-linux</code>, <code>&#8211;linux-style</code></p>
<dd> Use Linux coding style.<br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>.</p>
<dt><code>-lp</code>, <code>&#8211;continue-at-parentheses</code></p>
<dd> Line up continued lines at parentheses.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-lps</code>, <code>&#8211;leave-preprocessor-space</code></p>
<dd> Leave space between &#8216;#&#8217; and preprocessor directive.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-nlps</code>, <code>&#8211;remove-preprocessor-space</code></p>
<dd> Remove space between &#8216;#&#8217; and preprocessor directive.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-nbad</code>, <code>&#8211;no-blank-lines-after-declarations</code></p>
<dd> Do not force blank lines after declarations.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-nbap</code>, <code>&#8211;no-blank-lines-after-procedures</code></p>
<dd> Do not force blank lines after procedure bodies.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-nbbo</code>, <code>&#8211;break-after-boolean-operator</code></p>
<dd> Do not prefer to break long lines before boolean operators.<br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>.</p>
<dt><code>-nbc</code>, <code>&#8211;no-blank-lines-after-commas</code></p>
<dd> Do not force newlines after commas in declarations.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-nbfda</code>, <code>&#8211;dont-break-function-decl-args</code></p>
<dd> Don&#8217;t put each argument in a function declaration on a separate line.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-ncdb</code>, <code>&#8211;no-comment-delimiters-on-blank-lines</code></p>
<dd> Do not put comment delimiters on blank lines.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-ncdw</code>, <code>&#8211;dont-cuddle-do-while</code></p>
<dd> Do not cuddle <code>}</code> and the <code>while</code> of a <code>do {} while;</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-nce</code>, <code>&#8211;dont-cuddle-else</code></p>
<dd> Do not cuddle <code>}</code> and <code>else</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-ncs</code>, <code>&#8211;no-space-after-casts</code></p>
<dd> Do not put a space after cast operators.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-ndj</code><i>n</i>, <code>&#8211;dont-left-justify-declarations</code></p>
<dd> Comments after declarations are treated the same as comments after other statements.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-nfc1</code>, <code>&#8211;dont-format-first-column-comments</code></p>
<dd> Do not format comments in the first column as normal.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-nfca</code>, <code>&#8211;dont-format-comments</code></p>
<dd> Do not format any comments.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-nhnl</code>, <code>&#8211;ignore-newlines</code></p>
<dd> Do not prefer to break long lines at the position of newlines in the input.<br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>.</p>
<dt><code>-nip</code>, <code>&#8211;no-parameter-indentation</code></p>
<dd> Zero width indentation for parameters.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-nlp</code>, <code>&#8211;dont-line-up-parentheses</code></p>
<dd> Do not line up parentheses.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-npcs</code>, <code>&#8211;no-space-after-function-call-names</code></p>
<dd> Do not put space after the function in function calls.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-nprs</code>, <code>&#8211;no-space-after-parentheses</code></p>
<dd> Do not put a space after every &#8216;(&#8216; and before every &#8216;)&#8217;.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-npsl</code>, <code>&#8211;dont-break-procedure-type</code></p>
<dd> Put the type of a procedure on the same line as its name.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-nsaf</code>, <code>&#8211;no-space-after-for</code></p>
<dd> Do not put a space after every <code>for</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-nsai</code>, <code>&#8211;no-space-after-if</code></p>
<dd> Do not put a space after every <code>if</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-nsaw</code>, <code>&#8211;no-space-after-while</code></p>
<dd> Do not put a space after every <code>while</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-nsc</code>, <code>&#8211;dont-star-comments</code></p>
<dd> Do not put the &#8216;*&#8217; character at the left of comments.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-nsob</code>, <code>&#8211;leave-optional-blank-lines</code></p>
<dd> Do not swallow optional blank lines.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-nss</code>, <code>&#8211;dont-space-special-semicolon</code></p>
<dd> Do not force a space before the semicolon after certain statements. Disables &#8216;-ss&#8217;.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-nut</code>, <code>&#8211;no-tabs</code></p>
<dd> Use spaces instead of tabs.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-nv</code>, <code>&#8211;no-verbosity</code></p>
<dd> Disable verbose mode.<br />
 See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>.</p>
<dt><code>-orig</code>, <code>&#8211;original</code></p>
<dd> Use the original Berkeley coding style.<br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>.</p>
<dt><code>-npro</code>, <code>&#8211;ignore-profile</code></p>
<dd> Do not read &#8216;.indent.pro&#8217; files.<br />
 See <code>&nbsp;<wbr>INVOKING INDENT</code>.</p>
<dt><code>-pcs</code>, <code>&#8211;space-after-procedure-calls</code></p>
<dd> Insert a space between the name of the procedure being called and the &#8216;(&#8216;.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-pi</code><i>n</i>, <code>&#8211;paren-indentation</code><i>n</i></p>
<dd> Specify the extra indentation per open parentheses &#8216;(&#8216; when a statement is broken.See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-pmt</code>, <code>&#8211;preserve-mtime</code></p>
<dd> Preserve access and modification times on output files.See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>.</p>
<dt><code>-ppi</code><i>n</i>, <code>&#8211;preprocessor-indentation</code><i>n</i></p>
<dd> Specify the indentation for preprocessor conditional statements.See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-prs</code>, <code>&#8211;space-after-parentheses</code></p>
<dd> Put a space after every &#8216;(&#8216; and before every &#8216;)&#8217;.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-psl</code>, <code>&#8211;procnames-start-lines</code></p>
<dd> Put the type of a procedure on the line before its name.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-saf</code>, <code>&#8211;space-after-for</code></p>
<dd> Put a space after each <code>for</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-sai</code>, <code>&#8211;space-after-if</code></p>
<dd> Put a space after each <code>if</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-saw</code>, <code>&#8211;space-after-while</code></p>
<dd> Put a space after each <code>while</code>.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-sbi</code><i>n</i>, <code>&#8211;struct-brace-indentation</code><i>n</i></p>
<dd> Indent braces of a struct, union or enum N spaces.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-sc</code>, <code>&#8211;start-left-side-of-comments</code></p>
<dd> Put the &#8216;*&#8217; character at the left of comments.<br />
 See <code>&nbsp;<wbr>COMMENTS</code>.</p>
<dt><code>-sob</code>, <code>&#8211;swallow-optional-blank-lines</code></p>
<dd> Swallow optional blank lines.<br />
 See <code>&nbsp;<wbr>BLANK LINES</code>.</p>
<dt><code>-ss</code>, <code>&#8211;space-special-semicolon</code></p>
<dd> On one-line <code>for</code> and <code>while</code> statements, force a blank before the semicolon.<br />
 See <code>&nbsp;<wbr>STATEMENTS</code>.</p>
<dt><code>-st</code>, <code>&#8211;standard-output</code></p>
<dd> Write to standard output.<br />
 See <code>&nbsp;<wbr>INVOKING INDENT</code>.</p>
<dt><code>-T</code></p>
<dd> Tell <code>indent</code> the name of typenames.<br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>.</p>
<dt><code>-ts</code><i>n</i>, <code>&#8211;tab-size</code><i>n</i></p>
<dd> Set tab size to <i>n</i> spaces.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-ut</code>, <code>&#8211;use-tabs</code></p>
<dd> Use tabs. This is the default.<br />
 See <code>&nbsp;<wbr>INDENTATION</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Enable verbose mode.<br />
 See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>.</p>
<dt><code>-version</code></p>
<dd> Output the version number of <code>indent</code>.<br />
 See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>. </p>
</dl>
<h2>INVOKING INDENT</h2>
<p> As of version 1.3, the format of the <code>indent</code> command is: </p>
<pre><code>
indent[options][input - files] indent[options][single - input - file][-o output - file]
</code></pre>
<p> This format is different from earlier versions and other versions of <code>indent</code>. </p>
<p> In the first form, one or more input files are specified. <code>indent</code> makes a backup copy of each file, and the original file is replaced with its indented version. See <code>BACKUP FILES</code>, for an explanation of how backups are made. </p>
<p> In the second form, only one input file is specified. In this case, or when the standard input is used, you may specify an output file after the &#8216;-o&#8217; option. </p>
<p> To cause <code>indent</code> to write to standard output, use the &#8216;-st&#8217; option. This is only allowed when there is only one input file, or when the standard input is used. </p>
<p> If no input files are named, the standard input is read for input. Also, if a filename named &#8216;-&#8216; is specified, then the standard input is read. </p>
<p> As an example, each of the following commands will input the program &#8216;slithy_toves.c&#8217; and write its indented text to &#8216;slithy_toves.out&#8217;: </p>
<pre>
indent slithy_toves.c -o slithy_toves.out
indent -st slithy_toves.c &gt; slithy_toves.out
cat slithy_toves.c | indent -o slithy_toves.out
</pre>
<p> Most other options to <code>indent</code> control how programs are formatted. As of version 1.2, <code>indent</code> also recognizes a long name for each option name. Long options are prefixed by either &#8216;&#8211;&#8216; or &#8216;+&#8217;. [ &#8216;+&#8217; is being superseded by &#8216;&#8211;&#8216; to maintain consistency with the POSIX standard.]<br />
&nbsp;<wbr>In most of this document, the traditional, short names are used for the sake of brevity. See <code>OPTION SUMMARY</code>, for a list of options, including both long and short names. </p>
<p> Here is another example: </p>
<pre>
indent -br test/metabolism.c -l85
</pre>
<p> This will indent the program &#8216;test/metabolism.c&#8217; using the &#8216;-br&#8217; and &#8216;-l85&#8217; options, write the output back to &#8216;test/metabolism.c&#8217;, and write the original contents of &#8216;test/metabolism.c&#8217; to a backup file in the directory &#8216;test&#8217;. </p>
<p> Equivalent invocations using long option names for this example would be: </p>
<p>indent&#8211; braces &#8211; on &#8211; if &#8211; line&#8211; line &#8211; length185 test / metabolism.c indent + braces &#8211; on &#8211; if &#8211; line + line &#8211; length185 test / metabolism.c</p>
<p> If you find that you often use <code>indent</code> with the same options, you may put those options into a file named &#8216;.indent.pro&#8217;. <code>indent</code> will look for a profile file in three places. First it will check the environment variable <code>INDENT_PROFILE</code>. If that exists its value is expected to name the file that is to be used. If the environment variable does not exist, indent looks for &#8216;.indent.pro&#8217; in the current directory<br />
&nbsp;<wbr>and use that if found.&nbsp;<wbr>&nbsp;<wbr>Finally&nbsp;<wbr><code>indent</code>&nbsp;<wbr>will search your home directory for &#8216;.indent.pro&#8217; and use that file if it is found. This behaviour is different from that of other versions of <code>indent</code>, which load both files if they both exist. </p>
<p> The format of &#8216;.indent.pro&#8217; is simply a list of options, just as they would appear on the command line, separated by white space (tabs, spaces, and newlines). Options in &#8216;.indent.pro&#8217; may be surrounded by C or C++ comments, in which case they are ignored. </p>
<p> Command line switches are handled <i>after</i> processing &#8216; .indent.pro&#8217;. Options specified later override arguments specified earlier, with one exception: Explicitly specified options always override background options (See <code>COMMON STYLES</code>). You can prevent <code>indent</code> from reading an &#8216;.indent.pro&#8217; file by specifying the &#8216;-npro&#8217; option. </p>
<h2>BACKUP FILES</h2>
<p> As of version 1.3, GNU <code>indent</code> makes GNU-style backup files, the same way GNU Emacs does. This means that either <i>simple</i> or <i>numbered</i> backup filenames may be made. </p>
<p> Simple backup file names are generated by appending a suffix to the original file name. The default for this suffix is the one-character string &#8216;~&#8217; (tilde). Thus, the backup file for &#8216;python.c&#8217; would be &#8216;python.c~&#8217;. </p>
<p> Instead of the default, you may specify any string as a suffix by setting the environment variable <code>SIMPLE_BACKUP_SUFFIX</code> to your preferred suffix. </p>
<p> Numbered backup versions of a file &#8216;momeraths.c&#8217; look like &#8216;momeraths.c.~23~&#8217;, where 23 is the version of this particular backup. When making a numbered backup of the file &#8216;src/momeraths.c&#8217;, the backup file will be named &#8216;src/momeraths.c.~<i>V</i>~&#8217;, where <i>V</i> is one greater than the highest version currently existing in the directory &#8216;src&#8217;. The environment variable <code>VERSION_WIDTH</code> controls the number of digits, using left zero padding when necessary. For instance, setting this variable to &quot;2&quot; will lead to the backup file being named &#8216;momeraths.c.~04~&#8217;. </p>
<p> The type of backup file made is controlled by the value of the environment variable <code>VERSION_CONTROL</code>. If it is the string &#8216;simple&#8217;, then only simple backups will be made. If its value is the string &#8216;numbered&#8217;, then numbered backups will be made. If its value is &#8216;numbered-existing&#8217;, then numbered backups will be made if there <i>already exist</i> numbered backups for the file being indented; otherwise, a simple backup is made. If <code>VERSION_CONTROL</code> is not set, then <code>indent</code> assumes the behaviour of &#8216;numbered-existing&#8217;. </p>
<p> Other versions of <code>indent</code> use the suffix &#8216;.BAK&#8217; in naming backup files. This behaviour can be emulated by setting <code>SIMPLE_BACKUP_SUFFIX</code> to &#8216;.BAK&#8217;. </p>
<p> Note also that other versions of <code>indent</code> make backups in the current directory, rather than in the directory of the source file as GNU <code>indent</code> now does. </p>
<h2>COMMON STYLES</h2>
<p> There are several common styles of C code, including the GNU style, the Kernighan &amp; Ritchie style, and the original Berkeley style. A style may be selected with a single <i>background</i> option, which specifies a set of values for all other options. However, explicitly specified options always override options implied by a background option. </p>
<p> As of version 1.2, the default style of GNU <code>indent</code> is the GNU style. Thus, it is no longer necessary to specify the option &#8216;-gnu&#8217; to obtain this format, although doing so will not cause an error. Option settings which correspond to the GNU style are: </p>
<pre>
-nbad -bap -nbc -bbo -bl -bli2 -bls -ncdb -nce -cp1 -cs -di2
-ndj -nfc1 -nfca -hnl -i2 -ip5 -lp -pcs -nprs -psl -saf -sai
-saw -nsc -nsob
</pre>
<p> The GNU coding style is that preferred by the GNU project. It is the style that the GNU Emacs C mode encourages and which is used in the C portions of GNU Emacs. (People interested in writing programs for Project GNU should get a copy of &quot;The GNU Coding Standards&quot;, which also covers semantic and portability issues such as memory usage, the size of integers, etc.) </p>
<p> The Kernighan &amp; Ritchie style is used throughout their well-known book &quot;The C Programming Language&quot;. It is enabled with the &#8216;-kr&#8217; option. The Kernighan &amp; Ritchie style corresponds to the following set of options: </p>
<pre>
-nbad -bap -bbo -nbc -br -brs -c33 -cd33 -ncdb -ce -ci4 -cli0
-cp33 -cs -d0 -di1 -nfc1 -nfca -hnl -i4 -ip0 -l75 -lp -npcs
-nprs -npsl -saf -sai -saw -nsc -nsob -nss
</pre>
<p> Kernighan &amp; Ritchie style does not put comments to the right of code in the same column at all times (nor does it use only one space to the right of the code), so for this style <code>indent</code> has arbitrarily chosen column 33. </p>
<p> The style of the original Berkeley <code>indent</code> may be obtained by specifying &#8216;-orig&#8217; (or by specifying &#8216;&#8211;original&#8217;, using the long option name). This style is equivalent to the following settings: </p>
<pre>
-nbad -nbap -bbo -bc -br -brs -c33 -cd33 -cdb -ce -ci4 -cli0
-cp33 -di16 -fc1 -fca -hnl -i4 -ip4 -l75 -lp -npcs -nprs -psl
-saf -sai -saw -sc -nsob -nss -ts8
</pre>
<p> The Linux style is used in the linux kernel code and drivers. Code generally has to follow the Linux coding style to be accepted. This style is equivalent to the following settings: </p>
<pre>
-nbad -bap -nbc -bbo -hnl -br -brs -c33 -cd33 -ncdb -ce -ci4 
-cli0 -d0 -di1 -nfc1 -i8 -ip0 -l80 -lp -npcs -nprs -npsl -sai
-saf -saw -ncs -nsc -sob -nfca -cp33 -ss -ts8 -il1
</pre>
<h2>BLANK LINES</h2>
<p> Various programming styles use blank lines in different places. <code>indent</code> has a number of options to insert or delete blank lines in specific places. </p>
<p> The &#8216;-bad&#8217; option causes <code>indent</code> to force a blank line after every block of declarations. The &#8216;-nbad&#8217; option causes <code>indent</code> not to force such blank lines. </p>
<p> The &#8216;-bap&#8217; option forces a blank line after every procedure body. The &#8216;-nbap&#8217; option forces no such blank line. </p>
<p> The &#8216;-bbb&#8217; option forces a blank line before every boxed comment (See <code>COMMENTS</code>.) The &#8216;-nbbb&#8217; option does not force such blank lines. </p>
<p> The &#8216;-sob&#8217; option causes <code>indent</code> to swallow optional blank lines (that is, any optional blank lines present in the input will be removed from the output). If the &#8216;-nsob&#8217; is specified, any blank lines present in the input file will be copied to the output file. </p>
<h2>&#8211;blank-lines-after-declarations</h2>
<p> The &#8216;-bad&#8217; option forces a blank line after every block of declarations. The &#8216;-nbad&#8217; option does not add any such blank lines. </p>
<p> For example, given the input<br />
char *foo;<br />
char *bar;<br />
/* This separates blocks of declarations.  */<br />
int baz;</p>
<p> <code>indent -bad</code> produces </p>
<p>char *foo;<br />
char *bar;<br />
/* This separates blocks of declarations.  */<br />
int baz;</p>
<p> and <code>indent -nbad</code> produces </p>
<p>char *foo;<br />
char *bar;<br />
/* This separates blocks of declarations.  */<br />
int baz;</p>
<h2>&#8211;blank-lines-after-procedures</h2>
<p> The &#8216;-bap&#8217; option forces a blank line after every procedure body. </p>
<p> For example, given the input </p>
<p>int foo()<br />
{<br />
    puts(&#8220;Hi&#8221;);<br />
}<br />
/* The procedure bar is even less interesting.  */<br />
char *<br />
bar()<br />
{<br />
    puts(&#8220;Hello&#8221;);<br />
}</p>
<p> <code>indent -bap</code> produces </p>
<p>int foo()<br />
{<br />
    puts(&#8220;Hi&#8221;);<br />
}<br />
/* The procedure bar is even less interesting.  */<br />
char *<br />
bar()<br />
{<br />
    puts(&#8220;Hello&#8221;);<br />
}</p>
<p> and <code>indent -nbap</code> produces </p>
<p>int foo()<br />
{<br />
    puts(&#8220;Hi&#8221;);<br />
}<br />
/* The procedure bar is even less interesting.  */<br />
char *<br />
bar()<br />
{<br />
    puts(&#8220;Hello&#8221;);<br />
}</p>
<p> No blank line will be added after the procedure <code>foo</code>. </p>
<h2>COMMENTS</h2>
<p> <code>indent</code> formats both C and C++ comments. C comments are begun with &#8216;/*&#8217;, terminated with &#8216;*/&#8217; and may contain newline characters. C++ comments begin with the delimiter &#8216;//&#8217; and end at the newline. </p>
<p> <code>indent</code> handles comments differently depending upon their context. <code>indent</code> attempts to distinguish between comments which follow statements, comments which follow declarations, comments following preprocessor directives, and comments which are not preceded by code of any sort, i.e., they begin the text of the line (although not necessarily in column 1). </p>
<p> <code>indent</code> further distinguishes between comments found outside of procedures and aggregates, and those found within them. In particular, comments beginning a line found within a procedure will be indented to the column at which code is currently indented. The exception to this is a comment beginning in the leftmost column; such a comment is output at that column. </p>
<p> <code>indent</code> attempts to leave <i>boxed comments</i> unmodified. The general idea of such a comment is that it is enclosed in a rectangle or &#8221;box&#8221; of stars or dashes to visually set it apart. More precisely, boxed comments are defined as those in which the initial &#8216;/*&#8217; is followed immediately by the character &#8216;*&#8217;, &#8216;=&#8217;, &#8216;_&#8217;, or &#8216;-&#8216;, or those in which the beginning comment delimiter (&#8216;/*&#8217;) is on a line by itself, and the following line begins with a &#8216;*&#8217; in the same column as the star of the opening delimiter. </p>
<p> Examples of boxed comments are: </p>
<pre>
/**********************
 * Comment in a box!! *
 **********************/
       /*
        * A different kind of scent,
        * for a different kind of comment.
        */
</pre>
<p> <code>indent</code> attempts to leave boxed comments exactly as they are found in the source file. Thus the indentation of the comment is unchanged, and its length is not checked in any way. The only alteration made is that an embedded tab character may be converted into the appropriate number of spaces. </p>
<p> If the &#8216;-bbb&#8217; option is specified, all such boxed comments will be preceded by a blank line, unless such a comment is preceded by code. </p>
<p> Comments which are not boxed comments may be formatted, which means that the line is broken to fit within a right margin and left-filled with whitespace. Single newlines are equivalent to a space, but blank lines (two or more newlines in a row) are taken to mean a paragraph break. Formatting of comments which begin after the first column is enabled with the &#8216;-fca&#8217; option. To format those beginning in column one, specify &#8216;-fc1&#8217;. Such formatting is disabled by default. </p>
<p> The right margin for formatting defaults to 78, but may be changed with the &#8216;-lc&#8217; option. If the margin specified does not allow the comment to be printed, the margin will be automatically extended for the duration of that comment. The margin is not respected if the comment is not being formatted. </p>
<p> If the comment begins a line (i.e., there is no program text to its left), it will be indented to the column it was found in unless the comment is within a block of code. In that case, such a comment will be aligned with the indented code of that block (unless the comment began in the first column). This alignment may be affected by the &#8216;-d&#8217; option, which specifies an amount by which such comments are moved to the <i>left</i>, or unindented. For example, &#8216;-d2&#8217; places comments two spaces to the left of code. By default, comments are aligned with code, unless they begin in the first column, in which case they are left there by default &#8212; to get them aligned with the code, specify &#8216;-fc1&#8217;. </p>
<p> Comments to the right of code will appear by default in column 33. This may be changed with one of three options. &#8216;-c&#8217; will specify the column for comments following code, &#8216;-cd&#8217; specifies the column for comments following declarations, and &#8216;-cp&#8217; specifies the column for comments following preprocessor directives <code>#else</code> and <code>#endif</code>. &#8216;-dj&#8217; together with &#8216;-cd0&#8217; can be used to suppress alignment of comments to the right of declarations, causing the comment to follow one tabstop from the end of the declaration. Normally &#8216;-cd0&#8217; causes &#8216;-c&#8217; to become effective. </p>
<p> If the code to the left of the comment exceeds the beginning column, the comment column will be extended to the next tabstop column past the end of the code, or in the case of preprocessor directives, to one space past the end of the directive. This extension lasts only for the output of that particular comment. </p>
<p> The &#8216;-cdb&#8217; option places the comment delimiters on blank lines. Thus, a single line comment like <code>/* Loving hug */</code> can be transformed into: </p>
<pre>
/*
   Loving hug
 */
</pre>
<p> Stars can be placed at the beginning of multi-line comments with the &#8216;-sc&#8217; option. Thus, the single-line comment above can be transformed (with &#8216;-cdb -sc&#8217;) into: </p>
<pre>
/*
 * Loving hug
 */
</pre>
<h2>STATEMENTS</h2>
<p> The &#8216;-br&#8217; or &#8216;-bl&#8217; option specifies how to format braces. </p>
<p> The &#8216;-br&#8217; option formats statement braces like this: </p>
<p>if (x &gt; 0) {<br />
    x&#8211;;<br />
}</p>
<p> The &#8216;-bl&#8217; option formats them like this: </p>
<p>if (x &gt; 0) {<br />
    x&#8211;;<br />
}</p>
<p> If you use the &#8216;-bl&#8217; option, you may also want to specify the &#8216;-bli&#8217; option. This option specifies the number of spaces by which braces are indented. &#8216;-bli2&#8217;, the default, gives the result shown above. &#8216;-bli0&#8217; results in the following: </p>
<p>if (x &gt; 0) {<br />
    x&#8211;;<br />
}</p>
<p> If you are using the &#8216;-br&#8217; option, you probably want to also use the &#8216;-ce&#8217; option. This causes the <code>else</code> in an if-then-else construct to cuddle up to the immediately preceding &#8216;}&#8217;. For example, with &#8216;-br -ce&#8217; you get the following: </p>
<p>if (x &gt; 0) {<br />
    x&#8211;;<br />
} else {<br />
    fprintf(stderr, &#8220;&#8230;something wrong?
&#8221;);<br />
}</p>
<p> With &#8216;-br -nce&#8217; that code would appear as </p>
<p>if (x &gt; 0) {<br />
    x&#8211;;<br />
} else {<br />
    fprintf(stderr, &#8220;&#8230;something wrong?
&#8221;);<br />
}</p>
<p> This causes the <code>while</code> in a do-while loop to cuddle up to the immediately preceding &#8216;}&#8217;. For example, with &#8216;-cdw&#8217; you get the following: </p>
<p>do {<br />
    x&#8211;;<br />
} while (x);</p>
<p> With &#8216;-ncdw&#8217; that code would appear as </p>
<p>do {<br />
    x&#8211;;<br />
} while (x);</p>
<p> The &#8216;-cli&#8217; option specifies the number of spaces that case labels should be indented to the right of the containing <code>switch</code> statement. </p>
<p> The default gives code like: </p>
<p>switch (i) {<br />
case 0:<br />
    break;<br />
case 1: {<br />
    ++i;<br />
}<br />
default:<br />
    break;<br />
}</p>
<p> Using the &#8216;-cli2&#8217; that would become: </p>
<p>switch (i) {<br />
case 0:<br />
    break;<br />
case 1: {<br />
    ++i;<br />
}<br />
default:<br />
    break;<br />
}</p>
<p> The indentation of the braces below a case statement can be controlled with the &#8216;-cbi<i>n</i>&#8216; option. For example, using &#8216;-cli2 -cbi0&#8217; results in: </p>
<p>switch (i) {<br />
case 0:<br />
    break;<br />
case 1: {<br />
    ++i;<br />
}<br />
default:<br />
    break;<br />
}</p>
<p> If a semicolon is on the same line as a <code>for</code> or <code>while</code> statement, the &#8216;-ss&#8217; option will cause a space to be placed before the semicolon. This emphasizes the semicolon, making it clear that the body of the <code>for</code> or <code>while</code> statement is an empty statement. &#8216;-nss&#8217; disables this feature. </p>
<p> The &#8216;-pcs&#8217; option causes a space to be placed between the name of the procedure being called and the &#8216;(&#8216; (for example, <code>puts&nbsp;<wbr>(&quot;Hi&quot;);</code>. The &#8216;-npcs&#8217; option would give <code>puts(&quot;Hi&quot;);</code>). </p>
<p> If the &#8216;-cs&#8217; option is specified, <code>indent</code> puts a space between a cast operator and the object to be cast. The &#8216;-ncs&#8217; ensures that there is no space between the cast operator and the object. Remember that <code>indent</code> only knows about the standard C data types and so cannot recognise user-defined types in casts. Thus <code>(mytype)thing</code> is not treated as a cast. </p>
<p> The &#8216;-bs&#8217; option ensures that there is a space between the keyword <code>sizeof</code> and its argument. In some versions, this is known as the &#8216;Bill_Shannon&#8217; option. </p>
<p> The &#8216;-saf&#8217; option forces a space between a <code>for</code> and the following parenthesis. This is the default. </p>
<p> The &#8216;-sai&#8217; option forces a space between a <code>if</code> and the following parenthesis. This is the default. </p>
<p> The &#8216;-saw&#8217; option forces a space between a <code>while</code> and the following parenthesis. This is the default. </p>
<p> The &#8216;-prs&#8217; option causes all parentheses to be separated with a space from whatever is between them. For example, using &#8216;-prs&#8217; results in code like: </p>
<p>while ((e_code &#8211; s_code) &lt; (dec_ind &#8211; 1)) {<br />
    set_buf_break(bb_dec_ind);<br />
    *e_code++ = &#8216; &#8216;;<br />
}</p>
<h2>DECLARATIONS</h2>
<p> By default <code>indent</code> will line up identifiers, in the column specified by the &#8216;-di&#8217; option. For example, &#8216;-di16&#8217; makes things look like: </p>
<p>int foo;<br />
char *bar;</p>
<p> Using a small value (such as one or two) for the &#8216;-di&#8217; option can be used to cause the identifiers to be placed in the first available position; for example: </p>
<p>int foo;<br />
char *bar;</p>
<p> The value given to the &#8216;-di&#8217; option will still affect variables which are put on separate lines from their types, for example &#8216;-di2&#8217; will lead to: </p>
<pre>
int
  foo;
</pre>
<p> If the &#8216;-bc&#8217; option is specified, a newline is forced after each comma in a declaration. For example, </p>
<pre>
int a,
  b,
  c;
</pre>
<p> With the &#8216;-nbc&#8217; option this would look like </p>
<pre>
int a, b, c;
</pre>
<p> The &#8216;-bfda&#8217; option causes a newline to be forced after the comma separating the arguments of a function declaration. The arguments will appear at one indention level deeper than the function declaration. This is particularly helpful for functions with long argument lists. The option &#8216;-bfde&#8217; causes a newline to be forced before the closing bracket of the function declaration. For both options the &#8216;n&#8217; setting is the default: -nbdfa and -nbdfe. </p>
<p> For example, </p>
<p>void foo(int arg1, char arg2, int *arg3, long arg4, char arg5);<br />
 With the &#8216;-bfda&#8217; option this would look like </p>
<p>void foo(<br />
    int arg1,<br />
    char arg2,<br />
    int *arg3,<br />
    long arg4,<br />
    char arg5);</p>
<p> With, in addition, the &#8216;-bfde&#8217; option this would look like </p>
<p>void foo(<br />
    int arg1,<br />
    char arg2,<br />
    int *arg3,<br />
    long arg4,<br />
    char arg5);</p>
<p> The &#8216;-psl&#8217; option causes the type of a procedure being defined to be placed on the line before the name of the procedure. This style is required for the <code>etags</code> program to work correctly, as well as some of the <code>c-mode</code> functions of Emacs. </p>
<p> You must use the &#8216;-T&#8217; option to tell <code>indent</code> the name of all the typenames in your program that are defined by <code>typedef</code>. &#8216;-T&#8217; can be specified more than once, and all names specified are used. For example, if your program contains </p>
<p>typedef unsigned long CODE_ADDR;<br />
typedef enum { red,<br />
               blue,<br />
               green } COLOR;</p>
<p> you would use the options &#8216;-T CODE_ADDR -T COLOR&#8217;. </p>
<p> The &#8216;-brs&#8217; or &#8216;-bls&#8217; option specifies how to format braces in struct declarations. The &#8216;-brs&#8217; option formats braces like this: </p>
<p>struct foo {<br />
    int x;<br />
};</p>
<p> The &#8216;-bls&#8217; option formats them like this: </p>
<p>struct foo {<br />
    int x;<br />
};</p>
<p> Similarly to the structure brace &#8216;-brs&#8217; and &#8216;-bls&#8217; options,<br />
&nbsp;<wbr>the function brace options&nbsp;<wbr>&#8216;-brf&#8217;&nbsp;<wbr>or&nbsp;<wbr>&#8216;-blf&#8217;&nbsp;<wbr>specify how to format the braces in function definitions. The &#8216;-brf&#8217; option formats braces like this: </p>
<p>int one(void)<br />
{<br />
    return 1;<br />
};</p>
<p> The &#8216;-blf&#8217; option formats them like this: </p>
<p>int one(void)<br />
{<br />
    return 1;<br />
};</p>
<h2>INDENTATION</h2>
<p> One issue in the formatting of code is how far each line should be indented from the left margin. When the beginning of a statement such as <code>if</code> or <code>for</code> is encountered, the indentation level is increased by the value specified by the &#8216;-i&#8217; option. For example, use &#8216;-i8&#8217; to specify an eight character indentation for each level. When a statement is broken across two lines, the second line is indented by a number of additional spaces specified by the &#8216;-ci&#8217; option. &#8216;-ci&#8217; defaults to 0. However, if the &#8216;-lp&#8217; option is specified, and a line has a left parenthesis which is not closed on that line, then continuation lines will be lined up to start at the character position just after the left parenthesis. This processing also applies to &#8216;[&#8216; and applies to &#8216;{&#8216; when it occurs in initialization lists. For example, a piece of continued code might look like this with &#8216;-nlp -ci3&#8217; in effect: </p>
<pre>
  p1 = first_procedure (second_procedure (p2, p3),
     third_procedure (p4, p5));
</pre>
<p> With &#8216;-lp&#8217; in effect the code looks somewhat clearer: </p>
<pre>
  p1 = first_procedure (second_procedure (p2, p3),
                        third_procedure (p4, p5));
</pre>
<p> When a statement is broken in between two or more paren pairs (&#8230;), each extra pair causes the indentation level extra indentation: </p>
<p>if ((((i &lt; 2 &amp;&amp;<br />
       k &gt; 0) ||<br />
      p == 0) &amp;&amp;<br />
     q == 1) ||<br />
        n = 0)</p>
<p> The option &#8216;-ip<i>N</i>&#8216; can be used to set the extra offset per paren. For instance, &#8216;-ip0&#8217; would format the above as: </p>
<p>if ((((i &lt; 2 &amp;&amp;<br />
       k &gt; 0) ||<br />
      p == 0) &amp;&amp;<br />
     q == 1) ||<br />
        n = 0)</p>
<p> <code>indent</code> assumes that tabs are placed at regular intervals of both input and output character streams. These intervals are by default 8 columns wide, but (as of version 1.2) may be changed by the &#8216;-ts&#8217; option. Tabs are treated as the equivalent number of spaces. </p>
<p> The indentation of type declarations in old-style function definitions is controlled by the &#8216;-ip&#8217; parameter. This is a numeric parameter specifying how many spaces to indent type declarations. For example, the default &#8216;-ip5&#8217; makes definitions look like this: </p>
<p>char *<br />
create_world(x, y, scale)<br />
int x;<br />
int y;<br />
float scale;<br />
{<br />
    &#8230;<br />
}</p>
<p> For compatibility with other versions of indent, the option &#8216;-nip&#8217; is provided, which is equivalent to &#8216;-ip0&#8217;. </p>
<p> ANSI C allows white space to be placed on preprocessor command lines between the character &#8216;#&#8217; and the command name. By default, <code>indent</code> removes this space, but specifying the &#8216;-lps&#8217; option directs <code>indent</code> to leave this space unmodified. The option &#8216;-ppi&#8217; overrides &#8216;-nlps&#8217; and &#8216;-lps&#8217;. </p>
<p> This option can be used to request that preprocessor conditional statements can be indented by to given number of spaces, for example with the option &#8216;-ppi 3&#8217; </p>
<p>#if X<br />
#if Y<br />
#define Z 1<br />
#else<br />
#define Z 0<br />
#endif<br />
#endif<br />
 becomes<br />
#if X<br />
#if Y<br />
#define Z 1<br />
#else<br />
#define Z 0<br />
#endif<br />
#endif</p>
<p> This option sets the offset at which a label (except case labels) will be positioned. If it is set to zero or a positive number, this indicates how far from the left margin to indent a label. If it is set to a negative number, this indicates how far back from the current indent level to place the label. The default setting is -2 which matches the behaviour of earlier versions of indent. Note that this parameter does not affect the placing of case labels; see the &#8216;-cli&#8217; parameter for that. For example with the option &#8216;-il 1&#8217; </p>
<p>group function()<br />
{<br />
    if (do_stuff1() == ERROR)<br />
        goto cleanup1;<br />
    if (do_stuff2() == ERROR)<br />
        goto cleanup2;<br />
    return SUCCESS;<br />
cleanup2:<br />
    do_cleanup2();<br />
cleanup1:<br />
    do_cleanup1();<br />
    return ERROR;<br />
}<br />
 becomes<br />
group function()<br />
{<br />
    if (do_stuff1() == ERROR)<br />
        goto cleanup1;<br />
    if (do_stuff2() == ERROR)<br />
        goto cleanup2;<br />
    return SUCCESS;<br />
cleanup2:<br />
    do_cleanup2();<br />
cleanup1:<br />
    do_cleanup1();<br />
    return ERROR;<br />
}</p>
<h2>BREAKING LONG LINES</h2>
<p> With the option &#8216;-l<i>n</i>&#8216;, or &#8216;&#8211;line-length<i>n</i>&#8216;, it is possible to specify the maximum length of a line of C code, not including possible comments that follow it. </p>
<p> When lines become longer than the specified line length, GNU <code>indent</code> tries to break the line at a logical place. This is new as of version 2.1 however and not very intelligent or flexible yet. </p>
<p> Currently there are two options that allow one to interfere with the algorithm that determines where to break a line. </p>
<p> The &#8216;-bbo&#8217; option causes GNU <code>indent</code> to prefer to break long lines before the boolean operators <code>&amp;&amp;</code> and <code>||</code>. The &#8216;-nbbo&#8217; option causes GNU <code>indent</code> not have that preference. For example, the default option &#8216;-bbo&#8217; (together with &#8216;&#8211;line-length60&#8217; and &#8216;&#8211;ignore-newlines&#8217;) makes code look like this: </p>
<p>if (mask &amp;&amp; ((mask[0] == &#8216;
