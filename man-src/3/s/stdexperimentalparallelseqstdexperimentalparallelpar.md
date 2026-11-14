---
title: "stdexperimentalparallelseqstdexperimentalparallelpar(3)"
name: "stdexperimentalparallelseqstdexperimentalparallelpar"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalparallelseqstdexperimentalparallelpar/"
---

std::experimental::parallel::seq,std::experimental::parallel::par, - std::experimental::parallel::seq,std::experimental::parallel::par,

<h2>Synopsis</h2>

Defined in header&nbsp;<wbr>&lt;experimental/execution_policy&gt; 
constexpr sequential_execution_policy seq{};&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(parallelism TS) 
constexpr parallel_execution_policy par{};&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(parallelism TS) 
constexpr parallel_vector_execution_policy par_vec{};&nbsp;<wbr>&nbsp;<wbr>(parallelism TS) 
seq, par and par_vec are instances of the execution policy types 
sequential_execution_policy, parallel_execution_policy and 
parallel_vector_execution_policy respectively. They are used to specify the 
execution policy of parallel algorithms - i.e., the kinds of parallelism allowed. 
