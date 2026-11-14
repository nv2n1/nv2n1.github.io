---
title: "al(1)"
name: "al"
section: "1"
letter: "a"
url: "/docs/linux/man/1-al/"
description: "al, al2 – Mono Assembly Linker"
---

<h2>NAME</h2>
<p> al, al2 &#8211; Mono Assembly Linker</p>
<h2>SYNOPSIS</h2>
<p> <code>al [option] [source-files]</code></p>
<h2>DESCRIPTION</h2>
<p> AL is the Mono assembly linkder. </p>
<p> This linker is used to put together assemblies from a collection of modules (.netmodule files), assembly manifest files and resources. </p>
<p> Do not confuse this with the <code>monolinker,</code> which is a tool to reduce the size of assemblies based on the code used. </p>
<p> Use al for processing 1.0 assemblies, use al2 to process 2.0 assemblies.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>@&lt;filename&gt;</code></p>
<dd> Read response file for more options.</p>
<dt><code>-algid:&lt;id&gt;</code></p>
<dd> Algorithm used to hash files. The &lt;id&gt; must be specified in hexadecimal.</p>
<dt><code>-base:&lt;addr&gt; | -baseaddress:&lt;addr&gt;</code></p>
<dd> Base address for the library. THIS FEATURE ISN&#8217;T IMPLEMENTED.</p>
<dt><code>-bugreport:&lt;filename&gt;</code></p>
<dd> Create a &#8216;Bug Report&#8217; file. THIS FEATURE ISN&#8217;T IMPLEMENTED.</p>
<dt><code>-comp:&lt;text&gt; | -company:&lt;text&gt;</code></p>
<dd> This inserts the company name into the assembly metadata. This is equivalent to adding the [AssemblyCompany (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-config:&lt;text&gt; | -configuration:&lt;text&gt;</code></p>
<dd> This inserts the configuration string into the assembly metadata. This is equivalent to adding the [AssemblyConfiguration (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-copy:&lt;text&gt; | -copyright:&lt;text&gt;</code></p>
<dd> This inserts the copyright message into the assembly metadata. This is equivalent to adding the [AssemblyCopyright (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-c:&lt;text&gt; | -culture:&lt;text&gt;</code></p>
<dd> This inserts the supported culture into the assembly metadata. This is equivalent to adding the [AssemblyCulture (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-delay | -delay+ | -delaysign | -delaysign+</code></p>
<dd> The generated assembly will be delay signed. This is equivalent to adding the [AssemblyDelaySignAttribute (true)] attribute into C# source code.</p>
<dt><code>-delay- | -delaysign-</code></p>
<dd> The generated assembly will be fully signed (i.e. not delay signed). This is the default option when signing (-keyfile or -keyname).</p>
<dt><code>-descr:&lt;text&gt; | -description:&lt;text&gt;</code></p>
<dd> This inserts a description of the assembly into the assembly metadata. This is equivalent to adding the [AssemblyDescription (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-e:&lt;filename&gt; | -evidence:&lt;filename&gt;</code></p>
<dd> This embed into the assembly the specified file as assembly security evidences.</p>
<dt><code>-fileversion:&lt;version&gt;</code></p>
<dd> Optional Win32 version. This overrides the normal assembly version.</p>
<dt><code>-flags:&lt;flags&gt;</code></p>
<dd> Assembly flags. The &lt;flags&gt; must be specified in hexadecimal.</p>
<dt><code>-fullpaths</code></p>
<dd> Display files using fully-qualified filenames.</p>
<dt><code>-keyf:&lt;filename&gt; | -keyfile:&lt;filename&gt;</code></p>
<dd> Strongname (sign) the output assembly using the key pair present in the specified strong name key file (snk). A full key pair is required unless the delay signing option is also specified (-delay+). This is equivalent to adding the [AssemblyKeyFile (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-keyn:&lt;text&gt; | -keyname:&lt;text&gt;</code></p>
<dd> Strongname (sign) the output assembly using the key pair present in the specified container. Delay signing isn&#8217;t supported when using key containers. This is equivalent to adding the [AssemblyKeyName (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-main:&lt;method&gt;</code></p>
<dd> Specifies the method name of the assembly entry point.</p>
<dt><code>-nologo</code></p>
<dd> Suppress the startup banner and copyright message.</p>
<dt><code>-out:&lt;filename&gt;</code></p>
<dd> Output file name for the assembly manifest.</p>
<dt><code>-prod:&lt;text&gt; | product:&lt;text&gt;</code></p>
<dd> This inserts the product name into the assembly metadata. This is equivalent to adding the [AssemblyProduct (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-productv[ersion]:&lt;text&gt;</code></p>
<dd> This inserts the product version into the assembly metadata. This is equivalent to adding the [AssemblyInformationalVersion (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-t[arget]:&lt;target&gt; | -target=&lt;target&gt;</code></p>
<dd> Valid &lt;target&gt;s are: <code>lib | library</code> to create a library (.dll), <code>exe</code> to create a console executable (.exe), and <code>win | winexe</code> to create a Windows executable (.exe).</p>
<dt><code>-template:&lt;filename&gt;</code></p>
<dd> Specifies an assembly to get default options from.</p>
<dt><code>-title:&lt;text&gt;</code></p>
<dd> This inserts an assembly title into the assembly metadata. This is equivalent to adding the [AssemblyTitle (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-trade:&lt;text&gt; | -trademark:&lt;text&gt;</code></p>
<dd> This inserts a trademark message into the assembly metadata. This is equivalent to adding the [AssemblyTrademark (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-v:&lt;version&gt; | -version:&lt;version&gt;</code></p>
<dd> This inserts the assembly version into the assembly metadata. You can use * to auto-generate remaining numbers. This is equivalent to adding the [AssemblyVersion (&quot;&lt;text&gt;&quot;)] attribute into C# source code.</p>
<dt><code>-win32icon:&lt;filename&gt;</code></p>
<dd> Use this icon for the output.</p>
<dt><code>-win32res:&lt;filename&gt;</code></p>
<dd> Specifies the Win32 resource file.</p>
<dt><code>-? | -help</code></p>
<dd> Display information about AL</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sn/">sn</a>(1), <a href="/docs/linux/man/1-monolinker/">monolinker</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
