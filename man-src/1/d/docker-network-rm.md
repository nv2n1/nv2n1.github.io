---
title: "docker-network-rm(1)"
name: "docker-network-rm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-network-rm/"
description: "docker-network-rm – Remove one or more networks"
---

<h2 class="name">NAME</h2>
<p> docker-network-rm &#8211; Remove one or more networks </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network rm NETWORK [NETWORK&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Removes one or more networks by name or identifier. To remove a network, you must first disconnect any containers connected to it. To remove the network named &#8216;my-network&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
  $ docker network rm my-network
</pre>
</dl>
<p> To delete multiple networks in a single docker network rm command, provide multiple network names or ids. The following example deletes a network with id 3695c422697f and a network named my-network: </p>
<dl>
<dt>
<dd>
<pre>
  $ docker network rm 3695c422697f my-network
</pre>
</dl>
<p> When you specify multiple networks, the command attempts to delete each in turn. If the deletion of one network fails, the command continues to the next on the list and tries to delete that. The command reports success or failure for each deletion. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for rm</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-network/">docker-network</a>(1)</code> </p>
<h2>Index</h2>
