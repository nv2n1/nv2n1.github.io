---
title: "nextcode(3)"
name: "nextcode"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextcode/"
description: "QuantLib::IMM – Main cycle of the International Money Market (a.k.a. IMM) months."
---

<p>QuantLib::IMM &#8211; Main cycle of the International Money Market (a.k.a. IMM) months. </p>
<h2>Synopsis</h2>
<pre><code>enum Month { F = 1,
             G = 2,
             H = 3,
             J = 4,
             K = 5,
             M = 6,
             N = 7,
             Q = 8,
             U = 9,
             V = 10,
             X = 11,
             Z = 12 }

    Static Public Member Functions static bool
    isIMMdate(const Date &amp;d, bool mainCycle = true)

        returns whether
    or not the given date is an IMM date

       static bool isIMMcode(const std::string &amp;in, bool mainCycle = true)

           returns whether
    or not the given string is an IMM code

       static std::string code(const Date &amp;immDate)

           static Date date(const std::string &amp;immCode, const Date &amp;referenceDate = Date())

               static Date nextDate(const Date &amp;d = Date(), bool mainCycle = true)

                   next IMM date following the given date

       static Date nextDate(const std::string &amp;immCode, bool mainCycle = true, const Date &amp;referenceDate = Date())

           next IMM date following the given IMM code

       static std::string nextCode(const Date &amp;d = Date(), bool mainCycle = true)

           static std::string nextCode(const std::string &amp;immCode, bool mainCycle = true, const Date &amp;referenceDate = Date())</code></pre>
<h3>Public Types</h3>
<pre><code>enum Month { F = 1,
             G = 2,
             H = 3,
             J = 4,
             K = 5,
             M = 6,
             N = 7,
             Q = 8,
             U = 9,
             V = 10,
             X = 11,
             Z = 12 }

    Static Public Member Functions static bool
    isIMMdate(const Date &amp;d, bool mainCycle = true)

        returns whether
    or not the given date is an IMM date

       static bool isIMMcode(const std::string &amp;in, bool mainCycle = true)

           returns whether
    or not the given string is an IMM code

       static std::string code(const Date &amp;immDate)

           static Date date(const std::string &amp;immCode, const Date &amp;referenceDate = Date())

               static Date nextDate(const Date &amp;d = Date(), bool mainCycle = true)

                   next IMM date following the given date

       static Date nextDate(const std::string &amp;immCode, bool mainCycle = true, const Date &amp;referenceDate = Date())

           next IMM date following the given IMM code

       static std::string nextCode(const Date &amp;d = Date(), bool mainCycle = true)

           static std::string nextCode(const std::string &amp;immCode, bool mainCycle = true, const Date &amp;referenceDate = Date())</code></pre>
<h2>Detailed Description</h2>
<p>Main cycle of the International Money Market (a.k.a. IMM) months.</p>
<h2>Member Function Documentation</h2>
<h3>static std::string code (const <code>Date</code> &amp; immDate) [static]</h3>
<p>returns the <code>IMM</code> code for the given date (e.g. H3 for March 20th, 2013). </p>
<p> <code>Warning</code></p>
<dl>
<dd>It raises an exception if the input date is not an <code>IMM</code> date</dl>
<h3>static <code>Date</code> date (const std::string &amp; immCode, const <code>Date</code> &amp; referenceDate = <code>Date</code>()) [static]</h3>
<p>returns the <code>IMM</code> date for the given <code>IMM</code> code (e.g. March 20th, 2013 for H3). </p>
<p> <code>Warning</code></p>
<dl>
<dd>It raises an exception if the input string is not an <code>IMM</code> code</dl>
<h3>static <code>Date</code> nextDate (const <code>Date</code> &amp; d = <code>Date</code>(), bool mainCycle = true) [static]</h3>
<p>next <code>IMM</code> date following the given date </p>
<p> returns the 1st delivery date for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h3>static <code>Date</code> nextDate (const std::string &amp; immCode, bool mainCycle = true, const <code>Date</code> &amp; referenceDate = <code>Date</code>()) [static]</h3>
<p>next <code>IMM</code> date following the given <code>IMM</code> code </p>
<p> returns the 1st delivery date for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h3>static std::string nextCode (const <code>Date</code> &amp; d = <code>Date</code>(), bool mainCycle = true) [static]</h3>
<p>returns the <code>IMM</code> code for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h3>static std::string nextCode (const std::string &amp; immCode, bool mainCycle = true, const <code>Date</code> &amp; referenceDate = <code>Date</code>()) [static]</h3>
<p>returns the <code>IMM</code> code for next contract listed in the International <code>Money</code> Market section of the Chicago Mercantile Exchange.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
