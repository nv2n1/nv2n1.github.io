---
title: "stdthreadthread(3)"
name: "stdthreadthread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadthread/"
---

std::thread::~thread - std::thread::~thread

<h2>Synopsis</h2>

~thread(); <i>(since C++11)</i> 
Destroys the thread object. 
If *this has an associated thread (joinable() == true), std::terminate() is called. 

<h2>Notes</h2>

A thread object does not have an associated thread (and is safe to destroy) after 
* it was default-constructed 
* it was moved from 
* join() has been called 
* detach() has been called 
