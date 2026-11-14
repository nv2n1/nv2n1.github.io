---
title: "trial3(1)"
name: "trial3"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trial3/"
description: "trial – run unit tests"
---

<h2 class="name">NAME</h2>
<p> trial &#8211; run unit tests </p>
<h2>SYNOPSIS</h2>
<p> <code>trial</code> [ <i>options</i> ] [ <i>file</i> | <i>package</i> | <i>module</i> | <i>TestCase</i> | <i>testmethod</i> ] &#8230; </p>
<p> <code>trial &#8211;help</code> | <code>-h</code></p>
<h2>DESCRIPTION</h2>
<p> trial loads and executes a suite of unit tests, obtained from modules, packages and files listed on the command line. </p>
<p> trial will take either filenames or fully qualified Python names as arguments. Thus `trial myproject/foo.py&#8217;, `trial myproject.foo&#8217; and `trial myproject.foo.SomeTestCase.test_method&#8217; are all valid ways to invoke trial. Multiple such arguments are also accepted, and their order will determine the order in which the corresponding tests are run. </p>
<p> After running the given test suite, the default test reporter prints a summary of the test run. This consists of the word &quot;PASSED&quot; (if all tests ran as expected) or &quot;FAILED&quot; (if any test behaved unexpectedly) followed by a count of the different kinds of test results encountered. The possible kinds of test results includes:</p>
<dl>
<dt>successes</p>
<dd> Tests that passed all their assertions and completed without error. These are marked &quot;PASSED&quot; in the normal test output.</p>
<dt>failures</p>
<dd> Tests that failed an assertion, called self.fail() or explicitly raised self.failureException for some reason. These are marked &quot;FAILED&quot; in the normal test output.</p>
<dt>errors</p>
<dd> Tests that raised an unexpected exception (including AssertionError), tests that caused the tearDown() method to raise an exception, tests that run for longer than the timeout interval, tests that caused something to call twisted.python.log.err() without subsequently calling self.flushLoggedErrors(), tests that leave the reactor in an unclean state, etc. These are marked &quot;ERROR&quot; in the normal test output.</p>
<dt>
<dd> Note that because errors can be caused after the actual test method returns, it is possible for a single test to be reported as both an error and a failure, and hence the total number of test results can be greater than the total number of tests executed.</p>
<dt>skips</p>
<dd> Tests that were skipped, usually because of missing dependencies. These are marked &quot;SKIPPED&quot; in the normal test output.</p>
<dt>expectedFailures</p>
<dd> Tests that failed, but were expected to fail, usually because the test is for a feature that hasn&#8217;t been implemented yet. These are marked &quot;TODO&quot; in the normal test output.</p>
<dt>unexpectedSuccesses</p>
<dd> Tests that should have been listed under expectedFailures, except that for some reason the test succeeded. These are marked &quot;SUCCESS!?!&quot; in the normal test output.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-j</code>, <code>&#8211;jobs</code> <i>number</i></p>
<dd> Set the number of process workers to run. It conflicts with the debug, exitfirst and profile options.</p>
<dt><code>-b</code>, <code>&#8211;debug</code></p>
<dd> Run the tests in a debugger. If that debugger is &#8216;pdb&#8217; (which is the default if unspecified), a `.pdbrc&#8217; will be loaded from the current directory if it exists. Also does post-mortem debugging on exceptions.</p>
<dt><code>-B</code>, <code>&#8211;debug-stacktraces</code></p>
<dd> Report Deferred creation and callback stack traces.</p>
<dt><code>&#8211;coverage</code></p>
<dd> Generate coverage information in the `coverage&#8217; subdirectory of the trial temp directory (`_trial_temp&#8217; by default). For each Python module touched by the execution of the given tests, a file will be created in the coverage directory named for the module&#8217;s fully-qualified name with the suffix `.cover&#8217;. For example, because the trial test runner is written in Python, the coverage directory will almost always contain a file named `twisted.trial.runner.cover&#8217;. </p>
<p> Each `.cover&#8217; file contains a copy of the Python source of the module in question, with a prefix at the beginning of each line containing coverage information. For lines that are not executable (blank lines, comments, etc.) the prefix is blank. For executable lines that were run in the course of the test suite, the prefix is a number indicating the number of times that line was executed. The string `&gt;&gt;&gt;&gt;&gt;&gt;&#8217; prefixes executable lines that were not executed in the course of the test suite. </p>
<p> Note that this functionality uses Python&#8217;s sys.settrace() function, so tests that call sys.settrace() themselves are likely to break trial&#8217;s coverage functionality.</p>
<dt><code>&#8211;debugger</code></p>
<dd> Specifies the debugger to use when the &#8211;debug option is passed. The argument should be the fully qualified name of an object that implements the same interface as the standard library&#8217;s `pdb&#8217;.</p>
<dt><code>&#8211;disablegc</code></p>
<dd> Disable the garbage collector for the duration of the test run. As each test is run, trial saves the TestResult objects, which means that Python&#8217;s garbage collector has more non-garbage objects to wade through, making each garbage-collection run slightly slower. Disabling garbage collection entirely will make some test suites complete faster (contrast &#8211;force-gc, below), at the cost of increasing (possibly greatly) memory consumption. This option also makes tests slightly more deterministic, which might help debugging in extreme circumstances.</p>
<dt><code>-e</code>, <code>&#8211;rterrors</code></p>
<dd> Print tracebacks to standard output as soon as they occur.</p>
<dt><code>&#8211;force-gc</code></p>
<dd> Run gc.collect() before and after each test case. This can be used to isolate errors that occur when objects get collected. This option would be the default, except it makes tests run about ten times slower.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a usage message to standard output, then exit.</p>
<dt><code>&#8211;help-order</code></p>
<dd> Print a list of possible orders that TestCase test methods can be run in, then exit. The orders can be used with the &#8211;order option described below.</p>
<dt><code>&#8211;help-reporters</code></p>
<dd> Print a list of valid reporters to standard output, then exit. Reporters can be selected with the &#8211;reporter option described below.</p>
<dt><code>&#8211;help-reactors</code></p>
<dd> Print a list of possible reactors to standard output, then exit. Not all listed reactors are available on every platform. Reactors can be selected with the &#8211;reactor option described below.</p>
<dt><code>-l</code>, <code>&#8211;logfile</code> <i>logfile</i></p>
<dd> Direct the log to a different file. The default file is `test.log&#8217;. <i>logfile</i> is relative to _trial_temp.</p>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd> Go through all the tests and make them pass without running.</p>
<dt><code>-N</code>, <code>&#8211;no-recurse</code></p>
<dd> By default, trial recurses through packages to find every module inside every subpackage. Unless, that is, you specify this option.</p>
<dt><code>&#8211;nopm</code></p>
<dd> Don&#8217;t automatically jump into debugger for post-mortem analysis of exceptions. Only usable in conjunction with &#8211;debug.</p>
<dt><code>&#8211;order</code> <i>order</i></p>
<dd> Specify what order to run the individual test methods within the given TestCases. By default, they are run alphabetically. See &#8211;help-order for a list of other valid values.</p>
<dt><code>&#8211;profile</code></p>
<dd> Run tests under the Python profiler.</p>
<dt><code>-r</code>, <code>&#8211;reactor</code> <i>reactor</i></p>
<dd> Choose which reactor to use. See &#8211;help-reactors for a list.</p>
<dt><code>&#8211;recursionlimit</code> <i>limit</i></p>
<dd> Set Python&#8217;s recursion limit. See sys.setrecursionlimit().</p>
<dt><code>&#8211;reporter</code> <i>reporter</i></p>
<dd> Select the reporter to use for trial&#8217;s output. Use the &#8211;help-reporters option to see a list of valid reporters.</p>
<dt><code>-x</code>, <code>&#8211;exitfirst</code></p>
<dd> Stop the test run after the first test which does not succeed. This includes failures, errors, or unexpected successes. Won&#8217;t work with the &#8211;jobs option currently.</p>
<dt><code>&#8211;spew</code></p>
<dd> Print an insanely verbose log of everything that happens. Useful when debugging freezes or locks in complex code.</p>
<dt><code>&#8211;tbformat</code> <i>format</i></p>
<dd> Format to display tracebacks with. Acceptable values are `default&#8217;, `brief&#8217; and `verbose&#8217;. `brief&#8217; produces tracebacks that play nicely with Emacs&#8217; GUD.</p>
<dt><code>&#8211;temp-directory</code> <i>directory</i></p>
<dd> WARNING: Do not use this option unless you know what you are doing. By default, trial creates a directory called _trial_temp under the current working directory. When trial runs, it first <i>deletes</i> this directory, then creates it, then changes into the directory to run the tests. The log file and any coverage files are stored here. Use this option if you wish to have trial run in a directory other than _trial_temp. Be warned, trial will <i>delete</i> the directory before re-creating it.</p>
<dt><code>&#8211;testmodule</code> <i>filename</i></p>
<dd> Ask trial to look into <i>filename</i> and run any tests specified using the Emacs-style buffer variable `test-case-name&#8217;.</p>
<dt><code>&#8211;unclean-warnings</code></p>
<dd> As of Twisted 8.0, trial will report an error if the reactor is left unclean at the end of the test. This option is provided to assist in migrating from Twisted 2.5 to Twisted 8.0 and later. Enabling this option will turn the errors into warnings.</p>
<dt><code>-u</code>, <code>&#8211;until-failure</code></p>
<dd> Keep looping the tests until one of them raises an error or a failure. This is particularly useful for reproducing intermittent failures.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the Twisted version number and exit.</p>
<dt><code>&#8211;without-module</code> <i>modulenames</i></p>
<dd> Simulate the lack of the specified comma-separated list of modules. This makes it look like the modules are not present in the system, causing tests to check the behavior for that configuration.</p>
<dt><code>-z</code>, <code>&#8211;random</code> <i>seed</i></p>
<dd> Run the tests in random order using the specified seed. Don&#8217;t pass this option if you also are passing &#8211;order.</dl>
<h2>SEE ALSO</h2>
<p> The latest version of the trial documentation can be found at <a rel="nofollow" href="http://twistedmatrix.com/documents/current/core/howto/testing.html">http://twistedmatrix.com/documents/current/core/howto/testing.html</a></p>
<h2>AUTHOR</h2>
<p> Written by Jonathan M. Lange</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <a rel="nofollow" href="http://twistedmatrix.com/trac/newticket">http://twistedmatrix.com/trac/newticket</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2013 Twisted Matrix Laboratories<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
