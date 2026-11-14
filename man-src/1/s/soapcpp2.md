---
title: "soapcpp2(1)"
name: "soapcpp2"
section: "1"
letter: "s"
url: "/docs/linux/man/1-soapcpp2/"
description: "soapcpp2 – the gSOAP Stub and Skeleton Compiler for C and C++"
---

<h2 class="name">NAME</h2>
<p> soapcpp2 &#8211; the gSOAP Stub and Skeleton Compiler for C and C++ </p>
<h2>SYNOPSIS</h2>
<p> <code>soapcpp2</code> [<i>OPTIONS</i>] <i>INPUT</i></p>
<h2>DESCRIPTION</h2>
<p> Please see /usr/share/doc/gsoap/soapdoc2.html for details. </p>
<p> Create stubs and client and server code from input <i>INPUT</i> or standard input if <i>INPUT</i> is not specified.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> Generate SOAP 1.1 bindings.</p>
<dt><code>-2</code></p>
<dd> Generate SOAP 1.2 bindings.</p>
<dt><code>-0</code></p>
<dd> Remove SOAP bindings, use REST.</p>
<dt><code>-C</code></p>
<dd> Generate client-side code only.</p>
<dt><code>-S</code></p>
<dd> Generate server-side code only.</p>
<dt><code>-T</code></p>
<dd> Generate server-side auto-test code.</p>
<dt><code>-L</code></p>
<dd> Do not generate <code>soapClientLib</code>/<code>soapServerLib</code>.</p>
<dt><code>-a</code></p>
<dd> Use <code>SOAPAction</code> with WS-Addressing to invoke server-side operations.</p>
<dt><code>-A</code></p>
<dd> Require <code>SOAPAction</code> to invoke server-side operations.</p>
<dt><code>-b</code></p>
<dd> Serialize byte arrays char[N] as string.</p>
<dt><code>-c</code></p>
<dd> Generate C source code.</p>
<dt><code>-d</code><i>path</i></p>
<dd> Use <i>path</i> to save files.</p>
<dt><code>-e</code></p>
<dd> Generate SOAP RPC encoding style bindings.</p>
<dt><code>-f</code><i>N</i></p>
<dd> File split of <i>N</i> XML serializer implementations per file (N&gt;=10).</p>
<dt><code>-h</code></p>
<dd> Display help info.</p>
<dt><code>-I</code><i>path</i></p>
<dd> use <i>path</i>(s) for <code>#import</code> (paths separated with &#8216;:&#8217;).</p>
<dt><code>-i</code></p>
<dd> Generate C++ service proxies and objects inherited from <code>soap</code> struct.</p>
<dt><code>-j</code></p>
<dd> Generate C++ service proxies and objects that share a <code>soap</code> struct.</p>
<dt><code>-k</code></p>
<dd> Generate data structure walkers (experimental).</p>
<dt><code>-l</code></p>
<dd> Generate linkable modules (experimental).</p>
<dt><code>-m</code></p>
<dd> Generate Matlab(tm) code for MEX compiler.</p>
<dt><code>-n</code></p>
<dd> Use service name to rename service functions and namespace table.</p>
<dt><code>-p</code><i>name</i></p>
<dd> Save files with new prefix <i>name</i> instead of <code>soap</code>.</p>
<dt><code>-Q</code><i>name</i></p>
<dd> Use <i>name</i> as the C++ namespace for decls, including custom serializers.</p>
<dt><code>-q</code><i>name</i></p>
<dd> Use <i>name</i> as the C++ namespace for decls, excluding custom serializers.</p>
<dt><code>-s</code></p>
<dd> Generate deserialization code with strict XML validation checks.</p>
<dt><code>-t</code></p>
<dd> Generate code for fully <code>xsi:type</code> typed SOAP/XML messaging.</p>
<dt><code>-u</code></p>
<dd> Uncomment comments in WSDL/schema output by suppressing XML comments.</p>
<dt><code>-v</code></p>
<dd> Display version info.</p>
<dt><code>-w</code></p>
<dd> Do not generate WSDL and schema files.</p>
<dt><code>-x</code></p>
<dd> Do not generate sample XML message files.</p>
<dt><code>-y</code></p>
<dd> Include C/C++ type access information in sample XML messages.</p>
<dt><code>-z1</code></p>
<dd> Generate deprecated old-style C++ service proxies and objects.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wsdl2h/">wsdl2h</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Wana &lt;greuff [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
