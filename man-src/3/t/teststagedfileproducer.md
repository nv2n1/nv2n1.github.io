---
title: "teststagedfileproducer(3)"
name: "teststagedfileproducer"
section: "3"
letter: "t"
url: "/docs/linux/man/3-teststagedfileproducer/"
---

Test::StagedFileProducer -- mtime-based file production engine 

<h2>Synopsis</h2><pre> use Test::StagedFileProducer;
 my $wherever = '/your/test/directory';
 my $producer = Test::StagedFileProducer-&gt;new(path =&gt; $wherever);
 $producer-&gt;exclude(&quot;$wherever/log&quot;, &quot;$wherever/build-stamp&quot;);
 my $output = &quot;$wherever/file.out&quot;;
 $producer-&gt;add_stage(
 products =&gt; [$output],
 build =&gt;sub {
 printf &quot;Building $output.\n&quot;;
 },
 skip =&gt;sub {
 printf &quot;Skipping $output.\n&quot;;
 }
 );
 $producer-&gt;run(minimum_epoch =&gt; time, verbose =&gt; 1);</pre><h2>Description</h2>Provides a way to define and stack file production stages that all depend on subsets of the same group of files. 

 After the stages are defined, the processing engine takes an inventory of all files in a target directory. It excludes some files, like logs, that should not be considered. 

 Each stage adds its own products to the list of files to be excluded before deciding whether to produce them. The decision is based on relative file modification times, in addition to a systemic rebuilding threshold. Before rebuilding, each stage asks a lower stage to make the same determination. 

 The result is an engine with file production stages that depend on successively larger sets of files.
<h2>Functions</h2><dl COMPACT><dt>new(path =&gt; <font SIZE="-1">PATH</font>)
<dd>Create a new instance focused on files in directory <font SIZE="-1">PATH.</font>
<dt>exclude(<font SIZE="-1">LIST</font>)
<dd>Excludes all absolute paths in <font SIZE="-1">LIST</font> from all mtime comparisons. This is especially useful for logs. Calls to Path::Tiny-&gt;realpath are made to ensure the elements are canonical and have a chance of matching something returned by File::Find::Rule.
<dt>add_stage(<font SIZE="-1">HASH</font>)
<dd>Add a stage defined by <font SIZE="-1">HASH</font> to the processing engine for processing after stages previously added. <font SIZE="-1">HASH</font> can define the following keys: 

 <tt>$HASH</tt>{products} =&gt; <font SIZE="-1">LIST</font>; a list of full-path filenames to be produced. 

 <tt>$HASH</tt>{minimum_epoch} =&gt; <font SIZE="-1">EPOCH</font>; an integer threshold for maximum age 

 <tt>$HASH</tt>{build} =&gt; <font SIZE="-1">SUB</font>; a sub executed when production is required. 

 <tt>$HASH</tt>{skip} =&gt; <font SIZE="-1">SUB</font>; a sub executed when production is not required.
<dt>run(<font SIZE="-1">PARAMETERS</font>)
<dd>Runs the defined engine using the given parameters, which are arranged in a matching list suitable for assignment to a hash. The following two parameters are currently available: 

 minimum_epoch =&gt; <font SIZE="-1">EPOCH</font>; a systemic threshold, in epochs, below which rebuilding is mandatory for any product. 

 verbose =&gt; <font SIZE="-1">BOOLEAN</font>; an option to enable more verbose reporting
<dt>_process_remaining_stages(<font SIZE="-1">LIST</font>)
<dd>An internal subroutine that is used recursively to execute the stages. The list passed describes the list of files to be excluded from subsequent mtime calculations. 

 Please note that the bulk of the execution takes place after calling the next lower stage. That is to ensure that any lower build targets (or products, in our parlance) are met before the present stage attempts to do its job. 

</dl>
