---
title: "nl-qdisc-delete(8)"
name: "nl-qdisc-delete"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nl-qdisc-delete/"
description: "nl-qdisc-{add|list|delete} – Manage queueing disciplines"
---

<p>nl-qdisc-{add|list|delete} &#8211; Manage queueing disciplines</p>
<h2>Synopsis</h2>
<p><code>nl-qdisc-add &#8211;dev</code> <i>dev</i> <code>&#8211;parent</code> <i>id</i> <code>[OPTIONS]</code> <i>qdisc-type</i> <code>[QDISC]</code> <code>nl-qdisc-delete [ &#8211;interactive ] [OPTIONS]</code> <code>nl-qdisc-list [OPTIONS]</code> </p>
<h2>Description</h2>
<p>The nl-qdisc tools allow to manage and configure queueing disciplines (qdiscs) in the kernel. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Print help text to console and exit.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd>Print versioning information to console and exit.</p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd>Do not print informal notifications about actions taken to the console. By default a short description of each qdisc added/update/deleted will be printed to the console. This option disables this behaviour.</p>
<dt><code>-d</code> or <code>&#8211;dev</code>=DEV</p>
<dd>Network device the qdisc is attached to.</p>
<dt><code>-p</code> or <code>&#8211;parent</code>=ID</p>
<dd>Identifier of the parent qdisc/class this qdisc is attached to. The identifier can be specified as classid, name or one of the special values &quot;root&quot; or &quot;ingress&quot;.</p>
<dt><code>-i</code> or <code>&#8211;id</code>=ID</p>
<dd>Identifier of qdisc. It can be specified as classid or name. </p>
</dl>
<h3>nl-qdisc-add Options</h3>
<dl>
<dt><code>&#8211;update</code></p>
<dd>Update qdisc if it already exists, otherwise attempting to add a qdisc which already exists will result in an error. This does not include changing the type of the qdisc, use &#8211;replace if you wish to do so.</p>
<dt><code>&#8211;replace</code></p>
<dd>Replace or update qdisc if it already exists. Same behaviour as &#8211;update but will completely replace the qdisc if it exists already.</p>
<dt><code>&#8211;update-only</code></p>
<dd>Update an existing qdisc but do not create it if it does not exist.</p>
<dt><code>&#8211;replace-only</code></p>
<dd>Update or replace an existing qdisc but do not create it if it does exist. </p>
</dl>
<h3>nl-qdisc-delete Options</h3>
<dl>
<dt><code>&#8211;interactive</code></p>
<dd>The interactive mode requires confirmation by the user for each qdisc deleted. It will print a prompt for each qdisc matching the provided filter and requires the user to answer &#8216;y&#8217;es or &#8216;n&#8217;o.</p>
<dt><code>&#8211;yes</code></p>
<dd>Make the default answer for interactive prompts be &#8216;y&#8217;es. This option is also required to delete all qdiscs on all network devices.</p>
<dt><code>-k</code> or <code>&#8211;kind</code>=TYPE</p>
<dd>Only delete qdiscs of this type. </p>
</dl>
<h3>nl-qdisc-list Options</h3>
<dl>
<dt><code>&#8211;details</code></p>
<dd>Show detailed information for each qdisc listed.</p>
<dt><code>&#8211;stats</code></p>
<dd>Show statistics information for each qdisc listed. This option will also turn on detailed information automatically.</p>
<dt><code>-r</code> or <code>&#8211;recursive</code></p>
<dd>List all TC objects recurisvely attached to all qdiscs matching the filter.</p>
<dt><code>-k</code> or <code>&#8211;kind</code>=TYPE</p>
<dd>Only list qdiscs of this type. </p>
</dl>
<h2>Usage</h2>
<p>Add a HTB root qdisc with id &quot;5:&quot;: </p>
<dl>
<dd>nl-qdisc-add &#8211;dev eth0 &#8211;parent root &#8211;id 5: htb</dl>
<p> List all qdiscs on eth0 and print statistical data: </p>
<dl>
<dd>nl-qdisc-list &#8211;stats &#8211;dev eth0</dl>
<p> Delete the qdisc &quot;5:&quot;:</p>
<dl>
<dd>nl-qdisc-delete &#8211;id 5:</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nl-classid-lookup/">nl-classid-lookup</a>(8)</code> </p>
<h2>Author</h2>
<p>Thomas Graf is the original author and current maintainer of libnl and libnl tools. Many people have contributed to it since.</p>
