---
title: "yearfraction(3)"
name: "yearfraction"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yearfraction/"
description: "QuantLib::DayCounter – day counter class"
---

<p>QuantLib::DayCounter &#8211; day counter class </p>
<h2>Synopsis</h2>
<pre><code>bool empty () const


Returns whether or not the day counter is initialized.


std::string name () const


Returns the name of the day counter.


BigInteger dayCount (const Date &amp;, const Date &amp;) const


Returns the number of days between two dates.


Time yearFraction (const Date &amp;, const Date &amp;, const Date &amp;refPeriodStart=Date(), const Date &amp;refPeriodEnd=Date()) const


Returns the period between two dates as a fraction of year.




Protected Member Functions</code></pre>
<p> Inherited by <code>Actual360</code>, <code>Actual365Fixed</code>, <code>ActualActual</code>, <code>Business252</code>, <code>OneDayCounter</code>, <code>SimpleDayCounter</code>, and <code>Thirty360</code>.</p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>abstract base class for day counter implementations </i></p>
<h3>Public Member Functions</h3>
<p><code>DayCounter</code> ()<br />
 <code>DayCounter interface</code> </p>
<pre><code>bool empty () const


Returns whether or not the day counter is initialized.


std::string name () const


Returns the name of the day counter.


BigInteger dayCount (const Date &amp;, const Date &amp;) const


Returns the number of days between two dates.


Time yearFraction (const Date &amp;, const Date &amp;, const Date &amp;refPeriodStart=Date(), const Date &amp;refPeriodEnd=Date()) const


Returns the period between two dates as a fraction of year.




Protected Member Functions</code></pre>
<p> <code>DayCounter</code> (const boost::shared_ptr&lt; <code>Impl</code> &gt; &amp;impl)</p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code></p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 bool <code>operator==</code> (const <code>DayCounter</code> &amp;, const <code>DayCounter</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>DayCounter</code> &amp;, const <code>DayCounter</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>DayCounter</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>day counter class </p>
<p> This class provides methods for determining the length of a time period according to given market convention, both as a number of days and as a year fraction. </p>
<p> The Bridge pattern is used to provide the base behavior of the day counter. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>FRA.cpp</code>, <code>Replication.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>DayCounter</code> (const boost::shared_ptr&lt; <code>Impl</code> &gt; &amp; impl) [protected]</h3>
<p>This constructor can be invoked by derived classes which define a given implementation.</p>
<h3><code>DayCounter</code> ()</h3>
<p>The default constructor returns a day counter with a null implementation, which is therefore unusable except as a placeholder.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const</h3>
<p>Returns the name of the day counter. </p>
<p> <code>Warning</code></p>
<dl>
<dd>This method is used for output and comparison between day counters. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>DayCounter</code> &amp;, const <code>DayCounter</code> &amp;) [related]</h3>
<p>Returns true iff the two day counters belong to the same derived class.</p>
<h3>bool operator!= (const <code>DayCounter</code> &amp;, const <code>DayCounter</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>DayCounter</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
