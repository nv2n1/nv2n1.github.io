---
title: "singleton_settings(3)"
name: "singleton_settings"
section: "3"
letter: "s"
url: "/docs/linux/man/3-singleton_settings/"
description: "QuantLib::Settings – global repository for run-time library settings"
---

<p>QuantLib::Settings &#8211; global repository for run-time library settings </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/settings.hpp&gt; </p>
<p> Inherits <code>Singleton&lt; Settings &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>DateProxy &amp; <code>evaluationDate</code> ()<br />
 <i>the date at which pricing is to be performed. </i><br />
 const DateProxy &amp; <code>evaluationDate</code> () const </p>
<p> bool &amp; <code>enforcesTodaysHistoricFixings</code> () </p>
<p> bool <code>enforcesTodaysHistoricFixings</code> () const </p>
<h3>Friends</h3>
<p>class <code>Singleton&lt; Settings &gt;</code> </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const DateProxy &amp;) </p>
<h2>Detailed Description</h2>
<p>global repository for run-time library settings</p>
<h2>Member Function Documentation</h2>
<h3>DateProxy&amp; evaluationDate ()</h3>
<p>the date at which pricing is to be performed. </p>
<p> Client code can inspect the evaluation date, as in: </p>
<pre> Date d = Settings::instance().evaluationDate();</pre>
<p>&nbsp;<wbr>where today&#8217;s date is returned if the evaluation date is set to the null date&nbsp;<wbr>(its default value;)&nbsp;<wbr>can set it to a new value, as in:&nbsp;<wbr> </p>
<pre> Settings::instance().evaluationDate() = d;</pre>
<p>&nbsp;<wbr>and can register with it, as in:&nbsp;<wbr> </p>
<pre> registerWith(Settings::instance().evaluationDate());</pre>
<p>&nbsp;<wbr>to be notified when it is set to a new value.&nbsp;<wbr> </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>a notification is not sent when the evaluation date changes for natural causes&#8212;i.e., a date was not explicitly set (which results in today&#8217;s date being used for pricing) and the current date changes as the clock strikes midnight.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
