---
title: "lintianfilepath(3)"
name: "lintianfilepath"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianfilepath/"
description: "Lintian::File::Path – Lintian representation of a path entry in a package"
---

<p>Lintian::File::Path &#8211; Lintian representation of a path entry in a package </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('lintian', 'source', '/path/to/entry');</pre>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>init_from_tar_output</p>
<dd>
<dt>get_quoted_filename</p>
<dd>
<dt>unescape_c_style</p>
<dd>
<dt>magic(<font SIZE="-1">COUNT</font>)</p>
<dd>Returns the specified <font SIZE="-1">COUNT</font> of magic bytes for the file.</p>
<dt>get_interpreter</p>
<dd>Returns the interpreter for the file if it is a script.</p>
<dt>is_script</p>
<dd>Returns true if file is a script and false otherwise.</p>
<dt>is_control</p>
<dd>Returns true if file is a maintainer script and false otherwise.</p>
<dt>identity</p>
<dd>Returns the owner and group of the path, separated by a slash. </p>
<p> <font SIZE="-1">NB:</font> If only numerical owner information is available in the package, this may return a numerical owner (except uid 0 is always mapped to &#8220;root&#8221;)</p>
<dt>operm</p>
<dd>Returns the file permissions of this object in octal (e.g. 0644). </p>
<p> <font SIZE="-1">NB:</font> This is only well defined for file entries that are subject to permissions (e.g. files). Particularly, the value is not well defined for symlinks.</p>
<dt>children</p>
<dd>Returns a list of children (as Lintian::File::Path objects) of this entry. The list and its contents should not be modified. </p>
<p> Only returns direct children of this directory. The entries are sorted by name. </p>
<p> <font SIZE="-1">NB:</font> Returns the empty list for non-dir entries.</p>
<dt>descendants</p>
<dd>Returns a list of children (as Lintian::File::Path objects) of this entry. The list and its contents should not be modified. </p>
<p> Descends recursively into subdirectories and return the descendants in breadth-first order. Children of a given directory will be sorted by name. </p>
<p> <font SIZE="-1">NB:</font> Returns the empty list for non-dir entries.</p>
<dt>timestamp</p>
<dd>Returns a Unix timestamp for the given path. This is a number of seconds since the start of Unix epoch in <font SIZE="-1">UTC.</font></p>
<dt>child(<font SIZE="-1">BASENAME</font>)</p>
<dd>Returns the child named <font SIZE="-1">BASENAME</font> if it is a child of this directory. Otherwise, this method returns <tt>&quot;undef&quot;</tt>. </p>
<p> Even for directories, <font SIZE="-1">BASENAME</font> should not end with a slash. </p>
<p> When invoked on non-dirs, this method always returns <tt>&quot;undef&quot;</tt>. </p>
<p> Example: </p>
<pre> $dir_entry-&gt;child('foo') =&gt; $entry OR undef</pre>
<dt>is_symlink</p>
<dd>Returns a truth value if this entry is a symlink.</p>
<dt>is_hardlink</p>
<dd>Returns a truth value if this entry is a hardlink to a regular file. </p>
<p> <font SIZE="-1">NB:</font> The target of a hardlink is always a regular file (and not a dir etc.).</p>
<dt>is_dir</p>
<dd>Returns a truth value if this entry is a dir. </p>
<p> <font SIZE="-1">NB:</font> Unlike the &#8220;-d <tt>$dir</tt>&#8221; operator this will never return true for symlinks, even if the symlink points to a dir.</p>
<dt>is_file</p>
<dd>Returns a truth value if this entry is a regular file (or a hardlink to one). </p>
<p> <font SIZE="-1">NB:</font> Unlike the &#8220;-f <tt>$file</tt>&#8221; operator this will never return true for symlinks, even if the symlink points to a file (or hardlink).</p>
<dt>is_regular_file</p>
<dd>Returns a truth value if this entry is a regular file. </p>
<p> This is eqv. to <tt>$path</tt>-&gt;is_file and not <tt>$path</tt>-&gt;is_hardlink. </p>
<p> <font SIZE="-1">NB:</font> Unlike the &#8220;-f <tt>$file</tt>&#8221; operator this will never return true for symlinks, even if the symlink points to a file.</p>
<dt>link_normalized</p>
<dd>Returns the target of the link normalized against it&#8217;s directory name. If the link cannot be normalized or normalized path might escape the package root, this method returns <tt>&quot;undef&quot;</tt>. </p>
<p> <font SIZE="-1">NB:</font> This method will return the empty string for links pointing to the root dir of the package. </p>
<p> Only available on &#8220;links&#8221; (i.e. symlinks or hardlinks). On non-links this will croak. </p>
<p> <i>Symlinks only</i>: If you want the symlink target as a Lintian::File::Path object, use the resolve_path method with no arguments instead.</p>
<dt>is_readable</p>
<dd>Returns a truth value if the permission bits of this entry have at least one bit denoting readability set (bitmask 0444).</p>
<dt>is_writable</p>
<dd>Returns a truth value if the permission bits of this entry have at least one bit denoting writability set (bitmask 0222).</p>
<dt>is_executable</p>
<dd>Returns a truth value if the permission bits of this entry have at least one bit denoting executability set (bitmask 0111).</p>
<dt>unpacked_path</p>
<dd>Returns the path to this object on the file system, which must be a regular file, a hardlink or a directory. </p>
<p> This method may fail if:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>The object is neither a directory or a file-like object (e.g. a named pipe).</p>
<dt>&bull;</p>
<dd>If the object is dangling symlink or the path traverses a symlink outside the package root.</dl>
</dl>
<dl COMPACT>
<dd>To test if this is safe to call, if the target is (supposed) to be a:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>file or hardlink then test with &#8220;is_open_ok&#8221;.</p>
<dt>&bull;</p>
<dd>dir then assert resolve_path returns a defined entry, for which &#8220;is_dir&#8221; returns a truth value.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>is_open_ok</p>
<dd>Returns a truth value if it is safe to attempt open a read handle to the underlying file object. </p>
<p> Returns a truth value if the path may be opened.</p>
<dt>slurp</p>
<dd>Return the file contents as a scalar. </p>
<p> This method may fail for the same reasons as &#8220;open([<font SIZE="-1">LAYER</font>])&#8221;.</p>
<dt>follow</p>
<dd>Return dereferenced link if applicable</p>
<dt>resolve_path([<font SIZE="-1">PATH</font>])</p>
<dd>Resolve <font SIZE="-1">PATH</font> relative to this path entry. </p>
<p> If <font SIZE="-1">PATH</font> starts with a slash and the file hierarchy has a well-defined root directory, then <font SIZE="-1">PATH</font> will instead be resolved relatively to the root dir. If the file hierarchy does not have a well-defined root dir (e.g. for source packages), this method will return <tt>&quot;undef&quot;</tt>. </p>
<p> If <font SIZE="-1">PATH</font> is omitted, then the entry is resolved and the target is returned if it is valid. Except for symlinks, all entries always resolve to themselves. <font SIZE="-1">NB:</font> hardlinks also resolve as themselves. </p>
<p> It is an error to attempt to resolve a <font SIZE="-1">PATH</font> against a non-directory and non-symlink entry &#8211; as such resolution would always fail (i.e. foo/../bar is an invalid path unless foo is a directory or a symlink to a dir). </p>
<p> The resolution takes symlinks into account and following them provided that the target path is valid (and can be followed safely). If the path is invalid or circular (symlinks), escapes the root directory or follows an unsafe symlink, the method returns <tt>&quot;undef&quot;</tt>. Otherwise, it returns the path entry that denotes the target path. </p>
<p> If <font SIZE="-1">PATH</font> contains at least one path segment and ends with a slash, then the resolved path will end in a directory (or fail). Otherwise, the resolved <font SIZE="-1">PATH</font> can end in any entry <i>except</i> a symlink. </p>
<p> Examples: </p>
<pre> $symlink_entry-&gt;resolve_path =&gt; $nonsymlink_entry OR undef
 $x-&gt;resolve_path =&gt; $x
 For directory or symlink entries (dol), you can also resolve a path:
 $dol_entry-&gt;resolve_path('some/../where') =&gt; $nonsymlink_entry OR undef
 # Note the trailing slash
 $dol_entry-&gt;resolve_path('some/../where/') =&gt; $dir_entry OR undef</pre>
<dt>name</p>
<dd>Returns the name of the file (relative to the package root). </p>
<p> <font SIZE="-1">NB:</font> It will never have any leading &#8220;./&#8221; (or &#8220;/&#8221;) in it.</p>
<dt>basename</p>
<dd>Returns the &#8220;filename&#8221; part of the name, similar <code><a href="/docs/linux/man/1-basename/">basename</a></code>(1) or File::Basename::basename (without passing a suffix to strip in either case). </p>
<p> <font SIZE="-1">NB:</font> Returns the empty string for the &#8220;root&#8221; dir.</p>
<dt>dirname</p>
<dd>Returns the &#8220;directory&#8221; part of the name, similar to <code><a href="/docs/linux/man/1-dirname/">dirname</a></code>(1) or File::Basename::dirname. The dirname will end with a trailing slash (except the &#8220;root&#8221; dir &#8211; see below). </p>
<p> <font SIZE="-1">NB:</font> Returns the empty string for the &#8220;root&#8221; dir.</p>
<dt>link</p>
<dd>If this is a link (i.e. is_symlink or is_hardlink returns a truth value), this method returns the target of the link. </p>
<p> If this is not a link, then this returns undef. </p>
<p> If the path is a symlink this method can be used to determine if the symlink is relative or absolute. This is <i>not</i> true for hardlinks, where the link target is always relative to the root. </p>
<p> <font SIZE="-1">NB:</font> Even for symlinks, a leading &#8220;./&#8221; will be stripped.</p>
<dt>normalized</p>
<dd>
<dt>faux</p>
<dd>Returns a truth value if this entry absent in the package. This can happen if a package does not include all intermediate directories.</p>
<dt>size</p>
<dd>Returns the size of the path in bytes. </p>
<p> <font SIZE="-1">NB:</font> Only regular files can have a non-zero file size.</p>
<dt>date</p>
<dd>Return the modification date as YYYY-MM-DD.</p>
<dt>time</p>
<dd>
<dt>perm</p>
<dd>
<dt>path_info</p>
<dd>
<dt>owner</p>
<dd>Returns the owner of the path entry as a username. </p>
<p> <font SIZE="-1">NB:</font> If only numerical owner information is available in the package, this may return a numerical owner (except uid 0 is always mapped to &#8220;root&#8221;)</p>
<dt>group</p>
<dd>Returns the group of the path entry as a username. </p>
<p> <font SIZE="-1">NB:</font> If only numerical owner information is available in the package, this may return a numerical group (except gid 0 is always mapped to &#8220;root&#8221;)</p>
<dt>uid</p>
<dd>Returns the uid of the owner of the path entry. </p>
<p> <font SIZE="-1">NB:</font> If the uid is not available, 0 will be returned. This usually happens if the numerical data is not collected (e.g. in source packages)</p>
<dt>gid</p>
<dd>Returns the gid of the owner of the path entry. </p>
<p> <font SIZE="-1">NB:</font> If the gid is not available, 0 will be returned. This usually happens if the numerical data is not collected (e.g. in source packages)</p>
<dt>file_info</p>
<dd>Return the data from <code><a href="/docs/linux/man/1-file/">file</a></code>(1) if it has been collected. </p>
<p> Note this is only defined for files as Lintian only runs <code><a href="/docs/linux/man/1-file/">file</a></code>(1) on files.</p>
<dt>java_info</p>
<dd>
<dt>script</p>
<dd>
<dt>strings</p>
<dd>
<dt>objdump</p>
<dd>
<dt>control</p>
<dd>
<dt>&quot;basedir&quot;</p>
<dd>
<dt>index</p>
<dd>
<dt>parent_dir</p>
<dd>
<dt>child_table</p>
<dd>
<dt>sorted_children</p>
<dd>Returns the parent directory entry of this entry as a Lintian::File::Path. </p>
<p> <font SIZE="-1">NB:</font> Returns <tt>&quot;undef&quot;</tt> for the &#8220;root&#8221; dir.</p>
<dt>&quot;childnames&quot;</p>
<dd>
<dt>parent_dir</p>
<dd>Return the parent dir entry of this the path entry.</p>
<dt>dereferenced</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
