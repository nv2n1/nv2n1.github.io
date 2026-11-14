---
title: "nitrate-notes(1)"
name: "nitrate-notes"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nitrate-notes/"
description: "Release Notes – python-nitrate release notes"
---

<h2>NAME</h2>
<p> Release Notes &#8211; python-nitrate release notes</p>
<h2>PYTHON-NITRATE 1.0</h2>
<p> There have been many substantial changes in the python-nitrate implementation and a bunch of new features have been added. Many thanks to Filip Holec for contributing substantial part of the new caching implementation. Here&#8217;s the summary of important changes: </p>
<p> Improved Performance</p>
<dl>
<dt>&bull;</p>
<dd> Common caching support for all Nitrate classes</p>
<dt>&bull;</p>
<dd> Persistent cache implementation, MultiCall support</p>
<dt>&bull;</p>
<dd> Cache().update() support for multicall slicing</p>
<dt>&bull;</p>
<dd> Experimental support for fetching data from Teiid </p>
<p> New Object Attributes</p>
<dt>&bull;</p>
<dd> TestPlan.owner attribute holding the default owner</p>
<dt>&bull;</p>
<dd> TestPlan.sortkey() for getting/setting test case order</p>
<dt>&bull;</p>
<dd> TestRun.testcases for easy iteration over linked cases</p>
<dt>&bull;</p>
<dd> TestRun.started and TestRun.finished timestamps</p>
<dt>&bull;</p>
<dd> TestCase.created for accessing the creation date </p>
<p> Other Features</p>
<dt>&bull;</p>
<dd> Huge api module refactored into several modules</p>
<dt>&bull;</p>
<dd> New utility functions header() and sliced() added</p>
<dt>&bull;</p>
<dd> Support for colored logging, new custom log levels</p>
<dt>&bull;</p>
<dd> Plain authentication supported in addition to Kerberos</p>
<dt>&bull;</p>
<dd> Improved man pages, module documentation and examples </p>
<p> Under the Hood</p>
<dt>&bull;</p>
<dd> The big cleanup of ininitialization and caching</p>
<dt>&bull;</p>
<dd> TestPlan.testruns reimplemented using PlanRuns container</p>
<dt>&bull;</p>
<dd> TestRun.caseruns and TestRun.testcases containers</p>
<dt>&bull;</p>
<dd> Test case containers iterate over sorted test cases</p>
<dt>&bull;</p>
<dd> Bugs reimplemented with containers and caching</p>
<dt>&bull;</p>
<dd> Store the initial object dict as _inject for future use </p>
<p> Test Suite</p>
<dt>&bull;</p>
<dd> New unit test cases implemented, many improved</p>
<dt>&bull;</p>
<dd> Added support for performance tests (&#8211;performance)</p>
<dt>&bull;</p>
<dd> Overall test summary printed at the end of testing </p>
<p> API Changes </p>
<p> Several backward-incompatible changes had to be introduced in order to improve the performance and because of necessary cleanup. Below you can find the list of differences in the module API. </p>
<p> Object id cannot be provided as string: </p>
<pre>
− TestCase(&quot;1234&quot;)
+ TestCase(1234)
</pre>
<p> Tags are now regular objects and should be used instead of strings (although for adding/removing and presence checking backward compatiblity is silently preserved): </p>
<pre>
− testcase.tags.add(&quot;TestParametrized&quot;)
+ testcase.tags.add(Tag(&quot;TestParametrized&quot;))
− &quot;TestParametrized&quot; in testcase.tags
+ Tag(&quot;TestParametrized&quot;) in testcase.tags
</pre>
<p> Default version has been moved from Product into TestPlan class. Placing the default product version inside the Product class was by mistake. The TestPlan class has been adjusted by adding a new attribute &#8216;version&#8217; as this is the proper place for this data: </p>
<pre>
− Product(name=&quot;Fedora&quot;, version=&quot;20)
+ Product(name=&quot;Fedora&quot;)
+ Product(&quot;Fedora&quot;)
</pre>
<p> This is also why <code>version</code> is now a required field when creating a new test plan: </p>
<pre>
− TestPlan(name=N, product=P, type=T)
+ TestPlan(name=N, product=P, version=V, type=T)
</pre>
<p> Long-ago obsoleted functions for setting log level, cache level and coloring mode were removed, all log level constants are now directly available in the main module: </p>
<pre>
− setLogLevel(log.DEBUG)
+ set_log_level(LOG_DEBUG)
− setColorMode(COLOR_OFF)
+ set_color_mode(COLOR_OFF)
− setCacheLevel(CACHE_PERSISTENT)
+ set_cache_level(CACHE_PERSISTENT)
</pre>
<p> Utility function color() does not reflect the current color mode automatically. Instead, new parameter &#8216;enabled&#8217; should be used to disable the coloring when desired, for example: </p>
<pre>
color(&quot;txt&quot;, color=&quot;red&quot;, enabled=config.Coloring().enabled())
</pre>
</dl>
<h2>Index</h2>
