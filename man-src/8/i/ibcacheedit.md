---
title: "ibcacheedit(8)"
name: "ibcacheedit"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibcacheedit/"
description: "IBCACHEEDIT –"
---

<p>IBCACHEEDIT &#8211;</p>
<h2>Edit An Ibnetdiscover Cache</h2>
<h3>Synopsis</h3>
<p>ibcacheedit [options] &lt;orig.cache&gt; &lt;new.cache&gt;</p>
<h3>Description</h3>
<p>ibcacheedit allows users to edit an ibnetdiscover cache created through the <code>&#8211;cache</code> option in <code><a href="/docs/linux/man/8-ibnetdiscover/">ibnetdiscover</a>(8)</code> .</p>
<h3>Options</h3>
<dl>
<dt><code>&#8211;switchguid BEFOREGUID:AFTERGUID</code></p>
<dd>Specify a switchguid that should be changed. The before and after guid should be separated by a colon. On switches, port guids are identical to the switch guid, so port guids will be adjusted as well on switches.</p>
<dt><code>&#8211;caguid BEFOREGUID:AFTERGUID</code></p>
<dd>Specify a caguid that should be changed. The before and after guid should be separated by a colon.</p>
<dt><code>&#8211;sysimgguid BEFOREGUID:AFTERGUID</code></p>
<dd>Specify a sysimgguid that should be changed. The before and after guid should be spearated by a colon.</p>
<dt><code>&#8211;portguid NODEGUID:BEFOREGUID:AFTERGUID</code></p>
<dd>Specify a portguid that should be changed. The nodeguid of the port (e.g. switchguid or caguid) should be specified first, followed by a colon, the before port guid, another colon, then the after port guid. On switches, port guids are identical to the switch guid, so the switch guid will be adjusted as well on switches.</dl>
<h3>Debugging flags</h3>
<p><code>-h, &#8211;help</code> show the usage message </p>
<p> <code>-V, &#8211;version</code> show the version info.</p>
<h3>Authors</h3>
<dl>
<dt><code>Albert Chu</code></p>
<dd>&lt; <i>chu11 [at] llnl.gov</i> &gt; </p>
</dl>
