---
title: "mdoc-export-html(1)"
name: "mdoc-export-html"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdoc-export-html/"
description: "mdoc export-html – Convert mdoc(5) XML to HTML."
---

<h2>NAME</h2>
<p> mdoc export-html &#8211; Convert <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) XML to HTML.</p>
<h2>SYNOPSIS</h2>
<p> <code>mdoc export-html</code> [OPTION]* DIRECTORIES</p>
<h2>DESCRIPTION</h2>
<p> <code>mdoc export-html</code> creates HTML files from the <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5)-formatted documentation XML files within <i>DIRECTORIES</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;default-template</code></p>
<dd> Writes the default XSLT used to <i>stdout</i>.</p>
<dt><code>&#8211;ext</code>=<i>EXTENSION</i></p>
<dd> The file extension to use for created files. </p>
<p> This defaults to <i>html</i>.</p>
<dt><code>&#8211;force-update</code></p>
<dd> Always generate new files. If not specified, will only generate a new output file if the source documentation file is newer than the target output file.</p>
<dt><code>-o</code>, <code>&#8211;out</code>=<i>DIRECTORY</i></p>
<dd> Write the created files within directory <i>DIRECTORY</i>.</p>
<dt><code>&#8211;template</code>=<i>FILE</i></p>
<dd> An XSLT file to use to generate the created files. </p>
<p> If not specified, uses the template produced by <i>&#8211;dump-template</i>. </p>
<p> See the <i>TEMPLATE FORMAT</i> section below for more information.</p>
<dt><code>&#8211;with-profile</code>=<i>PROFILE</i></p>
<dd> Only process types and members within the .NET profile <i>PROFILE</i>. May be specified multiple times. If not specified, all types and members, regardless of version, are processed. </p>
<p> Valid profiles are: </p>
<pre>
        monotouch
        net_1_0
        net_1_1
        net_2_0
        net_3_0
        net_3_5
        net_4_0
        silverlight
</pre>
<dt><code>&#8211;with-version</code>=<i>VERSION</i></p>
<dd> Only process types and members within the assembly version <i>VERSION</i>. May be specified multiple times. If not specified, all types and members, regardless of version, are processed. </p>
<p> <i>VERSION</i> is an assembly version, e.g. 2.0.5.0.</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Display a help message and exit.</dl>
<h2>TEMPLATE FORMAT</h2>
<p> The template file is an XSLT which needs to process the following input XML document: </p>
<pre>
  &lt;Page&gt;
    &lt;CollectionTitle&gt;Collection Title&lt;/CollectionTitle&gt;
    &lt;PageTitle&gt;Page Title&lt;/PageTitle&gt;
    &lt;Summary&gt;Page Summary&lt;/Summary&gt;
    &lt;Signature&gt;Type Declaration&lt;/Signature&gt;
    &lt;Remarks&gt;Type Remarks&lt;/Remarks&gt;
    &lt;Members&gt;Type Members&lt;/Members&gt;
    &lt;Copyright&gt;Documentation Copyright&lt;/Copyright&gt;
  &lt;/Page&gt;
</pre>
<p> The generated HTML also makes use of several CSS classes. You can either use the <i>create-default-style</i> named template found within the <i>&#8211;default-template</i> output to generate these classes, or explicitly define the following CSS classes:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>.CollectionTitle</i></p>
<dd>
<dt><i>.PageTitle</i></p>
<dd>
<dt><i>.Summary</i></p>
<dd>
<dt><i>.Signature</i></p>
<dd>
<dt><i>.Remarks</i></p>
<dd>
<dt><i>.Members</i></p>
<dd>
<dt><i>.Copyright</i></p>
<dd>
<dt><i>.Section</i></p>
<dd>
<dt><i>.SectionBox</i></p>
<dd>
<dt><i>.NamespaceName</i></p>
<dd>
<dt><i>.NamespaceSummary</i></p>
<dd>
<dt><i>.MemberName</i></p>
<dd>
<dt><i>.MemberSignature</i></p>
<dd>
<dt><i>.MemberBox</i></p>
<dd>
<dt><i>.Subsection</i></p>
<dd>
<dt><i>.SubsectionBox</i></p>
<dd>
<dt><i>.SignatureTable</i></p>
<dd>
<dt><i>.EnumerationsTable</i></p>
<dd>
<dt><i>.CodeExampleTable</i></p>
<dd>
<dt><i>.MembersListing</i></p>
<dd>
<dt><i>.TypesListing</i></p>
<dd>
<dt><i>.InnerSignatureTable</i></p>
<dd>
<dt><i>.TypePermissionsTable</i></p>
<dd></dl>
</dl>
<h2>HTML LINKS</h2>
<p> All members within the HTML file have an <i>id</i> attribute to permit linking to a specific member. The value of the <i>id</i> attribute is the String ID of the specified member. </p>
<p> See the <i>CREF FORMAT</i> section of <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) for more information.</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/mdoc/">http://www.mono-project.com/docs/tools+libraries/tools/mdoc/</a> for details </p>
<h2>Index</h2>
