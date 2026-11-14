---
title: "log4cppfactoryparams(3)"
name: "log4cppfactoryparams"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppfactoryparams/"
description: "log4cpp::FactoryParams –"
---

<p>log4cpp::FactoryParams &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;FactoryParams.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef storage_t::const_iterator <code>const_iterator</code> </p>
<h3>Public Member Functions</h3>
<p>const std::string &amp; <code>operator[]</code> (const std::string &amp;v) const </p>
<p> std::string &amp; <code>operator[]</code> (const std::string &amp;v) </p>
<p> <code>details::parameter_validator</code> <code>get_for</code> (const char *tag) const </p>
<p> <code>const_iterator</code> <code>find</code> (const std::string &amp;t) const </p>
<p> <code>const_iterator</code> <code>begin</code> () const </p>
<p> <code>const_iterator</code> <code>end</code> () const </p>
<h2>Member Typedef Documentation</h2>
<h3>typedef storage_t::const_iterator <code>log4cpp::FactoryParams::const_iterator</code></h3>
<h2>Member Function Documentation</h2>
<h3><code>const_iterator</code> log4cpp::FactoryParams::begin () const [inline]</h3>
<h3><code>const_iterator</code> log4cpp::FactoryParams::end () const [inline]</h3>
<h3><code>FactoryParams::const_iterator</code> log4cpp::FactoryParams::find (const std::string &amp;t) const</h3>
<h3><code>details::parameter_validator</code> log4cpp::FactoryParams::get_for (const char *tag) const [inline]</h3>
<h3>const std::string &amp; log4cpp::FactoryParams::operator[] (const std::string &amp;v) const</h3>
<h3>std::string&amp; log4cpp::FactoryParams::operator[] (const std::string &amp;v) [inline]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
