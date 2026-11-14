---
title: "quantlib_dategeneration(3)"
name: "quantlib_dategeneration"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dategeneration/"
description: "QuantLib::DateGeneration – Date-generation rule."
---

<p>QuantLib::DateGeneration &#8211; Date-generation rule. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/dategenerationrule.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Rule</code> { <code>Backward</code>, <code>Forward</code>, <code>Zero</code>, <code>ThirdWednesday</code>, <code>Twentieth</code>, <code>TwentiethIMM</code> } </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, <code>DateGeneration::Rule</code>) </p>
<h2>Detailed Description</h2>
<p>Date-generation rule. </p>
<p> These conventions specify the rule used to generate dates in a <code>Schedule</code>.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Rule</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Backward </i></p>
<dd>Backward from termination date to effective date.</p>
<dt><i>Forward </i></p>
<dd><code>Forward</code> from effective date to termination date.</p>
<dt><i>Zero </i></p>
<dd>No intermediate dates between effective date and termination date.</p>
<dt><i>ThirdWednesday </i></p>
<dd>All dates but effective date and termination date are taken to be on the third wednesday of their month (with forward calculation.)</p>
<dt><i>Twentieth </i></p>
<dd>All dates but the effective date are taken to be the twentieth of their month (used for CDS schedules in emerging markets.) The termination date is also modified.</p>
<dt><i>TwentiethIMM </i></p>
<dd>All dates but the effective date are taken to be the twentieth of an <code>IMM</code> month (used for CDS schedules.) The termination date is also modified.</dl>
<h2>Friends And Related Function Documentation</h2>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, <code>DateGeneration::Rule</code>) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
