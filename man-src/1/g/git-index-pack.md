---
title: "git-index-pack(1)"
name: "git-index-pack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-index-pack/"
description: "git-index-pack – Build pack index file for an existing packed archive"
---

<h2 class="name">NAME</h2>
<p> git-index-pack &#8211; Build pack index file for an existing packed archive </p>
<h2>SYNOPSIS</h2>
<pre><code>
git index - pack[-v][-o&lt;index - file&gt;][--[no - ] rev - index]&lt;pack - file&gt; git index - pack-- stdin[--fix - thin][--keep][-v][-o&lt;index - file&gt;][--[no - ] rev - index][&lt;pack - file&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads a packed archive (.pack) from the specified file, and builds a pack index file (.idx) for it. Optionally writes a reverse-index (.rev) for the specified pack. The packed archive together with the pack index can then be placed in the objects/pack/ directory of a Git repository.</p>
<h2>OPTIONS</h2>
<p> -v</p>
<dl>
<dt>
<dd> Be verbose about what is going on, including progress status.</dl>
<p> -o &lt;index-file&gt;</p>
<dl>
<dt>
<dd> Write the generated pack index into the specified file. Without this option the name of pack index file is constructed from the name of packed archive file by replacing .pack with .idx (and the program fails if the name of packed archive does not end with .pack).</dl>
<p> &#8211;[no-]rev-index</p>
<dl>
<dt>
<dd> When this flag is provided, generate a reverse index (a <code>.rev</code> file) corresponding to the given pack. If <code>&#8211;verify</code> is given, ensure that the existing reverse index is correct. Takes precedence over <code>pack.writeReverseIndex</code>.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> When this flag is provided, the pack is read from stdin instead and a copy is then written to &lt;pack-file&gt;. If &lt;pack-file&gt; is not specified, the pack is written to objects/pack/ directory of the current Git repository with a default name determined from the pack content. If &lt;pack-file&gt; is not specified consider using &#8211;keep to prevent a race condition between this process and <i>git repack</i>.</dl>
<p> &#8211;fix-thin</p>
<dl>
<dt>
<dd> Fix a &quot;thin&quot; pack produced by <code>git pack-objects &#8211;thin</code> (see <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) for details) by adding the excluded objects the deltified objects are based on to the pack. This option only makes sense in conjunction with &#8211;stdin.</dl>
<p> &#8211;keep</p>
<dl>
<dt>
<dd> Before moving the index into its final destination create an empty .keep file for the associated pack file. This option is usually necessary with &#8211;stdin to prevent a simultaneous <i>git repack</i> process from deleting the newly constructed pack and index before refs can be updated to use objects contained in the pack.</dl>
<p> &#8211;keep=&lt;msg&gt;</p>
<dl>
<dt>
<dd> Like &#8211;keep create a .keep file before moving the index into its final destination, but rather than creating an empty file place <i>&lt;msg&gt;</i> followed by an LF into the .keep file. The <i>&lt;msg&gt;</i> message can later be searched for within all .keep files to locate any which have outlived their usefulness.</dl>
<p> &#8211;index-version=&lt;version&gt;[,&lt;offset&gt;]</p>
<dl>
<dt>
<dd> This is intended to be used by the test suite only. It allows to force the version for the generated pack index, and to force 64-bit index entries on objects located above the given offset.</dl>
<p> &#8211;strict</p>
<dl>
<dt>
<dd> Die, if the pack contains broken objects or links.</dl>
<p> &#8211;progress-title</p>
<dl>
<dt>
<dd> For internal use only. </p>
<p> Set the title of the progress bar. The title is &quot;Receiving objects&quot; by default and &quot;Indexing objects&quot; when <code>&#8211;stdin</code> is specified.</dl>
<p> &#8211;check-self-contained-and-connected</p>
<dl>
<dt>
<dd> Die if the pack contains broken links. For internal use only.</dl>
<p> &#8211;fsck-objects</p>
<dl>
<dt>
<dd> For internal use only. </p>
<p> Die if the pack contains broken objects. If the pack contains a tree pointing to a .gitmodules blob that does not exist, prints the hash of that blob (for the caller to check) after the hash that goes into the name of the pack/idx file (see &quot;Notes&quot;).</dl>
<p> &#8211;threads=&lt;n&gt;</p>
<dl>
<dt>
<dd> Specifies the number of threads to spawn when resolving deltas. This requires that index-pack be compiled with pthreads otherwise this option is ignored with a warning. This is meant to reduce packing time on multiprocessor machines. The required amount of memory for the delta search window is however multiplied by the number of threads. Specifying 0 will cause Git to auto-detect the number of CPU&#8217;s and use maximum 3 threads.</dl>
<p> &#8211;max-input-size=&lt;size&gt;</p>
<dl>
<dt>
<dd> Die, if the pack is larger than &lt;size&gt;.</dl>
<p> &#8211;object-format=&lt;hash-algorithm&gt;</p>
<dl>
<dt>
<dd> Specify the given object format (hash algorithm) for the pack. The valid values are <i>sha1</i> and (if enabled) <i>sha256</i>. The default is the algorithm for the current repository (set by <code>extensions.objectFormat</code>), or <i>sha1</i> if no value is set or outside a repository. </p>
<p> This option cannot be used with &#8211;stdin. </p>
<p> THIS OPTION IS EXPERIMENTAL! SHA-256 support is experimental and still in an early stage. A SHA-256 repository will in general not be able to share work with &quot;regular&quot; SHA-1 repositories. It should be assumed that, e.g., Git internal file formats in relation to SHA-256 repositories may change in backwards-incompatible ways. Only use <code>&#8211;object-format=sha256</code> for testing purposes.</dl>
<h2>NOTES</h2>
<p> Once the index has been created, the hash that goes into the name of the pack/idx file is printed to stdout. If &#8211;stdin was also used then this is prefixed by either &quot;pack	&quot;, or &quot;keep	&quot; if a new .keep file was successfully created. This is useful to remove a .keep file used as a lock to prevent the race with <i>git repack</i> mentioned above.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
