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
<dt><code>help</code></p>
<dd>This command just prints a help text for the <code>ctrl</code> object.</p>
<dt><code>list</code></p>
<dd>Show the registered netlink users.</p>
<dt><code>monitor</code></p>
<dd>Listen for generic netlink notifications.</p>
<dt><code>get</code></p>
<dd>Query the controller for a given user, identified either by <code>name</code> or <code>id</code>.</dl>
<h2>Options</h2>
<p>genl supports the following options.</p>
<dl>
<dt><code>-h, -help</code></p>
<dd>Show summary of options.</p>
<dt><code>-V, -Version</code></p>
<dd>Show version of program.</p>
<dt><code>-s, -stats, -statistics</code></p>
<dd>Show object statistics.</p>
<dt><code>-d, -details</code></p>
<dd>Show object details.</p>
<dt><code>-r, -raw</code></p>
<dd>Dump raw output only.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Author</h2>
<p>genl was written by Jamal Hadi Salim &lt;hadi [at] cyberus.ca&gt;. </p>
<p> This manual page was written by Petr Sabata &lt;contyk [at] redhat.com&gt;.</p>
