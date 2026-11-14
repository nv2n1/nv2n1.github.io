---
title: "quantlib_exchangeratemanager(3)"
name: "quantlib_exchangeratemanager"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_exchangeratemanager/"
description: "QuantLib::ExchangeRateManager – exchange-rate repository"
---

<p>QuantLib::ExchangeRateManager &#8211; exchange-rate repository </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/currencies/exchangeratemanager.hpp&gt; </p>
<p> Inherits <code>Singleton&lt; ExchangeRateManager &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>add</code> (const <code>ExchangeRate</code> &amp;, const <code>Date</code> &amp;startDate=Date::minDate(), const <code>Date</code> &amp;endDate=Date::maxDate())<br />
 <i>Add an exchange rate. </i><br />
 <code>ExchangeRate</code> <code>lookup</code> (const <code>Currency</code> &amp;source, const <code>Currency</code> &amp;target, <code>Date</code> date=<code>Date</code>(), <code>ExchangeRate::Type</code> type=ExchangeRate::Derived) const </p>
<p> void <code>clear</code> ()<br />
 <i>remove the added exchange rates </i></p>
<h3>Friends</h3>
<p>class <code>Singleton&lt; ExchangeRateManager &gt;</code> </p>
<h2>Detailed Description</h2>
<p>exchange-rate repository </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>lookup of direct, triangulated, and derived exchange rates is tested.</dl>
<h2>Member Function Documentation</h2>
<h3>void add (const <code>ExchangeRate</code> &amp;, const <code>Date</code> &amp; startDate = Date::minDate(), const <code>Date</code> &amp; endDate = Date::maxDate())</h3>
<p>Add an exchange rate. </p>
<p> The given rate is valid between the given dates. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If two rates are given between the same currencies and with overlapping date ranges, the latest one added takes precedence during lookup.</dl>
<h3><code>ExchangeRate</code> lookup (const <code>Currency</code> &amp; source, const <code>Currency</code> &amp; target, <code>Date</code> date = <code>Date</code>(), <code>ExchangeRate::Type</code> type = ExchangeRate::Derived) const</h3>
<p>Lookup the exchange rate between two currencies at a given date. If the given type is Direct, only direct exchange rates will be returned if available; if Derived, direct rates are still preferred but derived rates are allowed. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>if two or more exchange-rate chains are possible which allow to specify a requested rate, it is unspecified which one is returned.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
