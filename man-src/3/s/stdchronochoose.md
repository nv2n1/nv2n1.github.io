---
title: "stdchronochoose(3)"
name: "stdchronochoose"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronochoose/"
---

std::chrono::choose - std::chrono::choose

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;chrono&gt;

enum class choose {

    earliest,                   (since C++20)

    latest

};</code></pre> 
The scoped enumeration choose can be passed to certain member functions of std::chrono::time_zone and std::chrono::zoned_time to control how ambiguous or nonexistent local times should be resolved. Passing choose::earliest causes the earlier time point to be returned, while passing choose::latest causes the later time point to be returned. (For nonexistent local times, these two time points are identical.) 
If a choose is not passed and an ambiguous or nonexistent local time is encountered, a std::chrono::ambiguous_local_time or std::chrono::nonexistent_local_time exception (as applicable) will be thrown. 
