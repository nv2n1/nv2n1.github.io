---
title: "log4cppproperties(3)"
name: "log4cppproperties"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppproperties/"
description: "log4cpp::Properties –"
---

<p>log4cpp::Properties &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;Properties.hh&gt; </p>
<p> Inherits map&lt; std::string, std::string &gt;.</p>
<h3>Public Member Functions</h3>
<p><code>Properties</code> () </p>
<p> virtual <code>~Properties</code> () </p>
<p> virtual void <code>load</code> (std::istream &amp;in) </p>
<p> virtual void <code>save</code> (std::ostream &amp;out) </p>
<p> virtual int <code>getInt</code> (const std::string &amp;property, int defaultValue) </p>
<p> virtual bool <code>getBool</code> (const std::string &amp;property, bool defaultValue) </p>
<p> virtual std::string <code>getString</code> (const std::string &amp;property, const char *defaultValue) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>_substituteVariables</code> (std::string &amp;value) </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::Properties::Properties ()</h3>
<h3>log4cpp::Properties::~Properties () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::Properties::_substituteVariables (std::string &amp;value) [protected], [virtual]</h3>
<h3>bool log4cpp::Properties::getBool (const std::string &amp;property, booldefaultValue) [virtual]</h3>
<h3>int log4cpp::Properties::getInt (const std::string &amp;property, intdefaultValue) [virtual]</h3>
<h3>std::string log4cpp::Properties::getString (const std::string &amp;property, const char *defaultValue) [virtual]</h3>
<h3>void log4cpp::Properties::load (std::istream &amp;in) [virtual]</h3>
<h3>void log4cpp::Properties::save (std::ostream &amp;out) [virtual]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
