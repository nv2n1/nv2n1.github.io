---
title: "monodocer(1)"
name: "monodocer"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monodocer/"
description: "monodocer – ECMA Documentation Format Support"
---

<h2>NAME</h2>
<p> monodocer &#8211; ECMA Documentation Format Support</p>
<h2>SYNOPSIS</h2>
<p> <code>monodocer</code> [OPTIONS]*</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-assembly:ASSEMBLY</i></p>
<dd> <i>ASSEMBLY</i> is a .NET assembly to generate documentation stubs for. </p>
<p> Specify a file path or the name of a GAC&#8217;d assembly.</p>
<dt><i>-delete</i></p>
<dd> Allow monodocer to delete members from documentation files. The only members deleted are for members which are no longer present within the assembly. </p>
<p> If a type is no longer present, the documentation file is <i>not</i> deleted, but is instead <i>renamed</i> to have a <code>.remove </code> extension.</p>
<dt><i>-?, -help</i></p>
<dd> Show program argument information.</p>
<dt><i>-ignoremembers</i></p>
<dd> Do not update members. </p>
<p> This will add documentation stubs for added types, but will <i>not</i> add or remove documentation for any members of any type (including any added types).</p>
<dt><i>-importslashdoc:FILE</i></p>
<dd> <i>FILE</i> is an XML file generated with the <code>/doc:FILE</code> C# compiler flag (e.g. <i>mcs -doc:foo.xml foo.cs</i> ). Import the member documentation contained within <i>FILE</i> into the documentation format used by monodoc.</p>
<dt><i>-name:NAME</i></p>
<dd> <i>NAME</i> is the name of the project this documentation is for. </p>
<p> This sets the <i>/Overview/Title</i> element within the <i>index.xml</i> file created at the directory specified by <i>-path</i> . This is used by some programs for title information (e.g. <i>monodocs2html</i> ).</p>
<dt><i>-namespace:NAMESPACE</i></p>
<dd> Only update the types within the namespace <i>NAMESPACE</i> .</p>
<dt><i>-overrides</i></p>
<dd> Include overridden methods in documentation. </p>
<p> This normally isn&#8217;t necessary, as the Mono Documentation Browser will provide a link to the base type members anyway, as will <i>monodocs2html</i> if the base type is within the same assembly.</p>
<dt><i>-path:OUTPUT_DIR</i></p>
<dd> <i>OUTPUT_DIR</i> is the directory which will contain the new/updated documentation stubs.</p>
<dt><i>-pretty</i></p>
<dd> Indent the XML files nicely.</p>
<dt><i>-since:SINCE</i></p>
<dd> Create a &lt;since/&gt; element for added types and members with the value <i>SINCE</i> . </p>
<p> For example, when given <i>-since:Gtk# 2.4</i> an element will be inserted into the <i>Docs</i> element for all added types and type members: </p>
<pre>
        &lt;since version=&quot;Gtk# 2.4&quot; /&gt;
</pre>
<p> The Mono Documentation Browser and <i>monodocs2html</i> will use this element to specify in which version a member was added.</p>
<dt><i>-type:TYPE</i></p>
<dd> Only create/update documentation for the type <i>TYPE</i> .</p>
<dt><i>-updateto:PATH</i></p>
<dd> When updating documentation, write the updated documentation files into the directory <i>PATH</i> .</p>
<dt><i>-V, -version</i></p>
<dd> Display version and licensing information.</dl>
<h2>DESCRIPTION</h2>
<p> <code>monodocer</code> has been obsoleted by <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1). See the <code><a href="/docs/linux/man/1-mdoc-update/">mdoc-update</a></code>(1) man page. </p>
<p> <i>monodocer</i> is a program that creates XML documentation stubs in the ECMA Documentation Format. It does not rely on documentation found within the source code. </p>
<p> The advantages are:</p>
<dl>
<dt><i>*</i></p>
<dd> <code>Code readability.</code> Good documentation is frequently (a) verbose, and (b) filled with examples. (For comparison, compare Microsoft .NET Framework documentation, which is often a page or more of docs for each member, to JavaDoc documentation, which can often be a sentence for each member.) </p>
<p> Inserting good documentation into the source code can frequently bloat the source file, as the documentation can be longer than the actual method that is being documented.</p>
<dt><i>*</i></p>
<dd> <code>Localization.</code> In-source documentation formats (such as <code>/doc</code> ) have no support for multiple human languages. If you need to support more than one human language for documentation purposes, <i>monodocer</i> is useful as it permits each language to get its own directory, and <i>monodocer</i> can add types/members for each separate documentation directory.</p>
<dt><i>*</i></p>
<dd> <code>Administration.</code> It&#8217;s not unusual to have separate documentation and development teams. It&#8217;s also possible that the documentation team will have minimal experience with the programming language being used. In such circumstances, inline documentation is not desirable as the documentation team could inadvertantly insert an error into the source code while updating the documentation. Alternatively, you may not want the documentation team to have access to the source code for security reasons. <i>monodocer</i> allows the documentation to be kept <i>completely</i> separate and distinct from the source code used to create the assembly.</dl>
<p> To turn the <i>monodocer </i> documentation into something that can be consumed by the Mono Documentation Browser (the desktop help browser, or the web interface for it) it is necessary to compile the documentation into a packed format. This is done with the mdassembler tool, for example, you could use this toolchain like this: </p>
<pre>
        $ monodocer -assembly:MyWidgets -path:generated_docs
        $ mdassembler --ecma generated_docs -out:MyWidgets
</pre>
<p> The above would generate a MyWidgets.zip and a MyWidgets.tree that can then be installed in the system. In addition to the two files (.zip and .tree) you must provide a .sources file which describes where in the help system the documentation should be hooked up, it is a very simple XML file, like this: </p>
<pre>
&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;monodoc&gt;
  &lt;source provider=&quot;ecma&quot; basefile=&quot;MyWidgets&quot; path=&quot;classlib-gnome&quot;/&gt;
&lt;/monodoc&gt;
</pre>
<p> The above configuration file describes that the documentation is in ECMA format (the compiled version) that the base file name is MyWidgets and that it should be hooked up in the &quot;classlib-gnome&quot; part of the tree. If you want to look at the various nodes defined in the documentation, you can look at monodoc.xml file which is typically installed in /usr/lib/monodoc/monodoc.xml. </p>
<p> Once you have all of your files (.zip, .tree and .sources) you can install them into the system with the following command: </p>
<pre>
        $ cp MyWidgets.tree MyWidgets.zip MyWidgets.source `pkg-config monodoc --variable sourcesdir`
  
</pre>
<p> The above will copy the files into the directory that Monodoc has registered (you might need root permissions to do this). The actual directory is returned by the <i>pkg-config </i> invocation.</p>
<h2>STRING ID FORMAT</h2>
<p> String IDs are used to refer to a type or member of a type. String IDs are documented in ECMA-334 3rd Edition, Annex E.3.1. They consist of a <i>member type prefix</i> , the full type name (namespace + name, separated by &#8216;.&#8217;), possibly followed by the member name and other information. </p>
<p> Member type prefixes:</p>
<dl>
<dt><i>E:</i></p>
<dd> The String ID refers to an event. The event name follows the type name: <i>E:System.AppDomain.AssemblyLoad</i></p>
<dt><i>F:</i></p>
<dd> The String ID refers to a field. The field name follows the type name: <i>F:System.Runtime.InteropServices.DllImportAttribute.SetLastError</i></p>
<dt><i>M:</i></p>
<dd> Refers to a constructor or method. Constructors append <i>.ctor</i> to the type name, while methods append the method name (with an optional count of the number of generic parameters). </p>
<p> If the constructor or method take arguments, these are listed within paranthesis after the constructor/method name: </p>
<p> <i>M:System.Object..ctor</i> , <i>M:System.String..ctor(System.Char[])</i> , <i>M:System.String.Concat(System.Object)</i> , <i>M:System.Array.Sort&#8220;1(&#8220;0[])</i> , <i>M:System.Collections.Generic.List`1..ctor</i> , <i>M:System.Collections.Generic.List`1.Add(`0)</i> .</p>
<dt><i>N:</i></p>
<dd> Refers to a namespace, e.g. <i>N:System</i></p>
<dt><i>P:</i></p>
<dd> Refers to a property. If the property is an indexer or takes parameters, the parameter types are appended to the property name and enclosed with paranthesis: <i>P:System.String.Length</i> , <i>P:System.String.Chars(System.Int32)</i> .</p>
<dt><i>T:</i></p>
<dd> The String ID refers to a type, with the number of generic types appended: <i>T:System.String</i> , <i>T:System.Collections.Generic.List`1</i></dl>
<p> To make matters more interesting, generic types &amp; members have two representations: the &quot;unbound&quot; representation (shown in examples above), in which class names have the count of generic parameters appended to their name. There is also a &quot;bound&quot; representation, in which the binding of generic parameters is listed within &#8216;{&#8216; and &#8216;}&#8217;. </p>
<p> <code>Unbound:</code> <i>T:System.Collections.Generic.List`1</i> , <i>T:System.Collections.Generic.Dictionary`2</i> . </p>
<p> <code>Bound:</code> <i>T:System.Collections.Generic.List{System.Int32}</i> <i>T:System.Collections.Generic.Dictionary{System.String,System.Collections.Generic.List{System.Predicate{System.String}}}</i> . </p>
<p> As you can see, bound variants can be arbitrarily complex (just like generics). </p>
<p> Furthermore, if a generic parameter is bound to the generic parameter of a type or method, the &quot;index&quot; of the type/method&#8217;s generic parameter is used as the binding, so given </p>
<pre><code>
class FooType
{
  public
    static void Foo&lt;T&gt;(System.Predicate&lt;T&gt; predicate)
    {
    }
}
</code></pre>
<p> The String ID for this method is <i>M:FooType.Foo&#8220;1(System.Predicate{&#8220;0})</i> , as <i>&#8220;0</i> is the 0th generic parameter index which is bound to <i>System.Predicate&lt;T&gt;</i> .</p>
<h2>DOCUMENTATION FORMAT</h2>
<p> <i>monodocer</i> generates documentation similar to the Ecma documentation format, as described in ECMA-335 3rd Edition, Partition IV, Chapter 7. </p>
<p> The principal difference from the ECMA format is that each type gets its own file, within a directory identical to the namespace of the type. </p>
<p> Most of the information within the documentation should <i>not</i> be edited. This includes the type name ( <i>/Type/@FullName</i> ), implemented interfaces ( <i>/Type/Interfaces</i> ), member information ( <i>/Type/Members/Member/@MemberName</i> , <i>/Type/Members/Member/MemberSignature</i> , <i>/Type/Members/Member/MemberType</i> , <i>/Type/Members/Member/Parameters</i> , etc.). </p>
<p> What <i>should</i> be modified are all elements with the text <i>To be added.</i> , which are present under the <i>//Docs</i> elements (e.g. <i>/Type/Docs</i> , <i>/Type/Members/Member/Docs</i> ). The contents of the <i>Docs</i> element is <i>identical</i> in semantics and structure to the inline C# documentation format, consisting of these elements (listed in ECMA-334 3rd Edition, Annex E, Section 2). The following are used within the element descriptions:</p>
<dl>
<dt><i>CREF</i></p>
<dd> Refers to a class (or member) reference, and is a string in the format described above in the <i>STRING ID FORMAT</i> section.</p>
<dt><i>TEXT</i></p>
<dd> Non-XML text, and XML should not be nested. <i></p>
<dt>XML</i></p>
<dd> Only XML elements should be nested (which indirectly may contain text), but non-whitespace text should not be an immediate child node.</p>
<dt><i>XML_TEXT</i></p>
<dd> Free-form text and XML, so that other XML elements may be nested.</dl>
<p> The following elements are used in documentation:</p>
<dl>
<dt><i>&lt;block subset=SUBSET type=TYPE&gt;XML_TEXT&lt;/block&gt;</i></p>
<dd> Create a block of text, similar in concept to a paragraph, but is used to create divisions within the text. To some extent, a &lt;block/&gt; is equivalent to the HTML &lt;h2/&gt; tag. </p>
<p> <i>SUBSET</i> should always be the value <i>none</i> . </p>
<p> <i>TYPE</i> specifies the heading and formatting to use. Recognized types are: </p>
<p> <i>behaviors</i> Creates a section with the heading <i>Operation</i> . </p>
<p> <i>note</i> Creates a section with the heading <i>Note:</i> . </p>
<p> <i>overrides</i> Creates a section with the heading <i>Note to Inheritors</i> . </p>
<p> <i>usage</i> Creates a section with the heading <i>Usage</i> .</p>
<dt><i>&lt;c&gt;XML_TEXT&lt;/c&gt;</i></p>
<dd> Set text in a code-like font (similar to the HTML &lt;tt/&gt; element).</p>
<dt><i>&lt;code lang=LANGUAGE&gt;TEXT&lt;/code&gt;</i></p>
<dd> Display multiple lines of text in a code-like font (similar to the HTML &lt;pre/&gt; element). <i>LANGUAGE</i> is the language this code block is for. For example, if <i>LANGUAGE</i> is <code>C#</code> , then <i>TEXT</i> will get syntax highlighting for the C# language within the Mono Documentation Browser.</p>
<dt><i>&lt;example&gt;XML_TEXT&lt;/example&gt;</i></p>
<dd> Indicates an example that should be displayed specially. For example: </p>
<pre><code>
        &lt;example&gt;
          &lt;para&gt;An introductory paragraph.&lt;/para&gt;
          &lt;code lang="C#"&gt;
            class Example {
              public static void Main ()
              {
                System.Console.WriteLine ("Hello, World!");
              }
            }
          &lt;/code&gt;
        &lt;/example&gt;
</code></pre>
<dt><i>&lt;exception cref=CREF&gt;XML_TEXT&lt;/exception&gt;</i></p>
<dd> Identifies an exception that can be thrown by the documented member. </p>
<p> <i>&lt;exception/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> <i>CREF</i> is the exception type that is thrown, while <i>XML_TEXT</i> contains the circumstances that would cause <i>CREF</i> to be thrown. </p>
<pre>
        &lt;exception cref=&quot;T:System.ArgumentNullException&quot;&gt;
          &lt;paramref name=&quot;foo&quot; /&gt; was &lt;see langword=&quot;null&quot; /&gt;.
        &lt;/exception&gt;
</pre>
<dt><i>&lt;list&gt;XML&lt;/list&gt;</i></p>
<dd> Create a list or table of items. <i>&lt;list/&gt;</i> makes use of nested <i>&lt;item&gt;XML&lt;/item&gt;</i> , <i>&lt;listheader&gt;XML&lt;/listheader&gt;</i> , <i>&lt;term&gt;XML_TEXT&lt;/term&gt;</i> , and <i>&lt;description&gt;XML_TEXT&lt;/description&gt;</i> elements. </p>
<p> <i>Lists</i> have the syntax: </p>
<pre>
        &lt;list type=&quot;bullet&quot;&gt; &lt;!-- or type=&quot;number&quot; --&gt;
          &lt;item&gt;&lt;term&gt;Bullet 1&lt;/term&gt;&lt;/item&gt;
          &lt;item&gt;&lt;term&gt;Bullet 2&lt;/term&gt;&lt;/item&gt;
          &lt;item&gt;&lt;term&gt;Bullet 3&lt;/term&gt;&lt;/item&gt;
        &lt;/list&gt;
</pre>
<p> <i>Tables</i> have the syntax: </p>
<pre>
        &lt;list type=&quot;table&quot;&gt;
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
        &lt;/list&gt;
</pre>
<dt><i>&lt;para&gt;XML_TEXT&lt;/para&gt;</i></p>
<dd> Insert a paragraph of <i>XML_TEXT</i><br />
&nbsp;<wbr>. This is for use within other tags, such as <i>&lt;example/&gt;</i> , <i>&lt;remarks/&gt;</i> , <i>&lt;returns/&gt;</i> , <i>&lt;term/&gt;</i> and <i>&lt;description/&gt;</i> (see <i>&lt;list/&gt;</i> , above), and most other elements. </p>
<p> For example, </p>
<pre>
        &lt;para&gt;This is a paragraph of text.&lt;/para&gt;
</pre>
<dt><i>&lt;param name=NAME&gt;XML_TEXT&lt;/param&gt;</i></p>
<dd> <i>&lt;param/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Describes the parameter <i>NAME</i> of the current constructor, method, or property: </p>
<pre>
        &lt;param name=&quot;count&quot;&gt;
          A &lt;see cref=&quot;T:System.Int32&quot; /&gt; containing the number
          of widgets to process.
        &lt;/param&gt;
</pre>
<dt><i>&lt;paramref name=NAME /&gt;</i></p>
<dd> Indicates that <i>NAME</i> is a parameter. </p>
<p> This usually renders <i>NAME</i> as italic text, so it is frequently (ab)used as an equivalent to the HTML &lt;i/&gt; element. See the <i>&lt;exception/&gt;</i> documentation (above) for an example.</p>
<dt><i>&lt;permission cref=CREF&gt;XML_TEXT&lt;/permission&gt;</i></p>
<dd> Documentes the security accessibility requirements of the current member. </p>
<p> <i>&lt;permission/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> <i>CREF</i> is a type reference to the security permission required, while <i>XML_TEXT</i> is a description of why the permission is required. </p>
<pre>
        &lt;permission cref=&quot;T:System.Security.Permissions.FileIOPermission&quot;&gt;
          Requires permission for reading and writing files. See 
          &lt;see cref=&quot;F:System.Security.Permissions.FileIOPermissionAccess.Read&quot; /&gt;, 
          &lt;see cref=&quot;F:System.Security.Permissions.FileIOPermissionAccess.Write&quot; /&gt;.
        &lt;/permission&gt;
</pre>
<dt><i>&lt;remarks&gt;XML_TEXT&lt;/remarks&gt;</i></p>
<dd> Contains detailed information about a member. </p>
<p> <i>&lt;remarks/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<pre>
        &lt;remarks&gt;Insert detailed information here.&lt;/remarks&gt;
</pre>
<dt><i>&lt;returns&gt;XML_TEXT&lt;/returns&gt;</i></p>
<dd>
<p> <i>&lt;remarks/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Describes the return value of a method: </p>
<pre>
        &lt;returns&gt;
          A &lt;see cref=&quot;T:System.Boolean&quot; /&gt; specifying whether 
          or not the process can access 
          &lt;see cref=&quot;P:Mono.Unix.UnixFileSystemInfo.FullName&quot; /&gt;.
        &lt;/returns&gt;
</pre>
<dt><i>&lt;see cref=CREF /&gt;</i></p>
<dd> Creates a link to the specified member within the current text: </p>
<pre>
        &lt;see cref=&quot;M:Some.Namespace.With.Type.Method&quot; /&gt;
</pre>
<dt><i>&lt;seealso cref=CREF /&gt;</i></p>
<dd>
<p> <i>&lt;seealso/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Allows an entry to be generated for the <i>See Also</i> subclause. Use <i>&lt;see/&gt;</i> to specify a link from within text. </p>
<pre>
        &lt;seealso cref=&quot;P:System.Exception.Message&quot; /&gt;
</pre>
<dt><i>&lt;since version=VERSION /&gt;</i></p>
<dd>
<p> <i>&lt;since/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Permits specification of which version introduced the specified type or member. </p>
<pre>
        &lt;since version=&quot;Gtk# 2.4&quot; /&gt;
</pre>
<dt><i>&lt;summary&gt;DESCRIPTION&lt;/summary&gt;</i></p>
<dd>
<p> <i>&lt;summary/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Provides a (brief!) overview about a type or type member. </p>
<p> This is usually displayed as part of a class declaration, and should be a reasonably short description of the type/member. Use <i>&lt;remarks/&gt;</i> for more detailed information.</p>
<dt><i>&lt;typeparam name=NAME&gt;DESCRPITION&lt;/typeparam&gt;</i></p>
<dd> <i>&lt;typeparam/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> This is used to describe type parameter for a generic type or generic method. </p>
<p> <i>NAME</i> is the name of the type parameter, while <i>DESCRIPTION</i> contains a description of the parameter (what it&#8217;s used for, what restrictions it must meet, etc.). </p>
<pre>
        &lt;typeparam name=&quot;T&quot;&gt;The type of the underlying collection&lt;/typeparam&gt;
</pre>
<dt><i>&lt;typeparamref&gt;</i></p>
<dd> Used to indicate that a word is a type parameter, for use within other text blocks (e.g. within <i>&lt;para/&gt;</i> ). </p>
<pre>
        &lt;para&gt;If &lt;typeparamref name=&quot;T&quot; /&gt; is a struct, then...&lt;/para&gt;
</pre>
<dt><i>&lt;value&gt;DESCRIPTION&lt;/value&gt;</i></p>
<dd> <i>&lt;value/&gt;</i> is a top-level element, and should be nested directly under the <i>&lt;Docs/&gt;</i> element. </p>
<p> Allows a property to be described. </p>
<pre>
        &lt;value&gt;
          A &lt;see cref=&quot;T:System.String&quot; /&gt; containing a widget name.
        &lt;/value&gt;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mdassembler/">mdassembler</a>(1), <a href="/docs/linux/man/1-mdcs2ecma/">mdcs2ecma</a>(1), <a href="/docs/linux/man/1-mdnormalizer/">mdnormalizer</a>(1), <a href="/docs/linux/man/1-mdvalidator/">mdvalidator</a>(1), <a href="/docs/linux/man/1-monodocs2html/">monodocs2html</a>(1)</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
