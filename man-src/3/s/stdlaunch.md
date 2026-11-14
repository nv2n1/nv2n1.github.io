---
title: "stdlaunch(3)"
name: "stdlaunch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlaunch/"
---

std::launch - std::launch

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;future&gt;

enum class launch : /* unspecified */ {

    async = /* unspecified */,

    deferred = /* unspecified */,            (since C++11)

    /* implementation-defined */

};</code></pre> 
Specifies the launch policy for a task executed by the std::async function. std::launch is an enumeration used as BitmaskType. 
The following constants denoting individual bits are defined by the standard library: 
Constant Explanation 
std::launch::async a new thread is launched to execute the task asynchronously 
std::launch::deferred the task is executed on the calling thread the first time its result is requested (lazy evaluation) 
In addition, implementations are allowed to: 
* define additional bits and bitmasks to specify restrictions on task interactions applicable to a subset of launch policies, and 
* enable those additional bitmasks for the first (default) overload of std::async. 

<h2>See also</h2>

async runs a function asynchronously (potentially in a new thread) and returns a std::future that will hold the result 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
