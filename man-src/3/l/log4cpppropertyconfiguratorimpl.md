---
title: "log4cpppropertyconfiguratorimpl(3)"
name: "log4cpppropertyconfiguratorimpl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpppropertyconfiguratorimpl/"
description: "log4cpp::PropertyConfiguratorImpl –"
---

<p>log4cpp::PropertyConfiguratorImpl &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;PropertyConfiguratorImpl.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef std::map&lt; std::string,<br />
 <code>Appender</code> * &gt; <code>AppenderMap</code>&quot; </p>
<h3>Public Member Functions</h3>
<p><code>PropertyConfiguratorImpl</code> () </p>
<p> virtual <code>~PropertyConfiguratorImpl</code> () </p>
<p> virtual void <code>doConfigure</code> (const std::string &amp;initFileName) throw (ConfigureFailure) </p>
<p> virtual void <code>doConfigure</code> (std::istream &amp;in) throw (ConfigureFailure) </p>
<h3>Protected Member Functions</h3>
<p>void <code>configureCategory</code> (const std::string &amp;categoryname) throw (ConfigureFailure)<br />
 <i>configure the given category. </i><br />
 void <code>getCategories</code> (std::vector&lt; std::string &gt; &amp;categories) const<br />
 <i>Get a list of categories for which we should do the configuration. </i><br />
 void <code>instantiateAllAppenders</code> () throw (ConfigureFailure) </p>
<p> <code>Appender</code> * <code>instantiateAppender</code> (const std::string &amp;name)<br />
 <i>Intantiate and configure the appender referred to by the given name. </i><br />
 void <code>setLayout</code> (<code>Appender</code> *appender, const std::string &amp;name)<br />
 <i>Method for instantiating and configuring the layouts associated with each appender. </i></p>
<h3>Protected Attributes</h3>
<p><code>Properties</code> <code>_properties</code> </p>
<p> <code>AppenderMap</code> <code>_allAppenders</code> </p>
<h2>Member Typedef Documentation</h2>
<h3>typedef std::map&lt;std::string, <code>Appender</code>*&gt; <code>log4cpp::PropertyConfiguratorImpl::AppenderMap</code></h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::PropertyConfiguratorImpl::PropertyConfiguratorImpl ()</h3>
<h3>log4cpp::PropertyConfiguratorImpl::~PropertyConfiguratorImpl () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::PropertyConfiguratorImpl::configureCategory (const std::string &amp;categoryname)<code>ConfigureFailure</code> [protected]</h3>
<p>configure the given category. This includes setting its <code>Priority</code> and adding any Appenders. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>setting other properties like &#8216;additivity&#8217;.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>categoryname</i> Name of the category to configure. The name &#8216;rootCategory&#8217; refers to the root <code>Category</code>. throw <code>ConfigureFailure</code></dl>
<h3>void log4cpp::PropertyConfiguratorImpl::doConfigure (const std::string &amp;initFileName)<code>ConfigureFailure</code> [virtual]</h3>
<h3>void log4cpp::PropertyConfiguratorImpl::doConfigure (std::istream &amp;in)<code>ConfigureFailure</code> [virtual]</h3>
<h3>void log4cpp::PropertyConfiguratorImpl::getCategories (std::vector&lt; std::string &gt; &amp;categories) const [protected]</h3>
<p>Get a list of categories for which we should do the configuration. Get the categories contained within the map of properties. </p>
<p> This simply extracts the categories from the map. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>categories</i> Reference to a list which is to receive the list of categories.</dl>
<p> Since the category looks something like &#8216;category.xxxxx.yyy.zzz&#8217;, we need to search the entire map to figure out which properties are category listings. Seems like there might be a more elegant solution.</p>
<h3>void log4cpp::PropertyConfiguratorImpl::instantiateAllAppenders ()<code>ConfigureFailure</code> [protected]</h3>
<h3><code>Appender</code> * log4cpp::PropertyConfiguratorImpl::instantiateAppender (const std::string &amp;name) [protected]</h3>
<p>Intantiate and configure the appender referred to by the given name. This method searches the map to find all configuration parameters for the appender, and adds the appender to the given category. This isn&#8217;t very general in the sense that it will need to be modified for each type of appender and layout. A more general solution would be to define an &#8216;options&#8217; interface for each appender and layout, so that we can simply call this method with a list of options instead of needing to know what is or is not available. This would also require some generic way of instantiating an object for which we have no knowledge. An &#8216;AppenderFactory&#8217; could be used which maps the given type to an actual object class registered with the factory (?? is this possible?). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> String containing the name of the type of appender to be instantiated.</dl>
<h3>void log4cpp::PropertyConfiguratorImpl::setLayout (<code>Appender</code> *appender, const std::string &amp;name) [protected]</h3>
<p>Method for instantiating and configuring the layouts associated with each appender. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>appender</i> <code>Appender</code> to which we are setting this layout.<br />
 <i>name</i> Name in the properties of this appender.</dl>
<h2>Member Data Documentation</h2>
<h3><code>AppenderMap</code> log4cpp::PropertyConfiguratorImpl::_allAppenders [protected]</h3>
<h3><code>Properties</code> log4cpp::PropertyConfiguratorImpl::_properties [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
