---
title: "log4cpphierarchymaintainer(3)"
name: "log4cpphierarchymaintainer"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpphierarchymaintainer/"
description: "log4cpp::HierarchyMaintainer –"
---

<p>log4cpp::HierarchyMaintainer &#8211; </p>
<p> <code>HierarchyMaintainer</code> is an internal <code>log4cpp</code> class.</p>
<h2>Synopsis</h2>
<p>#include &lt;HierarchyMaintainer.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef std::map&lt; std::string,<br />
 <code>Category</code> * &gt; <code>CategoryMap</code>&quot; </p>
<p> typedef void(* <code>shutdown_fun_ptr</code> )() </p>
<h3>Public Member Functions</h3>
<p><code>HierarchyMaintainer</code> () </p>
<p> virtual <code>~HierarchyMaintainer</code> () </p>
<p> virtual <code>Category</code> * <code>getExistingInstance</code> (const std::string &amp;name) </p>
<p> virtual <code>Category</code> &amp; <code>getInstance</code> (const std::string &amp;name) </p>
<p> virtual std::vector&lt; <code>Category</code> * &gt; * <code>getCurrentCategories</code> () const </p>
<p> virtual void <code>shutdown</code> () </p>
<p> void <code>register_shutdown_handler</code> (<code>shutdown_fun_ptr</code> handler) </p>
<p> virtual void <code>deleteAllCategories</code> () </p>
<h3>Static Public Member Functions</h3>
<p>static <code>HierarchyMaintainer</code> &amp; <code>getDefaultMaintainer</code> () </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Category</code> * <code>_getExistingInstance</code> (const std::string &amp;name) </p>
<p> virtual <code>Category</code> &amp; <code>_getInstance</code> (const std::string &amp;name) </p>
<h3>Protected Attributes</h3>
<p><code>CategoryMap</code> <code>_categoryMap</code> </p>
<p> <code>threading::Mutex</code> <code>_categoryMutex</code> </p>
<h3>Friends</h3>
<p>class <code>Log4cppCleanup</code> </p>
<h2>Detailed Description</h2>
<p><code>HierarchyMaintainer</code> is an internal <code>log4cpp</code> class. </p>
<p> It is responsible for maintaining the hierarchy of Categories. Applications should not have to use this class directly.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef std::map&lt;std::string, <code>Category</code>*&gt; <code>log4cpp::HierarchyMaintainer::CategoryMap</code></h3>
<h3>typedef void(* log4cpp::HierarchyMaintainer::shutdown_fun_ptr)()</h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::HierarchyMaintainer::HierarchyMaintainer ()</h3>
<h3>log4cpp::HierarchyMaintainer::~HierarchyMaintainer () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3><code>Category</code> * log4cpp::HierarchyMaintainer::_getExistingInstance (const std::string &amp;name) [protected], [virtual]</h3>
<h3><code>Category</code> &amp; log4cpp::HierarchyMaintainer::_getInstance (const std::string &amp;name) [protected], [virtual]</h3>
<h3>void log4cpp::HierarchyMaintainer::deleteAllCategories () [virtual]</h3>
<h3>std::vector&lt; <code>Category</code> * &gt; * log4cpp::HierarchyMaintainer::getCurrentCategories () const [virtual]</h3>
<h3><code>HierarchyMaintainer</code> &amp; log4cpp::HierarchyMaintainer::getDefaultMaintainer () [static]</h3>
<h3><code>Category</code> * log4cpp::HierarchyMaintainer::getExistingInstance (const std::string &amp;name) [virtual]</h3>
<h3><code>Category</code> &amp; log4cpp::HierarchyMaintainer::getInstance (const std::string &amp;name) [virtual]</h3>
<h3>void log4cpp::HierarchyMaintainer::register_shutdown_handler (<code>shutdown_fun_ptr</code>handler)</h3>
<h3>void log4cpp::HierarchyMaintainer::shutdown () [virtual]</h3>
<h2>Friends And Related Function Documentation</h2>
<h3>friend class Log4cppCleanup [friend]</h3>
<h2>Member Data Documentation</h2>
<h3><code>CategoryMap</code> log4cpp::HierarchyMaintainer::_categoryMap [protected]</h3>
<h3><code>threading::Mutex</code> log4cpp::HierarchyMaintainer::_categoryMutex [mutable], [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
