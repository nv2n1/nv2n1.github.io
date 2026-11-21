---

title: "indent(1)"
name: "indent"
section: "1"
letter: "i"
url: "/docs/linux/man/1-indent/"
description: "indent – changes the appearance of a C program by inserting or deleting whitespace."
---

<p> indent - changes the appearance of a C program by inserting or deleting whitespace.  </p>
<h2>SYNOPSIS</h2>
<p> <code>indent </code> [options] [input-files] </p>
<p> <code>indent </code> [options] [single-input-file] [-o output-file] </p>
<p> <code>indent </code> --version  </p>
<h2>DESCRIPTION</h2>
<p> This man page is generated from the file <i>indent.texinfo</i>. This is Edition of &quot;The <code>indent</code> Manual&quot;, for Indent Version , last updated . </p>
<p> The <code>indent</code> program can be used to make code easier to read. It can also convert from one style of writing C to another. </p>
<p> <code>indent</code> understands a substantial amount about the syntax of C, but it also attempts to cope with incomplete and misformed syntax. </p>
<p> In version 1.2 and more recent versions, the GNU style of indenting is the default.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-bad</code>, <code>--blank-lines-after-declarations</code></dt>
<dd> <p> Force blank lines after the declarations. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-bap</code>, <code>--blank-lines-after-procedures</code></dt>
<dd> <p> Force blank lines after procedure bodies. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-bbb</code>, <code>--blank-lines-before-block-comments</code></dt>
<dd> <p> Force blank lines before block comments. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-bbo</code>, <code>--break-before-boolean-operator</code></dt>
<dd> <p> Prefer to break long lines before boolean operators. <br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>. </p>
 </dd>
<dt><code>-bc</code>, <code>--blank-lines-after-commas</code></dt>
<dd> <p> Force newline after comma in declaration. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-bl</code>, <code>--braces-after-if-line</code></dt>
<dd> <p> Put braces on line after <code>if</code>, etc. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-blf</code>, <code>--braces-after-func-def-line</code></dt>
<dd> <p> Put braces on line following function definition line. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-bli</code><i>n</i>, <code>--brace-indent</code><i>n</i></dt>
<dd> <p> Indent braces <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-bls</code>, <code>--braces-after-struct-decl-line</code></dt>
<dd> <p> Put braces on the line after <code>struct</code> declaration lines. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-br</code>, <code>--braces-on-if-line</code></dt>
<dd> <p> Put braces on line with <code>if</code>, etc. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-brf</code>, <code>--braces-on-func-def-line</code></dt>
<dd> <p> Put braces on function definition line. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-brs</code>, <code>--braces-on-struct-decl-line</code></dt>
<dd> <p> Put braces on <code>struct</code> declaration line. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-bs</code>, <code>--Bill-Shannon</code>, <code>--blank-before-sizeof</code></dt>
<dd> <p> Put a space between <code>sizeof</code> and its argument. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-c</code><i>n</i>, <code>--comment-indentation</code><i>n</i></dt>
<dd> <p> Put comments to the right of code in column <i>n</i>. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-cbi</code><i>n</i>, <code>--case-brace-indentation</code><i>n</i></dt>
<dd> <p> Indent braces after a case label N spaces. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-cd</code><i>n</i>, <code>--declaration-comment-column</code><i>n</i></dt>
<dd> <p> Put comments to the right of the declarations in column <i>n</i>. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-cdb</code>, <code>--comment-delimiters-on-blank-lines</code></dt>
<dd> <p> Put comment delimiters on blank lines. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-cdw</code>, <code>--cuddle-do-while</code></dt>
<dd> <p> Cuddle while of <code>do {} while;</code> and preceding &#8216;}&#8216;. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-ce</code>, <code>--cuddle-else</code></dt>
<dd> <p> Cuddle else and preceding &#8216;}&#8216;. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-ci</code><i>n</i>, <code>--continuation-indentation</code><i>n</i></dt>
<dd> <p> Continuation indent of <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-cli</code><i>n</i>, <code>--case-indentation</code><i>n</i></dt>
<dd> <p> Case label indent of <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-cp</code><i>n</i>, <code>--else-endif-column</code><i>n</i></dt>
<dd> <p> Put comments to the right of <code>#else</code> and <code> #endif</code> statements in column <i>n</i>. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-cs</code>, <code>--space-after-cast</code></dt>
<dd> <p> Put a space after a cast operator. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-d</code><i>n</i>, <code>--line-comments-indentation</code><i>n</i></dt>
<dd> <p> Set indentation of comments not to the right of code to <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-bfda</code>, <code>--break-function-decl-args</code></dt>
<dd> <p> Break the line before all arguments in a declaration. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-bfde</code>, <code>--break-function-decl-args-end</code></dt>
<dd> <p> Break the line after the last argument in a declaration. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-dj</code><i>n</i>, <code>--left-justify-declarations</code></dt>
<dd> <p> If -cd 0 is used then comments after declarations are left justified behind the declaration. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-di</code><i>n</i>, <code>--declaration-indentation</code><i>n</i></dt>
<dd> <p> Put variables in column <i>n</i>. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-fc1</code>, <code>--format-first-column-comments</code></dt>
<dd> <p> Format comments in the first column. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-fca</code>, <code>--format-all-comments</code></dt>
<dd> <p> Do not disable all formatting of comments. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-gnu</code>, <code>--gnu-style</code></dt>
<dd> <p> Use GNU coding style. This is the default. <br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>. </p>
 </dd>
<dt><code>-hnl</code>, <code>--honour-newlines</code></dt>
<dd> <p> Prefer to break long lines at the position of newlines in the input. <br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>. </p>
 </dd>
<dt><code>-i</code><i>n</i>, <code>--indent-level</code><i>n</i></dt>
<dd> <p> Set indentation level to <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-il</code><i>n</i>, <code>--indent-label</code><i>n</i></dt>
<dd> <p> Set offset for labels to column <i>n</i>. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-ip</code><i>n</i>, <code>--parameter-indentation</code><i>n</i></dt>
<dd> <p> Indent parameter types in old-style function definitions by <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-kr</code>, <code>--k-and-r-style</code></dt>
<dd> <p> Use Kernighan &amp; Ritchie coding style. <br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>. </p>
 </dd>
<dt><code>-l</code><i>n</i>, <code>--line-length</code><i>n</i></dt>
<dd> <p> Set maximum line length for non-comment lines to <i>n</i>. <br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>. </p>
 </dd>
<dt><code>-lc</code><i>n</i>, <code>--comment-line-length</code><i>n</i></dt>
<dd> <p> Set maximum line length for comment formatting to <i>n</i>. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-linux</code>, <code>--linux-style</code></dt>
<dd> <p> Use Linux coding style. <br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>. </p>
 </dd>
<dt><code>-lp</code>, <code>--continue-at-parentheses</code></dt>
<dd> <p> Line up continued lines at parentheses. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-lps</code>, <code>--leave-preprocessor-space</code></dt>
<dd> <p> Leave space between &#8216;#&#8216; and preprocessor directive. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-nlps</code>, <code>--remove-preprocessor-space</code></dt>
<dd> <p> Remove space between &#8216;#&#8216; and preprocessor directive. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-nbad</code>, <code>--no-blank-lines-after-declarations</code></dt>
<dd> <p> Do not force blank lines after declarations. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-nbap</code>, <code>--no-blank-lines-after-procedures</code></dt>
<dd> <p> Do not force blank lines after procedure bodies. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-nbbo</code>, <code>--break-after-boolean-operator</code></dt>
<dd> <p> Do not prefer to break long lines before boolean operators. <br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>. </p>
 </dd>
<dt><code>-nbc</code>, <code>--no-blank-lines-after-commas</code></dt>
<dd> <p> Do not force newlines after commas in declarations. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-nbfda</code>, <code>--dont-break-function-decl-args</code></dt>
<dd> <p> Don&#8217;t put each argument in a function declaration on a separate line. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-ncdb</code>, <code>--no-comment-delimiters-on-blank-lines</code></dt>
<dd> <p> Do not put comment delimiters on blank lines. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-ncdw</code>, <code>--dont-cuddle-do-while</code></dt>
<dd> <p> Do not cuddle <code>}</code> and the <code>while</code> of a <code>do {} while;</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-nce</code>, <code>--dont-cuddle-else</code></dt>
<dd> <p> Do not cuddle <code>}</code> and <code>else</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-ncs</code>, <code>--no-space-after-casts</code></dt>
<dd> <p> Do not put a space after cast operators. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-ndj</code><i>n</i>, <code>--dont-left-justify-declarations</code></dt>
<dd> <p> Comments after declarations are treated the same as comments after other statements. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-nfc1</code>, <code>--dont-format-first-column-comments</code></dt>
<dd> <p> Do not format comments in the first column as normal. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-nfca</code>, <code>--dont-format-comments</code></dt>
<dd> <p> Do not format any comments. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-nhnl</code>, <code>--ignore-newlines</code></dt>
<dd> <p> Do not prefer to break long lines at the position of newlines in the input. <br />
 See <code>&nbsp;<wbr>BREAKING LONG LINES</code>. </p>
 </dd>
<dt><code>-nip</code>, <code>--no-parameter-indentation</code></dt>
<dd> <p> Zero width indentation for parameters. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-nlp</code>, <code>--dont-line-up-parentheses</code></dt>
<dd> <p> Do not line up parentheses. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-npcs</code>, <code>--no-space-after-function-call-names</code></dt>
<dd> <p> Do not put space after the function in function calls. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-nprs</code>, <code>--no-space-after-parentheses</code></dt>
<dd> <p> Do not put a space after every &#8216;(&#8216; and before every &#8216;)&#8216;. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-npsl</code>, <code>--dont-break-procedure-type</code></dt>
<dd> <p> Put the type of a procedure on the same line as its name. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-nsaf</code>, <code>--no-space-after-for</code></dt>
<dd> <p> Do not put a space after every <code>for</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-nsai</code>, <code>--no-space-after-if</code></dt>
<dd> <p> Do not put a space after every <code>if</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-nsaw</code>, <code>--no-space-after-while</code></dt>
<dd> <p> Do not put a space after every <code>while</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-nsc</code>, <code>--dont-star-comments</code></dt>
<dd> <p> Do not put the &#8216;*&#8216; character at the left of comments. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-nsob</code>, <code>--leave-optional-blank-lines</code></dt>
<dd> <p> Do not swallow optional blank lines. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-nss</code>, <code>--dont-space-special-semicolon</code></dt>
<dd> <p> Do not force a space before the semicolon after certain statements. Disables &#8216;-ss&#8217;. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-nut</code>, <code>--no-tabs</code></dt>
<dd> <p> Use spaces instead of tabs. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-nv</code>, <code>--no-verbosity</code></dt>
<dd> <p> Disable verbose mode. <br />
 See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>. </p>
 </dd>
<dt><code>-orig</code>, <code>--original</code></dt>
<dd> <p> Use the original Berkeley coding style. <br />
 See <code>&nbsp;<wbr>COMMON STYLES</code>. </p>
 </dd>
<dt><code>-npro</code>, <code>--ignore-profile</code></dt>
<dd> <p> Do not read &#8216;.indent.pro&#8217; files. <br />
 See <code>&nbsp;<wbr>INVOKING INDENT</code>. </p>
 </dd>
<dt><code>-pcs</code>, <code>--space-after-procedure-calls</code></dt>
<dd> <p> Insert a space between the name of the procedure being called and the &#8216;(&#8216;. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-pi</code><i>n</i>, <code>--paren-indentation</code><i>n</i></dt>
<dd> <p> Specify the extra indentation per open parentheses &#8216;(&#8216; when a statement is broken.See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-pmt</code>, <code>--preserve-mtime</code></dt>
<dd> <p> Preserve access and modification times on output files.See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>. </p>
 </dd>
<dt><code>-ppi</code><i>n</i>, <code>--preprocessor-indentation</code><i>n</i></dt>
<dd> <p> Specify the indentation for preprocessor conditional statements.See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-prs</code>, <code>--space-after-parentheses</code></dt>
<dd> <p> Put a space after every &#8216;(&#8216; and before every &#8216;)&#8216;. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-psl</code>, <code>--procnames-start-lines</code></dt>
<dd> <p> Put the type of a procedure on the line before its name. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-saf</code>, <code>--space-after-for</code></dt>
<dd> <p> Put a space after each <code>for</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-sai</code>, <code>--space-after-if</code></dt>
<dd> <p> Put a space after each <code>if</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-saw</code>, <code>--space-after-while</code></dt>
<dd> <p> Put a space after each <code>while</code>. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-sbi</code><i>n</i>, <code>--struct-brace-indentation</code><i>n</i></dt>
<dd> <p> Indent braces of a struct, union or enum N spaces. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-sc</code>, <code>--start-left-side-of-comments</code></dt>
<dd> <p> Put the &#8216;*&#8216; character at the left of comments. <br />
 See <code>&nbsp;<wbr>COMMENTS</code>. </p>
 </dd>
<dt><code>-sob</code>, <code>--swallow-optional-blank-lines</code></dt>
<dd> <p> Swallow optional blank lines. <br />
 See <code>&nbsp;<wbr>BLANK LINES</code>. </p>
 </dd>
<dt><code>-ss</code>, <code>--space-special-semicolon</code></dt>
<dd> <p> On one-line <code>for</code> and <code>while</code> statements, force a blank before the semicolon. <br />
 See <code>&nbsp;<wbr>STATEMENTS</code>. </p>
 </dd>
<dt><code>-st</code>, <code>--standard-output</code></dt>
<dd> <p> Write to standard output. <br />
 See <code>&nbsp;<wbr>INVOKING INDENT</code>. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> Tell <code>indent</code> the name of typenames. <br />
 See <code>&nbsp;<wbr>DECLARATIONS</code>. </p>
 </dd>
<dt><code>-ts</code><i>n</i>, <code>--tab-size</code><i>n</i></dt>
<dd> <p> Set tab size to <i>n</i> spaces. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-ut</code>, <code>--use-tabs</code></dt>
<dd> <p> Use tabs. This is the default. <br />
 See <code>&nbsp;<wbr>INDENTATION</code>. </p>
 </dd>
<dt><code>-v</code>, <code>--verbose</code></dt>
<dd> <p> Enable verbose mode. <br />
 See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Output the version number of <code>indent</code>. <br />
 See <code>&nbsp;<wbr>MISCELLANEOUS OPTIONS</code>. </p>
 </dd></dl>
<h2>INVOKING INDENT</h2>
<p> As of version 1.3, the format of the <code>indent</code> command is: </p>
<pre><code>indent [ options ] [ input-files ]
indent [ options ] [ single-input-file ] [-o output-file ]
</code></pre>
<p> This format is different from earlier versions and other versions of <code>indent</code>. </p>
<p> In the first form, one or more input files are specified. <code>indent</code> makes a backup copy of each file, and the original file is replaced with its indented version. See <code>BACKUP FILES</code>, for an explanation of how backups are made. </p>
<p> In the second form, only one input file is specified. In this case, or when the standard input is used, you may specify an output file after the &#8216;-o&#8217; option. </p>
<p> To cause <code>indent</code> to write to standard output, use the &#8216;-st&#8217; option. This is only allowed when there is only one input file, or when the standard input is used. </p>
<p> If no input files are named, the standard input is read for input. Also, if a filename named &#8216;-&#8216; is specified, then the standard input is read. </p>
<p> As an example, each of the following commands will input the program &#8216;slithy_toves.c&#8217; and write its indented text to &#8216;slithy_toves.out&#8217;: </p>
<pre><code>indent slithy_toves.c -o slithy_toves.out
indent -st slithy_toves.c &gt; slithy_toves.out
cat slithy_toves.c | indent -o slithy_toves.out
</code></pre>
<p> Most other options to <code>indent</code> control how programs are formatted. As of version 1.2, <code>indent</code> also recognizes a long name for each option name. Long options are prefixed by either &#8216;--&#8216; or &#8216;+&#8216;. [ &#8216;+&#8216; is being superseded by &#8216;--&#8216; to maintain consistency with the POSIX standard.] <br />
&nbsp;<wbr>In most of this document, the traditional, short names are used for the sake of brevity. See <code>OPTION SUMMARY</code>, for a list of options, including both long and short names. </p>
<p> Here is another example: </p>
<pre><code>indent -br test/metabolism.c -l85
</code></pre>
<p> This will indent the program &#8216;test/metabolism.c&#8217; using the &#8216;-br&#8217; and &#8216;-l85&#8217; options, write the output back to &#8216;test/metabolism.c&#8217;, and write the original contents of &#8216;test/metabolism.c&#8217; to a backup file in the directory &#8216;test&#8217;. </p>
<p> Equivalent invocations using long option names for this example would be: </p>
<pre><code>indent --braces-on-if-line --line-length185 test/metabolism.c
indent +braces-on-if-line +line-length185 test/metabolism.c
</code></pre>
<p> If you find that you often use <code>indent</code> with the same options, you may put those options into a file named &#8216;.indent.pro&#8217;. <code>indent</code> will look for a profile file in three places. First it will check the environment variable <code>INDENT_PROFILE</code>. If that exists its value is expected to name the file that is to be used. If the environment variable does not exist, indent looks for &#8216;.indent.pro&#8217; in the current directory <br />
&nbsp;<wbr>and use that if found.&nbsp;<wbr>&nbsp;<wbr>Finally&nbsp;<wbr><code>indent</code>&nbsp;<wbr>will search your home directory for &#8216;.indent.pro&#8217; and use that file if it is found. This behaviour is different from that of other versions of <code>indent</code>, which load both files if they both exist. </p>
<p> The format of &#8216;.indent.pro&#8217; is simply a list of options, just as they would appear on the command line, separated by white space (tabs, spaces, and newlines). Options in &#8216;.indent.pro&#8217; may be surrounded by C or C++ comments, in which case they are ignored. </p>
<p> Command line switches are handled <i>after</i> processing &#8216; .indent.pro&#8217;. Options specified later override arguments specified earlier, with one exception: Explicitly specified options always override background options (See <code>COMMON STYLES</code>). You can prevent <code>indent</code> from reading an &#8216;.indent.pro&#8217; file by specifying the &#8216;-npro&#8217; option. </p>
<h2>BACKUP FILES</h2>
<p> As of version 1.3, GNU <code>indent</code> makes GNU-style backup files, the same way GNU Emacs does. This means that either <i>simple</i> or <i>numbered</i> backup filenames may be made. </p>
<p> Simple backup file names are generated by appending a suffix to the original file name. The default for this suffix is the one-character string &#8216;~&#8216; (tilde). Thus, the backup file for &#8216;python.c&#8217; would be &#8216;python.c~&#8216;. </p>
<p> Instead of the default, you may specify any string as a suffix by setting the environment variable <code>SIMPLE_BACKUP_SUFFIX</code> to your preferred suffix. </p>
<p> Numbered backup versions of a file &#8216;momeraths.c&#8217; look like &#8216;momeraths.c.~23~&#8216;, where 23 is the version of this particular backup. When making a numbered backup of the file &#8216;src/momeraths.c&#8217;, the backup file will be named &#8216;src/momeraths.c.~<i>V</i>~&#8216;, where <i>V</i> is one greater than the highest version currently existing in the directory &#8216;src&#8217;. The environment variable <code>VERSION_WIDTH</code> controls the number of digits, using left zero padding when necessary. For instance, setting this variable to &quot;2&quot; will lead to the backup file being named &#8216;momeraths.c.~04~&#8216;. </p>
<p> The type of backup file made is controlled by the value of the environment variable <code>VERSION_CONTROL</code>. If it is the string &#8216;simple&#8217;, then only simple backups will be made. If its value is the string &#8216;numbered&#8217;, then numbered backups will be made. If its value is &#8216;numbered-existing&#8217;, then numbered backups will be made if there <i>already exist</i> numbered backups for the file being indented; otherwise, a simple backup is made. If <code>VERSION_CONTROL</code> is not set, then <code>indent</code> assumes the behaviour of &#8216;numbered-existing&#8217;. </p>
<p> Other versions of <code>indent</code> use the suffix &#8216;.BAK&#8217; in naming backup files. This behaviour can be emulated by setting <code>SIMPLE_BACKUP_SUFFIX</code> to &#8216;.BAK&#8217;. </p>
<p> Note also that other versions of <code>indent</code> make backups in the current directory, rather than in the directory of the source file as GNU <code>indent</code> now does. </p>
<h2>COMMON STYLES</h2>
<p> There are several common styles of C code, including the GNU style, the Kernighan &amp; Ritchie style, and the original Berkeley style. A style may be selected with a single <i>background</i> option, which specifies a set of values for all other options. However, explicitly specified options always override options implied by a background option. </p>
<p> As of version 1.2, the default style of GNU <code>indent</code> is the GNU style. Thus, it is no longer necessary to specify the option &#8216;-gnu&#8217; to obtain this format, although doing so will not cause an error. Option settings which correspond to the GNU style are: </p>
<pre><code>-nbad -bap -nbc -bbo -bl -bli2 -bls -ncdb -nce -cp1 -cs -di2
-ndj -nfc1 -nfca -hnl -i2 -ip5 -lp -pcs -nprs -psl -saf -sai
-saw -nsc -nsob
</code></pre>
<p> The GNU coding style is that preferred by the GNU project. It is the style that the GNU Emacs C mode encourages and which is used in the C portions of GNU Emacs. (People interested in writing programs for Project GNU should get a copy of &quot;The GNU Coding Standards&quot;, which also covers semantic and portability issues such as memory usage, the size of integers, etc.) </p>
<p> The Kernighan &amp; Ritchie style is used throughout their well-known book &quot;The C Programming Language&quot;. It is enabled with the &#8216;-kr&#8217; option. The Kernighan &amp; Ritchie style corresponds to the following set of options: </p>
<pre><code>-nbad -bap -bbo -nbc -br -brs -c33 -cd33 -ncdb -ce -ci4 -cli0
-cp33 -cs -d0 -di1 -nfc1 -nfca -hnl -i4 -ip0 -l75 -lp -npcs
-nprs -npsl -saf -sai -saw -nsc -nsob -nss
</code></pre>
<p> Kernighan &amp; Ritchie style does not put comments to the right of code in the same column at all times (nor does it use only one space to the right of the code), so for this style <code>indent</code> has arbitrarily chosen column 33. </p>
<p> The style of the original Berkeley <code>indent</code> may be obtained by specifying &#8216;-orig&#8217; (or by specifying &#8216;--original&#8217;, using the long option name). This style is equivalent to the following settings: </p>
<pre><code>-nbad -nbap -bbo -bc -br -brs -c33 -cd33 -cdb -ce -ci4 -cli0
-cp33 -di16 -fc1 -fca -hnl -i4 -ip4 -l75 -lp -npcs -nprs -psl
-saf -sai -saw -sc -nsob -nss -ts8
</code></pre>
<p> The Linux style is used in the linux kernel code and drivers. Code generally has to follow the Linux coding style to be accepted. This style is equivalent to the following settings: </p>
<pre><code>-nbad -bap -nbc -bbo -hnl -br -brs -c33 -cd33 -ncdb -ce -ci4
-cli0 -d0 -di1 -nfc1 -i8 -ip0 -l80 -lp -npcs -nprs -npsl -sai
-saf -saw -ncs -nsc -sob -nfca -cp33 -ss -ts8 -il1
</code></pre>
<h2>BLANK LINES</h2>
<p> Various programming styles use blank lines in different places. <code>indent</code> has a number of options to insert or delete blank lines in specific places. </p>
<p> The &#8216;-bad&#8217; option causes <code>indent</code> to force a blank line after every block of declarations. The &#8216;-nbad&#8217; option causes <code>indent</code> not to force such blank lines. </p>
<p> The &#8216;-bap&#8217; option forces a blank line after every procedure body. The &#8216;-nbap&#8217; option forces no such blank line. </p>
<p> The &#8216;-bbb&#8217; option forces a blank line before every boxed comment (See <code>COMMENTS</code>.) The &#8216;-nbbb&#8217; option does not force such blank lines. </p>
<p> The &#8216;-sob&#8217; option causes <code>indent</code> to swallow optional blank lines (that is, any optional blank lines present in the input will be removed from the output). If the &#8216;-nsob&#8217; is specified, any blank lines present in the input file will be copied to the output file. </p>
<h2>--blank-lines-after-declarations</h2>
<p> The &#8216;-bad&#8217; option forces a blank line after every block of declarations. The &#8216;-nbad&#8217; option does not add any such blank lines. </p>
<p> For example, given the input </p>
<pre><code>char *foo;
char *bar;
/* This separates blocks of declarations. */
int baz;
</code></pre>
<p> <code>indent -bad</code> produces </p>
<pre><code>char *foo;
char *bar;
/* This separates blocks of declarations. */
int baz;
</code></pre>
<p> and <code>indent -nbad</code> produces </p>
<pre><code>char *foo;
char *bar;
/* This separates blocks of declarations. */
int baz;
</code></pre>
<h2>--blank-lines-after-procedures</h2>
<p> The &#8216;-bap&#8217; option forces a blank line after every procedure body. </p>
<p> For example, given the input </p>
<pre><code>int
foo ()
{
  puts(&quot;Hi&quot;);
}
/* The procedure bar is even less interesting. */
char *
bar ()
{
  puts(&quot;Hello&quot;);
}
</code></pre>
<p> <code>indent -bap</code> produces </p>
<pre><code>int
foo ()
{
  puts (&quot;Hi&quot;);
}
/* The procedure bar is even less interesting. */
char *
bar ()
{
  puts (&quot;Hello&quot;);
}
</code></pre>
<p> and <code>indent -nbap</code> produces </p>
<pre><code>int
foo ()
{
  puts (&quot;Hi&quot;);
}
/* The procedure bar is even less interesting. */
char *
bar ()
{
  puts (&quot;Hello&quot;);
}
</code></pre>
<p> No blank line will be added after the procedure <code>foo</code>. </p>
<h2>COMMENTS</h2>
<p> <code>indent</code> formats both C and C++ comments. C comments are begun with &#8216;/*&#8216;, terminated with &#8216;*/&#8216; and may contain newline characters. C++ comments begin with the delimiter &#8216;//&#8216; and end at the newline. </p>
<p> <code>indent</code> handles comments differently depending upon their context. <code>indent</code> attempts to distinguish between comments which follow statements, comments which follow declarations, comments following preprocessor directives, and comments which are not preceded by code of any sort, i.e., they begin the text of the line (although not necessarily in column 1). </p>
<p> <code>indent</code> further distinguishes between comments found outside of procedures and aggregates, and those found within them. In particular, comments beginning a line found within a procedure will be indented to the column at which code is currently indented. The exception to this is a comment beginning in the leftmost column; such a comment is output at that column. </p>
<p> <code>indent</code> attempts to leave <i>boxed comments</i> unmodified. The general idea of such a comment is that it is enclosed in a rectangle or &#8216;&#8216;box&#8217;&#8216; of stars or dashes to visually set it apart. More precisely, boxed comments are defined as those in which the initial &#8216;/*&#8216; is followed immediately by the character &#8216;*&#8216;, &#8216;=&#8216;, &#8216;_&#8216;, or &#8216;-&#8216;, or those in which the beginning comment delimiter (&#8216;/*&#8216;) is on a line by itself, and the following line begins with a &#8216;*&#8216; in the same column as the star of the opening delimiter. </p>
<p> Examples of boxed comments are: </p>
<pre><code>/**********************
 * Comment in a box!! *
 **********************/
       /*
        * A different kind of scent,
        * for a different kind of comment.
        */
</code></pre>
<p> <code>indent</code> attempts to leave boxed comments exactly as they are found in the source file. Thus the indentation of the comment is unchanged, and its length is not checked in any way. The only alteration made is that an embedded tab character may be converted into the appropriate number of spaces. </p>
<p> If the &#8216;-bbb&#8217; option is specified, all such boxed comments will be preceded by a blank line, unless such a comment is preceded by code. </p>
<p> Comments which are not boxed comments may be formatted, which means that the line is broken to fit within a right margin and left-filled with whitespace. Single newlines are equivalent to a space, but blank lines (two or more newlines in a row) are taken to mean a paragraph break. Formatting of comments which begin after the first column is enabled with the &#8216;-fca&#8217; option. To format those beginning in column one, specify &#8216;-fc1&#8217;. Such formatting is disabled by default. </p>
<p> The right margin for formatting defaults to 78, but may be changed with the &#8216;-lc&#8217; option. If the margin specified does not allow the comment to be printed, the margin will be automatically extended for the duration of that comment. The margin is not respected if the comment is not being formatted. </p>
<p> If the comment begins a line (i.e., there is no program text to its left), it will be indented to the column it was found in unless the comment is within a block of code. In that case, such a comment will be aligned with the indented code of that block (unless the comment began in the first column). This alignment may be affected by the &#8216;-d&#8217; option, which specifies an amount by which such comments are moved to the <i>left</i>, or unindented. For example, &#8216;-d2&#8217; places comments two spaces to the left of code. By default, comments are aligned with code, unless they begin in the first column, in which case they are left there by default --- to get them aligned with the code, specify &#8216;-fc1&#8217;. </p>
<p> Comments to the right of code will appear by default in column 33. This may be changed with one of three options. &#8216;-c&#8217; will specify the column for comments following code, &#8216;-cd&#8217; specifies the column for comments following declarations, and &#8216;-cp&#8217; specifies the column for comments following preprocessor directives <code>#else</code> and <code>#endif</code>. &#8216;-dj&#8217; together with &#8216;-cd0&#8217; can be used to suppress alignment of comments to the right of declarations, causing the comment to follow one tabstop from the end of the declaration. Normally &#8216;-cd0&#8217; causes &#8216;-c&#8217; to become effective. </p>
<p> If the code to the left of the comment exceeds the beginning column, the comment column will be extended to the next tabstop column past the end of the code, or in the case of preprocessor directives, to one space past the end of the directive. This extension lasts only for the output of that particular comment. </p>
<p> The &#8216;-cdb&#8217; option places the comment delimiters on blank lines. Thus, a single line comment like <code>/* Loving hug */</code> can be transformed into: </p>
<pre><code>/*
   Loving hug
 */
</code></pre>
<p> Stars can be placed at the beginning of multi-line comments with the &#8216;-sc&#8217; option. Thus, the single-line comment above can be transformed (with &#8216;-cdb -sc&#8217;) into: </p>
<pre><code>/*
 * Loving hug
 */
</code></pre>
<h2>STATEMENTS</h2>
<p> The &#8216;-br&#8217; or &#8216;-bl&#8217; option specifies how to format braces. </p>
<p> The &#8216;-br&#8217; option formats statement braces like this: </p>
<pre><code>if (x &gt; 0) {
  x--;
}
</code></pre>
<p> The &#8216;-bl&#8217; option formats them like this: </p>
<pre><code>if (x &gt; 0)
  {
    x--;
  }
</code></pre>
<p> If you use the &#8216;-bl&#8217; option, you may also want to specify the &#8216;-bli&#8217; option. This option specifies the number of spaces by which braces are indented. &#8216;-bli2&#8217;, the default, gives the result shown above. &#8216;-bli0&#8217; results in the following: </p>
<pre><code>if (x &gt; 0)
{
  x--;
}
</code></pre>
<p> If you are using the &#8216;-br&#8217; option, you probably want to also use the &#8216;-ce&#8217; option. This causes the <code>else</code> in an if-then-else construct to cuddle up to the immediately preceding &#8216;}&#8216;. For example, with &#8216;-br -ce&#8217; you get the following: </p>
<pre><code>if (x &gt; 0) {
  x--;
} else {
  fprintf (stderr, &quot;...something wrong?\n&quot;);
}
</code></pre>
<p> With &#8216;-br -nce&#8217; that code would appear as </p>
<pre><code>if (x &gt; 0) {
  x--;
}
else {
  fprintf (stderr, &quot;...something wrong?\n&quot;);
}
</code></pre>
<p> This causes the <code>while</code> in a do-while loop to cuddle up to the immediately preceding &#8216;}&#8216;. For example, with &#8216;-cdw&#8217; you get the following: </p>
<pre><code>do {
  x--;
} while (x);
</code></pre>
<p> With &#8216;-ncdw&#8217; that code would appear as </p>
<pre><code>do {
  x--;
}
while (x);
</code></pre>
<p> The &#8216;-cli&#8217; option specifies the number of spaces that case labels should be indented to the right of the containing <code>switch</code> statement. </p>
<p> The default gives code like: </p>
<pre><code>switch (i)
  {
  case 0:
    break;
  case 1:
    {
      ++i;
    }
  default:
    break;
  }
</code></pre>
<p> Using the &#8216;-cli2&#8217; that would become: </p>
<pre><code>switch (i)
  {
    case 0:
      break;
    case 1:
      {
        ++i;
      }
    default:
      break;
  }
</code></pre>
<p> The indentation of the braces below a case statement can be controlled with the &#8216;-cbi <i>n</i>&#8216; option. For example, using &#8216;-cli2 -cbi0&#8217; results in: </p>
<pre><code>switch (i)
  {
    case 0:
      break;
    case 1:
    {
      ++i;
    }
    default:
      break;
  }
</code></pre>
<p> If a semicolon is on the same line as a <code>for</code> or <code>while</code> statement, the &#8216;-ss&#8217; option will cause a space to be placed before the semicolon. This emphasizes the semicolon, making it clear that the body of the <code>for</code> or <code>while</code> statement is an empty statement. &#8216;-nss&#8217; disables this feature. </p>
<p> The &#8216;-pcs&#8217; option causes a space to be placed between the name of the procedure being called and the &#8216;(&#8216; (for example, <code>puts&nbsp;<wbr>(&quot;Hi&quot;);</code>. The &#8216;-npcs&#8217; option would give <code>puts(&quot;Hi&quot;);</code>). </p>
<p> If the &#8216;-cs&#8217; option is specified, <code>indent</code> puts a space between a cast operator and the object to be cast. The &#8216;-ncs&#8217; ensures that there is no space between the cast operator and the object. Remember that <code>indent</code> only knows about the standard C data types and so cannot recognise user-defined types in casts. Thus <code>(mytype)thing</code> is not treated as a cast. </p>
<p> The &#8216;-bs&#8217; option ensures that there is a space between the keyword <code>sizeof</code> and its argument. In some versions, this is known as the &#8216;Bill_Shannon&#8217; option. </p>
<p> The &#8216;-saf&#8217; option forces a space between a <code>for</code> and the following parenthesis. This is the default. </p>
<p> The &#8216;-sai&#8217; option forces a space between a <code>if</code> and the following parenthesis. This is the default. </p>
<p> The &#8216;-saw&#8217; option forces a space between a <code>while</code> and the following parenthesis. This is the default. </p>
<p> The &#8216;-prs&#8217; option causes all parentheses to be separated with a space from whatever is between them. For example, using &#8216;-prs&#8217; results in code like: </p>
<pre><code>  while ( ( e_code - s_code ) &lt; ( dec_ind - 1 ) )
    {
      set_buf_break ( bb_dec_ind );
      *e_code++ = ' ';
    }
</code></pre>
<h2>DECLARATIONS</h2>
<p> By default <code>indent</code> will line up identifiers, in the column specified by the &#8216;-di&#8217; option. For example, &#8216;-di16&#8217; makes things look like: </p>
<pre><code>int foo;
char *bar;
</code></pre>
<p> Using a small value (such as one or two) for the &#8216;-di&#8217; option can be used to cause the identifiers to be placed in the first available position; for example: </p>
<pre><code>int foo;
char *bar;
</code></pre>
<p> The value given to the &#8216;-di&#8217; option will still affect variables which are put on separate lines from their types, for example &#8216;-di2&#8217; will lead to: </p>
<pre><code>int
  foo;
</code></pre>
<p> If the &#8216;-bc&#8217; option is specified, a newline is forced after each comma in a declaration. For example, </p>
<pre><code>int a,
  b,
  c;
</code></pre>
<p> With the &#8216;-nbc&#8217; option this would look like </p>
<pre><code>int a, b, c;
</code></pre>
<p> The &#8216;-bfda&#8217; option causes a newline to be forced after the comma separating the arguments of a function declaration. The arguments will appear at one indention level deeper than the function declaration. This is particularly helpful for functions with long argument lists. The option &#8216;-bfde&#8217; causes a newline to be forced before the closing bracket of the function declaration. For both options the &#8216;n&#8217; setting is the default: -nbdfa and -nbdfe. </p>
<p> For example, </p>
<pre><code>void foo (int arg1, char arg2, int *arg3, long arg4, char arg5);
</code></pre>
<p> With the &#8216;-bfda&#8217; option this would look like </p>
<pre><code>void foo (
    int arg1,
    char arg2,
    int *arg3,
    long arg4,
    char arg5);
</code></pre>
<p> With, in addition, the &#8216;-bfde&#8217; option this would look like </p>
<pre><code>void foo (
    int arg1,
    char arg2,
    int *arg3,
    long arg4,
    char arg5
    );
</code></pre>
<p> The &#8216;-psl&#8217; option causes the type of a procedure being defined to be placed on the line before the name of the procedure. This style is required for the <code>etags</code> program to work correctly, as well as some of the <code>c-mode</code> functions of Emacs. </p>
<p> You must use the &#8216;-T&#8217; option to tell <code>indent</code> the name of all the typenames in your program that are defined by <code>typedef</code>. &#8216;-T&#8217; can be specified more than once, and all names specified are used. For example, if your program contains </p>
<pre><code>typedef unsigned long CODE_ADDR;
typedef enum {red, blue, green} COLOR;
</code></pre>
<p> you would use the options &#8216;-T CODE_ADDR -T COLOR&#8217;. </p>
<p> The &#8216;-brs&#8217; or &#8216;-bls&#8217; option specifies how to format braces in struct declarations. The &#8216;-brs&#8217; option formats braces like this: </p>
<pre><code>struct foo {
  int x;
};
</code></pre>
<p> The &#8216;-bls&#8217; option formats them like this: </p>
<pre><code>struct foo
{
  int x;
};
</code></pre>
<p> Similarly to the structure brace &#8216;-brs&#8217; and &#8216;-bls&#8217; options, <br />
&nbsp;<wbr>the function brace options&nbsp;<wbr>&#8216;-brf&#8217;&nbsp;<wbr>or&nbsp;<wbr>&#8216;-blf&#8217;&nbsp;<wbr>specify how to format the braces in function definitions. The &#8216;-brf&#8217; option formats braces like this: </p>
<pre><code>int one(void) {
  return 1;
};
</code></pre>
<p> The &#8216;-blf&#8217; option formats them like this: </p>
<pre><code>int one(void)
{
  return 1;
};
</code></pre>
<h2>INDENTATION</h2>
<p> One issue in the formatting of code is how far each line should be indented from the left margin. When the beginning of a statement such as <code>if</code> or <code>for</code> is encountered, the indentation level is increased by the value specified by the &#8216;-i&#8217; option. For example, use &#8216;-i8&#8217; to specify an eight character indentation for each level. When a statement is broken across two lines, the second line is indented by a number of additional spaces specified by the &#8216;-ci&#8217; option. &#8216;-ci&#8217; defaults to 0. However, if the &#8216;-lp&#8217; option is specified, and a line has a left parenthesis which is not closed on that line, then continuation lines will be lined up to start at the character position just after the left parenthesis. This processing also applies to &#8216;[&#8216; and applies to &#8216;{&#8216; when it occurs in initialization lists. For example, a piece of continued code might look like this with &#8216;-nlp -ci3&#8217; in effect: </p>
<pre><code>  p1 = first_procedure (second_procedure (p2, p3),
     third_procedure (p4, p5));
</code></pre>
<p> With &#8216;-lp&#8217; in effect the code looks somewhat clearer: </p>
<pre><code>  p1 = first_procedure (second_procedure (p2, p3),
                        third_procedure (p4, p5));
</code></pre>
<p> When a statement is broken in between two or more paren pairs (...), each extra pair causes the indentation level extra indentation: </p>
<pre><code>if ((((i &lt; 2 &amp;&amp;
        k &gt; 0) || p == 0) &amp;&amp;
    q == 1) ||
  n = 0)
</code></pre>
<p> The option &#8216;-ip <i>N</i>&#8216; can be used to set the extra offset per paren. For instance, &#8216;-ip0&#8217; would format the above as: </p>
<pre><code>if ((((i &lt; 2 &amp;&amp;
  k &gt; 0) || p == 0) &amp;&amp;
  q == 1) ||
  n = 0)
</code></pre>
<p> <code>indent</code> assumes that tabs are placed at regular intervals of both input and output character streams. These intervals are by default 8 columns wide, but (as of version 1.2) may be changed by the &#8216;-ts&#8217; option. Tabs are treated as the equivalent number of spaces. </p>
<p> The indentation of type declarations in old-style function definitions is controlled by the &#8216;-ip&#8217; parameter. This is a numeric parameter specifying how many spaces to indent type declarations. For example, the default &#8216;-ip5&#8217; makes definitions look like this: </p>
<pre><code>char *
create_world (x, y, scale)
     int x;
     int y;
     float scale;
{
  . . .
}
</code></pre>
<p> For compatibility with other versions of indent, the option &#8216;-nip&#8217; is provided, which is equivalent to &#8216;-ip0&#8217;. </p>
<p> ANSI C allows white space to be placed on preprocessor command lines between the character &#8216;#&#8216; and the command name. By default, <code>indent</code> removes this space, but specifying the &#8216;-lps&#8217; option directs <code>indent</code> to leave this space unmodified. The option &#8216;-ppi&#8217; overrides &#8216;-nlps&#8217; and &#8216;-lps&#8217;. </p>
<p> This option can be used to request that preprocessor conditional statements can be indented by to given number of spaces, for example with the option &#8216;-ppi 3&#8217; </p>
<pre><code>#if X
#if Y
#define Z 1
#else
#define Z 0
#endif
#endif
</code></pre>
<p> becomes </p>
<pre><code>#if X
# if Y
# define Z 1
# else
# define Z 0
# endif
#endif
</code></pre>
<p> This option sets the offset at which a label (except case labels) will be positioned. If it is set to zero or a positive number, this indicates how far from the left margin to indent a label. If it is set to a negative number, this indicates how far back from the current indent level to place the label. The default setting is -2 which matches the behaviour of earlier versions of indent. Note that this parameter does not affect the placing of case labels; see the &#8216;-cli&#8217; parameter for that. For example with the option &#8216;-il 1&#8217; </p>
<pre><code>group
function()
{
    if (do_stuff1() == ERROR)
        goto cleanup1;
    if (do_stuff2() == ERROR)
        goto cleanup2;
    return SUCCESS;
  cleanup2:
    do_cleanup2();
  cleanup1:
    do_cleanup1();
    return ERROR;
}
</code></pre>
<p> becomes </p>
<pre><code>group
function()
{
    if (do_stuff1() == ERROR)
        goto cleanup1;
    if (do_stuff2() == ERROR)
        goto cleanup2;
    return SUCCESS;
 cleanup2:
    do_cleanup2();
 cleanup1:
    do_cleanup1();
    return ERROR;
}
</code></pre>
<h2>BREAKING LONG LINES</h2>
<p> With the option &#8216;-l <i>n</i>&#8216;, or &#8216;--line-length <i>n</i>&#8216;, it is possible to specify the maximum length of a line of C code, not including possible comments that follow it. </p>
<p> When lines become longer than the specified line length, GNU <code>indent</code> tries to break the line at a logical place. This is new as of version 2.1 however and not very intelligent or flexible yet. </p>
<p> Currently there are two options that allow one to interfere with the algorithm that determines where to break a line. </p>
<p> The &#8216;-bbo&#8217; option causes GNU <code>indent</code> to prefer to break long lines before the boolean operators <code>&amp;&amp;</code> and <code>||</code>. The &#8216;-nbbo&#8217; option causes GNU <code>indent</code> not have that preference. For example, the default option &#8216;-bbo&#8217; (together with &#8216;--line-length60&#8217; and &#8216;--ignore-newlines&#8217;) makes code look like this: </p>
<pre><code>  if (mask
      &amp;&amp; ((mask[0] == '\0')
          || (mask[1] == '\0'
              &amp;&amp; ((mask[0] == '0') || (mask[0] == '*')))))
</code></pre>
<p> Using the option &#8216;-nbbo&#8217; will make it look like this: </p>
<pre><code>  if (mask &amp;&amp;
      ((mask[0] == '\0') ||
       (mask[1] == '\0' &amp;&amp;
        ((mask[0] == '0') || (mask[0] == '*')))))
</code></pre>
<p> The default &#8216;-hnl&#8217;, however, honours newlines in the input file by giving them the highest possible priority to break lines at. For example, when the input file looks like this: </p>
<pre><code>  if (mask
      &amp;&amp; ((mask[0] == '\0')
      || (mask[1] == '\0' &amp;&amp; ((mask[0] == '0') || (mask[0] == '*')))))
</code></pre>
<p> then using the option &#8216;-hnl&#8217;, or &#8216;--honour-newlines&#8217;, together with the previously mentioned &#8216;-nbbo&#8217; and &#8216;--line-length60&#8217;, will cause the output not to be what is given in the last example but instead will prefer to break at the positions where the code was broken in the input file: </p>
<pre><code>  if (mask
      &amp;&amp; ((mask[0] == '\0')
          || (mask[1] == '\0' &amp;&amp;
              ((mask[0] == '0') || (mask[0] == '*')))))
</code></pre>
<p> The idea behind this option is that lines which are too long, but are already broken up, will not be touched by GNU <code>indent</code>. Really messy code should be run through <code>indent</code> at least once using the &#8216;--ignore-newlines&#8217; option though. </p>
<h2>DISABLING FORMATTING</h2>
<p> Formatting of C code may be disabled for portions of a program by embedding special <i>control comments</i> in the program. To turn off formatting for a section of a program, place the disabling control comment <code>/* *INDENT-OFF* */</code> on a line by itself just before that section. Program text scanned after this control comment is output precisely as input with no modifications until the corresponding enabling comment is scanned on a line by itself. The disabling control comment is <code>/* *INDENT-ON* */</code>, and any text following the comment on the line is also output unformatted. Formatting begins again with the input line following the enabling control comment. </p>
<p> More precisely, <code>indent</code> does not attempt to verify the closing delimiter (<code>*/</code>) for these C comments, and any whitespace on the line is totally transparent. </p>
<p> These control comments also function in their C++ formats, namely <code>// *INDENT-OFF*</code> and <code>// *INDENT-ON*</code>. </p>
<p> It should be noted that the internal state of <code>indent</code> remains unchanged over the course of the unformatted section. Thus, for example, turning off formatting in the middle of a function and continuing it after the end of the function may lead to bizarre results. It is therefore wise to be somewhat modular in selecting code to be left unformatted. </p>
<p> As a historical note, some earlier versions of <code>indent</code> produced error messages beginning with <code>*INDENT**</code>. These versions of <code>indent</code> were written to ignore any input text lines which began with such error messages. I have removed this incestuous feature from GNU <code>indent</code>. </p>
<h2>MISCELLANEOUS OPTIONS</h2>
<p> To find out what version of <code>indent</code> you have, use the command <code>indent -version</code>. This will report the version number of <code>indent</code>, without doing any of the normal processing. </p>
<p> The &#8216;-v&#8217; option can be used to turn on verbose mode. When in verbose mode, <code>indent</code> reports when it splits one line of input into two more more lines of output, and gives some size statistics at completion. </p>
<p> The &#8216;-pmt&#8217; option causes <code>indent</code> to preserve the access and modification times on the output files. Using this option has the advantage that running indent on all source and header files in a project won&#8217;t cause <code>make</code> to rebuild all targets. This option is only available on Operating Systems that have the POSIX <code><a href="/docs/linux/man/2-utime/">utime</a>(2)</code> function. </p>
<h2>BUGS</h2>
<p> Please report any bugs to bug-indent [at] gnu.org. </p>
<p> When <code>indent</code> is run twice on a file, with the same profile, it should <i>never</i> change that file the second time. With the current design of <code>indent</code>, this can not be guaranteed, and it has not been extensively tested. </p>
<p> <code>indent</code> does not understand C. In some cases this leads to the inability to join lines. The result is that running a file through <code>indent</code> is <i>irreversible</i>, even if the used input file was the result of running <code>indent</code> with a given profile (&#8216;.indent.pro&#8217;). </p>
<p> While an attempt was made to get <code>indent</code> working for C++, it will not do a good job on any C++ source except the very simplest. </p>
<p> <code>indent</code> does not look at the given &#8216;--line-length&#8217; option when writing comments to the output file. This results often in comments being put far to the right. In order to prohibit <code>indent</code> from joining a broken line that has a comment at the end, make sure that the comments start on the first line of the break. </p>
<p> <code>indent</code> does not count lines and comments (see the &#8216;-v&#8217; option) when <code>indent</code> is turned off with <code>/* *INDENT-OFF* */</code>. </p>
<p> Comments of the form <code>/*UPPERCASE*/</code> are not treated as comment but as an identifier, causing them to be joined with the next line. This renders comments of this type useless, unless they are embedded in the code to begin with. </p>
<h2>COPYRIGHT</h2>
<p> The following copyright notice applies to the <code>indent</code> program. The copyright and copying permissions for this manual appear near the beginning of &#8216;indent.texinfo&#8217; and &#8216;indent.info&#8217;, and near the end of &#8216;indent.1&#8217;. </p>
<pre><code>Copyright (c) 2001 David Ingamells.
Copyright (c) 1999 Carlo Wood.
Copyright (c) 1995, 1996 Joseph Arceneaux.
Copyright (c) 1989, 1992, 1993, 1994, 1995, 1996 Free Software Foundation
Copyright (c) 1985 Sun Microsystems, Inc.
Copyright (c) 1980 The Regents of the University of California.
Copyright (c) 1976 Board of Trustees of the University of Illinois.
All rights reserved.
Redistribution and use in source and binary forms are permitted
provided that the above copyright notice and this paragraph are
duplicated in all such forms and that any documentation,
advertising materials, and other materials related to such
distribution and use acknowledge that the software was developed
by the University of California, Berkeley, the University of Illinois,
Urbana, and Sun Microsystems, Inc. The name of either University
or Sun Microsystems may not be used to endorse or promote products
derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED ''AS IS'' AND WITHOUT ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
WARRANTIES OF MERCHANTIBILITY AND FITNESS FOR A PARTICULAR
PURPOSE.
</code></pre>
<h2>Options' Cross Key</h2>
<p> Here is a list of options alphabetized by long option, to help you find the corresponding short option. </p>
<pre><code>--blank-lines-after-commas -bc
--blank-lines-after-declarations -bad
--blank-lines-after-procedures -bap
--blank-lines-before-block-comments -bbb
--braces-after-if-line -bl
--braces-after-func-def-line -blf
--brace-indent -bli
--braces-after-struct-decl-line -bls
--braces-on-if-line -br
--braces-on-func-def-line -brf
--braces-on-struct-decl-line -brs
--break-after-boolean-operator -nbbo
--break-before-boolean-operator -bbo
--break-function-decl-args -bfda
--break-function-decl-args-end -bfde
--case-indentation -cli n --case-brace-indentation -cbi n --comment-delimiters-on-blank-lines -cdb
--comment-indentation -c n --continuation-indentation -ci n --continue-at-parentheses -lp
--cuddle-do-while -cdw
--cuddle-else -ce
--declaration-comment-column -cd n --declaration-indentation -di n --dont-break-function-decl-args -nbfda
--dont-break-function-decl-args-end -nbfde
--dont-break-procedure-type -npsl
--dont-cuddle-do-while -ncdw
--dont-cuddle-else -nce
--dont-format-comments -nfca
--dont-format-first-column-comments -nfc1
--dont-line-up-parentheses -nlp
--dont-left-justify-declarations -ndj
--dont-space-special-semicolon -nss
--dont-star-comments -nsc
--else-endif-column -cp n --format-all-comments -fca
--format-first-column-comments -fc1
--gnu-style -gnu
--honour-newlines -hnl
--ignore-newlines -nhnl
--ignore-profile -npro
--indent-label -il n --indent-level -i n --k-and-r-style -kr
--leave-optional-blank-lines -nsob
--leave-preprocessor-space -lps
--left-justify-declarations -dj
--line-comments-indentation -d n --line-length -l n --linux-style -linux
--no-blank-lines-after-commas -nbc
--no-blank-lines-after-declarations -nbad
--no-blank-lines-after-procedures -nbap
--no-blank-lines-before-block-comments -nbbb
--no-comment-delimiters-on-blank-lines -ncdb
--no-space-after-casts -ncs
--no-parameter-indentation -nip
--no-space-after-for -nsaf
--no-space-after-function-call-names -npcs
--no-space-after-if -nsai
--no-space-after-parentheses -nprs
--no-space-after-while -nsaw
--no-tabs -nut
--no-verbosity -nv
--original -orig
--parameter-indentation -ip n --paren-indentation -pi n --preserve-mtime -pmt
--preprocessor-indentation -ppi n --procnames-start-lines -psl
--remove-preprocessor-space -nlps
--space-after-cast -cs
--space-after-for -saf
--space-after-if -sai
--space-after-parentheses -prs
--space-after-procedure-calls -pcs
--space-after-while -saw
--space-special-semicolon -ss
--standard-output -st
--start-left-side-of-comments -sc
--struct-brace-indentation -sbi n --swallow-optional-blank-lines -sob
--tab-size -ts n --use-tabs -ut
--verbose -v
</code></pre>
<h2>RETURN VALUE</h2>
<p> Unknown  </p>
<h2>FILES</h2>
<p> <br />
 </p>
<pre><code>
 $HOME/.indent.pro    holds default options for indent.
</code></pre>
<h2>AUTHORS</h2>
<p> <br />
 Carlo Wood <br />
 Joseph Arceneaux <br />
 Jim Kingdon <br />
 David Ingamells  </p>
<h2>HISTORY</h2>
<p> Derived from the UCB program &quot;indent&quot;.  </p>
<h2>COPYING</h2>
<p> Copyright (C) 1989, 1992, 1993, 1994, 1995, 1996 Free Software Foundation, Inc. Copyright (C) 1995, 1996 Joseph Arceneaux. Copyright (C) 1999 Carlo Wood. Copyright (C) 2001 David Ingamells. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
