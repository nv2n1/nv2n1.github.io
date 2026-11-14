---
title: "ack(1)"
name: "ack"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ack/"
description: "ack – grep-like text finder"
---

<h2 class="name">NAME</h2>
<p> ack &#8211; grep-like text finder </p>
<h2>SYNOPSIS</h2>
<pre><code>
ack[options] PATTERN[FILE...] ack - f[options][DIRECTORY...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Ack is designed as a replacement for 99% of the uses of <i>grep</i>. </p>
<p> Ack searches the named input FILEs (or standard input if no files are named, or the file name &#8211; is given) for lines containing a match to the given <font SIZE="-1">PATTERN. </font> By default, ack prints the matching lines. </p>
<p> <font SIZE="-1">PATTERN</font> is a Perl regular expression. Perl regular expressions are commonly found in other programming languages, but for the particulars of their behavior, please consult &lt;<a rel="nofollow" href="http://perldoc.perl.org/perlreref.html|perlreref">http://perldoc.perl.org/perlreref.html|perlreref</a>&gt;. If you don&#8217;t know how to use regular expression but are interested in learning, you may consult &lt;<a rel="nofollow" href="http://perldoc.perl.org/perlretut.html|perlretut">http://perldoc.perl.org/perlretut.html|perlretut</a>&gt;. If you do not need or want ack to use regular expressions, please see the <tt>&quot;-Q&quot;</tt>/<tt>&quot;--literal&quot;</tt> option. </p>
<p> Ack can also list files that would be searched, without actually searching them, to let you take advantage of ack&#8217;s file-type filtering capabilities.</p>
<h2>FILE SELECTION</h2>
<p> If files are not specified for searching, either on the command line or piped in with the <tt>&quot;-x&quot;</tt> option, <i>ack</i> delves into subdirectories selecting files for searching. </p>
<p> <i>ack</i> is intelligent about the files it searches. It knows about certain file types, based on both the extension on the file and, in some cases, the contents of the file. These selections can be made with the <code>&#8211;type</code> option. </p>
<p> With no file selection, <i>ack</i> searches through regular files that are not explicitly excluded by <code>&#8211;ignore-dir</code> and <code>&#8211;ignore-file</code> options, either present in <i>ackrc</i> files or on the command line. </p>
<p> The default options for <i>ack</i> ignore certain files and directories. These include:</p>
<dl>
<dt>&bull;</p>
<dd> Backup files: Files matching <i>#*#</i> or ending with <i>~</i>.</p>
<dt>&bull;</p>
<dd> Coredumps: Files matching <i>core.\d+</i></p>
<dt>&bull;</p>
<dd> Version control directories like <i>.svn</i> and <i>.git</i>.</dl>
<p> Run <i>ack</i> with the <tt>&quot;--dump&quot;</tt> option to see what settings are set. </p>
<p> However, <i>ack</i> always searches the files given on the command line, no matter what type. If you tell <i>ack</i> to search in a coredump, it will search in a coredump.</p>
<h2>DIRECTORY SELECTION</h2>
<p> <i>ack</i> descends through the directory tree of the starting directories specified. If no directories are specified, the current working directory is used. However, it will ignore the shadow directories used by many version control systems, and the build directories used by the Perl MakeMaker system. You may add or remove a directory from this list with the <code>&#8211;[no]ignore-dir</code> option. The option may be repeated to add/remove multiple directories from the ignore list. </p>
<p> For a complete list of directories that do not get searched, run <tt>&quot;ack --dump&quot;</tt>.</p>
<h2>WHEN TO USE GREP</h2>
<p> <i>ack</i> trumps <i>grep</i> as an everyday tool 99% of the time, but don&#8217;t throw <i>grep</i> away, because there are times you&#8217;ll still need it. </p>
<p> E.g., searching through huge files looking for regexes that can be expressed with <i>grep</i> syntax should be quicker with <i>grep</i>. </p>
<p> If your script or parent program uses <i>grep</i> <tt>&quot;--quiet&quot;</tt> or <tt>&quot;--silent&quot;</tt> or needs exit 2 on <font SIZE="-1">IO</font> error, use <i>grep</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;ackrc</code></p>
<dd> Specifies an ackrc file to load after all others; see &#8220;<font SIZE="-1">ACKRC LOCATION SEMANTICS&#8221;</font>.</p>
<dt><code>-A </code><font SIZE="-1">NUM</font>, <code>&#8211;after-context=</code><font SIZE="-1">NUM</font></p>
<dd> Print <i></i><font SIZE="-1"><i>NUM</i></font><i></i> lines of trailing context after matching lines.</p>
<dt><code>-B </code><font SIZE="-1">NUM</font>, <code>&#8211;before-context=</code><font SIZE="-1">NUM</font></p>
<dd> Print <i></i><font SIZE="-1"><i>NUM</i></font><i></i> lines of leading context before matching lines.</p>
<dt><code>&#8211;[no]break</code></p>
<dd> Print a break between results from different files. On by default when used interactively.</p>
<dt><code>-C [</code><font SIZE="-1">NUM</font><code>]</code>, <code>&#8211;context[=</code><font SIZE="-1">NUM</font><code>]</code></p>
<dd> Print <i></i><font SIZE="-1"><i>NUM</i></font><i></i> lines (default 2) of context around matching lines.</p>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> Suppress normal output; instead print a count of matching lines for each input file. If <code>-l</code> is in effect, it will only show the number of lines for each file that has lines matching. Without <code>-l</code>, some line counts may be zeroes. </p>
<p> If combined with <code>-h</code> (<code>&#8211;no-filename</code>) ack outputs only one total count.</p>
<dt><code>&#8211;[no]color</code>, <code>&#8211;[no]colour</code></p>
<dd> <code>&#8211;color</code> highlights the matching text. <code>&#8211;nocolor</code> suppresses the color. This is on by default unless the output is redirected. </p>
<p> On Windows, this option is off by default unless the Win32::Console::ANSI module is installed or the <tt>&quot;ACK_PAGER_COLOR&quot;</tt> environment variable is used.</p>
<dt><code>&#8211;color-filename=</code>color</p>
<dd> Sets the color to be used for filenames.</p>
<dt><code>&#8211;color-match=</code>color</p>
<dd> Sets the color to be used for matches.</p>
<dt><code>&#8211;color-lineno=</code>color</p>
<dd> Sets the color to be used for line numbers.</p>
<dt><code>&#8211;[no]column</code></p>
<dd> Show the column number of the first match. This is helpful for editors that can place your cursor at a given position.</p>
<dt><code>&#8211;create-ackrc</code></p>
<dd> Dumps the default ack options to standard output. This is useful for when you want to customize the defaults.</p>
<dt><code>&#8211;dump</code></p>
<dd> Writes the list of options loaded and where they came from to standard output. Handy for debugging.</p>
<dt><code>&#8211;[no]env</code></p>
<dd> <code>&#8211;noenv</code> disables all environment processing. No <i>.ackrc</i> is read and all environment variables are ignored. By default, <i>ack</i> considers <i>.ackrc</i> and settings in the environment.</p>
<dt><code>&#8211;flush</code></p>
<dd> <code>&#8211;flush</code> flushes output immediately. This is off by default unless ack is running interactively (when output goes to a pipe or file).</p>
<dt><code>-f</code></p>
<dd> Only print the files that would be searched, without actually doing any searching. <font SIZE="-1">PATTERN</font> must not be specified, or it will be taken as a path to search.</p>
<dt><code>&#8211;files-from=</code><font SIZE="-1">FILE</font></p>
<dd> The list of files to be searched is specified in <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. The list of files are separated by newlines. If <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is <tt>&quot;-&quot;</tt>, the list is loaded from standard input.</p>
<dt><code>&#8211;[no]filter</code></p>
<dd> Forces ack to act as if it were receiving input via a pipe.</p>
<dt><code>&#8211;[no]follow</code></p>
<dd> Follow or don&#8217;t follow symlinks, other than whatever starting files or directories were specified on the command line. </p>
<p> This is off by default.</p>
<dt><code>-g </code><font SIZE="-1">PATTERN</font></p>
<dd> Print files where the relative path + filename matches <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i>. This option can be combined with <code>&#8211;color</code> to make it easier to spot the match.</p>
<dt><code>&#8211;[no]group</code></p>
<dd> <code>&#8211;group</code> groups matches by file name. This is the default when used interactively. </p>
<p> <code>&#8211;nogroup</code> prints one result per line, like grep. This is the default when output is redirected.</p>
<dt><code>-H</code>, <code>&#8211;with-filename</code></p>
<dd> Print the filename for each match. This is the default unless searching a single explicitly specified file.</p>
<dt><code>-h</code>, <code>&#8211;no-filename</code></p>
<dd> Suppress the prefixing of filenames on output when multiple files are searched.</p>
<dt><code>&#8211;[no]heading</code></p>
<dd> Print a filename heading above each file&#8217;s results. This is the default when used interactively.</p>
<dt><code>&#8211;help</code>, <code>-?</code></p>
<dd> Print a short help statement.</p>
<dt><code>&#8211;help-types</code>, <code>&#8211;help=types</code></p>
<dd> Print all known types.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> Ignore case distinctions in <font SIZE="-1">PATTERN</font></p>
<dt><code>&#8211;ignore-ack-defaults</code></p>
<dd> Tells ack to completely ignore the default definitions provided with ack. This is useful in combination with <code>&#8211;create-ackrc</code> if you <i>really</i> want to customize ack.</p>
<dt><code>&#8211;[no]ignore-dir=</code><font SIZE="-1">DIRNAME</font>, <code>&#8211;[no]ignore-directory=</code><font SIZE="-1">DIRNAME</font></p>
<dd> Ignore directory (as <font SIZE="-1">CVS, </font>.svn, etc are ignored). May be used multiple times to ignore multiple directories. For example, mason users may wish to include <code>&#8211;ignore-dir=data</code>. The <code>&#8211;noignore-dir</code> option allows users to search directories which would normally be ignored (perhaps to research the contents of <i>.svn/props</i> directories). </p>
<p> The <i></i><font SIZE="-1"><i>DIRNAME</i></font><i></i> must always be a simple directory name. Nested directories like <i>foo/bar</i> are <font SIZE="-1">NOT</font> supported. You would need to specify <code>&#8211;ignore-dir=foo</code> and then no files from any foo directory are taken into account by ack unless given explicitly on the command line.</p>
<dt><code>&#8211;ignore-file=</code><font SIZE="-1">FILTERTYPE:FILTERARGS</font></p>
<dd> Ignore files matching <i></i><font SIZE="-1"><i>FILTERTYPE:FILTERARGS</i></font><i></i>. The filters are specified identically to file type filters as seen in &#8220;Defining your own types&#8221;.</p>
<dt><code>-k</code>, <code>&#8211;known-types</code></p>
<dd> Limit selected files to those with types that ack knows about. This is equivalent to the default behavior found in ack 1.</p>
<dt><code>&#8211;lines=</code><font SIZE="-1">NUM</font></p>
<dd> Only print line <i></i><font SIZE="-1"><i>NUM</i></font><i></i> of each file. Multiple lines can be given with multiple <code>&#8211;lines</code> options or as a comma separated list (<code>&#8211;lines=3,5,7</code>). <code>&#8211;lines=4-7</code> also works. The lines are always output in ascending order, no matter the order given on the command line.</p>
<dt><code>-l</code>, <code>&#8211;files-with-matches</code></p>
<dd> Only print the filenames of matching files, instead of the matching text.</p>
<dt><code>-L</code>, <code>&#8211;files-without-matches</code></p>
<dd> Only print the filenames of files that do <i></i><font SIZE="-1"><i>NOT</i></font><i></i> match.</p>
<dt><code>&#8211;match </code><font SIZE="-1">PATTERN</font></p>
<dd> Specify the <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> explicitly. This is helpful if you don&#8217;t want to put the regex as your first argument, e.g. when executing multiple searches over the same set of files. </p>
<pre>
    # search for foo and bar in given files
    ack file1 t/file* --match foo
    ack file1 t/file* --match bar
</pre>
<dt><code>-m=</code><font SIZE="-1">NUM</font>, <code>&#8211;max-count=</code><font SIZE="-1">NUM</font></p>
<dd> Stop reading a file after <i></i><font SIZE="-1"><i>NUM</i></font><i></i> matches.</p>
<dt><code>&#8211;man</code></p>
<dd> Print this manual page.</p>
<dt><code>-n</code>, <code>&#8211;no-recurse</code></p>
<dd> No descending into subdirectories.</p>
<dt><code>-o</code></p>
<dd> Show only the part of each line matching <font SIZE="-1">PATTERN </font>(turns off text highlighting)</p>
<dt><code>&#8211;output=</code>expr</p>
<dd> Output the evaluation of <i>expr</i> for each line (turns off text highlighting) If <font SIZE="-1">PATTERN</font> matches more than once then a line is output for each non-overlapping match. For more information please see the section &quot;Examples of <i>&#8211;output</i>&quot;.</p>
<dt><code>&#8211;pager=</code>program, <code>&#8211;nopager</code></p>
<dd> <code>&#8211;pager</code> directs ack&#8217;s output through <i>program</i>. This can also be specified via the <tt>&quot;ACK_PAGER&quot;</tt> and <tt>&quot;ACK_PAGER_COLOR&quot;</tt> environment variables. </p>
<p> Using &#8211;pager does not suppress grouping and coloring like piping output on the command-line does. </p>
<p> <code>&#8211;nopager</code> cancels any setting in ~/.ackrc, <tt>&quot;ACK_PAGER&quot;</tt> or <tt>&quot;ACK_PAGER_COLOR&quot;</tt>. No output will be sent through a pager.</p>
<dt><code>&#8211;passthru</code></p>
<dd> Prints all lines, whether or not they match the expression. Highlighting will still work, though, so it can be used to highlight matches while still seeing the entire file, as in: </p>
<pre>
    # Watch a log file, and highlight a certain IP address
    $ tail -f ~/access.log | ack --passthru 123.45.67.89
</pre>
<dt><code>&#8211;print0</code></p>
<dd> Only works in conjunction with -f, -g, -l or -c (filename output). The filenames are output separated with a null byte instead of the usual newline. This is helpful when dealing with filenames that contain whitespace, e.g. </p>
<pre>
    # remove all files of type html
    ack -f --html --print0 | xargs -0 rm -f
</pre>
<dt><code>-Q</code>, <code>&#8211;literal</code></p>
<dd> Quote all metacharacters in <font SIZE="-1">PATTERN,</font> it is treated as a literal.</p>
<dt><code>-r</code>, <code>-R</code>, <code>&#8211;recurse</code></p>
<dd> Recurse into sub-directories. This is the default and just here for compatibility with grep. You can also use it for turning <code>&#8211;no-recurse</code> off.</p>
<dt><code>-s</code></p>
<dd> Suppress error messages about nonexistent or unreadable files. This is taken from fgrep.</p>
<dt><code>&#8211;[no]smart-case</code>, <code>&#8211;no-smart-case</code></p>
<dd> Ignore case in the search strings if <font SIZE="-1">PATTERN</font> contains no uppercase characters. This is similar to <tt>&quot;smartcase&quot;</tt> in vim. This option is off by default, and ignored if <tt>&quot;-i&quot;</tt> is specified. </p>
<p> <code>-i</code> always overrides this option.</p>
<dt><code>&#8211;sort-files</code></p>
<dd> Sorts the found files lexicographically. Use this if you want your file listings to be deterministic between runs of <i>ack</i>.</p>
<dt><code>&#8211;show-types</code></p>
<dd> Outputs the filetypes that ack associates with each file. </p>
<p> Works with <code>-f</code> and <code>-g</code> options.</p>
<dt><code>&#8211;type=[no]TYPE</code></p>
<dd> Specify the types of files to include or exclude from a search. <font SIZE="-1">TYPE</font> is a filetype, like <i>perl</i> or <i>xml</i>. <code>&#8211;type=perl</code> can also be specified as <code>&#8211;perl</code>, and <code>&#8211;type=noperl</code> can be done as <code>&#8211;noperl</code>. </p>
<p> If a file is of both type &#8220;foo&#8221; and &#8220;bar&#8221;, specifying &#8211;foo and &#8211;nobar will exclude the file, because an exclusion takes precedence over an inclusion. </p>
<p> Type specifications can be repeated and are ORed together. </p>
<p> See <i>ack &#8211;help=types</i> for a list of valid types.</p>
<dt><code>&#8211;type-add </code><font SIZE="-1">TYPE</font><code>:</code><font SIZE="-1">FILTER</font><code>:</code><font SIZE="-1">FILTERARGS</font></p>
<dd> Files with the given <font SIZE="-1">FILTERARGS</font> applied to the given <font SIZE="-1">FILTER</font> are recognized as being of (the existing) type <font SIZE="-1">TYPE.</font> See also &#8220;Defining your own types&#8221;.</p>
<dt><code>&#8211;type-set </code><font SIZE="-1">TYPE</font><code>:</code><font SIZE="-1">FILTER</font><code>:</code><font SIZE="-1">FILTERARGS</font></p>
<dd> Files with the given <font SIZE="-1">FILTERARGS</font> applied to the given <font SIZE="-1">FILTER</font> are recognized as being of type <font SIZE="-1">TYPE.</font> This replaces an existing definition for type <font SIZE="-1">TYPE. </font> See also &#8220;Defining your own types&#8221;.</p>
<dt><code>&#8211;type-del </code><font SIZE="-1">TYPE</font></p>
<dd> The filters associated with <font SIZE="-1">TYPE</font> are removed from Ack, and are no longer considered for searches.</p>
<dt><code>-v</code>, <code>&#8211;invert-match</code></p>
<dd> Invert match: select non-matching lines</p>
<dt><code>&#8211;version</code></p>
<dd> Display version and copyright information.</p>
<dt><code>-w</code>, <code>&#8211;word-regexp</code></p>
<dd> Force <font SIZE="-1">PATTERN</font> to match only whole words. The <font SIZE="-1">PATTERN</font> is wrapped with <tt>&quot;&quot;</tt> metacharacters.</p>
<dt><code>-x</code></p>
<dd> An abbreviation for <code>&#8211;files-from=-</code>; the list of files to search are read from standard input, with one line per file.</p>
<dt><code>-1</code></p>
<dd> Stops after reporting first match of any kind. This is different from <code>&#8211;max-count=1</code> or <code>-m1</code>, where only one match per file is shown. Also, <code>-1</code> works with <code>-f</code> and <code>-g</code>, where <code>-m</code> does not.</p>
<dt><code>&#8211;thpppt</code></p>
<dd> Display the all-important Bill The Cat logo. Note that the exact spelling of <code>&#8211;thpppppt</code> is not important. It&#8217;s checked against a regular expression.</p>
<dt><code>&#8211;bar</code></p>
<dd> Check with the admiral for traps.</p>
<dt><code>&#8211;cathy</code></p>
<dd> Chocolate, Chocolate, Chocolate!</dl>
<h2>THE .ackrc FILE</h2>
<p> The <i>.ackrc</i> file contains command-line options that are prepended to the command line before processing. Multiple options may live on multiple lines. Lines beginning with a # are ignored. A <i>.ackrc</i> might look like this: </p>
<pre><code>
#Always sort the files
--sort - files
#Always color, even if piping to a another program
    -- color
#Use "less -r" as my pager
    -- pager = less - r
</code></pre>
<p> Note that arguments with spaces in them do not need to be quoted, as they are not interpreted by the shell. Basically, each <i>line</i> in the <i>.ackrc</i> file is interpreted as one element of <tt>@ARGV</tt>. </p>
<p> <i>ack</i> looks in several locations for <i>.ackrc</i> files; the searching process is detailed in &#8220;<font SIZE="-1">ACKRC LOCATION SEMANTICS&#8221;</font>. These files are not considered if <code>&#8211;noenv</code> is specified on the command line.</p>
<h2>Defining your own types</h2>
<p> ack allows you to define your own types in addition to the predefined types. This is done with command line options that are best put into an <i>.ackrc</i> file &#8211; then you do not have to define your types over and over again. In the following examples the options will always be shown on one command line so that they can be easily copy &amp; pasted. </p>
<p> <i>ack &#8211;perl foo</i> searches for foo in all perl files. <i>ack &#8211;help=types</i> tells you, that perl files are files ending in .pl, .pm, .pod or .t. So what if you would like to include .xs files as well when searching for &#8211;perl files? <i>ack &#8211;type-add perl:ext:xs &#8211;perl foo</i> does this for you. <code>&#8211;type-add</code> appends additional extensions to an existing type. </p>
<p> If you want to define a new type, or completely redefine an existing type, then use <code>&#8211;type-set</code>. <i>ack &#8211;type-set eiffel:ext:e,eiffel</i> defines the type <i>eiffel</i> to include files with the extensions .e or .eiffel. So to search for all eiffel files containing the word Bertrand use <i>ack &#8211;type-set eiffel:ext:e,eiffel &#8211;eiffel Bertrand</i>. As usual, you can also write <code>&#8211;type=eiffel</code> instead of <code>&#8211;eiffel</code>. Negation also works, so <code>&#8211;noeiffel</code> excludes all eiffel files from a search. Redefining also works: <i>ack &#8211;type-set cc:ext:c,h</i> and <i>.xs</i> files no longer belong to the type <i>cc</i>. </p>
<p> When defining your own types in the <i>.ackrc</i> file you have to use the following: </p>
<pre>
  --type-set=eiffel:ext:e,eiffel
</pre>
<p> or writing on separate lines </p>
<pre>
  --type-set
  eiffel:ext:e,eiffel
</pre>
<p> The following does <font SIZE="-1"><code>NOT</code></font> work in the <i>.ackrc</i> file: </p>
<pre>
  --type-set eiffel:ext:e,eiffel
</pre>
<p> In order to see all currently defined types, use <i>&#8211;help-types</i>, e.g. <i>ack &#8211;type-set backup:ext:bak &#8211;type-add perl:ext:perl &#8211;help-types</i> </p>
<p> In addition to filtering based on extension (like ack 1.x allowed), ack 2 offers additional filter types. The generic syntax is <i>&#8211;type-set </i><font SIZE="-1"><i>TYPE:FILTER:FILTERARGS</i></font><i></i>; <i></i><font SIZE="-1"><i>FILTERARGS</i></font><i></i> depends on the value of <i></i><font SIZE="-1"><i>FILTER</i></font><i></i>.</p>
<dl>
<dt>is:<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd> <i>is</i> filters match the target filename exactly. It takes exactly one argument, which is the name of the file to match. </p>
<p> Example: </p>
<pre>
    --type-set make:is:Makefile
</pre>
<dt>ext:<i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i>[,<i></i><font SIZE="-1"><i>EXTENSION2</i></font><i></i>[,&#8230;]]</p>
<dd> <i>ext</i> filters match the extension of the target file against a list of extensions. No leading dot is needed for the extensions. </p>
<p> Example: </p>
<pre>
    --type-set perl:ext:pl,pm,t
</pre>
<dt>match:<i></i><font SIZE="-1"><i>PATTERN</i></font><i></i></p>
<dd> <i>match</i> filters match the target filename against a regular expression. The regular expression is made case insensitive for the search. </p>
<p> Example: </p>
<pre>
    --type-set make:match:/(gnu)?makefile/
</pre>
<dt>firstlinematch:<i></i><font SIZE="-1"><i>PATTERN</i></font><i></i></p>
<dd> <i>firstlinematch</i> matches the first line of the target file against a regular expression. Like <i>match</i>, the regular expression is made case insensitive. </p>
<p> Example: </p>
<pre>
    --type-add perl:firstlinematch:/perl/
</pre>
</dl>
<p> More filter types may be made available in the future.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> For commonly-used ack options, environment variables can make life much easier. These variables are ignored if <code>&#8211;noenv</code> is specified on the command line.</p>
<dl>
<dt><font SIZE="-1">ACKRC</font></p>
<dd> Specifies the location of the user&#8217;s <i>.ackrc</i> file. If this file doesn&#8217;t exist, <i>ack</i> looks in the default location.</p>
<dt><font SIZE="-1">ACK_OPTIONS</font></p>
<dd> This variable specifies default options to be placed in front of any explicit options on the command line.</p>
<dt><font SIZE="-1">ACK_COLOR_FILENAME</font></p>
<dd> Specifies the color of the filename when it&#8217;s printed in <code>&#8211;group</code> mode. By default, it&#8217;s &#8220;bold green&#8221;. </p>
<p> The recognized attributes are clear, reset, dark, bold, underline, underscore, blink, reverse, concealed black, red, green, yellow, blue, magenta, on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, and on_white. Case is not significant. Underline and underscore are equivalent, as are clear and reset. The color alone sets the foreground color, and on_color sets the background color. </p>
<p> This option can also be set with <code>&#8211;color-filename</code>.</p>
<dt><font SIZE="-1">ACK_COLOR_MATCH</font></p>
<dd> Specifies the color of the matching text when printed in <code>&#8211;color</code> mode. By default, it&#8217;s &#8220;black on_yellow&#8221;. </p>
<p> This option can also be set with <code>&#8211;color-match</code>. </p>
<p> See <font SIZE="-1"><code>ACK_COLOR_FILENAME</code></font> for the color specifications.</p>
<dt><font SIZE="-1">ACK_COLOR_LINENO</font></p>
<dd> Specifies the color of the line number when printed in <code>&#8211;color</code> mode. By default, it&#8217;s &#8220;bold yellow&#8221;. </p>
<p> This option can also be set with <code>&#8211;color-lineno</code>. </p>
<p> See <font SIZE="-1"><code>ACK_COLOR_FILENAME</code></font> for the color specifications.</p>
<dt><font SIZE="-1">ACK_PAGER</font></p>
<dd> Specifies a pager program, such as <tt>&quot;more&quot;</tt>, <tt>&quot;less&quot;</tt> or <tt>&quot;most&quot;</tt>, to which ack will send its output. </p>
<p> Using <tt>&quot;ACK_PAGER&quot;</tt> does not suppress grouping and coloring like piping output on the command-line does, except that on Windows ack will assume that <tt>&quot;ACK_PAGER&quot;</tt> does not support color. </p>
<p> <tt>&quot;ACK_PAGER_COLOR&quot;</tt> overrides <tt>&quot;ACK_PAGER&quot;</tt> if both are specified.</p>
<dt><font SIZE="-1">ACK_PAGER_COLOR</font></p>
<dd> Specifies a pager program that understands <font SIZE="-1">ANSI</font> color sequences. Using <tt>&quot;ACK_PAGER_COLOR&quot;</tt> does not suppress grouping and coloring like piping output on the command-line does. </p>
<p> If you are not on Windows, you never need to use <tt>&quot;ACK_PAGER_COLOR&quot;</tt>.</dl>
<h2>ACK &amp; OTHER TOOLS</h2>
<h3>Vim integration</h3>
<p> <i>ack</i> integrates easily with the Vim text editor. Set this in your <i>.vimrc</i> to use <i>ack</i> instead of <i>grep</i>: </p>
<pre>
    set grepprg=ack\ -k
</pre>
<p> That example uses <tt>&quot;-k&quot;</tt> to search through only files of the types ack knows about, but you may use other default flags. Now you can search with <i>ack</i> and easily step through the results in Vim: </p>
<pre>
  :grep Dumper perllib
</pre>
<p> Miles Sterrett has written a Vim plugin for <i>ack</i> which allows you to use <tt>&quot;:Ack&quot;</tt> instead of <tt>&quot;:grep&quot;</tt>, as well as several other advanced features. </p>
<p> &lt;<a rel="nofollow" href="https://github.com/mileszs/ack.vim">https://github.com/mileszs/ack.vim</a>&gt;</p>
<h3>Emacs integration</h3>
<p> Phil Jackson put together an <i>ack.el</i> extension that &#8220;provides a simple compilation mode &#8230; has the ability to guess what files you want to search for based on the major-mode.&#8221; </p>
<p> &lt;<a rel="nofollow" href="http://www.shellarchive.co.uk/content/emacs.html">http://www.shellarchive.co.uk/content/emacs.html</a>&gt;</p>
<h3>TextMate integration</h3>
<p> Pedro Melo is a TextMate user who writes &quot;I spend my day mostly inside TextMate, and the built-in find-in-project sucks with large projects. So I hacked a TextMate command that was using find + grep to use ack. The result is the Search in Project with ack, and you can find it here: &lt;<a rel="nofollow" href="http://www.simplicidade.org/notes/archives/2008/03/search_in_proje.html">http://www.simplicidade.org/notes/archives/2008/03/search_in_proje.html</a>&gt;&quot;</p>
<h3>Shell and Return Code</h3>
<p> For greater compatibility with <i>grep</i>, <i>ack</i> in normal use returns shell return or exit code of 0 only if something is found and 1 if no match is found. </p>
<p> (Shell exit code 1 is <tt>&quot;$?=256&quot;</tt> in perl with <tt>&quot;system&quot;</tt> or backticks.) </p>
<p> The <i>grep</i> code 2 for errors is not used. </p>
<p> If <tt>&quot;-f&quot;</tt> or <tt>&quot;-g&quot;</tt> are specified, then 0 is returned if at least one file is found. If no files are found, then 1 is returned.</p>
<h2>DEBUGGING ACK PROBLEMS</h2>
<p> If ack gives you output you&#8217;re not expecting, start with a few simple steps.</p>
<h3>Use <code>&#8211;noenv</code></h3>
<p> Your environment variables and <i>.ackrc</i> may be doing things you&#8217;re not expecting, or forgotten you specified. Use <code>&#8211;noenv</code> to ignore your environment and <i>.ackrc</i>.</p>
<h3>Use <code>-f</code> to see what files have been selected</h3>
<p> Ack&#8217;s <code>-f</code> was originally added as a debugging tool. If ack is not finding matches you think it should find, run <i>ack -f</i> to see what files have been selected. You can also add the <tt>&quot;--show-types&quot;</tt> options to show the type of each file selected.</p>
<h3>Use <code>&#8211;dump</code></h3>
<p> This lists the ackrc files that are loaded and the options loaded from them. So for example you can find a list of directories that do not get searched or where filetypes are defined.</p>
<h2>TIPS</h2>
<h3>Use the <i>.ackrc</i> file.</h3>
<p> The <i>.ackrc</i> is the place to put all your options you use most of the time but don&#8217;t want to remember. Put all your &#8211;type-add and &#8211;type-set definitions in it. If you like &#8211;smart-case, set it there, too. I also set &#8211;sort-files there.</p>
<h3>Use <i>-f</i> for working with big codesets</h3>
<p> Ack does more than search files. <tt>&quot;ack -f --perl&quot;</tt> will create a list of all the Perl files in a tree, ideal for sending into <i>xargs</i>. For example: </p>
<pre>
    # Change all &quot;this&quot; to &quot;that&quot; in all Perl files in a tree.
    ack -f --perl | xargs perl -p -i -e's/this/that/g'
</pre>
<p> or if you prefer: </p>
<pre>
    perl -p -i -e's/this/that/g' $(ack -f --perl)
</pre>
<h3>Use <i>-Q</i> when in doubt about metacharacters</h3>
<p> If you&#8217;re searching for something with a regular expression metacharacter, most often a period in a filename or <font SIZE="-1">IP</font> address, add the -Q to avoid false positives without all the backslashing. See the following example for more&#8230;</p>
<h3>Use ack to watch log files</h3>
<p> Here&#8217;s one I used the other day to find trouble spots for a website visitor. The user had a problem loading <i>troublesome.gif</i>, so I took the access log and scanned it with ack twice. </p>
<pre>
    ack -Q aa.bb.cc.dd /path/to/access.log | ack -Q -B5 troublesome.gif
</pre>
<p> The first ack finds only the lines in the Apache log for the given <font SIZE="-1">IP. </font> The second finds the match on my troublesome <font SIZE="-1">GIF,</font> and shows the previous five lines from the log in each case.</p>
<h3>Examples of <i>&#8211;output</i></h3>
<p> Following variables are useful in the expansion string:</p>
<dl>
<dt>$&amp;</p>
<dd> The whole string matched by <font SIZE="-1">PATTERN.</font></p>
<dt>$1, $2, &#8230;</p>
<dd> The contents of the 1st, 2nd &#8230; bracketed group in <font SIZE="-1">PATTERN.</font></p>
<dt>&quot;$`&quot;</p>
<dd> The string before the match.</p>
<dt>&quot;$&#8217;&quot;</p>
<dd> The string after the match.</dl>
<p> For more details and other variables see &lt;<a rel="nofollow" href="http://perldoc.perl.org/perlvar.html#Variables-related-to-regular-expressions|perlvar">http://perldoc.perl.org/perlvar.html#Variables-related-to-regular-expressions|perlvar</a>&gt;. </p>
<p> This example shows how to add text around a particular pattern (in this case adding _ around word with &#8220;e&#8221;) </p>
<pre>
    ack2.pl &quot;\w*e\w*&quot; quick.txt --output=&quot;$`_$&amp;_$'&quot;
    _The_ quick brown fox jumps over the lazy dog
    The quick brown fox jumps _over_ the lazy dog
    The quick brown fox jumps over _the_ lazy dog
</pre>
<p> This shows how to pick out particular parts of a match using ( ) within regular expression. </p>
<pre>
  ack '=head(\d+)\s+(.*)' --output=' $1 : $2'
  input file contains &quot;=head1 NAME&quot;
  output  &quot;1 : NAME&quot;
</pre>
<h3>Share your knowledge</h3>
<p> Join the ack-users mailing list. Send me your tips and I may add them here.</p>
<h2>FAQ</h2>
<h3>Why isn&#8217;t ack finding a match in (some file)?</h3>
<p> Probably because it&#8217;s of a type that ack doesn&#8217;t recognize. ack&#8217;s searching behavior is driven by filetype. <code>If ack doesn&#8217;t know what kind of file it is, ack ignores the file.</code> </p>
<p> Use the <tt>&quot;-f&quot;</tt> switch to see a list of files that ack will search for you. You can use the <tt>&quot;--show-types&quot;</tt> switch to show which type ack thinks each file is.</p>
<h3>Wouldn&#8217;t it be great if <i>ack</i> did search &amp; replace?</h3>
<p> No, ack will always be read-only. Perl has a perfectly good way to do search &amp; replace in files, using the <tt>&quot;-i&quot;</tt>, <tt>&quot;-p&quot;</tt> and <tt>&quot;-n&quot;</tt> switches. </p>
<p> You can certainly use ack to select your files to update. For example, to change all &#8220;foo&#8221; to &#8220;bar&#8221; in all <font SIZE="-1">PHP</font> files, you can do this from the Unix shell: </p>
<pre>
    $ perl -i -p -e's/foo/bar/g' $(ack -f --php)
</pre>
<h3>Can I make ack recognize <i>.xyz</i> files?</h3>
<p> Yes! Please see &#8220;Defining your own types&#8221;. If you think that <i>ack</i> should recognize a type by default, please see &#8220;<font SIZE="-1">ENHANCEMENTS&#8221;</font>.</p>
<h3>There&#8217;s already a program/package called ack.</h3>
<p> Yes, I know.</p>
<h3>Why is it called ack if it&#8217;s called ack-grep?</h3>
<p> The name of the program is &#8220;ack&#8221;. Some packagers have called it &#8220;ack-grep&#8221; when creating packages because there&#8217;s already a package out there called &#8220;ack&#8221; that has nothing to do with this ack. </p>
<p> I suggest you make a symlink named <i>ack</i> that points to <i>ack-grep</i> because one of the crucial benefits of ack is having a name that&#8217;s so short and simple to type. </p>
<p> To do that, run this with <i>sudo</i> or as root: </p>
<pre>
   ln -s /usr/bin/ack-grep /usr/bin/ack
</pre>
<p> Alternatively, you could use a shell alias: </p>
<pre>
    # bash/zsh
    alias ack=ack-grep
    # csh
    alias ack ack-grep
</pre>
<h3>What does <i>ack</i> mean?</h3>
<p> Nothing. I wanted a name that was easy to type and that you could pronounce as a single syllable.</p>
<h3>Can I do multi-line regexes?</h3>
<p> No, ack does not support regexes that match multiple lines. Doing so would require reading in the entire file at a time. </p>
<p> If you want to see lines near your match, use the <tt>&quot;--A&quot;</tt>, <tt>&quot;--B&quot;</tt> and <tt>&quot;--C&quot;</tt> switches for displaying context.</p>
<h3>Why is ack telling me I have an invalid option when searching for +foo?</h3>
<p> ack treats command line options beginning with <tt>&quot;+&quot;</tt> or <tt>&quot;-&quot;</tt> as options; if you would like to search for these, you may prefix your search term with <tt>&quot;--&quot;</tt> or use the <tt>&quot;--match&quot;</tt> option. (However, don&#8217;t forget that <tt>&quot;+&quot;</tt> is a regular expression metacharacter!)</p>
<h3>Why does ack &#8216;.{40000,}&#8217; fail? Isn&#8217;t that a valid regex?</h3>
<p> The Perl language limits the repetition quanitifier to 32K. You can search for <tt>&quot;.{32767}&quot;</tt> but not <tt>&quot;.{32768}&quot;</tt>.</p>
<h2>ACKRC LOCATION SEMANTICS</h2>
<p> Ack can load its configuration from many sources. This list specifies the sources Ack looks for configuration; each one that is found is loaded in the order specified here, and each one overrides options set in any of the sources preceding it. (For example, if I set &#8211;sort-files in my user ackrc, and &#8211;nosort-files on the command line, the command line takes precedence)</p>
<dl>
<dt>&bull;</p>
<dd> Defaults are loaded from App::Ack::ConfigDefaults. This can be omitted using <tt>&quot;--ignore-ack-defaults&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Global ackrc </p>
<p> Options are then loaded from the global ackrc. This is located at <tt>&quot;/etc/ackrc&quot;</tt> on Unix-like systems, and <tt>&quot;C:\Documents and Settings\All Users\Application Datackrc&quot;</tt> on Windows. This can be omitted using <tt>&quot;--noenv&quot;</tt>.</p>
<dt>&bull;</p>
<dd> User ackrc </p>
<p> Options are then loaded from the user&#8217;s ackrc. This is located at <tt>&quot;$HOME/.ackrc&quot;</tt> on Unix-like systems, and <tt>&quot;C:\Documents and Settings\$USER\Application Datackrc&quot;</tt>. If a different ackrc is desired, it may be overridden with the <tt>$ACKRC</tt> environment variable. This can be omitted using <tt>&quot;--noenv&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Project ackrc </p>
<p> Options are then loaded from the project ackrc. The project ackrc is the first ackrc file with the name <tt>&quot;.ackrc&quot;</tt> or <tt>&quot;_ackrc&quot;</tt>, first searching in the current directory, then the parent directory, then the grandparent directory, etc. This can be omitted using <tt>&quot;--noenv&quot;</tt>.</p>
<dt>&bull;</p>
<dd> &#8211;ackrc </p>
<p> The <tt>&quot;--ackrc&quot;</tt> option may be included on the command line to specify an ackrc file that can override all others. It is consulted even if <tt>&quot;--noenv&quot;</tt> is present.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">ACK_OPTIONS</font> </p>
<p> Options are then loaded from the environment variable <tt>&quot;ACK_OPTIONS&quot;</tt>. This can be omitted using <tt>&quot;--noenv&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Command line </p>
<p> Options are then loaded from the command line.</dl>
<h2>DIFFERENCES BETWEEN ACK 1.X AND ACK 2.X</h2>
<p> A lot of changes were made for ack 2; here is a list of them.</p>
<h3><font SIZE="-1">GENERAL CHANGES</font></h3>
<dl>
<dt>&bull;</p>
<dd> When no selectors are specified, ack 1.x only searches through files that it can map to a file type. ack 2.x, by contrast, will search through every regular, non-binary file that is not explicitly ignored via <code>&#8211;ignore-file</code> or <code>&#8211;ignore-dir</code>. This is similar to the behavior of the <code>-a/&#8211;all</code> option in ack 1.x.</p>
<dt>&bull;</p>
<dd> A more flexible filter system has been added, so that more powerful file types may be created by the user. For details, please consult &#8220;Defining your own types&#8221;.</p>
<dt>&bull;</p>
<dd> ack now loads multiple ackrc files; see &#8220;<font SIZE="-1">ACKRC LOCATION SEMANTICS&#8221;</font> for details.</p>
<dt>&bull;</p>
<dd> ack&#8217;s default filter definitions aren&#8217;t special; you may tell ack to completely disregard them if you don&#8217;t like them.</dl>
<h3><font SIZE="-1">REMOVED OPTIONS</font></h3>
<dl>
<dt>&bull;</p>
<dd> Because of the change in default search behavior, the <code>-a/&#8211;all</code> and <code>-u/&#8211;unrestricted</code> options have been removed. In addition, the <code>-k/&#8211;known-types</code> option was added to cause ack to behave with the default search behavior of ack 1.x.</p>
<dt>&bull;</p>
<dd> The <code>-G</code> option has been removed. Two regular expressions on the command line was considered too confusing; to simulate <code>-G</code>&#8216;s functionality, you may use the new <code>-x</code> option to pipe filenames from one invocation of ack into another.</p>
<dt>&bull;</p>
<dd> The <code>&#8211;binary</code> option has been removed.</p>
<dt>&bull;</p>
<dd> The <code>&#8211;skipped</code> option has been removed.</p>
<dt>&bull;</p>
<dd> The <code>&#8211;text</code> option has been removed.</p>
<dt>&bull;</p>
<dd> The <code>&#8211;invert-file-match</code> option has been removed. Instead, you may use <code>-v</code> with <code>-g</code>.</dl>
<h3><font SIZE="-1">CHANGED OPTIONS</font></h3>
<dl>
<dt>&bull;</p>
<dd> The options that modify the regular expression&#8217;s behavior (<code>-i</code>, <code>-w</code>, <code>-Q</code>, and <code>-v</code>) may now be used with <code>-g</code>.</dl>
<h3><font SIZE="-1">ADDED OPTIONS</font></h3>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;files-from</code> was added so that a user may submit a list of filenames as a list of files to search.</p>
<dt>&bull;</p>
<dd> <code>-x</code> was added to tell ack to accept a list of filenames via standard input; this list is the list of filenames that will be used for the search.</p>
<dt>&bull;</p>
<dd> <code>-s</code> was added to tell ack to suppress error messages about non-existent or unreadable files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;ignore-directory</code> and <code>&#8211;noignore-directory</code> were added as aliases for <code>&#8211;ignore-dir</code> and <code>&#8211;noignore-dir</code> respectively.</p>
<dt>&bull;</p>
<dd> <code>&#8211;ignore-file</code> was added so that users may specify patterns of files to ignore (ex. /.*~$/).</p>
<dt>&bull;</p>
<dd> <code>&#8211;dump</code> was added to allow users to easily find out which options are set where.</p>
<dt>&bull;</p>
<dd> <code>&#8211;create-ackrc</code> was added so that users may create custom ackrc files based on the default settings loaded by ack, and so that users may easily view those defaults.</p>
<dt>&bull;</p>
<dd> <code>&#8211;type-del</code> was added to selectively remove file type definitions.</p>
<dt>&bull;</p>
<dd> <code>&#8211;ignore-ack-defaults</code> was added so that users may ignore ack&#8217;s default options in favor of their own.</p>
<dt>&bull;</p>
<dd> <code>&#8211;bar</code> was added so ack users may consult Admiral Ackbar.</dl>
<h2>AUTHOR</h2>
<p> Andy Lester, <tt>&quot;&lt;andy at petdance.com&gt;&quot;</tt></p>
<h2>BUGS</h2>
<p> Please report any bugs or feature requests to the issues list at Github: &lt;<a rel="nofollow" href="https://github.com/petdance/ack2/issues">https://github.com/petdance/ack2/issues</a>&gt;</p>
<h2>ENHANCEMENTS</h2>
<p> All enhancement requests <font SIZE="-1">MUST</font> first be posted to the ack-users mailing list at &lt;<a rel="nofollow" href="http://groups.google.com/group/ack-users">http://groups.google.com/group/ack-users</a>&gt;. I will not consider a request without it first getting seen by other ack users. This includes requests for new filetypes. </p>
<p> There is a list of enhancements I want to make to <i>ack</i> in the ack issues list at Github: &lt;<a rel="nofollow" href="https://github.com/petdance/ack2/issues">https://github.com/petdance/ack2/issues</a>&gt; </p>
<p> Patches are always welcome, but patches with tests get the most attention.</p>
<h2>SUPPORT</h2>
<p> Support for and information about <i>ack</i> can be found at:</p>
<dl>
<dt>&bull;</p>
<dd> The ack homepage </p>
<p> &lt;<a rel="nofollow" href="http://beyondgrep.com/">http://beyondgrep.com/</a>&gt;</p>
<dt>&bull;</p>
<dd> The ack-users mailing list </p>
<p> &lt;<a rel="nofollow" href="http://groups.google.com/group/ack-users">http://groups.google.com/group/ack-users</a>&gt;</p>
<dt>&bull;</p>
<dd> The ack issues list at Github </p>
<p> &lt;<a rel="nofollow" href="https://github.com/petdance/ack2/issues">https://github.com/petdance/ack2/issues</a>&gt;</p>
<dt>&bull;</p>
<dd> AnnoCPAN: Annotated <font SIZE="-1">CPAN</font> documentation </p>
<p> &lt;<a rel="nofollow" href="http://annocpan.org/dist/ack">http://annocpan.org/dist/ack</a>&gt;</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CPAN</font> Ratings </p>
<p> &lt;<a rel="nofollow" href="http://cpanratings.perl.org/d/ack">http://cpanratings.perl.org/d/ack</a>&gt;</p>
<dt>&bull;</p>
<dd> Search <font SIZE="-1">CPAN</font> </p>
<p> &lt;<a rel="nofollow" href="http://search.cpan.org/dist/ack">http://search.cpan.org/dist/ack</a>&gt;</p>
<dt>&bull;</p>
<dd> Git source repository </p>
<p> &lt;<a rel="nofollow" href="https://github.com/petdance/ack2">https://github.com/petdance/ack2</a>&gt;</dl>
<h2>ACKNOWLEDGEMENTS</h2>
<p> How appropriate to have <i>ack</i>nowledgements! </p>
<p> Thanks to everyone who has contributed to ack in any way, including Fraser Tweedale, Raal Gundan, Steffen Jaeckel, Stephan Hohe, Michael Beijen, Alexandr Ciornii, Christian Walde, Charles Lee, Joe McMahon, John Warwick, David Steinbrunner, Kara Martens, Volodymyr Medvid, Ron Savage, Konrad Borowski, Dale Sedivic, Michael McClimon, Andrew Black, Ralph Bodenner, Shaun Patterson, Ryan Olson, Shlomi Fish, Karen Etheridge, Olivier Mengue, Matthew Wild, Scott Kyle, Nick Hooey, Bo Borgerson, Mark Szymanski, Marq Schneider, Packy Anderson, <font SIZE="-1">JR</font> Boyens, Dan Sully, Ryan Niebur, Kent Fredric, Mike Morearty, Ingmar Vanhassel, Eric Van Dewoestine, Sitaram Chamarty, Adam James, Richard Carlsson, Pedro Melo, <font SIZE="-1">AJ</font> Schuster, Phil Jackson, Michael Schwern, Jan Dubois, Christopher J. Madsen, Matthew Wickline, David Dyck, Jason Porritt, Jjgod Jiang, Thomas Klausner, Uri Guttman, Peter Lewis, Kevin Riggle, Ori Avtalion, Torsten Blix, Nigel Metheringham, Gabor Szabo, Tod Hagan, Michael Hendricks, AEvar Arnfjo.rd<i>&#8211;</i> Bjarmason, Piers Cawley, Stephen Steneker, Elias Lutfallah, Mark Leighton Fisher, Matt Diephouse, Christian Jaeger, Bill Sully, Bill Ricker, David Golden, Nilson Santos F. Jr, Elliot Shank, Merijn Broeren, Uwe Voelker, Rick Scott, Ask Bjorn Hansen, Jerry Gay, Will Coleda, Mike O&#8217;Regan, Slaven ReziX, Mark Stosberg, David Alan Pisoni, Adriano Ferreira, James Keenan, Leland Johnson, Ricardo Signes, Pete Krawczyk and Rob Hoelz.</p>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p> Copyright 2005-2013 Andy Lester. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the Artistic License v2.0. </p>
<p> See <a rel="nofollow" href="http://www.perlfoundation.org/artistic_license_2_0">http://www.perlfoundation.org/artistic_license_2_0</a> or the <font SIZE="-1">LICENSE</font>.md file that comes with the ack distribution. </p>
<h2>Index</h2>
<dt><a href="#lbAU">TIPS</a></p>
<dd>
<dt><a href="#lbBB">FAQ</a></p>
<dd>
<dt><a href="#lbBL">ACKRC LOCATION SEMANTICS</a></p>
<dd>
<dt><a href="#lbBM">DIFFERENCES BETWEEN ACK 1.X AND ACK 2.X</a></p>
<dd>
<dt><a href="#lbBR">AUTHOR</a></p>
<dd>
<dt><a href="#lbBS">BUGS</a></p>
<dd>
<dt><a href="#lbBT">ENHANCEMENTS</a></p>
<dd>
<dt><a href="#lbBU">SUPPORT</a></p>
<dd>
<dt><a href="#lbBV">ACKNOWLEDGEMENTS</a></p>
<dd>
<dt><a href="#lbBW">COPYRIGHT &amp; LICENSE</a></p>
<dd></dl>
