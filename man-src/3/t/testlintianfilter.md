---
title: "testlintianfilter(3)"
name: "testlintianfilter"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianfilter/"
---

Test::Lintian::Filter -- Functions to select with tests to run 

<h2>Synopsis</h2><pre> use Test::Lintian::Filter qw(find_selected_lintian_testpaths);
 my @testpaths = find_selected_lintian_testpaths('suite:changes');</pre><h2>Description</h2>Functions that parse the optional argument 'only_run' to find the tests that are supposed to run.
<h2>Functions</h2><dl COMPACT><dt>get_suitepath(TEST_SET, SUITE)
</dt><dd>Returns a string containing all test belonging to suite SUITE relative to path TEST_SET.
</dd><dt>find_selected_scripts(SCRIPT_PATH, ONLY_RUN)
</dt><dd>Find all test scripts in SCRIPT_PATH that are identified by the user's selection string ONLY_RUN.
</dd><dt>find_selected_lintian_testpaths(TEST_SET, ONLY_RUN)
</dt><dd>Find all those test paths with Lintian tests located in the directory TEST_SET and identified by the user's selection string ONLY_RUN.
</dd><dt>find_all_testpaths(PATH)
</dt><dd>Returns an array containing all test paths located under PATH. They are identified as test paths by a specially named file containing the test description (presently 'desc').
</dd><dt>find_testpaths_by_name(PATH, NAME)
</dt><dd>Returns an array containing all test paths with the name NAME located under PATH. The test paths are identified as such by a specially named file containing the test description (presently 'desc').
</dd><dt>find_all_tags(TEST_PATH)
</dt><dd>Returns an array containing all tags that somehow concern the test located in TEST_PATH. 
</dd></dl>
