---
title: "abipkgdiff(1)"
name: "abipkgdiff"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abipkgdiff/"
description: "abipkgdiff – compare ABIs of ELF files in software packages"
---

<h2>NAME</h2>
<p> abipkgdiff &#8211; compare ABIs of ELF files in software packages </p>
<p> <code>abipkgdiff</code> compares the Application Binary Interfaces (ABI) of the <i>ELF</i> binaries contained in two software packages. The software package formats currently supported are <i>Deb</i>, <i>RPM</i>, <i>tar</i> archives (either compressed or not) and plain directories that contain binaries. </p>
<p> For a comprehensive ABI change report that includes changes about function and variable sub-types, the two input packages must be accompanied with their debug information packages that contain debug information in <i>DWARF</i> format.</p>
<h2>INVOCATION</h2>
<pre>
abipkgdiff [option] &lt;package1&gt; &lt;package2&gt;
</pre>
<p> <code>package1</code> and <code>package2</code> are the packages that contain the binaries to be compared.</p>
<h2>ENVIRONMENT</h2>
<p> abipkgdiff loads two default <i>suppression specifications files</i>, merges their content and use it to filter out ABI change reports that might be considered as false positives to users.</p>
<dl>
<dt>&bull;</p>
<dd> Default system-wide suppression specification file </p>
<p> It&#8217;s located by the optional environment variable LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE. If that environment variable is not set, then abipkgdiff tries to load the suppression file $libdir/libabigail/libabigail-default.abignore. If that file is not present, then no default system-wide suppression specification file is loaded.</p>
<dt>&bull;</p>
<dd> Default user suppression specification file. </p>
<p> It&#8217;s located by the optional environment LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE. If that environment variable is not set, then abipkgdiff tries to load the suppression file $HOME/.abignore. If that file is not present, then no default user suppression specification is loaded.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd> <i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd> <code>&#8211;debug-info-pkg1 | &#8211;d1</code> &lt;path&gt; </p>
<p> For cases where the debug information for <i>package1</i> is split out into a separate file, tells <code>abipkgdiff</code> where to find that separate debug information package.</p>
<dt>&bull;</p>
<dd> <code>&#8211;debug-info-pkg2 | &#8211;d2</code> &lt;path&gt; </p>
<p> For cases where the debug information for <i>package2</i> is split out into a separate file, tells <code>abipkgdiff</code> where to find that separate debug information package.</p>
<dt>&bull;</p>
<dd> <code>&#8211;devel-pkg1 | &#8211;devel1</code> &lt;path&gt; </p>
<p> Specifies where to find the <i>Development Package</i> associated with the first package to be compared. That <i>Development Package</i> at <code>path</code> should at least contain header files in which public types exposed by the libraries (of the first package to be compared) are defined. When this option is provided, the tool filters out reports about ABI changes to types that are <i>NOT</i> defined in these header files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;devel-pkg2 | &#8211;devel2</code> &lt;path&gt; </p>
<p> Specifies where to find the <i>Development Package</i> associated with the second package to be compared. That <i>Development Package</i> at <code>path</code> should at least contains header files in which public types exposed by the libraries (of the second package to be compared) are defined. When this option is provided, the tool filters out reports about ABI changes to types that are <i>NOT</i> defined in these header files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;dso-only</code> </p>
<p> Compare ELF files that are shared libraries, only. Do not compare executable files, for instance.</p>
<dt>&bull;</p>
<dd> <code>&#8211;redundant</code> In the diff reports, do display redundant changes. A redundant change is a change that has been displayed elsewhere in a given report.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-linkage-name</code> </p>
<p> In the resulting report, do not display the linkage names of the added, removed, or changed functions or variables.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-added-syms</code> </p>
<p> Do not show the list of functions, variables, or any symbol that was added.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-added-binaries</code> </p>
<p> Do not show the list of binaries that got added to the second package. </p>
<p> Please note that the presence of such added binaries is not considered like an ABI change by this tool; as such, it doesn&#8217;t have any impact on the exit code of the tool. It does only have an informational value. Removed binaries are, however, considered as an ABI change.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-abignore</code> </p>
<p> Do not search the <i>package2</i> for the presence of suppression files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-parallel</code> </p>
<p> By default, <code>abipkgdiff</code> will use all the processors it has available to execute concurrently. This option tells it not to extract packages or run comparisons in parallel.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-default-suppression</code> </p>
<p> Do not load the <i>default suppression specification files</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;suppressions | &#8211;suppr</code> &lt;<i>path-to-suppressions</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppressions</i>. Note that this option can appear multiple times on the command line. In that case, all of the suppression specification files are taken into account. </p>
<p> Please note that, by default, if this option is not provided, then the <i>default suppression specification files</i> are loaded .</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd> <code>&#8211;show-identical-binaries</code> Show the names of the all binaries compared, including the binaries whose ABI compare equal. By default, when this option is not provided, only binaries with ABI changes are mentionned in the output.</p>
<dt>&bull;</p>
<dd> <code>&#8211;fail-no-dbg</code> </p>
<p> Make the program fail and return a non-zero exit code if couldn&#8217;t read any of the debug information that comes from the debug info packages that were given on the command line. If no debug info package were provided on the command line then this option is not active. </p>
<p> Note that the non-zero exit code returned by the program as a result of this option is the constant <code>ABIDIFF_ERROR</code>. To know the numerical value of that constant, please refer to the <i>exit code documentation</i>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;keep-tmp-files</code> </p>
<p> Do not erase the temporary directory files that are created during the execution of the tool.</p>
<dt>&bull;</p>
<dd> <code>&#8211;verbose</code> </p>
<p> Emit verbose progress messages.</dl>
<h2>RETURN VALUE</h2>
<p> The exit code of the <code>abipkgdiff</code> command is either 0 if the ABI of the binaries compared are equal, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the value of the exit code is the same as for the <i>abidiff tool</i>.</p>
<h2>AUTHOR</h2>
<p> Dodji Seketeli</p>
<h2>COPYRIGHT</h2>
<p> 2014-2016, Red Hat, Inc. </p>
<h2>Index</h2>
