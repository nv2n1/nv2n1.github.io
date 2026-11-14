---
title: "lintiancollect(3)"
name: "lintiancollect"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollect/"
---

Lintian::Collect - Lintian interface to package data collection 

<h2>Synopsis</h2><pre> my ($name, $type, $dir) = ('foobar', 'udeb', '/some/abs/path');
 my $collect = Lintian::Collect-&gt;new ($name, $type, $dir);
 $name = $collect-&gt;name;
 $type = $collect-&gt;type;</pre><h2>Description</h2>Lintian::Collect provides the shared interface to package data used by source, binary and udeb packages and .changes files. It creates an object of the appropriate type and provides common functions used by the collection interface to all types of package. 

 Usually instances should not be created directly (exceptions include collections), but instead be requested via the info method in Lintian::Lab::Entry. 

 This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data via this module and its subclasses so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.
<h2>Class Methods</h2><dl COMPACT><dt>new (<font SIZE="-1">PACKAGE, TYPE,</font> BASEDIR[, <font SIZE="-1">FIELDS</font>]))
<dd>Creates a new object appropriate to the package type. <font SIZE="-1">TYPE</font> can be retrieved later with the ``type'' method. Croaks if given an unknown <font SIZE="-1">TYPE.</font> 

 <font SIZE="-1">PACKAGE</font> is the name of the package and is stored in the collect object. It can be retrieved with the ``name'' method. 

 <font SIZE="-1">BASEDIR</font> is the base directory for the data and should be absolute. 

 If <font SIZE="-1">FIELDS</font> is given it is assumed to be the fields from the underlying control file. This is only used to avoid an unnecessary read operation (possibly incl. an ar | gzip pipeline) when the fields are already known.</dl><h2>Instance Methods</h2>In addition to the instance methods documented here, see the documentation of Lintian::Collect::Source, Lintian::Collect::Binary and Lintian::Collect::Changes for instance methods specific to source and binary / udeb packages and .changes files.
<dl COMPACT><dt>name
<dd>Returns the name of the package. 

 Needs-Info requirements for using <i>name</i>: none
<dt>type
<dd>Returns the type of the package. 

 Needs-Info requirements for using <i>type</i>: none
<dt>base_dir
<dd>Returns the base_dir where all the package information is stored. 

 Needs-Info requirements for using <i>base_dir</i>: none
<dt>lab_data_path ([<font SIZE="-1">ENTRY</font>])
<dd>Return the path to the <font SIZE="-1">ENTRY</font> in the lab. This is a convenience method around base_dir. If <font SIZE="-1">ENTRY</font> is not given, this method behaves like base_dir. 

 Needs-Info requirements for using <i>lab_data_path</i>: ``base_dir''
<dt>field ([FIELD[, <font SIZE="-1">DEFAULT</font>]])
<dd>If <font SIZE="-1">FIELD</font> is given, this method returns the value of the control field <font SIZE="-1">FIELD</font> in the control file for the package. For a source package, this is the *.dsc file; for a binary package, this is the control file in the control section of the package. 

 If <font SIZE="-1">FIELD</font> is passed but not present, then this method will return <font SIZE="-1">DEFAULT</font> (if given) or undef. 

 Otherwise this will return a hash of fields, where the key is the field name (in all lowercase). 

 Needs-Info requirements for using <i>field</i>: none
<dt>is_non_free
<dd>Returns a truth value if the package appears to be non-free (based on the section field; ``non-free/*'' and ``restricted/*'') 

 Needs-Info requirements for using <i>is_non_free</i>: ``field ([FIELD[, <font SIZE="-1">DEFAULT</font>]])''</dl><h2>Author</h2>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), Lintian::Collect::Binary, Lintian::Collect::Changes, Lintian::Collect::Source
