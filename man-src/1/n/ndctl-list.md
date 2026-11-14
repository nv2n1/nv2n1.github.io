---
title: "ndctl-list(1)"
name: "ndctl-list"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndctl-list/"
description: "ndctl-list – dump the platform nvdimm device topology and attributes in json"
---

<h2 class="name">NAME</h2>
<p> ndctl-list &#8211; dump the platform nvdimm device topology and attributes in json </p>
<h2>SYNOPSIS</h2>
<pre>
<i>ndctl list</i> [&lt;options&gt;]
</pre>
<p> Walk all the nvdimm buses in the system and list all attached devices along with some of their major attributes. </p>
<p> Options can be specified to limit the output to devices of a certain class. Where the classes are buses, dimms, regions, and namespaces. By default, <i>ndctl list</i> with no options is equivalent to: </p>
<pre>
ndctl list --namespaces --bus=all --region=all
</pre>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
# ndctl list --buses --namespaces
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
{
    "provider" : "nfit_test.1",
    "dev" : "ndbus2",
    "namespaces" : [
        {
            "dev" : "namespace9.0",
            "mode" : "raw",
            "size" : 33554432,
            "blockdev" : "pmem9"
        }
    ]
} {
    "provider" : "nfit_test.0",
    "dev" : "ndbus1"
} {
    "provider" : "e820",
                 "dev" : "ndbus0",
                         "namespaces" : [
                             {
                                 "dev" : "namespace0.0",
                                 "mode" : "memory",
                                 "size" : 8589934592,
                                 "blockdev" : "pmem0"
                             }
                         ]
}
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> -r, &#8211;region=</p>
<dl>
<dt>
<dd> A <i>regionX</i> device name, or a region id number. The keyword <i>all</i> can be specified to carry out the operation on every region in the system, optionally filtered by bus id (see &#8211;bus= option).</dl>
<p> -b, &#8211;bus=</p>
<dl>
<dt>
<dd> Enforce that the operation only be carried on devices that are attached to the given bus. Where <i>bus</i> can be a provider name or a bus id number.</dl>
<p> -d, &#8211;dimm=</p>
<dl>
<dt>
<dd> An <i>nmemX</i> device name, or dimm id number. Filter listing by devices that reference the given dimm. For example to see all namespaces comprised of storage capacity on nmem0:</dl>
<dl>
<dt>
<dd>
<pre>
# ndctl list --dimm=nmem0 --namespaces
</pre>
</dl>
<p> -n, &#8211;namespace=</p>
<dl>
<dt>
<dd> An <i>namespaceX.Y</i> device name, or namespace region plus id tuple <i>X.Y</i>. Limit the namespace list to the single identified device if present.</dl>
<p> -t, &#8211;type=</p>
<dl>
<dt>
<dd> Filter listing by region type (<i>pmem</i> or <i>blk</i>)</dl>
<p> -B, &#8211;buses</p>
<dl>
<dt>
<dd> Include bus info in the listing</dl>
<p> -D, &#8211;dimms</p>
<dl>
<dt>
<dd> Include dimm info in the listing</dl>
<p> -H, &#8211;health</p>
<dl>
<dt>
<dd> Include dimm health info in the listing. For example:</dl>
<dl>
<dt>
<dd>
<pre><code>
{
    "dev" : "nmem0",
            "health":
    {
        "health_state" : "non-critical",
                         "temperature_celsius" : 23,
                         "spares_percentage" : 75,
                         "alarm_temperature" : true,
                                               "alarm_spares" : true,
                                                                "temperature_threshold" : 40,
                                                                "spares_threshold" : 5,
                                                                "life_used_percentage" : 5,
                                                                "shutdown_state" : "clean"
    }
}
</code></pre>
</dl>
<p> -R, &#8211;regions</p>
<dl>
<dt>
<dd> Include region info in the listing</dl>
<p> -N, &#8211;namespaces</p>
<dl>
<dt>
<dd> Include namespace info in the listing. Namespace info is listed by default if no other options are specified to the command.</dl>
<p> -i, &#8211;idle</p>
<dl>
<dt>
<dd> Include idle (not enabled) devices in the listing</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ndctl-create-namespace/">ndctl-create-namespace</a></code>(1) </p>
<h2>Index</h2>
