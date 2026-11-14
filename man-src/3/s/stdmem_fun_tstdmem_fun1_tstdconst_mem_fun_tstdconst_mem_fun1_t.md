---
title: "stdmem_fun_tstdmem_fun1_tstdconst_mem_fun_tstdconst_mem_fun1_t(3)"
name: "stdmem_fun_tstdmem_fun1_tstdconst_mem_fun_tstdconst_mem_fun1_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmem_fun_tstdmem_fun1_tstdconst_mem_fun_tstdconst_mem_fun1_t/"
---

std::mem_fun_t,std::mem_fun1_t,std::const_mem_fun_t,std::const_mem_fun1_t - std::mem_fun_t,std::mem_fun1_t,std::const_mem_fun_t,std::const_mem_fun1_t

<h2>Synopsis</h2>

<pre><code>template &lt;class S, class T&gt;

class mem_fun_t : public unary_function&lt;T *, S&gt;
{

  public:
    (1)(deprecated in C++ 11)

        explicit mem_fun_t(S (T::*p)());
    (removed in C++ 17)

        S
        operator()(T *p) const;
};

template &lt;class S, class T&gt;

class const_mem_fun_t : public unary_function&lt;const T *, S&gt;
{

  public:
    (2)(deprecated in C++ 11)

        explicit const_mem_fun_t(S (T::*p)() const);
    (removed in C++ 17)

        S
        operator()(const T *p) const;
};

template &lt;class S, class T, class Arg&gt;

class mem_fun1_t : public binary_function&lt;T *, A, S&gt;
{

  public:
    (3)(deprecated in C++ 11)

        explicit mem_fun1_t(S (T::*p)(A));
    (removed in C++ 17)

        S
        operator()(T *p, A x) const;
};

template &lt;class S, class T, class A&gt;

class const_mem_fun1_t : public binary_function&lt;const T *, A, S&gt;
{

  public:
    (4)(deprecated in C++ 11)

        explicit const_mem_fun1_t(S (T::*p)(A) const);
    (removed in C++ 17)

        S
        operator()(const T *p, A x) const;
};</code></pre> 
Wrapper around a member function pointer. The class instance whose member function to call is passed as a pointer to the operator(). 
1) Wraps a non-const member function with no parameters. 
2) Wraps a const member function with no parameters. 
3) Wraps a non-const member function with a single parameter. 
4) Wraps a const member function with a single parameter. 

<h2>See also</h2>

mem_fun creates a wrapper from a pointer to member function, callable with a pointer to object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
mem_fun_ref_t 
mem_fun1_ref_t 
const_mem_fun_ref_t wrapper for a pointer to nullary or unary member function, callable with a reference to object 
const_mem_fun1_ref_t <i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
