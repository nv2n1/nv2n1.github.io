---
title: "systemd-id128(1)"
name: "systemd-id128"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-id128/"
description: "systemd-id128 – Generate and print sd-128 identifiers"
---

<h2 class="name">NAME</h2>
<p> systemd-id128 &#8211; Generate and print sd-128 identifiers </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-id128</code> [OPTIONS&#8230;] new</p>
<dt> <code>systemd-id128</code> [OPTIONS&#8230;] machine-id</p>
<dt> <code>systemd-id128</code> [OPTIONS&#8230;] boot-id</p>
<dt> <code>systemd-id128</code> [OPTIONS&#8230;] invocation-id</dl>
<h2>DESCRIPTION</h2>
<p> <code>id128</code></p>
<dd>may be used to conveniently print <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3) UUIDs. What identifier is printed depends on the specific verb. </p>
<p> With <code>new</code>, a new random identifier will be generated. </p>
<p> With <code>machine-id</code>, the identifier of the current machine will be printed. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5). </p>
<p> With <code>boot-id</code>, the identifier of the current boot will be printed. </p>
<p> Both <code>machine-id</code> and <code>boot-id</code> may be combined with the <code>&#8211;app-specific=</code><i>app-id</i> switch to generate application-specific IDs. See <code><a href="/docs/linux/man/3-sd_id128_get_machine/">sd_id128_get_machine</a></code>(3) for the discussion when this is useful. </p>
<p> With <code>invocation-id</code>, the identifier of the current service invocation will be printed. This is available in systemd services. See <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5). </p>
<p> With <code>show</code>, well-known UUIDs are printed. When no arguments are specified, all known UUIDs are shown. When arguments are specified, they must be the names or values of one or more known UUIDs, which are then printed.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-p</code>, <code>&#8211;pretty</code></p>
<dl>
<dt>
<dd> Generate output as programming language snippets.</dl>
<p> <code>-a </code><i>app-id</i>, <code>&#8211;app-specific=</code><i>app-id</i></p>
<dl>
<dt>
<dd> With this option, an identifier that is the result of hashing the application identifier <i>app-id</i> and the machine identifier will be printed. The <i>app-id</i> argument must be a valid sd-id128 string identifying the application.</dl>
<p> <code>-u</code>, <code>&#8211;uuid</code></p>
<dl>
<dt>
<dd> Generate output as an UUID formatted in the &quot;canonical representation&quot;, with five groups of digits separated by hyphens. See the m[blue]<code>wikipedia</code>m[]<font SIZE="-2">[1]</font> for more discussion.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3), <code><a href="/docs/linux/man/3-sd_id128_get_machine/">sd_id128_get_machine</a></code>(3)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> wikipedia</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://en.wikipedia.org/wiki/Universally_unique_identifier#Format">https://en.wikipedia.org/wiki/Universally_unique_identifier#Format</a></dl>
</dl>
<h2>Index</h2>
