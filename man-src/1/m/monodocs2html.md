---
title: "monodocs2html(1)"
name: "monodocs2html"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monodocs2html/"
description: "monodocs2html – Translate Monodoc XML to HTML"
---

<h2>NAME</h2>
<p> monodocs2html &#8211; Translate Monodoc XML to HTML</p>
<h2>SYNOPSIS</h2>
<p> <code>monodocs2html </code> -source:SOURCE_DIR -dest:DEST_DIR [OPTIONS]*</p>
<h2>DESCRIPTION</h2>
<p> <i>monodocs2html</i> has been obsoleted by <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1). See the <code><a href="/docs/linux/man/1-mdoc-export-html/">mdoc-export-html</a></code>(1) man page. </p>
<p> <i>monodocs2html</i> is a program that creates HTML documentation from the Monodoc documentation XML files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-dest:DEST_DIR</i></p>
<dd> Write the HTML files into the directory <i>DEST_DIR</i> .</p>
<dt><i>-dumptemplate</i></p>
<dd> Dump the default page template to standard output so that you can use it as a base for a new template for use with the <i>-template</i> option.</p>
<dt><i>-ext:FILE_EXTENSION</i></p>
<dd> <i>FILE_EXTENSION</i> is the file extension for generated files. </p>
<p> This defaults to <i>html</i> .</p>
<dt><i>-?, -help</i></p>
<dd> Show program argument information.</p>
<dt><i>-onlytype:TYPE</i></p>
<dd> Only generate HTML for the type <i>TYPE</i> .</p>
<dt><i>-source:SOURCE_DIR</i></p>
<dd> <i>SOURCE_DIR</i> is the base directory containing the Monodoc XML documentation. </p>
<p> This directory should contain an <i>index.xml</i> file, the <i>namespace-name.xml</i> files (one for each namespace), and <i>namespace-name</i> directories (one for each namespace), which will contain the <i>type.xml</i> files holding the monodoc documentation.</p>
<dt><i>-template:TEMPLATE</i></p>
<dd> Generate HTML using the page template <i>TEMPLATE</i> .</p>
<dt><i>-V, -version</i></p>
<dd> Display version and licensing information.</dl>
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
<p> The generated HTML also makes use of the following CSS classes, which should be defined so that output is nicely formatted:</p>
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
<p> All members within the HTML file have a <i>id</i> attribute to permit linking to a specific member. The value of the <i>id</i> attribute is the String ID of the specified member. See the <code>STRING ID FORMAT</code> section of the <code>monodocer</code> man page for more information.</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
