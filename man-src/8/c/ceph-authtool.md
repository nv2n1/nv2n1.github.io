---
title: "ceph-authtool(8)"
name: "ceph-authtool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph-authtool/"
description: "ceph-authtool – ceph keyring manipulation tool"
---

<p>ceph-authtool &#8211; ceph keyring manipulation tool</p>
<h2>Synopsis</h2>
<pre><code>ceph-authtool</code> <i>keyringfile</i> [ -l | --list ] [ -C | --create-keyring
] [ -p | --print ] [ -n | --name <i>entityname</i> ] [ --gen-key ] [ -a |
--add-key <i>base64_key</i> ] [ --caps <i>capfile</i> ]</pre>
<h2>Description</h2>
<p><code>ceph-authtool</code> is a utility to create, view, and modify a Ceph keyring file. A keyring file stores one or more Ceph authentication keys and possibly an associated capability specification. Each key is associated with an entity name, of the form <code>{client,mon,mds,osd}.name</code>. </p>
<p> <code>WARNING</code> Ceph provides authentication and protection against man-in-the-middle attacks once secret keys are in place. However, data over the wire is not encrypted, which may include the messages used to configure said keys. The system is primarily intended to be used in trusted environments.</p>
<h2>Options</h2>
<dl>
<dt><code>-l, &#8211;list</code></p>
<dd>will list all keys and capabilities present in the keyring</p>
<dt><code>-p, &#8211;print</code></p>
<dd>will print an encoded key for the specified entityname. This is suitable for the <code>mount -o secret=</code> argument</p>
<dt><code>-C, &#8211;create-keyring</code></p>
<dd>will create a new keyring, overwriting any existing keyringfile</p>
<dt><code>&#8211;gen-key</code></p>
<dd>will generate a new secret key for the specified entityname</p>
<dt><code>&#8211;add-key</code></p>
<dd>will add an encoded key to the keyring</p>
<dt><code>&#8211;cap subsystem capability</code></p>
<dd>will set the capability for given subsystem</p>
<dt><code>&#8211;caps capsfile</code></p>
<dd>will set all of capabilities associated with a given key, for all subsystems</dl>
<h2>Capabilities</h2>
<p>The subsystem is the name of a Ceph subsystem: <code>mon</code>, <code>mds</code>, or <code>osd</code>. </p>
<p> The capability is a string describing what the given user is allowed to do. This takes the form of a comma separated list of allow clauses with a permission specifier containing one or more of rwx for read, write, and execute permission. The <code>allow *</code> grants full superuser permissions for the given subsystem. </p>
<p> For example: </p>
<pre># can read, write, and execute objects
osd = &quot;allow rwx&quot;
# can access mds server
mds = &quot;allow&quot;
# can modify cluster state (i.e., is a server daemon)
mon = &quot;allow rwx&quot;</pre>
<p>A librados user restricted to a single pool might look like: </p>
<pre>mon = &quot;allow r&quot;
osd = &quot;allow rw pool foo&quot;</pre>
<p>A client using rbd with read access to one pool and read/write access to another: </p>
<pre>mon = &quot;allow r&quot;
osd = &quot;allow class-read object_prefix rbd_children, allow pool templates r class-read, allow pool vms rwx&quot;</pre>
<p>A client mounting the file system with minimal permissions would need caps like: </p>
<pre>mds = &quot;allow&quot;
osd = &quot;allow rw pool data&quot;
mon = &quot;allow r&quot;</pre>
<h2>Osd Capabilities</h2>
<p>In general, an osd capability follows the grammar: </p>
<pre>osdcap := grant[,grant...]
grant := allow (match capspec | capspec match)
match := [pool[=]&lt;poolname&gt; | object_prefix &lt;prefix&gt;]
capspec := * | [r][w][x] [class-read] [class-write]</pre>
<p>The capspec determines what kind of operations the entity can perform: </p>
<pre>r = read access to objects
w = write access to objects
x = can call any class method (same as class-read class-write)
class-read = can call class methods that are reads
class-write = can call class methods that are writes
* = equivalent to rwx, plus the ability to run osd admin commands,
 i.e. ceph osd tell ...</pre>
<p>The match criteria restrict a grant based on the pool being accessed. Grants are additive if the client fulfills the match condition. For example, if a client has the osd capabilities: &quot;allow r object_prefix prefix, allow w pool foo, allow x pool bar&quot;, then it has rw access to pool foo, rx access to pool bar, and r access to objects whose names begin with &#8216;prefix&#8217; in any pool.</p>
<h2>Caps File Format</h2>
<p>The caps file format consists of zero or more key/value pairs, one per line. The key and value are separated by an <code>=</code>, and the value must be quoted (with <code>&#8216;</code> or <code>&quot;</code>) if it contains any whitespace. The key is the name of the Ceph subsystem (<code>osd</code>, <code>mds</code>, <code>mon</code>), and the value is the capability string (see above).</p>
<h2>Example</h2>
<p>To create a new keyring containing a key for client.foo: </p>
<pre>ceph-authtool -C -n client.foo --gen-key keyring</pre>
<p>To associate some capabilities with the key (namely, the ability to mount a Ceph filesystem): </p>
<pre>ceph-authtool -n client.foo --cap mds 'allow' --cap osd 'allow rw pool=data' --cap mon 'allow r' keyring</pre>
<p>To display the contents of the keyring: </p>
<pre>ceph-authtool -l keyring</pre>
<p>When mounting a Ceph file system, you can grab the appropriately encoded secret key with: </p>
<pre>mount -t ceph serverhost:/ mountpoint -o name=foo,secret=`ceph-authtool -p -n client.foo keyring`</pre>
<h2>Availability</h2>
<p><code>ceph-authtool</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
