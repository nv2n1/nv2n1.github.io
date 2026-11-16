---
title: "cachefilesd-conf(5)"
name: "cachefilesd-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cachefilesd-conf/"
description: "/etc/cachefilesd.conf – Local file caching configuration file"
---

<p>/etc/cachefilesd.conf &#8211; Local file caching configuration file</p>
<h2>Synopsis</h2>
<p>The configuration file for cachefilesd which can manage a persistent cache for a variety of network filesystems using a set of files on an already mounted filesystem as the data store.</p>
<h2>Description</h2>
<p>This configuration file can contain a number of commands. Each one should be on a separate line. Blank lines and lines beginning with a &#8216;#&#8217; character are considered to be comments and are discarded. </p>
<p> The only mandatory command is:</p>
<dl>
<dt><code>dir &lt;path&gt;</code></dt>
<dd>This command specifies the directory containing the root of the cache. It may only specified once per configuration file.</dd></dl>
<p> All the other commands are optional:</p>
<dl>
<dt><code>secctx &lt;label&gt;</code></dt>
<dd>Specify an LSM security context as which the kernel will perform operations to access the cache. The default is to use cachefilesd&#8217;s security context. Files will be created in the cache with the label of directory specified to the &#8216;dir&#8217; command.</dd>
<dt><code>brun &lt;N&gt;%</code></dt>
<dd>
</dd><dt><code>bcull &lt;N&gt;%</code></dt>
<dd>
</dd><dt><code>bstop &lt;N&gt;%</code></dt>
<dd>
</dd><dt><code>frun &lt;N&gt;%</code></dt>
<dd>
</dd><dt><code>fcull &lt;N&gt;%</code></dt>
<dd>
</dd><dt><code>fstop &lt;N&gt;%</code></dt>
<dd>These commands configure the culling limits. The defaults are 7% (run), 5% (cull) and 1% (stop) respectively. See the section on cache culling for more information.</dd>
<dd>The commands beginning with a &#8216;b&#8217; are file space (block) limits, those beginning with an &#8216;f&#8217; are file count limits.</dd>
<dt><code>tag &lt;name&gt;</code></dt>
<dd>This command specifies a tag to FS-Cache to use in distinguishing multiple caches. This is only required if more than one cache is going to be used. The default is &quot;CacheFiles&quot;.</dd>
<dt><code>culltable &lt;log2size&gt;</code></dt>
<dd>This command specifies the size of the tables holding the lists of cullable objects in the cache. The bigger the number, the faster and more smoothly that culling can proceed when there are many objects in the cache, but the more memory will be consumed by cachefilesd.</dd>
<dd>The quantity is specified as log2 of the size actually required, for example 12 indicates a table of 4096 entries and 13 indicates 8192 entries. The permissible values are between 12 and 20, the latter indicating 1048576 entries. The default is 12.</dd>
<dt><code>nocull</code></dt>
<dd>Disable culling. Culling and building up the cull table take up a certain amount of a systems resources, which may be undesirable. Supplying this option disables all culling activity. The cache will keep building up to the limits set and won&#8217;t be shrunk, except by the removal of out-dated cache files.</dd>
<dt><code>resume_thresholds &lt;blocks&gt; &lt;files&gt;</code></dt>
<dd>This command specifies the amount of blocks or files that the kernel should let go of before the daemon should resume from culling table scan suspension.</dd>
<dd>Scanning to refill the cull table is suspended when all the objects in a cache are pinned by a live network filesystem in the kernel and there&#8217;s nothing to cull.</dd>
<dd>Either value can be &quot;-&quot; to indicate that this threshold should be ignored.</dd>
<dt><code>debug &lt;mask&gt;</code></dt>
<dd>This command specifies a numeric bitmask to control debugging in the kernel module. The default is zero (all off). The following values can be OR&#8217;d into the mask to collect various information:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>1</code></dt>
<dd>Turn on trace of function entry (_enter() macros)</dd>
<dt><code>2</code></dt>
<dd>Turn on trace of function exit (_leave() macros)</dd>
<dt><code>4</code></dt>
<dd>Turn on trace of internal debug points (_debug())</dd></dl>
</dl>
<dd>This mask can also be set through /sys/module/cachefiles/parameters/debug.</dd></dl>
<h2>Examples</h2>
<p>As an example, consider the following: </p>
<dl>
<dd>dir /var/cache/fscache<br />
 secctx cachefiles_kernel_t<br />
 tag mycache<br />
 brun 10%<br />
 bcull 7%<br />
 bstop 3%<br />
 secctx system_u:system_r:cachefiles_kernel_t:s0</dd></dl>
<p> This places the cache storage objects in a directory called &quot;/var/cache/fscache&quot;, names the cache &quot;mycache&quot;, permits the cache to run freely as long as there&#8217;s at least 10% free space on /var/cache/fscache/, starts culling the cache when the free space drops below 7% and stops writing new stuff into the cache if the amount of free space drops below 3%. If the cache is suspended, it won&#8217;t reactivate until the amount of free space rises again to 10% or better. </p>
<p> Furthermore, this will tell the kernel module the security context it should use when accessing the cache (SELinux is assumed to be the LSM in this example). In this case, SELinux would use cachefiles_kernel_t as the key into the policy.</p>
<h2>Cache Culling</h2>
<p>The cache may need culling occasionally to make space. This involves discarding objects from the cache that have been used less recently than anything else. Culling is based on the access time of data objects. Empty directories are culled if not in use. </p>
<p> Cache culling is done on the basis of the percentage of blocks and the percentage of files available in the underlying filesystem. There are six &quot;limits&quot;:</p>
<dl>
<dt><code>brun</code></dt>
<dd>
</dd><dt><code>frun</code></dt>
<dd>If the amount of free space and the number of available files in the cache rises above both these limits, then culling is turned off.</dd>
<dt><code>bcull</code></dt>
<dd>
</dd><dt><code>fcull</code></dt>
<dd>If the amount of available space or the number of available files in the cache falls below either of these limits, then culling is started.</dd>
<dt><code>bstop</code></dt>
<dd>
</dd><dt><code>fstop</code></dt>
<dd>If the amount of available space or the number of available files in the cache falls below either of these limits, then no further allocation of disk space or files is permitted until culling has raised things above these limits again.</dd></dl>
<p> These must be configured thusly:</p>
<dl>
<dd>0 &lt;= bstop &lt; bcull &lt; brun &lt; 100<br />
 0 &lt;= fstop &lt; fcull &lt; frun &lt; 100</dd></dl>
<p> Note that these are percentages of available space and available files, and do <i>not</i> appear as 100 minus the percentage displayed by the <code>df</code> program. </p>
<p> The userspace daemon scans the cache to build up a table of cullable objects. These are then culled in least recently used order. A new scan of the cache is started as soon as space is made in the table. Objects will be skipped if their atimes have changed or if the kernel module says it is still using them. </p>
<p> Culling can be disabled with the <code>nocull</code> option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cachefilesd/">cachefilesd</a></code>(8), <code><a href="/docs/linux/man/1-df/">df</a></code>(1), /usr/share/doc/cachefilesd/README</p>
<h2>Authors</h2>
<p>David Howells &lt;dhowells [at] redhat.com&gt;</p>
