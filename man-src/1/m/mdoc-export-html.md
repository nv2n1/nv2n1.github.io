---

title: "mdoc-export-html(1)"
name: "mdoc-export-html"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdoc-export-html/"
description: "mdoc export-html – Convert mdoc(5) XML to HTML."
---

<p> mdoc export-html &#8211; Convert <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) XML to HTML.</p>
<h2>SYNOPSIS</h2>
<p> <code>mdoc export-html</code> [OPTION]* DIRECTORIES</p>
<h2>DESCRIPTION</h2>
<p> <code>mdoc export-html</code> creates HTML files from the <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5)-formatted documentation XML files within <i>DIRECTORIES</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;default-template</code></dt>
<dd> Writes the default XSLT used to <i>stdout</i>.</dd>
<dt><code>&#8211;ext</code>=<i>EXTENSION</i></dt>
<dd> The file extension to use for created files. </dd>
<p> This defaults to <i>html</i>.</p>
<dt><code>&#8211;force-update</code></dt>
<dd> Always generate new files. If not specified, will only generate a new output file if the source documentation file is newer than the target output file.</dd>
<dt><code>-o</code>, <code>&#8211;out</code>=<i>DIRECTORY</i></dt>
<dd> Write the created files within directory <i>DIRECTORY</i>.</dd>
<dt><code>&#8211;template</code>=<i>FILE</i></dt>
<dd> An XSLT file to use to generate the created files. </dd>
<p> If not specified, uses the template produced by <i>&#8211;dump-template</i>. </p>
<p> See the <i>TEMPLATE FORMAT</i> section below for more information.</p>
<dt><code>&#8211;with-profile</code>=<i>PROFILE</i></dt>
<dd> Only process types and members within the .NET profile <i>PROFILE</i>. May be specified multiple times. If not specified, all types and members, regardless of version, are processed. </dd>
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
<dt><code>&#8211;with-version</code>=<i>VERSION</i></dt>
<dd> Only process types and members within the assembly version <i>VERSION</i>. May be specified multiple times. If not specified, all types and members, regardless of version, are processed. </dd>
<p> <i>VERSION</i> is an assembly version, e.g. 2.0.5.0.</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display a help message and exit.</dd></dl>
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
<dl>
<dt><i>.CollectionTitle</i></dt>
<dd>
</dd><dt><i>.PageTitle</i></dt>
<dd>
</dd><dt><i>.Summary</i></dt>
<dd>
</dd><dt><i>.Signature</i></dt>
<dd>
</dd><dt><i>.Remarks</i></dt>
<dd>
</dd><dt><i>.Members</i></dt>
<dd>
</dd><dt><i>.Copyright</i></dt>
<dd>
</dd><dt><i>.Section</i></dt>
<dd>
</dd><dt><i>.SectionBox</i></dt>
<dd>
</dd><dt><i>.NamespaceName</i></dt>
<dd>
</dd><dt><i>.NamespaceSummary</i></dt>
<dd>
</dd><dt><i>.MemberName</i></dt>
<dd>
</dd><dt><i>.MemberSignature</i></dt>
<dd>
</dd><dt><i>.MemberBox</i></dt>
<dd>
</dd><dt><i>.Subsection</i></dt>
<dd>
</dd><dt><i>.SubsectionBox</i></dt>
<dd>
</dd><dt><i>.SignatureTable</i></dt>
<dd>
</dd><dt><i>.EnumerationsTable</i></dt>
<dd>
</dd><dt><i>.CodeExampleTable</i></dt>
<dd>
</dd><dt><i>.MembersListing</i></dt>
<dd>
</dd><dt><i>.TypesListing</i></dt>
<dd>
</dd><dt><i>.InnerSignatureTable</i></dt>
<dd>
</dd><dt><i>.TypePermissionsTable</i></dt>
<dd></dd></dl>
</dl>
<h2>HTML LINKS</h2>
<p> All members within the HTML file have an <i>id</i> attribute to permit linking to a specific member. The value of the <i>id</i> attribute is the String ID of the specified member. </p>
<p> See the <i>CREF FORMAT</i> section of <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) for more information.</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</dt>
<dd></dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/mdoc/">http://www.mono-project.com/docs/tools+libraries/tools/mdoc/</a> for details </p>
