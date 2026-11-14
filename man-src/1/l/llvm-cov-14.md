---
title: "llvm-cov-14(1)"
name: "llvm-cov-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-cov-14/"
description: "llvm-cov – emit coverage information"
---

<h2 class="name">NAME</h2>
<p> llvm-cov &#8211; emit coverage information </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-cov</code> <i>command</i> [<i>args…</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-cov</code> tool shows code coverage information for programs that are instrumented to emit profile data. It can be used to work with <code>gcov</code>-style coverage or with <code>clang</code>&#8216;s instrumentation based profiling. </p>
<p> If the program is invoked with a base name of <code>gcov</code>, it will behave as if the <code>llvm-cov gcov</code> command were called. Otherwise, a command should be provided.</p>
<h2>COMMANDS</h2>
<dl>
<dt>&bull;</p>
<dd> <i>gcov</i></p>
<dt>&bull;</p>
<dd> <i>show</i></p>
<dt>&bull;</p>
<dd> <i>report</i></p>
<dt>&bull;</p>
<dd> <i>export</i></dl>
<h2>GCOV COMMAND</h2>
<h3>SYNOPSIS</h3>
<p> <code>llvm-cov gcov</code> [<i>options</i>] <i>SOURCEFILE</i></p>
<h3>DESCRIPTION</h3>
<p> The <code>llvm-cov gcov</code> tool reads code coverage data files and displays the coverage information for a specified source file. It is compatible with the <code>gcov</code> tool from version 4.2 of <code>GCC</code> and may also be compatible with some later versions of <code>gcov</code>. </p>
<p> To use <code>llvm-cov gcov</code>, you must first build an instrumented version of your application that collects coverage data as it runs. Compile with the <code>-fprofile-arcs</code> and <code>-ftest-coverage</code> options to add the instrumentation. (Alternatively, you can use the <code>&#8211;coverage</code> option, which includes both of those other options.) </p>
<p> At the time you compile the instrumented code, a <code>.gcno</code> data file will be generated for each object file. These <code>.gcno</code> files contain half of the coverage data. The other half of the data comes from <code>.gcda</code> files that are generated when you run the instrumented program, with a separate <code>.gcda</code> file for each object file. Each time you run the program, the execution counts are summed into any existing <code>.gcda</code> files, so be sure to remove any old files if you do not want their contents to be included. </p>
<p> By default, the <code>.gcda</code> files are written into the same directory as the object files, but you can override that by setting the <code>GCOV_PREFIX</code> and <code>GCOV_PREFIX_STRIP</code> environment variables. The <code>GCOV_PREFIX_STRIP</code> variable specifies a number of directory components to be removed from the start of the absolute path to the object file directory. After stripping those directories, the prefix from the <code>GCOV_PREFIX</code> variable is added. These environment variables allow you to run the instrumented program on a machine where the original object file directories are not accessible, but you will then need to copy the <code>.gcda</code> files back to the object file directories where <code>llvm-cov gcov</code> expects to find them. </p>
<p> Once you have generated the coverage data files, run <code>llvm-cov gcov</code> for each main source file where you want to examine the coverage results. This should be run from the same directory where you previously ran the compiler. The results for the specified source file are written to a file named by appending a <code>.gcov</code> suffix. A separate output file is also created for each file included by the main source file, also with a <code>.gcov</code> suffix added. </p>
<p> The basic content of an <code>.gcov</code> output file is a copy of the source file with an execution count and line number prepended to every line. The execution count is shown as <code>&#8211;</code> if a line does not contain any executable code. If a line contains code but that code was never executed, the count is displayed as <code>#####</code>.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-a, &#8211;all-blocks</code></p>
<dd> Display all basic blocks. If there are multiple blocks for a single line of source code, this option causes llvm-cov to show the count for each block instead of just one count for the entire line.</p>
<dt><code>-b, &#8211;branch-probabilities</code></p>
<dd> Display conditional branch probabilities and a summary of branch information.</p>
<dt><code>-c, &#8211;branch-counts</code></p>
<dd> Display branch counts instead of probabilities (requires -b).</p>
<dt><code>-m, &#8211;demangled-names</code></p>
<dd> Demangle function names.</p>
<dt><code>-f, &#8211;function-summaries</code></p>
<dd> Show a summary of coverage for each function instead of just one summary for an entire source file.</p>
<dt><code>&#8211;help</code></p>
<dd> Display available options (–help-hidden for more).</p>
<dt><code>-l, &#8211;long-file-names</code></p>
<dd> For coverage output of files included from the main source file, add the main file name followed by <code>##</code> as a prefix to the output file names. This can be combined with the –preserve-paths option to use complete paths for both the main file and the included file.</p>
<dt><code>-n, &#8211;no-output</code></p>
<dd> Do not output any <code>.gcov</code> files. Summary information is still displayed.</p>
<dt><code>-o=&lt;DIR|FILE&gt;, &#8211;object-directory=&lt;DIR&gt;, &#8211;object-file=&lt;FILE&gt;</code></p>
<dd> Find objects in DIR or based on FILE’s path. If you specify a particular object file, the coverage data files are expected to have the same base name with <code>.gcno</code> and <code>.gcda</code> extensions. If you specify a directory, the files are expected in that directory with the same base name as the source file.</p>
<dt><code>-p, &#8211;preserve-paths</code></p>
<dd> Preserve path components when naming the coverage output files. In addition to the source file name, include the directories from the path to that file. The directories are separate by <code>#</code> characters, with <code>.</code> directories removed and <code>..</code> directories replaced by <code>^</code> characters. When used with the –long-file-names option, this applies to both the main file name and the included file name.</p>
<dt><code>-r</code></p>
<dd> Only dump files with relative paths or absolute paths with the prefix specified by <code>-s</code>.</p>
<dt><code>-s=&lt;string&gt;</code></p>
<dd> Source prefix to elide.</p>
<dt><code>-t, &#8211;stdout</code></p>
<dd> Print to stdout instead of producing <code>.gcov</code> files.</p>
<dt><code>-u, &#8211;unconditional-branches</code></p>
<dd> Include unconditional branches in the output for the –branch-probabilities option.</p>
<dt><code>-version</code></p>
<dd> Display the version of llvm-cov.</p>
<dt><code>-x, &#8211;hash-filenames</code></p>
<dd> Use md5 hash of file name when naming the coverage output files. The source file name will be suffixed by <code>##</code> followed by MD5 hash calculated for it.</dl>
<h3>EXIT STATUS</h3>
<p> <code>llvm-cov gcov</code> returns 1 if it cannot read input files. Otherwise, it exits with zero.</p>
<h2>SHOW COMMAND</h2>
<h3>SYNOPSIS</h3>
<p> <code>llvm-cov show</code> [<i>options</i>] -instr-profile <i>PROFILE</i> <i>BIN</i> [<i>-object BIN,…</i>] [[<i>-object BIN</i>]] [<i>SOURCES</i>]</p>
<h3>DESCRIPTION</h3>
<p> The <code>llvm-cov show</code> command shows line by line coverage of the binaries <i>BIN</i>,… using the profile data <i>PROFILE</i>. It can optionally be filtered to only show the coverage for the files listed in <i>SOURCES</i>. </p>
<p> <i>BIN</i> may be an executable, object file, dynamic library, or archive (thin or otherwise). </p>
<p> To use <code>llvm-cov show</code>, you need a program that is compiled with instrumentation to emit profile and coverage data. To build such a program with <code>clang</code> use the <code>-fprofile-instr-generate</code> and <code>-fcoverage-mapping</code> flags. If linking with the <code>clang</code> driver, pass <code>-fprofile-instr-generate</code> to the link stage to make sure the necessary runtime libraries are linked in. </p>
<p> The coverage information is stored in the built executable or library itself, and this is what you should pass to <code>llvm-cov show</code> as a <i>BIN</i> argument. The profile data is generated by running this instrumented program normally. When the program exits it will write out a raw profile file, typically called <code>default.profraw</code>, which can be converted to a format that is suitable for the <i>PROFILE</i> argument using the <code>llvm-profdata merge</code> tool.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-show-branches=&lt;VIEW&gt;</code></p>
<dd> Show coverage for branch conditions in terms of either count or percentage. The supported views are: “count”, “percent”.</p>
<dt><code>-show-line-counts</code></p>
<dd> Show the execution counts for each line. Defaults to true, unless another <code>-show</code> option is used.</p>
<dt><code>-show-expansions</code></p>
<dd> Expand inclusions, such as preprocessor macros or textual inclusions, inline in the display of the source file. Defaults to false.</p>
<dt><code>-show-instantiations</code></p>
<dd> For source regions that are instantiated multiple times, such as templates in <code>C++</code>, show each instantiation separately as well as the combined summary. Defaults to true.</p>
<dt><code>-show-regions</code></p>
<dd> Show the execution counts for each region by displaying a caret that points to the character where the region starts. Defaults to false.</p>
<dt><code>-show-line-counts-or-regions</code></p>
<dd> Show the execution counts for each line if there is only one region on the line, but show the individual regions if there are multiple on the line. Defaults to false.</p>
<dt><code>-use-color</code></p>
<dd> Enable or disable color output. By default this is autodetected.</p>
<dt><code>-arch=[*NAMES*]</code></p>
<dd> Specify a list of architectures such that the Nth entry in the list corresponds to the Nth specified binary. If the covered object is a universal binary, this specifies the architecture to use. It is an error to specify an architecture that is not included in the universal binary or to use an architecture that does not match a non-universal binary.</p>
<dt><code>-name=&lt;NAME&gt;</code></p>
<dd> Show code coverage only for functions with the given name.</p>
<dt><code>-name-allowlist=&lt;FILE&gt;</code></p>
<dd> Show code coverage only for functions listed in the given file. Each line in the file should start with <i>allowlist_fun:</i>, immediately followed by the name of the function to accept. This name can be a wildcard expression.</p>
<dt><code>-name-whitelist=&lt;FILE&gt;</code></p>
<dd> Show code coverage only for functions listed in the given file. Each line in the file should start with <i>whitelist_fun:</i>, immediately followed by the name of the function to accept. This name can be a wildcard expression. This option will be deprecated for <i>-name-allowlist=&lt;FILE&gt;</i> in future releases.</p>
<dt><code>-name-regex=&lt;PATTERN&gt;</code></p>
<dd> Show code coverage only for functions that match the given regular expression.</p>
<dt><code>-ignore-filename-regex=&lt;PATTERN&gt;</code></p>
<dd> Skip source code files with file paths that match the given regular expression.</p>
<dt><code>-format=&lt;FORMAT&gt;</code></p>
<dd> Use the specified output format. The supported formats are: “text”, “html”.</p>
<dt><code>-tab-size=&lt;TABSIZE&gt;</code></p>
<dd> Replace tabs with &lt;TABSIZE&gt; spaces when preparing reports. Currently, this is only supported for the html format.</p>
<dt><code>-output-dir=PATH</code></p>
<dd> Specify a directory to write coverage reports into. If the directory does not exist, it is created. When used in function view mode (i.e when -name or -name-regex are used to select specific functions), the report is written to PATH/functions.EXTENSION. When used in file view mode, a report for each file is written to PATH/REL_PATH_TO_FILE.EXTENSION.</p>
<dt><code>-Xdemangler=&lt;TOOL&gt;|&lt;TOOL-OPTION&gt;</code></p>
<dd> Specify a symbol demangler. This can be used to make reports more human-readable. This option can be specified multiple times to supply arguments to the demangler (e.g <i>-Xdemangler c++filt -Xdemangler -n</i> for C++). The demangler is expected to read a newline-separated list of symbols from stdin and write a newline-separated list of the same length to stdout.</p>
<dt><code>-num-threads=N, -j=N</code></p>
<dd> Use N threads to write file reports (only applicable when -output-dir is specified). When N=0, llvm-cov auto-detects an appropriate number of threads to use. This is the default.</p>
<dt><code>-compilation-dir=&lt;dir&gt;</code></p>
<dd> Directory used as a base for relative coverage mapping paths. Only applicable when binaries have been compiled with one of <i>-fcoverage-prefix-map</i> <i>-fcoverage-compilation-dir</i>, or <i>-ffile-compilation-dir</i>.</p>
<dt><code>-line-coverage-gt=&lt;N&gt;</code></p>
<dd> Show code coverage only for functions with line coverage greater than the given threshold.</p>
<dt><code>-line-coverage-lt=&lt;N&gt;</code></p>
<dd> Show code coverage only for functions with line coverage less than the given threshold.</p>
<dt><code>-region-coverage-gt=&lt;N&gt;</code></p>
<dd> Show code coverage only for functions with region coverage greater than the given threshold.</p>
<dt><code>-region-coverage-lt=&lt;N&gt;</code></p>
<dd> Show code coverage only for functions with region coverage less than the given threshold.</p>
<dt><code>-path-equivalence=&lt;from&gt;,&lt;to&gt;</code></p>
<dd> Map the paths in the coverage data to local source file paths. This allows you to generate the coverage data on one machine, and then use llvm-cov on a different machine where you have the same files on a different path.</dl>
<h2>REPORT COMMAND</h2>
<h3>SYNOPSIS</h3>
<p> <code>llvm-cov report</code> [<i>options</i>] -instr-profile <i>PROFILE</i> <i>BIN</i> [<i>-object BIN,…</i>] [[<i>-object BIN</i>]] [<i>SOURCES</i>]</p>
<h3>DESCRIPTION</h3>
<p> The <code>llvm-cov report</code> command displays a summary of the coverage of the binaries <i>BIN</i>,… using the profile data <i>PROFILE</i>. It can optionally be filtered to only show the coverage for the files listed in <i>SOURCES</i>. </p>
<p> <i>BIN</i> may be an executable, object file, dynamic library, or archive (thin or otherwise). </p>
<p> If no source files are provided, a summary line is printed for each file in the coverage data. If any files are provided, summaries can be shown for each function in the listed files if the <code>-show-functions</code> option is enabled. </p>
<p> For information on compiling programs for coverage and generating profile data, see <i>SHOW COMMAND</i>.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-use-color[=VALUE]</code></p>
<dd> Enable or disable color output. By default this is autodetected.</p>
<dt><code>-arch=&lt;name&gt;</code></p>
<dd> If the covered binary is a universal binary, select the architecture to use. It is an error to specify an architecture that is not included in the universal binary or to use an architecture that does not match a non-universal binary.</p>
<dt><code>-show-region-summary</code></p>
<dd> Show statistics for all regions. Defaults to true.</p>
<dt><code>-show-branch-summary</code></p>
<dd> Show statistics for all branch conditions. Defaults to true.</p>
<dt><code>-show-functions</code></p>
<dd> Show coverage summaries for each function. Defaults to false.</p>
<dt><code>-show-instantiation-summary</code></p>
<dd> Show statistics for all function instantiations. Defaults to false.</p>
<dt><code>-ignore-filename-regex=&lt;PATTERN&gt;</code></p>
<dd> Skip source code files with file paths that match the given regular expression.</p>
<dt><code>-compilation-dir=&lt;dir&gt;</code></p>
<dd> Directory used as a base for relative coverage mapping paths. Only applicable when binaries have been compiled with one of <i>-fcoverage-prefix-map</i> <i>-fcoverage-compilation-dir</i>, or <i>-ffile-compilation-dir</i>.</dl>
<h2>EXPORT COMMAND</h2>
<h3>SYNOPSIS</h3>
<p> <code>llvm-cov export</code> [<i>options</i>] -instr-profile <i>PROFILE</i> <i>BIN</i> [<i>-object BIN,…</i>] [[<i>-object BIN</i>]] [<i>SOURCES</i>]</p>
<h3>DESCRIPTION</h3>
<p> The <code>llvm-cov export</code> command exports coverage data of the binaries <i>BIN</i>,… using the profile data <i>PROFILE</i> in either JSON or lcov trace file format. </p>
<p> When exporting JSON, the regions, functions, branches, expansions, and summaries of the coverage data will be exported. When exporting an lcov trace file, the line-based coverage, branch coverage, and summaries will be exported. </p>
<p> The exported data can optionally be filtered to only export the coverage for the files listed in <i>SOURCES</i>. </p>
<p> For information on compiling programs for coverage and generating profile data, see <i>SHOW COMMAND</i>.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-arch=&lt;name&gt;</code></p>
<dd> If the covered binary is a universal binary, select the architecture to use. It is an error to specify an architecture that is not included in the universal binary or to use an architecture that does not match a non-universal binary.</p>
<dt><code>-format=&lt;FORMAT&gt;</code></p>
<dd> Use the specified output format. The supported formats are: “text” (JSON), “lcov”.</p>
<dt><code>-summary-only</code></p>
<dd> Export only summary information for each file in the coverage data. This mode will not export coverage information for smaller units such as individual functions or regions. The result will contain the same information as produced by the <code>llvm-cov report</code> command, but presented in JSON or lcov format rather than text.</p>
<dt><code>-ignore-filename-regex=&lt;PATTERN&gt;</code></p>
<dd> Skip source code files with file paths that match the given regular expression.</p>
<dt><code>-skip-expansions</code></p>
<dd>
<p> Skip exporting macro expansion coverage data.</p>
<dt><code>-skip-functions</code></p>
<dd>
<p> Skip exporting per-function coverage data.</p>
<dt><code>-num-threads=N, -j=N</code></p>
<dd>
<p> Use N threads to export coverage data. When N=0, llvm-cov auto-detects an appropriate number of threads to use. This is the default.</p>
<dt><code>-compilation-dir=&lt;dir&gt;</code></p>
<dd> Directory used as a base for relative coverage mapping paths. Only applicable when binaries have been compiled with one of <i>-fcoverage-prefix-map</i> <i>-fcoverage-compilation-dir</i>, or <i>-ffile-compilation-dir</i>.</dl>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
