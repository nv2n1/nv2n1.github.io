---
title: "tuned-profiles-origin-node(7)"
name: "tuned-profiles-origin-node"
section: "7"
letter: "t"
url: "/docs/linux/man/7-tuned-profiles-origin-node/"
description: "tuned-profiles-origin-node – description of profiles provided for OpenShift"
---

<p>tuned-profiles-origin-node &#8211; description of profiles provided for OpenShift </p>
<h2>Description</h2>
<p>These profiles are provided for OpenShift nodes. They provide performance optimizations for OpenShift Nodes running on either bare metal (origin-node-host) or virtual machines (origin-node-guest). </p>
<h2>Profiles</h2>
<p>The following profiles are provided: </p>
<dl>
<dt><code>origin-node-host</code></p>
<dd>Profile optimized for OpenShift hosts (bare metal). It is based on throughput-performance profile. It additionally increases SELinux AVC cache, PID limit and tunes netfilter connections tracking. </p>
<dt><code>origin-node-guest</code></p>
<dd>Profile optimized for virtual OpenShift guests. It is based on virtual-guest profile. It additionally increases SELinux AVC cache, PID limit and tunes netfilter connections tracking. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/tuned/*</i> <i>/usr/lib/tuned/*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tuned/">tuned</a></code>(8) <code><a href="/docs/linux/man/8-tuned-adm/">tuned-adm</a></code>(8) <code><a href="/docs/linux/man/7-tuned-profiles/">tuned-profiles</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap/">tuned-profiles-sap</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap-hana/">tuned-profiles-sap-hana</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-compat/">tuned-profiles-compat</a></code>(7)</p>
<h2>Author</h2>
<p>Scott Dodson &lt;sdodson [at] redhat.com&gt;</p>
