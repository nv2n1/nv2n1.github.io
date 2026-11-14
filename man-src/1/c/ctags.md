---
title: "ctags(1)"
name: "ctags"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctags/"
description: "ctags – Generate tag files for source code"
---

<h2 class="name">NAME</h2>
<p> ctags &#8211; Generate tag files for source code </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>ctags</code> [<code>options</code>] [<i>file(s)</i>]</p>
<dd>
<dt><code>etags</code> [<code>options</code>] [<i>file(s)</i>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>ctags</code> and <code>etags</code> programs (hereinafter collectively referred to as <code>ctags</code>, except where distinguished) generate an index (or &quot;tag&quot;) file for a variety of language objects found in <i>file(s)</i>. This tag file allows these items to be quickly and easily located by a text editor or other utility. A &quot;tag&quot; signifies a language object for which an index entry is available (or, alternatively, the index entry created for that object). </p>
<p> Alternatively, <code>ctags</code> can generate a cross reference file which lists, in human readable form, information about the various source objects found in a set of language files. </p>
<p> Tag index files are supported by numerous editors, which allow the user to locate the object associated with a name appearing in a source file and jump to the file and line which defines the name. Those known about at the time of this release are: </p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-vi/">Vi</a></code>(1) and its derivatives (e.g. Elvis, Vim, Vile, Lemmy), <code>CRiSP</code>, <code>Emacs</code>, <code>FTE</code> (Folding Text Editor), <code>JED</code>, <code>jEdit</code>, <code>Mined</code>, <code>NEdit</code> (Nirvana Edit), <code>TSE</code> (The SemWare Editor), <code>UltraEdit</code>, <code>WorkSpace</code>, <code>X2</code>, <code>Zeus</code></dl>
<p> <code>Ctags</code> is capable of generating different kinds of tags for each of many different languages. For a complete list of supported languages, the names by which they are recognized, and the kinds of tags which are generated for each, see the <code>&#8211;list-languages</code> and <code>&#8211;list-kinds</code> options. </p>
<h2>SOURCE FILES</h2>
<p> Unless the <code>&#8211;language-force</code> option is specified, the language of each source file is automatically selected based upon a mapping of file names to languages. The mappings in effect for each language may be display using the <code>&#8211;list-maps</code> option and may be changed using the <code>&#8211;langmap</code> option. On platforms which support it, if the name of a file is not mapped to a language and the file is executable, the first line of the file is checked to see if the file is a &quot;#!&quot; script for a recognized language. </p>
<p> By default, all other files names are ignored. This permits running <code>ctags</code> on all files in either a single directory (e.g. &quot;ctags *&quot;), or on all files in an entire source directory tree (e.g. &quot;ctags -R&quot;), since only those files whose names are mapped to languages will be scanned. </p>
<p> [The reason that .h extensions are mapped to C++ files rather than C files is because it is common to use .h extensions in C++, and no harm results in treating them as C++ files.] </p>
<h2>OPTIONS</h2>
<p> Despite the wealth of available options, defaults are set so that <code>ctags</code> is most commonly executed without any options (e.g. &quot;ctags *&quot;, or &quot;ctags -R&quot;), which will create a tag file in the current directory for all recognized source files. The options described below are provided merely to allow custom tailoring to meet special needs. </p>
<p> Note that spaces separating the single-letter options from their parameters are optional. </p>
<p> Note also that the boolean parameters to the long form options (those beginning with &quot;&#8211;&quot; and that take a &quot;<i>[=yes</i>|<i>no]</i>&quot; parameter) may be omitted, in which case &quot;<code>=</code><i>yes</i>&quot; is implied. (e.g. <code>&#8211;sort</code> is equivalent to <code>&#8211;sort</code>=<i>yes</i>). Note further that &quot;=<i>1</i>&quot; and &quot;=<i>on</i>&quot; are considered synonyms for &quot;=<i>yes</i>&quot;, and that &quot;=<i>0</i>&quot; and &quot;=<i>off</i>&quot; are considered synonyms for &quot;=<i>no</i>&quot;. </p>
<p> Some options are either ignored or useful only when used while running in etags mode (see <code>-e</code> option). Such options will be noted. </p>
<p> Most options may appear anywhere on the command line, affecting only those files which follow the option. A few options, however, must appear before the first file name and will be noted as such. </p>
<p> Options taking language names will accept those names in either upper or lower case. See the <code>&#8211;list-languages</code> option for a complete list of the built-in language names. </p>
<dl>
<dt><code>-a</code></p>
<dd> Equivalent to <code>&#8211;append</code>. </p>
<dt><code>-B</code></p>
<dd> Use backward searching patterns (e.g. ?pattern?). [Ignored in etags mode] </p>
<dt><code>-e</code></p>
<dd> Enable etags mode, which will create a tag file for use with the Emacs editor. Alternatively, if <code>ctags</code> is invoked by a name containing the string &quot;etags&quot; (either by renaming, or creating a link to, the executable), etags mode will be enabled. This option must appear before the first file name. </p>
<dt><code>-f</code><i> tagfile</i></p>
<dd> Use the name specified by <i>tagfile</i> for the tag file (default is &quot;tags&quot;, or &quot;TAGS&quot; when running in etags mode). If <i>tagfile</i> is specified as &quot;-&quot;, then the tag file is written to standard output instead. <code>Ctags</code> will stubbornly refuse to take orders if <i>tagfile</i> exists and its first line contains something other than a valid tags line. This will save your neck if you mistakenly type &quot;ctags -f *.c&quot;, which would otherwise overwrite your first C file with the tags generated by the rest! It will also refuse to accept a multi-character file name which begins with a &#8216;-&#8216; (dash) character, since this most likely means that you left out the tag file name and this option tried to grab the next option as the file name. If you really want to name your output tag file &quot;-ugly&quot;, specify it as &quot;./-ugly&quot;. This option must appear before the first file name. If this option is specified more than once, only the last will apply. </p>
<dt><code>-F</code></p>
<dd> Use forward searching patterns (e.g. /pattern/) (default). [Ignored in etags mode] </p>
<dt><code>-h</code><i> list</i></p>
<dd> Specifies a list of file extensions, separated by periods, which are to be interpreted as include (or header) files. To indicate files having no extension, use a period not followed by a non-period character (e.g. &quot;.&quot;, &quot;..x&quot;, &quot;.x.&quot;). This option only affects how the scoping of a particular kinds of tags is interpreted (i.e. whether or not they are considered as globally visible or visible only within the file in which they are defined); it does not map the extension to any particular language. Any tag which is located in a non-include file and cannot be seen (e.g. linked to) from another file is considered to have file-limited (e.g. static) scope. No kind of tag appearing in an include file will be considered to have file-limited scope. If the first character in the list is a plus sign, then the extensions in the list will be appended to the current list; otherwise, the list will replace the current list. See, also, the <code>&#8211;file-scope</code> option. The default list is &quot;.h.H.hh.hpp.hxx.h++.inc.def&quot;. To restore the default list, specify <code>-h</code> <i>default</i>. Note that if an extension supplied to this option is not already mapped to a particular language (see <code>SOURCE FILES</code>, above), you will also need to use either the <code>&#8211;langmap</code> or <code>&#8211;language-force</code> option. </p>
<dt><code>-I</code><i> identifier-list</i></p>
<dd> Specifies a list of identifiers which are to be specially handled while parsing C and C++ source files. This option is specifically provided to handle special cases arising through the use of preprocessor macros. When the identifiers listed are simple identifiers, these identifiers will be ignored during parsing of the source files. If an identifier is suffixed with a &#8216;+&#8217; character, <code>ctags</code> will also ignore any parenthesis-enclosed argument list which may immediately follow the identifier in the source files. If two identifiers are separated with the &#8216;=&#8217; character, the first identifiers is replaced by the second identifiers for parsing purposes. The list of identifiers may be supplied directly on the command line or read in from a separate file. If the first character of <i>identifier-list</i> is &#8216;@&#8217;, &#8216;.&#8217; or a pathname separator (&#8216;/&#8217; or &#8216;\&#8217;), or the first two characters specify a drive letter (e.g. &quot;C:&quot;), the parameter <i>identifier-list</i> will be interpreted as a filename from which to read a list of identifiers, one per input line. Otherwise, <i>identifier-list</i> is a list of identifiers (or identifier pairs) to be specially handled, each delimited by a either a comma or by white space (in which case the list should be quoted to keep the entire list as one command line argument). Multiple <code>-I</code> options may be supplied. To clear the list of ignore identifiers, supply a single dash (&quot;-&quot;) for <i>identifier-list</i>. </p>
<p> This feature is useful when preprocessor macros are used in such a way that they cause syntactic confusion due to their presence. Indeed, this is the best way of working around a number of problems caused by the presence of syntax-busting macros in source files (see <code>CAVEATS</code>, below). Some examples will illustrate this point. </p>
<dl>
<dt>
<dd> int foo ARGDECL4(void *, ptr, long int, nbytes)</dl>
<dt>
<dd> In the above example, the macro &quot;ARGDECL4&quot; would be mistakenly interpreted to be the name of the function instead of the correct name of &quot;foo&quot;. Specifying <code>-I</code> <i>ARGDECL4</i> results in the correct behavior. </p>
<dl>
<dt>
<dd> /* creates an RCS version string in module */<br />
 MODULE_VERSION(&quot;$Revision: 750 $&quot;)</dl>
<dt>
<dd> In the above example the macro invocation looks too much like a function definition because it is not followed by a semicolon (indeed, it could even be followed by a global variable definition that would look much like a K&amp;R style function parameter declaration). In fact, this seeming function definition could possibly even cause the rest of the file to be skipped over while trying to complete the definition. Specifying <code>-I</code> <i>MODULE_VERSION+</i> would avoid such a problem. </p>
<dl>
<dt>
<dd> CLASS Example { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;//&nbsp;your content here<br />
 };</dl>
<dt>
<dd> The example above uses &quot;CLASS&quot; as a preprocessor macro which expands to something different for each platform. For instance CLASS may be defined as &quot;class __declspec(dllexport)&quot; on Win32 platforms and simply &quot;class&quot; on UNIX. Normally, the absence of the C++ keyword &quot;class&quot; would cause the source file to be incorrectly parsed. Correct behavior can be restored by specifying <code>-I</code> <i>CLASS=class</i>. </p>
<dt><code>-L</code><i> file</i></p>
<dd> Read from <i>file</i> a list of file names for which tags should be generated. If <i>file</i> is specified as &quot;-&quot;, then file names are read from standard input. File names read using this option are processed following file names appearing on the command line. Options are also accepted in this input. If this option is specified more than once, only the last will apply. <code>Note:</code> <i>file</i> is read in line-oriented mode, where a new line is the only delimiter and non-trailing white space is considered significant, in order that file names containing spaces may be supplied (however, trailing white space is stripped from lines); this can affect how options are parsed if included in the input. </p>
<dt><code>-n</code></p>
<dd> Equivalent to <code>&#8211;excmd</code>=<i>number</i>. </p>
<dt><code>-N</code></p>
<dd> Equivalent to <code>&#8211;excmd</code>=<i>pattern</i>. </p>
<dt><code>-o</code><i> tagfile</i></p>
<dd> Equivalent to <code>-f</code> <i>tagfile</i>. </p>
<dt><code>-R</code></p>
<dd> Equivalent to <code>&#8211;recurse</code>. </p>
<dt><code>-u</code></p>
<dd> Equivalent to <code>&#8211;sort</code>=<i>no</i> (i.e. &quot;unsorted&quot;). </p>
<dt><code>-V</code></p>
<dd> Equivalent to <code>&#8211;verbose</code>. </p>
<dt><code>-w</code></p>
<dd> This option is silently ignored for backward-compatibility with the ctags of SVR4 Unix. </p>
<dt><code>-x</code></p>
<dd> Print a tabular, human-readable cross reference (xref) file to standard output instead of generating a tag file. The information contained in the output includes: the tag name; the kind of tag; the line number, file name, and source line (with extra white space condensed) of the file which defines the tag. No tag file is written and all options affecting tag file output will be ignored. Example applications for this feature are generating a listing of all functions located in a source file (e.g. <code>ctags -x &#8211;c-kinds</code>=<i>f</i> <i>file</i>), or generating a list of all externally visible global variables located in a source file (e.g. <code>ctags -x &#8211;c-kinds</code>=<i>v</i> <code>&#8211;file-scope</code>=<i>no file</i>). This option must appear before the first file name. </p>
<dt><code>&#8211;append</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Indicates whether tags generated from the specified files should be appended to those already present in the tag file or should replace them. This option is off by default. This option must appear before the first file name. </p>
<dt><code>&#8211;etags-include</code>=<i>file</i></p>
<dd> Include a reference to <i>file</i> in the tag file. This option may be specified as many times as desired. This supports Emacs&#8217; capability to use a tag file which &quot;includes&quot; other tag files. [Available only in etags mode] </p>
<dt><code>&#8211;exclude</code>=[<i>pattern</i>]</p>
<dd> Add <i>pattern</i> to a list of excluded files and directories. This option may be specified as many times as desired. For each file name considered by <code>ctags</code>, each <i>pattern</i> specified using this option will be compared against both the complete path (e.g. some/path/base.ext) and the base name (e.g. base.ext) of the file, thus allowing patterns which match a given file name irrespective of its path, or match only a specific path. If appropriate support is available from the runtime library of your C compiler, then <i>pattern</i> may contain the usual shell wildcards (not regular expressions) common on Unix (be sure to quote the option parameter to protect the wildcards from being expanded by the shell before being passed to <code>ctags</code>; also be aware that wildcards can match the slash character, &#8216;/&#8217;). You can determine if shell wildcards are available on your platform by examining the output of the <code>&#8211;version</code> option, which will include &quot;+wildcards&quot; in the compiled feature list; otherwise, <i>pattern</i> is matched against file names using a simple textual comparison. </p>
<p> If <i>pattern</i> begins with the character &#8216;@&#8217;, then the rest of the string is interpreted as a file name from which to read exclusion patterns, one per line. If <i>pattern</i> is empty, the list of excluded patterns is cleared. Note that at program startup, the default exclude list contains &quot;EIFGEN&quot;, &quot;SCCS&quot;, &quot;RCS&quot;, and &quot;CVS&quot;, which are names of directories for which it is generally not desirable to descend while processing the <code>&#8211;recurse</code> option. </p>
<dt><code>&#8211;excmd</code>=<i>type</i></p>
<dd> Determines the type of EX command used to locate tags in the source file. [Ignored in etags mode] </p>
<p> The valid values for <i>type</i> (either the entire word or the first letter is accepted) are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><i>number</i></p>
<dd> Use only line numbers in the tag file for locating tags. This has four advantages:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Significantly reduces the size of the resulting tag file.</p>
<dt>2.</p>
<dd> Eliminates failures to find tags because the line defining the tag has changed, causing the pattern match to fail (note that some editors, such as <code>vim</code>, are able to recover in many such instances).</p>
<dt>3.</p>
<dd> Eliminates finding identical matching, but incorrect, source lines (see <code>BUGS</code>, below).</p>
<dt>4.</p>
<dd> Retains separate entries in the tag file for lines which are identical in content. In <i>pattern</i> mode, duplicate entries are dropped because the search patterns they generate are identical, making the duplicate entries useless.</dl>
</dl>
<dt>
<dd> However, this option has one significant drawback: changes to the source files can cause the line numbers recorded in the tag file to no longer correspond to the lines in the source file, causing jumps to some tags to miss the target definition by one or more lines. Basically, this option is best used when the source code to which it is applied is not subject to change. Selecting this option type causes the following options to be ignored: <code>-BF</code>. </p>
<dt><i>pattern</i></p>
<dd> Use only search patterns for all tags, rather than the line numbers usually used for macro definitions. This has the advantage of not referencing obsolete line numbers when lines have been added or removed since the tag file was generated. </p>
<dt><i>mixed</i></p>
<dd> In this mode, patterns are generally used with a few exceptions. For C, line numbers are used for macro definition tags. This was the default format generated by the original <code>ctags</code> and is, therefore, retained as the default for this option. For Fortran, line numbers are used for common blocks because their corresponding source lines are generally identical, making pattern searches useless for finding all matches.</dl>
</dl>
<dt><code>&#8211;extra</code>=<i>[+|-]flags</i></p>
<dd> Specifies whether to include extra tag entries for certain kinds of information. The parameter <i>flags</i> is a set of one-letter flags, each representing one kind of extra tag entry to include in the tag file. If <i>flags</i> is preceded by either the &#8216;+&#8217; or &#8216;-&#8216; character, the effect of each flag is added to, or removed from, those currently enabled; otherwise the flags replace any current settings. The meaning of each flag is as follows: </p>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt><i>f</i></p>
<dd> Include an entry for the base file name of every source file (e.g. &quot;example.c&quot;), which addresses the first line of the file.</p>
<dt><i>q</i></p>
<dd> Include an extra class-qualified tag entry for each tag which is a member of a class (for languages for which this information is extracted; currently C++, Eiffel, and Java). The actual form of the qualified tag depends upon the language from which the tag was derived (using a form that is most natural for how qualified calls are specified in the language). For C++, it is in the form &quot;class::member&quot;; for Eiffel and Java, it is in the form &quot;class.member&quot;. This may allow easier location of a specific tags when multiple occurrences of a tag name occur in the tag file. Note, however, that this could potentially more than double the size of the tag file.</dl>
</dl>
<dl>
<dt><code>&#8211;fields</code>=<i>[+|-]flags</i></p>
<dd> Specifies the available extension fields which are to be included in the entries of the tag file (see <code>TAG FILE FORMAT</code>, below, for more information). The parameter <i>flags</i> is a set of one-letter flags, each representing one type of extension field to include, with the following meanings (disabled by default unless indicated): </p>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt><i>a</i></p>
<dd> Access (or export) of class members</p>
<dt><i>f</i></p>
<dd> File-restricted scoping [enabled]</p>
<dt><i>i</i></p>
<dd> Inheritance information</p>
<dt><i>k</i></p>
<dd> Kind of tag as a single letter [enabled]</p>
<dt><i>K</i></p>
<dd> Kind of tag as full name</p>
<dt><i>l</i></p>
<dd> Language of source file containing tag</p>
<dt><i>m</i></p>
<dd> Implementation information</p>
<dt><i>n</i></p>
<dd> Line number of tag definition</p>
<dt><i>s</i></p>
<dd> Scope of tag definition [enabled]</p>
<dt><i>S</i></p>
<dd> Signature of routine (e.g. prototype or parameter list)</p>
<dt><i>z</i></p>
<dd> Include the &quot;kind:&quot; key in kind field</p>
<dt><i>t</i></p>
<dd> Type and name of a variable or typedef as &quot;typeref:&quot; field [enabled]</dl>
</dl>
<dl>
<dt>
<dd> Each letter or group of letters may be preceded by either &#8216;+&#8217; to add it to the default set, or &#8216;-&#8216; to exclude it. In the absence of any preceding &#8216;+&#8217; or &#8216;-&#8216; sign, only those kinds explicitly listed in <i>flags</i> will be included in the output (i.e. overriding the default set). This option is ignored if the option <code>&#8211;format</code>=<i>1</i> has been specified. The default value of this option is <i>fkst</i>.</dl>
<dl>
<dt><code>&#8211;file-scope</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Indicates whether tags scoped only for a single file (i.e. tags which cannot be seen outside of the file in which they are defined, such as &quot;static&quot; tags) should be included in the output. See, also, the <code>-h</code> option. This option is enabled by default. </p>
<dt><code>&#8211;filter</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Causes <code>ctags</code> to behave as a filter, reading source file names from standard input and printing their tags to standard output on a file-by-file basis. If <code>&#8211;sorted</code> is enabled, tags are sorted only within the source file in which they are defined. File names are read from standard input in line-oriented input mode (see note for <code>-L</code> option) and only after file names listed on the command line or from any file supplied using the <code>-L</code> option. When this option is enabled, the options <code>-f</code>, <code>-o</code>, and <code>&#8211;totals</code> are ignored. This option is quite esoteric and is disabled by default. This option must appear before the first file name. </p>
<dt><code>&#8211;filter-terminator</code>=<i>string</i></p>
<dd> Specifies a string to print to standard output following the tags for each file name parsed when the <code>&#8211;filter</code> option is enabled. This may permit an application reading the output of ctags to determine when the output for each file is finished. Note that if the file name read is a directory and <code>&#8211;recurse</code> is enabled, this string will be printed only once at the end of all tags found for by descending the directory. This string will always be separated from the last tag line for the file by its terminating newline. This option is quite esoteric and is empty by default. This option must appear before the first file name. </p>
<dt><code>&#8211;format</code>=<i>level</i></p>
<dd> Change the format of the output tag file. Currently the only valid values for <i>level</i> are <i>1</i> or <i>2</i>. Level 1 specifies the original tag file format and level 2 specifies a new extended format containing extension fields (but in a manner which retains backward-compatibility with original <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) implementations). The default level is 2. This option must appear before the first file name. [Ignored in etags mode] </p>
<dt><code>&#8211;help</code></p>
<dd> Prints to standard output a detailed usage description, and then exits. </p>
<dt><code>&#8211;if0</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Indicates a preference as to whether code within an &quot;#if 0&quot; branch of a preprocessor conditional should be examined for non-macro tags (macro tags are always included). Because the intent of this construct is to disable code, the default value of this option is <i>no</i>. Note that this indicates a preference only and does not guarantee skipping code within an &quot;#if 0&quot; branch, since the fall-back algorithm used to generate tags when preprocessor conditionals are too complex follows all branches of a conditional. This option is disabled by default. </p>
<dt><code>&#8211;&lt;LANG&gt;-kinds</code>=<i>[+|-]kinds</i></p>
<dd> Specifies a list of language-specific kinds of tags (or kinds) to include in the output file for a particular language, where <code>&lt;LANG&gt;</code> is case-insensitive and is one of the built-in language names (see the <code>&#8211;list-languages</code> option for a complete list). The parameter <i>kinds</i> is a group of one-letter flags designating kinds of tags (particular to the language) to either include or exclude from the output. The specific sets of flags recognized for each language, their meanings and defaults may be list using the <code>&#8211;list-kinds</code> option. Each letter or group of letters may be preceded by either &#8216;+&#8217; to add it to, or &#8216;-&#8216; to remove it from, the default set. In the absence of any preceding &#8216;+&#8217; or &#8216;-&#8216; sign, only those kinds explicitly listed in <i>kinds</i> will be included in the output (i.e. overriding the default for the specified language). </p>
<p> As an example for the C language, in order to add prototypes and external variable declarations to the default set of tag kinds, but exclude macros, use <code>&#8211;c-kinds</code>=<i>+px-d</i>; to include only tags for functions, use <code>&#8211;c-kinds</code>=<i>f</i>. </p>
<dt><code>&#8211;langdef</code>=<i>name</i></p>
<dd> Defines a new user-defined language, <i>name</i>, to be parsed with regular expressions. Once defined, <i>name</i> may be used in other options taking language names. The typical use of this option is to first define the language, then map file names to it using <i>&#8211;langmap</i>, then specify regular expressions using <i>&#8211;regex-&lt;LANG&gt;</i> to define how its tags are found. </p>
<dt><code>&#8211;langmap</code>=<i>map[,map[&#8230;]]</i></p>
<dd> Controls how file names are mapped to languages (see the <code>&#8211;list-maps</code> option). Each comma-separated <i>map</i> consists of the language name (either a built-in or user-defined language), a colon, and a list of file extensions and/or file name patterns. A file extension is specified by preceding the extension with a period (e.g. &quot;.c&quot;). A file name pattern is specified by enclosing the pattern in parentheses (e.g. &quot;([Mm]akefile)&quot;). If appropriate support is available from the runtime library of your C compiler, then the file name pattern may contain the usual shell wildcards common on Unix (be sure to quote the option parameter to protect the wildcards from being expanded by the shell before being passed to <code>ctags</code>). You can determine if shell wildcards are available on your platform by examining the output of the <code>&#8211;version</code> option, which will include &quot;+wildcards&quot; in the compiled feature list; otherwise, the file name patterns are matched against file names using a simple textual comparison. When mapping a file extension, it will first be unmapped from any other languages. </p>
<p> If the first character in a map is a plus sign, then the extensions and file name patterns in that map will be appended to the current map for that language; otherwise, the map will replace the current map. For example, to specify that only files with extensions of .c and .x are to be treated as C language files, use &quot;<code>&#8211;langmap</code>=<i>c:.c.x</i>&quot;; to also add files with extensions of .j as Java language files, specify &quot;<code>&#8211;langmap</code>=<i>c:.c.x,java:+.j</i>&quot;. To map makefiles (e.g. files named either &quot;Makefile&quot;, &quot;makefile&quot;, or having the extension &quot;.mak&quot;) to a language called &quot;make&quot;, specify &quot;<code>&#8211;langmap</code>=<i>make:([Mm]akefile).mak</i>&quot;. To map files having no extension, specify a period not followed by a non-period character (e.g. &quot;.&quot;, &quot;..x&quot;, &quot;.x.&quot;). To clear the mapping for a particular language (thus inhibiting automatic generation of tags for that language), specify an empty extension list (e.g. &quot;<code>&#8211;langmap</code>=<i>fortran:</i>&quot;). To restore the default language mappings for all a particular language, supply the keyword &quot;default&quot; for the mapping. To specify restore the default language mappings for all languages, specify &quot;<code>&#8211;langmap</code>=<i>default</i>&quot;. Note that file extensions are tested before file name patterns when inferring the language of a file. </p>
<dt><code>&#8211;language-force</code>=<i>language</i></p>
<dd> By default, <code>ctags</code> automatically selects the language of a source file, ignoring those files whose language cannot be determined (see <code>SOURCE FILES</code>, above). This option forces the specified <i>language</i> (case-insensitive; either built-in or user-defined) to be used for every supplied file instead of automatically selecting the language based upon its extension. In addition, the special value <i>auto</i> indicates that the language should be automatically selected (which effectively disables this option). </p>
<dt><code>&#8211;languages</code>=<i>[+|-]list</i></p>
<dd> Specifies the languages for which tag generation is enabled, with <i>list</i> containing a comma-separated list of language names (case-insensitive; either built-in or user-defined). If the first language of <i>list</i> is not preceded by either a &#8216;+&#8217; or &#8216;-&#8216;, the current list will be cleared before adding or removing the languages in <i>list</i>. Until a &#8216;-&#8216; is encountered, each language in the list will be added to the current list. As either the &#8216;+&#8217; or &#8216;-&#8216; is encountered in the list, the languages following it are added or removed from the current list, respectively. Thus, it becomes simple to replace the current list with a new one, or to add or remove languages from the current list. The actual list of files for which tags will be generated depends upon the language extension mapping in effect (see the <code>&#8211;langmap</code> option). Note that all languages, including user-defined languages are enabled unless explicitly disabled using this option. Language names included in <i>list</i> may be any built-in language or one previously defined with <code>&#8211;langdef</code>. The default is &quot;all&quot;, which is also accepted as a valid argument. See the <code>&#8211;list-languages</code> option for a complete list of the built-in language names. </p>
<dt><code>&#8211;license</code></p>
<dd> Prints a summary of the software license to standard output, and then exits. </p>
<dt><code>&#8211;line-directives</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Specifies whether &quot;#line&quot; directives should be recognized. These are present in the output of preprocessors and contain the line number, and possibly the file name, of the original source file(s) from which the preprocessor output file was generated. When enabled, this option will cause <code>ctags</code> to generate tag entries marked with the file names and line numbers of their locations original source file(s), instead of their actual locations in the preprocessor output. The actual file names placed into the tag file will have the same leading path components as the preprocessor output file, since it is assumed that the original source files are located relative to the preprocessor output file (unless, of course, the #line directive specifies an absolute path). This option is off by default. <code>Note:</code> This option is generally only useful when used together with the <code>&#8211;excmd</code>=<i>number</i> (<code>-n</code>) option. Also, you may have to use either the <code>&#8211;langmap</code> or <code>&#8211;language-force</code> option if the extension of the preprocessor output file is not known to <code>ctags</code>. </p>
<dt><code>&#8211;links</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Indicates whether symbolic links (if supported) should be followed. When disabled, symbolic links are ignored. This option is on by default. </p>
<dt><code>&#8211;list-kinds</code>[=<i>language</i>|<i>all</i>]</p>
<dd> Lists the tag kinds recognized for either the specified language or all languages, and then exits. Each kind of tag recorded in the tag file is represented by a one-letter flag, which is also used to filter the tags placed into the output through use of the <code>&#8211;&lt;LANG&gt;-kinds</code> option. Note that some languages and/or tag kinds may be implemented using regular expressions and may not be available if regex support is not compiled into <code>ctags</code> (see the <code>&#8211;regex-&lt;LANG&gt;</code> option). Each kind listed is enabled unless followed by &quot;[off]&quot;. </p>
<dt><code>&#8211;list-maps</code>[=<i>language</i>|<i>all</i>]</p>
<dd> Lists the file extensions and file name patterns which associate a file name with a language for either the specified language or all languages, and then exits. See the <code>&#8211;langmap</code> option, and <code>SOURCE FILES</code>, above. </p>
<dt><code>&#8211;list-languages</code></p>
<dd> Lists the names of the languages understood by <code>ctags</code>, and then exits. These language names are case insensitive and may be used in the <code>&#8211;language-force</code>, <code>&#8211;languages</code>, <code>&#8211;&lt;LANG&gt;-kinds</code>, and <code>&#8211;regex-&lt;LANG&gt;</code> options. </p>
<dt><code>&#8211;options</code>=<i>file</i></p>
<dd> Read additional options from <i>file</i>. The file should contain one option per line. As a special case, if <code>&#8211;options</code>=<i>NONE</i> is specified as the first option on the command line, it will disable the automatic reading of any configuration options from either a file or the environment (see <code>FILES</code>). </p>
<dt><code>&#8211;recurse</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Recurse into directories encountered in the list of supplied files. If the list of supplied files is empty and no file list is specified with the <code>-L</code> option, then the current directory (i.e. &quot;.&quot;) is assumed. Symbolic links are followed. If you don&#8217;t like these behaviors, either explicitly specify the files or pipe the output of <code><a href="/docs/linux/man/1-find/">find</a></code>(1) into <code>ctags -L-</code> instead. <code>Note:</code> This option is not supported on all platforms at present. It is available if the output of the <code>&#8211;help</code> option includes this option. See, also, the <code>&#8211;exclude</code> to limit recursion. </p>
<dt><code>&#8211;regex-&lt;LANG&gt;</code>=<i>/regexp/replacement/[kind-spec/][flags]</i></p>
<dd> The <i>/regexp/replacement/</i> pair define a regular expression replacement pattern, similar in style to <code>sed</code> substitution commands, with which to generate tags from source files mapped to the named language, <code>&lt;LANG&gt;</code>, (case-insensitive; either a built-in or user-defined language). The regular expression, <i>regexp</i>, defines an extended regular expression (roughly that used by <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1)), which is used to locate a single source line containing a tag and may specify tab characters using 	. When a matching line is found, a tag will be generated for the name defined by <i>replacement</i>, which generally will contain the special back-references \1 through \9 to refer to matching sub-expression groups within <i>regexp</i>. The &#8216;/&#8217; separator characters shown in the parameter to the option can actually be replaced by any character. Note that whichever separator character is used will have to be escaped with a backslash (&#8216;\&#8217;) character wherever it is used in the parameter as something other than a separator. The regular expression defined by this option is added to the current list of regular expressions for the specified language unless the parameter is omitted, in which case the current list is cleared. </p>
<p> Unless modified by <i>flags</i>, <i>regexp</i> is interpreted as a Posix extended regular expression. The <i>replacement</i> should expand for all matching lines to a non-empty string of characters, or a warning message will be reported. An optional kind specifier for tags matching <i>regexp</i> may follow <i>replacement</i>, which will determine what kind of tag is reported in the &quot;kind&quot; extension field (see <code>TAG FILE FORMAT</code>, below). The full form of <i>kind-spec</i> is in the form of a single letter, a comma, a name (without spaces), a comma, a description, followed by a separator, which specify the short and long forms of the kind value and its textual description (displayed using <code>&#8211;list-kinds</code>). Either the kind name and/or the description may be omitted. If <i>kind-spec</i> is omitted, it defaults to &quot;<i>r,regex</i>&quot;. Finally, <i>flags</i> are one or more single-letter characters having the following effect upon the interpretation of <i>regexp</i>: </p>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt><i>b</i></p>
<dd> The pattern is interpreted as a Posix basic regular expression.</p>
<dt><i>e</i></p>
<dd> The pattern is interpreted as a Posix extended regular expression (default).</p>
<dt><i>i</i></p>
<dd> The regular expression is to be applied in a case-insensitive manner.</dl>
</dl>
<dl>
<dt>
<dd> Note that this option is available only if <code>ctags</code> was compiled with support for regular expressions, which depends upon your platform. You can determine if support for regular expressions is compiled in by examining the output of the <code>&#8211;version</code> option, which will include &quot;+regex&quot; in the compiled feature list. </p>
<p> For more information on the regular expressions used by <code>ctags</code>, see either the <code>regex(5,7)</code> man page, or the GNU info documentation for regex (e.g. &quot;info regex&quot;).</dl>
<dl>
<dt><code>&#8211;sort</code>[=<i>yes</i>|<i>no</i>|<i>foldcase</i>]</p>
<dd> Indicates whether the tag file should be sorted on the tag name (default is <i>yes</i>). Note that the original <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) required sorted tags. The <i>foldcase</i> value specifies case insensitive (or case-folded) sorting. Fast binary searches of tag files sorted with case-folding will require special support from tools using tag files, such as that found in the ctags readtags library, or Vim version 6.2 or higher (using &quot;set ignorecase&quot;). This option must appear before the first file name. [Ignored in etags mode] </p>
<dt><code>&#8211;tag-relative</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Indicates that the file paths recorded in the tag file should be relative to the directory containing the tag file, rather than relative to the current directory, unless the files supplied on the command line are specified with absolute paths. This option must appear before the first file name. The default is <i>yes</i> when running in etags mode (see the <code>-e</code> option), <i>no</i> otherwise. </p>
<dt><code>&#8211;totals</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Prints statistics about the source files read and the tag file written during the current invocation of <code>ctags</code>. This option is off by default. This option must appear before the first file name. </p>
<dt><code>&#8211;verbose</code>[=<i>yes</i>|<i>no</i>]</p>
<dd> Enable verbose mode. This prints out information on option processing and a brief message describing what action is being taken for each file considered by <code>ctags</code>. Normally, <code>ctags</code> does not read command line arguments until after options are read from the configuration files (see <code>FILES</code>, below) and the <code>CTAGS</code> environment variable. However, if this option is the first argument on the command line, it will take effect before any options are read from these sources. The default is <i>no</i>. </p>
<dt><code>&#8211;version</code></p>
<dd> Prints a version identifier for <code>ctags</code> to standard output, and then exits. This is guaranteed to always contain the string &quot;Exuberant Ctags&quot;. </p>
</dl>
<h2>OPERATIONAL DETAILS</h2>
<p> As <code>ctags</code> considers each file name in turn, it tries to determine the language of the file by applying the following three tests in order: if the file extension has been mapped to a language, if the file name matches a shell pattern mapped to a language, and finally if the file is executable and its first line specifies an interpreter using the Unix-style &quot;#!&quot; specification (if supported on the platform). If a language was identified, the file is opened and then the appropriate language parser is called to operate on the currently open file. The parser parses through the file and adds an entry to the tag file for each language object it is written to handle. See <code>TAG FILE FORMAT</code>, below, for details on these entries. </p>
<p> This implementation of <code>ctags</code> imposes no formatting requirements on C code as do legacy implementations. Older implementations of ctags tended to rely upon certain formatting assumptions in order to help it resolve coding dilemmas caused by preprocessor conditionals. </p>
<p> In general, <code>ctags</code> tries to be smart about conditional preprocessor directives. If a preprocessor conditional is encountered within a statement which defines a tag, <code>ctags</code> follows only the first branch of that conditional (except in the special case of &quot;#if 0&quot;, in which case it follows only the last branch). The reason for this is that failing to pursue only one branch can result in ambiguous syntax, as in the following example: </p>
<dl>
<dt>
<dd> #ifdef TWO_ALTERNATIVES<br />
 struct {<br />
 #else<br />
 union {<br />
 #endif</p>
<dl>
<dt>
<dd> short a;<br />
 long b;</dl>
<p> }</dl>
<p> Both branches cannot be followed, or braces become unbalanced and <code>ctags</code> would be unable to make sense of the syntax. </p>
<p> If the application of this heuristic fails to properly parse a file, generally due to complicated and inconsistent pairing within the conditionals, <code>ctags</code> will retry the file using a different heuristic which does not selectively follow conditional preprocessor branches, but instead falls back to relying upon a closing brace (&quot;}&quot;) in column 1 as indicating the end of a block once any brace imbalance results from following a #if conditional branch. </p>
<p> <code>Ctags</code> will also try to specially handle arguments lists enclosed in double sets of parentheses in order to accept the following conditional construct: </p>
<dl>
<dt>
<dd> extern void foo __ARGS((int one, char two));</dl>
<p> Any name immediately preceding the &quot;((&quot; will be automatically ignored and the previous name will be used. </p>
<p> C++ operator definitions are specially handled. In order for consistency with all types of operators (overloaded and conversion), the operator name in the tag file will always be preceded by the string &quot;operator &quot; (i.e. even if the actual operator definition was written as &quot;operator&lt;&lt;&quot;). </p>
<p> After creating or appending to the tag file, it is sorted by the tag name, removing identical tag lines. </p>
<h2>TAG FILE FORMAT</h2>
<p> When not running in etags mode, each entry in the tag file consists of a separate line, each looking like this in the most general case: </p>
<dl>
<dt>
<dd> tag_name&lt;TAB&gt;file_name&lt;TAB&gt;ex_cmd;&quot;&lt;TAB&gt;extension_fields</dl>
<p> The fields and separators of these lines are specified as follows: </p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> tag name</p>
<dt>2.</p>
<dd> single tab character</p>
<dt>3.</p>
<dd> name of the file in which the object associated with the tag is located</p>
<dt>4.</p>
<dd> single tab character</p>
<dt>5.</p>
<dd> EX command used to locate the tag within the file; generally a search pattern (either /pattern/ or ?pattern?) or line number (see <code>&#8211;excmd</code>). Tag file format 2 (see <code>&#8211;format</code>) extends this EX command under certain circumstances to include a set of extension fields (described below) embedded in an EX comment immediately appended to the EX command, which leaves it backward-compatible with original <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) implementations.</dl>
</dl>
<p> A few special tags are written into the tag file for internal purposes. These tags are composed in such a way that they always sort to the top of the file. Therefore, the first two characters of these tags are used a magic number to detect a tag file for purposes of determining whether a valid tag file is being overwritten rather than a source file. </p>
<p> Note that the name of each source file will be recorded in the tag file exactly as it appears on the command line. Therefore, if the path you specified on the command line was relative to the current directory, then it will be recorded in that same manner in the tag file. See, however, the <code>&#8211;tag-relative</code> option for how this behavior can be modified. </p>
<p> Extension fields are tab-separated key-value pairs appended to the end of the EX command as a comment, as described above. These key value pairs appear in the general form &quot;<i>key</i>:<i>value</i>&quot;. Their presence in the lines of the tag file are controlled by the <code>&#8211;fields</code> option. The possible keys and the meaning of their values are as follows: </p>
<dl>
<dt><i>access</i></p>
<dd> Indicates the visibility of this class member, where <i>value</i> is specific to the language. </p>
<dt><i>file</i></p>
<dd> Indicates that the tag has file-limited visibility. This key has no corresponding value. </p>
<dt><i>kind</i></p>
<dd> Indicates the type, or kind, of tag. Its value is either one of the corresponding one-letter flags described under the various <code>&#8211;&lt;LANG&gt;-kinds</code> options above, or a full name. It is permitted (and is, in fact, the default) for the key portion of this field to be omitted. The optional behaviors are controlled with the <code>&#8211;fields</code> option. </p>
<dt><i>implementation</i></p>
<dd> When present, this indicates a limited implementation (abstract vs. concrete) of a routine or class, where <i>value</i> is specific to the language (&quot;virtual&quot; or &quot;pure virtual&quot; for C++; &quot;abstract&quot; for Java). </p>
<dt><i>inherits</i></p>
<dd> When present, <i>value</i>. is a comma-separated list of classes from which this class is derived (i.e. inherits from). </p>
<dt><i>signature</i></p>
<dd> When present, <i>value</i> is a language-dependent representation of the signature of a routine. A routine signature in its complete form specifies the return type of a routine and its formal argument list. This extension field is presently supported only for C-based languages and does not include the return type. </p>
</dl>
<p> In addition, information on the scope of the tag definition may be available, with the key portion equal to some language-dependent construct name and its value the name declared for that construct in the program. This scope entry indicates the scope in which the tag was found. For example, a tag generated for a C structure member would have a scope looking like &quot;struct:myStruct&quot;. </p>
<h2>HOW TO USE WITH VI</h2>
<p> Vi will, by default, expect a tag file by the name &quot;tags&quot; in the current directory. Once the tag file is built, the following commands exercise the tag indexing feature:</p>
<dl>
<dt><code>vi -t tag</code></p>
<dd> Start vi and position the cursor at the file and line where &quot;tag&quot; is defined.</p>
<dt><code>:ta tag</code></p>
<dd> Find a tag.</p>
<dt><code>Ctrl-]</code></p>
<dd> Find the tag under the cursor.</p>
<dt><code>Ctrl-T</code></p>
<dd> Return to previous location before jump to tag (not widely implemented). </p>
</dl>
<h2>HOW TO USE WITH GNU EMACS</h2>
<p> Emacs will, by default, expect a tag file by the name &quot;TAGS&quot; in the current directory. Once the tag file is built, the following commands exercise the tag indexing feature:</p>
<dl>
<dt><code>M-x visit-tags-table &lt;RET&gt; FILE &lt;RET&gt;</code></p>
<dd> Select the tag file, &quot;FILE&quot;, to use.</p>
<dt><code>M-. [TAG] &lt;RET&gt;</code></p>
<dd> Find the first definition of TAG. The default tag is the identifier under the cursor.</p>
<dt><code>M-*</code></p>
<dd> Pop back to where you previously invoked &quot;M-.&quot;.</p>
<dt><code>C-u M-.</code></p>
<dd> Find the next definition for the last tag. </p>
</dl>
<p> For more commands, see the <i>Tags</i> topic in the Emacs info document. </p>
<h2>HOW TO USE WITH NEDIT</h2>
<p> NEdit version 5.1 and later can handle the new extended tag file format (see <code>&#8211;format</code>). To make NEdit use the tag file, select &quot;File-&gt;Load Tags File&quot;. To jump to the definition for a tag, highlight the word, then press Ctrl-D. NEdit 5.1 can can read multiple tag files from different directories. Setting the X resource nedit.tagFile to the name of a tag file instructs NEdit to automatically load that tag file at startup time. </p>
<h2>CAVEATS</h2>
<p> Because <code>ctags</code> is neither a preprocessor nor a compiler, use of preprocessor macros can fool <code>ctags</code> into either missing tags or improperly generating inappropriate tags. Although <code>ctags</code> has been designed to handle certain common cases, this is the single biggest cause of reported problems. In particular, the use of preprocessor constructs which alter the textual syntax of C can fool <code>ctags</code>. You can work around many such problems by using the <code>-I</code> option. </p>
<p> Note that since <code>ctags</code> generates patterns for locating tags (see the <code>&#8211;excmd</code> option), it is entirely possible that the wrong line may be found by your editor if there exists another source line which is identical to the line containing the tag. The following example demonstrates this condition: </p>
<dl>
<dt>
<dd> int variable; </p>
<p> /* &#8230; */<br />
 void foo(variable)<br />
 int variable;<br />
 {</p>
<dl>
<dt>
<dd> /* &#8230; */</dl>
<p> }</dl>
<p> Depending upon which editor you use and where in the code you happen to be, it is possible that the search pattern may locate the local parameter declaration in foo() before it finds the actual global variable definition, since the lines (and therefore their search patterns are identical). This can be avoided by use of the <code>&#8211;excmd</code>=<i>n</i> option. </p>
<h2>BUGS</h2>
<p> <code>Ctags</code> has more options than <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1). </p>
<p> When parsing a C++ member function definition (e.g. &quot;className::function&quot;), <code>ctags</code> cannot determine whether the scope specifier is a class name or a namespace specifier and always lists it as a class name in the scope portion of the extension fields. Also, if a C++ function is defined outside of the class declaration (the usual case), the access specification (i.e. public, protected, or private) and implementation information (e.g. virtual, pure virtual) contained in the function declaration are not known when the tag is generated for the function definition. It will, however be available for prototypes (e.g <code>&#8211;c++-kinds</code>=<i>+p</i>). </p>
<p> No qualified tags are generated for language objects inherited into a class. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CTAGS</code></p>
<dd> If this environment variable exists, it will be expected to contain a set of default options which are read when <code>ctags</code> starts, after the configuration files listed in <code>FILES</code>, below, are read, but before any command line options are read. Options appearing on the command line will override options specified in this variable. Only options will be read from this variable. Note that all white space in this variable is considered a separator, making it impossible to pass an option parameter containing an embedded space. If this is a problem, use a configuration file instead. </p>
<dt><code>ETAGS</code></p>
<dd> Similar to the <code>CTAGS</code> variable above, this variable, if found, will be read when <code>etags</code> starts. If this variable is not found, <code>etags</code> will try to use <code>CTAGS</code> instead. </p>
<dt><code>TMPDIR</code></p>
<dd> On Unix-like hosts where mkstemp() is available, the value of this variable specifies the directory in which to place temporary files. This can be useful if the size of a temporary file becomes too large to fit on the partition holding the default temporary directory defined at compilation time. <code>ctags</code> creates temporary files only if either (1) an emacs-style tag file is being generated, (2) the tag file is being sent to standard output, or (3) the program was compiled to use an internal sort algorithm to sort the tag files instead of the the sort utility of the operating system. If the sort utility of the operating system is being used, it will generally observe this variable also. Note that if <code>ctags</code> is setuid, the value of TMPDIR will be ignored. </p>
</dl>
<h2>FILES</h2>
<p> <i>/ctags.cnf (on MSDOS, MSWindows only)</i><br />
 <i>/etc/ctags.conf</i><br />
 <i>/usr/local/etc/ctags.conf</i><br />
 <i>$HOME/.ctags</i><br />
 <i>$HOME/ctags.cnf (on MSDOS, MSWindows only)</i><br />
 <i>.ctags</i><br />
 <i>ctags.cnf (on MSDOS, MSWindows only)</i></p>
<dl>
<dt>
<dd> If any of these configuration files exist, each will be expected to contain a set of default options which are read in the order listed when <code>ctags</code> starts, but before the <code>CTAGS</code> environment variable is read or any command line options are read. This makes it possible to set up site-wide, personal or project-level defaults. It is possible to compile <code>ctags</code> to read an additional configuration file before any of those shown above, which will be indicated if the output produced by the <code>&#8211;version</code> option lists the &quot;custom-conf&quot; feature. Options appearing in the <code>CTAGS</code> environment variable or on the command line will override options specified in these files. Only options will be read from these files. Note that the option files are read in line-oriented mode in which spaces are significant (since shell quoting is not possible). Each line of the file is read as one command line parameter (as if it were quoted with single quotes). Therefore, use new lines to indicate separate command-line arguments. </p>
<dt><i>tags</i></p>
<dd> The default tag file created by <code>ctags</code>.</p>
<dt><i>TAGS</i></p>
<dd> The default tag file created by <code>etags</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> The official Exuberant Ctags web site at: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://ctags.sourceforge.net">http://ctags.sourceforge.net</a></dl>
<p> Also <code><a href="/docs/linux/man/1-ex/">ex</a></code>(1), <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1), <code>elvis</code>, or, better yet, <code>vim</code>, the official editor of <code>ctags</code>. For more information on <code>vim</code>, see the VIM Pages web site at: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.vim.org/">http://www.vim.org/</a></dl>
<h2>AUTHOR</h2>
<p> Darren Hiebert &lt;dhiebert at users.sourceforge.net&gt;<br />
 <a rel="nofollow" href="http://DarrenHiebert.com/">http://DarrenHiebert.com/</a> </p>
<h2>MOTIVATION</h2>
<p> &quot;Think ye at all times of rendering some service to every member of the human race.&quot; </p>
<p> &quot;All effort and exertion put forth by man from the fullness of his heart is worship, if it is prompted by the highest motives and the will to do service to humanity.&quot; </p>
<dl>
<dt>
<dd> &#8212; From the Baha&#8217;i Writings</dl>
<h2>CREDITS</h2>
<p> This version of <code>ctags</code> was originally derived from and inspired by the ctags program by Steve Kirkendall &lt;kirkenda [at] cs.pdx.edu&gt; that comes with the Elvis vi clone (though virtually none of the original code remains). </p>
<p> Credit is also due Bram Moolenaar &lt;Bram [at] vim.org&gt;, the author of <code>vim</code>, who has devoted so much of his time and energy both to developing the editor as a service to others, and to helping the orphans of Uganda. </p>
<p> The section entitled &quot;HOW TO USE WITH GNU EMACS&quot; was shamelessly stolen from the info page for GNU <code>etags</code>. </p>
<h2>Index</h2>
