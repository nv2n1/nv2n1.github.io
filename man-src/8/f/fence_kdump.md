---
title: "fence_kdump(8)"
name: "fence_kdump"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_kdump/"
description: "fence_kdump – fencing agent for use with kdump crash recovery service"
---

<p>fence_kdump &#8211; fencing agent for use with kdump crash recovery service</p>
<h2>Synopsis</h2>
<p><code>fence_kdump</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>Description</h2>
<p><i>fence_kdump</i> is an I/O fencing agent to be used with the kdump crash recovery service. When the <i>fence_kdump</i> agent is invoked, it will listen for a message from the failed node that acknowledges that the failed node it executing the kdump crash kernel. Note that <i>fence_kdump</i> is not a replacement for traditional fencing methods. The <i>fence_kdump</i> agent can only detect that a node has entered the kdump crash recovery service. This allows the kdump crash recovery service complete without being preempted by traditional power fencing methods.</p>
<h2>Options</h2>
<dl>
<dt><code>-n, &#8211;nodename=</code><i>NODE</i></p>
<dd>Name or IP address of node to be fenced. This option is required for the &quot;off&quot; action. (default: none)</p>
<dt><code>-p, &#8211;ipport=</code><i>PORT</i></p>
<dd>IP port number that the <i>fence_kdump</i> agent will use to listen for messages. (default: 7410)</p>
<dt><code>-f, &#8211;family=</code><i>FAMILY</i></p>
<dd>IP network family. Force the <i>fence_kdump</i> agent to use a specific family. The value for <i>FAMILY</i> can be &quot;auto&quot;, &quot;ipv4&quot;, or &quot;ipv6&quot;. (default: auto)</p>
<dt><code>-o, &#8211;action=</code><i>ACTION</i></p>
<dd>Fencing action to perform. The value for <i>ACTION</i> can be either &quot;off&quot; or &quot;metadata&quot;. (default: off)</p>
<dt><code>-t, &#8211;timeout=</code><i>TIMEOUT</i></p>
<dd>Numer of seconds to wait for message from failed node. If no message is received within <i>TIMEOUT</i> seconds, the <i>fence_kdump</i> agent returns failure. (default: 60)</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Print verbose output.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage and exit.</dl>
<h2>Stdin Parameters</h2>
<p>These parameters are passed to <i>fence_kdump</i> via standard input if no command-line options are present.</p>
<dl>
<dt><code>nodename=</code><i>NODE</i></p>
<dd>Name or IP address of node to be fenced. This option is required for the &quot;off&quot; action. (default: none)</p>
<dt><code>ipport=</code><i>PORT</i></p>
<dd>IP port number that the <i>fence_kdump</i> agent will use to listen for messages. (default: 7410)</p>
<dt><code>action=</code><i>ACTION</i></p>
<dd>Fencing action to perform. The value for <i>ACTION</i> can be either &quot;off&quot; or &quot;metadata&quot;. (default: off)</p>
<dt><code>timeout=</code><i>TIMEOUT</i></p>
<dd>Numer of seconds to wait for message from failed node. If no message is received within <i>TIMEOUT</i> seconds, the <i>fence_kdump</i> agent returns failure. (default: 60)</dl>
<h2>Actions</h2>
<dl>
<dt><code>off</code></p>
<dd>Listen for message from failed node that acknowledges node has entered kdump crash recovery service. If a valid message is received from the failed node, the node is considered to be fenced and the agent returns success. Failure to receive a valid message from the failed node in the given timeout period results in fencing failure.</p>
<dt><code>metadata</code></p>
<dd>Print XML metadata to standard output.</dl>
<h2>Author</h2>
<p>Ryan O&#8217;Hara &lt;rohara [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence_kdump_send/">fence_kdump_send</a>(8), <a href="/docs/linux/man/8-fenced/">fenced</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
