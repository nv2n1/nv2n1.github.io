---
title: "corosync-objctl(8)"
name: "corosync-objctl"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-objctl/"
description: "corosync-objctl – Configure objects in the Object Database"
---

<p>corosync-objctl &#8211; Configure objects in the Object Database</p>
<h2>Synopsis</h2>
<p><code>corosync-objctl [-c|-w|-d|-a|-t-h] &lt;OBJECT-SPEC&gt;&#8230;</code></p>
<h2>Description</h2>
<p><code>corosync-objctl</code> is used to configure objects within the object database at runtime.</p>
<h2>Object-Spec</h2>
<dl>
<dt>There are two types of entities</p>
<dd><code>Objects</code> and <code>Key=Value pairs</code></p>
<dt><code>Objects</code></p>
<dd>Objects are container like entities that can hold other entities. They are specified as &quot;objectA&quot;.&quot;objectB&quot;. An example is logging.logger.</p>
<dt><code>Key=Value pairs</code></p>
<dd>These are the entities that actually hold values (read database &quot;fields&quot;). They are specified as object.key=value or just object.key if you are reading.</dl>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Create a new object.</p>
<dt><code>-d</code></p>
<dd>Delete an existing object.</p>
<dt><code>-w</code></p>
<dd>Use this option when you want to write a new value to a key.</p>
<dt><code>-a</code></p>
<dd>Display all values currently available.</p>
<dt><code>-t</code></p>
<dd>Track changes to an object and it&#8217;s children. As changes are made to the object they are printed out. this is kind of like a &quot;tail -f&quot; for the object database.</p>
<dt><code>-h</code></p>
<dd>Print basic usage.</dl>
<h2>Examples</h2>
<dl>
<dt>Print the objOne object (shouldn&#8217;t exist yet).</p>
<dd>$ corosync-objctl objOne</p>
<dt>Create the objOne object.</p>
<dd>$ corosync-objctl -c objOne</p>
<dt>Print the objOne object (empty).</p>
<dd>$ corosync-objctl objOne<br />
 objOne</p>
<dt>Write two new keys to the objOne object.</p>
<dd>$ corosync-objctl -w objOne.max=3000 objOne.min=100</p>
<dt>Print the objOne object (with the two new keys).</p>
<dd>$ corosync-objctl objOne<br />
 objOne.min=100<br />
 objOne.max=3000</p>
<dt>Delete the objOne.min key</p>
<dd>$ corosync-objctl -d objOne.min=100</p>
<dt>Prove that is gone.</p>
<dd>$ corosync-objctl objOne<br />
 objOne.max=3000</p>
<dt>Delete the whole objOne object.</p>
<dd>$ corosync-objctl -d objOne</p>
<dt>Prove that is gone.</p>
<dd>$ corosync-objctl objOne</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-confdb_initialize/">confdb_initialize</a></code>(3),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
