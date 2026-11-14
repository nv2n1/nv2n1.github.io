---
title: "stdunexpected(3)"
name: "stdunexpected"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunexpected/"
description: "std::unexpected – std::unexpected"
---

<p>std::unexpected &#8211; std::unexpected</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;exception&gt;<br />
void unexpected(); <i>(until C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i><br />
[[noreturn]] void unexpected(); <code>(deprecated)</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++17)<br />
std::unexpected() is called by the C++ runtime when a dynamic_exception_specification is violated: an exception is thrown from a function whose exception specification forbids exceptions of this type.<br />
std::unexpected() may also be called directly from the program.<br />
In either case, std::unexpected calls the currently installed std::unexpected_handler. The default std::unexpected_handler calls std::terminate.<br />
If a destructor reset the unexpected handler during stack unwinding and the unwinding later led to unexpected being called, the handler that was installed at the end of the throw expression is the one that will be called. (note: it was ambiguous whether re-throwing applied the new handlers) <i>(until C++11)</i><br />
If a destructor reset the unexpected handler during stack unwinding, it is unspecified which handler is called if the unwinding later led to unexpected being called. <i>(since C++11)</i> </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Exceptions</h2>
<p>Throw any exception thrown by the currently installed std::unexpected_handler </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_2111 C++11 effect of calling set_unexpected during stack unwinding differs from C++98 and breaks some ABIs made unspecified</p>
<h2>See also</h2>
<p>unexpected_handler the type of the function called by std::unexpected<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i><br />
(removed in C++17) </p>
