---
title: "rdma-resource(8)"
name: "rdma-resource"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma-resource/"
description: "rdma-resource – rdma resource configuration"
---

<p>rdma-resource &#8211; rdma resource configuration</p>
<h2>Synopsis</h2>
<pre><code>rdma

[ OPTIONS ] RESOURCE { COMMAND |

    help }

RESOURCE := {

    cm_id | cq | mr | pd | qp | ctx | srq }

OPTIONS := {

    -j[son] |
    -d[etails] }</code></pre>
<p> <code>rdma resource show</code> [ <i>DEV/PORT_INDEX</i> ]<br />
 <code>rdma resource help</code> </p>
<h2>Description</h2>
<h3>rdma resource show &#8211; display rdma resource tracking information</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the RDMA link to show. If this argument is omitted all links are listed. </p>
<h2>Examples</h2>
<p>rdma resource show</p>
<dl>
<dd>Shows summary for all devices on the system.</dl>
<p> rdma resource show mlx5_2</p>
<dl>
<dd>Shows the state of specified rdma device.</dl>
<p> rdma res show qp link mlx5_4</p>
<dl>
<dd>Get all QPs for the specific device.</dl>
<p> rdma res show qp link mlx5_4/1</p>
<dl>
<dd>Get QPs of specific port.</dl>
<p> rdma res show qp link mlx5_4/0</p>
<dl>
<dd>Provide illegal port number (0 is illegal).</dl>
<p> rdma res show qp link mlx5_4/-</p>
<dl>
<dd>Get QPs which have not assigned port yet.</dl>
<p> rdma res show qp link mlx5_4/- -d</p>
<dl>
<dd>Detailed view.</dl>
<p> rdma res show qp link mlx5_4/- -dd</p>
<dl>
<dd>Detailed view including driver-specific details.</dl>
<p> rdma res show qp link mlx5_4/1 lqpn 0-6</p>
<dl>
<dd>Limit to specific Local QPNs.</dl>
<p> rdma res show qp link mlx5_4/1 lqpn 6 -r</p>
<dl>
<dd>Driver specific details in raw format.</dl>
<p> rdma resource show cm_id dst-port 7174</p>
<dl>
<dd>Show CM_IDs with destination ip port of 7174.</dl>
<p> rdma resource show cm_id src-addr 172.16.0.100</p>
<dl>
<dd>Show CM_IDs bound to local ip address 172.16.0.100</dl>
<p> rdma resource show cq pid 30489</p>
<dl>
<dd>Show CQs belonging to pid 30489</dl>
<p> rdma resource show ctx ctxn 1</p>
<dl>
<dd>Show contexts that have index equal to 1.</dl>
<p> rdma resource show srq lqpn 5-7</p>
<dl>
<dd>Show SRQs that the QPs with lqpn 5-7 are associated with.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rdma/">rdma</a></code>(8), <code><a href="/docs/linux/man/8-rdma-dev/">rdma-dev</a></code>(8), <code><a href="/docs/linux/man/8-rdma-link/">rdma-link</a></code>(8), <code><a href="/docs/linux/man/8-rdma-statistic/">rdma-statistic</a></code>(8), </p>
<h2>Author</h2>
<p>Leon Romanovsky &lt;leonro [at] mellanox.com&gt;</p>
