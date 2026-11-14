---
title: "rgrep(1)"
name: "rgrep"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rgrep/"
description: "grep, egrep, fgrep, rgrep – print lines that match patterns"
---

<h2 class="name">NAME</h2>
<p> grep, egrep, fgrep, rgrep &#8211; print lines that match patterns </p>
<h2>SYNOPSIS</h2>
<p> <code>grep</code> [<i>OPTION</i>&#8230;] <i>PATTERNS</i> [<i>FILE</i>&#8230;]<br />
 <code>grep</code> [<i>OPTION</i>&#8230;] <code>-e</code> <i>PATTERNS</i> &#8230; [<i>FILE</i>&#8230;]<br />
 <code>grep</code> [<i>OPTION</i>&#8230;] <code>-f</code> <i>PATTERN_FILE</i> &#8230; [<i>FILE</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>grep</code> searches for <i>PATTERNS</i> in each <i>FILE</i>. <i>PATTERNS</i> is one or more patterns separated by newline characters, and <code>grep</code> prints each line that matches a pattern. Typically <i>PATTERNS</i> should be quoted when <code>grep</code> is used in a shell command. </p>
<p> A <i>FILE</i> of &#8220;<code>&#8211;</code>&#8221; stands for standard input. If no <i>FILE</i> is given, recursive searches examine the working directory, and nonrecursive searches read standard input. </p>
<p> In addition, the variant programs <code>egrep</code>, <code>fgrep</code> and <code>rgrep</code> are the same as <code>grep -E</code>, <code>grep -F</code>, and <code>grep -r</code>, respectively. These variants are deprecated, but are provided for backward compatibility.</p>
<h2>OPTIONS</h2>
<h3>Generic Program Information</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Output a usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Output the version number of <code>grep</code> and exit.</dl>
<h3>Pattern Syntax</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;extended-regexp</code></p>
<dd> Interpret <i>PATTERNS</i> as extended regular expressions (EREs, see below).</p>
<dt><code>-F</code>, <code>&#8211;fixed-strings</code></p>
<dd> Interpret <i>PATTERNS</i> as fixed strings, not regular expressions.</p>
<dt><code>-G</code>, <code>&#8211;basic-regexp</code></p>
<dd> Interpret <i>PATTERNS</i> as basic regular expressions (BREs, see below). This is the default.</p>
<dt><code>-P</code>, <code>&#8211;perl-regexp</code></p>
<dd> Interpret I&lt;PATTERNS&gt; as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the <code>-z</code> (<code>&#8211;null-data</code>) option, and <code>grep -P</code> may warn of unimplemented features.</dl>
<h3>Matching Control</h3>
<dl>
<dt><code>-e</code><i> PATTERNS</i>, &#8211;regexp=<i>PATTERNS</i></p>
<dd> Use <i>PATTERNS</i> as the patterns. If this option is used multiple times or is combined with the <code>-f</code> (<code>&#8211;file</code>) option, search for all patterns given. This option can be used to protect a pattern beginning with &#8220;-&#8221;.</p>
<dt><code>-f</code><i> FILE</i>, &#8211;file=<i>FILE</i></p>
<dd> Obtain patterns from <i>FILE</i>, one per line. If this option is used multiple times or is combined with the <code>-e</code> (<code>&#8211;regexp</code>) option, search for all patterns given. The empty file contains zero patterns, and therefore matches nothing.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.</p>
<dt><code>&#8211;no-ignore-case</code></p>
<dd> Do not ignore case distinctions in patterns and input data. This is the default. This option is useful for passing to shell scripts that already use <code>-i</code>, to cancel its effects because the two options override each other.</p>
<dt><code>-v</code>, <code>&#8211;invert-match</code></p>
<dd> Invert the sense of matching, to select non-matching lines.</p>
<dt><code>-w</code>, <code>&#8211;word-regexp</code></p>
<dd> Select only those lines containing matches that form whole words. The test is that the matching substring must either be at the beginning of the line, or preceded by a non-word constituent character. Similarly, it must be either at the end of the line or followed by a non-word constituent character. Word-constituent characters are letters, digits, and the underscore. This option has no effect if <code>-x</code> is also specified.</p>
<dt><code>-x</code>, <code>&#8211;line-regexp</code></p>
<dd> Select only those matches that exactly match the whole line. For a regular expression pattern, this is like parenthesizing the pattern and then surrounding it with <code>^</code> and <code>$</code>.</p>
<dt><code>-y</code></p>
<dd> Obsolete synonym for <code>-i</code>.</dl>
<h3>General Output Control</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> Suppress normal output; instead print a count of matching lines for each input file. With the <code>-v</code>, <code>&#8211;invert-match</code> option (see below), count non-matching lines.</p>
<dt><code>&#8211;color</code>[<code>=</code><i>WHEN</i>], <code>&#8211;colour</code>[<code>=</code><i>WHEN</i>]</p>
<dd> Surround the matched (non-empty) strings, matching lines, context lines, file names, line numbers, byte offsets, and separators (for fields and groups of context lines) with escape sequences to display them in color on the terminal. The colors are defined by the environment variable <code>GREP_COLORS</code>. The deprecated environment variable <code>GREP_COLOR</code> is still supported, but its setting does not have priority. <i>WHEN</i> is <code>never</code>, <code>always</code>, or <code>auto</code>.</p>
<dt><code>-L</code>, <code>&#8211;files-without-match</code></p>
<dd> Suppress normal output; instead print the name of each input file from which no output would normally have been printed.</p>
<dt><code>-l</code>, <code>&#8211;files-with-matches</code></p>
<dd> Suppress normal output; instead print the name of each input file from which output would normally have been printed. Scanning each input file stops upon first match.</p>
<dt><code>-m</code><i> NUM</i>, &#8211;max-count=<i>NUM</i></p>
<dd> Stop reading a file after <i>NUM</i> matching lines. If the input is standard input from a regular file, and <i>NUM</i> matching lines are output, <code>grep</code> ensures that the standard input is positioned to just after the last matching line before exiting, regardless of the presence of trailing context lines. This enables a calling process to resume a search. When <code>grep</code> stops after <i>NUM</i> matching lines, it outputs any trailing context lines. When the <code>-c</code> or <code>&#8211;count</code> option is also used, <code>grep</code> does not output a count greater than <i>NUM</i>. When the <code>-v</code> or <code>&#8211;invert-match</code> option is also used, <code>grep</code> stops after outputting <i>NUM</i> non-matching lines.</p>
<dt><code>-o</code>, <code>&#8211;only-matching</code></p>
<dd> Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> Quiet; do not write anything to standard output. Exit immediately with zero status if any match is found, even if an error was detected. Also see the <code>-s</code> or <code>&#8211;no-messages</code> option.</p>
<dt><code>-s</code>, <code>&#8211;no-messages</code></p>
<dd> Suppress error messages about nonexistent or unreadable files.</dl>
<h3>Output Line Prefix Control</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;byte-offset</code></p>
<dd> Print the 0-based byte offset within the input file before each line of output. If <code>-o</code> (<code>&#8211;only-matching</code>) is specified, print the offset of the matching part itself.</p>
<dt><code>-H</code>, <code>&#8211;with-filename</code></p>
<dd> Print the file name for each match. This is the default when there is more than one file to search. This is a GNU extension.</p>
<dt><code>-h</code>, <code>&#8211;no-filename</code></p>
<dd> Suppress the prefixing of file names on output. This is the default when there is only one file (or only standard input) to search.</p>
<dt><code>&#8211;label=</code><i>LABEL</i></p>
<dd> Display input actually coming from standard input as input coming from file <i>LABEL</i>. This can be useful for commands that transform a file&#8217;s contents before searching, e.g., <code>gzip -cd foo.gz | grep &#8211;label=foo -H &#8216;some pattern&#8217;</code>. See also the <code>-H</code> option.</p>
<dt><code>-n</code>, <code>&#8211;line-number</code></p>
<dd> Prefix each line of output with the 1-based line number within its input file.</p>
<dt><code>-T</code>, <code>&#8211;initial-tab</code></p>
<dd> Make sure that the first character of actual line content lies on a tab stop, so that the alignment of tabs looks normal. This is useful with options that prefix their output to the actual content: <code>-H</code>,<code>-n</code>, and <code>-b</code>. In order to improve the probability that lines from a single file will all start at the same column, this also causes the line number and byte offset (if present) to be printed in a minimum size field width.</p>
<dt><code>-Z</code>, <code>&#8211;null</code></p>
<dd> Output a zero byte (the ASCII <code>NUL</code> character) instead of the character that normally follows a file name. For example, <code>grep -lZ</code> outputs a zero byte after each file name instead of the usual newline. This option makes the output unambiguous, even in the presence of file names containing unusual characters like newlines. This option can be used with commands like <code>find -print0</code>, <code>perl -0</code>, <code>sort -z</code>, and <code>xargs -0</code> to process arbitrary file names, even those that contain newline characters.</dl>
<h3>Context Line Control</h3>
<dl>
<dt><code>-A</code><i> NUM</i>, &#8211;after-context=<i>NUM</i></p>
<dd> Print <i>NUM</i> lines of trailing context after matching lines. Places a line containing a group separator (<code>&#8212;</code>) between contiguous groups of matches. With the <code>-o</code> or <code>&#8211;only-matching</code> option, this has no effect and a warning is given.</p>
<dt><code>-B</code><i> NUM</i>, &#8211;before-context=<i>NUM</i></p>
<dd> Print <i>NUM</i> lines of leading context before matching lines. Places a line containing a group separator (<code>&#8212;</code>) between contiguous groups of matches. With the <code>-o</code> or <code>&#8211;only-matching</code> option, this has no effect and a warning is given.</p>
<dt><code>-C</code><i> NUM</i>, &#8211;<i>NUM</i>, &#8211;context=<i>NUM</i></p>
<dd> Print <i>NUM</i> lines of output context. Places a line containing a group separator (<code>&#8212;</code>) between contiguous groups of matches. With the <code>-o</code> or <code>&#8211;only-matching</code> option, this has no effect and a warning is given.</p>
<dt><code>&#8211;group-separator=</code><i>SEP</i></p>
<dd> When <code>-A</code>, <code>-B</code>, or <code>-C</code> are in use, print <i>SEP</i> instead of <code>&#8212;</code> between groups of lines.</p>
<dt><code>&#8211;no-group-separator</code></p>
<dd> When <code>-A</code>, <code>-B</code>, or <code>-C</code> are in use, do not print a separator between groups of lines.</dl>
<h3>File and Directory Selection</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;text</code></p>
<dd> Process a binary file as if it were text; this is equivalent to the <code>&#8211;binary-files=text</code> option.</p>
<dt><code>&#8211;binary-files=</code><i>TYPE</i></p>
<dd> If a file&#8217;s data or metadata indicate that the file contains binary data, assume that the file is of type <i>TYPE</i>. Non-text bytes indicate binary data; these are either output bytes that are improperly encoded for the current locale, or null input bytes when the <code>-z</code> option is not given.</p>
<dt>
<dd> By default, <i>TYPE</i> is <code>binary</code>, and <code>grep</code> suppresses output after null input binary data is discovered, and suppresses output lines that contain improperly encoded data. When some output is suppressed, <code>grep</code> follows any output with a one-line message saying that a binary file matches.</p>
<dt>
<dd> If <i>TYPE</i> is <code>without-match</code>, when <code>grep</code> discovers null input binary data it assumes that the rest of the file does not match; this is equivalent to the <code>-I</code> option.</p>
<dt>
<dd> If <i>TYPE</i> is <code>text</code>, <code>grep</code> processes a binary file as if it were text; this is equivalent to the <code>-a</code> option.</p>
<dt>
<dd> When <i>type</i> is <code>binary</code>, <code>grep</code> may treat non-text bytes as line terminators even without the <code>-z</code> option. This means choosing <code>binary</code> versus <code>text</code> can affect whether a pattern matches a file. For example, when <i>type</i> is <code>binary</code> the pattern <code>q$ might</code> match <code>q</code> immediately followed by a null byte, even though this is not matched when <i>type</i> is <code>text</code>. Conversely, when <i>type</i> is <code>binary</code> the pattern <code>.</code> (period) might not match a null byte.</p>
<dt>
<dd> <i>Warning:</i> The <code>-a</code> option might output binary garbage, which can have nasty side effects if the output is a terminal and if the terminal driver interprets some of it as commands. On the other hand, when reading files whose text encodings are unknown, it can be helpful to use <code>-a</code> or to set <code>LC_ALL=&#8217;C&#8217;</code> in the environment, in order to find more matches even if the matches are unsafe for direct display.</p>
<dt><code>-D</code><i> ACTION</i>, &#8211;devices=<i>ACTION</i></p>
<dd> If an input file is a device, FIFO or socket, use <i>ACTION</i> to process it. By default, <i>ACTION</i> is <code>read</code>, which means that devices are read just as if they were ordinary files. If <i>ACTION</i> is <code>skip</code>, devices are silently skipped.</p>
<dt><code>-d</code><i> ACTION</i>, &#8211;directories=<i>ACTION</i></p>
<dd> If an input file is a directory, use <i>ACTION</i> to process it. By default, <i>ACTION</i> is <code>read</code>, i.e., read directories just as if they were ordinary files. If <i>ACTION</i> is <code>skip</code>, silently skip directories. If <i>ACTION</i> is <code>recurse</code>, read all files under each directory, recursively, following symbolic links only if they are on the command line. This is equivalent to the <code>-r</code> option.</p>
<dt><code>&#8211;exclude=</code><i>GLOB</i></p>
<dd> Skip any command-line file with a name suffix that matches the pattern <i>GLOB</i>, using wildcard matching; a name suffix is either the whole name, or a trailing part that starts with a non-slash character immediately after a slash (<code>/</code>) in the name. When searching recursively, skip any subfile whose base name matches <i>GLOB</i>; the base name is the part after the last slash. A pattern can use <code>*</code>, <code>?</code>, and <code>[</code>&#8230;<code>]</code> as wildcards, and <code>\</code> to quote a wildcard or backslash character literally.</p>
<dt><code>&#8211;exclude-from=</code><i>FILE</i></p>
<dd> Skip files whose base name matches any of the file-name globs read from <i>FILE</i> (using wildcard matching as described under <code>&#8211;exclude</code>).</p>
<dt><code>&#8211;exclude-dir=</code><i>GLOB</i></p>
<dd> Skip any command-line directory with a name suffix that matches the pattern <i>GLOB</i>. When searching recursively, skip any subdirectory whose base name matches <i>GLOB</i>. Ignore any redundant trailing slashes in <i>GLOB</i>.</p>
<dt><code>-I</code></p>
<dd> Process a binary file as if it did not contain matching data; this is equivalent to the <code>&#8211;binary-files=without-match</code> option.</p>
<dt><code>&#8211;include=</code><i>GLOB</i></p>
<dd> Search only files whose base name matches <i>GLOB</i> (using wildcard matching as described under <code>&#8211;exclude</code>). If contradictory <code>&#8211;include</code> and <code>&#8211;exclude</code> options are given, the last matching one wins. If no <code>&#8211;include</code> or <code>&#8211;exclude</code> options match, a file is included unless the first such option is <code>&#8211;include</code>.</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> Read all files under each directory, recursively, following symbolic links only if they are on the command line. Note that if no file operand is given, B&lt;grep&gt; searches the working directory. This is equivalent to the <code>-d recurse</code> option.</p>
<dt><code>-R</code>, <code>&#8211;dereference-recursive</code></p>
<dd> Read all files under each directory, recursively. Follow all symbolic links, unlike <code>-r</code>.</dl>
<h3>Other Options</h3>
<dl>
<dt><code>&#8211;line-buffered</code></p>
<dd> Use line buffering on output. This can cause a performance penalty.</p>
<dt><code>-U</code>, <code>&#8211;binary</code></p>
<dd> Treat the file(s) as binary. By default, under MS-DOS and MS-Windows, <code>grep</code> guesses whether a file is text or binary as described for the <code>&#8211;binary-files</code> option. If <code>grep</code> decides the file is a text file, it strips the CR characters from the original file contents (to make regular expressions with <code>^</code> and <code>$</code> work correctly). Specifying <code>-U</code> overrules this guesswork, causing all files to be read and passed to the matching mechanism verbatim; if the file is a text file with CR/LF pairs at the end of each line, this will cause some regular expressions to fail. This option has no effect on platforms other than MS-DOS and MS-Windows.</p>
<dt><code>-z</code>, <code>&#8211;null-data</code></p>
<dd> Treat input and output data as sequences of lines, each terminated by a zero byte (the ASCII NUL character) instead of a newline. Like the <code>-Z</code> or <code>&#8211;null</code> option, this option can be used with commands like <code>sort -z</code> to process arbitrary file names.</dl>
<h2>REGULAR EXPRESSIONS</h2>
<p> A regular expression is a pattern that describes a set of strings. Regular expressions are constructed analogously to arithmetic expressions, by using various operators to combine smaller expressions. </p>
<p> <code>grep</code> understands three different versions of regular expression syntax: &#8220;basic&#8221; (BRE), &#8220;extended&#8221; (ERE) and &#8220;perl&#8221; (PCRE). In GNU <code>grep</code> there is no difference in available functionality between basic and extended syntaxes. In other implementations, basic regular expressions are less powerful. The following description applies to extended regular expressions; differences for basic regular expressions are summarized afterwards. Perl-compatible regular expressions give additional functionality, and are documented in B&lt;pcresyntax&gt;(3) and B&lt;pcrepattern&gt;(3), but work only if PCRE support is enabled. </p>
<p> The fundamental building blocks are the regular expressions that match a single character. Most characters, including all letters and digits, are regular expressions that match themselves. Any meta-character with special meaning may be quoted by preceding it with a backslash. </p>
<p> The period <code>.</code> matches any single character. It is unspecified whether it matches an encoding error.</p>
<h3>Character Classes and Bracket Expressions</h3>
<p> A <i>bracket expression</i> is a list of characters enclosed by <code>[</code> and <code>]</code>. It matches any single character in that list. If the first character of the list is the caret <code>^</code> then it matches any character <i>not</i> in the list; it is unspecified whether it matches an encoding error. For example, the regular expression <code>[0123456789]</code> matches any single digit. </p>
<p> Within a bracket expression, a <i>range expression</i> consists of two characters separated by a hyphen. It matches any single character that sorts between the two characters, inclusive, using the locale&#8217;s collating sequence and character set. For example, in the default C locale, <code>[a-d]</code> is equivalent to <code>[abcd]</code>. Many locales sort characters in dictionary order, and in these locales <code>[a-d]</code> is typically not equivalent to <code>[abcd]</code>; it might be equivalent to <code>[aBbCcDd]</code>, for example. To obtain the traditional interpretation of bracket expressions, you can use the C locale by setting the <code>LC_ALL</code> environment variable to the value <code>C</code>. </p>
<p> Finally, certain named classes of characters are predefined within bracket expressions, as follows. Their names are self explanatory, and they are <code>[:alnum:]</code>, <code>[:alpha:]</code>, <code>[:blank:]</code>, <code>[:cntrl:]</code>, <code>[:digit:]</code>, <code>[:graph:]</code>, <code>[:lower:]</code>, <code>[:print:]</code>, <code>[:punct:]</code>, <code>[:space:]</code>, <code>[:upper:]</code>, and <code>[:xdigit:]</code>. For example, <code>[[:alnum:]]</code> means the character class of numbers and letters in the current locale. In the C locale and ASCII character set encoding, this is the same as <code>[0-9A-Za-z]</code>. (Note that the brackets in these class names are part of the symbolic names, and must be included in addition to the brackets delimiting the bracket expression.) Most meta-characters lose their special meaning inside bracket expressions. To include a literal <code>]</code> place it first in the list. Similarly, to include a literal <code>^</code> place it anywhere but first. Finally, to include a literal <code>&#8211;</code> place it last.</p>
<h3>Anchoring</h3>
<p> The caret <code>^</code> and the dollar sign <code>$</code> are meta-characters that respectively match the empty string at the beginning and end of a line.</p>
<h3>The Backslash Character and Special Expressions</h3>
<p> The symbols <code>\&lt;</code> and <code>\&gt;</code> respectively match the empty string at the beginning and end of a word. The symbol <code></code> matches the empty string at the edge of a word, and <code>\B</code> matches the empty string provided it&#8217;s <i>not</i> at the edge of a word. The symbol <code>\w</code> is a synonym for <code>[_[:alnum:]]</code> and <code>\W</code> is a synonym for <code>[^_[:alnum:]]</code>.</p>
<h3>Repetition</h3>
<p> A regular expression may be followed by one of several repetition operators:</p>
<dl>
<dt><code>?</code></p>
<dd> The preceding item is optional and matched at most once.</p>
<dt><code>*</code></p>
<dd> The preceding item will be matched zero or more times.</p>
<dt><code>+</code></p>
<dd> The preceding item will be matched one or more times.</p>
<dt><code>{</code><i>n</i><code>}</code></p>
<dd> The preceding item is matched exactly <i>n</i> times.</p>
<dt><code>{</code><i>n</i><code>,}</code></p>
<dd> The preceding item is matched <i>n</i> or more times.</p>
<dt><code>{,</code><i>m</i><code>}</code></p>
<dd> The preceding item is matched at most <i>m</i> times. This is a GNU extension.</p>
<dt><code>{</code><i>n</i><code>,</code><i>m</i><code>}</code></p>
<dd> The preceding item is matched at least <i>n</i> times, but not more than <i>m</i> times.</dl>
<h3>Concatenation</h3>
<p> Two regular expressions may be concatenated; the resulting regular expression matches any string formed by concatenating two substrings that respectively match the concatenated expressions.</p>
<h3>Alternation</h3>
<p> Two regular expressions may be joined by the infix operator <code>|</code>; the resulting regular expression matches any string matching either alternate expression.</p>
<h3>Precedence</h3>
<p> Repetition takes precedence over concatenation, which in turn takes precedence over alternation. A whole expression may be enclosed in parentheses to override these precedence rules and form a subexpression.</p>
<h3>Back-references and Subexpressions</h3>
<p> The back-reference <code>\</code><i>n</i>, where <i>n</i> is a single digit, matches the substring previously matched by the <i>n</i>th parenthesized subexpression of the regular expression.</p>
<h3>Basic vs Extended Regular Expressions</h3>
<p> In basic regular expressions the meta-characters <code>?</code>, <code>+</code>, <code>{</code>, <code>|</code>, <code>(</code>, and <code>)</code> lose their special meaning; instead use the backslashed versions <code>\?</code>, <code>\+</code>, <code>\{</code>, <code>\|</code>, <code>\(</code>, and <code>\)</code>.</p>
<h2>EXIT STATUS</h2>
<p> Normally the exit status is 0 if a line is selected, 1 if no lines were selected, and 2 if an error occurred. However, if the <code>-q</code> or <code>&#8211;quiet</code> or <code>&#8211;silent</code> is used and a line is selected, the exit status is 0 even if an error occurred.</p>
<h2>ENVIRONMENT</h2>
<p> The behavior of <code>grep</code> is affected by the following environment variables. </p>
<p> The locale for category <code>LC_</code><i>foo</i> is specified by examining the three environment variables <code>LC_ALL</code>, <code>LC_</code><i>foo</i>, <code>LANG</code>, in that order. The first of these variables that is set specifies the locale. For example, if <code>LC_ALL</code> is not set, but <code>LC_MESSAGES</code> is set to <code>pt_BR</code>, then the Brazilian Portuguese locale is used for the <code>LC_MESSAGES</code> category. The C locale is used if none of these environment variables are set, if the locale catalog is not installed, or if <code>grep</code> was not compiled with national language support (NLS). The shell command <code>locale -a</code> lists locales that are currently available.</p>
<dl>
<dt><code>GREP_COLOR</code></p>
<dd> This variable specifies the color used to highlight matched (non-empty) text. It is deprecated in favor of <code>GREP_COLORS</code>, but still supported. The <code>mt</code>, <code>ms</code>, and <code>mc</code> capabilities of <code>GREP_COLORS</code> have priority over it. It can only specify the color used to highlight the matching non-empty text in any matching line (a selected line when the <code>-v</code> command-line option is omitted, or a context line when <code>-v</code> is specified). The default is <code>01;31</code>, which means a bold red foreground text on the terminal&#8217;s default background.</p>
<dt><code>GREP_COLORS</code></p>
<dd> Specifies the colors and other attributes used to highlight various parts of the output. Its value is a colon-separated list of capabilities that defaults to <code>ms=01;31:mc=01;31:sl=:cx=:fn=35:ln=32:bn=32:se=36</code> with the <code>rv</code> and <code>ne</code> boolean capabilities omitted (i.e., false). Supported capabilities are as follows.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sl=</code></p>
<dd> SGR substring for whole selected lines (i.e., matching lines when the <code>-v</code> command-line option is omitted, or non-matching lines when <code>-v</code> is specified). If however the boolean <code>rv</code> capability and the <code>-v</code> command-line option are both specified, it applies to context matching lines instead. The default is empty (i.e., the terminal&#8217;s default color pair).</p>
<dt><code>cx=</code></p>
<dd> SGR substring for whole context lines (i.e., non-matching lines when the <code>-v</code> command-line option is omitted, or matching lines when <code>-v</code> is specified). If however the boolean <code>rv</code> capability and the <code>-v</code> command-line option are both specified, it applies to selected non-matching lines instead. The default is empty (i.e., the terminal&#8217;s default color pair).</p>
<dt><code>rv</code></p>
<dd> Boolean value that reverses (swaps) the meanings of the <code>sl=</code> and <code>cx=</code> capabilities when the <code>-v</code> command-line option is specified. The default is false (i.e., the capability is omitted).</p>
<dt><code>mt=01;31</code></p>
<dd> SGR substring for matching non-empty text in any matching line (i.e., a selected line when the <code>-v</code> command-line option is omitted, or a context line when <code>-v</code> is specified). Setting this is equivalent to setting both <code>ms=</code> and <code>mc=</code> at once to the same value. The default is a bold red text foreground over the current line background.</p>
<dt><code>ms=01;31</code></p>
<dd> SGR substring for matching non-empty text in a selected line. (This is only used when the <code>-v</code> command-line option is omitted.) The effect of the <code>sl=</code> (or <code>cx=</code> if <code>rv</code>) capability remains active when this kicks in. The default is a bold red text foreground over the current line background.</p>
<dt><code>mc=01;31</code></p>
<dd> SGR substring for matching non-empty text in a context line. (This is only used when the <code>-v</code> command-line option is specified.) The effect of the <code>cx=</code> (or <code>sl=</code> if <code>rv</code>) capability remains active when this kicks in. The default is a bold red text foreground over the current line background.</p>
<dt><code>fn=35</code></p>
<dd> SGR substring for file names prefixing any content line. The default is a magenta text foreground over the terminal&#8217;s default background.</p>
<dt><code>ln=32</code></p>
<dd> SGR substring for line numbers prefixing any content line. The default is a green text foreground over the terminal&#8217;s default background.</p>
<dt><code>bn=32</code></p>
<dd> SGR substring for byte offsets prefixing any content line. The default is a green text foreground over the terminal&#8217;s default background.</p>
<dt><code>se=36</code></p>
<dd> SGR substring for separators that are inserted between selected line fields (<code>:</code>), between context line fields, (<code>&#8211;</code>), and between groups of adjacent lines when nonzero context is specified (<code>&#8212;</code>). The default is a cyan text foreground over the terminal&#8217;s default background.</p>
<dt><code>ne</code></p>
<dd> Boolean value that prevents clearing to the end of line using Erase in Line (EL) to Right (<code>\33[K</code>) each time a colorized item ends. This is needed on terminals on which EL is not supported. It is otherwise useful on terminals for which the <code>back_color_erase</code> (<code>bce</code>) boolean terminfo capability does not apply, when the chosen highlight colors do not affect the background, or when EL is too slow or causes too much flicker. The default is false (i.e., the capability is omitted).</dl>
<p> Note that boolean capabilities have no <code>=</code>&#8230; part. They are omitted (i.e., false) by default and become true when specified. </p>
<p> See the Select Graphic Rendition (SGR) section in the documentation of the text terminal that is used for permitted values and their meaning as character attributes. These substring values are integers in decimal representation and can be concatenated with semicolons. <code>grep</code> takes care of assembling the result into a complete SGR sequence (<code>\33[</code>&#8230;<code>m</code>). Common values to concatenate include <code>1</code> for bold, <code>4</code> for underline, <code>5</code> for blink, <code>7</code> for inverse, <code>39</code> for default foreground color, <code>30</code> to <code>37</code> for foreground colors, <code>90</code> to <code>97</code> for 16-color mode foreground colors, <code>38;5;0</code> to <code>38;5;255</code> for 88-color and 256-color modes foreground colors, <code>49</code> for default background color, <code>40</code> to <code>47</code> for background colors, <code>100</code> to <code>107</code> for 16-color mode background colors, and <code>48;5;0</code> to <code>48;5;255</code> for 88-color and 256-color modes background colors.</dl>
<dt><code>LC_ALL</code>, <code>LC_COLLATE</code>, <code>LANG</code></p>
<dd> These variables specify the locale for the <code>LC_COLLATE</code> category, which determines the collating sequence used to interpret range expressions like <code>[a-z]</code>.</p>
<dt><code>LC_ALL</code>, <code>LC_CTYPE</code>, <code>LANG</code></p>
<dd> These variables specify the locale for the <code>LC_CTYPE</code> category, which determines the type of characters, e.g., which characters are whitespace. This category also determines the character encoding, that is, whether text is encoded in UTF-8, ASCII, or some other encoding. In the C or POSIX locale, all characters are encoded as a single byte and every byte is a valid character.</p>
<dt><code>LC_ALL</code>, <code>LC_MESSAGES</code>, <code>LANG</code></p>
<dd> These variables specify the locale for the <code>LC_MESSAGES</code> category, which determines the language that <code>grep</code> uses for messages. The default C locale uses American English messages.</p>
<dt><code>POSIXLY_CORRECT</code></p>
<dd> If set, <code>grep</code> behaves as POSIX requires; otherwise, <code>grep</code> behaves more like other GNU programs. POSIX requires that options that follow file names must be treated as file names; by default, such options are permuted to the front of the operand list and are treated as options. Also, POSIX requires that unrecognized options be diagnosed as &#8220;illegal&#8221;, but since they are not really against the law the default is to diagnose them as &#8220;invalid&#8221;. <code>POSIXLY_CORRECT</code> also disables <code>_</code><i>N</i><code>_GNU_nonoption_argv_flags_</code>, described below.</p>
<dt><code>_</code><i>N</i><code>_GNU_nonoption_argv_flags_</code></p>
<dd> (Here <i>N</i> is <code>grep</code>&#8216;s numeric process ID.) If the <i>i</i>th character of this environment variable&#8217;s value is <code>1</code>, do not consider the <i>i</i>th operand of <code>grep</code> to be an option, even if it appears to be one. A shell can put this variable in the environment for each command it runs, specifying which operands are the results of file name wildcard expansion and therefore should not be treated as options. This behavior is available only with the GNU C library, and only when <code>POSIXLY_CORRECT</code> is not set.</dl>
<h2>NOTES</h2>
<p> This man page is maintained only fitfully; the full documentation is often more up-to-date.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1998-2000, 2002, 2005-2021 Free Software Foundation, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>BUGS</h2>
<h3>Reporting Bugs</h3>
<p> Email bug reports to the bug-reporting address An email archive and a bug tracker are available.</p>
<h3>Known Bugs</h3>
<p> Large repetition counts in the <code>{</code><i>n</i><code>,</code><i>m</i><code>}</code> construct may cause <code>grep</code> to use lots of memory. In addition, certain other obscure regular expressions require exponential time and space, and may cause <code>grep</code> to run out of memory. </p>
<p> Back-references are very slow, and may require exponential time.</p>
<h2>EXAMPLE</h2>
<p> The following example outputs the location and contents of any line containing &#8220;f&#8221; and ending in &#8220;.c&#8221;, within all files in the current directory whose names contain &#8220;g&#8221; and end in &#8220;.h&#8221;. The <code>-n</code> option outputs line numbers, the <code>&#8212;</code> argument treats expansions of &#8220;*g*.h&#8221; starting with &#8220;-&#8221; as file names not options, and the empty file /dev/null causes file names to be output even if only one file name happens to be of the form &#8220;*g*.h&#8221;. </p>
<p> $ <code>grep</code> -n &#8212; &#8216;f.*\.c$&#8217; *g*.h /dev/null argmatch.h:1:/* definitions and prototypes for argmatch.c </p>
<p> The only line that matches is line 1 of argmatch.h. Note that the regular expression syntax used in the pattern differs from the globbing syntax that the shell uses to match file names.</p>
<h2>SEE ALSO</h2>
<h3>Regular Manual Pages</h3>
<p> <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1), <code><a href="/docs/linux/man/1-cmp/">cmp</a></code>(1), <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1), <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1), <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/3-pcre/">pcre</a></code>(3), <code><a href="/docs/linux/man/3-pcresyntax/">pcresyntax</a></code>(3), <code><a href="/docs/linux/man/3-pcrepattern/">pcrepattern</a></code>(3), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5), <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7)</p>
<h3>Full Documentation</h3>
<p> A complete manual is available. If the <code>info</code> and <code>grep</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grep</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
