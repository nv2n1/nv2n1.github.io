---
title: "wsdl2h(1)"
name: "wsdl2h"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsdl2h/"
description: "wsdl2h – the gSOAP WSDL parser for C and C++"
---

<h2 class="name">NAME</h2>
<p> wsdl2h &#8211; the gSOAP WSDL parser for C and C++ </p>
<h2>SYNOPSIS</h2>
<p> <code>wsdl2h</code> [<i>OPTIONS</i>] <i>SOURCE</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Please see /usr/share/doc/gsoap/soapdoc2.html for details. </p>
<p> Converts a <code>WSDL</code> or <code>XSD</code> input file, or from an HTTP address, <i>SOURCE</i> to a declaration file that can be parsed by <code><a href="/docs/linux/man/1-soapcpp2/">soapcpp2</a></code>(1). If no <i>SOURCE</i> argument is specified, read from standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Generate indexed struct names for local elements with anonymous types.</p>
<dt><code>-b</code></p>
<dd> Bi-directional operations (duplex ops) added to serve one-way responses.</p>
<dt><code>-c</code></p>
<dd> Generate C source code.</p>
<dt><code>-d</code></p>
<dd> Use DOM to populate <code>xs</code>:<i>any</i>, <code>xs</code>:<i>anyType</i> and <code>xs</code>:<i>anyAttribute</i>.</p>
<dt><code>-e</code></p>
<dd> Do not qualify enum names.</p>
<dt><code>-f</code></p>
<dd> Generate flat C++ class hierarchy.</p>
<dt><code>-g</code></p>
<dd> Generate global top-level element declarations.</p>
<dt><code>-h</code></p>
<dd> Display help info.</p>
<dt><code>-I</code><i>path</i></p>
<dd> Use <i>path</i> to find files.</p>
<dt><code>-i</code></p>
<dd> Do not import (advanced option).</p>
<dt><code>-j</code></p>
<dd> Do not generate <code>SOAP_ENV__Header</code> and <code>SOAP_ENV__Detail</code> definitions.</p>
<dt><code>-k</code></p>
<dd> Do not generate <code>SOAP_ENV__Header</code> mustUnderstand qualifiers.</p>
<dt><code>-l</code></p>
<dd> Display license information.</p>
<dt><code>-m</code></p>
<dd> Use <code>xsd.h</code> module to import primitive types.</p>
<dt><code>-N</code><i>name</i></p>
<dd> Use <i>name</i> for service prefixes to produce a service for each binding.</p>
<dt><code>-n</code><i>name</i></p>
<dd> Use <i>name</i> as the base namespace prefix instead of <code>ns</code>.</p>
<dt><code>-o</code><i>file</i></p>
<dd> Output to file <i>file</i>.</p>
<dt><code>-P</code></p>
<dd> Do not create polymorphic types inherited from <code>xsd__anyType</code>.</p>
<dt><code>-p</code></p>
<dd> Create polymorphic types inherited from base <code>xsd__anyType</code>.</p>
<dt><code>-q</code><i>name</i></p>
<dd> Use <i>name</i> for the C++ namespace of all declarations.</p>
<dt><code>-R</code></p>
<dd> Generate REST operations for REST bindings in the WSDL.</p>
<dt><code>-r</code><i>host</i>[:<i>port</i>[:<i>uid</i>:<i>pwd</i>]]</p>
<dd> Connect via proxy <i>host</i>, <i>port</i> and proxy credentials.</p>
<dt><code>-s</code></p>
<dd> Do not generate STL code (no <code>std::string</code> and no <code>std::vector</code>).</p>
<dt><code>-t</code><i>file</i></p>
<dd> Use type map file <i>file</i> instead of the default file <code>typemap.dat</code>.</p>
<dt><code>-u</code></p>
<dd> Do not generate unions.</p>
<dt><code>-v</code></p>
<dd> Verbose output.</p>
<dt><code>-W</code></p>
<dd> Suppress warnings.</p>
<dt><code>-w</code></p>
<dd> Always wrap response parameters in a response struct (&lt;=1.1.4 behaviour).</p>
<dt><code>-x</code></p>
<dd> Do not generate <code>_XML</code> <i>any</i>/<i>anyAttribute</i> extensibility elements.</p>
<dt><code>-y</code></p>
<dd> Generate typedef synonyms for structs and enums.</p>
<dt><code>-z1</code></p>
<dd> Compatibility with 2.7.6e: Generate pointer-based arrays.</p>
<dt><code>-z2</code></p>
<dd> Compatibility with 2.7.7 to 2.7.15: Qualify element/attribute references.</p>
<dt><code>-z3</code></p>
<dd> Compatibility with 2.7.16 to 2.8.7: Qualify element/attribute references.</p>
<dt><code>-z4</code></p>
<dd> Compatibility up to 2.8.11: Do not generate union structs in <code>std::vector</code>.</p>
<dt><code>-z5</code></p>
<dd> Compatibility up to 2.8.15.</p>
<dt><code>-_</code></p>
<dd> Do not generate _USCORE (replace with UNICODE _x005f).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-soapcpp2/">soapcpp2</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Wana &lt;greuff [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
