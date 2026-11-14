---
title: "runc-update(8)"
name: "runc-update"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-update/"
description: "runc-update – update running container resource constraints"
---

<p><code>runc-update</code> &#8211; update running container resource constraints </p>
<h2>Synopsis</h2>
<p><code>runc update</code> [<i>option</i> &#8230;] <i>container-id</i> <code>runc update</code> <code>-r</code> <i>resources.json</i>|<code>&#8211;</code> <i>container-id</i> </p>
<h2>Description</h2>
<p>The <code>update</code> command change the resource constraints of a running container instance. The resources can be set using options, or, if <code>-r</code> is used, parsed from JSON provided as a file or from stdin. In case <code>-r</code> is used, the JSON format is like this: </p>
<pre><code>
{
    &quot;memory&quot;: {
        &quot;limit&quot;: 0,
        &quot;reservation&quot;: 0,
        &quot;swap&quot;: 0,
        &quot;kernel&quot;: 0,
        &quot;kernelTCP&quot;: 0
    },
    &quot;cpu&quot;: {
        &quot;shares&quot;: 0,
        &quot;quota&quot;: 0,
        &quot;period&quot;: 0,
        &quot;realtimeRuntime&quot;: 0,
        &quot;realtimePeriod&quot;: 0,
        &quot;cpus&quot;: &quot;&quot;,
        &quot;mems&quot;: &quot;&quot;
    },
    &quot;blockIO&quot;: {
        &quot;blkioWeight&quot;: 0
    }
}

</code></pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;resources</code>|<code>-r</code> <i>resources.json</i></p>
<dd>Read the new resource limtis from <i>resources.json</i>. Use <code>&#8211;</code> to read from stdin. If this option is used, all other options are ignored. </p>
<dt><code>&#8211;blkio-weight</code> <i>weight</i></p>
<dd>Set a new io weight. </p>
<dt><code>&#8211;cpu-period</code> <i>num</i></p>
<dd>Set CPU CFS period to be used for hardcapping (in microseconds) </p>
<dt><code>&#8211;cpu-quota</code> <i>num</i></p>
<dd>Set CPU usage limit within a given period (in microseconds). </p>
<dt><code>&#8211;cpu-rt-period</code> <i>num</i></p>
<dd>Set CPU realtime period to be used for hardcapping (in microseconds). </p>
<dt><code>&#8211;cpu-rt-runtime</code> <i>num</i></p>
<dd>Set CPU realtime hardcap limit (in usecs). Allowed cpu time in a given period. </p>
<dt><code>&#8211;cpu-share</code> <i>num</i></p>
<dd>Set CPU shares (relative weight vs. other containers). </p>
<dt><code>&#8211;cpuset-cpus</code> <i>list</i></p>
<dd>Set CPU(s) to use. The <i>list</i> can contain commas and ranges. For example: <code>0-3,7</code>. </p>
<dt><code>&#8211;cpuset-mems</code> <i>list</i></p>
<dd>Set memory node(s) to use. The <i>list</i> format is the same as for <code>&#8211;cpuset-cpus</code>. </p>
<dt><code>&#8211;memory</code> <i>num</i></p>
<dd>Set memory limit to <i>num</i> bytes. </p>
<dt><code>&#8211;memory-reservation</code> <i>num</i></p>
<dd>Set memory reservation, or soft limit, to <i>num</i> bytes. </p>
<dt><code>&#8211;memory-swap</code> <i>num</i></p>
<dd>Set total memory + swap usage to <i>num</i> bytes. Use <code>-1</code> to unset the limit (i.e. use unlimited swap). </p>
<dt><code>&#8211;pids-limit</code> <i>num</i></p>
<dd>Set the maximum number of processes allowed in the container. </p>
<dt><code>&#8211;l3-cache-schema</code> <i>value</i></p>
<dd>Set the value for Intel RDT/CAT L3 cache schema. </p>
<dt><code>&#8211;mem-bw-schema</code> <i>value</i></p>
<dd>Set the Intel RDT/MBA memory bandwidth schema. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
