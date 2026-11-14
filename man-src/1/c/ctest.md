---
title: "ctest(1)"
name: "ctest"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctest/"
description: "ctest – CTest Command-Line Reference"
---

<h2 class="name">NAME</h2>
<p> ctest &#8211; CTest Command-Line Reference </p>
<h3>Contents</h3>
<dl>
<dt>&bull;</p>
<dd> <i><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</i></p>
<dt>&bull;</p>
<dd> <i>Synopsis</i></p>
<dt>&bull;</p>
<dd> <i>Description</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></p>
<dt>&bull;</p>
<dd> <i>Label Matching</i></p>
<dt>&bull;</p>
<dd> <i>Label and Subproject Summary</i></p>
<dt>&bull;</p>
<dd> <i>Build and Test Mode</i></p>
<dt>&bull;</p>
<dd> <i>Dashboard Client</i></p>
<dt>&bull;</p>
<dd> <i>Dashboard Client Steps</i></p>
<dt>&bull;</p>
<dd> <i>Dashboard Client Modes</i></p>
<dt>&bull;</p>
<dd> <i>Dashboard Client via CTest Command-Line</i></p>
<dt>&bull;</p>
<dd> <i>Dashboard Client via CTest Script</i></p>
<dt>&bull;</p>
<dd> <i>Dashboard Client Configuration</i></p>
<dt>&bull;</p>
<dd> <i>CTest Start Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest Update Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest Configure Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest Build Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest Test Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest Coverage Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest MemCheck Step</i></p>
<dt>&bull;</p>
<dd> <i>CTest Submit Step</i></p>
<dt>&bull;</p>
<dd> <i>Show as JSON Object Model</i></p>
<dt>&bull;</p>
<dd> <i>Resource Allocation</i></p>
<dt>&bull;</p>
<dd> <i>Resource Specification File</i></p>
<dt>&bull;</p>
<dd> <i>RESOURCE_GROUPS Property</i></p>
<dt>&bull;</p>
<dd> <i>Environment Variables</i></p>
<dt>&bull;</p>
<dd> <i>See Also</i></dl>
<h2>SYNOPSIS</h2>
<pre><code>
ctest[&lt;options&gt;] ctest-- build - and-test&lt;path - to - source&gt;&lt;path - to - build&gt; --build - generator&lt;generator&gt;[&lt;options&gt;...][--build - options&lt;opts&gt;...][--test - command&lt;command&gt;[&lt;args&gt;...]] ctest { -D&lt;dashboard&gt; | -M&lt;model&gt; - T&lt;action&gt; | -S&lt;script&gt; | -SP&lt;script&gt; }[--&lt;dashboard - options&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ctest</code> executable is the CMake test driver program. CMake-generated build trees created for projects that use the <code>enable_testing()</code> and <code>add_test()</code> commands have testing support. This program will run the tests and report results.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;preset &lt;preset&gt;</code>, <code>&#8211;preset=&lt;preset&gt;</code></p>
<dd> Use a test preset to specify test options. The project binary directory is inferred from the <code>configurePreset</code> key. The current working directory must contain CMake preset files. See <code>preset</code> for more details.</p>
<dt><code>&#8211;list-presets</code></p>
<dd> Lists the available test presets. The current working directory must contain CMake preset files.</p>
<dt><code>-C &lt;cfg&gt;, &#8211;build-config &lt;cfg&gt;</code></p>
<dd> Choose configuration to test. </p>
<p> Some CMake-generated build trees can have multiple build configurations in the same tree. This option can be used to specify which one should be tested. Example configurations are <code>Debug</code> and <code>Release</code>.</p>
<dt><code>&#8211;progress</code></p>
<dd> Enable short progress output from tests. </p>
<p> When the output of <code>ctest</code> is being sent directly to a terminal, the progress through the set of tests is reported by updating the same line rather than printing start and end messages for each test on new lines. This can significantly reduce the verbosity of the test output. Test completion messages are still output on their own line for failed tests and the final test summary will also still be logged. </p>
<p> This option can also be enabled by setting the environment variable <code>CTEST_PROGRESS_OUTPUT</code>.</p>
<dt><code>-V,&#8211;verbose</code></p>
<dd> Enable verbose output from tests. </p>
<p> Test output is normally suppressed and only summary information is displayed. This option will show all test output.</p>
<dt><code>-VV,&#8211;extra-verbose</code></p>
<dd> Enable more verbose output from tests. </p>
<p> Test output is normally suppressed and only summary information is displayed. This option will show even more test output.</p>
<dt><code>&#8211;debug</code></p>
<dd> Displaying more verbose internals of CTest. </p>
<p> This feature will result in a large number of output that is mostly useful for debugging dashboard problems.</p>
<dt><code>&#8211;output-on-failure</code></p>
<dd> Output anything outputted by the test program if the test should fail. This option can also be enabled by setting the <code>CTEST_OUTPUT_ON_FAILURE</code> environment variable</p>
<dt><code>&#8211;stop-on-failure</code></p>
<dd> Stop running the tests when the first failure happens.</p>
<dt><code>-F</code></p>
<dd> Enable failover. </p>
<p> This option allows CTest to resume a test set execution that was previously interrupted. If no interruption occurred, the <code>-F</code> option will have no effect.</p>
<dt><code>-j &lt;jobs&gt;, &#8211;parallel &lt;jobs&gt;</code></p>
<dd> Run the tests in parallel using the given number of jobs. </p>
<p> This option tells CTest to run the tests in parallel using given number of jobs. This option can also be set by setting the <code>CTEST_PARALLEL_LEVEL</code> environment variable. </p>
<p> This option can be used with the <code>PROCESSORS</code> test property. </p>
<p> See <i>Label and Subproject Summary</i>.</p>
<dt><code>&#8211;resource-spec-file &lt;file&gt;</code></p>
<dd> Run CTest with <i>resource allocation</i> enabled, using the <i>resource specification file</i> specified in <code>&lt;file&gt;</code>. </p>
<p> When <code>ctest</code> is run as a <i>Dashboard Client</i> this sets the <code>ResourceSpecFile</code> option of the <i>CTest Test Step</i>.</p>
<dt><code>&#8211;test-load &lt;level&gt;</code></p>
<dd> While running tests in parallel (e.g. with <code>-j</code>), try not to start tests when they may cause the CPU load to pass above a given threshold. </p>
<p> When <code>ctest</code> is run as a <i>Dashboard Client</i> this sets the <code>TestLoad</code> option of the <i>CTest Test Step</i>.</p>
<dt><code>-Q,&#8211;quiet</code></p>
<dd> Make CTest quiet. </p>
<p> This option will suppress all the output. The output log file will still be generated if the <code>&#8211;output-log</code> is specified. Options such as <code>&#8211;verbose</code>, <code>&#8211;extra-verbose</code>, and <code>&#8211;debug</code> are ignored if <code>&#8211;quiet</code> is specified.</p>
<dt><code>-O &lt;file&gt;, &#8211;output-log &lt;file&gt;</code></p>
<dd> Output to log file. </p>
<p> This option tells CTest to write all its output to a <code>&lt;file&gt;</code> log file.</p>
<dt><code>&#8211;output-junit &lt;file&gt;</code></p>
<dd> Write test results in JUnit format. </p>
<p> This option tells CTest to write test results to <code>&lt;file&gt;</code> in JUnit XML format. If <code>&lt;file&gt;</code> already exists, it will be overwritten. If using the <code>-S</code> option to run a dashboard script, use the <code>OUTPUT_JUNIT</code> keyword with the <code>ctest_test()</code> command instead.</p>
<dt><code>-N,&#8211;show-only[=&lt;format&gt;]</code></p>
<dd> Disable actual execution of tests. </p>
<p> This option tells CTest to list the tests that would be run but not actually run them. Useful in conjunction with the <code>-R</code> and <code>-E</code> options. </p>
<p> <code>&lt;format&gt;</code> can be one of the following values.</p>
<dt><code>human</code></p>
<dd> Human-friendly output. This is not guaranteed to be stable. This is the default.</p>
<dt><code>json-v1</code></p>
<dd> Dump the test information in JSON format. See <i>Show as JSON Object Model</i>.</p>
<dt><code>-L &lt;regex&gt;, &#8211;label-regex &lt;regex&gt;</code></p>
<dd> Run tests with labels matching regular expression as described under string(REGEX). </p>
<p> This option tells CTest to run only the tests whose labels match the given regular expression. When more than one <code>-L</code> option is given, a test will only be run if each regular expression matches at least one of the test&#8217;s labels (i.e. the multiple <code>-L</code> labels form an <code>AND</code> relationship). See <i>Label Matching</i>.</p>
<dt><code>-R &lt;regex&gt;, &#8211;tests-regex &lt;regex&gt;</code></p>
<dd> Run tests matching regular expression. </p>
<p> This option tells CTest to run only the tests whose names match the given regular expression.</p>
<dt><code>-E &lt;regex&gt;, &#8211;exclude-regex &lt;regex&gt;</code></p>
<dd> Exclude tests matching regular expression. </p>
<p> This option tells CTest to NOT run the tests whose names match the given regular expression.</p>
<dt><code>-LE &lt;regex&gt;, &#8211;label-exclude &lt;regex&gt;</code></p>
<dd> Exclude tests with labels matching regular expression. </p>
<p> This option tells CTest to NOT run the tests whose labels match the given regular expression. When more than one <code>-LE</code> option is given, a test will only be excluded if each regular expression matches at least one of the test&#8217;s labels (i.e. the multiple <code>-LE</code> labels form an <code>AND</code> relationship). See <i>Label Matching</i>.</p>
<dt><code>-FA &lt;regex&gt;, &#8211;fixture-exclude-any &lt;regex&gt;</code></p>
<dd> Exclude fixtures matching <code>&lt;regex&gt;</code> from automatically adding any tests to the test set. </p>
<p> If a test in the set of tests to be executed requires a particular fixture, that fixture&#8217;s setup and cleanup tests would normally be added to the test set automatically. This option prevents adding setup or cleanup tests for fixtures matching the <code>&lt;regex&gt;</code>. Note that all other fixture behavior is retained, including test dependencies and skipping tests that have fixture setup tests that fail.</p>
<dt><code>-FS &lt;regex&gt;, &#8211;fixture-exclude-setup &lt;regex&gt;</code></p>
<dd> Same as <code>-FA</code> except only matching setup tests are excluded.</p>
<dt><code>-FC &lt;regex&gt;, &#8211;fixture-exclude-cleanup &lt;regex&gt;</code></p>
<dd> Same as <code>-FA</code> except only matching cleanup tests are excluded.</p>
<dt><code>-D &lt;dashboard&gt;, &#8211;dashboard &lt;dashboard&gt;</code></p>
<dd> Execute dashboard test. </p>
<p> This option tells CTest to act as a CDash client and perform a dashboard test. All tests are <code>&lt;Mode&gt;&lt;Test&gt;</code>, where <code>&lt;Mode&gt;</code> can be <code>Experimental</code>, <code>Nightly</code>, and <code>Continuous</code>, and <code>&lt;Test&gt;</code> can be <code>Start</code>, <code>Update</code>, <code>Configure</code>, <code>Build</code>, <code>Test</code>, <code>Coverage</code>, and <code>Submit</code>. </p>
<p> See <i>Dashboard Client</i>.</p>
<dt><code>-D &lt;var&gt;:&lt;type&gt;=&lt;value&gt;</code></p>
<dd> Define a variable for script mode. </p>
<p> Pass in variable values on the command line. Use in conjunction with <code>-S</code> to pass variable values to a dashboard script. Parsing <code>-D</code> arguments as variable values is only attempted if the value following <code>-D</code> does not match any of the known dashboard types.</p>
<dt><code>-M &lt;model&gt;, &#8211;test-model &lt;model&gt;</code></p>
<dd> Sets the model for a dashboard. </p>
<p> This option tells CTest to act as a CDash client where the <code>&lt;model&gt;</code> can be <code>Experimental</code>, <code>Nightly</code>, and <code>Continuous</code>. Combining <code>-M</code> and <code>-T</code> is similar to <code>-D</code>. </p>
<p> See <i>Dashboard Client</i>.</p>
<dt><code>-T &lt;action&gt;, &#8211;test-action &lt;action&gt;</code></p>
<dd> Sets the dashboard action to perform. </p>
<p> This option tells CTest to act as a CDash client and perform some action such as <code>start</code>, <code>build</code>, <code>test</code> etc. See <i>Dashboard Client Steps</i> for the full list of actions. Combining <code>-M</code> and <code>-T</code> is similar to <code>-D</code>. </p>
<p> See <i>Dashboard Client</i>.</p>
<dt><code>-S &lt;script&gt;, &#8211;script &lt;script&gt;</code></p>
<dd> Execute a dashboard for a configuration. </p>
<p> This option tells CTest to load in a configuration script which sets a number of parameters such as the binary and source directories. Then CTest will do what is required to create and run a dashboard. This option basically sets up a dashboard and then runs <code>ctest -D</code> with the appropriate options. </p>
<p> See <i>Dashboard Client</i>.</p>
<dt><code>-SP &lt;script&gt;, &#8211;script-new-process &lt;script&gt;</code></p>
<dd> Execute a dashboard for a configuration. </p>
<p> This option does the same operations as <code>-S</code> but it will do them in a separate process. This is primarily useful in cases where the script may modify the environment and you do not want the modified environment to impact other <code>-S</code> scripts. </p>
<p> See <i>Dashboard Client</i>.</p>
<dt><code>-I [Start,End,Stride,test#,test#|Test file], &#8211;tests-information</code></p>
<dd> Run a specific number of tests by number. </p>
<p> This option causes CTest to run tests starting at number <code>Start</code>, ending at number <code>End</code>, and incrementing by <code>Stride</code>. Any additional numbers after <code>Stride</code> are considered individual test numbers. <code>Start</code>, <code>End</code>, or <code>Stride</code> can be empty. Optionally a file can be given that contains the same syntax as the command line.</p>
<dt><code>-U, &#8211;union</code></p>
<dd> Take the Union of <code>-I</code> and <code>-R</code>. </p>
<p> When both <code>-R</code> and <code>-I</code> are specified by default the intersection of tests are run. By specifying <code>-U</code> the union of tests is run instead.</p>
<dt><code>&#8211;rerun-failed</code></p>
<dd> Run only the tests that failed previously. </p>
<p> This option tells CTest to perform only the tests that failed during its previous run. When this option is specified, CTest ignores all other options intended to modify the list of tests to run (<code>-L</code>, <code>-R</code>, <code>-E</code>, <code>-LE</code>, <code>-I</code>, etc). In the event that CTest runs and no tests fail, subsequent calls to CTest with the <code>&#8211;rerun-failed</code> option will run the set of tests that most recently failed (if any).</p>
<dt><code>&#8211;repeat &lt;mode&gt;:&lt;n&gt;</code></p>
<dd> Run tests repeatedly based on the given <code>&lt;mode&gt;</code> up to <code>&lt;n&gt;</code> times. The modes are:</p>
<dt><code>until-fail</code></p>
<dd> Require each test to run <code>&lt;n&gt;</code> times without failing in order to pass. This is useful in finding sporadic failures in test cases.</p>
<dt><code>until-pass</code></p>
<dd> Allow each test to run up to <code>&lt;n&gt;</code> times in order to pass. Repeats tests if they fail for any reason. This is useful in tolerating sporadic failures in test cases.</p>
<dt><code>after-timeout</code></p>
<dd> Allow each test to run up to <code>&lt;n&gt;</code> times in order to pass. Repeats tests only if they timeout. This is useful in tolerating sporadic timeouts in test cases on busy machines.</p>
<dt><code>&#8211;repeat-until-fail &lt;n&gt;</code></p>
<dd> Equivalent to <code>&#8211;repeat until-fail:&lt;n&gt;</code>.</p>
<dt><code>&#8211;max-width &lt;width&gt;</code></p>
<dd> Set the max width for a test name to output. </p>
<p> Set the maximum width for each test name to show in the output. This allows the user to widen the output to avoid clipping the test name which can be very annoying.</p>
<dt><code>&#8211;interactive-debug-mode [0|1]</code></p>
<dd> Set the interactive mode to <code>0</code> or <code>1</code>. </p>
<p> This option causes CTest to run tests in either an interactive mode or a non-interactive mode. In dashboard mode (<code>Experimental</code>, <code>Nightly</code>, <code>Continuous</code>), the default is non-interactive. In non-interactive mode, the environment variable <code>DASHBOARD_TEST_FROM_CTEST</code> is set. </p>
<p> Prior to CMake 3.11, interactive mode on Windows allowed system debug popup windows to appear. Now, due to CTest&#8217;s use of <code>libuv</code> to launch test processes, all system debug popup windows are always blocked.</p>
<dt><code>&#8211;no-label-summary</code></p>
<dd> Disable timing summary information for labels. </p>
<p> This option tells CTest not to print summary information for each label associated with the tests run. If there are no labels on the tests, nothing extra is printed. </p>
<p> See <i>Label and Subproject Summary</i>.</p>
<dt><code>&#8211;no-subproject-summary</code></p>
<dd> Disable timing summary information for subprojects. </p>
<p> This option tells CTest not to print summary information for each subproject associated with the tests run. If there are no subprojects on the tests, nothing extra is printed. </p>
<p> See <i>Label and Subproject Summary</i>. </p>
<p> <code>&#8211;build-and-test</code> See <i>Build and Test Mode</i>. </p>
<p> <code>&#8211;test-dir &lt;dir&gt;</code> Specify the directory in which to look for tests.</p>
<dt><code>&#8211;test-output-size-passed &lt;size&gt;</code></p>
<dd> Limit the output for passed tests to <code>&lt;size&gt;</code> bytes.</p>
<dt><code>&#8211;test-output-size-failed &lt;size&gt;</code></p>
<dd> Limit the output for failed tests to <code>&lt;size&gt;</code> bytes.</p>
<dt><code>&#8211;overwrite</code></p>
<dd> Overwrite CTest configuration option. </p>
<p> By default CTest uses configuration options from configuration file. This option will overwrite the configuration option.</p>
<dt><code>&#8211;force-new-ctest-process</code></p>
<dd> Run child CTest instances as new processes. </p>
<p> By default CTest will run child CTest instances within the same process. If this behavior is not desired, this argument will enforce new processes for child CTest processes.</p>
<dt><code>&#8211;schedule-random</code></p>
<dd> Use a random order for scheduling tests. </p>
<p> This option will run the tests in a random order. It is commonly used to detect implicit dependencies in a test suite.</p>
<dt><code>&#8211;submit-index</code></p>
<dd> Legacy option for old Dart2 dashboard server feature. Do not use.</p>
<dt><code>&#8211;timeout &lt;seconds&gt;</code></p>
<dd> Set the default test timeout. </p>
<p> This option effectively sets a timeout on all tests that do not already have a timeout set on them via the <code>TIMEOUT</code> property.</p>
<dt><code>&#8211;stop-time &lt;time&gt;</code></p>
<dd> Set a time at which all tests should stop running. </p>
<p> Set a real time of day at which all tests should timeout. Example: <code>7:00:00 -0400</code>. Any time format understood by the curl date parser is accepted. Local time is assumed if no timezone is specified.</p>
<dt><code>&#8211;print-labels</code></p>
<dd> Print all available test labels. </p>
<p> This option will not run any tests, it will simply print the list of all labels associated with the test set.</p>
<dt><code>&#8211;no-tests=&lt;[error|ignore]&gt;</code></p>
<dd> Regard no tests found either as error or ignore it. </p>
<p> If no tests were found, the default behavior of CTest is to always log an error message but to return an error code in script mode only. This option unifies the behavior of CTest by either returning an error code if no tests were found or by ignoring it.</p>
<dt><code>&#8211;help,-help,-usage,-h,-H,/?</code></p>
<dd> Print usage information and exit. </p>
<p> Usage describes the basic command line interface and its options.</p>
<dt><code>&#8211;version,-version,/V [&lt;f&gt;]</code></p>
<dd> Show program name/version banner and exit. </p>
<p> If a file is specified, the version is written into it. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-full [&lt;f&gt;]</code></p>
<dd> Print all help manuals and exit. </p>
<p> All manuals are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual &lt;man&gt; [&lt;f&gt;]</code></p>
<dd> Print one help manual and exit. </p>
<p> The specified manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual-list [&lt;f&gt;]</code></p>
<dd> List help manuals available and exit. </p>
<p> The list contains all manuals for which help may be obtained by using the <code>&#8211;help-manual</code> option followed by a manual name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command &lt;cmd&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one command and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual entry for <code>&lt;cmd&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command-list [&lt;f&gt;]</code></p>
<dd> List commands with help available and exit. </p>
<p> The list contains all commands for which help may be obtained by using the <code>&#8211;help-command</code> option followed by a command name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-commands [&lt;f&gt;]</code></p>
<dd> Print cmake-commands manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module &lt;mod&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one module and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual entry for <code>&lt;mod&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module-list [&lt;f&gt;]</code></p>
<dd> List modules with help available and exit. </p>
<p> The list contains all modules for which help may be obtained by using the <code>&#8211;help-module</code> option followed by a module name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-modules [&lt;f&gt;]</code></p>
<dd> Print cmake-modules manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy &lt;cmp&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one policy and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual entry for <code>&lt;cmp&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy-list [&lt;f&gt;]</code></p>
<dd> List policies with help available and exit. </p>
<p> The list contains all policies for which help may be obtained by using the <code>&#8211;help-policy</code> option followed by a policy name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policies [&lt;f&gt;]</code></p>
<dd> Print cmake-policies manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property &lt;prop&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one property and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual entries for <code>&lt;prop&gt;</code> are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property-list [&lt;f&gt;]</code></p>
<dd> List properties with help available and exit. </p>
<p> The list contains all properties for which help may be obtained by using the <code>&#8211;help-property</code> option followed by a property name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-properties [&lt;f&gt;]</code></p>
<dd> Print cmake-properties manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable &lt;var&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one variable and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual entry for <code>&lt;var&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable-list [&lt;f&gt;]</code></p>
<dd> List variables with help available and exit. </p>
<p> The list contains all variables for which help may be obtained by using the <code>&#8211;help-variable</code> option followed by a variable name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variables [&lt;f&gt;]</code></p>
<dd> Print cmake-variables manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</dl>
<h2>LABEL MATCHING</h2>
<p> Tests may have labels attached to them. Tests may be included or excluded from a test run by filtering on the labels. Each individual filter is a regular expression applied to the labels attached to a test. </p>
<p> When <code>-L</code> is used, in order for a test to be included in a test run, each regular expression must match at least one label. Using more than one <code>-L</code> option means &quot;match <code>all</code> of these&quot;. </p>
<p> The <code>-LE</code> option works just like <code>-L</code>, but excludes tests rather than including them. A test is excluded if each regular expression matches at least one label. </p>
<p> If a test has no labels attached to it, then <code>-L</code> will never include that test, and <code>-LE</code> will never exclude that test. As an example of tests with labels, consider five tests, with the following labels:</p>
<dl>
<dt>&bull;</p>
<dd> <i>test1</i> has labels <i>tuesday</i> and <i>production</i></p>
<dt>&bull;</p>
<dd> <i>test2</i> has labels <i>tuesday</i> and <i>test</i></p>
<dt>&bull;</p>
<dd> <i>test3</i> has labels <i>wednesday</i> and <i>production</i></p>
<dt>&bull;</p>
<dd> <i>test4</i> has label <i>wednesday</i></p>
<dt>&bull;</p>
<dd> <i>test5</i> has labels <i>friday</i> and <i>test</i> </p>
<p> Running <code>ctest</code> with <code>-L tuesday -L test</code> will select <i>test2</i>, which has both labels. Running CTest with <code>-L test</code> will select <i>test2</i> and <i>test5</i>, because both of them have a label that matches that regular expression. </p>
<p> Because the matching works with regular expressions, take note that running CTest with <code>-L es</code> will match all five tests. To select the <i>tuesday</i> and <i>wednesday</i> tests together, use a single regular expression that matches either of them, like <code>-L &quot;tue|wed&quot;</code>.</dl>
<h2>LABEL AND SUBPROJECT SUMMARY</h2>
<p> CTest prints timing summary information for each <code>LABEL</code> and subproject associated with the tests run. The label time summary will not include labels that are mapped to subprojects. </p>
<p> New in version 3.22: Labels added dynamically during test execution are also reported in the timing summary. See Additional Labels. </p>
<p> When the <code>PROCESSORS</code> test property is set, CTest will display a weighted test timing result in label and subproject summaries. The time is reported with <i>sec*proc</i> instead of just <i>sec</i>. </p>
<p> The weighted time summary reported for each label or subproject <code>j</code> is computed as: </p>
<p>Weighted Time Summary for Label/Subproject j =<br />
    sum(raw_test_time[j,i] * num_processors[j,i], i=1&#8230;num_tests[j])<br />
for labels/subprojects j=1&#8230;total</p>
<p> where:</p>
<dl>
<dt>&bull;</p>
<dd> <code>raw_test_time[j,i]</code>: Wall-clock time for the <code>i</code> test for the <code>j</code> label or subproject</p>
<dt>&bull;</p>
<dd> <code>num_processors[j,i]</code>: Value of the CTest <code>PROCESSORS</code> property for the <code>i</code> test for the <code>j</code> label or subproject</p>
<dt>&bull;</p>
<dd> <code>num_tests[j]</code>: Number of tests associated with the <code>j</code> label or subproject</p>
<dt>&bull;</p>
<dd> <code>total</code>: Total number of labels or subprojects that have at least one test run </p>
<p> Therefore, the weighted time summary for each label or subproject represents the amount of time that CTest gave to run the tests for each label or subproject and gives a good representation of the total expense of the tests for each label or subproject when compared to other labels or subprojects. </p>
<p> For example, if <code>SubprojectA</code> showed <code>100 sec*proc</code> and <code>SubprojectB</code> showed <code>10 sec*proc</code>, then CTest allocated approximately 10 times the CPU/core time to run the tests for <code>SubprojectA</code> than for <code>SubprojectB</code> (e.g. so if effort is going to be expended to reduce the cost of the test suite for the whole project, then reducing the cost of the test suite for <code>SubprojectA</code> would likely have a larger impact than effort to reduce the cost of the test suite for <code>SubprojectB</code>).</dl>
<h2>BUILD AND TEST MODE</h2>
<p> CTest provides a command-line signature to configure (i.e. run cmake on), build, and/or execute a test: </p>
<p>ctest&#8211; build &#8211; and-test&lt;path &#8211; to &#8211; source&gt;&lt;path &#8211; to &#8211; build&gt; &#8211;build &#8211; generator&lt;generator&gt;[&lt;options&gt;&#8230;][&#8211;build &#8211; options&lt;opts&gt;&#8230;][&#8211;test &#8211; command&lt;command&gt;[&lt;args&gt;&#8230;]]</p>
<p> The configure and test steps are optional. The arguments to this command line are the source and binary directories. The <code>&#8211;build-generator</code> option <i>must</i> be provided to use <code>&#8211;build-and-test</code>. If <code>&#8211;test-command</code> is specified then that will be run after the build is complete. Other options that affect this mode include:</p>
<dl>
<dt><code>&#8211;build-target</code></p>
<dd> Specify a specific target to build. </p>
<p> If left out the <code>all</code> target is built.</p>
<dt><code>&#8211;build-nocmake</code></p>
<dd> Run the build without running cmake first. </p>
<p> Skip the cmake step.</p>
<dt><code>&#8211;build-run-dir</code></p>
<dd> Specify directory to run programs from. </p>
<p> Directory where programs will be after it has been compiled.</p>
<dt><code>&#8211;build-two-config</code></p>
<dd> Run CMake twice.</p>
<dt><code>&#8211;build-exe-dir</code></p>
<dd> Specify the directory for the executable.</p>
<dt><code>&#8211;build-generator</code></p>
<dd> Specify the generator to use. See the <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code> manual.</p>
<dt><code>&#8211;build-generator-platform</code></p>
<dd> Specify the generator-specific platform.</p>
<dt><code>&#8211;build-generator-toolset</code></p>
<dd> Specify the generator-specific toolset.</p>
<dt><code>&#8211;build-project</code></p>
<dd> Specify the name of the project to build.</p>
<dt><code>&#8211;build-makeprogram</code></p>
<dd> Specify the explicit make program to be used by CMake when configuring and building the project. Only applicable for Make and Ninja based generators.</p>
<dt><code>&#8211;build-noclean</code></p>
<dd> Skip the make clean step.</p>
<dt><code>&#8211;build-config-sample</code></p>
<dd> A sample executable to use to determine the configuration that should be used. e.g. <code>Debug</code>, <code>Release</code> etc.</p>
<dt><code>&#8211;build-options</code></p>
<dd> Additional options for configuring the build (i.e. for CMake, not for the build tool). Note that if this is specified, the <code>&#8211;build-options</code> keyword and its arguments must be the last option given on the command line, with the possible exception of <code>&#8211;test-command</code>.</p>
<dt><code>&#8211;test-command</code></p>
<dd> The command to run as the test step with the <code>&#8211;build-and-test</code> option. All arguments following this keyword will be assumed to be part of the test command line, so it must be the last option given.</p>
<dt><code>&#8211;test-timeout</code></p>
<dd> The time limit in seconds</dl>
<h2>DASHBOARD CLIENT</h2>
<p> CTest can operate as a client for the <i>CDash</i> software quality dashboard application. As a dashboard client, CTest performs a sequence of steps to configure, build, and test software, and then submits the results to a <i>CDash</i> server. The command-line signature used to submit to <i>CDash</i> is: </p>
<pre>
ctest (-D &lt;dashboard&gt; | -M &lt;model&gt; -T &lt;action&gt; | -S &lt;script&gt; | -SP &lt;script&gt;)
      [-- &lt;dashboard-options&gt;...]
</pre>
<p> Options for Dashboard Client include:</p>
<dl>
<dt><code>&#8211;group &lt;group&gt;</code></p>
<dd> Specify what group you&#8217;d like to submit results to </p>
<p> Submit dashboard to specified group instead of default one. By default, the dashboard is submitted to Nightly, Experimental, or Continuous group, but by specifying this option, the group can be arbitrary. </p>
<p> This replaces the deprecated option <code>&#8211;track</code>. Despite the name change its behavior is unchanged.</p>
<dt><code>-A &lt;file&gt;, &#8211;add-notes &lt;file&gt;</code></p>
<dd> Add a notes file with submission. </p>
<p> This option tells CTest to include a notes file when submitting dashboard.</p>
<dt><code>&#8211;tomorrow-tag</code></p>
<dd> <code>Nightly</code> or <code>Experimental</code> starts with next day tag. </p>
<p> This is useful if the build will not finish in one day.</p>
<dt><code>&#8211;extra-submit &lt;file&gt;[;&lt;file&gt;]</code></p>
<dd> Submit extra files to the dashboard. </p>
<p> This option will submit extra files to the dashboard.</p>
<dt><code>&#8211;http1.0</code></p>
<dd> Submit using <i>HTTP 1.0</i>. </p>
<p> This option will force CTest to use <i>HTTP 1.0</i> to submit files to the dashboard, instead of <i>HTTP 1.1</i>.</p>
<dt><code>&#8211;no-compress-output</code></p>
<dd> Do not compress test output when submitting. </p>
<p> This flag will turn off automatic compression of test output. Use this to maintain compatibility with an older version of CDash which doesn&#8217;t support compressed test output.</dl>
<h3>Dashboard Client Steps</h3>
<p> CTest defines an ordered list of testing steps of which some or all may be run as a dashboard client:</p>
<dl>
<dt><code>Start</code></p>
<dd> Start a new dashboard submission to be composed of results recorded by the following steps. See the <i>CTest Start Step</i> section below.</p>
<dt><code>Update</code></p>
<dd> Update the source tree from its version control repository. Record the old and new versions and the list of updated source files. See the <i>CTest Update Step</i> section below.</p>
<dt><code>Configure</code></p>
<dd> Configure the software by running a command in the build tree. Record the configuration output log. See the <i>CTest Configure Step</i> section below.</p>
<dt><code>Build</code></p>
<dd> Build the software by running a command in the build tree. Record the build output log and detect warnings and errors. See the <i>CTest Build Step</i> section below.</p>
<dt><code>Test</code></p>
<dd> Test the software by loading a <code>CTestTestfile.cmake</code> from the build tree and executing the defined tests. Record the output and result of each test. See the <i>CTest Test Step</i> section below.</p>
<dt><code>Coverage</code></p>
<dd> Compute coverage of the source code by running a coverage analysis tool and recording its output. See the <i>CTest Coverage Step</i> section below.</p>
<dt><code>MemCheck</code></p>
<dd> Run the software test suite through a memory check tool. Record the test output, results, and issues reported by the tool. See the <i>CTest MemCheck Step</i> section below.</p>
<dt><code>Submit</code></p>
<dd> Submit results recorded from other testing steps to the software quality dashboard server. See the <i>CTest Submit Step</i> section below.</dl>
<h3>Dashboard Client Modes</h3>
<p> CTest defines three modes of operation as a dashboard client:</p>
<dl>
<dt><code>Nightly</code></p>
<dd> This mode is intended to be invoked once per day, typically at night. It enables the <code>Start</code>, <code>Update</code>, <code>Configure</code>, <code>Build</code>, <code>Test</code>, <code>Coverage</code>, and <code>Submit</code> steps by default. Selected steps run even if the <code>Update</code> step reports no changes to the source tree.</p>
<dt><code>Continuous</code></p>
<dd> This mode is intended to be invoked repeatedly throughout the day. It enables the <code>Start</code>, <code>Update</code>, <code>Configure</code>, <code>Build</code>, <code>Test</code>, <code>Coverage</code>, and <code>Submit</code> steps by default, but exits after the <code>Update</code> step if it reports no changes to the source tree.</p>
<dt><code>Experimental</code></p>
<dd> This mode is intended to be invoked by a developer to test local changes. It enables the <code>Start</code>, <code>Configure</code>, <code>Build</code>, <code>Test</code>, <code>Coverage</code>, and <code>Submit</code> steps by default.</dl>
<h3>Dashboard Client via CTest Command-Line</h3>
<p> CTest can perform testing on an already-generated build tree. Run the <code>ctest</code> command with the current working directory set to the build tree and use one of these signatures: </p>
<p>ctest &#8211; D&lt;mode&gt;[&lt;step&gt;] ctest &#8211; M&lt;mode&gt;[-T&lt;step&gt;]&#8230;</p>
<p> The <code>&lt;mode&gt;</code> must be one of the above <i>Dashboard Client Modes</i>, and each <code>&lt;step&gt;</code> must be one of the above <i>Dashboard Client Steps</i>. </p>
<p> CTest reads the <i>Dashboard Client Configuration</i> settings from a file in the build tree called either <code>CTestConfiguration.ini</code> or <code>DartConfiguration.tcl</code> (the names are historical). The format of the file is: </p>
<pre>
# Lines starting in '#' are comments.
# Other non-blank lines are key-value pairs.
&lt;setting&gt;: &lt;value&gt;
</pre>
<p> where <code>&lt;setting&gt;</code> is the setting name and <code>&lt;value&gt;</code> is the setting value. </p>
<p> In build trees generated by CMake, this configuration file is generated by the <code>CTest</code> module if included by the project. The module uses variables to obtain a value for each setting as documented with the settings below.</p>
<h3>Dashboard Client via CTest Script</h3>
<p> CTest can perform testing driven by a <code><a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7)</code> script that creates and maintains the source and build tree as well as performing the testing steps. Run the <code>ctest</code> command with the current working directory set outside of any build tree and use one of these signatures: </p>
<pre>
ctest -S &lt;script&gt;
ctest -SP &lt;script&gt;
</pre>
<p> The <code>&lt;script&gt;</code> file must call CTest Commands commands to run testing steps explicitly as documented below. The commands obtain <i>Dashboard Client Configuration</i> settings from their arguments or from variables set in the script.</p>
<h2>DASHBOARD CLIENT CONFIGURATION</h2>
<p> The <i>Dashboard Client Steps</i> may be configured by named settings as documented in the following sections.</p>
<h3>CTest Start Step</h3>
<p> Start a new dashboard submission to be composed of results recorded by the following steps. </p>
<p> In a <i>CTest Script</i>, the <code>ctest_start()</code> command runs this step. Arguments to the command may specify some of the step settings. The command first runs the command-line specified by the <code>CTEST_CHECKOUT_COMMAND</code> variable, if set, to initialize the source directory. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>BuildDirectory</code></p>
<dd> The full path to the project build tree.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_BINARY_DIRECTORY</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>PROJECT_BINARY_DIR</code></p>
<dt><code>SourceDirectory</code></p>
<dd> The full path to the project source tree.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SOURCE_DIRECTORY</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>PROJECT_SOURCE_DIR</code></dl>
<h3>CTest Update Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_update()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings to specify the version control tool include:</p>
<dl>
<dt><code>BZRCommand</code></p>
<dd> <code>bzr</code> command-line tool to use if source tree is managed by Bazaar.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_BZR_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: none</p>
<dt><code>BZRUpdateOptions</code></p>
<dd> Command-line options to the <code>BZRCommand</code> when updating the source.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_BZR_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: none</p>
<dt><code>CVSCommand</code></p>
<dd> <code>cvs</code> command-line tool to use if source tree is managed by CVS.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_CVS_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CVSCOMMAND</code></p>
<dt><code>CVSUpdateOptions</code></p>
<dd> Command-line options to the <code>CVSCommand</code> when updating the source.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_CVS_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CVS_UPDATE_OPTIONS</code></p>
<dt><code>GITCommand</code></p>
<dd> <code>git</code> command-line tool to use if source tree is managed by Git.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_GIT_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>GITCOMMAND</code> </p>
<p> The source tree is updated by <code>git fetch</code> followed by <code>git reset &#8211;hard</code> to the <code>FETCH_HEAD</code>. The result is the same as <code>git pull</code> except that any local modifications are overwritten. Use <code>GITUpdateCustom</code> to specify a different approach.</p>
<dt><code>GITInitSubmodules</code></p>
<dd> If set, CTest will update the repository&#8217;s submodules before updating.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_GIT_INIT_SUBMODULES</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_GIT_INIT_SUBMODULES</code></p>
<dt><code>GITUpdateCustom</code></p>
<dd> Specify a custom command line (as a semicolon-separated list) to run in the source tree (Git work tree) to update it instead of running the <code>GITCommand</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_GIT_UPDATE_CUSTOM</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_GIT_UPDATE_CUSTOM</code></p>
<dt><code>GITUpdateOptions</code></p>
<dd> Command-line options to the <code>GITCommand</code> when updating the source.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_GIT_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>GIT_UPDATE_OPTIONS</code></p>
<dt><code>HGCommand</code></p>
<dd> <code>hg</code> command-line tool to use if source tree is managed by Mercurial.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_HG_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: none</p>
<dt><code>HGUpdateOptions</code></p>
<dd> Command-line options to the <code>HGCommand</code> when updating the source.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_HG_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: none</p>
<dt><code>P4Client</code></p>
<dd> Value of the <code>-c</code> option to the <code>P4Command</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_P4_CLIENT</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_P4_CLIENT</code></p>
<dt><code>P4Command</code></p>
<dd> <code>p4</code> command-line tool to use if source tree is managed by Perforce.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_P4_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>P4COMMAND</code></p>
<dt><code>P4Options</code></p>
<dd> Command-line options to the <code>P4Command</code> for all invocations.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_P4_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_P4_OPTIONS</code></p>
<dt><code>P4UpdateCustom</code></p>
<dd> Specify a custom command line (as a semicolon-separated list) to run in the source tree (Perforce tree) to update it instead of running the <code>P4Command</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_P4_UPDATE_CUSTOM</code></p>
<dt><code>P4UpdateOptions</code></p>
<dd> Command-line options to the <code>P4Command</code> when updating the source.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_P4_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_P4_UPDATE_OPTIONS</code></p>
<dt><code>SVNCommand</code></p>
<dd> <code>svn</code> command-line tool to use if source tree is managed by Subversion.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SVN_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>SVNCOMMAND</code></p>
<dt><code>SVNOptions</code></p>
<dd> Command-line options to the <code>SVNCommand</code> for all invocations.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SVN_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_SVN_OPTIONS</code></p>
<dt><code>SVNUpdateOptions</code></p>
<dd> Command-line options to the <code>SVNCommand</code> when updating the source.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SVN_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>SVN_UPDATE_OPTIONS</code></p>
<dt><code>UpdateCommand</code></p>
<dd> Specify the version-control command-line tool to use without detecting the VCS that manages the source tree.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_UPDATE_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>&lt;VCS&gt;COMMAND</code> when <code>UPDATE_TYPE</code> is <code>&lt;vcs&gt;</code>, else <code>UPDATE_COMMAND</code></p>
<dt><code>UpdateOptions</code></p>
<dd> Command-line options to the <code>UpdateCommand</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_UPDATE_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>&lt;VCS&gt;_UPDATE_OPTIONS</code> when <code>UPDATE_TYPE</code> is <code>&lt;vcs&gt;</code>, else <code>UPDATE_OPTIONS</code></p>
<dt><code>UpdateType</code></p>
<dd> Specify the version-control system that manages the source tree if it cannot be detected automatically. The value may be <code>bzr</code>, <code>cvs</code>, <code>git</code>, <code>hg</code>, <code>p4</code>, or <code>svn</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none, detected from source tree</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>UPDATE_TYPE</code> if set, else <code>CTEST_UPDATE_TYPE</code></p>
<dt><code>UpdateVersionOnly</code></p>
<dd> Specify that you want the version control update command to only discover the current version that is checked out, and not to update to a different version.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_UPDATE_VERSION_ONLY</code></p>
<dt><code>UpdateVersionOverride</code></p>
<dd> Specify the current version of your source tree. </p>
<p> When this variable is set to a non-empty string, CTest will report the value you specified rather than using the update command to discover the current version that is checked out. Use of this variable supersedes <code>UpdateVersionOnly</code>. Like <code>UpdateVersionOnly</code>, using this variable tells CTest not to update the source tree to a different version.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_UPDATE_VERSION_OVERRIDE</code> </p>
<p> Additional configuration settings include:</p>
<dt><code>NightlyStartTime</code></p>
<dd> In the <code>Nightly</code> dashboard mode, specify the &quot;nightly start time&quot;. With centralized version control systems (<code>cvs</code> and <code>svn</code>), the <code>Update</code> step checks out the version of the software as of this time so that multiple clients choose a common version to test. This is not well-defined in distributed version-control systems so the setting is ignored.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_NIGHTLY_START_TIME</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>NIGHTLY_START_TIME</code> if set, else <code>CTEST_NIGHTLY_START_TIME</code></dl>
<h3>CTest Configure Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_configure()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>ConfigureCommand</code></p>
<dd> Command-line to launch the software configuration process. It will be executed in the location specified by the <code>BuildDirectory</code> setting.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_CONFIGURE_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CMAKE_COMMAND</code> followed by <code>PROJECT_SOURCE_DIR</code></p>
<dt><code>LabelsForSubprojects</code></p>
<dd> Specify a semicolon-separated list of labels that will be treated as subprojects. This mapping will be passed on to CDash when configure, test or build results are submitted.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_LABELS_FOR_SUBPROJECTS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_LABELS_FOR_SUBPROJECTS</code> </p>
<p> See <i>Label and Subproject Summary</i>.</dl>
<h3>CTest Build Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_build()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>DefaultCTestConfigurationType</code></p>
<dd> When the build system to be launched allows build-time selection of the configuration (e.g. <code>Debug</code>, <code>Release</code>), this specifies the default configuration to be built when no <code>-C</code> option is given to the <code>ctest</code> command. The value will be substituted into the value of <code>MakeCommand</code> to replace the literal string <code>${CTEST_CONFIGURATION_TYPE}</code> if it appears.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_CONFIGURATION_TYPE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DEFAULT_CTEST_CONFIGURATION_TYPE</code>, initialized by the <code>CMAKE_CONFIG_TYPE</code> environment variable</p>
<dt><code>LabelsForSubprojects</code></p>
<dd> Specify a semicolon-separated list of labels that will be treated as subprojects. This mapping will be passed on to CDash when configure, test or build results are submitted.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_LABELS_FOR_SUBPROJECTS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_LABELS_FOR_SUBPROJECTS</code> </p>
<p> See <i>Label and Subproject Summary</i>.</p>
<dt><code>MakeCommand</code></p>
<dd> Command-line to launch the software build process. It will be executed in the location specified by the <code>BuildDirectory</code> setting.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_BUILD_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MAKECOMMAND</code>, initialized by the <code>build_command()</code> command</p>
<dt><code>UseLaunchers</code></p>
<dd> For build trees generated by CMake using one of the Makefile Generators or the <code>Ninja</code> generator, specify whether the <code>CTEST_USE_LAUNCHERS</code> feature is enabled by the <code>CTestUseLaunchers</code> module (also included by the <code>CTest</code> module). When enabled, the generated build system wraps each invocation of the compiler, linker, or custom command line with a &quot;launcher&quot; that communicates with CTest via environment variables and files to report granular build warning and error information. Otherwise, CTest must &quot;scrape&quot; the build output log for diagnostics.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_USE_LAUNCHERS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_USE_LAUNCHERS</code></dl>
<h3>CTest Test Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_test()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>ResourceSpecFile</code></p>
<dd> Specify a <i>resource specification file</i>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_RESOURCE_SPEC_FILE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_RESOURCE_SPEC_FILE</code> </p>
<p> See <i>Resource Allocation</i> for more information.</p>
<dt><code>LabelsForSubprojects</code></p>
<dd> Specify a semicolon-separated list of labels that will be treated as subprojects. This mapping will be passed on to CDash when configure, test or build results are submitted.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_LABELS_FOR_SUBPROJECTS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_LABELS_FOR_SUBPROJECTS</code> </p>
<p> See <i>Label and Subproject Summary</i>.</p>
<dt><code>TestLoad</code></p>
<dd> While running tests in parallel (e.g. with <code>-j</code>), try not to start tests when they may cause the CPU load to pass above a given threshold.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_TEST_LOAD</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_TEST_LOAD</code></p>
<dt><code>TimeOut</code></p>
<dd> The default timeout for each test if not specified by the <code>TIMEOUT</code> test property.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_TEST_TIMEOUT</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DART_TESTING_TIMEOUT</code> </p>
<p> To report extra test values to CDash, see Additional Test Measurements.</dl>
<h3>CTest Coverage Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_coverage()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>CoverageCommand</code></p>
<dd> Command-line tool to perform software coverage analysis. It will be executed in the location specified by the <code>BuildDirectory</code> setting.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_COVERAGE_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>COVERAGE_COMMAND</code></p>
<dt><code>CoverageExtraFlags</code></p>
<dd> Specify command-line options to the <code>CoverageCommand</code> tool.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_COVERAGE_EXTRA_FLAGS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>COVERAGE_EXTRA_FLAGS</code> </p>
<p> These options are the first arguments passed to <code>CoverageCommand</code>.</dl>
<h3>CTest MemCheck Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_memcheck()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>MemoryCheckCommand</code></p>
<dd> Command-line tool to perform dynamic analysis. Test command lines will be launched through this tool.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_MEMORYCHECK_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MEMORYCHECK_COMMAND</code></p>
<dt><code>MemoryCheckCommandOptions</code></p>
<dd> Specify command-line options to the <code>MemoryCheckCommand</code> tool. They will be placed prior to the test command line.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_MEMORYCHECK_COMMAND_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MEMORYCHECK_COMMAND_OPTIONS</code></p>
<dt><code>MemoryCheckType</code></p>
<dd> Specify the type of memory checking to perform.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_MEMORYCHECK_TYPE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MEMORYCHECK_TYPE</code></p>
<dt><code>MemoryCheckSanitizerOptions</code></p>
<dd> Specify options to sanitizers when running with a sanitize-enabled build.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_MEMORYCHECK_SANITIZER_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MEMORYCHECK_SANITIZER_OPTIONS</code></p>
<dt><code>MemoryCheckSuppressionFile</code></p>
<dd> Specify a file containing suppression rules for the <code>MemoryCheckCommand</code> tool. It will be passed with options appropriate to the tool.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_MEMORYCHECK_SUPPRESSIONS_FILE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MEMORYCHECK_SUPPRESSIONS_FILE</code> </p>
<p> Additional configuration settings include:</p>
<dt><code>BoundsCheckerCommand</code></p>
<dd> Specify a <code>MemoryCheckCommand</code> that is known to be command-line compatible with Bounds Checker.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: none</p>
<dt><code>PurifyCommand</code></p>
<dd> Specify a <code>MemoryCheckCommand</code> that is known to be command-line compatible with Purify.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>PURIFYCOMMAND</code></p>
<dt><code>ValgrindCommand</code></p>
<dd> Specify a <code>MemoryCheckCommand</code> that is known to be command-line compatible with Valgrind.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>VALGRIND_COMMAND</code></p>
<dt><code>ValgrindCommandOptions</code></p>
<dd> Specify command-line options to the <code>ValgrindCommand</code> tool. They will be placed prior to the test command line.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>VALGRIND_COMMAND_OPTIONS</code></p>
<dt><code>DrMemoryCommand</code></p>
<dd> Specify a <code>MemoryCheckCommand</code> that is known to be a command-line compatible with DrMemory.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DRMEMORY_COMMAND</code></p>
<dt><code>DrMemoryCommandOptions</code></p>
<dd> Specify command-line options to the <code>DrMemoryCommand</code> tool. They will be placed prior to the test command line.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DRMEMORY_COMMAND_OPTIONS</code></p>
<dt><code>CudaSanitizerCommand</code></p>
<dd> Specify a <code>MemoryCheckCommand</code> that is known to be a command-line compatible with cuda-memcheck or compute-sanitizer.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CUDA_SANITIZER_COMMAND</code></p>
<dt><code>CudaSanitizerCommandOptions</code></p>
<dd> Specify command-line options to the <code>CudaSanitizerCommand</code> tool. They will be placed prior to the test command line.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CUDA_SANITIZER_COMMAND_OPTIONS</code></dl>
<h3>CTest Submit Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_submit()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>BuildName</code></p>
<dd> Describe the dashboard client platform with a short string. (Operating system, compiler, etc.)</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_BUILD_NAME</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>BUILDNAME</code></p>
<dt><code>CDashVersion</code></p>
<dd> Legacy option. Not used.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none, detected from server</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_CDASH_VERSION</code></p>
<dt><code>CTestSubmitRetryCount</code></p>
<dd> Specify a number of attempts to retry submission on network failure.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none, use the <code>ctest_submit()</code> <code>RETRY_COUNT</code> option.</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_SUBMIT_RETRY_COUNT</code></p>
<dt><code>CTestSubmitRetryDelay</code></p>
<dd> Specify a delay before retrying submission on network failure.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: none, use the <code>ctest_submit()</code> <code>RETRY_DELAY</code> option.</p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_SUBMIT_RETRY_DELAY</code></p>
<dt><code>CurlOptions</code></p>
<dd> Specify a semicolon-separated list of options to control the Curl library that CTest uses internally to connect to the server. Possible options are <code>CURLOPT_SSL_VERIFYPEER_OFF</code> and <code>CURLOPT_SSL_VERIFYHOST_OFF</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_CURL_OPTIONS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_CURL_OPTIONS</code></p>
<dt><code>DropLocation</code></p>
<dd> Legacy option. When <code>SubmitURL</code> is not set, it is constructed from <code>DropMethod</code>, <code>DropSiteUser</code>, <code>DropSitePassword</code>, <code>DropSite</code>, and <code>DropLocation</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_LOCATION</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_LOCATION</code> if set, else <code>CTEST_DROP_LOCATION</code></p>
<dt><code>DropMethod</code></p>
<dd> Legacy option. When <code>SubmitURL</code> is not set, it is constructed from <code>DropMethod</code>, <code>DropSiteUser</code>, <code>DropSitePassword</code>, <code>DropSite</code>, and <code>DropLocation</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_METHOD</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_METHOD</code> if set, else <code>CTEST_DROP_METHOD</code></p>
<dt><code>DropSite</code></p>
<dd> Legacy option. When <code>SubmitURL</code> is not set, it is constructed from <code>DropMethod</code>, <code>DropSiteUser</code>, <code>DropSitePassword</code>, <code>DropSite</code>, and <code>DropLocation</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_SITE</code> if set, else <code>CTEST_DROP_SITE</code></p>
<dt><code>DropSitePassword</code></p>
<dd> Legacy option. When <code>SubmitURL</code> is not set, it is constructed from <code>DropMethod</code>, <code>DropSiteUser</code>, <code>DropSitePassword</code>, <code>DropSite</code>, and <code>DropLocation</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE_PASSWORD</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_SITE_PASSWORD</code> if set, else <code>CTEST_DROP_SITE_PASWORD</code></p>
<dt><code>DropSiteUser</code></p>
<dd> Legacy option. When <code>SubmitURL</code> is not set, it is constructed from <code>DropMethod</code>, <code>DropSiteUser</code>, <code>DropSitePassword</code>, <code>DropSite</code>, and <code>DropLocation</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE_USER</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_SITE_USER</code> if set, else <code>CTEST_DROP_SITE_USER</code></p>
<dt><code>IsCDash</code></p>
<dd> Legacy option. Not used.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE_CDASH</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_DROP_SITE_CDASH</code></p>
<dt><code>ScpCommand</code></p>
<dd> Legacy option. Not used.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SCP_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>SCPCOMMAND</code></p>
<dt><code>Site</code></p>
<dd> Describe the dashboard client host site with a short string. (Hostname, domain, etc.)</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SITE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>SITE</code>, initialized by the <code>site_name()</code> command</p>
<dt><code>SubmitURL</code></p>
<dd> The <code>http</code> or <code>https</code> URL of the dashboard server to send the submission to.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_SUBMIT_URL</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>SUBMIT_URL</code> if set, else <code>CTEST_SUBMIT_URL</code></p>
<dt><code>TriggerSite</code></p>
<dd> Legacy option. Not used.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_TRIGGER_SITE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>TRIGGER_SITE</code> if set, else <code>CTEST_TRIGGER_SITE</code></dl>
<h2>SHOW AS JSON OBJECT MODEL</h2>
<p> When the <code>&#8211;show-only=json-v1</code> command line option is given, the test information is output in JSON format. Version 1.0 of the JSON object model is defined as follows:</p>
<dl>
<dt><code>kind</code></p>
<dd> The string &quot;ctestInfo&quot;.</p>
<dt><code>version</code></p>
<dd> A JSON object specifying the version components. Its members are</p>
<dt><code>major</code></p>
<dd> A non-negative integer specifying the major version component.</p>
<dt><code>minor</code></p>
<dd> A non-negative integer specifying the minor version component.</p>
<dt><code>backtraceGraph</code></p>
<dd> JSON object representing backtrace information with the following members:</p>
<dt><code>commands</code></p>
<dd> List of command names.</p>
<dt><code>files</code></p>
<dd> List of file names.</p>
<dt><code>nodes</code></p>
<dd> List of node JSON objects with members:</p>
<dt><code>command</code></p>
<dd> Index into the <code>commands</code> member of the <code>backtraceGraph</code>.</p>
<dt><code>file</code></p>
<dd> Index into the <code>files</code> member of the <code>backtraceGraph</code>.</p>
<dt><code>line</code></p>
<dd> Line number in the file where the backtrace was added.</p>
<dt><code>parent</code></p>
<dd> Index into the <code>nodes</code> member of the <code>backtraceGraph</code> representing the parent in the graph.</p>
<dt><code>tests</code></p>
<dd> A JSON array listing information about each test. Each entry is a JSON object with members:</p>
<dt><code>name</code></p>
<dd> Test name.</p>
<dt><code>config</code></p>
<dd> Configuration that the test can run on. Empty string means any config.</p>
<dt><code>command</code></p>
<dd> List where the first element is the test command and the remaining elements are the command arguments.</p>
<dt><code>backtrace</code></p>
<dd> Index into the <code>nodes</code> member of the <code>backtraceGraph</code>.</p>
<dt><code>properties</code></p>
<dd> Test properties. Can contain keys for each of the supported test properties.</dl>
<h2>RESOURCE ALLOCATION</h2>
<p> CTest provides a mechanism for tests to specify the resources that they need in a fine-grained way, and for users to specify the resources available on the running machine. This allows CTest to internally keep track of which resources are in use and which are free, scheduling tests in a way that prevents them from trying to claim resources that are not available. </p>
<p> When the resource allocation feature is used, CTest will not oversubscribe resources. For example, if a resource has 8 slots, CTest will not run tests that collectively use more than 8 slots at a time. This has the effect of limiting how many tests can run at any given time, even if a high <code>-j</code> argument is used, if those tests all use some slots from the same resource. In addition, it means that a single test that uses more of a resource than is available on a machine will not run at all (and will be reported as <code>Not Run</code>). </p>
<p> A common use case for this feature is for tests that require the use of a GPU. Multiple tests can simultaneously allocate memory from a GPU, but if too many tests try to do this at once, some of them will fail to allocate, resulting in a failed test, even though the test would have succeeded if it had the memory it needed. By using the resource allocation feature, each test can specify how much memory it requires from a GPU, allowing CTest to schedule tests in a way that running several of these tests at once does not exhaust the GPU&#8217;s memory pool. </p>
<p> Please note that CTest has no concept of what a GPU is or how much memory it has, nor does it have any way of communicating with a GPU to retrieve this information or perform any memory management. CTest simply keeps track of a list of abstract resource types, each of which has a certain number of slots available for tests to use. Each test specifies the number of slots that it requires from a certain resource, and CTest then schedules them in a way that prevents the total number of slots in use from exceeding the listed capacity. When a test is executed, and slots from a resource are allocated to that test, tests may assume that they have exclusive use of those slots for the duration of the test&#8217;s process. </p>
<p> The CTest resource allocation feature consists of two inputs:</p>
<dl>
<dt>&bull;</p>
<dd> The <i>resource specification file</i>, described below, which describes the resources available on the system.</p>
<dt>&bull;</p>
<dd> The <code>RESOURCE_GROUPS</code> property of tests, which describes the resources required by the test. </p>
<p> When CTest runs a test, the resources allocated to that test are passed in the form of a set of <i>environment variables</i> as described below. Using this information to decide which resource to connect to is left to the test writer. </p>
<p> The <code>RESOURCE_GROUPS</code> property tells CTest what resources a test expects to use grouped in a way meaningful to the test. The test itself must read the <i>environment variables</i> to determine which resources have been allocated to each group. For example, each group may correspond to a process the test will spawn when executed. </p>
<p> Note that even if a test specifies a <code>RESOURCE_GROUPS</code> property, it is still possible for that to test to run without any resource allocation (and without the corresponding <i>environment variables</i>) if the user does not pass a resource specification file. Passing this file, either through the <code>&#8211;resource-spec-file</code> command-line argument or the <code>RESOURCE_SPEC_FILE</code> argument to <code>ctest_test()</code>, is what activates the resource allocation feature. Tests should check the <code>CTEST_RESOURCE_GROUP_COUNT</code> environment variable to find out whether or not resource allocation is activated. This variable will always (and only) be defined if resource allocation is activated. If resource allocation is not activated, then the <code>CTEST_RESOURCE_GROUP_COUNT</code> variable will not exist, even if it exists for the parent <code>ctest</code> process. If a test absolutely must have resource allocation, then it can return a failing exit code or use the <code>SKIP_RETURN_CODE</code> or <code>SKIP_REGULAR_EXPRESSION</code> properties to indicate a skipped test.</dl>
<h3>Resource Specification File</h3>
<p> The resource specification file is a JSON file which is passed to CTest, either on the <i><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</i> command line as <code>&#8211;resource-spec-file</code>, or as the <code>RESOURCE_SPEC_FILE</code> argument of <code>ctest_test()</code>. If a dashboard script is used and <code>RESOURCE_SPEC_FILE</code> is not specified, the value of <code>CTEST_RESOURCE_SPEC_FILE</code> in the dashboard script is used instead. If <code>&#8211;resource-spec-file</code>, <code>RESOURCE_SPEC_FILE</code>, and <code>CTEST_RESOURCE_SPEC_FILE</code> in the dashboard script are not specified, the value of <code>CTEST_RESOURCE_SPEC_FILE</code> in the CMake build is used instead. If none of these are specified, no resource spec file is used. </p>
<p> The resource specification file must be a JSON object. All examples in this document assume the following resource specification file: </p>
<pre><code>
{
    "version" : {
        "major" : 1,
        "minor" : 0
    },
                "local" : [
                    {
                        "gpus" : [
                            {
                                "id" : "0",
                                "slots" : 2
                            },
                            {
                                "id" : "1",
                                "slots" : 4
                            },
                            {
                                "id" : "2",
                                "slots" : 2
                            },
                            {
                                "id" : "3"
                            }
                        ],
                        "crypto_chips" : [
                            {
                                "id" : "card0",
                                "slots" : 4
                            }
                        ]
                    }
                ]
}
</code></pre>
<p> The members are:</p>
<dl>
<dt><code>version</code></p>
<dd> An object containing a <code>major</code> integer field and a <code>minor</code> integer field. Currently, the only supported version is major <code>1</code>, minor <code>0</code>. Any other value is an error.</p>
<dt><code>local</code></p>
<dd> A JSON array of resource sets present on the system. Currently, this array is restricted to being of size 1. </p>
<p> Each array element is a JSON object with members whose names are equal to the desired resource types, such as <code>gpus</code>. These names must start with a lowercase letter or an underscore, and subsequent characters can be a lowercase letter, a digit, or an underscore. Uppercase letters are not allowed, because certain platforms have case-insensitive environment variables. See the <i>Environment Variables</i> section below for more information. It is recommended that the resource type name be the plural of a noun, such as <code>gpus</code> or <code>crypto_chips</code> (and not <code>gpu</code> or <code>crypto_chip</code>.) </p>
<p> Please note that the names <code>gpus</code> and <code>crypto_chips</code> are just examples, and CTest does not interpret them in any way. You are free to make up any resource type you want to meet your own requirements. </p>
<p> The value for each resource type is a JSON array consisting of JSON objects, each of which describe a specific instance of the specified resource. These objects have the following members:</p>
<dt><code>id</code></p>
<dd> A string consisting of an identifier for the resource. Each character in the identifier can be a lowercase letter, a digit, or an underscore. Uppercase letters are not allowed. </p>
<p> Identifiers must be unique within a resource type. However, they do not have to be unique across resource types. For example, it is valid to have a <code>gpus</code> resource named <code>0</code> and a <code>crypto_chips</code> resource named <code>0</code>, but not two <code>gpus</code> resources both named <code>0</code>. </p>
<p> Please note that the IDs <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, and <code>card0</code> are just examples, and CTest does not interpret them in any way. You are free to make up any IDs you want to meet your own requirements.</p>
<dt><code>slots</code></p>
<dd> An optional unsigned number specifying the number of slots available on the resource. For example, this could be megabytes of RAM on a GPU, or cryptography units available on a cryptography chip. If <code>slots</code> is not specified, a default value of <code>1</code> is assumed. </p>
<p> In the example file above, there are four GPUs with ID&#8217;s 0 through 3. GPU 0 has 2 slots, GPU 1 has 4, GPU 2 has 2, and GPU 3 has a default of 1 slot. There is also one cryptography chip with 4 slots.</dl>
<h3><code>RESOURCE_GROUPS</code> Property</h3>
<p> See <code>RESOURCE_GROUPS</code> for a description of this property.</p>
<h3>Environment Variables</h3>
<p> Once CTest has decided which resources to allocate to a test, it passes this information to the test executable as a series of environment variables. For each example below, we will assume that the test in question has a <code>RESOURCE_GROUPS</code> property of <code>2,gpus:2;gpus:4,gpus:1,crypto_chips:2</code>. </p>
<p> The following variables are passed to the test process:</p>
<dl>
<dt><code>CTEST_RESOURCE_GROUP_COUNT</code></p>
<dd> The total number of groups specified by the <code>RESOURCE_GROUPS</code> property. For example:</p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_COUNT=3</code> </p>
<p> This variable will only be defined if <i><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</i> has been given a <code>&#8211;resource-spec-file</code>, or if <code>ctest_test()</code> has been given a <code>RESOURCE_SPEC_FILE</code>. If no resource specification file has been given, this variable will not be defined.</p>
<dt><code>CTEST_RESOURCE_GROUP_&lt;num&gt;</code></p>
<dd> The list of resource types allocated to each group, with each item separated by a comma. <code>&lt;num&gt;</code> is a number from zero to <code>CTEST_RESOURCE_GROUP_COUNT</code> minus one. <code>CTEST_RESOURCE_GROUP_&lt;num&gt;</code> is defined for each <code>&lt;num&gt;</code> in this range. For example:</p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_0=gpus</code></p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_1=gpus</code></p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_2=crypto_chips,gpus</code></p>
<dt><code>CTEST_RESOURCE_GROUP_&lt;num&gt;_&lt;resource-type&gt;</code></p>
<dd> The list of resource IDs and number of slots from each ID allocated to each group for a given resource type. This variable consists of a series of pairs, each pair separated by a semicolon, and with the two items in the pair separated by a comma. The first item in each pair is <code>id:</code> followed by the ID of a resource of type <code>&lt;resource-type&gt;</code>, and the second item is <code>slots:</code> followed by the number of slots from that resource allocated to the given group. For example:</p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_0_GPUS=id:0,slots:2</code></p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_1_GPUS=id:2,slots:2</code></p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_2_GPUS=id:1,slots:4;id:3,slots:1</code></p>
<dt>&bull;</p>
<dd> <code>CTEST_RESOURCE_GROUP_2_CRYPTO_CHIPS=id:card0,slots:2</code> </p>
<p> In this example, group 0 gets 2 slots from GPU <code>0</code>, group 1 gets 2 slots from GPU <code>2</code>, and group 2 gets 4 slots from GPU <code>1</code>, 1 slot from GPU <code>3</code>, and 2 slots from cryptography chip <code>card0</code>. </p>
<p> <code>&lt;num&gt;</code> is a number from zero to <code>CTEST_RESOURCE_GROUP_COUNT</code> minus one. <code>&lt;resource-type&gt;</code> is the name of a resource type, converted to uppercase. <code>CTEST_RESOURCE_GROUP_&lt;num&gt;_&lt;resource-type&gt;</code> is defined for the product of each <code>&lt;num&gt;</code> in the range listed above and each resource type listed in <code>CTEST_RESOURCE_GROUP_&lt;num&gt;</code>. </p>
<p> Because some platforms have case-insensitive names for environment variables, the names of resource types may not clash in a case-insensitive environment. Because of this, for the sake of simplicity, all resource types must be listed in all lowercase in the <i>resource specification file</i> and in the <code>RESOURCE_GROUPS</code> property, and they are converted to all uppercase in the <code>CTEST_RESOURCE_GROUP_&lt;num&gt;_&lt;resource-type&gt;</code> environment variable.</dl>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake:</p>
<dl>
<dt><code>Home Page</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> </p>
<p> The primary starting point for learning about CMake.</p>
<dt><code>Online Documentation and Community Resources</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/documentation">https://cmake.org/documentation</a></i> </p>
<p> Links to available documentation and community resources may be found on this web page.</p>
<dt><code>Discourse Forum</code></p>
<dd> <i><a rel="nofollow" href="https://discourse.cmake.org">https://discourse.cmake.org</a></i> </p>
<p> The Discourse Forum hosts discussion and questions about CMake. </p>
<p> : <i><a rel="nofollow" href="https://cdash.org">https://cdash.org</a></i></dl>
<h2>COPYRIGHT</h2>
<p> 2000-2022 Kitware, Inc. and Contributors </p>
<h2>Index</h2>
<dt><a href="#lbBC">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBD">COPYRIGHT</a></p>
<dd></dl>
