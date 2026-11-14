---
title: "genxs(1)"
name: "genxs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genxs/"
description: "genxs – Mono’s Xml Serializer Generator"
---

<h2>NAME</h2>
<p> genxs &#8211; Mono&#8217;s Xml Serializer Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>genxs</code> configurationFile [destinationFolder]</p>
<h2>DESCRIPTION</h2>
<p> <i>genxs</i> is a tool for generating custom XML serialization writers and readers for classes. </p>
<p> <i>configurationFile</i> is configuration file which specifies several information, such as the class for which to generate the reader and writer, the name and namespace of the classes to generate, and a collection of hooks to apply. By using hooks it is possible to customize the behavior of the serializer without needing to modify the generated file, so you can safely regenerate it if the source class is modified. </p>
<p> <i>destinationFolder</i> specifies the folder where the files will be generated. </p>
<p> <code>NOTE: </code> This tool only runs in the Mono runtime, since it uses some internal classes not available in other runtimes.</p>
<h2>CONFIGURATION FILE FORMAT</h2>
<p> The configuration file is an xml document based on the following grammar (&quot;?&quot; means optional, &quot;*&quot; 0 or more): </p>
<pre>
        &lt;configuration&gt;
                &lt;serializer class=&quot;name&quot; assembly=&quot;name&quot;&gt; *
                        &lt;reader&gt;name&lt;/reader&gt; ?
                        &lt;writer&gt;name&lt;/writer&gt; ?
                        &lt;namespace&gt;name&lt;/namespace&gt; ?
                        &lt;outFileName&gt;name&lt;/outFileName&gt; ?
                        &lt;readerHooks&gt; ?
                                &lt;hook ...&gt; *
                        &lt;/readerHooks&gt;
                        &lt;writerHooks&gt; ?
                                &lt;hook ...&gt; *
                        &lt;/writerHooks&gt;
                &lt;/serializer&gt;
        &lt;/configuration&gt;
</pre>
<p> A configuration file can have multiple &quot;serializer&quot; elements, each of which specifies the class for which to generate a serializer together with several generation options. The source class is specified in the following attributes: </p>
<dl>
<dt> *</p>
<dd> <i>class</i> : name of the class (including namespace).</p>
<dt> *</p>
<dd> <i>assembly</i> : assembly name. It can include the complete path.</dl>
<p> Generation options are specified in child elements: </p>
<dl>
<dt> *</p>
<dd> <i>reader</i> : name of the reader class.</p>
<dt> *</p>
<dd> <i>noReader</i> : if &quot;true&quot;, it does not generate reader class.</p>
<dt> *</p>
<dd> <i>writer</i> : name of the writer class.</p>
<dt> *</p>
<dd> <i>baseSerializer</i> : name of the base xml serializer class. This item is 2.0 only.</p>
<dt> *</p>
<dd> <i>implementation</i> : name of the serializer implementation class. This item is 2.0 only.</p>
<dt> *</p>
<dd> <i>noWriter</i> : if &quot;true&quot;, it does not generate writer class.</p>
<dt> *</p>
<dd> <i>namespace</i> : namespace of the reader and writer classes.</p>
<dt> *</p>
<dd> <i>generateAsInternal</i> : if &quot;true&quot;, it generates classes as internal.</p>
<dt> *</p>
<dd> <i>outFileName</i> : name of the generated file.</p>
<dt> *</p>
<dd> <i>readerHooks</i> : a list of hooks to apply to the reader.</p>
<dt> *</p>
<dd> <i>writerHooks</i> : a list of hooks to apply to the writer.</dl>
<h2>SPECIFYING HOOKS</h2>
<p> Using hooks you can customize the behavior of readers and writers. A hook specification follows this grammar: </p>
<pre>
        &lt;hook type=&quot;name&quot;&gt;
                &lt;select&gt; ?
                        &lt;typeName&gt;name&lt;/typeName&gt; ?
                        &lt;typeAttribute&gt;name&lt;/typeAttribute&gt; *
                        &lt;typeMember&gt;name&lt;/typeMember&gt; ?
                &lt;/select&gt;
                &lt;replace&gt;source code&lt;/replace&gt; ?
                &lt;insertBefore&gt;source code&lt;/insertBefore&gt; ?
                &lt;insertAfter&gt;source code&lt;/insertAfter&gt; ?
        &lt;/hook&gt;
</pre>
<p> The &quot;type&quot; attribute specifies the context in which the hook is applied. It can be one of the following: </p>
<dl>
<dt> *</p>
<dd> <i>attributes</i> : hook is applied where attributes are serialized/deserialized.</p>
<dt> *</p>
<dd> <i>elements</i> : hook is applied where elements are serialized/deserialized.</p>
<dt> *</p>
<dd> <i>unknownAttribute</i> : hook is applied where unknown attributes are processed.</p>
<dt> *</p>
<dd> <i>unknownElement</i> : hook is applied where unknown elements are processed.</p>
<dt> *</p>
<dd> <i>member</i> : hook is applied where a member is serialized/deserialized.</p>
<dt> *</p>
<dd> <i>type</i> : hook is applied for the whole type.</dl>
<p> The &quot;select&quot; element specifies the classes and members to which the hook has to be added. It can contain the following elements: </p>
<dl>
<dt> *</p>
<dd> <i>typeName</i> : the class with that name will be selected (must include namespace)</p>
<dt> *</p>
<dd> <i>typeAttribute</i> : all classes which have that attribute applied will be selected (specify the full attribute class name, including namespace). Several attribute names can be specified.</p>
<dt> *</p>
<dd> <i>typeMember</i> : name of the class member for which the hook must be added.</dl>
<p> The hook source code can be specified using any of the following elements: </p>
<dl>
<dt> *</p>
<dd> <i>replace</i> : the provided source code will replace all serialization/deserialization operations in the hook context.</p>
<dt> *</p>
<dd> <i>insertBefore</i> : the source code will be added before the hook context.</p>
<dt> *</p>
<dd> <i>insertAfter</i> : the source code will be added after the hook context.</dl>
<p> When writing the code for a hook you can use some special variables that are defined during the code generation process. The variables are the following: </p>
<dl>
<dt> *</p>
<dd> <i>$TYPE:</i> name of the class being generated, without namespace.</p>
<dt> *</p>
<dd> <i>$FULLTYPE:</i> full name of the class being generated, including namespace.</p>
<dt> *</p>
<dd> <i>$OBJECT:</i> the object being serialized or deserialized. When using a replace reader hook of type &quot;type&quot;, the hook code must assign the deserialized object to this variable.</p>
<dt> *</p>
<dd> -I $ELEMENT: name of the element of the object being serialized/deserialized.</p>
<dt> *</p>
<dd> <i>$NAMESPACE:</i> namespace of the element of the object being serialized/deserialized.</p>
<dt> *</p>
<dd> <i>$MEMBER:</i> name of the member being serialized/deserialized. Only valid in the &quot;member&quot; context.</dl>
<h2>HOOK EXAMPLES</h2>
<p> The following example adds a call to a Validate method after the deserialization of any object: </p>
<pre>
&lt;hook type=&quot;type&quot;&gt;
        &lt;insertAfter&gt;
                System.Xml.Schema.XmlSchema.Validate$TYPE ($OBJECT);
        &lt;/insertAfter&gt;
&lt;/hook&gt;
</pre>
<p> This example specifies the code to be used to deserialize the XmlSchema class: </p>
<pre>
&lt;hook type=&quot;type&quot;&gt;
        &lt;select&gt;
                &lt;typeName&gt;System.Xml.Schema.XmlSchema&lt;/typeName&gt;
        &lt;/select&gt;
        &lt;replace&gt;
                $OBJECT = System.Xml.Schema.XmlSchema.Read (Reader, null);
        &lt;/replace&gt;
&lt;/hook&gt;
</pre>
<p> That one specifies the code to be used to read XmlSchema instances: </p>
<pre>
&lt;hook type=&quot;type&quot;&gt;
        &lt;select&gt;
                &lt;typeName&gt;System.Xml.Schema.XmlSchema&lt;/typeName&gt;
        &lt;/select&gt;
        &lt;replace&gt;$OBJECT.Write (Writer);&lt;/replace&gt;
&lt;/hook&gt;
</pre>
<p> With this two hooks the serializer will print some information when serializing the class &quot;MyClass&quot;: </p>
<pre><code>
&lt;hook type="type"&gt;
        &lt;select&gt;
                &lt;typeName&gt;MyNamespace.MyClass&lt;/typeName&gt;
        &lt;/select&gt;
        &lt;insertBefore&gt;Console.WriteLine ("Serializing MyClass");&lt;/replace&gt;
        &lt;insertAfter&gt;Console.WriteLine ("MyClass serialized");&lt;/insertAfter&gt;
&lt;/hook&gt;
&lt;hook type="member"&gt;
        &lt;select&gt;
                &lt;typeName&gt;MyNamespace.MyClass&lt;/typeName&gt;
        &lt;/select&gt;
        &lt;insertAfter&gt;
                Console.WriteLine ("Serialized member $MEMBER");
        &lt;/insertAfter&gt;
&lt;/hook&gt;
</code></pre>
<p> This hook writes an additional element for all types that have the custom attribute &quot;MyAttribute&quot;: </p>
<p>&lt;hook type=&#8221;elements&#8221;&gt;<br />
        &lt;select&gt;<br />
                &lt;typeAttribute&gt;MyNamespace.MyAttribute&lt;/typeAttribute&gt;<br />
        &lt;/select&gt;<br />
        &lt;insertAfter&gt;<br />
                Writer.WriteStartElement (&#8220;privateData&#8221;);<br />
                Writer.WriteString ($OBJECT.PrivateData);<br />
                Writer.WriteEndElement ();<br />
        &lt;/insertAfter&gt;<br />
&lt;/hook&gt;</p>
<h2>CONFIGURATION FILE EXAMPLE</h2>
<p> This is the configuration file used to generate the serializer for ServiceDescription: </p>
<pre><code>
&lt;configuration&gt;
        &lt;serializer class="System.Web.Services.Description.ServiceDescription" assembly="System.Web.Services"&gt;
                &lt;reader&gt;ServiceDescriptionReaderBase&lt;/reader&gt;
                &lt;writer&gt;ServiceDescriptionWriterBase&lt;/writer&gt;
                &lt;namespace&gt;System.Web.Services.Description&lt;/namespace&gt;
                &lt;outFileName&gt;ServiceDescriptionSerializerBase.cs&lt;/outFileName&gt;
                &lt;readerHooks&gt;
                        &lt;hook type="unknownElement"&gt;
                                &lt;select&gt;
                                        &lt;typeAttribute&gt;System.Web.Services.Configuration.XmlFormatExtensionPointAttribute&lt;/typeAttribute&gt;
                                &lt;/select&gt;
                                &lt;replace&gt;ServiceDescription.ReadExtension (Reader, $OBJECT);&lt;/replace&gt;
                        &lt;/hook&gt;
                        &lt;hook type="type"&gt;
                                &lt;select&gt;
                                        &lt;typeName&gt;System.Xml.Schema.XmlSchema&lt;/typeName&gt;
                                &lt;/select&gt;
                                &lt;replace&gt;$OBJECT = System.Xml.Schema.XmlSchema.Read (Reader, null);&lt;/replace&gt;
                        &lt;/hook&gt;
                &lt;/readerHooks&gt;
                &lt;writerHooks&gt;
                        &lt;hook type="elements"&gt;
                                &lt;select&gt;
                                        &lt;typeAttribute&gt;System.Web.Services.Configuration.XmlFormatExtensionPointAttribute&lt;/typeAttribute&gt;
                                &lt;/select&gt;
                                &lt;insertBefore&gt;ServiceDescription.WriteExtensions (Writer, $OBJECT);&lt;/insertBefore&gt;
                        &lt;/hook&gt;
                        &lt;hook type="type"&gt;
                                &lt;select&gt;
                                        &lt;typeName&gt;System.Xml.Schema.XmlSchema&lt;/typeName&gt;
                                &lt;/select&gt;
                                &lt;replace&gt;$OBJECT.Write (Writer);&lt;/replace&gt;
                        &lt;/hook&gt;
                &lt;/writerHooks&gt;
        &lt;/serializer&gt;
&lt;/configuration&gt;
</code></pre>
<h2>AUTHORS</h2>
<p> Lluis Sanchez Gual (lluis [at] ximian.com) </p>
<h2>LICENSE</h2>
<p> GenXS is released under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1), <a href="/docs/linux/man/1-sgen/">sgen</a>(1) </p>
<h2>Index</h2>
