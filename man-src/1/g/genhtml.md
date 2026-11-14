---
title: "genhtml(1)"
name: "genhtml"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genhtml/"
description: "genhtml – Generate HTML view from LCOV coverage data files"
---

<h2>NAME</h2>
<p> genhtml &#8211; Generate HTML view from LCOV coverage data files</p>
<h2>SYNOPSIS</h2>
<p> <code>genhtml</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>]</p>
<dl>
<dt>
<dd>
 [<code>-q</code>|<code>&#8211;quiet</code>] [<code>-s</code>|<code>&#8211;show-details</code>] [<code>-f</code>|<code>&#8211;frames</code>]<br />
 [<code>-b</code>|<code>&#8211;baseline-file</code>] <i>baseline-file</i><br />
 [<code>-o</code>|<code>&#8211;output-directory</code> <i>output-directory</i>]<br />
 [<code>-t</code>|<code>&#8211;title</code> <i>title</i>]<br />
 [<code>-d</code>|<code>&#8211;description-file</code> <i>description-file</i>]<br />
 [<code>-k</code>|<code>&#8211;keep-descriptions</code>] [<code>-c</code>|<code>&#8211;css-file</code> <i>css-file</i>]<br />
 [<code>-p</code>|<code>&#8211;prefix</code> <i>prefix</i>] [<code>&#8211;no-prefix</code>]<br />
 [<code>&#8211;no-source</code>] [<code>&#8211;num-spaces</code> <i>num</i>] [<code>&#8211;highlight</code>]<br />
 [<code>&#8211;legend</code>] [<code>&#8211;html-prolog</code> <i>prolog-file</i>]<br />
 [<code>&#8211;html-epilog</code> <i>epilog-file</i>] [<code>&#8211;html-extension</code> <i>extension</i>]<br />
 [<code>&#8211;html-gzip</code>] [<code>&#8211;sort</code>] [<code>&#8211;no-sort</code>]<br />
 [<code>&#8211;function-coverage</code>] [<code>&#8211;no-function-coverage</code>]<br />
 [<code>&#8211;branch-coverage</code>] [<code>&#8211;no-branch-coverage</code>]<br />
 [<code>&#8211;demangle-cpp</code>] [<code>&#8211;ignore-errors</code> <i>errors</i>]<br />
 [<code>&#8211;config-file</code> <i>config-file</i>] [<code>&#8211;rc</code> <i>keyword</i>=<i>value</i>]<br />
 <i>tracefile(s)</i></dl>
<h2>DESCRIPTION</h2>
<p> Create an HTML view of coverage data found in <i>tracefile</i>. Note that <i>tracefile</i> may also be a list of filenames. </p>
<p> HTML output files are created in the current working directory unless the &#8211;output-directory option is used. If <i>tracefile</i> ends with &quot;.gz&quot;, it is assumed to be GZIP-compressed and the gunzip tool will be used to decompress it transparently. </p>
<p> Note that all source code files have to be present and readable at the exact file system location they were compiled. </p>
<p> Use option <i>&#8211;css-file</i> to modify layout and colors of the generated HTML output. Files are marked in different colors depending on the associated coverage rate. By default, the coverage limits for low, medium and high coverage are set to 0-75%, 75-90% and 90-100% percent respectively. To change these values, use configuration file options <i>genhtml_hi_limit</i> and <i>genhtml_med_limit</i>. </p>
<p> Also note that when displaying percentages, 0% and 100% are only printed when the values are exactly 0% and 100% respectively. Other values which would conventionally be rounded to 0% or 100% are instead printed as nearest non-boundary value. This behavior is in accordance with that of the <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) tool. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code><br />
 <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text, then exit. </p>
</dl>
<p> <code>-v</code><br />
 <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version number, then exit. </p>
</dl>
<p> <code>-q</code><br />
 <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Do not print progress messages. </p>
<p> Suppresses all informational progress output. When this switch is enabled, only error or warning messages are printed. </p>
</dl>
<p> <code>-f</code><br />
 <code>&#8211;frames</code></p>
<dl>
<dt>
<dd> Use HTML frames for source code view. </p>
<p> If enabled, a frameset is created for each source code file, providing an overview of the source code as a &quot;clickable&quot; image. Note that this option will slow down output creation noticeably because each source code character has to be inspected once. Note also that the GD.pm Perl module has to be installed for this option to work (it may be obtained from <a rel="nofollow" href="http://www.cpan.org">http://www.cpan.org</a>). </p>
</dl>
<p> <code>-s</code><br />
 <code>&#8211;show-details</code></p>
<dl>
<dt>
<dd> Generate detailed directory view. </p>
<p> When this option is enabled, <code>genhtml</code> generates two versions of each file view. One containing the standard information plus a link to a &quot;detailed&quot; version. The latter additionally contains information about which test case covered how many lines of each source file. </p>
</dl>
<p> <code>-b </code><i>baseline-file</i><br />
 <code>&#8211;baseline-file </code><i>baseline-file</i></p>
<dl>
<dt>
<dd> Use data in <i>baseline-file</i> as coverage baseline. </p>
<p> The tracefile specified by <i>baseline-file</i> is read and all counts found in the original <i>tracefile</i> are decremented by the corresponding counts in <i>baseline-file</i> before creating any output. </p>
<p> Note that when a count for a particular line in <i>baseline-file</i> is greater than the count in the <i>tracefile</i>, the result is zero. </p>
</dl>
<p> <code>-o </code><i>output-directory</i><br />
 <code>&#8211;output-directory </code><i>output-directory</i></p>
<dl>
<dt>
<dd> Create files in <i>output-directory.</i> </p>
<p> Use this option to tell <code>genhtml</code> to write the resulting files to a directory other than the current one. If <i>output-directory</i> does not exist, it will be created. </p>
<p> It is advisable to use this option since depending on the project size, a lot of files and subdirectories may be created. </p>
</dl>
<p> <code>-t </code><i>title</i><br />
 <code>&#8211;title </code><i>title</i></p>
<dl>
<dt>
<dd> Display <i>title</i> in header of all pages. </p>
<p> <i>title</i> is written to the header portion of each generated HTML page to identify the context in which a particular output was created. By default this is the name of the tracefile. </p>
</dl>
<p> <code>-d </code><i>description-file</i><br />
 <code>&#8211;description-file </code><i>description-file</i></p>
<dl>
<dt>
<dd> Read test case descriptions from <i>description-file</i>. </p>
<p> All test case descriptions found in <i>description-file</i> and referenced in the input data file are read and written to an extra page which is then incorporated into the HTML output. </p>
<p> The file format of <i>description-file </i>is: </p>
<p> for each test case:</p>
<dl>
<dt>
<dd> TN:&lt;testname&gt;<br />
 TD:&lt;test description&gt; </p>
</dl>
<p> Valid test case names can consist of letters, numbers and the underscore character (&#8216;_&#8217;).</dl>
<p> <code>-k</code><br />
 <code>&#8211;keep-descriptions</code></p>
<dl>
<dt>
<dd> Do not remove unused test descriptions. </p>
<p> Keep descriptions found in the description file even if the coverage data indicates that the associated test case did not cover any lines of code. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_keep_descriptions</i>. </p>
</dl>
<p> <code>-c </code><i>css-file</i><br />
 <code>&#8211;css-file </code><i>css-file</i></p>
<dl>
<dt>
<dd> Use external style sheet file <i>css-file</i>. </p>
<p> Using this option, an extra .css file may be specified which will replace the default one. This may be helpful if the default colors make your eyes want to jump out of their sockets :) </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_css_file</i>. </p>
</dl>
<p> <code>-p </code><i>prefix</i><br />
 <code>&#8211;prefix </code><i>prefix</i></p>
<dl>
<dt>
<dd> Remove <i>prefix</i> from all directory names. </p>
<p> Because lists containing long filenames are difficult to read, there is a mechanism implemented that will automatically try to shorten all directory names on the overview page beginning with a common prefix. By default, this is done using an algorithm that tries to find the prefix which, when applied, will minimize the resulting sum of characters of all directory names. </p>
<p> Use this option to specify the prefix to be removed by yourself. </p>
</dl>
<p> <code>&#8211;no-prefix</code></p>
<dl>
<dt>
<dd> Do not remove prefix from directory names. </p>
<p> This switch will completely disable the prefix mechanism described in the previous section. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_no_prefix</i>. </p>
</dl>
<p> <code>&#8211;no-source</code></p>
<dl>
<dt>
<dd> Do not create source code view. </p>
<p> Use this switch if you don&#8217;t want to get a source code view for each file. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_no_source</i>. </p>
</dl>
<p> <code>&#8211;num-spaces </code><i>spaces</i></p>
<dl>
<dt>
<dd> Replace tabs in source view with <i>num</i> spaces. </p>
<p> Default value is 8. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_num_spaces</i>. </p>
</dl>
<p> <code>&#8211;highlight</code></p>
<dl>
<dt>
<dd> Highlight lines with converted-only coverage data. </p>
<p> Use this option in conjunction with the &#8211;diff option of <code>lcov</code> to highlight those lines which were only covered in data sets which were converted from previous source code versions. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_highlight</i>. </p>
</dl>
<p> <code>&#8211;legend</code></p>
<dl>
<dt>
<dd> Include color legend in HTML output. </p>
<p> Use this option to include a legend explaining the meaning of color coding in the resulting HTML output. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_legend</i>. </p>
</dl>
<p> <code>&#8211;html-prolog </code><i>prolog-file</i></p>
<dl>
<dt>
<dd> Read customized HTML prolog from <i>prolog-file</i>. </p>
<p> Use this option to replace the default HTML prolog (the initial part of the HTML source code leading up to and including the &lt;body&gt; tag) with the contents of <i>prolog-file</i>. Within the prolog text, the following words will be replaced when a page is generated: </p>
<p> <code>@pagetitle@</code><br />
 The title of the page. </p>
<p> <code>@basedir@</code><br />
 A relative path leading to the base directory (e.g. for locating css-files). </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_html_prolog</i>. </p>
</dl>
<p> <code>&#8211;html-epilog </code><i>epilog-file</i></p>
<dl>
<dt>
<dd> Read customized HTML epilog from <i>epilog-file</i>. </p>
<p> Use this option to replace the default HTML epilog (the final part of the HTML source including &lt;/body&gt;) with the contents of <i>epilog-file</i>. </p>
<p> Within the epilog text, the following words will be replaced when a page is generated: </p>
<p> <code>@basedir@</code><br />
 A relative path leading to the base directory (e.g. for locating css-files). </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_html_epilog</i>. </p>
</dl>
<p> <code>&#8211;html-extension </code><i>extension</i></p>
<dl>
<dt>
<dd> Use customized filename extension for generated HTML pages. </p>
<p> This option is useful in situations where different filename extensions are required to render the resulting pages correctly (e.g. php). Note that a &#8216;.&#8217; will be inserted between the filename and the extension specified by this option. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_html_extension</i>.</dl>
<p> <code>&#8211;html-gzip</code></p>
<dl>
<dt>
<dd> Compress all generated html files with gzip and add a .htaccess file specifying gzip-encoding in the root output directory. </p>
<p> Use this option if you want to save space on your webserver. Requires a webserver with .htaccess support and a browser with support for gzip compressed html. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_html_gzip</i>. </p>
</dl>
<p> <code>&#8211;sort</code><br />
 <code>&#8211;no-sort</code></p>
<dl>
<dt>
<dd> Specify whether to include sorted views of file and directory overviews. </p>
<p> Use &#8211;sort to include sorted views or &#8211;no-sort to not include them. Sorted views are <code>enabled</code> by default. </p>
<p> When sorted views are enabled, each overview page will contain links to views of that page sorted by coverage rate. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_sort</i>. </p>
</dl>
<p> <code>&#8211;function-coverage</code><br />
 <code>&#8211;no-function-coverage</code></p>
<dl>
<dt>
<dd> Specify whether to display function coverage summaries in HTML output. </p>
<p> Use &#8211;function-coverage to enable function coverage summaries or &#8211;no-function-coverage to disable it. Function coverage summaries are <code>enabled</code> by default </p>
<p> When function coverage summaries are enabled, each overview page will contain the number of functions found and hit per file or directory, together with the resulting coverage rate. In addition, each source code view will contain a link to a page which lists all functions found in that file plus the respective call count for those functions. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_function_coverage</i>. </p>
</dl>
<p> <code>&#8211;branch-coverage</code><br />
 <code>&#8211;no-branch-coverage</code></p>
<dl>
<dt>
<dd> Specify whether to display branch coverage data in HTML output. </p>
<p> Use &#8211;branch-coverage to enable branch coverage display or &#8211;no-branch-coverage to disable it. Branch coverage data display is <code>enabled</code> by default </p>
<p> When branch coverage display is enabled, each overview page will contain the number of branches found and hit per file or directory, together with the resulting coverage rate. In addition, each source code view will contain an extra column which lists all branches of a line with indications of whether the branch was taken or not. Branches are shown in the following format: </p>
<p>&nbsp;<wbr>&#8216;&nbsp;<wbr>+&nbsp;<wbr>&#8216;: Branch was taken at least once </p>
<p>&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8211;&nbsp;<wbr>&#8216;: Branch was not taken </p>
<p>&nbsp;<wbr>&#8216;&nbsp;<wbr>#&nbsp;<wbr>&#8216;: The basic block containing the branch was never executed </p>
<p> Note that it might not always be possible to relate branches to the corresponding source code statements: during compilation, GCC might shuffle branches around or eliminate some of them to generate better code. </p>
<p> This option can also be configured permanently using the configuration file option <i>genhtml_branch_coverage</i>. </p>
</dl>
<p> <code>&#8211;demangle-cpp</code></p>
<dl>
<dt>
<dd> Specify whether to demangle C++ function names. </p>
<p> Use this option if you want to convert C++ internal function names to human readable format for display on the HTML function overview page. This option requires that the c++filt tool is installed (see <code>c++<a href="/docs/linux/man/1-filt/">filt</a></code>(1)). </p>
</dl>
<p> <code>&#8211;ignore-errors</code> <i>errors</i> </p>
<dl>
<dt>
<dd> Specify a list of errors after which to continue processing. </p>
<p> Use this option to specify a list of one or more classes of errors after which geninfo should continue processing instead of aborting. </p>
<p> <i>errors</i> can be a comma-separated list of the following keywords: </p>
<p> <code>source:</code> the source code file for a data set could not be found.</dl>
<p> <code>&#8211;config-file</code> <i>config-file</i> </p>
<dl>
<dt>
<dd> Specify a configuration file to use. </p>
<p> When this option is specified, neither the system-wide configuration file /etc/lcovrc, nor the per-user configuration file ~/.lcovrc is read. </p>
<p> This option may be useful when there is a need to run several instances of <code>genhtml</code> with different configuration file options in parallel.</dl>
<p> <code>&#8211;rc</code> <i>keyword</i>=<i>value</i> </p>
<dl>
<dt>
<dd> Override a configuration directive. </p>
<p> Use this option to specify a <i>keyword</i>=<i>value</i> statement which overrides the corresponding configuration statement in the lcovrc configuration file. You can specify this option more than once to override multiple configuration statements. See <code><a href="/docs/linux/man/5-lcovrc/">lcovrc</a></code>(5) for a list of available keywords and their meaning.</dl>
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
<p> <code><a href="/docs/linux/man/1-lcov/">lcov</a></code>(1), <code><a href="/docs/linux/man/5-lcovrc/">lcovrc</a></code>(5), <code><a href="/docs/linux/man/1-geninfo/">geninfo</a></code>(1), <code><a href="/docs/linux/man/1-genpng/">genpng</a></code>(1), <code><a href="/docs/linux/man/1-gendesc/">gendesc</a></code>(1), <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) </p>
<h2>Index</h2>
