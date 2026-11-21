---
title: "gtester(1)"
name: "gtester"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtester/"
description: "gtester – test running utility"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtester</code> [OPTION&#8230;] [testprogram]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gtester</code></p>
<dd>is a utility to run unit tests that have been written using the GLib test framework. </dd>
<p> Since GLib 2.62, <code>gtester-report</code> is deprecated. Use TAP for reporting test results instead, and feed it to the test harness provided by your build system. </p>
<p> When called with the <code>-o</code> option, <code>gtester</code> writes an XML report of the test results, which can be converted into HTML using the <code>gtester-report</code> utility.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> print help and exit</dd></dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> print version information and exit</dd></dl>
<p> <code>&#8211;g-fatal-warnings</code></p>
<dl>
<dt>
</dt><dd> make warnings fatal</dd></dl>
<p> <code>-k</code>, <code>&#8211;keep-going</code></p>
<dl>
<dt>
</dt><dd> continue running after tests failed</dd></dl>
<p> <code>-l</code></p>
<dl>
<dt>
</dt><dd> list paths of available test cases</dd></dl>
<p> <code>-m=</code><i>MODE</i></p>
<dl>
<dt>
</dt><dd> run test cases in <i>MODE</i>, which can be one of: </dd>
<p> <code>perf</code></p>
<dl>
<dt>
</dt><dd> run performance tests</dd></dl>
<p> <code>slow</code>, <code>thorough</code></p>
<dl>
<dt>
</dt><dd> run slow tests, or repeat non-deterministic tests more often</dd></dl>
<p> <code>quick</code></p>
<dl>
<dt>
</dt><dd> do not run slow or performance tests, or do extra repeats of non-deterministic tests (default)</dd></dl>
<p> <code>undefined</code></p>
<dl>
<dt>
</dt><dd> run test cases that deliberately provoke checks or assertion failures, if implemented (default)</dd></dl>
<p> <code>no-undefined</code></p>
<dl>
<dt>
</dt><dd> do not run test cases that deliberately provoke checks or assertion failures</dd></dl>
</dl>
<p> <code>-p=</code><i>TESTPATH</i></p>
<dl>
<dt>
</dt><dd> only run test cases matching <i>TESTPATH</i></dd></dl>
<p> <code>-s=</code><i>TESTPATH</i></p>
<dl>
<dt>
</dt><dd> skip test cases matching <i>TESTPATH</i></dd></dl>
<p> <code>&#8211;seed=</code><i>SEEDSTRING</i></p>
<dl>
<dt>
</dt><dd> run all test cases with random number seed <i>SEEDSTRING</i></dd></dl>
<p> <code>-o=</code><i>LOGFILE</i></p>
<dl>
<dt>
</dt><dd> write the test log to <i>LOGFILE</i></dd></dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
</dt><dd> suppress per test binary output</dd></dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> report success per testcase</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtester-report/">gtester-report</a></code>(1) </p>
