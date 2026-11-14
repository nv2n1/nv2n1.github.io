---
title: "corosync-keygen(8)"
name: "corosync-keygen"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-keygen/"
description: "corosync-keygen – Generate an authentication key for Corosync."
---

<p>corosync-keygen &#8211; Generate an authentication key for Corosync.</p>
<h2>Synopsis</h2>
<p><code>corosync-keygen [-k &lt;filename&gt;] [-l]</code></p>
<h2>Description</h2>
<p>If you want to configure corosync to use cryptographic techniques to ensure authenticity and privacy of the messages, you will need to generate a private key. </p>
<p> <code>corosync-keygen</code> creates this key and writes it to /etc/corosync/authkey or to file specified by -k option. </p>
<p> This private key must be copied to every processor in the cluster. If the private key isn&#8217;t the same for every node, those nodes with nonmatching private keys will not be able to join the same configuration. </p>
<p> Copy the key to some security transportable storage or use ssh to transmit the key from node to node. Then install the key with the command: </p>
<p> unix#: install -D &#8211;group=0 &#8211;owner=0 &#8211;mode=0400 /path_to_authkey/authkey /etc/corosync/authkey </p>
<p> If a message &quot;Invalid digest&quot; appears from the corosync executive, the keys are not consistent between processors. </p>
<p> <code>Note: corosync-keygen</code> will ask for user input to assist in generating entropy unless the -l option is used.</p>
<h2>Options</h2>
<dl>
<dt><code>-k &lt;filename&gt;</code></p>
<dd>This specifies the fully qualified path to the shared key to create.<br />
 The default is /etc/corosync/authkey.</p>
<dt><code>-l</code></p>
<dd>Use a less secure random data source that will not require user input to help generate entropy. This may be useful when this utility is used from a script or hardware random number generator is not available (f.e. in virtual machine). </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>Generate the key.</p>
<dd></dl>
<p> # corosync-keygen<br />
 Corosync Cluster Engine Authentication key generator.<br />
 Gathering 1024 bits for key from /dev/random.<br />
 Press keys on your keyboard to generate entropy. </p>
<p> $ corosync-keygen -l -k /tmp/authkey<br />
 Corosync Cluster Engine Authentication key generator.<br />
 Writing corosync key to /tmp/authkey.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
