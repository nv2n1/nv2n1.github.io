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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display usage summary.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version information.</dd>
<dt><code>-v</code> <code>&#8211;verbose</code></dt>
<dd> Operate verbosely.</dd>
<dt><code>-d</code> <code>&#8211;debug</code></dt>
<dd> Operate in debug mode.</dd>
<dt><code>-P</code> <code>&#8211;profile</code></dt>
<dd> Profile execution.</dd>
<dt><code>-o</code> &lt;file&gt;, <code>&#8211;output=</code>&lt;file&gt;</dt>
<dd> Write output to &lt;file&gt;.</dd>
<dt><code>-p</code> &lt;lang&gt;, <code>&#8211;parser=</code>&lt;lang&gt;</dt>
<dd> Select a parser for &lt;lang&gt;.</dd>
<dt><code>-Wp</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</dt>
<dd> Send &lt;args&gt; to the parser.</dd>
<dt> <code>-t</code> [&lt;markup&gt;]</dt>
<dt><code>&#8211;translate[=</code>&lt;markup&gt;]</dt>
<dd>
</dd><dd>Translate comments to doc-strings, processing it as &lt;markup&gt; (typical values are &#8216;javadoc&#8217; or &#8216;rst&#8217;).</dd>
<dt><code>&#8211;cfilter=</code>&lt;filter&gt;</dt>
<dd> Specify a comment filter.</dd>
<dt><code>&#8211;cprocessor=</code>&lt;processor&gt;</dt>
<dd> Specify a comment processor.</dd>
<dt><code>-Wc</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</dt>
<dd> Send &lt;args&gt; to the comment translator.</dd>
<dt><code>-l</code></dt>
<dd> Run the linker.</dd>
<dt><code>-Wl</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</dt>
<dd> Send &lt;args&gt; to the linker.</dd>
<dt><code>&#8211;linker=</code>&lt;processor&gt;</dt>
<dd> Link, and invoke &lt;processor&gt;.</dd>
<dt> <code>-f</code> &lt;type&gt;,</dt>
<dt><code>&#8211;formatter=</code>&lt;type&gt;</dt>
<dd>
</dd><dd>Select a formatter for &lt;type&gt;.</dd>
<dt><code>-Wf</code>,&lt;arg&gt;[,&lt;arg&gt;&#8230;]</dt>
<dd> Send &lt;args&gt; to the formatter.</dd>
<dt><code>-I</code> &lt;path&gt;</dt>
<dd> Add &lt;path&gt; to list of include paths.</dd>
<dt><code>-D</code> &lt;macro&gt;</dt>
<dd> Add &lt;macro&gt; to list of predefined macros.</dd>
<dt> <code>-s</code> &lt;directory&gt;,</dt>
<dt><code>&#8211;sxr=</code>&lt;directory&gt;</dt>
<dd>
</dd><dd>Specify sxr directory. If given, process source cross-references.</dd>
<dt><code>&#8211;probe</code></dt>
<dd> Probe the specified processor. </dd>
</dl>
<h2>Index</h2>
