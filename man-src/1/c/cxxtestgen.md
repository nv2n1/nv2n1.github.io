---

title: "cxxtestgen(1)"
name: "cxxtestgen"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cxxtestgen/"
description: "cxxtestgen – performs test discovery to create a CxxTest test runner"
---

<p> cxxtestgen [options] [&lt;filename&gt; &#8230;]</p>
<p> The cxxtestgen command processes C++ header files to perform test discovery, and then it creates files for the CxxTest test runner.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
</dt><dd> show this help message and exit</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Write the CxxTest version.</dd></dl>
<p> <code>-o, &#8211;output</code>=<i>NAME</i></p>
<dl>
<dt>
</dt><dd> Write output to file NAME.</dd></dl>
<p> <code>-w, &#8211;world</code></p>
<dl>
<dt>
</dt><dd> The label of the tests, used to name the XML results.</dd></dl>
<p> <code>&#8211;include</code>=<i>HEADER</i></p>
<dl>
<dt>
</dt><dd> Include file HEADER in the test runner before other headers.</dd></dl>
<p> <code>&#8211;abort-on-fail</code></p>
<dl>
<dt>
</dt><dd> Abort tests on failed asserts (like xUnit).</dd></dl>
<p> <code>&#8211;main</code></p>
<dl>
<dt>
</dt><dd> Specify an alternative name for the main() function.</dd></dl>
<p> <code>&#8211;headers</code></p>
<dl>
<dt>
</dt><dd> Specify a filename that contains a list of header files that are processed to generate a test runner.</dd></dl>
<p> <code>&#8211;runner</code>=<i>CLASS</i></p>
<dl>
<dt>
</dt><dd> Create a test runner that processes test events using the class CxxTest::CLASS.</dd></dl>
<p> <code>&#8211;gui</code>=<i>CLASS</i></p>
<dl>
<dt>
</dt><dd> Create a GUI test runner that processes test events using the class CxxTest::CLASS. (deprecated)</dd></dl>
<p> <code>&#8211;error-printer</code></p>
<dl>
<dt>
</dt><dd> Create a test runner using the ErrorPrinter class, and allow the use of the standard library.</dd></dl>
<p> <code>&#8211;xunit-printer</code></p>
<dl>
<dt>
</dt><dd> Create a test runner using the XUnitPrinter class.</dd></dl>
<p> <code>&#8211;xunit-file</code></p>
<dl>
<dt>
</dt><dd> The file to which the XML summary is written for test runners using the XUnitPrinter class. The default XML filename is TEST-&lt;world&gt;.xml, where &lt;world&gt; is the value of the &#8211;world option. (default: cxxtest)</dd></dl>
<p> <code>&#8211;have-std</code></p>
<dl>
<dt>
</dt><dd> Use the standard library (even if not found in tests).</dd></dl>
<p> <code>&#8211;no-std</code></p>
<dl>
<dt>
</dt><dd> Do not use standard library (even if found in tests).</dd></dl>
<p> <code>&#8211;have-eh</code></p>
<dl>
<dt>
</dt><dd> Use exception handling (even if not found in tests).</dd></dl>
<p> <code>&#8211;no-eh</code></p>
<dl>
<dt>
</dt><dd> Do not use exception handling (even if found in tests).</dd></dl>
<p> <code>&#8211;longlong</code>=<i>TYPE</i></p>
<dl>
<dt>
</dt><dd> Use TYPE as for long long integers. (default: not supported)</dd></dl>
<p> <code>&#8211;no-static-init</code></p>
<dl>
<dt>
</dt><dd> Do not rely on static initialization in the test runner.</dd></dl>
<p> <code>&#8211;template</code>=<i>TEMPLATE</i></p>
<dl>
<dt>
</dt><dd> Generate the test runner using file TEMPLATE to define a template.</dd></dl>
<p> <code>&#8211;root</code></p>
<dl>
<dt>
</dt><dd> Write the main() function and global data for a test runner.</dd></dl>
<p> <code>&#8211;part</code></p>
<dl>
<dt>
</dt><dd> Write the tester classes for a test runner.</dd></dl>
<p> <code>-f, &#8211;fog-parser</code></p>
<dl>
<dt>
</dt><dd> Use new FOG C++ parser (disabled)</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
</dt><dd> Success</dd></dl>
<p> <code>1</code></p>
<dl>
<dt>
</dt><dd> Failure (syntax or usage error; configuration error; document processing failure; unexpected error).</dd></dl>
<h2>BUGS</h2>
<p> See the CxxTest Home Page for the link to the CxxTest ticket repository.</p>
<h2>AUTHOR</h2>
<p> CxxTest was originally written by Erez Volk. Many people have contributed to it.</p>
<h2>RESOURCES</h2>
<p> Home page: <a rel="nofollow" href="http://cxxtest.com/">http://cxxtest.com/</a> </p>
<p> CxxTest User Guide: <a rel="nofollow" href="http://cxxtest.com/cxxtest/doc/guide.html">http://cxxtest.com/cxxtest/doc/guide.html</a></p>
<h2>COPYING</h2>
<p> Copyright (c) 2008 Sandia Corporation. This software is distributed under the Lesser GNU General Public License (LGPL) v3 </p>
