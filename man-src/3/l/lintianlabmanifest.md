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

 <pre> $self-&gt;{'state'}{$name}{$version}{$architecture}</pre>The (order of the) fields used in the tree are listed in the @{<font SIZE="-1">BIN,SRC,CHG</font>}_QUERY lists below. The fields may (and generally do) differ between package types.
<h2>Class Methods</h2><dl COMPACT><dt>new (TYPE[, <font SIZE="-1">GROUPING</font>])
<dd>Creates a new packages list for a certain type of packages. This type defines the format of the files. 

 The known types are: 
&nbsp;*&nbsp;binary 
&nbsp;*&nbsp;changes 
&nbsp;*&nbsp;source 
&nbsp;*&nbsp;udeb 
&nbsp;*&nbsp;<font SIZE="-1">GROUP</font> 

 If <font SIZE="-1">TYPE</font> is <font SIZE="-1">GROUP,</font> then <font SIZE="-1">GROUPING</font> should be omitted.</dl><h2>Instance Methods</h2><dl COMPACT><dt>dirty
<dd>Returns a truth value if the manifest has changed since it was last written.
<dt>type
<dd>Returns the type of packages that this manifest has information about. (one of binary, udeb, source or changes)
<dt>read_list (<font SIZE="-1">FILE</font>)
<dd>Reads a manifest from <font SIZE="-1">FILE.</font> Any records already in the manifest will be discarded before reading the contents. 

 On success, this will clear the ``dirty'' flag and on error it will croak.
<dt>write_list (<font SIZE="-1">FILE</font>)
<dd>Writes the manifest to <font SIZE="-1">FILE.</font> 

 On success, this will clear the ``dirty'' flag and on error it will croak. 

 On error, the contents of <font SIZE="-1">FILE</font> are undefined.
<dt>visit_all (VISITOR[, <font SIZE="-1">KEY1, ..., KEYN</font>])
<dd>Visits entries and passes them to <font SIZE="-1">VISITOR.</font> If any keys are passed they are used to reduce the search. See get for a list of (common) keys. 

 The <font SIZE="-1">VISITOR</font> is called as: 

 <pre> VISITOR-&gt;(ENTRY, KEYS)</pre>where <font SIZE="-1">ENTRY</font> is the entry and <font SIZE="-1">KEYS</font> are the keys to be used to look up this entry via get method. So for the lintian 2.5.2 binary the keys would be something like: 
&nbsp;('lintian',&nbsp;'2.5.2',&nbsp;'all')
<dt>get (<font SIZE="-1">KEYS...</font>)
<dd>Fetches the entry for <font SIZE="-1">KEYS</font> (if any). Returns <tt>&quot;undef&quot;</tt> if the entry is not known. If <font SIZE="-1">KEYS</font> is exactly one item, it is assumed to be a Lintian::Processable and the correct keys are extracted from it. 

 Otherwise, the keys are (in general and in order):
<dl COMPACT><dd><dl COMPACT><dt>package/source
<dd><dt>version
<dd><dt>architecture
<dd>except for source packages</dl></dl><dl COMPACT><dd></dl><dt>set (<font SIZE="-1">ENTRY</font>)
<dd>Inserts <font SIZE="-1">ENTRY</font> into the manifest. This may replace an existing entry. 

 Note: The interesting fields from <font SIZE="-1">ENTRY</font> are copied, so later changes to <font SIZE="-1">ENTRY</font> will not affect the data in the manifest.
<dt>set_transient_marker (<font SIZE="-1">TRANSIENT, KEYS...</font>)
<dd>Set or clear transient flag. Transient entries are not written to the disk (i.e. They will not appear in the file created/written by ``write_list (<font SIZE="-1">FILE</font>)''). <font SIZE="-1">KEYS</font> is passed as is passed to ``get (<font SIZE="-1">KEYS...</font>)''. 

 By default all entries are persistent.
<dt>delete (<font SIZE="-1">KEYS...</font>)
<dd>Removes the entry/entries found by <font SIZE="-1">KEYS</font> (if any). <font SIZE="-1">KEYS</font> must contain at least one item - if the list of keys cannot uniquely identify a single element, all ``matching'' elements will be removed. Examples: 

 <pre> # Delete the gcc-4.6 entry at version 4.6.1-4 that is also architecture i386
 $manifest-&gt;delete ('gcc-4.6', '4.6.1-4', 'i386');
 
 # Delete all gcc-4.6 entries at version 4.6.1-4 regardless of their
 # architecture
 $manifest-&gt;delete ('gcc-4.6', '4.6.1-4');
 
 # Delete all gcc-4.6 entries regardless of version and architecture
 $manifest-&gt;delete ('gcc-4.6')</pre>If <font SIZE="-1">KEYS</font> is exactly one item, it is assumed to be a Lintian::Processable. If so, the proper keys will be extracted from that processable and (if present) that one element will be removed. 

 This will mark the list as dirty if an element was removed. If it returns a truth value, an element was removed - otherwise it will return 0. 

 See ``get (<font SIZE="-1">KEYS...</font>)'' for the key names.
<dt>diff (<font SIZE="-1">MANIFEST</font>)
<dd>Returns a diff between this manifest and <font SIZE="-1">MANIFEST.</font> 

 This instance is considered the ``original'' and <font SIZE="-1">MANIFEST</font> is ``new'' version of the manifest. (See the olist and nlist methods of Lintian::Lab::ManifestDiff for more information.</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1)
