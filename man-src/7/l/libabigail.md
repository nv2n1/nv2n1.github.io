---
title: "libabigail(7)"
name: "libabigail"
section: "7"
letter: "l"
url: "/docs/linux/man/7-libabigail/"
description: "libabigail – Library to analyze and compare ELF ABIs"
---

<p>libabigail &#8211; Library to analyze and compare ELF ABIs</p>
<h2>Overview Of The Abigail Framework</h2>
<p><code>ABIGAIL</code> stands for the Application Binary Interface Generic Analysis and Instrumentation Library. </p>
<p> It&#8217;s a framework which aims at helping developers and software distributors to spot some ABI-related issues like interface incompatibility in <i>ELF</i> shared libraries by performing a static analysis of the <i>ELF</i> binaries at hand. </p>
<p> The type of interface incompatibilities that <code>Abigail</code> focuses on is related to changes on the exported ELF functions and variables symbols, as well as layout and size changes of data types of the functions and variables exported by shared libraries. </p>
<p> In other words, if the return type of a function exported by a shared library changes in an incompatible way from one version of a given shared library to another, we want <code>Abigail</code> to help people catch that. </p>
<p> In more concrete terms, the Abigail framwork provides a shared library named <code>libabigail</code> which exposes an API to parse a shared library in <i>ELF</i> format (accompanied with its associated debug information in <i>DWARF</i> format) build an internal representation of all the functions and variables it exports, along with their types. <code>Libabigail</code> also builds an internal representation of the <i>ELF symbols</i> of these functions and variables. That information about these exported functions and variables is roughly what we consider as being the ABI of the shared library, at least, in the scope of <code>Libabigail</code>. </p>
<p> Aside of this internal representation, <code>libabigail</code> provides facilities to perform deep comparisons of two ABIs. That is, it can compare the types of two sets of functions or variables and represents the result in a way that allows it to emit textual reports about the differences. </p>
<p> This allows us to write tools like <code>abidiff</code> that can compare the ABI of two shared libraries and represent the result in a meaningful enough way to help us spot ABI incompatibilities. There are several <code>other tools</code> that are built using the <code>Abigail</code> framwork.</p>
<h2>Tools</h2>
<h3>Overview</h3>
<p>The upstream code repository of Libabigail contains several tools written using the library. They are maintained and released as part of the project. All tools come with a bash-completion script.</p>
<h3>Tools manuals</h3>
<h3>abidiff</h3>
<p>abidiff compares the Application Binary Interfaces (ABI) of two shared libraries in <i>ELF</i> format. It emits a meaningful report describing the differences between the two ABIs. </p>
<p> For a comprehensive ABI change report that includes changes about function and variable sub-types, the two input shared libraries must be accompanied with their debug information in <i>DWARF</i> format. Otherwise, only <i>ELF</i> symbols that were added or removed are reported.</p>
<h3>Invocation</h3>
<pre>abidiff [options] &lt;first-shared-library&gt; &lt;second-shared-library&gt;</pre>
<h3>Environment</h3>
<p>abidiff loads two default <i>suppression specifications files</i>, merges their content and use it to filter out ABI change reports that might be considered as false positives to users.</p>
<dl>
<dt>&bull;</p>
<dd>Default system-wide suppression specification file </p>
<p> It&#8217;s located by the optional environment variable LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE. If that environment variable is not set, then abidiff tries to load the suppression file $libdir/libabigail/libabigail-default.abignore. If that file is not present, then no default system-wide suppression specification file is loaded.</p>
<dt>&bull;</p>
<dd>Default user suppression specification file. </p>
<p> It&#8217;s located by the optional environment LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE. If that environment variable is not set, then abidiff tries to load the suppression file $HOME/.abignore. If that file is not present, then no default user suppression specification is loaded.</dl>
<h3>Options</h3>
<dl>
<dt>&bull;</p>
<dd><code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd><i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug-info-dir1 | &#8211;d1</code> &lt;<i>di-path1</i>&gt; </p>
<p> For cases where the debug information for <i>first-shared-library</i> is split out into a separate file, tells <code>abidiff</code> where to find that separate debug information file. </p>
<p> Note that <i>di-path</i> must point to the root directory under which the debug information is arranged in a tree-like manner. Under Red Hat based systems, that directory is usually <code>&lt;root&gt;/usr/lib/debug</code>. </p>
<p> Note also that this option is not mandatory for split debug information installed by your system&#8217;s package manager because then <code>abidiff</code> knows where to find it.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug-info-dir2 | &#8211;d2</code> &lt;<i>di-path2</i>&gt; </p>
<p> Like <code>&#8211;debug-info-dir1</code>, this options tells <code>abidiff</code> where to find the split debug information for the <i>second-shared-library</i> file.</p>
<dt>&bull;</p>
<dd><code>&#8211;headers-dir1 | &#8211;hd1</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the first shared library that the tool has to consider. The tool will thus filter out ABI changes on types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd><code>&#8211;headers-dir2 | &#8211;hd2</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the second shared library that the tool has to consider. The tool will thus filter out ABI changes on types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd><code>&#8211;dont-drop-private-types</code> </p>
<p> This option is to be used with the <code>&#8211;headers-dir1</code> and <code>&#8211;headers-dir2</code> options. Without this option, types that are <i>NOT</i> defined in the headers are entirely dropped from the internal representation build by Libabigail to represent the ABI. They thus don&#8217;t have to be filtered out from the final ABI change report because they are not even present in Libabigail&#8217;s representation. </p>
<p> With this option however, those private types are kept in the internal representation and later filtered out from the report. </p>
<p> This options thus potentially makes Libabigail to potentially consume more memory. It&#8217;s meant to be mainly used for debugging purposes.</p>
<dt>&bull;</p>
<dd><code>&#8211;stat</code> </p>
<p> Rather than displaying the detailed ABI differences between <i>first-shared-library</i> and <i>second-shared-library</i>, just display some summary statistics about these differences.</p>
<dt>&bull;</p>
<dd><code>&#8211;symtabs</code> </p>
<p> Only display the symbol tables of the <i>first-shared-library</i> and <i>second-shared-library</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;deleted-fns</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the globally defined functions that got deleted from <i>first-shared-library</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;changed-fns</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the changes in sub-types of the global functions defined in <i>first-shared-library</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;added-fns</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the globally defined functions that were added to <i>second-shared-library</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;deleted-vars</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the globally defined variables that were deleted from <i>first-shared-library</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;changed-vars</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the changes in the sub-types of the global variables defined in <i>first-shared-library</i></p>
<dt>&bull;</p>
<dd><code>&#8211;added-vars</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the global variables that were added (defined) to <i>second-shared-library</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-linkage-name</code> </p>
<p> In the resulting report, do not display the linkage names of the added, removed, or changed functions or variables.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-unreferenced-symbols</code> </p>
<p> In the resulting report, do not display change information about function and variable symbols that are not referenced by any debug information. Note that for these symbols not referenced by any debug information, the change information displayed is either added or removed symbols.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-default-suppression</code> </p>
<p> Do not load the <i>default suppression specification files</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;suppressions | &#8211;suppr</code> &lt;<i>path-to-suppressions</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppressions</i>. Note that this option can appear multiple times on the command line. In that case, all of the provided suppression specification files are taken into account. </p>
<p> Please note that, by default, if this option is not provided, then the <i>default suppression specification files</i> are loaded .</p>
<dt>&bull;</p>
<dd><code>&#8211;drop</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, drop the globally defined functions and variables which name match the regular expression <i>regex</i>. As a result, no change involving these functions or variables will be emitted in the diff report.</p>
<dt>&bull;</p>
<dd><code>&#8211;drop-fn</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, drop the globally defined functions which name match the regular expression <i>regex</i>. As a result, no change involving these functions will be emitted in the diff report.</p>
<dt>&bull;</p>
<dd><code>&#8211;drop-var</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, drop the globally defined variables matching a the regular expression <i>regex</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;keep</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, keep the globally defined functions and variables which names match the regular expression <i>regex</i>. All other functions and variables are dropped on the floor and will thus not appear in the resulting diff report.</p>
<dt>&bull;</p>
<dd><code>&#8211;keep-fn</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, keep the globally defined functions which name match the regular expression <i>regex</i>. All other functions are dropped on the floor and will thus not appear in the resulting diff report.</p>
<dt>&bull;</p>
<dd><code>&#8211;keep-var</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, keep the globally defined which names match the regular expression <i>regex</i>. All other variables are dropped on the floor and will thus not appear in the resulting diff report.</p>
<dt>&bull;</p>
<dd><code>&#8211;harmless</code> </p>
<p> In the diff report, display only the <i>harmless</i> changes. By default, the harmless changes are filtered out of the diff report keep the clutter to a minimum and have a greater change to spot real ABI issues.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-harmful</code> </p>
<p> In the diff report, do not display the <i>harmful</i> changes. By default, only the harmful changes are displayed in diff report.</p>
<dt>&bull;</p>
<dd><code>&#8211;redundant</code> </p>
<p> In the diff report, do display redundant changes. A redundant change is a change that has been displayed elsewhere in the report.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-redundant</code> </p>
<p> In the diff report, do <i>NOT</i> display redundant changes. A redundant change is a change that has been displayed elsewhere in the report. This option is switched on by default.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-architecture</code> </p>
<p> Do not take architecture in account when comparing ABIs.</p>
<dt>&bull;</p>
<dd><code>&#8211;dump-diff-tree</code> After the diff report, emit a textual representation of the diff nodes tree used by the comparison engine to represent the changed functions and variables. That representation is emitted to the error output for debugging purposes. Note that this diff tree is relevant only to functions and variables that have some sub-type changes. Added or removed functions and variables do not have any diff nodes tree associated to them.</p>
<dt>&bull;</p>
<dd><code>&#8211;stats</code> </p>
<p> Emit statistics about various internal things.</p>
<dt>&bull;</p>
<dd><code>&#8211;verbose</code> </p>
<p> Emit verbose logs about the progress of miscellaneous internal things.</dl>
<h3>Return values</h3>
<p>The exit code of the <code>abidiff</code> command is either 0 if the ABI of the binaries being compared are equal, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the exit code is a 8-bits-wide bit field in which each bit has a specific meaning. </p>
<p> The first bit, of value 1, named <code>ABIDIFF_ERROR</code> means there was an error. </p>
<p> The second bit, of value 2, named <code>ABIDIFF_USAGE_ERROR</code> means there was an error in the way the user invoked the tool. It might be set, for instance, if the user invoked the tool with an unknown command line switch, with a wrong number or argument, etc. If this bit is set, then the <code>ABIDIFF_ERROR</code> bit must be set as well. </p>
<p> The third bit, of value 4, named <code>ABIDIFF_ABI_CHANGE</code> means the ABI of the binaries being compared are different. </p>
<p> The fourth bit, of value 8, named <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code> means the ABI of the binaries compared are different in an incompatible way. If this bit is set, then the <code>ABIDIFF_ABI_CHANGE</code> bit must be set as well. If the <code>ABIDIFF_ABI_CHANGE</code> is set and the <code>ABIDIFF_INCOMPATIBLE_CHANGE</code> is <i>NOT</i> set, then it means that the ABIs being compared might or might not be compatible. In that case, a human being needs to review the ABI changes to decide if they are compatible or not. </p>
<p> Note that, at the moment, there are only a few kinds of ABI changes that would result in setting the flag <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code>. Those ABI changes are either:</p>
<dl>
<dt>&bull;</p>
<dd>the removal of the symbol of a function or variable that has been defined and exported.</p>
<dt>&bull;</p>
<dd>the modification of the index of a member of a virtual function table (for C++ programs and libraries). </p>
<p> With time, when more ABI change patterns are found to <i>always</i> constitute incompatible ABI changes, we will adapt the code to recognize those cases and set the <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code> accordingly. So, if you find such patterns, please let us know. </p>
<p> The remaining bits are not used for the moment.</dl>
<h3>Usage examples</h3>
<dl>
<dt>1.</p>
<dd>Detecting a change in a sub-type of a function: </p>
<pre>$ cat -n test-v0.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
 3
 4 struct S0
 5 {
 6 int m0;
 7 };
 8
 9 void
 10 foo(S0* /*parameter_name*/)
 11 {
 12 // do something with parameter_name.
 13 }
$
$ cat -n test-v1.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
 3
 4 struct type_base
 5 {
 6 int inserted;
 7 };
 8
 9 struct S0 : public type_base
 10 {
 11 int m0;
 12 };
 13
 14 void
 15 foo(S0* /*parameter_name*/)
 16 {
 17 // do something with parameter_name.
 18 }
$
$ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
$ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
$
$ ../build/tools/abidiff libtest-v0.so libtest-v1.so
Functions changes summary: 0 Removed, 1 Changed, 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function void foo(S0*)' has some indirect sub-type changes:
 parameter 0 of type 'S0*' has sub-type changes:
 in pointed to type 'struct S0':
 size changed from 32 to 64 bits
 1 base class insertion:
 struct type_base
 1 data member change:
 'int S0::m0' offset changed from 0 to 32
$</pre>
<dt>2.</p>
<dd>Detecting another change in a sub-type of a function: </p>
<pre>$ cat -n test-v0.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
 3
 4 struct S0
 5 {
 6 int m0;
 7 };
 8
 9 void
 10 foo(S0&amp; /*parameter_name*/)
 11 {
 12 // do something with parameter_name.
 13 }
$
$ cat -n test-v1.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
 3
 4 struct S0
 5 {
 6 char inserted_member;
 7 int m0;
 8 };
 9
 10 void
 11 foo(S0&amp; /*parameter_name*/)
 12 {
 13 // do something with parameter_name.
 14 }
$
$ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
$ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
$
$ ../build/tools/abidiff libtest-v0.so libtest-v1.so
Functions changes summary: 0 Removed, 1 Changed, 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function void foo(S0&amp;)' has some indirect sub-type changes:
 parameter 0 of type 'S0&amp;' has sub-type changes:
 in referenced type 'struct S0':
 size changed from 32 to 64 bits
 1 data member insertion:
 'char S0::inserted_member', at offset 0 (in bits)
 1 data member change:
 'int S0::m0' offset changed from 0 to 32
$</pre>
<dt>3.</p>
<dd>Detecting that functions got removed or added to a library: </p>
<pre>$ cat -n test-v0.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
 3
 4 struct S0
 5 {
 6 int m0;
 7 };
 8
 9 void
 10 foo(S0&amp; /*parameter_name*/)
 11 {
 12 // do something with parameter_name.
 13 }
$
$ cat -n test-v1.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
 3
 4 struct S0
 5 {
 6 char inserted_member;
 7 int m0;
 8 };
 9
 10 void
 11 bar(S0&amp; /*parameter_name*/)
 12 {
 13 // do something with parameter_name.
 14 }
$
$ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
$ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
$
$ ../build/tools/abidiff libtest-v0.so libtest-v1.so
Functions changes summary: 1 Removed, 0 Changed, 1 Added functions
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 Removed function:
 'function void foo(S0&amp;)' {_Z3fooR2S0}
1 Added function:
 'function void bar(S0&amp;)' {_Z3barR2S0}
$</pre>
</dl>
<h3>abipkgdiff</h3>
<p><code>abipkgdiff</code> compares the Application Binary Interfaces (ABI) of the <i>ELF</i> binaries contained in two software packages. The software package formats currently supported are <i>Deb</i>, <i>RPM</i>, <i>tar</i> archives (either compressed or not) and plain directories that contain binaries. </p>
<p> For a comprehensive ABI change report that includes changes about function and variable sub-types, the two input packages must be accompanied with their debug information packages that contain debug information in <i>DWARF</i> format.</p>
<h3>Invocation</h3>
<pre>abipkgdiff [option] &lt;package1&gt; &lt;package2&gt;</pre>
<p><code>package1</code> and <code>package2</code> are the packages that contain the binaries to be compared.</p>
<h3>Environment</h3>
<p>abipkgdiff loads two default <i>suppression specifications files</i>, merges their content and use it to filter out ABI change reports that might be considered as false positives to users.</p>
<dl>
<dt>&bull;</p>
<dd>Default system-wide suppression specification file </p>
<p> It&#8217;s located by the optional environment variable LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE. If that environment variable is not set, then abipkgdiff tries to load the suppression file $libdir/libabigail/libabigail-default.abignore. If that file is not present, then no default system-wide suppression specification file is loaded.</p>
<dt>&bull;</p>
<dd>Default user suppression specification file. </p>
<p> It&#8217;s located by the optional environment LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE. If that environment variable is not set, then abipkgdiff tries to load the suppression file $HOME/.abignore. If that file is not present, then no default user suppression specification is loaded.</dl>
<h3>Options</h3>
<dl>
<dt>&bull;</p>
<dd><code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd><i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug-info-pkg1 | &#8211;d1</code> &lt;path&gt; </p>
<p> For cases where the debug information for <i>package1</i> is split out into a separate file, tells <code>abipkgdiff</code> where to find that separate debug information package.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug-info-pkg2 | &#8211;d2</code> &lt;path&gt; </p>
<p> For cases where the debug information for <i>package2</i> is split out into a separate file, tells <code>abipkgdiff</code> where to find that separate debug information package.</p>
<dt>&bull;</p>
<dd><code>&#8211;devel-pkg1 | &#8211;devel1</code> &lt;path&gt; </p>
<p> Specifies where to find the <i>Development Package</i> associated with the first package to be compared. That <i>Development Package</i> at <code>path</code> should at least contain header files in which public types exposed by the libraries (of the first package to be compared) are defined. When this option is provided, the tool filters out reports about ABI changes to types that are <i>NOT</i> defined in these header files.</p>
<dt>&bull;</p>
<dd><code>&#8211;devel-pkg2 | &#8211;devel2</code> &lt;path&gt; </p>
<p> Specifies where to find the <i>Development Package</i> associated with the second package to be compared. That <i>Development Package</i> at <code>path</code> should at least contains header files in which public types exposed by the libraries (of the second package to be compared) are defined. When this option is provided, the tool filters out reports about ABI changes to types that are <i>NOT</i> defined in these header files.</p>
<dt>&bull;</p>
<dd><code>&#8211;dso-only</code> </p>
<p> Compare ELF files that are shared libraries, only. Do not compare executable files, for instance.</p>
<dt>&bull;</p>
<dd><code>&#8211;redundant</code> In the diff reports, do display redundant changes. A redundant change is a change that has been displayed elsewhere in a given report.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-linkage-name</code> </p>
<p> In the resulting report, do not display the linkage names of the added, removed, or changed functions or variables.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-added-syms</code> </p>
<p> Do not show the list of functions, variables, or any symbol that was added.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-added-binaries</code> </p>
<p> Do not show the list of binaries that got added to the second package. </p>
<p> Please note that the presence of such added binaries is not considered like an ABI change by this tool; as such, it doesn&#8217;t have any impact on the exit code of the tool. It does only have an informational value. Removed binaries are, however, considered as an ABI change.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-abignore</code> </p>
<p> Do not search the <i>package2</i> for the presence of suppression files.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-parallel</code> </p>
<p> By default, <code>abipkgdiff</code> will use all the processors it has available to execute concurrently. This option tells it not to extract packages or run comparisons in parallel.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-default-suppression</code> </p>
<p> Do not load the <i>default suppression specification files</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;suppressions | &#8211;suppr</code> &lt;<i>path-to-suppressions</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppressions</i>. Note that this option can appear multiple times on the command line. In that case, all of the suppression specification files are taken into account. </p>
<p> Please note that, by default, if this option is not provided, then the <i>default suppression specification files</i> are loaded .</p>
<dt>&bull;</p>
<dd><code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd><code>&#8211;show-identical-binaries</code> Show the names of the all binaries compared, including the binaries whose ABI compare equal. By default, when this option is not provided, only binaries with ABI changes are mentionned in the output.</p>
<dt>&bull;</p>
<dd><code>&#8211;fail-no-dbg</code> </p>
<p> Make the program fail and return a non-zero exit code if couldn&#8217;t read any of the debug information that comes from the debug info packages that were given on the command line. If no debug info package were provided on the command line then this option is not active. </p>
<p> Note that the non-zero exit code returned by the program as a result of this option is the constant <code>ABIDIFF_ERROR</code>. To know the numerical value of that constant, please refer to the <i>exit code documentation</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;keep-tmp-files</code> </p>
<p> Do not erase the temporary directory files that are created during the execution of the tool.</p>
<dt>&bull;</p>
<dd><code>&#8211;verbose</code> </p>
<p> Emit verbose progress messages.</dl>
<h3>Return value</h3>
<p>The exit code of the <code>abipkgdiff</code> command is either 0 if the ABI of the binaries compared are equal, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the value of the exit code is the same as for the <i>abidiff tool</i>.</p>
<h3>abicompat</h3>
<p>abicompat checks that an application that links against a given shared library is still ABI compatible with a subsequent version of that library. If the new version of the library introduces an ABI incompatibility, then abicompat hints the user at what exactly that incompatibility is.</p>
<h3>Invocation</h3>
<pre>abicompat [options] [&lt;application&gt; &lt;shared-library-first-version&gt; &lt;shared-library-second-version&gt;]</pre>
<h3>Options</h3>
<dl>
<dt>&bull;</p>
<dd><code>&#8211;help</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd><i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;list-undefined-symbols | -u</code> </p>
<p> Display the list of undefined symbols of the application and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;show-base-names | -b</code> </p>
<p> In the resulting report emitted by the tool, this option makes the application and libraries be referred to by their base names only; not by a full absolute name. This can be useful for use in scripts that wants to compare names of the application and libraries independently of what their directory names are.</p>
<dt>&bull;</p>
<dd><code>&#8211;app-debug-info-dir | &#8211;appd</code> &lt;path-to-app-debug-info-directory&gt; </p>
<p> Set the path to the directory under which the debug information of the application is supposed to be laid out. This is useful for application binaries for which the debug info is in a separate set of files.</p>
<dt>&bull;</p>
<dd><code>&#8211;lib-debug-info-dir1 | &#8211;libd1</code> &lt;path-to-lib1-debug-info&gt; </p>
<p> Set the path to the directory under which the debug information of the first version of the shared library is supposed to be laid out. This is useful for shared library binaries for which the debug info is in a separate set of files.</p>
<dt>&bull;</p>
<dd><code>&#8211;lib-debug-info-dir2 | &#8211;libd2</code> &lt;path-to-lib1-debug-info&gt; </p>
<p> Set the path to the directory under which the debug information of the second version of the shared library is supposed to be laid out. This is useful for shared library binaries for which the debug info is in a separate set of files.</p>
<dt>&bull;</p>
<dd><code>&#8211;suppressions | &#8211;suppr</code> &lt;<i>path-to-suppressions</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppressions</i>. Note that this option can appear multiple times on the command line; all the suppression specification files are then taken into account.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd><code>&#8211;weak-mode</code> </p>
<p> This triggers the weak mode of <code>abicompat</code>. In this mode, only one version of the library is required. That is, abicompat is invoked like this: </p>
<pre>abicompat --weak-mode &lt;the-application&gt; &lt;the-library&gt;</pre>
<p>Note that the <code>&#8211;weak-mode</code> option can even be omitted if only one version of the library is given, along with the application; in that case, <code>abicompat</code> automatically switches to operate in weak mode: </p>
<pre>abicompat &lt;the-application&gt; &lt;the-library&gt;</pre>
<p>In this weak mode, the types of functions and variables exported by the library and consumed by the application (as in, the symbols of the these functions and variables are undefined in the application and are defined and exported by the library) are compared to the version of these types as expected by the application. And if these two versions of types are different, <code>abicompat</code> tells the user what the differences are. </p>
<p> In other words, in this mode, <code>abicompat</code> checks that the types of the functions and variables exported by the library mean the same thing as what the application expects, as far as the ABI is concerned. </p>
<p> Note that in this mode, <i>abicompat</i> doesn&#8217;t detect exported functions or variables (symbols) that are expected by the application but that are removed from the library. That is why it is called <code>weak</code> mode.</dl>
<h3>Return values</h3>
<p>The exit code of the <code>abicompat</code> command is either 0 if the ABI of the binaries being compared are equal, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the exit code is a 8-bits-wide bit field in which each bit has a specific meaning. </p>
<p> The first bit, of value 1, named <code>ABIDIFF_ERROR</code> means there was an error. </p>
<p> The second bit, of value 2, named <code>ABIDIFF_USAGE_ERROR</code> means there was an error in the way the user invoked the tool. It might be set, for instance, if the user invoked the tool with an unknown command line switch, with a wrong number or argument, etc. If this bit is set, then the <code>ABIDIFF_ERROR</code> bit must be set as well. </p>
<p> The third bit, of value 4, named <code>ABIDIFF_ABI_CHANGE</code> means the ABI of the binaries being compared are different. </p>
<p> The fourth bit, of value 8, named <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code> means the ABI of the binaries compared are different in an incompatible way. If this bit is set, then the <code>ABIDIFF_ABI_CHANGE</code> bit must be set as well. If the <code>ABIDIFF_ABI_CHANGE</code> is set and the <code>ABIDIFF_INCOMPATIBLE_CHANGE</code> is <i>NOT</i> set, then it means that the ABIs being compared might or might not be compatible. In that case, a human being needs to review the ABI changes to decide if they are compatible or not. </p>
<p> The remaining bits are not used for the moment.</p>
<h3>Usage examples</h3>
<dl>
<dt>&bull;</p>
<dd>Detecting a possible ABI incompatibility in a new shared library version: </p>
<pre>$ cat -n test0.h
 1 struct foo
 2 {
 3 int m0;
 4
 5 foo()
 6 : m0()
 7 {}
 8 };
 9
 10 foo*
 11 first_func();
 12
 13 void
 14 second_func(foo&amp;);
 15
 16 void
 17 third_func();
$
$ cat -n test-app.cc
 1 // Compile with:
 2 // g++ -g -Wall -o test-app -L. -ltest-0 test-app.cc
 3
 4 #include &quot;test0.h&quot;
 5
 6 int
 7 main()
 8 {
 9 foo* f = first_func();
 10 second_func(*f);
 11 return 0;
 12 }
$
$ cat -n test0.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-0.so test0.cc
 3
 4 #include &quot;test0.h&quot;
 5
 6 foo*
 7 first_func()
 8 {
 9 foo* f = new foo();
 10 return f;
 11 }
 12
 13 void
 14 second_func(foo&amp;)
 15 {
 16 }
 17
 18 void
 19 third_func()
 20 {
 21 }
$
$ cat -n test1.h
 1 struct foo
 2 {
 3 int m0;
 4 char m1; /* &lt;-- a new member got added here! */
 5
 6 foo()
 7 : m0(),
 8 m1()
 9 {}
 10 };
 11
 12 foo*
 13 first_func();
 14
 15 void
 16 second_func(foo&amp;);
 17
 18 void
 19 third_func();
$
$ cat -n test1.cc
 1 // Compile this with:
 2 // g++ -g -Wall -shared -o libtest-1.so test1.cc
 3
 4 #include &quot;test1.h&quot;
 5
 6 foo*
 7 first_func()
 8 {
 9 foo* f = new foo();
 10 return f;
 11 }
 12
 13 void
 14 second_func(foo&amp;)
 15 {
 16 }
 17
 18 /* Let's comment out the definition of third_func()
 19 void
 20 third_func()
 21 {
 22 }
 23 */
$</pre>
<dt>&bull;</p>
<dd>Compile the first and second versions of the libraries: <code>libtest-0.so</code> and <code>libtest-1.so</code>: </p>
<pre>$ g++ -g -Wall -shared -o libtest-0.so test0.cc
$ g++ -g -Wall -shared -o libtest-1.so test1.cc</pre>
<dt>&bull;</p>
<dd>Compile the application and link it against the first version of the library, creating the <code>test-app</code> binary: </p>
<pre>$ g++ -g -Wall -o test-app -L. -ltest-0.so test-app.cc</pre>
<dt>&bull;</p>
<dd>Now, use <code>abicompat</code> to see if libtest-1.so is ABI compatible with app, with respect to the ABI of libtest-0.so: </p>
<pre>$ abicompat test-app libtest-0.so libtest-1.so
ELF file 'test-app' might not be ABI compatible with 'libtest-1.so' due to differences with 'libtest-0.so' below:
Functions changes summary: 0 Removed, 2 Changed, 0 Added functions
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
2 functions with some indirect sub-type change:
 [C]'function foo* first_func()' has some indirect sub-type changes:
 return type changed:
 in pointed to type 'struct foo':
 size changed from 32 to 64 bits
 1 data member insertion:
 'char foo::m1', at offset 32 (in bits)
 [C]'function void second_func(foo&amp;)' has some indirect sub-type changes:
 parameter 0 of type 'foo&amp;' has sub-type changes:
 referenced type 'struct foo' changed, as reported earlier
$</pre>
<dt>&bull;</p>
<dd>Now use the weak mode of abicompat, that is, providing just the application and the new version of the library: </p>
<pre>$ abicompat --weak-mode test-app libtest-1.so
functions defined in library
 'libtest-1.so'
have sub-types that are different from what application
 'test-app'
expects:
 function foo* first_func():
 return type changed:
 in pointed to type 'struct foo':
 size changed from 32 to 64 bits
 1 data member insertion:
 'char foo::m1', at offset 32 (in bits)
$</pre>
</dl>
<h3>abidw</h3>
<p>abidw reads a shared library in <i>ELF</i> format and emits an XML representation of its ABI to standard output. The emitted representation includes all the globally defined functions and variables, along with a complete representation of their types. It also includes a representation of the globally defined ELF symbols of the file. The input shared library must contain associated debug information in <i>DWARF</i> format.</p>
<h3>Invocation</h3>
<pre>abidw [options] [&lt;path-to-elf-file&gt;]</pre>
<h3>Options</h3>
<dl>
<dt>&bull;</p>
<dd><code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd><i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug-info-dir | -d</code> &lt;<i>dir-path</i>&gt; </p>
<p> In cases where the debug info for <i>path-to-elf-file</i> is in a separate file that is located in a non-standard place, this tells <code>abidw</code> where to look for that debug info file. </p>
<p> Note that <i>dir-path</i> must point to the root directory under which the debug information is arranged in a tree-like manner. Under Red Hat based systems, that directory is usually <code>&lt;root&gt;/usr/lib/debug</code>. </p>
<p> Note that this option is not mandatory for split debug information installed by your system&#8217;s package manager because then <code>abidw</code> knows where to find it.</p>
<dt>&bull;</p>
<dd><code>&#8211;out-file</code> &lt;<i>file-path</i>&gt; </p>
<p> This option instructs <code>abidw</code> to emit the XML representation of <i>path-to-elf-file</i> into the file <i>file-path</i>, rather than emitting it to its standard output.</p>
<dt>&bull;</p>
<dd><code>&#8211;noout</code> </p>
<p> This option instructs <code>abidw</code> to not emit the XML representation of the ABI. So it only reads the ELF and debug information, builds the internal representation of the ABI and exits. This option is usually useful for debugging purposes.</p>
<dt>&bull;</p>
<dd><code>&#8211;suppressions | suppr</code> &lt;<i>path-to-suppression-specifications-file</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppression-specifications-file</i>. Note that this option can appear multiple times on the command line. In that case, all of the provided suppression specification files are taken into account. ABI artifacts matched by the suppression specifications are suppressed from the output of this tool.</p>
<dt>&bull;</p>
<dd><code>&#8211;headers-dir | &#8211;hd</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the first shared library that the tool has to consider. The tool will thus filter out types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd><code>&#8211;check-alternate-debug-info</code> &lt;<i>elf-path</i>&gt; </p>
<p> If the debug info for the file <i>elf-path</i> contains a reference to an <i>alternate debug info</i> file, <code>abidw</code> checks that it can find that alternate debug info file. In that case, it emits a meaningful success message mentioning the full path to the alternate debug info file found. Otherwise, it emits an error code.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd><code>&#8211;check-alternate-debug-info-base-name</code> &lt;<i>elf-path</i>&gt; </p>
<p> Like <code>&#8211;check-alternate-debug-info</code>, but in the success message, only mention the base name of the debug info file; not its full path.</p>
<dt>&bull;</p>
<dd><code>&#8211;load-all-types</code> </p>
<p> By default, <code>libabigail</code> (and thus <code>abidw</code>) only loads types that are reachable from functions and variables declarations that are publicly defined and exported by the binary. So only those types are present in the output of <code>abidw</code>. This option however makes <code>abidw</code> load <i>all</i> the types defined in the binaries, even those that are not reachable from public declarations.</p>
<dt>&bull;</p>
<dd><code>&#8211;abidiff</code> Load the ABI of the ELF binary given in argument, save it in libabigail&#8217;s XML format in a temporary file; read the ABI from the temporary XML file and compare the ABI that has been read back against the ABI of the ELF binary given in argument. The ABIs should compare equal. If they don&#8217;t, the program emits a diagnostic and exits with a non-zero code. </p>
<p> This is a debugging and sanity check option.</p>
<dt>&bull;</p>
<dd><code>&#8211;stats</code> </p>
<p> Emit statistics about various internal things.</p>
<dt>&bull;</p>
<dd><code>&#8211;verbose</code> </p>
<p> Emit verbose logs about the progress of miscellaneous internal things.</dl>
<h3>Notes</h3>
<h3>Alternate debug info files</h3>
<p>As of the version 4 of the DWARF specification, <i>Alternate debug information</i> is a <i>GNU</i> extension to the DWARF specification. It has however been proposed for inclusion into the upcoming version 5 of the DWARF standard. You can read more about the GNU extensions to the DWARF standard <i>here</i>.</p>
<h3>abilint</h3>
<p>abilint parses the native XML representation of an ABI as emitted by <code>abidw</code>. Once it has parsed the XML representation of the ABI, <code>abilint</code> builds and in-memory model from it. It then tries to save it back to an XML form, to standard output. If that read-write operation succeeds chances are the input XML ABI representation is meaningful. </p>
<p> Note that the main intent of this tool to help debugging issues in the underlying Libabigail library. </p>
<p> Note also that <code>abilint</code> can also read an <i>ELF</i> input file, build the in-memory model for its ABI, and serialize that model back into XML to standard output. In that case, the <i>ELF</i> input file must be accompanied with its debug information in the <i>DWARF</i> format.</p>
<h3>Invocation</h3>
<pre>abilint [options] [&lt;abi-file1&gt;]</pre>
<h3>Options</h3>
<dl>
<dt>&bull;</p>
<dd><code>&#8211;help</code> </p>
<p> Display a short help message and exits.</p>
<dt>&bull;</p>
<dd><i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug-info-dir</code> &lt;<i>path</i>&gt; </p>
<p> When reading an <i>ELF</i> input file which debug information is split out into a separate file, this options tells <code>abilint</code> where to find that separate debug information file. </p>
<p> Note that <i>path</i> must point to the root directory under which the debug information is arranged in a tree-like manner. Under Red Hat based systems, that directory is usually <code>&lt;root&gt;/usr/lib/debug</code>. </p>
<p> Note also that this option is not mandatory for split debug information installed by your system&#8217;s package manager because then <code>abidiff</code> knows where to find it.</p>
<dt>&bull;</p>
<dd><code>&#8211;diff</code> </p>
<p> For XML inputs, perform a text diff between the input and the memory model saved back to disk. This can help to spot issues in the handling of the XML format by the underlying Libabigail library.</p>
<dt>&bull;</p>
<dd><code>&#8211;noout</code> </p>
<p> Do not display anything on standard output. The return code of the command is the only way to know if the command succeeded.</p>
<dt>&bull;</p>
<dd><code>&#8211;suppressions | suppr</code> &lt;<i>path-to-suppression-specifications-file</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppression-specifications-file</i>. Note that this option can appear multiple times on the command line. In that case, all of the provided suppression specification files are taken into account. ABI artifacts matched by the suppression specifications are suppressed from the output of this tool.</p>
<dt>&bull;</p>
<dd><code>&#8211;headers-dir | &#8211;hd</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the first shared library that the tool has to consider. The tool will thus filter out types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd><code>&#8211;stdin | &#8212;</code> </p>
<p> Read the input content from standard input.</p>
<dt>&bull;</p>
<dd><code>&#8211;tu</code> </p>
<p> Expect the input XML to represent a single translation unit.</dl>
<h3>fedabipkgdiff</h3>
<p><code>fedabipkgdiff</code> compares the ABI of shared libraries in <i>Fedora</i> packages. It&#8217;s a convenient way to do so without having to manually download packages from the <i>Fedora Build System</i>. </p>
<p> <code>fedabipkgdiff</code> knows how to talk with the <i>Fedora Build System</i> to find the right packages versions, their associated debug information and development packages, download them, compare their ABI locally, and report about the possible ABI changes. </p>
<p> Note that by default, this tool reports ABI changes about types that are defined in public header files found in the development packages associated with the packages being compared. It also reports ABI changes about functions and global variables whose symbols are defined and exported in the ELF binaries found in the packages being compared.</p>
<h3>Invocation</h3>
<pre>fedabipkgdiff [option] &lt;NVR&gt; ...</pre>
<h3>Environment</h3>
<p>fedabipkgdiff loads two default <i>suppression specifications files</i>, merges their content and use it to filter out ABI change reports that might be considered as false positives to users.</p>
<dl>
<dt>&bull;</p>
<dd>Default system-wide suppression specification file </p>
<p> It&#8217;s located by the optional environment variable LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE. If that environment variable is not set, then fedabipkgdiff tries to load the suppression file $libdir/libabigail/libabigail-default.abignore. If that file is not present, then no default system-wide suppression specification file is loaded.</p>
<dt>&bull;</p>
<dd>Default user suppression specification file. </p>
<p> It&#8217;s located by the optional environment LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE. If that environment variable is not set, then fedabipkgdiff tries to load the suppression file $HOME/.abignore. If that file is not present, then no default user suppression specification is loaded.</dl>
<h3>Options</h3>
<dl>
<dt>&bull;</p>
<dd><code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd><code>&#8211;dry-run</code> </p>
<p> Don&#8217;t actually perform the ABI comparison. Details about what is going to be done are emitted on standard output.</p>
<dt>&bull;</p>
<dd><code>&#8211;debug</code> </p>
<p> Emit debugging messages about the execution of the program. Details about each method invocation, including input parameters and returned values, are emitted.</p>
<dt>&bull;</p>
<dd><code>&#8211;traceback</code> </p>
<p> Show traceback when an exception raised. This is useful for developers of the tool itself to know more exceptional errors.</p>
<dt>&bull;</p>
<dd><code>&#8211;server</code> &lt;URL&gt; </p>
<p> Specifies the URL of the <i>Koji</i> XMLRPC service the tool talks to. The default value of this option is <i><a rel="nofollow" href="http://koji.fedoraproject.org/kojihub">http://koji.fedoraproject.org/kojihub</a></i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;topdir</code> &lt;URL&gt; </p>
<p> Specifies the URL of the package store the tool downloads RPMs from. The default value of this option is <i><a rel="nofollow" href="https://kojipkgs.fedoraproject.org">https://kojipkgs.fedoraproject.org</a></i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;from</code> &lt;distro&gt; </p>
<p> Specifies the name of the baseline <i>Fedora</i> distribution in which to find the first <i>build</i> that is used for comparison. The <code>distro</code> value can be any valid value of the RPM macro <code>%{?dist}</code> for <i>Fedora</i>, for example, <code>fc4</code>, <code>fc23</code>, <code>fc25</code>.</p>
<dt>&bull;</p>
<dd><code>&#8211;to</code> &lt;distro&gt; </p>
<p> Specifies the name of the <i>Fedora</i> distribution in which to find the <i>build</i> that is compared against the baseline specified by option <code>&#8211;from</code>. The <code>distro</code> value could be any valid value of the RPM macro <code>%{?dist}</code> for <i>Fedora</i>, for example, <code>fc4</code>, <code>fc23</code>.</p>
<dt>&bull;</p>
<dd><code>&#8211;all-subpackages</code> </p>
<p> Instructs the tool to also compare the ABI of the binaries in the sub-packages of the packages specified.</p>
<dt>&bull;</p>
<dd><code>&#8211;dso-only</code> </p>
<p> Compares the ABI of shared libraries only. If this option is not provided, the tool compares the ABI of all ELF binaries found in the packages.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-default-suppression</code> </p>
<p> Do not load the <i>default suppression specification files</i>.</p>
<dt>&bull;</p>
<dd><code>&#8211;no-devel-pkg</code> </p>
<p> Do not take associated development packages into account when performing the ABI comparison. This makes the tool report ABI changes about all types that are reachable from functions and global variables which symbols are defined and publicly exported in the binaries being compared, even if those types are not defined in public header files available from the packages being compared.</p>
<dt>&bull;</p>
<dd><code>&#8211;show-identical-binaries</code> Show the names of the all binaries compared, including the binaries whose ABI compare equal. By default, when this option is not provided, only binaries with ABI changes are mentionned in the output.</p>
<dt>&bull;</p>
<dd><code>&#8211;abipkgdiff</code> &lt;path/to/abipkgdiff&gt; </p>
<p> Specify an alternative abipkgdiff instead of the one installed in system. </p>
<p> Note that a build is a specific version and release of an RPM package. It&#8217;s specified by its the package name, version and release. These are specified by the <i>Fedora Naming Guidelines</i></dl>
<h3>Return value</h3>
<p>The exit code of the <code>abipkgdiff</code> command is either 0 if the ABI of the binaries compared are equivalent, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the value of the exit code is the same as for the <i>abidiff tool</i>.</p>
<h3>Use cases</h3>
<p>Below are some usage examples currently supported by <code>fedabipkgdiff</code>.</p>
<dl>
<dt>1.</p>
<dd>Compare the ABI of binaries in a local package against the ABI of the latest stable package in <i>Fedora</i> 23. </p>
<p> Suppose you have built just built the <code>httpd</code> package and you want to compare the ABI of the binaries in this locally built package against the ABI of the binaries in the latest <code>http</code> build from <i>Fedora</i> 23. The command line invocation would be: </p>
<pre>$ fedabipkgdiff --from fc23 ./httpd-2.4.18-2.fc24.x86_64.rpm</pre>
<dt>2.</p>
<dd>Compare the ABI of binaries in the latest build of the <code>httpd</code> package in <code>Fedora 23</code> against the ABI of the binaries in the latest build of the same package in 24. </p>
<p> In this case, note that neither of the two packages are available locally. The tool is going to talk with the <i>Fedora Build System</i>, determine what the versions and releases of the latest packages are, download them and perform the comparison locally. The command line invocation would be: </p>
<pre>$ fedabipkgdiff --from fc23 --to fc24 httpd</pre>
<dt>3.</p>
<dd>Compare the ABI of binaries of two builds of the <code>httpd</code> package, designated their versions and releases. </p>
<p> If we want to do perform the ABI comparison for all the processor architectures supported by <i>Fedora</i> the command line invocation would be: </p>
<pre>$ fedabipkgdiff httpd-2.8.14.fc23 httpd-2.8.14.fc24</pre>
<p>But if we want to perform the ABI comparison for a specific architecture, say, x86_64, then the command line invocation would be: </p>
<pre>$ fedabipkgdiff httpd-2.8.14.fc23.x86_64 httpd-2.8.14.fc24.x86_64</pre>
<dt>4.</p>
<dd>If the use wants to also compare the sub-packages of a given package, she can use the &#8211;all-subpackages option. The first command of the previous example would thus look like: </p>
<pre>$ fedabipkgdiff --all-subpackages httpd-2.8.14.fc23 httpd-2.8.14.fc24</pre>
</dl>
<h2>Concepts</h2>
<h3>ABI artifacts</h3>
<p>An ABI artifact is a relevant part of the ABI of a shared library or program. Examples of ABI artifacts are exported types, variables, functions, or <i>ELF</i> symbols exported by a shared library. </p>
<p> The set of ABI artifact for a binary is called an ABI Corpus.</p>
<h3>Harmful changes</h3>
<p>A change in the diff report is considered harmful if it might cause ABI compatibility issues. That is, it might prevent an application dynamically linked against a given version of a library to keep working with the changed subsequent versions of the same library.</p>
<h3>Harmless changes</h3>
<p>A change in the diff report is considered harmless if it will not cause any ABI compatibility issue. That is, it will not prevent an application dynamically linked against given version of a library to keep working with the changed subsequent versions of the same library. </p>
<p> By default, <code>abidiff</code> filters harmless changes from the diff report.</p>
<h3>Suppression specifications</h3>
<h3>Definition</h3>
<p>A suppression specification file is a way for a user to instruct <i>abidiff</i>, <i>abipkgdiff</i> or any other relevant libabigail tool to avoid emitting reports for changes involving certain <i>ABI artifacts</i>. </p>
<p> It contains directives (or specifications) that describe the set of ABI artifacts to avoid emitting change reports about.</p>
<h3>Introductory examples</h3>
<p>Its syntax is based on a simplified and customized form of <i>Ini File Syntax</i>. For instance, to specify that change reports on a type named FooPrivateType should be suppressed, one could write this suppression specification: </p>
<pre>[suppress_type]
 name = FooPrivateType</pre>
<p>If we want to ensure that only change reports about structures named FooPrivateType should be suppressed, we could write: </p>
<pre>[suppress_type]
 type_kind = struct
 name = FooPrivateType</pre>
<p>But we could also want to suppress change reports avoid typedefs named FooPrivateType. In that case we would write: </p>
<pre>[suppress_type]
 type_kind = typedef
 name = FooPrivateType</pre>
<p>Or, we could want to suppress change reports about all struct which names end with the string &quot;PrivateType&quot;: </p>
<pre>[suppress_type]
 type_kind = struct
 name_regexp = ^.*PrivateType</pre>
<p>Let&#8217;s now look at the generic syntax of suppression specification files.</p>
<h3>Syntax</h3>
<h3>Properties</h3>
<p>More generally, the format of suppression lists is organized around the concept of <i>property</i>. Every property has a name and a value, delimited by the <code>=</code> sign. E.g: </p>
<pre>name = value</pre>
<p>Leading and trailing white spaces are ignored around property names and values.</p>
<h3>Regular expressions</h3>
<p>The value of some properties might be a regular expression. In that case, they must comply with the syntax of <i>extended POSIX regular expressions</i>. Note that Libabigail uses the regular expression engine of the <i>GNU C Library</i>.</p>
<h3>Escaping a character in a regular expression</h3>
<p>When trying to match a string that contains a <code>*</code> character, like in the pointer type <code>int*</code>, one must be careful to notice that the character <code>*</code> is a special character in the extended POSIX regular expression syntax. And that character must be escaped for the regular expression engine. Thus the regular expression that would match the string <code>int*</code> in a suppression file should be </p>
<pre>int\*</pre>
<p>Wait; but then why the two <code>\</code> characters? Well, because the <code>\</code> character is a special character in the <i>Ini File Syntax</i> used for specifying suppressions. So it must be escaped as well, so that the Ini File parser leaves a <code>\</code> character intact in the data stream that is handed to the regular expression engine. Hence the <code>\</code> targeted at the Ini File parser. </p>
<p> So, in short, to escape a character in a regular expression, always prefix the character with the <code>\</code> sequence.</p>
<h3>Modus operandi</h3>
<p>Suppression specifications can be applied at two different points of the processing pipeline of libabigail. </p>
<p> In the default operating mode called &quot;late suppression mode&quot;, suppression specifications are applied to the result of comparing the in-memory internal representations of two ABIs. In this mode, if an ABI artifact matches a suppression specification, its changes are not mentioned in the ABI change report. The internal representation of the &quot;suppressed&quot; changed ABI artifact is still present in memory; it is just not mentioned in the ABI change report. The change report can still mention statistics about the number of changed ABI artifacts that were suppressed. </p>
<p> There is another operating mode called the &quot;early suppression mode&quot; where suppression specifications are applied during the construction of the in-memory internal representation of a given ABI. In that mode, if an ABI artifact matches a suppression specification, no in-memory internal representation is built for it. As a result, no change about the matched ABI artifact is going to be mentioned in the ABI change report and no statistic about the number of suppressed ABI changes is available. Also, please note that because suppressed ABI artifacts are removed from the in-memory internal representation in this mode, the amount memory used by the internal representation is potentially smaller than the memory consumption in the late suppression mode.</p>
<h3>Sections</h3>
<p>Properties are then grouped into arbitrarily named sections that shall not be nested. The name of the section is on a line by itself and is surrounded by square brackets, i.e: </p>
<pre>[section_name]
property1_name = property1_value
property2_name = property2_value</pre>
<p>A section might or might not have properties. Sections that expect to have properties and which are found nonetheless empty are just ignored. Properties that are not recognized by the reader are ignored as well.</p>
<h3>Section names</h3>
<p>Each different section can be thought of as being a directive to suppress ABI change reports for a particular kind of ABI artifact.</p>
<h3><code>[suppress_file]</code></h3>
<p>This directive prevents a given tool from loading a file (binary or not) if its file name matches certain properties. Thus, if the tool is meant to compare the ABIs of two files, and if the directive prevents it from loading either one of the files, then no comparison is performed. </p>
<p> Note that for the <code>[suppress_file]</code> directive to work, at least one of the following properties must be provided: <code>file_name_regexp</code>, <code>file_name_not_regexp</code>. </p>
<p> The potential properties of this sections are listed below:</p>
<dl>
<dt>&bull;</p>
<dd><code>file_name_regexp</code> </p>
<p> Usage: <code>file_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Prevents the system from loading the file which name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>file_name_not_regexp</code> </p>
<p> Usage: <code>file_name_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Prevents the system from loading the file which name does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>label</code> Usage: <code>label</code> <code>=</code> &lt;some-value&gt; </p>
<p> Define a label for the section. A label is just an informative string that might be used by the tool to refer to a type suppression in error messages.</dl>
<h3><code>[suppress_type]</code></h3>
<p>This directive suppresses report messages about a type change. </p>
<p> Note that for the <code>[suppress_type]</code> directive to work, at least one of the following properties must be provided: <code>file_name_regexp</code>, <code>file_name_not_regexp</code>, <code>soname_regexp</code>, <code>soname_not_regexp</code>, <code>name</code>, <code>name_regexp</code>, <code>type_kind</code>, <code>source_location_not_in</code>, <code>source_location_not_regexp</code>. </p>
<p> If none of the following properties are provided, then the <code>[suppress_type]</code> directive is simply ignored. </p>
<p> The potential properties of this sections are listed below:</p>
<dl>
<dt>&bull;</p>
<dd><code>file_name_regexp</code> </p>
<p> Usage: <code>file_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a binary file which name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>file_name_not_regexp</code> </p>
<p> Usage: <code>file_name_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a binary file which name does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>soname_regexp</code> </p>
<p> Usage: <code>soname_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a shared library which SONAME property matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>soname_not_regexp</code> </p>
<p> Usage: <code>soname_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a shared library which SONAME property does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>name_regexp</code> Usage: <code>name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving types whose name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>name</code> Usage: <code>name</code> <code>=</code> &lt;a-value&gt; </p>
<p> Suppresses change reports involving types whose name equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>type_kind</code> Usage:</p>
<dt><code>type_kind</code> <code>=</code> <code>class</code> | <code>struct</code> | <code>union</code> | <code>enum</code> |</p>
<dd><code>array</code> | <code>typedef</code> | <code>builtin</code> </p>
<p> Suppresses change reports involving a certain kind of type. The kind of type to suppress change reports for is specified by the possible values listed above:</p>
<dt>&bull;</p>
<dd>
<dt><code>class</code>: suppress change reports for class types. Note that</p>
<dd>even if class types don&#8217;t exist for C, this value still triggers the suppression of change reports for struct types, in C. In C++ however, it should do what it suggests.</p>
<dt>&bull;</p>
<dd>
<dt><code>struct</code>: suppress change reports for struct types in C or C++.</p>
<dd>Note that the value <code>class</code> above is a super-set of this one.</p>
<dt>&bull;</p>
<dd><code>union</code>: suppress change reports for union types.</p>
<dt>&bull;</p>
<dd><code>enum</code>: suppress change reports for enum types.</p>
<dt>&bull;</p>
<dd><code>array</code>: suppress change reports for array types.</p>
<dt>&bull;</p>
<dd><code>typedef</code>: suppress change reports for typedef types.</p>
<dt>&bull;</p>
<dd><code>builtin</code>: suppress change reports for built-in (or native) types. Example of built-in types are char, int, unsigned int, etc.</p>
<dt>&bull;</p>
<dd><code>source_location_not_in</code> Usage: <code>source_location_not_in</code> <code>=</code> &lt;<code>list-of-file-paths</code>&gt; </p>
<p> Suppresses change reports involving a type which is defined in a file which path is <i>NOT</i> listed in the value <code>list-of-file-paths</code>. Note that the value is a comma-separated list of file paths e.g, this property </p>
<pre>source_location_not_in = libabigail/abg-ir.h, libabigail/abg-dwarf-reader.h</pre>
<p>suppresses change reports about all the types that are <i>NOT</i> defined in header files whose path end up with the strings libabigail/abg-ir.h or libabigail/abg-dwarf-reader.h.</p>
<dt>&bull;</p>
<dd><code>source_location_not_regexp</code> Usage: <code>source_location_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving a type which is defined in a file which path does <i>NOT</i> match the <i>regular expression</i> provided as value of the property. E.g, this property </p>
<pre>source_location_not_regexp = libabigail/abg-.*\.h</pre>
<p>suppresses change reports involving all the types that are <i>NOT</i> defined in header files whose path match the regular expression provided a value of the property.</p>
<dt>&bull;</p>
<dd><code>has_data_member_inserted_at</code> Usage: <code>has_data_member_inserted_at</code> <code>=</code> &lt;<code>offset-in-bit</code>&gt; </p>
<p> Suppresses change reports involving a type which has at least one data member inserted at an offset specified by the property value <code>offset-in-bit</code>. The value <code>offset-in-bit</code> is either:</p>
<dt>&bull;</p>
<dd>an integer value, expressed in bits, which denotes the offset of the insertion point of the data member, starting from the beginning of the relevant structure or class.</p>
<dt>&bull;</p>
<dd>the keyword <code>end</code> which is a named constant which value equals the offset of the end of the of the structure or class.</p>
<dt>&bull;</p>
<dd>the function call expression <code>offset_of(data-member-name)</code> where <i>data-member-name</i> is the name of a given data member of the relevant structure or class. The value of this function call expression is an integer that represents the offset of the data member denoted by <code>data-member-name</code>.</p>
<dt>&bull;</p>
<dd>the function call expression <code>offset_after(data-member-name)</code> where <i>data-member-name</i> is the name of a given data member of the relevant structure or class. The value of this function call expression is an integer that represents the offset of the point that comes right after the region occupied by the data member denoted by <code>data-member-name</code>.</p>
<dt>&bull;</p>
<dd><code>has_data_member_inserted_between</code> Usage: <code>has_data_member_inserted_between</code> <code>=</code> {&lt;<code>range-begin</code>&gt;, &lt;<code>range-end</code>&gt;} </p>
<p> Suppresses change reports involving a type which has at least one data mber inserted at an offset that is comprised in the range between range-begin&#8220; and <code>range-end</code>. Please note that each of the lues <code>range-begin</code> and <code>range-end</code> can be of the same form as the <i>has_data_member_inserted_at</i> property above. </p>
<p> Usage examples of this properties are: </p>
<pre>has_data_member_inserted_between = {8, 64}</pre>
<p>or: </p>
<pre>has_data_member_inserted_between = {16, end}</pre>
<p>or: </p>
<pre>has_data_member_inserted_between = {offset_after(member1), end}</pre>
<dt>&bull;</p>
<dd><code>has_data_members_inserted_between</code> Usage: <code>has_data_members_inserted_between</code> <code>=</code> {&lt;sequence-of-ranges&gt;} </p>
<p> Suppresses change reports involving a type which has multiple data member inserted in various offset ranges. A usage example of this property is, for instance: </p>
<pre>has_data_members_inserted_between = &#123;&#123;8, 31}, {72, 95}}</pre>
<p>This usage example suppresses change reports involving a type which has data members inserted in bit offset ranges [8 31] and [72 95]. The length of the sequence of ranges or this <code>has_data_members_inserted_between</code> is not bounded; it can be as long as the system can cope with. The values of the boundaries of the ranges are of the same kind as for the <i>has_data_member_inserted_at</i> property above. </p>
<p> Another usage example of this property is thus: </p>
<pre>has_data_members_inserted_between =
 {
 {offset_after(member0), offset_of(member1)},
 {72, end}
 }</pre>
<dt>&bull;</p>
<dd><code>accessed_through</code> Usage: <code>accessed_through</code> <code>=</code> &lt;some-predefined-values&gt; </p>
<p> Suppress change reports involving a type which is referred to either directly or through a pointer or a reference. The potential values of this property are the predefined keywords below:</p>
<dt>&bull;</p>
<dd><code>direct</code> </p>
<p> So if the <code>[suppress_type]</code> contains the property description: </p>
<pre>accessed_through = direct</pre>
<p>then changes about a type that is referred-to directly (i.e, not through a pointer or a reference) are going to be suppressed.</p>
<dt>&bull;</p>
<dd><code>pointer</code> </p>
<p> If the <code>accessed_through</code> property is set to the value <code>pointer</code> then changes about a type that is referred-to through a pointer are going to be suppressed.</p>
<dt>&bull;</p>
<dd><code>reference</code> </p>
<p> If the <code>accessed_through</code> property is set to the value <code>reference</code> then changes about a type that is referred-to through a reference are going to be suppressed.</p>
<dt>&bull;</p>
<dd><code>reference-or-pointer</code> </p>
<p> If the <code>accessed_through</code> property is set to the value <code>reference-or-pointer</code> then changes about a type that is referred-to through either a reference or a pointer are going to be suppressed. </p>
<p> For an extensive example of how to use this property, please check out the example below about <i>suppressing change reports about types accessed either directly or through pointers</i>.</p>
<dt>&bull;</p>
<dd><code>drop</code> Usage: <code>drop</code> <code>=</code> yes | no </p>
<p> If a type is matched by a suppression specification which contains the &quot;drop&quot; property set to &quot;yes&quot; (or to &quot;true&quot;) then the type is not even going to be represented in the internal representation of the ABI being analyzed. This property makes its enclosing suppression specification to be applied in the <i>early suppression specification mode</i>. The net effect is that it potentially reduces the memory used to represent the ABI being analyzed. </p>
<p> Please note that for this property to be effective, the enclosing suppression specification must have at least one of the following properties specified: <code>name_regexp</code>, <code>name</code>, <code>name_regexp</code>, <code>source_location_not_in</code> or <code>source_location_not_regexp</code>.</p>
<dt>&bull;</p>
<dd><code>label</code> Usage: <code>label</code> <code>=</code> &lt;some-value&gt; </p>
<p> Define a label for the section. A label is just an informative string that might be used by a tool to refer to a type suppression in error messages.</dl>
<h3><code>[suppress_function]</code></h3>
<p>This directive suppresses report messages about changes on a set of functions. </p>
<p> Note that for the <code>[suppress_function]</code> directive to work, at least one of the following properties must be provided: <code>label</code>, <code>file_name_regexp</code>, <code>file_name_not_regexp</code>, <code>soname_regexp</code>, <code>soname_not_regexp</code>, <code>name</code>, <code>name_regexp</code>, <code>name_not_regexp</code>, <code>parameter</code>, <code>return_type_name</code>, <code>symbol_name</code>, <code>symbol_name_regexp</code>, <code>symbol_version</code>, </p>
<p> <code>symbol_version_regexp</code>. </p>
<p> If none of the following properties are provided, then the <code>[suppress_function]</code> directive is simply ignored. </p>
<p> The potential properties of this sections are:</p>
<dl>
<dt>&bull;</p>
<dd><code>label</code> Usage: <code>label</code> <code>=</code> &lt;some-value&gt; </p>
<p> This property is the same as the <i>label property</i> defined above.</p>
<dt>&bull;</p>
<dd><code>file_name_regexp</code> </p>
<p> Usage: </p>
<p> <code>file_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a binary file which name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>file_name_not_regexp</code> </p>
<p> Usage: <code>file_name_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a binary file which name does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>soname_regexp</code> </p>
<p> Usage: <code>soname_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a shared library which SONAME property matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>soname_not_regexp</code> </p>
<p> Usage: <code>soname_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a shared library which SONAME property does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>name</code> Usage: <code>name</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving functions whose name equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>name_regexp</code> Usage: <code>name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving functions whose name matches the regular expression specified as value of this property. </p>
<p> Let&#8217;s consider the case of functions that have several symbol names. This happens when the underlying symbol for the function has aliases. Each symbol name is actually one alias name. </p>
<p> In this case, if the regular expression matches the name of at least one of the aliases names, then it must match the names of all of the aliases of the function for the directive to actually suppress the diff reports for said function.</p>
<dt>&bull;</p>
<dd><code>name_not_regexp</code> Usage: <code>name_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving functions whose names don&#8217;t match the regular expression specified as value of this property. </p>
<p> The rules for functions that have several symbol names are the same rules as for the <code>name_regexp</code> property above.</p>
<dt>&bull;</p>
<dd><code>change_kind</code> Usage: <code>change_kind</code> <code>=</code> &lt;predefined-possible-values&gt; </p>
<p> Specifies the kind of changes this suppression specification should apply to. The possible values of this property as well as their meaning are listed below:</p>
<dt>&bull;</p>
<dd><code>function-subtype-change</code> </p>
<p> This suppression specification applies to functions that which have at least one sub-type that has changed.</p>
<dt>&bull;</p>
<dd><code>added-function</code> </p>
<p> This suppression specification applies to functions that have been added to the binary.</p>
<dt>&bull;</p>
<dd><code>deleted-function</code> </p>
<p> This suppression specification applies to functions that have been removed from the binary.</p>
<dt>&bull;</p>
<dd><code>all</code> </p>
<p> This suppression specification applies to functions that have all of the changes above. Note that not providing the <code>change_kind</code> property at all is equivalent to setting it to the value <code>all</code>.</p>
<dt>&bull;</p>
<dd><code>parameter</code> Usage: <code>parameter</code> <code>=</code> &lt;function-parameter-specification&gt; </p>
<p> Suppresses change reports involving functions whose parameters match the parameter specification indicated as value of this property. </p>
<p> The format of the function parameter specification is: </p>
<p> <code>&#8216;</code> <code>&lt;parameter-index&gt;</code> <code>&lt;space&gt;</code> <code>&lt;type-name-or-regular-expression&gt;</code> </p>
<p> That is, an apostrophe followed by a number that is the index of the parameter, followed by one of several spaces, followed by either the name of the type of the parameter, or a regular expression describing a family of parameter type names. </p>
<p> If the parameter type name is designated by a regular expression, then said regular expression must be enclosed between two slashes; like <code>/some-regular-expression/</code>. </p>
<p> The index of the first parameter of the function is zero. Note that for member functions (methods of classes), the this is the first parameter that comes after the implicit &quot;this&quot; pointer parameter. </p>
<p> Examples of function parameter specifications are: </p>
<pre>'0 int</pre>
<p>Which means, the parameter at index 0, whose type name is <code>int</code>. </p>
<pre>'4 unsigned char*</pre>
<p>Which means, the parameter at index 4, whose type name is <code>unsigned char*</code>. </p>
<pre>'2 /^foo.*&amp;/</pre>
<p>Which means, the parameter at index 2, whose type name starts with the string &quot;foo&quot; and ends with an &#8216;&amp;&#8217;. In other words, this is the third parameter and it&#8217;s a reference on a type that starts with the string &quot;foo&quot;.</p>
<dt>&bull;</p>
<dd><code>return_type_name</code> Usage: <code>return_type_name</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving functions whose return type name equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>return_type_regexp</code> Usage: <code>return_type_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving functions whose return type name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>symbol_name</code> Usage: <code>symbol_name</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving functions whose symbol name equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>symbol_name_regexp</code> Usage: <code>symbol_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving functions whose symbol name matches the regular expression specified as value of this property. </p>
<p> Let&#8217;s consider the case of functions that have several symbol names. This happens when the underlying symbol for the function has aliases. Each symbol name is actually one alias name. </p>
<p> In this case, the regular expression must match the names of all of the aliases of the function for the directive to actually suppress the diff reports for said function.</p>
<dt>&bull;</p>
<dd><code>symbol_version</code> Usage: <code>symbol_version</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving functions whose symbol version equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>symbol_version_regexp</code> Usage: <code>symbol_version_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving functions whose symbol version matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>drop</code> Usage: <code>drop</code> <code>=</code> yes | no </p>
<p> If a function is matched by a suppression specification which contains the &quot;drop&quot; property set to &quot;yes&quot; (or to &quot;true&quot;) then the function is not even going to be represented in the internal representation of the ABI being analyzed. This property makes its enclosing suppression specification to be applied in the <i>early suppression specification mode</i>. The net effect is that it potentially reduces the memory used to represent the ABI being analyzed. </p>
<p> Please note that for this property to be effective, the enclosing suppression specification must have at least one of the following properties specified: <code>name_regexp</code>, <code>name</code>, <code>name_regexp</code>, <code>source_location_not_in</code> or <code>source_location_not_regexp</code>.</dl>
<h3><code>[suppress_variable]</code></h3>
<p>This directive suppresses report messages about changes on a set of variables. </p>
<p> Note that for the <code>[suppress_variable]</code> directive to work, at least one of the following properties must be provided: <code>label</code>, <code>file_name_regexp</code>, <code>file_name_not_regexp</code>, <code>soname_regexp</code>, <code>soname_not_regexp</code>, <code>name</code>, <code>name_regexp</code>, <code>symbol_name</code>, <code>symbol_name_regexp</code>, <code>symbol_version</code>, <code>symbol_version_regexp</code>. </p>
<p> If none of the following properties are provided, then the <code>[suppres_variable]</code> directive is simply ignored. </p>
<p> The potential properties of this sections are:</p>
<dl>
<dt>&bull;</p>
<dd><code>label</code> Usage: <code>label</code> <code>=</code> &lt;some-value&gt; </p>
<p> This property is the same as the <i>label property</i> defined above.</p>
<dt>&bull;</p>
<dd><code>file_name_regexp</code> </p>
<p> Usage: </p>
<p> <code>file_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a binary file which name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>file_name_not_regexp</code> </p>
<p> Usage: <code>file_name_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a binary file which name does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>soname_regexp</code> </p>
<p> Usage: <code>soname_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a shared library which SONAME property matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>soname_not_regexp</code> </p>
<p> Usage: <code>soname_not_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports about ABI artifacts that are defined in a shared library which SONAME property does not match the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>name</code> Usage: <code>name</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving variables whose name equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>name_regexp</code> Usage: <code>name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving variables whose name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>change_kind</code> Usage: <code>change_kind</code> <code>=</code> &lt;predefined-possible-values&gt; </p>
<p> Specifies the kind of changes this suppression specification should apply to. The possible values of this property as well as their meaning are the same as when it&#8217;s <i>used in the [suppress_function] section</i>.</p>
<dt>&bull;</p>
<dd><code>symbol_name</code> Usage: <code>symbol_name</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving variables whose symbol name equals the value of this property.</p>
<dt>&bull;</p>
<dd>symbol_name_regexp Usage: <code>symbol_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving variables whose symbol name matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>symbol_version</code> Usage: <code>symbol_version</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving variables whose symbol version equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>symbol_version_regexp</code> Usage: <code>symbol_version_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving variables whose symbol version matches the regular expression specified as value of this property.</p>
<dt>&bull;</p>
<dd><code>type_name</code> Usage: <code>type_name</code> <code>=</code> &lt;some-value&gt; </p>
<p> Suppresses change reports involving variables whose type name equals the value of this property.</p>
<dt>&bull;</p>
<dd><code>type_name_regexp</code> Usage: <code>type_name_regexp</code> <code>=</code> &lt;<i>regular-expression</i>&gt; </p>
<p> Suppresses change reports involving variables whose type name matches the regular expression specified as value of this property.</dl>
<h3>Comments</h3>
<p><code>;</code> or <code>#</code> ASCII character at the beginning of a line indicates a comment. Comment lines are ignored.</p>
<h3>Code examples</h3>
<dl>
<dt>1.</p>
<dd>Suppressing change reports about types. </p>
<p> Suppose we have a library named <code>libtest1-v0.so</code> which contains this very useful code: </p>
<pre>$ cat -n test1-v0.cc
 1 // A forward declaration for a type considered to be opaque to
 2 // function foo() below.
 3 struct opaque_type;
 4
 5 // This function cannot touch any member of opaque_type. Hence,
 6 // changes to members of opaque_type should not impact foo, as far as
 7 // ABI is concerned.
 8 void
 9 foo(opaque_type*)
 10 {
 11 }
 12
 13 struct opaque_type
 14 {
 15 int member0;
 16 char member1;
 17 };
$</pre>
<p>Let&#8217;s change the layout of struct opaque_type by inserting a data member around line 15, leading to a new version of the library, that we shall name <code>libtest1-v1.so</code>: </p>
<pre>$ cat -n test1-v1.cc
 1 // A forward declaration for a type considered to be opaque to
 2 // function foo() below.
 3 struct opaque_type;
 4
 5 // This function cannot touch any member of opaque_type; Hence,
 6 // changes to members of opaque_type should not impact foo, as far as
 7 // ABI is concerned.
 8 void
 9 foo(opaque_type*)
 10 {
 11 }
 12
 13 struct opaque_type
 14 {
 15 char added_member; // &lt;-- a new member got added here now.
 16 int member0;
 17 char member1;
 18 };
$</pre>
<p>Let&#8217;s compile both examples. We shall not forget to compile them with debug information generation turned on: </p>
<pre>$ g++ -shared -g -Wall -o libtest1-v0.so test1-v0.cc
$ g++ -shared -g -Wall -o libtest1-v1.so test1-v1.cc</pre>
<p>Let&#8217;s ask <i>abidiff</i> which ABI differences it sees between <code>libtest1-v0.so</code> and <code>libtest1-v1.so</code>: </p>
<pre>$ abidiff libtest1-v0.so libtest1-v1.so
Functions changes summary: 0 Removed, 1 Changed, 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function void foo(opaque_type*)' has some indirect sub-type changes:
 parameter 0 of type 'opaque_type*' has sub-type changes:
 in pointed to type 'struct opaque_type':
 size changed from 64 to 96 bits
 1 data member insertion:
 'char opaque_type::added_member', at offset 0 (in bits)
 2 data member changes:
 'int opaque_type::member0' offset changed from 0 to 32
 'char opaque_type::member1' offset changed from 32 to 64</pre>
<p>So <code>abidiff</code> reports that the opaque_type&#8217;s layout has changed in a significant way, as far as ABI implications are concerned, in theory. After all, a sub-type (<code>struct opaque_type</code>) of an exported function (<code>foo()</code>) has seen its layout change. This might have non negligible ABI implications. But in practice here, the programmer of the litest1-v1.so library knows that the &quot;soft&quot; contract between the function <code>foo()</code> and the type <code>struct opaque_type</code> is to stay away from the data members of the type. So layout changes of <code>struct opaque_type</code> should not impact <code>foo()</code>. </p>
<p> Now to teach <code>abidiff</code> about this soft contract and have it avoid emitting what amounts to false positives in this case, we write the suppression specification file below: </p>
<pre>$ cat test1.suppr
[suppress_type]
 type_kind = struct
 name = opaque_type</pre>
<p>Translated in plain English, this suppression specification would read: &quot;Do not emit change reports about a struct which name is opaque_type&quot;. </p>
<p> Let&#8217;s now invoke <code>abidiff</code> on the two versions of the library again, but this time with the suppression specification: </p>
<pre>$ abidiff --suppressions test1.suppr libtest1-v0.so libtest1-v1.so
Functions changes summary: 0 Removed, 0 Changed (1 filtered out), 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable</pre>
<p>As you can see, <code>abidiff</code> does not report the change anymore; it tells us that it was filtered out instead. </p>
<p> Suppressing change reports about types with data member insertions </p>
<p> Suppose the first version of a library named <code>libtest3-v0.so</code> has this source code: </p>
<pre>/* Compile this with:
 gcc -g -Wall -shared -o libtest3-v0.so test3-v0.c
 */
struct S
{
 char member0;
 int member1; /*
 between member1 and member2, there is some padding,
 at least on some popular platforms. On
 these platforms, adding a small enough data
 member into that padding shouldn't change
 the offset of member1. Right?
 */
};
int
foo(struct S* s)
{
 return s-&gt;member0 + s-&gt;member1;
}</pre>
<p>Now, suppose the second version of the library named <code>libtest3-v1.so</code> has this source code in which a data member has been added in the padding space of struct S and another data member has been added at its end: </p>
<pre>/* Compile this with:
 gcc -g -Wall -shared -o libtest3-v1.so test3-v1.c
 */
struct S
{
 char member0;
 char inserted1; /* &lt;---- A data member has been added here... */
 int member1;
 char inserted2; /* &lt;---- ... and another one has been added here. */
};
int
foo(struct S* s)
{
 return s-&gt;member0 + s-&gt;member1;
}</pre>
<p>In libtest3-v1.so, adding char data members <code>S::inserted1</code> and <code>S::inserted2</code> can be considered harmless (from an ABI compatibility perspective), at least on the x86 platform, because that doesn&#8217;t change the offsets of the data members S::member0 and S::member1. But then running <code>abidiff</code> on these two versions of library yields: </p>
<pre>$ abidiff libtest3-v0.so libtest3-v1.so
Functions changes summary: 0 Removed, 1 Changed, 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function int foo(S*)' has some indirect sub-type changes:
 parameter 0 of type 'S*' has sub-type changes:
 in pointed to type 'struct S':
 type size changed from 64 to 96 bits
 2 data member insertions:
 'char S::inserted1', at offset 8 (in bits)
 'char S::inserted2', at offset 64 (in bits)
$</pre>
<p>That is, <code>abidiff</code> shows us the two changes, even though we (the developers of that very involved library) know that these changes are harmless in this particular context. </p>
<p> Luckily, we can devise a suppression specification that essentially tells abidiff to filter out change reports about adding a data member between <code>S::member0</code> and <code>S::member1</code>, and adding a data member at the end of struct S. We have written such a suppression specification in a file called test3-1.suppr and it unsurprisingly looks like: </p>
<pre>[suppress_type]
 name = S
 has_data_member_inserted_between = {offset_after(member0), offset_of(member1)}
 has_data_member_inserted_at = end</pre>
<p>Now running <code>abidiff</code> with this suppression specification yields: </p>
<pre>$ ../build/tools/abidiff --suppressions test3-1.suppr libtest3-v0.so libtest3-v1.so
Functions changes summary: 0 Removed, 0 Changed (1 filtered out), 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
$</pre>
<p>Hooora! \o/ (I guess) </p>
<p> Suppressing change reports about types accessed either directly or through pointers </p>
<p> Suppose we have a first version of an object file which source code is the file widget-v0.cc below: </p>
<pre>// Compile with: g++ -g -c widget-v0.cc
struct widget
{
 int x;
 int y;
 widget()
 :x(), y()
 {}
};
void
fun0(widget*)
{
 // .. do stuff here.
}
void
fun1(widget&amp;)
{
 // .. do stuff here ..
}
void
fun2(widget w)
{
 // ... do other stuff here ...
}</pre>
<p>Now suppose in the second version of that file, named widget-v1.cc, we have added some data members at the end of the type <code>struct widget</code>; here is what the content of that file would look like: </p>
<pre>// Compile with: g++ -g -c widget-v1.cc
struct widget
{
 int x;
 int y;
 int w; // We have added these two new data members here ..
 int h; // ... and here.
 widget()
 : x(), y(), w(), h()
 {}
};
void
fun0(widget*)
{
 // .. do stuff here.
}
void
fun1(widget&amp;)
{
 // .. do stuff here ..
}
void
fun2(widget w)
{
 // ... do other stuff here ...
}</pre>
<p>When we invoke <code>abidiff</code> on the object files resulting from the compilation of the two file above, here is what we get: </p>
<pre> $ abidiff widget-v0.o widget-v1.o
 Functions changes summary: 0 Removed, 2 Changed (1 filtered out), 0 Added functions
 Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
 2 functions with some indirect sub-type change:
 [C]'function void fun0(widget*)' has some indirect sub-type changes:
 parameter 1 of type 'widget*' has sub-type changes:
 in pointed to type 'struct widget':
 type size changed from 64 to 128 bits
 2 data member insertions:
 'int widget::w', at offset 64 (in bits)
 'int widget::h', at offset 96 (in bits)
 [C]'function void fun2(widget)' has some indirect sub-type changes:
 parameter 1 of type 'struct widget' has sub-type changes:
 details were reported earlier
$</pre>
<p>I guess a little bit of explaining is due here. <code>abidiff</code> detects that two data member got added at the end of <code>struct widget</code>. it also tells us that the type change impacts the exported function <code>fun0()</code> which uses the type <code>struct widget</code> through a pointer, in its signature. </p>
<p> Careful readers will notice that the change to <code>struct widget</code> also impacts the exported function <code>fun1()</code>, that uses type <code>struct widget</code> through a reference. But then <code>abidiff</code> doesn&#8217;t tell us about the impact on that function <code>fun1()</code> because it has evaluated that change as being <code>redundant</code> with the change it reported on <code>fun0()</code>. It has thus filtered it out, to avoid cluttering the output with noise. </p>
<p> Redundancy detection and filtering is fine and helpful to avoid burying the important information in a sea of noise. However, it must be treated with care, by fear of mistakenly filtering out relevant and important information. </p>
<p> That is why <code>abidiff</code> tells us about the impact that the change to <code>struct widget</code> has on function <code>fun2()</code>. In this case, that function uses the type <code>struct widget</code> <code>directly</code> (in its signature). It does not use it via a pointer or a reference. In this case, the direct use of this type causes <code>fun2()</code> to be exposed to a potentially harmful ABI change. Hence, the report about <code>fun2()</code> is not filtered out, even though it&#8217;s about that same change on <code>struct widget</code>. </p>
<p> To go further in suppressing reports about changes that are harmless and keeping only those that we know are harmful, we would like to go tell abidiff to suppress reports about this particular <code>struct widget</code> change when it impacts uses of <code>struct widget</code> through a pointer or reference. In other words, suppress the change reports about <code>fun0()</code> <code>and</code> <code>fun1()</code>. We would then write this suppression specification, in file <code>widget.suppr</code>: </p>
<pre>[suppress_type]
 name = widget
 type_kind = struct
 has_data_member_inserted_at = end
 accessed_through = reference-or-pointer
 # So this suppression specification says to suppress reports about
 # the type 'struct widget', if this type was added some data member
 # at its end, and if the change impacts uses of the type through a
 # reference or a pointer.</pre>
<p>Invoking <code>abidiff</code> on <code>widget-v0.o</code> and <code>widget-v1.o</code> with this suppression specification yields: </p>
<pre>$ abidiff --suppressions widget.suppr widget-v0.o widget-v1.o
Functions changes summary: 0 Removed, 1 Changed (2 filtered out), 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function void fun2(widget)' has some indirect sub-type changes:
 parameter 1 of type 'struct widget' has sub-type changes:
 type size changed from 64 to 128 bits
 2 data member insertions:
 'int widget::w', at offset 64 (in bits)
 'int widget::h', at offset 96 (in bits)
$</pre>
<p>As expected, I guess. </p>
<p> Suppressing change reports about functions. </p>
<p> Suppose we have a first version a library named <code>libtest2-v0.so</code> whose source code is: </p>
<pre> $ cat -n test2-v0.cc
 1 struct S1
 2 {
 3 int m0;
 4
 5 S1()
 6 : m0()
 7 {}
 8 };
 9
 10 struct S2
 11 {
 12 int m0;
 13
 14 S2()
 15 : m0()
 16 {}
 17 };
 18
 19 struct S3
 20 {
 21 int m0;
 22
 23 S3()
 24 : m0()
 25 {}
 26 };
 27
 28 int
 29 func(S1&amp;)
 30 {
 31 // suppose the code does something with the argument.
 32 return 0;
 33
 34 }
 35
 36 char
 37 func(S2*)
 38 {
 39 // suppose the code does something with the argument.
 40 return 0;
 41 }
 42
 43 unsigned
 44 func(S3)
 45 {
 46 // suppose the code does something with the argument.
 47 return 0;
 48 }
$</pre>
<p>And then we come up with a second version <code>libtest2-v1.so</code> of that library; the source code is modified by making the structures <code>S1</code>, <code>S2</code>, <code>S3</code> inherit another struct: </p>
<pre>$ cat -n test2-v1.cc
 1 struct base_type
 2 {
 3 int m_inserted;
 4 };
 5
 6 struct S1 : public base_type // &lt;--- S1 now has base_type as its base
 7 // type.
 8 {
 9 int m0;
 10
 11 S1()
 12 : m0()
 13 {}
 14 };
 15
 16 struct S2 : public base_type // &lt;--- S2 now has base_type as its base
 17 // type.
 18 {
 19 int m0;
 20
 21 S2()
 22 : m0()
 23 {}
 24 };
 25
 26 struct S3 : public base_type // &lt;--- S3 now has base_type as its base
 27 // type.
 28 {
 29 int m0;
 30
 31 S3()
 32 : m0()
 33 {}
 34 };
 35
 36 int
 37 func(S1&amp;)
 38 {
 39 // suppose the code does something with the argument.
 40 return 0;
 41
 42 }
 43
 44 char
 45 func(S2*)
 46 {
 47 // suppose the code does something with the argument.
 48 return 0;
 49 }
 50
 51 unsigned
 52 func(S3)
 53 {
 54 // suppose the code does something with the argument.
 55 return 0;
 56 }
 $</pre>
<p>Now let&#8217;s build the two libraries: </p>
<pre>g++ -Wall -g -shared -o libtest2-v0.so test2-v0.cc
g++ -Wall -g -shared -o libtest2-v0.so test2-v0.cc</pre>
<p>Let&#8217;s look at the output of <code>abidiff</code>: </p>
<pre>$ abidiff libtest2-v0.so libtest2-v1.so
Functions changes summary: 0 Removed, 3 Changed, 0 Added functions
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
3 functions with some indirect sub-type change:
 [C]'function unsigned int func(S3)' has some indirect sub-type changes:
 parameter 0 of type 'struct S3' has sub-type changes:
 size changed from 32 to 64 bits
 1 base class insertion:
 struct base_type
 1 data member change:
 'int S3::m0' offset changed from 0 to 32
 [C]'function char func(S2*)' has some indirect sub-type changes:
 parameter 0 of type 'S2*' has sub-type changes:
 in pointed to type 'struct S2':
 size changed from 32 to 64 bits
 1 base class insertion:
 struct base_type
 1 data member change:
 'int S2::m0' offset changed from 0 to 32
 [C]'function int func(S1&amp;)' has some indirect sub-type changes:
 parameter 0 of type 'S1&amp;' has sub-type changes:
 in referenced type 'struct S1':
 size changed from 32 to 64 bits
 1 base class insertion:
 struct base_type
 1 data member change:
 'int S1::m0' offset changed from 0 to 32
$</pre>
<p>Let&#8217;s tell <code>abidiff</code> to avoid showing us the differences on the overloads of <code>func</code> that takes either a pointer or a reference. For that, we author this simple suppression specification: </p>
<pre>$ cat -n libtest2.suppr
 1 [suppress_function]
 2 name = func
 3 parameter = '0 S1&amp;
 4
 5 [suppress_function]
 6 name = func
 7 parameter = '0 S2*
$</pre>
<p>And then let&#8217;s invoke <code>abidiff</code> with the suppression specification: </p>
<pre>$ ../build/tools/abidiff --suppressions libtest2.suppr libtest2-v0.so libtest2-v1.so
Functions changes summary: 0 Removed, 1 Changed (2 filtered out), 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function unsigned int func(S3)' has some indirect sub-type changes:
 parameter 0 of type 'struct S3' has sub-type changes:
 size changed from 32 to 64 bits
 1 base class insertion:
 struct base_type
 1 data member change:
 'int S3::m0' offset changed from 0 to 32</pre>
<p>The suppression specification could be reduced using <i>regular expressions</i>: </p>
<pre>$ cat -n libtest2-1.suppr
 1 [suppress_function]
 2 name = func
 3 parameter = '0 /^S.(&amp;|\*)/
$
$ ../build/tools/abidiff --suppressions libtest2-1.suppr libtest2-v0.so libtest2-v1.so
Functions changes summary: 0 Removed, 1 Changed (2 filtered out), 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
1 function with some indirect sub-type change:
 [C]'function unsigned int func(S3)' has some indirect sub-type changes:
 parameter 0 of type 'struct S3' has sub-type changes:
 size changed from 32 to 64 bits
 1 base class insertion:
 struct base_type
 1 data member change:
 'int S3::m0' offset changed from 0 to 32
$</pre>
</dl>
<h2>Author</h2>
<p>Dodji Seketeli</p>
<h2>Copyright</h2>
<p>2014-2016, Red Hat, Inc.</p>
