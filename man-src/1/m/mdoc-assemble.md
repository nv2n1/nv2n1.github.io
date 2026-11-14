---
title: "mdoc-assemble(1)"
name: "mdoc-assemble"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdoc-assemble/"
description: "mdoc assemble – Compile documentation for use in monodoc(1)"
---

<h2>NAME</h2>
<p> mdoc assemble &#8211; Compile documentation for use in <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>mdoc assemble</code> [OPTIONS]+ PATHS+</p>
<h2>DESCRIPTION</h2>
<p> <code>mdoc assemble</code> creates <i>.tree</i> and <i>.zip</i> files from <i>PATHS</i> for use in the <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) documentation browser. </p>
<p> The input files must have a supported <i>format</i>, specified with the <i>&#8211;format</i> option. </p>
<p> The <i>.tree</i> and <i>.zip</i> files are copied into <code>monodoc</code>&#8216;s <i>sources</i> directory, alongside a <i>.source</i> file which is used by <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) to specify where the documentation should be displayed. </p>
<p> The <i>.source</i> file has the following format: </p>
<pre><code>
  &lt;?xml version="1.0"?&gt;
  &lt;monodoc&gt;
    &lt;node label="LABEL" name="PATH" parent="PARENT"&gt;
      &lt;node label="LABEL2" name="PATH2" /&gt;
      &lt;!-- ... --&gt;
    &lt;/node&gt;
    &lt;source provider="PROVIDER" basefile="BASEFILE" path="PATH" /&gt;
    &lt;!-- other &lt;source/&gt; elements --&gt;
  &lt;/monodoc&gt;
</code></pre>
<p> The <i>/monodoc/node</i> node is an optional node that specifies where in the monodoc tree the documentation should be displayed, and <i>//node</i> elements may be nested to any depth to create trees. <i>//node/@label</i> is the label that will be displayed within the monodoc tree. </p>
<p> <i>//node/@name</i> is the name of the monodoc tree node, and may be used as the value of the <i>/monodoc/source/@path</i> value. </p>
<p> <i>//node/@parent</i> is the node name to use as the parent node. <i>$MONO_INSTALL_PREFIX/lib/monodoc/monodoc.xml</i> contains a list of such names, and this can be any <i>//node/@name</i> value. If the <i>//node/@parent</i> value isn&#8217;t found, then it&#8217;s inserted under the &quot;Various&quot; tree node. </p>
<p> The <i>/monodoc/source/@provider</i> attribute specifies which format provider should be used when reading the <i>.tree</i> and <i>.zip</i> files; this <i>must</i> correspond to one of the <i>&#8211;format</i> values. </p>
<p> The <i>/monodoc/source/@basefile</i> attribute specifies the filename prefix for the documentation files. This must be the same prefix as used with the <i>&#8211;out</i> parameter. There should be <i>no</i> filename extension on this value. </p>
<p> The <i>/monodoc/source/@path</i> attribute specifies the parent node in <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1)&#8217;s tree view where the documentation will be inserted. See the <i>$MONO_INSTALL_PREFIX/lib/monodoc/monodoc.xml</i> file for a list of <i>PATH</i> values (the <i>//node/@name</i> values), or it may be a <i>//node/@name</i> value in the same <i>.source</i> file. </p>
<p> Once the <i>BASEFILE.source</i> has been written, the documentation can be installed so that <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) will display the documentation with the command: </p>
<pre>
  cp BASEFILE.source BASEFILE.tree BASEFILE.zip \
    `pkg-config monodoc --variable=sourcesdir`
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>FORMAT</i></p>
<dd> Specifies the documentation format used within <i>PATHS</i>. Valid <i>FORMAT</i> values include: <i>ecma</i>, <i>ecmaspec</i>, <i>error</i>, <i>hb</i>, <i>man</i>, <i>simple</i>, and <i>xhtml</i>. </p>
<p> See the <i>FORMATS</i> section below for more information about these formats. </p>
<p> The default format (if none is specifed) is <i>ecma</i>. </p>
<p> The <i>&#8211;format</i> option may be interleaved with <i>PATHS</i> to change the format used for the remaining parameters (until the next <i>&#8211;format</i> option is seen), e.g.: </p>
<pre>
  mdoc assemble -o PREFIX A B --format=man C D --format=xhtml E
</pre>
<p> will assemble directories <i>A</i> and <i>B</i> with the <i>ecma</i> format, files <i>C</i> and <i>D</i> with the <i>man</i> formt, and directory <i>E</i> with the <i>xhtml</i> format.</p>
<dt><code>-o</code>, <code>&#8211;out</code>=<i>PREFIX</i></p>
<dd> Specify the output file prefix. <code>mdoc assemble</code> creates the files <i>PREFIX.zip</i> and <i>PREFIX.tree</i>.</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Display a help message and exit.</dl>
<h2>FORMATS</h2>
<p> The following documentation formats are supported:</p>
<h3>ecma</h3>
<p> The <i>Mono ECMA Documentation Format</i>, an XML documentation format with one file per type. </p>
<p> See the <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) man page for more information.</p>
<h3>ecmaspec</h3>
<p> The <i>Mono ECMA Specification Documentation Format</i>. This is not the format you&#8217;re looking for; it is the format used to represent the ECMA-334 (C#) standard within <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1). It is not used to display class library documentation; for class library documentation, use the <code>ecma</code> format.</p>
<h3>error</h3>
<p> The <i>Error Documentation Format</i> is used to present detailed error messages, and is used in <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1)&#8217;s &quot;C# Compiler Error Reference&quot; tree. </p>
<p> In this format, <i>PATHS</i> is a configuration file, containing the XML: </p>
<pre>
    &lt;ErrorProviderConfig&gt;
        &lt;FilesPath&gt;../../mcs/errors&lt;/FilesPath&gt;
        &lt;Match&gt;cs????*.cs&lt;/Match&gt;
        &lt;ErrorNumSubstringStart&gt;2&lt;/ErrorNumSubstringStart&gt;
        &lt;ErrorNumSubstringLength&gt;4&lt;/ErrorNumSubstringLength&gt;
        &lt;FriendlyFormatString&gt;CS{0:0###}&lt;/FriendlyFormatString&gt;
    &lt;/ErrorProviderConfig&gt;
</pre>
<p> The elements mean:</p>
<dl>
<dt><i>/ErrorProviderConfig/FilesPath</i></p>
<dd> Specifies where to look for files.</p>
<dt><i>/ErrorProviderConfig/Match</i></p>
<dd> Specifies the filename pattern to look for within the <i>/ErrorProviderConfig/FilesPath</i> directory.</p>
<dt><i>/ErrorProviderConfig/ErrorNumSubstringStart</i></p>
<dd> Specifies where within the filename the error number starts.</p>
<dt><i>/ErrorProviderConfig/ErrorNumSubstringLength</i></p>
<dd> Specifies how many characters after <i>/ErrorProviderConfig/ErrorNumSubstringStart</i> to use for the error number.</p>
<dt><i>/ErrorProviderConfig/FriendlyFormatString</i></p>
<dd> Specifies the formatting/display of the node in the <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) tree.</dl>
<p> For each file found, it is converted to HTML with C# syntax coloring applied.</p>
<h3>simple</h3>
<p> The <i>Simple Documentation Format</i> file format recursively adds all files and directories underneath <i>PATHS</i>. When displayed, HTML files are displayed as-is. Text files are converted into HTML by translating each newline into an HTML <i>&lt;br&gt;</i> element. No other file type is supported.</p>
<h3>man</h3>
<p> The <i>Man Page Documentation Format</i> displays groff man pages. (This is <i>not</i> a full groff parser, and only handles the man page constructs used within the mono man pages.) </p>
<p> <i>PATHS</i> is a set of XML files containing: </p>
<pre>
  &lt;?xml version=&quot;1.0&quot;?&gt;
  &lt;manpages&gt;
    &lt;manpage name=&quot;NAME&quot; page=&quot;FILE&quot; /&gt;
  &lt;/manpages&gt;
</pre>
<p> There may be multiple <i>//manpage</i> elements within the root <i>/manpage</i> element. </p>
<p> The <i>/manpages/manpage/@name</i> attribute contains the display name for the tree view node, which is also the URL of the man page when using <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1)&#8217;s <i>Lookup URL</i> command (before prefixing with a <i>man:</i> prefix). Thus, if <i>/manpages/manpage/@name</i> contains <i><a href="/docs/linux/man/1-mono/">mono</a>(1)</i>, then <i><a href="/docs/linux/man/1-man-mono/">man:mono</a>(1)</i> can be used in the <i>Lookup URL</i> command to view the <i><a href="/docs/linux/man/1-mono/">mono</a>(1)</i> man page. </p>
<p> The <i>/manpages/manpage/@page</i> attribute is the filename that contains the man page. If this file does not exist, then <i>/manpages/manpage/@name</i> will not be displayed within the tree view.</p>
<h3>xhtml</h3>
<p> The XHTML provider interprets <i>PATHS</i> as a Windows Help file XHTML TOC file and looks for referenced documents to create the help source.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1), <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5), <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1)</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> See also: <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/mdoc/">http://www.mono-project.com/docs/tools+libraries/tools/mdoc/</a> </p>
<h2>Index</h2>
