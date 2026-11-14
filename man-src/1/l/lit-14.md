---
title: "lit-14(1)"
name: "lit-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lit-14/"
description: "lit – LLVM Integrated Tester"
---

<h2 class="name">NAME</h2>
<p> lit &#8211; LLVM Integrated Tester </p>
<h2>SYNOPSIS</h2>
<p> <code>lit</code> [<i>options</i>] [<i>tests</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lit</code> is a portable tool for executing LLVM and Clang style test suites, summarizing their results, and providing indication of failures. <code>lit</code> is designed to be a lightweight testing tool with as simple a user interface as possible. </p>
<p> <code>lit</code> should be run with one or more <i>tests</i> to run specified on the command line. Tests can be either individual test files or directories to search for tests (see <i>TEST DISCOVERY</i>). </p>
<p> Each specified test will be executed (potentially concurrently) and once all tests have been run <code>lit</code> will print summary information on the number of tests which passed or failed (see <i>TEST STATUS RESULTS</i>). The <code>lit</code> program will execute with a non-zero exit code if any tests fail. </p>
<p> By default <code>lit</code> will use a succinct progress display and will only print summary information for test failures. See <i>OUTPUT OPTIONS</i> for options controlling the <code>lit</code> progress display and output. </p>
<p> <code>lit</code> also includes a number of options for controlling how tests are executed (specific features may depend on the particular test format). See <i>EXECUTION OPTIONS</i> for more information. </p>
<p> Finally, <code>lit</code> also supports additional options for only running a subset of the options specified on the command line, see <i>SELECTION OPTIONS</i> for more information. </p>
<p> <code>lit</code> parses options from the environment variable <code>LIT_OPTS</code> after parsing options from the command line. <code>LIT_OPTS</code> is primarily useful for supplementing or overriding the command-line options supplied to <code>lit</code> by <code>check</code> targets defined by a project’s build system. </p>
<p> Users interested in the <code>lit</code> architecture or designing a <code>lit</code> testing implementation should see <i>LIT INFRASTRUCTURE</i>.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the <code>lit</code> help message.</p>
<dt><code>-j N, &#8211;workers=N</code></p>
<dd> Run <code>N</code> tests in parallel. By default, this is automatically chosen to match the number of detected available CPUs.</p>
<dt><code>&#8211;config-prefix=NAME</code></p>
<dd> Search for <i>NAME</i><code>.cfg</code> and <i>NAME</i><code>.site.cfg</code> when searching for test suites, instead of <code>lit.cfg</code> and <code>lit.site.cfg</code>.</p>
<dt><code>-D NAME[=VALUE], &#8211;param NAME[=VALUE]</code></p>
<dd> Add a user defined parameter <code>NAME</code> with the given <code>VALUE</code> (or the empty string if not given). The meaning and use of these parameters is test suite dependent.</dl>
<h2>OUTPUT OPTIONS</h2>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress any output except for test failures.</p>
<dt><code>-s, &#8211;succinct</code></p>
<dd> Show less output, for example don’t show information on tests that pass. Also show a progress bar, unless <code>&#8211;no-progress-bar</code> is specified.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Show more information on test failures, for example the entire test output instead of just the test result.</p>
<dt><code>-vv, &#8211;echo-all-commands</code></p>
<dd> Echo all commands to stdout, as they are being executed. This can be valuable for debugging test failures, as the last echoed command will be the one which has failed. <code>lit</code> normally inserts a no-op command (<code>:</code> in the case of bash) with argument <code>&#8216;RUN: at line N&#8217;</code> before each command pipeline, and this option also causes those no-op commands to be echoed to stdout to help you locate the source line of the failed command. This option implies <code>&#8211;verbose</code>.</p>
<dt><code>-a, &#8211;show-all</code></p>
<dd> Show more information about all tests, for example the entire test commandline and output.</p>
<dt><code>&#8211;no-progress-bar</code></p>
<dd> Do not use curses based progress bar.</p>
<dt><code>&#8211;show-unsupported</code></p>
<dd> Show the names of unsupported tests.</p>
<dt><code>&#8211;show-xfail</code></p>
<dd> Show the names of tests that were expected to fail.</dl>
<h2>EXECUTION OPTIONS</h2>
<dl>
<dt><code>&#8211;path=PATH</code></p>
<dd> Specify an additional <code>PATH</code> to use when searching for executables in tests.</p>
<dt><code>&#8211;vg</code></p>
<dd> Run individual tests under valgrind (using the memcheck tool). The <code>&#8211;error-exitcode</code> argument for valgrind is used so that valgrind failures will cause the program to exit with a non-zero status. </p>
<p> When this option is enabled, <code>lit</code> will also automatically provide a “<code>valgrind</code>” feature that can be used to conditionally disable (or expect failure in) certain tests.</p>
<dt><code>&#8211;vg-arg=ARG</code></p>
<dd> When <i>&#8211;vg</i> is used, specify an additional argument to pass to <code>valgrind</code> itself.</p>
<dt><code>&#8211;vg-leak</code></p>
<dd> When <i>&#8211;vg</i> is used, enable memory leak checks. When this option is enabled, <code>lit</code> will also automatically provide a “<code>vg_leak</code>” feature that can be used to conditionally disable (or expect failure in) certain tests.</p>
<dt><code>&#8211;time-tests</code></p>
<dd> Track the wall time individual tests take to execute and includes the results in the summary output. This is useful for determining which tests in a test suite take the most time to execute.</p>
<dt><code>&#8211;ignore-fail</code></p>
<dd> Exit with status zero even if some tests fail.</p>
<dt><code>&#8211;no-indirectly-run-check</code></p>
<dd> Do not error if a test would not be run if the user had specified the containing directory instead of naming the test directly.</dl>
<h2>SELECTION OPTIONS</h2>
<p> By default, <i>lit</i> will run failing tests first, then run tests in descending execution time order to optimize concurrency. The execution order can be changed using the <i>&#8211;order</i> option. </p>
<p> The timing data is stored in the <i>test_exec_root</i> in a file named <i>.lit_test_times.txt</i>. If this file does not exist, then <i>lit</i> checks the <i>test_source_root</i> for the file to optionally accelerate clean builds.</p>
<dl>
<dt><code>&#8211;shuffle</code></p>
<dd> Run the tests in a random order, not failing/slowest first. Deprecated, use <i>&#8211;order</i> instead.</p>
<dt><code>&#8211;max-failures N</code></p>
<dd> Stop execution after the given number <code>N</code> of failures. An integer argument should be passed on the command line prior to execution.</p>
<dt><code>&#8211;max-tests=N</code></p>
<dd> Run at most <code>N</code> tests and then terminate.</p>
<dt><code>&#8211;max-time=N</code></p>
<dd> Spend at most <code>N</code> seconds (approximately) running tests and then terminate. Note that this is not an alias for <i>&#8211;timeout</i>; the two are different kinds of maximums.</p>
<dt><code>&#8211;num-shards=M</code></p>
<dd> Divide the set of selected tests into <code>M</code> equal-sized subsets or “shards”, and run only one of them. Must be used with the <code>&#8211;run-shard=N</code> option, which selects the shard to run. The environment variable <code>LIT_NUM_SHARDS</code> can also be used in place of this option. These two options provide a coarse mechanism for partitioning large testsuites, for parallel execution on separate machines (say in a large testing farm).</p>
<dt><code>&#8211;order={lexical,random,smart}</code></p>
<dd> Define the order in which tests are run. The supported values are:</p>
<dt>&bull;</p>
<dd> lexical &#8211; tests will be run in lexical order according to the test file path. This option is useful when predictable test order is desired.</p>
<dt>&bull;</p>
<dd> random &#8211; tests will be run in random order.</p>
<dt>&bull;</p>
<dd> smart &#8211; tests that failed previously will be run first, then the remaining tests, all in descending execution time order. This is the default as it optimizes concurrency.</p>
<dt><code>&#8211;run-shard=N</code></p>
<dd> Select which shard to run, assuming the <code>&#8211;num-shards=M</code> option was provided. The two options must be used together, and the value of <code>N</code> must be in the range <code>1..M</code>. The environment variable <code>LIT_RUN_SHARD</code> can also be used in place of this option.</p>
<dt><code>&#8211;timeout=N</code></p>
<dd> Spend at most <code>N</code> seconds (approximately) running each individual test. <code>0</code> means no time limit, and <code>0</code> is the default. Note that this is not an alias for <i>&#8211;max-time</i>; the two are different kinds of maximums.</p>
<dt><code>&#8211;filter=REGEXP</code></p>
<dd> Run only those tests whose name matches the regular expression specified in <code>REGEXP</code>. The environment variable <code>LIT_FILTER</code> can be also used in place of this option, which is especially useful in environments where the call to <code>lit</code> is issued indirectly.</p>
<dt><code>&#8211;filter-out=REGEXP</code></p>
<dd> Filter out those tests whose name matches the regular expression specified in <code>REGEXP</code>. The environment variable <code>LIT_FILTER_OUT</code> can be also used in place of this option, which is especially useful in environments where the call to <code>lit</code> is issued indirectly.</p>
<dt><code>&#8211;xfail=LIST</code></p>
<dd> Treat those tests whose name is in the semicolon separated list <code>LIST</code> as <code>XFAIL</code>. This can be helpful when one does not want to modify the test suite. The environment variable <code>LIT_XFAIL</code> can be also used in place of this option, which is especially useful in environments where the call to <code>lit</code> is issued indirectly. </p>
<p> A test name can specified as a file name relative to the test suite directory. For example: </p>
<pre>
LIT_XFAIL=&quot;affinity/kmp-hw-subset.c;offloading/memory_manager.cpp&quot;
</pre>
<p> In this case, all of the following tests are treated as <code>XFAIL</code>: </p>
<pre>
libomp :: affinity/kmp-hw-subset.c
libomptarget :: nvptx64-nvidia-cuda :: offloading/memory_manager.cpp
libomptarget :: x86_64-pc-linux-gnu :: offloading/memory_manager.cpp
</pre>
<p> Alternatively, a test name can be specified as the full test name reported in LIT output. For example, we can adjust the previous example not to treat the <code>nvptx64-nvidia-cuda</code> version of <code>offloading/memory_manager.cpp</code> as XFAIL: </p>
<pre>
LIT_XFAIL=&quot;affinity/kmp-hw-subset.c;libomptarget :: x86_64-pc-linux-gnu :: offloading/memory_manager.cpp&quot;
</pre>
<dt><code>&#8211;xfail-not=LIST</code></p>
<dd> Do not treat the specified tests as <code>XFAIL</code>. The environment variable <code>LIT_XFAIL_NOT</code> can also be used in place of this option. The syntax is the same as for <i>&#8211;xfail</i> and <code>LIT_XFAIL</code>. <i>&#8211;xfail-not</i> and <code>LIT_XFAIL_NOT</code> always override all other <code>XFAIL</code> specifications, including an <i>&#8211;xfail</i> appearing later on the command line. The primary purpose is to suppress an <code>XPASS</code> result without modifying a test case that uses the <code>XFAIL</code> directive.</dl>
<h2>ADDITIONAL OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Run <code>lit</code> in debug mode, for debugging configuration issues and <code>lit</code> itself.</p>
<dt><code>&#8211;show-suites</code></p>
<dd> List the discovered test suites and exit.</p>
<dt><code>&#8211;show-tests</code></p>
<dd> List all of the discovered tests and exit.</dl>
<h2>EXIT STATUS</h2>
<p> <code>lit</code> will exit with an exit code of 1 if there are any FAIL or XPASS results. Otherwise, it will exit with the status 0. Other exit codes are used for non-test related failures (for example a user error or an internal program error).</p>
<h2>TEST DISCOVERY</h2>
<p> The inputs passed to <code>lit</code> can be either individual tests, or entire directories or hierarchies of tests to run. When <code>lit</code> starts up, the first thing it does is convert the inputs into a complete list of tests to run as part of <i>test discovery</i>. </p>
<p> In the <code>lit</code> model, every test must exist inside some <i>test suite</i>. <code>lit</code> resolves the inputs specified on the command line to test suites by searching upwards from the input path until it finds a <code>lit.cfg</code> or <code>lit.site.cfg</code> file. These files serve as both a marker of test suites and as configuration files which <code>lit</code> loads in order to understand how to find and run the tests inside the test suite. </p>
<p> Once <code>lit</code> has mapped the inputs into test suites it traverses the list of inputs adding tests for individual files and recursively searching for tests in directories. </p>
<p> This behavior makes it easy to specify a subset of tests to run, while still allowing the test suite configuration to control exactly how tests are interpreted. In addition, <code>lit</code> always identifies tests by the test suite they are in, and their relative path inside the test suite. For appropriately configured projects, this allows <code>lit</code> to provide convenient and flexible support for out-of-tree builds.</p>
<h2>TEST STATUS RESULTS</h2>
<p> Each test ultimately produces one of the following eight results: </p>
<p> <code>PASS</code> The test succeeded. </p>
<p> <code>FLAKYPASS</code> The test succeeded after being re-run more than once. This only applies to tests containing an <code>ALLOW_RETRIES:</code> annotation. </p>
<p> <code>XFAIL</code> The test failed, but that is expected. This is used for test formats which allow specifying that a test does not currently work, but wish to leave it in the test suite. </p>
<p> <code>XPASS</code> The test succeeded, but it was expected to fail. This is used for tests which were specified as expected to fail, but are now succeeding (generally because the feature they test was broken and has been fixed). </p>
<p> <code>FAIL</code> The test failed. </p>
<p> <code>UNRESOLVED</code> The test result could not be determined. For example, this occurs when the test could not be run, the test itself is invalid, or the test was interrupted. </p>
<p> <code>UNSUPPORTED</code> The test is not supported in this environment. This is used by test formats which can report unsupported tests. </p>
<p> <code>TIMEOUT</code> The test was run, but it timed out before it was able to complete. This is considered a failure. </p>
<p> Depending on the test format tests may produce additional information about their status (generally only for failures). See the <i>OUTPUT OPTIONS</i> section for more information.</p>
<h2>LIT INFRASTRUCTURE</h2>
<p> This section describes the <code>lit</code> testing architecture for users interested in creating a new <code>lit</code> testing implementation, or extending an existing one. </p>
<p> <code>lit</code> proper is primarily an infrastructure for discovering and running arbitrary tests, and to expose a single convenient interface to these tests. <code>lit</code> itself doesn’t know how to run tests, rather this logic is defined by <i>test suites</i>.</p>
<h3>TEST SUITES</h3>
<p> As described in <i>TEST DISCOVERY</i>, tests are always located inside a <i>test suite</i>. Test suites serve to define the format of the tests they contain, the logic for finding those tests, and any additional information to run the tests. </p>
<p> <code>lit</code> identifies test suites as directories containing <code>lit.cfg</code> or <code>lit.site.cfg</code> files (see also <i>&#8211;config-prefix</i>). Test suites are initially discovered by recursively searching up the directory hierarchy for all the input files passed on the command line. You can use <i>&#8211;show-suites</i> to display the discovered test suites at startup. </p>
<p> Once a test suite is discovered, its config file is loaded. Config files themselves are Python modules which will be executed. When the config file is executed, two important global variables are predefined: </p>
<p> <code>lit_config</code> The global <code>lit</code> configuration object (a <i>LitConfig</i> instance), which defines the builtin test formats, global configuration parameters, and other helper routines for implementing test configurations. </p>
<p> <code>config</code> This is the config object (a <i>TestingConfig</i> instance) for the test suite, which the config file is expected to populate. The following variables are also available on the <i>config</i> object, some of which must be set by the config and others are optional or predefined: </p>
<p> <code>name</code> <i>[required]</i> The name of the test suite, for use in reports and diagnostics. </p>
<p> <code>test_format</code> <i>[required]</i> The test format object which will be used to discover and run tests in the test suite. Generally this will be a builtin test format available from the <i>lit.formats</i> module. </p>
<p> <code>test_source_root</code> The filesystem path to the test suite root. For out-of-dir builds this is the directory that will be scanned for tests. </p>
<p> <code>test_exec_root</code> For out-of-dir builds, the path to the test suite root inside the object directory. This is where tests will be run and temporary output files placed. </p>
<p> <code>environment</code> A dictionary representing the environment to use when executing tests in the suite. </p>
<p> <code>standalone_tests</code> When true, mark a directory with tests expected to be run standalone. Test discovery is disabled for that directory and <i>–no-indirectly-run-check</i> is in effect. <i>lit.suffixes</i> and <i>lit.excludes</i> must be empty when this variable is true. </p>
<p> <code>suffixes</code> For <code>lit</code> test formats which scan directories for tests, this variable is a list of suffixes to identify test files. Used by: <i>ShTest</i>. </p>
<p> <code>substitutions</code> For <code>lit</code> test formats which substitute variables into a test script, the list of substitutions to perform. Used by: <i>ShTest</i>. </p>
<p> <code>unsupported</code> Mark an unsupported directory, all tests within it will be reported as unsupported. Used by: <i>ShTest</i>. </p>
<p> <code>parent</code> The parent configuration, this is the config object for the directory containing the test suite, or None. </p>
<p> <code>root</code> The root configuration. This is the top-most <code>lit</code> configuration in the project. </p>
<p> <code>pipefail</code> Normally a test using a shell pipe fails if any of the commands on the pipe fail. If this is not desired, setting this variable to false makes the test fail only if the last command in the pipe fails. </p>
<p> <code>available_features</code> A set of features that can be used in <i>XFAIL</i>, <i>REQUIRES</i>, and <i>UNSUPPORTED</i> directives.</p>
<h3>TEST DISCOVERY</h3>
<p> Once test suites are located, <code>lit</code> recursively traverses the source directory (following <i>test_source_root</i>) looking for tests. When <code>lit</code> enters a sub-directory, it first checks to see if a nested test suite is defined in that directory. If so, it loads that test suite recursively, otherwise it instantiates a local test config for the directory (see <i>LOCAL CONFIGURATION FILES</i>). </p>
<p> Tests are identified by the test suite they are contained within, and the relative path inside that suite. Note that the relative path may not refer to an actual file on disk; some test formats (such as <i>GoogleTest</i>) define “virtual tests” which have a path that contains both the path to the actual test file and a subpath to identify the virtual test.</p>
<h3>LOCAL CONFIGURATION FILES</h3>
<p> When <code>lit</code> loads a subdirectory in a test suite, it instantiates a local test configuration by cloning the configuration for the parent directory — the root of this configuration chain will always be a test suite. Once the test configuration is cloned <code>lit</code> checks for a <i>lit.local.cfg</i> file in the subdirectory. If present, this file will be loaded and can be used to specialize the configuration for each individual directory. This facility can be used to define subdirectories of optional tests, or to change other configuration parameters — for example, to change the test format, or the suffixes which identify test files.</p>
<h3>SUBSTITUTIONS</h3>
<p> <code>lit</code> allows patterns to be substituted inside RUN commands. It also provides the following base set of substitutions, which are defined in TestRunner.py: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Macro </td>
<td> Substitution
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %s </td>
<td> source path (path to the file currently being run)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %S </td>
<td> source dir (directory of the file currently being run)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %p </td>
<td> same as %S
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{pathsep} </td>
<td> path separator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %t </td>
<td> temporary file name unique to the test
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %basename_t </td>
<td> The last path component of %t but without the <code>.tmp</code> extension
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %T </td>
<td> parent directory of %t (not unique, deprecated, do not use)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %% </td>
<td> %
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %/s </td>
<td> %s but <code>\</code> is replaced by <code>/</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %/S </td>
<td> %S but <code>\</code> is replaced by <code>/</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %/p </td>
<td> %p but <code>\</code> is replaced by <code>/</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %/t </td>
<td> %t but <code>\</code> is replaced by <code>/</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %/T </td>
<td> %T but <code>\</code> is replaced by <code>/</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{/s:regex_replacement} </td>
<td> %/s but escaped for use in the replacement of a <code>s@@@</code> command in sed
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{/S:regex_replacement} </td>
<td> %/S but escaped for use in the replacement of a <code>s@@@</code> command in sed
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{/p:regex_replacement} </td>
<td> %/p but escaped for use in the replacement of a <code>s@@@</code> command in sed
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{/t:regex_replacement} </td>
<td> %/t but escaped for use in the replacement of a <code>s@@@</code> command in sed
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %{/T:regex_replacement} </td>
<td> %/T but escaped for use in the replacement of a <code>s@@@</code> command in sed
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %:s </td>
<td> On Windows, %/s but a <code>:</code> is removed if its the second character. Otherwise, %s but with a single leading <code>/</code> removed.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %:S </td>
<td> On Windows, %/S but a <code>:</code> is removed if its the second character. Otherwise, %S but with a single leading <code>/</code> removed.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %:p </td>
<td> On Windows, %/p but a <code>:</code> is removed if its the second character. Otherwise, %p but with a single leading <code>/</code> removed.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %:t </td>
<td> On Windows, %/t but a <code>:</code> is removed if its the second character. Otherwise, %t but with a single leading <code>/</code> removed.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> %:T </td>
<td> On Windows, %/T but a <code>:</code> is removed if its the second character. Otherwise, %T but with a single leading <code>/</code> removed.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Other substitutions are provided that are variations on this base set and further substitution patterns can be defined by each test module. See the modules <i>LOCAL CONFIGURATION FILES</i>. </p>
<p> By default, substitutions are expanded exactly once, so that if e.g. a substitution <code>%build</code> is defined in top of another substitution <code>%cxx</code>, <code>%build</code> will expand to <code>%cxx</code> textually, not to what <code>%cxx</code> expands to. However, if the <code>recursiveExpansionLimit</code> property of the <code>TestingConfig</code> is set to a non-negative integer, substitutions will be expanded recursively until that limit is reached. It is an error if the limit is reached and expanding substitutions again would yield a different result. </p>
<p> More detailed information on substitutions can be found in the ../TestingGuide.</p>
<h3>TEST RUN OUTPUT FORMAT</h3>
<p> The <code>lit</code> output for a test run conforms to the following schema, in both short and verbose modes (although in short mode no PASS lines will be shown). This schema has been chosen to be relatively easy to reliably parse by a machine (for example in buildbot log scraping), and for other tools to generate. </p>
<p> Each test result is expected to appear on a line that matches: </p>
<pre>
&lt;result code&gt;: &lt;test name&gt; (&lt;progress info&gt;)
</pre>
<p> where <code>&lt;result-code&gt;</code> is a standard test result such as PASS, FAIL, XFAIL, XPASS, UNRESOLVED, or UNSUPPORTED. The performance result codes of IMPROVED and REGRESSED are also allowed. </p>
<p> The <code>&lt;test name&gt;</code> field can consist of an arbitrary string containing no newline. </p>
<p> The <code>&lt;progress info&gt;</code> field can be used to report progress information such as (1/300) or can be empty, but even when empty the parentheses are required. </p>
<p> Each test result may include additional (multiline) log information in the following format: </p>
<pre>
&lt;log delineator&gt; TEST '(&lt;test name&gt;)' &lt;trailing delineator&gt;
... log message ...
&lt;log delineator&gt;
</pre>
<p> where <code>&lt;test name&gt;</code> should be the name of a preceding reported test, <code>&lt;log delineator&gt;</code> is a string of “*” characters <i>at least</i> four characters long (the recommended length is 20), and <code>&lt;trailing delineator&gt;</code> is an arbitrary (unparsed) string. </p>
<p> The following is an example of a test run output which consists of four tests A, B, C, and D, and a log message for the failing test C: </p>
<pre>
PASS: A (1 of 4)
PASS: B (2 of 4)
FAIL: C (3 of 4)
******************** TEST 'C' FAILED ********************
Test 'C' failed as a result of exit code 1.
********************
PASS: D (4 of 4)
</pre>
<h3>LIT EXAMPLE TESTS</h3>
<p> The <code>lit</code> distribution contains several example implementations of test suites in the <i>ExampleTests</i> directory.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1)</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
