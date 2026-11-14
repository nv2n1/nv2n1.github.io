---
title: "stdexecutionsequenced_policystdexecutionparallel_policy(3)"
name: "stdexecutionsequenced_policystdexecutionparallel_policy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexecutionsequenced_policystdexecutionparallel_policy/"
description: "std::execution::sequenced_policy,std::execution::parallel_policy, – std::execution::sequenced_policy,std::execution::parallel_policy,"
---

<p>std::execution::sequenced_policy,std::execution::parallel_policy, &#8211; std::execution::sequenced_policy,std::execution::parallel_policy,</p>
<h2>Synopsis</h2>
<p>Defined in header&nbsp;<wbr>&lt;execution&gt;<br />
class sequenced_policy&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>unspecified&nbsp;<wbr>*/&nbsp;<wbr>};&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr><i>(since C++17)</i><br />
class parallel_policy&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>unspecified&nbsp;<wbr>*/&nbsp;<wbr>};&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr><i>(since C++17)</i><br />
class parallel_unsequenced_policy&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>unspecified&nbsp;<wbr>*/&nbsp;<wbr>};&nbsp;<wbr><code>(3)</code>&nbsp;<wbr><i>(since C++17)</i><br />
class unsequenced_policy&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>unspecified&nbsp;<wbr>*/&nbsp;<wbr>};&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr><i>(since C++20)</i><br />
1)&nbsp;<wbr>The execution policy type used as a unique type to disambiguate parallel<br />
algorithm overloading and require that a parallel algorithm&#8217;s execution may not be<br />
parallelized. The invocations of element access functions in parallel algorithms<br />
invoked with this policy&nbsp;<wbr>(usually specified as std::execution::seq)&nbsp;<wbr>are<br />
indeterminately sequenced in the calling thread.<br />
2)&nbsp;<wbr>The execution policy type used as a unique type to disambiguate parallel<br />
algorithm overloading and indicate that a parallel algorithm&#8217;s execution may be<br />
parallelized. The invocations of element access functions in parallel algorithms<br />
invoked with this policy&nbsp;<wbr>(usually specified as std::execution::par)&nbsp;<wbr>are permitted to<br />
execute in either the invoking thread or in a thread implicitly created by the<br />
library to support parallel algorithm execution. Any such invocations executing in<br />
the same thread are indeterminately sequenced with respect to each other.<br />
3)&nbsp;<wbr>The execution policy type used as a unique type to disambiguate parallel<br />
algorithm overloading and indicate that a parallel algorithm&#8217;s execution may be<br />
parallelized, vectorized, or migrated across threads&nbsp;<wbr>(such as by a parent-stealing<br />
scheduler). The invocations of element access functions in parallel algorithms<br />
invoked with this policy are permitted to execute in an unordered fashion in<br />
unspecified threads, and unsequenced with respect to one another within each thread.<br />
4)&nbsp;<wbr>The execution policy type used as a unique type to disambiguate parallel<br />
algorithm overloading and indicate that a parallel algorithm&#8217;s execution may be<br />
vectorized, e.g., executed on a single thread using instructions that operate on<br />
multiple data items.<br />
During the execution of a parallel algorithm with any of these three execution<br />
policies, if the invocation of an element access function exits via an uncaught<br />
exception, std::terminate is called, but the implementations may define additional<br />
execution policies that handle exceptions differently. </p>
<h2>Notes</h2>
<p>When using parallel execution policy, it is the programmer&#8217;s responsibility to avoid<br />
data races and deadlocks:<br />
Unsequenced execution policies are the only case where function calls are<br />
unsequenced with respect to each other, meaning they can be interleaved. In all<br />
other situations in C++, they are indeterminately-sequenced&nbsp;<wbr>(cannot interleave).<br />
Because of that, users are not allowed to allocate or deallocate memory, acquire<br />
mutexes, use non-lockfree std::atomic specializations, or, in general, perform any<br />
vectorization-unsafe operations when using these policies&nbsp;<wbr>(vectorization-unsafe<br />
functions are the ones that synchronize-with another function, e.g.<br />
std::mutex::unlock synchronizes-with the next std::mutex::lock)<br />
If the implementation cannot parallelize or vectorize&nbsp;<wbr>(e.g. due to lack of<br />
resources), all standard execution policies can fall back to sequential execution. </p>
<h2>See also</h2>
<p>seq<br />
par<br />
par_unseq<br />
unseq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>global execution policy objects<br />
<i>(C++17)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(constant)<br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
(C++20) </p>
