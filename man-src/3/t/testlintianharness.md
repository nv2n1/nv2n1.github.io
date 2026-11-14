---
title: "testlintianharness(3)"
name: "testlintianharness"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianharness/"
---

Test::Lintian::Harness -- Helper tools for t/runtests 

<h2>Synopsis</h2><pre> use Test::Lintian::Harness qw(up_to_date);
 if (not up_to_date('some/build-stamp', 'some/dir')) {
 # do rebuild
 }</pre><h2>Description</h2>Helper functions for t/runtests.
<h2>Functions</h2><dl COMPACT><dt>skip_reaon(<font SIZE="-1">SKIP_FILE</font>)
<dd>Return the (human-readable) reason for skipping a test by reading the <font SIZE="-1">SKIP_FILE.</font>
<dt>copy_template_dir(<font SIZE="-1">SKEL_DIR, TEST_SRC_DIR, TEST_TARGET_DIR,</font> [EXCL_SKEL[, <font SIZE="-1">EXCL_SRC</font>]])
<dd>Populate <font SIZE="-1">TEST_TARGET_DIR</font> with files/dirs from <font SIZE="-1">SKEL_DIR</font> and <font SIZE="-1">TEST_SRC_DIR.</font> If given, <font SIZE="-1">EXCL_SKEL</font> and <font SIZE="-1">EXCL_SRC</font> must be a listref containing rsync ``--exclude'' options.
<dt>runsystem(<font SIZE="-1">CMD...</font>)
<dd>Run <font SIZE="-1">CMD</font> via system, but throw an error if <font SIZE="-1">CMD</font> does not return 0.
<dt>runsystem_ok(<font SIZE="-1">CMD...</font>)
<dd>Run <font SIZE="-1">CMD</font> via system, but throw an error if <font SIZE="-1">CMD</font> does not return 0 or 1. 

 Returns 1 if <font SIZE="-1">CMD</font> returned successfully (i.e. 0), otherwise 0. 

 This is mostly useful for running Lintian, which may return 0 or 1 on ``success''.
<dt>up_to_date(<font SIZE="-1">STAMPFILE,</font> DIR[, <font SIZE="-1">RUNNER_TS</font>])
<dd>Returns true if the mtime of <font SIZE="-1">STAMPFILE</font> is greater than or equal to the mtime of all files in <font SIZE="-1">DIR.</font> If <font SIZE="-1">RUNNER_TS</font> is given, then the mtime of <font SIZE="-1">STAMPFILE</font> must also be greater than or equal to the value of <font SIZE="-1">RUNNER_TS.</font> 

 If <font SIZE="-1">STAMPFILE</font> does not exist, this function returns false unconditionally.
<dt>check_test_depends(<font SIZE="-1">TESTDATA</font>)
<dd>Given a <font SIZE="-1">TESTDATA</font> with a dependency requirement, check whether the dependency requirement is satisfied. If satisfied, return <tt>&quot;undef&quot;</tt>, otherwise return a (human-readable) string containing the missing dependencies.
<dt>read_test_desc(<font SIZE="-1">FILENAME</font>)
<dd>Parse <font SIZE="-1">FILENAME</font> as a test description file, do a quick validation of its contents and return it in a hashref. This is similar get_dsc_control (<font SIZE="-1">DSCFILE</font>) except for the extra validation.
<dt>fill_in_tmpl(<font SIZE="-1">FILE, DATA</font>)
<dd>Create <font SIZE="-1">FILE</font> using ``${<font SIZE="-1">FILE</font>}.in'' as a template and <font SIZE="-1">DATA</font> as template data.
<dt>chdir_runcmd(<font SIZE="-1">DIR,</font> CMD_REF[, <font SIZE="-1">LOG_FILE</font>])
<dd>Fork, chdir to <font SIZE="-1">DIR</font> and exec the command (plus arguments) contained in <font SIZE="-1">CMD_REF.</font> The child process's <font SIZE="-1">STDERR</font> is merged into its <font SIZE="-1">STDOUT.</font> The <font SIZE="-1">STDOUT</font> stream of the child process is either directed to the path denoted by <font SIZE="-1">LOG_FILE</font> (if given and not <tt>&quot;undef&quot;</tt>) or to <i>/dev/null</i>. 

 Returns 0 on success and non-zero otherwise.
<dt>is_tag_in_file(<font SIZE="-1">TAGNAME, FILENAME</font>)
<dd>Returns true if <font SIZE="-1">FILENAME</font> appears to be output from Lintian, which emitted <font SIZE="-1">TAGNAME</font> from that run.
<dt>find_tests_for_tag(<font SIZE="-1">TAGNAME, GLOB_EXPR</font>)
<dd>Find checks for the Lintian tag denoted by <font SIZE="-1">TAGNAME</font> that match the <font SIZE="-1">GLOB_EXPR.</font> Note that <font SIZE="-1">GLOB_EXPR</font> must match only the ``desc'' file of the tests. 

 This function returns a list of the test-data for each of these tests.
<dt>generic_find_test_for_tag(<font SIZE="-1">TAGNAME,</font> GLOB_EXPR[, <font SIZE="-1">TCODE</font>])
<dd>Looks for <font SIZE="-1">TAGNAME</font> in all files returned by using glob on <font SIZE="-1">GLOB_EXPR. TCODE</font> is called for each file with <font SIZE="-1">TAGNAME</font> as first argument and the filename as second argument. <font SIZE="-1">TCODE</font> is expected to return a truth value that if the test should be run. If <font SIZE="-1">TCODE</font> returns something that is not just a raw truth value (e.g. a hash ref), this will be taken as the ``test'', otherwise this sub will attempt to guess the test name from the file. 

 If <font SIZE="-1">TCODE</font> is omitted, ``is_tag_in_file(<font SIZE="-1">TAGNAME, FILENAME</font>)'' will be used. 

 Returns a list of values returned by <font SIZE="-1">TCODE</font> or guessed test names (as per above) 

</dl>
