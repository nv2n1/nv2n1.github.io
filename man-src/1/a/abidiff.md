---
title: "abidiff(1)"
name: "abidiff"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abidiff/"
description: "abidiff – compare ABIs of ELF files"
---

<h2>NAME</h2>
<p> abidiff &#8211; compare ABIs of ELF files </p>
<p> abidiff compares the Application Binary Interfaces (ABI) of two shared libraries in <i>ELF</i> format. It emits a meaningful report describing the differences between the two ABIs. </p>
<p> For a comprehensive ABI change report that includes changes about function and variable sub-types, the two input shared libraries must be accompanied with their debug information in <i>DWARF</i> format. Otherwise, only <i>ELF</i> symbols that were added or removed are reported.</p>
<h2>INVOCATION</h2>
<pre>
abidiff [options] &lt;first-shared-library&gt; &lt;second-shared-library&gt;
</pre>
<h2>ENVIRONMENT</h2>
<p> abidiff loads two default <i>suppression specifications files</i>, merges their content and use it to filter out ABI change reports that might be considered as false positives to users.</p>
<dl>
<dt>&bull;</p>
<dd> Default system-wide suppression specification file </p>
<p> It&#8217;s located by the optional environment variable LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE. If that environment variable is not set, then abidiff tries to load the suppression file $libdir/libabigail/libabigail-default.abignore. If that file is not present, then no default system-wide suppression specification file is loaded.</p>
<dt>&bull;</p>
<dd> Default user suppression specification file. </p>
<p> It&#8217;s located by the optional environment LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE. If that environment variable is not set, then abidiff tries to load the suppression file $HOME/.abignore. If that file is not present, then no default user suppression specification is loaded.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd> <i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd> <code>&#8211;debug-info-dir1 | &#8211;d1</code> &lt;<i>di-path1</i>&gt; </p>
<p> For cases where the debug information for <i>first-shared-library</i> is split out into a separate file, tells <code>abidiff</code> where to find that separate debug information file. </p>
<p> Note that <i>di-path</i> must point to the root directory under which the debug information is arranged in a tree-like manner. Under Red Hat based systems, that directory is usually <code>&lt;root&gt;/usr/lib/debug</code>. </p>
<p> Note also that this option is not mandatory for split debug information installed by your system&#8217;s package manager because then <code>abidiff</code> knows where to find it.</p>
<dt>&bull;</p>
<dd> <code>&#8211;debug-info-dir2 | &#8211;d2</code> &lt;<i>di-path2</i>&gt; </p>
<p> Like <code>&#8211;debug-info-dir1</code>, this options tells <code>abidiff</code> where to find the split debug information for the <i>second-shared-library</i> file.</p>
<dt>&bull;</p>
<dd> <code>&#8211;headers-dir1 | &#8211;hd1</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the first shared library that the tool has to consider. The tool will thus filter out ABI changes on types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd> <code>&#8211;headers-dir2 | &#8211;hd2</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the second shared library that the tool has to consider. The tool will thus filter out ABI changes on types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd> <code>&#8211;dont-drop-private-types</code> </p>
<p> This option is to be used with the <code>&#8211;headers-dir1</code> and <code>&#8211;headers-dir2</code> options. Without this option, types that are <i>NOT</i> defined in the headers are entirely dropped from the internal representation build by Libabigail to represent the ABI. They thus don&#8217;t have to be filtered out from the final ABI change report because they are not even present in Libabigail&#8217;s representation. </p>
<p> With this option however, those private types are kept in the internal representation and later filtered out from the report. </p>
<p> This options thus potentially makes Libabigail to potentially consume more memory. It&#8217;s meant to be mainly used for debugging purposes.</p>
<dt>&bull;</p>
<dd> <code>&#8211;stat</code> </p>
<p> Rather than displaying the detailed ABI differences between <i>first-shared-library</i> and <i>second-shared-library</i>, just display some summary statistics about these differences.</p>
<dt>&bull;</p>
<dd> <code>&#8211;symtabs</code> </p>
<p> Only display the symbol tables of the <i>first-shared-library</i> and <i>second-shared-library</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;deleted-fns</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the globally defined functions that got deleted from <i>first-shared-library</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;changed-fns</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the changes in sub-types of the global functions defined in <i>first-shared-library</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;added-fns</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the globally defined functions that were added to <i>second-shared-library</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;deleted-vars</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the globally defined variables that were deleted from <i>first-shared-library</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;changed-vars</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the changes in the sub-types of the global variables defined in <i>first-shared-library</i></p>
<dt>&bull;</p>
<dd> <code>&#8211;added-vars</code> </p>
<p> In the resulting report about the differences between <i>first-shared-library</i> and <i>second-shared-library</i>, only display the global variables that were added (defined) to <i>second-shared-library</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-linkage-name</code> </p>
<p> In the resulting report, do not display the linkage names of the added, removed, or changed functions or variables.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-unreferenced-symbols</code> </p>
<p> In the resulting report, do not display change information about function and variable symbols that are not referenced by any debug information. Note that for these symbols not referenced by any debug information, the change information displayed is either added or removed symbols.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-default-suppression</code> </p>
<p> Do not load the <i>default suppression specification files</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;suppressions | &#8211;suppr</code> &lt;<i>path-to-suppressions</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppressions</i>. Note that this option can appear multiple times on the command line. In that case, all of the provided suppression specification files are taken into account. </p>
<p> Please note that, by default, if this option is not provided, then the <i>default suppression specification files</i> are loaded .</p>
<dt>&bull;</p>
<dd> <code>&#8211;drop</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, drop the globally defined functions and variables which name match the regular expression <i>regex</i>. As a result, no change involving these functions or variables will be emitted in the diff report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;drop-fn</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, drop the globally defined functions which name match the regular expression <i>regex</i>. As a result, no change involving these functions will be emitted in the diff report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;drop-var</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, drop the globally defined variables matching a the regular expression <i>regex</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;keep</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, keep the globally defined functions and variables which names match the regular expression <i>regex</i>. All other functions and variables are dropped on the floor and will thus not appear in the resulting diff report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;keep-fn</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, keep the globally defined functions which name match the regular expression <i>regex</i>. All other functions are dropped on the floor and will thus not appear in the resulting diff report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;keep-var</code> &lt;<i>regex</i>&gt; </p>
<p> When reading the <i>first-shared-library</i> and <i>second-shared-library</i> ELF input files, keep the globally defined which names match the regular expression <i>regex</i>. All other variables are dropped on the floor and will thus not appear in the resulting diff report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;harmless</code> </p>
<p> In the diff report, display only the <i>harmless</i> changes. By default, the harmless changes are filtered out of the diff report keep the clutter to a minimum and have a greater change to spot real ABI issues.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-harmful</code> </p>
<p> In the diff report, do not display the <i>harmful</i> changes. By default, only the harmful changes are displayed in diff report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;redundant</code> </p>
<p> In the diff report, do display redundant changes. A redundant change is a change that has been displayed elsewhere in the report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-redundant</code> </p>
<p> In the diff report, do <i>NOT</i> display redundant changes. A redundant change is a change that has been displayed elsewhere in the report. This option is switched on by default.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-architecture</code> </p>
<p> Do not take architecture in account when comparing ABIs.</p>
<dt>&bull;</p>
<dd> <code>&#8211;dump-diff-tree</code> After the diff report, emit a textual representation of the diff nodes tree used by the comparison engine to represent the changed functions and variables. That representation is emitted to the error output for debugging purposes. Note that this diff tree is relevant only to functions and variables that have some sub-type changes. Added or removed functions and variables do not have any diff nodes tree associated to them.</p>
<dt>&bull;</p>
<dd> <code>&#8211;stats</code> </p>
<p> Emit statistics about various internal things.</p>
<dt>&bull;</p>
<dd> <code>&#8211;verbose</code> </p>
<p> Emit verbose logs about the progress of miscellaneous internal things.</dl>
<h2>RETURN VALUES</h2>
<p> The exit code of the <code>abidiff</code> command is either 0 if the ABI of the binaries being compared are equal, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the exit code is a 8-bits-wide bit field in which each bit has a specific meaning. </p>
<p> The first bit, of value 1, named <code>ABIDIFF_ERROR</code> means there was an error. </p>
<p> The second bit, of value 2, named <code>ABIDIFF_USAGE_ERROR</code> means there was an error in the way the user invoked the tool. It might be set, for instance, if the user invoked the tool with an unknown command line switch, with a wrong number or argument, etc. If this bit is set, then the <code>ABIDIFF_ERROR</code> bit must be set as well. </p>
<p> The third bit, of value 4, named <code>ABIDIFF_ABI_CHANGE</code> means the ABI of the binaries being compared are different. </p>
<p> The fourth bit, of value 8, named <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code> means the ABI of the binaries compared are different in an incompatible way. If this bit is set, then the <code>ABIDIFF_ABI_CHANGE</code> bit must be set as well. If the <code>ABIDIFF_ABI_CHANGE</code> is set and the <code>ABIDIFF_INCOMPATIBLE_CHANGE</code> is <i>NOT</i> set, then it means that the ABIs being compared might or might not be compatible. In that case, a human being needs to review the ABI changes to decide if they are compatible or not. </p>
<p> Note that, at the moment, there are only a few kinds of ABI changes that would result in setting the flag <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code>. Those ABI changes are either:</p>
<dl>
<dt>&bull;</p>
<dd> the removal of the symbol of a function or variable that has been defined and exported.</p>
<dt>&bull;</p>
<dd> the modification of the index of a member of a virtual function table (for C++ programs and libraries). </p>
<p> With time, when more ABI change patterns are found to <i>always</i> constitute incompatible ABI changes, we will adapt the code to recognize those cases and set the <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code> accordingly. So, if you find such patterns, please let us know. </p>
<p> The remaining bits are not used for the moment.</dl>
<h2>USAGE EXAMPLES</h2>
<dl>
<dt>1.</p>
<dd> Detecting a change in a sub-type of a function: </p>
<pre><code>
$ cat - n test - v0.cc 1 // Compile this with:
                 2       //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                 3 4 struct S0 5
{
    6 int m0;
    7
};
8 9 void 10 foo(S0 * /*parameter_name*/) 11 {
    12 // do something with parameter_name.
    13} $
    $ cat
    - n test - v1.cc 1 // Compile this with:
               2       //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
               3 4 struct type_base 5
{
    6 int inserted;
    7
};
8 9 struct S0 : public type_base 10 {
    11 int m0;
    12
};
13 14 void 15 foo(S0 * /*parameter_name*/) 16 {
    17 // do something with parameter_name.
    18} $
    $ g++ -
    g - Wall - shared - o libtest - v0.so test - v0.cc $ g++ - g - Wall - shared - o libtest - v1.so test - v1.cc $ $../ build / tools / abidiff libtest - v0.so libtest - v1.so Functions changes summary : 0 Removed,
    1 Changed, 0 Added function Variables changes summary : 0 Removed, 0 Changed, 0 Added variable 1 function with some indirect sub - type change : [C] 'function void foo(S0*)' has some indirect sub - type changes : parameter 0 of type 'S0*' has sub - type changes : in pointed to type 'struct S0' : size changed from 32 to 64 bits 1 base class insertion : struct type_base 1 data member change : 'int S0::m0' offset changed from 0 to 32 $
</code></pre>
<dt>2.</p>
<dd> Detecting another change in a sub-type of a function: </p>
<p>$ cat &#8211; n test &#8211; v0.cc 1 // Compile this with:<br />
                 2       //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc<br />
                 3 4 struct S0 5<br />
{<br />
    6 int m0;<br />
    7<br />
};<br />
8 9 void 10 foo(S0 &amp; /*parameter_name*/) 11 {<br />
    12 // do something with parameter_name.<br />
    13} $<br />
    $ cat<br />
    &#8211; n test &#8211; v1.cc 1 // Compile this with:<br />
               2       //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc<br />
               3 4 struct S0 5<br />
{<br />
    6 char inserted_member;<br />
    7 int m0;<br />
    8<br />
};<br />
9 10 void 11 foo(S0 &amp; /*parameter_name*/) 12 {<br />
    13 // do something with parameter_name.<br />
    14} $<br />
    $ g++ &#8211;<br />
    g &#8211; Wall &#8211; shared &#8211; o libtest &#8211; v0.so test &#8211; v0.cc $ g++ &#8211; g &#8211; Wall &#8211; shared &#8211; o libtest &#8211; v1.so test &#8211; v1.cc $ $../ build / tools / abidiff libtest &#8211; v0.so libtest &#8211; v1.so Functions changes summary : 0 Removed,<br />
    1 Changed, 0 Added function Variables changes summary : 0 Removed, 0 Changed, 0 Added variable 1 function with some indirect sub &#8211; type change : [C] &#8216;function void foo(S0&amp;)&#8217; has some indirect sub &#8211; type changes : parameter 0 of type &#8216;S0&amp;&#8217; has sub &#8211; type changes : in referenced type &#8216;struct S0&#8217; : size changed from 32 to 64 bits 1 data member insertion : &#8216;char S0::inserted_member&#8217;, at offset 0(in bits)1 data member change : &#8216;int S0::m0&#8217; offset changed from 0 to 32 $</p>
<dt>3.</p>
<dd> Detecting that functions got removed or added to a library: </p>
<pre><code>
$ cat - n test - v0.cc 1 // Compile this with:
                 2       //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                 3 4 struct S0 5
{
    6 int m0;
    7
};
8 9 void 10 foo(S0 &amp; /*parameter_name*/) 11 {
    12 // do something with parameter_name.
    13} $
    $ cat
    - n test - v1.cc 1 // Compile this with:
               2       //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
               3 4 struct S0 5
{
    6 char inserted_member;
    7 int m0;
    8
};
9 10 void 11 bar(S0 &amp; /*parameter_name*/) 12 {
    13 // do something with parameter_name.
    14} $
    $ g++ -
    g - Wall - shared - o libtest - v0.so test - v0.cc $ g++ - g - Wall - shared - o libtest - v1.so test - v1.cc $ $../ build / tools / abidiff libtest - v0.so libtest - v1.so Functions changes summary : 1 Removed,
    0 Changed, 1 Added functions Variables changes summary : 0 Removed, 0 Changed, 0 Added variable 1 Removed function : 'function void foo(S0&amp;)'
{
    _Z3fooR2S0
}
1 Added function : 'function void bar(S0&amp;)' {_Z3barR2S0} $
</code></pre>
</dl>
<h2>AUTHOR</h2>
<p> Dodji Seketeli</p>
<h2>COPYRIGHT</h2>
<p> 2014-2016, Red Hat, Inc. </p>
<h2>Index</h2>
