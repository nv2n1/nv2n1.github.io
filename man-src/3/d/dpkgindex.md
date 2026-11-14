---
title: "dpkgindex(3)"
name: "dpkgindex"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgindex/"
---

Dpkg::Index - generic index of control information 

<h2>Description</h2>This object represent a set of Dpkg::Control objects.
<h2>Functions</h2><dl COMPACT><dt>my $index = Dpkg::Index-&gt;new(%opts)
<dd>Creates a new empty index. See <i>set_options()</i> for more details.
<dt>$index-&gt;set_options(%opts)
<dd>The ``type'' option is checked first to define default values for other options. Here are the relevant options: ``get_key_func'' is a function returning a key for the item passed in parameters. The index can only contain one item with a given key. The function used depend on the type: for <font SIZE="-1">CTRL_INFO_PKG, CTRL_INDEX_SRC, CTRL_INDEX_PKG</font> and <font SIZE="-1">CTRL_PKG_DEB</font> it's simply the Package field; for <font SIZE="-1">CTRL_PKG_SRC</font> and <font SIZE="-1">CTRL_INFO_SRC,</font> it's the Source field; for <font SIZE="-1">CTRL_CHANGELOG</font> it's the Source and the Version fields (concatenated with an intermediary ``_''); for <font SIZE="-1">CTRL_FILE_CHANGES</font> it's the Source, Version and Architecture fields (concatenated with ``_''); for <font SIZE="-1">CTRL_FILE_VENDOR</font> it's the Vendor field; for <font SIZE="-1">CTRL_FILE_STATUS</font> it's the Package and Architecture fields (concatenated with ``_''). Otherwise it's the Package field by default.
<dt>$index-&gt;<i>get_type()</i>
<dd>Returns the type of control information stored. See the type parameter set during <i>new()</i>.
<dt>$index-&gt;add($item, [$key])
<dd>Add a new item in the index. If the <tt>$key</tt> parameter is omitted, the key will be generated with the get_key_func function (see <i>set_options()</i> for details).
<dt>$index-&gt;load($file)
<dd>Reads the file and creates all items parsed. Returns the number of items parsed. Handles compressed files transparently based on their extensions.
<dt>$index-&gt;parse($fh, $desc)
<dd>Reads the filehandle and creates all items parsed. Returns the number of items parsed.
<dt>$index-&gt;save($file)
<dd>Writes the content of the index in a file. Auto-compresses files based on their extensions.
<dt>my $item = $index-&gt;<i>new_item()</i>
<dd>Creates a new item. Mainly useful for derived objects that would want to override this method to return something else than a Dpkg::Control object.
<dt>my $item = $index-&gt;get_by_key($key)
<dd>Returns the item identified by <tt>$key</tt> or undef.
<dt>my @keys = $index-&gt;get_keys(%criteria)
<dd>Returns the keys of items that matches all the criteria. The key of the <tt>%criteria</tt> hash is a field name and the value is either a regex that needs to match the field value, or a reference to a function that must return true and that receives the field value as single parameter, or a scalar that must be equal to the field value.
<dt>my @items = $index-&gt;get(%criteria)
<dd>Returns all the items that matches all the criteria.
<dt>$index-&gt;remove_by_key($key)
<dd>Remove the item identified by the given key.
<dt>my @items = $index-&gt;remove(%criteria)
<dd>Returns and removes all the items that matches all the criteria.
<dt>$index-&gt;merge($other_index, %opts)
<dd>Merge the entries of the other index. While merging, the keys of the merged index are used, they are not re-computed (unless you have set the options ``keep_keys'' to ``0''). It's your responsibility to ensure that they have been computed with the same function.
<dt>$index-&gt;sort(\&amp;sortfunc)
<dd>Sort the index with the given sort function. If no function is given, an alphabetic sort is done based on the keys. The sort function receives the items themselves as parameters and not the keys.
<dt>my $str = $index-&gt;<i>output()</i>
<dd><dt>&quot;$index&quot;
<dd>Get a string representation of the index. The Dpkg::Control objects are output in the order which they have been read or added except if the order hae been changed with <i>sort()</i>.
<dt>$index-&gt;output($fh)
<dd>Print the string representation of the index to a filehandle.</dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
