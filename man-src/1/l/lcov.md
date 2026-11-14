---
title: "lcov(1)"
name: "lcov"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lcov/"
description: "lcov – a graphical GCOV front-end"
---

<h2>NAME</h2>
<p> lcov &#8211; a graphical GCOV front-end</p>
<h2>SYNOPSIS</h2>
<p> <code>lcov</code> <code>-c</code>|<code>&#8211;capture</code></p>
<dl>
<dt>
<dd>
 [<code>-d</code>|<code>&#8211;directory</code> <i>directory</i>] [<code>-k</code>|<code>&#8211;kernel-directory</code> <i>directory</i>]<br />
 [<code>-o</code>|<code>&#8211;output-file</code> <i>tracefile</i>] [<code>-t</code>|<code>&#8211;test-name</code> <i>testname</i>]<br />
 [<code>-b</code>|<code>&#8211;base-directory</code> <i>directory</i>] [<code>-i</code>|<code>&#8211;initial</code>] [<code>&#8211;gcov-tool</code> <i>tool</i>]<br />
 [<code>&#8211;checksum</code>] [<code>&#8211;no-checksum</code>] [<code>&#8211;no-recursion</code>] [<code>-f</code>|<code>&#8211;follow</code>]<br />
 [<code>&#8211;compat-libtool</code>] [<code>&#8211;no-compat-libtool</code>] [<code>&#8211;ignore-errors</code> <i>errors</i>]<br />
 [<code>&#8211;to-package</code> <i>package</i>] [<code>&#8211;from-package</code> <i>package</i>] [<code>-q</code>|<code>&#8211;quiet</code>]<br />
 [<code>&#8211;no-markers</code>] [<code>&#8211;external</code>] [<code>&#8211;no-external</code>]<br />
 [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]<br />
 [<code>&#8211;compat</code> <i>mode</i>=on|off|auto]
</dl>
<p> <code>lcov</code> <code>-z</code>|<code>&#8211;zerocounters</code></p>
<dl>
<dt>
<dd>
 [<code>-d</code>|<code>&#8211;directory</code> <i>directory</i>] [<code>&#8211;no-recursion</code>] [<code>-f</code>|<code>&#8211;follow</code>]<br />
 [<code>-q</code>|<code>&#8211;quiet</code>]
</dl>
<p> <code>lcov</code> <code>-l</code>|<code>&#8211;list</code> <i>tracefile</i></p>
<dl>
<dt>
<dd>
 [<code>-q</code>|<code>&#8211;quiet</code>] [<code>&#8211;list-full-path</code>] [<code>&#8211;no-list-full-path</code>]<br />
 [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]
</dl>
<p> <code>lcov</code> <code>-a</code>|<code>&#8211;add-tracefile</code> <i>tracefile</i></p>
<dl>
<dt>
<dd>
 [<code>-o</code>|<code>&#8211;output-file</code> <i>tracefile</i>] [<code>&#8211;checksum</code>] [<code>&#8211;no-checksum</code>]<br />
 [<code>-q</code>|<code>&#8211;quiet</code>] [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]
</dl>
<p> <code>lcov</code> <code>-e</code>|<code>&#8211;extract</code> <i>tracefile pattern</i></p>
<dl>
<dt>
<dd>
 [<code>-o</code>|<code>&#8211;output-file</code> <i>tracefile</i>] [<code>&#8211;checksum</code>] [<code>&#8211;no-checksum</code>]<br />
 [<code>-q</code>|<code>&#8211;quiet</code>] [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]
</dl>
<p> <code>lcov</code> <code>-r</code>|<code>&#8211;remove</code> <i>tracefile pattern</i></p>
<dl>
<dt>
<dd>
 [<code>-o</code>|<code>&#8211;output-file</code> <i>tracefile</i>] [<code>&#8211;checksum</code>] [<code>&#8211;no-checksum</code>]<br />
 [<code>-q</code>|<code>&#8211;quiet</code>] [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]
</dl>
<p> <code>lcov</code> <code>&#8211;diff</code> <i>tracefile diff</i></p>
<dl>
<dt>
<dd>
 [<code>-o</code>|<code>&#8211;output-file</code> <i>tracefile</i>] [<code>&#8211;checksum</code>] [<code>&#8211;no-checksum</code>]<br />
 [<code>&#8211;convert-filenames</code>] [<code>&#8211;strip</code> <i>depth</i>] [<code>&#8211;path</code> <i>path</i>] [<code>-q</code>|<code>&#8211;quiet</code>]<br />
 [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]
</dl>
<p> <code>lcov</code> <code>&#8211;summary</code> <i>tracefile</i></p>
<dl>
<dt>
<dd>
 [<code>-q</code>|<code>&#8211;quiet</code>]
</dl>
<p> <code>lcov</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>]</p>
<dl>
<dt>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>lcov</code> is a graphical front-end for GCC&#8217;s coverage testing tool gcov. It collects line, function and branch coverage data for multiple source files and creates HTML pages containing the source code annotated with coverage information. It also adds overview pages for easy navigation within the file structure. </p>
<p> Use <code>lcov</code> to collect coverage data and <code>genhtml</code> to create HTML pages. Coverage data can either be collected from the currently running Linux kernel or from a user space application. To do this, you have to complete the following preparation steps: </p>
<p> For Linux kernel coverage:</p>
<dl>
<dt>
<dd> Follow the setup instructions for the gcov-kernel infrastructure: <i><a rel="nofollow" href="http://ltp.sourceforge.net/coverage/gcov.php">http://ltp.sourceforge.net/coverage/gcov.php</a></i> </p>
</dl>
<p> For user space application coverage:</p>
<dl>
<dt>
<dd> Compile the application with GCC using the options &quot;-fprofile-arcs&quot; and &quot;-ftest-coverage&quot;.</dl>
<p> Please note that this man page refers to the output format of <code>lcov</code> as &quot;.info file&quot; or &quot;tracefile&quot; and that the output of GCOV is called &quot;.da file&quot;. </p>
<p> Also note that when printing percentages, 0% and 100% are only printed when the values are exactly 0% and 100% respectively. Other values which would conventionally be rounded to 0% or 100% are instead printed as nearest non-boundary value. This behavior is in accordance with that of the <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) tool. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code> <i>tracefile</i><br />
 <code>&#8211;add-tracefile</code> <i>tracefile</i> </p>
<dl>
<dt>
<dd> Add contents of <i>tracefile</i>. </p>
<p> Specify several tracefiles using the -a switch to combine the coverage data contained in these files by adding up execution counts for matching test and filename combinations. </p>
<p> The result of the add operation will be written to stdout or the tracefile specified with -o. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time. </p>
</dl>
<p> <code>-b</code> <i>directory</i><br />
 <code>&#8211;base-directory</code> <i>directory</i> </p>
<dl>
<dt>
<dd> Use <i>directory</i> as base directory for relative paths. </p>
<p> Use this option to specify the base directory of a build-environment when lcov produces error messages like: </p>
<dl>
<dt>
<dd> ERROR: could not read source file /home/user/project/subdir1/subdir2/subdir1/subdir2/file.c</dl>
<p> In this example, use /home/user/project as base directory. </p>
<p> This option is required when using lcov on projects built with libtool or similar build environments that work with a base directory, i.e. environments, where the current working directory when invoking the compiler is not the same directory in which the source code file is located. </p>
<p> Note that this option will not work in environments where multiple base directories are used. In that case use configuration file setting <code>geninfo_auto_base=1</code> (see <code><a href="/docs/linux/man/5-lcovrc/">lcovrc</a></code>(5)).</dl>
<p> <code>-c</code><br />
 <code>&#8211;capture</code> </p>
<dl>
<dt>
<dd> Capture coverage data. </p>
<p> By default captures the current kernel execution counts and writes the resulting coverage data to the standard output. Use the &#8211;directory option to capture counts for a user space program. </p>
<p> The result of the capture operation will be written to stdout or the tracefile specified with -o. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<p> <code>&#8211;checksum</code><br />
 <code>&#8211;no-checksum</code> </p>
<dl>
<dt>
<dd> Specify whether to generate checksum data when writing tracefiles. </p>
<p> Use &#8211;checksum to enable checksum generation or &#8211;no-checksum to disable it. Checksum generation is <code>disabled</code> by default. </p>
<p> When checksum generation is enabled, a checksum will be generated for each source code line and stored along with the coverage data. This checksum will be used to prevent attempts to combine coverage data from different source code versions. </p>
<p> If you don&#8217;t work with different source code versions, disable this option to speed up coverage data processing and to reduce the size of tracefiles.</dl>
<p> <code>&#8211;compat</code> <i>mode</i>=<i>value</i>[,<i>mode</i>=<i>value</i>,&#8230;] </p>
<dl>
<dt>
<dd> Set compatibility mode. </p>
<p> Use &#8211;compat to specify that lcov should enable one or more compatibility modes when capturing coverage data. You can provide a comma-separated list of mode=value pairs to specify the values for multiple modes. </p>
<p> Valid <i>values</i> are: </p>
<p> <code>on</code></p>
<dl>
<dt>
<dd> Enable compatibility mode.</dl>
<p> <code>off</code></p>
<dl>
<dt>
<dd> Disable compatibility mode.</dl>
<p> <code>auto</code></p>
<dl>
<dt>
<dd> Apply auto-detection to determine if compatibility mode is required. Note that auto-detection is not available for all compatibility modes.</dl>
<p> If no value is specified, &#8216;on&#8217; is assumed as default value. </p>
<p> Valid <i>modes</i> are: </p>
<p> <code>libtool</code></p>
<dl>
<dt>
<dd> Enable this mode if you are capturing coverage data for a project that was built using the libtool mechanism. See also &#8211;compat-libtool. </p>
<p> The default value for this setting is &#8216;on&#8217;. </p>
</dl>
<p> <code>hammer</code></p>
<dl>
<dt>
<dd> Enable this mode if you are capturing coverage data for a project that was built using a version of GCC 3.3 that contains a modification (hammer patch) of later GCC versions. You can identify a modified GCC 3.3 by checking the build directory of your project for files ending in the extension &#8216;.bbg&#8217;. Unmodified versions of GCC 3.3 name these files &#8216;.bb&#8217;. </p>
<p> The default value for this setting is &#8216;auto&#8217;. </p>
</dl>
<p> <code>split_crc</code></p>
<dl>
<dt>
<dd> Enable this mode if you are capturing coverage data for a project that was built using a version of GCC 4.6 that contains a modification (split function checksums) of later GCC versions. Typical error messages when running lcov on coverage data produced by such GCC versions are &#8216;out of memory&#8217; and &#8216;reached unexpected end of file&#8217;. </p>
<p> The default value for this setting is &#8216;auto&#8217;</dl>
</dl>
<p> <code>&#8211;compat-libtool</code><br />
 <code>&#8211;no-compat-libtool</code> </p>
<dl>
<dt>
<dd> Specify whether to enable libtool compatibility mode. </p>
<p> Use &#8211;compat-libtool to enable libtool compatibility mode or &#8211;no-compat-libtool to disable it. The libtool compatibility mode is <code>enabled</code> by default. </p>
<p> When libtool compatibility mode is enabled, lcov will assume that the source code relating to a .da file located in a directory named &quot;.libs&quot; can be found in its parent directory. </p>
<p> If you have directories named &quot;.libs&quot; in your build environment but don&#8217;t use libtool, disable this option to prevent problems when capturing coverage data.</dl>
<p> <code>&#8211;config-file</code> <i>config-file</i> </p>
<dl>
<dt>
<dd> Specify a configuration file to use. </p>
<p> When this option is specified, neither the system-wide configuration file /etc/lcovrc, nor the per-user configuration file ~/.lcovrc is read. </p>
<p> This option may be useful when there is a need to run several instances of <code>lcov</code> with different configuration file options in parallel.</dl>
<p> <code>&#8211;convert-filenames</code> </p>
<dl>
<dt>
<dd> Convert filenames when applying diff. </p>
<p> Use this option together with &#8211;diff to rename the file names of processed data sets according to the data provided by the diff.</dl>
<p> <code>&#8211;diff</code> <i>tracefile</i> <i>difffile</i> </p>
<dl>
<dt>
<dd> Convert coverage data in <i>tracefile</i> using source code diff file <i>difffile</i>. </p>
<p> Use this option if you want to merge coverage data from different source code levels of a program, e.g. when you have data taken from an older version and want to combine it with data from a more current version. <code>lcov</code> will try to map source code lines between those versions and adjust the coverage data respectively. <i>difffile</i> needs to be in unified format, i.e. it has to be created using the &quot;-u&quot; option of the <code>diff</code> tool. </p>
<p> Note that lines which are not present in the old version will not be counted as instrumented, therefore tracefiles resulting from this operation should not be interpreted individually but together with other tracefiles taken from the newer version. Also keep in mind that converted coverage data should only be used for overview purposes as the process itself introduces a loss of accuracy. </p>
<p> The result of the diff operation will be written to stdout or the tracefile specified with -o. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<p> <code>-d</code> <i>directory</i><br />
 <code>&#8211;directory</code> <i>directory</i> </p>
<dl>
<dt>
<dd> Use .da files in <i>directory</i> instead of kernel. </p>
<p> If you want to work on coverage data for a user space program, use this option to specify the location where the program was compiled (that&#8217;s where the counter files ending with .da will be stored). </p>
<p> Note that you may specify this option more than once.</dl>
<p> <code>&#8211;external</code><br />
 <code>&#8211;no-external</code> </p>
<dl>
<dt>
<dd> Specify whether to capture coverage data for external source files. </p>
<p> External source files are files which are not located in one of the directories specified by &#8211;directory or &#8211;base-directory. Use &#8211;external to include external source files while capturing coverage data or &#8211;no-external to ignore this data. </p>
<p> Data for external source files is <code>included</code> by default.</dl>
<p> <code>-e</code> <i>tracefile</i> <i>pattern</i><br />
 <code>&#8211;extract</code> <i>tracefile</i> <i>pattern</i> </p>
<dl>
<dt>
<dd> Extract data from <i>tracefile</i>. </p>
<p> Use this switch if you want to extract coverage data for only a particular set of files from a tracefile. Additional command line parameters will be interpreted as shell wildcard patterns (note that they may need to be escaped accordingly to prevent the shell from expanding them first). Every file entry in <i>tracefile</i> which matches at least one of those patterns will be extracted. </p>
<p> The result of the extract operation will be written to stdout or the tracefile specified with -o. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<p> <code>-f</code><br />
 <code>&#8211;follow</code> </p>
<dl>
<dt>
<dd> Follow links when searching for .da files.</dl>
<p> <code>&#8211;from-package</code> <i>package</i> </p>
<dl>
<dt>
<dd> Use .da files in <i>package</i> instead of kernel or directory. </p>
<p> Use this option if you have separate machines for build and test and want to perform the .info file creation on the build machine. See &#8211;to-package for more information.</dl>
<p> <code>&#8211;gcov-tool</code> <i>tool</i> </p>
<dl>
<dt>
<dd> Specify the location of the gcov tool.</dl>
<p> <code>-h</code><br />
 <code>&#8211;help</code> </p>
<dl>
<dt>
<dd> Print a short help text, then exit.</dl>
<p> <code>&#8211;ignore-errors</code> <i>errors</i> </p>
<dl>
<dt>
<dd> Specify a list of errors after which to continue processing. </p>
<p> Use this option to specify a list of one or more classes of errors after which lcov should continue processing instead of aborting. </p>
<p> <i>errors</i> can be a comma-separated list of the following keywords: </p>
<p> <code>gcov:</code> the gcov tool returned with a non-zero return code. </p>
<p> <code>source:</code> the source code file for a data set could not be found.</dl>
<p> <code>-i</code><br />
 <code>&#8211;initial</code></p>
<dl>
<dt>
<dd> Capture initial zero coverage data. </p>
<p> Run lcov with -c and this option on the directories containing .bb, .bbg or .gcno files before running any test case. The result is a &quot;baseline&quot; coverage data file that contains zero coverage for every instrumented line. Combine this data file (using lcov -a) with coverage data files captured after a test run to ensure that the percentage of total lines covered is correct even when not all source code files were loaded during the test. </p>
<p> Recommended procedure when capturing data for a test case: </p>
<p> 1. create baseline coverage data file</p>
<dl>
<dt>
<dd> # lcov -c -i -d appdir -o app_base.info </p>
</dl>
<p> 2. perform test</p>
<dl>
<dt>
<dd> # appdir/test </p>
</dl>
<p> 3. create test coverage data file</p>
<dl>
<dt>
<dd> # lcov -c -d appdir -o app_test.info </p>
</dl>
<p> 4. combine baseline and test coverage data</p>
<dl>
<dt>
<dd> # lcov -a app_base.info -a app_test.info -o app_total.info </p>
</dl>
</dl>
<p> <code>-k</code> <i>subdirectory</i><br />
 <code>&#8211;kernel-directory</code> <i>subdirectory</i> </p>
<dl>
<dt>
<dd> Capture kernel coverage data only from <i>subdirectory</i>. </p>
<p> Use this option if you don&#8217;t want to get coverage data for all of the kernel, but only for specific subdirectories. This option may be specified more than once. </p>
<p> Note that you may need to specify the full path to the kernel subdirectory depending on the version of the kernel gcov support.</dl>
<p> <code>-l</code> <i>tracefile</i><br />
 <code>&#8211;list</code> <i>tracefile</i> </p>
<dl>
<dt>
<dd> List the contents of the <i>tracefile</i>. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<p> <code>&#8211;list-full-path</code><br />
 <code>&#8211;no-list-full-path</code> </p>
<dl>
<dt>
<dd> Specify whether to show full paths during list operation. </p>
<p> Use &#8211;list-full-path to show full paths during list operation or &#8211;no-list-full-path to show shortened paths. Paths are <code>shortened</code> by default.</dl>
<p> <code>&#8211;no-markers</code> </p>
<dl>
<dt>
<dd> Use this option if you want to get coverage data without regard to exclusion markers in the source code file. See <code>geninfo </code>(1) for details on exclusion markers.</dl>
<p> <code>&#8211;no-recursion</code> </p>
<dl>
<dt>
<dd> Use this option if you want to get coverage data for the specified directory only without processing subdirectories.</dl>
<p> <code>-o</code> <i>tracefile</i><br />
 <code>&#8211;output-file</code> <i>tracefile</i> </p>
<dl>
<dt>
<dd> Write data to <i>tracefile</i> instead of stdout. </p>
<p> Specify &quot;-&quot; as a filename to use the standard output. </p>
<p> By convention, lcov-generated coverage data files are called &quot;tracefiles&quot; and should have the filename extension &quot;.info&quot;.</dl>
<p> <code>&#8211;path</code> <i>path</i> </p>
<dl>
<dt>
<dd> Strip path from filenames when applying diff. </p>
<p> Use this option together with &#8211;diff to tell lcov to disregard the specified initial path component when matching between tracefile and diff filenames.</dl>
<p> <code>-q</code><br />
 <code>&#8211;quiet</code> </p>
<dl>
<dt>
<dd> Do not print progress messages. </p>
<p> This option is implied when no output filename is specified to prevent progress messages to mess with coverage data which is also printed to the standard output.</dl>
<p> <code>&#8211;rc</code> <i>keyword</i>=<i>value</i> </p>
<dl>
<dt>
<dd> Override a configuration directive. </p>
<p> Use this option to specify a <i>keyword</i>=<i>value</i> statement which overrides the corresponding configuration statement in the lcovrc configuration file. You can specify this option more than once to override multiple configuration statements. See <code><a href="/docs/linux/man/5-lcovrc/">lcovrc</a></code>(5) for a list of available keywords and their meaning.</dl>
<p> <code>-r</code> <i>tracefile</i> <i>pattern</i><br />
 <code>&#8211;remove</code> <i>tracefile</i> <i>pattern</i> </p>
<dl>
<dt>
<dd> Remove data from <i>tracefile</i>. </p>
<p> Use this switch if you want to remove coverage data for a particular set of files from a tracefile. Additional command line parameters will be interpreted as shell wildcard patterns (note that they may need to be escaped accordingly to prevent the shell from expanding them first). Every file entry in <i>tracefile</i> which matches at least one of those patterns will be removed. </p>
<p> The result of the remove operation will be written to stdout or the tracefile specified with -o. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<p> <code>&#8211;strip</code> <i>depth</i> </p>
<dl>
<dt>
<dd> Strip path components when applying diff. </p>
<p> Use this option together with &#8211;diff to tell lcov to disregard the specified number of initial directories when matching tracefile and diff filenames.</dl>
<p> <code>&#8211;summary</code> <i>tracefile</i> </p>
<dl>
<dt>
<dd> Show summary coverage information for the specified tracefile. </p>
<p> Note that you may specify this option more than once. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<p> <code>-t</code> <i>testname</i><br />
 <code>&#8211;test-name</code> <i>testname</i> </p>
<dl>
<dt>
<dd> Specify test name to be stored in the tracefile. </p>
<p> This name identifies a coverage data set when more than one data set is merged into a combined tracefile (see option -a). </p>
<p> Valid test names can consist of letters, decimal digits and the underscore character (&quot;_&quot;).</dl>
<p> <code>&#8211;to-package</code> <i>package</i> </p>
<dl>
<dt>
<dd> Store .da files for later processing. </p>
<p> Use this option if you have separate machines for build and test and want to perform the .info file creation on the build machine. To do this, follow these steps: </p>
<p> On the test machine:</p>
<dl>
<dt>
<dd>
 &#8211; run the test<br />
 &#8211; run lcov -c [-d directory] &#8211;to-package <i>file</i><br />
 &#8211; copy <i>file</i> to the build machine</dl>
<p> On the build machine:</p>
<dl>
<dt>
<dd>
 &#8211; run lcov -c &#8211;from-package <i>file</i> [-o and other options]</dl>
<p> This works for both kernel and user space coverage data. Note that you might have to specify the path to the build directory using -b with either &#8211;to-package or &#8211;from-package. Note also that the package data must be converted to a .info file before recompiling the program or it will become invalid.</dl>
<p> <code>-v</code><br />
 <code>&#8211;version</code> </p>
<dl>
<dt>
<dd> Print version number, then exit.</dl>
<p> <code>-z</code><br />
 <code>&#8211;zerocounters</code> </p>
<dl>
<dt>
<dd> Reset all execution counts to zero. </p>
<p> By default tries to reset kernel execution counts. Use the &#8211;directory option to reset all counters of a user space program. </p>
<p> Only one of -z, -c, -a, -e, -r, -l, &#8211;diff or &#8211;summary may be specified at a time.</dl>
<h2>FILES</h2>
<p> <i>/etc/lcovrc</i></p>
<dl>
<dt>
<dd> The system-wide configuration file.</dl>
<p> <i>~/.lcovrc</i></p>
<dl>
<dt>
<dd> The per-user configuration file.</dl>
<h2>AUTHOR</h2>
<p> Peter Oberparleiter &lt;Peter.Oberparleiter [at] de.ibm.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-lcovrc/">lcovrc</a></code>(5), <code><a href="/docs/linux/man/1-genhtml/">genhtml</a></code>(1), <code><a href="/docs/linux/man/1-geninfo/">geninfo</a></code>(1), <code><a href="/docs/linux/man/1-genpng/">genpng</a></code>(1), <code><a href="/docs/linux/man/1-gendesc/">gendesc</a></code>(1), <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) </p>
<h2>Index</h2>
