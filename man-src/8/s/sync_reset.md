---
title: "sync_reset(8)"
name: "sync_reset"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sync_reset/"
description: "sync_reset – Account reset utility. DANGER."
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>sync_reset &#8211; Account reset utility. DANGER.</p>
<h2>Synopsis</h2>
<p><code>sync_reset</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-v</code> ] [ <code>-f</code> ]</p>
<h2>Description</h2>
<p><i>Sync_reset</i> is a small utility program to destroy user accounts on a system. The only safeguard which is in place is the obligary force option.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt><code>-f</code></p>
<dd>Force operation. Without this flag <i>sync_reset</i> just bails out with an error. Principally here to try and prevent accidents with command autorepeat.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sync_client/">sync_client</a>(8)</code></p>
<h2>Authors</h2>
<p>David Carter (dpc22 [at] cam.ac.uk), Ken Murchison (ken [at] oceana.com)</p>
