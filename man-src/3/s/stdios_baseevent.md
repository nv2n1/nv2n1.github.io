---
title: "stdios_baseevent(3)"
name: "stdios_baseevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseevent/"
---

std::ios_base::event - std::ios_base::event

<h2>Synopsis</h2>

<pre><code>enum event {erase_event, imbue_event, copyfmt_event};</code></pre> 
Specifies the event type which is passed to functions registered by register_callback() on specific events. The following constants are defined: 
Constant Explanation 
erase_event issued on ~ios_base() or basic_ios::copyfmt() (before the copy of members takes place) 
imbue_event issued on imbue() 
copyfmt_event issued on basic_ios::copyfmt() (after the copy of members takes place, but before the exception settings are copied) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
