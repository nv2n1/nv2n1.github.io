---
title: "lit(1)"
name: "lit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lit/"
description: "lit – LLVM Integrated Tester"
---

<h2 class="name">NAME</h2>
<p> lit &#8211; LLVM Integrated Tester </p>
<h2>SYNOPSIS</h2>
<p> <code>lit</code> [<i>options</i>] [<i>tests</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lit</code> is a portable tool for executing <font SIZE="-1">LLVM</font> and Clang style test suites, summarizing their results, and providing indication of failures. <code>lit</code> is designed to be a lightweight testing tool with as simple a user interface as possible. </p>
<p> <code>lit</code> should be run with one or more <i>tests</i> to run specified on the command line. Tests can be either individual test files or directories to search for tests (see &#8220;<font SIZE="-1">TEST</font> <font SIZE="-1">DISCOVERY</font>&#8221;). </p>
<p> Each specified test will be executed (potentially in parallel) and once all tests have been run <code>lit</code> will print summary information on the number of tests which passed or failed (see &#8220;<font SIZE="-1">TEST</font> <font SIZE="-1">STATUS</font> <font SIZE="-1">RESULTS</font>&#8221;). The <code>lit</code> program will execute with a non-zero exit code if any tests fail. </p>
<p> By default <code>lit</code> will use a succinct progress display and will only print summary information for test failures. See &#8220;<font SIZE="-1">OUTPUT</font> <font SIZE="-1">OPTIONS</font>&#8221; for options controlling the <code>lit</code> progress display and output. </p>
<p> <code>lit</code> also includes a number of options for controlling how tests are exected (specific features may depend on the particular test format). See &#8220;<font SIZE="-1">EXECUTION</font> <font SIZE="-1">OPTIONS</font>&#8221; for more information. </p>
<p> Finally, <code>lit</code> also supports additional options for only running a subset of the options specified on the command line, see &#8220;<font SIZE="-1">SELECTION</font> <font SIZE="-1">OPTIONS</font>&#8221; for more information. </p>
<p> Users interested in the <code>lit</code> architecture or designing a <code>lit</code> testing implementation should see &#8220;<font SIZE="-1">LIT</font> <font SIZE="-1">ARCHITECTURE</font>&#8221;</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the <code>lit</code> help message.</p>
<dt><code>-j</code> <i>N</i>, <code>&#8211;threads</code>=<i>N</i></p>
<dd> Run <i>N</i> tests in parallel. By default, this is automatically chosen to match the number of detected available CPUs.</p>
<dt><code>&#8211;config-prefix</code>=<i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> Search for <i></i><font SIZE="-1"><i>NAME</i></font><i>.cfg</i> and <i></i><font SIZE="-1"><i>NAME</i></font><i>.site.cfg</i> when searching for test suites, instead of <i>lit.cfg</i> and <i>lit.site.cfg</i>.</p>
<dt><code>&#8211;param</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i>, <code>&#8211;param</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i>=<i></i><font SIZE="-1"><i>VALUE</i></font><i></i></p>
<dd> Add a user defined parameter <i></i><font SIZE="-1"><i>NAME</i></font><i></i> with the given <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> (or the empty string if not given). The meaning and use of these parameters is test suite dependent.</dl>
<h2>OUTPUT OPTIONS</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress any output except for test failures.</p>
<dt><code>-s</code>, <code>&#8211;succinct</code></p>
<dd> Show less output, for example don&#8217;t show information on tests that pass.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Show more information on test failures, for example the entire test output instead of just the test result.</p>
<dt><code>&#8211;no-progress-bar</code></p>
<dd> Do not use curses based progress bar.</dl>
<h2>EXECUTION OPTIONS</h2>
<dl>
<dt><code>&#8211;path</code>=<i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> Specify an addition <i></i><font SIZE="-1"><i>PATH</i></font><i></i> to use when searching for executables in tests.</p>
<dt><code>&#8211;vg</code></p>
<dd> Run individual tests under valgrind (using the memcheck tool). The <i>&#8211;error-exitcode</i> argument for valgrind is used so that valgrind failures will cause the program to exit with a non-zero status.</p>
<dt><code>&#8211;vg-arg</code>=<i></i><font SIZE="-1"><i>ARG</i></font><i></i></p>
<dd> When <i>&#8211;vg</i> is used, specify an additional argument to pass to valgrind itself.</p>
<dt><code>&#8211;time-tests</code></p>
<dd> Track the wall time individual tests take to execute and includes the results in the summary output. This is useful for determining which tests in a test suite take the most time to execute. Note that this option is most useful with <i>-j 1</i>.</dl>
<h2>SELECTION OPTIONS</h2>
<dl>
<dt><code>&#8211;max-tests</code>=<i>N</i></p>
<dd> Run at most <i>N</i> tests and then terminate.</p>
<dt><code>&#8211;max-time</code>=<i>N</i></p>
<dd> Spend at most <i>N</i> seconds (approximately) running tests and then terminate.</p>
<dt><code>&#8211;shuffle</code></p>
<dd> Run the tests in a random order.</dl>
<h2>ADDITIONAL OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Run <code>lit</code> in debug mode, for debugging configuration issues and <code>lit</code> itself.</p>
<dt><code>&#8211;show-suites</code></p>
<dd> List the discovered test suites as part of the standard output.</p>
<dt><code>&#8211;no-tcl-as-sh</code></p>
<dd> Run Tcl scripts internally (instead of converting to shell scripts).</p>
<dt><code>&#8211;repeat</code>=<i>N</i></p>
<dd> Run each test <i>N</i> times. Currently this is primarily useful for timing tests, other results are not collated in any reasonable fashion.</dl>
<h2>EXIT STATUS</h2>
<p> <code>lit</code> will exit with an exit code of 1 if there are any <font SIZE="-1">FAIL</font> or <font SIZE="-1">XPASS</font> results. Otherwise, it will exit with the status 0. Other exit codes used for non-test related failures (for example a user error or an internal program error).</p>
<h2>TEST DISCOVERY</h2>
<p> The inputs passed to <code>lit</code> can be either individual tests, or entire directories or hierarchies of tests to run. When <code>lit</code> starts up, the first thing it does is convert the inputs into a complete list of tests to run as part of <i>test discovery</i>. </p>
<p> In the <code>lit</code> model, every test must exist inside some <i>test suite</i>. <code>lit</code> resolves the inputs specified on the command line to test suites by searching upwards from the input path until it finds a <i>lit.cfg</i> or <i>lit.site.cfg</i> file. These files serve as both a marker of test suites and as configuration files which <code>lit</code> loads in order to understand how to find and run the tests inside the test suite. </p>
<p> Once <code>lit</code> has mapped the inputs into test suites it traverses the list of inputs adding tests for individual files and recursively searching for tests in directories. </p>
<p> This behavior makes it easy to specify a subset of tests to run, while still allowing the test suite configuration to control exactly how tests are interpreted. In addition, <code>lit</code> always identifies tests by the test suite they are in, and their relative path inside the test suite. For appropriately configured projects, this allows <code>lit</code> to provide convenient and flexible support for out-of-tree builds.</p>
<h2>TEST STATUS RESULTS</h2>
<p> Each test ultimately produces one of the following six results:</p>
<dl>
<dt><font SIZE="-1"><code>PASS</code></font></p>
<dd> The test succeeded.</p>
<dt><font SIZE="-1"><code>XFAIL</code></font></p>
<dd> The test failed, but that is expected. This is used for test formats which allow specifying that a test does not currently work, but wish to leave it in the test suite.</p>
<dt><font SIZE="-1"><code>XPASS</code></font></p>
<dd> The test succeeded, but it was expected to fail. This is used for tests which were specified as expected to fail, but are now succeeding (generally because the feautre they test was broken and has been fixed).</p>
<dt><font SIZE="-1"><code>FAIL</code></font></p>
<dd> The test failed.</p>
<dt><font SIZE="-1"><code>UNRESOLVED</code></font></p>
<dd> The test result could not be determined. For example, this occurs when the test could not be run, the test itself is invalid, or the test was interrupted.</p>
<dt><font SIZE="-1"><code>UNSUPPORTED</code></font></p>
<dd> The test is not supported in this environment. This is used by test formats which can report unsupported tests.</dl>
<p> Depending on the test format tests may produce additional information about their status (generally only for failures). See the Output section for more information.</p>
<h2>LIT INFRASTRUCTURE</h2>
<p> This section describes the <code>lit</code> testing architecture for users interested in creating a new <code>lit</code> testing implementation, or extending an existing one. </p>
<p> <code>lit</code> proper is primarily an infrastructure for discovering and running arbitrary tests, and to expose a single convenient interface to these tests. <code>lit</code> itself doesn&#8217;t know how to run tests, rather this logic is defined by <i>test suites</i>.</p>
<h2><font SIZE="-1">TEST</font> <font SIZE="-1">SUITES</font></h2>
<p> As described in &#8220;<font SIZE="-1">TEST</font> <font SIZE="-1">DISCOVERY</font>&#8221;, tests are always located inside a <i>test suite</i>. Test suites serve to define the format of the tests they contain, the logic for finding those tests, and any additional information to run the tests. </p>
<p> <code>lit</code> identifies test suites as directories containing <i>lit.cfg</i> or <i>lit.site.cfg</i> files (see also <code>&#8211;config-prefix</code>. Test suites are initially discovered by recursively searching up the directory hierarchy for all the input files passed on the command line. You can use <code>&#8211;show-suites</code> to display the discovered test suites at startup. </p>
<p> Once a test suite is discovered, its config file is loaded. Config files themselves are just Python modules which will be executed. When the config file is executed, two important global variables are predefined:</p>
<dl>
<dt><code>lit</code></p>
<dd> The global <code>lit</code> configuration object (a <i>LitConfig</i> instance), which defines the builtin test formats, global configuration parameters, and other helper routines for implementing test configurations.</p>
<dt><code>config</code></p>
<dd> This is the config object (a <i>TestingConfig</i> instance) for the test suite, which the config file is expected to populate. The following variables are also available on the <i>config</i> object, some of which must be set by the config and others are optional or predefined: </p>
<p> <code>name</code> <i>[required]</i> The name of the test suite, for use in reports and diagnostics. </p>
<p> <code>test_format</code> <i>[required]</i> The test format object which will be used to discover and run tests in the test suite. Generally this will be a builtin test format available from the <i>lit.formats</i> module. </p>
<p> <code>test_src_root</code> The filesystem path to the test suite root. For out-of-dir builds this is the directory that will be scanned for tests. </p>
<p> <code>test_exec_root</code> For out-of-dir builds, the path to the test suite root inside the object directory. This is where tests will be run and temporary output files places. </p>
<p> <code>environment</code> A dictionary representing the environment to use when executing tests in the suite. </p>
<p> <code>suffixes</code> For <code>lit</code> test formats which scan directories for tests, this variable as a list of suffixes to identify test files. Used by: <i>ShTest</i>, <i>TclTest</i>. </p>
<p> <code>substitutions</code> For <code>lit</code> test formats which substitute variables into a test script, the list of substitutions to perform. Used by: <i>ShTest</i>, <i>TclTest</i>. </p>
<p> <code>unsupported</code> Mark an unsupported directory, all tests within it will be reported as unsupported. Used by: <i>ShTest</i>, <i>TclTest</i>. </p>
<p> <code>parent</code> The parent configuration, this is the config object for the directory containing the test suite, or None. </p>
<p> <code>on_clone</code> The config is actually cloned for every subdirectory inside a test suite, to allow local configuration on a per-directory basis. The <i>on_clone</i> variable can be set to a Python function which will be called whenever a configuration is cloned (for a subdirectory). The function should takes three arguments: (1) the parent configuration, (2) the new configuration (which the <i>on_clone</i> function will generally modify), and (3) the test path to the new directory being scanned.</dl>
<h2><font SIZE="-1">TEST</font> <font SIZE="-1">DISCOVERY</font></h2>
<p> Once test suites are located, <code>lit</code> recursively traverses the source directory (following <i>test_src_root</i>) looking for tests. When <code>lit</code> enters a sub-directory, it first checks to see if a nest test suite is defined in that directory. If so, it loads that test suite recursively, otherwise it instantiates a local test config for the directory (see &#8220;<font SIZE="-1">LOCAL</font> <font SIZE="-1">CONFIGURATION</font> <font SIZE="-1">FILES</font>&#8221;). </p>
<p> Tests are identified by the test suite they are contained within, and the relative path inside that suite. Note that the relative path may not refer to an actual file on disk; some test formats (such as <i>GoogleTest</i>) define &#8220;virtual tests&#8221; which have a path that contains both the path to the actual test file and a subpath to identify the virtual test.</p>
<h2><font SIZE="-1">LOCAL</font> <font SIZE="-1">CONFIGURATION</font> <font SIZE="-1">FILES</font></h2>
<p> When <code>lit</code> loads a subdirectory in a test suite, it instantiates a local test configuration by cloning the configuration for the parent direction &#8212; the root of this configuration chain will always be a test suite. Once the test configuration is cloned <code>lit</code> checks for a <i>lit.local.cfg</i> file in the subdirectory. If present, this file will be loaded and can be used to specialize the configuration for each individual directory. This facility can be used to define subdirectories of optional tests, or to change other configuration parameters &#8212; for example, to change the test format, or the suffixes which identify test files.</p>
<h2><font SIZE="-1">LIT</font> <font SIZE="-1">EXAMPLE</font> <font SIZE="-1">TESTS</font></h2>
<p> The <code>lit</code> distribution contains several example implementations of test suites in the <i>ExampleTests</i> directory.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-valgrind/">valgrind</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Daniel Dunbar and maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
