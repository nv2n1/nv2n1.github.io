---
title: "stdfegetenvstdfesetenv(3)"
name: "stdfegetenvstdfesetenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfegetenvstdfesetenv/"
description: "std::fegetenv,std::fesetenv – std::fegetenv,std::fesetenv"
---

<p>std::fegetenv,std::fesetenv &#8211; std::fegetenv,std::fesetenv</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cfenv&gt;<br />
int fegetenv( std::fenv_t* envp ) <code>(1)</code> <i>(since C++11)</i><br />
int fesetenv( const std::fenv_t* envp ); <code>(2)</code> <i>(since C++11)</i><br />
Manages the status of the floating-point environment.<br />
1) Attempts to store the status of the floating-point environment in the object pointed to by envp.<br />
2) Attempts to establish the floating-point environment from the object pointed to by envp. The value of that object must be previously obtained by a call to std::feholdexcept or std::fegetenv or be a floating-point macro constant. If any of the floating-point status flags are set in envp, they become set in the environment (and are then testable with std::fetestexcept), but the corresponding floating-point exceptions are not raised (execution continues uninterrupted) </p>
<h2>Parameters</h2>
<p>envp &#8211; pointer to the object of type std::fenv_t which holds the status of the floating-point environment</p>
<h2>Return value</h2>
<p>0 on success, non-zero otherwise. </p>
<h2>See also</h2>
<p>feholdexcept saves the environment, clears all status flags and ignores all future errors<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
feupdateenv restores the floating-point environment and raises the previously raise exceptions<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
FE_DFL_ENV default floating-point environment<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(macro constant)<br />
<i>(C++11)</i> </p>
