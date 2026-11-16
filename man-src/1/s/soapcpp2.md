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
<dt><code>-1</code></dt>
<dd> Generate SOAP 1.1 bindings.</dd>
<dt><code>-2</code></dt>
<dd> Generate SOAP 1.2 bindings.</dd>
<dt><code>-0</code></dt>
<dd> Remove SOAP bindings, use REST.</dd>
<dt><code>-C</code></dt>
<dd> Generate client-side code only.</dd>
<dt><code>-S</code></dt>
<dd> Generate server-side code only.</dd>
<dt><code>-T</code></dt>
<dd> Generate server-side auto-test code.</dd>
<dt><code>-L</code></dt>
<dd> Do not generate <code>soapClientLib</code>/<code>soapServerLib</code>.</dd>
<dt><code>-a</code></dt>
<dd> Use <code>SOAPAction</code> with WS-Addressing to invoke server-side operations.</dd>
<dt><code>-A</code></dt>
<dd> Require <code>SOAPAction</code> to invoke server-side operations.</dd>
<dt><code>-b</code></dt>
<dd> Serialize byte arrays char[N] as string.</dd>
<dt><code>-c</code></dt>
<dd> Generate C source code.</dd>
<dt><code>-d</code><i>path</i></dt>
<dd> Use <i>path</i> to save files.</dd>
<dt><code>-e</code></dt>
<dd> Generate SOAP RPC encoding style bindings.</dd>
<dt><code>-f</code><i>N</i></dt>
<dd> File split of <i>N</i> XML serializer implementations per file (N&gt;=10).</dd>
<dt><code>-h</code></dt>
<dd> Display help info.</dd>
<dt><code>-I</code><i>path</i></dt>
<dd> use <i>path</i>(s) for <code>#import</code> (paths separated with &#8216;:&#8217;).</dd>
<dt><code>-i</code></dt>
<dd> Generate C++ service proxies and objects inherited from <code>soap</code> struct.</dd>
<dt><code>-j</code></dt>
<dd> Generate C++ service proxies and objects that share a <code>soap</code> struct.</dd>
<dt><code>-k</code></dt>
<dd> Generate data structure walkers (experimental).</dd>
<dt><code>-l</code></dt>
<dd> Generate linkable modules (experimental).</dd>
<dt><code>-m</code></dt>
<dd> Generate Matlab(tm) code for MEX compiler.</dd>
<dt><code>-n</code></dt>
<dd> Use service name to rename service functions and namespace table.</dd>
<dt><code>-p</code><i>name</i></dt>
<dd> Save files with new prefix <i>name</i> instead of <code>soap</code>.</dd>
<dt><code>-Q</code><i>name</i></dt>
<dd> Use <i>name</i> as the C++ namespace for decls, including custom serializers.</dd>
<dt><code>-q</code><i>name</i></dt>
<dd> Use <i>name</i> as the C++ namespace for decls, excluding custom serializers.</dd>
<dt><code>-s</code></dt>
<dd> Generate deserialization code with strict XML validation checks.</dd>
<dt><code>-t</code></dt>
<dd> Generate code for fully <code>xsi:type</code> typed SOAP/XML messaging.</dd>
<dt><code>-u</code></dt>
<dd> Uncomment comments in WSDL/schema output by suppressing XML comments.</dd>
<dt><code>-v</code></dt>
<dd> Display version info.</dd>
<dt><code>-w</code></dt>
<dd> Do not generate WSDL and schema files.</dd>
<dt><code>-x</code></dt>
<dd> Do not generate sample XML message files.</dd>
<dt><code>-y</code></dt>
<dd> Include C/C++ type access information in sample XML messages.</dd>
<dt><code>-z1</code></dt>
<dd> Generate deprecated old-style C++ service proxies and objects.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wsdl2h/">wsdl2h</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Wana &lt;greuff [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
