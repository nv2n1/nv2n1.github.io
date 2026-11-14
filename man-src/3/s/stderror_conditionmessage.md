---
title: "stderror_conditionmessage(3)"
name: "stderror_conditionmessage"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_conditionmessage/"
---

std::error_condition::message - std::error_condition::message

<h2>Synopsis</h2>

std::string message() const; <i>(since C++11)</i> 
Returns an explanatory message for the stored error code and error category. Effectively calls category().message(value()). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

An explanatory message for the stored error code and error category. 

<h2>Exceptions</h2>

<i>(none)</i>
