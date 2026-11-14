---
title: "stdchronozoned_time(3)"
name: "stdchronozoned_time"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronozoned_time/"
description: "std::chrono::zoned_time<Duration,TimeZonePtr>::zoned_time – std::chrono::zoned_time<Duration,TimeZonePtr>::zoned_time"
---

<p>std::chrono::zoned_time&lt;Duration,TimeZonePtr&gt;::zoned_time &#8211; std::chrono::zoned_time&lt;Duration,TimeZonePtr&gt;::zoned_time</p>
<h2>Synopsis</h2>
<pre><code>zoned_time();
(1)(since C++ 20)

    zoned_time(const std::chrono::sys_time&lt;Duration&gt; &amp;st);
(2)(since C++ 20)

    zoned_time(const zoned_time &amp;other) = default;
(3)(since C++ 20)

    template &lt;class Duration2&gt;
    (4)(since C++ 20)

        zoned_time(const std::chrono::zoned_time&lt;Duration2, TimeZonePtr&gt; &amp;other);

explicit zoned_time(TimeZonePtr z);
(5)(since C++ 20)

    explicit zoned_time(std::string_view name);
(6)(since C++ 20)

    zoned_time(TimeZonePtr z, const std::chrono::sys_time&lt;Duration&gt; &amp;st);
(7)(since C++ 20)

    zoned_time(std::string_view name, const std::chrono::sys_time&lt;Duration&gt; &amp;st);
(8)(since C++ 20)

    zoned_time(TimeZonePtr z, const std::chrono::local_time&lt;Duration&gt; &amp;tp);
(9)(since C++ 20)

    zoned_time(std::string_view name, const std::chrono::local_time&lt;Duration&gt; &amp;tp);
(10)(since C++ 20)

    zoned_time(TimeZonePtr z, const std::chrono::local_time&lt;Duration&gt; &amp;tp, (11)(since C++ 20)

                                                                               std::chrono::choose c);

zoned_time(std::string_view name, const std::chrono::local_time&lt;Duration&gt; &amp;tp, (12)(since C++ 20)

                                                                                   std::chrono::choose c);

template &lt;class Duration2, class TimeZonePtr2&gt;
(13)(since C++ 20)

    zoned_time(TimeZonePtr z, const std::chrono::zoned_time&lt;Duration2, TimeZonePtr2&gt; &amp;zt);

template &lt;class Duration2, class TimeZonePtr2&gt;
(14)(since C++ 20)

    zoned_time(TimeZonePtr z, const std::chrono::zoned_time&lt;Duration2, TimeZonePtr2&gt; &amp;zt, choose);

template &lt;class Duration2, class TimeZonePtr2&gt;
(15)(since C++ 20)

    zoned_time(std::string_view name, const std::chrono::zoned_time&lt;Duration2, TimeZonePtr2&gt; &amp;zt);

template &lt;class Duration2, class TimeZonePtr2&gt;
(16)(since C++ 20)

    zoned_time(std::string_view name, const std::chrono::zoned_time&lt;Duration2, TimeZonePtr2&gt; &amp;zt, choose);</code></pre>
<p>Constructs a zoned_time object, initializing the stored time zone pointer and time point according to the following table, where traits is std::chrono::zoned_traits&lt;TimeZonePtr&gt;:<br />
Overload Time zone pointer (denoted zone) Time point (a std::chrono::sys_time&lt;duration&gt;) Notes<br />
<code>(1)</code> traits::default_zone() default constructed (a)<br />
<code>(2)</code> st<br />
<code>(3)</code> other.get_time_zone() other.get_sys_time() (b)<br />
<code>(4)</code> other.get_time_zone() other.get_sys_time() (e)<br />
<code>(5)</code> std::move(z) default constructed<br />
<code>(6)</code> traits::locate_zone(name) (c)<br />
<code>(7)</code> std::move(z) st<br />
<code>(8)</code> traits::locate_zone(name) (c)<br />
<code>(9)</code> std::move(z) zone-&gt;to_sys(tp) (d)<br />
<code>(10)</code> traits::locate_zone(name) (c,d)<br />
<code>(11)</code> std::move(z) zone-&gt;to_sys(tp, c) (d)<br />
<code>(12)</code> traits::locate_zone(name) (c,d)<br />
(13-14) std::move(z) zt.get_sys_time() (e)<br />
(15-16) traits::locate_zone(name) (c,e)<br />
a) Constructors specified to call traits::default_zone() (1-2) do not participate in overload resolution if that expression is not well-formed.<br />
b) The defaulted copy constructor <code>(3)</code> is defined as deleted if std::is_copy_constructible_v&lt;TimeZonePtr&gt; is false.<br />
c) Constructors with a std::string_view parameter name (6,8,10,12,15-16) do not participate in overload resolution if traits::locate_zone(name) is not well-formed or if that expression is not convertible to TimeZonePtr.<br />
d) Constructors specified to call zone-&gt;to_sys (9-12) do not participate in overload resolution if that call expression is not well-formed or if the result is not convertible to std::chrono::sys_time&lt;duration&gt;.<br />
e) Constructors with a template parameter Duration2 (4,13-16) do not participate in overload resolution if Duration2 is not convertible to Duration.<br />
The behavior is undefined if the time zone pointer (initialized as described above) does not refer to a time zone. </p>
<h2>Notes</h2>
<p>zoned_time does not have a move constructor and attempting to move one will perform a copy instead using the defaulted copy constructor <code>(3)</code>. Thus, when TimeZonePtr is a move-only type, zoned_time is immovable: it can be neither moved nor copied.<br />
The constructors (14,16) accept a std::chrono::choose parameter, but that parameter has no effect. </p>
