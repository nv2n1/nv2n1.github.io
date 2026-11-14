---
title: "travelccm-library(3)"
name: "travelccm-library"
section: "3"
letter: "t"
url: "/docs/linux/man/3-travelccm-library/"
description: "travelccm-library –"
---

<p>travelccm-library &#8211; </p>
<pre> C++ Travel Customer Choice Model Library</pre>
<h2>Synopsis</h2>
<pre><code>#include &lt;travelccm/...&gt;
</code></pre>
<h2>Description</h2>
<p>aims at providing a clean API, and the corresponding C++ implementation, for choosing one item among a set of travel solutions, given demand-related characteristics (e.g., Willingness-To-Pay, preferred airline, preferred cabin, etc.). </p>
<p> The ${PROJECT_NAME} C++ library implements some simple Customer Choice Models (CCM), as referenced in the literature (PhD dissertations at MIT, for instance: <a rel="nofollow" href="http://dspace.mit.edu">http://dspace.mit.edu</a>). </p>
<p> The ${PROJECT_NAME} C++ library exposes a simple, clean and object-oriented, API. For instance, the choose() method takes, as input, both a structure representing the travel request (e.g., from Washington, DC, US, to Beijing, China, on the 25th of May) and a list of travel solutions (as provided by the Airline Schedule Manager project: <a rel="nofollow" href="http://sourceforge.net/projects/travel-ccm">http://sourceforge.net/projects/travel-ccm</a>), and yields, as output, the chosen item. </p>
<p> The output can then be used by other systems, for instance to book the corresponding travel or to visualise it on a map and calendar and to share it with others. </p>
<p> ${PROJECT_NAME} makes an extensive use of existing open-source libraries for increased functionality, speed and accuracy. In particular the Boost (C++ Standard Extensions: <a rel="nofollow" href="http://www.boost.org)">http://www.boost.org)</a> library is used.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-travelccm/">travelccm</a>(1)</code>, <code><a href="/docs/linux/man/1-travelccm-config/">travelccm-config</a></code>(1)</p>
<h2>Support</h2>
<p>Please report any bugs to <a rel="nofollow" href="https://sourceforge.net/apps/trac/travel-ccm/report">https://sourceforge.net/apps/trac/travel-ccm/report</a></p>
<h2>Copyright</h2>
<p>Copyright © 2009-2011 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr></p>
