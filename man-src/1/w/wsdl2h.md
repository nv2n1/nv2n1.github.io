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
<dt><code>-a</code></dt>
<dd> Generate indexed struct names for local elements with anonymous types.</dd>
<dt><code>-b</code></dt>
<dd> Bi-directional operations (duplex ops) added to serve one-way responses.</dd>
<dt><code>-c</code></dt>
<dd> Generate C source code.</dd>
<dt><code>-d</code></dt>
<dd> Use DOM to populate <code>xs</code>:<i>any</i>, <code>xs</code>:<i>anyType</i> and <code>xs</code>:<i>anyAttribute</i>.</dd>
<dt><code>-e</code></dt>
<dd> Do not qualify enum names.</dd>
<dt><code>-f</code></dt>
<dd> Generate flat C++ class hierarchy.</dd>
<dt><code>-g</code></dt>
<dd> Generate global top-level element declarations.</dd>
<dt><code>-h</code></dt>
<dd> Display help info.</dd>
<dt><code>-I</code><i>path</i></dt>
<dd> Use <i>path</i> to find files.</dd>
<dt><code>-i</code></dt>
<dd> Do not import (advanced option).</dd>
<dt><code>-j</code></dt>
<dd> Do not generate <code>SOAP_ENV__Header</code> and <code>SOAP_ENV__Detail</code> definitions.</dd>
<dt><code>-k</code></dt>
<dd> Do not generate <code>SOAP_ENV__Header</code> mustUnderstand qualifiers.</dd>
<dt><code>-l</code></dt>
<dd> Display license information.</dd>
<dt><code>-m</code></dt>
<dd> Use <code>xsd.h</code> module to import primitive types.</dd>
<dt><code>-N</code><i>name</i></dt>
<dd> Use <i>name</i> for service prefixes to produce a service for each binding.</dd>
<dt><code>-n</code><i>name</i></dt>
<dd> Use <i>name</i> as the base namespace prefix instead of <code>ns</code>.</dd>
<dt><code>-o</code><i>file</i></dt>
<dd> Output to file <i>file</i>.</dd>
<dt><code>-P</code></dt>
<dd> Do not create polymorphic types inherited from <code>xsd__anyType</code>.</dd>
<dt><code>-p</code></dt>
<dd> Create polymorphic types inherited from base <code>xsd__anyType</code>.</dd>
<dt><code>-q</code><i>name</i></dt>
<dd> Use <i>name</i> for the C++ namespace of all declarations.</dd>
<dt><code>-R</code></dt>
<dd> Generate REST operations for REST bindings in the WSDL.</dd>
<dt><code>-r</code><i>host</i>[:<i>port</i>[:<i>uid</i>:<i>pwd</i>]]</dt>
<dd> Connect via proxy <i>host</i>, <i>port</i> and proxy credentials.</dd>
<dt><code>-s</code></dt>
<dd> Do not generate STL code (no <code>std::string</code> and no <code>std::vector</code>).</dd>
<dt><code>-t</code><i>file</i></dt>
<dd> Use type map file <i>file</i> instead of the default file <code>typemap.dat</code>.</dd>
<dt><code>-u</code></dt>
<dd> Do not generate unions.</dd>
<dt><code>-v</code></dt>
<dd> Verbose output.</dd>
<dt><code>-W</code></dt>
<dd> Suppress warnings.</dd>
<dt><code>-w</code></dt>
<dd> Always wrap response parameters in a response struct (&lt;=1.1.4 behaviour).</dd>
<dt><code>-x</code></dt>
<dd> Do not generate <code>_XML</code> <i>any</i>/<i>anyAttribute</i> extensibility elements.</dd>
<dt><code>-y</code></dt>
<dd> Generate typedef synonyms for structs and enums.</dd>
<dt><code>-z1</code></dt>
<dd> Compatibility with 2.7.6e: Generate pointer-based arrays.</dd>
<dt><code>-z2</code></dt>
<dd> Compatibility with 2.7.7 to 2.7.15: Qualify element/attribute references.</dd>
<dt><code>-z3</code></dt>
<dd> Compatibility with 2.7.16 to 2.8.7: Qualify element/attribute references.</dd>
<dt><code>-z4</code></dt>
<dd> Compatibility up to 2.8.11: Do not generate union structs in <code>std::vector</code>.</dd>
<dt><code>-z5</code></dt>
<dd> Compatibility up to 2.8.15.</dd>
<dt><code>-_</code></dt>
<dd> Do not generate _USCORE (replace with UNICODE _x005f).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-soapcpp2/">soapcpp2</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Wana &lt;greuff [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
