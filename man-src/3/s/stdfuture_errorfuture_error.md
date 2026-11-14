---
title: "stdfuture_errorfuture_error(3)"
name: "stdfuture_errorfuture_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuture_errorfuture_error/"
---

std::future_error::future_error - std::future_error::future_error

<h2>Synopsis</h2>

explicit future_error( std::future_errc ec ); <i>(since C++17)</i> 
Constructs a new future error object containing the error code std::make_error_code(ec). 

<h2>Parameters</h2>

ec - error code

<h2>Notes</h2>

There is no standard-compliant way for the user to construct a future_error prior to C++17. C++11 and C++14 depict an exposition-only public constructor taking a std::error_code, and some implementations provide such a constructor. 
