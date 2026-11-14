---
title: "stdexperimentalparallelseqstdexperimentalparallelparstdexperimentalparallelpar_vec(3)"
name: "stdexperimentalparallelseqstdexperimentalparallelparstdexperimentalparallelpar_vec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalparallelseqstdexperimentalparallelparstdexperimentalparallelpar_vec/"
---

std::experimental::parallel::seq,std::experimental::parallel::par,std::experimental::parallel::par_vec - std::experimental::parallel::seq,std::experimental::parallel::par,std::experimental::parallel::par_vec

<h2>Synopsis</h2>

Defined in header &lt;experimental/execution_policy&gt; 
constexpr sequential_execution_policy seq{}; (parallelism TS) 
constexpr parallel_execution_policy par{}; (parallelism TS) 
constexpr parallel_vector_execution_policy par_vec{}; (parallelism TS) 
seq, par and par_vec are instances of the execution policy types sequential_execution_policy, parallel_execution_policy and parallel_vector_execution_policy respectively. They are used to specify the execution policy of parallel algorithms - i.e., the kinds of parallelism allowed. 
