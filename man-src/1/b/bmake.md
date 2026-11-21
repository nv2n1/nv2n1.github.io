---

title: "bmake(1)"
name: "bmake"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bmake/"
description: "bmake – maintain program dependencies"
---

<p> <code>bmake</code> &#8211; maintain program dependencies</p>
<h2>SYNOPSIS</h2>
<p> [-<code>BeikNnqrstWX</code> ] -words [-<code>D </code><i>variable</i> ] -words [-<code>d </code><i>flags</i> ] -words [-<code>f </code><i>makefile</i> ] -words [-<code>I </code><i>directory</i> ] -words [-<code>J </code><i>private</i> ] -words [-<code>j </code><i>max_jobs</i> ] -words [-<code>m </code><i>directory</i> ] -words [-<code>T </code><i>file</i> ] -words [-<code>V </code><i>variable</i> ] [<i>variable=value</i> ] -words [<i>target &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a program designed to simplify the maintenance of other programs. Its input is a list of specifications as to the files upon which programs and other files depend. If no &#8211;<code>f </code><i>makefile</i> makefile option is given, will try to open `makefile &#8216; then `Makefile &#8216; in order to find the specifications. If the file `.depend &#8216; exists, it is read (see mkdep(1)). </p>
<p> This manual page is intended as a reference document only. For a more thorough description of and makefiles, please refer to <i>&quot;Make &#8211; A Tutorial&quot; .</i> </p>
<p> will prepend the contents of the <i>MAKEFLAGS</i> environment variable to the command line arguments before parsing them. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-B</code></dt>
<dd> Try to be backwards compatible by executing a single shell per command and by executing the commands to make the sources of a dependency line in sequence.</dd>
<dt><code>-D </code><i>variable</i></dt>
<dd> Define <i>variable</i> to be 1, in the global context.</dd>
<dt><code>-d </code><i>[-]flags</i></dt>
<dd> Turn on debugging, and specify which portions of are to print debugging information. Unless the flags are preceded by `-&#8216; they are added to the <i>MAKEFLAGS</i> environment variable and will be processed by any child make processes. By default, debugging information is printed to standard error, but this can be changed using the <i>F</i> debugging flag. The debugging output is always unbuffered; in addition, if debugging is enabled but debugging output is not directed to standard output, then the standard output is line buffered. <i>Flags</i> is one or more of the following:</dd>
<dl>
<dt><i>A</i></dt>
<dd> Print all possible debugging information; equivalent to specifying all of the debugging flags.</dd>
<dt><i>a</i></dt>
<dd> Print debugging information about archive searching and caching.</dd>
<dt><i>C</i></dt>
<dd> Print debugging information about current working directory.</dd>
<dt><i>c</i></dt>
<dd> Print debugging information about conditional evaluation.</dd>
<dt><i>d</i></dt>
<dd> Print debugging information about directory searching and caching.</dd>
<dt><i>e</i></dt>
<dd> Print debugging information about failed commands and targets.</dd>
<dt><i>F </i>[<code>+ </code><i>filename</i> ]</dt>
<dd> Specify where debugging output is written. This must be the last flag, because it consumes the remainder of the argument. If the character immediately after the `F&#8217; flag is `+&#8217; , then the file will be opened in append mode; otherwise the file will be overwritten. If the file name is `stdout&#8217; or `stderr&#8217; then debugging output will be written to the standard output or standard error output file descriptors respectively (and the `+&#8217; option has no effect). Otherwise, the output will be written to the named file. If the file name ends `.%d&#8217; then the `%d&#8217; is replaced by the pid.</dd>
<dt><i>f</i></dt>
<dd> Print debugging information about loop evaluation.</dd>
<dt><i>g1</i></dt>
<dd> Print the input graph before making anything.</dd>
<dt><i>g2</i></dt>
<dd> Print the input graph after making everything, or before exiting on error.</dd>
<dt><i>g3</i></dt>
<dd> Print the input graph before exiting on error.</dd>
<dt><i>j</i></dt>
<dd> Print debugging information about running multiple shells.</dd>
<dt><i>l</i></dt>
<dd> Print commands in Makefiles regardless of whether or not they are prefixed by `@&#8217; or other &quot;quiet&quot; flags. Also known as &quot;loud&quot; behavior.</dd>
<dt><i>m</i></dt>
<dd> Print debugging information about making targets, including modification dates.</dd>
<dt><i>n</i></dt>
<dd> Don&#8217;t delete the temporary command scripts created in /tmp when running commands. These are created via <a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3) and have names of the form /tmp/makeXXXXX <i>NOTE</i> This can create many file in /tmp so use with care.</dd>
<dt><i>p</i></dt>
<dd> Print debugging information about makefile parsing.</dd>
<dt><i>s</i></dt>
<dd> Print debugging information about suffix-transformation rules.</dd>
<dt><i>t</i></dt>
<dd> Print debugging information about target list maintenance.</dd>
<dt><i>v</i></dt>
<dd> Print debugging information about variable assignment.</dd>
<dt><i>x</i></dt>
<dd> Run shell commands with &#8211;<code>x</code> so the actual commands are printed as they are executed.</dd></dl>
<dt><code>-e</code></dt>
<dd> Specify that environment variables override macro assignments within makefiles.</dd>
<dt><code>-f </code><i>makefile</i></dt>
<dd> Specify a makefile to read instead of the default `makefile &#8216; If <i>makefile</i> is `- &#8216; standard input is read. Multiple makefiles may be specified, and are read in the order specified.</dd>
<dt><code>-I </code><i>directory</i></dt>
<dd> Specify a directory in which to search for makefiles and included makefiles. The system makefile directory (or directories, see the &#8211;<code>m</code> option) is automatically included as part of this list.</dd>
<dt><code>-i</code></dt>
<dd> Ignore non-zero exit of shell commands in the makefile. Equivalent to specifying `- &#8216; before each command line in the makefile.</dd>
<dt><code>-J </code><i>private</i></dt>
<dd> This option should <i>not</i> be specified by the user. </dd>
<p> When the <i>j</i> option is in use in a recursive build, this option is passed by a make to child makes to allow all the make processes in the build to cooperate to avoid overloading the system.</p>
<dt><code>-j </code><i>max_jobs</i></dt>
<dd> Specify the maximum number of jobs that may have running at any one time. Turns compatibility mode off, unless the <i>B</i> flag is also specified. When compatibility mode is off, all commands associated with a target are executed in a single shell invocation as opposed to the traditional one shell invocation per line. This can break traditional scripts which change directories on each command invocation and then expect to start with a fresh environment on the next line. It is more efficient to correct the scripts rather than turn backwards compatibility on.</dd>
<dt><code>-k</code></dt>
<dd> Continue processing after errors are encountered, but only on those targets that do not depend on the target whose creation caused the error.</dd>
<dt><code>-m </code><i>directory</i></dt>
<dd> Specify a directory in which to search for sys.mk and makefiles included via the Ao Ar file Ac Ns -style include statement. The &#8211;<code>m</code> option can be used multiple times to form a search path. This path will override the default system include path: /usr/share/mk. Furthermore the system include path will be appended to the search path used for Qo Ar file Qc Ns -style include statements (see the &#8211;<code>I</code> option). </dd>
<p> If a file or directory name in the &#8211;<code>m</code> argument (or the <code>MAKESYSPATH</code> environment variable) starts with the string Qq &#8230;/ then will search for the specified file or directory named in the remaining part of the argument string. The search starts with the current directory of the Makefile and then works upward towards the root of the filesystem. If the search is successful, then the resulting directory replaces the Qq &#8230;/ specification in the &#8211;<code>m</code> argument. If used, this feature allows to easily search in the current source tree for customized sys.mk files (e.g., by using Qq &#8230;/mk/sys.mk as an argument).</p>
<dt><code>-n</code></dt>
<dd> Display the commands that would have been executed, but do not actually execute them unless the target depends on the .MAKE special source (see below).</dd>
<dt><code>-N</code></dt>
<dd> Display the commands which would have been executed, but do not actually execute any of them; useful for debugging top-level makefiles without descending into subdirectories.</dd>
<dt><code>-q</code></dt>
<dd> Do not execute any commands, but exit 0 if the specified targets are up-to-date and 1, otherwise.</dd>
<dt><code>-r</code></dt>
<dd> Do not use the built-in rules specified in the system makefile.</dd>
<dt><code>-s</code></dt>
<dd> Do not echo any commands as they are executed. Equivalent to specifying `<code>@</code> &#8216; before each command line in the makefile.</dd>
<dt><code>-T </code><i>tracefile</i></dt>
<dd> When used with the &#8211;<code>j</code> flag, append a trace record to <i>tracefile</i> for each job started and completed.</dd>
<dt><code>-t</code></dt>
<dd> Rather than re-building a target as specified in the makefile, create it or update its modification time to make it appear up-to-date.</dd>
<dt><code>-V </code><i>variable</i></dt>
<dd> Print <code>&#8216;s</code> idea of the value of <i>variable</i> in the global context. Do not build any targets. Multiple instances of this option may be specified; the variables will be printed one per line, with a blank line for each null or undefined variable. If <i>variable</i> contains a `$&#8217; then the value will be expanded before printing.</dd>
<dt><code>-W</code></dt>
<dd> Treat any warnings during makefile parsing as errors.</dd>
<dt><code>-X</code></dt>
<dd> Don&#8217;t export variables passed on the command line to the environment individually. Variables passed on the command line are still exported via the <i>MAKEFLAGS</i> environment variable. This option may be useful on systems which have a small limit on the size of command arguments.</dd>
<dt><i>variable=value</i></dt>
<dd> Set the value of the variable <i>variable</i> to <i>value</i> Normally, all values passed on the command line are also exported to sub-makes in the environment. The &#8211;<code>X</code> flag disables this behavior. Variable assignments should follow options for POSIX compatibility but no ordering is enforced.</dd></dl>
<p> There are seven different types of lines in a makefile: file dependency specifications, shell commands, variable assignments, include statements, conditional directives, for loops, and comments. </p>
<p> In general, lines may be continued from one line to the next by ending them with a backslash (`\&#8217; ) The trailing newline character and initial whitespace on the following line are compressed into a single space.</p>
<h2>FILE DEPENDENCY SPECIFICATIONS</h2>
<p> Dependency lines consist of one or more targets, an operator, and zero or more sources. This creates a relationship where the targets &#8220;depend&#8221; on the sources and are usually created from them. The exact relationship between the target and the source is determined by the operator that separates them. The three operators are as follows:</p>
<dl>
<dt><code>:</code></dt>
<dd> A target is considered out-of-date if its modification time is less than those of any of its sources. Sources for a target accumulate over dependency lines when this operator is used. The target is removed if is interrupted.</dd>
<dt><code>!</code></dt>
<dd> Targets are always re-created, but not until all sources have been examined and re-created as necessary. Sources for a target accumulate over dependency lines when this operator is used. The target is removed if is interrupted.</dd>
<dt><code>::</code></dt>
<dd> If no sources are specified, the target is always re-created. Otherwise, a target is considered out-of-date if any of its sources has been modified more recently than the target. Sources for a target do not accumulate over dependency lines when this operator is used. The target will not be removed if is interrupted.</dd></dl>
<p> Targets and sources may contain the shell wildcard values `?&#8217; , `*&#8217; , `[]&#8217; , and `{}&#8217; The values `?&#8217; , `*&#8217; , and `[]&#8217; may only be used as part of the final component of the target or source, and must be used to describe existing files. The value `{}&#8217; need not necessarily be used to describe existing files. Expansion is in directory order, not alphabetically as done in the shell.</p>
<h2>SHELL COMMANDS</h2>
<p> Each target may have associated with it a series of shell commands, normally used to create the target. Each of the commands in this script <i>must</i> be preceded by a tab. While any target may appear on a dependency line, only one of these dependencies may be followed by a creation script, unless the `<code>::</code> &#8216; operator is used. </p>
<p> If the first characters of the command line are any combination of `<code>@</code> &#8216; , `<code>+</code> &#8216; , or `<code>&#8211;</code> &#8216; , the command is treated specially. A `<code>@</code> &#8216; causes the command not to be echoed before it is executed. A `<code>+</code> &#8216; causes the command to be executed even when &#8211;<code>n</code> is given. This is similar to the effect of the .MAKE special source, except that the effect can be limited to a single line of a script. A `<code>&#8211;</code> &#8216; causes any non-zero exit status of the command line to be ignored.</p>
<h2>VARIABLE ASSIGNMENTS</h2>
<p> Variables in make are much like variables in the shell, and, by tradition, consist of all upper-case letters.</p>
<h3>Variable assignment modifiers</h3>
<p> The five operators that can be used to assign values to variables are as follows:</p>
<dl>
<dt><code>=</code></dt>
<dd> Assign the value to the variable. Any previous value is overridden.</dd>
<dt><code>+=</code></dt>
<dd> Append the value to the current value of the variable.</dd>
<dt><code>?=</code></dt>
<dd> Assign the value to the variable if it is not already defined.</dd>
<dt><code>:=</code></dt>
<dd> Assign with expansion, i.e. expand the value before assigning it to the variable. Normally, expansion is not done until the variable is referenced. <i>NOTE</i> References to undefined variables are <i>not</i> expanded. This can cause problems when variable modifiers are used.</dd>
<dt><code>!=</code></dt>
<dd> Expand the value and pass it to the shell for execution and assign the result to the variable. Any newlines in the result are replaced with spaces.</dd></dl>
<p> Any white-space before the assigned <i>value</i> is removed; if the value is being appended, a single space is inserted between the previous contents of the variable and the appended value. </p>
<p> Variables are expanded by surrounding the variable name with either curly braces (`{}&#8217; ) or parentheses (`()&#8217; ) and preceding it with a dollar sign (`$&#8217; ) If the variable name contains only a single letter, the surrounding braces or parentheses are not required. This shorter form is not recommended. </p>
<p> If the variable name contains a dollar, then the name itself is expanded first. This allows almost arbitrary variable names, however names containing dollar, braces, parenthesis, or whitespace are really best avoided! </p>
<p> If the result of expanding a variable contains a dollar sign (`$&#8217; ) the string is expanded again. </p>
<p> Variable substitution occurs at two distinct times, depending on where the variable is being used. Variables in dependency lines are expanded as the line is read. Variables in shell commands are expanded when the shell command is executed.</p>
<h3>Variable classes</h3>
<p> The four different classes of variables (in order of increasing precedence) are:</p>
<dl>
<dt><code>Environment variables</code></dt>
<dd> Variables defined as part of <code>&#8216;s</code> environment.</dd>
<dt><code>Global variables</code></dt>
<dd> Variables defined in the makefile or in included makefiles.</dd>
<dt><code>Command line variables</code></dt>
<dd> Variables defined as part of the command line.</dd>
<dt><code>Local variables</code></dt>
<dd> Variables that are defined specific to a certain target. The seven local variables are as follows:</dd>
<dl>
<dt><i>.ALLSRC</i></dt>
<dd> The list of all sources for this target; also known as `<i>Gt]</i> &#8216;</dd>
<dt><i>.ARCHIVE</i></dt>
<dd> The name of the archive file.</dd>
<dt><i>.IMPSRC</i></dt>
<dd> In suffix-transformation rules, the name/path of the source from which the target is to be transformed (the &#8220;implied&#8221; source); also known as `<i>Lt]</i> &#8216; It is not defined in explicit rules.</dd>
<dt><i>.MEMBER</i></dt>
<dd> The name of the archive member.</dd>
<dt><i>.OODATE</i></dt>
<dd> The list of sources for this target that were deemed out-of-date; also known as `<i>?</i> &#8216;</dd>
<dt><i>.PREFIX</i></dt>
<dd> The file prefix of the file, containing only the file portion, no suffix or preceding directory components; also known as `<i>*</i> &#8216;</dd>
<dt><i>.TARGET</i></dt>
<dd> The name of the target; also known as `<i>@</i> &#8216;</dd></dl>
<p> The shorter forms `<i>@</i> &#8216; , `<i>?</i> &#8216; , `<i>Lt]</i> &#8216; , `<i>Gt]</i> &#8216; , and `<i>*</i> &#8216; are permitted for backward compatibility with historical makefiles and are not recommended. The six variables `<i>@F</i> &#8216; , `<i>@D</i> &#8216; , `<i>Lt]F</i> &#8216; , `<i>Lt]D</i> &#8216; , `<i>*F</i> &#8216; , and `<i>*D</i> &#8216; are permitted for compatibility with AT&amp;T System V makefiles and are not recommended. </p>
<p> Four of the local variables may be used in sources on dependency lines because they expand to the proper value for each target on the line. These variables are `<i>.TARGET</i> &#8216; , `<i>.PREFIX</i> &#8216; , `<i>.ARCHIVE</i> &#8216; , and `<i>.MEMBER</i> &#8216;</dl>
<h3>Additional built-in variables</h3>
<p> In addition, sets or knows about the following variables:</p>
<dl>
<dt><i>$</i></dt>
<dd> A single dollar sign `$&#8217; , i.e. `$$&#8217; expands to a single dollar sign.</dd>
<dt><i>.ALLTARGETS</i></dt>
<dd> The list of all targets encountered in the Makefile. If evaluated during Makefile parsing, lists only those targets encountered thus far.</dd>
<dt><i>.CURDIR</i></dt>
<dd> A path to the directory where was executed. Refer to the description of `<code>PWD</code> &#8216; for more details.</dd>
<dt><code>MAKE</code></dt>
<dd> The name that was executed with (<i>argv[0]</i> ) For compatibility also sets <i>.MAKE</i> with the same value. The preferred variable to use is the environment variable <code>MAKE</code> because it is more compatible with other versions of and cannot be confused with the special target with the same name.</dd>
<dt><i>.MAKE.EXPORTED</i></dt>
<dd> The list of variables exported by <code>.</code></dd>
<dt><i>.MAKE.MAKEFILES</i></dt>
<dd> The list of makefiles read by <code>,</code> which is useful for tracking dependencies. Each makefile is recorded only once, regardless of the number of times read.</dd>
<dt><i>.MAKE.PID</i></dt>
<dd> The process-id of <code>.</code></dd>
<dt><i>.MAKE.PPID</i></dt>
<dd> The parent process-id of <code>.</code></dd>
<dt><i>.MAKE.JOB.PREFIX</i></dt>
<dd> If is run with <i>j</i> then output for each target is prefixed with a token `&#8212;&#8216; target &#8212; the first part of which can be controlled via <i>.MAKE.JOB.PREFIX</i><br />
 For example: <code>.MAKE.JOB.PREFIX=${.newline}&#8212;${.MAKE:T}[${.MAKE.PID}]</code> would produce tokens like `&#8212;make[1234]&#8217; target &#8212; making it easier to track the degree of parallelism being achieved.</dd>
<dt><code>MAKEFLAGS</code></dt>
<dd> The environment variable `<code>MAKEFLAGS</code> &#8216; may contain anything that may be specified on <code>&#8216;s</code> command line. Anything specified on <code>&#8216;s</code> command line is appended to the `<code>MAKEFLAGS</code> &#8216; variable which is then entered into the environment for all programs which executes.</dd>
<dt><i>.MAKEOVERRIDES</i></dt>
<dd> This variable is used to record the names of variables assigned to on the command line, so that they may be exported as part of `<code>MAKEFLAGS</code> &#8216; This behaviour can be disabled by assigning an empty value to `<i>.MAKEOVERRIDES</i> &#8216; within a makefile. Extra variables can be exported from a makefile by appending their names to `<i>.MAKEOVERRIDES</i> &#8216; `<code>MAKEFLAGS</code> &#8216; is re-exported whenever `<i>.MAKEOVERRIDES</i> &#8216; is modified.</dd>
<dt><i>MAKE_PRINT_VAR_ON_ERROR</i></dt>
<dd> When stops due to an error, it prints its name and the value of `<i>.CURDIR</i> &#8216; as well as the value of any variables named in `<i>MAKE_PRINT_VAR_ON_ERROR</i> &#8216;</dd>
<dt><i>.newline</i></dt>
<dd> This variable is simply assigned a newline character as its value. This allows expansions using the <code>:@</code> modifier to put a newline between iterations of the loop rather than a space. For example, the printing of `<i>MAKE_PRINT_VAR_ON_ERROR</i> &#8216; could be done as ${MAKE_PRINT_VAR_ON_ERROR:@v@$v=&#8217;${$v}&#8217;${.newline}@}.</dd>
<dt><i>.OBJDIR</i></dt>
<dd> A path to the directory where the targets are built. Its value is determined by trying to <a href="/docs/linux/man/2-chdir/">chdir</a>(2) to the following directories in order and using the first match: </dd>
<ol>
<li> <code>${MAKEOBJDIRPREFIX}${.CURDIR}</code>
<p> (Only if `<code>MAKEOBJDIRPREFIX</code> &#8216; is set in the environment or on the command line.) </p>
<li> <code>${MAKEOBJDIR}</code>
<p> (Only if `<code>MAKEOBJDIR</code> &#8216; is set in the environment or on the command line.) </p>
<li> <code>${.CURDIR} /obj. ${MACHINE}</code>
<li> <code>${.CURDIR} /obj </code>
<li> /usr/obj/ <code>${.CURDIR}</code>
<li> <code>${.CURDIR}</code> </ol>
<p> Variable expansion is performed on the value before it&#8217;s used, so expressions such as </p>
<blockquote><p><tt>${.CURDIR:C,^/usr/src,/var/obj,}</tt></p></blockquote>
<p> may be used. </p>
<p> `<i>.OBJDIR</i> &#8216; may be modified in the makefile as a global variable. In all cases, will <a href="/docs/linux/man/2-chdir/">chdir</a>(2) to `<i>.OBJDIR</i> &#8216; and set `<code>PWD</code> &#8216; to that directory before executing any targets.</p>
<dt><i>.PARSEDIR</i></dt>
<dd> A path to the directory of the current `Makefile &#8216; being parsed.</dd>
<dt><i>.PARSEFILE</i></dt>
<dd> The basename of the current `Makefile &#8216; being parsed. This variable and `<i>.PARSEDIR</i> &#8216; are both set only while the `Makefiles &#8216; are being parsed.</dd>
<dt><i>.PATH</i></dt>
<dd> A variable that represents the list of directories that will search for files. The search list should be updated using the target `<i>.PATH</i> &#8216; rather than the variable.</dd>
<dt><code>PWD</code></dt>
<dd> Alternate path to the current directory. normally sets `<i>.CURDIR</i> &#8216; to the canonical path given by <a href="/docs/linux/man/3-getcwd/">getcwd</a>(3). However, if the environment variable `<code>PWD</code> &#8216; is set and gives a path to the current directory, then sets `<i>.CURDIR</i> &#8216; to the value of `<code>PWD</code> &#8216; instead. This behaviour is disabled if `<code>MAKEOBJDIRPREFIX</code> &#8216; is set or `<code>MAKEOBJDIR</code> &#8216; contains a variable transform. `<code>PWD</code> &#8216; is set to the value of `<i>.OBJDIR</i> &#8216; for all programs which executes.</dd>
<dt><code>VPATH</code></dt>
<dd> Colon-separated (&#8220;:&#8221; ) lists of directories that will search for files. The variable is supported for compatibility with old make programs only, use `<i>.PATH</i> &#8216; instead.</dd></dl>
<h3>Variable modifiers</h3>
<p> Variable expansion may be modified to select or modify each word of the variable (where a &#8220;word&#8221; is white-space delimited sequence of characters). The general format of a variable expansion is as follows: </p>
<blockquote><p><tt>${variable[:modifier[:...]]}</tt></p></blockquote>
<p> Each modifier begins with a colon, which may be escaped with a backslash (`\&#8217; ) </p>
<p> A set of modifiers can be specified via a variable, as follows: </p>
<blockquote><p><tt>modifier_variable=modifier[:...]</tt></p></blockquote>
<blockquote><p><tt>${variable:${modifier_variable}[:...]}</tt></p></blockquote>
<p> In this case the first modifier in the modifier_variable does not start with a colon, since that must appear in the referencing variable. If any of the modifiers in the modifier_variable contain a dollar sign (`$&#8217; ) these must be doubled to avoid early expansion. </p>
<p> The supported modifiers are:</p>
<dl>
<dt><code>:E</code></dt>
<dd> Replaces each word in the variable with its suffix.</dd>
<dt><code>:H</code></dt>
<dd> Replaces each word in the variable with everything but the last component.</dd>
<dt><code>:M </code><i>pattern</i></dt>
<dd> Select only those words that match <i>pattern</i> The standard shell wildcard characters ( `*&#8217; `?&#8217; , and `[)] &#8216; may be used. The wildcard characters may be escaped with a backslash (`\&#8217; )</dd>
<dt><code>:N </code><i>pattern</i></dt>
<dd> This is identical to `<code>:M</code> &#8216; , but selects all words which do not match <i>pattern</i></dd>
<dt><code>:O</code></dt>
<dd> Order every word in variable alphabetically. To sort words in reverse order use the `<code>:O:[-1..1]</code> &#8216; combination of modifiers.</dd>
<dt><code>:Ox </code>Randomize words in variable.</dt>
<dd> The results will be different each time you are referring to the modified variable; use the assignment with expansion (`<code>:=</code> &#8216; ) to prevent such behaviour. For example, </dd>
<blockquote>
<pre><code>
LIST = uno due tre quattro
    RANDOM_LIST = ${LIST : Ox} STATIC_RANDOM_LIST : = ${LIST : Ox} all : @echo "${RANDOM_LIST}"
                                                                         @echo "${RANDOM_LIST}"
                                                                         @echo "${STATIC_RANDOM_LIST}"
                                                                         @echo "${STATIC_RANDOM_LIST}"
</code></pre>
</blockquote>
<p> may produce output similar to: </p>
<blockquote>
<pre>
quattro due tre uno
tre due quattro uno
due uno quattro tre
due uno quattro tre
</pre>
</blockquote>
<dt><code>:Q</code></dt>
<dd> Quotes every shell meta-character in the variable, so that it can be passed safely through recursive invocations of <code>.</code></dd>
<dt><code>:R</code></dt>
<dd> Replaces each word in the variable with everything but its suffix.</dd>
<dt><code>:tl</code></dt>
<dd> Converts variable to lower-case letters.</dd>
<dt><code>:ts </code><i>c</i></dt>
<dd> Words in the variable are normally separated by a space on expansion. This modifier sets the separator to the character <i>c</i> If <i>c</i> is omitted, then no separator is used.</dd>
<dt><code>:tu</code></dt>
<dd> Converts variable to upper-case letters.</dd>
<dt><code>:tW</code></dt>
<dd> Causes the value to be treated as a single word (possibly containing embedded white space). See also `<code>:[*]</code> &#8216;</dd>
<dt><code>:tw</code></dt>
<dd> Causes the value to be treated as a sequence of words delimited by white space. See also `<code>:[@]</code> &#8216;</dd>
<dt><code>:S / </code><i>old_string </i> <code>/ </code><i>new_string</i> <code>/ </code>[<code>1gW</code> ]</dt>
<dd>
</dd><dd>Modify the first occurrence of <i>old_string</i> in the variable&#8217;s value, replacing it with <i>new_string</i> If a `g&#8217; is appended to the last slash of the pattern, all occurrences in each word are replaced. If a `1&#8242; is appended to the last slash of the pattern, only the first word is affected. If a `W&#8217; is appended to the last slash of the pattern, then the value is treated as a single word (possibly containing embedded white space). If <i>old_string</i> begins with a caret (`^&#8217; ) <i>old_string</i> is anchored at the beginning of each word. If <i>old_string</i> ends with a dollar sign (`$&#8217; ) it is anchored at the end of each word. Inside <i>new_string</i> an ampersand (`Am]&#8217; ) is replaced by <i>old_string</i> (without any `^&#8217; or `$&#8217; ) . Any character may be used as a delimiter for the parts of the modifier string. The anchoring, ampersand and delimiter characters may be escaped with a backslash (`\&#8217; ) </dd>
<p> Variable expansion occurs in the normal fashion inside both <i>old_string</i> and <i>new_string</i> with the single exception that a backslash is used to prevent the expansion of a dollar sign (`$&#8217; ) not a preceding dollar sign as is usual.</p>
<dt><code>:C / </code><i>pattern </i> <code>/ </code><i>replacement</i> <code>/ </code>[<code>1gW</code> ]</dt>
<dd>
</dd><dd>The <code>:C</code> modifier is just like the <code>:S</code> modifier except that the old and new strings, instead of being simple strings, are a regular expression (see <a href="/docs/linux/man/3-regex/">regex</a>(3)) string <i>pattern</i> and an <a href="/docs/linux/man/1-ed/">ed</a>(1)Ns-style string <i>replacement</i> Normally, the first occurrence of the pattern <i>pattern</i> in each word of the value is substituted with <i>replacement</i> The `1&#8242; modifier causes the substitution to apply to at most one word; the `g&#8217; modifier causes the substitution to apply to as many instances of the search pattern <i>pattern</i> as occur in the word or words it is found in; the `W&#8217; modifier causes the value to be treated as a single word (possibly containing embedded white space). Note that `1&#8242; and `g&#8217; are orthogonal; the former specifies whether multiple words are potentially affected, the latter whether multiple substitutions can potentially occur within each affected word.</dd>
<dt><code>:T</code></dt>
<dd> Replaces each word in the variable with its last component.</dd>
<dt><code>:u</code></dt>
<dd> Remove adjacent duplicate words (like <a href="/docs/linux/man/1-uniq/">uniq</a>(1)).</dd>
<dt><code>:? </code><i>true_string </i><code>: </code><i>false_string</i></dt>
<dd> If the variable name (not its value), when parsed as a .if conditional expression, evaluates to true, return as its value the <i>true_string</i> otherwise return the <i>false_string</i> Since the variable name is used as the expression, :? must be the first modifier after the variable name itself &#8211; which will, of course, usually contain variable expansions. If the expression is a single token, it will likely be treated as a check for the name being defined.</dd>
<dt><i>:old_string=new_string</i></dt>
<dd> This is the AT&amp;T System V style variable substitution. It must be the last modifier specified. If <i>old_string</i> or <i>new_string</i> do not contain the pattern matching character <i>%</i> then it is assumed that they are anchored at the end of each word, so only suffixes or entire words may be replaced. Otherwise <i>%</i> is the substring of <i>old_string</i> to be replaced in <i>new_string</i> </dd>
<p> Variable expansion occurs in the normal fashion inside both <i>old_string</i> and <i>new_string</i> with the single exception that a backslash is used to prevent the expansion of a dollar sign (`$&#8217; ) not a preceding dollar sign as is usual.</p>
<dt><code>:@ </code><i>temp </i><code>@ </code> <i>string </i><code>@</code></dt>
<dd>
</dd><dd>This is the loop expansion mechanism from the OSF Development Environment (ODE) make. Unlike <code>.for</code> loops expansion occurs at the time of reference. Assign <i>temp</i> to each word in the variable and evaluate <i>string</i> The ODE convention is that <i>temp</i> should start and end with a period. For example. </dd>
<blockquote><p><tt>${LINKS:@.LINK.@${LN} ${TARGET} ${.LINK.}@}</tt></p></blockquote>
<dt><code>:U </code><i>newval</i></dt>
<dd> If the variable is undefined <i>newval</i> is the value. If the variable is defined, the existing value is returned. This is another ODE make feature. It is handy for setting per-target CFLAGS for instance: </dd>
<blockquote><p><tt>${_${.TARGET:T}_CFLAGS:U${DEF_CFLAGS}}</tt></p></blockquote>
<p> If a value is only required if the variable is undefined, use: </p>
<blockquote><p><tt>${VAR:D:Unewval}</tt></p></blockquote>
<dt><code>:D </code><i>newval</i></dt>
<dd> If the variable is defined <i>newval</i> is the value.</dd>
<dt><code>:L</code></dt>
<dd> The name of the variable is the value.</dd>
<dt><code>:P</code></dt>
<dd> The path of the node which has the same name as the variable is the value. If no such node exists or its path is null, then the name of the variable is used.</dd>
<dt><code>:! </code><i>cmd </i><code>!</code></dt>
<dd> The output of running <i>cmd</i> is the value.</dd>
<dt><code>:sh</code></dt>
<dd> If the variable is non-empty it is run as a command and the output becomes the new value.</dd>
<dt><code>::= </code><i>str</i></dt>
<dd> The variable is assigned the value <i>str</i> after substitution. This modifier and its variations are useful in obscure situations such as wanting to set a variable when shell commands are being parsed. These assignment modifiers always expand to nothing, so if appearing in a rule line by themselves should be preceded with something to keep happy. </dd>
<p> The `<code>::</code> &#8216; helps avoid false matches with the AT&amp;T System V style <code>:=</code> modifier and since substitution always occurs the <code>::=</code> form is vaguely appropriate.</p>
<dt><code>::?= </code><i>str</i></dt>
<dd> As for <code>::=</code> but only if the variable does not already have a value.</dd>
<dt><code>::+= </code><i>str</i></dt>
<dd> Append <i>str</i> to the variable.</dd>
<dt><code>::!= </code><i>cmd</i></dt>
<dd> Assign the output of <i>cmd</i> to the variable.</dd>
<dt><code>:[ </code><i>range </i><code>]</code></dt>
<dd> Selects one or more words from the value, or performs other operations related to the way in which the value is divided into words. </dd>
<p> Ordinarily, a value is treated as a sequence of words delimited by white space. Some modifiers suppress this behaviour, causing a value to be treated as a single word (possibly containing embedded white space). An empty value, or a value that consists entirely of white-space, is treated as a single word. For the purposes of the `<code>:[]</code> &#8216; modifier, the words are indexed both forwards using positive integers (where index 1 represents the first word), and backwards using negative integers (where index -1 represents the last word). </p>
<p> The <i>range</i> is subjected to variable expansion, and the expanded result is then interpreted as follows:</p>
<dl>
<dt><i>index</i></dt>
<dd> Selects a single word from the value.</dd>
<dt><i>start </i><code>.. </code><i>end</i></dt>
<dd> Selects all words from <i>start</i> to <i>end</i> inclusive. For example, `<code>:[2..-1]</code> &#8216; selects all words from the second word to the last word. If <i>start</i> is greater than <i>end</i> then the words are output in reverse order. For example, `<code>:[-1..1]</code> &#8216; selects all the words from last to first.</dd>
<dt><code>*</code></dt>
<dd> Causes subsequent modifiers to treat the value as a single word (possibly containing embedded white space). Analogous to the effect of &quot;$*&quot; in Bourne shell.</dd>
<dt><code>0</code></dt>
<dd> Means the same as `<code>:[*]</code> &#8216;</dd>
<dt><code>@</code></dt>
<dd> Causes subsequent modifiers to treat the value as a sequence of words delimited by white space. Analogous to the effect of &quot;$@&quot; in Bourne shell.</dd>
<dt><code>#</code></dt>
<dd> Returns the number of words in the value.</dd></dl>
</dl>
<h2>INCLUDE STATEMENTS, CONDITIONALS AND FOR LOOPS</h2>
<p> Makefile inclusion, conditional structures and for loops reminiscent of the C programming language are provided in <code>.</code> All such structures are identified by a line beginning with a single dot (`.&#8217; ) character. Files are included with either <code>.include Aq </code><i>file</i> or <code>.include </code><i>file </i> Variables between the angle brackets or double quotes are expanded to form the file name. If angle brackets are used, the included makefile is expected to be in the system makefile directory. If double quotes are used, the including makefile&#8217;s directory and any directories specified using the &#8211;<code>I</code> option are searched before the system makefile directory. For compatibility with other versions of `include&#8217; file &#8230; is also accepted. If the include statement is written as <code>.-include</code> or as <code>.sinclude</code> then errors locating and/or opening include files are ignored. </p>
<p> Conditional expressions are also preceded by a single dot as the first character of a line. The possible conditionals are as follows:</p>
<dl>
<dt><code>.export </code><i>variable</i></dt>
<dd> Export the specified global variable. If no variable is provided, all globals are exported except for internal variables (those that start with `.&#8217; ). This is not affected by the &#8211;<code>X</code> flag, so should be used with caution. Appending a variable name to <i>.MAKE.EXPORTED</i> is equivalent to exporting a variable.</dd>
<dt><code>.undef </code><i>variable</i></dt>
<dd> Un-define the specified global variable. Only global variables may be un-defined.</dd>
<dt> <code>.if</code> [! <i>expression</i> ] [<i>operator expression &#8230;</i> ]</dt>
<dd>
</dd><dd>Test the value of an expression.</dd>
<dt> <code>.ifdef</code> [! <i>variable</i> ] [<i>operator variable &#8230;</i> ]</dt>
<dd>
</dd><dd>Test the value of a variable.</dd>
<dt> <code>.ifndef</code> [! <i>variable</i> ] [<i>operator variable &#8230;</i> ]</dt>
<dd>
</dd><dd>Test the value of a variable.</dd>
<dt> <code>.ifmake</code> [! <i>target</i> ] [<i>operator target &#8230;</i> ]</dt>
<dd>
</dd><dd>Test the target being built.</dd>
<dt> <code>.ifnmake</code> [! <i>target</i> ] [<i>operator target &#8230;</i> ]</dt>
<dd>
</dd><dd>Test the target being built.</dd>
<dt><code>.else</code></dt>
<dd> Reverse the sense of the last conditional.</dd>
<dt> <code>.elif</code> [! <i>expression</i> ] [<i>operator expression &#8230;</i> ]</dt>
<dd>
</dd><dd>A combination of `<code>.else</code> &#8216; followed by `<code>.if</code> &#8216;</dd>
<dt> <code>.elifdef</code> [! <i>variable</i> ] [<i>operator variable &#8230;</i> ]</dt>
<dd>
</dd><dd>A combination of `<code>.else</code> &#8216; followed by `<code>.ifdef</code> &#8216;</dd>
<dt> <code>.elifndef</code> [! <i>variable</i> ] [<i>operator variable &#8230;</i> ]</dt>
<dd>
</dd><dd>A combination of `<code>.else</code> &#8216; followed by `<code>.ifndef</code> &#8216;</dd>
<dt> <code>.elifmake</code> [! <i>target</i> ] [<i>operator target &#8230;</i> ]</dt>
<dd>
</dd><dd>A combination of `<code>.else</code> &#8216; followed by `<code>.ifmake</code> &#8216;</dd>
<dt> <code>.elifnmake</code> [! <i>target</i> ] [<i>operator target &#8230;</i> ]</dt>
<dd>
</dd><dd>A combination of `<code>.else</code> &#8216; followed by `<code>.ifnmake</code> &#8216;</dd>
<dt><code>.endif</code></dt>
<dd> End the body of the conditional.</dd></dl>
<p> The <i>operator</i> may be any one of the following:</p>
<dl>
<dt><code>||</code></dt>
<dd> Logical OR.</dd>
<dt><code>Am]Am]</code></dt>
<dd> Logical <code>AND</code> of higher precedence than &#8220;||&#8221;</dd></dl>
<p> As in C, will only evaluate a conditional as far as is necessary to determine its value. Parentheses may be used to change the order of evaluation. The boolean operator `<code>!</code> &#8216; may be used to logically negate an entire conditional. It is of higher precedence than `<code>Am]Am]</code> &#8216; </p>
<p> The value of <i>expression</i> may be any of the following:</p>
<dl>
<dt><code>defined</code></dt>
<dd> Takes a variable name as an argument and evaluates to true if the variable has been defined.</dd>
<dt><code>make</code></dt>
<dd> Takes a target name as an argument and evaluates to true if the target was specified as part of <code>&#8216;s</code> command line or was declared the default target (either implicitly or explicitly, see <i>.MAIN</i> before the line containing the conditional.</dd>
<dt><code>empty</code></dt>
<dd> Takes a variable, with possible modifiers, and evaluates to true if the expansion of the variable would result in an empty string.</dd>
<dt><code>exists</code></dt>
<dd> Takes a file name as an argument and evaluates to true if the file exists. The file is searched for on the system search path (see <i>.PATH )</i></dd>
<dt><code>target</code></dt>
<dd> Takes a target name as an argument and evaluates to true if the target has been defined.</dd>
<dt><code>commands</code></dt>
<dd> Takes a target name as an argument and evaluates to true if the target has been defined and has commands associated with it.</dd></dl>
<p> <i>Expression</i> may also be an arithmetic or string comparison. Variable expansion is performed on both sides of the comparison, after which the integral values are compared. A value is interpreted as hexadecimal if it is preceded by 0x, otherwise it is decimal; octal numbers are not supported. The standard C relational operators are all supported. If after variable expansion, either the left or right hand side of a `<code>==</code> &#8216; or `<code>!=</code> &#8216; operator is not an integral value, then string comparison is performed between the expanded variables. If no relational operator is given, it is assumed that the expanded variable is being compared against 0 or an empty string in the case of a string comparison. </p>
<p> When is evaluating one of these conditional expressions, and it encounters a (white-space separated) word it doesn&#8217;t recognize, either the &#8220;make&#8221; or &#8220;defined&#8221; expression is applied to it, depending on the form of the conditional. If the form is `<code>.ifdef</code> &#8216; , `<code>.ifndef</code> &#8216; , or `<code>.if</code> &#8216; the &#8220;defined&#8221; expression is applied. Similarly, if the form is `<code>.ifmake</code> &#8216; or `<code>.ifnmake</code> &#8216; , the &#8220;make&#8221; expression is applied. </p>
<p> If the conditional evaluates to true the parsing of the makefile continues as before. If it evaluates to false, the following lines are skipped. In both cases this continues until a `<code>.else</code> &#8216; or `<code>.endif</code> &#8216; is found. </p>
<p> For loops are typically used to apply a set of rules to a list of files. The syntax of a for loop is: </p>
<dl>
<dt> <code>.for</code> <i>variable</i> [<i>variable &#8230;</i> ] <code>in</code> <i>expression</i></dt>
<dd>
</dd><dt><code>Aq </code>make-rules</dt>
<dd>
</dd><dt><code>.endfor</code></dt>
<dd></dd></dl>
<dd>After the for <code>expression</code> is evaluated, it is split into words. On each iteration of the loop, one word is taken and assigned to each <code>variable</code> in order, and these <code>variables</code> are substituted into the <code>make-rules</code> inside the body of the for loop. The number of words must come out even; that is, if there are three iteration variables, the number of words provided must be a multiple of three.</dd>
<h2>COMMENTS</h2>
<p> Comments begin with a hash (`#&#8217; ) character, anywhere but in a shell command line, and continue to the end of an unescaped new line.</p>
<h2>SPECIAL SOURCES (ATTRIBUTES)</h2>
<dl>
<dt><code>.EXEC</code></dt>
<dd> Target is never out of date, but always execute commands anyway.</dd>
<dt><code>.IGNORE</code></dt>
<dd> Ignore any errors from the commands associated with this target, exactly as if they all were preceded by a dash (`-&#8216; )</dd>
<dt><code>.MADE</code></dt>
<dd> Mark all sources of this target as being up-to-date.</dd>
<dt><code>.MAKE</code></dt>
<dd> Execute the commands associated with this target even if the &#8211;<code>n</code> or &#8211;<code>t</code> options were specified. Normally used to mark recursive <code>&#8216;s</code></dd>
<dt><code>.NOPATH</code></dt>
<dd> Do not search for the target in the directories specified by <code>.PATH</code></dd>
<dt><code>.NOTMAIN</code></dt>
<dd> Normally selects the first target it encounters as the default target to be built if no target was specified. This source prevents this target from being selected.</dd>
<dt><code>.OPTIONAL</code></dt>
<dd> If a target is marked with this attribute and can&#8217;t figure out how to create it, it will ignore this fact and assume the file isn&#8217;t needed or already exists.</dd>
<dt><code>.PHONY</code></dt>
<dd> The target does not correspond to an actual file; it is always considered to be out of date, and will not be created with the &#8211;<code>t</code> option.</dd>
<dt><code>.PRECIOUS</code></dt>
<dd> When is interrupted, it normally removes any partially made targets. This source prevents the target from being removed.</dd>
<dt><code>.RECURSIVE</code></dt>
<dd> Synonym for <code>.MAKE</code></dd>
<dt><code>.SILENT</code></dt>
<dd> Do not echo any of the commands associated with this target, exactly as if they all were preceded by an at sign (`@&#8217; )</dd>
<dt><code>.USE</code></dt>
<dd> Turn the target into <code>&#8216;s</code> version of a macro. When the target is used as a source for another target, the other target acquires the commands, sources, and attributes (except for <code>.USE</code> of the source. If the target already has commands, the <code>.USE</code> target&#8217;s commands are appended to them.</dd>
<dt><code>.USEBEFORE</code></dt>
<dd> Exactly like <code>.USE</code> but prepend the <code>.USEBEFORE</code> target commands to the target.</dd>
<dt><code>.WAIT</code></dt>
<dd> If <code>.WAIT</code> appears in a dependency line, the sources that precede it are made before the sources that succeed it in the line. Since the dependents of files are not made until the file itself could be made, this also stops the dependents being built unless they are needed for another branch of the dependency tree. So given: </dd>
<pre>
x: a .WAIT b
        echo x
a:
        echo a
b: b1
        echo b
b1:
        echo b1
</pre>
<p> the output is always `a&#8217; , `b1&#8242; , `b&#8217; , `x&#8217;<br />
 The ordering imposed by <code>.WAIT</code> is only relevant for parallel makes.</dl>
<h2>SPECIAL TARGETS</h2>
<p> Special targets may not be included with other targets, i.e. they must be the only target specified.</p>
<dl>
<dt><code>.BEGIN</code></dt>
<dd> Any command lines attached to this target are executed before anything else is done.</dd>
<dt><code>.DEFAULT</code></dt>
<dd> This is sort of a <code>.USE</code> rule for any target (that was used only as a source) that can&#8217;t figure out any other way to create. Only the shell script is used. The <code>.IMPSRC</code> variable of a target that inherits <code>.DEFAULT &#8216;s</code> commands is set to the target&#8217;s own name.</dd>
<dt><code>.END</code></dt>
<dd> Any command lines attached to this target are executed after everything else is done.</dd>
<dt><code>.IGNORE</code></dt>
<dd> Mark each of the sources with the <code>.IGNORE</code> attribute. If no sources are specified, this is the equivalent of specifying the &#8211;<code>i</code> option.</dd>
<dt><code>.INTERRUPT</code></dt>
<dd> If is interrupted, the commands for this target will be executed.</dd>
<dt><code>.MAIN</code></dt>
<dd> If no target is specified when is invoked, this target will be built.</dd>
<dt><code>.MAKEFLAGS</code></dt>
<dd> This target provides a way to specify flags for when the makefile is used. The flags are as if typed to the shell, though the &#8211;<code>f</code> option will have no effect.</dd>
<dt><code>.NOPATH</code></dt>
<dd> Apply the <code>.NOPATH</code> attribute to any specified sources.</dd>
<dt><code>.NOTPARALLEL</code></dt>
<dd> Disable parallel mode.</dd>
<dt><code>.NO_PARALLEL</code></dt>
<dd> Synonym for <code>.NOTPARALLEL</code> for compatibility with other pmake variants.</dd>
<dt><code>.ORDER</code></dt>
<dd> The named targets are made in sequence. This ordering does not add targets to the list of targets to be made. Since the dependents of a target do not get built until the target itself could be built, unless `a&#8217; is built by another part of the dependency graph, the following is a dependency loop: </dd>
<pre>
.ORDER a b
b: a
</pre>
<p> The ordering imposed by <code>.ORDER</code> is only relevant for parallel makes.</p>
<dt><code>.PATH</code></dt>
<dd> The sources are directories which are to be searched for files not found in the current directory. If no sources are specified, any previously specified directories are deleted. If the source is the special <code>.DOTLAST</code> target, then the current working directory is searched last.</dd>
<dt><code>.PHONY</code></dt>
<dd> Apply the <code>.PHONY</code> attribute to any specified sources.</dd>
<dt><code>.PRECIOUS</code></dt>
<dd> Apply the <code>.PRECIOUS</code> attribute to any specified sources. If no sources are specified, the <code>.PRECIOUS</code> attribute is applied to every target in the file.</dd>
<dt><code>.SHELL</code></dt>
<dd> Sets the shell that will use to execute commands. The sources are a set of <i>field=value</i> pairs.</dd>
<dl>
<dt><i>name</i></dt>
<dd> This is the minimal specification, used to select one of the builtin shell specs; <i>sh</i> <i>ksh</i> and <i>csh</i></dd>
<dt><i>path</i></dt>
<dd> Specifies the path to the shell.</dd>
<dt><i>hasErrCtl</i></dt>
<dd> Indicates whether the shell supports exit on error.</dd>
<dt><i>check</i></dt>
<dd> The command to turn on error checking.</dd>
<dt><i>ignore</i></dt>
<dd> The command to disable error checking.</dd>
<dt><i>echo</i></dt>
<dd> The command to turn on echoing of commands executed.</dd>
<dt><i>quiet</i></dt>
<dd> The command to turn off echoing of commands executed.</dd>
<dt><i>filter</i></dt>
<dd> The output to filter after issuing the <i>quiet</i> command. It is typically identical to <i>quiet</i></dd>
<dt><i>errFlag</i></dt>
<dd> The flag to pass the shell to enable error checking.</dd>
<dt><i>echoFlag</i></dt>
<dd> The flag to pass the shell to enable command echoing.</dd>
<dt><i>newline</i></dt>
<dd> The string literal to pass the shell that results in a single newline character when used outside of any quoting characters.</dd></dl>
<p> Example: </p>
<pre>
.SHELL: name=ksh path=/bin/ksh hasErrCtl=true \
        check=&quot;set -e&quot; ignore=&quot;set +e&quot; \
        echo=&quot;set -v&quot; quiet=&quot;set +v&quot; filter=&quot;set +v&quot; \
        echoFlag=v errFlag=e newline=&quot;'
'&quot;
</pre>
<dt><code>.SILENT</code></dt>
<dd> Apply the <code>.SILENT</code> attribute to any specified sources. If no sources are specified, the <code>.SILENT</code> attribute is applied to every command in the file.</dd>
<dt><code>.SUFFIXES</code></dt>
<dd> Each source specifies a suffix to <code>.</code> If no sources are specified, any previously specified suffixes are deleted. It allows the creation of suffix-transformation rules. </dd>
<p> Example: </p>
<pre><code>
.SUFFIXES :.o
               .c.o : cc -
    o ${.TARGET} - c $
{
    .IMPSRC
}
</code></pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> uses the following environment variables, if they exist: <code>MACHINE</code> <code>MACHINE_ARCH</code> <code>MAKE</code> <code>MAKEFLAGS</code> <code>MAKEOBJDIR</code> <code>MAKEOBJDIRPREFIX</code> <code>MAKESYSPATH</code> and <code>PWD</code> </p>
<p> <code>MAKEOBJDIRPREFIX</code> and <code>MAKEOBJDIR</code> may only be set in the environment or on the command line to and not as makefile variables; see the description of `<i>.OBJDIR</i> &#8216; for more details.</p>
<h2>FILES</h2>
<dl>
<dt><code>.depend</code></dt>
<dd> list of dependencies</dd>
<dt><code>Makefile</code></dt>
<dd> list of dependencies</dd>
<dt><code>makefile</code></dt>
<dd> list of dependencies</dd>
<dt><code>sys.mk</code></dt>
<dd> system makefile</dd>
<dt><code>/usr/share/mk</code></dt>
<dd> system makefile directory</dd></dl>
<h2>COMPATIBILITY</h2>
<p> The basic make syntax is compatible between different versions of make, however the special variables, variable modifiers and conditionals are not. </p>
<p> The way that parallel makes are scheduled changed in Nx 4.0 so that .ORDER and .WAIT apply recursively to the dependant nodes. The algorithms used may change again in the future. </p>
<p> The way that .for loop variables are substituted changed after Nx 5.0 so that they still appear to be variable expansions. In particular this stops them being treated as syntax, and removes some obscure problems using them in .if statements.</p>
<h2>SEE ALSO</h2>
<p> mkdep(1)</p>
<h2>HISTORY</h2>
<p> is derived from NetBSD&#8217;s <a href="/docs/linux/man/1-make/">make</a>(1). It uses autoconf to facilitate portability to other platforms. </p>
