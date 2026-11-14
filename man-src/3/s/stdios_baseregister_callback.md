---
title: "stdios_baseregister_callback(3)"
name: "stdios_baseregister_callback"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseregister_callback/"
---

std::ios_base::register_callback - std::ios_base::register_callback

<h2>Synopsis</h2>

<pre><code>void register_callback(event_callback function, int index);</code></pre> 
Registers a user-defined function which will be called by imbue(), std::basic_ios::copyfmt() and ~ios_base(). Every registered callback is called every time: the event type (a value of type event) is passed as its first argument, and may be used to distinguish between the callers. 
The callbacks are called in the reverse order of registration (in other words, register_callback() pushes a callback pair on the callback stack). If register_callback() is called from within a callback function to add a new callback, the new callback is only called on the next event. 
The user-defined callback function is not allowed to throw exceptions. 

<h2>Parameters</h2>

function - the function which will be called on event, supplied as a function pointer of type event_callback 
index - custom parameter which will be passed to the function

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

Once registered, a callback cannot be deregistered: it remains a part of the stream object for the rest of its lifetime. If the behavior of a callback needs to change, it may be controlled through iword() or pword(). 
If the same function is registered multiple times, it is called multiple times. 
The integer value that is stored together with the callback is typically an index obtained from xalloc() 

<h2>Example</h2>

demonstrates the use of register_callback to update locale-dependent cached values that are used by a custom output operator 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

#include &lt;functional&gt;
// cached locale-specific message and its hash

typedef std::pair&lt;std::string, std::size_t&gt; cache_t;
// populate the cached message and its hash from the locale

void update_cache(cache_t &amp;cache, std::locale loc)

{
    auto &amp;fct = std::use_facet&lt;std::messages&lt;char&gt;&gt;(loc);
    std::messages_base::catalog cat = fct.open(&quot;sed&quot;, loc);
    cache.first = cat &lt; 0 ? &quot;&quot; : fct.get(cat, 0, 0, &quot;Memory exhausted&quot;);
    cache.second = std::hash&lt;std::string&gt;()(cache.first);
}
// update the cache if the locale changed

void true_callback(std::ios_base::event evt, std::ios_base &amp;str, int idx)

{
    if (evt == std::ios_base::imbue_event) {
        cache_t *ptr = static_cast&lt;cache_t *&gt;(str.pword(idx));
        update_cache(*ptr, str.getloc());
    }
}
// registers the cache in pword() and sets up the callback

struct CacheSetup

{
    CacheSetup(std::ostream &amp;os, std::ios_base::event_callback f, cache_t *cache)
    {
        int index = std::ostream::xalloc();
        os.pword(index) = cache;           // store pointer to cache in the stream
        os.register_callback(f, index);    // store callback and the index to the pointer
        update_cache(*cache, os.getloc()); // initialize cache
    };
};
// some custom class

struct S {
};

// some custom class's operator&lt;&lt; that needs fast access to hashed message

std::ostream &amp;operator&lt;&lt;(std::ostream &amp;os, const S &amp;)

{
    static cache_t cache;
    static CacheSetup setup(os, true_callback, &amp;cache);
    return os &lt;&lt; cache.first &lt;&lt; &quot; : &quot; &lt;&lt; cache.second;
}
int main()

{
    std::locale loc(&quot;en_US.utf8&quot;);
    S s;
    std::cout.imbue(loc);
    std::cout &lt;&lt; s &lt;&lt; '\n';
    std::cout.imbue(std::locale(loc, new std::messages_byname&lt;char&gt;(&quot;de_DE.utf8&quot;)));
    std::cout &lt;&lt; s &lt;&lt; '\n';
    std::cout.imbue(std::locale(loc, new std::messages_byname&lt;char&gt;(&quot;ja_JP.utf8&quot;)));
    std::cout &lt;&lt; s &lt;&lt; '\n';
    std::cout.imbue(std::locale(loc, new std::messages_byname&lt;char&gt;(&quot;ru_RU.utf8&quot;)));
    std::cout &lt;&lt; s &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Memory exhausted : 2,295,079,096 
&nbsp;<wbr>&nbsp;Speicher erschöpft : 3,139,423,551 
&nbsp;<wbr>&nbsp;メモリーが足りません : 3,837,351,114 
&nbsp;<wbr>&nbsp;Память исчерпана : 3,742,732,851
