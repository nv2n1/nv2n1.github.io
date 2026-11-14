---
title: "synopsis(1)"
name: "synopsis"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synopsis/"
description: "synopsis – simple frontend to the Synopsis framework, a multi-language source code introspection tool that provides a variety of representations for the parsed code, to enable further processing su..."
---

<h2>NAME</h2>
<p> synopsis &#8211; simple frontend to the Synopsis framework, a multi-language source code introspection tool that provides a variety of representations for the parsed code, to enable further processing such as documentation extraction, reverse engineering, and source-to-source translation.</p>
<h2>DESCRIPTION</h2>
<p> Usage : synopsis [options] &lt;input files&gt;</p>
<h3>List of options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage summary.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Operate verbosely.</p>
<dt><code>-d</code> <code>&#8211;debug</code></p>
<dd> Operate in debug mode.</p>
<dt><code>-P</code> <code>&#8211;profile</code></p>
<dd> Profile execution.</p>
<dt><code>-o</code> &lt;file&gt;, <code>&#8211;output=</code>&lt;file&gt;</p>
<dd> Write output to &lt;file&gt;.</p>
<dt><code>-p</code> &lt;lang&gt;, <code>&#8211;parser=</code>&lt;lang&gt;</p>
<dd> Select a parser for &lt;lang&gt;.</p>
<dt><code>-Wp</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</p>
<dd> Send &lt;args&gt; to the parser.</p>
<dt> <code>-t</code> [&lt;markup&gt;]</p>
<dt><code>&#8211;translate[=</code>&lt;markup&gt;]</p>
<dd>
<dd>Translate comments to doc-strings, processing it as &lt;markup&gt; (typical values are &#8216;javadoc&#8217; or &#8216;rst&#8217;).</p>
<dt><code>&#8211;cfilter=</code>&lt;filter&gt;</p>
<dd> Specify a comment filter.</p>
<dt><code>&#8211;cprocessor=</code>&lt;processor&gt;</p>
<dd> Specify a comment processor.</p>
<dt><code>-Wc</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</p>
<dd> Send &lt;args&gt; to the comment translator.</p>
<dt><code>-l</code></p>
<dd> Run the linker.</p>
<dt><code>-Wl</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</p>
<dd> Send &lt;args&gt; to the linker.</p>
<dt><code>&#8211;linker=</code>&lt;processor&gt;</p>
<dd> Link, and invoke &lt;processor&gt;.</p>
<dt> <code>-f</code> &lt;type&gt;,</p>
<dt><code>&#8211;formatter=</code>&lt;type&gt;</p>
<dd>
<dd>Select a formatter for &lt;type&gt;.</p>
<dt><code>-Wf</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</p>
<dd> Send &lt;args&gt; to the formatter.</p>
<dt><code>-I</code> &lt;path&gt;</p>
<dd> Add &lt;path&gt; to list of include paths.</p>
<dt><code>-D</code> &lt;macro&gt;</p>
<dd> Add &lt;macro&gt; to list of predefined macros.</p>
<dt> <code>-s</code> &lt;directory&gt;,</p>
<dt><code>&#8211;sxr=</code>&lt;directory&gt;</p>
<dd>
<dd>Specify sxr directory. If given, process source cross-references.</p>
<dt><code>&#8211;probe</code></p>
<dd> Probe the specified processor. </p>
</dl>
<h2>Index</h2>
