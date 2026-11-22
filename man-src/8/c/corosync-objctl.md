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
<dt>There are two types of entities</dt>
<dd><code>Objects</code> and <code>Key=Value pairs</code></dd>
<dt><code>Objects</code></dt>
<dd>Objects are container like entities that can hold other entities. They are specified as &quot;objectA&quot;.&quot;objectB&quot;. An example is logging.logger.</dd>
<dt><code>Key=Value pairs</code></dt>
<dd>These are the entities that actually hold values (read database &quot;fields&quot;). They are specified as object.key=value or just object.key if you are reading.</dd></dl>
<h2>Options</h2>
<dl>
<dt><code>-c</code></dt>
<dd>Create a new object.</dd>
<dt><code>-d</code></dt>
<dd>Delete an existing object.</dd>
<dt><code>-w</code></dt>
<dd>Use this option when you want to write a new value to a key.</dd>
<dt><code>-a</code></dt>
<dd>Display all values currently available.</dd>
<dt><code>-t</code></dt>
<dd>Track changes to an object and it&#8217;s children. As changes are made to the object they are printed out. this is kind of like a &quot;tail -f&quot; for the object database.</dd>
<dt><code>-h</code></dt>
<dd>Print basic usage.</dd></dl>
<h2>Examples</h2>
<dl>
<dt>Print the objOne object (shouldn&#8217;t exist yet).</dt>
<dd>$ corosync-objctl objOne</dd>
<dt>Create the objOne object.</dt>
<dd>$ corosync-objctl -c objOne</dd>
<dt>Print the objOne object (empty).</dt>
<dd>$ corosync-objctl objOne<br/>
 objOne</dd>
<dt>Write two new keys to the objOne object.</dt>
<dd>$ corosync-objctl -w objOne.max=3000 objOne.min=100</dd>
<dt>Print the objOne object (with the two new keys).</dt>
<dd>$ corosync-objctl objOne<br/>
 objOne.min=100<br/>
 objOne.max=3000</dd>
<dt>Delete the objOne.min key</dt>
<dd>$ corosync-objctl -d objOne.min=100</dd>
<dt>Prove that is gone.</dt>
<dd>$ corosync-objctl objOne<br/>
 objOne.max=3000</dd>
<dt>Delete the whole objOne object.</dt>
<dd>$ corosync-objctl -d objOne</dd>
<dt>Prove that is gone.</dt>
<dd>$ corosync-objctl objOne</dd></dl>
<h2>See Also</h2>
<p><code>confdb_initialize</code>(3),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
