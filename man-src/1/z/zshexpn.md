---
title: "zshexpn(1)"
name: "zshexpn"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshexpn/"
description: "zshexpn – zsh expansion and substitution"
---

<h2 class="name">NAME</h2>
<p> zshexpn &#8211; zsh expansion and substitution </p>
<h2>DESCRIPTION</h2>
<p> The following types of expansions are performed in the indicated order in five steps: </p>
<dl>
<dt>
<dd> <i>History Expansion</i> This is performed only in interactive shells.</p>
<dt><i>Alias Expansion</i></p>
<dd> Aliases are expanded immediately before the command line is parsed as explained under Aliasing in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dt>
<dd> <i>Process Substitution</i></p>
<dt>
<dd> <i>Parameter Expansion</i></p>
<dt>
<dd> <i>Command Substitution</i></p>
<dt>
<dd> <i>Arithmetic Expansion</i></p>
<dt>
<dd> <i>Brace Expansion</i> These five are performed in left-to-right fashion. On each argument, any of the five steps that are needed are performed one after the other. Hence, for example, all the parts of parameter expansion are completed before command substitution is started. After these expansions, all unquoted occurrences of the characters `<code>\</code>&#8216;,`<code>&#8216;</code>&#8216; and `<code>&quot;</code>&#8216; are removed.</p>
<dt><i>Filename Expansion</i></p>
<dd> If the <code>SH_FILE_EXPANSION</code> option is set, the order of expansion is modified for compatibility with <code>sh</code> and <code>ksh</code>. In that case <i>filename expansion</i> is performed immediately after <i>alias expansion</i>, preceding the set of five expansions mentioned above.</p>
<dt><i>Filename Generation</i></p>
<dd> This expansion, commonly referred to as <code>globbing</code>, is always done last.</dl>
<p> The following sections explain the types of expansion in detail. </p>
<h2>HISTORY EXPANSION</h2>
<p> History expansion allows you to use words from previous command lines in the command line you are typing. This simplifies spelling corrections and the repetition of complicated commands or arguments. </p>
<p> Immediately before execution, each command is saved in the history list, the size of which is controlled by the <code>HISTSIZE</code> parameter. The one most recent command is always retained in any case. Each saved command in the history list is called a history <i>event</i> and is assigned a number, beginning with 1 (one) when the shell starts up. The history number that you may see in your prompt (see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)) is the number that is to be assigned to the <i>next</i> command. </p>
<h3>Overview</h3>
<p> A history expansion begins with the first character of the <code>histchars</code> parameter, which is `<code>!</code>&#8216; by default, and may occur anywhere on the command line, including inside double quotes (but not inside single quotes <code>&#8216;&#8230;&#8217;</code> or C-style quotes <code>$&#8217;&#8230;&#8217;</code> nor when escaped with a backslash). </p>
<p> The first character is followed by an optional event designator (see the section `Event Designators&#8217;) and then an optional word designator (the section `Word Designators&#8217;); if neither of these designators is present, no history expansion occurs. </p>
<p> Input lines containing history expansions are echoed after being expanded, but before any other expansions take place and before the command is executed. It is this expanded form that is recorded as the history event for later references. </p>
<p> History expansions do not nest. </p>
<p> By default, a history reference with no event designator refers to the same event as any preceding history reference on that command line; if it is the only history reference in a command, it refers to the previous command. However, if the option <code>CSH_JUNKIE_HISTORY</code> is set, then every history reference with no event specification <i>always</i> refers to the previous command. </p>
<p> For example, `<code>!</code>&#8216; is the event designator for the previous command, so `<code>!!:1</code>&#8216; always refers to the first word of the previous command, and `<code>!!$</code>&#8216; always refers to the last word of the previous command. With <code>CSH_JUNKIE_HISTORY</code> set, then `<code>!:1</code>&#8216; and `<code>!$</code>&#8216; function in the same manner as `<code>!!:1</code>&#8216; and `<code>!!$</code>&#8216;, respectively. Conversely, if <code>CSH_JUNKIE_HISTORY</code> is unset, then `<code>!:1</code>&#8216; and `<code>!$</code>&#8216; refer to the first and last words, respectively, of the same event referenced by the nearest other history reference preceding them on the current command line, or to the previous command if there is no preceding reference. </p>
<p> The character sequence `<code>^</code><i>foo</i><code>^</code><i>bar</i>&#8216; (where `<code>^</code>&#8216; is actually the second character of the <code>histchars</code> parameter) repeats the last command, replacing the string <i>foo</i> with <i>bar</i>. More precisely, the sequence `<code>^</code><i>foo</i><code>^</code><i>bar</i><code>^</code>&#8216; is synonymous with `<code>!!:s</code><code>^</code><i>foo</i><code>^</code><i>bar</i><code>^</code>&#8216;, hence other modifiers (see the section `Modifiers&#8217;) may follow the final `<code>^</code>&#8216;. In particular, `<code>^</code><i>foo</i><code>^</code><i>bar</i><code>^:G</code>&#8216; performs a global substitution. </p>
<p> If the shell encounters the character sequence `<code>!&quot;</code>&#8216; in the input, the history mechanism is temporarily disabled until the current list (see <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)) is fully parsed. The `<code>!&quot;</code>&#8216; is removed from the input, and any subsequent `<code>!</code>&#8216; characters have no special significance. </p>
<p> A less convenient but more comprehensible form of command history support is provided by the <code>fc</code> builtin.</p>
<h3>Event Designators</h3>
<p> An event designator is a reference to a command-line entry in the history list. In the list below, remember that the initial <code>`!&#8217;</code> in each item may be changed to another character by setting the <code>histchars</code> parameter. </p>
<dl>
<dt>
<dd> <code>!</code> Start a history expansion, except when followed by a blank, newline, `<code>=</code>&#8216; or `<code>(</code>&#8216;. If followed immediately by a word designator (see the section `Word Designators&#8217;), this forms a history reference with no event designator (see the section `Overview&#8217;).</p>
<dt><code>!!</code></p>
<dd> Refer to the previous command. By itself, this expansion repeats the previous command.</p>
<dt><code>!</code><i>n</i></p>
<dd> Refer to command-line <i>n</i>.</p>
<dt><code>!-</code><i>n</i></p>
<dd> Refer to the current command-line minus <i>n</i>.</p>
<dt><code>!</code><i>str</i></p>
<dd> Refer to the most recent command starting with <i>str</i>.</p>
<dt><code>!?</code><i>str</i>[<code>?</code>]</p>
<dd> Refer to the most recent command containing <i>str</i>. The trailing `<code>?</code>&#8216; is necessary if this reference is to be followed by a modifier or followed by any text that is not to be considered part of <i>str</i>.</p>
<dt><code>!#</code></p>
<dd> Refer to the current command line typed in so far. The line is treated as if it were complete up to and including the word before the one with the `<code>!#</code>&#8216; reference.</p>
<dt><code>!{</code>&#8230;<code>}</code></p>
<dd> Insulate a history reference from adjacent characters (if necessary).</dl>
<h3>Word Designators</h3>
<p> A word designator indicates which word or words of a given command line are to be included in a history reference. A `<code>:</code>&#8216; usually separates the event specification from the word designator. It may be omitted only if the word designator begins with a `<code>^</code>&#8216;, `<code>$</code>&#8216;, `<code>*</code>&#8216;, `<code>&#8211;</code>&#8216; or `<code>%</code>&#8216;. Word designators include: </p>
<dl>
<dt><code>0</code></p>
<dd> The first input word (command).</p>
<dt><i>n</i></p>
<dd> The <i>n</i>th argument.</p>
<dt><code>^</code></p>
<dd> The first argument. That is, <code>1</code>.</p>
<dt><code>$</code></p>
<dd> The last argument.</p>
<dt><code>%</code></p>
<dd> The word matched by (the most recent) <code>?</code><i>str</i> search.</p>
<dt><i>x</i><code>&#8211;</code><i>y</i></p>
<dd> A range of words; <i>x</i> defaults to <code>0</code>.</p>
<dt><code>*</code></p>
<dd> All the arguments, or a null value if there are none.</p>
<dt><i>x</i><code>*</code></p>
<dd> Abbreviates `<i>x</i><code>-$</code>&#8216;.</p>
<dt><i>x</i><code>&#8211;</code></p>
<dd> Like `<i>x</i><code>*</code>&#8216; but omitting word <code>$</code>.</dl>
<p> Note that a `<code>%</code>&#8216; word designator works only when used in one of `<code>!%</code>&#8216;, `<code>!:%</code>&#8216; or `<code>!?</code><i>str</i><code>?:%</code>&#8216;, and only when used after a <code>!?</code> expansion (possibly in an earlier command). Anything else results in an error, although the error may not be the most obvious one.</p>
<h3>Modifiers</h3>
<p> After the optional word designator, you can add a sequence of one or more of the following modifiers, each preceded by a `<code>:</code>&#8216;. These modifiers also work on the result of <i>filename generation</i> and <i>parameter expansion</i>, except where noted. </p>
<dl>
<dt>
<dd> <code>a</code> Turn a file name into an absolute path: prepends the current directory, if necessary; remove `<code>.</code>&#8216; path segments; and remove `<code>..</code>&#8216; path segments and the segments that immediately precede them.</p>
<dl>
<dt>
<dd>
<p> This transformation is agnostic about what is in the filesystem, i.e. is on the logical, not the physical directory. It takes place in the same manner as when changing directories when neither of the options <code>CHASE_DOTS</code> or <code>CHASE_LINKS</code> is set. For example, `<code>/before/here/../after</code>&#8216; is always transformed to `<code>/before/after</code>&#8216;, regardless of whether `<code>/before/here</code>&#8216; exists or what kind of object (dir, file, symlink, etc.) it is.</dl>
<dt><code>A</code></p>
<dd> Turn a file name into an absolute path as the `<code>a</code>&#8216; modifier does, and <i>then</i> pass the result through the <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code> library function to resolve symbolic links.</p>
<dl>
<dt>
<dd>
<p> Note: on systems that do not have a <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code> library function, symbolic links are not resolved, so on those systems `<code>a</code>&#8216; and `<code>A</code>&#8216; are equivalent. </p>
<p> Note: <code>foo:A</code> and <code>realpath(foo)</code> are different on some inputs. For <code>realpath(foo)</code> semantics, see the `<code>P</code>` modifier.</dl>
<dt><code>c</code></p>
<dd> Resolve a command name into an absolute path by searching the command path given by the <code>PATH</code> variable. This does not work for commands containing directory parts. Note also that this does not usually work as a glob qualifier unless a file of the same name is found in the current directory.</p>
<dt><code>e</code></p>
<dd> Remove all but the part of the filename extension following the `<code>.</code>&#8216;; see the definition of the filename extension in the description of the <code>r</code> modifier below. Note that according to that definition the result will be empty if the string ends with a `<code>.</code>&#8216;.</p>
<dt><code>h</code> [ <i>digits</i> ]</p>
<dd> Remove a trailing pathname component, shortening the path by one directory level: this is the `head&#8217; of the pathname. This works like `<code>dirname</code>&#8216;. If the <code>h</code> is followed immediately (with no spaces or other separator) by any number of decimal digits, and the value of the resulting number is non-zero, that number of leading components is preserved instead of the final component being removed. In an absolute path the leading `<code>/</code>&#8216; is the first component, so, for example, if <code>var=/my/path/to/something</code>, then <code>${var:h3}</code> substitutes <code>/my/path</code>. Consecutive `/&#8217;s are treated the same as a single `/&#8217;. In parameter substitution, digits may only be used if the expression is in braces, so for example the short form substitution <code>$var:h2</code> is treated as <code>${var:h}2</code>, not as <code>${var:h2}</code>. No restriction applies to the use of digits in history substitution or globbing qualifiers. If more components are requested than are present, the entire path is substituted (so this does not trigger a `failed modifier&#8217; error in history expansion).</p>
<dt><code>l</code></p>
<dd> Convert the words to all lowercase.</p>
<dt><code>p</code></p>
<dd> Print the new command but do not execute it. Only works with history expansion.</p>
<dt><code>P</code></p>
<dd> Turn a file name into an absolute path, like <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code>. The resulting path will be absolute, have neither `<code>.</code>&#8216; nor `<code>..</code>&#8216; components, and refer to the same directory entry as the input filename.</p>
<dl>
<dt>
<dd>
<p> Unlike <code><a href="/docs/linux/man/3-realpath/">realpath</a>(3)</code>, non-existent trailing components are permitted and preserved.</dl>
<dt><code>q</code></p>
<dd> Quote the substituted words, escaping further substitutions. Works with history expansion and parameter expansion, though for parameters it is only useful if the resulting text is to be re-evaluated such as by <code>eval</code>.</p>
<dt><code>Q</code></p>
<dd> Remove one level of quotes from the substituted words.</p>
<dt><code>r</code></p>
<dd> Remove a filename extension leaving the root name. Strings with no filename extension are not altered. A filename extension is a `<code>.</code>&#8216; followed by any number of characters (including zero) that are neither `<code>.</code>&#8216; nor `<code>/</code>&#8216; and that continue to the end of the string. For example, the extension of `<code>foo.orig.c</code>&#8216; is `<code>.c</code>&#8216;, and `<code>dir.c/foo</code>&#8216; has no extension.</p>
<dt><code>s/</code><i>l</i><code>/</code><i>r</i>[<code>/</code>]</p>
<dd> Substitute <i>r</i> for <i>l</i> as described below. The substitution is done only for the first string that matches <i>l</i>. For arrays and for filename generation, this applies to each word of the expanded text. See below for further notes on substitutions.</p>
<dl>
<dt>
<dd>
<p> The forms `<code>gs/</code><i>l</i><code>/</code><i>r</i>&#8216; and `<code>s/</code><i>l</i><code>/</code><i>r</i><code>/:G</code>&#8216; perform global substitution, i.e. substitute every occurrence of <i>r</i> for <i>l</i>. Note that the <code>g</code> or <code>:G</code> must appear in exactly the position shown. </p>
<p> See further notes on this form of substitution below.</dl>
<dt><code>&amp;</code></p>
<dd> Repeat the previous <code>s</code> substitution. Like <code>s</code>, may be preceded immediately by a <code>g</code>. In parameter expansion the <code>&amp;</code> must appear inside braces, and in filename generation it must be quoted with a backslash.</p>
<dt><code>t</code> [ <i>digits</i> ]</p>
<dd> Remove all leading pathname components, leaving the final component (tail). This works like `<code>basename</code>&#8216;. Any trailing slashes are first removed. Decimal digits are handled as described above for (h), but in this case that number of trailing components is preserved instead of the default 1; 0 is treated the same as 1.</p>
<dt><code>u</code></p>
<dd> Convert the words to all uppercase.</p>
<dt><code>x</code></p>
<dd> Like <code>q</code>, but break into words at whitespace. Does not work with parameter expansion.</dl>
<p> The <code>s/</code><i>l</i><code>/</code><i>r</i><code>/</code> substitution works as follows. By default the left-hand side of substitutions are not patterns, but character strings. Any character can be used as the delimiter in place of `<code>/</code>&#8216;. A backslash quotes the delimiter character. The character `<code>&amp;</code>&#8216;, in the right-hand-side <i>r</i>, is replaced by the text from the left-hand-side <i>l</i>. The `<code>&amp;</code>&#8216; can be quoted with a backslash. A null <i>l</i> uses the previous string either from the previous <i>l</i> or from the contextual scan string <i>s</i> from `<code>!?</code><i>s</i>&#8216;. You can omit the rightmost delimiter if a newline immediately follows <i>r</i>; the rightmost `<code>?</code>&#8216; in a context scan can similarly be omitted. Note the same record of the last <i>l</i> and <i>r</i> is maintained across all forms of expansion. </p>
<p> Note that if a `<code>&amp;</code>&#8216; is used within glob qualifiers an extra backslash is needed as a <code>&amp;</code> is a special character in this case. </p>
<p> Also note that the order of expansions affects the interpretation of <i>l</i> and <i>r</i>. When used in a history expansion, which occurs before any other expansions, <i>l</i> and <i>r</i> are treated as literal strings (except as explained for <code>HIST_SUBST_PATTERN</code> below). When used in parameter expansion, the replacement of <i>r</i> into the parameter&#8217;s value is done first, and then any additional process, parameter, command, arithmetic, or brace references are applied, which may evaluate those substitutions and expansions more than once if <i>l</i> appears more than once in the starting value. When used in a glob qualifier, any substitutions or expansions are performed once at the time the qualifier is parsed, even before the `<code>:s</code>&#8216; expression itself is divided into <i>l</i> and <i>r</i> sides. </p>
<p> If the option <code>HIST_SUBST_PATTERN</code> is set, <i>l</i> is treated as a pattern of the usual form described in the section FILENAME GENERATION below. This can be used in all the places where modifiers are available; note, however, that in globbing qualifiers parameter substitution has already taken place, so parameters in the replacement string should be quoted to ensure they are replaced at the correct time. Note also that complicated patterns used in globbing qualifiers may need the extended glob qualifier notation <code>(#q:s/</code><i>&#8230;</i><code>/</code><i>&#8230;</i><code>/)</code> in order for the shell to recognize the expression as a glob qualifier. Further, note that bad patterns in the substitution are not subject to the <code>NO_BAD_PATTERN</code> option so will cause an error. </p>
<p> When <code>HIST_SUBST_PATTERN</code> is set, <i>l</i> may start with a <code>#</code> to indicate that the pattern must match at the start of the string to be substituted, and a <code>%</code> may appear at the start or after an <code>#</code> to indicate that the pattern must match at the end of the string to be substituted. The <code>%</code> or <code>#</code> may be quoted with two backslashes. </p>
<p> For example, the following piece of filename generation code with the <code>EXTENDED_GLOB</code> option: </p>
<dl>
<dt>
<dd>
<pre><code>
print - r-- *.c(#q
                : s / # % (#b)s(*).c / 'S${match[1]}.C' /)
</code></pre>
</dl>
<p> takes the expansion of <code>*.c</code> and applies the glob qualifiers in the <code>(#q</code><i>&#8230;</i><code>)</code> expression, which consists of a substitution modifier anchored to the start and end of each word (<code>#%</code>). This turns on backreferences (<code>(#b)</code>), so that the parenthesised subexpression is available in the replacement string as <code>${match[1]}</code>. The replacement string is quoted so that the parameter is not substituted before the start of filename generation. </p>
<p> The following <code>f</code>, <code>F</code>, <code>w</code> and <code>W</code> modifiers work only with parameter expansion and filename generation. They are listed here to provide a single point of reference for all modifiers. </p>
<dl>
<dt>
<dd> <code>f</code> Repeats the immediately (without a colon) following modifier until the resulting word doesn&#8217;t change any more.</p>
<dt><code>F:</code><i>expr</i><code>:</code></p>
<dd> Like <code>f</code>, but repeats only <i>n</i> times if the expression <i>expr</i> evaluates to <i>n</i>. Any character can be used instead of the `<code>:</code>&#8216;; if `<code>(</code>&#8216;, `<code>[</code>&#8216;, or `<code>{</code>&#8216; is used as the opening delimiter, the closing delimiter should be &#8216;<code>)</code>&#8216;, `<code>]</code>&#8216;, or `<code>}</code>&#8216;, respectively.</p>
<dt><code>w</code></p>
<dd> Makes the immediately following modifier work on each word in the string.</p>
<dt><code>W:</code><i>sep</i><code>:</code></p>
<dd> Like <code>w</code> but words are considered to be the parts of the string that are separated by <i>sep</i>. Any character can be used instead of the `<code>:</code>&#8216;; opening parentheses are handled specially, see above.</dl>
<h2>PROCESS SUBSTITUTION</h2>
<p> Each part of a command argument that takes the form `<code>&lt;(</code><i>list</i><code>)</code>&#8216;, `<code>&gt;(</code><i>list</i><code>)</code>&#8216; or `<code>=(</code><i>list</i><code>)</code>&#8216; is subject to process substitution. The expression may be preceded or followed by other strings except that, to prevent clashes with commonly occurring strings and patterns, the last form must occur at the start of a command argument, and the forms are only expanded when first parsing command or assignment arguments. Process substitutions may be used following redirection operators; in this case, the substitution must appear with no trailing string. </p>
<p> Note that `<code>&lt;&lt;(</code><i>list</i><code>)</code>&#8216; is not a special syntax; it is equivalent to `<code>&lt; &lt;(</code><i>list</i><code>)</code>&#8216;, redirecting standard input from the result of process substitution. Hence all the following documentation applies. The second form (with the space) is recommended for clarity. </p>
<p> In the case of the <code>&lt;</code> or <code>&gt;</code> forms, the shell runs the commands in <i>list</i> as a subprocess of the job executing the shell command line. If the system supports the <code>/dev/fd</code> mechanism, the command argument is the name of the device file corresponding to a file descriptor; otherwise, if the system supports named pipes (FIFOs), the command argument will be a named pipe. If the form with <code>&gt;</code> is selected then writing on this special file will provide input for <i>list</i>. If <code>&lt;</code> is used, then the file passed as an argument will be connected to the output of the <i>list</i> process. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>paste &lt;(cut -f1</code> <i>file1</i><code>) &lt;(cut -f3</code> <i>file2</i><code>) |
tee &gt;(</code><i>process1</i><code>) &gt;(</code><i>process2</i><code>) &gt;/dev/null</code>
</pre>
</dl>
<p> cuts fields 1 and 3 from the files <i>file1</i> and <i>file2</i> respectively, pastes the results together, and sends it to the processes <i>process1</i> and <i>process2</i>. </p>
<p> If <code>=(</code><i>&#8230;</i><code>)</code> is used instead of <code>&lt;(</code><i>&#8230;</i><code>)</code>, then the file passed as an argument will be the name of a temporary file containing the output of the <i>list</i> process. This may be used instead of the <code>&lt;</code> form for a program that expects to lseek (see <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2)) on the input file. </p>
<p> There is an optimisation for substitutions of the form <code>=(&lt;&lt;&lt;</code><i>arg</i><code>)</code>, where <i>arg</i> is a single-word argument to the here-string redirection <code>&lt;&lt;&lt;</code>. This form produces a file name containing the value of <i>arg</i> after any substitutions have been performed. This is handled entirely within the current shell. This is effectively the reverse of the special form <code>$(&lt;</code><i>arg</i><code>)</code> which treats <i>arg</i> as a file name and replaces it with the file&#8217;s contents. </p>
<p> The <code>=</code> form is useful as both the <code>/dev/fd</code> and the named pipe implementation of <code>&lt;(</code><i>&#8230;</i><code>)</code> have drawbacks. In the former case, some programmes may automatically close the file descriptor in question before examining the file on the command line, particularly if this is necessary for security reasons such as when the programme is running setuid. In the second case, if the programme does not actually open the file, the subshell attempting to read from or write to the pipe will (in a typical implementation, different operating systems may have different behaviour) block for ever and have to be killed explicitly. In both cases, the shell actually supplies the information using a pipe, so that programmes that expect to lseek (see <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2)) on the file will not work. </p>
<p> Also note that the previous example can be more compactly and efficiently written (provided the <code>MULTIOS</code> option is set) as: </p>
<dl>
<dt>
<dd>
<pre>
<code>paste &lt;(cut -f1</code> <i>file1</i><code>) &lt;(cut -f3</code> <i>file2</i><code>)</code> \ 
<code>&gt; &gt;(</code><i>process1</i><code>) &gt; &gt;(</code><i>process2</i><code>)</code>
</pre>
</dl>
<p> The shell uses pipes instead of FIFOs to implement the latter two process substitutions in the above example. </p>
<p> There is an additional problem with <code>&gt;(</code><i>process</i><code>)</code>; when this is attached to an external command, the parent shell does not wait for <i>process</i> to finish and hence an immediately following command cannot rely on the results being complete. The problem and solution are the same as described in the section <i>MULTIOS</i> in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). Hence in a simplified version of the example above: </p>
<dl>
<dt>
<dd>
<pre>
<code>paste &lt;(cut -f1</code> <i>file1</i><code>) &lt;(cut -f3</code> <i>file2</i><code>)</code> <code>&gt; &gt;(</code><i>process</i><code>)</code>
</pre>
</dl>
<p> (note that no <code>MULTIOS</code> are involved), <i>process</i> will be run asynchronously as far as the parent shell is concerned. The workaround is: </p>
<dl>
<dt>
<dd>
<pre>
<code>{ paste &lt;(cut -f1</code> <i>file1</i><code>) &lt;(cut -f3</code> <i>file2</i><code>) }</code> <code>&gt; &gt;(</code><i>process</i><code>)</code>
</pre>
</dl>
<p> The extra processes here are spawned from the parent shell which will wait for their completion. </p>
<p> Another problem arises any time a job with a substitution that requires a temporary file is disowned by the shell, including the case where `<code>&amp;!</code>&#8216; or `<code>&amp;|</code>&#8216; appears at the end of a command containing a substitution. In that case the temporary file will not be cleaned up as the shell no longer has any memory of the job. A workaround is to use a subshell, for example, </p>
<dl>
<dt>
<dd>
<pre>
<code>(mycmd =(myoutput)) &amp;!</code>
</pre>
</dl>
<p> as the forked subshell will wait for the command to finish then remove the temporary file. </p>
<p> A general workaround to ensure a process substitution endures for an appropriate length of time is to pass it as a parameter to an anonymous shell function (a piece of shell code that is run immediately with function scope). For example, this code: </p>
<dl>
<dt>
<dd>
<pre>
<code>() {
   print File $1:
   cat $1
} =(print This be the verse)</code>
</pre>
</dl>
<p> outputs something resembling the following </p>
<dl>
<dt>
<dd>
<pre>
<code>File /tmp/zsh6nU0kS:
This be the verse</code>
</pre>
</dl>
<p> The temporary file created by the process substitution will be deleted when the function exits. </p>
<h2>PARAMETER EXPANSION</h2>
<p> The character `<code>$</code>&#8216; is used to introduce parameter expansions. See <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1) for a description of parameters, including arrays, associative arrays, and subscript notation to access individual array elements. </p>
<p> Note in particular the fact that words of unquoted parameters are not automatically split on whitespace unless the option <code>SH_WORD_SPLIT</code> is set; see references to this option below for more details. This is an important difference from other shells. However, as in other shells, null words are elided from unquoted parameters&#8217; expansions. </p>
<p> With default options, after the assignments: </p>
<dl>
<dt>
<dd>
<pre>
<code>array=(&quot;first word&quot; &quot;&quot; &quot;third word&quot;)
scalar=&quot;only word&quot;</code>
</pre>
</dl>
<p> then <code>$array</code> substitutes two words, `<code>first word</code>&#8216; and `<code>third word</code>&#8216;, and <code>$scalar</code> substitutes a single word `<code>only word</code>&#8216;. Note that second element of <code>array</code> was elided. Scalar parameters can be elided too if their value is null (empty). To avoid elision, use quoting as follows: <code>&quot;$scalar&quot;</code> for scalars and <code>&quot;${array[@]}&quot;</code> or <code>&quot;${(@)array}&quot;</code> for arrays. (The last two forms are equivalent.) </p>
<p> Parameter expansions can involve <i>flags</i>, as in `<code>${(@kv)aliases}</code>&#8216;, and other operators, such as `<code>${PREFIX:-&quot;/usr/local&quot;}</code>&#8216;. Parameter expansions can also be nested. These topics will be introduced below. The full rules are complicated and are noted at the end. </p>
<p> In the expansions discussed below that require a pattern, the form of the pattern is the same as that used for filename generation; see the section `Filename Generation&#8217;. Note that these patterns, along with the replacement text of any substitutions, are themselves subject to parameter expansion, command substitution, and arithmetic expansion. In addition to the following operations, the colon modifiers described in the section `Modifiers&#8217; in the section `History Expansion&#8217; can be applied: for example, <code>${i:s/foo/bar/}</code> performs string substitution on the expansion of parameter <code>$i</code>. </p>
<p> In the following descriptions, `<i>word</i>&#8216; refers to a single word substituted on the command line, not necessarily a space delimited word. </p>
<dl>
<dt>
<dd> <code>${</code><i>name</i><code>}</code> The value, if any, of the parameter <i>name</i> is substituted. The braces are required if the expansion is to be followed by a letter, digit, or underscore that is not to be interpreted as part of <i>name</i>. In addition, more complicated forms of substitution usually require the braces to be present; exceptions, which only apply if the option <code>KSH_ARRAYS</code> is not set, are a single subscript or any colon modifiers appearing after the name, or any of the characters `<code>^</code>&#8216;, `<code>=</code>&#8216;, `<code>~</code>&#8216;, `<code>#</code>&#8216; or `<code>+</code>&#8216; appearing before the name, all of which work with or without braces.</p>
<dl>
<dt>
<dd>
<p> If <i>name</i> is an array parameter, and the <code>KSH_ARRAYS</code> option is not set, then the value of each element of <i>name</i> is substituted, one element per word. Otherwise, the expansion results in one word only; with <code>KSH_ARRAYS</code>, this is the first element of an array. No field splitting is done on the result unless the <code>SH_WORD_SPLIT</code> option is set. See also the flags <code>=</code> and <code>s:</code><i>string</i><code>:</code>.</dl>
<dt><code>${+</code><i>name</i><code>}</code></p>
<dd> If <i>name</i> is the name of a set parameter `<code>1</code>&#8216; is substituted, otherwise `<code>0</code>&#8216; is substituted.</p>
<dt>
<dd> <code>${</code><i>name</i><code>&#8211;</code><i>word</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:-</code><i>word</i><code>}</code> If <i>name</i> is set, or in the second form is non-null, then substitute its value; otherwise substitute <i>word</i>. In the second form <i>name</i> may be omitted, in which case <i>word</i> is always substituted.</p>
<dt>
<dd> <code>${</code><i>name</i><code>+</code><i>word</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:+</code><i>word</i><code>}</code> If <i>name</i> is set, or in the second form is non-null, then substitute <i>word</i>; otherwise substitute nothing.</p>
<dt>
<dd> <code>${</code><i>name</i><code>=</code><i>word</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:=</code><i>word</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>::=</code><i>word</i><code>}</code> In the first form, if <i>name</i> is unset then set it to <i>word</i>; in the second form, if <i>name</i> is unset or null then set it to <i>word</i>; and in the third form, unconditionally set <i>name</i> to <i>word</i>. In all forms, the value of the parameter is then substituted.</p>
<dt>
<dd> <code>${</code><i>name</i><code>?</code><i>word</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:?</code><i>word</i><code>}</code> In the first form, if <i>name</i> is set, or in the second form if <i>name</i> is both set and non-null, then substitute its value; otherwise, print <i>word</i> and exit from the shell. Interactive shells instead return to the prompt. If <i>word</i> is omitted, then a standard message is printed.</dl>
<p> In any of the above expressions that test a variable and substitute an alternate <i>word</i>, note that you can use standard shell quoting in the <i>word</i> value to selectively override the splitting done by the <code>SH_WORD_SPLIT</code> option and the <code>=</code> flag, but not splitting by the <code>s:</code><i>string</i><code>:</code> flag. </p>
<p> In the following expressions, when <i>name</i> is an array and the substitution is not quoted, or if the `<code>(@)</code>&#8216; flag or the <i>name</i><code>[@]</code> syntax is used, matching and replacement is performed on each array element separately. </p>
<dl>
<dt>
<dd> <code>${</code><i>name</i><code>#</code><i>pattern</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>##</code><i>pattern</i><code>}</code> If the <i>pattern</i> matches the beginning of the value of <i>name</i>, then substitute the value of <i>name</i> with the matched portion deleted; otherwise, just substitute the value of <i>name</i>. In the first form, the smallest matching pattern is preferred; in the second form, the largest matching pattern is preferred.</p>
<dt>
<dd> <code>${</code><i>name</i><code>%</code><i>pattern</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>%%</code><i>pattern</i><code>}</code> If the <i>pattern</i> matches the end of the value of <i>name</i>, then substitute the value of <i>name</i> with the matched portion deleted; otherwise, just substitute the value of <i>name</i>. In the first form, the smallest matching pattern is preferred; in the second form, the largest matching pattern is preferred.</p>
<dt><code>${</code><i>name</i><code>:#</code><i>pattern</i><code>}</code></p>
<dd> If the <i>pattern</i> matches the value of <i>name</i>, then substitute the empty string; otherwise, just substitute the value of <i>name</i>. If <i>name</i> is an array the matching array elements are removed (use the `<code>(M)</code>&#8216; flag to remove the non-matched elements).</p>
<dt><code>${</code><i>name</i><code>:|</code><i>arrayname</i><code>}</code></p>
<dd> If <i>arrayname</i> is the name (N.B., not contents) of an array variable, then any elements contained in <i>arrayname</i> are removed from the substitution of <i>name</i>. If the substitution is scalar, either because <i>name</i> is a scalar variable or the expression is quoted, the elements of <i>arrayname</i> are instead tested against the entire expression.</p>
<dt><code>${</code><i>name</i><code>:*</code><i>arrayname</i><code>}</code></p>
<dd> Similar to the preceding substitution, but in the opposite sense, so that entries present in both the original substitution and as elements of <i>arrayname</i> are retained and others removed.</p>
<dt>
<dd> <code>${</code><i>name</i><code>:^</code><i>arrayname</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:^^</code><i>arrayname</i><code>}</code> Zips two arrays, such that the output array is twice as long as the shortest (longest for `<code>:^^</code>&#8216;) of <code>name</code> and <code>arrayname</code>, with the elements alternatingly being picked from them. For `<code>:^</code>&#8216;, if one of the input arrays is longer, the output will stop when the end of the shorter array is reached. Thus,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
a = (1 2 3 4);<br />
b = (a b);<br />
print $<br />
{<br />
a:<br />
    ^b<br />
}
</dl>
<p> will output `<code>1 a 2 b</code>&#8216;. For `<code>:^^</code>&#8216;, then the input is repeated until all of the longer array has been used up and the above will output `<code>1 a 2 b 3 a 4 b</code>&#8216;. </p>
<p> Either or both inputs may be a scalar, they will be treated as an array of length 1 with the scalar as the only element. If either array is empty, the other array is output with no extra elements inserted. </p>
<p> Currently the following code will output `<code>a b</code>&#8216; and `<code>1</code>&#8216; as two separate elements, which can be unexpected. The second print provides a workaround which should continue to work if this is changed. </p>
<dl>
<dt>
<dd>
a = (a b);<br />
b = (1 2);<br />
print &#8211; l &#8220;${a:^b}&#8221;;<br />
print &#8211; l &#8220;${${a:^b}}&#8221;
</dl>
</dl>
<dt>
<dd> <code>${</code><i>name</i><code>:</code><i>offset</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:</code><i>offset</i><code>:</code><i>length</i><code>}</code> This syntax gives effects similar to parameter subscripting in the form <code>$</code><i>name</i><code>[</code><i>start</i><code>,</code><i>end</i><code>]</code>, but is compatible with other shells; note that both <i>offset</i> and <i>length</i> are interpreted differently from the components of a subscript.</p>
<dl>
<dt>
<dd>
<p> If <i>offset</i> is non-negative, then if the variable <i>name</i> is a scalar substitute the contents starting <i>offset</i> characters from the first character of the string, and if <i>name</i> is an array substitute elements starting <i>offset</i> elements from the first element. If <i>length</i> is given, substitute that many characters or elements, otherwise the entire rest of the scalar or array. </p>
<p> A positive <i>offset</i> is always treated as the offset of a character or element in <i>name</i> from the first character or element of the array (this is different from native zsh subscript notation). Hence 0 refers to the first character or element regardless of the setting of the option <code>KSH_ARRAYS</code>. </p>
<p> A negative offset counts backwards from the end of the scalar or array, so that -1 corresponds to the last character or element, and so on. </p>
<p> When positive, <i>length</i> counts from the <i>offset</i> position toward the end of the scalar or array. When negative, <i>length</i> counts back from the end. If this results in a position smaller than <i>offset</i>, a diagnostic is printed and nothing is substituted. </p>
<p> The option <code>MULTIBYTE</code> is obeyed, i.e. the offset and length count multibyte characters where appropriate. </p>
<p> <i>offset</i> and <i>length</i> undergo the same set of shell substitutions as for scalar assignment; in addition, they are then subject to arithmetic evaluation. Hence, for example </p>
<dl>
<dt>
<dd>
print ${foo : 3} print ${foo : 1 + 2} print ${foo : $((1 + 2))} print $<br />
{<br />
foo:<br />
    $(echo 1 + 2)<br />
}
</dl>
<p> all have the same effect, extracting the string starting at the fourth character of <code>$foo</code> if the substitution would otherwise return a scalar, or the array starting at the fourth element if <code>$foo</code> would return an array. Note that with the option <code>KSH_ARRAYS</code> <code>$foo</code> always returns a scalar (regardless of the use of the offset syntax) and a form such as <code>${foo[*]:3}</code> is required to extract elements of an array named <code>foo</code>. </p>
<p> If <i>offset</i> is negative, the <code>&#8211;</code> may not appear immediately after the <code>:</code> as this indicates the <code>${</code><i>name</i><code>:-</code><i>word</i><code>}</code> form of substitution. Instead, a space may be inserted before the <code>&#8211;</code>. Furthermore, neither <i>offset</i> nor <i>length</i> may begin with an alphabetic character or <code>&amp;</code> as these are used to indicate history-style modifiers. To substitute a value from a variable, the recommended approach is to precede it with a <code>$</code> as this signifies the intention (parameter substitution can easily be rendered unreadable); however, as arithmetic substitution is performed, the expression <code>${var: offs}</code> does work, retrieving the offset from <code>$offs</code>. </p>
<p> For further compatibility with other shells there is a special case for array offset 0. This usually accesses the first element of the array. However, if the substitution refers to the positional parameter array, e.g. <code>$@</code> or <code>$*</code>, then offset 0 instead refers to <code>$0</code>, offset 1 refers to <code>$1</code>, and so on. In other words, the positional parameter array is effectively extended by prepending <code>$0</code>. Hence <code>${*:0:1}</code> substitutes <code>$0</code> and <code>${*:1:1}</code> substitutes <code>$1</code>.</dl>
<dt>
<dd> <code>${</code><i>name</i><code>/</code><i>pattern</i><code>/</code><i>repl</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>//</code><i>pattern</i><code>/</code><i>repl</i><code>}</code></p>
<dt>
<dd> <code>${</code><i>name</i><code>:/</code><i>pattern</i><code>/</code><i>repl</i><code>}</code> Replace the longest possible match of <i>pattern</i> in the expansion of parameter <i>name</i> by string <i>repl</i>. The first form replaces just the first occurrence, the second form all occurrences, and the third form replaces only if <i>pattern</i> matches the entire string. Both <i>pattern</i> and <i>repl</i> are subject to double-quoted substitution, so that expressions like <code>${name/$opat/$npat}</code> will work, but obey the usual rule that pattern characters in <code>$opat</code> are not treated specially unless either the option <code>GLOB_SUBST</code> is set, or <code>$opat</code> is instead substituted as <code>${~opat}</code>.</p>
<dl>
<dt>
<dd>
<p> The <i>pattern</i> may begin with a `<code>#</code>&#8216;, in which case the <i>pattern</i> must match at the start of the string, or `<code>%</code>&#8216;, in which case it must match at the end of the string, or `<code>#%</code>&#8216; in which case the <i>pattern</i> must match the entire string. The <i>repl</i> may be an empty string, in which case the final `<code>/</code>&#8216; may also be omitted. To quote the final `<code>/</code>&#8216; in other cases it should be preceded by a single backslash; this is not necessary if the `<code>/</code>&#8216; occurs inside a substituted parameter. Note also that the `<code>#</code>&#8216;, `<code>%</code>&#8216; and `<code>#%</code> are not active if they occur inside a substituted parameter, even at the start. </p>
<p> If, after quoting rules apply, <code>${</code><i>name</i><code>}</code> expands to an array, the replacements act on each element individually. Note also the effect of the <code>I</code> and <code>S</code> parameter expansion flags below; however, the flags <code>M</code>, <code>R</code>, <code>B</code>, <code>E</code> and <code>N</code> are not useful. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
foo = &#8220;twinkle twinkle little star&#8221; sub = &#8220;t*e&#8221; rep = &#8220;spy&#8221; print $<br />
{<br />
    foo //${~sub}/$rep}<br />
        print $<br />
    {<br />
        (S) foo //${~sub}/$rep}
</dl>
<p> Here, the `<code>~</code>&#8216; ensures that the text of <code>$sub</code> is treated as a pattern rather than a plain string. In the first case, the longest match for <code>t*e</code> is substituted and the result is `<code>spy star</code>&#8216;, while in the second case, the shortest matches are taken and the result is `<code>spy spy lispy star</code>&#8216;.</dl>
<dt><code>${#</code><i>spec</i><code>}</code></p>
<dd> If <i>spec</i> is one of the above substitutions, substitute the length in characters of the result instead of the result itself. If <i>spec</i> is an array expression, substitute the number of elements of the result. This has the side-effect that joining is skipped even in quoted forms, which may affect other sub-expressions in <i>spec</i>. Note that `<code>^</code>&#8216;, `<code>=</code>&#8216;, and `<code>~</code>&#8216;, below, must appear to the left of `<code>#</code>&#8216; when these forms are combined.</p>
<dl>
<dt>
<dd>
<p> If the option <code>POSIX_IDENTIFIERS</code> is not set, and <i>spec</i> is a simple name, then the braces are optional; this is true even for special parameters so e.g. <code>$#-</code> and <code>$#*</code> take the length of the string <code>$-</code> and the array <code>$*</code> respectively. If <code>POSIX_IDENTIFIERS</code> is set, then braces are required for the <code>#</code> to be treated in this fashion.</dl>
<dt><code>${^</code><i>spec</i><code>}</code></p>
<dd> Turn on the <code>RC_EXPAND_PARAM</code> option for the evaluation of <i>spec</i>; if the `<code>^</code>&#8216; is doubled, turn it off. When this option is set, array expansions of the form <i>foo</i><code>${</code><i>xx</i><code>}</code><i>bar</i>, where the parameter <i>xx</i> is set to <code>(</code><i>a b c</i><code>)</code>, are substituted with `<i>fooabar foobbar foocbar</i>&#8216; instead of the default `<i>fooa b cbar</i>&#8216;. Note that an empty array will therefore cause all arguments to be removed.</p>
<dl>
<dt>
<dd>
<p> Internally, each such expansion is converted into the equivalent list for brace expansion. E.g., <code>${^var}</code> becomes <code>{$var[1],$var[2],</code>&#8230;<code>}</code>, and is processed as described in the section `Brace Expansion&#8217; below: note, however, the expansion happens immediately, with any explicit brace expansion happening later. If word splitting is also in effect the <code>$var[</code><i>N</i><code>]</code> may themselves be split into different list elements.</dl>
<dt><code>${=</code><i>spec</i><code>}</code></p>
<dd> Perform word splitting using the rules for <code>SH_WORD_SPLIT</code> during the evaluation of <i>spec</i>, but regardless of whether the parameter appears in double quotes; if the `<code>=</code>&#8216; is doubled, turn it off. This forces parameter expansions to be split into separate words before substitution, using <code>IFS</code> as a delimiter. This is done by default in most other shells.</p>
<dl>
<dt>
<dd>
<p> Note that splitting is applied to <i>word</i> in the assignment forms of <i>spec</i> <i>before</i> the assignment to <i>name</i> is performed. This affects the result of array assignments with the <code>A</code> flag.</dl>
<dt><code>${~</code><i>spec</i><code>}</code></p>
<dd> Turn on the <code>GLOB_SUBST</code> option for the evaluation of <i>spec</i>; if the `<code>~</code>&#8216; is doubled, turn it off. When this option is set, the string resulting from the expansion will be interpreted as a pattern anywhere that is possible, such as in filename expansion and filename generation and pattern-matching contexts like the right hand side of the `<code>=</code>&#8216; and `<code>!=</code>&#8216; operators in conditions.</p>
<dl>
<dt>
<dd>
<p> In nested substitutions, note that the effect of the <code>~</code> applies to the result of the current level of substitution. A surrounding pattern operation on the result may cancel it. Hence, for example, if the parameter <code>foo</code> is set to <code>*</code>, <code>${~foo//\*/*.c}</code> is substituted by the pattern <code>*.c</code>, which may be expanded by filename generation, but <code>${${~foo}//\*/*.c}</code> substitutes to the string <code>*.c</code>, which will not be further expanded.</dl>
</dl>
<p> If a <code>${</code>&#8230;<code>}</code> type parameter expression or a <code>$(</code>&#8230;<code>)</code> type command substitution is used in place of <i>name</i> above, it is expanded first and the result is used as if it were the value of <i>name</i>. Thus it is possible to perform nested operations: <code>${${foo#head}%tail}</code> substitutes the value of <code>$foo</code> with both `<code>head</code>&#8216; and `<code>tail</code>&#8216; deleted. The form with <code>$(</code>&#8230;<code>)</code> is often useful in combination with the flags described next; see the examples below. Each <i>name</i> or nested <code>${</code>&#8230;<code>}</code> in a parameter expansion may also be followed by a subscript expression as described in <i>Array Parameters</i> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<p> Note that double quotes may appear around nested expressions, in which case only the part inside is treated as quoted; for example, <code>${(f)&quot;$(foo)&quot;}</code> quotes the result of <code>$(foo)</code>, but the flag `<code>(f)</code>&#8216; (see below) is applied using the rules for unquoted expansions. Note further that quotes are themselves nested in this context; for example, in <code>&quot;${(@f)&quot;$(foo)&quot;}&quot;</code>, there are two sets of quotes, one surrounding the whole expression, the other (redundant) surrounding the <code>$(foo)</code> as before. </p>
<h3>Parameter Expansion Flags</h3>
<p> If the opening brace is directly followed by an opening parenthesis, the string up to the matching closing parenthesis will be taken as a list of flags. In cases where repeating a flag is meaningful, the repetitions need not be consecutive; for example, `(<code>q%q%q</code>)&#8217; means the same thing as the more readable `(<code>%%qqq</code>)&#8217;. The following flags are supported: </p>
<dl>
<dt>
<dd> <code>#</code> Evaluate the resulting words as numeric expressions and output the characters corresponding to the resulting integer. Note that this form is entirely distinct from use of the <code>#</code> without parentheses.</p>
<dl>
<dt>
<dd>
<p> If the <code>MULTIBYTE</code> option is set and the number is greater than 127 (i.e. not an ASCII character) it is treated as a Unicode character.</dl>
<dt><code>%</code></p>
<dd> Expand all <code>%</code> escapes in the resulting words in the same way as in prompts (see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)). If this flag is given twice, full prompt expansion is done on the resulting words, depending on the setting of the <code>PROMPT_PERCENT</code>, <code>PROMPT_SUBST</code> and <code>PROMPT_BANG</code> options.</p>
<dt><code>@</code></p>
<dd> In double quotes, array elements are put into separate words. E.g., `<code>&quot;${(@)foo}&quot;</code>&#8216; is equivalent to `<code>&quot;${foo[@]}&quot;</code>&#8216; and `<code>&quot;${(@)foo[1,2]}&quot;</code>&#8216; is the same as `<code>&quot;$foo[1]&quot; &quot;$foo[2]&quot;</code>&#8216;. This is distinct from <i>field splitting</i> by the <code>f</code>, <code>s</code> or <code>z</code> flags, which still applies within each array element.</p>
<dt><code>A</code></p>
<dd> Convert the substitution into an array expression, even if it otherwise would be scalar. This has lower precedence than subscripting, so one level of nested expansion is required in order that subscripts apply to array elements. Thus <code>${${(A</code><code>)</code><i>name</i><code>}[1]}</code> yields the full value of <i>name</i> when <i>name</i> is scalar.</p>
<dl>
<dt>
<dd>
<p> This assigns an array parameter with `<code>${</code>&#8230;<code>=</code>&#8230;<code>}</code>&#8216;, `<code>${</code>&#8230;<code>:=</code>&#8230;<code>}</code>&#8216; or `<code>${</code>&#8230;<code>::=</code>&#8230;<code>}</code>&#8216;. If this flag is repeated (as in `<code>AA</code>&#8216;), assigns an associative array parameter. Assignment is made before sorting or padding; if field splitting is active, the <i>word</i> part is split before assignment. The <i>name</i> part may be a subscripted range for ordinary arrays; when assigning an associative array, the <i>word</i> part <i>must</i> be converted to an array, for example by using `<code>${(AA)=</code><i>name</i><code>=</code>&#8230;<code>}</code>&#8216; to activate field splitting. </p>
<p> Surrounding context such as additional nesting or use of the value in a scalar assignment may cause the array to be joined back into a single string again.</dl>
<dt><code>a</code></p>
<dd> Sort in array index order; when combined with `<code>O</code>&#8216; sort in reverse array index order. Note that `<code>a</code>&#8216; is therefore equivalent to the default but `<code>Oa</code>&#8216; is useful for obtaining an array&#8217;s elements in reverse order.</p>
<dt><code>b</code></p>
<dd> Quote with backslashes only characters that are special to pattern matching. This is useful when the contents of the variable are to be tested using <code>GLOB_SUBST</code>, including the <code>${~</code><i>&#8230;</i><code>}</code> switch.</p>
<dl>
<dt>
<dd>
<p> Quoting using one of the <code>q</code> family of flags does not work for this purpose since quotes are not stripped from non-pattern characters by <code>GLOB_SUBST</code>. In other words, </p>
<dl>
<dt>
<dd>
pattern = $<br />
{<br />
    (q) str<br />
}<br />
[[$str = ${~pattern}]]
</dl>
<p> works if <code>$str</code> is `<code>a*b</code>&#8216; but not if it is `<code>a b</code>&#8216;, whereas </p>
<dl>
<dt>
<dd>
pattern = $<br />
{<br />
    (b) str<br />
}<br />
[[$str = ${~pattern}]]
</dl>
<p> is always true for any possible value of <code>$str</code>.</dl>
<dt><code>c</code></p>
<dd> With <code>${#</code><i>name</i><code>}</code>, count the total number of characters in an array, as if the elements were concatenated with spaces between them. This is not a true join of the array, so other expressions used with this flag may have an effect on the elements of the array before it is counted.</p>
<dt><code>C</code></p>
<dd> Capitalize the resulting words. `Words&#8217; in this case refers to sequences of alphanumeric characters separated by non-alphanumerics, <i>not</i> to words that result from field splitting.</p>
<dt><code>D</code></p>
<dd> Assume the string or array elements contain directories and attempt to substitute the leading part of these by names. The remainder of the path (the whole of it if the leading part was not substituted) is then quoted so that the whole string can be used as a shell argument. This is the reverse of `<code>~</code>&#8216; substitution: see the section FILENAME EXPANSION below.</p>
<dt><code>e</code></p>
<dd> Perform single word shell expansions, namely <i>parameter expansion</i>, <i>command substitution</i> and <i>arithmetic expansion</i>, on the result. Such expansions can be nested but too deep recursion may have unpredictable effects.</p>
<dt><code>f</code></p>
<dd> Split the result of the expansion at newlines. This is a shorthand for `<code>ps:
:</code>&#8216;.</p>
<dt><code>F</code></p>
<dd> Join the words of arrays together using newline as a separator. This is a shorthand for `<code>pj:
:</code>&#8216;.</p>
<dt><code>g:</code><i>opts</i><code>:</code></p>
<dd> Process escape sequences like the echo builtin when no options are given (<code>g::</code>). With the <code>o</code> option, octal escapes don&#8217;t take a leading zero. With the <code>c</code> option, sequences like `<code>^X</code>&#8216; are also processed. With the <code>e</code> option, processes `<code>\M-t</code>&#8216; and similar sequences like the print builtin. With both of the <code>o</code> and <code>e</code> options, behaves like the print builtin except that in none of these modes is `<code>
