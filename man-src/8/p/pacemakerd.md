---
title: "pacemakerd(8)"
name: "pacemakerd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pacemakerd/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>pacemakerd</code> <i>mode </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>pacemakerd &#8211; Start/Stop Pacemaker</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd>This text</dd>
<dt>-$, <code>&#8211;version</code></dt>
<dd>Version information</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd>Increase debug output</dd>
<dt><code>-S</code>, <code>&#8211;shutdown</code></dt>
<dd>Instruct Pacemaker to shutdown on this machine</dd>
<dt><code>-F</code>, <code>&#8211;features</code></dt>
<dd>Display the full version and list of features Pacemaker was built with</dd></dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;foreground</code></dt>
<dd>(Ignored) Pacemaker always runs in the foreground</dd>
<dt><code>-p</code>, <code>&#8211;pid-file</code>=<i>value</i></dt>
<dd>(Ignored) Daemon pid file location</dd></dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
