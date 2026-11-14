---
title: "rlm_idn(5)"
name: "rlm_idn"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_idn/"
description: "rlm_idn – FreeRADIUS Module"
---

<p>rlm_idn &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>When instantiated, the <i>rlm_idn</i> module provides an xlat for performing IDNA encoding of internationalized domain names. Decoding and other similar encodings like plain punycode are not currently supported. For example, the following unlang expression would evaluate to TRUE: &quot;%{idn:fūbar.site}&quot; == &quot;xn--fbar-v7a.site&quot; Each instance of rlm_idn may take the following parameters:</p>
<dl>
<dt>use_std3_ascii_rules</p>
<dd>This boolean is set by default and prohibits e.g. underscores in domain names.</p>
<dt>allow_unassigned</p>
<dd>This boolean is unset by default, which prohibits use of unassigned Unicode points.</dl>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>References</h2>
<p>RFC 3490</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5) <code><a href="/docs/linux/man/3-idna_to_ascii_8z/">idna_to_ascii_8z</a></code>(3)</p>
<h2>Author</h2>
<p>Brian S. Julin, bjulin [at] clarku.edu</p>
