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
<dt><code>&#8211;help</code></p>
<dd>
<dt><code>&#8211;vapidir=</code><i>DIRECTORY</i>&#8230;</p>
<dd>Look for package bindings in <i>DIRECTORY</i></p>
<dt><code>&#8211;girdir=</code><i>DIRECTORY</i>&#8230;</p>
<dd>Look for .gir files in <i>DIRECTORY</i></p>
<dt><code>&#8211;metadatadir=</code><i>DIRECTORY</i>&#8230;</p>
<dd>Look for GIR .metadata files in <i>DIRECTORY</i></p>
<dt><code>&#8211;pkg=</code><i>PACKAGE</i>&#8230;</p>
<dd>Include binding for <i>PACKAGE</i></p>
<dt><code>&#8211;vapi=</code><i>FILE</i></p>
<dd>Output VAPI file name</p>
<dt><code>&#8211;library=</code><i>NAME</i></p>
<dd>Library name</p>
<dt><code>&#8211;gir=</code><i>NAME</i>&#8211;<i>VERSION</i>.gir</p>
<dd>GObject-Introspection repository file name</p>
<dt><code>&#8211;gresources=</code><i>FILE</i>&#8230;</p>
<dd>GResources XML file name</p>
<dt><code>-b, &#8211;basedir=</code><i>DIRECTORY</i></p>
<dd>Base source directory</p>
<dt><code>-d, &#8211;directory=</code><i>DIRECTORY</i></p>
<dd>Output directory</p>
<dt><code>&#8211;version</code></p>
<dd>Display version number</p>
<dt><code>&#8211;api-version</code></p>
<dd>Display API version number</p>
<dt><code>-C, &#8211;ccode</code></p>
<dd>Output C code</p>
<dt><code>-H, &#8211;header=</code><i>FILE</i></p>
<dd>Output C header file</p>
<dt><code>&#8211;use-header</code></p>
<dd>Use C header file</p>
<dt><code>&#8211;includedir=</code><i>DIRECTORY</i></p>
<dd>Directory used to include the C header file</p>
<dt><code>-h, &#8211;internal-header=</code><i>FILE</i></p>
<dd>Output internal C header file</p>
<dt><code>&#8211;internal-vapi=</code><i>FILE</i></p>
<dd>Output vapi with internal api</p>
<dt><code>&#8211;symbols=</code><i>FILE</i></p>
<dd>Output symbols file</p>
<dt><code>-c, &#8211;compile</code></p>
<dd>Compile but do not link</p>
<dt><code>-o, &#8211;output=</code><i>FILE</i></p>
<dd>Place output in file <i>FILE</i></p>
<dt><code>-g, &#8211;debug</code></p>
<dd>Produce debug information</p>
<dt><code>&#8211;thread</code></p>
<dd>Enable multithreading support</p>
<dt><code>&#8211;enable-mem-profiler</code></p>
<dd>Enable GLib memory profiler</p>
<dt><code>-D, &#8211;define=SYMBOL&#8230;</code></p>
<dd>Define SYMBOL</p>
<dt><code>&#8211;main=SYMBOL&#8230;</code></p>
<dd>Use SYMBOL as entry point</p>
<dt><code>&#8211;nostdpkg</code></p>
<dd>Do not include standard packages</p>
<dt><code>&#8211;disable-assert</code></p>
<dd>Disable assertions</p>
<dt><code>&#8211;enable-checking</code></p>
<dd>Enable additional run-time checks</p>
<dt><code>&#8211;enable-deprecated</code></p>
<dd>Enable deprecated features</p>
<dt><code>&#8211;enable-experimental</code></p>
<dd>Enable experimental features</p>
<dt><code>&#8211;disable-warnings</code></p>
<dd>Disable warnings</p>
<dt><code>&#8211;fatal-warnings</code></p>
<dd>Treat warnings as fatal</p>
<dt><code>&#8211;enable-experimental-non-null</code></p>
<dd>Enable experimental enhancements for non-null types</p>
<dt><code>&#8211;cc=</code><i>COMMAND</i></p>
<dd>Use <i>COMMAND</i> as C compiler command</p>
<dt><code>-X, &#8211;Xcc=</code><i>OPTION</i>&#8230;</p>
<dd>Pass <i>OPTION</i>. to the C compiler</p>
<dt><code>&#8211;dump-tree=</code><i>FILE</i></p>
<dd>Write code tree to <i>FILE</i></p>
<dt><code>&#8211;save-temps</code></p>
<dd>Keep temporary files</p>
<dt><code>&#8211;profile=</code><i>PROFILE</i></p>
<dd>Use the given profile instead of the default</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Do not print messages to the console</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Print additional messages to the console</p>
<dt><code>&#8211;target-glib=</code><i>MAJOR</i>.<i>MINOR</i></p>
<dd>Target version of glib for code generation</p>
<dt><code>&#8211;enable-version-header</code></p>
<dd>Write vala build version in generated files</p>
<dt><code>&#8211;disable-version-header</code></p>
<dd>Do not write vala build version in generated files</dl>
<h2>Features</h2>
<p>Interfaces, properties, signals, foreach, lambda expressions, type inference for local variables, generics, non-null types, assisted memory management, exception handling</p>
<h2>Homepage And Bug Report</h2>
<p><a rel="nofollow" href="http://www.vala-project.org/">http://www.vala-project.org/</a></p>
<h2>Authors</h2>
<p>Jürg Billeter, Raffaele Sandrini. </p>
<p> Man page written to conform with Debian by Marc-Andre Lureau.</p>
