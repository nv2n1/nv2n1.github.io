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
<dd>Internal constructor (used by Lintian::Collect::Package). 

 Argument is a hash containing the data read from the index file.
<dt>name
<dd>Returns the name of the file (relative to the package root). 

 <font SIZE="-1">NB:</font> It will never have any leading ``./'' (or ``/'') in it.
<dt>owner
<dd>Returns the owner of the path entry as a username. 

 <font SIZE="-1">NB:</font> If only numerical owner information is available in the package, this may return a numerical owner (except uid 0 is always mapped to ``root'')
<dt>group
<dd>Returns the group of the path entry as a username. 

 <font SIZE="-1">NB:</font> If only numerical owner information is available in the package, this may return a numerical group (except gid 0 is always mapped to ``root'')
<dt>uid
<dd>Returns the uid of the owner of the path entry. 

 <font SIZE="-1">NB:</font> If the uid is not available, 0 will be returned. This usually happens if the numerical data is not collected (e.g. in source packages)
<dt>gid
<dd>Returns the gid of the owner of the path entry. 

 <font SIZE="-1">NB:</font> If the gid is not available, 0 will be returned. This usually happens if the numerical data is not collected (e.g. in source packages)
<dt>link
<dd>If this is a link (i.e. is_symlink or is_hardlink returns a truth value), this method returns the target of the link. 

 If this is not a link, then this returns undef. 

 If the path is a symlink this method can be used to determine if the symlink is relative or absolute. This is <i>not</i> true for hardlinks, where the link target is always relative to the root. 

 <font SIZE="-1">NB:</font> Even for symlinks, a leading ``./'' will be stripped.
<dt>size
<dd>Returns the size of the path in bytes. 

 <font SIZE="-1">NB:</font> Only regular files can have a non-zero file size.
<dt>date
<dd>Return the modification date as YYYY-MM-DD.
<dt>parent_dir
<dd>Returns the parent directory entry of this entry as a Lintian::Path. 

 <font SIZE="-1">NB:</font> Returns <tt>&quot;undef&quot;</tt> for the ``root'' dir.
<dt>dirname
<dd>Returns the ``directory'' part of the name, similar to <i><a HREF="/docs/linux/man/1-dirname/">dirname</a></i>(1) or File::Basename::dirname. The dirname will end with a trailing slash (except the ``root'' dir - see below). 

 <font SIZE="-1">NB:</font> Returns the empty string for the ``root'' dir.
<dt>basename
<dd>Returns the ``filename'' part of the name, similar <i><a HREF="/docs/linux/man/1-basename/">basename</a></i>(1) or File::Basename::basename (without passing a suffix to strip in either case). For dirs, the basename will end with a trailing slash (except for the ``root'' dir - see below). 

 <font SIZE="-1">NB:</font> Returns the empty string for the ``root'' dir.
<dt>faux
<dd>Returns a truth value if this entry absent in the package. This can happen if a package does not include all intermediate directories.
<dt>operm
<dd>Returns the file permissions of this object in octal (e.g. 0644). 

 <font SIZE="-1">NB:</font> This is only well defined for file entries that are subject to permissions (e.g. files). Particularly, the value is not well defined for symlinks.
<dt>children([<font SIZE="-1">RECURSIVE_MODE</font>])
<dd>Returns a list of children (as Lintian::Path objects) of this entry. The list and its contents should not be modified. 

 The optional <font SIZE="-1">RECURSIVE_MODE</font> parameter can be used to control if and how descendants of this directory is selected. The following values are supported:
<dl COMPACT><dd><dl COMPACT><dt>direct
<dd>This is the default and only returns direct children of this directory. The entries are sorted by name.
<dt>breadth-first
<dd>Recursive into subdirectories and return the descendants in breadth-first order. Children of a given directory will be sorted by name.</dl></dl><dl COMPACT><dd><font SIZE="-1">NB:</font> Returns the empty list for non-dir entries.</dl><dt>timestamp
<dd>Returns a Unix timestamp for the given path. This is a number of seconds since the start of Unix epoch in <font SIZE="-1">UTC.</font>
<dt>child(<font SIZE="-1">BASENAME</font>)
<dd>Returns the child named <font SIZE="-1">BASENAME</font> if it is a child of this directory. Otherwise, this method returns <tt>&quot;undef&quot;</tt>. Note if <font SIZE="-1">BASENAME</font> has a trailing slash, the child entry must be a directory. If the child exist, but is not a directory, <tt>&quot;undef&quot;</tt> will be returned instead. 

 For non-dirs, this method always returns <tt>&quot;undef&quot;</tt>. 

 Example: 

 <pre> $dir_entry-&gt;child('foo') =&gt; $entry OR undef
 $dir_entry-&gt;child('foo/') =&gt; $dir_entry OR undef</pre><dt>is_symlink
<dd>Returns a truth value if this entry is a symlink.
<dt>is_hardlink
<dd>Returns a truth value if this entry is a hardlink to a regular file. 

 <font SIZE="-1">NB:</font> The target of a hardlink is always a regular file (and not a dir etc.).
<dt>is_dir
<dd>Returns a truth value if this entry is a dir. 

 <font SIZE="-1">NB:</font> Unlike the ``-d <tt>$dir</tt>'' operator this will never return true for symlinks, even if the symlink points to a dir.
<dt>is_file
<dd>Returns a truth value if this entry is a regular file (or a hardlink to one). 

 <font SIZE="-1">NB:</font> Unlike the ``-f <tt>$file</tt>'' operator this will never return true for symlinks, even if the symlink points to a file (or hardlink).
<dt>is_regular_file
<dd>Returns a truth value if this entry is a regular file. 

 This is eqv. to <tt>$path</tt>-&gt;is_file and not <tt>$path</tt>-&gt;is_hardlink. 

 <font SIZE="-1">NB:</font> Unlike the ``-f <tt>$file</tt>'' operator this will never return true for symlinks, even if the symlink points to a file.
<dt>link_normalized
<dd>Returns the target of the link normalized against it's directory name. If the link cannot be normalized or normalized path might escape the package root, this method returns <tt>&quot;undef&quot;</tt>. 

 <font SIZE="-1">NB:</font> This method will return the empty string for links pointing to the root dir of the package. 

 Only available on ``links'' (i.e. symlinks or hardlinks). On non-links this will croak. 

 <i>Symlinks only</i>: If you want the symlink target as a Lintian::Path object, use the resolve_path method with no arguments instead.
<dt>is_readable
<dd>Returns a truth value if the permission bits of this entry have at least one bit denoting readability set (bitmask 0444).
<dt>is_writable
<dd>Returns a truth value if the permission bits of this entry have at least one bit denoting writability set (bitmask 0222).
<dt>is_executable
<dd>Returns a truth value if the permission bits of this entry have at least one bit denoting executability set (bitmask 0111).
<dt>file_info
<dd>Return the data from <i><a HREF="/docs/linux/man/1-file/">file</a></i>(1) if it has been collected. 

 Note this is only defined for files as Lintian only runs <i><a HREF="/docs/linux/man/1-file/">file</a></i>(1) on files.
<dt>fs_path
<dd>Returns the path to this object on the file system, which must be a regular file, a hardlink or a directory. 

 This method may fail if:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The object is neither a directory or a file-like object (e.g. a named pipe).
<dt>&bull;
<dd>If the object is dangling symlink or the path traverses a symlink outside the package root.</dl></dl><dl COMPACT><dd>To test if this is safe to call, if the target is (supposed) to be a:
<dl COMPACT><dt>&bull;
<dd>file or hardlink then test with ``is_open_ok''.
<dt>&bull;
<dd>dir then assert resolve_path returns a defined entry, for which ``is_dir'' returns a truth value.</dl></dl><dl COMPACT><dd></dl><dt>is_open_ok
<dd>Returns a truth value if it is safe to attempt open a read handle to the underlying file object. 

 Returns a truth value if the path may be opened.
<dt>open([<font SIZE="-1">LAYER</font>])
<dd>Open and return a read handle to the file. It optionally accepts the <font SIZE="-1">LAYER</font> argument. If given it should specify the layer/discipline to use when opening the file including the initial colon (e.g. ':raw'). 

 Beyond regular issues with opening a file, this method may fail if:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The object is not a file-like object (e.g. a directory or a named pipe).
<dt>&bull;
<dd>If the object is dangling symlink or the path traverses a symlink outside the package root.</dl></dl><dl COMPACT><dd>It is possible to test for these by using ``is_open_ok''.</dl><dt>open_gz
<dd>Open a read handle to the file and decompress it as a GZip compressed file. This method may fail for the same reasons as ``open([<font SIZE="-1">LAYER</font>])''. 

 The returned handle may be a pipe from an external process.
<dt>file_contents
<dd>Return the file contents as a scalar. 

 This method may fail for the same reasons as ``open([<font SIZE="-1">LAYER</font>])''.
<dt>root_dir
<dd>Return the root dir entry of this the path entry.
<dt>resolve_path([<font SIZE="-1">PATH</font>])
<dd>Resolve <font SIZE="-1">PATH</font> relative to this path entry. 

 If <font SIZE="-1">PATH</font> starts with a slash and the file hierarchy has a well-defined root directory, then <font SIZE="-1">PATH</font> will instead be resolved relatively to the root dir. If the file hierarchy does not have a well-defined root dir (e.g. for source packages), this method will return <tt>&quot;undef&quot;</tt>. 

 If <font SIZE="-1">PATH</font> is omitted, then the entry is resolved and the target is returned if it is valid. Except for symlinks, all entries always resolve to themselves. <font SIZE="-1">NB:</font> hardlinks also resolve as themselves. 

 It is an error to attempt to resolve a <font SIZE="-1">PATH</font> against a non-directory and non-symlink entry - as such resolution would always fail (i.e. foo/../bar is an invalid path unless foo is a directory or a symlink to a dir). 

 The resolution takes symlinks into account and following them provided that the target path is valid (and can be followed safely). If the path is invalid or circular (symlinks), escapes the root directory or follows an unsafe symlink, the method returns <tt>&quot;undef&quot;</tt>. Otherwise, it returns the path entry that denotes the target path. 

 If <font SIZE="-1">PATH</font> contains at least one path segment and ends with a slash, then the resolved path will end in a directory (or fail). Otherwise, the resolved <font SIZE="-1">PATH</font> can end in any entry <i>except</i> a symlink. 

 Examples: 

 <pre> $symlink_entry-&gt;resolve_path =&gt; $nonsymlink_entry OR undef
 $x-&gt;resolve_path =&gt; $x
 For directory or symlink entries (dol), you can also resolve a path:
 $dol_entry-&gt;resolve_path('some/../where') =&gt; $nonsymlink_entry OR undef
 # Note the trailing slash
 $dol_entry-&gt;resolve_path('some/../where/') =&gt; $dir_entry OR undef</pre></dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--collect/">Lintian::Collect</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect--binary/">Lintian::Collect::Binary</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect--source/">Lintian::Collect::Source</a></i>(3)
