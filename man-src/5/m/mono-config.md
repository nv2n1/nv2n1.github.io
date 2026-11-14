---
title: "mono-config(5)"
name: "mono-config"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mono-config/"
description: "mono-config – Mono runtime file format configuration"
---

<p>mono-config &#8211; Mono runtime file format configuration</p>
<h2>Description</h2>
<p>The Mono runtime will load configuration data from the installation prefix /etc/mono/config file, the ~/.mono/config or from the file pointed by the MONO_CONFIG environment variable. </p>
<p> For each assembly loaded a config file with the name: /path/to/the/assembly.exe.config is loaded as well as the ~/.mono/assemblies/ASSEMBLY/ASSEMBLY.EXT.config file. </p>
<p> This file controls the behavior of the runtime. </p>
<p> The file contains an XML-like file with various sections, all of them contained inside a section (It actually uses GMarkup to parse the file). </p>
<p> This page describes the Unix-specific and Mono-specific extensions to the configuration file; For complete details, see the <a rel="nofollow" href="http://www.mono-project.com/Config">http://www.mono-project.com/Config</a> web page.</p>
<h2>&lt;dllmap&gt; directive</h2>
<p>You use the dllmap directive to map shared libraries referenced by P/Invoke in your assemblies to a different shared library. </p>
<p> This is typically used to map Windows libraries to Unix library names. The <code>dllmap</code> element takes two attributes:</p>
<dl>
<dt><i>dll</i></p>
<dd>This should be the same string used in the DllImport attribute, optionally prefixed with &quot;i:&quot; to indicate that the string must be matched in a case-insensitive way</p>
<dt><i>target</i></p>
<dd>This should be the name of the library where the function can be found: this name should be suitable for use with the platform native shared library loading routines (dlopen etc.), so you may want to check the manpages for that, too.</dl>
<h2>&lt;dllentry&gt; directive</h2>
<p>This directive can be used to map a specific dll/function pair to a different library and also a different function name. It should appear inside a <code>dllmap</code> element with only the dll attribute specified. </p>
<p> The <code>dllentry</code> element takes 3 attributes:</p>
<dl>
<dt><i>dll</i></p>
<dd>This is the target library, where the function can be found.</p>
<dt><i>name</i></p>
<dd>This is the name of the function as it appears in the metadata: it is the name of the P/Invoke method.</p>
<dt><i>target</i></p>
<dd>This is the name of the function to lookup instead of the name specified in the P/Invoke method.</dl>
<h2>Mapping based on operating system and cpu</h2>
<p>Both the <code>dllmap</code> and the <code>dllentry</code> elements allow the following two attributes which make it easy to use a single configuration file and support multiple operating systems and architectures with different mapping requirements:</p>
<dl>
<dt><i>os</i></p>
<dd>This is the name of the operating system for which the mapping should be applied. Allowed values are: linux, osx, solaris, freebsd, openbsd, netbsd, windows, aix, hpux.</p>
<dt><i>cpu</i></p>
<dd>This is the name of the architecture for which the mapping should be applied. Allowed values are: x86, x86-64, sparc, ppc, s390, s390x, arm, mips, alpha, hppa, ia64.</p>
<dt><i>wordsize</i></p>
<dd>This is the size of registers on the target architecture, it can be either 32 or 64.</dl>
<p> The attribute value for both attributes can be a comma-separated list of the allowed values. Additionally, the first character may be a <i>&#8216;!&#8217;</i> to reverse the meaning. An attribute value of &quot;!windows,osx&quot;, for example, would mean that the entry is considered on all operating systems, except on Windows and OS X. No spaces are allowed in any part of the value. </p>
<p> Note that later entries will override the entries defined earlier in the file.</p>
<h2>Examples</h2>
<p>The following example maps references to the `cygwin1.dll&#8217; shared library to the `libc.so.6&#8242; file. </p>
<pre>&lt;configuration&gt;
 &lt;dllmap dll=&quot;i:cygwin1.dll&quot; target=&quot;libc.so.6&quot;/&gt;
&lt;/configuration&gt;</pre>
<p>The library name in the DllImport attribute is allowed to be in any case variant, like the following examples: </p>
<pre> [DllImport (&quot;cygwin1.dll&quot;)]
 [DllImport (&quot;Cygwin1.dll&quot;)]
 [DllImport (&quot;cygwiN1.Dll&quot;)]</pre>
<p>This one maps the following C# method: </p>
<pre> [DllImport (&quot;libc&quot;)]
 static extern void somefunction ();</pre>
<p>to <code>differentfunction</code> in <code>libdifferent.so</code> , but to the same function in the library <code>libanother.so</code> when running under the Solaris and FreeBSD operating systems. </p>
<pre>&lt;configuration&gt;
 &lt;dllmap dll=&quot;libc&quot;&gt;
 &lt;dllentry dll=&quot;libdifferent.so&quot; name=&quot;somefunction&quot; target=&quot;differentfunction&quot; /&gt;
 &lt;dllentry os=&quot;solaris,freebsd&quot; dll=&quot;libanother.so&quot; name=&quot;somefunction&quot; target=&quot;differentfunction&quot; /&gt;
 &lt;/dllmap&gt;
&lt;/configuration&gt;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mono/">mono</a>(1),</code><a href="/docs/linux/man/1-monodis/">monodis</a>(1),<code><a href="/docs/linux/man/1-mint/">mint</a>(1)</code> </p>
