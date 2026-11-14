---
title: "ccs_sync(8)"
name: "ccs_sync"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ccs_sync/"
description: "ccs_sync – Cluster Synchronization Utility"
---

<p>ccs_sync &#8211; Cluster Synchronization Utility</p>
<h2>Synopsis</h2>
<p><code>ccs_sync</code> [options] [&lt;host0&gt; [&#8230; &lt;hostN&gt;]]</p>
<h2>Description</h2>
<p><code>ccs_sync</code> is used to synchronize the cluster configuration file to one or more machines in a cluster.</p>
<h2>Options</h2>
<dl>
<dt>-f &lt;cluster_conf&gt;</p>
<dd>Specify the path of the cluster.conf file to propagate.</p>
<dt>-c &lt;NSS certificate DB&gt;</p>
<dd>Specify the path to the cacert.pem file.</p>
<dt>-i</p>
<dd>Increment the version in the configuration file before propagating.</p>
<dt>-h</p>
<dd>Display a usage message.</p>
<dt>-p &lt;port number&gt;</p>
<dd>Connect to ricci on the specified port</p>
<dt>-w</p>
<dd>Exit with failure status if any warnings are issued</dl>
<h2>Warning</h2>
<p>It is recommended that &#8216;cman_tool version -r &lt;x&gt;&#8217; be used instead of <code>ccs_sync</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cman_tool/">cman_tool</a>(8) </p>
