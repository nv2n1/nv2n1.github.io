---
title: "git-repack(1)"
name: "git-repack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-repack/"
description: "git-repack – Pack unpacked objects in a repository"
---

<h2 class="name">NAME</h2>
<p> git-repack &#8211; Pack unpacked objects in a repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git repack[-a][-A][-d][-f][-F][-l][-n][-q][-b][-m][--window = &lt;n&gt;][--depth = &lt;n&gt;][--threads = &lt;n&gt;][--keep - pack = &lt;pack - name&gt;][--write - midx]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command is used to combine all objects that do not currently reside in a &quot;pack&quot;, into a pack. It can also be used to re-organize existing packs into a single, more efficient pack. </p>
<p> A pack is a collection of objects, individually compressed, with delta compression applied, stored in a single file, with an associated index file. </p>
<p> Packs are used to reduce the load on mirror systems, backup engines, disk storage, etc.</p>
<h2>OPTIONS</h2>
<p> -a</p>
<dl>
<dt>
<dd> Instead of incrementally packing the unpacked objects, pack everything referenced into a single pack. Especially useful when packing a repository that is used for private development. Use with <code>-d</code>. This will clean up the objects that <code>git prune</code> leaves behind, but <code>git fsck &#8211;full &#8211;dangling</code> shows as dangling. </p>
<p> Note that users fetching over dumb protocols will have to fetch the whole new pack in order to get any contained object, no matter how many other objects in that pack they already have locally. </p>
<p> Promisor packfiles are repacked separately: if there are packfiles that have an associated &quot;.promisor&quot; file, these packfiles will be repacked into another separate pack, and an empty &quot;.promisor&quot; file corresponding to the new separate pack will be written.</dl>
<p> -A</p>
<dl>
<dt>
<dd> Same as <code>-a</code>, unless <code>-d</code> is used. Then any unreachable objects in a previous pack become loose, unpacked objects, instead of being left in the old pack. Unreachable objects are never intentionally added to a pack, even when repacking. This option prevents unreachable objects from being immediately deleted by way of being left in the old pack and then removed. Instead, the loose unreachable objects will be pruned according to normal expiry rules with the next <i>git gc</i> invocation. See <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1).</dl>
<p> -d</p>
<dl>
<dt>
<dd> After packing, if the newly created packs make some existing packs redundant, remove the redundant packs. Also run <i>git prune-packed</i> to remove redundant loose object files.</dl>
<p> -l</p>
<dl>
<dt>
<dd> Pass the <code>&#8211;local</code> option to <i>git pack-objects</i>. See <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1).</dl>
<p> -f</p>
<dl>
<dt>
<dd> Pass the <code>&#8211;no-reuse-delta</code> option to <code>git-pack-objects</code>, see <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1).</dl>
<p> -F</p>
<dl>
<dt>
<dd> Pass the <code>&#8211;no-reuse-object</code> option to <code>git-pack-objects</code>, see <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1).</dl>
<p> -q</p>
<dl>
<dt>
<dd> Pass the <code>-q</code> option to <i>git pack-objects</i>. See <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1).</dl>
<p> -n</p>
<dl>
<dt>
<dd> Do not update the server information with <i>git update-server-info</i>. This option skips updating local catalog files needed to publish this repository (or a direct copy of it) over HTTP or FTP. See <code><a href="/docs/linux/man/1-git-update-server-info/">git-update-server-info</a></code>(1).</dl>
<p> &#8211;window=&lt;n&gt;, &#8211;depth=&lt;n&gt;</p>
<dl>
<dt>
<dd> These two options affect how the objects contained in the pack are stored using delta compression. The objects are first internally sorted by type, size and optionally names and compared against the other objects within <code>&#8211;window</code> to see if using delta compression saves space. <code>&#8211;depth</code> limits the maximum delta depth; making it too deep affects the performance on the unpacker side, because delta data needs to be applied that many times to get to the necessary object. </p>
<p> The default value for &#8211;window is 10 and &#8211;depth is 50. The maximum depth is 4095.</dl>
<p> &#8211;threads=&lt;n&gt;</p>
<dl>
<dt>
<dd> This option is passed through to <code>git pack-objects</code>.</dl>
<p> &#8211;window-memory=&lt;n&gt;</p>
<dl>
<dt>
<dd> This option provides an additional limit on top of <code>&#8211;window</code>; the window size will dynamically scale down so as to not take up more than <i>&lt;n&gt;</i> bytes in memory. This is useful in repositories with a mix of large and small objects to not run out of memory with a large window, but still be able to take advantage of the large window for the smaller objects. The size can be suffixed with &quot;k&quot;, &quot;m&quot;, or &quot;g&quot;. <code>&#8211;window-memory=0</code> makes memory usage unlimited. The default is taken from the <code>pack.windowMemory</code> configuration variable. Note that the actual memory usage will be the limit multiplied by the number of threads used by <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1).</dl>
<p> &#8211;max-pack-size=&lt;n&gt;</p>
<dl>
<dt>
<dd> Maximum size of each output pack file. The size can be suffixed with &quot;k&quot;, &quot;m&quot;, or &quot;g&quot;. The minimum size allowed is limited to 1 MiB. If specified, multiple packfiles may be created, which also prevents the creation of a bitmap index. The default is unlimited, unless the config variable <code>pack.packSizeLimit</code> is set. Note that this option may result in a larger and slower repository; see the discussion in <code>pack.packSizeLimit</code>.</dl>
<p> -b, &#8211;write-bitmap-index</p>
<dl>
<dt>
<dd> Write a reachability bitmap index as part of the repack. This only makes sense when used with <code>-a</code>, <code>-A</code> or <code>-m</code>, as the bitmaps must be able to refer to all reachable objects. This option overrides the setting of <code>repack.writeBitmaps</code>. This option has no effect if multiple packfiles are created, unless writing a MIDX (in which case a multi-pack bitmap is created).</dl>
<p> &#8211;pack-kept-objects</p>
<dl>
<dt>
<dd> Include objects in <code>.keep</code> files when repacking. Note that we still do not delete <code>.keep</code> packs after <code>pack-objects</code> finishes. This means that we may duplicate objects, but this makes the option safe to use when there are concurrent pushes or fetches. This option is generally only useful if you are writing bitmaps with <code>-b</code> or <code>repack.writeBitmaps</code>, as it ensures that the bitmapped packfile has the necessary objects.</dl>
<p> &#8211;keep-pack=&lt;pack-name&gt;</p>
<dl>
<dt>
<dd> Exclude the given pack from repacking. This is the equivalent of having <code>.keep</code> file on the pack. <code>&lt;pack-name&gt;</code> is the pack file name without leading directory (e.g. <code>pack-123.pack</code>). The option could be specified multiple times to keep multiple packs.</dl>
<p> &#8211;unpack-unreachable=&lt;when&gt;</p>
<dl>
<dt>
<dd> When loosening unreachable objects, do not bother loosening any objects older than <code>&lt;when&gt;</code>. This can be used to optimize out the write of any objects that would be immediately pruned by a follow-up <code>git prune</code>.</dl>
<p> -k, &#8211;keep-unreachable</p>
<dl>
<dt>
<dd> When used with <code>-ad</code>, any unreachable objects from existing packs will be appended to the end of the packfile instead of being removed. In addition, any unreachable loose objects will be packed (and their loose counterparts removed).</dl>
<p> -i, &#8211;delta-islands</p>
<dl>
<dt>
<dd> Pass the <code>&#8211;delta-islands</code> option to <code>git-pack-objects</code>, see <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1).</dl>
<p> -g=&lt;factor&gt;, &#8211;geometric=&lt;factor&gt;</p>
<dl>
<dt>
<dd> Arrange resulting pack structure so that each successive pack contains at least <code>&lt;factor&gt;</code> times the number of objects as the next-largest pack. </p>
<p> <code>git repack</code> ensures this by determining a &quot;cut&quot; of packfiles that need to be repacked into one in order to ensure a geometric progression. It picks the smallest set of packfiles such that as many of the larger packfiles (by count of objects contained in that pack) may be left intact. </p>
<p> Unlike other repack modes, the set of objects to pack is determined uniquely by the set of packs being &quot;rolled-up&quot;; in other words, the packs determined to need to be combined in order to restore a geometric progression. </p>
<p> When <code>&#8211;unpacked</code> is specified, loose objects are implicitly included in this &quot;roll-up&quot;, without respect to their reachability. This is subject to change in the future. This option (implying a drastically different repack mode) is not guaranteed to work with all other combinations of option to <code>git repack</code>. </p>
<p> When writing a multi-pack bitmap, <code>git repack</code> selects the largest resulting pack as the preferred pack for object selection by the MIDX (see <code><a href="/docs/linux/man/1-git-multi-pack-index/">git-multi-pack-index</a></code>(1)).</dl>
<p> -m, &#8211;write-midx</p>
<dl>
<dt>
<dd> Write a multi-pack index (see <code><a href="/docs/linux/man/1-git-multi-pack-index/">git-multi-pack-index</a></code>(1)) containing the non-redundant packs.</dl>
<h2>CONFIGURATION</h2>
<p> Various configuration variables affect packing, see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) (search for &quot;pack&quot; and &quot;delta&quot;). </p>
<p> By default, the command passes <code>&#8211;delta-base-offset</code> option to <i>git pack-objects</i>; this typically results in slightly smaller packs, but the generated packs are incompatible with versions of Git older than version 1.4.4. If you need to share your repository with such ancient Git versions, either directly or via the dumb http protocol, then you need to set the configuration variable <code>repack.UseDeltaBaseOffset</code> to &quot;false&quot; and repack. Access from old Git versions over the native protocol is unaffected by this option as the conversion is performed on the fly as needed in that case. </p>
<p> Delta compression is not used on objects larger than the <code>core.bigFileThreshold</code> configuration variable and on files with the attribute <code>delta</code> set to false.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) <code><a href="/docs/linux/man/1-git-prune-packed/">git-prune-packed</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
