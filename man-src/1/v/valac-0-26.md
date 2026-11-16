---
title: "valac-0-26(1)"
name: "valac-0-26"
section: "1"
letter: "v"
url: "/docs/linux/man/1-valac-0-26/"
description: "valac – compiler that translates Vala source code into C source and header files"
---

<p>valac &#8211; compiler that translates Vala source code into C source and header files</p>
<h2>Synopsis</h2>
<p><code>valac</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>Description</h2>
<p>Vala is a new programming language that aims to bring modern programming language features to GNOME developers without imposing any additional runtime requirements and without using a different ABI compared to applications and libraries written in C. </p>
<p> valac, the Vala compiler, is a self-hosting compiler that translates Vala source code into C source and header files. It uses the GObject type system to create classes and interfaces declared in the Vala source code.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>&#8211;help</code></dt>
<dd>
</dd><dt><code>&#8211;vapidir=</code><i>DIRECTORY</i>&#8230;</dt>
<dd>Look for package bindings in <i>DIRECTORY</i></dd>
<dt><code>&#8211;girdir=</code><i>DIRECTORY</i>&#8230;</dt>
<dd>Look for .gir files in <i>DIRECTORY</i></dd>
<dt><code>&#8211;metadatadir=</code><i>DIRECTORY</i>&#8230;</dt>
<dd>Look for GIR .metadata files in <i>DIRECTORY</i></dd>
<dt><code>&#8211;pkg=</code><i>PACKAGE</i>&#8230;</dt>
<dd>Include binding for <i>PACKAGE</i></dd>
<dt><code>&#8211;vapi=</code><i>FILE</i></dt>
<dd>Output VAPI file name</dd>
<dt><code>&#8211;library=</code><i>NAME</i></dt>
<dd>Library name</dd>
<dt><code>&#8211;gir=</code><i>NAME</i>&#8211;<i>VERSION</i>.gir</dt>
<dd>GObject-Introspection repository file name</dd>
<dt><code>&#8211;gresources=</code><i>FILE</i>&#8230;</dt>
<dd>GResources XML file name</dd>
<dt><code>-b, &#8211;basedir=</code><i>DIRECTORY</i></dt>
<dd>Base source directory</dd>
<dt><code>-d, &#8211;directory=</code><i>DIRECTORY</i></dt>
<dd>Output directory</dd>
<dt><code>&#8211;version</code></dt>
<dd>Display version number</dd>
<dt><code>&#8211;api-version</code></dt>
<dd>Display API version number</dd>
<dt><code>-C, &#8211;ccode</code></dt>
<dd>Output C code</dd>
<dt><code>-H, &#8211;header=</code><i>FILE</i></dt>
<dd>Output C header file</dd>
<dt><code>&#8211;use-header</code></dt>
<dd>Use C header file</dd>
<dt><code>&#8211;includedir=</code><i>DIRECTORY</i></dt>
<dd>Directory used to include the C header file</dd>
<dt><code>-h, &#8211;internal-header=</code><i>FILE</i></dt>
<dd>Output internal C header file</dd>
<dt><code>&#8211;internal-vapi=</code><i>FILE</i></dt>
<dd>Output vapi with internal api</dd>
<dt><code>&#8211;symbols=</code><i>FILE</i></dt>
<dd>Output symbols file</dd>
<dt><code>-c, &#8211;compile</code></dt>
<dd>Compile but do not link</dd>
<dt><code>-o, &#8211;output=</code><i>FILE</i></dt>
<dd>Place output in file <i>FILE</i></dd>
<dt><code>-g, &#8211;debug</code></dt>
<dd>Produce debug information</dd>
<dt><code>&#8211;thread</code></dt>
<dd>Enable multithreading support</dd>
<dt><code>&#8211;enable-mem-profiler</code></dt>
<dd>Enable GLib memory profiler</dd>
<dt><code>-D, &#8211;define=SYMBOL&#8230;</code></dt>
<dd>Define SYMBOL</dd>
<dt><code>&#8211;main=SYMBOL&#8230;</code></dt>
<dd>Use SYMBOL as entry point</dd>
<dt><code>&#8211;nostdpkg</code></dt>
<dd>Do not include standard packages</dd>
<dt><code>&#8211;disable-assert</code></dt>
<dd>Disable assertions</dd>
<dt><code>&#8211;enable-checking</code></dt>
<dd>Enable additional run-time checks</dd>
<dt><code>&#8211;enable-deprecated</code></dt>
<dd>Enable deprecated features</dd>
<dt><code>&#8211;enable-experimental</code></dt>
<dd>Enable experimental features</dd>
<dt><code>&#8211;disable-warnings</code></dt>
<dd>Disable warnings</dd>
<dt><code>&#8211;fatal-warnings</code></dt>
<dd>Treat warnings as fatal</dd>
<dt><code>&#8211;enable-experimental-non-null</code></dt>
<dd>Enable experimental enhancements for non-null types</dd>
<dt><code>&#8211;cc=</code><i>COMMAND</i></dt>
<dd>Use <i>COMMAND</i> as C compiler command</dd>
<dt><code>-X, &#8211;Xcc=</code><i>OPTION</i>&#8230;</dt>
<dd>Pass <i>OPTION</i>. to the C compiler</dd>
<dt><code>&#8211;dump-tree=</code><i>FILE</i></dt>
<dd>Write code tree to <i>FILE</i></dd>
<dt><code>&#8211;save-temps</code></dt>
<dd>Keep temporary files</dd>
<dt><code>&#8211;profile=</code><i>PROFILE</i></dt>
<dd>Use the given profile instead of the default</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd>Do not print messages to the console</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Print additional messages to the console</dd>
<dt><code>&#8211;target-glib=</code><i>MAJOR</i>.<i>MINOR</i></dt>
<dd>Target version of glib for code generation</dd>
<dt><code>&#8211;enable-version-header</code></dt>
<dd>Write vala build version in generated files</dd>
<dt><code>&#8211;disable-version-header</code></dt>
<dd>Do not write vala build version in generated files</dd></dl>
<h2>Features</h2>
<p>Interfaces, properties, signals, foreach, lambda expressions, type inference for local variables, generics, non-null types, assisted memory management, exception handling</p>
<h2>Homepage And Bug Report</h2>
<p><a rel="nofollow" href="http://www.vala-project.org/">http://www.vala-project.org/</a></p>
<h2>Authors</h2>
<p>Jürg Billeter, Raffaele Sandrini. </p>
<p> Man page written to conform with Debian by Marc-Andre Lureau.</p>
