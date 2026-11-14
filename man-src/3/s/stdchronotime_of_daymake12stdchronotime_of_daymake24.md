---
title: "stdchronotime_of_daymake12stdchronotime_of_daymake24(3)"
name: "stdchronotime_of_daymake12stdchronotime_of_daymake24"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_of_daymake12stdchronotime_of_daymake24/"
description: "std::chrono::time_of_day<Duration>::make12,std::chrono::time_of_day<Duration>::make24 – std::chrono::time_of_day<Duration>::make12,std::chrono::time_of_day<Duration>::make24"
---

<p>std::chrono::time_of_day&lt;Duration&gt;::make12,std::chrono::time_of_day&lt;Duration&gt;::make24 &#8211; std::chrono::time_of_day&lt;Duration&gt;::make12,std::chrono::time_of_day&lt;Duration&gt;::make24</p>
<h2>Synopsis</h2>
<p>constexpr void make12() noexcept; <code>(1)</code><br />
constexpr void make24() noexcept; <code>(2)</code><br />
Changes the output format.<br />
1) If the current output format is 24-hour, converts to 12-hour time. Otherwise no effects.<br />
2) If the current output format is 12-hour, converts to 24-hour time. Otherwise no effects. </p>
<h2>Notes</h2>
<p>It is not possible to query the current output format. </p>
