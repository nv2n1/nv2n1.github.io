---
title: "euca-add-group(1)"
name: "euca-add-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-add-group/"
description: "euca-add-group – Eucalyptus tool: Creates a new security group."
---

<h2>NAME</h2>
<p> euca-add-group &#8211; Eucalyptus tool: Creates a new security group.</p>
<h2>DESCRIPTION</h2>
<p> Creates a new security group. </p>
<p> euca-add-group <code>-d</code>, <code>&#8211;description</code> group_description [-h, <code>&#8211;help]</code> [&#8211;version] [&#8211;debug] group_name </p>
<p> REQUIRED PARAMETERS </p>
<p> <code>-d</code>, <code>&#8211;description</code> Description for the group to be created. </p>
<p> OPTIONAL PARAMETERS </p>
<p> <code>-a</code>, <code>&#8211;access-key</code> User&#8217;s Access Key ID. </p>
<p> <code>-s</code>, <code>&#8211;secret-key</code> User&#8217;s Secret Key. </p>
<p> <code>-U</code>, <code>&#8211;url</code> URL of the Cloud to connect to. </p>
<p> <code>&#8211;config</code> Read credentials and cloud settings from the</p>
<dl>
<dt>
<dd> specified config file (defaults to $HOME/.eucarc or /etc/euca2ools/eucarc).</dl>
<p> <code>-h</code>, <code>&#8211;help</code> Display this help message. </p>
<p> <code>&#8211;version</code> Display the version of this tool. </p>
<p> <code>&#8211;debug</code> Turn on debugging. </p>
<p> Euca2ools will use the environment variables EC2_URL, EC2_ACCESS_KEY, EC2_SECRET_KEY, EC2_CERT, EC2_PRIVATE_KEY, S3_URL, EUCALYPTUS_CERT by default. </p>
<h2>Index</h2>
