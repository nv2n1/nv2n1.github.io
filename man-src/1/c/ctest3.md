---
title: "ctest3(1)"
name: "ctest3"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctest3/"
description: "ctest – CTest Command-Line Reference"
---

<h2>NAME</h2>
<p> ctest &#8211; CTest Command-Line Reference</p>
<h2>SYNOPSIS</h2>
<pre>
ctest3 [&lt;options&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> The &quot;ctest3&quot; executable is the CMake test driver program. CMake-generated build trees created for projects that use the ENABLE_TESTING and ADD_TEST commands have testing support. This program will run the tests and report results.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C &lt;cfg&gt;, &#8211;build-config &lt;cfg&gt;</code></p>
<dd> Choose configuration to test. </p>
<p> Some CMake-generated build trees can have multiple build configurations in the same tree. This option can be used to specify which one should be tested. Example configurations are &quot;Debug&quot; and &quot;Release&quot;.</p>
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
<dd> Output anything outputted by the test program if the test should fail. This option can also be enabled by setting the environment variable <code>CTEST_OUTPUT_ON_FAILURE</code>.</p>
<dt><code>-F</code></p>
<dd> Enable failover. </p>
<p> This option allows ctest to resume a test set execution that was previously interrupted. If no interruption occurred, the -F option will have no effect.</p>
<dt><code>-j &lt;jobs&gt;, &#8211;parallel &lt;jobs&gt;</code></p>
<dd> Run the tests in parallel using the given number of jobs. </p>
<p> This option tells ctest to run the tests in parallel using given number of jobs. This option can also be set by setting the environment variable <code>CTEST_PARALLEL_LEVEL</code>.</p>
<dt><code>&#8211;test-load &lt;level&gt;</code></p>
<dd> While running tests in parallel (e.g. with <code>-j</code>), try not to start tests when they may cause the CPU load to pass above a given threshold. </p>
<p> When <code>ctest3</code> is run as a <i>Dashboard Client</i> this sets the <code>TestLoad</code> option of the <i>CTest Test Step</i>.</p>
<dt><code>-Q,&#8211;quiet</code></p>
<dd> Make ctest quiet. </p>
<p> This option will suppress all the output. The output log file will still be generated if the &#8211;output-log is specified. Options such as &#8211;verbose, &#8211;extra-verbose, and &#8211;debug are ignored if &#8211;quiet is specified.</p>
<dt><code>-O &lt;file&gt;, &#8211;output-log &lt;file&gt;</code></p>
<dd> Output to log file </p>
<p> This option tells ctest to write all its output to a log file.</p>
<dt><code>-N,&#8211;show-only</code></p>
<dd> Disable actual execution of tests. </p>
<p> This option tells ctest to list the tests that would be run but not actually run them. Useful in conjunction with the -R and -E options.</p>
<dt><code>-L &lt;regex&gt;, &#8211;label-regex &lt;regex&gt;</code></p>
<dd> Run tests with labels matching regular expression. </p>
<p> This option tells ctest to run only the tests whose labels match the given regular expression.</p>
<dt><code>-R &lt;regex&gt;, &#8211;tests-regex &lt;regex&gt;</code></p>
<dd> Run tests matching regular expression. </p>
<p> This option tells ctest to run only the tests whose names match the given regular expression.</p>
<dt><code>-E &lt;regex&gt;, &#8211;exclude-regex &lt;regex&gt;</code></p>
<dd> Exclude tests matching regular expression. </p>
<p> This option tells ctest to NOT run the tests whose names match the given regular expression.</p>
<dt><code>-LE &lt;regex&gt;, &#8211;label-exclude &lt;regex&gt;</code></p>
<dd> Exclude tests with labels matching regular expression. </p>
<p> This option tells ctest to NOT run the tests whose labels match the given regular expression.</p>
<dt><code>-D &lt;dashboard&gt;, &#8211;dashboard &lt;dashboard&gt;</code></p>
<dd> Execute dashboard test </p>
<p> This option tells ctest to act as a CDash client and perform a dashboard test. All tests are &lt;Mode&gt;&lt;Test&gt;, where Mode can be Experimental, Nightly, and Continuous, and Test can be Start, Update, Configure, Build, Test, Coverage, and Submit.</p>
<dt><code>-D &lt;var&gt;:&lt;type&gt;=&lt;value&gt;</code></p>
<dd> Define a variable for script mode </p>
<p> Pass in variable values on the command line. Use in conjunction with -S to pass variable values to a dashboard script. Parsing -D arguments as variable values is only attempted if the value following -D does not match any of the known dashboard types.</p>
<dt><code>-M &lt;model&gt;, &#8211;test-model &lt;model&gt;</code></p>
<dd> Sets the model for a dashboard </p>
<p> This option tells ctest to act as a CDash client where the TestModel can be Experimental, Nightly, and Continuous. Combining -M and -T is similar to -D</p>
<dt><code>-T &lt;action&gt;, &#8211;test-action &lt;action&gt;</code></p>
<dd> Sets the dashboard action to perform </p>
<p> This option tells ctest to act as a CDash client and perform some action such as start, build, test etc. Combining -M and -T is similar to -D</p>
<dt><code>&#8211;track &lt;track&gt;</code></p>
<dd> Specify the track to submit dashboard to </p>
<p> Submit dashboard to specified track instead of default one. By default, the dashboard is submitted to Nightly, Experimental, or Continuous track, but by specifying this option, the track can be arbitrary.</p>
<dt><code>-S &lt;script&gt;, &#8211;script &lt;script&gt;</code></p>
<dd> Execute a dashboard for a configuration </p>
<p> This option tells ctest to load in a configuration script which sets a number of parameters such as the binary and source directories. Then ctest will do what is required to create and run a dashboard. This option basically sets up a dashboard and then runs ctest3 -D with the appropriate options.</p>
<dt><code>-SP &lt;script&gt;, &#8211;script-new-process &lt;script&gt;</code></p>
<dd> Execute a dashboard for a configuration </p>
<p> This option does the same operations as -S but it will do them in a separate process. This is primarily useful in cases where the script may modify the environment and you do not want the modified environment to impact other -S scripts.</p>
<dt><code>-A &lt;file&gt;, &#8211;add-notes &lt;file&gt;</code></p>
<dd> Add a notes file with submission </p>
<p> This option tells ctest to include a notes file when submitting dashboard.</p>
<dt><code>-I [Start,End,Stride,test#,test#|Test file], &#8211;tests-information</code></p>
<dd> Run a specific number of tests by number. </p>
<p> This option causes ctest to run tests starting at number Start, ending at number End, and incrementing by Stride. Any additional numbers after Stride are considered individual test numbers. Start, End,or stride can be empty. Optionally a file can be given that contains the same syntax as the command line.</p>
<dt><code>-U, &#8211;union</code></p>
<dd> Take the Union of -I and -R </p>
<p> When both -R and -I are specified by default the intersection of tests are run. By specifying -U the union of tests is run instead.</p>
<dt><code>&#8211;rerun-failed</code></p>
<dd> Run only the tests that failed previously </p>
<p> This option tells ctest to perform only the tests that failed during its previous run. When this option is specified, ctest ignores all other options intended to modify the list of tests to run (-L, -R, -E, -LE, -I, etc). In the event that CTest runs and no tests fail, subsequent calls to ctest3 with the &#8211;rerun-failed option will run the set of tests that most recently failed (if any).</p>
<dt><code>&#8211;repeat-until-fail &lt;n&gt;</code></p>
<dd> Require each test to run <code>&lt;n&gt;</code> times without failing in order to pass. </p>
<p> This is useful in finding sporadic failures in test cases.</p>
<dt><code>&#8211;max-width &lt;width&gt;</code></p>
<dd> Set the max width for a test name to output </p>
<p> Set the maximum width for each test name to show in the output. This allows the user to widen the output to avoid clipping the test name which can be very annoying.</p>
<dt><code>&#8211;interactive-debug-mode [0|1]</code></p>
<dd> Set the interactive mode to 0 or 1. </p>
<p> This option causes ctest to run tests in either an interactive mode or a non-interactive mode. On Windows this means that in non-interactive mode, all system debug pop up windows are blocked. In dashboard mode (Experimental, Nightly, Continuous), the default is non-interactive. When just running tests not for a dashboard the default is to allow popups and interactive debugging.</p>
<dt><code>&#8211;no-label-summary</code></p>
<dd> Disable timing summary information for labels. </p>
<p> This option tells ctest not to print summary information for each label associated with the tests run. If there are no labels on the tests, nothing extra is printed.</p>
<dt><code>&#8211;build-and-test</code></p>
<dd> Configure, build and run a test. </p>
<p> This option tells ctest to configure (i.e. run cmake on), build, and or execute a test. The configure and test steps are optional. The arguments to this command line are the source and binary directories. By default this will run CMake on the Source/Bin directories specified unless &#8211;build-nocmake is specified. The &#8211;build-generator option <i>must</i> be provided to use &#8211;build-and-test. If &#8211;test-command is specified then that will be run after the build is complete. Other options that affect this mode are &#8211;build-target &#8211;build-nocmake, &#8211;build-run-dir, &#8211;build-two-config, &#8211;build-exe-dir, &#8211;build-project,&#8211;build-noclean, &#8211;build-options</p>
<dt><code>&#8211;build-target</code></p>
<dd> Specify a specific target to build. </p>
<p> This option goes with the &#8211;build-and-test option, if left out the all target is built.</p>
<dt><code>&#8211;build-nocmake</code></p>
<dd> Run the build without running cmake first. </p>
<p> Skip the cmake step.</p>
<dt><code>&#8211;build-run-dir</code></p>
<dd> Specify directory to run programs from. </p>
<p> Directory where programs will be after it has been compiled.</p>
<dt><code>&#8211;build-two-config</code></p>
<dd> Run CMake twice</p>
<dt><code>&#8211;build-exe-dir</code></p>
<dd> Specify the directory for the executable.</p>
<dt><code>&#8211;build-generator</code></p>
<dd> Specify the generator to use.</p>
<dt><code>&#8211;build-generator-platform</code></p>
<dd> Specify the generator-specific platform.</p>
<dt><code>&#8211;build-generator-toolset</code></p>
<dd> Specify the generator-specific toolset.</p>
<dt><code>&#8211;build-project</code></p>
<dd> Specify the name of the project to build.</p>
<dt><code>&#8211;build-makeprogram</code></p>
<dd> Override the make program chosen by CTest with a given one.</p>
<dt><code>&#8211;build-noclean</code></p>
<dd> Skip the make clean step.</p>
<dt><code>&#8211;build-config-sample</code></p>
<dd> A sample executable to use to determine the configuration </p>
<p> A sample executable to use to determine the configuration that should be used. e.g. Debug/Release/etc</p>
<dt><code>&#8211;build-options</code></p>
<dd> Add extra options to the build step. </p>
<p> This option must be the last option with the exception of &#8211;test-command</p>
<dt><code>&#8211;test-command</code></p>
<dd> The test to run with the &#8211;build-and-test option.</p>
<dt><code>&#8211;test-output-size-passed &lt;size&gt;</code></p>
<dd> Limit the output for passed tests to &lt;size&gt; bytes.</p>
<dt><code>&#8211;test-output-size-failed &lt;size&gt;</code></p>
<dd> Limit the output for failed tests to &lt;size&gt; bytes.</p>
<dt><code>&#8211;test-timeout</code></p>
<dd> The time limit in seconds, internal use only.</p>
<dt><code>&#8211;tomorrow-tag</code></p>
<dd> Nightly or experimental starts with next day tag. </p>
<p> This is useful if the build will not finish in one day.</p>
<dt><code>&#8211;ctest-config</code></p>
<dd> The configuration file used to initialize CTest state when submitting dashboards. </p>
<p> This option tells CTest to use different initialization file instead of CTestConfiguration.tcl. This way multiple initialization files can be used for example to submit to multiple dashboards.</p>
<dt><code>&#8211;overwrite</code></p>
<dd> Overwrite CTest configuration option. </p>
<p> By default ctest uses configuration options from configuration file. This option will overwrite the configuration option.</p>
<dt><code>&#8211;extra-submit &lt;file&gt;[;&lt;file&gt;]</code></p>
<dd> Submit extra files to the dashboard. </p>
<p> This option will submit extra files to the dashboard.</p>
<dt><code>&#8211;force-new-ctest-process</code></p>
<dd> Run child CTest instances as new processes </p>
<p> By default CTest will run child CTest instances within the same process. If this behavior is not desired, this argument will enforce new processes for child CTest processes.</p>
<dt><code>&#8211;schedule-random</code></p>
<dd> Use a random order for scheduling tests </p>
<p> This option will run the tests in a random order. It is commonly used to detect implicit dependencies in a test suite.</p>
<dt><code>&#8211;submit-index</code></p>
<dd> Legacy option for old Dart2 dashboard server feature. Do not use.</p>
<dt><code>&#8211;timeout &lt;seconds&gt;</code></p>
<dd> Set a global timeout on all tests. </p>
<p> This option will set a global timeout on all tests that do not already have a timeout set on them.</p>
<dt><code>&#8211;stop-time &lt;time&gt;</code></p>
<dd> Set a time at which all tests should stop running. </p>
<p> Set a real time of day at which all tests should timeout. Example: 7:00:00 -0400. Any time format understood by the curl date parser is accepted. Local time is assumed if no timezone is specified.</p>
<dt><code>&#8211;http1.0</code></p>
<dd> Submit using HTTP 1.0. </p>
<p> This option will force CTest to use HTTP 1.0 to submit files to the dashboard, instead of HTTP 1.1.</p>
<dt><code>&#8211;no-compress-output</code></p>
<dd> Do not compress test output when submitting. </p>
<p> This flag will turn off automatic compression of test output. Use this to maintain compatibility with an older version of CDash which doesn&#8217;t support compressed test output.</p>
<dt><code>&#8211;print-labels</code></p>
<dd> Print all available test labels. </p>
<p> This option will not run any tests, it will simply print the list of all labels associated with the test set.</p>
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
<h2>DASHBOARD CLIENT</h2>
<p> CTest can operate as a client for the <i>CDash</i> software quality dashboard application. As a dashboard client, CTest performs a sequence of steps to configure, build, and test software, and then submits the results to a <i>CDash</i> server.</p>
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
<p> CTest can perform testing on an already-generated build tree. Run the <code>ctest3</code> command with the current working directory set to the build tree and use one of these signatures: </p>
<pre><code>
ctest3 - D&lt;mode&gt;[&lt;step&gt;] ctest3 - M&lt;mode&gt;[-T&lt;step&gt;]...
</code></pre>
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
<p> CTest can perform testing driven by a <code><a href="/docs/linux/man/7-cmake3-language/">cmake3-language</a>(7)</code> script that creates and maintains the source and build tree as well as performing the testing steps. Run the <code>ctest3</code> command with the current working directory set outside of any build tree and use one of these signatures: </p>
<pre>
ctest3 -S &lt;script&gt;
ctest3 -SP &lt;script&gt;
</pre>
<p> The <code>&lt;script&gt;</code> file must call <i>CTest Commands</i> commands to run testing steps explicitly as documented below. The commands obtain <i>Dashboard Client Configuration</i> settings from their arguments or from variables set in the script.</p>
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
<p> The source tree is updated by <code>git fetch</code> followed by <code>git reset &#8211;hard</code> to the <code>FETCH_HEAD</code>. The result is the same as <code>git pull</code> except that any local moficiations are overwritten. Use <code>GITUpdateCustom</code> to specify a different approach.</p>
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
<dd> <i>CTest Script</i> variable: <code>CTEST_UPDATE_VERSION_ONLY</code> </p>
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
<dd> <code>CTest</code> module variable: <code>CMAKE_COMMAND</code> followed by <code>PROJECT_SOURCE_DIR</code></dl>
<h3>CTest Build Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_build()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
<dt><code>DefaultCTestConfigurationType</code></p>
<dd> When the build system to be launched allows build-time selection of the configuration (e.g. <code>Debug</code>, <code>Release</code>), this specifies the default configuration to be built when no <code>-C</code> option is given to the <code>ctest3</code> command. The value will be substituted into the value of <code>MakeCommand</code> to replace the literal string <code>${CTEST_CONFIGURATION_TYPE}</code> if it appears.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_CONFIGURATION_TYPE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DEFAULT_CTEST_CONFIGURATION_TYPE</code>, initialized by the <code>CMAKE_CONFIG_TYPE</code> environment variable</p>
<dt><code>MakeCommand</code></p>
<dd> Command-line to launch the software build process. It will be executed in the location specified by the <code>BuildDirectory</code> setting.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_BUILD_COMMAND</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>MAKECOMMAND</code>, initialized by the <code>build_command()</code> command</p>
<dt><code>UseLaunchers</code></p>
<dd> For build trees generated by CMake using one of the <i>Makefile Generators</i> or the <code>Ninja</code> generator, specify whether the <code>CTEST_USE_LAUNCHERS</code> feature is enabled by the <code>CTestUseLaunchers</code> module (also included by the <code>CTest</code> module). When enabled, the generated build system wraps each invocation of the compiler, linker, or custom command line with a &quot;launcher&quot; that communicates with CTest via environment variables and files to report granular build warning and error information. Otherwise, CTest must &quot;scrape&quot; the build output log for diagnostics.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_USE_LAUNCHERS</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_USE_LAUNCHERS</code></dl>
<h3>CTest Test Step</h3>
<p> In a <i>CTest Script</i>, the <code>ctest_test()</code> command runs this step. Arguments to the command may specify some of the step settings. </p>
<p> Configuration settings include:</p>
<dl>
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
<dd> <code>CTest</code> module variable: <code>DART_TESTING_TIMEOUT</code></dl>
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
<dd> <code>CTest</code> module variable: <code>COVERAGE_EXTRA_FLAGS</code></dl>
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
<dd> <code>CTest</code> module variable: <code>VALGRIND_COMMAND_OPTIONS</code></dl>
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
<dd> Specify the version of <i>CDash</i> on the server.</p>
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
<dd> The path on the dashboard server to send the submission.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_LOCATION</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_LOCATION</code> if set, else <code>CTEST_DROP_LOCATION</code></p>
<dt><code>DropMethod</code></p>
<dd> Specify the method by which results should be submitted to the dashboard server. The value may be <code>cp</code>, <code>ftp</code>, <code>http</code>, <code>https</code>, <code>scp</code>, or <code>xmlrpc</code> (if CMake was built with support for it).</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_METHOD</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_METHOD</code> if set, else <code>CTEST_DROP_METHOD</code></p>
<dt><code>DropSite</code></p>
<dd> The dashboard server name (for <code>ftp</code>, <code>http</code>, and <code>https</code>, <code>scp</code>, and <code>xmlrpc</code>).</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_SITE</code> if set, else <code>CTEST_DROP_SITE</code></p>
<dt><code>DropSitePassword</code></p>
<dd> The dashboard server login password, if any (for <code>ftp</code>, <code>http</code>, and <code>https</code>).</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE_PASSWORD</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_SITE_PASSWORD</code> if set, else <code>CTEST_DROP_SITE_PASWORD</code></p>
<dt><code>DropSiteUser</code></p>
<dd> The dashboard server login user name, if any (for <code>ftp</code>, <code>http</code>, and <code>https</code>).</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE_USER</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>DROP_SITE_USER</code> if set, else <code>CTEST_DROP_SITE_USER</code></p>
<dt><code>IsCDash</code></p>
<dd> Specify whether the dashboard server is <i>CDash</i> or an older dashboard server implementation requiring <code>TriggerSite</code>.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_DROP_SITE_CDASH</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>CTEST_DROP_SITE_CDASH</code></p>
<dt><code>ScpCommand</code></p>
<dd> <code>scp</code> command-line tool to use when <code>DropMethod</code> is <code>scp</code>.</p>
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
<dt><code>TriggerSite</code></p>
<dd> Legacy option to support older dashboard server implementations. Not used when <code>IsCDash</code> is true.</p>
<dt>&bull;</p>
<dd> <i>CTest Script</i> variable: <code>CTEST_TRIGGER_SITE</code></p>
<dt>&bull;</p>
<dd> <code>CTest</code> module variable: <code>TRIGGER_SITE</code> if set, else <code>CTEST_TRIGGER_SITE</code></dl>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake:</p>
<dl>
<dt><code>Home Page</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> </p>
<p> The primary starting point for learning about CMake.</p>
<dt><code>Frequently Asked Questions</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/Wiki/CMake_FAQ">https://cmake.org/Wiki/CMake_FAQ</a></i> </p>
<p> A Wiki is provided containing answers to frequently asked questions.</p>
<dt><code>Online Documentation</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/documentation">https://cmake.org/documentation</a></i> </p>
<p> Links to available documentation may be found on this web page.</p>
<dt><code>Mailing List</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/mailing-lists">https://cmake.org/mailing-lists</a></i> </p>
<p> For help and discussion about using cmake, a mailing list is provided at <i>cmake [at] cmake.org</i>. The list is member-post-only but one may sign up on the CMake web page. Please first read the full documentation at <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> before posting questions to the list.</dl>
<h2>COPYRIGHT</h2>
<p> 2000-2016 Kitware, Inc. </p>
<h2>Index</h2>
