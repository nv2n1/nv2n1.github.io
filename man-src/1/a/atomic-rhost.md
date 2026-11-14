---
title: "atomic-rhost(1)"
name: "atomic-rhost"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-rhost/"
description: "atomic-rhost – Manage cluster hosts"
---

<h2 class="name">NAME</h2>
<p> atomic-rhost &#8211; Manage cluster hosts </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic rhost [OPTIONS] SUBCOMMAND</code> </p>
<p> <code>atomic rhost</code> will issue commands to a Commissaire server over HTTP. </p>
<p> Commissaire allows administrators of a Kubernetes, Atomic Enterprise or OpenShift installation to perform administrative tasks without the need to write custom scripts or manually intervene on systems. </p>
<h2>NOTE</h2>
<p> The rhost subcommand is only available when commctl is installed. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>-help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement. </p>
<h2>SUBCOMMANDS</h2>
<p> <code>create</code> [<code>-c</code>/<code>&#8211;cluster</code> CLUSTER_NAME] IP_ADDRESS SSH_PRIV_KEY<br />
&nbsp;<wbr>&nbsp;<wbr>Register a new host with the specified IP address.&nbsp;<wbr>&nbsp;<wbr>SSH_PRIV_KEY is a file path to the host&#8217;s private SSH key&nbsp;<wbr>(e.g. id_rsa), used to drive operations on the host.&nbsp;<wbr>&nbsp;<wbr>Use&nbsp;<wbr><code>&#8211;cluster</code>&nbsp;<wbr>to add the host to an existing cluster. </p>
<p> <code>delete</code> IP_ADDRESS<br />
&nbsp;<wbr>&nbsp;<wbr>Unregister the specified IP address and, if applicable, disassociate it from its cluster. </p>
<p> <code>get</code> IP_ADDRESS<br />
&nbsp;<wbr>&nbsp;<wbr>Report status of the host with the specified IP address. </p>
<p> <code>list</code><br />
&nbsp;<wbr>&nbsp;<wbr>List all available hosts by IP address. </p>
<h2>HISTORY</h2>
<p> Initial revision by Matthew Barnes (mbarnes at redhat dot com) May 2016 </p>
<h2>Index</h2>
