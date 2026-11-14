---
title: "stdexperimentalpropagate_constswap(3)"
name: "stdexperimentalpropagate_constswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constswap/"
---

std::experimental::propagate_const&lt;T&gt;::swap - std::experimental::propagate_const&lt;T&gt;::swap

<h2>Synopsis</h2>

constexpr void swap(propagate_const &amp; pt) noexcept(/* see below */); (library fundamentals TS v2) 
Swaps the wrapped pointer with that of pt. Let t_ designate the private data member that is the wrapped pointer-like object, then this function is equivalent to swap(t_, pt.t_). 

<h2>Parameters</h2>

pt - another propagate_const object to swap with

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(swap(t_, pt.t_)))
