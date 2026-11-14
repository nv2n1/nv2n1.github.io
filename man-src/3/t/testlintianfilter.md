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
<h2>Functions</h2><dl COMPACT><dt>get_suitepath(<font SIZE="-1">TEST_SET, SUITE</font>)
<dd>Returns a string containing all test belonging to suite <font SIZE="-1">SUITE</font> relative to path <font SIZE="-1">TEST_SET.</font>
<dt>find_selected_scripts(<font SIZE="-1">SCRIPT_PATH, ONLY_RUN</font>)
<dd>Find all test scripts in <font SIZE="-1">SCRIPT_PATH</font> that are identified by the user's selection string <font SIZE="-1">ONLY_RUN.</font>
<dt>find_selected_lintian_testpaths(<font SIZE="-1">TEST_SET, ONLY_RUN</font>)
<dd>Find all those test paths with Lintian tests located in the directory <font SIZE="-1">TEST_SET</font> and identified by the user's selection string <font SIZE="-1">ONLY_RUN.</font>
<dt>find_all_testpaths(<font SIZE="-1">PATH</font>)
<dd>Returns an array containing all test paths located under <font SIZE="-1">PATH.</font> They are identified as test paths by a specially named file containing the test description (presently 'desc').
<dt>find_testpaths_by_name(<font SIZE="-1">PATH, NAME</font>)
<dd>Returns an array containing all test paths with the name <font SIZE="-1">NAME</font> located under <font SIZE="-1">PATH.</font> The test paths are identified as such by a specially named file containing the test description (presently 'desc').
<dt>find_all_tags(<font SIZE="-1">TEST_PATH</font>)
<dd>Returns an array containing all tags that somehow concern the test located in <font SIZE="-1">TEST_PATH.</font> 

</dl>
