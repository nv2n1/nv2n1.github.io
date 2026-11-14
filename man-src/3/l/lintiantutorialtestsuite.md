---
title: "lintiantutorialtestsuite(3)"
name: "lintiantutorialtestsuite"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiantutorialtestsuite/"
description: "Lintian::Tutorial::TestSuite — Quick intro to running the Lintian testsuite"
---

<p>Lintian::Tutorial::TestSuite &#8212; Quick intro to running the Lintian testsuite </p>
<h2>Synopsis</h2>
<p>Warning: This document may be out of date. </p>
<p> This guide will quickly introduce you to running the Lintian test suite and some tricks. The Lintian test suite is fairly large and accordingly it can take a substantial amount of time to run. To speed up development, there are various options to limit the tests to run. </p>
<p> If you are looking for a guide on how to write tests, please consult Lintian::Tutorial::WritingTests.</p>
<h2>Description</h2>
<p>The Lintian test suite is an extensive collection of various test cases. The test suite is divided into 4 &#8220;sub-suites&#8221;. The majority of tests are currently located in the &#8220;tests&#8221; sub-suite. </p>
<p> To run the full suite: </p>
<pre> $ rm -rf debian/test-out; t/bin/build-test-packages; t/bin/runtests</pre>
<p>While writing a new tag (or check) you probably only want to run a particular (subset of the) test(s). See &#8220;Running a subset of the tests&#8221; for the available options.</p>
<h3>Running a subset of the tests</h3>
<p>First, you have to build the test packages with: </p>
<pre> $ rm -rf debian/test-out; t/bin/build-test-packages;</pre>
<p>Then, the following options are available:</p>
<dl COMPACT>
<dt>Running a single test</p>
<dd>To run a single test by its name, use: </p>
<pre> $ t/bin/runtests --onlyrun=test:$name</pre>
<dt>Running all tests for a check</p>
<dd>To run all tests for a given check, use: </p>
<pre> $ t/bin/runtests --onlyrun=check:$name</pre>
<p><tt>$check</tt> must be the name of a check (it will test for checks/$check.desc) or &#8220;legacy&#8221;. This will run all tests that start with &#8220;$check-&#8221;.</p>
<dt>Running all tests designed for a specific tag</p>
<dd>To run all tests that have a &#8220;Test-For&#8221; or a &#8220;Test-Against&#8221; for a given tag, use: </p>
<pre> $ t/bin/runtests --onlyrun=tag:$name</pre>
</dl>
<h3>Running tests under coverage</h3>
<p>This feature is currently untested. </p>
<p> It is possible to run most of the tests under Devel::Cover. This is done by passing <i>&#8211;coverage</i> to <i>t/bin/runtests</i>. Example: </p>
<pre> $ t/bin/runtests --coverage --dump-logs -j1 -k t debian/test-out</pre>
<p>Please note that Devel::Cover does not seem to handle multiple threads too well. You may see spurious warnings/errors if you run the tests with 2 or more active worker threads. </p>
<p> <code>Caveat</code> 1: Coverage for collections (i.e. programs in <i>collection/</i>) does not seem to work at the moment. Therefore, they often end up with (next to) zero coverage in the generated reports. </p>
<p> <code>Caveat</code> 2: Devel::Cover sometimes changes the output of Lintian or tools called by Lintian. Obviously, this leads to test failures. Therefore, you may see weird test failures (or warnings) when running under coverage. </p>
<p> <i>Collecting the coverage you want in a reasonable time</i> </p>
<p> Collecting coverage is excruciatingly slow. This is not helped by the fact that it becomes unreliable when run under 2 or more threads. </p>
<p> Fortunately, Devel::Cover &#8220;appends&#8221; to its cover database. This allows you to &#8220;slowly&#8221; build up the coverage database over multiple runs. Example: </p>
<pre> $ t/bin/runtests --coverage --dump-logs -j1 -k t debian/test-out suite:scripts
 $ t/bin/runtests --coverage --dump-logs -j1 -k t debian/test-out suite:debs
 $ t/bin/runtests --coverage --dump-logs -j1 -k t debian/test-out suite:source
 ...</pre>
<p>Or: </p>
<pre> $ t/bin/runtests --coverage --dump-logs -j1 -k t debian/test-out $check
 $ t/bin/runtests --coverage --dump-logs -j1 -k t debian/test-out legacy</pre>
<h2>See Also</h2>
<p>Lintian::Tutorial::WritingTests</p>
