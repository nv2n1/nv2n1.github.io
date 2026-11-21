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
<dt><code>-k</code><i> keyring</i></dt>
<dd> Dump the contents of the specified keyring.</dd>
<dt><code>-2</code></dt>
<dd> Use the default keyring for PGP 2.x.</dd>
<dt><code>-5</code></dt>
<dd> Use the default keyring for PGP 5.</dd>
<dt><code>-s</code></dt>
<dd> Dump the secret keyring.</dd>
<dt><code>-S</code></dt>
<dd> Dump signatures.</dd>
<dt><code>-f</code></dt>
<dd> Dump fingerprints. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Thomas Roessler &lt;roessler [at] does-not-exist.org&gt; </p>
