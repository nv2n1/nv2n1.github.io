---
title: "stdchronotzdb_listendstdchronotzdb_listcend(3)"
name: "stdchronotzdb_listendstdchronotzdb_listcend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdb_listendstdchronotzdb_listcend/"
---

std::chrono::tzdb_list::end,std::chrono::tzdb_list::cend - std::chrono::tzdb_list::end,std::chrono::tzdb_list::cend

<h2>Synopsis</h2>

const_iterator end() const noexcept; <i>(since C++20)</i> 
const_iterator cend() const noexcept; <i>(since C++20)</i> 
Returns the past-the-end iterator of the tzdb_list. Attempting to dereference this iterator results in undefined behavior. 

<h2>Return value</h2>

The past-the-end iterator. 
