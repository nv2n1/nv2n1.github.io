---
title: "bats(1)"
name: "bats"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bats/"
description: "bats – Bash Automated Testing System"
---

<h2>NAME</h2>
<p> <code>bats</code> &#8211; Bash Automated Testing System</p>
<h2>SYNOPSIS</h2>
<p> bats [-c] [-p | -t] <i>test</i> [<i>test</i> &#8230;] </p>
<p> <i>test</i> is the path to a Bats test file, or the path to a directory containing Bats test files.</p>
<h2>DESCRIPTION</h2>
<p> Bats is a TAP-compliant testing framework for Bash. It provides a simple way to verify that the UNIX programs you write behave as expected. </p>
<p> A Bats test file is a Bash script with special syntax for defining test cases. Under the hood, each test case is just a function with a description. </p>
<p> Test cases consist of standard shell commands. Bats makes use of Bash&#8217;s <code>errexit</code> (<code>set -e</code>) option when running test cases. If every command in the test case exits with a <code>0</code> status code (success), the test passes. In this way, each line is an assertion of truth. </p>
<p> See <code><a href="/docs/linux/man/7-bats/">bats</a></code>(7) for more information on writing Bats tests.</p>
<h2>RUNNING TESTS</h2>
<p> To run your tests, invoke the <code>bats</code> interpreter with a path to a test file. The file&#8217;s test cases are run sequentially and in isolation. If all the test cases pass, <code>bats</code> exits with a <code>0</code> status code. If there are any failures, <code>bats</code> exits with a <code>1</code> status code. </p>
<p> You can invoke the <code>bats</code> interpreter with multiple test file arguments, or with a path to a directory containing multiple <code>.bats</code> files. Bats will run each test file individually and aggregate the results. If any test case fails, <code>bats</code> exits with a <code>1</code> status code.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> Count the number of test cases without running any tests</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help message</p>
<dt><code>-p</code>, <code>&#8211;pretty</code></p>
<dd> Show results in pretty format (default for terminals)</p>
<dt><code>-t</code>, <code>&#8211;tap</code></p>
<dd> Show results in TAP format</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display the version number</dl>
<h2>OUTPUT</h2>
<p> When you run Bats from a terminal, you&#8217;ll see output as each test is performed, with a check-mark next to the test&#8217;s name if it passes or an &quot;X&quot; if it fails.</p>
<dl>
<dt>
<dd>
<pre>
$ bats addition.bats
 ✓ addition using bc
 ✓ addition using dc
2 tests, 0 failures
</pre>
<dt>
<dd></dl>
<p> If Bats is not connected to a terminal&#8211;in other words, if you run it from a continuous integration system or redirect its output to a file&#8211;the results are displayed in human-readable, machine-parsable TAP format. You can force TAP output from a terminal by invoking Bats with the <code>&#8211;tap</code> option.</p>
<dl>
<dt>
<dd>
<pre>
$ bats --tap addition.bats
1..2
ok 1 addition using bc
ok 2 addition using dc
</pre>
<dt>
<dd></dl>
<h2>EXIT STATUS</h2>
<p> The <code>bats</code> interpreter exits with a value of <code>0</code> if all test cases pass, or <code>1</code> if one or more test cases fail.</p>
<h2>SEE ALSO</h2>
<p> Bats wiki: <i><a rel="nofollow" href="https://github.com/sstephenson/bats/wiki/">https://github.com/sstephenson/bats/wiki/</a></i> </p>
<p> <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/7-bats/">bats</a></code>(7)</p>
<h2>COPYRIGHT</h2>
<p> (c) 2014 Sam Stephenson </p>
<p> Bats is released under the terms of an MIT-style license. </p>
<h2>Index</h2>
