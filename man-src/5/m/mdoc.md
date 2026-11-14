---
title: "mdoc(5)"
name: "mdoc"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mdoc/"
description: "mdoc – Mono Documentation XML Format"
---

<p>mdoc &#8211; Mono Documentation XML Format</p>
<h2>Description</h2>
<p>The assorted Mono documentation programs generate or manipulate XML files following the mono documentation schema:</p>
<dl>
<dt><i>mdoc update</i></p>
<dd>Creates or updates mono documentation XML for a set of assemblies.</p>
<dt><i>mdoc validate</i></p>
<dd>Validates the mono documentation XML against the mono documentation XML schema.</p>
<dt><i>mdoc assemble</i></p>
<dd>Converts the mono documentation XML within a directory structure into a set of files for use with <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1).</p>
<dt><i>mdoc export-html</i></p>
<dd>Converts the mono documentation XML within a directory structure into a set of HTML files that can be viewed with a web browser.</dl>
<p> All of these tools (and more) use the common XML schema described in this man page.</p>
<h2>File/Directory Structure</h2>
<p>There are three sets of Mono documentation XML files:</p>
<dl>
<dt><code>*</code></p>
<dd><code>index.xml:</code> contains a list of all assemblies within the containing directory, and all types and namespaces within those assemblies.</p>
<dt><code>*</code></p>
<dd><code>ns-*.xml:</code> There is one ns-*.xml file for each namespace within the assembly; these files are siblings to <i>index.xml</i> . </p>
<p> Examples of <i>ns-*.xml</i> files include: <i>ns-System.xml</i>, <i>ns-System.Collections.xml</i>, and <i>ns-.xml</i> (for the root namespace, though it is recommended to NOT place types into the root namespace, as <code><a href="/docs/linux/man/1-monodoc/">monodoc</a></code>(1) doesn&#8217;t display them). </p>
<p> The <i>ns-*.xml</i> files contain per-namespace documentation.</p>
<dt><code>*</code></p>
<dd><code>NamespaceName/TypeName.xml:</code> These files are within a dotted <i>NamespaceName</i> directory, and <i>TypeName</i> is the name of the type. </p>
<p> Examples include: <i>RootType.xml</i> (if the type has no namespace), <i>System/String.xml</i>, <i>System.Collections/IEnumerable.xml</i>, and <i>System.Collections.Generic/List`1+Enumerator.xml</i> (the <i>`1</i> is the number of generic type parameters the type accepts, and everything after the <i>+</i> is a nested type).</dl>
<p> Thus, typical directory contents would resemble: </p>
<pre> index.xml
 ns-System.xml
 ns-System.Collections.Generic.xml
 System/String.xml
 System.Collections.Generic/List`1.xml</pre>
<h2>Documentation Format</h2>
<h3><code>index.xml File Format</code></h3>
<p>The <i>index.xml</i> file contains a list of the assemblies nested under the directory containing <i>index.xml</i> and all namespaces and types within those assemblies. It looks something like this: </p>
<pre> &lt;Overview&gt;
 &lt;Assemblies&gt;
 &lt;Assembly Name=&quot;mscorlib&quot; Version=&quot;2.0.0.0&quot; /&gt;
 &lt;!-- other &lt;Assembly/&gt; elements... --&gt;
 &lt;/Assemblies&gt;
 &lt;Remarks&gt;To be added.&lt;/Remarks&gt;
 &lt;Copyright&gt;To be added.&lt;/Copyright&gt;
 &lt;Types&gt;
 &lt;Namespace Name=&quot;System&quot;&gt;
 &lt;Type Name=&quot;String&quot; /&gt;
 &lt;!-- Other &lt;Type/&gt; elements --&gt;
 &lt;/Namespace&gt;
 &lt;Namespace Name=&quot;System.Collections.Generic&quot;&gt;
 &lt;Type Name=&quot;List`1&quot; DisplayName=&quot;List&amp;lt;T&amp;gt;&quot; /&gt;
 &lt;!-- Other &lt;Type/&gt; elements --&gt;
 &lt;/Namespace&gt;
 &lt;!-- other &lt;Namespace/&gt; elements --&gt;
 &lt;/Types&gt;
 &lt;Title&gt;DocTest&lt;/Title&gt;
 &lt;/Overview&gt;</pre>
<p>Most of this is maintained automatically, in particular the <i>/Overview/Assemblies</i> and <i>/Overview/Types</i> elements. </p>
<p> The <i>//Namespace/@Name</i> attribute corresponds to a directory which contains files named <i>//Type/@Name</i>.xml, while the <i>//Type/@DisplayName</i> attribute contains a C# type name (if <i>//Type/@DisplayName</i> isn&#8217;t found, then <i>//Type/@Name</i> is used as the display name). There should also be a <i>ns-[//Namespace/@Name].xml</i> file. </p>
<p> There are three elements of interest to authors: <i>/Overview/Remarks</i>, <i>/Overview/Copyright</i>, and <i>/Overview/Title</i>, which contain assembly-level documentation. These elements can contain any of the following XML elements (documented in the <code>Documentation XML Elements</code> section): <i>block</i>, <i>code</i>, <i>example</i>, <i>list</i>, <i>para</i>, <i>paramref</i>, <i>typeparamref</i>, <i>see</i>, and <i>ul</i>.</p>
<h3><code>ns-*.xml File Format</code></h3>
<p>The <i>ns-*.xml</i> files contain namespace documentation: </p>
<pre> &lt;Namespace Name=&quot;System&quot;&gt;
 &lt;Docs&gt;
 &lt;summary&gt;To be added.&lt;/summary&gt;
 &lt;remarks&gt;To be added.&lt;/remarks&gt;
 &lt;/Docs&gt;
 &lt;/Namespace&gt;</pre>
<p>The <i>/Namespace/Docs/summary</i> and <i>/Namespace/Docs/remarks</i> elements should contain namespace documentation. </p>
<p> The <i>remarks</i> and <i>summary</i> elements are documented in the <code>Documentation XML Elements</code> section.</p>
<h3><code>NamespaceName/TypeName.xml File Format</code></h3>
<p>The <i>mono documentation format</i> is similar to the Ecma documentation format, as described in ECMA-335 3rd Edition, Partition IV, Chapter 7. The principal difference from the ECMA format is that each type gets its own file, within a directory identical to the namespace of the type. There is a lot of information that is maintained automatically by <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1); Most of the information within the documentation should <i>not</i> be edited. This includes the type name (<i>/Type/@FullName</i>), implemented interfaces (<i>/Type/Interfaces</i>), member information (<i>/Type/Members/Member/@MemberName</i>, <i>/Type/Members/Member/MemberSignature</i>, <i>/Type/Members/Member/MemberType</i>, <i>/Type/Members/Member/Parameters</i>, etc.). </p>
<pre> &lt;Type Name=&quot;DocAttribute&quot; FullName=&quot;Mono.DocTest.DocAttribute&quot;&gt;
 &lt;TypeSignature Language=&quot;C#&quot; Value=&quot;public class DocAttribute : Attribute&quot; /&gt;
 &lt;AssemblyInfo&gt;
 &lt;AssemblyName&gt;DocTest&lt;/AssemblyName&gt;
 &lt;AssemblyVersion&gt;0.0.0.0&lt;/AssemblyVersion&gt;
 &lt;/AssemblyInfo&gt;
 &lt;Base&gt;
 &lt;BaseTypeName&gt;System.Attribute&lt;/BaseTypeName&gt;
 &lt;/Base&gt;
 &lt;Interfaces /&gt;
 &lt;Attributes&gt;
 &lt;Attribute&gt;
 &lt;AttributeName&gt;System.AttributeUsage(System.AttributeTargets.All)&lt;/AttributeName&gt;
 &lt;/Attribute&gt;
 &lt;/Attributes&gt;
 &lt;Docs&gt;
 &lt;summary&gt;To be added.&lt;/summary&gt;
 &lt;remarks&gt;To be added.&lt;/remarks&gt;
 &lt;/Docs&gt;
 &lt;Members&gt;
 &lt;Member MemberName=&quot;.ctor&quot;&gt;
 &lt;MemberSignature Language=&quot;C#&quot; Value=&quot;public DocAttribute (string docs);&quot; /&gt;
 &lt;MemberType&gt;Constructor&lt;/MemberType&gt;
 &lt;AssemblyInfo&gt;
 &lt;AssemblyVersion&gt;0.0.0.0&lt;/AssemblyVersion&gt;
 &lt;/AssemblyInfo&gt;
 &lt;Parameters&gt;
 &lt;Parameter Name=&quot;docs&quot; Type=&quot;System.String&quot; /&gt;
 &lt;/Parameters&gt;
 &lt;Docs&gt;
 &lt;param name=&quot;docs&quot;&gt;To be added.&lt;/param&gt;
 &lt;summary&gt;To be added.&lt;/summary&gt;
 &lt;remarks&gt;To be added.&lt;/remarks&gt;
 &lt;/Docs&gt;
 &lt;/Member&gt;
 &lt;/Members&gt;
 &lt;/Type&gt;</pre>
<p>The only elements that normally need to be edited are children of the <i>//Docs</i> elements, which usually contain the text <i>To be added.</i> The <i>/Type/Docs</i> element contains type-level documentation, while the <i>/Type/Members/Member/Docs</i> element contains per-member documentation. </p>
<p> The <i>//Docs</i> elements can contain the following elements: <i>altcompliant</i>, <i>altmember</i>, <i>example</i>, <i>exception</i>, <i>param</i>, <i>permission</i>, <i>remarks</i>, <i>returns</i>, <i>since</i>, <i>summary</i>, <i>threadsafe</i>, <i>typeparam</i>, and <i>value</i>. </p>
<p> Nested types are not members; they are types, and are documented in their own file. Consequently, the <i>NamespaceName/TypeName.xml</i> files are not recursive; you do not store a <i>&lt;Type/&gt;</i> element within a <i>&lt;Type/&gt;</i> element.</p>
<h3><code>Documentation XML Elements</code></h3>
<p>The contents of the <i>Docs</i> element is <i>identical</i> in semantics and structure to the inline C# documentation format, consisting of these elements (listed in ECMA-334 3rd Edition, Annex E, Section 2). The following are used within the element descriptions:</p>
<dl>
<dt><i>CREF</i></p>
<dd>Refers to a class (or member) reference, and is a string in the format described below in the <code>CREF FORMAT</code> section.</p>
<dt><i>TEXT</i></p>
<dd>Non-XML text, and XML should not be nested. <i></p>
<dt>XML</i></p>
<dd>Only XML elements should be nested (which indirectly may contain text), but non-whitespace text should not be an immediate child node.</p>
<dt><i>XML_TEXT</i></p>
<dd>Free-form text and XML, so that other XML elements may be nested.</dl>
<p> The following elements are used in documentation:</p>
<dl>
<dt><i>&lt;altmember cref=CREF /&gt;</i></p>
<dd><i>&lt;altmember/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Allows an entry to be generated for the <i>See Also</i> section. Use <i>&lt;see/&gt;</i> to specify a link from within text. </p>
<pre> &lt;altmember cref=&quot;P:System.Exception.Message&quot; /&gt;</pre>
<dt><i>&lt;block subset=SUBSET type=TYPE&gt;XML_TEXT&lt;/block&gt;</i></p>
<dd>Create a block of text, similar in concept to a paragraph, but is used to create divisions within the text. To some extent, a &lt;block/&gt; is equivalent to the HTML &lt;h2/&gt; tag. </p>
<p> <i>SUBSET</i> should always be the value <i>&quot;none&quot;</i>. </p>
<p> <i>TYPE</i> specifies the heading and formatting to use. Recognized types are: </p>
<p> <i>behaviors</i> Creates a section with the heading <i>Operation</i>. </p>
<p> <i>note</i> Creates a section with the heading <i>Note:</i>. </p>
<p> <i>overrides</i> Creates a section with the heading <i>Note to Inheritors</i>. </p>
<p> <i>usage</i> Creates a section with the heading <i>Usage</i>. </p>
<p> The <i>block</i> element can contain the following elements: <i>block</i>, <i>c</i>, <i>code</i>, <i>list</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, <i>subscript</i>, <i>sup</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;c&gt;XML_TEXT&lt;/c&gt;</i></p>
<dd>Set text in a code-like font (similar to the HTML &lt;tt/&gt; element). </p>
<p> The <i>c</i> element can contain the following elements: <i>code</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;code lang=LANGUAGE src=SOURCE&gt;TEXT&lt;/code&gt;</i></p>
<dd>Display multiple lines of text in a code-like font (similar to the HTML &lt;pre/&gt; element). </p>
<p> <i>LANGUAGE</i> is the language this code block is for. For example, if <i>LANGUAGE</i> is <code>C#</code>, then <i>TEXT</i> will get syntax highlighting for the C# language within the Mono Documentation Browser. </p>
<p> <i>SOURCE</i> is only interpreted by <code><a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a></code>(1). If the <i>src</i> attribute is present when <code><a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a></code>(1) is run, then <i>SOURCE</i> is a file (relative to <code><a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a></code>(1)&#8217;s <code>&#8211;out</code> directory) that should be inserted as the value for <i>TEXT</i>. The contents of <i>TEXT</i> will be ignored by <code><a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a></code>(1) and replaced on every invocation. <i>SOURCE</i> can also contain an &quot;anchor&quot;, e.g. <i>src=&quot;path/to/file.cs#RegionMarker&quot;</i>. If an anchor is present, <i>and</i> <i>LANGUAGE</i> is <i>C#</i>, then <i>#region RegionMarker</i> will be searched for, and the contents between the <i>#region</i> and the following <i>#endregion</i> will be inserted as the value for <i>TEXT</i> element.</p>
<dt><i>&lt;example&gt;XML_TEXT&lt;/example&gt;</i></p>
<dd>Indicates an example that should be displayed specially. For example: </p>
<pre> &lt;example&gt;
 &lt;para&gt;An introductory paragraph.&lt;/para&gt;
 &lt;code lang=&quot;C#&quot;&gt;
 class Example {
 public static void Main ()
 {
 System.Console.WriteLine (&quot;Hello, World!&quot;);
 }
 }
 &lt;/code&gt;
 &lt;/example&gt;</pre>
<p>The <i>example</i> element can contain the following elements: <i>c</i>, <i>code</i>, <i>list</i>, <i>para</i>, and <i>see</i>.</p>
<dt><i>&lt;exception cref=CREF&gt;XML_TEXT&lt;/exception&gt;</i></p>
<dd>Identifies an exception that can be thrown by the documented member. </p>
<p> <i>&lt;exception/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> <i>CREF</i> is the exception type that is thrown, while <i>XML_TEXT</i> contains the circumstances that would cause <i>CREF</i> to be thrown. </p>
<pre> &lt;exception cref=&quot;T:System.ArgumentNullException&quot;&gt;
 &lt;paramref name=&quot;foo&quot; /&gt; was &lt;see langword=&quot;null&quot; /&gt;.
 &lt;/exception&gt;</pre>
<p>The <i>exception</i> element can contain the following elements: <i>block</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;format type=TYPE&gt;XML_TEXT&lt;/format&gt;</i></p>
<dd>The <i>&lt;format/&gt;</i> element is an &quot;escape hatch,&quot; for including (possibly XML) content that is not valid <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) content. It&#8217;s the moral equivalent of <code><a href="/docs/linux/man/1-perlpod/">perlpod</a></code>(1) <i>=begin format</i> blocks. </p>
<p> <i>TYPE</i> is the mime type of <i>XML_TEXT</i>. <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) processors may skip <i>format/&gt;</i> blocks of they use a type that isn&#8217;t supported. </p>
<p> For example: </p>
<pre> &lt;format type=&quot;text/html&quot;&gt;
 &lt;table width=&quot;100%&quot;&gt;
 &lt;tr&gt;&lt;td style=&quot;color:red&quot;&gt;Hello, world!&lt;/td&gt;&lt;/tr&gt;
 &lt;/table&gt;
 &lt;/format&gt;</pre>
<p>would cause the embedded HTML <i>&lt;table/&gt;</i> element to be inserted inline into the resulting HTML document when <code><a href="/docs/linux/man/1-mdoc-export-html/">mdoc-export-html</a></code>(1) processes the file. (Likewise, it may be skipped if processed by another program.) </p>
<p> <i>format/&gt;</i> is intended to simplify importing documentation from existing documentation sources. It should not be relied upon, if at all possible.</p>
<dt><i>&lt;list&gt;XML&lt;/list&gt;</i></p>
<dd>Create a list or table of items. <i>&lt;list/&gt;</i> makes use of nested <i>&lt;item&gt;XML&lt;/item&gt;</i>, <i>&lt;listheader&gt;XML&lt;/listheader&gt;</i>, <i>&lt;term&gt;XML_TEXT&lt;/term&gt;</i>, and <i>&lt;description&gt;XML_TEXT&lt;/description&gt;</i> elements. </p>
<p> <i>Lists</i> have the syntax: </p>
<pre> &lt;list type=&quot;bullet&quot;&gt; &lt;!-- or type=&quot;number&quot; --&gt;
 &lt;item&gt;&lt;term&gt;Bullet 1&lt;/term&gt;&lt;/item&gt;
 &lt;item&gt;&lt;term&gt;Bullet 2&lt;/term&gt;&lt;/item&gt;
 &lt;item&gt;&lt;term&gt;Bullet 3&lt;/term&gt;&lt;/item&gt;
 &lt;/list&gt;</pre>
<p><i>Tables</i> have the syntax: </p>
<pre> &lt;list type=&quot;table&quot;&gt;
 &lt;listheader&gt; &lt;!-- listheader bolds this row --&gt;
 &lt;term&gt;Column 1&lt;/term&gt;
 &lt;description&gt;Column 2&lt;/description&gt;
 &lt;description&gt;Column 3&lt;/description&gt;
 &lt;/listheader&gt;
 &lt;item&gt;
 &lt;term&gt;Item 1-A&lt;/term&gt;
 &lt;description&gt;Item 1-B&lt;/description&gt;
 &lt;description&gt;Item 1-C&lt;/description&gt;
 &lt;/item&gt;
 &lt;item&gt;
 &lt;term&gt;Item 2-A&lt;/term&gt;
 &lt;description&gt;Item 2-B&lt;/description&gt;
 &lt;description&gt;Item 2-C&lt;/description&gt;
 &lt;/item&gt;
 &lt;/list&gt;</pre>
<p>The <i>item</i> and <i>description</i> elements can each contain text and the following elements: <i>block</i>, <i>c</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, <i>sup</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;para&gt;XML_TEXT&lt;/para&gt;</i></p>
<dd>Insert a paragraph of <i>XML_TEXT</i>. For example, </p>
<pre> &lt;para&gt;
 This is a paragraph of text.
 &lt;/para&gt;</pre>
<p>The <i>para</i> element can contain the following elements: <i>block</i>, <i>c</i>, <i>example</i>, <i>link</i>, <i>list</i>, <i>onequarter</i>, <i>paramref</i>, <i>see</i>, <i>sub</i>, <i>sup</i>, <i>typeparamref</i>, and <i>ul</i>.</p>
<dt><i>&lt;param name=NAME&gt;XML_TEXT&lt;/param&gt;</i></p>
<dd><i>&lt;param/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Describes the parameter <i>NAME</i> of the current constructor, method, or property: </p>
<pre> &lt;param name=&quot;count&quot;&gt;
 A &lt;see cref=&quot;T:System.Int32&quot; /&gt; containing the number
 of widgets to process.
 &lt;/param&gt;</pre>
<p>The <i>param</i> element can contain the following elements: <i>block</i>, <i>c</i>, <i>example</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;paramref name=NAME /&gt;</i></p>
<dd>Indicates that <i>NAME</i> is a parameter. </p>
<p> This usually renders <i>NAME</i> as italic text, so it is frequently (ab)used as an equivalent to the HTML &lt;i/&gt; element. See the <i>&lt;exception/&gt;</i> documentation (above) for an example. </p>
<dt><i>&lt;permission cref=CREF&gt;XML_TEXT&lt;/permission&gt;</i></p>
<dd>Documents the security accessibility requirements of the current member. </p>
<p> <i>&lt;permission/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> <i>CREF</i> is a type reference to the security permission required, while <i>XML_TEXT</i> is a description of why the permission is required. </p>
<pre> &lt;permission cref=&quot;T:System.Security.Permissions.FileIOPermission&quot;&gt;
 Requires permission for reading and writing files. See 
 &lt;see cref=&quot;F:System.Security.Permissions.FileIOPermissionAccess.Read&quot; /&gt;, 
 &lt;see cref=&quot;F:System.Security.Permissions.FileIOPermissionAccess.Write&quot; /&gt;.
 &lt;/permission&gt;</pre>
<p>The <i>permission</i> element can contain the following elements: <i>block</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;remarks&gt;XML_TEXT&lt;/remarks&gt;</i></p>
<dd>Contains detailed information about a member. </p>
<p> <i>&lt;remarks/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<pre> &lt;remarks&gt;
 Insert detailed information here.
 &lt;/remarks&gt;</pre>
<p>The <i>remarks</i> element can contain the following elements: <i>block</i>, <i>c</i>, <i>code</i>, <i>example</i>, <i>list</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;returns&gt;XML_TEXT&lt;/returns&gt;</i></p>
<dd><i>&lt;returns/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Describes the return value of a method: </p>
<pre> &lt;returns&gt;
 A &lt;see cref=&quot;T:System.Boolean&quot; /&gt; specifying whether 
 or not the process can access 
 &lt;see cref=&quot;P:Mono.Unix.UnixFileSystemInfo.FullName&quot; /&gt;.
 &lt;/returns&gt;</pre>
<p>The <i>returns</i> element can contain the following elements: <i>c</i>, <i>format</i>, <i>list</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;see cref=&quot;CREF&quot; /&gt;</i>, <i>&lt;see langword=&quot;LANGWORD&quot; /&gt;</i></p>
<dd>Creates a link to the specified member within the current text: </p>
<pre> &lt;see cref=&quot;M:Some.Namespace.With.Type.Method&quot; /&gt;</pre>
<p>or specifies that <i>LANGWORD</i> is a language keyword: </p>
<pre> &lt;see langword=&quot;null&quot; /&gt;</pre>
<dt><i>&lt;seealso cref=CREF /&gt;</i></p>
<dd>Do not use <i>seealso</i>, use <i>altmember</i>.</p>
<dt><i>&lt;since version=VERSION /&gt;</i></p>
<dd><i>&lt;since/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Permits specification of which version introduced the specified type or member. </p>
<pre> &lt;since version=&quot;Gtk# 2.4&quot; /&gt;</pre>
<p>This generally isn&#8217;t required, as the <i>//AssemblyInfo/AssemblyVersion</i> elements track which assembly versions contain type or member.</p>
<dt><i>&lt;summary&gt;XML_TEXT&lt;/summary&gt;</i></p>
<dd><i>&lt;summary/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Provides a (brief!) overview about a type or type member. </p>
<p> This is usually displayed as part of a class declaration, and should be a reasonably short description of the type/member. Use <i>&lt;remarks/&gt;</i> for more detailed information. </p>
<p> The <i>summary</i> element can contain the following elements: <i>block</i>, <i>list</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;typeparam name=NAME&gt;XML_TEXT&lt;/typeparam&gt;</i></p>
<dd><i>&lt;typeparam/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> This is used to document a type parameter for a generic type or generic method. </p>
<p> <i>NAME</i> is the name of the type parameter, while <i>XML_TEXT</i> contains a description of the parameter (what it&#8217;s used for, what restrictions it must meet, etc.). </p>
<pre> &lt;typeparam name=&quot;T&quot;&gt;
 The type of the underlying collection
 &lt;/typeparam&gt;</pre>
<p>The <i>typeparam</i> element can contain the following elements: <i>block</i>, <i>c</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</p>
<dt><i>&lt;typeparamref name=NAME&gt;</i></p>
<dd>Used to indicate that <i>NAME</i> is a type parameter.</p>
<dt><i>&lt;value&gt;XML_TEXT&lt;/value&gt;</i></p>
<dd><i>&lt;value/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Allows a property to be described. </p>
<pre> &lt;value&gt;
 A &lt;see cref=&quot;T:System.String&quot; /&gt; containing a widget name.
 &lt;/value&gt;</pre>
<p>The <i>value</i> element can contain the following elements: <i>block</i>, <i>c</i>, <i>example</i>, <i>list</i>, <i>para</i>, <i>paramref</i>, <i>see</i>, and <i>typeparamref</i>.</dl>
<h2>Cref Format</h2>
<p>String IDs (<i>CREF</i>s) are used to refer to a type or member of a type. String IDs are documented in ECMA-334 3rd Edition, Annex E.3.1. They consist of a <i>member type prefix</i>, the full type name (namespace + name, separated by <i>.</i>), possibly followed by the member name and other information. </p>
<p> Member type prefixes:</p>
<dl>
<dt><i>C:</i></p>
<dd>The CREF refers to a constructor. The (optional) parameter list is enclosed in parenthesis and follows the type name: <i>C:System.String(System.Char,System.Int32)</i>.</p>
<dt><i>E:</i></p>
<dd>The CREF refers to an event. The event name follows the type name: <i>E:System.AppDomain.AssemblyLoad</i>.</p>
<dt><i>F:</i></p>
<dd>The CREF refers to a field. The field name follows the type name: <i>F:System.Runtime.InteropServices.DllImportAttribute.SetLastError</i>.</p>
<dt><i>M:</i></p>
<dd>Refers to a constructor or method. Constructors may append <i>.ctor</i> to the type name (instead of using the above <i>C:</i> constructor format), while methods append the method name and an (optional) count of the number of generic parameters. Both constructors and methods may append the method parameter list enclosed in parenthesis. </p>
<p> Examples: <i>M:System.Object..ctor</i>, <i>M:System.String..ctor(System.Char[])</i>, <i>M:System.String.Concat(System.Object)</i>, <i>M:System.Array.Sort&#8220;1(&#8220;0[])</i>, <i>M:System.Collections.Generic.List`1..ctor</i>, <i>M:System.Collections.Generic.List`1.Add(`0)</i>.</p>
<dt><i>N:</i></p>
<dd>Refers to a namespace, e.g. <i>N:System</i>.</p>
<dt><i>P:</i></p>
<dd>Refers to a property. If the property is an indexer or takes parameters, the parameter types are appended to the property name and enclosed with paranthesis: <i>P:System.String.Length</i>, <i>P:System.String.Chars(System.Int32)</i>.</p>
<dt><i>T:</i></p>
<dd>The CREF refers to a type, with the number of generic types appended: <i>T:System.String</i>, <i>T:System.Collections.Generic.List`1</i>, <i>T:System.Collections.Generic.List`1.Enumerator</i>.</dl>
<p> To make matters more interesting, generic types &amp; members have two representations: the &quot;unbound&quot; representation (shown in examples above), in which class names have the count of generic parameters appended to their name. There is also a &quot;bound&quot; representation, in which the binding of generic parameters is listed within &#8216;{&#8216; and &#8216;}&#8217; or &#8216;&lt;&#8216; and &#8216;&gt;&#8217;. (Use of &#8216;&lt;&#8216; and &#8216;&gt;&#8217; is less common, as within an XML document their escaped character entities must instead be used, leading to &#8216;&amp;lt;&#8217; and &#8216;&amp;gt;&#8217;.) </p>
<p> <code>Unbound:</code></p>
<dl>
<dt><code>*</code></p>
<dd><i>T:System.Collections.Generic.List`1</i></p>
<dt><code>*</code></p>
<dd><i>T:System.Collections.Generic.Dictionary`2</i></dl>
<p> <code>Bound:</code></p>
<dl>
<dt><code>*</code></p>
<dd><i>T:System.Collections.Generic.List{System.Int32}</i></p>
<dt><code>*</code></p>
<dd><i>T:System.Collections.Generic.List&lt;System.Int32&gt;</i></p>
<dt><code>*</code></p>
<dd><i>T:System.Collections.Generic.List&amp;lt;System.Int32&amp;gt;</i></p>
<dt><code>*</code></p>
<dd><i>T:System.Predicate{System.Action{System.String}}</i></dl>
<p> As you can see, bound variants can be arbitrarily complex (just like generics). </p>
<p> Furthermore, if a generic parameter is bound to the generic parameter of a type or method, the &quot;index&quot; of the type/method&#8217;s generic parameter is used as the binding, so given </p>
<pre> class FooType {
 public static void Foo&lt;T&gt; (System.Predicate&lt;T&gt; predicate)
 {
 }
 }</pre>
<p>The CREF for this method is <i>M:FooType.Foo&#8220;1(System.Predicate{&#8220;0})</i>, <i>&#8220;0</i> is the 0th generic parameter index which is bound to <i>System.Predicate&lt;T&gt;</i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mdoc/">mdoc</a>(1), <a href="/docs/linux/man/1-monodocer/">monodocer</a>(1)</p>
<h2>Mailing Lists</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>Web Site</h2>
<p>Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
