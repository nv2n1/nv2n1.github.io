---
title: "dividendvector(3)"
name: "dividendvector"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dividendvector/"
description: "ql/cashflows/dividend.hpp – A stock dividend."
---

<p>ql/cashflows/dividend.hpp &#8211; A stock dividend. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflow.hpp&gt;<br />
 #include &lt;ql/utilities/null.hpp&gt;<br />
 #include &lt;vector&gt; </p>
<h3>Classes</h3>
<p>class <code>Dividend</code><br />
 <i>Predetermined cash flow. </i><br />
 class <code>FixedDividend</code><br />
 <i>Predetermined cash flow. </i><br />
 class <code>FractionalDividend</code><br />
 <i>Predetermined cash flow. </i></p>
<h3>Functions</h3>
<p>std::vector&lt; boost::shared_ptr&lt; Dividend &gt; &gt; <code>DividendVector</code> (const std::vector&lt; Date &gt; &amp;dividendDates, const std::vector&lt; Real &gt; &amp;dividends)<br />
 <i>helper function building a sequence of fixed dividends </i></p>
<h2>Detailed Description</h2>
<p>A stock dividend. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
