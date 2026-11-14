---
title: "histories(3)"
name: "histories"
section: "3"
letter: "h"
url: "/docs/linux/man/3-histories/"
description: "QuantLib::IndexManager – global repository for past index fixings"
---

<h2 class="name">NAME</h2>
<p> QuantLib::IndexManager &#8211; global repository for past index fixings </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/indexes/indexmanager.hpp&gt; </p>
<p> Inherits <code>Singleton&lt; IndexManager &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p> bool <code>hasHistory</code> (const std::string &amp;name) const<br />
 <i>returns whether historical fixings were stored for the index </i><br />
 const <code>TimeSeries</code>&lt; <code>Real</code> &gt; &amp; <code>getHistory</code> (const std::string &amp;name) const<br />
 <i>returns the (possibly empty) history of the index fixings </i><br />
 void <code>setHistory</code> (const std::string &amp;name, const <code>TimeSeries</code>&lt; <code>Real</code> &gt; &amp;)<br />
 <i>stores the historical fixings of the index </i><br />
 boost::shared_ptr&lt; <code>Observable</code> &gt; <code>notifier</code> (const std::string &amp;name) const<br />
 <i>observer notifying of changes in the index fixings </i><br />
 std::vector&lt; std::string &gt; <code>histories</code> () const<br />
 <i>returns all names of the indexes for which fixings were stored </i><br />
 void <code>clearHistory</code> (const std::string &amp;name)<br />
 <i>clears the historical fixings of the index </i><br />
 void <code>clearHistories</code> ()<br />
 <i>clears all stored fixings </i></p>
<h3>Friends</h3>
<p> class <code>Singleton&lt; IndexManager &gt;</code> </p>
<h2>Detailed Description</h2>
<p> global repository for past index fixings </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> index names are case insensitive</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
