---
title: "omniidl(1)"
name: "omniidl"
section: "1"
letter: "o"
url: "/docs/linux/man/1-omniidl/"
description: "omniidl – omniORB idl compiler"
---

<h2>NAME</h2>
<p> omniidl &#8211; omniORB idl compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>omniidl</code> [options] -b&lt;back-end&gt; [back-end options] file</p>
<h2>DESCRIPTION</h2>
<p> omniidl is the omniORB IDL compiler front end. If a back-end is not specified, it checks the input IDL file for validity, and produces no output. Usually, a language mapping back-end is specified, so stubs and skeletons in the target language are produced. </p>
<p> The input files are processed by the C preprocessor before they are parsed by the compiler. </p>
<h2>COMMON OPTIONS</h2>
<dl>
<dt><code>-b&lt;backend&gt;</code></p>
<dd> Run the specified back-end (e.g., -bcxx = C++, -bpython = Python)</p>
<dt><code>-D&lt;name&gt;=&lt;value&gt;</code></p>
<dd> Define &lt;name&gt; for the C preprocessor.</p>
<dt><code>-U&lt;name&gt;</code></p>
<dd> Undefine &lt;name&gt; for the C preprocessor.</p>
<dt><code>-I&lt;dir&gt;</code></p>
<dd> Include &lt;dir&gt; in the C preprocessor search path.</p>
<dt><code>-E</code></p>
<dd> Only run the C preprocessor, sending its output to stdout.</p>
<dt><code>-Y&lt;cmd&gt;</code></p>
<dd> Use &lt;cmd&gt; as the preprocessor instead of the default.</p>
<dt><code>-N</code></p>
<dd> Do not run the C preprocessor.</p>
<dt><code>-Wp&lt;arg&gt;</code></p>
<dd> Send &lt;arg&gt; to the C preprocessor.</p>
<dt><code>-Wb&lt;arg&gt;</code></p>
<dd> Send &lt;arg&gt; to the back-end.</p>
<dt><code>-nf</code></p>
<dd> Do not warn about unresolved forward declarations.</p>
<dt><code>-k</code></p>
<dd> Keep comments after declarations, to be used by some back-ends.</p>
<dt><code>-K</code></p>
<dd> Keep comments before declarations, to be used by some back-ends.</p>
<dt><code>-C&lt;dir&gt;</code></p>
<dd> Change directory to &lt;dir&gt; before writing output files.</p>
<dt><code>-d</code></p>
<dd> Dump the parsed IDL then exit, without running a back-end.</p>
<dt><code>-p&lt;dir&gt;</code></p>
<dd> Use &lt;dir&gt; as a path to find omniidl back-ends.</p>
<dt><code>-V</code></p>
<dd> Print version information then exit.</p>
<dt><code>-u</code></p>
<dd> Print usage information.</p>
<dt><code>-v</code></p>
<dd> Verbose: trace compilation stages. </p>
</dl>
<h2>C++ BACK-END</h2>
<p> Choose the C++ back-end with <code>-bcxx.</code> The C++ back-end is only available when you have omniORB for C++ installed. </p>
<p> The C++ back-end produces two output files: a header and a stub/skeleton file. By default they are named by appending suffixes <code>.hh</code> and <code>SK.cc</code> to the base name of the input IDL file. </p>
<p> If the <code>-Wba</code> option is specified, then a third file is generated (with default suffix <code>DynSK.cc</code> ), containing code for TypeCode and Any. </p>
<h2>C++ BACK-END OPTIONS</h2>
<dl>
<dt><code>-Wbh=&lt;suffix&gt;</code></p>
<dd> Use &lt;suffix&gt; instead of .hh</p>
<dt><code>-Wbs=&lt;suffix&gt;</code></p>
<dd> Use &lt;suffix&gt; instead of SK.cc</p>
<dt><code>-Wbd=&lt;suffix&gt;</code></p>
<dd> Use &lt;suffix&gt; instead of DynSK.cc. If the same suffix is specified for <code>-Wbs</code> and <code>-Wbd</code> then a single skeleton file containing all the definitions is output.</p>
<dt><code>-Wba</code></p>
<dd> Generate definitions for TypeCode and Any.</p>
<dt><code>-Wbinline</code></p>
<dd> Output stubs for #included IDL files in line with the main file.</p>
<dt><code>-Wbtp</code></p>
<dd> Generate tie implementation skeletons.</p>
<dt><code>-Wbtf</code></p>
<dd> Generate flattened tie implementation skeletons.</p>
<dt><code>-Wbsplice-modules</code></p>
<dd> Splice together multiply-opened modules into one.</p>
<dt><code>-Wbexample</code></p>
<dd> Generate example implementation code.</p>
<dt><code>-WbBOA</code></p>
<dd> Generate BOA compatible skeletons.</p>
<dt><code>-Wbkeep_inc_path</code></p>
<dd> Preserve IDL #include paths in generated #include directives.</p>
<dt><code>-Wbuse_quotes</code></p>
<dd> Use quotes in #include directives (e.g. &quot;foo&quot; rather than &lt;foo&gt;). </p>
</dl>
<h2>PYTHON BACK-END</h2>
<p> Choose the Python back-end with <code>-bpython.</code> The Python back-end produces Python packages according to the standard IDL to Python mapping, to be used with omniORBpy. The Python back-end is only available when you have omniORBpy installed. </p>
<p> The Python back-end generates Python package directories named after the modules declared in IDL, as required by the IDL to Python mapping. It also creates separate stub files that are imported by the packages. </p>
<h2>PYTHON BACK-END OPTIONS</h2>
<dl>
<dt><code>-Wbinline</code></p>
<dd> Output stubs for #included IDL files in line with the main file.</p>
<dt><code>-Wbglobal=&lt;name&gt;</code></p>
<dd> Use &lt;name&gt; as the name for the global IDL scope (default _GlobalIDL).</p>
<dt><code>-Wbpackage=&lt;name&gt;</code></p>
<dd> Put both Python modules and stub files in package &lt;name&gt;.</p>
<dt><code>-Wbmodules=&lt;name&gt;</code></p>
<dd> Put Python modules in package &lt;name&gt;</p>
<dt><code>-Wbstubs=&lt;name&gt;</code></p>
<dd> Put stub files in package &lt;name&gt; </p>
</dl>
<h2>SEE ALSO</h2>
<p> See the omniORB or omniORBpy manual for full details of <code>omniidl.</code> </p>
<h2>AUTHOR</h2>
<p> Duncan Grisby </p>
<h2>Index</h2>
