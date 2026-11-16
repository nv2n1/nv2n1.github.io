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
<dt><code>-b&lt;backend&gt;</code></dt>
<dd> Run the specified back-end (e.g., -bcxx = C++, -bpython = Python)</dd>
<dt><code>-D&lt;name&gt;=&lt;value&gt;</code></dt>
<dd> Define &lt;name&gt; for the C preprocessor.</dd>
<dt><code>-U&lt;name&gt;</code></dt>
<dd> Undefine &lt;name&gt; for the C preprocessor.</dd>
<dt><code>-I&lt;dir&gt;</code></dt>
<dd> Include &lt;dir&gt; in the C preprocessor search path.</dd>
<dt><code>-E</code></dt>
<dd> Only run the C preprocessor, sending its output to stdout.</dd>
<dt><code>-Y&lt;cmd&gt;</code></dt>
<dd> Use &lt;cmd&gt; as the preprocessor instead of the default.</dd>
<dt><code>-N</code></dt>
<dd> Do not run the C preprocessor.</dd>
<dt><code>-Wp&lt;arg&gt;</code></dt>
<dd> Send &lt;arg&gt; to the C preprocessor.</dd>
<dt><code>-Wb&lt;arg&gt;</code></dt>
<dd> Send &lt;arg&gt; to the back-end.</dd>
<dt><code>-nf</code></dt>
<dd> Do not warn about unresolved forward declarations.</dd>
<dt><code>-k</code></dt>
<dd> Keep comments after declarations, to be used by some back-ends.</dd>
<dt><code>-K</code></dt>
<dd> Keep comments before declarations, to be used by some back-ends.</dd>
<dt><code>-C&lt;dir&gt;</code></dt>
<dd> Change directory to &lt;dir&gt; before writing output files.</dd>
<dt><code>-d</code></dt>
<dd> Dump the parsed IDL then exit, without running a back-end.</dd>
<dt><code>-p&lt;dir&gt;</code></dt>
<dd> Use &lt;dir&gt; as a path to find omniidl back-ends.</dd>
<dt><code>-V</code></dt>
<dd> Print version information then exit.</dd>
<dt><code>-u</code></dt>
<dd> Print usage information.</dd>
<dt><code>-v</code></dt>
<dd> Verbose: trace compilation stages. </dd>
</dl>
<h2>C++ BACK-END</h2>
<p> Choose the C++ back-end with <code>-bcxx.</code> The C++ back-end is only available when you have omniORB for C++ installed. </p>
<p> The C++ back-end produces two output files: a header and a stub/skeleton file. By default they are named by appending suffixes <code>.hh</code> and <code>SK.cc</code> to the base name of the input IDL file. </p>
<p> If the <code>-Wba</code> option is specified, then a third file is generated (with default suffix <code>DynSK.cc</code> ), containing code for TypeCode and Any. </p>
<h2>C++ BACK-END OPTIONS</h2>
<dl>
<dt><code>-Wbh=&lt;suffix&gt;</code></dt>
<dd> Use &lt;suffix&gt; instead of .hh</dd>
<dt><code>-Wbs=&lt;suffix&gt;</code></dt>
<dd> Use &lt;suffix&gt; instead of SK.cc</dd>
<dt><code>-Wbd=&lt;suffix&gt;</code></dt>
<dd> Use &lt;suffix&gt; instead of DynSK.cc. If the same suffix is specified for <code>-Wbs</code> and <code>-Wbd</code> then a single skeleton file containing all the definitions is output.</dd>
<dt><code>-Wba</code></dt>
<dd> Generate definitions for TypeCode and Any.</dd>
<dt><code>-Wbinline</code></dt>
<dd> Output stubs for #included IDL files in line with the main file.</dd>
<dt><code>-Wbtp</code></dt>
<dd> Generate tie implementation skeletons.</dd>
<dt><code>-Wbtf</code></dt>
<dd> Generate flattened tie implementation skeletons.</dd>
<dt><code>-Wbsplice-modules</code></dt>
<dd> Splice together multiply-opened modules into one.</dd>
<dt><code>-Wbexample</code></dt>
<dd> Generate example implementation code.</dd>
<dt><code>-WbBOA</code></dt>
<dd> Generate BOA compatible skeletons.</dd>
<dt><code>-Wbkeep_inc_path</code></dt>
<dd> Preserve IDL #include paths in generated #include directives.</dd>
<dt><code>-Wbuse_quotes</code></dt>
<dd> Use quotes in #include directives (e.g. &quot;foo&quot; rather than &lt;foo&gt;). </dd>
</dl>
<h2>PYTHON BACK-END</h2>
<p> Choose the Python back-end with <code>-bpython.</code> The Python back-end produces Python packages according to the standard IDL to Python mapping, to be used with omniORBpy. The Python back-end is only available when you have omniORBpy installed. </p>
<p> The Python back-end generates Python package directories named after the modules declared in IDL, as required by the IDL to Python mapping. It also creates separate stub files that are imported by the packages. </p>
<h2>PYTHON BACK-END OPTIONS</h2>
<dl>
<dt><code>-Wbinline</code></dt>
<dd> Output stubs for #included IDL files in line with the main file.</dd>
<dt><code>-Wbglobal=&lt;name&gt;</code></dt>
<dd> Use &lt;name&gt; as the name for the global IDL scope (default _GlobalIDL).</dd>
<dt><code>-Wbpackage=&lt;name&gt;</code></dt>
<dd> Put both Python modules and stub files in package &lt;name&gt;.</dd>
<dt><code>-Wbmodules=&lt;name&gt;</code></dt>
<dd> Put Python modules in package &lt;name&gt;</dd>
<dt><code>-Wbstubs=&lt;name&gt;</code></dt>
<dd> Put stub files in package &lt;name&gt; </dd>
</dl>
<h2>SEE ALSO</h2>
<p> See the omniORB or omniORBpy manual for full details of <code>omniidl.</code> </p>
<h2>AUTHOR</h2>
<p> Duncan Grisby </p>
<h2>Index</h2>
