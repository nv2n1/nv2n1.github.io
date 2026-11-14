---
title: "stdexecutionseqstdexecutionparstdexecutionpar_unseqstdexecutionunseq(3)"
name: "stdexecutionseqstdexecutionparstdexecutionpar_unseqstdexecutionunseq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexecutionseqstdexecutionparstdexecutionpar_unseqstdexecutionunseq/"
---

std::execution::seq,std::execution::par,std::execution::par_unseq,std::execution::unseq - std::execution::seq,std::execution::par,std::execution::par_unseq,std::execution::unseq

<h2>Synopsis</h2>

Defined in header &lt;execution&gt; 
inline constexpr std::execution::sequenced_policy seq { /* unspecified */ }; <i>(since C++17)</i> 
inline constexpr std::execution::parallel_policy par { /* unspecified */ }; <i>(since C++17)</i> 
inline constexpr std::execution::parallel_unsequenced_policy par_unseq { /* unspecified */ }; <i>(since C++17)</i> 
inline constexpr std::execution::unsequenced_policy unseq { /* unspecified */ }; <i>(since C++20)</i> 
std::execution::seq, std::execution::par, std::execution::par_unseq, and std::execution::unseq are instances of the execution policy types std::execution::sequenced_policy, std::execution::parallel_policy, std::execution::parallel_unsequenced_policy, and std::execution::unsequenced_policy respectively. They are used to specify the execution policy of parallel algorithms - i.e., the kinds of parallelism allowed. 
Additional execution policies may be provided by a standard library implementation (possible future additions may include std::parallel::cuda and std::parallel::opencl) 

<h2>See also</h2>

sequenced_policy 
parallel_policy 
parallel_unsequenced_policy 
unsequenced_policy execution policy types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
(C++20) 
