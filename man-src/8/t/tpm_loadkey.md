---
title: "tpm_loadkey(8)"
name: "tpm_loadkey"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_loadkey/"
description: "tpm_loadkey"
---

<p>tpm_loadkey</p>
<h2>Synopsis</h2>
<p><code>tpm_loadkey</code> [<code>-r HOST</code>] [<code>-hv</code>] BLOB-FILE UUID-FILE</p>
<h2>Description</h2>
<p>The program loads the key in BLOB-FILE into persistent storage and registers it using the UUID in UUID-FILE.</p>
<dl>
<dt>-r HOST</p>
<dd>Perform operation on remote HOST.</p>
<dt>-h</p>
<dd>Display command usage info.</p>
<dt>-v</p>
<dd>Display command version info.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_quote_tools/">tpm_quote_tools</a></code>(8), <code><a href="/docs/linux/man/8-tpm_mkuuid/">tpm_mkuuid</a></code>(8), <code><a href="/docs/linux/man/8-tpm_mkaik/">tpm_mkaik</a></code>(8), <code><a href="/docs/linux/man/8-tpm_unloadkey/">tpm_unloadkey</a></code>(8) </p>
