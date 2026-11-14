---
title: "key-dns_resolver(8)"
name: "key-dns_resolver"
section: "8"
letter: "k"
url: "/docs/linux/man/8-key-dns_resolver/"
description: "key.dns_resolver – upcall for request-key to handle dns_resolver keys"
---

<p>key.dns_resolver &#8211; upcall for request-key to handle dns_resolver keys</p>
<h2>Synopsis</h2>
<p><code>/sbin/key.dns_resolver </code>&lt;key&gt;<br />
 <code>/sbin/key.dns_resolver </code>-D [-v] [-v] &lt;keydesc&gt; &lt;calloutinfo&gt;</p>
<h2>Description</h2>
<p>This program is invoked by request-key on behalf of the kernel when kernel services (such as NFS, CIFS and AFS) want to perform a hostname lookup and the kernel does not have the key cached. It is not ordinarily intended to be called directly. </p>
<p> It can be called in debugging mode to test its functionality by passing a <code>-D</code> flag on the command line. For this to work, the key description and the callout information must be supplied. Verbosity can be increased by supplying one or more <code>-v</code> flags.</p>
<h2>Errors</h2>
<p>All errors will be logged to the syslog.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
