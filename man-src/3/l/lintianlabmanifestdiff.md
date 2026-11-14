---
title: "lintianlabmanifestdiff(3)"
name: "lintianlabmanifestdiff"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianlabmanifestdiff/"
---

Lintian::Lab::ManifestDiff -- Difference representation between two Manifests 

<h2>Synopsis</h2><pre> use Lintian::Lab::Manifest;
 
 my $olist = Lintian::Lab::Manifest-&gt;new ('binary');
 my $nlist = Lintian::Lab::Manifest-&gt;new ('binary');
 $olist-&gt;read_list ('old/binary-packages');
 $nlist-&gt;read_list ('new/binary-packages');
 my $diff = $olist-&gt;diff($nlist);
 foreach my $added (@{ $diff-&gt;added }) {
 my $entry = $nlist-&gt;get (@$added);
 # do something
 }
 foreach my $removed (@{ $diff-&gt;removed }) {
 my $entry = $olist-&gt;get (@$removed);
 # do something
 }
 foreach my $changed (@{ $diff-&gt;changed }) {
 my $oentry = $olist-&gt;get (@$changed);
 my $nentry = $nlist-&gt;get (@$changed);
 # use/diff $oentry and $nentry as needed
 }</pre><h2>Description</h2>Instances of this class provides access to the packages list used by the Lab as caches.
<h2>Methods</h2><dl COMPACT><dt>$diff-&gt;added
<dd>Returns a listref containing the keys of the elements that has been added. 

 Each element is a listref of keys; this list (when dereferenced) can be used with the manifest's get method to look up the item.
<dt>$diff-&gt;removed
<dd>Returns a listref containing the keys of the elements that has been removed. 

 Each element is a listref of keys; this list (when dereferenced) can be used with the manifest's get method to look up the item.
<dt>$diff-&gt;changed
<dd>Returns a listref containing the keys of the elements that has been changed. 

 Each element is a listref of keys; this list (when dereferenced) can be used with the manifest's get method to look up the item.
<dt>$diff-&gt;nlist
<dd>Returns the ``new'' manifest used to create this diff. Note the manifest is not copied and may have been changed since the diff has been created.
<dt>$diff-&gt;olist
<dd>Returns the ``orig'' manifest used to create this diff. Note the manifest is not copied and may have been changed since the diff has been created.</dl>
 

 Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1)
