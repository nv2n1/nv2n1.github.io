---
title: "ata_slave_link_init(9)"
name: "ata_slave_link_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_slave_link_init/"
description: "ata_slave_link_init – initialize slave link"
---

<p>ata_slave_link_init &#8211; initialize slave link</p>
<h2>Synopsis</h2>
<pre><code>int ata_slave_link_init(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>port to initialize slave link for</dl>
<h2>Description</h2>
<p>Create and initialize slave link for <i>ap</i>. This enables slave link handling on the port. </p>
<p> In libata, a port contains links and a link contains devices. There is single host link but if a PMP is attached to it, there can be multiple fan-out links. On SATA, there&#8217;s usually a single device connected to a link but PATA and SATA controllers emulating TF based interface can have two &#8211; master and slave. </p>
<p> However, there are a few controllers which don&#8217;t fit into this abstraction too well &#8211; SATA controllers which emulate TF interface with both master and slave devices but also have separate SCR register sets for each device. These controllers need separate links for physical link handling (e.g. onlineness, link speed) but should be treated like a traditional M/S controller for everything else (e.g. command issue, softreset). </p>
<p> slave_link is libata&#8217;s way of handling this class of controllers without impacting core layer too much. For anything other than physical link handling, the default host link is used for both master and slave. For physical link handling, separate <i>ap</i>-&gt;slave_link is used. All dirty details are implemented inside libata core layer. From LLD&#8217;s POV, the only difference is that prereset, hardreset and postreset are called once more for the slave link, so the reset sequence looks like the following. </p>
<p> prereset(M) -&gt; prereset(S) -&gt; hardreset(M) -&gt; hardreset(S) -&gt; softreset(M) -&gt; postreset(M) -&gt; postreset(S) </p>
<p> Note that softreset is called only for the master. Softreset resets both M/S by definition, so SRST on master should handle both (the standard method will work just fine). </p>
<p> LOCKING: Should be called before host is registered.</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
