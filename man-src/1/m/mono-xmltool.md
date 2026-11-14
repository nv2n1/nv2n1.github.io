---
title: "mono-xmltool(1)"
name: "mono-xmltool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mono-xmltool/"
description: "mono-xmltool – Mono XML validation and transformation tool."
---

<h2>NAME</h2>
<p> mono-xmltool &#8211; Mono XML validation and transformation tool.</p>
<h2>SYNOPSIS</h2>
<p> <code>mono-xmltool &#8211;validate [*.rng | *.rnc | *.nvdl | *.xsd] [instances]</code> </p>
<p> <code>mono-xmltool &#8211;validate-rng relax-ng-grammar-xml [instances]</code> </p>
<p> <code>mono-xmltool &#8211;validate-rnc relax-ng-compact-grammar-file [instances]</code> </p>
<p> <code>mono-xmltool &#8211;validate-nvdl nvdl-script-xml [instances]</code> </p>
<p> <code>mono-xmltool &#8211;validate-xsd xml-schema [instances]</code> </p>
<p> <code>mono-xmltool &#8211;transform stylesheet instance-xml</code> </p>
<p> <code>mono-xmltool &#8211;prettyprint [source [result]]</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>mono-xmltool</i> is a command line front end for various functions available in the Mono XML class libraries. It currently it offers validation with various different kinds of schemas, xslt transformations and pretty printing. </p>
<h2>XML VALIDATION</h2>
<p> mono-xmltool can validate a given set of XML files (the instances parameter) using the given schema file. Currently supported schema files include Relax NG (*.rng), Compact Relax NG (*.rnc), Namespace-based Validation Dispatching Language (*.nvdl) and XML Schema (*.xsd). </p>
<p> If invoked with the &#8211;validate argument, Mono will use the filename extension to guess the kind of validation required. The &#8211;validate-xxx flags would force a specific kind of validation. </p>
<p> The following lists the flags and the actual class that implements them in Mono:</p>
<dl>
<dt><i>&#8211;validate-rng </i></p>
<dd>
<p> Commons.Xml.Relaxng.RelaxNgPattern as the schema, and Commons.Xml.Relaxng.RelaxngValidatingReader validator.</p>
<dt><i>&#8211;validate-rnc</i></p>
<dd> Commons.Xml.Relaxng.RncParser as the schema, and Commons.Xml.Relaxng.RelaxngValidatingReader validator.</p>
<dt><i>&#8211;validate-nvdl </i></p>
<dd>
<p> Commons.Xml.Nvdl as the schema and Commons.Xml.NvdlValidatingReader validator.</p>
<dt><i>&#8211;validate-xsd</i></p>
<dd> System.Xml.Schema.XmlSchema as the schema and uses System.Xml.XmlValidatingReader as the validator.</dl>
<h2>TRANSFORMATIONS</h2>
<p> This does an XSLT transformation. The stylesheet must be an XSLT file, the instance-xml is the document to be processed. Output it sent to the standard output.</p>
<h2>PRETTY PRINTING</h2>
<p> Produces a pretty-print rendering of the <i>source</i> file. If it is not specified it reads the standard input. If <i>result </i> is not specified, the output is sent to the standard output.</p>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at the <a rel="nofollow" href="http://www.mono-project.com/community/help/mailing-lists/">http://www.mono-project.com/community/help/mailing-lists/</a></p>
<h2>WEB SITE</h2>
<p> <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1),</code><a href="/docs/linux/man/1-mcs/">mcs</a>(1). </p>
<h2>Index</h2>
