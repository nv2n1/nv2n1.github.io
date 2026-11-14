---
title: "lintianlab(3)"
name: "lintianlab"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianlab/"
---

Lintian::Lab -- Interface to the Lintian Lab 

<h2>Synopsis</h2><pre> use Lintian::Lab;
 
 # Static lab
 my $lab = Lintian::Lab-&gt;new ('/var/lib/lintian/static-lab');
 if (!$lab-&gt;exists) {
 $lab-&gt;create;
 }
 $lab-&gt;open;
 
 # Fetch a package from the lab
 my $lpkg = $lab-&gt;get_package ('lintian', 'binary', '2.5.4', 'all');
 
 my $visitor = sub {
 my ($lpkg, $pkg_name, $pkg_ver, $pkg_arch) = @_;
 # do stuff with that entry
 };
 $lab-&gt;visit_packages ($visitor, 'source');
 
 $lab-&gt;close;</pre><h2>Description</h2>This module provides an abstraction from ``How and where'' packages are placed. It handles creation and deletion of the Lintian Lab itself as well as providing access to the entries.
<h2>Class Methods</h2><dl COMPACT><dt>new ([<font SIZE="-1">DIR</font>])
<dd>Creates a new Lab instance. If <font SIZE="-1">DIR</font> is defined it will be used as the path to the lab and the lab will be in static mode. Otherwise the lab will be in temporary mode and will point to a temporary directory.</dl><h2>Instance Methods</h2><dl COMPACT><dt>dir
<dd>Returns the absolute path to the base of the lab. 

 Note: This may return the empty string if either the lab has been deleted or this is a temporary lab that has not been created yet. In the latter case, ``create'' or ``open'' should be run to get a non-empty value from this method.
<dt>is_open
<dd>Returns a truth value if this lab is open. 

 Note: If the lab is open, it also exists. However, if the lab is closed then the lab may or may not exist (see ``exists'').
<dt>exists
<dd>Returns a truth value if the instance points to an existing lab. 

 Note: This never implies that the lab is open. Though it may imply the lab is closed (see ``is_open'').
<dt>get_package (<font SIZE="-1">NAME,</font> TYPE[, <font SIZE="-1">EXTRA</font>]), get_package (<font SIZE="-1">PROC</font>)
<dd>Fetches an existing package from the lab. 

 The first argument can be a processable. In that case all other arguments are ignored. 

 If the first calling convention is used then this method will search for an existing package. The <font SIZE="-1">EXTRA</font> argument can be used to narrow the search or even to add a new entry. 

 <font SIZE="-1">EXTRA</font> consists of (in order):
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>version
<dt>&bull;
<dd>arch (ignored if <font SIZE="-1">TYPE</font> is ``source'')</dl></dl><dl COMPACT><dd>If version or arch is omitted (or if it is undef) then that search parameter is consider a wildcard for ``any''. Example: 

 <pre> # Returns all eclipse-platform packages with architecture i386 regardless
 # of their version (if any)
 @ps = $lab-&gt;get_package ('eclipse-platform', 'binary', undef, 'i386');
 # Returns all eclipse-platform packages with version 3.5.2-11 regardless
 # of their architecture (if any)
 @ps = $lab-&gt;get_package ('eclipse-platform', 'binary', '3.5.2-11');
 # Return the eclipse-platform package with version 3.5.2-11 and architecture
 # i386 (or undef)
 $pkg = $lab-&gt;get_package ('eclipse-platform', 'binary', '3.5.2-11', 'i386');</pre>In list context, this returns a list of matches. In scalar context this returns the first match (if any). Note there is no guaranteed order (e.g. the returned list is not ordered). 

 If the second calling convention is used, then this method will search for an entry matching the processable passed. If such an entry does not exists, a new ``non-existing'' entry will be returned. This entry can be created by using the create method on the entry.</dl><dt>lab_query (<font SIZE="-1">QUERY</font>)
<dd>Process a given <font SIZE="-1">QUERY</font> and return the results from it. A <font SIZE="-1">QUERY</font> is a string of the format: 

 <pre> [TYPE:]NAME[/VERSION[/ARCH]]</pre><font SIZE="-1">TYPE</font> can be one of the regular package type (e.g. ``binary'') or one of the two special values ``<font SIZE="-1">ALL''</font> (default if omitted) or ``<font SIZE="-1">GROUP''.</font> If <font SIZE="-1">TYPE</font> is <font SIZE="-1">ALL,</font> then the query is one once for each of package type. 

 <font SIZE="-1">NAME</font> is the name of the package to request. For <font SIZE="-1">GROUP</font> queries, this is the name of the source package. It is not possible to do any kind of wildcards in <font SIZE="-1">NAME:</font> 

 <font SIZE="-1">VERSION</font> is the version of the package. For <font SIZE="-1">GROUP</font> queries, this is the version of the source package. If omitted or the string '_', then any version will match. 

 <font SIZE="-1">ARCH</font> is the architecture of the package. For <font SIZE="-1">GROUP</font> and ``source'' queries, <font SIZE="-1">ARCH</font> is ignored (if given). If <font SIZE="-1">ARCH</font> is omitted or the string '_', then any package architecture will match. <font SIZE="-1">NB:</font> The <font SIZE="-1">ARCH</font> field should match the architecture field of the entry (which for <i>.changes</i> files usually contains spaces). 

 lab_query will return a list of entries matching the query. If no entries match, an empty list will be returned.
<dt>visit_packages (VISITOR[, <font SIZE="-1">TYPE</font>])
<dd>Passes each lab entry to <font SIZE="-1">VISITOR.</font> If <font SIZE="-1">TYPE</font> is passed, then only entries of that type are passed. 

 <font SIZE="-1">VISITOR</font> is given a reference to the entry, the package name, the package version and the package architecture (may be undef for source packages).
<dt>generate_diffs (<font SIZE="-1">LIST</font>)
<dd>Each member of <font SIZE="-1">LIST</font> must be a Lintian::Lab::Manifest. 

 The lab will generate a diff between the given member and its state for the given package type. 

 The diffs are accurate until the original manifest is modified or a package is added or removed to the lab.
<dt>repair
<dd>Checks the lab contents against the current meta-data and syncs them. The lab must be open and should not be access while this method is running. 

 This returns the number of corrections done by this process. If there were any corrections, the state files are written before returning. 

 The method may croak if it is unable to do a full check of the lab or if it is unable to write the corrected metadata. 

 Note: This may (and generally will) correct ``broken'' entries by removing them.
<dt>create ([<font SIZE="-1">OPTS</font>])
<dd>Creates a new lab. It will create ``dir'' if it does not exist. It will also create a basic empty lab. If this is a temporary lab, this method will also setup the temporary dir for the lab. 

 The lab will <i>not</i> be opened by this method. This should be done afterwards by invoking the ``open'' method. 

 <font SIZE="-1">OPTS</font> (if present) is a hashref containing options. The following options are accepted:
<dl COMPACT><dd><dl COMPACT><dt>keep-lab
<dd>If ``keep-lab'' points to a truth value the temporary directory will <i>not</i> be removed by closing the lab (nor exiting the application). However, explicitly calling ``remove'' will remove the lab.
<dt>mode
<dd>If present, this will be used as mode for creating directories. Will default to 0777 if not specified. It is passed to mkdir and is thus subject to umask settings.</dl></dl><dl COMPACT><dd>Note: This will not create parent directories of ``dir'' and will croak if these does not exist. 

 Note: This may update the value of ``dir'' as resolving the path requires it to exist. 

 Note: This does nothing if the lab appears to already exists.</dl><dt>open
<dd>Opens the lab and reads the contents into caches. If the lab is temporary and does not exists, this method will call create to initialize the temporary lab. 

 This will croak if the lab is already open. It may also croak for the same reasons as ``create'' if the lab is temporary. 

 Note: for static labs, ``dir'' must point to an existing consistent lab or this will croak. To open a new lab, please use ``create''. 

 Note: It is not possible to pass options to the creation of the temporary lab. If special options are required, please use ``create'' directly.
<dt>close
<dd>Close the lab - all state caches will be flushed to the disk and the lab can no longer be used. All references to entries in the lab should be considered invalid. 

 Note: if the lab is a temporary one, this will be deleted unless it was created with ``keep-lab'' (see ``create'').
<dt>remove
<dd>Removes the lab and everything in it. Any reference to an entry returned from this lab will immediately become invalid. 

 If this is a temporary lab, the lab root dir (as returned ``dir'') will be removed as well on success. Otherwise the lab root dir will not be removed by this call. 

 On success, this will return a truth value. If the lab is a temporary lab, the directory path will be set to the empty string (that is, ``dir'' will return ''). 

 On error, this method will croak. 

 If the lab has already been removed (or does not exist), this will return a truth value.
<dt>is_temp
<dd>Returns a truth value if lab is a temporary lab. 

 Note: This returns a truth value, even if the lab was created with the ``keep-lab'' property.</dl><h2>Changes to the lab format.</h2>Lab formats up to (and including) ``10'' used to store the lab format with each entry. The files in <tt>$LAB</tt>/info/ were used to list packages from a mirror (dist). 

 In lab format 11 the lab format is stored in <tt>$LAB</tt>/info/lab-info. The rest of the files in <tt>$LAB</tt>/info/* have been re-purposed to be a list of packages in the lab. 

 The <tt>$LAB</tt>/info/lab-info is parsed as a debian control file (See Debian Policy Manual X5.1 for syntax). The consists of a single paragraph and only the following fields are allowed:
<dl COMPACT><dt>Lab-Format (simple, mandatory)
<dd>This field contains the lab format of this lab. Generally this is simply an integer (though during development non-integers have been used).
<dt>Layout (simple, optional)
<dd>The layout parameter describes how packages are stored in the lab. Currently the only accepted value is ``pool'' and the value is not case-sensitive. 

 The pool format dictates that packages are stored in: 

 <pre> pool/$l/${name}/${name}_${version}[_${arch}]_${type}/</pre>Note that <tt>$arch</tt> is left out for source packages, <tt>$l</tt> is the first letter of the package name (except if the name starts with ``lib'', then it is the first 4 letters of the package name). Whitespace (e.g. `` '') are replaced with dashes (``-'') and colons (``:'') with underscores (``_''). 

 If the field is missing, it defaults to ``pool''.</dl>
 

 It is allowed to use comments in <tt>$LAB</tt>/info/lab-info as described in the Debian Policy Manual X5.1.
<h2>Author</h2>Niels Thykier &lt;niels [at] thykier.net&gt; 

 Based on the work of various others.
