---
title: "nl-qdisc-list(8)"
name: "nl-qdisc-list"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nl-qdisc-list/"
description: "nl-qdisc-{add|list|delete} – Manage queueing disciplines"
---

<p>nl-qdisc-{add|list|delete} &#8211; Manage queueing disciplines</p>
<h2>Synopsis</h2>
<p><code>nl-qdisc-add &#8211;dev</code> <i>dev</i> <code>&#8211;parent</code> <i>id</i> <code>[OPTIONS]</code> <i>qdisc-type</i> <code>[QDISC]</code> <code>nl-qdisc-delete [ &#8211;interactive ] [OPTIONS]</code> <code>nl-qdisc-list [OPTIONS]</code> </p>
<h2>Description</h2>
<p>The nl-qdisc tools allow to manage and configure queueing disciplines (qdiscs) in the kernel. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd>Print help text to console and exit.</dd>
<dt><code>-v</code> or <code>&#8211;version</code></dt>
<dd>Print versioning information to console and exit.</dd>
<dt><code>-q</code> or <code>&#8211;quiet</code></dt>
<dd>Do not print informal notifications about actions taken to the console. By default a short description of each qdisc added/update/deleted will be printed to the console. This option disables this behaviour.</dd>
<dt><code>-d</code> or <code>&#8211;dev</code>=DEV</dt>
<dd>Network device the qdisc is attached to.</dd>
<dt><code>-p</code> or <code>&#8211;parent</code>=ID</dt>
<dd>Identifier of the parent qdisc/class this qdisc is attached to. The identifier can be specified as classid, name or one of the special values &quot;root&quot; or &quot;ingress&quot;.</dd>
<dt><code>-i</code> or <code>&#8211;id</code>=ID</dt>
<dd>Identifier of qdisc. It can be specified as classid or name. </dd>
</dl>
<h3>nl-qdisc-add Options</h3>
<dl>
<dt><code>&#8211;update</code></dt>
<dd>Update qdisc if it already exists, otherwise attempting to add a qdisc which already exists will result in an error. This does not include changing the type of the qdisc, use &#8211;replace if you wish to do so.</dd>
<dt><code>&#8211;replace</code></dt>
<dd>Replace or update qdisc if it already exists. Same behaviour as &#8211;update but will completely replace the qdisc if it exists already.</dd>
<dt><code>&#8211;update-only</code></dt>
<dd>Update an existing qdisc but do not create it if it does not exist.</dd>
<dt><code>&#8211;replace-only</code></dt>
<dd>Update or replace an existing qdisc but do not create it if it does exist. </dd>
</dl>
<h3>nl-qdisc-delete Options</h3>
<dl>
<dt><code>&#8211;interactive</code></dt>
<dd>The interactive mode requires confirmation by the user for each qdisc deleted. It will print a prompt for each qdisc matching the provided filter and requires the user to answer &#8216;y&#8217;es or &#8216;n&#8217;o.</dd>
<dt><code>&#8211;yes</code></dt>
<dd>Make the default answer for interactive prompts be &#8216;y&#8217;es. This option is also required to delete all qdiscs on all network devices.</dd>
<dt><code>-k</code> or <code>&#8211;kind</code>=TYPE</dt>
<dd>Only delete qdiscs of this type. </dd>
</dl>
<h3>nl-qdisc-list Options</h3>
<dl>
<dt><code>&#8211;details</code></dt>
<dd>Show detailed information for each qdisc listed.</dd>
<dt><code>&#8211;stats</code></dt>
<dd>Show statistics information for each qdisc listed. This option will also turn on detailed information automatically.</dd>
<dt><code>-r</code> or <code>&#8211;recursive</code></dt>
<dd>List all TC objects recurisvely attached to all qdiscs matching the filter.</dd>
<dt><code>-k</code> or <code>&#8211;kind</code>=TYPE</dt>
<dd>Only list qdiscs of this type. </dd>
</dl>
<h2>Usage</h2>
<p>Add a HTB root qdisc with id &quot;5:&quot;: </p>
<dl>
<dd>nl-qdisc-add &#8211;dev eth0 &#8211;parent root &#8211;id 5: htb</dd></dl>
<p> List all qdiscs on eth0 and print statistical data: </p>
<dl>
<dd>nl-qdisc-list &#8211;stats &#8211;dev eth0</dd></dl>
<p> Delete the qdisc &quot;5:&quot;:</p>
<dl>
<dd>nl-qdisc-delete &#8211;id 5:</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nl-classid-lookup/">nl-classid-lookup</a>(8)</code> </p>
<h2>Author</h2>
<p>Thomas Graf is the original author and current maintainer of libnl and libnl tools. Many people have contributed to it since.</p>
