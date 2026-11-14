---
title: "std_mu(3)"
name: "std_mu"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_mu/"
---

std::_Mu&lt; _Arg, _IsBindExp, _IsPlaceholder &gt; -

<h2>Synopsis</h2>



<h2>Detailed Description</h2>

<h3>template&lt;typename _Arg, bool _IsBindExp = is_bind_expression&lt;_Arg&gt;::value, bool _IsPlaceholder = (is_placeholder&lt;_Arg&gt;::value &gt; 0)&gt;class std::_Mu&lt; _Arg, _IsBindExp, _IsPlaceholder &gt;</h3>

Maps an argument to bind() into an actual argument to the bound function object [TR1 3.6.3/5]. Only the first parameter should be specified: the rest are used to determine among the various implementations. Note that, although this class is a function object, it isn't entirely normal because it takes only two parameters regardless of the number of parameters passed to the bind expression. The first parameter is the bound argument and the second parameter is a tuple containing references to the rest of the arguments. 

 Definition at line 1103 of file functional.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
