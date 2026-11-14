---
title: "xsd(1)"
name: "xsd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsd/"
description: "xsd – Mono’s utility for generating schema or class files"
---

<h2>NAME</h2>
<p> xsd &#8211; Mono&#8217;s utility for generating schema or class files</p>
<h2>SYNOPSIS</h2>
<p> <code>xsd</code> &lt;schema.xsd&gt; /classes [options] </p>
<p> <code>xsd</code> &lt;schema.xsd&gt; /dataset [options] </p>
<p> <code>xsd</code> &lt;assembly&gt;.dll|&lt;assembly&gt;.exe [options] </p>
<p> <code>xsd</code> &lt;instance.xml&gt; [&lt;instance.xml&gt; &#8230;] [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>xsd</i> is a tool for intended to complement the XML serialization support of Mono. It can do the following tasks:</p>
<dl>
<dt>Generate serializable classes</p>
<dd> From a given XML schema, generate a class that can be used to read and write xml documents that conform that schema (/classes option).</p>
<dt>Generate typed datasets</p>
<dd> From a given XML schema, generate a typed DataSet class that can be used to read and write xml documents that conform that schema (/dataset option).</p>
<dt>Generate XML schemas</p>
<dd> From a given assembly and an optional type name, generate an XML schema that can be used to validate the xml documents that can be obtained by serializing objects of that type. If no type is provided, xsd generates a schema for all types in the assembly. When specifying the assembly name do not include the file extension (.dll or .exe). xsd will look for the assembly using the standard assembly loading rules.</p>
<dt>Infer XML schemas</p>
<dd> From a given set of XML documents, infer the XML schema that can be used to validate those documents. </p>
</dl>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><i>/element:name /e:name</i></p>
<dd> Specifies the name of the XML schema element for which a class or a dataset has to be generated.</p>
<dt>
<dt><i>/namespace:name /n:name</i></p>
<dd>
<dd> Specifies the namespace of the XML schema element for which a class or a dataset has to be generated.</p>
<dt><i>/language:name /l:name</i></p>
<dd> Specifies the programming language to use for the generated code. The only supported languages are CS (C#) and VB (Visual Basic.NET).</p>
<dt><i>/generator:type,assembly /g:type,assembly</i></p>
<dd> Indicates xsd.exe to use custom CodeDomProvider to generate code. The type name must be full name. Assembly name is a local file name that is going to be loaded. The specified Type must have the default constructor.</p>
<dt><i>/outputdir:path /o:path</i></p>
<dd> Specifies the directory where to generate the code or schemas.</p>
<dt><i>/type:name /t:name</i></p>
<dd> Specifies the full name of the type (including namespace) for which to generate the XML schema.</p>
<dt><i>/help /h</i></p>
<dd> Show usage help.</dl>
<h2>AUTHORS</h2>
<p> Lluis Sanchez Gual (lluis [at] ximian.com)<br />
 Atsushi Enomoto (atsushi [at] ximian.com) </p>
<h2>LICENSE</h2>
<p> xsd is released under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-disco/">disco</a>(1), <a href="/docs/linux/man/1-soapsuds/">soapsuds</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1), <a href="/docs/linux/man/1-wsdl/">wsdl</a>(1) </p>
<h2>Index</h2>
