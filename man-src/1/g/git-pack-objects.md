---
title: "git-pack-objects(1)"
name: "git-pack-objects"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-pack-objects/"
description: "git-pack-objects – Create a packed archive of objects"
---

<h2 class="name">NAME</h2>
<p> git-pack-objects &#8211; Create a packed archive of objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
git pack - objects[-q | --progress | --all - progress][--all - progress - implied]
                  [--no - reuse - delta][--delta - base - offset][--non - empty]
                  [--local][--incremental][--window = &lt;n&gt;][--depth = &lt;n&gt;]
                  [--revs[--unpacked | --all]][--keep - pack = &lt;pack - name&gt;]
                  [--stdout[--filter = &lt;filter - spec&gt;] | base - name]
                  [--shallow][--keep - true - parents][--[no - ] sparse] &lt;
    object - list
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads list of objects from the standard input, and writes either one or more packed archives with the specified base-name to disk, or a packed archive to the standard output. </p>
<p> A packed archive is an efficient way to transfer a set of objects between two repositories as well as an access efficient archival format. In a packed archive, an object is either stored as a compressed whole or as a difference from some other object. The latter is often called a delta. </p>
<p> The packed archive format (.pack) is designed to be self-contained so that it can be unpacked without any further information. Therefore, each object that a delta depends upon must be present within the pack. </p>
<p> A pack index file (.idx) is generated for fast, random access to the objects in the pack. Placing both the index file (.idx) and the packed archive (.pack) in the pack/ subdirectory of $GIT_OBJECT_DIRECTORY (or any of the directories on $GIT_ALTERNATE_OBJECT_DIRECTORIES) enables Git to read from the pack archive. </p>
<p> The <i>git unpack-objects</i> command can read the packed archive and expand the objects contained in the pack into &quot;one-file one-object&quot; format; this is typically done by the smart-pull commands when a pack is created on-the-fly for efficient network transport by their peers.</p>
<h2>OPTIONS</h2>
<p> base-name</p>
<dl>
<dt>
<dd> Write into pairs of files (.pack and .idx), using &lt;base-name&gt; to determine the name of the created file. When this option is used, the two files in a pair are written in &lt;base-name&gt;-&lt;SHA-1&gt;.{pack,idx} files. &lt;SHA-1&gt; is a hash based on the pack content and is written to the standard output of the command.</dl>
<p> &#8211;stdout</p>
<dl>
<dt>
<dd> Write the pack contents (what would have been written to .pack file) out to the standard output.</dl>
<p> &#8211;revs</p>
<dl>
<dt>
<dd> Read the revision arguments from the standard input, instead of individual object names. The revision arguments are processed the same way as <i>git rev-list</i> with the <code>&#8211;objects</code> flag uses its <code>commit</code> arguments to build the list of objects it outputs. The objects on the resulting list are packed. Besides revisions, <code>&#8211;not</code> or <code>&#8211;shallow &lt;SHA-1&gt;</code> lines are also accepted.</dl>
<p> &#8211;unpacked</p>
<dl>
<dt>
<dd> This implies <code>&#8211;revs</code>. When processing the list of revision arguments read from the standard input, limit the objects packed to those that are not already packed.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> This implies <code>&#8211;revs</code>. In addition to the list of revision arguments read from the standard input, pretend as if all refs under <code>refs/</code> are specified to be included.</dl>
<p> &#8211;include-tag</p>
<dl>
<dt>
<dd> Include unasked-for annotated tags if the object they reference was included in the resulting packfile. This can be useful to send new tags to native Git clients.</dl>
<p> &#8211;stdin-packs</p>
<dl>
<dt>
<dd> Read the basenames of packfiles (e.g., <code>pack-1234abcd.pack</code>) from the standard input, instead of object names or revision arguments. The resulting pack contains all objects listed in the included packs (those not beginning with <code>^</code>), excluding any objects listed in the excluded packs (beginning with <code>^</code>). </p>
<p> Incompatible with <code>&#8211;revs</code>, or options that imply <code>&#8211;revs</code> (such as <code>&#8211;all</code>), with the exception of <code>&#8211;unpacked</code>, which is compatible.</dl>
<p> &#8211;window=&lt;n&gt;, &#8211;depth=&lt;n&gt;</p>
<dl>
<dt>
<dd> These two options affect how the objects contained in the pack are stored using delta compression. The objects are first internally sorted by type, size and optionally names and compared against the other objects within &#8211;window to see if using delta compression saves space. &#8211;depth limits the maximum delta depth; making it too deep affects the performance on the unpacker side, because delta data needs to be applied that many times to get to the necessary object. </p>
<p> The default value for &#8211;window is 10 and &#8211;depth is 50. The maximum depth is 4095.</dl>
<p> &#8211;window-memory=&lt;n&gt;</p>
<dl>
<dt>
<dd> This option provides an additional limit on top of <code>&#8211;window</code>; the window size will dynamically scale down so as to not take up more than <i>&lt;n&gt;</i> bytes in memory. This is useful in repositories with a mix of large and small objects to not run out of memory with a large window, but still be able to take advantage of the large window for the smaller objects. The size can be suffixed with &quot;k&quot;, &quot;m&quot;, or &quot;g&quot;. <code>&#8211;window-memory=0</code> makes memory usage unlimited. The default is taken from the <code>pack.windowMemory</code> configuration variable.</dl>
<p> &#8211;max-pack-size=&lt;n&gt;</p>
<dl>
<dt>
<dd> In unusual scenarios, you may not be able to create files larger than a certain size on your filesystem, and this option can be used to tell the command to split the output packfile into multiple independent packfiles, each not larger than the given size. The size can be suffixed with &quot;k&quot;, &quot;m&quot;, or &quot;g&quot;. The minimum size allowed is limited to 1 MiB. The default is unlimited, unless the config variable <code>pack.packSizeLimit</code> is set. Note that this option may result in a larger and slower repository; see the discussion in <code>pack.packSizeLimit</code>.</dl>
<p> &#8211;honor-pack-keep</p>
<dl>
<dt>
<dd> This flag causes an object already in a local pack that has a .keep file to be ignored, even if it would have otherwise been packed.</dl>
<p> &#8211;keep-pack=&lt;pack-name&gt;</p>
<dl>
<dt>
<dd> This flag causes an object already in the given pack to be ignored, even if it would have otherwise been packed. <code>&lt;pack-name&gt;</code> is the pack file name without leading directory (e.g. <code>pack-123.pack</code>). The option could be specified multiple times to keep multiple packs.</dl>
<p> &#8211;incremental</p>
<dl>
<dt>
<dd> This flag causes an object already in a pack to be ignored even if it would have otherwise been packed.</dl>
<p> &#8211;local</p>
<dl>
<dt>
<dd> This flag causes an object that is borrowed from an alternate object store to be ignored even if it would have otherwise been packed.</dl>
<p> &#8211;non-empty</p>
<dl>
<dt>
<dd> Only create a packed archive if it would contain at least one object.</dl>
<p> &#8211;progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal.</dl>
<p> &#8211;all-progress</p>
<dl>
<dt>
<dd> When &#8211;stdout is specified then progress report is displayed during the object count and compression phases but inhibited during the write-out phase. The reason is that in some cases the output stream is directly linked to another command which may wish to display progress status of its own as it processes incoming pack data. This flag is like &#8211;progress except that it forces progress report for the write-out phase as well even if &#8211;stdout is used.</dl>
<p> &#8211;all-progress-implied</p>
<dl>
<dt>
<dd> This is used to imply &#8211;all-progress whenever progress display is activated. Unlike &#8211;all-progress this flag doesn&#8217;t actually force any progress display by itself.</dl>
<p> -q</p>
<dl>
<dt>
<dd> This flag makes the command not to report its progress on the standard error stream.</dl>
<p> &#8211;no-reuse-delta</p>
<dl>
<dt>
<dd> When creating a packed archive in a repository that has existing packs, the command reuses existing deltas. This sometimes results in a slightly suboptimal pack. This flag tells the command not to reuse existing deltas but compute them from scratch.</dl>
<p> &#8211;no-reuse-object</p>
<dl>
<dt>
<dd> This flag tells the command not to reuse existing object data at all, including non deltified object, forcing recompression of everything. This implies &#8211;no-reuse-delta. Useful only in the obscure case where wholesale enforcement of a different compression level on the packed data is desired.</dl>
<p> &#8211;compression=&lt;n&gt;</p>
<dl>
<dt>
<dd> Specifies compression level for newly-compressed data in the generated pack. If not specified, pack compression level is determined first by pack.compression, then by core.compression, and defaults to -1, the zlib default, if neither is set. Add &#8211;no-reuse-object if you want to force a uniform compression level on all data no matter the source.</dl>
<p> &#8211;[no-]sparse</p>
<dl>
<dt>
<dd> Toggle the &quot;sparse&quot; algorithm to determine which objects to include in the pack, when combined with the &quot;&#8211;revs&quot; option. This algorithm only walks trees that appear in paths that introduce new objects. This can have significant performance benefits when computing a pack to send a small change. However, it is possible that extra objects are added to the pack-file if the included commits contain certain types of direct renames. If this option is not included, it defaults to the value of <code>pack.useSparse</code>, which is true unless otherwise specified.</dl>
<p> &#8211;thin</p>
<dl>
<dt>
<dd> Create a &quot;thin&quot; pack by omitting the common objects between a sender and a receiver in order to reduce network transfer. This option only makes sense in conjunction with &#8211;stdout. </p>
<p> Note: A thin pack violates the packed archive format by omitting required objects and is thus unusable by Git without making it self-contained. Use <code>git index-pack &#8211;fix-thin</code> (see <code><a href="/docs/linux/man/1-git-index-pack/">git-index-pack</a></code>(1)) to restore the self-contained property.</dl>
<p> &#8211;shallow</p>
<dl>
<dt>
<dd> Optimize a pack that will be provided to a client with a shallow repository. This option, combined with &#8211;thin, can result in a smaller pack at the cost of speed.</dl>
<p> &#8211;delta-base-offset</p>
<dl>
<dt>
<dd> A packed archive can express the base object of a delta as either a 20-byte object name or as an offset in the stream, but ancient versions of Git don&#8217;t understand the latter. By default, <i>git pack-objects</i> only uses the former format for better compatibility. This option allows the command to use the latter format for compactness. Depending on the average delta chain length, this option typically shrinks the resulting packfile by 3-5 per-cent. </p>
<p> Note: Porcelain commands such as <code>git gc</code> (see <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1)), <code>git repack</code> (see <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1)) pass this option by default in modern Git when they put objects in your repository into pack files. So does <code>git bundle</code> (see <code><a href="/docs/linux/man/1-git-bundle/">git-bundle</a></code>(1)) when it creates a bundle.</dl>
<p> &#8211;threads=&lt;n&gt;</p>
<dl>
<dt>
<dd> Specifies the number of threads to spawn when searching for best delta matches. This requires that pack-objects be compiled with pthreads otherwise this option is ignored with a warning. This is meant to reduce packing time on multiprocessor machines. The required amount of memory for the delta search window is however multiplied by the number of threads. Specifying 0 will cause Git to auto-detect the number of CPU&#8217;s and set the number of threads accordingly.</dl>
<p> &#8211;index-version=&lt;version&gt;[,&lt;offset&gt;]</p>
<dl>
<dt>
<dd> This is intended to be used by the test suite only. It allows to force the version for the generated pack index, and to force 64-bit index entries on objects located above the given offset.</dl>
<p> &#8211;keep-true-parents</p>
<dl>
<dt>
<dd> With this option, parents that are hidden by grafts are packed nevertheless.</dl>
<p> &#8211;filter=&lt;filter-spec&gt;</p>
<dl>
<dt>
<dd> Requires <code>&#8211;stdout</code>. Omits certain objects (usually blobs) from the resulting packfile. See <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) for valid <code>&lt;filter-spec&gt;</code> forms.</dl>
<p> &#8211;no-filter</p>
<dl>
<dt>
<dd> Turns off any previous <code>&#8211;filter=</code> argument.</dl>
<p> &#8211;missing=&lt;missing-action&gt;</p>
<dl>
<dt>
<dd> A debug option to help with future &quot;partial clone&quot; development. This option specifies how missing objects are handled. </p>
<p> The form <i>&#8211;missing=error</i> requests that pack-objects stop with an error if a missing object is encountered. If the repository is a partial clone, an attempt to fetch missing objects will be made before declaring them missing. This is the default action. </p>
<p> The form <i>&#8211;missing=allow-any</i> will allow object traversal to continue if a missing object is encountered. No fetch of a missing object will occur. Missing objects will silently be omitted from the results. </p>
<p> The form <i>&#8211;missing=allow-promisor</i> is like <i>allow-any</i>, but will only allow object traversal to continue for EXPECTED promisor missing objects. No fetch of a missing object will occur. An unexpected missing object will raise an error.</dl>
<p> &#8211;exclude-promisor-objects</p>
<dl>
<dt>
<dd> Omit objects that are known to be in the promisor remote. (This option has the purpose of operating only on locally created objects, so that when we repack, we still maintain a distinction between locally created objects [without .promisor] and objects from the promisor remote [with .promisor].) This is used with partial clone.</dl>
<p> &#8211;keep-unreachable</p>
<dl>
<dt>
<dd> Objects unreachable from the refs in packs named with &#8211;unpacked= option are added to the resulting pack, in addition to the reachable objects that are not in packs marked with *.keep files. This implies <code>&#8211;revs</code>.</dl>
<p> &#8211;pack-loose-unreachable</p>
<dl>
<dt>
<dd> Pack unreachable loose objects (and their loose counterparts removed). This implies <code>&#8211;revs</code>.</dl>
<p> &#8211;unpack-unreachable</p>
<dl>
<dt>
<dd> Keep unreachable objects in loose form. This implies <code>&#8211;revs</code>.</dl>
<p> &#8211;delta-islands</p>
<dl>
<dt>
<dd> Restrict delta matches based on &quot;islands&quot;. See DELTA ISLANDS below.</dl>
<h2>DELTA ISLANDS</h2>
<p> When possible, <code>pack-objects</code> tries to reuse existing on-disk deltas to avoid having to search for new ones on the fly. This is an important optimization for serving fetches, because it means the server can avoid inflating most objects at all and just send the bytes directly from disk. This optimization can&#8217;t work when an object is stored as a delta against a base which the receiver does not have (and which we are not already sending). In that case the server &quot;breaks&quot; the delta and has to find a new one, which has a high CPU cost. Therefore it&#8217;s important for performance that the set of objects in on-disk delta relationships match what a client would fetch. </p>
<p> In a normal repository, this tends to work automatically. The objects are mostly reachable from the branches and tags, and that&#8217;s what clients fetch. Any deltas we find on the server are likely to be between objects the client has or will have. </p>
<p> But in some repository setups, you may have several related but separate groups of ref tips, with clients tending to fetch those groups independently. For example, imagine that you are hosting several &quot;forks&quot; of a repository in a single shared object store, and letting clients view them as separate repositories through <code>GIT_NAMESPACE</code> or separate repos using the alternates mechanism. A naive repack may find that the optimal delta for an object is against a base that is only found in another fork. But when a client fetches, they will not have the base object, and we&#8217;ll have to find a new delta on the fly. </p>
<p> A similar situation may exist if you have many refs outside of <code>refs/heads/</code> and <code>refs/tags/</code> that point to related objects (e.g., <code>refs/pull</code> or <code>refs/changes</code> used by some hosting providers). By default, clients fetch only heads and tags, and deltas against objects found only in those other groups cannot be sent as-is. </p>
<p> Delta islands solve this problem by allowing you to group your refs into distinct &quot;islands&quot;. Pack-objects computes which objects are reachable from which islands, and refuses to make a delta from an object <code>A</code> against a base which is not present in all of <code>A</code>&#8216;s islands. This results in slightly larger packs (because we miss some delta opportunities), but guarantees that a fetch of one island will not have to recompute deltas on the fly due to crossing island boundaries. </p>
<p> When repacking with delta islands the delta window tends to get clogged with candidates that are forbidden by the config. Repacking with a big &#8211;window helps (and doesn&#8217;t take as long as it otherwise might because we can reject some object pairs based on islands before doing any computation on the content). </p>
<p> Islands are configured via the <code>pack.island</code> option, which can be specified multiple times. Each value is a left-anchored regular expressions matching refnames. For example: </p>
<dl>
<dt>
<dd>
<pre>
[pack]
island = refs/heads/
island = refs/tags/
</pre>
</dl>
<p> puts heads and tags into an island (whose name is the empty string; see below for more on naming). Any refs which do not match those regular expressions (e.g., <code>refs/pull/123</code>) is not in any island. Any object which is reachable only from <code>refs/pull/</code> (but not heads or tags) is therefore not a candidate to be used as a base for <code>refs/heads/</code>. </p>
<p> Refs are grouped into islands based on their &quot;names&quot;, and two regexes that produce the same name are considered to be in the same island. The names are computed from the regexes by concatenating any capture groups from the regex, with a <i>&#8211;</i> dash in between. (And if there are no capture groups, then the name is the empty string, as in the above example.) This allows you to create arbitrary numbers of islands. Only up to 14 such capture groups are supported though. </p>
<p> For example, imagine you store the refs for each fork in <code>refs/virtual/ID</code>, where <code>ID</code> is a numeric identifier. You might then configure: </p>
<dl>
<dt>
<dd>
<pre><code>
[pack] island = refs / virtual / ([0 - 9] +) / heads /
                island = refs / virtual / ([0 - 9] +) / tags /
                         island = refs / virtual / ([0 - 9] +) / (pull) /
</code></pre>
</dl>
<p> That puts the heads and tags for each fork in their own island (named &quot;1234&quot; or similar), and the pull refs for each go into their own &quot;1234-pull&quot;. </p>
<p> Note that we pick a single island for each regex to go into, using &quot;last one wins&quot; ordering (which allows repo-specific config to take precedence over user-wide config, and so forth).</p>
<h2>CONFIGURATION</h2>
<p> Various configuration variables affect packing, see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) (search for &quot;pack&quot; and &quot;delta&quot;). </p>
<p> Notably, delta compression is not used on objects larger than the <code>core.bigFileThreshold</code> configuration variable and on files with the attribute <code>delta</code> set to false.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) <code><a href="/docs/linux/man/1-git-prune-packed/">git-prune-packed</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
