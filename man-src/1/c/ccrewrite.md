---
title: "ccrewrite(1)"
name: "ccrewrite"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccrewrite/"
description: "ccrewrite – Rewrite CLR assemblies for runtime code contract verification."
---

<h2>NAME</h2>
<p> ccrewrite &#8211; Rewrite CLR assemblies for runtime code contract verification.</p>
<h2>SYNOPSIS</h2>
<p> <code>ccrewrite &#8211;assembly=&lt;assembly&gt; [options]</code></p>
<h2>DESCRIPTION</h2>
<p> Rewrite CLR assemblies to convert calls into the System.Diagnostics.Contracts namespace to perform runtime contract verification. This includes contract inheritance for virtual methods. </p>
<p> The assembly must have been built with the symbol CONTRACTS_FULL defined, otherwise the calls to the contract methods will have been removed by the compiler. </p>
<p> Currently only pre-conditions are supported, using the Contract.Requires() method. Contract inheritance for virtual methods is supported. Only a limited range of operations and types can be used within a pre-condition, an error message will be shown if ccrewrite is unable to process the specified assembly.</p>
<h2>CONFIGURATION OPTIONS</h2>
<dl>
<dt><i>&#8211;assembly &lt;assembly-name&gt;</i></p>
<dd> The assembly to rewrite. If no &#8211;output option is specified, then this file overwritten with the rewritten version.</p>
<dt><i>&#8211;debug</i></p>
<dd> Use debug information if available to improve the usefulness of contract failure messages.</p>
<dt><i>&#8211;help</i></p>
<dd> Show help for ccrewrite, listing configuration options.</p>
<dt><i>&#8211;level &lt;level&gt; (default=4)</i></p>
<dd> Set the which contract types are present in rewritten assembly: 0 = No contracts; 1 = Release requires; 2 = Requires; 3 = Ensures; 4 = Invariants; (Each level includes all previous levels)</p>
<dt><i>&#8211;output &lt;file-name&gt;</i></p>
<dd> Write the rewritten assembly to the specified file. If this is not present then the input assembly file is overwritten with the rewritten version.</p>
<dt><i>&#8211;rewrite (default=true)</i></p>
<dd> Rewrite the assembly. If false, then nothing is done.</p>
<dt><i>&#8211;throwOnFailure (default=false)</i></p>
<dd> Throw a ContractException on unhandled contract failure. The default behaviour is to Assert. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Chris Bacon</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 Chris Bacon. Released under MIT license.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
