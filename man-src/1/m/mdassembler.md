---
title: "mdassembler(1)"
name: "mdassembler"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdassembler/"
description: "mdassembler – Compile documentation for use in monodoc browser"
---

<h2>NAME</h2>
<p> mdassembler &#8211; Compile documentation for use in monodoc browser</p>
<h2>SYNOPSIS</h2>
<p> <code>mdassembler</code> OPTIONS* DIRS+</p>
<h2>DESCRIPTION</h2>
<p> <i>mdassembler</i> has been obsoleted by <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1). See the <code><a href="/docs/linux/man/1-mdoc-assemble/">mdoc-assemble</a></code>(1) man page. </p>
<p> <i>mdassembler</i> is a program that creates <i>.tree</i> and <i>.zip</i> files for use in the <code>monodoc</code> documentation browser. </p>
<p> The <i>.tree</i> and <i>.zip</i> files are copied into monodoc&#8217;s <i>sources</i> directory, and reside with a <i>.source</i> file which is used by <code>monodoc</code> to specify where the documentation should be displayed. The <i>.source</i> file&#8217;s <i>/monodoc/source/@basefile</i> attribute specifies the filename prefix for the documentation files. This must be the same prefix as used with the <code>&#8211;out</code> parameter. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;ecma</i></p>
<dd> The documentation found within <i>DIRS</i> is in the Mono ECMA documentation format. See the <code>Mono ECMA Documentation Format</code> section below.</p>
<dt><i>&#8211;ecmaspec</i></p>
<dd> The documentation found within <i>DIRS</i> is in the ECMA Specification documentation format. See the <code>Mono ECMA Specification Documentation Format</code> section below.</p>
<dt><i>&#8211;error</i></p>
<dd> The documentation found within <i>DIRS</i> is in &quot;error&quot; format. See the <code>Error Documentation Format</code> section below.</p>
<dt><i>&#8211;help</i></p>
<dd> Show program argument information.</p>
<dt><i>&#8211;man</i></p>
<dd> The documentation found within <i>DIRS</i> is in man page format. See the <code>Man Page Documentation Format</code> section below.</p>
<dt><i>-o, &#8211;out PREFIX</i></p>
<dd> Specify the output file prefix. <code>mdassembler</code> creates the files <i>PREFIX.zip</i> and <i>PREFIX.tree</i> .</p>
<dt><i>&#8211;simple</i></p>
<dd> The documentation found within <i>DIRS</i> is in &quot;simple&quot; format. See the <code>Simple Documentation Format</code> section below.</p>
<dt><i>&#8211;xhtml, &#8211;hb</i></p>
<dd> The documentation found within <i>DIRS</i> is in XHTML format. See the <code>XHTML Documentation Format</code> section below.</dl>
<h2>FORMATS</h2>
<p> The following documentation formats are supported:</p>
<h3>Mono ECMA Documentation Format</h3>
<p> An XML documentation format with one file per type. </p>
<p> See the <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) man page for more information.</p>
<h3>Mono ECMA Specification Documentation Format</h3>
<p> This is not the format you&#8217;re looking for. </p>
<p> This is the format used to represent the ECMA-334 (C#) standard within <code>monodoc</code>. It is not used to display class library documentation; for class library documentation, use the <code>&#8211;ecma</code> format.</p>
<h3>Error Documentation Format</h3>
<p> Used to present detailed error messages, and is used in <code>monodoc</code>&#8216;s &quot;C# Compiler Error Reference&quot; tree. <i>DIRS</i> is not a directory, but is instead a configuration file, containing the XML: </p>
<pre>
    &lt;ErrorProviderConfig&gt;
        &lt;FilesPath&gt;../../mcs/errors&lt;/FilesPath&gt;
        &lt;Match&gt;cs????*.cs&lt;/Match&gt;
        &lt;ErrorNumSubstringStart&gt;2&lt;/ErrorNumSubstringStart&gt;
        &lt;ErrorNumSubstringLength&gt;4&lt;/ErrorNumSubstringLength&gt;
        &lt;FriendlyFormatString&gt;CS{0:0###}&lt;/FriendlyFormatString&gt;
    &lt;/ErrorProviderConfig&gt;
</pre>
<p> <i>/ErrorProviderConfig/FilesPath</i> specifies where to look for files, <i>/ErrorProviderConfig/Match</i> specifies the filename pattern to look for within <i>/ErrorProviderConfig/FilesPath</i>, <i>/ErrorProviderConfig/ErrorNumSubstringStart</i> and <i>/ErrorProviderConfig/ErrorNumSubstringLength</i> control which portion of the filename is used as the error number, and <i>/ErrorProviderConfig/FriendlyFormatString</i> controls how the formatting/display of the node in the <code>monodoc</code> tree. </p>
<p> For each file found, it is converted to HTML with C# syntax coloring applied.</p>
<h3>Simple Documentation Format</h3>
<p> Converts text files into HTML by translating each newline into an HTML <i>&lt;br&gt;</i> element.</p>
<h3>Man Page Documentation Format</h3>
<p> Converts man pages into HTML for display.</p>
<h3>XHTML Documentation Format</h3>
<p> Copies the XHTML file as-is.</p>
<h2>EXAMPLES</h2>
<p> To install your documenation for use with monodoc:</p>
<dl>
<dt><i>Create a PREFIX.source file</i></p>
<dd> with the contents: </p>
<pre>
&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;monodoc&gt;
  &lt;source provider=&quot;FORMAT&quot; basefile=&quot;PREFIX&quot; path=&quot;PATH&quot;/&gt;
&lt;/monodoc&gt;
</pre>
<p> where FORMAT is the documentation format contained within the <i>PREFIX.tree</i> file, e.g. <i>ecma</i>, or <i>simple</i>. <i>PREFIX is the basename of the </i> <i>.tree</i> and <i>.zip</i> files that <code>mdassembler</code> creates. <i>PATH</i> is the &quot;path&quot; in the monodoc tree that should contain the documentation. See the <i>@prefix@/lib/monodoc/monodoc.xml</i> file for a list of PATH values (the <i>//node/@name</i> values). </p>
<p> See also: <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/monodoc/generating-documentation/">http://www.mono-project.com/docs/tools+libraries/tools/monodoc/generating-documentation/</a></p>
<dt><i>Create your documentation</i></p>
<dd> See also the <code><a href="/docs/linux/man/1-monodocer/">monodocer</a></code>(1) man page, e.g. </p>
<pre>
        monodocer -assembly:foo.dll -path:foo/en
</pre>
<dt><i>Assemble the documentation</i></p>
<dd>
<pre>
        mdassembler --ecma foo/en PREFIX
</pre>
<p> Make sure that you use the same <i>PREFIX</i> here as you did above.</p>
<dt><i>Install the documentation by using the command</i></p>
<dd>
<pre>
        cp PREFIX.source PREFIX.tree PREFIX.zip \
        `pkg-config monodoc --variable=sourcesdir`
</pre>
<p> (Note the backticks used in the <code>pkg-config</code> command!) This copies the <i>.source</i> , <i>.tree</i> , and <i>.zip</i> files into the <code>monodoc</code> <i>sources</i> directory, which will allow <code>monodoc</code> to display the documentation.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdcs2ecma/">mdcs2ecma</a></code>(1), <code><a href="/docs/linux/man/1-mdnormalizer/">mdnormalizer</a></code>(1), <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1), <code><a href="/docs/linux/man/1-mdoc-assemble/">mdoc-assemble</a></code>(1), <code><a href="/docs/linux/man/1-mdvalidator/">mdvalidator</a></code>(1), <code><a href="/docs/linux/man/1-monodocer/">monodocer</a></code>(1), <code><a href="/docs/linux/man/1-monodocs2html/">monodocs2html</a></code>(1)</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> See also: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> and <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/mdassembler/">http://www.mono-project.com/docs/tools+libraries/tools/mdassembler/</a> </p>
<h2>Index</h2>
