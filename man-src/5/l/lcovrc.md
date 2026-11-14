---
title: "lcovrc(5)"
name: "lcovrc"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lcovrc/"
description: "lcovrc – lcov configuration file"
---

<p>lcovrc &#8211; lcov configuration file</p>
<h2>Description</h2>
<p>The <i>lcovrc</i> file contains configuration information for the <code>lcov</code> code coverage tool (see <code><a href="/docs/linux/man/1-lcov/">lcov</a></code>(1)).<br />
 The system-wide configuration file is located at <i>/etc/lcovrc</i>. To change settings for a single user, place a customized copy of this file at location <i>~/.lcovrc</i>. Where available, command-line options override configuration file settings. Lines in a configuration file can either be:</p>
<dl>
<dt> *</p>
<dd>empty lines or lines consisting only of white space characters. These lines are ignored.</p>
<dt> *</p>
<dd>comment lines which start with a hash sign (&#8216;#&#8217;). These are treated like empty lines and will be ignored.</p>
<dt> *</p>
<dd>statements in the form &#8216;<i>key</i> = <i>value</i>&#8216;. A list of valid statements and their description can be found in section &#8216;OPTIONS&#8217; below.</dl>
<p> <code>Example configuration:</code></p>
<dl>
<dd>#<br />
 # Example LCOV configuration file<br />
 #<br />
 # External style sheet file<br />
 #genhtml_css_file = gcov.css<br />
 # Coverage rate limits<br />
 genhtml_hi_limit = 90<br />
 genhtml_med_limit = 75<br />
 # Width of line coverage field in source code view<br />
 genhtml_line_field_width = 12<br />
 # Width of branch coverage field in source code view<br />
 genhtml_branch_field_width = 16<br />
 # Width of overview image<br />
 genhtml_overview_width = 80<br />
 # Resolution of overview navigation<br />
 genhtml_nav_resolution = 4<br />
 # Offset for source code navigation<br />
 genhtml_nav_offset = 10<br />
 # Do not remove unused test descriptions if non-zero<br />
 genhtml_keep_descriptions = 0<br />
 # Do not remove prefix from directory names if non-zero<br />
 genhtml_no_prefix = 0<br />
 # Do not create source code view if non-zero<br />
 genhtml_no_source = 0<br />
 # Specify size of tabs<br />
 genhtml_num_spaces = 8<br />
 # Highlight lines with converted-only data if non-zero<br />
 genhtml_highlight = 0<br />
 # Include color legend in HTML output if non-zero<br />
 genhtml_legend = 0<br />
 # Include HTML file at start of HTML output<br />
 #genhtml_html_prolog = prolog.html<br />
 # Include HTML file at end of HTML output<br />
 #genhtml_html_epilog = epilog.html<br />
 # Use custom HTML file extension<br />
 #genhtml_html_extension = html<br />
 # Compress all generated html files with gzip.<br />
 #genhtml_html_gzip = 1<br />
 # Include sorted overview pages<br />
 genhtml_sort = 1<br />
 # Include function coverage data display<br />
 #genhtml_function_coverage = 1<br />
 # Include branch coverage data display<br />
 #genhtml_branch_coverage = 1<br />
 # Specify the character set of all generated HTML pages<br />
 genhtml_charset=UTF-8<br />
 # Location of the gcov tool<br />
 #geninfo_gcov_tool = gcov<br />
 # Adjust test names if non-zero<br />
 #geninfo_adjust_testname = 0<br />
 # Calculate a checksum for each line if non-zero<br />
 geninfo_checksum = 0<br />
 # Enable libtool compatibility mode if non-zero<br />
 geninfo_compat_libtool = 0<br />
 # Specify whether to capture coverage data for external source<br />
 # files<br />
 #geninfo_external = 1<br />
 # Use gcov&#8217;s &#8211;all-blocks option if non-zero<br />
 #geninfo_gcov_all_blocks = 1<br />
 # Specify compatiblity modes (same as &#8211;compat option<br />
 # of geninfo)<br />
 #geninfo_compat = libtool=on, hammer=auto, split_crc=auto<br />
 # Adjust path to source files by removing or changing path<br />
 # components that match the specified pattern (Perl regular<br />
 # expression format)<br />
 #geninfo_adjust_src_path = /tmp/build =&gt; /usr/src # Specify if geninfo should try to automatically determine<br />
 # the base-directory when collecting coverage data.<br />
 geninfo_auto_base = 1<br />
 # Directory containing gcov kernel files<br />
 lcov_gcov_dir = /proc/gcov<br />
 # Location for temporary directories<br />
 lcov_tmp_dir = /tmp<br />
 # Show full paths during list operation if non-zero<br />
 lcov_list_full_path = 0<br />
 # Specify the maximum width for list output. This value is<br />
 # ignored when lcov_list_full_path is non-zero.<br />
 lcov_list_width = 80<br />
 # Specify the maximum percentage of file names which may be<br />
 # truncated when choosing a directory prefix in list output.<br />
 # This value is ignored when lcov_list_full_path is non-zero.<br />
 lcov_list_truncate_max = 20 # Specify if function coverage data should be collected and<br />
 # processed.<br />
 lcov_function_coverage = 1<br />
 # Specify if branch coverage data should be collected and<br />
 # processed.<br />
 lcov_branch_coverage = 0
</dl>
<h2>Options</h2>
<p><code>genhtml_css_file</code> = <i>filename</i></p>
<dl>
<dd>Specify an external style sheet file. Use this option to modify the appearance of the HTML output as generated by <code>genhtml</code>. During output generation, a copy of this file will be placed in the output directory. </p>
<p> This option corresponds to the &#8211;css-file command line option of <code>genhtml</code>. </p>
<p> By default, a standard CSS file is generated.</dl>
<p> <code>genhtml_hi_limit</code> = <i>hi_limit</i><br />
 <code>genhtml_med_limit</code> = <i>med_limit</i> </p>
<dl>
<dd>Specify coverage rate limits for classifying file entries. Use this option to modify the coverage rates (in percent) for line, function and branch coverage at which a result is classified as high, medium or low coverage. This classification affects the color of the corresponding entries on the overview pages of the HTML output: </p>
<p> High: hi_limit &lt;= rate &lt;= 100 default color: green<br />
 Medium: med_limit &lt;= rate &lt; hi_limit default color: orange<br />
 Low: 0 &lt;= rate &lt; med_limit default color: red </p>
<p> Defaults are 90 and 75 percent.</dl>
<p> <code>genhtml_line_field_width</code> = <i>number_of_characters</i></p>
<dl>
<dd>Specify the width (in characters) of the source code view column containing line coverage information. </p>
<p> Default is 12.</dl>
<p> <code>genhtml_branch_field_width</code> = <i>number_of_characters</i></p>
<dl>
<dd>Specify the width (in characters) of the source code view column containing branch coverage information. </p>
<p> Default is 16.</dl>
<p> <code>genhtml_overview_width</code> = <i>pixel_size</i></p>
<dl>
<dd>Specify the width (in pixel) of the overview image created when generating HTML output using the &#8211;frames option of <code>genhtml</code>. </p>
<p> Default is 80.</dl>
<p> <code>genhtml_nav_resolution</code> = <i>lines</i></p>
<dl>
<dd>Specify the resolution of overview navigation when generating HTML output using the &#8211;frames option of <code>genhtml</code>. This number specifies the maximum difference in lines between the position a user selected from the overview and the position the source code window is scrolled to. </p>
<p> Default is 4.</dl>
<p> <code>genhtml_nav_offset</code> = <i>lines</i></p>
<dl>
<dd>Specify the overview navigation line offset as applied when generating HTML output using the &#8211;frames option of <code>genhtml.</code> </p>
<p> Clicking a line in the overview image should show the source code view at a position a bit further up, so that the requested line is not the first line in the window. This number specifies that offset. </p>
<p> Default is 10.</dl>
<p> <code>genhtml_keep_descriptions</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, keep unused test descriptions when generating HTML output using <code>genhtml</code>. </p>
<p> This option corresponds to the &#8211;keep-descriptions option of <code>genhtml</code>. </p>
<p> Default is 0.</dl>
<p> <code>genhtml_no_prefix</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, do not try to find and remove a common prefix from directory names. </p>
<p> This option corresponds to the &#8211;no-prefix option of <code>genhtml</code>. </p>
<p> Default is 0.</dl>
<p> <code>genhtml_no_source</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, do not create a source code view when generating HTML output using <code>genhtml</code>. </p>
<p> This option corresponds to the &#8211;no-source option of <code>genhtml</code>. </p>
<p> Default is 0.</dl>
<p> <code>genhtml_num_spaces</code> = <i>num</i></p>
<dl>
<dd>Specify the number of spaces to use as replacement for tab characters in the HTML source code view as generated by <code>genhtml</code>. </p>
<p> This option corresponds to the &#8211;num-spaces option of <code>genthml</code>. </p>
<p> Default is 8. </p>
</dl>
<p> <code>genhtml_highlight</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, highlight lines with converted-only data in HTML output as generated by <code>genhtml</code>. </p>
<p> This option corresponds to the &#8211;highlight option of <code>genhtml</code>. </p>
<p> Default is 0.</dl>
<p> <code>genhtml_legend</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, include a legend explaining the meaning of color coding in the HTML output as generated by <code>genhtml</code>. </p>
<p> This option corresponds to the &#8211;legend option of <code>genhtml</code>. </p>
<p> Default is 0.</dl>
<p> <code>genhtml_html_prolog</code> = <i>filename</i></p>
<dl>
<dd>If set, include the contents of the specified file at the beginning of HTML output. </p>
<p> This option corresponds to the &#8211;html-prolog option of <code>genhtml</code>. </p>
<p> Default is to use no extra prolog.</dl>
<p> <code>genhtml_html_epilog</code> = <i>filename</i></p>
<dl>
<dd>If set, include the contents of the specified file at the end of HTML output. </p>
<p> This option corresponds to the &#8211;html-epilog option of <code>genhtml</code>. </p>
<p> Default is to use no extra epilog.</dl>
<p> <code>genhtml_html_extension</code> = <i>extension</i></p>
<dl>
<dd>If set, use the specified string as filename extension for generated HTML files. </p>
<p> This option corresponds to the &#8211;html-extension option of <code>genhtml</code>. </p>
<p> Default extension is &quot;html&quot;.</dl>
<p> <code>genhtml_html_gzip</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If set, compress all html files using gzip. </p>
<p> This option corresponds to the &#8211;html-gzip option of <code>genhtml</code>. </p>
<p> Default extension is 0.</dl>
<p> <code>genhtml_sort</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, create overview pages sorted by coverage rates when generating HTML output using <code>genhtml</code>. </p>
<p> This option can be set to 0 by using the &#8211;no-sort option of <code>genhtml</code>. </p>
<p> Default is 1.</dl>
<p> <code>genhtml_function_coverage</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, include function coverage data when generating HTML output using <code>genhtml</code>. </p>
<p> This option can be set to 0 by using the &#8211;no-function-coverage option of <code>genhtml</code>. </p>
<p> Default is 1.</dl>
<p> <code>genhtml_branch_coverage</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, include branch coverage data when generating HTML output using <code>genhtml</code>. </p>
<p> This option can be set to 0 by using the &#8211;no-branch-coverage option of <code>genhtml</code>. </p>
<p> Default is 1.</dl>
<p> <code>genhtml_charset</code> = <i>charset</i></p>
<dl>
<dd>Specify the character set of all generated HTML pages. </p>
<p> Use this option if the source code contains characters which are not part of the default character set. Note that this option is ignored when a custom HTML prolog is specified (see also <code>genhtml_html_prolog</code>). </p>
<p> Default is UTF-8.</dl>
<p> <code>geninfo_gcov_tool</code> = <i>path_to_gcov</i></p>
<dl>
<dd>Specify the location of the gcov tool (see <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1)) which is used to generate coverage information from data files. </p>
<p> Default is &#8216;gcov&#8217;.</dl>
<p> <code>geninfo_adjust_testname</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, adjust test names to include operating system information when capturing coverage data. </p>
<p> Default is 0.</dl>
<p> <code>geninfo_checksum</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, generate source code checksums when capturing coverage data. Checksums are useful to prevent merging coverage data from incompatible source code versions but checksum generation increases the size of coverage files and the time used to generate those files. </p>
<p> This option corresponds to the &#8211;checksum and &#8211;no-checksum command line option of <code>geninfo</code>. </p>
<p> Default is 0.</dl>
<p> <code>geninfo_compat_libtool</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, enable libtool compatibility mode. When libtool compatibility mode is enabled, lcov will assume that the source code relating to a .da file located in a directory named &quot;.libs&quot; can be found in its parent directory. </p>
<p> This option corresponds to the &#8211;compat-libtool and &#8211;no-compat-libtool command line option of <code>geninfo</code>. </p>
<p> Default is 1.</dl>
<p> <code>geninfo_external</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, capture coverage data for external source files. </p>
<p> External source files are files which are not located in one of the directories (including sub-directories) specified by the &#8211;directory or &#8211;base-directory options of <code>lcov</code>/<code>geninfo</code>. </p>
<p> Default is 1.</dl>
<p> <code>geninfo_gcov_all_blocks</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, call the gcov tool with option &#8211;all-blocks. </p>
<p> Using &#8211;all-blocks will produce more detailed branch coverage information for each line. Set this option to zero if you do not need detailed branch coverage information to speed up the process of capturing code coverage or to work around a bug in some versions of gcov which will cause it to endlessly loop when analysing some files. </p>
<p> Default is 1.</dl>
<p> <code>geninfo_compat</code> = <i>mode</i>=<i>value</i>[,<i>mode</i>=<i>value</i>,&#8230;]</p>
<dl>
<dd>Specify that geninfo should enable one or more compatibility modes when capturing coverage data. </p>
<p> This option corresponds to the &#8211;compat command line option of <code>geninfo</code>. </p>
<p> Default is &#8216;libtool=on, hammer=auto, split_crc=auto&#8217;.</dl>
<p> <code>geninfo_adjust_src_path</code> = <i>pattern</i> =&gt; <i>replacement</i><br />
 <code>geninfo_adjust_src_path</code> = <i>pattern</i></p>
<dl>
<dd>Adjust source paths when capturing coverage data. </p>
<p> Use this option in situations where geninfo cannot find the correct path to source code files of a project. By providing a <i>pattern</i> in Perl regular expression format (see <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1)) and an optional replacement string, you can instruct geninfo to remove or change parts of the incorrect source path. </p>
<p> <code>Example:</code> </p>
<p> 1. When geninfo reports that it cannot find source file </p>
<p>&nbsp;<wbr>/path/to/src/.libs/file.c </p>
<p> while the file is actually located in </p>
<p>&nbsp;<wbr>/path/to/src/file.c </p>
<p> use the following parameter: </p>
<p>&nbsp;<wbr>geninfo_adjust_src_path&nbsp;<wbr>=&nbsp;<wbr>/.libs </p>
<p> This will remove all &quot;/.libs&quot; strings from the path. </p>
<p> 2. When geninfo reports that it cannot find source file </p>
<p>&nbsp;<wbr>/tmp/build/file.c </p>
<p> while the file is actually located in </p>
<p>&nbsp;<wbr>/usr/src/file.c </p>
<p> use the following parameter: </p>
<p>&nbsp;<wbr>geninfo_adjust_src_path&nbsp;<wbr>=&nbsp;<wbr>/tmp/build&nbsp;<wbr>=&gt;&nbsp;<wbr>/usr/src </p>
<p> This will change all &quot;/tmp/build&quot; strings in the path to &quot;/usr/src&quot;.</dl>
<p> <code>geninfo_auto_base</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, apply a heuristic to determine the base directory when collecting coverage data. </p>
<p> Use this option when using geninfo on projects built with libtool or similar build environments that work with multiple base directories, i.e. environments, where the current working directory when invoking the compiler ist not the same directory in which the source code file is located, and in addition, is different between files of the same project. </p>
<p> Default is 1.</dl>
<p> <code>lcov_gcov_dir</code> = <i>path_to_kernel_coverage_data</i></p>
<dl>
<dd>Specify the path to the directory where kernel coverage data can be found or leave undefined for auto-detection. </p>
<p> Default is auto-detection.</dl>
<p> <code>lcov_tmp_dir</code> = <i>temp</i></p>
<dl>
<dd>Specify the location of a directory used for temporary files. </p>
<p> Default is &#8216;/tmp&#8217;.</dl>
<p> <code>lcov_list_full_path</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>If non-zero, print the full path to source code files during a list operation. </p>
<p> This option corresponds to the &#8211;list-full-path option of <code>lcov</code>. </p>
<p> Default is 0.</dl>
<p> <code>lcov_list_max_width</code> = <i>width</i></p>
<dl>
<dd>Specify the maximum width for list output. This value is ignored when lcov_list_full_path is non-zero. </p>
<p> Default is 80.</dl>
<p> <code>lcov_list_truncate_max</code> <code> =</code> <i>percentage</i></p>
<dl>
<dd>Specify the maximum percentage of file names which may be truncated when choosing a directory prefix in list output. This value is ignored when lcov_list_full_path is non-zero. </p>
<p> Default is 20.</dl>
<p> <code>lcov_function_coverage</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>Specify whether lcov should handle function coverage data. </p>
<p> Setting this option to 0 can reduce memory and CPU time consumption when lcov is collecting and processing coverage data, as well as reduce the size of the resulting data files. Note that setting <code>genhtml_function_coverage</code> will override this option for HTML generation. </p>
<p> Default is 1.</dl>
<p> <code>lcov_branch_coverage</code> = <i>0</i>|<i>1</i></p>
<dl>
<dd>Specify whether lcov should handle branch coverage data. </p>
<p> Setting this option to 0 can reduce memory and CPU time consumption when lcov is collecting and processing coverage data, as well as reduce the size of the resulting data files. Note that setting <code>genhtml_branch_coverage</code> will override this option for HTML generation. </p>
<p> Default is 0.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/lcovrc</i></p>
<dd>The system-wide <code>lcov</code> configuration file. </p>
<dt><i>~/.lcovrc</i></p>
<dd>The individual per-user configuration file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lcov/">lcov</a></code>(1), <code><a href="/docs/linux/man/1-genhtml/">genhtml</a></code>(1), <code><a href="/docs/linux/man/1-geninfo/">geninfo</a></code>(1), <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) </p>
