---
title: "testlintian(3)"
name: "testlintian"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintian/"
description: "Test::Lintian — Check Lintian files for issues"
---

<p>Test::Lintian &#8212; Check Lintian files for issues </p>
<h2>Synopsis</h2>
<pre> # file 1
 use Test::Lintian;
 use Test::More import =&gt; ['done_testing'];
 test_load_profiles('some/path');
 done_testing;
 # file 2
 use Test::Lintian;
 use Test::More import =&gt; ['done_testing'];
 load_profile_for_test('vendor/profile', 'some/path', '/usr/share/lintian');
 test_check_desc('some/path/checks');
 test_load_checks('some/path/checks');
 test_tags_implemented('some/path/checks');
 done_testing;</pre>
<h2>Description</h2>
<p>A testing framework for testing various Lintian files for common errors.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>test_check_desc([<font SIZE="-1">OPTS,</font> ]CHECKS&#8230;)</p>
<dd>Test check desc files (and the tags in them) for common errors. </p>
<p> <font SIZE="-1">OPTS</font> is an optional <font SIZE="-1">HAShref</font> containing key/value pairs, which are described below. </p>
<p> <font SIZE="-1">CHECKS</font> is a list of paths in which to check desc files. Any given element in <font SIZE="-1">CHECKS</font> can be either a file or a dir. Files are assumed to be check desc file. Directories are searched and all <i>.desc</i> files in those dirs are processed. </p>
<p> As the number of tests depends on the number of tags in desc, it is difficult to &#8220;plan ahead&#8221; when using this test. It is therefore recommended to not specify a plan and use <code>done_testing()</code>. </p>
<p> This sub uses a Data file (see &#8220;load_profile_for_test ([PROFNAME[, <font SIZE="-1">INC&#8230;</font>]])&#8221;). </p>
<p> <font SIZE="-1">OPTS</font> may contain the following key/value pairs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>filter</p>
<dd>If defined, it is a filter function that examines <tt>$_</tt> (or its first argument) and returns a truth value if <tt>$_</tt> should be considered or false otherwise. <tt>$_</tt> will be the path to the current file (or dir) in question; it may be relative or absolute. </p>
<p> <font SIZE="-1">NB:</font> <i>all</i> elements in <font SIZE="-1">CHECKS</font> are subject to the filter. </p>
<p> <font SIZE="-1">CAVEAT:</font> If the filter rejects a directory, none of the files in it will be considered either. Even if the filter accepts a file, that file will only be processed if it has the proper extension (i.e. with <i>.desc</i>).</p>
<dt>translation</p>
<dd>If defined and a truth value, the desc files are expected to contain translations. Otherwise, they must be regular checks.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>test_load_profiles(<font SIZE="-1">ROOT, INC&#8230;</font>)</p>
<dd>Test that all profiles in <i>ROOT/profiles</i> are loadable. <font SIZE="-1">INC</font> will be the <font SIZE="-1">INC</font> path used as include path for the profile. </p>
<p> If <font SIZE="-1">INC</font> is omitted, then the include path will consist of (<font SIZE="-1">ROOT,</font> &#8216;/usr/share/lintian&#8217;). Otherwise, <font SIZE="-1">INC</font> will be used as is (and should include <font SIZE="-1">ROOT</font>). </p>
<p> This sub will do one test per profile loaded.</p>
<dt>test_load_checks([<font SIZE="-1">OPTS,</font> ]DIR[, <font SIZE="-1">CHECKNAMES&#8230;</font>])</p>
<dd>Test that the Perl module implementation of the checks can be loaded and has a run sub. </p>
<p> <font SIZE="-1">OPTS</font> is an optional <font SIZE="-1">HAShref</font> containing key/value pairs, which are described below. </p>
<p> <font SIZE="-1">DIR</font> is the directory where the checks can be found. </p>
<p> <font SIZE="-1">CHECKNAMES</font> is a list of check names. If <font SIZE="-1">CHECKNAMES</font> is given, only the checks in this list will be processed. Otherwise, all the checks in <font SIZE="-1">DIR</font> will be processed. </p>
<p> For planning purposes, every check processed counts for 2 tests and the call itself does on additional check. So if <font SIZE="-1">CHECKNAMES</font> contains 10 elements, then 21 tests will be done (2 * 10 + 1). Filtered out checks will <i>not</i> be counted. </p>
<p> All data files created at compile time or in the file scope will be loaded immediately (instead of lazily as done during the regular runs). This is done to spot missing data files or typos in their names. Therefore, this sub will load a profile if one hasn&#8217;t been loaded already. (see &#8220;load_profile_for_test ([PROFNAME[, <font SIZE="-1">INC&#8230;</font>]])&#8221;) </p>
<p> <font SIZE="-1">OPTS</font> may contain the following key/value pairs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>filter</p>
<dd>If defined, it is a filter function that examines <tt>$_</tt> (or its first argument) and returns a truth value if <tt>$_</tt> should be considered or false otherwise. <tt>$_</tt> will be the path to the current file (or dir) in question; it may be relative or absolute. </p>
<p> <font SIZE="-1">NB:</font> filter is <i>not</i> used if <font SIZE="-1">CHECKNAMES</font> is given. </p>
<p> <font SIZE="-1">CAVEAT:</font> If the filter rejects a directory, none of the files in it will be considered either. Even if the filter accepts a file, that file will only be processed if it has the proper extension (i.e. with <i>.desc</i>).</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>test_tags_implemented ([<font SIZE="-1">OPTS,</font> ]DIR[, <font SIZE="-1">CHECKNAMES&#8230;</font>])</p>
<dd>Test a given check implements all the tags listed in its desc file. For planning purposes, each check counts as one test and the call itself do one additional check. So if 10 checks are tested, the plan should account for 11 tests. </p>
<p> This is a simple scan of the source code looking asserting that the tag names <i>appear</i> (in the actual code part). For a vast majority of Lintian&#8217;s tags it is reliable enough to be useful. However it has false-positives and false-negatives &#8211; the former can be handled via &#8220;exclude-pattern&#8221; (see below). </p>
<p> The <font SIZE="-1">DIR</font> argument is the directory in which to find the checks. </p>
<p> <font SIZE="-1">CHECKNAMES</font> is a list of the check names. If <font SIZE="-1">CHECKNAMES</font> is given, only the checks in this list will be processed. Otherwise, all the checks in <font SIZE="-1">DIR</font> will be processed. </p>
<p> The optional parameter <font SIZE="-1">OPTS</font> is a hashref. If passed it must be the first argument. The following key/value pairs are defined:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>exclude-pattern</p>
<dd>The value is assumed to be a regex (or a string describing a regex). Any tag matching this regex will be excluded from this test and is assumed to be implemented (regardless of whether that is true or not). </p>
<p> This is useful for avoiding false-positives with cases like: </p>
<pre> foreach my $x (@y) {
 tag &quot;some-tag-for-$x&quot;, &quot;blah blah $x&quot;
 unless f($x);
 }</pre>
<dt>filter</p>
<dd>If defined, it is a filter function that examines <tt>$_</tt> (or its first argument) and returns a truth value if <tt>$_</tt> should be considered or false otherwise. <tt>$_</tt> will be the path to the current file (or dir) in question; it may be relative or absolute. </p>
<p> <font SIZE="-1">NB:</font> filter is <i>not</i> used if <font SIZE="-1">CHECKNAMES</font> is given. </p>
<p> <font SIZE="-1">CAVEAT:</font> If the filter rejects a directory, none of the files in it will be considered either. Even if the filter accepts a file, that file will only be processed if it has the proper extension (i.e. with <i>.desc</i>).</dl>
</dl>
<dl COMPACT>
<dd>As mentioned, this test assert that the tag name appears in the code. Consider the following example: </p>
<pre> my $tagname = 'my-tag';
 $tagname = 'my-other-tag' if $condition;</pre>
<p>In this example, this test would conclude that &#8216;my-tag&#8217; and &#8216;my-other-tag&#8217; are both implemented. </p>
<p> Comment lines are <i>not</i> ignored, so comments can be used as an alternative to the exclude-pattern (above).</dl>
<dt>load_profile_for_test ([PROFNAME[, <font SIZE="-1">INC&#8230;</font>]])</p>
<dd>Load a Lintian::Profile and ensure Data files can be used. This is needed if the test needs to access a data file or if a special profile is needed for the test. It does <i>not</i> test the profile for issues. </p>
<p> <font SIZE="-1">PROFNAME</font> is the name of the profile to load. It can be omitted, in which case the sub ensures that a profile has been loaded. If no profile has been loaded, &#8216;debian/main&#8217; will be loaded. </p>
<p> <font SIZE="-1">INC</font> is a list of extra &#8220;include dirs&#8221; (or Lintian &#8220;roots&#8221;) to be used for finding the profile. If not specified, it defaults to <i></i>$ENV<i>{&#8216;</i><font SIZE="-1"><i>LINTIAN_TEST_ROOT</i></font><i>&#8216;}</i> and <i>/usr/share/lintian</i> (in order). <font SIZE="-1">INC</font> is ignored if a profile has already been loaded. </p>
<p> <font SIZE="-1">CAVEAT:</font> Only one profile can be loaded in a given test. Once a profile has been loaded, it is not possible to replace it with another one. So if this is invoked multiple times, <font SIZE="-1">PROFNAME</font> must be omitted or must match the name of the loaded profile.</p>
<dt>program_name_to_perl_paths(<font SIZE="-1">PROGNAME</font>)</p>
<dd>Map the program name (e.g. <tt>$0</tt>) to a list of directories or/and files that should be processed. </p>
<p> This helper sub is mostly useful for splitting up slow tests run over all Perl scripts/modules in Lintian. This allows better use of multiple cores. Example: </p>
<pre> t/scripts/my-test/
 runner.pl
 checks.t -&gt; runner.pl
 collection.t -&gt; runner.pl
 ...</pre>
<p>And then in runner.pl: </p>
<pre> use Test::Lintian;
 
 my @paths = program_name_to_perl_paths($0);
 # test all files/dirs listed in @paths</pre>
<p>For a more concrete example, see t/scripts/01-critic/ and the files/symlinks beneath it. </p>
</dl>
