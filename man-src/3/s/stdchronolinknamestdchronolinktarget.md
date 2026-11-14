---
title: "stdchronolinknamestdchronolinktarget(3)"
name: "stdchronolinknamestdchronolinktarget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronolinknamestdchronolinktarget/"
description: "std::chrono::link::name,std::chrono::link::target – std::chrono::link::name,std::chrono::link::target"
---

<p>std::chrono::link::name,std::chrono::link::target &#8211; std::chrono::link::name,std::chrono::link::target</p>
<h2>Synopsis</h2>
<p>std::string_view name() const noexcept; <code>(1)</code><br />
std::string_view target() const noexcept; <code>(2)</code><br />
Accesses the name and target of this link object. </p>
<h2>Return value</h2>
<p>1) The alternative name this link object represents.<br />
2) The name of the std::chrono::time_zone for which this link object provides an alternative name. </p>
