---
title: "bats(7)"
name: "bats"
section: "7"
letter: "b"
url: "/docs/linux/man/7-bats/"
description: "bats – Bats test file format"
---

<p><code>bats</code> &#8211; Bats test file format</p>
<h2>Description</h2>
<p>A Bats test file is a Bash script with special syntax for defining test cases. Under the hood, each test case is just a function with a description.</p>
<dl>
<dd>
<pre>#!/usr/bin/env bats
@test &quot;addition using bc&quot; {
 result=&quot;$(echo 2+2 | bc)&quot;
 [ &quot;$result&quot; -eq 4 ]
}
@test &quot;addition using dc&quot; {
 result=&quot;$(echo 2 2+p | dc)&quot;
 [ &quot;$result&quot; -eq 4 ]
}</pre>
<dd></dl>
<p> Each Bats test file is evaluated n+1 times, where <i>n</i> is the number of test cases in the file. The first run counts the number of test cases, then iterates over the test cases and executes each one in its own process.</p>
<h2>The Run Helper</h2>
<p>Many Bats tests need to run a command and then make assertions about its exit status and output. Bats includes a <code>run</code> helper that invokes its arguments as a command, saves the exit status and output into special global variables, and then returns with a <code>0</code> status code so you can continue to make assertions in your test case. </p>
<p> For example, let&#8217;s say you&#8217;re testing that the <code>foo</code> command, when passed a nonexistent filename, exits with a <code>1</code> status code and prints an error message.</p>
<dl>
<dd>
<pre>@test &quot;invoking foo with a nonexistent file prints an error&quot; {
 run foo nonexistent_filename
 [ &quot;$status&quot; -eq 1 ]
 [ &quot;$output&quot; = &quot;foo: no such file 'nonexistent_filename'&quot; ]
}</pre>
<dd></dl>
<p> The <code>$status</code> variable contains the status code of the command, and the <code>$output</code> variable contains the combined contents of the command&#8217;s standard output and standard error streams. </p>
<p> A third special variable, the <code>$lines</code> array, is available for easily accessing individual lines of output. For example, if you want to test that invoking <code>foo</code> without any arguments prints usage information on the first line:</p>
<dl>
<dd>
<pre>@test &quot;invoking foo without arguments prints usage&quot; {
 run foo
 [ &quot;$status&quot; -eq 1 ]
 [ &quot;${lines[0]}&quot; = &quot;usage: foo &lt;filename&gt;&quot; ]
}</pre>
<dd></dl>
<h2>The Load Command</h2>
<p>You may want to share common code across multiple test files. Bats includes a convenient <code>load</code> command for sourcing a Bash source file relative to the location of the current test file. For example, if you have a Bats test in <code>test/foo.bats</code>, the command</p>
<dl>
<dd>
<pre>load test_helper</pre>
<dd></dl>
<p> will source the script <code>test/test_helper.bash</code> in your test file. This can be useful for sharing functions to set up your environment or load fixtures.</p>
<h2>The Skip Command</h2>
<p>Tests can be skipped by using the <code>skip</code> command at the point in a test you wish to skip.</p>
<dl>
<dd>
<pre>@test &quot;A test I don't want to execute for now&quot; {
 skip
 run foo
 [ &quot;$status&quot; -eq 0 ]
}</pre>
<dd></dl>
<p> Optionally, you may include a reason for skipping:</p>
<dl>
<dd>
<pre>@test &quot;A test I don't want to execute for now&quot; {
 skip &quot;This command will return zero soon, but not now&quot;
 run foo
 [ &quot;$status&quot; -eq 0 ]
}</pre>
<dd></dl>
<p> Or you can skip conditionally:</p>
<dl>
<dd>
<pre>@test &quot;A test which should run&quot; {
 if [ foo != bar ]; then
 skip &quot;foo isn't bar&quot;
 fi
 run foo
 [ &quot;$status&quot; -eq 0 ]
}</pre>
<dd></dl>
<h2>Setup And Teardown Functions</h2>
<p>You can define special <code>setup</code> and <code>teardown</code> functions which run before and after each test case, respectively. Use these to load fixtures, set up your environment, and clean up when you&#8217;re done.</p>
<h2>Code Outside Of Test Cases</h2>
<p>You can include code in your test file outside of <code>@test</code> functions. For example, this may be useful if you want to check for dependencies and fail immediately if they&#8217;re not present. However, any output that you print in code outside of <code>@test</code>, <code>setup</code> or <code>teardown</code> functions must be redirected to <code>stderr</code> (<code>&gt;&amp;2</code>). Otherwise, the output may cause Bats to fail by polluting the TAP stream on <code>stdout</code>.</p>
<h2>Special Variables</h2>
<p>There are several global variables you can use to introspect on Bats tests:</p>
<dl>
<dt>&bull;</p>
<dd><code>$BATS_TEST_FILENAME</code> is the fully expanded path to the Bats test file.</p>
<dt>&bull;</p>
<dd><code>$BATS_TEST_DIRNAME</code> is the directory in which the Bats test file is located.</p>
<dt>&bull;</p>
<dd><code>$BATS_TEST_NAMES</code> is an array of function names for each test case.</p>
<dt>&bull;</p>
<dd><code>$BATS_TEST_NAME</code> is the name of the function containing the current test case.</p>
<dt>&bull;</p>
<dd><code>$BATS_TEST_DESCRIPTION</code> is the description of the current test case.</p>
<dt>&bull;</p>
<dd><code>$BATS_TEST_NUMBER</code> is the (1-based) index of the current test case in the test file.</p>
<dt>&bull;</p>
<dd><code>$BATS_TMPDIR</code> is the location to a directory that may be used to store temporary files.</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-bats/">bats</a></code>(1) </p>
