---
title: "log4cpppatternlayoutpatterncomponent(3)"
name: "log4cpppatternlayoutpatterncomponent"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpppatternlayoutpatterncomponent/"
description: "log4cpp::PatternLayout::PatternComponent –"
---

<p>log4cpp::PatternLayout::PatternComponent &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;PatternLayout.hh&gt; </p>
<p> Inherited by <code>log4cpp::CategoryNameComponent</code>, <code>log4cpp::FormatModifierComponent</code>, <code>log4cpp::MessageComponent</code>, <code>log4cpp::MillisSinceEpochComponent</code>, <code>log4cpp::NDCComponent</code>, <code>log4cpp::PriorityComponent</code>, <code>log4cpp::ProcessorTimeComponent</code>, <code>log4cpp::SecondsSinceEpochComponent</code>, <code>log4cpp::StringLiteralComponent</code>, <code>log4cpp::ThreadNameComponent</code>, and <code>log4cpp::TimeStampComponent</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~PatternComponent</code> () </p>
<p> virtual void <code>append</code> (<code>std::ostringstream</code> &amp;out, const <code>LoggingEvent</code> &amp;event)=0 </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>virtual log4cpp::PatternLayout::PatternComponent::~PatternComponent () [inline], [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>virtual void log4cpp::PatternLayout::PatternComponent::append (<code>std::ostringstream</code> &amp;out, const <code>LoggingEvent</code> &amp;event) [pure virtual]</h3>
<p>Implemented in <code>log4cpp::FormatModifierComponent</code>, <code>log4cpp::MillisSinceEpochComponent</code>, <code>log4cpp::SecondsSinceEpochComponent</code>, <code>log4cpp::TimeStampComponent</code>, <code>log4cpp::ProcessorTimeComponent</code>, <code>log4cpp::ThreadNameComponent</code>, <code>log4cpp::PriorityComponent</code>, <code>log4cpp::NDCComponent</code>, <code>log4cpp::MessageComponent</code>, <code>log4cpp::CategoryNameComponent</code>, and <code>log4cpp::StringLiteralComponent</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
