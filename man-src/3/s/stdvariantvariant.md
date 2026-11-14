---
title: "stdvariantvariant(3)"
name: "stdvariantvariant"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariantvariant/"
---

std::variant&lt;Types...&gt;::~variant - std::variant&lt;Types...&gt;::~variant

<h2>Synopsis</h2>

~variant(); <i>(since C++17)</i> 
If valueless_by_exception is true, does nothing. Otherwise, destroys the currently contained value. 
This destructor is trivial if std::is_trivially_destructible_v&lt;T_i&gt; is true for all T_i in Types... 
