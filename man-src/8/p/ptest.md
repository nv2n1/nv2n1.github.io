---
title: "ptest(8)"
name: "ptest"
section: "8"
letter: "p"
url: "/docs/linux/man/8-ptest/"
description: "ptest – Part of the Pacemaker cluster resource manager"
---

<p>ptest &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>ptest</code> [<i>-?Vv</i>] <i>&#8211;</i>[<i>Xxp</i>] <i>{other options}</i></p>
<h2>Description</h2>
<p>ptest &#8211; Calculate the cluster&#8217;s response to the supplied cluster state</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-S</code>, <code>&#8211;simulate</code></p>
<dd>Simulate the transition&#8217;s execution to find invalid graphs</p>
<dt><code>-s</code>, <code>&#8211;show-scores</code></p>
<dd>Display resource allocation scores</p>
<dt><code>-a</code>, <code>&#8211;all-actions</code></p>
<dd>Display all possible actions &#8211; even ones not part of the transition graph</p>
<dt><code>-L</code>, <code>&#8211;live-check</code></p>
<dd>Connect to the CIB and use the current contents as input</p>
<dt><code>-X</code>, <code>&#8211;xml-text</code>=<i>value</i></p>
<dd>Retrieve XML from the supplied string</p>
<dt><code>-x</code>, <code>&#8211;xml-file</code>=<i>value</i></p>
<dd>Retrieve XML from the named file</p>
<dt><code>-I</code>, <code>&#8211;save-input</code>=<i>value</i></p>
<dd>Save the input to the named file</p>
<dt><code>-G</code>, <code>&#8211;save-graph</code>=<i>value</i></p>
<dd>Save the transition graph (XML format) to the named file</p>
<dt><code>-D</code>, <code>&#8211;save-dotfile</code>=<i>value</i></p>
<dd>Save the transition graph (DOT format) to the named file</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
