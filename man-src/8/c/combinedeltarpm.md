---
title: "combinedeltarpm(8)"
name: "combinedeltarpm"
section: "8"
letter: "c"
url: "/docs/linux/man/8-combinedeltarpm/"
description: "combindeltarpm – combine multiple deltarpms to a single one"
---

<p>combindeltarpm &#8211; combine multiple deltarpms to a single one </p>
<h2>Synopsis</h2>
<p><code>combinedeltarpm</code> [<code>-v</code>] [<code>-V</code> <i>version</i>] [<code>-z</code> <i>compression</i>] [<code>-S</code> <i>signaturerpm</i>] <i>olddeltarpms&#8230;</i> <i>newdeltarpm</i> </p>
<h2>Description</h2>
<p>combinedeltarpm creates a new deltarpm from multiple old ones. Applying the rsulting deltarpm has the same effect as applying each of the old ones in the specified order. Use the <code>-v</code> option to make combinedeltarpm more verbose about its work. combinedeltarpm normally produces a V3 format deltarpm, use the <code>-V</code> option to specify a different version if desired. The <code>-z</code> option can be used to specify a different compression method, the default is to use the same compression method as used in the last of the old deltarpms. If you want to use a different header signature you can also specify a rpm with the <code>-S</code> option which will be used as signature reference. This feature can be used to if a deltarpm was made against an unsigned rpm which later got signed. </p>
<h2>Memory Considerations</h2>
<p>The implementation of combinedeltarpm currently unpacks the add-blocks of the deltarpms in memory, thus it needs about twice the uncompressed payload size of the target rpm.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-makedeltarpm/">makedeltarpm</a></code>(8) <code><a href="/docs/linux/man/8-applydeltarpm/">applydeltarpm</a></code>(8) </p>
<h2>Author</h2>
<p>Michael Schroeder &lt;mls [at] suse.de&gt;</p>
