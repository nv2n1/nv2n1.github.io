---
title: "geostore(8)"
name: "geostore"
section: "8"
letter: "g"
url: "/docs/linux/man/8-geostore/"
description: "geostore – geo cluster attribute manager"
---

<p>geostore &#8211; geo cluster attribute manager</p>
<h2>Synopsis</h2>
<p><code>geostore</code> <i>set</i> [-t <i>ticket</i>] [-s <i>site</i>] [-c <i>config</i>] <i>attribute</i> <i>value</i> </p>
<p> <code>geostore</code> <i>get</i> [-t <i>ticket</i>] [-s <i>site</i>] [-c <i>config</i>] <i>attribute</i> </p>
<p> <code>geostore</code> <i>delete</i> [-t <i>ticket</i>] [-s <i>site</i>] [-c <i>config</i>] <i>attribute</i> </p>
<p> <code>geostore</code> <i>list</i> [-t <i>ticket</i>] [-s <i>site</i>] [-c <i>config</i>]</p>
<h2>Description</h2>
<p>Applications running in GEO cluster environments may need more information apart from tickets to make decisions. One example may be the status of data replication. </p>
<p> <i>geostore</i> is a helper program to manage site attributes. The attributes are defined on a per-ticket basis, that is every ticket may have one or more attributes. </p>
<p> It can set an attribute value, retrieve an attribute, or delete it. The attributes are stored in the CIB status section which is managed by the pacemaker <i>cib</i> process. <i><a href="/docs/linux/man/8-boothd/">boothd</a>(8)</i> provides transport for attributes to other sites. </p>
<p> <i><a href="/docs/linux/man/8-crm_ticket/">crm_ticket</a>(8)</i> is invoked at the target site to manage the attributes.</p>
<h2>Short Examples</h2>
<dl>
<dd>
<pre># geostore set -t ticket-A -s other bigdb-repl-status UPTODATE
# geostore get -t ticket-A -s other bigdb-repl-status
# geostore delete -t ticket-A -s 44.0.0.61 bigdb-repl-status
# geostore list -t ticket-A -s other</pre>
</dl>
<h2>Options</h2>
<p><code>-t</code></p>
<dl>
<dd>Ticket scope of the attribute (required, if more than one ticket is configured).</dl>
<p> <code>-s</code></p>
<dl>
<dd>Site address or name where the attribute is to be stored/retrieved. </p>
<dl>
<dd>
<pre>The special value 'other' can be used to specify the other
site. Obviously, in that case, the booth configuration must
have exactly two sites defined.</pre>
</dl>
</dl>
<p> <code>-c</code> <i>configfile</i></p>
<dl>
<dd>Configuration to use. </p>
<p> Can be a full path to a configuration file, or a short name; in the latter case, the directory <i>/etc/booth</i> and suffix <i>.conf</i> are added. Per default <i>booth</i> is used, which results in the path <i>/etc/booth/booth.conf</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Give a short usage output.</dl>
<h2>Commands</h2>
<p><i>set</i></p>
<dl>
<dd>Sets the attribute to the value.</dl>
<p> <i>get</i></p>
<dl>
<dd>Get the attribute value and print it to <i>stdout</i>. If the attribute doesn&#8217;t exist, appropriate error message is printed to <i>stderr</i>.</dl>
<p> <i>delete</i></p>
<dl>
<dd>Delete the attribute. If the attribute doesn&#8217;t exist, appropriate error message is printed to <i>stderr</i>.</dl>
<p> <i>list</i></p>
<dl>
<dd>List all attributes and their values stored at the site.</dl>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>Success.</dl>
<p> <code>1</code></p>
<dl>
<dd>Request failed or bad usage.</dl>
<h2>Resources</h2>
<p>GitHub: <a rel="nofollow" href="https://github.com/ClusterLabs/booth">https://github.com/ClusterLabs/booth</a></p>
<h2>Copying</h2>
<p>Copyright &#169; 2015 Dejan Muhamedagic &lt;dmuhamedagic [at] suse.com&gt; </p>
<p> Free use of this software is granted under the terms of the GNU General Public License (GPL) as of version 2 (see COPYING file) or later.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-boothd/">boothd</a>(8)</i>, <i><a href="/docs/linux/man/8-crm_attribute/">crm_attribute</a>(8)</i> </p>
