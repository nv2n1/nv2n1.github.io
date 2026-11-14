---
title: "ipa-csreplica-manage(1)"
name: "ipa-csreplica-manage"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-csreplica-manage/"
description: "ipa-csreplica-manage – Manage an IPA CS replica"
---

<h2>NAME</h2>
<p> ipa-csreplica-manage &#8211; Manage an IPA CS replica</p>
<h2>SYNOPSIS</h2>
<p> ipa-csreplica-manage [<i>OPTION</i>]&#8230; [connect|disconnect|del|list|re-initialize|force-sync]</p>
<h2>DESCRIPTION</h2>
<p> Manages the CA replication agreements of an IPA server for domain at domain level 0. </p>
<p> To manage CA replication agreements in a domain at domain level 1, use IPA CLI or Web UI, see `ipa help topology` for additional information. </p>
<dl>
<dt><code>connect</code> [SERVER_A] &lt;SERVER_B&gt;</p>
<dd> &#8211; Adds a new replication agreement between SERVER_A/localhost and SERVER_B. Applicable only at domain level 0.</p>
<dt><code>disconnect</code> [SERVER_A] &lt;SERVER_B&gt;</p>
<dd> &#8211; Removes a replication agreement between SERVER_A/localhost and SERVER_B. Applicable only at domain level 0.</p>
<dt><code>del</code> &lt;SERVER&gt;</p>
<dd> &#8211; Removes all replication agreements and data about SERVER. Applicable only at domain level 0. </p>
<dt><code>list</code> [SERVER]</p>
<dd> &#8211; Lists all the servers or the list of agreements of SERVER</p>
<dt><code>re-initialize</code></p>
<dd> &#8211; Forces a full re-initialization of the IPA CA server retrieving data from the server specified with the &#8211;from option</p>
<dt><code>force-sync</code></p>
<dd> &#8211; Immediately flush any data to be replicated from a server specified with the &#8211;from option</p>
<dt><code>set-renewal-master</code> [SERVER]</p>
<dd> &#8211; Set CA server which handles renewal of CA subsystem certificates to SERVER</p>
<dt>The connect and disconnect options are used to manage the replication topology. When a replica is created it is only connected with the master that created it. The connect option may be used to connect it to other existing replicas.</p>
<dd>
<dt>The disconnect option cannot be used to remove the last link of a replica. To remove a replica from the topology use the del option.</p>
<dd>
<dt>If a replica is deleted and then re-added within a short time-frame then the 389-ds instance on the master that created it should be restarted before re-installing the replica. The master will have the old service principals cached which will cause replication to fail.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code> <i>HOST</i>, <code>&#8211;host</code>=<i>HOST</i></p>
<dd> The IPA server to manage. The default is the machine on which the command is run Not honoured by the re-initialize command.</p>
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;password</code>=<i>DM_PASSWORD</i></p>
<dd> The Directory Manager password to use for authentication</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Provide additional information</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Ignore some types of errors</p>
<dt><code>&#8211;from</code>=<i>SERVER</i></p>
<dd> The server to pull the data from, used by the re-initialize and force-sync commands.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>List a server&#8217;s replication agreements.</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-csreplica-manage list srv1.example.com<br />
&nbsp;<wbr>srv2.example.com<br />
&nbsp;<wbr>srv3.example.com</p>
<dt>Re-initialize a replica:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-csreplica-manage re-initialize &#8211;from srv2.example.com </p>
<p> This will re-initialize the data on the server where you execute the command, retrieving the data from the srv2.example.com replica</p>
<dt>Add a new replication agreement:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-csreplica-manage connect srv2.example.com srv4.example.com</p>
<dt>Remove an existing replication agreement:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-csreplica-manage disconnect srv1.example.com srv3.example.com</p>
<dt>Completely remove a replica at domain level 0:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-csreplica-manage del srv4.example.com</p>
<dt>Completely remove a replica at domain level 1:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage del srv4.example.com</p>
<dt>Using connect/disconnect you can manage the replication topology.</p>
<dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful</p>
<dl>
<dt>1 if an error occurred</p>
<dd>
</dl>
<h2>Index</h2>
