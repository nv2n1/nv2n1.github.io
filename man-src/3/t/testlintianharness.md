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
<h2>Functions</h2><dl COMPACT><dt>skip_reaon(SKIP_FILE)
</dt><dd>Return the (human-readable) reason for skipping a test by reading the SKIP_FILE.
</dd><dt>copy_template_dir(SKEL_DIR, TEST_SRC_DIR, TEST_TARGET_DIR, [EXCL_SKEL[, EXCL_SRC]])
</dt><dd>Populate TEST_TARGET_DIR with files/dirs from SKEL_DIR and TEST_SRC_DIR. If given, EXCL_SKEL and EXCL_SRC must be a listref containing rsync ``--exclude'' options.
</dd><dt>runsystem(CMD...)
</dt><dd>Run CMD via system, but throw an error if CMD does not return 0.
</dd><dt>runsystem_ok(CMD...)
</dt><dd>Run CMD via system, but throw an error if CMD does not return 0 or 1. 
 Returns 1 if CMD returned successfully (i.e. 0), otherwise 0. 
 This is mostly useful for running Lintian, which may return 0 or 1 on ``success''.
</dd><dt>up_to_date(STAMPFILE, DIR[, RUNNER_TS])
</dt><dd>Returns true if the mtime of STAMPFILE is greater than or equal to the mtime of all files in DIR. If RUNNER_TS is given, then the mtime of STAMPFILE must also be greater than or equal to the value of RUNNER_TS. 
 If STAMPFILE does not exist, this function returns false unconditionally.
</dd><dt>check_test_depends(TESTDATA)
</dt><dd>Given a TESTDATA with a dependency requirement, check whether the dependency requirement is satisfied. If satisfied, return <tt>&quot;undef&quot;</tt>, otherwise return a (human-readable) string containing the missing dependencies.
</dd><dt>read_test_desc(FILENAME)
</dt><dd>Parse FILENAME as a test description file, do a quick validation of its contents and return it in a hashref. This is similar get_dsc_control (DSCFILE) except for the extra validation.
</dd><dt>fill_in_tmpl(FILE, DATA)
</dt><dd>Create FILE using ``${FILE}.in'' as a template and DATA as template data.
</dd><dt>chdir_runcmd(DIR, CMD_REF[, LOG_FILE])
</dt><dd>Fork, chdir to DIR and exec the command (plus arguments) contained in CMD_REF. The child process's STDERR is merged into its STDOUT. The STDOUT stream of the child process is either directed to the path denoted by LOG_FILE (if given and not <tt>&quot;undef&quot;</tt>) or to <i>/dev/null</i>. 
 Returns 0 on success and non-zero otherwise.
</dd><dt>is_tag_in_file(TAGNAME, FILENAME)
</dt><dd>Returns true if FILENAME appears to be output from Lintian, which emitted TAGNAME from that run.
</dd><dt>find_tests_for_tag(TAGNAME, GLOB_EXPR)
</dt><dd>Find checks for the Lintian tag denoted by TAGNAME that match the GLOB_EXPR. Note that GLOB_EXPR must match only the ``desc'' file of the tests. 
 This function returns a list of the test-data for each of these tests.
</dd><dt>generic_find_test_for_tag(TAGNAME, GLOB_EXPR[, TCODE])
</dt><dd>Looks for TAGNAME in all files returned by using glob on GLOB_EXPR. TCODE is called for each file with TAGNAME as first argument and the filename as second argument. TCODE is expected to return a truth value that if the test should be run. If TCODE returns something that is not just a raw truth value (e.g. a hash ref), this will be taken as the ``test'', otherwise this sub will attempt to guess the test name from the file. 
 If TCODE is omitted, ``is_tag_in_file(TAGNAME, FILENAME)'' will be used. 
 Returns a list of values returned by TCODE or guessed test names (as per above) 
</dd></dl>
