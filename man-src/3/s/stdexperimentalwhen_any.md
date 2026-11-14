---
title: "stdexperimentalwhen_any(3)"
name: "stdexperimentalwhen_any"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalwhen_any/"
---

std::experimental::when_any - std::experimental::when_any

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / future&gt;

    template &lt;class Sequence&gt;

    struct when_any_result {

    std::size_t index;
    (concurrency TS)

        Sequence futures;
};

template &lt;class InputIt&gt;

auto when_any(InputIt first, InputIt last)(1)(concurrency TS)

    -&gt; future&lt;when_any_result&lt;std::vector&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt;&gt;&gt;;

template &lt;class... Futures&gt;

auto when_any(Futures &amp;&amp;...futures)(2)(concurrency TS)

    -&gt; future&lt;when_any_result&lt;std::tuple&lt;std::decay_t&lt;Futures&gt;...&gt;&gt;&gt;;
Create a future object that becomes ready when at least one of the input futures and shared_futures become ready. The behavior is undefined if any input future or shared_future is invalid.

In particular, let Sequence be a std::vector&lt;typename std::iterator_traits&lt;InputIt&gt;::value_type&gt; for (1) and std::tuple&lt;std::decay_t&lt;Futures&gt;...&gt; for (2). This function template creates a shared state containing when_any_result&lt;Sequence&gt; and returns a future referring to the shared state. Every input future is moved into the corresponding object in the futures member of the when_any_result&lt;Sequence&gt; in the shared state, and every input shared_future is copied to the corresponding object in the futures member of the when_any_result&lt;Sequence&gt; in the shared state. The order of the objects in the Sequence matches the order of arguments.

1) This function does not participate in overload resolution unless InputIt's value type (i.e., typename std::iterator_traits&lt;InputIt&gt;::value_type) is a std::experimental::future or std::experimental::shared_future.

2) This function does not participate in overload resolution unless every argument is either a (possibly cv-qualified) std::experimental::shared_future or a cv-unqualified std::experimental::future. (Formally, for every type Fn in Futures, either std::remove_reference_t&lt;Fn&gt; is std::experimental::future&lt;Rn&gt;, or std::decay_t&lt;Fn&gt; is std::experimental::shared_future&lt;Rn&gt;.)

After this call, every input future is no longer valid;
every input shared_future remains valid.
</code></pre>

<h2>Return value</h2>

A future referring to the shared state created by the call. The future is always valid(), and it becomes ready when at least one of the input futures and shared_futures the call are ready. The index member of the when_any_result contains the position of the ready future or shared_future in the futures member. 
1) If the range is empty (i.e., first == last), the returned future is ready immediately; the futures field of the when_any_result is an empty vector, and the index field is size_t(-1). 
2) If no argument is provided, the returned future is ready immediately; the futures field of the when_any_result is an empty tuple, and the index field is size_t(-1). 
