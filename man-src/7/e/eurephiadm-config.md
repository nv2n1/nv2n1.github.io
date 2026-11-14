---
title: "eurephiadm-config(7)"
name: "eurephiadm-config"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-config/"
description: "eurephiadm config – Show and modify eurephia configuration settings"
---

<p>eurephiadm config &#8211; Show and modify eurephia configuration settings</p>
<h2>Description</h2>
<p>The config command let you add, change or delete configuration parameters in the eurephia database in an easy way. To be allowed to do so, you must have been granted &#8216;config&#8217; access.</p>
<h2>Options</h2>
<p>The following arguments are accepted:</p>
<dl>
<dt><code>-l</code> | <code>&#8211;list</code></p>
<dd>List all parameters set in the database</p>
<dt><code>-s</code> | <code>&#8211;set</code> &lt;key&gt; &lt;value&gt;</p>
<dd>Add or change a parameter.</p>
<dt><code>-D</code> | <code>&#8211;delete</code> &lt;key&gt;</p>
<dd>Remove the parameter.</p>
<dt>If no arguments is given, you can give a key name, and the associated value will be printed.</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm/">eurephiadm</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
