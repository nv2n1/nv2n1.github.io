---
title: "lintianpath(3)"
name: "lintianpath"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianpath/"
---

Lintian::Path - Lintian representation of a path entry in a package 

<h2>Synopsis</h2><pre> my ($name, $type, $dir) = ('lintian', 'source', '/path/to/entry');
 my $info = Lintian::Collect-&gt;new ($name, $type, $dir);
 my $path = $info-&gt;index('bin/ls');
 if ($path-&gt;is_file) {
 # is file (or hardlink)
 if ($path-&gt;is_hardlink) { }
 if ($path-&gt;is_regular_file) { }
 } elsif ($path-&gt;is_dir) {
 # is dir
 if ($path-&gt;owner eq 'root') { }
 if ($path-&gt;group eq 'root') { }
 } elsif ($path-&gt;is_symlink) {
 my $normalized = $path-&gt;link_normalized;
 if (defined($normalized)) {
 my $more_info = $info-&gt;index($normalized);
 if (defined($more_info)) {
 # target exists in the package...
 }
 }
 }</pre><h2>Instance Methods</h2><dl COMPACT><dt>Lintian::Path-&gt;new ($data)
</dt><dd>Internal constructor (used by Lintian::Collect::Package). 
 Argument is a hash containing the data read from the index file.
</dd><dt>name
</dt><dd>Returns the name of the file (relative to the package root). 
 NB: It will never have any leading ``./'' (or ``/'') in it.
</dd><dt>owner
</dt><dd>Returns the owner of the path entry as a username. 
 NB: If only numerical owner information is available in the package, this may return a numerical owner (except uid 0 is always mapped to ``root'')
</dd><dt>group
</dt><dd>Returns the group of the path entry as a username. 
 NB: If only numerical owner information is available in the package, this may return a numerical group (except gid 0 is always mapped to ``root'')
</dd><dt>uid
</dt><dd>Returns the uid of the owner of the path entry. 
 NB: If the uid is not available, 0 will be returned. This usually happens if the numerical data is not collected (e.g. in source packages)
</dd><dt>gid
</dt><dd>Returns the gid of the owner of the path entry. 
 NB: If the gid is not available, 0 will be returned. This usually happens if the numerical data is not collected (e.g. in source packages)
</dd><dt>link
</dt><dd>If this is a link (i.e. is_symlink or is_hardlink returns a truth value), this method returns the target of the link. 
 If this is not a link, then this returns undef. 
 If the path is a symlink this method can be used to determine if the symlink is relative or absolute. This is <i>not</i> true for hardlinks, where the link target is always relative to the root. 
 NB: Even for symlinks, a leading ``./'' will be stripped.
</dd><dt>size
</dt><dd>Returns the size of the path in bytes. 
 NB: Only regular files can have a non-zero file size.
</dd><dt>date
</dt><dd>Return the modification date as YYYY-MM-DD.
</dd><dt>parent_dir
</dt><dd>Returns the parent directory entry of this entry as a Lintian::Path. 
 NB: Returns <tt>&quot;undef&quot;</tt> for the ``root'' dir.
</dd><dt>dirname
</dt><dd>Returns the ``directory'' part of the name, similar to <i><a HREF="/docs/linux/man/1-dirname/">dirname</a></i>(1) or File::Basename::dirname. The dirname will end with a trailing slash (except the ``root'' dir - see below). 
 NB: Returns the empty string for the ``root'' dir.
</dd><dt>basename
</dt><dd>Returns the ``filename'' part of the name, similar <i><a HREF="/docs/linux/man/1-basename/">basename</a></i>(1) or File::Basename::basename (without passing a suffix to strip in either case). For dirs, the basename will end with a trailing slash (except for the ``root'' dir - see below). 
 NB: Returns the empty string for the ``root'' dir.
</dd><dt>faux
</dt><dd>Returns a truth value if this entry absent in the package. This can happen if a package does not include all intermediate directories.
</dd><dt>operm
</dt><dd>Returns the file permissions of this object in octal (e.g. 0644). 
 NB: This is only well defined for file entries that are subject to permissions (e.g. files). Particularly, the value is not well defined for symlinks.
</dd><dt>children([RECURSIVE_MODE])
</dt><dd>Returns a list of children (as Lintian::Path objects) of this entry. The list and its contents should not be modified. 
 The optional RECURSIVE_MODE parameter can be used to control if and how descendants of this directory is selected. The following values are supported:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>direct
</dt><dd>This is the default and only returns direct children of this directory. The entries are sorted by name.
</dd><dt>breadth-first
</dt><dd>Recursive into subdirectories and return the descendants in breadth-first order. Children of a given directory will be sorted by name.</dd></dl></dl><dl COMPACT><dd>NB: Returns the empty list for non-dir entries.</dd></dl><dt>timestamp
</dt><dd>Returns a Unix timestamp for the given path. This is a number of seconds since the start of Unix epoch in UTC.
</dd><dt>child(BASENAME)
</dt><dd>Returns the child named BASENAME if it is a child of this directory. Otherwise, this method returns <tt>&quot;undef&quot;</tt>. Note if BASENAME has a trailing slash, the child entry must be a directory. If the child exist, but is not a directory, <tt>&quot;undef&quot;</tt> will be returned instead. 

 For non-dirs, this method always returns <tt>&quot;undef&quot;</tt>. 

 Example: 

 <pre> $dir_entry-&gt;child('foo') =&gt; $entry OR undef
 $dir_entry-&gt;child('foo/') =&gt; $dir_entry OR undef</pre></dd><dt>is_symlink
</dt><dd>Returns a truth value if this entry is a symlink.
</dd><dt>is_hardlink
</dt><dd>Returns a truth value if this entry is a hardlink to a regular file. 

 NB: The target of a hardlink is always a regular file (and not a dir etc.).
</dd><dt>is_dir
</dt><dd>Returns a truth value if this entry is a dir. 

 NB: Unlike the ``-d <tt>$dir</tt>'' operator this will never return true for symlinks, even if the symlink points to a dir.
</dd><dt>is_file
</dt><dd>Returns a truth value if this entry is a regular file (or a hardlink to one). 

 NB: Unlike the ``-f <tt>$file</tt>'' operator this will never return true for symlinks, even if the symlink points to a file (or hardlink).
</dd><dt>is_regular_file
</dt><dd>Returns a truth value if this entry is a regular file. 

 This is eqv. to <tt>$path</tt>-&gt;is_file and not <tt>$path</tt>-&gt;is_hardlink. 

 NB: Unlike the ``-f <tt>$file</tt>'' operator this will never return true for symlinks, even if the symlink points to a file.
</dd><dt>link_normalized
</dt><dd>Returns the target of the link normalized against it's directory name. If the link cannot be normalized or normalized path might escape the package root, this method returns <tt>&quot;undef&quot;</tt>. 

 NB: This method will return the empty string for links pointing to the root dir of the package. 

 Only available on ``links'' (i.e. symlinks or hardlinks). On non-links this will croak. 

 <i>Symlinks only</i>: If you want the symlink target as a Lintian::Path object, use the resolve_path method with no arguments instead.
</dd><dt>is_readable
</dt><dd>Returns a truth value if the permission bits of this entry have at least one bit denoting readability set (bitmask 0444).
</dd><dt>is_writable
</dt><dd>Returns a truth value if the permission bits of this entry have at least one bit denoting writability set (bitmask 0222).
</dd><dt>is_executable
</dt><dd>Returns a truth value if the permission bits of this entry have at least one bit denoting executability set (bitmask 0111).
</dd><dt>file_info
</dt><dd>Return the data from <i><a HREF="/docs/linux/man/1-file/">file</a></i>(1) if it has been collected. 

 Note this is only defined for files as Lintian only runs <i><a HREF="/docs/linux/man/1-file/">file</a></i>(1) on files.
</dd><dt>fs_path
</dt><dd>Returns the path to this object on the file system, which must be a regular file, a hardlink or a directory. 

 This method may fail if:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>&bull;
</dt><dd>The object is neither a directory or a file-like object (e.g. a named pipe).
</dd><dt>&bull;
</dt><dd>If the object is dangling symlink or the path traverses a symlink outside the package root.</dd></dl></dl><dl COMPACT><dd>To test if this is safe to call, if the target is (supposed) to be a:
</dd><dl COMPACT><dt>&bull;
</dt><dd>file or hardlink then test with ``is_open_ok''.
</dd><dt>&bull;
</dt><dd>dir then assert resolve_path returns a defined entry, for which ``is_dir'' returns a truth value.</dd></dl></dl><dl COMPACT><dd></dd></dl><dt>is_open_ok
</dt><dd>Returns a truth value if it is safe to attempt open a read handle to the underlying file object. 

 Returns a truth value if the path may be opened.
</dd><dt>open([LAYER])
</dt><dd>Open and return a read handle to the file. It optionally accepts the LAYER argument. If given it should specify the layer/discipline to use when opening the file including the initial colon (e.g. ':raw'). 

 Beyond regular issues with opening a file, this method may fail if:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>&bull;
</dt><dd>The object is not a file-like object (e.g. a directory or a named pipe).
</dd><dt>&bull;
</dt><dd>If the object is dangling symlink or the path traverses a symlink outside the package root.</dd></dl></dl><dl COMPACT><dd>It is possible to test for these by using ``is_open_ok''.</dd></dl><dt>open_gz
</dt><dd>Open a read handle to the file and decompress it as a GZip compressed file. This method may fail for the same reasons as ``open([LAYER])''. 

 The returned handle may be a pipe from an external process.
</dd><dt>file_contents
</dt><dd>Return the file contents as a scalar. 

 This method may fail for the same reasons as ``open([LAYER])''.
</dd><dt>root_dir
</dt><dd>Return the root dir entry of this the path entry.
</dd><dt>resolve_path([PATH])
</dt><dd>Resolve PATH relative to this path entry. 

 If PATH starts with a slash and the file hierarchy has a well-defined root directory, then PATH will instead be resolved relatively to the root dir. If the file hierarchy does not have a well-defined root dir (e.g. for source packages), this method will return <tt>&quot;undef&quot;</tt>. 

 If PATH is omitted, then the entry is resolved and the target is returned if it is valid. Except for symlinks, all entries always resolve to themselves. NB: hardlinks also resolve as themselves. 

 It is an error to attempt to resolve a PATH against a non-directory and non-symlink entry - as such resolution would always fail (i.e. foo/../bar is an invalid path unless foo is a directory or a symlink to a dir). 

 The resolution takes symlinks into account and following them provided that the target path is valid (and can be followed safely). If the path is invalid or circular (symlinks), escapes the root directory or follows an unsafe symlink, the method returns <tt>&quot;undef&quot;</tt>. Otherwise, it returns the path entry that denotes the target path. 

 If PATH contains at least one path segment and ends with a slash, then the resolved path will end in a directory (or fail). Otherwise, the resolved PATH can end in any entry <i>except</i> a symlink. 

 Examples: 

 <pre> $symlink_entry-&gt;resolve_path =&gt; $nonsymlink_entry OR undef
 $x-&gt;resolve_path =&gt; $x
 For directory or symlink entries (dol), you can also resolve a path:
 $dol_entry-&gt;resolve_path('some/../where') =&gt; $nonsymlink_entry OR undef
 # Note the trailing slash
 $dol_entry-&gt;resolve_path('some/../where/') =&gt; $dir_entry OR undef</pre></dd></dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i>Lintian::Collect</i>(3), <i>Lintian::Collect::Binary</i>(3), <i>Lintian::Collect::Source</i>(3)
