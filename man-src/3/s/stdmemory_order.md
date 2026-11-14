---
title: "stdmemory_order(3)"
name: "stdmemory_order"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmemory_order/"
description: "std::memory_order – std::memory_order"
---

<p>std::memory_order &#8211; std::memory_order</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;atomic&gt;

typedef enum memory_order {

    memory_order_relaxed,

    memory_order_consume,

    memory_order_acquire,                                                        (since C++11)

    memory_order_release,                                                        (until C++20)

    memory_order_acq_rel,

    memory_order_seq_cst

} memory_order;

enum class memory_order : /*unspecified*/ {

    relaxed, consume, acquire, release, acq_rel, seq_cst

};

inline constexpr memory_order memory_order_relaxed = memory_order::relaxed;

inline constexpr memory_order memory_order_consume = memory_order::consume;  (since C++20)

inline constexpr memory_order memory_order_acquire = memory_order::acquire;

inline constexpr memory_order memory_order_release = memory_order::release;

inline constexpr memory_order memory_order_acq_rel = memory_order::acq_rel;

inline constexpr memory_order memory_order_seq_cst = memory_order::seq_cst;</code></pre>
<p>std::memory_order specifies how memory accesses, including regular, non-atomic memory accesses, are to be ordered around an atomic operation. Absent any constraints on a multi-core system, when multiple threads simultaneously read and write to several variables, one thread can observe the values change in an order different from the order another thread wrote them. Indeed, the apparent order of changes can even differ among multiple reader threads. Some similar effects can occur even on uniprocessor systems due to compiler transformations allowed by the memory model.<br />
The default behavior of all atomic operations in the library provides for sequentially consistent ordering (see discussion below). That default can hurt performance, but the library&#8217;s atomic operations can be given an additional std::memory_order argument to specify the exact constraints, beyond atomicity, that the compiler and processor must enforce for that operation. </p>
<h2>Constants</h2>
<p>Defined in header &lt;atomic&gt;<br />
Value Explanation<br />
memory_order_relaxed Relaxed operation: there are no synchronization or ordering constraints imposed on other reads or writes, only this operation&#8217;s atomicity is guaranteed (see Relaxed_ordering below)<br />
memory_order_consume A load operation with this memory order performs a consume operation on the affected memory location: no reads or writes in the current thread dependent on the value currently loaded can be reordered before this load. Writes to data-dependent variables in other threads that release the same atomic variable are visible in the current thread. On most platforms, this affects compiler optimizations only (see Release-Consume_ordering below)<br />
memory_order_acquire A load operation with this memory order performs the acquire operation on the affected memory location: no reads or writes in the current thread can be reordered before this load. All writes in other threads that release the same atomic variable are visible in the current thread (see Release-Acquire_ordering below)<br />
memory_order_release A store operation with this memory order performs the release operation: no reads or writes in the current thread can be reordered after this store. All writes in the current thread are visible in other threads that acquire the same atomic variable (see Release-Acquire_ordering below) and writes that carry a dependency into the atomic variable become visible in other threads that consume the same atomic (see Release-Consume_ordering below).<br />
memory_order_acq_rel A read-modify-write operation with this memory order is both an acquire operation and a release operation. No memory reads or writes in the current thread can be reordered before or after this store. All writes in other threads that release the same atomic variable are visible before the modification and the modification is visible in other threads that acquire the same atomic variable.<br />
memory_order_seq_cst A load operation with this memory order performs an acquire operation, a store performs a release operation, and read-modify-write performs both an acquire operation and a release operation, plus a single total order exists in which all threads observe all modifications in the same order (see Sequentially-consistent_ordering below)</p>
<h2>Formal description</h2>
<p>Inter-thread synchronization and memory ordering determine how evaluations and side effects of expressions are ordered between different threads of execution. They are defined in the following terms:</p>
<h2>Sequenced-before</h2>
<p>Within the same thread, evaluation A may be sequenced-before evaluation B, as described in evaluation_order.</p>
<h2>Carries dependency</h2>
<p>Within the same thread, evaluation A that is sequenced-before evaluation B may also carry a dependency into B (that is, B depends on A), if any of the following is true<br />
1) The value of A is used as an operand of B, except<br />
a) if B is a call to std::kill_dependency<br />
b) if A is the left operand of the built-in &amp;&amp;, ||, ?:, or , operators.<br />
2) A writes to a scalar object M, B reads from M<br />
3) A carries dependency into another evaluation X, and X carries dependency into B</p>
<h2>Modification order</h2>
<p>All modifications to any particular atomic variable occur in a total order that is specific to this one atomic variable.<br />
The following four requirements are guaranteed for all atomic operations:<br />
1) Write-write coherence: If evaluation A that modifies some atomic M (a write) happens-before evaluation B that modifies M, then A appears earlier than B in the modification order of M<br />
2) Read-read coherence: if a value computation A of some atomic M (a read) happens-before a value computation B on M, and if the value of A comes from a write X on M, then the value of B is either the value stored by X, or the value stored by a side effect Y on M that appears later than X in the modification order of M.<br />
3) Read-write coherence: if a value computation A of some atomic M (a read) happens-before an operation B on M (a write), then the value of A comes from a side-effect (a write) X that appears earlier than B in the modification order of M<br />
4) Write-read coherence: if a side effect (a write) X on an atomic object M happens-before a value computation (a read) B of M, then the evaluation B shall take its value from X or from a side effect Y that follows X in the modification order of M</p>
<h2>Release sequence</h2>
<p>After a release operation A is performed on an atomic object M, the longest continuous subsequence of the modification order of M that consists of </p>
<p>1) Writes performed by the same thread that performed A <i>(until C++20)</i> </p>
<p>2) Atomic read-modify-write operations made to M by any thread<br />
is known as release sequence headed by A</p>
<h2>Dependency-ordered before</h2>
<p>Between threads, evaluation A is dependency-ordered before evaluation B if any of the following is true<br />
1) A performs a release operation on some atomic M, and, in a different thread, B performs a consume operation on the same atomic M, and B reads a value written by any part of the release sequence headed by A.<br />
2) A is dependency-ordered before X and X carries a dependency into B.</p>
<h2>Inter-thread happens-before</h2>
<p>Between threads, evaluation A inter-thread happens before evaluation B if any of the following is true<br />
1) A synchronizes-with B<br />
2) A is dependency-ordered before B<br />
3) A synchronizes-with some evaluation X, and X is sequenced-before B<br />
4) A is sequenced-before some evaluation X, and X inter-thread happens-before B<br />
5) A inter-thread happens-before some evaluation X, and X inter-thread happens-before B</p>
<h2>Happens-before</h2>
<p>Regardless of threads, evaluation A happens-before evaluation B if any of the following is true:<br />
1) A is sequenced-before B<br />
2) A inter-thread happens before B<br />
The implementation is required to ensure that the happens-before relation is acyclic, by introducing additional synchronization if necessary (it can only be necessary if a consume operation is involved, see Batty_et_al)<br />
If one evaluation modifies a memory location, and the other reads or modifies the same memory location, and if at least one of the evaluations is not an atomic operation, the behavior of the program is undefined (the program has a data_race) unless there exists a happens-before relationship between these two evaluations. </p>
<p>Strongly happens-before </p>
<p>Regardless of threads, evaluation A strongly happens-before evaluation B if any of the following is true: <i>(until C++20)</i><br />
1) A is sequenced-before B<br />
2) A synchronizes-with B<br />
3) A strongly happens-before X, and X strongly happens-before B </p>
<p>Simply happens-before </p>
<p>Regardless of threads, evaluation A simply happens-before evaluation B if any of the following is true:<br />
1) A is sequenced-before B<br />
2) A synchronizes-with B<br />
3) A simply happens-before X, and X simply happens-before B<br />
Note: without consume operations, simply happens-before and happens-before relations are the same.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i><br />
Strongly happens-before </p>
<p>Regardless of threads, evaluation A strongly happens-before evaluation B if any of the following is true:<br />
1) A is sequenced-before B<br />
2) A synchronizes with B, and both A and B are sequentially consistent atomic operations<br />
3) A is sequenced-before X, X simply happens-before Y, and Y is sequenced-before B<br />
4) A strongly happens-before X, and X strongly happens-before B<br />
Note: informally, if A strongly happens-before B, then A appears to be evaluated before B in all contexts.<br />
Note: strongly happens-before excludes consume operations.</p>
<h2>Visible side-effects</h2>
<p>The side-effect A on a scalar M (a write) is visible with respect to value computation B on M (a read) if both of the following are true:<br />
1) A happens-before B<br />
2) There is no other side effect X to M where A happens-before X and X happens-before B<br />
If side-effect A is visible with respect to the value computation B, then the longest contiguous subset of the side-effects to M, in modification order, where B does not happen-before it is known as the visible sequence of side-effects. (the value of M, determined by B, will be the value stored by one of these side effects)<br />
Note: inter-thread synchronization boils down to preventing data races (by establishing happens-before relationships) and defining which side effects become visible under what conditions</p>
<h2>Consume operation</h2>
<p>Atomic load with memory_order_consume or stronger is a consume operation. Note that std::atomic_thread_fence imposes stronger synchronization requirements than a consume operation.</p>
<h2>Acquire operation</h2>
<p>Atomic load with memory_order_acquire or stronger is an acquire operation. The lock() operation on a Mutex is also an acquire operation. Note that std::atomic_thread_fence imposes stronger synchronization requirements than an acquire operation.</p>
<h2>Release operation</h2>
<p>Atomic store with memory_order_release or stronger is a release operation. The unlock() operation on a Mutex is also a release operation. Note that std::atomic_thread_fence imposes stronger synchronization requirements than a release operation.</p>
<h2>Explanation</h2>
<h2>Relaxed ordering</h2>
<p>Atomic operations tagged memory_order_relaxed are not synchronization operations; they do not impose an order among concurrent memory accesses. They only guarantee atomicity and modification order consistency.<br />
For example, with x and y initially zero, </p>
<p>&nbsp;<wbr>&nbsp;// Thread 1:<br />
&nbsp;<wbr>&nbsp;r1 = y.load(std::memory_order_relaxed); // A<br />
&nbsp;<wbr>&nbsp;x.store(r1, std::memory_order_relaxed); // B<br />
&nbsp;<wbr>&nbsp;// Thread 2:<br />
&nbsp;<wbr>&nbsp;r2 = x.load(std::memory_order_relaxed); // C<br />
&nbsp;<wbr>&nbsp;y.store(42, std::memory_order_relaxed); // D </p>
<p>is allowed to produce r1 == r2 == 42 because, although A is sequenced-before B within thread 1 and C is sequenced before D within thread 2, nothing prevents D from appearing before A in the modification order of y, and B from appearing before C in the modification order of x. The side-effect of D on y could be visible to the load A in thread 1 while the side effect of B on x could be visible to the load C in thread 2. In particular, this may occur if D is completed before C in thread 2, either due to compiler reordering or at runtime. </p>
<p>Even with relaxed memory model, out-of-thin-air values are not allowed to circularly depend on their own computations, for example, with x and y initially zero, </p>
<p>&nbsp;<wbr>&nbsp;// Thread 1:<br />
&nbsp;<wbr>&nbsp;r1 = x.load(std::memory_order_relaxed);<br />
&nbsp;<wbr>&nbsp;if (r1 == 42) y.store(r1, std::memory_order_relaxed); <i>(since C++14)</i><br />
&nbsp;<wbr>&nbsp;// Thread 2:<br />
&nbsp;<wbr>&nbsp;r2 = y.load(std::memory_order_relaxed);<br />
&nbsp;<wbr>&nbsp;if (r2 == 42) x.store(42, std::memory_order_relaxed); </p>
<p>is not allowed to produce r1 == r2 == 42 since the store of 42 to y is only possible if the store to x stores 42, which circularly depends on the store to y storing 42. Note that until C++14, this was technically allowed by the specification, but not recommended for implementors. </p>
<p>Typical use for relaxed memory ordering is incrementing counters, such as the reference counters of std::shared_ptr, since this only requires atomicity, but not ordering or synchronization (note that decrementing the shared_ptr counters requires acquire-release synchronization with the destructor)<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;vector&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;iostream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;thread&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;atomic&gt; </p>
<p>&nbsp;<wbr>&nbsp;std::atomic&lt;int&gt; cnt = {0}; </p>
<p>&nbsp;<wbr>&nbsp;void f()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (int n = 0; n &lt; 1000; ++n) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cnt.fetch_add(1, std::memory_order_relaxed);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;std::thread&gt; v;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (int n = 0; n &lt; 10; ++n) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v.emplace_back(f);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (auto&amp; t : v) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t.join();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;Final counter value is &quot; &lt;&lt; cnt &lt;&lt; &#8216;
&#8217;;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Final counter value is 10000</p>
<h2>Release-Acquire ordering</h2>
<p>If an atomic store in thread A is tagged memory_order_release and an atomic load in thread B from the same variable is tagged memory_order_acquire, all memory writes (non-atomic and relaxed atomic) that happened-before the atomic store from the point of view of thread A, become visible side-effects in thread B. That is, once the atomic load is completed, thread B is guaranteed to see everything thread A wrote to memory.<br />
The synchronization is established only between the threads releasing and acquiring the same atomic variable. Other threads can see different order of memory accesses than either or both of the synchronized threads.<br />
On strongly-ordered systems — x86, SPARC TSO, IBM mainframe, etc. — release-acquire ordering is automatic for the majority of operations. No additional CPU instructions are issued for this synchronization mode; only certain compiler optimizations are affected (e.g., the compiler is prohibited from moving non-atomic stores past the atomic store-release or performing non-atomic loads earlier than the atomic load-acquire). On weakly-ordered systems (ARM, Itanium, PowerPC), special CPU load or memory fence instructions are used.<br />
Mutual exclusion locks, such as std::mutex or atomic_spinlock, are an example of release-acquire synchronization: when the lock is released by thread A and acquired by thread B, everything that took place in the critical section (before the release) in the context of thread A has to be visible to thread B (after the acquire) which is executing the same critical section.<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;thread&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;atomic&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;cassert&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;string&gt; </p>
<p>&nbsp;<wbr>&nbsp;std::atomic&lt;std::string*&gt; ptr;<br />
&nbsp;<wbr>&nbsp;int data; </p>
<p>&nbsp;<wbr>&nbsp;void producer()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::string* p = new std::string(&quot;Hello&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data = 42;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptr.store(p, std::memory_order_release);<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void consumer()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::string* p2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (!(p2 = ptr.load(std::memory_order_acquire)))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(*p2 == &quot;Hello&quot;); // never fires<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(data == 42); // never fires<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread t1(producer);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread t2(consumer);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t1.join(); t2.join();<br />
&nbsp;<wbr>&nbsp;} </p>
<p>The following example demonstrates transitive release-acquire ordering across three threads<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;thread&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;atomic&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;cassert&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;vector&gt; </p>
<p>&nbsp;<wbr>&nbsp;std::vector&lt;int&gt; data;<br />
&nbsp;<wbr>&nbsp;std::atomic&lt;int&gt; flag = {0}; </p>
<p>&nbsp;<wbr>&nbsp;void thread_1()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data.push_back<code>(42)</code>;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flag.store(1, std::memory_order_release);<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void thread_2()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int expected=1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (!flag.compare_exchange_strong(expected, 2, std::memory_order_acq_rel)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;expected = 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void thread_3()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (flag.load(std::memory_order_acquire) &lt; 2)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(data.at<code>(0)</code> == 42); // will never fire<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread a(thread_1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread b(thread_2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread c(thread_3);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a.join(); b.join(); c.join();<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Release-Consume ordering</h2>
<p>If an atomic store in thread A is tagged memory_order_release and an atomic load in thread B from the same variable is tagged memory_order_consume, all memory writes (non-atomic and relaxed atomic) that are dependency-ordered-before the atomic store from the point of view of thread A, become visible side-effects within those operations in thread B into which the load operation carries dependency, that is, once the atomic load is completed, those operators and functions in thread B that use the value obtained from the load are guaranteed to see what thread A wrote to memory.<br />
The synchronization is established only between the threads releasing and consuming the same atomic variable. Other threads can see different order of memory accesses than either or both of the synchronized threads.<br />
On all mainstream CPUs other than DEC Alpha, dependency ordering is automatic, no additional CPU instructions are issued for this synchronization mode, only certain compiler optimizations are affected (e.g. the compiler is prohibited from performing speculative loads on the objects that are involved in the dependency chain).<br />
Typical use cases for this ordering involve read access to rarely written concurrent data structures (routing tables, configuration, security policies, firewall rules, etc) and publisher-subscriber situations with pointer-mediated publication, that is, when the producer publishes a pointer through which the consumer can access information: there is no need to make everything else the producer wrote to memory visible to the consumer (which may be an expensive operation on weakly-ordered architectures). An example of such scenario is rcu_dereference.<br />
See also std::kill_dependency and [[carries_dependency]] for fine-grained dependency chain control.<br />
Note that currently (2/2015) no known production compilers track dependency chains: consume operations are lifted to acquire operations. </p>
<p>The specification of release-consume ordering is being revised, and the use of memory_order_consume is temporarily discouraged. <i>(since C++17)</i> </p>
<p>This example demonstrates dependency-ordered synchronization for pointer-mediated publication: the integer data is not related to the pointer to string by a data-dependency relationship, thus its value is undefined in the consumer.<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;thread&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;atomic&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;cassert&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;string&gt; </p>
<p>&nbsp;<wbr>&nbsp;std::atomic&lt;std::string*&gt; ptr;<br />
&nbsp;<wbr>&nbsp;int data; </p>
<p>&nbsp;<wbr>&nbsp;void producer()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::string* p = new std::string(&quot;Hello&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data = 42;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptr.store(p, std::memory_order_release);<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void consumer()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::string* p2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (!(p2 = ptr.load(std::memory_order_consume)))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(*p2 == &quot;Hello&quot;); // never fires: *p2 carries dependency from ptr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(data == 42); // may or may not fire: data does not carry dependency from ptr<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread t1(producer);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread t2(consumer);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t1.join(); t2.join();<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Sequentially-consistent ordering</h2>
<p>Atomic operations tagged memory_order_seq_cst not only order memory the same way as release/acquire ordering (everything that happened-before a store in one thread becomes a visible side effect in the thread that did a load), but also establish a single total modification order of all atomic operations that are so tagged. </p>
<p>Formally,<br />
Each memory_order_seq_cst operation B that loads from atomic variable M, observes one of the following: </p>
<p>* the result of the last operation A that modified M, which appears before B in the single total order<br />
* OR, if there was such an A, B may observe the result of some modification on M that is not memory_order_seq_cst and does not happen-before A<br />
* OR, if there wasn&#8217;t such an A, B may observe the result of some unrelated modification of M that is not memory_order_seq_cst </p>
<p>If there was a memory_order_seq_cst std::atomic_thread_fence operation X sequenced-before B, then B observes one of the following: </p>
<p>* the last memory_order_seq_cst modification of M that appears before X in the single total order<br />
* some unrelated modification of M that appears later in M&#8217;s modification order </p>
<p>For a pair of atomic operations on M called A and B, where A writes and B reads M&#8217;s value, if there are two memory_order_seq_cst std::atomic_thread_fences X and Y, and if A is sequenced-before X, Y is sequenced-before B, and X appears before Y in the Single Total Order, then B observes either: <i>(until C++20)</i> </p>
<p>* the effect of A<br />
* some unrelated modification of M that appears after A in M&#8217;s modification order </p>
<p>For a pair of atomic modifications of M called A and B, B occurs after A in M&#8217;s modification order if </p>
<p>* there is a memory_order_seq_cst std::atomic_thread_fence X such that A is sequenced-before X and X appears before B in the Single Total Order<br />
* or, there is a memory_order_seq_cst std::atomic_thread_fence Y such that Y is sequenced-before B and A appears before Y in the Single Total Order<br />
* or, there are memory_order_seq_cst std::atomic_thread_fences X and Y such that A is sequenced-before X, Y is sequenced-before B, and X appears before Y in the Single Total Order. </p>
<p>Note that this means that:<br />
1) as soon as atomic operations that are not tagged memory_order_seq_cst enter the picture, the sequential consistency is lost<br />
2) the sequentially-consistent fences are only establishing total ordering for the fences themselves, not for the atomic operations in the general case (sequenced-before is not a cross-thread relationship, unlike happens-before)<br />
Formally,<br />
An atomic operation A on some atomic object M is coherence-ordered-before another atomic operation B on M if any of the following is true:<br />
1) A is a modification, and B reads the value stored by A<br />
2) A precedes B in the modification order of M<br />
3) A reads the value stored by an atomic modification X, X precedes B in the modification order, and A and B are not the same atomic read-modify-write operation<br />
4) A is coherence-ordered-before X, and X is coherence-ordered-before B<br />
There is a single total order S on all memory_order_seq_cst operations, including fences, that satisfies the following constraints:<br />
1) if A and B are memory_order_seq_cst operations, and A strongly happens-before B, then A precedes B in S<br />
2) for every pair of atomic operations A and B on an object M, where A is coherence-ordered-before B:<br />
a) if A and B are both memory_order_seq_cst operations, then A precedes B in S<br />
b) if A is a memory_order_seq_cst operation, and B happens-before a memory_order_seq_cst fence Y, then A precedes Y in S<br />
c) if a memory_order_seq_cst fence X happens-before A, and B is a memory_order_seq_cst operation, then X precedes B in S<br />
d) if a memory_order_seq_cst fence X happens-before A, and B happens-before a memory_order_seq_cst fence Y, then X precedes Y in S<br />
The formal definition ensures that:<br />
1) the single total order is consistent with the modification order of any atomic object<br />
2) a memory_order_seq_cst load gets its value either from the last memory_order_seq_cst modification, or from some non-memory_order_seq_cst modification that does not happen-before preceding memory_order_seq_cst modifications<br />
The single total order might not be consistent with happens-before. This allows more efficient implementation of memory_order_acquire and memory_order_release on some CPUs. It can produce surprising results when memory_order_acquire and memory_order_release are mixed with memory_order_seq_cst. <i>(since C++20)</i><br />
For example, with x and y initially zero, </p>
<p>&nbsp;<wbr>&nbsp;// Thread 1:<br />
&nbsp;<wbr>&nbsp;x.store(1, std::memory_order_seq_cst); // A<br />
&nbsp;<wbr>&nbsp;y.store(1, std::memory_order_release); // B<br />
&nbsp;<wbr>&nbsp;// Thread 2:<br />
&nbsp;<wbr>&nbsp;r1 = y.fetch_add(1, std::memory_order_seq_cst); // C<br />
&nbsp;<wbr>&nbsp;r2 = y.load(std::memory_order_relaxed); // D<br />
&nbsp;<wbr>&nbsp;// Thread 3:<br />
&nbsp;<wbr>&nbsp;y.store(3, std::memory_order_seq_cst); // E<br />
&nbsp;<wbr>&nbsp;r3 = x.load(std::memory_order_seq_cst); // F </p>
<p>is allowed to produce r1 == 1 &amp;&amp; r2 == 3 &amp;&amp; r3 == 0, where A happens-before C, but C precedes A in the single total order C-E-F-A of memory_order_seq_cst (see Lahav_et_al).<br />
Note that:<br />
1) as soon as atomic operations that are not tagged memory_order_seq_cst enter the picture, the sequential consistency guarantee for the program is lost<br />
2) in many cases, memory_order_seq_cst atomic operations are reorderable with respect to other atomic operations performed by the same thread </p>
<p>Sequential ordering may be necessary for multiple producer-multiple consumer situations where all consumers must observe the actions of all producers occurring in the same order.<br />
Total sequential ordering requires a full memory fence CPU instruction on all multi-core systems. This may become a performance bottleneck since it forces the affected memory accesses to propagate to every core.<br />
This example demonstrates a situation where sequential ordering is necessary. Any other ordering may trigger the assert because it would be possible for the threads c and d to observe changes to the atomics x and y in opposite order.<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;thread&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;atomic&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;cassert&gt; </p>
<p>&nbsp;<wbr>&nbsp;std::atomic&lt;bool&gt; x = {false};<br />
&nbsp;<wbr>&nbsp;std::atomic&lt;bool&gt; y = {false};<br />
&nbsp;<wbr>&nbsp;std::atomic&lt;int&gt; z = {0}; </p>
<p>&nbsp;<wbr>&nbsp;void write_x()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x.store(true, std::memory_order_seq_cst);<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void write_y()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;y.store(true, std::memory_order_seq_cst);<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void read_x_then_y()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (!x.load(std::memory_order_seq_cst))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (y.load(std::memory_order_seq_cst)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++z;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;void read_y_then_x()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (!y.load(std::memory_order_seq_cst))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (x.load(std::memory_order_seq_cst)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++z;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread a(write_x);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread b(write_y);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread c(read_x_then_y);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::thread d(read_y_then_x);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a.join(); b.join(); c.join(); d.join();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(z.load() != 0); // will never happen<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Relationship with volatile</h2>
<p>Within a thread of execution, accesses (reads and writes) through volatile_glvalues cannot be reordered past observable side-effects (including other volatile accesses) that are sequenced-before or sequenced-after within the same thread, but this order is not guaranteed to be observed by another thread, since volatile access does not establish inter-thread synchronization.<br />
In addition, volatile accesses are not atomic (concurrent read and write is a data_race) and do not order memory (non-volatile memory accesses may be freely reordered around the volatile access).<br />
One notable exception is Visual Studio, where, with default settings, every volatile write has release semantics and every volatile read has acquire semantics (MSDN), and thus volatiles may be used for inter-thread synchronization. Standard volatile semantics are not applicable to multithreaded programming, although they are sufficient for e.g. communication with a std::signal handler that runs in the same thread when applied to sig_atomic_t variables.</p>
<h2>See also</h2>
<h2>External links</h2>
<p>* MOESI_protocol </p>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: let&#8217;s find good refs on QPI, MOESI, and maybe Dragon </p>
<p>* x86-TSO:_A_Rigorous_and_Usable_Programmer’s_Model_for_x86_Multiprocessors P. Sewell et. al., 2010<br />
* A_Tutorial_Introduction_to_the_ARM_and_POWER_Relaxed_Memory_Models P. Sewell et al, 2012<br />
* MESIF:_A_Two-Hop_Cache_Coherency_Protocol_for_Point-to-Point_Interconnects J.R. Goodman, H.H.J. Hum, 2009</p>
