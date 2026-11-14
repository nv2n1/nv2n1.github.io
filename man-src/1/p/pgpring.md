---
title: "pgpring(1)"
name: "pgpring"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgpring/"
description: "pgpring – Mutt key ring dumper"
---

<h2>NAME</h2>
<p> pgpring &#8211; Mutt key ring dumper </p>
<h2>SYNTAX</h2>
<p> <code>pgpring</code> [ <code>-k</code> <i>keyring</i> ] [ <code>-2</code> | <code>-5</code> ] [ <code>-s</code> ] [ <code>-S</code> ] [ <code>-f</code> ] </p>
<h2>DESCRIPTION</h2>
<p> pgpring is a key ring dumper. It extracts information from PGP&#8217;s binary key ring and emits it in an (almost) readable output format understood by mutt&#8217;s key selection routines. This output format mimics the one used by the GNU Privacy Guard (GPG). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code><i> keyring</i></p>
<dd> Dump the contents of the specified keyring.</p>
<dt><code>-2</code></p>
<dd> Use the default keyring for PGP 2.x.</p>
<dt><code>-5</code></p>
<dd> Use the default keyring for PGP 5.</p>
<dt><code>-s</code></p>
<dd> Dump the secret keyring.</p>
<dt><code>-S</code></p>
<dd> Dump signatures.</p>
<dt><code>-f</code></p>
<dd> Dump fingerprints. </p>
</dl>
<h2>AUTHORS</h2>
<p> Thomas Roessler &lt;roessler [at] does-not-exist.org&gt; </p>
<h2>Index</h2>
