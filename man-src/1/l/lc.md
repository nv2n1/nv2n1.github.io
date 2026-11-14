---
title: "lc(1)"
name: "lc"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lc/"
description: "lc – Mono License Compiler"
---

<h2>NAME</h2>
<p> lc &#8211; Mono License Compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>lc -c filename -t targetassembly [-i reference&#8230;] [-v] [-o outputpath] [-nologo]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>lc</i> tool is a license compiler for Mono. It&#8217;s used to convert a licenses.licx file to a resource that can be embedded into an executable. </p>
<p> When using commercial components for .NET they often require a license resource at runtime to make sure the developer was licensed to use this control. The most common way of making sure the component was properly licensed is by using license resources. At compile time the developer uses the <i>lc</i> tool to convert a licenses.licx file to a programname.exe.licenses file and embed that as a managed resource during compilation.</p>
<h2>RUNTIME OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>&#8211;complist=filename</code>, <code>-c filename</code></p>
<dd> This option is used to specify the input file, the licenses.licx file to create a license reesource for. This option is required. The license compiler will read each line in this file and try to load the types specified on that line.</p>
<dt><code>&#8211;target=assemblyname</code>, <code>-t targetassembly</code></p>
<dd> full assembly name with file extension for the target assembly. The license compiler uses this as a key when compiling the licenses. It has to match the assembly the resource will be embedded in. This option is required.</p>
<dt><code>&#8211;load=reference</code>, <code>-i reference</code></p>
<dd> Assembly reference to load before trying to compile a license. This option is needed for assemblies where the references are not in the gac. Compilers should pass all references to the license compiler.</p>
<dt><code>&#8211;verbose,</code>, <code>-v</code></p>
<dd> Gives more verbose output about the license compiling process.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Displays usage instructions.</p>
<dt><code>&#8211;outdir=path</code>, <code>-o path</code></p>
<dd> Target path file the licenses resource. By default the license compiler emits the resource in the current directory. The filename will always match the target assembly passed to &#8211;target with .licenses added.</p>
<dt><code>&#8211;nologo</code></p>
<dd> Do not emit the &quot;Mono License Compiler&quot; logo on stdout while compilng. </p>
</dl>
<h2>LICENSE FILES</h2>
<p> The format for the license files (licenses.licx) is the following: </p>
<pre>
        # comment
        namespace.type, assemblyname
        namespace.type, full-assemblyname
</pre>
<p> All lines starting with a # are ignored. the first form requires that the assembly was loaded through the &#8211;load,-i option but does not require the full assembly name, only the first part. </p>
<p> The second form requires the full assembly name including locale, version and publickeytoken. </p>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at the <a rel="nofollow" href="http://www.mono-project.com/community/help/mailing-lists/">http://www.mono-project.com/community/help/mailing-lists/</a></p>
<h2>WEB SITE</h2>
<p> <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1) </p>
<h2>Index</h2>
