---
title: "log4cpppatternlayout(3)"
name: "log4cpppatternlayout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpppatternlayout/"
description: "log4cpp::PatternLayout –"
---

<p>log4cpp::PatternLayout &#8211; </p>
<p> <code>PatternLayout</code> is a simple fixed format <code>Layout</code> implementation.</p>
<h2>Synopsis</h2>
<p>#include &lt;PatternLayout.hh&gt; </p>
<p> Inherits <code>log4cpp::Layout</code>.</p>
<h3>Classes</h3>
<p>class <code>PatternComponent</code> </p>
<h3>Public Member Functions</h3>
<p><code>PatternLayout</code> () </p>
<p> virtual <code>~PatternLayout</code> () </p>
<p> virtual std::string <code>format</code> (const <code>LoggingEvent</code> &amp;event)<br />
 <i>Formats the </i><code>LoggingEvent</code> in the style set by the setConversionPattern call.<br />
 virtual void <code>setConversionPattern</code> (const std::string &amp;conversionPattern) throw (ConfigureFailure)<br />
 <i>Sets the format of log lines handled by this </i><code>PatternLayout</code>.<br />
 virtual std::string <code>getConversionPattern</code> () const </p>
<p> virtual void <code>clearConversionPattern</code> () </p>
<h3>Static Public Attributes</h3>
<p>static const char * <code>DEFAULT_CONVERSION_PATTERN</code> = &#8216;%m%n&#8217;<br />
 <i>The default conversion pattern. </i><br />
 static const char * <code>SIMPLE_CONVERSION_PATTERN</code> = &#8216;%p &#8211; %m%n&#8217;<br />
 <i>A conversion pattern equivalent to the </i><code>SimpleLayout</code>.<br />
 static const char * <code>BASIC_CONVERSION_PATTERN</code> = &#8216;%R %p %c %x: %m%n&#8217;<br />
 <i>A conversion pattern equivalent to the </i><code>BasicLayout</code>.<br />
 static const char * <code>TTCC_CONVERSION_PATTERN</code> = &#8216;%r [%t] %p %c %x &#8211; %m%n&#8217;<br />
 <i>A conversion pattern equivalent to the TTCCLayout. </i></p>
<h2>Detailed Description</h2>
<p><code>PatternLayout</code> is a simple fixed format <code>Layout</code> implementation.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::PatternLayout::PatternLayout ()</h3>
<h3>log4cpp::PatternLayout::~PatternLayout () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::PatternLayout::clearConversionPattern () [virtual]</h3>
<h3>std::string log4cpp::PatternLayout::format (const <code>LoggingEvent</code> &amp;event) [virtual]</h3>
<p>Formats the <code>LoggingEvent</code> in the style set by the setConversionPattern call. By default, set to &#8216;%%m%%n&#8217; </p>
<p> Implements <code>log4cpp::Layout</code>.</p>
<h3>std::string log4cpp::PatternLayout::getConversionPattern () const [virtual]</h3>
<h3>void log4cpp::PatternLayout::setConversionPattern (const std::string &amp;conversionPattern)<code>ConfigureFailure</code> [virtual]</h3>
<p>Sets the format of log lines handled by this <code>PatternLayout</code>. By default, set to &#8216;%%m%%n&#8217;. </p>
<p>&nbsp;<wbr>Format characters are as follows: </p>
<p>&nbsp;<wbr><code>%%</code>&nbsp;<wbr>&#8211; a single percent sign&nbsp;<wbr><code>%c</code>&nbsp;<wbr>&#8211; the category&nbsp;<wbr><code>%d</code>&nbsp;<wbr>&#8211; the date </p>
<p>&nbsp;<wbr>Date format: The date format character may be followed by a date format specifier enclosed between braces. For example,&nbsp;<wbr>%d{%H:%M:%S,%l}&nbsp;<wbr>or&nbsp;<wbr>%d{%d&nbsp;<wbr>%m&nbsp;<wbr>%Y&nbsp;<wbr>%H:%M:%S,%l}. If no date format specifier is given then the following format is used:&nbsp;<wbr>&#8216;Wed Jan 02 02:03:55 1980&#8217;. The date format specifier admits the same syntax as the ANSI C function strftime, with 1 addition. The addition is the specifier&nbsp;<wbr>%l for milliseconds, padded with zeros to make 3 digits.&nbsp;<wbr><code>%m</code>&nbsp;<wbr>&#8211; the message&nbsp;<wbr><code>%n</code>&nbsp;<wbr>&#8211; the platform specific line separator&nbsp;<wbr><code>%p</code>&nbsp;<wbr>&#8211; the priority&nbsp;<wbr><code>%r</code>&nbsp;<wbr>&#8211; milliseconds since this layout was created.&nbsp;<wbr><code>%R</code>&nbsp;<wbr>&#8211; seconds since Jan 1, 1970&nbsp;<wbr><code>%u</code>&nbsp;<wbr>&#8211; clock ticks since process start&nbsp;<wbr><code>%x</code>&nbsp;<wbr>&#8211; the&nbsp;<wbr><code>NDC</code>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>conversionPattern</i> the conversion pattern</dl>
<p> <code>Exceptions:</code></p>
<dl COMPACT>
<dd><i></i><code>ConfigureFailure</code> if the pattern is invalid</dl>
<h2>Member Data Documentation</h2>
<h3>const char * log4cpp::PatternLayout::BASIC_CONVERSION_PATTERN = &#8216;%R %p %c %x: %m%n&#8217; [static]</h3>
<p>A conversion pattern equivalent to the <code>BasicLayout</code>.</p>
<h3>const char * log4cpp::PatternLayout::DEFAULT_CONVERSION_PATTERN = &#8216;%m%n&#8217; [static]</h3>
<p>The default conversion pattern.</p>
<h3>const char * log4cpp::PatternLayout::SIMPLE_CONVERSION_PATTERN = &#8216;%p &#8211; %m%n&#8217; [static]</h3>
<p>A conversion pattern equivalent to the <code>SimpleLayout</code>.</p>
<h3>const char * log4cpp::PatternLayout::TTCC_CONVERSION_PATTERN = &#8216;%r [%t] %p %c %x &#8211; %m%n&#8217; [static]</h3>
<p>A conversion pattern equivalent to the TTCCLayout. Note: TTCCLayout is in log4j but not <code>log4cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
