---
title: "opreport(1)"
name: "opreport"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opreport/"
description: "opreport – produce symbol or binary image summaries"
---

<h2 class="name">NAME</h2>
<p> opreport &#8211; produce symbol or binary image summaries </p>
<h2>SYNOPSIS</h2>
<p> <code>opreport</code> [ <i>options</i> ] [profile specification]</p>
<h2>DESCRIPTION</h2>
<p> <code>opreport</code> outputs binary image summaries, or per-symbol data, from OProfile profiling sessions. See <a href="/docs/linux/man/1-oprofile/">oprofile</a>(1) for how to write profile specifications. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;accumulated / -a</code></p>
<dd> Accumulate sample and percentage counts in the symbol list. </p>
<dt><code>&#8211;debug-info / -g</code></p>
<dd> Show source file and line for each symbol. </p>
<dt><code>&#8211;demangle / -D none|smart|normal</code></p>
<dd> none: no demangling. normal: use default demangler (default) smart: use pattern-matching to make C++ symbol demangling more readable. </p>
<dt><code>&#8211;callgraph / -c</code></p>
<dd> Show call graph information if available. </p>
<dt><code>&#8211;details / -d</code></p>
<dd> Show per-instruction details for all selected symbols. </p>
<dt><code>&#8211;exclude-dependent / -x</code></p>
<dd> Do not include application-specific images for libraries, kernel modules and the kernel. This option only makes sense if the profile session used &#8211;separate. </p>
<dt><code>&#8211;exclude-symbols / -e [symbols]</code></p>
<dd> Exclude all the symbols in the given comma-separated list. </p>
<dt><code>&#8211;global-percent / -%</code></p>
<dd> Make all percentages relative to the whole profile. </p>
<dt><code>&#8211;help / -? / &#8211;usage</code></p>
<dd> Show help message. </p>
<dt><code>&#8211;image-path / -p [paths]</code></p>
<dd> Comma-separated list of additional paths to search for binaries. This is needed to find modules in kernels 2.6 and upwards. </p>
<dt><code>&#8211;root / -R [path]</code></p>
<dd> A path to a filesystem to search for additional binaries. </p>
<dt><code>&#8211;include-symbols / -i [symbols]</code></p>
<dd> Only include symbols in the given comma-separated list. </p>
<dt><code>&#8211;long-filenames / -f</code></p>
<dd> Output full paths instead of basenames. </p>
<dt><code>&#8211;merge / -m [lib,cpu,tid,tgid,unitmask,all]</code></p>
<dd> Merge any profiles separated in a &#8211;separate session. </p>
<dt><code>&#8211;no-header / -n</code></p>
<dd> Don&#8217;t output a header detailing profiling parameters. </p>
<dt><code>&#8211;output-file / -o [file]</code></p>
<dd> Output to the given file instead of stdout. </p>
<dt><code>&#8211;reverse-sort / -r</code></p>
<dd> Reverse the sort from the default. </p>
<dt><code>&#8211;session-dir=dir_path</code></p>
<dd> Use sample database from the specified directory <i>dir_path</i> instead of the default locations. If <i>&#8211;session-dir</i> is not specified, then <code>opreport</code> will search for samples in <i>&lt;current_dir&gt;/oprofile_data</i> first. If that directory does not exist, the standard session-dir of /var/lib/oprofile is used. </p>
<dt><code>&#8211;show-address / -w</code></p>
<dd> Show each symbol&#8217;s VMA address. </p>
<dt><code>&#8211;sort / -s [vma,sample,symbol,debug,image]</code></p>
<dd> Sort the list of symbols by, respectively, symbol address, number of samples, symbol name, debug filename and line number, binary image filename. </p>
<dt><code>&#8211;symbols / -l</code></p>
<dd> List per-symbol information instead of a binary image summary.<br />
 Usually, the total of all per-symbols samples for a given binary image equals the summary count for the binary image (shown by running <code>opreport</code> with no options). However, it&#8217;s possible for some sample addresses to fall outside the range of any symbols for a given binary image. In such cases, the total number of per-symbols samples for the binary image may be less than the summary count for the image. Running <code>opreport</code> with the <i>&#8211;verbose=debug</i> option will display an informational message when this difference is detected. This difference is typically very small and can be ignored. </p>
<dt><code>&#8211;threshold / -t [percentage]</code></p>
<dd> Only output data for symbols that have more than the given percentage of total samples. </p>
<dt><code>&#8211;verbose / -V [options]</code></p>
<dd> Give verbose debugging output. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show version. </p>
<dt><code>&#8211;xml / -X</code></p>
<dd> Generate XML output. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognized by opreport. </p>
<h2>FILES</h2>
<p> <i>&lt;current_dir&gt;/oprofile_data/samples</i></p>
<dl>
<dt>
<dd> Or</dl>
<p> <i>/var/lib/oprofile/samples/</i> </p>
<dl>
<dt>
<dd> The location of the generated sample files.</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
