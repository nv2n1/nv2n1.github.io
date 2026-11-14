---
title: "ceph-conf(8)"
name: "ceph-conf"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph-conf/"
description: "ceph-conf – ceph conf file tool"
---

<p>ceph-conf &#8211; ceph conf file tool</p>
<h2>Synopsis</h2>
<pre><code>ceph-conf</code> -c <i>conffile</i> --list-all-sections
<code>ceph-conf</code> -c <i>conffile</i> -L
<code>ceph-conf</code> -c <i>conffile</i> -l <i>prefix</i>
<code>ceph-conf</code> <i>key</i> -s <i>section1</i> ...
<code>ceph-conf</code> [-s <i>section</i> ] --lookup <i>key</i>
<code>ceph-conf</code> [-s <i>section</i> ] <i>key</i></pre>
<h2>Description</h2>
<p><code>ceph-conf</code> is a utility for getting information about a ceph configuration file. As with most Ceph programs, you can specify which Ceph configuration file to use with the <code>-c</code> flag.</p>
<h2>Actions</h2>
<p><code>ceph-conf</code> will perform one of the following actions: </p>
<p> &#8211;list-all-sections or -L prints out a list of all the section names in the configuration file. </p>
<p> &#8211;list-sections or -l prints out a list of all the sections that begin with a given prefix. For example, &#8211;list-sections mon would list all sections beginning with mon. </p>
<p> &#8211;lookup will search the configuration for a given value. By default, the sections that are searched are determined by the Ceph name that we are using. The Ceph name defaults to client.admin. It can be specified with &#8211;name. </p>
<p> For example, if we specify &#8211;name osd.0, the following sections will be searched: [osd.0], [osd], [global] </p>
<p> You can specify additional sections to search with &#8211;section or -s. These additional sections will be searched before the sections that would normally be searched. As always, the first matching entry we find will be returned. </p>
<p> Note: &#8211;lookup is the default action. If no other actions are given on the command line, we will default to doing a lookup.</p>
<h2>Examples</h2>
<p>To find out what value osd 0 will use for the &quot;osd data&quot; option: </p>
<pre>ceph-conf -c foo.conf --name osd.0 --lookup &quot;osd data&quot;</pre>
<p>To find out what value will mds a use for the &quot;log file&quot; option: </p>
<pre>ceph-conf -c foo.conf --name mds.a &quot;log file&quot;</pre>
<p>To list all sections that begin with osd: </p>
<pre>ceph-conf -c foo.conf -l osd</pre>
<p>To list all sections: </p>
<pre>ceph-conf -c foo.conf -L</pre>
<h2>Availability</h2>
<p><code>ceph-conf</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8),</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
