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
<h2>Class Methods</h2><dl COMPACT><dt>new (COLLMAP, PROFILE[, OPTIONS])
</dt><dd>Creates a new unpacker. 
 COLLMAP is a Lintian::DepMap::Properties describing the dependencies between the collections. Each node in COLLMAP must have a Lintian::CollScript as property. 
 OPTIONS is an optional hashref containing optional configurations. If a key is not present, its value is assumed to be <tt>&quot;undef&quot;</tt> unless otherwise stated. The following key/values are available:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>&quot;profile&quot;
</dt><dd>If this key is present and its value is defined, the value must be Lintian::Profile. The unpacker will use the enabled checks of the Profile to determine what collections to use. 
 If ``profile'' is not present or its value is undefined, then all collections in COLLMAP will be unpacked.
</dd><dt>&quot;extra-coll&quot;
</dt><dd>If this key is present and its value is defined, it must be a reference to a hash table. The keys are considered names of ``extra'' collections to unpack. The values in this table is ignored. 
 Extra collections will be unpacked on top of other collections. 
 NB: This value is ignored if ``profile'' is not given.
</dd><dt>&quot;jobs&quot;
</dt><dd>This value is the max number of jobs to be run in parallel. Can be changed with the ``jobs'' method later. If omitted, it defaults to 0. Refer to ``jobs'' for more info.</dd></dl></dl><dl COMPACT><dd></dd></dl></dl><h2>Instance Methods</h2><dl COMPACT><dt>prepare_tasks (ERRHANDLER, LAB-ENTRY...)
</dt><dd>Prepare a number of lab entries for unpacking. 
 The ERRHANDLER should be a code ref, which will be invoked in case that an entry is not in the laboratory and cannot be created (via the create method). It is invoked once per failed entry giving the entry as first (and only) argument. 
 If ERRHANDLER returns normally, the entry is skipped (and will not be unpacked later). If ERRHANDLER croaks/dies/etc., the method will attempt to update the status file for any entry it created before passing back the error to the caller (via die). 
 LAB-ENTRY is an array of lab entries to be processed. They must be instances of Lintian::Lab::Entry, but do not have to exists. They will be created as needed. 
 Returns a truth value if at least one entry needs to be processed and it did not cause an error. Otherwise, it returns <tt>&quot;undef&quot;</tt>. 
 NB: The status file is not updated for created entries on successful return. It should either be done by running the process_tasks method or manually.
</dd><dt>process_tasks (HOOKS)
</dt><dd>Process the current tasks. This method blocks until all tasks and jobs have terminated. 
 The return value is unspecified. 
 HOOKS (if given) is a hashref of hooks. The following hooks are available:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>coll-hook (LPKG, EVENT, COLL, PID[, STATUS])
</dt><dd>Called each time a new collection job is started or finished. 
 LPKG is the entry it is applied to. COLL is the collection being applied. EVENT is either ``start'' for a new job or ``finish'' for a job terminating. 
 PID is the process id of the job. If EVENT is ``start'' this can be -1 to signal a failure. 
 STATUS is the exit status of the finishing job. It is only available if EVENT is ``finish'' and if STATUS is non-zero is considered an error.</dd></dl></dl><dl COMPACT><dd></dd></dl><dt>reset_worklist
</dt><dd>Wait for all running jobs (see ``wait_for_jobs'') and discard the current worklist.
</dd><dt>wait_for_jobs
</dt><dd>Block and wait for all running jobs to terminate. Usually this is not needed unless process_tasks was interrupted somehow.
</dd><dt>kill_jobs
</dt><dd>Forcefully terminate all running jobs. Usually this is not needed unless process_tasks was interrupted somehow.
</dd><dt>jobs
</dt><dd>Returns or sets the max number of jobs to be processed in parallel. 

 If the limit is 0, then there is no limit for the number of parallel jobs.</dd></dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i>Lintian::CollScript</i>(3), <i>Lintian::Lab::Entry</i>(3)
