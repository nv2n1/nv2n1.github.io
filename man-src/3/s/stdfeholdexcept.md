---
title: "stdfeholdexcept(3)"
name: "stdfeholdexcept"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfeholdexcept/"
---

std::feholdexcept - std::feholdexcept

<h2>Synopsis</h2>

Defined in header &lt;cfenv&gt; 
int feholdexcept( std::fenv_t* envp ) <i>(since C++11)</i> 
First, saves the current floating-point environment to the object pointed to by envp (similar to std::fegetenv), then clears all floating-point status flags, and then installs the non-stop mode: future floating-point exceptions will not interrupt execution (will not trap), until the floating-point environment is restored by std::feupdateenv or std::fesetenv. 
This function may be used in the beginning of a subroutine that must hide the floating-point exceptions it may raise from the caller. If only some exceptions must be suppressed, while others must be reported, the non-stop mode is usually ended with a call to std::feupdateenv after clearing the unwanted exceptions. 

<h2>Parameters</h2>

envp - pointer to the object of type std::fenv_t where the floating-point environment will be stored

<h2>Return value</h2>

0 on success, non-zero otherwise. 

<h2>See also</h2>

feupdateenv restores the floating-point environment and raises the previously raise exceptions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
fegetenv saves or restores the current floating point environment 
fesetenv <i>(function)</i> 
<i>(C++11)</i> 
FE_DFL_ENV default floating-point environment 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(macro constant) 
<i>(C++11)</i> 
