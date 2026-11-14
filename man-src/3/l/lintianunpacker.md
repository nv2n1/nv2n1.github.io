---
title: "lintianunpacker(3)"
name: "lintianunpacker"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianunpacker/"
---

Lintian::Unpacker -- Job handler to unpack collections 

<h2>Synopsis</h2><pre> use Lintian::DepMap::Properties;
 use Lintian::Unpacker;
 
 my $done = 1;
 my $joblimit = 4;
 my $collmap = Lintian::DepMap::Properties-&gt;new;
 my %requested = ( 'debfiles' =&gt; 1 );
 # Initialise $collmap with the collections and their relations
 # - Each node in $collmap should an instance of L::CollScript
 # as property.
 my $unpacker = Lintian::Unpacker-&gt;new ($collmap, \%requested,
 $joblimit);
 
 while (1) {
 my $errhandler = sub {}; # Insert hook
 my @lpkgs; # List of Lintian::Lab::Entry instances
 $unpacker-&gt;reset_worklist;
 next unless $unpacker-&gt;prepare_tasks ($errhandler, @lpkgs);
 
 my %hooks = (
 'coll-hook' =&gt; sub {}, # Insert hook
 'finish-hook' =&gt; sub {}, # Insert hook
 );
 $unpacker-&gt;process_tasks ();
 last if $done;
 }</pre><h2>Description</h2>An unpacker class to extract data from lab entries and make it available via Lintian::Collect.
<h2>Class Methods</h2><dl COMPACT><dt>new (<font SIZE="-1">COLLMAP,</font> PROFILE[, <font SIZE="-1">OPTIONS</font>])
<dd>Creates a new unpacker. 

 <font SIZE="-1">COLLMAP</font> is a Lintian::DepMap::Properties describing the dependencies between the collections. Each node in <font SIZE="-1">COLLMAP</font> must have a Lintian::CollScript as property. 

 <font SIZE="-1">OPTIONS</font> is an optional hashref containing optional configurations. If a key is not present, its value is assumed to be <tt>&quot;undef&quot;</tt> unless otherwise stated. The following key/values are available:
<dl COMPACT><dd><dl COMPACT><dt>&quot;profile&quot;
<dd>If this key is present and its value is defined, the value must be Lintian::Profile. The unpacker will use the enabled checks of the Profile to determine what collections to use. 

 If ``profile'' is not present or its value is undefined, then all collections in <font SIZE="-1">COLLMAP</font> will be unpacked.
<dt>&quot;extra-coll&quot;
<dd>If this key is present and its value is defined, it must be a reference to a hash table. The keys are considered names of ``extra'' collections to unpack. The values in this table is ignored. 

 Extra collections will be unpacked on top of other collections. 

 <font SIZE="-1">NB:</font> This value is ignored if ``profile'' is not given.
<dt>&quot;jobs&quot;
<dd>This value is the max number of jobs to be run in parallel. Can be changed with the ``jobs'' method later. If omitted, it defaults to 0. Refer to ``jobs'' for more info.</dl></dl><dl COMPACT><dd></dl></dl><h2>Instance Methods</h2><dl COMPACT><dt>prepare_tasks (<font SIZE="-1">ERRHANDLER,</font> LAB-ENTRY...)
<dd>Prepare a number of lab entries for unpacking. 

 The <font SIZE="-1">ERRHANDLER</font> should be a code ref, which will be invoked in case that an entry is not in the laboratory and cannot be created (via the create method). It is invoked once per failed entry giving the entry as first (and only) argument. 

 If <font SIZE="-1">ERRHANDLER</font> returns normally, the entry is skipped (and will not be unpacked later). If <font SIZE="-1">ERRHANDLER</font> croaks/dies/etc., the method will attempt to update the status file for any entry it created before passing back the error to the caller (via die). 

 LAB-ENTRY is an array of lab entries to be processed. They must be instances of Lintian::Lab::Entry, but do not have to exists. They will be created as needed. 

 Returns a truth value if at least one entry needs to be processed and it did not cause an error. Otherwise, it returns <tt>&quot;undef&quot;</tt>. 

 <font SIZE="-1">NB:</font> The status file is not updated for created entries on successful return. It should either be done by running the process_tasks method or manually.
<dt>process_tasks (<font SIZE="-1">HOOKS</font>)
<dd>Process the current tasks. This method blocks until all tasks and jobs have terminated. 

 The return value is unspecified. 

 <font SIZE="-1">HOOKS</font> (if given) is a hashref of hooks. The following hooks are available:
<dl COMPACT><dd><dl COMPACT><dt>coll-hook (<font SIZE="-1">LPKG, EVENT, COLL,</font> PID[, <font SIZE="-1">STATUS</font>])
<dd>Called each time a new collection job is started or finished. 

 <font SIZE="-1">LPKG</font> is the entry it is applied to. <font SIZE="-1">COLL</font> is the collection being applied. <font SIZE="-1">EVENT</font> is either ``start'' for a new job or ``finish'' for a job terminating. 

 <font SIZE="-1">PID</font> is the process id of the job. If <font SIZE="-1">EVENT</font> is ``start'' this can be -1 to signal a failure. 

 <font SIZE="-1">STATUS</font> is the exit status of the finishing job. It is only available if <font SIZE="-1">EVENT</font> is ``finish'' and if <font SIZE="-1">STATUS</font> is non-zero is considered an error.</dl></dl><dl COMPACT><dd></dl><dt>reset_worklist
<dd>Wait for all running jobs (see ``wait_for_jobs'') and discard the current worklist.
<dt>wait_for_jobs
<dd>Block and wait for all running jobs to terminate. Usually this is not needed unless process_tasks was interrupted somehow.
<dt>kill_jobs
<dd>Forcefully terminate all running jobs. Usually this is not needed unless process_tasks was interrupted somehow.
<dt>jobs
<dd>Returns or sets the max number of jobs to be processed in parallel. 

 If the limit is 0, then there is no limit for the number of parallel jobs.</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--collscript/">Lintian::CollScript</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--lab--entry/">Lintian::Lab::Entry</a></i>(3)
