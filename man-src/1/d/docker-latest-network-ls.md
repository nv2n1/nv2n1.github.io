---
title: "docker-latest-network-ls(1)"
name: "docker-latest-network-ls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-network-ls/"
description: "docker-network-ls – list networks"
---

<h2 class="name">NAME</h2>
<p> docker-network-ls &#8211; list networks </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network ls</code> [<code>-f</code>|<code>&#8211;filter</code>[=<i>[]</i>]] [<code>&#8211;no-trunc</code>[=<i>true</i>|<i>false</i>]] [<code>-q</code>|<code>&#8211;quiet</code>[=<i>true</i>|<i>false</i>]] [<code>&#8211;help</code>] </p>
<h2>DESCRIPTION</h2>
<p> Lists all the networks the Engine daemon knows about. This includes the networks that span across multiple hosts in a cluster, for example: </p>
<dl>
<dt>
<dd>
<pre>
    $ docker network ls
    NETWORK ID          NAME                DRIVER
    7fca4eb8c647        bridge              bridge
    9f904ee27bf5        none                null
    cf03ee007fb4        host                host
    78b03ee04fc4        multi-host          overlay
</pre>
</dl>
<p> Use the &#8211;no-trunc option to display the full network id: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --no-trunc
NETWORK ID                                                         NAME                DRIVER
18a2866682b85619a026c81b98a5e375bd33e1b0936a26cc497c283d27bae9b3   none                null                
c288470c46f6c8949c5f7e5099b5b7947b07eabe8d9a27d79a9cbf111adcbf47   host                host                
7b369448dccbf865d397c8d2be0cda7cf7edc6b0945f77d2529912ae917a0185   bridge              bridge              
95e74588f40db048e86320c6526440c504650a1ff3e9f7d60a497c4d2163e5bd   foo                 bridge    
63d1ff1f77b07ca51070a8c227e962238358bd310bde1529cf62e6c307ade161   dev                 bridge
</pre>
</dl>
<h2>Filtering</h2>
<p> The filtering flag (-f or &#8211;filter) format is a key=value pair. If there is more than one filter, then pass multiple flags (e.g. &#8211;filter &quot;foo=bar&quot; &#8211;filter &quot;bif=baz&quot;). Multiple filter flags are combined as an OR filter. For example, -f type=custom -f type=builtin returns both custom and builtin networks. </p>
<p> The currently supported filters are:</p>
<dl>
<dt>step]</p>
<dd>
<p> item driver item id (network&#8217;s id) item label (label=&lt;key&gt; or label=&lt;key&gt;=&lt;value&gt;) item name (network&#8217;s name) item type (custom|builtin)</dl>
<h3>Driver</h3>
<p> The driver filter matches networks based on their driver. </p>
<p> The following example matches networks with the bridge driver: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --filter driver=bridge
NETWORK ID          NAME                DRIVER
db9db329f835        test1               bridge
f6e212da9dfd        test2               bridge
</pre>
</dl>
<h3>ID</h3>
<p> The id filter matches on all or part of a network&#8217;s ID. </p>
<p> The following filter matches all networks with an ID containing the 63d1ff1f77b0&#8230; string. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --filter id=63d1ff1f77b07ca51070a8c227e962238358bd310bde1529cf62e6c307ade161
NETWORK ID          NAME                DRIVER
63d1ff1f77b0        dev                 bridge
</pre>
</dl>
<p> You can also filter for a substring in an ID as this shows: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --filter id=95e74588f40d
NETWORK ID          NAME                DRIVER
95e74588f40d        foo                 bridge
$ docker network ls --filter id=95e
NETWORK ID          NAME                DRIVER
95e74588f40d        foo                 bridge
</pre>
</dl>
<h3>Label</h3>
<p> The label filter matches networks based on the presence of a label alone or a label and a value. </p>
<p> The following filter matches networks with the usage label regardless of its value. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls -f &quot;label=usage&quot;
NETWORK ID          NAME                DRIVER
db9db329f835        test1               bridge              
f6e212da9dfd        test2               bridge
</pre>
</dl>
<p> The following filter matches networks with the usage label with the prod value. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls -f &quot;label=usage=prod&quot;
NETWORK ID          NAME                DRIVER
f6e212da9dfd        test2               bridge
</pre>
</dl>
<h3>Name</h3>
<p> The name filter matches on all or part of a network&#8217;s name. </p>
<p> The following filter matches all networks with a name containing the foobar string. </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --filter name=foobar
NETWORK ID          NAME                DRIVER
06e7eef0a170        foobar              bridge
</pre>
</dl>
<p> You can also filter for a substring in a name as this shows: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --filter name=foo
NETWORK ID          NAME                DRIVER
95e74588f40d        foo                 bridge
06e7eef0a170        foobar              bridge
</pre>
</dl>
<h3>Type</h3>
<p> The type filter supports two values; builtin displays predefined networks (bridge, none, host), whereas custom displays user defined networks. </p>
<p> The following filter matches all user defined networks: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network ls --filter type=custom
NETWORK ID          NAME                DRIVER
95e74588f40d        foo                 bridge
63d1ff1f77b0        dev                 bridge
</pre>
</dl>
<p> By having this flag it allows for batch cleanup. For example, use this filter to delete all user defined networks: </p>
<dl>
<dt>
<dd>
<pre>
$ docker network rm `docker network ls --filter type=custom -q`
</pre>
</dl>
<p> A warning will be issued when trying to remove a network that has containers attached. </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;filter</code>=<i>[]</i><br />
&nbsp;<wbr>&nbsp;<wbr>filter output based on conditions provided. </p>
<p> <code>&#8211;no-trunc</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Do not truncate the output </p>
<p> <code>-q</code>, <code>&#8211;quiet</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Only display network IDs </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>HISTORY</h2>
<p> OCT 2015, created by Mary Anthony &lt;mary [at] docker.com&gt; </p>
<h2>Index</h2>
