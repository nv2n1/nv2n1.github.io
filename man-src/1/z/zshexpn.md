---
title: "zshexpn(1)"
name: "zshexpn"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshexpn/"
description: "zshexpn – zsh expansion and substitution"
---
<h2 class="name">NAME</h2>
<p> zshexpn - zsh expansion and substitution </p>
<h2>DESCRIPTION</h2>
<p> The following types of expansions are performed in the indicated order in five steps: </p>
<dl>
<dd> <p> <i>History Expansion</i> This is performed only in interactive shells. </p>
 </dd>
<dt><i>Alias Expansion</i></dt>
<dd> <p> Aliases are expanded immediately before the command line is parsed as explained under Aliasing in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </p>
 </dd>
<dd> <p> <i>Process Substitution</i> </p>
 </dd>
<dd> <p> <i>Parameter Expansion</i> </p>
 </dd>
<dd> <p> <i>Command Substitution</i> </p>
 </dd>
<dd> <p> <i>Arithmetic Expansion</i> </p>
 </dd>
<dd> <p> <i>Brace Expansion</i> These five are performed in left-to-right fashion. On each argument, any of the five steps that are needed are performed one after the other. Hence, for example, all the parts of parameter expansion are completed before command substitution is started. After these expansions, all unquoted occurrences of the characters `<code>\</code>&#8216;,`<code>&#8216;</code>&#8216; and `<code>&quot;</code>&#8216; are removed. </p>
 </dd>
<dt><i>Filename Expansion</i></dt>
<dd> <p> If the <code>SH_FILE_EXPANSION</code> option is set, the order of expansion is modified for compatibility with <code>sh</code> and <code>ksh</code>. In that case <i>filename expansion</i> is performed immediately after <i>alias expansion</i>, preceding the set of five expansions mentioned above. </p>
 </dd>
<dt><i>Filename Generation</i></dt>
<dd> <p> This expansion, commonly referred to as <code>globbing</code>, is always done last. </p>
 </dd></dl>
<p> The following sections explain the types of expansion in detail. </p>
<h2>HISTORY EXPANSION</h2>
<p> History expansion allows you to use words from previous command lines in the command line you are typing. This simplifies spelling corrections and the repetition of complicated commands or arguments. </p>
<p> Immediately before execution, each command is saved in the history list, the size of which is controlled by the <code>HISTSIZE</code> parameter. The one most recent command is always retained in any case. Each saved command in the history list is called a history <i>event</i> and is assigned a number, beginning with 1 (one) when the shell starts up. The history number that you may see in your prompt (see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)) is the number that is to be assigned to the <i>next</i> command. </p>
<h3>Overview</h3>
<p> A history expansion begins with the first character of the <code>histchars</code> parameter, which is `<code>!</code>&#8216; by default, and may occur anywhere on the command line, including inside double quotes (but not inside single quotes <code>&#8216;...&#8216;</code> or C-style quotes <code>$&#8216;...&#8216;</code> nor when escaped with a backslash). </p>
<p> The first character is followed by an optional event designator (see the section `Event Designators&#8217;) and then an optional word designator (the section `Word Designators&#8217;); if neither of these designators is present, no history expansion occurs. </p>
<p> Input lines containing history expansions are echoed after being expanded, but before any other expansions take place and before the command is executed. It is this expanded form that is recorded as the history event for later references. </p>
<p> History expansions do not nest. </p>
<p> By default, a history reference with no event designator refers to the same event as any preceding history reference on that command line; if it is the only history reference in a command, it refers to the previous command. However, if the option <code>CSH_JUNKIE_HISTORY</code> is set, then every history reference with no event specification <i>always</i> refers to the previous command. </p>
<p> For example, `<code>!</code>&#8216; is the event designator for the previous command, so `<code>!!:1</code>&#8216; always refers to the first word of the previous command, and `<code>!!$</code>&#8216; always refers to the last word of the previous command. With <code>CSH_JUNKIE_HISTORY</code> set, then `<code>!:1</code>&#8216; and `<code>!$</code>&#8216; function in the same manner as `<code>!!:1</code>&#8216; and `<code>!!$</code>&#8216;, respectively. Conversely, if <code>CSH_JUNKIE_HISTORY</code> is unset, then `<code>!:1</code>&#8216; and `<code>!$</code>&#8216; refer to the first and last words, respectively, of the same event referenced by the nearest other history reference preceding them on the current command line, or to the previous command if there is no preceding reference. </p>
<p> The character sequence `<code>^</code><i>foo</i><code>^</code><i>bar</i>&#8216; (where `<code>^</code>&#8216; is actually the second character of the <code>histchars</code> parameter) repeats the last command, replacing the string <i>foo</i> with <i>bar</i>. More precisely, the sequence `<code>^</code><i>foo</i><code>^</code><i>bar</i><code>^</code>&#8216; is synonymous with `<code>!!:s</code><code>^</code><i>foo</i><code>^</code><i>bar</i><code>^</code>&#8216;, hence other modifiers (see the section `Modifiers&#8217;) may follow the final `<code>^</code>&#8216;. In particular, `<code>^</code><i>foo</i><code>^</code><i>bar</i><code>^:G</code>&#8216; performs a global substitution. </p>
<p> If the shell encounters the character sequence `<code>!&quot;</code>&#8216; in the input, the history mechanism is temporarily disabled until the current list (see <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)) is fully parsed. The `<code>!&quot;</code>&#8216; is removed from the input, and any subsequent `<code>!</code>&#8216; characters have no special significance. </p>
<p> A less convenient but more comprehensible form of command history support is provided by the <code>fc</code> builtin.  </p>
<h3>Event Designators</h3>
<p> An event designator is a reference to a command-line entry in the history list. In the list below, remember that the initial <code>`!&#8216;</code> in each item may be changed to another character by setting the <code>histchars</code> parameter. </p>
<dl>
<dd> <p> <code>!</code> Start a history expansion, except when followed by a blank, newline, `<code>=</code>&#8216; or `<code>(</code>&#8216;. If followed immediately by a word designator (see the section `Word Designators&#8217;), this forms a history reference with no event designator (see the section `Overview&#8217;). </p>
 </dd>
<dt><code>!!</code></dt>
<dd> <p> Refer to the previous command. By itself, this expansion repeats the previous command. </p>
 </dd>
<dt><code>!</code><i>n</i></dt>
<dd> <p> Refer to command-line <i>n</i>. </p>
 </dd>
<dt><code>!-</code><i>n</i></dt>
<dd> <p> Refer to the current command-line minus <i>n</i>. </p>
 </dd>
<dt><code>!</code><i>str</i></dt>
<dd> <p> Refer to the most recent command starting with <i>str</i>. </p>
 </dd>
<dt><code>!?</code><i>str</i>[<code>?</code>]</dt>
<dd> <p> Refer to the most recent command containing <i>str</i>. The trailing `<code>?</code>&#8216; is necessary if this reference is to be followed by a modifier or followed by any text that is not to be considered part of <i>str</i>. </p>
 </dd>
<dt><code>!#</code></dt>
<dd> <p> Refer to the current command line typed in so far. The line is treated as if it were complete up to and including the word before the one with the `<code>!#</code>&#8216; reference. </p>
 </dd>
<dt><code>!{</code>...<code>}</code></dt>
<dd> <p> Insulate a history reference from adjacent characters (if necessary). </p>
 </dd></dl>
<h3>Word Designators</h3>
<p> A word designator indicates which word or words of a given command line are to be included in a history reference. A `<code>:</code>&#8216; usually separates the event specification from the word designator. It may be omitted only if the word designator begins with a `<code>^</code>&#8216;, `<code>$</code>&#8216;, `<code>*</code>&#8216;, `<code>-</code>&#8216; or `<code>%</code>&#8216;. Word designators include: </p>
<dl>
<dt><code>0</code></dt>
<dd> <p> The first input word (command). </p>
 </dd>
<dt><i>n</i></dt>
<dd> <p> The <i>n</i>th argument. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> The first argument. That is, <code>1</code>. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> The last argument. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> The word matched by (the most recent) <code>?</code><i>str</i> search. </p>
 </dd>
<dt><i>x</i><code>-</code><i>y</i></dt>
<dd> <p> A range of words; <i>x</i> defaults to <code>0</code>. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> All the arguments, or a null value if there are none. </p>
 </dd>
<dt><i>x</i><code>*</code></dt>
<dd> <p> Abbreviates `<i>x</i><code>-$</code>&#8216;. </p>
 </dd>
<dt><i>x</i><code>-</code></dt>
<dd> <p> Like `<i>x</i><code>*</code>&#8216; but omitting word <code>$</code>. </p>
 </dd></dl>
<p> Note that a `<code>%</code>&#8216; word designator works only when used in one of `<code>!%</code>&#8216;, `<code>!:%</code>&#8216; or `<code>!?</code><i>str</i><code>?:%</code>&#8216;, and only when used after a <code>!?</code> expansion (possibly in an earlier command). Anything else results in an error, although the error may not be the most obvious one.  </p>
<h3>Modifiers</h3>
<p> After the optional word designator, you can add a sequence of one or more of the following modifiers, each preceded by a `<code>:</code>&#8216;. These modifiers also work on the result of <i>filename generation</i> and <i>parameter expansion</i>, except where noted. </p>
<dl>
<dd> <p> <code>a</code> Turn a file name into an absolute path: prepends the current directory, if necessary; remove `<code>.</code>&#8216; path segments; and remove `<code>..</code>&#8216; path segments and the segments that immediately precede them. </p>
 </dd>
<dl>
<dd> <p> This transformation is agnostic about what is in the filesystem, i.e. is on the logical, not the physical directory. It takes place in the same manner as when changing directories when neither of the options <code>CHASE_DOTS</code> or <code>CHASE_LINKS</code> is set. For example, `<code>/before/here/../after</code>&#8216; is always transformed to `<code>/before/after</code>&#8216;, regardless of whether `<code>/before/here</code>&#8216; exists or what kind of object (dir, file, symlink, etc.) it is. </p>
 </dd></dl>
<dt><code>A</code></dt>
<dd> <p> Turn a file name into an absolute path as the `<code>a</code>&#8216; modifier does, and <i>then</i> pass the result through the <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code> library function to resolve symbolic links. </p>
 </dd>
<dl>
<dd> <p> Note: on systems that do not have a <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code> library function, symbolic links are not resolved, so on those systems `<code>a</code>&#8216; and `<code>A</code>&#8216; are equivalent. </p>
<p> Note: <code>foo:A</code> and <code>realpath(foo)</code> are different on some inputs. For <code>realpath(foo)</code> semantics, see the `<code>P</code>` modifier. </p>
 </dd></dl>
<dt><code>c</code></dt>
<dd> <p> Resolve a command name into an absolute path by searching the command path given by the <code>PATH</code> variable. This does not work for commands containing directory parts. Note also that this does not usually work as a glob qualifier unless a file of the same name is found in the current directory. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Remove all but the part of the filename extension following the `<code>.</code>&#8216;; see the definition of the filename extension in the description of the <code>r</code> modifier below. Note that according to that definition the result will be empty if the string ends with a `<code>.</code>&#8216;. </p>
 </dd>
<dt><code>h</code> [ <i>digits</i> ]</dt>
<dd> <p> Remove a trailing pathname component, shortening the path by one directory level: this is the `head&#8217; of the pathname. This works like `<code>dirname</code>&#8216;. If the <code>h</code> is followed immediately (with no spaces or other separator) by any number of decimal digits, and the value of the resulting number is non-zero, that number of leading components is preserved instead of the final component being removed. In an absolute path the leading `<code>/</code>&#8216; is the first component, so, for example, if <code>var=/my/path/to/something</code>, then <code>${var:h3}</code> substitutes <code>/my/path</code>. Consecutive `/&#8216;s are treated the same as a single `/&#8216;. In parameter substitution, digits may only be used if the expression is in braces, so for example the short form substitution <code>$var:h2</code> is treated as <code>${var:h}2</code>, not as <code>${var:h2}</code>. No restriction applies to the use of digits in history substitution or globbing qualifiers. If more components are requested than are present, the entire path is substituted (so this does not trigger a `failed modifier&#8217; error in history expansion). </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> Convert the words to all lowercase. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Print the new command but do not execute it. Only works with history expansion. </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> Turn a file name into an absolute path, like <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code>. The resulting path will be absolute, have neither `<code>.</code>&#8216; nor `<code>..</code>&#8216; components, and refer to the same directory entry as the input filename. </p>
 </dd>
<dl>
<dd> <p> Unlike <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code>, non-existent trailing components are permitted and preserved. </p>
 </dd></dl>
<dt><code>q</code></dt>
<dd> <p> Quote the substituted words, escaping further substitutions. Works with history expansion and parameter expansion, though for parameters it is only useful if the resulting text is to be re-evaluated such as by <code>eval</code>. </p>
 </dd>
<dt><code>Q</code></dt>
<dd> <p> Remove one level of quotes from the substituted words. </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Remove a filename extension leaving the root name. Strings with no filename extension are not altered. A filename extension is a `<code>.</code>&#8216; followed by any number of characters (including zero) that are neither `<code>.</code>&#8216; nor `<code>/</code>&#8216; and that continue to the end of the string. For example, the extension of `<code>foo.orig.c</code>&#8216; is `<code>.c</code>&#8216;, and `<code>dir.c/foo</code>&#8216; has no extension. </p>
 </dd>
<dt><code>s/</code><i>l</i><code>/</code><i>r</i>[<code>/</code>]</dt>
<dd> <p> Substitute <i>r</i> for <i>l</i> as described below. The substitution is done only for the first string that matches <i>l</i>. For arrays and for filename generation, this applies to each word of the expanded text. See below for further notes on substitutions. </p>
 </dd>
<dl>
<dd> <p> The forms `<code>gs/</code><i>l</i><code>/</code><i>r</i>&#8216; and `<code>s/</code><i>l</i><code>/</code><i>r</i><code>/:G</code>&#8216; perform global substitution, i.e. substitute every occurrence of <i>r</i> for <i>l</i>. Note that the <code>g</code> or <code>:G</code> must appear in exactly the position shown. </p>
<p> See further notes on this form of substitution below. </p>
 </dd></dl>
<dt><code>&amp;</code></dt>
<dd> <p> Repeat the previous <code>s</code> substitution. Like <code>s</code>, may be preceded immediately by a <code>g</code>. In parameter expansion the <code>&amp;</code> must appear inside braces, and in filename generation it must be quoted with a backslash. </p>
 </dd>
<dt><code>t</code> [ <i>digits</i> ]</dt>
<dd> <p> Remove all leading pathname components, leaving the final component (tail). This works like `<code>basename</code>&#8216;. Any trailing slashes are first removed. Decimal digits are handled as described above for (h), but in this case that number of trailing components is preserved instead of the default 1; 0 is treated the same as 1. </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> Convert the words to all uppercase. </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> Like <code>q</code>, but break into words at whitespace. Does not work with parameter expansion. </p>
 </dd></dl>
<p> The <code>s/</code><i>l</i><code>/</code><i>r</i><code>/</code> substitution works as follows. By default the left-hand side of substitutions are not patterns, but character strings. Any character can be used as the delimiter in place of `<code>/</code>&#8216;. A backslash quotes the delimiter character. The character `<code>&amp;</code>&#8216;, in the right-hand-side <i>r</i>, is replaced by the text from the left-hand-side <i>l</i>. The `<code>&amp;</code>&#8216; can be quoted with a backslash. A null <i>l</i> uses the previous string either from the previous <i>l</i> or from the contextual scan string <i>s</i> from `<code>!?</code><i>s</i>&#8216;. You can omit the rightmost delimiter if a newline immediately follows <i>r</i>; the rightmost `<code>?</code>&#8216; in a context scan can similarly be omitted. Note the same record of the last <i>l</i> and <i>r</i> is maintained across all forms of expansion. </p>
<p> Note that if a `<code>&amp;</code>&#8216; is used within glob qualifiers an extra backslash is needed as a <code>&amp;</code> is a special character in this case. </p>
<p> Also note that the order of expansions affects the interpretation of <i>l</i> and <i>r</i>. When used in a history expansion, which occurs before any other expansions, <i>l</i> and <i>r</i> are treated as literal strings (except as explained for <code>HIST_SUBST_PATTERN</code> below). When used in parameter expansion, the replacement of <i>r</i> into the parameter&#8217;s value is done first, and then any additional process, parameter, command, arithmetic, or brace references are applied, which may evaluate those substitutions and expansions more than once if <i>l</i> appears more than once in the starting value. When used in a glob qualifier, any substitutions or expansions are performed once at the time the qualifier is parsed, even before the `<code>:s</code>&#8216; expression itself is divided into <i>l</i> and <i>r</i> sides. </p>
<p> If the option <code>HIST_SUBST_PATTERN</code> is set, <i>l</i> is treated as a pattern of the usual form described in the section FILENAME GENERATION below. This can be used in all the places where modifiers are available; note, however, that in globbing qualifiers parameter substitution has already taken place, so parameters in the replacement string should be quoted to ensure they are replaced at the correct time. Note also that complicated patterns used in globbing qualifiers may need the extended glob qualifier notation <code>(#q:s/</code><i>...</i><code>/</code><i>...</i><code>/)</code> in order for the shell to recognize the expression as a glob qualifier. Further, note that bad patterns in the substitution are not subject to the <code>NO_BAD_PATTERN</code> option so will cause an error. </p>
<p> When <code>HIST_SUBST_PATTERN</code> is set, <i>l</i> may start with a <code>#</code> to indicate that the pattern must match at the start of the string to be substituted, and a <code>%</code> may appear at the start or after an <code>#</code> to indicate that the pattern must match at the end of the string to be substituted. The <code>%</code> or <code>#</code> may be quoted with two backslashes. </p>
<p> For example, the following piece of filename generation code with the <code>EXTENDED_GLOB</code> option: </p>
<dl>
<dd> <pre><code>
 print -r -- *.c(#q:s/#%(#b)s(*).c/'S${match[1]}.C'/) 
</code></pre>
 </dd></dl>
<p> takes the expansion of <code>*.c</code> and applies the glob qualifiers in the <code>(#q</code><i>...</i><code>)</code> expression, which consists of a substitution modifier anchored to the start and end of each word (<code>#%</code>). This turns on backreferences (<code>(#b)</code>), so that the parenthesised subexpression is available in the replacement string as <code>${match[1]}</code>. The replacement string is quoted so that the parameter is not substituted before the start of filename generation. </p>
<p> The following <code>f</code>, <code>F</code>, <code>w</code> and <code>W</code> modifiers work only with parameter expansion and filename generation. They are listed here to provide a single point of reference for all modifiers. </p>
<dl>
<dd> <p> <code>f</code> Repeats the immediately (without a colon) following modifier until the resulting word doesn&#8217;t change any more. </p>
 </dd>
<dt><code>F:</code><i>expr</i><code>:</code></dt>
<dd> <p> Like <code>f</code>, but repeats only <i>n</i> times if the expression <i>expr</i> evaluates to <i>n</i>. Any character can be used instead of the `<code>:</code>&#8216;; if `<code>(</code>&#8216;, `<code>[</code>&#8216;, or `<code>{</code>&#8216; is used as the opening delimiter, the closing delimiter should be &#8216;<code>)</code>&#8216;, `<code>]</code>&#8216;, or `<code>}</code>&#8216;, respectively. </p>
 </dd>
<dt><code>w</code></dt>
<dd> <p> Makes the immediately following modifier work on each word in the string. </p>
 </dd>
<dt><code>W:</code><i>sep</i><code>:</code></dt>
<dd> <p> Like <code>w</code> but words are considered to be the parts of the string that are separated by <i>sep</i>. Any character can be used instead of the `<code>:</code>&#8216;; opening parentheses are handled specially, see above. </p>
 </dd></dl>
<h2>PROCESS SUBSTITUTION</h2>
<p> Each part of a command argument that takes the form `<code>&lt;(</code><i>list</i><code>)</code>&#8216;, `<code>&gt;(</code><i>list</i><code>)</code>&#8216; or `<code>=(</code><i>list</i><code>)</code>&#8216; is subject to process substitution. The expression may be preceded or followed by other strings except that, to prevent clashes with commonly occurring strings and patterns, the last form must occur at the start of a command argument, and the forms are only expanded when first parsing command or assignment arguments. Process substitutions may be used following redirection operators; in this case, the substitution must appear with no trailing string. </p>
<p> Note that `<code>&lt;&lt;(</code><i>list</i><code>)</code>&#8216; is not a special syntax; it is equivalent to `<code>&lt; &lt;(</code><i>list</i><code>)</code>&#8216;, redirecting standard input from the result of process substitution. Hence all the following documentation applies. The second form (with the space) is recommended for clarity. </p>
<p> In the case of the <code>&lt;</code> or <code>&gt;</code> forms, the shell runs the commands in <i>list</i> as a subprocess of the job executing the shell command line. If the system supports the <code>/dev/fd</code> mechanism, the command argument is the name of the device file corresponding to a file descriptor; otherwise, if the system supports named pipes (FIFOs), the command argument will be a named pipe. If the form with <code>&gt;</code> is selected then writing on this special file will provide input for <i>list</i>. If <code>&lt;</code> is used, then the file passed as an argument will be connected to the output of the <i>list</i> process. For example, </p>
<dl>
<dd> <pre><code>
 paste &lt;(cut -f1  file1  ) &lt;(cut -f3  file2  ) |
tee &gt;(  process1  ) &gt;(  process2  ) &gt;/dev/null 
</code></pre>
 </dd></dl>
<p> cuts fields 1 and 3 from the files <i>file1</i> and <i>file2</i> respectively, pastes the results together, and sends it to the processes <i>process1</i> and <i>process2</i>. </p>
<p> If <code>=(</code><i>...</i><code>)</code> is used instead of <code>&lt;(</code><i>...</i><code>)</code>, then the file passed as an argument will be the name of a temporary file containing the output of the <i>list</i> process. This may be used instead of the <code>&lt;</code> form for a program that expects to lseek (see <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2)) on the input file. </p>
<p> There is an optimisation for substitutions of the form <code>=(&lt;&lt;&lt;</code><i>arg</i><code>)</code>, where <i>arg</i> is a single-word argument to the here-string redirection <code>&lt;&lt;&lt;</code>. This form produces a file name containing the value of <i>arg</i> after any substitutions have been performed. This is handled entirely within the current shell. This is effectively the reverse of the special form <code>$(&lt;</code><i>arg</i><code>)</code> which treats <i>arg</i> as a file name and replaces it with the file&#8217;s contents. </p>
<p> The <code>=</code> form is useful as both the <code>/dev/fd</code> and the named pipe implementation of <code>&lt;(</code><i>...</i><code>)</code> have drawbacks. In the former case, some programmes may automatically close the file descriptor in question before examining the file on the command line, particularly if this is necessary for security reasons such as when the programme is running setuid. In the second case, if the programme does not actually open the file, the subshell attempting to read from or write to the pipe will (in a typical implementation, different operating systems may have different behaviour) block for ever and have to be killed explicitly. In both cases, the shell actually supplies the information using a pipe, so that programmes that expect to lseek (see <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2)) on the file will not work. </p>
<p> Also note that the previous example can be more compactly and efficiently written (provided the <code>MULTIOS</code> option is set) as: </p>
<dl>
<dd> <pre><code>
 paste &lt;(cut -f1  file1  ) &lt;(cut -f3  file2  )  \
 &gt; &gt;(  process1  ) &gt; &gt;(  process2  ) 
</code></pre>
 </dd></dl>
<p> The shell uses pipes instead of FIFOs to implement the latter two process substitutions in the above example. </p>
<p> There is an additional problem with <code>&gt;(</code><i>process</i><code>)</code>; when this is attached to an external command, the parent shell does not wait for <i>process</i> to finish and hence an immediately following command cannot rely on the results being complete. The problem and solution are the same as described in the section <i>MULTIOS</i> in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). Hence in a simplified version of the example above: </p>
<dl>
<dd> <pre><code>
 paste &lt;(cut -f1  file1  ) &lt;(cut -f3  file2  )  &gt; &gt;(  process  ) 
</code></pre>
 </dd></dl>
<p> (note that no <code>MULTIOS</code> are involved), <i>process</i> will be run asynchronously as far as the parent shell is concerned. The workaround is: </p>
<dl>
<dd> <pre><code>
 { paste &lt;(cut -f1  file1  ) &lt;(cut -f3  file2  ) }  &gt; &gt;(  process  ) 
</code></pre>
 </dd></dl>
<p> The extra processes here are spawned from the parent shell which will wait for their completion. </p>
<p> Another problem arises any time a job with a substitution that requires a temporary file is disowned by the shell, including the case where `<code>&amp;!</code>&#8216; or `<code>&amp;|</code>&#8216; appears at the end of a command containing a substitution. In that case the temporary file will not be cleaned up as the shell no longer has any memory of the job. A workaround is to use a subshell, for example, </p>
<dl>
<dd> <pre><code>
 (mycmd =(myoutput)) &amp;! 
</code></pre>
 </dd></dl>
<p> as the forked subshell will wait for the command to finish then remove the temporary file. </p>
<p> A general workaround to ensure a process substitution endures for an appropriate length of time is to pass it as a parameter to an anonymous shell function (a piece of shell code that is run immediately with function scope). For example, this code: </p>
<dl>
<dd> <pre><code>
 () {
   print File $1:
   cat $1
} =(print This be the verse) 
</code></pre>
 </dd></dl>
<p> outputs something resembling the following </p>
<dl>
<dd> <pre><code>
 File /tmp/zsh6nU0kS:
This be the verse 
</code></pre>
 </dd></dl>
<p> The temporary file created by the process substitution will be deleted when the function exits. </p>
<h2>PARAMETER EXPANSION</h2>
<p> The character `<code>$</code>&#8216; is used to introduce parameter expansions. See <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1) for a description of parameters, including arrays, associative arrays, and subscript notation to access individual array elements. </p>
<p> Note in particular the fact that words of unquoted parameters are not automatically split on whitespace unless the option <code>SH_WORD_SPLIT</code> is set; see references to this option below for more details. This is an important difference from other shells. However, as in other shells, null words are elided from unquoted parameters&#8217; expansions. </p>
<p> With default options, after the assignments: </p>
<dl>
<dd> <pre><code>
 array=(&quot;first word&quot; &quot;&quot; &quot;third word&quot;)
scalar=&quot;only word&quot; 
</code></pre>
 </dd></dl>
<p> then <code>$array</code> substitutes two words, `<code>first word</code>&#8216; and `<code>third word</code>&#8216;, and <code>$scalar</code> substitutes a single word `<code>only word</code>&#8216;. Note that second element of <code>array</code> was elided. Scalar parameters can be elided too if their value is null (empty). To avoid elision, use quoting as follows: <code>&quot;$scalar&quot;</code> for scalars and <code>&quot;${array[@]}&quot;</code> or <code>&quot;${(@)array}&quot;</code> for arrays. (The last two forms are equivalent.) </p>
<p> Parameter expansions can involve <i>flags</i>, as in `<code>${(@kv)aliases}</code>&#8216;, and other operators, such as `<code>${PREFIX:-&quot;/usr/local&quot;}</code>&#8216;. Parameter expansions can also be nested. These topics will be introduced below. The full rules are complicated and are noted at the end. </p>
<p> In the expansions discussed below that require a pattern, the form of the pattern is the same as that used for filename generation; see the section `Filename Generation&#8217;. Note that these patterns, along with the replacement text of any substitutions, are themselves subject to parameter expansion, command substitution, and arithmetic expansion. In addition to the following operations, the colon modifiers described in the section `Modifiers&#8217; in the section `History Expansion&#8217; can be applied: for example, <code>${i:s/foo/bar/}</code> performs string substitution on the expansion of parameter <code>$i</code>. </p>
<p> In the following descriptions, `<i>word</i>&#8216; refers to a single word substituted on the command line, not necessarily a space delimited word. </p>
<dl>
<dd> <p> <code>${</code><i>name</i><code>}</code> The value, if any, of the parameter <i>name</i> is substituted. The braces are required if the expansion is to be followed by a letter, digit, or underscore that is not to be interpreted as part of <i>name</i>. In addition, more complicated forms of substitution usually require the braces to be present; exceptions, which only apply if the option <code>KSH_ARRAYS</code> is not set, are a single subscript or any colon modifiers appearing after the name, or any of the characters `<code>^</code>&#8216;, `<code>=</code>&#8216;, `<code>~</code>&#8216;, `<code>#</code>&#8216; or `<code>+</code>&#8216; appearing before the name, all of which work with or without braces. </p>
 </dd>
<dl>
<dd> <p> If <i>name</i> is an array parameter, and the <code>KSH_ARRAYS</code> option is not set, then the value of each element of <i>name</i> is substituted, one element per word. Otherwise, the expansion results in one word only; with <code>KSH_ARRAYS</code>, this is the first element of an array. No field splitting is done on the result unless the <code>SH_WORD_SPLIT</code> option is set. See also the flags <code>=</code> and <code>s:</code><i>string</i><code>:</code>. </p>
 </dd></dl>
<dt><code>${+</code><i>name</i><code>}</code></dt>
<dd> <p> If <i>name</i> is the name of a set parameter `<code>1</code>&#8216; is substituted, otherwise `<code>0</code>&#8216; is substituted. </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>-</code><i>word</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:-</code><i>word</i><code>}</code> If <i>name</i> is set, or in the second form is non-null, then substitute its value; otherwise substitute <i>word</i>. In the second form <i>name</i> may be omitted, in which case <i>word</i> is always substituted. </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>+</code><i>word</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:+</code><i>word</i><code>}</code> If <i>name</i> is set, or in the second form is non-null, then substitute <i>word</i>; otherwise substitute nothing. </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>=</code><i>word</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:=</code><i>word</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>::=</code><i>word</i><code>}</code> In the first form, if <i>name</i> is unset then set it to <i>word</i>; in the second form, if <i>name</i> is unset or null then set it to <i>word</i>; and in the third form, unconditionally set <i>name</i> to <i>word</i>. In all forms, the value of the parameter is then substituted. </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>?</code><i>word</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:?</code><i>word</i><code>}</code> In the first form, if <i>name</i> is set, or in the second form if <i>name</i> is both set and non-null, then substitute its value; otherwise, print <i>word</i> and exit from the shell. Interactive shells instead return to the prompt. If <i>word</i> is omitted, then a standard message is printed. </p>
 </dd></dl>
<p> In any of the above expressions that test a variable and substitute an alternate <i>word</i>, note that you can use standard shell quoting in the <i>word</i> value to selectively override the splitting done by the <code>SH_WORD_SPLIT</code> option and the <code>=</code> flag, but not splitting by the <code>s:</code><i>string</i><code>:</code> flag. </p>
<p> In the following expressions, when <i>name</i> is an array and the substitution is not quoted, or if the `<code>(@)</code>&#8216; flag or the <i>name</i><code>[@]</code> syntax is used, matching and replacement is performed on each array element separately. </p>
<dl>
<dd> <p> <code>${</code><i>name</i><code>#</code><i>pattern</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>##</code><i>pattern</i><code>}</code> If the <i>pattern</i> matches the beginning of the value of <i>name</i>, then substitute the value of <i>name</i> with the matched portion deleted; otherwise, just substitute the value of <i>name</i>. In the first form, the smallest matching pattern is preferred; in the second form, the largest matching pattern is preferred. </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>%</code><i>pattern</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>%%</code><i>pattern</i><code>}</code> If the <i>pattern</i> matches the end of the value of <i>name</i>, then substitute the value of <i>name</i> with the matched portion deleted; otherwise, just substitute the value of <i>name</i>. In the first form, the smallest matching pattern is preferred; in the second form, the largest matching pattern is preferred. </p>
 </dd>
<dt><code>${</code><i>name</i><code>:#</code><i>pattern</i><code>}</code></dt>
<dd> <p> If the <i>pattern</i> matches the value of <i>name</i>, then substitute the empty string; otherwise, just substitute the value of <i>name</i>. If <i>name</i> is an array the matching array elements are removed (use the `<code>(M)</code>&#8216; flag to remove the non-matched elements). </p>
 </dd>
<dt><code>${</code><i>name</i><code>:|</code><i>arrayname</i><code>}</code></dt>
<dd> <p> If <i>arrayname</i> is the name (N.B., not contents) of an array variable, then any elements contained in <i>arrayname</i> are removed from the substitution of <i>name</i>. If the substitution is scalar, either because <i>name</i> is a scalar variable or the expression is quoted, the elements of <i>arrayname</i> are instead tested against the entire expression. </p>
 </dd>
<dt><code>${</code><i>name</i><code>:*</code><i>arrayname</i><code>}</code></dt>
<dd> <p> Similar to the preceding substitution, but in the opposite sense, so that entries present in both the original substitution and as elements of <i>arrayname</i> are retained and others removed. </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:^</code><i>arrayname</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:^^</code><i>arrayname</i><code>}</code> Zips two arrays, such that the output array is twice as long as the shortest (longest for `<code>:^^</code>&#8216;) of <code>name</code> and <code>arrayname</code>, with the elements alternatingly being picked from them. For `<code>:^</code>&#8216;, if one of the input arrays is longer, the output will stop when the end of the shorter array is reached. Thus, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>
 a=(1 2 3 4); b=(a b); print ${a:^b} 
</code></pre>
 </dd></dl>
<p> will output `<code>1 a 2 b</code>&#8216;. For `<code>:^^</code>&#8216;, then the input is repeated until all of the longer array has been used up and the above will output `<code>1 a 2 b 3 a 4 b</code>&#8216;. </p>
<p> Either or both inputs may be a scalar, they will be treated as an array of length 1 with the scalar as the only element. If either array is empty, the other array is output with no extra elements inserted. </p>
<p> Currently the following code will output `<code>a b</code>&#8216; and `<code>1</code>&#8216; as two separate elements, which can be unexpected. The second print provides a workaround which should continue to work if this is changed. </p>
<dl>
<dd> <pre><code>
 a=(a b); b=(1 2); print -l &quot;${a:^b}&quot;; print -l &quot;${${a:^b}}&quot; 
</code></pre>
 </dd></dl>
</dl>
<dd> <p> <code>${</code><i>name</i><code>:</code><i>offset</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:</code><i>offset</i><code>:</code><i>length</i><code>}</code> This syntax gives effects similar to parameter subscripting in the form <code>$</code><i>name</i><code>[</code><i>start</i><code>,</code><i>end</i><code>]</code>, but is compatible with other shells; note that both <i>offset</i> and <i>length</i> are interpreted differently from the components of a subscript. </p>
 </dd>
<dl>
<dd> <p> If <i>offset</i> is non-negative, then if the variable <i>name</i> is a scalar substitute the contents starting <i>offset</i> characters from the first character of the string, and if <i>name</i> is an array substitute elements starting <i>offset</i> elements from the first element. If <i>length</i> is given, substitute that many characters or elements, otherwise the entire rest of the scalar or array. </p>
<p> A positive <i>offset</i> is always treated as the offset of a character or element in <i>name</i> from the first character or element of the array (this is different from native zsh subscript notation). Hence 0 refers to the first character or element regardless of the setting of the option <code>KSH_ARRAYS</code>. </p>
<p> A negative offset counts backwards from the end of the scalar or array, so that -1 corresponds to the last character or element, and so on. </p>
<p> When positive, <i>length</i> counts from the <i>offset</i> position toward the end of the scalar or array. When negative, <i>length</i> counts back from the end. If this results in a position smaller than <i>offset</i>, a diagnostic is printed and nothing is substituted. </p>
<p> The option <code>MULTIBYTE</code> is obeyed, i.e. the offset and length count multibyte characters where appropriate. </p>
<p> <i>offset</i> and <i>length</i> undergo the same set of shell substitutions as for scalar assignment; in addition, they are then subject to arithmetic evaluation. Hence, for example </p>
 </dd>
<dl>
<dd> <pre><code>
 print ${foo:3}
print ${foo: 1 + 2}
print ${foo:$(( 1 + 2))}
print ${foo:$(echo 1 + 2)} 
</code></pre>
 </dd></dl>
<p> all have the same effect, extracting the string starting at the fourth character of <code>$foo</code> if the substitution would otherwise return a scalar, or the array starting at the fourth element if <code>$foo</code> would return an array. Note that with the option <code>KSH_ARRAYS</code> <code>$foo</code> always returns a scalar (regardless of the use of the offset syntax) and a form such as <code>${foo[*]:3}</code> is required to extract elements of an array named <code>foo</code>. </p>
<p> If <i>offset</i> is negative, the <code>-</code> may not appear immediately after the <code>:</code> as this indicates the <code>${</code><i>name</i><code>:-</code><i>word</i><code>}</code> form of substitution. Instead, a space may be inserted before the <code>-</code>. Furthermore, neither <i>offset</i> nor <i>length</i> may begin with an alphabetic character or <code>&amp;</code> as these are used to indicate history-style modifiers. To substitute a value from a variable, the recommended approach is to precede it with a <code>$</code> as this signifies the intention (parameter substitution can easily be rendered unreadable); however, as arithmetic substitution is performed, the expression <code>${var: offs}</code> does work, retrieving the offset from <code>$offs</code>. </p>
<p> For further compatibility with other shells there is a special case for array offset 0. This usually accesses the first element of the array. However, if the substitution refers to the positional parameter array, e.g. <code>$@</code> or <code>$*</code>, then offset 0 instead refers to <code>$0</code>, offset 1 refers to <code>$1</code>, and so on. In other words, the positional parameter array is effectively extended by prepending <code>$0</code>. Hence <code>${*:0:1}</code> substitutes <code>$0</code> and <code>${*:1:1}</code> substitutes <code>$1</code>. </dl>
 </p>
<dd> <p> <code>${</code><i>name</i><code>/</code><i>pattern</i><code>/</code><i>repl</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>//</code><i>pattern</i><code>/</code><i>repl</i><code>}</code> </p>
 </dd>
<dd> <p> <code>${</code><i>name</i><code>:/</code><i>pattern</i><code>/</code><i>repl</i><code>}</code> Replace the longest possible match of <i>pattern</i> in the expansion of parameter <i>name</i> by string <i>repl</i>. The first form replaces just the first occurrence, the second form all occurrences, and the third form replaces only if <i>pattern</i> matches the entire string. Both <i>pattern</i> and <i>repl</i> are subject to double-quoted substitution, so that expressions like <code>${name/$opat/$npat}</code> will work, but obey the usual rule that pattern characters in <code>$opat</code> are not treated specially unless either the option <code>GLOB_SUBST</code> is set, or <code>$opat</code> is instead substituted as <code>${~opat}</code>. </p>
 </dd>
<dl>
<dd> <p> The <i>pattern</i> may begin with a `<code>#</code>&#8216;, in which case the <i>pattern</i> must match at the start of the string, or `<code>%</code>&#8216;, in which case it must match at the end of the string, or `<code>#%</code>&#8216; in which case the <i>pattern</i> must match the entire string. The <i>repl</i> may be an empty string, in which case the final `<code>/</code>&#8216; may also be omitted. To quote the final `<code>/</code>&#8216; in other cases it should be preceded by a single backslash; this is not necessary if the `<code>/</code>&#8216; occurs inside a substituted parameter. Note also that the `<code>#</code>&#8216;, `<code>%</code>&#8216; and `<code>#%</code> are not active if they occur inside a substituted parameter, even at the start. </p>
<p> If, after quoting rules apply, <code>${</code><i>name</i><code>}</code> expands to an array, the replacements act on each element individually. Note also the effect of the <code>I</code> and <code>S</code> parameter expansion flags below; however, the flags <code>M</code>, <code>R</code>, <code>B</code>, <code>E</code> and <code>N</code> are not useful. </p>
<p> For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 foo=&quot;twinkle twinkle little star&quot; sub=&quot;t*e&quot; rep=&quot;spy&quot;
print ${foo//${~sub}/$rep}
print ${(S)foo//${~sub}/$rep} 
</code></pre>
 </dd></dl>
<p> Here, the `<code>~</code>&#8216; ensures that the text of <code>$sub</code> is treated as a pattern rather than a plain string. In the first case, the longest match for <code>t*e</code> is substituted and the result is `<code>spy star</code>&#8216;, while in the second case, the shortest matches are taken and the result is `<code>spy spy lispy star</code>&#8216;. </dl>
 </p>
<dt><code>${#</code><i>spec</i><code>}</code></dt>
<dd> <p> If <i>spec</i> is one of the above substitutions, substitute the length in characters of the result instead of the result itself. If <i>spec</i> is an array expression, substitute the number of elements of the result. This has the side-effect that joining is skipped even in quoted forms, which may affect other sub-expressions in <i>spec</i>. Note that `<code>^</code>&#8216;, `<code>=</code>&#8216;, and `<code>~</code>&#8216;, below, must appear to the left of `<code>#</code>&#8216; when these forms are combined. </p>
 </dd>
<dl>
<dd> <p> If the option <code>POSIX_IDENTIFIERS</code> is not set, and <i>spec</i> is a simple name, then the braces are optional; this is true even for special parameters so e.g. <code>$#-</code> and <code>$#*</code> take the length of the string <code>$-</code> and the array <code>$*</code> respectively. If <code>POSIX_IDENTIFIERS</code> is set, then braces are required for the <code>#</code> to be treated in this fashion. </p>
 </dd></dl>
<dt><code>${^</code><i>spec</i><code>}</code></dt>
<dd> <p> Turn on the <code>RC_EXPAND_PARAM</code> option for the evaluation of <i>spec</i>; if the `<code>^</code>&#8216; is doubled, turn it off. When this option is set, array expansions of the form <i>foo</i><code>${</code><i>xx</i><code>}</code><i>bar</i>, where the parameter <i>xx</i> is set to <code>(</code><i>a b c</i><code>)</code>, are substituted with `<i>fooabar foobbar foocbar</i>&#8216; instead of the default `<i>fooa b cbar</i>&#8216;. Note that an empty array will therefore cause all arguments to be removed. </p>
 </dd>
<dl>
<dd> <p> Internally, each such expansion is converted into the equivalent list for brace expansion. E.g., <code>${^var}</code> becomes <code>{$var[1],$var[2],</code>...<code>}</code>, and is processed as described in the section `Brace Expansion&#8217; below: note, however, the expansion happens immediately, with any explicit brace expansion happening later. If word splitting is also in effect the <code>$var[</code><i>N</i><code>]</code> may themselves be split into different list elements. </p>
 </dd></dl>
<dt><code>${=</code><i>spec</i><code>}</code></dt>
<dd> <p> Perform word splitting using the rules for <code>SH_WORD_SPLIT</code> during the evaluation of <i>spec</i>, but regardless of whether the parameter appears in double quotes; if the `<code>=</code>&#8216; is doubled, turn it off. This forces parameter expansions to be split into separate words before substitution, using <code>IFS</code> as a delimiter. This is done by default in most other shells. </p>
 </dd>
<dl>
<dd> <p> Note that splitting is applied to <i>word</i> in the assignment forms of <i>spec</i> <i>before</i> the assignment to <i>name</i> is performed. This affects the result of array assignments with the <code>A</code> flag. </p>
 </dd></dl>
<dt><code>${~</code><i>spec</i><code>}</code></dt>
<dd> <p> Turn on the <code>GLOB_SUBST</code> option for the evaluation of <i>spec</i>; if the `<code>~</code>&#8216; is doubled, turn it off. When this option is set, the string resulting from the expansion will be interpreted as a pattern anywhere that is possible, such as in filename expansion and filename generation and pattern-matching contexts like the right hand side of the `<code>=</code>&#8216; and `<code>!=</code>&#8216; operators in conditions. </p>
 </dd>
<dl>
<dd> <p> In nested substitutions, note that the effect of the <code>~</code> applies to the result of the current level of substitution. A surrounding pattern operation on the result may cancel it. Hence, for example, if the parameter <code>foo</code> is set to <code>*</code>, <code>${~foo//\*/*.c}</code> is substituted by the pattern <code>*.c</code>, which may be expanded by filename generation, but <code>${${~foo}//\*/*.c}</code> substitutes to the string <code>*.c</code>, which will not be further expanded. </p>
 </dd></dl>
</dl>
<p> If a <code>${</code>...<code>}</code> type parameter expression or a <code>$(</code>...<code>)</code> type command substitution is used in place of <i>name</i> above, it is expanded first and the result is used as if it were the value of <i>name</i>. Thus it is possible to perform nested operations: <code>${${foo#head}%tail}</code> substitutes the value of <code>$foo</code> with both `<code>head</code>&#8216; and `<code>tail</code>&#8216; deleted. The form with <code>$(</code>...<code>)</code> is often useful in combination with the flags described next; see the examples below. Each <i>name</i> or nested <code>${</code>...<code>}</code> in a parameter expansion may also be followed by a subscript expression as described in <i>Array Parameters</i> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<p> Note that double quotes may appear around nested expressions, in which case only the part inside is treated as quoted; for example, <code>${(f)&quot;$(foo)&quot;}</code> quotes the result of <code>$(foo)</code>, but the flag `<code>(f)</code>&#8216; (see below) is applied using the rules for unquoted expansions. Note further that quotes are themselves nested in this context; for example, in <code>&quot;${(@f)&quot;$(foo)&quot;}&quot;</code>, there are two sets of quotes, one surrounding the whole expression, the other (redundant) surrounding the <code>$(foo)</code> as before. </p>
<h3>Parameter Expansion Flags</h3>
<p> If the opening brace is directly followed by an opening parenthesis, the string up to the matching closing parenthesis will be taken as a list of flags. In cases where repeating a flag is meaningful, the repetitions need not be consecutive; for example, `(<code>q%q%q</code>)&#8216; means the same thing as the more readable `(<code>%%qqq</code>)&#8216;. The following flags are supported: </p>
<dl>
<dd> <p> <code>#</code> Evaluate the resulting words as numeric expressions and output the characters corresponding to the resulting integer. Note that this form is entirely distinct from use of the <code>#</code> without parentheses. </p>
 </dd>
<dl>
<dd> <p> If the <code>MULTIBYTE</code> option is set and the number is greater than 127 (i.e. not an ASCII character) it is treated as a Unicode character. </p>
 </dd></dl>
<dt><code>%</code></dt>
<dd> <p> Expand all <code>%</code> escapes in the resulting words in the same way as in prompts (see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)). If this flag is given twice, full prompt expansion is done on the resulting words, depending on the setting of the <code>PROMPT_PERCENT</code>, <code>PROMPT_SUBST</code> and <code>PROMPT_BANG</code> options. </p>
 </dd>
<dt><code>@</code></dt>
<dd> <p> In double quotes, array elements are put into separate words. E.g., `<code>&quot;${(@)foo}&quot;</code>&#8216; is equivalent to `<code>&quot;${foo[@]}&quot;</code>&#8216; and `<code>&quot;${(@)foo[1,2]}&quot;</code>&#8216; is the same as `<code>&quot;$foo[1]&quot; &quot;$foo[2]&quot;</code>&#8216;. This is distinct from <i>field splitting</i> by the <code>f</code>, <code>s</code> or <code>z</code> flags, which still applies within each array element. </p>
 </dd>
<dt><code>A</code></dt>
<dd> <p> Convert the substitution into an array expression, even if it otherwise would be scalar. This has lower precedence than subscripting, so one level of nested expansion is required in order that subscripts apply to array elements. Thus <code>${${(A</code><code>)</code><i>name</i><code>}[1]}</code> yields the full value of <i>name</i> when <i>name</i> is scalar. </p>
 </dd>
<dl>
<dd> <p> This assigns an array parameter with `<code>${</code>...<code>=</code>...<code>}</code>&#8216;, `<code>${</code>...<code>:=</code>...<code>}</code>&#8216; or `<code>${</code>...<code>::=</code>...<code>}</code>&#8216;. If this flag is repeated (as in `<code>AA</code>&#8216;), assigns an associative array parameter. Assignment is made before sorting or padding; if field splitting is active, the <i>word</i> part is split before assignment. The <i>name</i> part may be a subscripted range for ordinary arrays; when assigning an associative array, the <i>word</i> part <i>must</i> be converted to an array, for example by using `<code>${(AA)=</code><i>name</i><code>=</code>...<code>}</code>&#8216; to activate field splitting. </p>
<p> Surrounding context such as additional nesting or use of the value in a scalar assignment may cause the array to be joined back into a single string again. </p>
 </dd></dl>
<dt><code>a</code></dt>
<dd> <p> Sort in array index order; when combined with `<code>O</code>&#8216; sort in reverse array index order. Note that `<code>a</code>&#8216; is therefore equivalent to the default but `<code>Oa</code>&#8216; is useful for obtaining an array&#8217;s elements in reverse order. </p>
 </dd>
<dt><code>b</code></dt>
<dd> <p> Quote with backslashes only characters that are special to pattern matching. This is useful when the contents of the variable are to be tested using <code>GLOB_SUBST</code>, including the <code>${~</code><i>...</i><code>}</code> switch. </p>
 </dd>
<dl>
<dd> <p> Quoting using one of the <code>q</code> family of flags does not work for this purpose since quotes are not stripped from non-pattern characters by <code>GLOB_SUBST</code>. In other words, </p>
 </dd>
<dl>
<dd> <pre><code>
 pattern=${(q)str}
[[ $str = ${~pattern} ]] 
</code></pre>
 </dd></dl>
<p> works if <code>$str</code> is `<code>a*b</code>&#8216; but not if it is `<code>a b</code>&#8216;, whereas </p>
<dl>
<dd> <pre><code>
 pattern=${(b)str}
[[ $str = ${~pattern} ]] 
</code></pre>
 </dd></dl>
<p> is always true for any possible value of <code>$str</code>. </dl>
 </p>
<dt><code>c</code></dt>
<dd> <p> With <code>${#</code><i>name</i><code>}</code>, count the total number of characters in an array, as if the elements were concatenated with spaces between them. This is not a true join of the array, so other expressions used with this flag may have an effect on the elements of the array before it is counted. </p>
 </dd>
<dt><code>C</code></dt>
<dd> <p> Capitalize the resulting words. `Words&#8217; in this case refers to sequences of alphanumeric characters separated by non-alphanumerics, <i>not</i> to words that result from field splitting. </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Assume the string or array elements contain directories and attempt to substitute the leading part of these by names. The remainder of the path (the whole of it if the leading part was not substituted) is then quoted so that the whole string can be used as a shell argument. This is the reverse of `<code>~</code>&#8216; substitution: see the section FILENAME EXPANSION below. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Perform single word shell expansions, namely <i>parameter expansion</i>, <i>command substitution</i> and <i>arithmetic expansion</i>, on the result. Such expansions can be nested but too deep recursion may have unpredictable effects. </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> Split the result of the expansion at newlines. This is a shorthand for `<code>ps:\n:</code>&#8216;. </p>
 </dd>
<dt><code>F</code></dt>
<dd> <p> Join the words of arrays together using newline as a separator. This is a shorthand for `<code>pj:\n:</code>&#8216;. </p>
 </dd>
<dt><code>g:</code><i>opts</i><code>:</code></dt>
<dd> <p> Process escape sequences like the echo builtin when no options are given (<code>g::</code>). With the <code>o</code> option, octal escapes don&#8217;t take a leading zero. With the <code>c</code> option, sequences like `<code>^X</code>&#8216; are also processed. With the <code>e</code> option, processes `<code>\M-t</code>&#8216; and similar sequences like the print builtin. With both of the <code>o</code> and <code>e</code> options, behaves like the print builtin except that in none of these modes is `<code>\c</code>&#8216; interpreted. </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Sort case-insensitively. May be combined with `<code>n</code>&#8216; or `<code>O</code>&#8216;. </p>
 </dd>
<dt><code>k</code></dt>
<dd> <p> If <i>name</i> refers to an associative array, substitute the <i>keys</i> (element names) rather than the values of the elements. Used with subscripts (including ordinary arrays), force indices or keys to be substituted even if the subscript form refers to values. However, this flag may not be combined with subscript ranges. With the <code>KSH_ARRAYS</code> option a subscript `<code>[*]</code>&#8216; or `<code>[@]</code>&#8216; is needed to operate on the whole array, as usual. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> Convert all letters in the result to lower case. </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> Sort decimal integers numerically; if the first differing characters of two test strings are not digits, sorting is lexical. Integers with more initial zeroes are sorted before those with fewer or none. Hence the array `<code>foo1 foo02 foo2 foo3 foo20 foo23</code>&#8216; is sorted into the order shown. May be combined with `<code>i</code>&#8216; or `<code>O</code>&#8216;. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Sort the resulting words in ascending order; if this appears on its own the sorting is lexical and case-sensitive (unless the locale renders it case-insensitive). Sorting in ascending order is the default for other forms of sorting, so this is ignored if combined with `<code>a</code>&#8216;, `<code>i</code>&#8216; or `<code>n</code>&#8216;. </p>
 </dd>
<dt><code>O</code></dt>
<dd> <p> Sort the resulting words in descending order; `<code>O</code>&#8216; without `<code>a</code>&#8216;, `<code>i</code>&#8216; or `<code>n</code>&#8216; sorts in reverse lexical order. May be combined with `<code>a</code>&#8216;, `<code>i</code>&#8216; or `<code>n</code>&#8216; to reverse the order of sorting. </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> This forces the value of the parameter <i>name</i> to be interpreted as a further parameter name, whose value will be used where appropriate. Note that flags set with one of the <code>typeset</code> family of commands (in particular case transformations) are not applied to the value of <i>name</i> used in this fashion. </p>
 </dd>
<dl>
<dd> <p> If used with a nested parameter or command substitution, the result of that will be taken as a parameter name in the same way. For example, if you have `<code>foo=bar</code>&#8216; and `<code>bar=baz</code>&#8216;, the strings <code>${(P)foo}</code>, <code>${(P)${foo}}</code>, and <code>${(P)$(echo bar)}</code> will be expanded to `<code>baz</code>&#8216;. </p>
<p> Likewise, if the reference is itself nested, the expression with the flag is treated as if it were directly replaced by the parameter name. It is an error if this nested substitution produces an array with more than one word. For example, if `<code>name=assoc</code>&#8216; where the parameter <code>assoc</code> is an associative array, then `<code>${${(P)name}[elt]}</code>&#8216; refers to the element of the associative subscripted `<code>elt</code>&#8216;. </p>
 </dd></dl>
<dt><code>q</code></dt>
<dd> <p> Quote characters that are special to the shell in the resulting words with backslashes; unprintable or invalid characters are quoted using the <code>$&#8216;\</code><i>NNN</i><code>&#8216;</code> form, with separate quotes for each octet. </p>
 </dd>
<dl>
<dd> <p> If this flag is given twice, the resulting words are quoted in single quotes and if it is given three times, the words are quoted in double quotes; in these forms no special handling of unprintable or invalid characters is attempted. If the flag is given four times, the words are quoted in single quotes preceded by a <code>$</code>. Note that in all three of these forms quoting is done unconditionally, even if this does not change the way the resulting string would be interpreted by the shell. </p>
<p> If a <code>q-</code> is given (only a single <code>q</code> may appear), a minimal form of single quoting is used that only quotes the string if needed to protect special characters. Typically this form gives the most readable output. </p>
<p> If a <code>q+</code> is given, an extended form of minimal quoting is used that causes unprintable characters to be rendered using <code>$&#8216;</code><i>...</i><code>&#8216;</code>. This quoting is similar to that used by the output of values by the <code>typeset</code> family of commands. </p>
 </dd></dl>
<dt><code>Q</code></dt>
<dd> <p> Remove one level of quotes from the resulting words. </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> Use a string describing the type of the parameter where the value of the parameter would usually appear. This string consists of keywords separated by hyphens (`<code>-</code>&#8216;). The first keyword in the string describes the main type, it can be one of `<code>scalar</code>&#8216;, `<code>array</code>&#8216;, `<code>integer</code>&#8216;, `<code>float</code>&#8216; or `<code>association</code>&#8216;. The other keywords describe the type in more detail: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>local</code> for local parameters </p>
 </dd>
<dt><code>left</code></dt>
<dd> <p> for left justified parameters </p>
 </dd>
<dt><code>right_blanks</code></dt>
<dd> <p> for right justified parameters with leading blanks </p>
 </dd>
<dt><code>right_zeros</code></dt>
<dd> <p> for right justified parameters with leading zeros </p>
 </dd>
<dt><code>lower</code></dt>
<dd> <p> for parameters whose value is converted to all lower case when it is expanded </p>
 </dd>
<dt><code>upper</code></dt>
<dd> <p> for parameters whose value is converted to all upper case when it is expanded </p>
 </dd>
<dt><code>readonly</code></dt>
<dd> <p> for readonly parameters </p>
 </dd>
<dt><code>tag</code></dt>
<dd> <p> for tagged parameters </p>
 </dd>
<dt><code>export</code></dt>
<dd> <p> for exported parameters </p>
 </dd>
<dt><code>unique</code></dt>
<dd> <p> for arrays which keep only the first occurrence of duplicated values </p>
 </dd>
<dt><code>hide</code></dt>
<dd> <p> for parameters with the `hide&#8217; flag </p>
 </dd>
<dt><code>hideval</code></dt>
<dd> <p> for parameters with the `hideval&#8217; flag </p>
 </dd>
<dt><code>special</code></dt>
<dd> <p> for special parameters defined by the shell </p>
 </dd></dl>
</dl>
<dt><code>u</code></dt>
<dd> <p> Expand only the first occurrence of each unique word. </p>
 </dd>
<dt><code>U</code></dt>
<dd> <p> Convert all letters in the result to upper case. </p>
 </dd>
<dt><code>v</code></dt>
<dd> <p> Used with <code>k</code>, substitute (as two consecutive words) both the key and the value of each associative array element. Used with subscripts, force values to be substituted even if the subscript form refers to indices or keys. </p>
 </dd>
<dt><code>V</code></dt>
<dd> <p> Make any special characters in the resulting words visible. </p>
 </dd>
<dt><code>w</code></dt>
<dd> <p> With <code>${#</code><i>name</i><code>}</code>, count words in arrays or strings; the <code>s</code> flag may be used to set a word delimiter. </p>
 </dd>
<dt><code>W</code></dt>
<dd> <p> Similar to <code>w</code> with the difference that empty words between repeated delimiters are also counted. </p>
 </dd>
<dt><code>X</code></dt>
<dd> <p> With this flag, parsing errors occurring with the <code>Q</code>, <code>e</code> and <code>#</code> flags or the pattern matching forms such as `<code>${</code><i>name</i><code>#</code><i>pattern</i><code>}</code>&#8216; are reported. Without the flag, errors are silently ignored. </p>
 </dd>
<dt><code>z</code></dt>
<dd> <p> Split the result of the expansion into words using shell parsing to find the words, i.e. taking into account any quoting in the value. Comments are not treated specially but as ordinary strings, similar to interactive shells with the <code>INTERACTIVE_COMMENTS</code> option unset (however, see the <code>Z</code> flag below for related options) </p>
 </dd>
<dl>
<dd> <p> Note that this is done very late, even later than the `<code>(s)</code>&#8216; flag. So to access single words in the result use nested expansions as in `<code>${${(z)foo}[2]}</code>&#8216;. Likewise, to remove the quotes in the resulting words use `<code>${(Q)${(z)foo}}</code>&#8216;. </p>
 </dd></dl>
<dt><code>0</code></dt>
<dd> <p> Split the result of the expansion on null bytes. This is a shorthand for `<code>ps:\0:</code>&#8216;. </p>
 </dd></dl>
<p> The following flags (except <code>p</code>) are followed by one or more arguments as shown. Any character, or the matching pairs `<code>(</code>...<code>)</code>&#8216;, `<code>{</code>...<code>}</code>&#8216;, `<code>[</code>...<code>]</code>&#8216;, or `<code>&lt;</code>...<code>&gt;</code>&#8216;, may be used in place of a colon as delimiters, but note that when a flag takes more than one argument, a matched pair of delimiters must surround each argument. </p>
<dl>
<dd> <p> <code>p</code> Recognize the same escape sequences as the <code>print</code> builtin in string arguments to any of the flags described below that follow this argument. </p>
 </dd>
<dl>
<dd> <p> Alternatively, with this option string arguments may be in the form <code>$</code><i>var</i> in which case the value of the variable is substituted. Note this form is strict; the string argument does not undergo general parameter expansion. </p>
<p> For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 sep=:
val=a:b:c
print ${(ps.$sep.)val} 
</code></pre>
 </dd></dl>
<p> splits the variable on a <code>:</code>. </dl>
 </p>
<dt><code>~</code></dt>
<dd> <p> Strings inserted into the expansion by any of the flags below are to be treated as patterns. This applies to the string arguments of flags that follow <code>~</code> within the same set of parentheses. Compare with <code>~</code> outside parentheses, which forces the entire substituted string to be treated as a pattern. Hence, for example, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>
 [[ &quot;?&quot; = ${(~j.|.)array} ]] 
</code></pre>
 </dd></dl>
<p> treats `<code>|</code>&#8216; as a pattern and succeeds if and only if <code>$array</code> contains the string `<code>?</code>&#8216; as an element. The <code>~</code> may be repeated to toggle the behaviour; its effect only lasts to the end of the parenthesised group. </dl>
 </p>
<dt><code>j:</code><i>string</i><code>:</code></dt>
<dd> <p> Join the words of arrays together using <i>string</i> as a separator. Note that this occurs before field splitting by the <code>s:</code><i>string</i><code>:</code> flag or the <code>SH_WORD_SPLIT</code> option. </p>
 </dd>
<dt><code>l:</code><i>expr</i><code>::</code><i>string1</i><code>::</code><i>string2</i><code>:</code></dt>
<dd> <p> Pad the resulting words on the left. Each word will be truncated if required and placed in a field <i>expr</i> characters wide. </p>
 </dd>
<dl>
<dd> <p> The arguments <code>:</code><i>string1</i><code>:</code> and <code>:</code><i>string2</i><code>:</code> are optional; neither, the first, or both may be given. Note that the same pairs of delimiters must be used for each of the three arguments. The space to the left will be filled with <i>string1</i> (concatenated as often as needed) or spaces if <i>string1</i> is not given. If both <i>string1</i> and <i>string2</i> are given, <i>string2</i> is inserted once directly to the left of each word, truncated if necessary, before <i>string1</i> is used to produce any remaining padding. </p>
<p> If either of <i>string1</i> or <i>string2</i> is present but empty, i.e. there are two delimiters together at that point, the first character of <code>$IFS</code> is used instead. </p>
<p> If the <code>MULTIBYTE</code> option is in effect, the flag <code>m</code> may also be given, in which case widths will be used for the calculation of padding; otherwise individual multibyte characters are treated as occupying one unit of width. </p>
<p> If the <code>MULTIBYTE</code> option is not in effect, each byte in the string is treated as occupying one unit of width. </p>
<p> Control characters are always assumed to be one unit wide; this allows the mechanism to be used for generating repetitions of control characters. </p>
 </dd></dl>
<dt><code>m</code></dt>
<dd> <p> Only useful together with one of the flags <code>l</code> or <code>r</code> or with the <code>#</code> length operator when the <code>MULTIBYTE</code> option is in effect. Use the character width reported by the system in calculating how much of the string it occupies or the overall length of the string. Most printable characters have a width of one unit, however certain Asian character sets and certain special effects use wider characters; combining characters have zero width. Non-printable characters are arbitrarily counted as zero width; how they would actually be displayed will vary. </p>
 </dd>
<dl>
<dd> <p> If the <code>m</code> is repeated, the character either counts zero (if it has zero width), else one. For printable character strings this has the effect of counting the number of glyphs (visibly separate characters), except for the case where combining characters themselves have non-zero width (true in certain alphabets). </p>
 </dd></dl>
<dt><code>r:</code><i>expr</i><code>::</code><i>string1</i><code>::</code><i>string2</i><code>:</code></dt>
<dd> <p> As <code>l</code>, but pad the words on the right and insert <i>string2</i> immediately to the right of the string to be padded. </p>
 </dd>
<dl>
<dd> <p> Left and right padding may be used together. In this case the strategy is to apply left padding to the first half width of each of the resulting words, and right padding to the second half. If the string to be padded has odd width the extra padding is applied on the left. </p>
 </dd></dl>
<dt><code>s:</code><i>string</i><code>:</code></dt>
<dd> <p> Force field splitting at the separator <i>string</i>. Note that a <i>string</i> of two or more characters means that all of them must match in sequence; this differs from the treatment of two or more characters in the <code>IFS</code> parameter. See also the <code>=</code> flag and the <code>SH_WORD_SPLIT</code> option. An empty string may also be given in which case every character will be a separate element. </p>
 </dd>
<dl>
<dd> <p> For historical reasons, the usual behaviour that empty array elements are retained inside double quotes is disabled for arrays generated by splitting; hence the following: </p>
 </dd>
<dl>
<dd> <pre><code>
 line=&quot;one::three&quot;
print -l &quot;${(s.:.)line}&quot; 
</code></pre>
 </dd></dl>
<p> produces two lines of output for <code>one</code> and <code>three</code> and elides the empty field. To override this behaviour, supply the `<code>(@)</code>&#8216; flag as well, i.e. <code>&quot;${(@s.:.)line}&quot;</code>. </dl>
 </p>
<dt><code>Z:</code><i>opts</i><code>:</code></dt>
<dd> <p> As <code>z</code> but takes a combination of option letters between a following pair of delimiter characters. With no options the effect is identical to <code>z</code>. <code>(Z+c+)</code> causes comments to be parsed as a string and retained; any field in the resulting array beginning with an unquoted comment character is a comment. <code>(Z+C+)</code> causes comments to be parsed and removed. The rule for comments is standard: anything between a word starting with the third character of <code>$HISTCHARS</code>, default <code>#</code>, up to the next newline is a comment. <code>(Z+n+)</code> causes unquoted newlines to be treated as ordinary whitespace, else they are treated as if they are shell code delimiters and converted to semicolons. Options are combined within the same set of delimiters, e.g. <code>(Z+Cn+)</code>. </p>
 </dd>
<dt><code>_:</code><i>flags</i><code>:</code></dt>
<dd> <p> The underscore (<code>_</code>) flag is reserved for future use. As of this revision of zsh, there are no valid <i>flags</i>; anything following an underscore, other than an empty pair of delimiters, is treated as an error, and the flag itself has no effect. </p>
 </dd></dl>
<p> The following flags are meaningful with the <code>${</code>...<code>#</code>...<code>}</code> or <code>${</code>...<code>%</code>...<code>}</code> forms. The <code>S</code> and <code>I</code> flags may also be used with the <code>${</code>...<code>/</code>...<code>}</code> forms. </p>
<dl>
<dd> <p> <code>S</code> With <code>#</code> or <code>##</code>, search for the match that starts closest to the start of the string (a `substring match&#8217;). Of all matches at a particular position, <code>#</code> selects the shortest and <code>##</code> the longest: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>
 % str=&quot;aXbXc&quot;
% echo ${(S)str#X*}
abXc
% echo ${(S)str##X*}
a
% 
</code></pre>
 </dd></dl>
<p> With <code>%</code> or <code>%%</code>, search for the match that starts closest to the end of the string: </p>
<dl>
<dd> <pre><code>
 % str=&quot;aXbXc&quot;
% echo ${(S)str%X*}
aXbc
% echo ${(S)str%%X*}
aXb
% 
</code></pre>
 </dd></dl>
<p> (Note that <code>%</code> and <code>%%</code> don&#8217;t search for the match that ends closest to the end of the string, as one might expect.) </p>
<p> With substitution via <code>${</code>...<code>/</code>...<code>}</code> or <code>${</code>...<code>//</code>...<code>}</code>, specifies non-greedy matching, i.e. that the shortest instead of the longest match should be replaced: </p>
<dl>
<dd> <pre><code>
 % str=&quot;abab&quot;
% echo ${str/*b/_}
_
% echo ${(S)str/*b/_}
_ab
% 
</code></pre>
 </dd></dl>
</dl>
<dt><code>I:</code><i>expr</i><code>:</code></dt>
<dd> <p> Search the <i>expr</i>th match (where <i>expr</i> evaluates to a number). This only applies when searching for substrings, either with the <code>S</code> flag, or with <code>${</code>...<code>/</code>...<code>}</code> (only the <i>expr</i>th match is substituted) or <code>${</code>...<code>//</code>...<code>}</code> (all matches from the <i>expr</i>th on are substituted). The default is to take the first match. </p>
 </dd>
<dl>
<dd> <p> The <i>expr</i>th match is counted such that there is either one or zero matches from each starting position in the string, although for global substitution matches overlapping previous replacements are ignored. With the <code>${</code>...<code>%</code>...<code>}</code> and <code>${</code>...<code>%%</code>...<code>}</code> forms, the starting position for the match moves backwards from the end as the index increases, while with the other forms it moves forward from the start. </p>
<p> Hence with the string </p>
 </dd>
<dl>
<dd> <pre><code>
 which switch is the right switch for Ipswich? 
</code></pre>
 </dd></dl>
<p> substitutions of the form <code>${</code>(<code>SI:</code><i>N</i><code>:</code>)<code>string#w*ch}</code> as <i>N</i> increases from 1 will match and remove `<code>which</code>&#8216;, `<code>witch</code>&#8216;, `<code>witch</code>&#8216; and `<code>wich</code>&#8216;; the form using `<code>##</code>&#8216; will match and remove `<code>which switch is the right switch for Ipswich</code>&#8216;, `<code>witch is the right switch for Ipswich</code>&#8216;, `<code>witch for Ipswich</code>&#8216; and `<code>wich</code>&#8216;. The form using `<code>%</code>&#8216; will remove the same matches as for `<code>#</code>&#8216;, but in reverse order, and the form using `<code>%%</code>&#8216; will remove the same matches as for `<code>##</code>&#8216; in reverse order. </dl>
 </p>
<dt><code>B</code></dt>
<dd> <p> Include the index of the beginning of the match in the result. </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> Include the index one character past the end of the match in the result (note this is inconsistent with other uses of parameter index). </p>
 </dd>
<dt><code>M</code></dt>
<dd> <p> Include the matched portion in the result. </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> Include the length of the match in the result. </p>
 </dd>
<dt><code>R</code></dt>
<dd> <p> Include the unmatched portion in the result (the <i>R</i>est). </p>
 </dd></dl>
<h3>Rules</h3>
<p> Here is a summary of the rules for substitution; this assumes that braces are present around the substitution, i.e. <code>${</code><i>...</i><code>}</code>. Some particular examples are given below. Note that the Zsh Development Group accepts <i>no responsibility</i> for any brain damage which may occur during the reading of the following rules. </p>
<dl>
<dd> <p> <code>1.</code> <i>Nested substitution</i> If multiple nested <code>${</code><i>...</i><code>}</code> forms are present, substitution is performed from the inside outwards. At each level, the substitution takes account of whether the current value is a scalar or an array, whether the whole substitution is in double quotes, and what flags are supplied to the current level of substitution, just as if the nested substitution were the outermost. The flags are not propagated up to enclosing substitutions; the nested substitution will return either a scalar or an array as determined by the flags, possibly adjusted for quoting. All the following steps take place where applicable at all levels of substitution. </p>
 </dd>
<dl>
<dd> <p> Note that, unless the `<code>(P)</code>&#8216; flag is present, the flags and any subscripts apply directly to the value of the nested substitution; for example, the expansion <code>${${foo}}</code> behaves exactly the same as <code>${foo}</code>. When the `<code>(P)</code>&#8216; flag is present in a nested substitution, the other substitution rules are applied to the value <i>before</i> it is interpreted as a name, so <code>${${(P)foo}}</code> may differ from <code>${(P)foo}</code>. </p>
<p> At each nested level of substitution, the substituted words undergo all forms of single-word substitution (i.e. not filename generation), including command substitution, arithmetic expansion and filename expansion (i.e. leading <code>~</code> and <code>=</code>). Thus, for example, <code>${${:-=cat}:h}</code> expands to the directory where the <code>cat</code> program resides. (Explanation: the internal substitution has no parameter but a default value <code>=cat</code>, which is expanded by filename expansion to a full path; the outer substitution then applies the modifier <code>:h</code> and takes the directory part of the path.) </p>
 </dd></dl>
<dt><code>2.</code><i>Internal parameter flags</i></dt>
<dd> <p> Any parameter flags set by one of the <code>typeset</code> family of commands, in particular the <code>-L</code>, <code>-R</code>, <code>-Z</code>, <code>-u</code> and <code>-l</code> options for padding and capitalization, are applied directly to the parameter value. Note these flags are options to the command, e.g. `<code>typeset -Z</code>&#8216;; they are not the same as the flags used within parameter substitutions. </p>
 </dd>
<dl>
<dd> <p> At the outermost level of substitution, the `<code>(P)</code>&#8216; flag (rule <code>4.</code>) ignores these transformations and uses the unmodified value of the parameter as the name to be replaced. This is usually the desired behavior because padding may make the value syntactically illegal as a parameter name, but if capitalization changes are desired, use the <code>${${(P)foo}}</code> form (rule <code>25.</code>). </p>
 </dd></dl>
<dt><code>3.</code><i>Parameter subscripting</i></dt>
<dd> <p> If the value is a raw parameter reference with a subscript, such as <code>${</code><i>var</i><code>[3]}</code>, the effect of subscripting is applied directly to the parameter. Subscripts are evaluated left to right; subsequent subscripts apply to the scalar or array value yielded by the previous subscript. Thus if <code>var</code> is an array, <code>${var[1][2]}</code> is the second character of the first word, but <code>${var[2,4][2]}</code> is the entire third word (the second word of the range of words two through four of the original array). Any number of subscripts may appear. Flags such as `<code>(k)</code>&#8216; and `<code>(v)</code>&#8216; which alter the result of subscripting are applied. </p>
 </dd>
<dt><code>4.</code><i>Parameter name replacement</i></dt>
<dd> <p> At the outermost level of nesting only, the `<code>(P)</code>&#8216; flag is applied. This treats the value so far as a parameter name (which may include a subscript expression) and replaces that with the corresponding value. This replacement occurs later if the `<code>(P)</code>&#8216; flag appears in a nested substitution. </p>
 </dd>
<dl>
<dd> <p> If the value so far names a parameter that has internal flags (rule <code>2.</code>), those internal flags are applied to the new value after replacement. </p>
 </dd></dl>
<dt><code>5.</code><i>Double-quoted joining</i></dt>
<dd> <p> If the value after this process is an array, and the substitution appears in double quotes, and neither an `<code>(@)</code>&#8216; flag nor a `<code>#</code>&#8216; length operator is present at the current level, then words of the value are joined with the first character of the parameter <code>$IFS</code>, by default a space, between each word (single word arrays are not modified). If the `<code>(j)</code>&#8216; flag is present, that is used for joining instead of <code>$IFS</code>. </p>
 </dd>
<dt><code>6.</code><i>Nested subscripting</i></dt>
<dd> <p> Any remaining subscripts (i.e. of a nested substitution) are evaluated at this point, based on whether the value is an array or a scalar. As with <code>3.</code>, multiple subscripts can appear. Note that <code>${foo[2,4][2]}</code> is thus equivalent to <code>${${foo[2,4]}[2]}</code> and also to <code>&quot;${${(@)foo[2,4]}[2]}&quot;</code> (the nested substitution returns an array in both cases), but not to <code>&quot;${${foo[2,4]}[2]}&quot;</code> (the nested substitution returns a scalar because of the quotes). </p>
 </dd>
<dt><code>7.</code><i>Modifiers</i></dt>
<dd> <p> Any modifiers, as specified by a trailing `<code>#</code>&#8216;, `<code>%</code>&#8216;, `<code>/</code>&#8216; (possibly doubled) or by a set of modifiers of the form `<code>:...</code>&#8216; (see the section `Modifiers&#8217; in the section `History Expansion&#8217;), are applied to the words of the value at this level. </p>
 </dd>
<dt><code>8.</code><i>Character evaluation</i></dt>
<dd> <p> Any `<code>(#)</code>&#8216; flag is applied, evaluating the result so far numerically as a character. </p>
 </dd>
<dt><code>9.</code><i>Length</i></dt>
<dd> <p> Any initial `<code>#</code>&#8216; modifier, i.e. in the form <code>${#</code><i>var</i><code>}</code>, is used to evaluate the length of the expression so far. </p>
 </dd>
<dt><code>10.</code><i>Forced joining</i></dt>
<dd> <p> If the `<code>(j)</code>&#8216; flag is present, or no `<code>(j)</code>&#8216; flag is present but the string is to be split as given by rule <code>11.</code>, and joining did not take place at rule <code>5.</code>, any words in the value are joined together using the given string or the first character of <code>$IFS</code> if none. Note that the `<code>(F)</code>&#8216; flag implicitly supplies a string for joining in this manner. </p>
 </dd>
<dt><code>11.</code><i>Simple word splitting</i></dt>
<dd> <p> If one of the `<code>(s)</code>&#8216; or `<code>(f)</code>&#8216; flags are present, or the `<code>=</code>&#8216; specifier was present (e.g. <code>${=</code><i>var</i><code>}</code>), the word is split on occurrences of the specified string, or (for <code>=</code> with neither of the two flags present) any of the characters in <code>$IFS</code>. </p>
 </dd>
<dl>
<dd> <p> If no `<code>(s)</code>&#8216;, `<code>(f)</code>&#8216; or `<code>=</code>&#8216; was given, but the word is not quoted and the option <code>SH_WORD_SPLIT</code> is set, the word is split on occurrences of any of the characters in <code>$IFS</code>. Note this step, too, takes place at all levels of a nested substitution. </p>
 </dd></dl>
<dt><code>12.</code><i>Case modification</i></dt>
<dd> <p> Any case modification from one of the flags `<code>(L)</code>&#8216;, `<code>(U)</code>&#8216; or `<code>(C)</code>&#8216; is applied. </p>
 </dd>
<dt><code>13.</code><i>Escape sequence replacement</i></dt>
<dd> <p> First any replacements from the `<code>(g)</code>&#8216; flag are performed, then any prompt-style formatting from the `<code>(%)</code>&#8216; family of flags is applied. </p>
 </dd>
<dt><code>14.</code><i>Quote application</i></dt>
<dd> <p> Any quoting or unquoting using `<code>(q)</code>&#8216; and `<code>(Q)</code>&#8216; and related flags is applied. </p>
 </dd>
<dt><code>15.</code><i>Directory naming</i></dt>
<dd> <p> Any directory name substitution using `<code>(D)</code>&#8216; flag is applied. </p>
 </dd>
<dt><code>16.</code><i>Visibility enhancement</i></dt>
<dd> <p> Any modifications to make characters visible using the `<code>(V)</code>&#8216; flag are applied. </p>
 </dd>
<dt><code>17.</code><i>Lexical word splitting</i></dt>
<dd> <p> If the &#8216;<code>(z)</code>&#8216; flag or one of the forms of the &#8216;<code>(Z)</code>&#8216; flag is present, the word is split as if it were a shell command line, so that quotation marks and other metacharacters are used to decide what constitutes a word. Note this form of splitting is entirely distinct from that described by rule <code>11.</code>: it does not use <code>$IFS</code>, and does not cause forced joining. </p>
 </dd>
<dt><code>18.</code><i>Uniqueness</i></dt>
<dd> <p> If the result is an array and the `<code>(u)</code>&#8216; flag was present, duplicate elements are removed from the array. </p>
 </dd>
<dt><code>19.</code><i>Ordering</i></dt>
<dd> <p> If the result is still an array and one of the `<code>(o)</code>&#8216; or `<code>(O)</code>&#8216; flags was present, the array is reordered. </p>
 </dd>
<dt><code>20.</code><code>RC_EXPAND_PARAM</code></dt>
<dd> <p> At this point the decision is made whether any resulting array elements are to be combined element by element with surrounding text, as given by either the <code>RC_EXPAND_PARAM</code> option or the `<code>^</code>&#8216; flag. </p>
 </dd>
<dt><code>21.</code><i>Re-evaluation</i></dt>
<dd> <p> Any `<code>(e)</code>&#8216; flag is applied to the value, forcing it to be re-examined for new parameter substitutions, but also for command and arithmetic substitutions. </p>
 </dd>
<dt><code>22.</code><i>Padding</i></dt>
<dd> <p> Any padding of the value by the `<code>(l.</code><i>fill</i><code>.)</code>&#8216; or `<code>(r.</code><i>fill</i><code>.)</code>&#8216; flags is applied. </p>
 </dd>
<dt><code>23.</code><i>Semantic joining</i></dt>
<dd> <p> In contexts where expansion semantics requires a single word to result, all words are rejoined with the first character of <code>IFS</code> between. So in `<code>${(P</code><code>)${(f</code><code>)lines}}</code>&#8216; the value of <code>${lines}</code> is split at newlines, but then must be joined again before the `<code>(P)</code>&#8216; flag can be applied. </p>
 </dd>
<dl>
<dd> <p> If a single word is not required, this rule is skipped. </p>
 </dd></dl>
<dt><code>24.</code><i>Empty argument removal</i></dt>
<dd> <p> If the substitution does not appear in double quotes, any resulting zero-length argument, whether from a scalar or an element of an array, is elided from the list of arguments inserted into the command line. </p>
 </dd>
<dl>
<dd> <p> Strictly speaking, the removal happens later as the same happens with other forms of substitution; the point to note here is simply that it occurs after any of the above parameter operations. </p>
 </dd></dl>
<dt><code>25.</code><i>Nested parameter name replacement</i></dt>
<dd> <p> If the `<code>(P)</code>&#8216; flag is present and rule <code>4.</code> has not applied, the value so far is treated as a parameter name (which may include a subscript expression) and replaced with the corresponding value, with internal flags (rule <code>2.</code>) applied to the new value. </p>
 </dd></dl>
<h3>Examples</h3>
<p> The flag <code>f</code> is useful to split a double-quoted substitution line by line. For example, <code>${(f)&quot;$(&lt;</code><i>file</i><code>)&quot;}</code> substitutes the contents of <i>file</i> divided so that each line is an element of the resulting array. Compare this with the effect of <code>$</code><code>(&lt;</code><i>file</i><code>)</code> alone, which divides the file up by words, or the same inside double quotes, which makes the entire content of the file a single string. </p>
<p> The following illustrates the rules for nested parameter expansions. Suppose that <code>$foo</code> contains the array <code>(bar baz</code><code>)</code>: </p>
<dl>
<dd> <p> <code>&quot;${(@)${foo}[1]}&quot;</code> This produces the result <code>b</code>. First, the inner substitution <code>&quot;${foo}&quot;</code>, which has no array (<code>@</code>) flag, produces a single word result <code>&quot;bar baz&quot;</code>. The outer substitution <code>&quot;${(@)...[1]}&quot;</code> detects that this is a scalar, so that (despite the `<code>(@)</code>&#8216; flag) the subscript picks the first character. </p>
 </dd>
<dt><code>&quot;${${(@)foo}[1]}&quot;</code></dt>
<dd> <p> This produces the result `<code>bar</code>&#8216;. In this case, the inner substitution <code>&quot;${(@)foo}&quot;</code> produces the array `<code>(bar baz</code><code>)</code>&#8216;. The outer substitution <code>&quot;${...[1]}&quot;</code> detects that this is an array and picks the first word. This is similar to the simple case <code>&quot;${foo[1]}&quot;</code>. </p>
 </dd></dl>
<p> As an example of the rules for word splitting and joining, suppose <code>$foo</code> contains the array `<code>(ax1 bx1</code><code>)</code>&#8216;. Then </p>
<dl>
<dd> <p> <code>${(s/x/)foo}</code> produces the words `<code>a</code>&#8216;, `<code>1 b</code>&#8216; and `<code>1</code>&#8216;. </p>
 </dd>
<dt><code>${(j/x/s/x/)foo}</code></dt>
<dd> <p> produces `<code>a</code>&#8216;, `<code>1</code>&#8216;, `<code>b</code>&#8216; and `<code>1</code>&#8216;. </p>
 </dd>
<dt><code>${(s/x/)foo%%1*}</code></dt>
<dd> <p> produces `<code>a</code>&#8216; and `<code> b</code>&#8216; (note the extra space). As substitution occurs before either joining or splitting, the operation first generates the modified array <code>(ax bx</code><code>)</code>, which is joined to give <code>&quot;ax bx&quot;</code>, and then split to give `<code>a</code>&#8216;, `<code> b</code>&#8216; and `&#8216;. The final empty string will then be elided, as it is not in double quotes. </p>
 </dd></dl>
<h2>COMMAND SUBSTITUTION</h2>
<p> A command enclosed in parentheses preceded by a dollar sign, like `<code>$(</code>...<code>)</code>&#8216;, or quoted with grave accents, like `<code>`</code>...<code>`</code>&#8216;, is replaced with its standard output, with any trailing newlines deleted. If the substitution is not enclosed in double quotes, the output is broken into words using the <code>IFS</code> parameter. </p>
<p> The substitution `<code>$(cat</code> <i>foo</i><code>)</code>&#8216; may be replaced by the faster `<code>$(&lt;</code><i>foo</i><code>)</code>&#8216;. In this case <i>foo</i> undergoes single word shell expansions (<i>parameter expansion</i>, <i>command substitution</i> and <i>arithmetic expansion</i>), but not filename generation. </p>
<p> If the option <code>GLOB_SUBST</code> is set, the result of any unquoted command substitution, including the special form just mentioned, is eligible for filename generation. </p>
<h2>ARITHMETIC EXPANSION</h2>
<p> A string of the form `<code>$[</code><i>exp</i><code>]</code>&#8216; or `<code>$((</code><i>exp</i><code>))</code>&#8216; is substituted with the value of the arithmetic expression <i>exp</i>. <i>exp</i> is subjected to <i>parameter expansion</i>, <i>command substitution</i> and <i>arithmetic expansion</i> before it is evaluated. See the section `Arithmetic Evaluation&#8217;.  </p>
<h2>BRACE EXPANSION</h2>
<p> A string of the form `<i>foo</i><code>{</code><i>xx</i><code>,</code><i>yy</i><code>,</code><i>zz</i><code>}</code><i>bar</i>&#8216; is expanded to the individual words `<i>fooxxbar</i>&#8216;, `<i>fooyybar</i>&#8216; and `<i>foozzbar</i>&#8216;. Left-to-right order is preserved. This construct may be nested. Commas may be quoted in order to include them literally in a word. </p>
<p> An expression of the form `<code>{</code><i>n1</i><code>..</code><i>n2</i><code>}</code>&#8216;, where <i>n1</i> and <i>n2</i> are integers, is expanded to every number between <i>n1</i> and <i>n2</i> inclusive. If either number begins with a zero, all the resulting numbers will be padded with leading zeroes to that minimum width, but for negative numbers the <code>-</code> character is also included in the width. If the numbers are in decreasing order the resulting sequence will also be in decreasing order. </p>
<p> An expression of the form `<code>{</code><i>n1</i><code>..</code><i>n2</i><code>..</code><i>n3</i><code>}</code>&#8216;, where <i>n1</i>, <i>n2</i>, and <i>n3</i> are integers, is expanded as above, but only every <i>n3</i>th number starting from <i>n1</i> is output. If <i>n3</i> is negative the numbers are output in reverse order, this is slightly different from simply swapping <i>n1</i> and <i>n2</i> in the case that the step <i>n3</i> doesn&#8217;t evenly divide the range. Zero padding can be specified in any of the three numbers, specifying it in the third can be useful to pad for example `<code>{-99..100..01}</code>&#8216; which is not possible to specify by putting a 0 on either of the first two numbers (i.e. pad to two characters). </p>
<p> An expression of the form `<code>{</code><i>c1</i><code>..</code><i>c2</i><code>}</code>&#8216;, where <i>c1</i> and <i>c2</i> are single characters (which may be multibyte characters), is expanded to every character in the range from <i>c1</i> to <i>c2</i> in whatever character sequence is used internally. For characters with code points below 128 this is US ASCII (this is the only case most users will need). If any intervening character is not printable, appropriate quotation is used to render it printable. If the character sequence is reversed, the output is in reverse order, e.g. `<code>{d..a}</code>&#8216; is substituted as `<code>d c b a</code>&#8216;. </p>
<p> If a brace expression matches none of the above forms, it is left unchanged, unless the option <code>BRACE_CCL</code> (an abbreviation for `brace character class&#8217;) is set. In that case, it is expanded to a list of the individual characters between the braces sorted into the order of the characters in the ASCII character set (multibyte characters are not currently handled). The syntax is similar to a <code>[</code>...<code>]</code> expression in filename generation: `<code>-</code>&#8216; is treated specially to denote a range of characters, but `<code>^</code>&#8216; or `<code>!</code>&#8216; as the first character is treated normally. For example, `<code>{abcdef0-9}</code>&#8216; expands to 16 words <code>0 1 2 3 4 5 6 7 8 9 a b c d e f</code>. </p>
<p> Note that brace expansion is not part of filename generation (globbing); an expression such as <code>*/{foo,bar}</code> is split into two separate words <code>*/foo</code> and <code>*/bar</code> before filename generation takes place. In particular, note that this is liable to produce a `no match&#8217; error if <i>either</i> of the two expressions does not match; this is to be contrasted with <code>*/(foo|bar)</code>, which is treated as a single pattern but otherwise has similar effects. </p>
<p> To combine brace expansion with array expansion, see the <code>${^</code><i>spec</i><code>}</code> form described in the section Parameter Expansion above. </p>
<h2>FILENAME EXPANSION</h2>
<p> Each word is checked to see if it begins with an unquoted `<code>~</code>&#8216;. If it does, then the word up to a `<code>/</code>&#8216;, or the end of the word if there is no `<code>/</code>&#8216;, is checked to see if it can be substituted in one of the ways described here. If so, then the `<code>~</code>&#8216; and the checked portion are replaced with the appropriate substitute value. </p>
<p> A `<code>~</code>&#8216; by itself is replaced by the value of <code>$HOME</code>. A `<code>~</code>&#8216; followed by a `<code>+</code>&#8216; or a `<code>-</code>&#8216; is replaced by current or previous working directory, respectively. </p>
<p> A `<code>~</code>&#8216; followed by a number is replaced by the directory at that position in the directory stack. `<code>~0</code>&#8216; is equivalent to `<code>~+</code>&#8216;, and `<code>~1</code>&#8216; is the top of the stack. `<code>~+</code>&#8216; followed by a number is replaced by the directory at that position in the directory stack. `<code>~+0</code>&#8216; is equivalent to `<code>~+</code>&#8216;, and `<code>~+1</code>&#8216; is the top of the stack. `<code>~-</code>&#8216; followed by a number is replaced by the directory that many positions from the bottom of the stack. `<code>~-0</code>&#8216; is the bottom of the stack. The <code>PUSHD_MINUS</code> option exchanges the effects of `<code>~+</code>&#8216; and `<code>~-</code>&#8216; where they are followed by a number. </p>
<h3>Dynamic named directories</h3>
<p> If the function <code>zsh_directory_name</code> exists, or the shell variable <code>zsh_directory_name_functions</code> exists and contains an array of function names, then the functions are used to implement dynamic directory naming. The functions are tried in order until one returns status zero, so it is important that functions test whether they can handle the case in question and return an appropriate status. </p>
<p> A `<code>~</code>&#8216; followed by a string <i>namstr</i> in unquoted square brackets is treated specially as a dynamic directory name. Note that the first unquoted closing square bracket always terminates <i>namstr</i>. The shell function is passed two arguments: the string <code>n</code> (for name) and <i>namstr</i>. It should either set the array <code>reply</code> to a single element which is the directory corresponding to the name and return status zero (executing an assignment as the last statement is usually sufficient), or it should return status non-zero. In the former case the element of reply is used as the directory; in the latter case the substitution is deemed to have failed. If all functions fail and the option <code>NOMATCH</code> is set, an error results. </p>
<p> The functions defined as above are also used to see if a directory can be turned into a name, for example when printing the directory stack or when expanding <code>%~</code> in prompts. In this case each function is passed two arguments: the string <code>d</code> (for directory) and the candidate for dynamic naming. The function should either return non-zero status, if the directory cannot be named by the function, or it should set the array reply to consist of two elements: the first is the dynamic name for the directory (as would appear within `<code>~[</code><i>...</i><code>]</code>&#8216;), and the second is the prefix length of the directory to be replaced. For example, if the trial directory is <code>/home/myname/src/zsh</code> and the dynamic name for <code>/home/myname/src</code> (which has 16 characters) is <code>s</code>, then the function sets </p>
<dl>
<dd> <pre><code>
 reply=(s 16) 
</code></pre>
 </dd></dl>
<p> The directory name so returned is compared with possible static names for parts of the directory path, as described below; it is used if the prefix length matched (16 in the example) is longer than that matched by any static name. </p>
<p> It is not a requirement that a function implements both <code>n</code> and <code>d</code> calls; for example, it might be appropriate for certain dynamic forms of expansion not to be contracted to names. In that case any call with the first argument <code>d</code> should cause a non-zero status to be returned. </p>
<p> The completion system calls `<code>zsh_directory_name c</code>&#8216; followed by equivalent calls to elements of the array <code>zsh_directory_name_functions</code>, if it exists, in order to complete dynamic names for directories. The code for this should be as for any other completion function as described in <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1). </p>
<p> As a working example, here is a function that expands any dynamic names beginning with the string <code>p:</code> to directories below <code>/home/pws/perforce</code>. In this simple case a static name for the directory would be just as effective. </p>
<dl>
<dd> <pre><code>
 zsh_directory_name() {
  emulate -L zsh
  setopt extendedglob
  local -a match mbegin mend
  if [[ $1 = d ]]; then
    # turn the directory into a name
    if [[ $2 = (#b)(/home/pws/perforce/)([^/]##)* ]]; then
      typeset -ga reply
      reply=(p:$match[2] $(( ${#match[1]} + ${#match[2]} )) )
    else
      return 1
    fi
  elif [[ $1 = n ]]; then
    # turn the name into a directory
    [[ $2 != (#b)p:(?*) ]] &amp;&amp; return 1
    typeset -ga reply
    reply=(/home/pws/perforce/$match[1])
  elif [[ $1 = c ]]; then
    # complete names
    local expl
    local -a dirs
    dirs=(/home/pws/perforce/*(/:t))
    dirs=(p:${^dirs})
    _wanted dynamic-dirs expl 'dynamic directory' compadd -S\] -a dirs
    return
  else
    return 1
  fi
  return 0
} 
</code></pre>
 </dd></dl>
<h3>Static named directories</h3>
<p> A `<code>~</code>&#8216; followed by anything not already covered consisting of any number of alphanumeric characters or underscore (`<code>_</code>&#8216;), hyphen (`<code>-</code>&#8216;), or dot (`<code>.</code>&#8216;) is looked up as a named directory, and replaced by the value of that named directory if found. Named directories are typically home directories for users on the system. They may also be defined if the text after the `<code>~</code>&#8216; is the name of a string shell parameter whose value begins with a `<code>/</code>&#8216;. Note that trailing slashes will be removed from the path to the directory (though the original parameter is not modified). </p>
<p> It is also possible to define directory names using the <code>-d</code> option to the <code>hash</code> builtin. </p>
<p> When the shell prints a path (e.g. when expanding <code>%~</code> in prompts or when printing the directory stack), the path is checked to see if it has a named directory as its prefix. If so, then the prefix portion is replaced with a `<code>~</code>&#8216; followed by the name of the directory. The shorter of the two ways of referring to the directory is used, i.e. either the directory name or the full path; the name is used if they are the same length. The parameters <code>$PWD</code> and <code>$OLDPWD</code> are never abbreviated in this fashion. </p>
<h3>`=' expansion</h3>
<p> If a word begins with an unquoted `<code>=</code>&#8216; and the <code>EQUALS</code> option is set, the remainder of the word is taken as the name of a command. If a command exists by that name, the word is replaced by the full pathname of the command. </p>
<h3>Notes</h3>
<p> Filename expansion is performed on the right hand side of a parameter assignment, including those appearing after commands of the <code>typeset</code> family. In this case, the right hand side will be treated as a colon-separated list in the manner of the <code>PATH</code> parameter, so that a `<code>~</code>&#8216; or an `<code>=</code>&#8216; following a `<code>:</code>&#8216; is eligible for expansion. All such behaviour can be disabled by quoting the `<code>~</code>&#8216;, the `<code>=</code>&#8216;, or the whole expression (but not simply the colon); the <code>EQUALS</code> option is also respected. </p>
<p> If the option <code>MAGIC_EQUAL_SUBST</code> is set, any unquoted shell argument in the form `<i>identifier</i><code>=</code><i>expression</i>&#8216; becomes eligible for file expansion as described in the previous paragraph. Quoting the first `<code>=</code>&#8216; also inhibits this. </p>
<h2>FILENAME GENERATION</h2>
<p> If a word contains an unquoted instance of one of the characters `<code>*</code>&#8216;, `<code>(</code>&#8216;, `<code>|</code>&#8216;, `<code>&lt;</code>&#8216;, `<code>[</code>&#8216;, or `<code>?</code>&#8216;, it is regarded as a pattern for filename generation, unless the <code>GLOB</code> option is unset. If the <code>EXTENDED_GLOB</code> option is set, the `<code>^</code>&#8216; and `<code>#</code>&#8216; characters also denote a pattern; otherwise they are not treated specially by the shell. </p>
<p> The word is replaced with a list of sorted filenames that match the pattern. If no matching pattern is found, the shell gives an error message, unless the <code>NULL_GLOB</code> option is set, in which case the word is deleted; or unless the <code>NOMATCH</code> option is unset, in which case the word is left unchanged. </p>
<p> In filename generation, the character `<code>/</code>&#8216; must be matched explicitly; also, a `<code>.</code>&#8216; must be matched explicitly at the beginning of a pattern or after a `<code>/</code>&#8216;, unless the <code>GLOB_DOTS</code> option is set. No filename generation pattern matches the files `<code>.</code>&#8216; or `<code>..</code>&#8216;. In other instances of pattern matching, the `<code>/</code>&#8216; and `<code>.</code>&#8216; are not treated specially.  </p>
<h3>Glob Operators</h3>
<dl>
<dd> <p> <code>*</code> Matches any string, including the null string. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Matches any character. </p>
 </dd>
<dt><code>[</code>...<code>]</code></dt>
<dd> <p> Matches any of the enclosed characters. Ranges of characters can be specified by separating two characters by a `<code>-</code>&#8216;. A `<code>-</code>&#8216; or `<code>]</code>&#8216; may be matched by including it as the first character in the list. There are also several named classes of characters, in the form `<code>[:</code><i>name</i><code>:]</code>&#8216; with the following meanings. The first set use the macros provided by the operating system to test for the given character combinations, including any modifications due to local language settings, see <i>ctype</i>(3): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>[:alnum:]</code> The character is alphanumeric </p>
 </dd>
<dt><code>[:alpha:]</code></dt>
<dd> <p> The character is alphabetic </p>
 </dd>
<dt><code>[:ascii:]</code></dt>
<dd> <p> The character is 7-bit, i.e. is a single-byte character without the top bit set. </p>
 </dd>
<dt><code>[:blank:]</code></dt>
<dd> <p> The character is a blank character </p>
 </dd>
<dt><code>[:cntrl:]</code></dt>
<dd> <p> The character is a control character </p>
 </dd>
<dt><code>[:digit:]</code></dt>
<dd> <p> The character is a decimal digit </p>
 </dd>
<dt><code>[:graph:]</code></dt>
<dd> <p> The character is a printable character other than whitespace </p>
 </dd>
<dt><code>[:lower:]</code></dt>
<dd> <p> The character is a lowercase letter </p>
 </dd>
<dt><code>[:print:]</code></dt>
<dd> <p> The character is printable </p>
 </dd>
<dt><code>[:punct:]</code></dt>
<dd> <p> The character is printable but neither alphanumeric nor whitespace </p>
 </dd>
<dt><code>[:space:]</code></dt>
<dd> <p> The character is whitespace </p>
 </dd>
<dt><code>[:upper:]</code></dt>
<dd> <p> The character is an uppercase letter </p>
 </dd>
<dt><code>[:xdigit:]</code></dt>
<dd> <p> The character is a hexadecimal digit </p>
 </dd></dl>
<p> Another set of named classes is handled internally by the shell and is not sensitive to the locale: </p>
<dl>
<dd> <p> <code>[:IDENT:]</code> The character is allowed to form part of a shell identifier, such as a parameter name </p>
 </dd>
<dt><code>[:IFS:]</code></dt>
<dd> <p> The character is used as an input field separator, i.e. is contained in the <code>IFS</code> parameter </p>
 </dd>
<dt><code>[:IFSSPACE:]</code></dt>
<dd> <p> The character is an IFS white space character; see the documentation for <code>IFS</code> in the <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1) manual page. </p>
 </dd>
<dt><code>[:INCOMPLETE:]</code></dt>
<dd> <p> Matches a byte that starts an incomplete multibyte character. Note that there may be a sequence of more than one bytes that taken together form the prefix of a multibyte character. To test for a potentially incomplete byte sequence, use the pattern `<code>[[:INCOMPLETE:]]*</code>&#8216;. This will never match a sequence starting with a valid multibyte character. </p>
 </dd>
<dt><code>[:INVALID:]</code></dt>
<dd> <p> Matches a byte that does not start a valid multibyte character. Note this may be a continuation byte of an incomplete multibyte character as any part of a multibyte string consisting of invalid and incomplete multibyte characters is treated as single bytes. </p>
 </dd>
<dt><code>[:WORD:]</code></dt>
<dd> <p> The character is treated as part of a word; this test is sensitive to the value of the <code>WORDCHARS</code> parameter </p>
 </dd></dl>
<p> Note that the square brackets are additional to those enclosing the whole set of characters, so to test for a single alphanumeric character you need `<code>[[:alnum:]]</code>&#8216;. Named character sets can be used alongside other types, e.g. `<code>[[:alpha:]0-9]</code>&#8216;. </dl>
 </p>
<dd> <p> <code>[^</code>...<code>]</code> </p>
 </dd>
<dd> <p> <code>[!</code>...<code>]</code> Like <code>[</code>...<code>]</code>, except that it matches any character which is not in the given set. </p>
 </dd>
<dt><code>&lt;</code>[<i>x</i>]<code>-</code>[<i>y</i>]<code>&gt;</code></dt>
<dd> <p> Matches any number in the range <i>x</i> to <i>y</i>, inclusive. Either of the numbers may be omitted to make the range open-ended; hence `<code>&lt;-&gt;</code>&#8216; matches any number. To match individual digits, the <code>[</code>...<code>]</code> form is more efficient. </p>
 </dd>
<dl>
<dd> <p> Be careful when using other wildcards adjacent to patterns of this form; for example, <code>&lt;0-9&gt;*</code> will actually match any number whatsoever at the start of the string, since the `<code>&lt;0-9&gt;</code>&#8216; will match the first digit, and the `<code>*</code>&#8216; will match any others. This is a trap for the unwary, but is in fact an inevitable consequence of the rule that the longest possible match always succeeds. Expressions such as `<code>&lt;0-9&gt;[^[:digit:]]*</code>&#8216; can be used instead. </p>
 </dd></dl>
<dt><code>(</code>...<code>)</code></dt>
<dd> <p> Matches the enclosed pattern. This is used for grouping. If the <code>KSH_GLOB</code> option is set, then a `<code>@</code>&#8216;, `<code>*</code>&#8216;, `<code>+</code>&#8216;, `<code>?</code>&#8216; or `<code>!</code>&#8216; immediately preceding the `<code>(</code>&#8216; is treated specially, as detailed below. The option <code>SH_GLOB</code> prevents bare parentheses from being used in this way, though the <code>KSH_GLOB</code> option is still available. </p>
 </dd>
<dl>
<dd> <p> Note that grouping cannot extend over multiple directories: it is an error to have a `<code>/</code>&#8216; within a group (this only applies for patterns used in filename generation). There is one exception: a group of the form <code>(</code><i>pat</i><code>/)#</code> appearing as a complete path segment can match a sequence of directories. For example, <code>foo/(a*/)#bar</code> matches <code>foo/bar</code>, <code>foo/any/bar</code>, <code>foo/any/anyother/bar</code>, and so on. </p>
 </dd></dl>
<dt><i>x</i><code>|</code><i>y</i></dt>
<dd> <p> Matches either <i>x</i> or <i>y</i>. This operator has lower precedence than any other. The `<code>|</code>&#8216; character must be within parentheses, to avoid interpretation as a pipeline. The alternatives are tried in order from left to right. </p>
 </dd>
<dt><code>^</code><i>x</i></dt>
<dd> <p> (Requires <code>EXTENDED_GLOB</code> to be set.) Matches anything except the pattern <i>x</i>. This has a higher precedence than `<code>/</code>&#8216;, so `<code>^foo/bar</code>&#8216; will search directories in `<code>.</code>&#8216; except `<code>./foo</code>&#8216; for a file named `<code>bar</code>&#8216;. </p>
 </dd>
<dt><i>x</i><code>~</code><i>y</i></dt>
<dd> <p> (Requires <code>EXTENDED_GLOB</code> to be set.) Match anything that matches the pattern <i>x</i> but does not match <i>y</i>. This has lower precedence than any operator except `<code>|</code>&#8216;, so `<code>*/*~foo/bar</code>&#8216; will search for all files in all directories in `<code>.</code>&#8216; and then exclude `<code>foo/bar</code>&#8216; if there was such a match. Multiple patterns can be excluded by `<i>foo</i><code>~</code><i>bar</i><code>~</code><i>baz</i>&#8216;. In the exclusion pattern (<i>y</i>), `<code>/</code>&#8216; and `<code>.</code>&#8216; are not treated specially the way they usually are in globbing. </p>
 </dd>
<dt><i>x</i><code>#</code></dt>
<dd> <p> (Requires <code>EXTENDED_GLOB</code> to be set.) Matches zero or more occurrences of the pattern <i>x</i>. This operator has high precedence; `<code>12#</code>&#8216; is equivalent to `<code>1(2#)</code>&#8216;, rather than `<code>(12)#</code>&#8216;. It is an error for an unquoted `<code>#</code>&#8216; to follow something which cannot be repeated; this includes an empty string, a pattern already followed by `<code>##</code>&#8216;, or parentheses when part of a <code>KSH_GLOB</code> pattern (for example, `<code>!(</code><i>foo</i><code>)#</code>&#8216; is invalid and must be replaced by `<code>*(!(</code><i>foo</i><code>))</code>&#8216;). </p>
 </dd>
<dt><i>x</i><code>##</code></dt>
<dd> <p> (Requires <code>EXTENDED_GLOB</code> to be set.) Matches one or more occurrences of the pattern <i>x</i>. This operator has high precedence; `<code>12##</code>&#8216; is equivalent to `<code>1(2##)</code>&#8216;, rather than `<code>(12)##</code>&#8216;. No more than two active `<code>#</code>&#8216; characters may appear together. (Note the potential clash with glob qualifiers in the form `<code>1(2##)</code>&#8216; which should therefore be avoided.) </p>
 </dd></dl>
<h3>ksh-like Glob Operators</h3>
<p> If the <code>KSH_GLOB</code> option is set, the effects of parentheses can be modified by a preceding `<code>@</code>&#8216;, `<code>*</code>&#8216;, `<code>+</code>&#8216;, `<code>?</code>&#8216; or `<code>!</code>&#8216;. This character need not be unquoted to have special effects, but the `<code>(</code>&#8216; must be. </p>
<dl>
<dd> <p> <code>@(</code>...<code>)</code> Match the pattern in the parentheses. (Like `<code>(</code>...<code>)</code>&#8216;.) </p>
 </dd>
<dt><code>*(</code>...<code>)</code></dt>
<dd> <p> Match any number of occurrences. (Like `<code>(</code>...<code>)#</code>&#8216;, except that recursive directory searching is not supported.) </p>
 </dd>
<dt><code>+(</code>...<code>)</code></dt>
<dd> <p> Match at least one occurrence. (Like `<code>(</code>...<code>)##</code>&#8216;, except that recursive directory searching is not supported.) </p>
 </dd>
<dt><code>?(</code>...<code>)</code></dt>
<dd> <p> Match zero or one occurrence. (Like `<code>(|</code>...<code>)</code>&#8216;.) </p>
 </dd>
<dt><code>!(</code>...<code>)</code></dt>
<dd> <p> Match anything but the expression in parentheses. (Like `<code>(^(</code>...<code>))</code>&#8216;.) </p>
 </dd></dl>
<h3>Precedence</h3>
<p> The precedence of the operators given above is (highest) `<code>^</code>&#8216;, `<code>/</code>&#8216;, `<code>~</code>&#8216;, `<code>|</code>&#8216; (lowest); the remaining operators are simply treated from left to right as part of a string, with `<code>#</code>&#8216; and `<code>##</code>&#8216; applying to the shortest possible preceding unit (i.e. a character, `<code>?</code>&#8216;, `<code>[</code>...<code>]</code>&#8216;, `<code>&lt;</code>...<code>&gt;</code>&#8216;, or a parenthesised expression). As mentioned above, a `<code>/</code>&#8216; used as a directory separator may not appear inside parentheses, while a `<code>|</code>&#8216; must do so; in patterns used in other contexts than filename generation (for example, in <code>case</code> statements and tests within `<code>[[</code>...<code>]]</code>&#8216;), a `<code>/</code>&#8216; is not special; and `<code>/</code>&#8216; is also not special after a `<code>~</code>&#8216; appearing outside parentheses in a filename pattern.  </p>
<h3>Globbing Flags</h3>
<p> There are various flags which affect any text to their right up to the end of the enclosing group or to the end of the pattern; they require the <code>EXTENDED_GLOB</code> option. All take the form <code>(#</code><i>X</i><code>)</code> where <i>X</i> may have one of the following forms: </p>
<dl>
<dd> <p> <code>i</code> Case insensitive: upper or lower case characters in the pattern match upper or lower case characters. </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> Lower case characters in the pattern match upper or lower case characters; upper case characters in the pattern still only match upper case characters. </p>
 </dd>
<dt><code>I</code></dt>
<dd> <p> Case sensitive: locally negates the effect of <code>i</code> or <code>l</code> from that point on. </p>
 </dd>
<dt><code>b</code></dt>
<dd> <p> Activate backreferences for parenthesised groups in the pattern; this does not work in filename generation. When a pattern with a set of active parentheses is matched, the strings matched by the groups are stored in the array <code>$match</code>, the indices of the beginning of the matched parentheses in the array <code>$mbegin</code>, and the indices of the end in the array <code>$mend</code>, with the first element of each array corresponding to the first parenthesised group, and so on. These arrays are not otherwise special to the shell. The indices use the same convention as does parameter substitution, so that elements of <code>$mend</code> and <code>$mbegin</code> may be used in subscripts; the <code>KSH_ARRAYS</code> option is respected. Sets of globbing flags are not considered parenthesised groups; only the first nine active parentheses can be referenced. </p>
 </dd>
<dl>
<dd> <p> For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 foo=&quot;a_string_with_a_message&quot;
if [[ $foo = (a|an)_(#b)(*) ]]; then
  print ${foo[$mbegin[1],$mend[1]]}
fi 
</code></pre>
 </dd></dl>
<p> prints `<code>string_with_a_message</code>&#8216;. Note that the first set of parentheses is before the <code>(#b)</code> and does not create a backreference. </p>
<p> Backreferences work with all forms of pattern matching other than filename generation, but note that when performing matches on an entire array, such as <code>${</code><i>array</i><code>#</code><i>pattern</i><code>}</code>, or a global substitution, such as <code>${</code><i>param</i><code>//</code><i>pat</i><code>/</code><i>repl</i><code>}</code>, only the data for the last match remains available. In the case of global replacements this may still be useful. See the example for the <code>m</code> flag below. </p>
<p> The numbering of backreferences strictly follows the order of the opening parentheses from left to right in the pattern string, although sets of parentheses may be nested. There are special rules for parentheses followed by `<code>#</code>&#8216; or `<code>##</code>&#8216;. Only the last match of the parenthesis is remembered: for example, in `<code>[[ abab = (#b)([ab])# ]]</code>&#8216;, only the final `<code>b</code>&#8216; is stored in <code>match[1]</code>. Thus extra parentheses may be necessary to match the complete segment: for example, use `<code>X((ab|cd)#)Y</code>&#8216; to match a whole string of either `<code>ab</code>&#8216; or `<code>cd</code>&#8216; between `<code>X</code>&#8216; and `<code>Y</code>&#8216;, using the value of <code>$match[1]</code> rather than <code>$match[2]</code>. </p>
<p> If the match fails none of the parameters is altered, so in some cases it may be necessary to initialise them beforehand. If some of the backreferences fail to match -- which happens if they are in an alternate branch which fails to match, or if they are followed by <code>#</code> and matched zero times -- then the matched string is set to the empty string, and the start and end indices are set to -1. </p>
<p> Pattern matching with backreferences is slightly slower than without. </dl>
 </p>
<dt><code>B</code></dt>
<dd> <p> Deactivate backreferences, negating the effect of the <code>b</code> flag from that point on. </p>
 </dd>
<dt><code>c</code><i>N</i><code>,</code><i>M</i></dt>
<dd> <p> The flag <code>(#c</code><i>N</i><code>,</code><i>M</i><code>)</code> can be used anywhere that the <code>#</code> or <code>##</code> operators can be used except in the expressions `<code>(*/)#</code>&#8216; and `<code>(*/)##</code>&#8216; in filename generation, where `<code>/</code>&#8216; has special meaning; it cannot be combined with other globbing flags and a bad pattern error occurs if it is misplaced. It is equivalent to the form <code>{</code><i>N</i><code>,</code><i>M</i><code>}</code> in regular expressions. The previous character or group is required to match between <i>N</i> and <i>M</i> times, inclusive. The form <code>(#c</code><i>N</i><code>)</code> requires exactly <code>N</code> matches; <code>(#c,</code><i>M</i><code>)</code> is equivalent to specifying <i>N</i> as 0; <code>(#c</code><i>N</i><code>,)</code> specifies that there is no maximum limit on the number of matches. </p>
 </dd>
<dt><code>m</code></dt>
<dd> <p> Set references to the match data for the entire string matched; this is similar to backreferencing and does not work in filename generation. The flag must be in effect at the end of the pattern, i.e. not local to a group. The parameters <code>$MATCH</code>, <code>$MBEGIN</code> and <code>$MEND</code> will be set to the string matched and to the indices of the beginning and end of the string, respectively. This is most useful in parameter substitutions, as otherwise the string matched is obvious. </p>
 </dd>
<dl>
<dd> <p> For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 arr=(veldt jynx grimps waqf zho buck)
print ${arr//(#m)[aeiou]/${(U)MATCH}} 
</code></pre>
 </dd></dl>
<p> forces all the matches (i.e. all vowels) into uppercase, printing `<code>vEldt jynx grImps wAqf zhO bUck</code>&#8216;. </p>
<p> Unlike backreferences, there is no speed penalty for using match references, other than the extra substitutions required for the replacement strings in cases such as the example shown. </dl>
 </p>
<dt><code>M</code></dt>
<dd> <p> Deactivate the <code>m</code> flag, hence no references to match data will be created. </p>
 </dd>
<dt><code>a</code><i>num</i></dt>
<dd> <p> Approximate matching: <i>num</i> errors are allowed in the string matched by the pattern. The rules for this are described in the next subsection. </p>
 </dd>
<dt><code>s</code>, <code>e</code></dt>
<dd> <p> Unlike the other flags, these have only a local effect, and each must appear on its own: `<code>(#s)</code>&#8216; and `<code>(#e)</code>&#8216; are the only valid forms. The `<code>(#s)</code>&#8216; flag succeeds only at the start of the test string, and the `<code>(#e)</code>&#8216; flag succeeds only at the end of the test string; they correspond to `<code>^</code>&#8216; and `<code>$</code>&#8216; in standard regular expressions. They are useful for matching path segments in patterns other than those in filename generation (where path segments are in any case treated separately). For example, `<code>*((#s)|/)test((#e)|/)*</code>&#8216; matches a path segment `<code>test</code>&#8216; in any of the following strings: <code>test</code>, <code>test/at/start</code>, <code>at/end/test</code>, <code>in/test/middle</code>. </p>
 </dd>
<dl>
<dd> <p> Another use is in parameter substitution; for example `<code>${array/(#s)A*Z(#e)}</code>&#8216; will remove only elements of an array which match the complete pattern `<code>A*Z</code>&#8216;. There are other ways of performing many operations of this type, however the combination of the substitution operations `<code>/</code>&#8216; and `<code>//</code>&#8216; with the `<code>(#s)</code>&#8216; and `<code>(#e)</code>&#8216; flags provides a single simple and memorable method. </p>
<p> Note that assertions of the form `<code>(^(#s))</code>&#8216; also work, i.e. match anywhere except at the start of the string, although this actually means `anything except a zero-length portion at the start of the string&#8217;; you need to use `<code>(&quot;&quot;~(#s))</code>&#8216; to match a zero-length portion of the string not at the start. </p>
 </dd></dl>
<dt><code>q</code></dt>
<dd> <p> A `<code>q</code>&#8216; and everything up to the closing parenthesis of the globbing flags are ignored by the pattern matching code. This is intended to support the use of glob qualifiers, see below. The result is that the pattern `<code>(#b)(*).c(#q.)</code>&#8216; can be used both for globbing and for matching against a string. In the former case, the `<code>(#q.)</code>&#8216; will be treated as a glob qualifier and the `<code>(#b)</code>&#8216; will not be useful, while in the latter case the `<code>(#b)</code>&#8216; is useful for backreferences and the `<code>(#q.)</code>&#8216; will be ignored. Note that colon modifiers in the glob qualifiers are also not applied in ordinary pattern matching. </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> Respect the current locale in determining the presence of multibyte characters in a pattern, provided the shell was compiled with <code>MULTIBYTE_SUPPORT</code>. This overrides the <code>MULTIBYTE</code> option; the default behaviour is taken from the option. Compare <code>U</code>. (Mnemonic: typically multibyte characters are from Unicode in the UTF-8 encoding, although any extension of ASCII supported by the system library may be used.) </p>
 </dd>
<dt><code>U</code></dt>
<dd> <p> All characters are considered to be a single byte long. The opposite of <code>u</code>. This overrides the <code>MULTIBYTE</code> option. </p>
 </dd></dl>
<p> For example, the test string <code>fooxx</code> can be matched by the pattern <code>(#i</code><code>)FOOXX</code>, but not by <code>(#l</code><code>)FOOXX</code>, <code>(#i</code><code>)FOO</code><code>(#I</code><code>)XX</code> or <code>((#i</code><code>)FOOX</code><code>)X</code>. The string <code>(#ia2</code><code>)readme</code> specifies case-insensitive matching of <code>readme</code> with up to two errors. </p>
<p> When using the ksh syntax for grouping both <code>KSH_GLOB</code> and <code>EXTENDED_GLOB</code> must be set and the left parenthesis should be preceded by <code>@</code>. Note also that the flags do not affect letters inside <code>[</code>...<code>]</code> groups, in other words <code>(#i</code><code>)[a-z]</code> still matches only lowercase letters. Finally, note that when examining whole paths case-insensitively every directory must be searched for all files which match, so that a pattern of the form <code>(#i</code><code>)/foo/bar/...</code> is potentially slow. </p>
<h3>Approximate Matching</h3>
<p> When matching approximately, the shell keeps a count of the errors found, which cannot exceed the number specified in the <code>(#a</code><i>num</i><code>)</code> flags. Four types of error are recognised: </p>
<dl>
<dd> <p> 1. Different characters, as in <code>fooxbar</code> and <code>fooybar</code>. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Transposition of characters, as in <code>banana</code> and <code>abnana</code>. </p>
 </dd>
<dt>3.</dt>
<dd> <p> A character missing in the target string, as with the pattern <code>road</code> and target string <code>rod</code>. </p>
 </dd>
<dt>4.</dt>
<dd> <p> An extra character appearing in the target string, as with <code>stove</code> and <code>strove</code>. </p>
 </dd></dl>
<p> Thus, the pattern <code>(#a3</code><code>)abcd</code> matches <code>dcba</code>, with the errors occurring by using the first rule twice and the second once, grouping the string as <code>[d][cb][a]</code> and <code>[a][bc][d]</code>. </p>
<p> Non-literal parts of the pattern must match exactly, including characters in character ranges: hence <code>(#a1</code><code>)???</code> matches strings of length four, by applying rule 4 to an empty part of the pattern, but not strings of length two, since all the <code>?</code> must match. Other characters which must match exactly are initial dots in filenames (unless the <code>GLOB_DOTS</code> option is set), and all slashes in filenames, so that <code>a/bc</code> is two errors from <code>ab/c</code> (the slash cannot be transposed with another character). Similarly, errors are counted separately for non-contiguous strings in the pattern, so that <code>(ab|cd</code><code>)ef</code> is two errors from <code>aebf</code>. </p>
<p> When using exclusion via the <code>~</code> operator, approximate matching is treated entirely separately for the excluded part and must be activated separately. Thus, <code>(#a1</code><code>)README~READ_ME</code> matches <code>READ.ME</code> but not <code>READ_ME</code>, as the trailing <code>READ_ME</code> is matched without approximation. However, <code>(#a1</code><code>)README~(#a1</code><code>)READ_ME</code> does not match any pattern of the form <code>READ</code><i>?</i><code>ME</code> as all such forms are now excluded. </p>
<p> Apart from exclusions, there is only one overall error count; however, the maximum errors allowed may be altered locally, and this can be delimited by grouping. For example, <code>(#a1</code><code>)cat</code><code>((#a0</code><code>)dog</code><code>)fox</code> allows one error in total, which may not occur in the <code>dog</code> section, and the pattern <code>(#a1</code><code>)cat</code><code>(#a0</code><code>)dog</code><code>(#a1</code><code>)fox</code> is equivalent. Note that the point at which an error is first found is the crucial one for establishing whether to use approximation; for example, <code>(#a1)abc(#a0)xyz</code> will not match <code>abcdxyz</code>, because the error occurs at the `<code>x</code>&#8216;, where approximation is turned off. </p>
<p> Entire path segments may be matched approximately, so that `<code>(#a1)/foo/d/is/available/at/the/bar</code>&#8216; allows one error in any path segment. This is much less efficient than without the <code>(#a1)</code>, however, since every directory in the path must be scanned for a possible approximate match. It is best to place the <code>(#a1)</code> after any path segments which are known to be correct. </p>
<h3>Recursive Globbing</h3>
<p> A pathname component of the form `<code>(</code><i>foo</i><code>/)#</code>&#8216; matches a path consisting of zero or more directories matching the pattern <i>foo</i>. </p>
<p> As a shorthand, `<code>**/</code>&#8216; is equivalent to `<code>(*/)#</code>&#8216;; note that this therefore matches files in the current directory as well as subdirectories. Thus: </p>
<dl>
<dd> <pre><code>
 ls -ld -- (*/)#bar 
</code></pre>
 </dd></dl>
<p> or </p>
<dl>
<dd> <pre><code>
 ls -ld -- **/bar 
</code></pre>
 </dd></dl>
<p> does a recursive directory search for files named `<code>bar</code>&#8216; (potentially including the file `<code>bar</code>&#8216; in the current directory). This form does not follow symbolic links; the alternative form `<code>***/</code>&#8216; does, but is otherwise identical. Neither of these can be combined with other forms of globbing within the same path segment; in that case, the `<code>*</code>&#8216; operators revert to their usual effect. </p>
<p> Even shorter forms are available when the option <code>GLOB_STAR_SHORT</code> is set. In that case if no <code>/</code> immediately follows a <code>**</code> or <code>***</code> they are treated as if both a <code>/</code> plus a further <code>*</code> are present. Hence: </p>
<dl>
<dd> <pre><code>
 setopt GLOBSTARSHORT
ls -ld -- **.c 
</code></pre>
 </dd></dl>
<p> is equivalent to </p>
<dl>
<dd> <pre><code>
 ls -ld -- **/*.c 
</code></pre>
 </dd></dl>
<h3>Glob Qualifiers</h3>
<p> Patterns used for filename generation may end in a list of qualifiers enclosed in parentheses. The qualifiers specify which filenames that otherwise match the given pattern will be inserted in the argument list. </p>
<p> If the option <code>BARE_GLOB_QUAL</code> is set, then a trailing set of parentheses containing no `<code>|</code>&#8216; or `<code>(</code>&#8216; characters (or `<code>~</code>&#8216; if it is special) is taken as a set of glob qualifiers. A glob subexpression that would normally be taken as glob qualifiers, for example `<code>(^x)</code>&#8216;, can be forced to be treated as part of the glob pattern by doubling the parentheses, in this case producing `<code>((^x))</code>&#8216;. </p>
<p> If the option <code>EXTENDED_GLOB</code> is set, a different syntax for glob qualifiers is available, namely `<code>(#q</code><i>x</i><code>)</code>&#8216; where <i>x</i> is any of the same glob qualifiers used in the other format. The qualifiers must still appear at the end of the pattern. However, with this syntax multiple glob qualifiers may be chained together. They are treated as a logical AND of the individual sets of flags. Also, as the syntax is unambiguous, the expression will be treated as glob qualifiers just as long any parentheses contained within it are balanced; appearance of `<code>|</code>&#8216;, `<code>(</code>&#8216; or `<code>~</code>&#8216; does not negate the effect. Note that qualifiers will be recognised in this form even if a bare glob qualifier exists at the end of the pattern, for example `<code>*(#q*)(.)</code>&#8216; will recognise executable regular files if both options are set; however, mixed syntax should probably be avoided for the sake of clarity. Note that within conditions using the `<code>[[</code>&#8216; form the presence of a parenthesised expression <code>(#q</code><i>...</i><code>)</code> at the end of a string indicates that globbing should be performed; the expression may include glob qualifiers, but it is also valid if it is simply <code>(#q)</code>. This does not apply to the right hand side of pattern match operators as the syntax already has special significance. </p>
<p> A qualifier may be any one of the following: </p>
<dl>
<dd> <p> <code>/</code> directories </p>
 </dd>
<dt><code>F</code></dt>
<dd> <p> `full&#8217; (i.e. non-empty) directories. Note that the opposite sense <code>(^F</code><code>)</code> expands to empty directories and all non-directories. Use <code>(/^F</code><code>)</code> for empty directories. </p>
 </dd>
<dt><code>.</code></dt>
<dd> <p> plain files </p>
 </dd>
<dt><code>@</code></dt>
<dd> <p> symbolic links </p>
 </dd>
<dt><code>=</code></dt>
<dd> <p> sockets </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> named pipes (FIFOs) </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> executable plain files (0100 or 0010 or 0001) </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> device files (character or block special) </p>
 </dd>
<dt><code>%b</code></dt>
<dd> <p> block special files </p>
 </dd>
<dt><code>%c</code></dt>
<dd> <p> character special files </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> owner-readable files (0400) </p>
 </dd>
<dt><code>w</code></dt>
<dd> <p> owner-writable files (0200) </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> owner-executable files (0100) </p>
 </dd>
<dt><code>A</code></dt>
<dd> <p> group-readable files (0040) </p>
 </dd>
<dt><code>I</code></dt>
<dd> <p> group-writable files (0020) </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> group-executable files (0010) </p>
 </dd>
<dt><code>R</code></dt>
<dd> <p> world-readable files (0004) </p>
 </dd>
<dt><code>W</code></dt>
<dd> <p> world-writable files (0002) </p>
 </dd>
<dt><code>X</code></dt>
<dd> <p> world-executable files (0001) </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> setuid files (04000) </p>
 </dd>
<dt><code>S</code></dt>
<dd> <p> setgid files (02000) </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> files with the sticky bit (01000) </p>
 </dd>
<dt><code>f</code><i>spec</i></dt>
<dd> <p> files with access rights matching <i>spec</i>. This <i>spec</i> may be a octal number optionally preceded by a `<code>=</code>&#8216;, a `<code>+</code>&#8216;, or a `<code>-</code>&#8216;. If none of these characters is given, the behavior is the same as for `<code>=</code>&#8216;. The octal number describes the mode bits to be expected, if combined with a `<code>=</code>&#8216;, the value given must match the file-modes exactly, with a `<code>+</code>&#8216;, at least the bits in the given number must be set in the file-modes, and with a `<code>-</code>&#8216;, the bits in the number must not be set. Giving a `<code>?</code>&#8216; instead of a octal digit anywhere in the number ensures that the corresponding bits in the file-modes are not checked, this is only useful in combination with `<code>=</code>&#8216;. </p>
 </dd>
<dl>
<dd> <p> If the qualifier `<code>f</code>&#8216; is followed by any other character anything up to the next matching character (`<code>[</code>&#8216;, `<code>{</code>&#8216;, and `<code>&lt;</code>&#8216; match `<code>]</code>&#8216;, `<code>}</code>&#8216;, and `<code>&gt;</code>&#8216; respectively, any other character matches itself) is taken as a list of comma-separated <i>sub-spec</i>s. Each <i>sub-spec</i> may be either an octal number as described above or a list of any of the characters `<code>u</code>&#8216;, `<code>g</code>&#8216;, `<code>o</code>&#8216;, and `<code>a</code>&#8216;, followed by a `<code>=</code>&#8216;, a `<code>+</code>&#8216;, or a `<code>-</code>&#8216;, followed by a list of any of the characters `<code>r</code>&#8216;, `<code>w</code>&#8216;, `<code>x</code>&#8216;, `<code>s</code>&#8216;, and `<code>t</code>&#8216;, or an octal digit. The first list of characters specify which access rights are to be checked. If a `<code>u</code>&#8216; is given, those for the owner of the file are used, if a `<code>g</code>&#8216; is given, those of the group are checked, a `<code>o</code>&#8216; means to test those of other users, and the `<code>a</code>&#8216; says to test all three groups. The `<code>=</code>&#8216;, `<code>+</code>&#8216;, and `<code>-</code>&#8216; again says how the modes are to be checked and have the same meaning as described for the first form above. The second list of characters finally says which access rights are to be expected: `<code>r</code>&#8216; for read access, `<code>w</code>&#8216; for write access, `<code>x</code>&#8216; for the right to execute the file (or to search a directory), `<code>s</code>&#8216; for the setuid and setgid bits, and `<code>t</code>&#8216; for the sticky bit. </p>
<p> Thus, `<code>*(f70?)</code>&#8216; gives the files for which the owner has read, write, and execute permission, and for which other group members have no rights, independent of the permissions for other users. The pattern `<code>*(f-100)</code>&#8216; gives all files for which the owner does not have execute permission, and `<code>*(f:gu+w,o-rx:)</code>&#8216; gives the files for which the owner and the other members of the group have at least write permission, and for which other users don&#8217;t have read or execute permission. </p>
 </dd></dl>
<dd> <p> <code>e</code><i>string</i> </p>
 </dd>
<dd> <p> <code>+</code><i>cmd</i> The <i>string</i> will be executed as shell code. The filename will be included in the list if and only if the code returns a zero status (usually the status of the last command). </p>
 </dd>
<dl>
<dd> <p> In the first form, the first character after the `<code>e</code>&#8216; will be used as a separator and anything up to the next matching separator will be taken as the <i>string</i>; `<code>[</code>&#8216;, `<code>{</code>&#8216;, and `<code>&lt;</code>&#8216; match `<code>]</code>&#8216;, `<code>}</code>&#8216;, and `<code>&gt;</code>&#8216;, respectively, while any other character matches itself. Note that expansions must be quoted in the <i>string</i> to prevent them from being expanded before globbing is done. <i>string</i> is then executed as shell code. The string <code>globqual</code> is appended to the array <code>zsh_eval_context</code> the duration of execution. </p>
<p> During the execution of <i>string</i> the filename currently being tested is available in the parameter <code>REPLY</code>; the parameter may be altered to a string to be inserted into the list instead of the original filename. In addition, the parameter <code>reply</code> may be set to an array or a string, which overrides the value of <code>REPLY</code>. If set to an array, the latter is inserted into the command line word by word. </p>
<p> For example, suppose a directory contains a single file `<code>lonely</code>&#8216;. Then the expression `<code>*(e:&#8216;reply=(${REPLY}{1,2})&#8216;:)</code>&#8216; will cause the words `<code>lonely1</code>&#8216; and `<code>lonely2</code>&#8216; to be inserted into the command line. Note the quoting of <i>string</i>. </p>
<p> The form <code>+</code><i>cmd</i> has the same effect, but no delimiters appear around <i>cmd</i>. Instead, <i>cmd</i> is taken as the longest sequence of characters following the <code>+</code> that are alphanumeric or underscore. Typically <i>cmd</i> will be the name of a shell function that contains the appropriate test. For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 nt() { [[ $REPLY -nt $NTREF ]] }
NTREF=reffile
ls -ld -- *(+nt) 
</code></pre>
 </dd></dl>
<p> lists all files in the directory that have been modified more recently than <code>reffile</code>. </dl>
 </p>
<dt><code>d</code><i>dev</i></dt>
<dd> <p> files on the device <i>dev</i> </p>
 </dd>
<dt><code>l</code>[<code>-</code>|<code>+</code>]<i>ct</i></dt>
<dd> <p> files having a link count less than <i>ct</i> (<code>-</code>), greater than <i>ct</i> (<code>+</code>), or equal to <i>ct</i> </p>
 </dd>
<dt><code>U</code></dt>
<dd> <p> files owned by the effective user ID </p>
 </dd>
<dt><code>G</code></dt>
<dd> <p> files owned by the effective group ID </p>
 </dd>
<dt><code>u</code><i>id</i></dt>
<dd> <p> files owned by user ID <i>id</i> if that is a number. Otherwise, <i>id</i> specifies a user name: the character after the `<code>u</code>&#8216; will be taken as a separator and the string between it and the next matching separator will be taken as a user name. The starting separators `<code>[</code>&#8216;, `<code>{</code>&#8216;, and `<code>&lt;</code>&#8216; match the final separators `<code>]</code>&#8216;, `<code>}</code>&#8216;, and `<code>&gt;</code>&#8216;, respectively; any other character matches itself. The selected files are those owned by this user. For example, `<code>u:foo:</code>&#8216; or `<code>u[foo]</code>&#8216; selects files owned by user `<code>foo</code>&#8216;. </p>
 </dd>
<dt><code>g</code><i>id</i></dt>
<dd> <p> like <code>u</code><i>id</i> but with group IDs or names </p>
 </dd>
<dt><code>a</code>[<code>Mwhms</code>][<code>-</code>|<code>+</code>]<i>n</i></dt>
<dd> <p> files accessed exactly <i>n</i> days ago. Files accessed within the last <i>n</i> days are selected using a negative value for <i>n</i> (<code>-</code><i>n</i>). Files accessed more than <i>n</i> days ago are selected by a positive <i>n</i> value (<code>+</code><i>n</i>). Optional unit specifiers `<code>M</code>&#8216;, `<code>w</code>&#8216;, `<code>h</code>&#8216;, `<code>m</code>&#8216; or `<code>s</code>&#8216; (e.g. `<code>ah5</code>&#8216;) cause the check to be performed with months (of 30 days), weeks, hours, minutes or seconds instead of days, respectively. An explicit `<code>d</code>&#8216; for days is also allowed. </p>
 </dd>
<dl>
<dd> <p> Any fractional part of the difference between the access time and the current part in the appropriate units is ignored in the comparison. For instance, `<code>echo *(ah-5)</code>&#8216; would echo files accessed within the last five hours, while `<code>echo *(ah+5)</code>&#8216; would echo files accessed at least six hours ago, as times strictly between five and six hours are treated as five hours. </p>
 </dd></dl>
<dt><code>m</code>[<code>Mwhms</code>][<code>-</code>|<code>+</code>]<i>n</i></dt>
<dd> <p> like the file access qualifier, except that it uses the file modification time. </p>
 </dd>
<dt><code>c</code>[<code>Mwhms</code>][<code>-</code>|<code>+</code>]<i>n</i></dt>
<dd> <p> like the file access qualifier, except that it uses the file inode change time. </p>
 </dd>
<dt><code>L</code>[<code>+</code>|<code>-</code>]<i>n</i></dt>
<dd> <p> files less than <i>n</i> bytes (<code>-</code>), more than <i>n</i> bytes (<code>+</code>), or exactly <i>n</i> bytes in length. </p>
 </dd>
<dl>
<dd> <p> If this flag is directly followed by a <i>size specifier</i> `<code>k</code>&#8216; (`<code>K</code>&#8216;), `<code>m</code>&#8216; (`<code>M</code>&#8216;), or `<code>p</code>&#8216; (`<code>P</code>&#8216;) (e.g. `<code>Lk-50</code>&#8216;) the check is performed with kilobytes, megabytes, or blocks (of 512 bytes) instead. (On some systems additional specifiers are available for gigabytes, `<code>g</code>&#8216; or `<code>G</code>&#8216;, and terabytes, `<code>t</code>&#8216; or `<code>T</code>&#8216;.) If a size specifier is used a file is regarded as &quot;exactly&quot; the size if the file size rounded up to the next unit is equal to the test size. Hence `<code>*(Lm1)</code>&#8216; matches files from 1 byte up to 1 Megabyte inclusive. Note also that the set of files &quot;less than&quot; the test size only includes files that would not match the equality test; hence `<code>*(Lm-1)</code>&#8216; only matches files of zero size. </p>
 </dd></dl>
<dt><code>^</code></dt>
<dd> <p> negates all qualifiers following it </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> toggles between making the qualifiers work on symbolic links (the default) and the files they point to </p>
 </dd>
<dt><code>M</code></dt>
<dd> <p> sets the <code>MARK_DIRS</code> option for the current pattern </p>
 </dd>
<dt><code>T</code></dt>
<dd> <p> appends a trailing qualifier mark to the filenames, analogous to the <code>LIST_TYPES</code> option, for the current pattern (overrides <code>M</code>) </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> sets the <code>NULL_GLOB</code> option for the current pattern </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> sets the <code>GLOB_DOTS</code> option for the current pattern </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> sets the <code>NUMERIC_GLOB_SORT</code> option for the current pattern </p>
 </dd>
<dt><code>Y</code><i>n</i></dt>
<dd> <p> enables short-circuit mode: the pattern will expand to at most <i>n</i> filenames. If more than <i>n</i> matches exist, only the first <i>n</i> matches in directory traversal order will be considered. </p>
 </dd>
<dl>
<dd> <p> Implies <code>oN</code> when no <code>o</code><i>c</i> qualifier is used. </p>
 </dd></dl>
<dt><code>o</code><i>c</i></dt>
<dd> <p> specifies how the names of the files should be sorted. If <i>c</i> is <code>n</code> they are sorted by name; if it is <code>L</code> they are sorted depending on the size (length) of the files; if <code>l</code> they are sorted by the number of links; if <code>a</code>, <code>m</code>, or <code>c</code> they are sorted by the time of the last access, modification, or inode change respectively; if <code>d</code>, files in subdirectories appear before those in the current directory at each level of the search -- this is best combined with other criteria, for example `<code>odon</code>&#8216; to sort on names for files within the same directory; if <code>N</code>, no sorting is performed. Note that <code>a</code>, <code>m</code>, and <code>c</code> compare the age against the current time, hence the first name in the list is the youngest file. Also note that the modifiers <code>^</code> and <code>-</code> are used, so `<code>*(^-oL)</code>&#8216; gives a list of all files sorted by file size in descending order, following any symbolic links. Unless <code>oN</code> is used, multiple order specifiers may occur to resolve ties. </p>
 </dd>
<dl>
<dd> <p> The default sorting is <code>n</code> (by name) unless the <code>Y</code> glob qualifier is used, in which case it is <code>N</code> (unsorted). </p>
<p> <code>oe</code> and <code>o+</code> are special cases; they are each followed by shell code, delimited as for the <code>e</code> glob qualifier and the <code>+</code> glob qualifier respectively (see above). The code is executed for each matched file with the parameter <code>REPLY</code> set to the name of the file on entry and <code>globsort</code> appended to <code>zsh_eval_context</code>. The code should modify the parameter <code>REPLY</code> in some fashion. On return, the value of the parameter is used instead of the file name as the string on which to sort. Unlike other sort operators, <code>oe</code> and <code>o+</code> may be repeated, but note that the maximum number of sort operators of any kind that may appear in any glob expression is 12. </p>
 </dd></dl>
<dt><code>O</code><i>c</i></dt>
<dd> <p> like `<code>o</code>&#8216;, but sorts in descending order; i.e. `<code>*(^oc)</code>&#8216; is the same as `<code>*(Oc)</code>&#8216; and `<code>*(^Oc)</code>&#8216; is the same as `<code>*(oc)</code>&#8216;; `<code>Od</code>&#8216; puts files in the current directory before those in subdirectories at each level of the search. </p>
 </dd>
<dt><code>[</code><i>beg</i>[<code>,</code><i>end</i>]<code>]</code></dt>
<dd> <p> specifies which of the matched filenames should be included in the returned list. The syntax is the same as for array subscripts. <i>beg</i> and the optional <i>end</i> may be mathematical expressions. As in parameter subscripting they may be negative to make them count from the last match backward. E.g.: `<code>*(-OL[1,3])</code>&#8216; gives a list of the names of the three largest files. </p>
 </dd>
<dt><code>P</code><i>string</i></dt>
<dd> <p> The <i>string</i> will be prepended to each glob match as a separate word. <i>string</i> is delimited in the same way as arguments to the <code>e</code> glob qualifier described above. The qualifier can be repeated; the words are prepended separately so that the resulting command line contains the words in the same order they were given in the list of glob qualifiers. </p>
 </dd>
<dl>
<dd> <p> A typical use for this is to prepend an option before all occurrences of a file name; for example, the pattern `<code>*(P:-f:)</code>&#8216; produces the command line arguments `<code>-f</code> <i>file1</i> <code>-f</code> <i>file2</i> ...&#8216; </p>
<p> If the modifier <code>^</code> is active, then <i>string</i> will be appended instead of prepended. Prepending and appending is done independently so both can be used on the same glob expression; for example by writing `<code>*(P:foo:^P:bar:^P:baz:)</code>&#8216; which produces the command line arguments `<code>foo</code> <code>baz</code> <i>file1</i> <code>bar</code> ...&#8216; </p>
 </dd></dl>
</dl>
<p> More than one of these lists can be combined, separated by commas. The whole list matches if at least one of the sublists matches (they are `or&#8217;ed, the qualifiers in the sublists are `and&#8217;ed). Some qualifiers, however, affect all matches generated, independent of the sublist in which they are given. These are the qualifiers `<code>M</code>&#8216;, `<code>T</code>&#8216;, `<code>N</code>&#8216;, `<code>D</code>&#8216;, `<code>n</code>&#8216;, `<code>o</code>&#8216;, `<code>O</code>&#8216; and the subscripts given in brackets (`<code>[</code><i>...</i><code>]</code>&#8216;). </p>
<p> If a `<code>:</code>&#8216; appears in a qualifier list, the remainder of the expression in parenthesis is interpreted as a modifier (see the section `Modifiers&#8217; in the section `History Expansion&#8217;). Each modifier must be introduced by a separate `<code>:</code>&#8216;. Note also that the result after modification does not have to be an existing file. The name of any existing file can be followed by a modifier of the form `<code>(:</code><i>...</i><code>)</code>&#8216; even if no actual filename generation is performed, although note that the presence of the parentheses causes the entire expression to be subjected to any global pattern matching options such as <code>NULL_GLOB</code>. Thus: </p>
<dl>
<dd> <pre><code>
 ls -ld -- *(-/) 
</code></pre>
 </dd></dl>
<p> lists all directories and symbolic links that point to directories, and </p>
<dl>
<dd> <pre><code>
 ls -ld -- *(-@) 
</code></pre>
 </dd></dl>
<p> lists all broken symbolic links, and </p>
<dl>
<dd> <pre><code>
 ls -ld -- *(%W) 
</code></pre>
 </dd></dl>
<p> lists all world-writable device files in the current directory, and </p>
<dl>
<dd> <pre><code>
 ls -ld -- *(W,X) 
</code></pre>
 </dd></dl>
<p> lists all files in the current directory that are world-writable or world-executable, and </p>
<dl>
<dd> <pre><code>
 print -rC1 /tmp/foo*(u0^@:t) 
</code></pre>
 </dd></dl>
<p> outputs the basename of all root-owned files beginning with the string `<code>foo</code>&#8216; in <code>/tmp</code>, ignoring symlinks, and </p>
<dl>
<dd> <pre><code>
 ls -ld -- *.*~(lex|parse).[ch](^D^l1) 
</code></pre>
 </dd></dl>
<p> lists all files having a link count of one whose names contain a dot (but not those starting with a dot, since <code>GLOB_DOTS</code> is explicitly switched off) except for <code>lex.c</code>, <code>lex.h</code>, <code>parse.c</code> and <code>parse.h</code>. </p>
<dl>
<dd> <pre><code>
 print -rC1 b*.pro(#q:s/pro/shmo/)(#q.:s/builtin/shmiltin/) 
</code></pre>
 </dd></dl>
<p> demonstrates how colon modifiers and other qualifiers may be chained together. The ordinary qualifier `<code>.</code>&#8216; is applied first, then the colon modifiers in order from left to right. So if <code>EXTENDED_GLOB</code> is set and the base pattern matches the regular file <code>builtin.pro</code>, the shell will print `<code>shmiltin.shmo</code>&#8216;. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">HISTORY EXPANSION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAE">Overview</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Event Designators</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Word Designators</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Modifiers</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAI">PROCESS SUBSTITUTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">PARAMETER EXPANSION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAK">Parameter Expansion Flags</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Rules</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">Examples</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAN">COMMAND SUBSTITUTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">ARITHMETIC EXPANSION</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">BRACE EXPANSION</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">FILENAME EXPANSION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAR">Dynamic named directories</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">Static named directories</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">`=&#8216; expansion</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">Notes</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAV">FILENAME GENERATION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAW">Glob Operators</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">ksh-like Glob Operators</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">Precedence</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">Globbing Flags</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">Approximate Matching</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">Recursive Globbing</a></dt>
<dd>  </dd>
<dt><a href="#lbBC">Glob Qualifiers</a></dt>
<dd>  </dd></dl>
</dl>
