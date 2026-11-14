---
title: "log4cppthreadingthreadlocaldataholder(3)"
name: "log4cppthreadingthreadlocaldataholder"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppthreadingthreadlocaldataholder/"
description: "log4cpp::threading::ThreadLocalDataHolder< T > –"
---

<p>log4cpp::threading::ThreadLocalDataHolder&lt; T &gt; &#8211; </p>
<p> This class holds Thread local data of type T, i.e.</p>
<h2>Synopsis</h2>
<p>#include &lt;BoostThreads.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef T <code>data_type</code> </p>
<p> typedef T <code>data_type</code> </p>
<p> typedef T <code>data_type</code> </p>
<h3>Public Member Functions</h3>
<p>T * <code>get</code> () const </p>
<p> T * <code>operator-&gt;</code> () const </p>
<p> T &amp; <code>operator*</code> () const </p>
<p> T * <code>release</code> () </p>
<p> void <code>reset</code> (T *p=NULL) </p>
<p> <code>ThreadLocalDataHolder</code> () </p>
<p> <code>~ThreadLocalDataHolder</code> () </p>
<p> T * <code>get</code> () const </p>
<p> T * <code>operator-&gt;</code> () const </p>
<p> T &amp; <code>operator*</code> () const </p>
<p> T * <code>release</code> () </p>
<p> void <code>reset</code> (T *p=NULL) </p>
<p> <code>ThreadLocalDataHolder</code> () </p>
<p> <code>~ThreadLocalDataHolder</code> () </p>
<p> T * <code>get</code> () const<br />
 <i>Obtains the Object held for the current thread. </i><br />
 T * <code>operator-&gt;</code> () const<br />
 <i>Obtains the Object held for the current thread. </i><br />
 T &amp; <code>operator*</code> () const<br />
 <i>Obtains the Object held for the current thread. </i><br />
 T * <code>release</code> ()<br />
 <i>Releases the Object held for the current thread. </i><br />
 void <code>reset</code> (T *p=NULL)<br />
 <i>Sets a new Object to be held for the current thread. </i><br />
 <code>ThreadLocalDataHolder</code> () </p>
<p> <code>~ThreadLocalDataHolder</code> () </p>
<p> T * <code>get</code> () const<br />
 <i>Obtains the Object held for the current thread. </i><br />
 T * <code>operator-&gt;</code> () const<br />
 <i>Obtains the Object held for the current thread. </i><br />
 T &amp; <code>operator*</code> () const<br />
 <i>Obtains the Object held for the current thread. </i><br />
 T * <code>release</code> ()<br />
 <i>Releases the Object held for the current thread. </i><br />
 void <code>reset</code> (T *p=NULL)<br />
 <i>Sets a new Object to be held for the current thread. </i><br />
 <code>ThreadLocalDataHolder</code> () </p>
<p> <code>~ThreadLocalDataHolder</code> () </p>
<p> T * <code>get</code> () const </p>
<p> T * <code>operator-&gt;</code> () const </p>
<p> T &amp; <code>operator*</code> () const </p>
<p> T * <code>release</code> () </p>
<p> void <code>reset</code> (T *p=NULL) </p>
<h3>Static Public Member Functions</h3>
<p>static void <code>freeHolder</code> (void *p) </p>
<h2>Detailed Description</h2>
<h3>template&lt;typename T&gt;class log4cpp::threading::ThreadLocalDataHolder&lt; T &gt;</h3>
<p>This class holds Thread local data of type T, i.e. </p>
<p> for each thread a <code>ThreadLocalDataHolder</code> holds 0 or 1 instance of T. The held object must be heap allocated and will be deleted upon termination of the thread to which it belongs. </p>
<p> for each thread a <code>ThreadLocalDataHolder</code> holds 0 or 1 instance of T. The held object must be heap allocated and will be deleted upon termination of the thread to wich it belongs. This is an omni_threads based equivalent of Boost.Threads thread_specific_ptr&lt;T&gt; class.</p>
<h2>Member Typedef Documentation</h2>
<h3>template&lt;typename T &gt; typedef T <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>data_type</code></h3>
<h3>template&lt;typename T &gt; typedef T <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>data_type</code></h3>
<h3>template&lt;typename T &gt; typedef T <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>data_type</code></h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::~<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::~<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::~<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h3>template&lt;typename T &gt; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::~<code>ThreadLocalDataHolder</code> () [inline]</h3>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename T &gt; static void <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::freeHolder (void *p) [inline], [static]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::get () const [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::get () const [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::get () const [inline]</h3>
<p>Obtains the Object held for the current thread. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the held Object or NULL if no Object has been set for the current thread.</dl>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::get () const [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::get () const [inline]</h3>
<p>Obtains the Object held for the current thread. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the held Object or NULL if no Object has been set for the current thread.</dl>
<h3>template&lt;typename T &gt; T&amp; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator* () const [inline]</h3>
<h3>template&lt;typename T &gt; T&amp; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator* () const [inline]</h3>
<h3>template&lt;typename T &gt; T&amp; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator* () const [inline]</h3>
<p>Obtains the Object held for the current thread. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd><code>get()</code> != NULL</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a reference to the held Object.</dl>
<h3>template&lt;typename T &gt; T&amp; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator* () const [inline]</h3>
<h3>template&lt;typename T &gt; T&amp; <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator* () const [inline]</h3>
<p>Obtains the Object held for the current thread. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd><code>get()</code> != NULL</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a reference to the held Object.</dl>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator-&gt; () const [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator-&gt; () const [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator-&gt; () const [inline]</h3>
<p>Obtains the Object held for the current thread. Initially each thread holds NULL. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the held Object or NULL if no Object has been set for the current thread.</dl>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator-&gt; () const [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::operator-&gt; () const [inline]</h3>
<p>Obtains the Object held for the current thread. Initially each thread holds NULL. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the held Object or NULL if no Object has been set for the current thread.</dl>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::release () [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::release () [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::release () [inline]</h3>
<p>Releases the Object held for the current thread. </p>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd><code>get()</code> == NULL</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the Object thas was held for the current thread or NULL if no Object was held.</dl>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::release () [inline]</h3>
<h3>template&lt;typename T &gt; T* <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::release () [inline]</h3>
<p>Releases the Object held for the current thread. </p>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd><code>get()</code> == NULL</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the Object thas was held for the current thread or NULL if no Object was held.</dl>
<h3>template&lt;typename T &gt; void <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::reset (T *p = NULL) [inline]</h3>
<h3>template&lt;typename T &gt; void <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::reset (T *p = NULL) [inline]</h3>
<h3>template&lt;typename T &gt; void <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::reset (T *p = NULL) [inline]</h3>
<p>Sets a new Object to be held for the current thread. A previously set Object will be deleted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> the new object to hold.</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd><code>get()</code> == p</dl>
<h3>template&lt;typename T &gt; void <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::reset (T *p = NULL) [inline]</h3>
<h3>template&lt;typename T &gt; void <code>log4cpp::threading::ThreadLocalDataHolder</code>&lt; T &gt;::reset (T *p = NULL) [inline]</h3>
<p>Sets a new Object to be held for the current thread. A previously set Object will be deleted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> the new object to hold.</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd><code>get()</code> == p</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
