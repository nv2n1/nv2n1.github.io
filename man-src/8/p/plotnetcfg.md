---
title: "plotnetcfg(8)"
name: "plotnetcfg"
section: "8"
letter: "p"
url: "/docs/linux/man/8-plotnetcfg/"
description: "plotnetcfg – plot diagram of network configuration"
---

<p>plotnetcfg &#8211; plot diagram of network configuration</p>
<h2>Synopsis</h2>
<p><code>plotnetcfg</code> [<code>options</code>]</p>
<h2>Description</h2>
<p><code>plotnetcfg</code> is a tool that scans networking configuration on the machine and outputs a diagram of the configuration hierarchy. By default, the output is in the <code>dot</code> language. The output can be converted by the <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1) tool from <code><a href="/docs/linux/man/7-graphviz/">graphviz</a></code>(7) package to various formats such as PDF, PostScript or SVG. <code>plotnetcfg</code> is able to scan different network name spaces and figure out relations that span name spaces. It supports all kinds of network interfaces and understands specifics of VLANs, bridges, veth pairs and Open vSwitch. The tool has to be run under root or with both CAP_SYS_ADMIN and CAP_NET_ADMIN capabilities. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) for details. <code>plotnetcfg</code> is lightweight with as few library dependencies as possible. Currently, the only dependencies are <code>libc</code> and <code>libjansson</code>. Optionally, it can be statically linked against the latter which allows the <code>plotnetcfg</code> binary to be copied to a target machine and run there (provided it has the same or newer version of <code>glibc</code> as <code>plotnetcfg</code> was compiled against). See EXAMPLES for typical <code>plotnetcfg</code> usage. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>FORMAT</i></p>
<dd>Set output format. When not specified, <code>dot</code> is used.</p>
<dt><code>-F</code>, <code>&#8211;list-formats</code></p>
<dd>Print available output formats.</p>
<dt><code>-D</code>, <code>&#8211;ovs-db</code>=<i>PATH</i></p>
<dd>Path to the socket used to communicate with Open vSwitch database server. Only UNIX sockets are supported. The default is <code>/var/run/openvswitch/db.sock</code>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print short help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Print program version and exit. </p>
</dl>
<h2>Examples</h2>
<p>Display network configuration of the local machine:</p>
<dl>
<dd><code>plotnetcfg | dot -Tpdf | okular &#8211;</code></dl>
<p> Save network configuration to a file for later analysis:</p>
<dl>
<dd><code>plotnetcfg &gt;</code> <i>file</i></dl>
<p> Create PDF with network configuration of a remote machine:</p>
<dl>
<dd><code>scp /usr/sbin/plotnetcfg</code> <code>root@</code><i>target</i><code>:</code><br />
 <code>ssh</code> <code>root@</code><i>target</i> <code>./plotnetcfg | dot -Tpdf &gt;</code> <i>file.pdf</i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), <code><a href="/docs/linux/man/7-graphviz/">graphviz</a></code>(7), <code><a href="/docs/linux/man/5-plotnetcfg-json/">plotnetcfg-json</a></code>(5) </p>
<h2>Author</h2>
<p><code>plotnetcfg</code> was written and is maintained by Jiri Benc &lt;jbenc [at] redhat.com&gt;.</p>
