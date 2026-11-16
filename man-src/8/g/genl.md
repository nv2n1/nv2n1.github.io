---
title: "genl(8)"
name: "genl"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genl/"
description: "genl – generic netlink utility frontend"
---

<p>genl &#8211; generic netlink utility frontend</p>
<h2>Synopsis</h2>
<p><code>genl</code> [ <code>-s</code>[<code>tatistics</code>] ] [ <code>-d</code>[<code>etails</code>] ] [ <code>-r</code>[<code>aw</code>] ] <code>OBJECT</code> </p>
<pre><code>genl { -V[ersion] | -h[elp] }
OBJECT := {
    ctrl
    CTRL_OPTS }
CTRL_OPTS := {
    help | list | monitor | get
    PARMS }
PARMS := {
    name
    NAME |
    id
    ID }</code></pre>
<h2>Description</h2>
<p>The <code>genl</code> utility provides a simple frontend to the generic netlink library. Although it&#8217;s designed to support multiple <i>OBJECT</i>s, for now only the <code>ctrl</code> object is available, which is used to query the generic netlink controller.</p>
<h3>ctrl</h3>
<p>The generic netlink controller can be queried in various ways:</p>
<dl>
<dt><code>help</code></dt>
<dd>This command just prints a help text for the <code>ctrl</code> object.</dd>
<dt><code>list</code></dt>
<dd>Show the registered netlink users.</dd>
<dt><code>monitor</code></dt>
<dd>Listen for generic netlink notifications.</dd>
<dt><code>get</code></dt>
<dd>Query the controller for a given user, identified either by <code>name</code> or <code>id</code>.</dd></dl>
<h2>Options</h2>
<p>genl supports the following options.</p>
<dl>
<dt><code>-h, -help</code></dt>
<dd>Show summary of options.</dd>
<dt><code>-V, -Version</code></dt>
<dd>Show version of program.</dd>
<dt><code>-s, -stats, -statistics</code></dt>
<dd>Show object statistics.</dd>
<dt><code>-d, -details</code></dt>
<dd>Show object details.</dd>
<dt><code>-r, -raw</code></dt>
<dd>Dump raw output only.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Author</h2>
<p>genl was written by Jamal Hadi Salim &lt;hadi [at] cyberus.ca&gt;. </p>
<p> This manual page was written by Petr Sabata &lt;contyk [at] redhat.com&gt;.</p>
