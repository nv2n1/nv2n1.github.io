---
title: "lintianlabmanifest(3)"
name: "lintianlabmanifest"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianlabmanifest/"
---

Lintian::Lab::Manifest -- Lintian Lab manifest 

<h2>Synopsis</h2><pre> use Lintian::Lab::Manifest;
 my $plist = Lintian::Lab::Manifest-&gt;new ('binary');
 # Read the file
 $plist-&gt;read_list('info/binary-packages');
 # fetch the entry for lintian (if any)
 my $entry = $plist-&gt;get('lintian', '2.5.2', 'all');
 if ( $entry &amp;&amp; exits $entry-&gt;{'version'} ) {
 print &quot;Lintian has version $entry-&gt;{'version'}\n&quot;;
 }
 # delete all lintian entries
 $plist-&gt;delete('lintian');
 # Write to file if changed
 if ($plist-&gt;dirty) {
 $plist-&gt;write_list('info/binary-packages');
 }</pre><h2>Description</h2>Instances of this class provide access to the packages list used by the lab as caches. 

 The data structure is basically a tree (using hashes). For binaries is looks (something) like: 

 <pre> $self-&gt;{'state'}{$name}{$version}{$architecture}</pre>The (order of the) fields used in the tree are listed in the @{BIN,SRC,CHG}_QUERY lists below. The fields may (and generally do) differ between package types.
<h2>Class Methods</h2><dl COMPACT><dt>new (TYPE[, GROUPING])
</dt><dd>Creates a new packages list for a certain type of packages. This type defines the format of the files. 
 The known types are: 
&nbsp;*&nbsp;binary 
&nbsp;*&nbsp;changes 
&nbsp;*&nbsp;source 
&nbsp;*&nbsp;udeb 
&nbsp;*&nbsp;GROUP 
 If TYPE is GROUP, then GROUPING should be omitted.</dd></dl><h2>Instance Methods</h2><dl COMPACT><dt>dirty
</dt><dd>Returns a truth value if the manifest has changed since it was last written.
</dd><dt>type
</dt><dd>Returns the type of packages that this manifest has information about. (one of binary, udeb, source or changes)
</dd><dt>read_list (FILE)
</dt><dd>Reads a manifest from FILE. Any records already in the manifest will be discarded before reading the contents. 
 On success, this will clear the ``dirty'' flag and on error it will croak.
</dd><dt>write_list (FILE)
</dt><dd>Writes the manifest to FILE. 
 On success, this will clear the ``dirty'' flag and on error it will croak. 
 On error, the contents of FILE are undefined.
</dd><dt>visit_all (VISITOR[, KEY1, ..., KEYN])
</dt><dd>Visits entries and passes them to VISITOR. If any keys are passed they are used to reduce the search. See get for a list of (common) keys. 
 The VISITOR is called as: 
 <pre> VISITOR-&gt;(ENTRY, KEYS)</pre>where ENTRY is the entry and KEYS are the keys to be used to look up this entry via get method. So for the lintian 2.5.2 binary the keys would be something like: 
&nbsp;('lintian',&nbsp;'2.5.2',&nbsp;'all')
</dd><dt>get (KEYS...)
</dt><dd>Fetches the entry for KEYS (if any). Returns <tt>&quot;undef&quot;</tt> if the entry is not known. If KEYS is exactly one item, it is assumed to be a Lintian::Processable and the correct keys are extracted from it. 
 Otherwise, the keys are (in general and in order):
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>package/source
</dt><dd></dd><dt>version
</dt><dd></dd><dt>architecture
</dt><dd>except for source packages</dd></dl></dl><dl COMPACT><dd></dd></dl><dt>set (ENTRY)
</dt><dd>Inserts ENTRY into the manifest. This may replace an existing entry. 

 Note: The interesting fields from ENTRY are copied, so later changes to ENTRY will not affect the data in the manifest.
</dd><dt>set_transient_marker (TRANSIENT, KEYS...)
</dt><dd>Set or clear transient flag. Transient entries are not written to the disk (i.e. They will not appear in the file created/written by ``write_list (FILE)''). KEYS is passed as is passed to ``get (KEYS...)''. 

 By default all entries are persistent.
</dd><dt>delete (KEYS...)
</dt><dd>Removes the entry/entries found by KEYS (if any). KEYS must contain at least one item - if the list of keys cannot uniquely identify a single element, all ``matching'' elements will be removed. Examples: 

 <pre> # Delete the gcc-4.6 entry at version 4.6.1-4 that is also architecture i386
 $manifest-&gt;delete ('gcc-4.6', '4.6.1-4', 'i386');
 # Delete all gcc-4.6 entries at version 4.6.1-4 regardless of their
 # architecture
 $manifest-&gt;delete ('gcc-4.6', '4.6.1-4');
 # Delete all gcc-4.6 entries regardless of version and architecture
 $manifest-&gt;delete ('gcc-4.6')</pre>If KEYS is exactly one item, it is assumed to be a Lintian::Processable. If so, the proper keys will be extracted from that processable and (if present) that one element will be removed. 

 This will mark the list as dirty if an element was removed. If it returns a truth value, an element was removed - otherwise it will return 0. 

 See ``get (KEYS...)'' for the key names.
</dd><dt>diff (MANIFEST)
</dt><dd>Returns a diff between this manifest and MANIFEST. 

 This instance is considered the ``original'' and MANIFEST is ``new'' version of the manifest. (See the olist and nlist methods of Lintian::Lab::ManifestDiff for more information.</dd></dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1)
