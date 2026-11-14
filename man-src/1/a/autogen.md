---
title: "autogen(1)"
name: "autogen"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autogen/"
description: "autogen – The Automated Program Generator"
---

<h2 class="name">NAME</h2>
<p> autogen &#8211; The Automated Program Generator </p>
<h2>SYNOPSIS</h2>
<p> <code>autogen</code> [<code>&#8211;</code><i>flag</i> [<i>value</i>]]&#8230; [<code>&#8212;</code><i>opt-name</i>[[=| ]<i>value</i>]]&#8230;[ &lt;def-file&gt; ] </p>
<p> AutoGen creates text files from templates using external definitions.</p>
<h2>DESCRIPTION</h2>
<p> <code>AutoGen</code> is designed for generating program files that contain repetitive text with varied substitutions. The goal is to simplify the maintenance of programs that contain large amounts of repetitious text. This is especially valuable if there are several blocks of such text that must be kept synchronized. </p>
<p> One common example is the problem of maintaining the code required for processing program options. Processing options requires a minimum of four different constructs be kept in proper order in different places in your program. You need at least: The flag character in the flag string, code to process the flag when it is encountered, a global state variable or two, and a line in the usage text. You will need more things besides this if you choose to implement long option names, configuration file processing, environment variables and so on. </p>
<p> All of this can be done mechanically; with the proper templates and this program.</p>
<h2>OPTIONS</h2>
<h3>The following options select definitions, templates and scheme functions to use</h3>
<dl>
<dt><code>-L</code> <i>dir</i>, <code>&#8211;templ-dirs</code>=<i>dir</i></p>
<dd> Search for templates in <i>DIR</i>. This option may appear an unlimited number of times. </p>
<p> Add a directory to the list of directories <code>autogen</code> searches when opening a template, either as the primary template or an included one. The last entry has the highest priority in the search list. That is to say, they are searched in reverse order.</p>
<dt><code>-T</code> <i>tpl-file</i>, <code>&#8211;override-tpl</code>=<i>tpl-file</i></p>
<dd> Use <i>TPL-FILE</i> for the template. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> Definition files specify the standard template that is to be expanded. This option will override that name and expand a different template.</p>
<dt><code>-l</code> <i>tpl-file</i>, <code>&#8211;lib-template</code>=<i>tpl-file</i></p>
<dd> Load AutoGen macros from <i>TPL-FILE</i>. This option may appear an unlimited number of times. </p>
<p> DEFINE macros are saved from this template file for use in processing the main macro file. Template text aside from the DEFINE macros is is ignored. </p>
<p> Do not use this. Instead, use the INCLUDE macro in your template. </p>
<p> <code>NOTE: THIS OPTION IS DEPRECATED</code></p>
<dt><code>&#8211;definitions</code>=<i>file</i>,<code> &#8211;no-definitions</code></p>
<dd> Read definitions from <i>FILE</i>. The <i>no-definitions</i> form will disable the option. This option is enabled by default. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> Use this argument to specify the input definitions file with a command line option. If you do not specify this option, then there must be a command line argument that specifies the file, even if only to specify stdin with a hyphen (<code>&#8211;</code>). Specify, <code>&#8211;no-definitions</code> when you wish to process a template without any active AutoGen definitions.</p>
<dt><code>&#8211;shell</code>=<i>shell</i></p>
<dd> name or path name of shell to use. </p>
<p> By default, when AutoGen is built, the configuration is probed for a reasonable Bourne-like shell to use for shell script processing. If a particular template needs an alternate shell, it must be specified with this option on the command line, with an environment variable (<code>SHELL</code>) or in the configuration/initialization file.</p>
<dt><code>-m</code>, <code>&#8211;no-fmemopen</code></p>
<dd> Do not use in-mem streams. </p>
<p> If the local C library supports &quot;<code><a href="//www.systutorials.com/docs/linux/man/3GNU-fopencookie/">fopencookie</a>(3GNU)</code>&quot;, or &quot;<code><a href="//www.systutorials.com/docs/linux/man/3BSD-funopen/">funopen</a>(3BSD)</code>&quot; then AutoGen prefers to use in-memory stream buffer opens instead of anonymous files. This may lead to problems if there is a shortage of virtual memory. If, for a particular application, you run out of memory, then specify this option. This is unlikely in a modern 64-bit virtual memory environment. </p>
<p> On platforms without these functions, the option is accepted but ignored. <code>fmemopen(POSIX)</code> is not adequate because its string buffer is not reallocatable. <code>open_memstream(POSIX)</code> is <i>also</i> not adequate because the stream is only opened for output. AutoGen needs a reallocatable buffer available for both reading and writing.</p>
<dt><code>&#8211;equate</code>=<i>char-list</i></p>
<dd> characters considered equivalent. The default <i>char-list</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>_-^ </p>
<p> This option will alter the list of characters considered equivalent. The default are the three characters, &quot;_-^&quot;. (The last is conventional on a Tandem/HP-NonStop, and I used to do a lot of work on Tandems.)</dl>
<h3>The following options modify how output is handled</h3>
<dl>
<dt><code>-b</code> <i>name</i>, <code>&#8211;base-name</code>=<i>name</i></p>
<dd> Specify <code>NAME</code> as the base name for output. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> A template may specify the exact name of the output file. Normally, it does not. Instead, the name is composed of the base name of the definitions file with suffixes appended. This option will override the base name derived from the definitions file name. This is required if there is no definitions file and advisable if definitions are being read from stdin. If the definitions are being read from standard in, the base name defaults to <i>stdin</i>. Any leading directory components in the name will be silently removed. If you wish the output file to appear in a particular directory, it is recommended that you &quot;cd&quot; into that directory first, or use directory names in the format specification for the output suffix lists, see: pseudo macro.</p>
<dt><code>&#8211;source-time,</code> <code>&#8211;no-source-time</code></p>
<dd> set mod times to latest source. The <i>no-source-time</i> form will disable the option. </p>
<p> If you stamp your output files with the <code>DNE</code> macro output, then your output files will always be different, even if the content has not really changed. If you use this option, then the modification time of the output files will change only if the input files change. This will help reduce unneeded builds.</p>
<dt><code>&#8211;writable,</code> <code>&#8211;not-writable</code></p>
<dd> Allow output files to be writable. The <i>not-writable</i> form will disable the option. </p>
<p> This option will leave output files writable. Normally, output files are read-only.</dl>
<h3>The following options are often useful while debugging new templates</h3>
<p> They specify limits that prevent the template from taking overly long or producing more output than expected.</p>
<dl>
<dt><code>&#8211;loop-limit</code>=<i>lim</i></p>
<dd> Limit on increment loops. This option takes an integer number as its argument. The value of <i>lim</i> is constrained to being: </p>
<pre>
exactly -1, or
in the range  1 through 0x1000000
</pre>
<p> The default <i>lim</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>256 </p>
<p> This option prevents runaway loops. For example, if you accidentally specify, &quot;FOR x (for-from 1) (for-to -1) (for-by 1)&quot;, it will take a long time to finish. If you do have more than 256 entries in tables, you will need to specify a new limit with this option.</p>
<dt><code>-t</code> <i>seconds</i>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> Limit server shell operations to <code>SECONDS</code>. This option takes an integer number as its argument. The value of <i>seconds</i> is constrained to being: </p>
<pre>
in the range  0 through 3600
</pre>
<p> AutoGen works with a shell server process. Most normal commands will complete in less than 10 seconds. If, however, your commands need more time than this, use this option. </p>
<p> The valid range is 0 to 3600 seconds (1 hour). Zero will disable the server time limit.</p>
<dt><code>&#8211;trace</code>=<i>level</i></p>
<dd> tracing level of detail. This option takes a keyword as its argument. The argument sets an enumeration value that can be tested by comparing them against the option value macro. The available keywords are: </p>
<pre>
nothing       debug-message server-shell
templates     block-macros  expressions
everything
</pre>
<p> or their numeric equivalent. </p>
<p> The default <i>level</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>nothing </p>
<p> This option will cause AutoGen to display a trace of its template processing. There are six levels, each level including messages from the previous levels: </p>
<p> <i>nothing</i> Does no tracing at all (default) </p>
<p> <i>debug-message</i> Print messages from the &quot;DEBUG&quot; AutoGen macro (see: DEBUG). </p>
<p> <i>server-shell</i> Traces all input and output to the server shell. This includes a shell &quot;independent&quot; initialization script about 30 lines long. Its output is discarded and not inserted into any template. </p>
<p> <i>templates</i> Traces the invocation of <code>DEFINE</code>d macros and <code>INCLUDE</code>s </p>
<p> <i>block-macros</i> Traces all block macros. The above, plus <code>IF</code>, <code>FOR</code>, <code>CASE</code> and <code>WHILE</code>. </p>
<p> <i>expressions</i> Displays the results of expression evaluations. </p>
<p> <i>everything</i> Displays the invocation of every AutoGen macro, even <code>TEXT</code> macros (i.e. the text outside of macro quotes). Additionally, if you rebuild the &#8220;expr.ini&#8221; file with debugging enabled, then all calls to AutoGen defined scheme functions will also get logged: </p>
<pre>
    cd ${top_builddir}/agen5
    DEBUG_ENABLED=true bash bootstrap.dir expr.ini
    make CFLAGS='-g -DDEBUG_ENABLED=1'
</pre>
<p> Be aware that you cannot rebuild this source in this way without first having installed the <code>autogen</code> executable in your search path. Because of this, &quot;expr.ini&quot; is in the distributed source list, and not in the dependencies. </p>
<dt><code>&#8211;trace-out</code>=<i>file</i></p>
<dd> tracing output file or filter. </p>
<p> The output specified may be a file name, a file that is appended to, or, if the option argument begins with the <code>pipe</code> operator (<code>|</code>), a command that will receive the tracing output as standard in. For example, <code>&#8211;traceout=&#8217;| less&#8217;</code> will run the trace output through the <code>less</code> program. Appending to a file is specified by preceeding the file name with two greater-than characters (<code>&gt;&gt;</code>).</p>
<dt><code>&#8211;show-defs</code></p>
<dd> Show the definition tree. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> This will print out the complete definition tree before processing the template.</p>
<dt><code>&#8211;used-defines</code></p>
<dd> Show the definitions used. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> This will print out the names of definition values searched for during the processing of the template, whether actually found or not. There may be other referenced definitions in a template in portions of the template not evaluated. Some of the names listed may be computed names and others AutoGen macro arguments. This is not a means for producing a definitive, all-encompassing list of all and only the values used from a definition file. This is intended as an aid to template documentation only.</p>
<dt><code>-C</code>, <code>&#8211;core</code></p>
<dd> Leave a core dump on a failure exit. </p>
<p> Many systems default to a zero sized core limit. If the system has the sys/resource.h header and if this option is supplied, then in the failure exit path, autogen will attempt to set the soft core limit to whatever the hard core limit is. If that does not work, then an administrator must raise the hard core size limit.</dl>
<h3>These options can be used to control what gets processed</h3>
<p> in the definitions files and template files&quot; They specify which outputs and parts of outputs to produce.</p>
<dl>
<dt><code>-s</code> <i>suffix</i>, <code>&#8211;skip-suffix</code>=<i>suffix</i></p>
<dd> Skip the file with this <i>SUFFIX</i>. This option may appear an unlimited number of times. This option may not be preset with environment variables or in initialization (rc) files. This option must not appear in combination with any of the following options: select-suffix. </p>
<p> Occasionally, it may not be desirable to produce all of the output files specified in the template. (For example, only the <i>.h</i> header file, but not the <i>.c</i> program text.) To do this specify <code>&#8211;skip-suffix=c</code> on the command line.</p>
<dt><code>-o</code> <i>suffix</i>, <code>&#8211;select-suffix</code>=<i>suffix</i></p>
<dd> specify this output suffix. This option may appear an unlimited number of times. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> If you wish to override the suffix specifications in the template, you can use one or more copies of this option. See the suffix specification in the @ref{pseudo macro} section of the info doc.</p>
<dt><code>-D</code> <i>value</i>, <code>&#8211;define</code>=<i>value</i></p>
<dd> name to add to definition list. This option may appear an unlimited number of times. </p>
<p> The AutoGen define names are used for the following purposes: </p>
<p> Sections of the AutoGen definitions may be enabled or disabled by using C-style #ifdef and #ifndef directives. </p>
<p> When defining a value for a name, you may specify the index for a particular value. That index may be a literal value, a define option or a value #define-d in the definitions themselves. </p>
<p> The name of a file may be prefixed with <code>$NAME/</code>. The <code>$NAME</code> part of the name string will be replaced with the define-d value for <code>NAME</code>. </p>
<p> When AutoGen is finished loading the definitions, the defined values are exported to the environment with, <code><a href="/docs/linux/man/3-putenv/">putenv</a>(3)</code>. These values can then be used in shell scripts with <code>${NAME@</code>} references and in templates with <code>(getenv &quot;NAME&quot;)</code>. </p>
<p> While processing a template, you may specify an index to retrieve a specific value. That index may also be a define-d value. </p>
<p> It is entirely equivalent to place this name in the exported environment. Internally, that is what AutoGen actually does with this option.</p>
<dt><code>-U</code> <i>name-pat</i>, <code>&#8211;undefine</code>=<i>name-pat</i></p>
<dd> definition list removal pattern. This option may appear an unlimited number of times. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> Similar to &#8216;C&#8217;, AutoGen uses <code>#ifdef/#ifndef</code> preprocessing directives. This option will cause the matching names to be removed from the list of defined values.</dl>
<h3>This option is used to automate dependency tracking</h3>
<dl>
<dt><code>-M</code> <i>type</i>, <code>&#8211;make-dep</code>[<code>=</code><i>type</i>]</p>
<dd> emit make dependency file. This option may appear an unlimited number of times. This option may not be preset with environment variables or in initialization (rc) files. </p>
<p> This option behaves fairly closely to the way the <code>-M</code> series of options work with the gcc compiler, except that instead of just emitting the predecessor dependencies, this also emits the successor dependencies (output target files). By default, the output dependency information will be placed in <code>&lt;base-name&gt;.d</code>, but may also be specified with <code>-MF&lt;file&gt;</code>. The time stamp on this file will be manipulated so that it will be one second older than the oldest primary output file. </p>
<p> The target in this dependency file will normally be the dependency file name, but may also be overridden with <code>-MT&lt;targ-name&gt;</code>. AutoGen will not alter the contents of that file, but it may create it and it will adjust the modification time to match the start time. </p>
<p> <code>NB:</code> these second letters are part of the option argument, so <code>-MF &lt;file&gt;</code> must have the space character quoted or omitted, and <code>-M &quot;F &lt;file&gt;&quot;</code> is acceptable because the <code>F</code> is part of the option argument. </p>
<p> <code>-M</code> may be followed by any of the letters M, F, P, T, Q, D, or G. However, only F, Q, T and P are meaningful. All but F have somewhat different meanings. <code>-MT&lt;name&gt;</code> is interpreted as meaning <code>&lt;name&gt;</code> is a sentinel file that will depend on all inputs (templates and definition files) and all the output files will depend on this sentinel file. It is suitable for use as a real make target. Q is treated identically to T, except dollar characters (&#8216;$&#8217;) are doubled. P causes a special clean (clobber) phoney rule to be inserted into the make file fragment. An empty rule is always created for building the list of targets. </p>
<p> This is the recommended usage: </p>
<pre>
      -MFwhatever-you-like.dep -MTyour-sentinel-file -MP
</pre>
<p> and then in your <code>Makefile</code>, make the <i>autogen</i> rule: </p>
<pre>
      -include whatever-you-like.dep
      clean_targets += clean-your-sentinel-file
    .sp
      your-sentinel-file:
          autogen -MT$@@ -MF$*.d .....
    .sp
      local-clean :
          rm -f $(clean_targets)
</pre>
<p> The modification time on the dependency file is adjusted to be one second before the earliest time stamp of any other output file. Consequently, it is suitable for use as the sentinel file testifying to the fact the program was successfully run. (<code>-include</code> is the GNU make way of specifying &quot;include it if it exists&quot;. Your make must support that feature or your bootstrap process must create the file.) </p>
<p> All of this may also be specified using the <code>DEPENDENCIES_OUTPUT</code> or <code>AUTOGEN_MAKE_DEP</code> environment variables. If defined, dependency information will be output. If defined with white space free text that is something other than <code>true</code>, <code>false</code>, <code>yes</code>, <code>no</code>, <code>0</code> or <code>1</code>, then the string is taken to be an output file name. If it contains a string of white space characters, the first token is as above and the second token is taken to be the target (sentinel) file as <code>-MT</code> in the paragraphs above. <code>DEPENDENCIES_OUTPUT</code> will be ignored if there are multiple sequences of white space characters or if its contents are, specifically, <code>false</code>, <code>no</code> or <code>0</code>.</dl>
<h3>help, version and option handling</h3>
<dl>
<dt><code>-?</code>,<code> &#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-!</code>,<code> &#8211;more-help</code></p>
<dd> Pass the extended usage information through a pager.</p>
<dt><code>-&gt;</code> [<i>cfgfile</i>],<code> &#8211;save-opts</code>[=<i>cfgfile</i>]</p>
<dd> Save the option state to <i>cfgfile</i>. The default is the <i>last</i> configuration file listed in the <code>OPTION PRESETS</code> section, below. The command will exit after updating the config file.</p>
<dt><code>-&lt;</code> <i>cfgfile</i>,<code> &#8211;load-opts</code>=<i>cfgfile</i>,<code> &#8211;no-load-opts</code></p>
<dd> Load options from <i>cfgfile</i>. The <i>no-load-opts</i> form will disable the loading of earlier config/rc/ini files. <i>&#8211;no-load-opts</i> is handled early, out of order.</p>
<dt><code>-v</code> [{<i>v|c|n</i>}],<code> &#8211;version</code>[={<i>v|c|n</i>}]</p>
<dd> Output version of program and exit. The default mode is `v&#8217;, a simple version. The `c&#8217; mode will print copyright information and `n&#8217; will print the full copyright notice.</dl>
<h2>OPTION PRESETS</h2>
<p> Any option that is not marked as <i>not presettable</i> may be preset by loading values from configuration (&quot;RC&quot; or &quot;.INI&quot;) file(s) and values from environment variables named: </p>
<pre>
  <code>AUTOGEN_&lt;option-name&gt;</code> or <code>AUTOGEN</code>
</pre>
<p> The environmental presets take precedence (are processed later than) the configuration files. The <i>homerc</i> files are &quot;<i>$HOME</i>&quot;, and &quot;<i>.</i>&quot;. If any of these are directories, then the file <i>.autogenrc</i> is searched for within those directories.</p>
<h2>ENVIRONMENT</h2>
<p> See <code>OPTION PRESETS</code> for configuration environment variables.</p>
<h2>FILES</h2>
<p> See <code>OPTION PRESETS</code> for configuration files.</p>
<h2>EXAMPLES</h2>
<p> Here is how the man page is produced: </p>
<pre>
autogen -Tagman-cmd.tpl -MFman-dep -MTstamp-man opts.def
</pre>
<p> This command produced this man page from the AutoGen option definition file. It overrides the template specified in <i>opts.def</i> (normally <i>options.tpl</i>) and uses <i>agman-cmd.tpl</i>. It also sets the make file dependency output to <i>man-dep</i> and the sentinel file (time stamp file) to <i>man-stamp</i>. The base of the file name is derived from the defined <code>prog-name</code>. </p>
<p> The texi invocation document is produced via: </p>
<pre>
autogen -Tagtexi-cmd.tpl -MFtexi-dep -MTtexi-stamp opts.def
</pre>
<h2>EXIT STATUS</h2>
<p> One of the following exit values will be returned:</p>
<dl>
<dt><code>0</code> (EXIT_SUCCESS)</p>
<dd> Successful program execution.</p>
<dt><code>1</code> (EXIT_OPTION_ERROR)</p>
<dd> The command options were misconfigured.</p>
<dt><code>2</code> (EXIT_BAD_TEMPLATE)</p>
<dd> An error was encountered processing the template.</p>
<dt><code>3</code> (EXIT_BAD_DEFINITIONS)</p>
<dd> The definitions could not be deciphered.</p>
<dt><code>4</code> (EXIT_LOAD_ERROR)</p>
<dd> An error was encountered during the load phase.</p>
<dt><code>128</code> (EXIT_SIGNAL)</p>
<dd> <code>autogen</code> exited due to catching a signal. If your template includes string formatting, a number argument to a &quot;%s&quot; formatting element will trigger a segmentation fault. Autogen will catch the seg fault signal and exit with <code><a href="/docs/linux/man/5-autogen_exit_signal/">AUTOGEN_EXIT_SIGNAL</a>(5)</code>. Alternatively, AutoGen may have been interrupted with a <code><a href="/docs/linux/man/2-kill/">kill</a>(2)</code> signal. Subtract 128 from the actual exit code to detect the signal number.</p>
<dt><code>66</code> (EX_NOINPUT)</p>
<dd> A specified configuration file could not be loaded.</p>
<dt><code>70</code> (EX_SOFTWARE)</p>
<dd> libopts had an internal operational error. Please report it to autogen-users [at] lists.sourceforge.net. Thank you.</dl>
<h2>AUTHORS</h2>
<p> Bruce Korb</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1992-2013 Bruce Korb all rights reserved. This program is released under the terms of the GNU General Public License, version 3 or later.</p>
<h2>BUGS</h2>
<p> Please send bug reports to: autogen-users [at] lists.sourceforge.net</p>
<h2>NOTES</h2>
<p> This manual page was <i>AutoGen</i>-erated from the <code>autogen</code> option definitions. </p>
<h2>Index</h2>
