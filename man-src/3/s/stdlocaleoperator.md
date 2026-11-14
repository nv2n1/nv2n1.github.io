---
title: "stdlocaleoperator(3)"
name: "stdlocaleoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaleoperator/"
description: "std::locale::operator==,operator!= – std::locale::operator==,operator!="
---

<p>std::locale::operator==,operator!= &#8211; std::locale::operator==,operator!=</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
bool operator==( const locale&amp; other ) const; <code>(1)</code><br />
bool operator!=( const locale&amp; other ) const; <code>(2)</code><br />
Tests two locales for equality. Named locales are considered equal if their names are equal. Unnamed locales are considered equal if they are copies of each other. </p>
<h2>Parameters</h2>
<p>other &#8211; a std::locale object to compare</p>
<h2>Return value</h2>
<p>1) true if other is a copy of *this or has an identical name, false otherwise.<br />
2) false if other is a copy of *this or has an identical name, true otherwise. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new locale<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the name of the locale or &quot;*&quot; if unnamed<br />
name <i>(public member function)</i> </p>
