---
title: "smiquery(1)"
name: "smiquery"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smiquery/"
description: "smiquery – query single information from SMI MIB modules"
---

<h2>NAME</h2>
<p> smiquery &#8211; query single information from SMI MIB modules</p>
<h2>SYNOPSIS</h2>
<p> <code>smiquery</code> [ <code>-Vh</code> ] [ <code>-p </code><i>module</i> ] <i>command name</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>smiquery</code> program is used to query information on a single item from an MIB module, e.g. module meta information or a single type definition.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Show the smiquery version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a help text and exit. The help text lists all available <code>command</code>s.</p>
<dt><code>-p </code><i>module</i><code>, &#8211;preload </code><i>module</i></p>
<dd> Preload the module <i>module</i> before reading the main module. This may be helpful if an incomplete main module misses to import some definitions.</p>
<dt><i>command name</i></p>
<dd> This specifies the kind of information to retrieve (module, imports, revisions, node, parent, compliance, index, members, children, type, or macro) and the item to retrieve.</dl>
<p> The module in question is searched along a path, which is initialized by the <code>SMIPATH</code> environment variable or by /usr/share/mibs if <code>SMIPATH</code> is not set. Files with a <code>.sming</code> extension are expected to be (old-style!) SMIng module files. Files with a <code>.my</code> or without any extension are expected to be SMIv1/v2 module files.</p>
<h2>EXAMPLE</h2>
<p> This example queries for information on the node ifNumber defined in the module IF-MIB. </p>
<pre>
  $ smiquery node IF-MIB::ifNumber
       MibNode: IF-MIB::ifNumber
           OID: 1.3.6.1.2.1.2.1
          Type: Integer32
   Declaration: OBJECT-TYPE
      NodeKind: scalar
        Access: read-only
        Status: current
   Description: The number of network interfaces (regardless of their
                current state) present on this system.
</pre>
<h2>SEE ALSO</h2>
<p> The <code><a href="/docs/linux/man/3-libsmi/">libsmi</a></code>(3) project is documented at <code><a rel="nofollow" href="http://www.ibr.cs.tu-bs.de/projects/libsmi/">http://www.ibr.cs.tu-bs.de/projects/libsmi/</a></code>.</p>
<h2>AUTHOR</h2>
<p> (C) 1999-2004 F. Strauss, TU Braunschweig, Germany &lt;strauss [at] ibr.cs.tu-bs.de&gt; </p>
<h2>Index</h2>
