---
title: "fc_get_event_number(9)"
name: "fc_get_event_number"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_get_event_number/"
description: "fc_get_event_number – Obtain the next sequential FC event number"
---

<p>fc_get_event_number &#8211; Obtain the next sequential FC event number</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 fc_get_event_number(</code><i>void</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Notes</h2>
<p>We could have inlined this, but it would have required fc_event_seq to be exposed. For now, live with the subroutine call. Atomic used to avoid lock/unlock&#8230;</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
