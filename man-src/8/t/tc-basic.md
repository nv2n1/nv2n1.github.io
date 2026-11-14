---
title: "tc-basic(8)"
name: "tc-basic"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-basic/"
description: "basic – basic traffic control filter"
---

<p>basic &#8211; basic traffic control filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>basic</code> [ <code>match</code> <i>EMATCH_TREE</i> ] [ <code>action</code> <i>ACTION_SPEC</i> ] [ <code>classid</code> <i>CLASSID</i> ]</p>
<h2>Description</h2>
<p>The <code>basic</code> filter allows to classify packets using the extended match infrastructure.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Push matching packets into the class identified by <i>CLASSID</i>.</p>
<dt><code>match</code><i> EMATCH_TREE</i></p>
<dd>Match packets using the extended match infrastructure. See <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8) for a detailed description of the allowed syntax in <i>EMATCH_TREE</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8) </p>
