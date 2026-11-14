---
title: "nrports(5)"
name: "nrports"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nrports/"
description: "nrports – NET/ROM port configuration file."
---

<p>nrports &#8211; NET/ROM port configuration file.</p>
<h2>Description</h2>
<p><code>Nrports</code> is an ASCII file that contains information about each of the NET/ROM ports that are to be used. When dealing with an NET/ROM utility such as <code>call,</code> it takes an optional argument that is the port name. This port name is a reference to the line within <code>nrports,</code> which has the same name. The information on each line contains enough information to bind the command to a particular NET/ROM interface, this binding is done by matching the callsign on the line in <code>nrports</code> with the callsign of the port set by <code>ifconfig.</code> </p>
<p> The <code>nrports</code> file may contain comments that begin with a # in the first column, or a port description in the following format, each field being delimited by white space: </p>
<dl>
<dd>name callsign alias paclen description</dl>
<p> The field descriptions are: </p>
<dl>
<dd>
<dl>
<dt><code>name</code></p>
<dd>this is the unique NET/ROM port identifier.</p>
<dt><code>callsign</code></p>
<dd>the callsign of the NET/ROM interface to bind to.</p>
<dt><code>alias</code></p>
<dd>this is the alias of the NET/ROM port.</p>
<dt><code>paclen</code></p>
<dd>is the default packet size for this interface.</p>
<dt><code>description</code></p>
<dd>a free format description of this interface, this field extends to the end of the line. It may contain spaces.</dl>
</dl>
<h2>Files</h2>
<p>/etc/ax25/nrports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8). </p>
