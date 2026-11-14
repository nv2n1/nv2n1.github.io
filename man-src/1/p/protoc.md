---
title: "protoc(1)"
name: "protoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-protoc/"
description: "protoc – compile protocol buffer description files"
---

<h2 class="name">NAME</h2>
<p> protoc &#8211; compile protocol buffer description files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>protoc</code> [<code>&#8211;cpp_out=</code><i>OUT_DIR</i>] [<code>&#8211;java_out=</code><i>OUT_DIR</i>] [<code>&#8211;python_out=</code><i>OUT_DIR</i>] [<code>-I</code><i>PATH</i>&nbsp;|&nbsp;<code>&#8211;proto_path=</code><i>PATH</i>] <i>PROTO_FILE</i></p>
<dt> <code>protoc</code> {<code>-h</code> | <code>&#8211;help</code>}</p>
<dt> <code>protoc</code> <code>&#8211;version</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>protoc</code></p>
<dd>is a compiler for protocol buffers definitions files. It can can generate C++, Java and Python source code for the classes defined in <i>PROTO_FILE</i>.</p>
<h2>OPTIONS</h2>
<p> <code>-I</code><i>PATH</i>, <code>&#8211;proto_path=</code><i>PATH</i></p>
<dl>
<dt>
<dd> Specify the directory in which to search for imports. May be specified multiple times; directories will be searched in order. If not given, the current working directory is used.</dl>
<p> <code>&#8211;cpp_out=</code><i>OUT_DIR</i></p>
<dl>
<dt>
<dd> Enable generation of C++ bindings and store them in <i>OUT_DIR</i>.</dl>
<p> <code>&#8211;java_out=</code><i>OUT_DIR</i></p>
<dl>
<dt>
<dd> Enable generation of Java bindings and store them in <i>OUT_DIR</i>.</dl>
<p> <code>&#8211;python_out=</code><i>OUT_DIR</i></p>
<dl>
<dt>
<dd> Enable generation of Python bindings and store them in <i>OUT_DIR</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version of program.</dl>
<p> Note that at least one of the <code>&#8211;cpp_out</code>, <code>&#8211;java_out</code> and <code>&#8211;python_out</code> options must be given (otherwise the program has nothing to do). It&#8217;s also possible to specify more than one.</p>
<h2>BUGS</h2>
<p> The program currently exits with code 255 for all errors, which makes it hard to differentiante from scripts the actual error. </p>
<p> The upstreams BTS can be found at m[blue]<code><a rel="nofollow" href="http://code.google.com/p/protobuf/issues/list">http://code.google.com/p/protobuf/issues/list</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> More documentation about protocol buffers syntax and APIs is available online at m[blue]<code><a rel="nofollow" href="http://code.google.com/apis/protocolbuffers/docs/overview.html">http://code.google.com/apis/protocolbuffers/docs/overview.html</a></code>m[].</p>
<h2>AUTHOR</h2>
<p> <code>Iustin Pop</code> &lt;iustin [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Wrote this manpage for the Debian system.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Iustin Pop </p>
<p> This manual page was written for the Debian system (but may be used by others). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or (at your option) any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
