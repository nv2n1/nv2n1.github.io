---
title: "rsports(5)"
name: "rsports"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rsports/"
description: "rsports – Rose port configuration file."
---

<p>rsports &#8211; Rose port configuration file.</p>
<h2>Description</h2>
<p><code>Rsports</code> is an ASCII file that contains information about each of the Rose ports that are to be used. When dealing with a Rose utility such as <code>call,</code> it takes an optional argument that is the port name. This port name is a reference to the line within <code>rsports,</code> which has the same name. The information on each line contains enough information to bind the command to a particular Rose interface, this binding is done by matching the address on the line in <code>rsports</code> with the address of the port set by <code>ifconfig</code> or <code>rsattach.</code> </p>
<p> The <code>rsports</code> file may contain comments that begin with a # in the first column, or a port description in the following format, each field being delimited by white space: </p>
<dl>
<dd>name address description</dl>
<p> The field descriptions are: </p>
<dl>
<dd>
<dl>
<dt><code>name</code></p>
<dd>this is the unique Rose port identifier.</p>
<dt><code>address</code></p>
<dd>the address of the Rose interface to bind to.</p>
<dt><code>description</code></p>
<dd>a free format description of this interface, this field extends to the end of the line. It may contain spaces.</dl>
</dl>
<h2>Files</h2>
<p>/etc/ax25/rsports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-rsparms/">rsparms</a></code>(8). </p>
