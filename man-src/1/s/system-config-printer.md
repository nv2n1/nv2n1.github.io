---
title: "system-config-printer(1)"
name: "system-config-printer"
section: "1"
letter: "s"
url: "/docs/linux/man/1-system-config-printer/"
description: "system-config-printer – configure a CUPS server"
---

<h2 class="name">NAME</h2>
<p> system-config-printer &#8211; configure a CUPS server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>system-config-printer</code> [[&#8211;show-jobs&nbsp;<i>printer</i>] | [&#8211;debug] | [&#8211;help]]</dl>
<h2>DESCRIPTION</h2>
<p> <code>system-config-printer</code></p>
<dd>configures a CUPS server. It uses the CUPS API (bound to Python with pycups) to do this. The communication with the server is performed using IPP. As a result, it is equally able to configure a remote CUPS server as a local one.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;show-jobs </code><i>printer</i></p>
<dl>
<dt>
<dd> Show the named print queue.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Enable debugging output.</dl>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
