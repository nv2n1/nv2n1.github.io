---
title: "stdfegetexceptflagstdfesetexceptflag(3)"
name: "stdfegetexceptflagstdfesetexceptflag"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfegetexceptflagstdfesetexceptflag/"
description: "std::fegetexceptflag,std::fesetexceptflag – std::fegetexceptflag,std::fesetexceptflag"
---

<p>std::fegetexceptflag,std::fesetexceptflag &#8211; std::fegetexceptflag,std::fesetexceptflag</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cfenv&gt;<br />
int fegetexceptflag( std::fexcept_t* flagp, int excepts ); <code>(1)</code> <i>(since C++11)</i><br />
int fesetexceptflag( const std::fexcept_t* flagp, int excepts ); <code>(2)</code> <i>(since C++11)</i><br />
1) Attempts to obtain the full contents of the floating-point exception flags that are listed in the bitmask argument excepts, which is a bitwise OR of the floating_point_exception_macros.<br />
2) Attempts to copy the full contents of the floating-point exception flags that are listed in excepts from flagp into the floating-point environment. Does not raise any exceptions, only modifies the flags.<br />
The full contents of a floating-point exception flag is not necessarily a boolean value indicating whether the exception is raised or cleared. For example, it may be a struct which includes the boolean status and the address of the code that triggered the exception. These functions obtain all such content and obtain/store it in flagp in implementation-defined format. </p>
<h2>Parameters</h2>
<p>flagp &#8211; pointer to an std::fexcept_t object where the flags will be stored or read from<br />
excepts &#8211; bitmask listing the exception flags to get/set</p>
<h2>Return value</h2>
<p>0 on success, non-zero otherwise. </p>
<h2>See Also</h2>
