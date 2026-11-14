---
title: "ceph-dencoder(8)"
name: "ceph-dencoder"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph-dencoder/"
description: "ceph-dencoder – ceph encoder/decoder utility"
---

<p>ceph-dencoder &#8211; ceph encoder/decoder utility</p>
<h2>Synopsis</h2>
<pre><code>ceph-dencoder</code> [commands...]</pre>
<h2>Description</h2>
<p><code>ceph-dencoder</code> is a utility to encode, decode, and dump ceph data structures. It is used for debugging and for testing inter-version compatibility. </p>
<p> <code>ceph-dencoder</code> takes a simple list of commands and performs them in order.</p>
<h2>Commands</h2>
<dl>
<dt><code>version</code></p>
<dd>Print the version string for the <code>ceph-dencoder</code> binary.</p>
<dt><code>import &lt;file&gt;</code></p>
<dd>Read a binary blob of encoded data from the given file. It will be placed in an in-memory buffer.</p>
<dt><code>export &lt;file&gt;</code></p>
<dd>Write the contents of the current in-memory buffer to the given file.</p>
<dt><code>list_types</code></p>
<dd>List the data types known to this build of <code>ceph-dencoder</code>.</p>
<dt><code>type &lt;name&gt;</code></p>
<dd>Select the given type for future <code>encode</code> or <code>decode</code> operations.</p>
<dt><code>decode</code></p>
<dd>Decode the contents of the in-memory buffer into an instance of the previously selected type. If there is an error, report it.</p>
<dt><code>encode</code></p>
<dd>Encode the contents of the in-memory instance of the previously selected type to the in-memory buffer.</p>
<dt><code>dump_json</code></p>
<dd>Print a JSON-formatted description of the in-memory object.</p>
<dt><code>count_tests</code></p>
<dd>Print the number of built-in test instances of the previosly selected type that <code>ceph-dencoder</code> is able to generate.</p>
<dt><code>select_test &lt;n&gt;</code></p>
<dd>Select the given build-in test instance as a the in-memory instance of the type.</p>
<dt><code>get_features</code></p>
<dd>Print the decimal value of the feature set supported by this version of <code>ceph-dencoder</code>. Each bit represents a feature. These correspond to CEPH_FEATURE_* defines in src/include/ceph_features.h.</p>
<dt><code>set_features &lt;f&gt;</code></p>
<dd>Set the feature bits provided to <code>encode</code> to <i>f</i>. This allows you to encode objects such that they can be understood by old versions of the software (for those types that support it).</dl>
<h2>Example</h2>
<p>Say you want to examine an attribute on an object stored by <code>ceph-osd</code>. You can do: </p>
<pre>$ cd /mnt/osd.12/current/2.b_head
$ attr -l foo_bar_head_EFE6384B
Attribute &quot;ceph.snapset&quot; has a 31 byte value for foo_bar_head_EFE6384B
Attribute &quot;ceph._&quot; has a 195 byte value for foo_bar_head_EFE6384B
$ attr foo_bar_head_EFE6384B -g ceph._ -q &gt; /tmp/a
$ ceph-dencoder type object_info_t import /tmp/a decode dump_json
{ &quot;oid&quot;: { &quot;oid&quot;: &quot;foo&quot;,
 &quot;key&quot;: &quot;bar&quot;,
 &quot;snapid&quot;: -2,
 &quot;hash&quot;: 4024842315,
 &quot;max&quot;: 0},
 &quot;locator&quot;: { &quot;pool&quot;: 2,
 &quot;preferred&quot;: -1,
 &quot;key&quot;: &quot;bar&quot;},
 &quot;category&quot;: &quot;&quot;,
 &quot;version&quot;: &quot;9'1&quot;,
 &quot;prior_version&quot;: &quot;0'0&quot;,
 &quot;last_reqid&quot;: &quot;client.4116.0:1&quot;,
 &quot;size&quot;: 1681,
 &quot;mtime&quot;: &quot;2012-02-21 08:58:23.666639&quot;,
 &quot;lost&quot;: 0,
 &quot;wrlock_by&quot;: &quot;unknown.0.0:0&quot;,
 &quot;snaps&quot;: [],
 &quot;truncate_seq&quot;: 0,
 &quot;truncate_size&quot;: 0,
 &quot;watchers&quot;: {}}</pre>
<h2>Availability</h2>
<p><code>ceph-dencoder</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
