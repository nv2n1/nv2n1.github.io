---
title: "nosetests(1)"
name: "nosetests"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nosetests/"
description: "nosetests – Nicer testing for Python"
---

<h2>NAME</h2>
<p> nosetests &#8211; Nicer testing for Python</p>
<h2>NICER TESTING FOR PYTHON</h2>
<h3>SYNOPSIS</h3>
<p> nosetests [options] [names]</p>
<h3>DESCRIPTION</h3>
<p> nose collects tests automatically from python source files, directories and packages found in its working directory (which defaults to the current working directory). Any python source file, directory or package that matches the testMatch regular expression (by default: <i>(?:^|[b_.-])[Tt]est)</i> will be collected as a test (or source for collection of tests). In addition, all other packages found in the working directory will be examined for python source files or directories that match testMatch. Package discovery descends all the way down the tree, so package.tests and package.sub.tests and package.sub.sub2.tests will all be collected. </p>
<p> Within a test directory or package, any python source file matching testMatch will be examined for test cases. Within a test module, functions and classes whose names match testMatch and TestCase subclasses with any name will be loaded and executed as tests. Tests may use the assert keyword or raise AssertionErrors to indicate test failure. TestCase subclasses may do the same or use the various TestCase methods available. </p>
<p> <code>It is important to note that the default behavior of nose is to not include tests from files which are executable.</code> To include tests from such files, remove their executable bit or use the &#8211;exe flag (see &#8216;Options&#8217; section below).</p>
<h3>Selecting Tests</h3>
<p> To specify which tests to run, pass test names on the command line: </p>
<pre>
nosetests only_test_this.py
</pre>
<p> Test names specified may be file or module names, and may optionally indicate the test case to run by separating the module or file name from the test case name with a colon. Filenames may be relative or absolute. Examples: </p>
<pre>
nosetests test.module
nosetests another.test:TestCase.test_method
nosetests a.test:TestCase
nosetests /path/to/test/file.py:test_function
</pre>
<p> You may also change the working directory where nose looks for tests by using the -w switch: </p>
<pre>
nosetests -w /path/to/tests
</pre>
<p> Note, however, that support for multiple -w arguments is now deprecated and will be removed in a future release. As of nose 0.10, you can get the same behavior by specifying the target directories <i>without</i> the -w switch: </p>
<pre>
nosetests /path/to/tests /another/path/to/tests
</pre>
<p> Further customization of test selection and loading is possible through the use of plugins. </p>
<p> Test result output is identical to that of unittest, except for the additional features (error classes, and plugin-supplied features such as output capture and assert introspection) detailed in the options below.</p>
<h3>Configuration</h3>
<p> In addition to passing command-line options, you may also put configuration options in your project&#8217;s <i>setup.cfg</i> file, or a .noserc or nose.cfg file in your home directory. In any of these standard ini-style config files, you put your nosetests configuration in a <code>[nosetests]</code> section. Options are the same as on the command line, with the &#8212; prefix removed. For options that are simple switches, you must supply a value: </p>
<pre>
[nosetests]
verbosity=3
with-doctest=1
</pre>
<p> All configuration files that are found will be loaded and their options combined. You can override the standard config file loading with the <code>-c</code> option.</p>
<h3>Using Plugins</h3>
<p> There are numerous nose plugins available via easy_install and elsewhere. To use a plugin, just install it. The plugin will add command line options to nosetests. To verify that the plugin is installed, run: </p>
<pre>
nosetests --plugins
</pre>
<p> You can add -v or -vv to that command to show more information about each plugin. </p>
<p> If you are running nose.main() or nose.run() from a script, you can specify a list of plugins to use by passing a list of plugins with the plugins keyword argument.</p>
<h3>0.9 plugins</h3>
<p> nose 1.0 can use SOME plugins that were written for nose 0.9. The default plugin manager inserts a compatibility wrapper around 0.9 plugins that adapts the changed plugin api calls. However, plugins that access nose internals are likely to fail, especially if they attempt to access test case or test suite classes. For example, plugins that try to determine if a test passed to startTest is an individual test or a suite will fail, partly because suites are no longer passed to startTest and partly because it&#8217;s likely that the plugin is trying to find out if the test is an instance of a class that no longer exists.</p>
<h3>0.10 and 0.11 plugins</h3>
<p> All plugins written for nose 0.10 and 0.11 should work with nose 1.0.</p>
<h3>Options</h3>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Output nose version and exit</p>
<dt><code>-p, &#8211;plugins</code></p>
<dd> Output list of available plugins and exit. Combine with higher verbosity for greater detail</p>
<dt><code>-v=DEFAULT, &#8211;verbose=DEFAULT</code></p>
<dd> Be more verbose. [NOSE_VERBOSE]</p>
<dt><code>&#8211;verbosity=VERBOSITY</code></p>
<dd> Set verbosity; &#8211;verbosity=2 is the same as -v</p>
<dt><code>-q=DEFAULT, &#8211;quiet=DEFAULT</code></p>
<dd> Be less verbose</p>
<dt><code>-c=FILES, &#8211;config=FILES</code></p>
<dd> Load configuration from config file(s). May be specified multiple times; in that case, all config files will be loaded and combined</p>
<dt><code>-w=WHERE, &#8211;where=WHERE</code></p>
<dd> Look for tests in this directory. May be specified multiple times. The first directory passed will be used as the working directory, in place of the current working directory, which is the default. Others will be added to the list of tests to execute. [NOSE_WHERE]</p>
<dt><code>&#8211;py3where=PY3WHERE</code></p>
<dd> Look for tests in this directory under Python 3.x. Functions the same as &#8216;where&#8217;, but only applies if running under Python 3.x or above. Note that, if present under 3.x, this option completely replaces any directories specified with &#8216;where&#8217;, so the &#8216;where&#8217; option becomes ineffective. [NOSE_PY3WHERE]</p>
<dt><code>-m=REGEX, &#8211;match=REGEX, &#8211;testmatch=REGEX</code></p>
<dd> Files, directories, function names, and class names that match this regular expression are considered tests. Default: (?:^|[b_./-])[Tt]est [NOSE_TESTMATCH]</p>
<dt><code>&#8211;tests=NAMES</code></p>
<dd> Run these tests (comma-separated list). This argument is useful mainly from configuration files; on the command line, just pass the tests to run as additional arguments with no switch.</p>
<dt><code>-l=DEFAULT, &#8211;debug=DEFAULT</code></p>
<dd> Activate debug logging for one or more systems. Available debug loggers: nose, nose.importer, nose.inspector, nose.plugins, nose.result and nose.selector. Separate multiple names with a comma.</p>
<dt><code>&#8211;debug-log=FILE</code></p>
<dd> Log debug messages to this file (default: sys.stderr)</p>
<dt><code>&#8211;logging-config=FILE, &#8211;log-config=FILE</code></p>
<dd> Load logging config from this file &#8212; bypasses all other logging config settings.</p>
<dt><code>-I=REGEX, &#8211;ignore-files=REGEX</code></p>
<dd> Completely ignore any file that matches this regular expression. Takes precedence over any other settings or plugins. Specifying this option will replace the default setting. Specify this option multiple times to add more regular expressions [NOSE_IGNORE_FILES]</p>
<dt><code>-e=REGEX, &#8211;exclude=REGEX</code></p>
<dd> Don&#8217;t run tests that match regular expression [NOSE_EXCLUDE]</p>
<dt><code>-i=REGEX, &#8211;include=REGEX</code></p>
<dd> This regular expression will be applied to files, directories, function names, and class names for a chance to include additional tests that do not match TESTMATCH. Specify this option multiple times to add more regular expressions [NOSE_INCLUDE]</p>
<dt><code>-x, &#8211;stop</code></p>
<dd> Stop running tests after the first error or failure</p>
<dt><code>-P, &#8211;no-path-adjustment</code></p>
<dd> Don&#8217;t make any changes to sys.path when loading tests [NOSE_NOPATH]</p>
<dt><code>&#8211;exe</code></p>
<dd> Look for tests in python modules that are executable. Normal behavior is to exclude executable modules, since they may not be import-safe [NOSE_INCLUDE_EXE]</p>
<dt><code>&#8211;noexe</code></p>
<dd> DO NOT look for tests in python modules that are executable. (The default on the windows platform is to do so.)</p>
<dt><code>&#8211;traverse-namespace</code></p>
<dd> Traverse through all path entries of a namespace package</p>
<dt><code>&#8211;first-package-wins, &#8211;first-pkg-wins, &#8211;1st-pkg-wins</code></p>
<dd> nose&#8217;s importer will normally evict a package from sys.modules if it sees a package with the same name in a different location. Set this option to disable that behavior.</p>
<dt><code>&#8211;no-byte-compile</code></p>
<dd> Prevent nose from byte-compiling the source into .pyc files while nose is scanning for and running tests.</p>
<dt><code>-a=ATTR, &#8211;attr=ATTR</code></p>
<dd> Run only tests that have attributes specified by ATTR [NOSE_ATTR]</p>
<dt><code>-A=EXPR, &#8211;eval-attr=EXPR</code></p>
<dd> Run only tests for whose attributes the Python expression EXPR evaluates to True [NOSE_EVAL_ATTR]</p>
<dt><code>-s, &#8211;nocapture</code></p>
<dd> Don&#8217;t capture stdout (any stdout output will be printed immediately) [NOSE_NOCAPTURE]</p>
<dt><code>&#8211;nologcapture</code></p>
<dd> Disable logging capture plugin. Logging configuration will be left intact. [NOSE_NOLOGCAPTURE]</p>
<dt><code>&#8211;logging-format=FORMAT</code></p>
<dd> Specify custom format to print statements. Uses the same format as used by standard logging handlers. [NOSE_LOGFORMAT]</p>
<dt><code>&#8211;logging-datefmt=FORMAT</code></p>
<dd> Specify custom date/time format to print statements. Uses the same format as used by standard logging handlers. [NOSE_LOGDATEFMT]</p>
<dt><code>&#8211;logging-filter=FILTER</code></p>
<dd> Specify which statements to filter in/out. By default, everything is captured. If the output is too verbose, use this option to filter out needless output. Example: filter=foo will capture statements issued ONLY to<br />
&nbsp;<wbr>foo or foo.what.ever.sub but not foobar or other logger. Specify multiple loggers with comma: filter=foo,bar,baz. If any logger name is prefixed with a minus, eg filter=-foo, it will be excluded rather than included. Default: exclude logging messages from nose itself (-nose). [NOSE_LOGFILTER]</p>
<dt><code>&#8211;logging-clear-handlers</code></p>
<dd> Clear all other logging handlers</p>
<dt><code>&#8211;logging-level=DEFAULT</code></p>
<dd> Set the log level to capture</p>
<dt><code>&#8211;with-coverage</code></p>
<dd> Enable plugin Coverage: Activate a coverage report using Ned Batchelder&#8217;s coverage module.<br />
&nbsp;<wbr>[NOSE_WITH_COVERAGE]</p>
<dt><code>&#8211;cover-package=PACKAGE</code></p>
<dd> Restrict coverage output to selected packages [NOSE_COVER_PACKAGE]</p>
<dt><code>&#8211;cover-erase</code></p>
<dd> Erase previously collected coverage statistics before run</p>
<dt><code>&#8211;cover-tests</code></p>
<dd> Include test modules in coverage report [NOSE_COVER_TESTS]</p>
<dt><code>&#8211;cover-min-percentage=DEFAULT</code></p>
<dd> Minimum percentage of coverage for tests to pass [NOSE_COVER_MIN_PERCENTAGE]</p>
<dt><code>&#8211;cover-inclusive</code></p>
<dd> Include all python files under working directory in coverage report. Useful for discovering holes in test coverage if not all files are imported by the test suite. [NOSE_COVER_INCLUSIVE]</p>
<dt><code>&#8211;cover-html</code></p>
<dd> Produce HTML coverage information</p>
<dt><code>&#8211;cover-html-dir=DIR</code></p>
<dd> Produce HTML coverage information in dir</p>
<dt><code>&#8211;cover-branches</code></p>
<dd> Include branch coverage in coverage report [NOSE_COVER_BRANCHES]</p>
<dt><code>&#8211;cover-xml</code></p>
<dd> Produce XML coverage information</p>
<dt><code>&#8211;cover-xml-file=FILE</code></p>
<dd> Produce XML coverage information in file</p>
<dt><code>&#8211;pdb</code></p>
<dd> Drop into debugger on failures or errors</p>
<dt><code>&#8211;pdb-failures</code></p>
<dd> Drop into debugger on failures</p>
<dt><code>&#8211;pdb-errors</code></p>
<dd> Drop into debugger on errors</p>
<dt><code>&#8211;no-deprecated</code></p>
<dd> Disable special handling of DeprecatedTest exceptions.</p>
<dt><code>&#8211;with-doctest</code></p>
<dd> Enable plugin Doctest: Activate doctest plugin to find and run doctests in non-test modules.<br />
&nbsp;<wbr>[NOSE_WITH_DOCTEST]</p>
<dt><code>&#8211;doctest-tests</code></p>
<dd> Also look for doctests in test modules. Note that classes, methods and functions should have either doctests or non-doctest tests, not both. [NOSE_DOCTEST_TESTS]</p>
<dt><code>&#8211;doctest-extension=EXT</code></p>
<dd> Also look for doctests in files with this extension [NOSE_DOCTEST_EXTENSION]</p>
<dt><code>&#8211;doctest-result-variable=VAR</code></p>
<dd> Change the variable name set to the result of the last interpreter command from the default &#8216;_&#8217;. Can be used to avoid conflicts with the _() function used for text translation. [NOSE_DOCTEST_RESULT_VAR]</p>
<dt><code>&#8211;doctest-fixtures=SUFFIX</code></p>
<dd> Find fixtures for a doctest file in module with this name appended to the base name of the doctest file</p>
<dt><code>&#8211;doctest-options=OPTIONS</code></p>
<dd> Specify options to pass to doctest. Eg. &#8216;+ELLIPSIS,+NORMALIZE_WHITESPACE&#8217;</p>
<dt><code>&#8211;with-isolation</code></p>
<dd> Enable plugin IsolationPlugin: Activate the isolation plugin to isolate changes to external modules to a single test module or package. The isolation plugin resets the contents of sys.modules after each test module or package runs to its state before the test. PLEASE NOTE that this plugin should not be used with the coverage plugin, or in any other case where module reloading may produce undesirable side-effects.<br />
&nbsp;<wbr>[NOSE_WITH_ISOLATION]</p>
<dt><code>-d, &#8211;detailed-errors, &#8211;failure-detail</code></p>
<dd> Add detail to error output by attempting to evaluate failed asserts [NOSE_DETAILED_ERRORS]</p>
<dt><code>&#8211;with-profile</code></p>
<dd> Enable plugin Profile: Use this plugin to run tests using the hotshot profiler.<br />
&nbsp;<wbr>[NOSE_WITH_PROFILE]</p>
<dt><code>&#8211;profile-sort=SORT</code></p>
<dd> Set sort order for profiler output</p>
<dt><code>&#8211;profile-stats-file=FILE</code></p>
<dd> Profiler stats file; default is a new temp file on each run</p>
<dt><code>&#8211;profile-restrict=RESTRICT</code></p>
<dd> Restrict profiler output. See help for pstats.Stats for details</p>
<dt><code>&#8211;no-skip</code></p>
<dd> Disable special handling of SkipTest exceptions.</p>
<dt><code>&#8211;with-id</code></p>
<dd> Enable plugin TestId: Activate to add a test id (like #1) to each test name output. Activate with &#8211;failed to rerun failing tests only.<br />
&nbsp;<wbr>[NOSE_WITH_ID]</p>
<dt><code>&#8211;id-file=FILE</code></p>
<dd> Store test ids found in test runs in this file. Default is the file .noseids in the working directory.</p>
<dt><code>&#8211;failed</code></p>
<dd> Run the tests that failed in the last test run.</p>
<dt><code>&#8211;processes=NUM</code></p>
<dd> Spread test run among this many processes. Set a number equal to the number of processors or cores in your machine for best results. Pass a negative number to have the number of processes automatically set to the number of cores. Passing 0 means to disable parallel testing. Default is 0 unless NOSE_PROCESSES is set. [NOSE_PROCESSES]</p>
<dt><code>&#8211;process-timeout=SECONDS</code></p>
<dd> Set timeout for return of results from each test runner process. Default is 10. [NOSE_PROCESS_TIMEOUT]</p>
<dt><code>&#8211;process-restartworker</code></p>
<dd> If set, will restart each worker process once their tests are done, this helps control memory leaks from killing the system. [NOSE_PROCESS_RESTARTWORKER]</p>
<dt><code>&#8211;with-xunit</code></p>
<dd> Enable plugin Xunit: This plugin provides test results in the standard XUnit XML format. [NOSE_WITH_XUNIT]</p>
<dt><code>&#8211;xunit-file=FILE</code></p>
<dd> Path to xml file to store the xunit report in. Default is nosetests.xml in the working directory [NOSE_XUNIT_FILE]</p>
<dt><code>&#8211;xunit-testsuite-name=PACKAGE</code></p>
<dd> Name of the testsuite in the xunit xml, generated by plugin. Default test suite name is nosetests.</p>
<dt><code>&#8211;all-modules</code></p>
<dd> Enable plugin AllModules: Collect tests from all python modules.<br />
&nbsp;<wbr>[NOSE_ALL_MODULES]</p>
<dt><code>&#8211;collect-only</code></p>
<dd> Enable collect-only: Collect and output test names only, don&#8217;t run any tests.<br />
&nbsp;<wbr>[COLLECT_ONLY]</dl>
<h2>AUTHOR</h2>
<p> Nose developers</p>
<h2>COPYRIGHT</h2>
<p> 2009, Jason Pellerin </p>
<h2>Index</h2>
