---

title: "cargo-fetch(1)"
name: "cargo-fetch"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-fetch/"
description: "cargo-fetch – Fetch dependencies of a package from the network"
---

<p> cargo fetch [OPTIONS]</p>
<p> If a lockfile is available, this command will ensure that all of the git dependencies and/or registries dependencies are downloaded and locally available. The network is never touched after a `cargo fetch` unless the lockfile changes. </p>
<p> If the lockfile is not available, then this is the equivalent of `cargo generate-lockfile`. A lockfile is generated and dependencies are also all updated. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;manifest-path </code>PATH</dt>
<dd> Path to the manifest to fetch dependencies for.</dd>
<dl>
</dl>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Use verbose output.</dd>
<dl>
</dl>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> No output printed to stdout.</dd>
<dl>
</dl>
<dt><code>&#8211;color </code>WHEN</dt>
<dd> Coloring: auto, always, never.</dd>
<dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-update/">cargo-update</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
