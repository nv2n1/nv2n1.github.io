---
title: "stdchronozoned_traits(3)"
name: "stdchronozoned_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronozoned_traits/"
---

std::chrono::zoned_traits - std::chrono::zoned_traits

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;chrono&gt;

    template &lt;class TimeZonePtr&gt;
    (1)(since C++ 20)

        struct zoned_traits {
};

template &lt;&gt;
(2)(since C++ 20)

    struct zoned_traits&lt;const std::chrono::time_zone *&gt;;</code></pre> 
The class zoned_traits provides a way to customize the behavior of the constructors of std::chrono::zoned_time with custom time zone pointer types. In particular, it allows such types to specify the default time zone to use and the mapping of a time zone's name to the corresponding time zone pointer. It is acceptable for custom time zone pointer types to not support either operation, in which case the corresponding constructors of zoned_time will not participate in overload resolution. 
The primary template is empty. A specialization is provided for const std::chrono::time_zone*, the default time zone pointer type. 

<h2>Member functions</h2>

&nbsp;std::chrono::zoned_traits&lt;const std::chrono::time_zone*&gt;::default_zone 

 

 
static const std::chrono::time_zone* default_zone(); 

 
Returns a time zone pointer for the default time zone (UTC).

<h2>Return value</h2>

std::chrono::locate_zone(&quot;UTC&quot;). 
&nbsp;std::chrono::zoned_traits&lt;const std::chrono::time_zone*&gt;::locate_zone <pre><code>static const std::chrono::time_zone *locate_zone(std::string_view name);</code></pre> 
Returns the time zone pointer for the time zone designated by name. 

<h2>Return value</h2>

std::chrono::locate_zone(name). 
