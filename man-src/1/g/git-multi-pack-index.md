---
title: "git-multi-pack-index(1)"
name: "git-multi-pack-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-multi-pack-index/"
description: "git-multi-pack-index – Write and verify multi-pack-indexes"
---

<h2 class="name">NAME</h2>
<p> git-multi-pack-index &#8211; Write and verify multi-pack-indexes </p>
<h2>SYNOPSIS</h2>
<pre><code>
git multi - pack - index[--object - dir = &lt;dir&gt;][--[no - ] bitmap]&lt;sub - command&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Write or verify a multi-pack-index (MIDX) file.</p>
<h2>OPTIONS</h2>
<p> &#8211;object-dir=&lt;dir&gt;</p>
<dl>
<dt>
<dd> Use given directory for the location of Git objects. We check <code>&lt;dir&gt;/packs/multi-pack-index</code> for the current MIDX file, and <code>&lt;dir&gt;/packs</code> for the pack-files to index. </p>
<p> <code>&lt;dir&gt;</code> must be an alternate of the current repository.</dl>
<p> &#8211;[no-]progress</p>
<dl>
<dt>
<dd> Turn progress on/off explicitly. If neither is specified, progress is shown if standard error is connected to a terminal. Supported by sub-commands <code>write</code>, <code>verify</code>, <code>expire</code>, and `repack.</dl>
<p> The following subcommands are available: </p>
<p> write</p>
<dl>
<dt>
<dd> Write a new MIDX file. The following options are available for the <code>write</code> sub-command: </p>
<p> &#8211;preferred-pack=&lt;pack&gt;</p>
<dl>
<dt>
<dd> Optionally specify the tie-breaking pack used when multiple packs contain the same object. <code>&lt;pack&gt;</code> must contain at least one object. If not given, ties are broken in favor of the pack with the lowest mtime.</dl>
<p> &#8211;[no-]bitmap</p>
<dl>
<dt>
<dd> Control whether or not a multi-pack bitmap is written.</dl>
<p> &#8211;stdin-packs</p>
<dl>
<dt>
<dd> Write a multi-pack index containing only the set of line-delimited pack index basenames provided over stdin.</dl>
<p> &#8211;refs-snapshot=&lt;path&gt;</p>
<dl>
<dt>
<dd> With <code>&#8211;bitmap</code>, optionally specify a file which contains a &quot;refs snapshot&quot; taken prior to repacking. </p>
<p> A reference snapshot is composed of line-delimited OIDs corresponding to the reference tips, usually taken by <code>git repack</code> prior to generating a new pack. A line may optionally start with a <code>+</code> character to indicate that the reference which corresponds to that OID is &quot;preferred&quot; (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)&#8217;s <code>pack.preferBitmapTips</code>.) </p>
<p> The file given at <code>&lt;path&gt;</code> is expected to be readable, and can contain duplicates. (If a given OID is given more than once, it is marked as preferred if at least one instance of it begins with the special <code>+</code> marker).</dl>
</dl>
<p> verify</p>
<dl>
<dt>
<dd> Verify the contents of the MIDX file.</dl>
<p> expire</p>
<dl>
<dt>
<dd> Delete the pack-files that are tracked by the MIDX file, but have no objects referenced by the MIDX. Rewrite the MIDX file afterward to remove all references to these pack-files.</dl>
<p> repack</p>
<dl>
<dt>
<dd> Create a new pack-file containing objects in small pack-files referenced by the multi-pack-index. If the size given by the <code>&#8211;batch-size=&lt;size&gt;</code> argument is zero, then create a pack containing all objects referenced by the multi-pack-index. For a non-zero batch size, Select the pack-files by examining packs from oldest-to-newest, computing the &quot;expected size&quot; by counting the number of objects in the pack referenced by the multi-pack-index, then divide by the total number of objects in the pack and multiply by the pack size. We select packs with expected size below the batch size until the set of packs have total expected size at least the batch size, or all pack-files are considered. If only one pack-file is selected, then do nothing. If a new pack-file is created, rewrite the multi-pack-index to reference the new pack-file. A later run of <i>git multi-pack-index expire</i> will delete the pack-files that were part of this batch. </p>
<p> If <code>repack.packKeptObjects</code> is <code>false</code>, then any pack-files with an associated <code>.keep</code> file will not be selected for the batch to repack.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Write a MIDX file for the packfiles in the current <code>.git</code> directory. </p>
<dl>
<dt>
<dd>
<pre>
$ git multi-pack-index write
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Write a MIDX file for the packfiles in the current <code>.git</code> directory with a corresponding bitmap. </p>
<dl>
<dt>
<dd>
<pre>
$ git multi-pack-index write --preferred-pack=&lt;pack&gt; --bitmap
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Write a MIDX file for the packfiles in an alternate object store. </p>
<dl>
<dt>
<dd>
<pre>
$ git multi-pack-index --object-dir &lt;alt&gt; write
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Verify the MIDX file for the packfiles in the current <code>.git</code> directory. </p>
<dl>
<dt>
<dd>
<pre>
$ git multi-pack-index verify
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> See m[blue]<code>The Multi-Pack-Index Design Document</code>m[]<font SIZE="-2">[1]</font> and m[blue]<code>The Multi-Pack-Index Format</code>m[]<font SIZE="-2">[2]</font> for more information on the multi-pack-index feature.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> The Multi-Pack-Index Design Document</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/multi-pack-index.html</dl>
<dt> 2.</p>
<dd> The Multi-Pack-Index Format</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/pack-format.html</dl>
</dl>
<h2>Index</h2>
