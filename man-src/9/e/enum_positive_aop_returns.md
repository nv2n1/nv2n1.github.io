---
title: "enum_positive_aop_returns(9)"
name: "enum_positive_aop_returns"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_positive_aop_returns/"
description: "enum_positive_aop_returns – aop return codes with specific semantics"
---

<p>enum_positive_aop_returns &#8211; aop return codes with specific semantics</p>
<h2>Synopsis</h2>
<pre>enum positive_aop_returns {
 AOP_WRITEPAGE_ACTIVATE,
 AOP_TRUNCATED_PAGE
}; </pre>
<h2>Constants</h2>
<p>AOP_WRITEPAGE_ACTIVATE</p>
<dl>
<dd>Informs the caller that page writeback has completed, that the page is still locked, and should be considered active. The VM uses this hint to return the page to the active list &#8212; it won&#8217;t be a candidate for writeback again in the near future. Other callers must be careful to unlock the page if they get this return. Returned by <code>writepage</code>;</dl>
<p> AOP_TRUNCATED_PAGE</p>
<dl>
<dd>The AOP method that was handed a locked page has unlocked it and the page might have been truncated. The caller should back up to acquiring a new page and trying again. The aop will be taking reasonable precautions not to livelock. If the caller held a page reference, it should drop it before retrying. Returned by <code>readpage</code>.</dl>
<h2>Description</h2>
<p>address_space_operation functions return these large constants to indicate special semantics to the caller. These are much larger than the bytes in a page to allow for functions that return the number of bytes operated on in a given page.</p>
<h2>Copyright</h2>
