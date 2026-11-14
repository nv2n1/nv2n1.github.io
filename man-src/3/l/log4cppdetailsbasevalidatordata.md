---
title: "log4cppdetailsbasevalidatordata(3)"
name: "log4cppdetailsbasevalidatordata"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppdetailsbasevalidatordata/"
description: "log4cpp::details::base_validator_data –"
---

<p>log4cpp::details::base_validator_data &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;FactoryParams.hh&gt; </p>
<p> Inherited by <code>log4cpp::details::optional_params_validator</code>, <code>log4cpp::details::parameter_validator</code>, and <code>log4cpp::details::required_params_validator</code>.</p>
<h3>Public Member Functions</h3>
<p><code>base_validator_data</code> (const char *tag, const <code>FactoryParams</code> *params) </p>
<h3>Protected Member Functions</h3>
<p>template&lt;typename T &gt; void <code>assign</code> (const std::string &amp;param_value, T &amp;value) const </p>
<p> template&lt;typename T &gt; void <code>assign_impl</code> (const std::string &amp;param_value, T &amp;value) const </p>
<p> void <code>assign_impl</code> (const std::string &amp;param_value, std::string &amp;value) const </p>
<p> void <code>throw_error</code> (const char *param_name) const </p>
<h3>Protected Attributes</h3>
<p>const char * <code>tag_</code> </p>
<p> const <code>FactoryParams</code> * <code>params_</code> </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::details::base_validator_data::base_validator_data (const char *tag, const <code>FactoryParams</code> *params) [inline]</h3>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename T &gt; void log4cpp::details::base_validator_data::assign (const std::string &amp;param_value, T &amp;value) const [inline], [protected]</h3>
<h3>template&lt;typename T &gt; void log4cpp::details::base_validator_data::assign_impl (const std::string &amp;param_value, T &amp;value) const [inline], [protected]</h3>
<h3>void log4cpp::details::base_validator_data::assign_impl (const std::string &amp;param_value, std::string &amp;value) const [inline], [protected]</h3>
<h3>void log4cpp::details::base_validator_data::throw_error (const char *param_name) const [inline], [protected]</h3>
<h2>Member Data Documentation</h2>
<h3>const <code>FactoryParams</code>* log4cpp::details::base_validator_data::params_ [protected]</h3>
<h3>const char* log4cpp::details::base_validator_data::tag_ [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
