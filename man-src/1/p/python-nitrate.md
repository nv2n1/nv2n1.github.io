---
title: "python-nitrate(1)"
name: "python-nitrate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-python-nitrate/"
---

<h2>NAME</h2>

 python-nitrate - Python API for the Nitrate test case management system

<h2>DESCRIPTION</h2>

 

 python-nitrate is a Python interface to the Nitrate test case management system. The package consists of a high-level Python module (provides natural object interface), a low-level driver (allows to directly access Nitrate's xmlrpc API) and a command line interpreter (useful for fast debugging and experimenting).

<h2>FEATURES</h2>

 

 Among the most essential python-nitrate features are:
<dl>
<dt>&bull;
<dd> Natural and concise Python interface
<dt>&bull;
<dd> Custom level of caching &amp; logging
<dt>&bull;
<dd> Automated status coloring
<dt>&bull;
<dd> Integrated test suite
<dt>&bull;
<dd> Utility functions 

 The main motivation was to hide unnecessary implementation details wherever possible so that using the API is as concise as possible. 

 Scripts importing python-nitrate can make use of several useful helper functions including info() for logging to stderr, listed() which converts list into nice human readable form, color() for coloring and of course log.{debug,info,warn,error} for logging.</dl>

<h2>EXAMPLES</h2>

 

 Initialize or create an object: 

 <pre>
testcase = TestCase(1234)
testrun = TestRun(testplan=&lt;plan&gt;, summary=&lt;summary&gt;)
</pre> 

 Default iterators provided for all container objects: 

 <pre><code>
for
case in TestRun(1234):
    if
    case.automated:
    case.status = Status("RUNNING") case.update()
</code></pre> 

 Linking case to a plan is as simple as adding an item to a set: 

 <pre>
testplan.testcases.add(testcase)
testplan.update()
</pre> 

 However, it's still possible to use the low-level driver when a specific features is not implemented yet or not efficient enough: 

 <pre>
inject = Nitrate()._server.TestCase.get(46490)
</pre> 

 For a quick start you can get some inspiration in the examples directory. The 'matrix.py' script demonstrates how to easily display a matrix view of the test run results for a specific test plan. The 'create.py' script gives a broader overview covering object creation, attribute setting, adjusting logs and caching.

<h2>INSTALLATION</h2>

 

 Install directly from Fedora/Copr repository using yum or dnf: 

 <pre>
yum install python-nitrate
</pre> 

 or use PIP (sudo required if not in a virtualenv): 

 <pre>
pip install nitrate
</pre> 

 Note that for successfull pip installation several extra dependencies are necessary: 

 <pre>
yum install gcc krb5-devel python-devel postgresql-devel
</pre>

<h2>CONFIGURATION</h2>

 

 To be able to contact the Nitrate server a minimal user config file ~/.nitrate has to be provided in the user home directory: 

 <pre>
[nitrate]
url = <a rel="nofollow" HREF="https://nitrate.server/xmlrpc/">https://nitrate.server/xmlrpc/</a>
</pre>

<h2>TEST SUITE</h2>

 

 The high-level interface has an integrated test suite, which can be easily run against a stage server instance. For this a couple of objects needs to be prepared and already existing on the server so that we can check valid results. For detailed information about what data has to be prepared see the module documentation.

<h2>LINKS</h2>

 

 Project page: <i><a rel="nofollow" HREF="https://github.com/psss/python-nitrate">https://github.com/psss/python-nitrate</a></i> 

 Download: <i><a rel="nofollow" HREF="https://github.com/psss/python-nitrate/releases">https://github.com/psss/python-nitrate/releases</a></i> 

 Copr repo: <i><a rel="nofollow" HREF="http://copr.fedoraproject.org/coprs/psss/python-nitrate/">http://copr.fedoraproject.org/coprs/psss/python-nitrate/</a></i> 

 PyPI: <i><a rel="nofollow" HREF="https://pypi.python.org/pypi/nitrate">https://pypi.python.org/pypi/nitrate</a></i> 

 File bugs: <i><a rel="nofollow" HREF="https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora">https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora</a>&amp;component=python-nitrate</i> 

 Nitrate: <i><a rel="nofollow" HREF="https://fedorahosted.org/nitrate/">https://fedorahosted.org/nitrate/</a></i>

<h2>SEE ALSO</h2>

 

 Manual pages covering command line interpreter and release notes: 

 <pre>
nitrate
nitrate-notes
</pre> 

 For more detailed and most up-to-date description of all available nitrate module features see the Python online documentation: 

 <pre>
pydoc nitrate
</pre> 

 For area-specific details see respective module documentation: 

 <pre>
nitrate.base ......... Nitrate class, search support
nitrate.cache ........ Persistent cache, multicall support
nitrate.config ....... Configuration, logging, coloring, caching
nitrate.containers ... Container classes implementation
nitrate.immutable .... Immutable Nitrate objects
nitrate.mutable ...... Mutable Nitrate objects
nitrate.teiid ........ Teiid support
nitrate.tests ........ Test suite
nitrate.utils ........ Utilities
nitrate.xmlrpc ....... XMLRPC driver
</pre>

<h2>AUTHORS</h2>

 

 High-level Python module: Petr Šplíchal, Zbyšek Mráz, Martin Kyral, Lukáš Zachar, Filip Holec, Aleš Zelinka, Miroslav Vadkerti, Leoš Pol and Iveta Wiedermann. 

 Low-level XMLRPC driver: Airald Hapairai, David Malcolm, Will Woods, Bill Peck, Chenxiong Qi, Tang Chaobin, Yuguang Wang and Xuqing Kuang. 

 Hope, the library will save you time and bring some joy when writing scripts interacting with the Nitrate server. Looking forward to your feedback, comments, suggestions and patches ;-) 

 Petr Šplíchal &lt;<i>psplicha [at] redhat.com</i>&gt;

<h2>COPYRIGHT</h2>

 

 Copyright (c) 2012 Red Hat, Inc. All rights reserved. 

 This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. 

<h2>Index</h2>


