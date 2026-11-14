---
title: "log4cpptimestampcomponent(3)"
name: "log4cpptimestampcomponent"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpptimestampcomponent/"
description: "log4cpp::TimeStampComponent –"
---

<p>log4cpp::TimeStampComponent &#8211; </p>
<h2>Synopsis</h2>
<p>Inherits <code>log4cpp::PatternLayout::PatternComponent</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TimeStampComponent</code> (std::string timeFormat) </p>
<p> virtual void <code>append</code> (<code>std::ostringstream</code> &amp;out, const <code>LoggingEvent</code> &amp;event) </p>
<h3>Static Public Attributes</h3>
<p>static const char *const <code>FORMAT_ISO8601</code> = &#8216;%Y-%m-%d %H:%M:%S,%l&#8217; </p>
<p> static const char *const <code>FORMAT_ABSOLUTE</code> = &#8216;%H:%M:%S,%l&#8217; </p>
<p> static const char *const <code>FORMAT_DATE</code> = &#8216;%d %b %Y %H:%M:%S,%l&#8217; </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::TimeStampComponent::TimeStampComponent (std::stringtimeFormat) [inline]</h3>
<h2>Member Function Documentation</h2>
<h3>virtual void log4cpp::TimeStampComponent::append (<code>std::ostringstream</code> &amp;out, const <code>LoggingEvent</code> &amp;event) [inline], [virtual]</h3>
<p>Implements <code>log4cpp::PatternLayout::PatternComponent</code>.</p>
<h2>Member Data Documentation</h2>
<h3>const char *const log4cpp::TimeStampComponent::FORMAT_ABSOLUTE = &#8216;%H:%M:%S,%l&#8217; [static]</h3>
<h3>const char *const log4cpp::TimeStampComponent::FORMAT_DATE = &#8216;%d %b %Y %H:%M:%S,%l&#8217; [static]</h3>
<h3>const char *const log4cpp::TimeStampComponent::FORMAT_ISO8601 = &#8216;%Y-%m-%d %H:%M:%S,%l&#8217; [static]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
