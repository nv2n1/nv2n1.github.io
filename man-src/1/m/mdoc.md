---
title: "mdoc(1)"
name: "mdoc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdoc/"
description: "mdoc – Mono documentation management tool"
---

<h2>NAME</h2>
<p> mdoc &#8211; Mono documentation management tool</p>
<h2>SYNOPSIS</h2>
<p> <code>mdoc</code> <i>command</i> [<i>options</i>] [<i>args</i>]</p>
<h2>OVERVIEW</h2>
<p> <i>mdoc</i> is an assembly-based documentation management system. </p>
<p> <i>mdoc</i> permits creating and updating documentation <i>stubs</i> based on the contents of an assembly. It does not rely on documentation found within the source code. </p>
<p> The advantages are:</p>
<dl>
<dt><code>*</code></p>
<dd> <code>Code readability.</code> Good documentation is frequently (a) verbose, and (b) filled with examples. (For comparison, compare Microsoft .NET Framework documentation, which is often a page or more of docs for each member, to JavaDoc documentation, which can often be a sentence for each member.) </p>
<p> Inserting good documentation into the source code can frequently bloat the source file, as the documentation can be longer than the actual method that is being documented.</p>
<dt><code>*</code></p>
<dd> <code>Localization.</code> In-source documentation formats (such as <i>csc /doc</i>) have no support for multiple human languages. If you need to support more than one human language for documentation purposes, <i>mdoc</i> is useful as it permits each language&#8217;s output to reside in its own directory, and <i>mdoc</i> can add types/members for each separate documentation directory.</p>
<dt><code>*</code></p>
<dd> <code>Administration.</code> It&#8217;s not unusual to have separate documentation and development teams. It&#8217;s also possible that the documentation team will have minimal experience with the programming language being used. In such circumstances, inline documentation is not desirable as the documentation team could inadvertantly insert an error into the source code while updating the documentation. Alternatively, you may not want the documentation team to have access to the source code for security reasons. <i>mdoc</i> allows the documentation to be kept <i>completely</i> separate and distinct from the source code used to create the assembly.</dl>
<p> Documentation can be generated using the <code>mdoc update</code> command: </p>
<pre>
    mdoc update -o docs/en ProjectName.dll
</pre>
<p> Once the documentation stubs have been generated (and hopefully later filled in with actual documentation), there are three ways to view the documentation:</p>
<dl>
<dt><code>*</code></p>
<dd> To generate a simple directory of HTML pages (one HTML file per type), use <code>mdoc export-html</code>: </p>
<pre>
    mdoc export-html -o /srv/www/htdocs/ProjectName docs/en
</pre>
<dt><code>*</code></p>
<dd> To use an ASP.NET webapp to display the sources, see: <i><a rel="nofollow" href="http://anonsvn.mono-project.com/source/trunk/monodoc/engine/web/">http://anonsvn.mono-project.com/source/trunk/monodoc/engine/web/</a></i>. </p>
<p> From a <i>monodoc</i> source checkout, you can do this: </p>
<pre>
    cd engine
    make web
</pre>
<p> This will use <code><a href="/docs/linux/man/1-xsp/">xsp</a></code>(1) to serve the ASP.NET webapp; Visit <i><a rel="nofollow" href="http://localhost:8080/">http://localhost:8080/</a></i> to view the documentation.</p>
<dt><code>*</code></p>
<dd> To use the <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) documentation browser, you must first <i>assemble</i> the documentation: </p>
<pre>
    mdoc assemble -o ProjectName docs/en
</pre>
<p> The above command creates the files <i>ProjectName.tree</i> and <i>ProjectName.zip</i>. An additional <i>ProjectName.sources</i> file must be provided which describes where in the help system the documentation should be hooked up; it is a very simple XML file, like this: </p>
<pre>
    &lt;?xml version=&quot;1.0&quot;?&gt;
    &lt;monodoc&gt;
      &lt;source provider=&quot;ecma&quot; basefile=&quot;ProjectName&quot;
        path=&quot;various&quot; /&gt;
    &lt;/monodoc&gt;
</pre>
<p> The above configuration file describes that the documentation is in ECMA format, that the base file name is <i>ProjectName</i> and that it should be hooked up in the <i>&quot;various&quot;</i> part of the documentation tree. If you want to look at the various nodes defined in the documentation, you can look at the <i>monodoc.xml</i> file which is typically installed in <i>/usr/lib/monodoc/monodoc.xml</i>. </p>
<p> Once you have all of the required files (.zip, .tree and .sources) you can install them into the system with the following command: </p>
<pre>
    cp ProjectName.tree ProjectName.zip ProjectName.source \
      `pkg-config monodoc --variable sourcesdir`
</pre>
<p> The above will copy the files into the directory that Monodoc has registered; you might need root permissions to do this. The actual directory is returned by the <i>pkg-config</i> invocation.</dl>
<h2>MDOC COMMANDS</h2>
<p> <code>mdoc assemble</code></p>
<dl>
<dt>
<dd> Compiles documentation for use within the <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) browser. </p>
<p> See the <code><a href="/docs/linux/man/1-mdoc-assemble/">mdoc-assemble</a></code>(1) man page for details.</dl>
<p> <code>mdoc export-html</code></p>
<dl>
<dt>
<dd> Exports documentation into a directory structure of HTML files. </p>
<p> See the <code><a href="/docs/linux/man/1-mdoc-export-html/">mdoc-export-html</a></code>(1) man page for details.</dl>
<p> <code>mdoc export-msxdoc</code></p>
<dl>
<dt>
<dd> Exports documentation into the single-file <i>Microsoft XML Documentation</i> format. </p>
<p> See the <code><a href="/docs/linux/man/1-mdoc-export-msxdoc/">mdoc-export-msxdoc</a></code>(1) man page for details.</dl>
<p> <code>mdoc help</code></p>
<dl>
<dt>
<dd> View internal help for a given command. </p>
<pre>
    mdoc help assemble
</pre>
<p> is equivalent to: </p>
<pre>
    mdoc assemble --help
</pre>
<p> Multiple sub-commands may be listed at once: </p>
<pre>
    mdoc help assemble export-html update validate
</pre>
</dl>
<p> <code>mdoc update</code></p>
<dl>
<dt>
<dd> Updates documentation, adding and removing members based upon a reference assembly. </p>
<p> See the <code><a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a></code>(1) man page for details.</dl>
<p> <code>mdoc validate</code></p>
<dl>
<dt>
<dd> Validates the documentation against the Mono documentation schema. </p>
<p> See the <code><a href="/docs/linux/man/1-mdoc-validate/">mdoc-validate</a></code>(1) man page for details.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-mdoc/">mdoc</a>(5), <a href="/docs/linux/man/1-mdoc-assemble/">mdoc-assemble</a>(1), <a href="/docs/linux/man/1-mdoc-export-html/">mdoc-export-html</a>(1), <a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a>(1), <a href="/docs/linux/man/1-mdoc-validate/">mdoc-validate</a>(1)</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/mdoc/">http://www.mono-project.com/docs/tools+libraries/tools/mdoc/</a> for details </p>
<h2>Index</h2>
