---
title: "opannotate(1)"
name: "opannotate"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opannotate/"
description: "opannotate – produce source or assembly annotated with profile data"
---

<h2 class="name">NAME</h2>
<p> opannotate &#8211; produce source or assembly annotated with profile data </p>
<h2>SYNOPSIS</h2>
<p> <code>opannotate</code> [ <i>options</i> ] [profile specification]</p>
<h2>DESCRIPTION</h2>
<p> <code>opannotate</code> outputs annotated source and/or assembly from profile data of an OProfile session. See <a href="/docs/linux/man/1-oprofile/">oprofile</a>(1) for how to write profile specifications. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;assembly / -a</code></dt>
<dd> Output annotated assembly. The binary file to be annotated does not need full debugging information to use this option, but symbol information <i>is</i> required. Without symbol information, <code>opannotate</code> will silently refuse to annotate the binary. If this option is combined with &#8211;source, then mixed source / assembly annotations are output. </dd>
<dt><code>&#8211;demangle / -D none|smart|normal</code></dt>
<dd> none: no demangling. normal: use default demangler (default) smart: use pattern-matching to make C++ symbol demangling more readable. </dd>
<dt><code>&#8211;exclude-dependent / -x</code></dt>
<dd> Do not include application-specific images for libraries, kernel modules and the kernel. This option only makes sense if the profile session used &#8211;separate. </dd>
<dt><code>&#8211;exclude-file [files]</code></dt>
<dd> Exclude all files in the given comma-separated list of glob patterns. </dd>
<dt><code>&#8211;exclude-symbols / -e [symbols]</code></dt>
<dd> Exclude all the symbols in the given comma-separated list. </dd>
<dt><code>&#8211;help / -? / &#8211;usage</code></dt>
<dd> Show help message. </dd>
<dt><code>&#8211;image-path / -p [paths]</code></dt>
<dd> Comma-separated list of additional paths to search for binaries. This is needed to find modules in kernels 2.6 and upwards. </dd>
<dt><code>&#8211;root / -R [path]</code></dt>
<dd> A path to a filesystem to search for additional binaries. </dd>
<dt><code>&#8211;include-file [files]</code></dt>
<dd> Only include files in the given comma-separated list of glob patterns. </dd>
<dt><code>&#8211;merge / -m [lib,cpu,tid,tgid,unitmask,all]</code></dt>
<dd> Merge any profiles separated in a &#8211;separate session. </dd>
<dt><code>&#8211;include-symbols / -i [symbols]</code></dt>
<dd> Only include symbols in the given comma-separated list. </dd>
<dt><code>&#8211;objdump-params [params]</code></dt>
<dd> Pass the given parameters as extra values when calling objdump. If more than one option is to be passed to objdump, the parameters must be enclosed in a quoted string. </dd>
<p> An example of where this option is useful is when your toolchain does not automatically recognize instructions that are specific to your processor. For example, on IBM POWER7/RHEL 6, objdump must be told that a binary file may have POWER7-specific instructions. The opannotate option to show the POWER7-specific instructions is:<br />
&#8211;objdump-params=-Mpower7 </p>
<p> The opannotate option to show the POWER7-specific instructions, the source code (&#8211;source) and the line numbers (-l) would be:<br />
&#8211;objdump-params=&quot;-Mpower7 -l &#8211;source&quot; </p>
<dt><code>&#8211;output-dir / -o [dir]</code></dt>
<dd> Output directory. This makes opannotate output one annotated file for each source file. This option can&#8217;t be used in conjunction with &#8211;assembly. </dd>
<dt><code>&#8211;search-dirs / -d [paths]</code></dt>
<dd> Comma-separated list of paths to search for source files. You may need to use this option when the debug information for an image contains relative paths. </dd>
<dt><code>&#8211;base-dirs / -b [paths]</code></dt>
<dd> Comma-separated list of paths to strip from debug source files, prior to looking for them in &#8211;search-dirs. </dd>
<dt><code>&#8211;session-dir=dir_path</code></dt>
<dd> Use sample database from the specified directory <i>dir_path</i> instead of the default locations. If <i>&#8211;session-dir</i> is not specified, then <code>opannotate</code> will search for samples in <i>&lt;current_dir&gt;/oprofile_data</i> first. If that directory does not exist, the standard session-dir of /var/lib/oprofile is used. </dd>
<dt><code>&#8211;source / -s</code></dt>
<dd> Output annotated source. This requires debugging information to be available for the binaries. </dd>
<dt><code>&#8211;threshold / -t [percentage]</code></dt>
<dd> Only output data for symbols that have more than the given percentage of total samples. </dd>
<dt><code>&#8211;verbose / -V [options]</code></dt>
<dd> Give verbose debugging output. </dd>
<dt><code>&#8211;version / -v</code></dt>
<dd> Show version. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by opannotate. </p>
<h2>FILES</h2>
<p> <i>&lt;current_dir&gt;/oprofile_data/samples</i></p>
<dl>
<dt>
</dt><dd> Or</dd></dl>
<p> <i>/var/lib/oprofile/samples/</i> </p>
<dl>
<dt>
</dt><dd> The location of the generated sample files.</dd></dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</dt>
<dd>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
