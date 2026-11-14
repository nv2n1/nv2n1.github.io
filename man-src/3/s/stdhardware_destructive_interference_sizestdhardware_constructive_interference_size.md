---
title: "stdhardware_destructive_interference_sizestdhardware_constructive_interference_size(3)"
name: "stdhardware_destructive_interference_sizestdhardware_constructive_interference_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhardware_destructive_interference_sizestdhardware_constructive_interference_size/"
description: "std::hardware_destructive_interference_size,std::hardware_constructive_interference_size – std::hardware_destructive_interference_size,std::hardware_constructive_interference_size"
---

<p>std::hardware_destructive_interference_size,std::hardware_constructive_interference_size &#8211; std::hardware_destructive_interference_size,std::hardware_constructive_interference_size</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;new&gt;

inline constexpr std::size_t                                          (1) (since C++17)

hardware_destructive_interference_size = /*implementation-defined*/;

inline constexpr std::size_t                                          (2) (since C++17)

hardware_constructive_interference_size = /*implementation-defined*/;</code></pre>
<p>1) Minimum offset between two objects to avoid false sharing. Guaranteed to be at least alignof(std::max_align_t) struct keep_apart {<br />
    alignas(std::hardware_destructive_interference_size) std::atomic&lt;int&gt; cat;<br />
    alignas(std::hardware_destructive_interference_size) std::atomic&lt;int&gt; dog;<br />
};<br />
2) Maximum size of contiguous memory to promote true sharing. Guaranteed to be at least alignof(std::max_align_t) </p>
<pre><code>struct together {
    std::atomic&lt;int&gt; dog;
    int puppy;
};

struct kennel {
    // Other data members...
    alignas(sizeof(together)) together pack;
    // Other data members...
};

static_assert(sizeof(together) &lt;= std::hardware_constructive_interference_size);
</code></pre>
<h2>Notes</h2>
<p>These constants provide a portable way to access the L1 data cache line size. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>hardware_concurrency returns the number of concurrent threads supported by the implementation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::thread)</i><br />
<code>[static]</code> </p>
