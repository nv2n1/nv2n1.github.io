---
title: "idr_get_next(9)"
name: "idr_get_next"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_get_next/"
description: "idr_get_next – lookup next object of id to given id."
---

<p>idr_get_next &#8211; lookup next object of id to given id.</p>
<h2>Synopsis</h2>
<pre><code>void *idr_get_next(struct idr *idp, int *nextidp);</code></pre>
<h2>Arguments</h2>
<p><i>idp</i></p>
<dl>
<dd>
<dd>idr handle</dl>
<p> <i>nextidp</i></p>
<dl>
<dd>pointer to lookup key</dl>
<h2>Description</h2>
<p>Returns pointer to registered object with id, which is next number to given id. After being looked up, *<i>nextidp</i> will be updated for the next iteration. </p>
<p> This function can be called under <code>rcu_read_lock</code>, given that the leaf pointers lifetimes are correctly managed.</p>
<h2>Copyright</h2>
