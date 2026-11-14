---
title: "axports(5)"
name: "axports"
section: "5"
letter: "a"
url: "/docs/linux/man/5-axports/"
description: "axports – AX.25 port configuration file."
---

<p>axports &#8211; AX.25 port configuration file.</p>
<h2>Description</h2>
<p><code>Axports</code> is an ASCII file that contains information about each of the physical AX.25 ports that are to be used. When dealing with an AX.25 utility such as <code>call,</code> it takes an optional argument that is the port name. This port name is a reference to the line within <code>axports,</code> which has that name as its first argument. The information on each line contains enough information to bind the command to a particular physical AX.25 interface, this binding is done by matching the callsign on the line in <code>axports</code> with the callsign of the port set by <code>kissattach.</code> </p>
<p> The lines within <code>axports</code> must either be a comment line, which starts with a # in the first column, or a port description in the following format, each field being delimited by white space: </p>
<dl>
<dd>name callsign speed paclen window description</dl>
<p> The field descriptions are: </p>
<dl>
<dd>
<dl>
<dt><code>name</code></p>
<dd>is the unique identifier of the port. This is the name given as the port argument of many of the AX.25 support programs.</p>
<dt><code>callsign</code></p>
<dd>the callsign of the physical interface to bind to.</p>
<dt><code>speed</code></p>
<dd>this is the speed of interface, a value of zero means that no speed will be set by <a href="/docs/linux/man/8-kissattach/">kissattach</a>(8).</p>
<dt><code>paclen</code></p>
<dd>is the default maximum packet size for this interface.</p>
<dt><code>window</code></p>
<dd>the default window size for this interface.</p>
<dt><code>description</code></p>
<dd>a free format description of this interface, this field extends to the end of the line. This field may contain spaces.</dl>
</dl>
<h2>Files</h2>
<p>/etc/ax25/axports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/8-axparms/">axparms</a></code>(8), <code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8). </p>
