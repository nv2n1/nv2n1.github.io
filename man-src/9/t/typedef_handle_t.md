---
title: "typedef_handle_t(9)"
name: "typedef_handle_t"
section: "9"
letter: "t"
url: "/docs/linux/man/9-typedef_handle_t/"
description: "typedef_handle_t – The handle_t type represents a single atomic update being performed by some process."
---

<p>typedef_handle_t &#8211; The handle_t type represents a single atomic update being performed by some process.</p>
<h2>Synopsis</h2>
<pre>typedef handle_t;</pre>
<h2>Description</h2>
<p>All filesystem modifications made by the process go through this handle. Recursive operations (such as quota operations) are gathered into a single update. </p>
<p> The buffer credits field is used to account for journaled buffers being modified by the running process. To ensure that there is enough log space for all outstanding operations, we need to limit the number of outstanding buffers possible at any time. When the operation completes, any buffer credits not used are credited back to the transaction, so that at all times we know how many buffers the outstanding updates on a transaction might possibly touch. </p>
<p> This is an opaque datatype.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
