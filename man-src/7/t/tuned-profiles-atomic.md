---
title: "tuned-profiles-atomic(7)"
name: "tuned-profiles-atomic"
section: "7"
letter: "t"
url: "/docs/linux/man/7-tuned-profiles-atomic/"
description: "tuned-profiles-atomic – description of profiles provided for the Project Atomic"
---

<p>tuned-profiles-atomic &#8211; description of profiles provided for the Project Atomic </p>
<h2>Description</h2>
<p>These profiles are provided for the Project Atomic. They provides performance optimizations for the Atomic hosts (bare metal) and virtual guests. </p>
<h2>Profiles</h2>
<p>The following profiles are provided: </p>
<dl>
<dt><code>atomic-host</code></p>
<dd>Profile optimized for Atomic hosts (bare metal). It is based on throughput-performance profile. It additionally increases SELinux AVC cache, PID limit and tunes netfilter connections tracking. </p>
<dt><code>atomic-guest</code></p>
<dd>Profile optimized for virtual Atomic guests. It is based on virtual-guest profile. It additionally increases SELinux AVC cache, PID limit and tunes netfilter connections tracking. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/tuned/*</i> <i>/usr/lib/tuned/*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tuned/">tuned</a></code>(8) <code><a href="/docs/linux/man/8-tuned-adm/">tuned-adm</a></code>(8) <code><a href="/docs/linux/man/7-tuned-profiles/">tuned-profiles</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap/">tuned-profiles-sap</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap-hana/">tuned-profiles-sap-hana</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-oracle/">tuned-profiles-oracle</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-realtime/">tuned-profiles-realtime</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-nfv/">tuned-profiles-nfv</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-compat/">tuned-profiles-compat</a></code>(7)</p>
<h2>Author</h2>
<p>Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt;</p>
