---
title: "stdfeupdateenv(3)"
name: "stdfeupdateenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfeupdateenv/"
---

std::feupdateenv - std::feupdateenv

<h2>Synopsis</h2>

Defined in header &lt;cfenv&gt; 
int feupdateenv( const std::fenv_t* envp ) <i>(since C++11)</i> 
First, remembers the currently raised floating-point exceptions, then restores the floating-point environment from the object pointed to by envp (similar to std::fesetenv), then raises the floating-point exceptions that were saved. 
This function may be used to end the non-stop mode established by an earlier call to std::feholdexcept. 

<h2>Parameters</h2>

envp - pointer to the object of type std::fenv_t set by an earlier call to std::feholdexcept or std::fegetenv or equal to FE_DFL_ENV

<h2>Return value</h2>

0 on success, non-zero otherwise. 

<h2>See also</h2>

feholdexcept saves the environment, clears all status flags and ignores all future errors 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
fegetenv saves or restores the current floating point environment 
fesetenv <i>(function)</i> 
<i>(C++11)</i> 
FE_DFL_ENV default floating-point environment 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(macro constant) 
<i>(C++11)</i> 
