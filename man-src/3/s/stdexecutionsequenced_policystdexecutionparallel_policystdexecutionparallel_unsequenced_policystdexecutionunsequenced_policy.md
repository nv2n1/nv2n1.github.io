---
title: "stdexecutionsequenced_policystdexecutionparallel_policystdexecutionparallel_unsequenced_policystdexecutionunsequenced_policy(3)"
name: "stdexecutionsequenced_policystdexecutionparallel_policystdexecutionparallel_unsequenced_policystdexecutionunsequenced_policy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexecutionsequenced_policystdexecutionparallel_policystdexecutionparallel_unsequenced_policystdexecutionunsequenced_policy/"
description: "std::execution::sequenced_policy,std::execution::parallel_policy,std::execution::parallel_unsequenced_policy,std::execution::unsequenced_policy – std::execution::sequenced_policy,std::execution::pa..."
---

<p>std::execution::sequenced_policy,std::execution::parallel_policy,std::execution::parallel_unsequenced_policy,std::execution::unsequenced_policy &#8211; std::execution::sequenced_policy,std::execution::parallel_policy,std::execution::parallel_unsequenced_policy,std::execution::unsequenced_policy</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;execution&gt;<br />
class sequenced_policy { /* unspecified */ }; <code>(1)</code> <i>(since C++17)</i><br />
class parallel_policy { /* unspecified */ }; <code>(2)</code> <i>(since C++17)</i><br />
class parallel_unsequenced_policy { /* unspecified */ }; <code>(3)</code> <i>(since C++17)</i><br />
class unsequenced_policy { /* unspecified */ }; <code>(4)</code> <i>(since C++20)</i><br />
1) The execution policy type used as a unique type to disambiguate parallel algorithm overloading and require that a parallel algorithm&#8217;s execution may not be parallelized. The invocations of element access functions in parallel algorithms invoked with this policy (usually specified as std::execution::seq) are indeterminately sequenced in the calling thread.<br />
2) The execution policy type used as a unique type to disambiguate parallel algorithm overloading and indicate that a parallel algorithm&#8217;s execution may be parallelized. The invocations of element access functions in parallel algorithms invoked with this policy (usually specified as std::execution::par) are permitted to execute in either the invoking thread or in a thread implicitly created by the library to support parallel algorithm execution. Any such invocations executing in the same thread are indeterminately sequenced with respect to each other.<br />
3) The execution policy type used as a unique type to disambiguate parallel algorithm overloading and indicate that a parallel algorithm&#8217;s execution may be parallelized, vectorized, or migrated across threads (such as by a parent-stealing scheduler). The invocations of element access functions in parallel algorithms invoked with this policy are permitted to execute in an unordered fashion in unspecified threads, and unsequenced with respect to one another within each thread.<br />
4) The execution policy type used as a unique type to disambiguate parallel algorithm overloading and indicate that a parallel algorithm&#8217;s execution may be vectorized, e.g., executed on a single thread using instructions that operate on multiple data items.<br />
During the execution of a parallel algorithm with any of these three execution policies, if the invocation of an element access function exits via an uncaught exception, std::terminate is called, but the implementations may define additional execution policies that handle exceptions differently. </p>
<h2>Notes</h2>
<p>When using parallel execution policy, it is the programmer&#8217;s responsibility to avoid data races and deadlocks:<br />
Unsequenced execution policies are the only case where function calls are unsequenced with respect to each other, meaning they can be interleaved. In all other situations in C++, they are indeterminately-sequenced (cannot interleave). Because of that, users are not allowed to allocate or deallocate memory, acquire mutexes, use non-lockfree std::atomic specializations, or, in general, perform any vectorization-unsafe operations when using these policies (vectorization-unsafe functions are the ones that synchronize-with another function, e.g. std::mutex::unlock synchronizes-with the next std::mutex::lock)<br />
If the implementation cannot parallelize or vectorize (e.g. due to lack of resources), all standard execution policies can fall back to sequential execution. </p>
<h2>See also</h2>
<p>seq<br />
par<br />
par_unseq<br />
unseq global execution policy objects<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant)<br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
(C++20) </p>
