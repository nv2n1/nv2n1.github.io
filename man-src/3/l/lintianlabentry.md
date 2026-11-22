---
title: "lintianlabentry(3)"
name: "lintianlabentry"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianlabentry/"
---

Lintian::Lab::Entry - A package inside the Lab 

<h2>Synopsis</h2><pre> use Lintian::Lab;
 my $lab = Lintian::Lab-&gt;new (&quot;dir&quot;);
 my $lpkg = $lab-&gt;get_package (&quot;name&quot;, &quot;type&quot;, &quot;version&quot;, &quot;arch&quot;);
 # create the entry
 $lpkg-&gt;create;
 # obtain a Lintian::Collect object.
 my $info = $lpkg-&gt;info;
 $lpkg-&gt;clear_cache;
 # Remove package from lab.
 $lpkg-&gt;remove;</pre><h2>Description</h2>This module provides basic access and manipulation about an entry (i.e. processable) stored in the Lab. Instances of this class are not created directly, instead they are returned by various methods from Lintian::Lab.
<h2>Class Methods</h2><dl COMPACT><dt>new_from_metadata (PKG_TYPE, METADATA, LAB, BASEDIR)
</dt><dd>Overrides same constructor in Lintian::Processable. 
 Used by Lintian::Lab to load an existing entry from the lab.</dd></dl><h2>Instance Methods</h2><dl COMPACT><dt>base_dir
</dt><dd>Returns the base directory of this package inside the lab.
</dd><dt>lab
</dt><dd>Returns a reference to the laboratory related to this entry.
</dd><dt>from_lab (LAB)
</dt><dd>Returns a truth value if this entry is from LAB.
</dd><dt>info
</dt><dd>Returns the info object associated with this entry. 
 Overrides info from Lintian::Processable.
</dd><dt>clear_cache
</dt><dd>Clears any caches held; this includes discarding the info object. 
 Overrides clear_cache from Lintian::Processable.
</dd><dt>remove
</dt><dd>Removes all unpacked parts of the package in the lab. Returns a truth value if successful.
</dd><dt>exists
</dt><dd>Returns a truth value if the entry exists.
</dd><dt>create
</dt><dd>Creates a minimum entry, in which collections and checks can be run. Note if it already exists, then this will do nothing.
</dd><dt>coll_version (COLL)
</dt><dd>Returns the version of the collection named COLL, if that COLL has been marked as finished. 
 Returns the empty string if COLL has not been marked as finished. 
 Note: The version can be 0.
</dd><dt>is_coll_finished (COLL, VERSION)
</dt><dd>Returns a truth value if the collection COLL has been completed and its version is at least VERSION. The versions are assumed to be integers (the comparison is performed with ``&gt;=''). 
 This returns 0 if the collection COLL has not been marked as finished.
</dd><dt>update_status_file
</dt><dd>Flushes the cached changes of which collections have been completed. 
 This should also be called for new entries to create the status file.</dd></dl><h2>Author</h2>Niels Thykier &lt;niels [at] thykier.net&gt;
