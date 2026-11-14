---
title: "log4cppthreading(3)"
name: "log4cppthreading"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppthreading/"
description: "log4cpp::threading –"
---

<p>log4cpp::threading &#8211; </p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>ThreadLocalDataHolder</code><br />
 <i>This class holds Thread local data of type T, i.e. </i><br />
 class <code>MSMutex</code><br />
 <i>A simple object wrapper around CreateMutex() and DeleteMutex() </i><br />
 class <code>MSScopedLock</code><br />
 <i>A simple object wrapper around WaitForSingleObject() and ReleaseMutex() </i><br />
 class <code>Mutex</code> </p>
<p> class <code>ScopedLock</code><br />
 <i>definition of </i><code>ScopedLock</code>;</p>
<h3>Typedefs</h3>
<p>typedef boost::mutex <code>Mutex</code><br />
 <i>Dummy type &#8216;int&#8217; for </i><code>Mutex</code>.<br />
 typedef boost::mutex::scoped_lock <code>ScopedLock</code><br />
 <i>Dummy type &#8216;int&#8217; defintion of </i><code>ScopedLock</code>;.</p>
<h3>Functions</h3>
<p>static std::string <code>getThreadId</code> ()<br />
 <i>Return an identifier for the current thread. </i></p>
<h2>Typedef Documentation</h2>
<h3>typedef omni_mutex <code>log4cpp::threading::Mutex</code></h3>
<p>Dummy type &#8216;int&#8217; for <code>Mutex</code>. A simple, non recursive <code>Mutex</code>. </p>
<p> Yes, this adds a bit of overhead in the for of extra memory, but unfortunately &#8216;void&#8217; is illegal. </p>
<p> Equivalent to Boost.Threads boost::mutex</p>
<h3>typedef omni_mutex_lock <code>log4cpp::threading::ScopedLock</code></h3>
<p>Dummy type &#8216;int&#8217; defintion of <code>ScopedLock</code>;. A simple &#8216;resource acquisition is initialization&#8217; idiom type lock for <code>Mutex</code>. </p>
<p> Equivalent to Boost.Threads boost::scoped_lock.</p>
<h2>Function Documentation</h2>
<h3>std::string log4cpp::threading::getThreadId () [static]</h3>
<p>Return an identifier for the current thread. returns the thread ID </p>
<p> What these identifiers look like is completely up to the underlying thread library. </p>
<p> What these identifiers look like is completely up to the underlying thread library. OmniThreads returns the POSIX thread Id.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
