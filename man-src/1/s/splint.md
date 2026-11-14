---
title: "splint(1)"
name: "splint"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splint/"
description: "splint – A tool for statically checking C programs"
---

<h2 class="name">NAME</h2>
<p> splint &#8211; A tool for statically checking C programs</p>
<h2>SYNOPSIS</h2>
<p> <code>splint</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <code>Splint</code> is a tool for statically checking C programs for security vulnerabilities and common programming mistakes. With minimal effort, Splint can be used as a better <a href="/docs/linux/man/1-lint/">lint</a>(1).If additional effort is invested adding annotations to programs, Splint can perform stronger checks than can be done by any standard lint. For full documentation, please see <a rel="nofollow" href="http://www.splint.org.">http://www.splint.org.</a> This man page only covers a few of the available options. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Shows help </p>
</dl>
<p> <code>Initialization</code> </p>
<p> These flags control directories and files used by Splint. They may be used from the command line or in an options file, but may not be used as control comments in the source code. Except where noted. they have the same meaning preceded by &#8211; or +. </p>
<dl>
<dt><code>-tmpdir</code><i> directory</i></p>
<dd> Set directory for writing temp files. Default is /tmp/. </p>
<dt><code>-I</code><i> directory</i></p>
<dd> Add directory to path searched for C include files. Note there is no space after the I, to be consistent with C preprocessor flags. </p>
<dt><code>-S</code><i> directory</i></p>
<dd> Add directory to path search for .lcl specification files. </p>
<dt><code>-f</code><i> file</i></p>
<dd> Load options file &lt;file&gt;. If this flag is used from the command line, the default ~/.splintrc file is not loaded. This flag may be used in an options file to load in another options file. </p>
<dt><code>-nof </code></p>
<dd> Prevents the default options files (./.splintrc and ~/.splintrc) from being loaded. (Setting -nof overrides +nof, causing the options files to be loaded normally.) </p>
<dt><code>-systemdirs</code><i> directories</i></p>
<dd> Set directories for system files (default is &quot;/usr/include&quot;). Separate directories with colons (e.g., &quot;/usr/include:/usr/local/lib&quot;). Flag settings propagate to files in a system directory. If -systemdirerrors is set, no errors are reported for files in system directories. </p>
</dl>
<p> <code>Pre-processor</code> </p>
<p> These flags are used to define or undefine pre-processor constants. The -I&lt;directory&gt; flag is also passed to the C pre-processor. </p>
<dl>
<dt><code>-D</code><i> initializer</i></p>
<dd> Passed to the C pre-processor. </p>
<dt><code>-U</code><i> initializer</i></p>
<dd> Passed to the C pre-processor </p>
</dl>
<p> <code>Libraries</code> These flags control the creation and use of libraries. </p>
<dl>
<dt><code>-dump</code><i> file</i></p>
<dd> Save state in &lt;file&gt; for loading. The default extension .lcd is added if &lt;file&gt; has no extension. </p>
<dt><code>-load</code><i> file</i></p>
<dd> Load state from &lt;file&gt; (created by -dump). The default extension .lcd is added if &lt;file&gt; has no extension. Only one library file may be loaded. </p>
<p> By default, the standard library is loaded if the -load flag is not used to load a user library. If no user library is loaded, one of the following flags may be used to select a different standard library. Precede the flag by + to load the described library (or prevent a library from being loaded using nolib). See Apppendix F for information on the provided libraries. </p>
<dt><code>-nolib </code></p>
<dd> Do not load any library. This prevents the standard library from being loaded. </p>
<dt><code>-ansi-lib </code></p>
<dd> Use the ANSI standard library (selected by default). </p>
<dt><code>-strict-lib </code></p>
<dd> Use strict version of the ANSI standard library. </p>
<dt><code>-posix-lib </code></p>
<dd> Use the POSIX standard library. </p>
<dt><code>-posix-strict-lib </code></p>
<dd> Use the strict version of the POSIX standard library. </p>
<dt><code>-1-lib </code></p>
<dd> Use UNIX version of standard library. </p>
<dt><code>-1-strict-lib </code></p>
<dd> Use the strict version of the UNIX standard library. </p>
</dl>
<p> <code>Output</code> </p>
<p> These flags control what additional information is printed by Splint. Setting +&lt;flag&gt; causes the described information to be printed; setting -&lt;flag&gt; prevents it. By default, all these flags are off. </p>
<dl>
<dt><code>-usestderr </code></p>
<dd> Send error messages to standard error (instead of standard out). </p>
<dt><code>-showsummary </code></p>
<dd> Show a summary of all errors reported and suppressed. Counts of suppressed errors are not necessarily correct since turning a flag off may prevent some checking from being done to save computation, and errors that are not reported may propagate differently from when they are reported. </p>
<dt><code>-showscan </code></p>
<dd> Show file names are they are processed. </p>
<dt><code>-showalluses </code></p>
<dd> Show list of uses of all external identifiers sorted by number of uses. </p>
<dt><code>-stats </code></p>
<dd> Display number of lines processed and checking time. </p>
<dt><code>-timedist </code></p>
<dd> Display distribution of where checking time is spent. </p>
<dt><code>-quiet </code></p>
<dd> Suppress herald and error count. (If quiet is not set, Splint prints out a herald with version information before checking begins, and a line summarizing the total number of errors reported.) </p>
<dt><code>-whichlib </code></p>
<dd> Print out the standard library filename and creation information. </p>
<dt><code>-limit</code><i> number</i></p>
<dd> At most &lt;number&gt; similar errors are reported consecutively. Further errors are suppressed, and a message showing the number of suppressed messages is printed. </p>
</dl>
<p> <code>Expected Errors</code> </p>
<p> Normally, Splint will expect to report no errors. The exit status will be success (0) if no errors are reported, and failure if any errors are reported. Flags can be used to set the expected number of reported errors. Because of the provided error suppression mechanisms, these options should probably not be used for final checking real programs but may be useful in developing programs using make. </p>
<dl>
<dt><code>-expect &lt;number&gt; </code></p>
<dd> Exactly &lt;number&gt; code errors are expected. Splint will exit with failure exit status unless &lt;number&gt; code errors are detected. </p>
<dt><code>-Message Format</code></p>
<dd> These flags control how messages are printed. They may be set at the command line, in options files, or locally in syntactic comments. The linelen and limit flags may be preceded by + or &#8211; with the same meaning; for the other flags, + turns on the describe printing and &#8211; turns it off. The box to the left of each flag gives its default value. </p>
<dt><code>-showcolumn </code></p>
<dd> Show column number where error is found. Default: + </p>
<dt><code>-showfunc </code></p>
<dd> Show name of function (or macro) definition containing error. The function name is printed once before the first message detected in that function. Default: + </p>
<dt><code>-showallconjs </code></p>
<dd> Show all possible alternate types (see Section 8.2.2). Default: &#8211; </p>
<dt><code>-paren-file-format </code></p>
<dd> Use file(line) format in messages. </p>
<dt><code>-hints </code></p>
<dd> Provide hints describing an error and how a message may be suppressed for the first error reported in each error class. Default: + </p>
<dt><code>-forcehints </code></p>
<dd> Provide hints for all errors reported, even if the hint has already been displayed for the same error class. Default: &#8211; </p>
<dt><code>-linelen</code><i> number</i></p>
<dd> Set length of maximum message line to &lt;number&gt; characters. Splint will split messages longer than &lt;number&gt; characters long into multiple lines. Default: 80 </p>
</dl>
<p> <code>Mode Selector Flags</code> </p>
<p> Mode selects flags set the mode checking flags to predefined values. They provide a quick coarse-grain way of controlling what classes of errors are reported. Specific checking flags may be set after a mode flag to override the mode settings. Mode flags may be used locally, however the mode settings will override specific command line flag settings. A warning is produced if a mode flag is used after a mode checking flag has been set. </p>
<p> These are brief descriptions to give a general idea of what each mode does. To see the complete flag settings in each mode, use splint -help modes. A mode flag has the same effect when used with either + or -. </p>
<dl>
<dt><code>-weak </code></p>
<dd> Weak checking, intended for typical unannotated C code. No modifies checking, macro checking, rep exposure, or clean interface checking is done. Return values of type int may be ignored. The types bool, int, char and user-defined enum types are all equivalent. Old style declarations are unreported. </p>
<dt><code>-standard </code></p>
<dd> The default mode. All checking done by weak, plus modifies checking, global alias checking, use all parameters, using released storage, ignored return values or any type, macro checking, unreachable code, infinite loops, and fall-through cases. The types bool, int and char are distinct. Old style declarations are reported. </p>
<dt><code>-checks </code></p>
<dd> Moderately strict checking. All checking done by standard, plus must modification checking, rep exposure, return alias, memory management and complete interfaces. </p>
<dt><code>-strict </code></p>
<dd> Absurdly strict checking. All checking done by checks, plus modifications and global variables used in unspecified functions, strict standard library, and strict typing of C operators. A special reward will be presented to the first person to produce a real program that produces no errors with strict checking. </p>
</dl>
<h2>AUTHOR</h2>
<p> If you need to get in contact with the authors send email to </p>
<p> or visit </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lint/">lint</a>(1) </p>
<h2>Index</h2>
