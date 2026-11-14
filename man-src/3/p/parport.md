---
title: "parport(3)"
name: "parport"
section: "3"
letter: "p"
url: "/docs/linux/man/3-parport/"
description: "parport – representation of a parallel port"
---

<p>parport &#8211; representation of a parallel port</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ieee1284.h&gt;</code></pre>
<h2>Description</h2>
<p>A parport structure represents a parallel port.</p>
<h2>Structure Members</h2>
<p>The structure has the following members: </p>
<dl>
<dd>
<pre>struct parport {
 /* An artibrary name for the port. */
 const char *name;
 /* The base address of the port, if that has any meaning, or zero. */
 unsigned long base_addr;
 /* The ECR address of the port, if that has any meaning, or zero. */
 unsigned long hibase_addr;
 /* The filename associated with this port,
 * if that has any meaning, or NULL. */
 const char *filename;
};</pre>
</dl>
<h2>Author</h2>
<p><code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2001-2003 Tim Waugh</p>
