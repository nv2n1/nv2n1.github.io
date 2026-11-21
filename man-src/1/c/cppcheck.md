---
title: "cppcheck(1)"
name: "cppcheck"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cppcheck/"
description: "cppcheck – Tool for static C/C++ code analysis"
---

<h2 class="name">NAME</h2>
<p> cppcheck &#8211; Tool for static C/C++ code analysis </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cppcheck</code> [<code>&#8211;append=&lt;file&gt;</code>] [<code>&#8211;check-config</code>] [<code>&#8211;check-library</code>] [<code>-D&lt;id&gt;</code>] [<code>-U&lt;id&gt;</code>] [<code>&#8211;enable=&lt;id&gt;</code>] [<code>&#8211;error-exitcode=&lt;n&gt;</code>] [<code>&#8211;errorlist</code>] [<code>&#8211;exitcode-suppressions=&lt;file&gt;</code>] [<code>&#8211;file-list=&lt;file&gt;</code>] [<code>&#8211;force</code>] [<code>&#8211;help</code>] [<code>-I&lt;dir&gt;</code>] [<code>&#8211;includes-file=&lt;file&gt;</code>] [<code>&#8211;config-exclude=&lt;dir&gt;</code>] [<code>&#8211;config-excludes-file=&lt;file&gt;</code>] [<code>&#8211;include=&lt;file&gt;</code>] [<code>-i&lt;dir&gt;</code>] [<code>&#8211;inconclusive</code>] [<code>&#8211;inline-suppr</code>] [<code>-j&lt;jobs&gt;</code>] [<code>-l&lt;load&gt;</code>] [<code>&#8211;language=&lt;language&gt;</code>] [<code>&#8211;library=&lt;cfg&gt;</code>] [<code>&#8211;max-configs=&lt;limit&gt;</code>] [<code>&#8211;platform=&lt;type&gt;</code>] [<code>&#8211;quiet</code>] [<code>&#8211;relative-paths=&lt;paths&gt;</code>] [<code>&#8211;report-progress</code>] [<code>&#8211;rule=&lt;rule&gt;</code>] [<code>&#8211;rule-file=&lt;file&gt;</code>] [<code>&#8211;std=&lt;id&gt;</code>] [<code>&#8211;suppress=&lt;spec&gt;</code>] [<code>&#8211;suppressions-list=&lt;file&gt;</code>] [<code>&#8211;template='&lt;text&gt;&#8217;</code>] [<code>&#8211;verbose</code>] [<code>&#8211;version</code>] [<code>&#8211;xml</code>] [<code>&#8211;xml-version=&lt;version&gt;]</code>] [<code>file or path</code>] <code>&#8230;</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>Cppcheck is a command-line tool that tries to detect bugs that your C/C++ compiler doesn&#8217;t see. It is versatile, and can check non-standard code including various compiler extensions, inline assembly code, etc. Its internal preprocessor can handle includes, macros, and several preprocessor commands. While Cppcheck is highly configurable, you can start using it just by giving it a path to the source code.</dd>
<h2>OPTIONS</h2>
<p> Analyze given C/C++ files for common errors. </p>
<p> <code>&#8211;append=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> This allows you to provide information about functions by providing an implementation for these.</dd></dl>
<p> <code>&#8211;check-config</code></p>
<dl>
<dt>
</dt><dd> Check Cppcheck configuration. The normal code analysis is disabled by this flag.</dd></dl>
<p> <code>&#8211;check-library</code></p>
<dl>
<dt>
</dt><dd> Show information messages when library files have incomplete info.</dd></dl>
<p> <code>-D&lt;id&gt;</code></p>
<dl>
<dt>
</dt><dd> By default Cppcheck checks all configurations. Use -D to limit the checking. When -D is used the checking is limited to the given configuration. Example: -DDEBUG=1 -D__cplusplus</dd></dl>
<p> <code>-U&lt;id&gt;</code></p>
<dl>
<dt>
</dt><dd> By default Cppcheck checks all configurations. Use &#8216;-U&#8217; to explicitly hide certain #ifdef &lt;id&gt; code paths from checking. Example: &#8216;-UDEBUG&#8217;</dd></dl>
<p> <code>&#8211;enable=&lt;id&gt;</code></p>
<dl>
<dt>
</dt><dd> Enable additional checks. The available ids are: </dd>
<p> all</p>
<dl>
<dt>
</dt><dd> Enable all checks. It is recommended to only use &#8211;enable=all when the whole program is scanned, because this enables unusedFunction.</dd></dl>
<p> warning</p>
<dl>
<dt>
</dt><dd> Enable warning messages</dd></dl>
<p> style</p>
<dl>
<dt>
</dt><dd> Enable all coding style checks. All messages with the severities &#8216;style&#8217;, &#8216;performance&#8217; and &#8216;portability&#8217; are enabled.</dd></dl>
<p> performance</p>
<dl>
<dt>
</dt><dd> Enable performance messages</dd></dl>
<p> portability</p>
<dl>
<dt>
</dt><dd> Enable portability messages</dd></dl>
<p> information</p>
<dl>
<dt>
</dt><dd> Enable information messages</dd></dl>
<p> unusedFunction</p>
<dl>
<dt>
</dt><dd> Check for unused functions. It is recommend to only enable this when the whole program is scanned</dd></dl>
<p> missingInclude</p>
<dl>
<dt>
</dt><dd> Warn if there are missing includes. For detailed information use &#8211;check-config</dd></dl>
<p> By default none of the additional checks are enabled. Several ids can be given if you separate them with commas, e.g. &#8211;enable=style,unusedFunction. See also &#8211;std</dl>
<p> <code>&#8211;error-exitcode=&lt;n&gt;</code></p>
<dl>
<dt>
</dt><dd> If errors are found, integer &lt;n&gt; is returned instead of default 0. EXIT_FAILURE is returned if arguments are not valid or if no input files are provided. Note that your operating system can modify this value, e.g. 256 can become 0.</dd></dl>
<p> <code>&#8211;errorlist</code></p>
<dl>
<dt>
</dt><dd> Print a list of all possible error messages in XML format.</dd></dl>
<p> <code>&#8211;exitcode-suppressions=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Used when certain messages should be displayed but should not cause a non-zero exitcode.</dd></dl>
<p> <code>&#8211;file-list=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Specify the files to check in a text file. One filename per line. When file is -, the file list will be read from standard input.</dd></dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
</dt><dd> Force checking of files that have a lot of configurations. Error is printed if such a file is found so there is no reason to use this by default. If used together with &#8211;max-configs=, the last option is the one that is effective.</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print help text.</dd></dl>
<p> <code>-I &lt;dir&gt;</code></p>
<dl>
<dt>
</dt><dd> Give path to search for include files. Give several -I parameters to give several paths. First given path is searched for contained header files first. If paths are relative to source files, this is not needed.</dd></dl>
<p> <code>&#8211;includes-file=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Specify directory paths to search for included header files in a text file. Add one include path per line. First given path is searched for contained header files first. If paths are relative to source files, this is not needed.</dd></dl>
<p> <code>&#8211;config-exclude=&lt;dir&gt;</code></p>
<dl>
<dt>
</dt><dd> Path (prefix) to be excluded from configuration checking. Preprocessor configurations defined in headers (but not sources) matching the prefix will not be considered for evaluation of configuration alternatives.</dd></dl>
<p> <code>&#8211;config-exclude-file=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> A file that contains a list of config-excludes.</dd></dl>
<p> <code>&#8211;include=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Force inclusion of a file before the checked file. Can be used for example when checking the Linux kernel, where autoconf.h needs to be included for every file compiled. Works the same way as the GCC -include option.</dd></dl>
<p> <code>-i &lt;dir&gt;</code></p>
<dl>
<dt>
</dt><dd> Give path to ignore. Give several -i parameters to ignore several paths. Give directory name or filename with path as parameter. Directory name is matched to all parts of the path.</dd></dl>
<p> <code>&#8211;inconclusive</code></p>
<dl>
<dt>
</dt><dd> Allow that Cppcheck reports even though the analysis is inconclusive. There are false positives with this option. Each result must be carefully investigated before you know if it is good or bad.</dd></dl>
<p> <code>&#8211;inline-suppr</code></p>
<dl>
<dt>
</dt><dd> Enable inline suppressions. Use them by placing comments in the form: // cppcheck-suppress memleak before the line to suppress.</dd></dl>
<p> <code>-j &lt;jobs&gt;</code></p>
<dl>
<dt>
</dt><dd> Start &lt;jobs&gt; threads to do the checking work.</dd></dl>
<p> <code>-l &lt;load&gt;</code></p>
<dl>
<dt>
</dt><dd> Specifies that no new threads should be started if there are other threads running and the load average is at least &lt;load&gt; (ignored on non UNIX-like systems)</dd></dl>
<p> <code>&#8211;language=&lt;language&gt;</code></p>
<dl>
<dt>
</dt><dd> Forces cppcheck to check all files as the given language. Valid values are: c, c++</dd></dl>
<p> <code>&#8211;library=&lt;cfg&gt;</code></p>
<dl>
<dt>
</dt><dd> Use library configuration.</dd></dl>
<p> <code>&#8211;max-configs=&lt;limit&gt;</code></p>
<dl>
<dt>
</dt><dd> Maximum number of configurations to check in a file before skipping it. Default is 12. If used together with &#8211;force, the last option is the one that is effective.</dd></dl>
<p> <code>&#8211;platform=&lt;type&gt;</code></p>
<dl>
<dt>
</dt><dd> Specifies platform specific types and sizes.The available platforms are: </dd>
<p> unix32</p>
<dl>
<dt>
</dt><dd> 32 bit unix variant</dd></dl>
<p> unix64</p>
<dl>
<dt>
</dt><dd> 64 bit unix variant</dd></dl>
<p> win32A</p>
<dl>
<dt>
</dt><dd> 32 bit Windows ASCII character encoding</dd></dl>
<p> win32W</p>
<dl>
<dt>
</dt><dd> 32 bit Windows UNICODE character encoding</dd></dl>
<p> win64</p>
<dl>
<dt>
</dt><dd> 64 bit Windows</dd></dl>
<p> By default the platform which was used to compile Cppcheck is used.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
</dt><dd> Only print something when there is an error.</dd></dl>
<p> <code>-rp</code>, <code>-rp=&lt;paths&gt;</code>, <code>&#8211;relative-paths;</code>, <code>&#8211;relative-paths=&lt;paths&gt;</code></p>
<dl>
<dt>
</dt><dd> Use relative paths in output. When given, &lt;paths&gt; are used as base. You can separate multiple paths by &#8216;;&#8217;. Otherwise path where source files are searched is used. E.g. if given value is test, when checking test/test.cpp, the path in output will be test.cpp instead of test/test.cpp. The feature uses string comparison to create relative paths, so using e.g. ~ for home folder does not work. It is currently only possible to apply the base paths to files that are on a lower level in the directory tree.</dd></dl>
<p> <code>&#8211;report-progress</code></p>
<dl>
<dt>
</dt><dd> Report progress when checking a file.</dd></dl>
<p> <code>&#8211;rule=&lt;rule&gt;</code></p>
<dl>
<dt>
</dt><dd> Match regular expression to create your own checks. E.g. rule &quot;/ 0&quot; can be used to check division by zero. This command is only available if cppcheck was compiled with HAVE_RULES=yes.</dd></dl>
<p> <code>&#8211;rule-file=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Use given rule XML file. See <a rel="nofollow" href="https://sourceforge.net/projects/cppcheck/files/Articles/">https://sourceforge.net/projects/cppcheck/files/Articles/</a> for more info about the syntax. This command is only available if cppcheck was compiled with HAVE_RULES=yes.</dd></dl>
<p> <code>&#8211;std=&lt;id&gt;</code></p>
<dl>
<dt>
</dt><dd> Set standard. The available options are: </dd>
<p> posix</p>
<dl>
<dt>
</dt><dd> POSIX compatible code</dd></dl>
<p> c89</p>
<dl>
<dt>
</dt><dd> C code is C89 compatible</dd></dl>
<p> c99</p>
<dl>
<dt>
</dt><dd> C code is C99 compatible</dd></dl>
<p> c11</p>
<dl>
<dt>
</dt><dd> C code is C11 compatible (default)</dd></dl>
<p> c++03</p>
<dl>
<dt>
</dt><dd> C++ code is C++03 compatible</dd></dl>
<p> c++11</p>
<dl>
<dt>
</dt><dd> C++ code is C++11 compatible (default)</dd></dl>
<p> Example to set more than one standards: &#8216;cppcheck &#8211;std=c99 &#8211;std=posix file.cpp&#8217;</dl>
<p> <code>&#8211;suppress=&lt;spec&gt;</code></p>
<dl>
<dt>
</dt><dd> Suppress a specific warning. The format of &lt;spec&gt; is: [error id]:[filename]:[line]. The [filename] and [line] are optional. [error id] may be * to suppress all warnings (for a specified file or files). [filename] may contain the wildcard characters * or ?.</dd></dl>
<p> <code>&#8211;suppressions-list=&lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Suppress warnings listed in the file. Each suppression is in the format of &lt;spec&gt; above.</dd></dl>
<p> <code>&#8211;template='&lt;text&gt;&#8217;</code></p>
<dl>
<dt>
</dt><dd> Format the error messages. E.g. &#8216;{file}:{line},{severity},{id},{message}&#8217; or &#8216;{file}({line}):({severity}) {message}&#8217;. Pre-defined templates: gcc, vs</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> More detailed error reports</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print out version information</dd></dl>
<p> <code>&#8211;xml</code></p>
<dl>
<dt>
</dt><dd> Write results in XML to error stream</dd></dl>
<p> <code>&#8211;xml-version=&lt;version&gt;</code></p>
<dl>
<dt>
</dt><dd> Select the XML file version. Currently versions 1 and 2 are available. The default version is 1.</dd></dl>
<h2>AUTHOR</h2>
<p> The program was written by Daniel Marjam&auml;ki and Cppcheck team. See AUTHORS file for list of team members.</p>
<h2>SEE ALSO</h2>
<p> Full list of features: <a rel="nofollow" href="http://cppcheck.wiki.sourceforge.net/">http://cppcheck.wiki.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> <code>Reijo Tomperi</code> &lt;aggro80 [at] users.sourceforge.net&gt;</p>
<dl>
<dt>
</dt><dd> Wrote this manpage for the Debian system.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 &#8211; 2016 Reijo Tomperi </p>
<p> This manual page was written for the Debian system (but may be used by others). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 or (at your option) any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-3. </p>
