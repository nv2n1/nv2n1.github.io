---
title: "protoc-gen-go(1)"
name: "protoc-gen-go"
section: "1"
letter: "p"
url: "/docs/linux/man/1-protoc-gen-go/"
description: "protoc-gen-go – Go compiler output filter for the protocol buffer compiler"
---

<h2 class="name">NAME</h2>
<p> protoc-gen-go &#8211; Go compiler output filter for the protocol buffer compiler </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>protoc</code></p>
<dd> <i>&#8211;plugin=protoc-gen-go=/usr/bin/protoc-gen-go</i> <i>&#8211;go_out=gocode</i> <i>input.proto</i></p>
<dt><code>protoc</code></p>
<dd> <i>&#8211;go_out=gocode</i> <i>input.proto</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>protoc-gen-go</code> is a filter for the <code><a href="/docs/linux/man/1-protoc/">protoc</a></code>(1) protocol buffer compiler. It takes the protocol buffer format from <code><a href="/docs/linux/man/1-protoc/">protoc</a></code>(1) as input and produces Go code as output which can then be used to encode (marshal) and decode (unmarshal) data in the protocol buffer format specified in its input. The input is typically produced by <code><a href="/docs/linux/man/1-protoc/">protoc</a></code>(1) by taking a .proto input file and converting it to a protocol buffer descriptor format which <code>protoc-gen-go</code> can then read. If <code>protoc-gen-go</code> can be found in the regular search path, the <i>&#8211;plugin</i> flag can be omitted.</p>
<h2>OPTIONS</h2>
<p> <code>protoc-gen-go</code> itself doesn&#8217;t like options. All input is taken from stdin. If you use the protobuf compiler to invoke protoc-gen-go, see <code><a href="/docs/linux/man/1-protoc/">protoc</a></code>(1) for a detailed list of all options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-protoc/">protoc</a></code>(1)<code>.</code></p>
<h2>AUTHOR</h2>
<p> <code>protoc-gen-go</code> was mostly written by Rob Pike and David Symonds for The Go Authors.</p>
<h2>REPORTING BUGS</h2>
<p> Please file any bug in the bug tracker at <i><a rel="nofollow" href="https://code.google.com/p/goprotobuf/issues/list">https://code.google.com/p/goprotobuf/issues/list</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2010-2013 The Go Authors. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<dl>
<dt>&bull;</p>
<dd> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.</p>
<dt>&bull;</p>
<dd> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
<dt>&bull;</p>
<dd> Neither the name of Google Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.</dl>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<h2>Index</h2>
