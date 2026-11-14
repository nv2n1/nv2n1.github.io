---
title: "parport_list(3)"
name: "parport_list"
section: "3"
letter: "p"
url: "/docs/linux/man/3-parport_list/"
description: "parport_list – a collection of parallel ports"
---

<p>parport_list &#8211; a collection of parallel ports</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ieee1284.h&gt;</code></pre>
<h2>Description</h2>
<p>A parport_list structure is just a vector of parport structures.</p>
<h2>Structure Members</h2>
<p>The structure has the following members: </p>
<dl>
<dd>
<pre>struct parport_list {
 /* Number of elements in the vector. */
 int portc;
 /* The ports. */
 struct parport **portv;
};</pre>
</dl>
<h2>Author</h2>
<p><code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2001-2003 Tim Waugh</p>
