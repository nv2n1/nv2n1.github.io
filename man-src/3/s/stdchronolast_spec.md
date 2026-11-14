---
title: "stdchronolast_spec(3)"
name: "stdchronolast_spec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronolast_spec/"
---

std::chrono::last_spec - std::chrono::last_spec

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;chrono&gt;

    struct last_spec

{
    (since C++ 20)

        explicit last_spec() = default;
};

inline constexpr last_spec last{};
(since C++ 20)</code></pre> 
last_spec is an empty tag type that is used in conjunction with other calendar types to indicate the last thing in a sequence. Depending on context, it may indicate the last day of a month (as in 2018y/February/last, for last day of February 2018, i.e., 2018-02-28) or the last day of the week in a month (as in 2018/February/Sunday[last], for last Sunday of February 2018, i.e., 2018-02-25). 
