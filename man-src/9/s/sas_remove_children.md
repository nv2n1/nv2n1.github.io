---
title: "sas_remove_children(9)"
name: "sas_remove_children"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_remove_children/"
description: "sas_remove_children – tear down a devices SAS data structures"
---

<p>sas_remove_children &#8211; tear down a devices SAS data structures</p>
<h2>Synopsis</h2>
<pre><code>void sas_remove_children(struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device belonging to the sas object</dl>
<h2>Description</h2>
<p>Removes all SAS PHYs and remote PHYs for a given object</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
