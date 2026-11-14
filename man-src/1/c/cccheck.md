---
title: "cccheck(1)"
name: "cccheck"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cccheck/"
description: "cccheck – Perform static code contracts verification for CLR assemblies."
---

<h2>NAME</h2>
<p> cccheck &#8211; Perform static code contracts verification for CLR assemblies.</p>
<h2>SYNOPSIS</h2>
<p> <code>cccheck &#8211;assembly=&lt;assembly&gt; [options]</code></p>
<h2>DESCRIPTION</h2>
<p> Perform static code contracts verification to find bugs and inconsistences between code and specification. This includes non-null, integer analyses. </p>
<p> The assembly must have been built with the symbol CONTRACTS_FULL defined, otherwise the calls to the contract methods will have been removed by the compiler. </p>
<p> Currently only Contract.Assume() and Contract.Assert() methods are supported. Only non-null analysis is supported, the consecutive analyses are in development. An error message will be shown if cccheck is unable to process all or some of the methods of specified assembly.</p>
<h2>CONFIGURATION OPTIONS</h2>
<dl>
<dt><i>&#8211;assembly &lt;assembly-name&gt;</i></p>
<dd> The assembly to perform static verification.</p>
<dt><i>&#8211;debug</i></p>
<dd> Shows debug information about process of proving the assertions. It shows four layers of abstraction, raw layer, stack layer, heap layer, and substituted expression level.</p>
<dt><i>&#8211;method=&lt;method-name-substring&gt;</i></p>
<dd> String for finding method. It filters all methods in assembly where method name has this parameter as a substring.</p>
<dt><i>&#8211;help</i></p>
<dd> Show help for cccheck, listing configuration options. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Suppose you have a method:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>void Method()&nbsp;<wbr>{<br />
&nbsp;<wbr>object x&nbsp;<wbr>=&nbsp;<wbr>null;<br />
&nbsp;<wbr>int y&nbsp;<wbr>=&nbsp;<wbr>1;<br />
&nbsp;<wbr>if&nbsp;<wbr>(y&nbsp;<wbr>%&nbsp;<wbr>2&nbsp;<wbr>==&nbsp;<wbr>1)<br />
x&nbsp;<wbr>=&nbsp;<wbr>new object();<br />
&nbsp;<wbr>else<br />
x&nbsp;<wbr>=&nbsp;<wbr>new string(); </p>
<p>Contract.Assert(x&nbsp;<wbr>!=&nbsp;<wbr>null); } </p>
<p> After the verification the tool will have results in following format: &quot;Assertion at : [Subroutine: &lt;id&gt; Block &lt;blockId&gt; PC &lt;id&gt;] :<br />
&nbsp;<wbr>is&nbsp;<wbr>(true|false|unproven|unreachable)&quot;. (PC is a program counter) </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Alexander Chebaturkin</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2011 Alexander Chebaturkin. Released under MIT license.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
