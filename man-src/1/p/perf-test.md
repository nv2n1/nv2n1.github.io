---

title: "perf-test(1)"
name: "perf-test"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-test/"
---

perf-test - Runs sanity tests. 

<pre><code>
perf test[&lt;options&gt;][{list&lt;test - name - fragment&gt; | [&lt;test - name - fragments&gt; | &lt;test - numbers&gt;]}]
</code></pre>

This command does assorted sanity tests, initially through linked routines but also will look for a directory with more tests in the form of scripts. 

 To get a list of available tests use <i>perf test list</i>, specifying a test name fragment will show all tests that have it. 

 To run just specific tests, inform test name fragments or the numbers obtained from <i>perf test list</i>.

<h2>OPTIONS</h2>

 

 -s, --skip
<dl>
<dt>
</dt><dd> Tests to skip (comma separated numeric list).</dd></dl>
 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be more verbose.</dd></dl>
