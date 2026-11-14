---
title: "atomic-cluster(1)"
name: "atomic-cluster"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-cluster/"
description: "atomic-cluster – Manage cluster hosts"
---

<h2 class="name">NAME</h2>
<p> atomic-cluster &#8211; Manage cluster hosts </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic cluster [OPTIONS] SUBCOMMAND</code> </p>
<p> <code>atomic cluster</code> will issue commands to a Commissaire server over HTTP. </p>
<p> Commissaire allows administrators of a Kubernetes, Atomic Enterprise or OpenShift installation to perform administrative tasks without the need to write custom scripts or manually intervene on systems. </p>
<h2>NOTE</h2>
<p> The cluster subcommand is only available when commctl is installed. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>-help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement. </p>
<h2>SUBCOMMANDS</h2>
<p> <code>create</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Register a new cluster with the specified name. </p>
<p> <code>delete</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Unregister the specified cluster and disassociate all of its hosts. </p>
<p> <code>get</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Report status of the specified cluster. </p>
<p> <code>list</code><br />
&nbsp;<wbr>&nbsp;<wbr>List all available clusters by name. </p>
<p> <code>deploy start</code> CLUSTER_NAME VERSION<br />
&nbsp;<wbr>&nbsp;<wbr>Initiate deployment of a tree image with a version tag matching VERSION on all hosts associated with the specified cluster. </p>
<p> <code>deploy status</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Report status of a deployment operation on the specified cluster. </p>
<p> <code>restart start</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Initiate a restart of all hosts associated with the specified cluster. </p>
<p> <code>restart status</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Report status of a restart operation on the specified cluster. </p>
<p> <code>upgrade start</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Initiate an upgrade of all hosts associated with the specified cluster. </p>
<p> <code>upgrade status</code> CLUSTER_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>Report status of an upgrade operation on the specified cluster. </p>
<h2>HISTORY</h2>
<p> Initial revision by Matthew Barnes (mbarnes at redhat dot com) May 2016 </p>
<h2>Index</h2>
