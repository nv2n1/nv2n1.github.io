---
title: "stdthreadid(3)"
name: "stdthreadid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadid/"
---

std::thread::id - std::thread::id

<h2>Synopsis</h2>

Defined in header &lt;thread&gt; 
class thread::id; <i>(since C++11)</i> 
The class thread::id is a lightweight, trivially copyable class that serves as a unique identifier of std::thread objects. 
Instances of this class may also hold the special distinct value that does not represent any thread. Once a thread has finished, the value of std::thread::id may be reused by another thread. 
This class is designed for use as key in associative containers, both ordered and unordered. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an id that does not represent a thread 
constructor <i>(public member function)</i>

<h2>Non-member functions</h2>

operator== 
operator!= compares two thread::id objects 
operator&lt;_ <i>(function)</i> 
operator&lt;=_ 
operator&gt;_ 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;serializes a thread::id object 
operator&lt;&lt; <i>(function template)</i>

<h2>Helper classes</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes std::hash 
std::hash&lt;std::thread::id&gt; <i>(class template specialization)</i>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the id of the thread 
get_id <i>(public member function)</i> 
get_id returns the thread id of the current thread 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
