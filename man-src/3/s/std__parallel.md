---
title: "std__parallel(3)"
name: "std__parallel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__parallel/"
---

std::__parallel -

<h2>Synopsis</h2>



<h3>Classes</h3>

<pre><code>struct _CRandNumber



Functions
template&lt;typename _IIter , typename _Tp , typename _Tag &gt; _Tp __accumulate_switch (_IIter, _IIter, _Tp, _Tag)



template&lt;typename _IIter , typename _Tp , typename _IteratorTag &gt; _Tp __accumulate_switch (_IIter __begin, _IIter __end, _Tp __init, _IteratorTag)



template&lt;typename _IIter , typename _Tp , typename _BinaryOper , typename _Tag &gt; _Tp __accumulate_switch (_IIter, _IIter, _Tp, _BinaryOper, _Tag)



template&lt;typename _IIter , typename _Tp , typename _BinaryOperation , typename _IteratorTag &gt; _Tp __accumulate_switch (_IIter __begin, _IIter __end, _Tp __init, _BinaryOperation __binary_op, _IteratorTag)



template&lt;typename _RAIter , typename _Tp , typename _BinaryOper &gt; _Tp __accumulate_switch (_RAIter, _RAIter, _Tp, _BinaryOper, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism=__gnu_parallel::parallel_unbalanced)



template&lt;typename __RAIter , typename _Tp , typename _BinaryOperation &gt; _Tp __accumulate_switch (__RAIter __begin, __RAIter __end, _Tp __init, _BinaryOperation __binary_op, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_unbalanced)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper , typename _Tag1 , typename _Tag2 &gt; _OIter __adjacent_difference_switch (_IIter, _IIter, _OIter, _BinaryOper, _Tag1, _Tag2)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter __adjacent_difference_switch (_IIter, _IIter, _OIter, _BinaryOper, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism=__gnu_parallel::parallel_unbalanced)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation , typename _IteratorTag1 , typename _IteratorTag2 &gt; _OutputIterator __adjacent_difference_switch (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __bin_op, _IteratorTag1, _IteratorTag2)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator __adjacent_difference_switch (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __bin_op, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _FIter , typename _IterTag &gt; _FIter __adjacent_find_switch (_FIter, _FIter, _IterTag)



template&lt;typename _FIter , typename _BiPredicate , typename _IterTag &gt; _FIter __adjacent_find_switch (_FIter, _FIter, _BiPredicate, _IterTag)



template&lt;typename _RAIter , typename _BiPredicate &gt; _RAIter __adjacent_find_switch (_RAIter, _RAIter, _BiPredicate, random_access_iterator_tag)



template&lt;typename _RAIter &gt; _RAIter __adjacent_find_switch (_RAIter __begin, _RAIter __end, random_access_iterator_tag)



template&lt;typename _FIterator , typename _IteratorTag &gt; _FIterator __adjacent_find_switch (_FIterator __begin, _FIterator __end, _IteratorTag)



template&lt;typename _FIterator , typename _BinaryPredicate , typename _IteratorTag &gt; _FIterator __adjacent_find_switch (_FIterator __begin, _FIterator __end, _BinaryPredicate __pred, _IteratorTag)



template&lt;typename _RAIter , typename _BinaryPredicate &gt; _RAIter __adjacent_find_switch (_RAIter __begin, _RAIter __end, _BinaryPredicate __pred, random_access_iterator_tag)



template&lt;typename _IIter , typename _Predicate , typename _IterTag &gt; iterator_traits&lt; _IIter &gt;


::difference_type __count_if_switch (_IIter, _IIter, _Predicate, _IterTag)&quot;


template&lt;typename _RAIter , typename _Predicate &gt; iterator_traits&lt; _RAIter &gt;


::difference_type __count_if_switch (_RAIter __begin, _RAIter __end, _Predicate __pred, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_unbalanced)&quot;


template&lt;typename _IIter , typename _Predicate , typename _IteratorTag &gt; iterator_traits&lt; _IIter &gt;


::difference_type __count_if_switch (_IIter __begin, _IIter __end, _Predicate __pred, _IteratorTag)&quot;


template&lt;typename _IIter , typename _Tp , typename _IterTag &gt; iterator_traits&lt; _IIter &gt;


::difference_type __count_switch (_IIter, _IIter, const _Tp &amp;, _IterTag)&quot;


template&lt;typename _RAIter , typename _Tp &gt; iterator_traits&lt; _RAIter &gt;


::difference_type __count_switch (_RAIter __begin, _RAIter __end, const _Tp &amp;__value, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_unbalanced)&quot;


template&lt;typename _IIter , typename _Tp , typename _IteratorTag &gt; iterator_traits&lt; _IIter &gt;


::difference_type __count_switch (_IIter __begin, _IIter __end, const _Tp &amp;__value, _IteratorTag)&quot;


template&lt;typename _IIter , typename _FIter , typename _IterTag1 , typename _IterTag2 &gt; _IIter __find_first_of_switch (_IIter, _IIter, _FIter, _FIter, _IterTag1, _IterTag2)



template&lt;typename _RAIter , typename _FIter , typename _BiPredicate , typename _IterTag &gt; _RAIter __find_first_of_switch (_RAIter, _RAIter, _FIter, _FIter, _BiPredicate, random_access_iterator_tag, _IterTag)



template&lt;typename _IIter , typename _FIter , typename _BiPredicate , typename _IterTag1 , typename _IterTag2 &gt; _IIter __find_first_of_switch (_IIter, _IIter, _FIter, _FIter, _BiPredicate, _IterTag1, _IterTag2)



template&lt;typename _IIter , typename _FIterator , typename _IteratorTag1 , typename _IteratorTag2 &gt; _IIter __find_first_of_switch (_IIter __begin1, _IIter __end1, _FIterator __begin2, _FIterator __end2, _IteratorTag1, _IteratorTag2)



template&lt;typename _RAIter , typename _FIterator , typename _BinaryPredicate , typename _IteratorTag &gt; _RAIter __find_first_of_switch (_RAIter __begin1, _RAIter __end1, _FIterator __begin2, _FIterator __end2, _BinaryPredicate __comp, random_access_iterator_tag, _IteratorTag)



template&lt;typename _IIter , typename _FIterator , typename _BinaryPredicate , typename _IteratorTag1 , typename _IteratorTag2 &gt; _IIter __find_first_of_switch (_IIter __begin1, _IIter __end1, _FIterator __begin2, _FIterator __end2, _BinaryPredicate __comp, _IteratorTag1, _IteratorTag2)



template&lt;typename _IIter , typename _Predicate , typename _IterTag &gt; _IIter __find_if_switch (_IIter, _IIter, _Predicate, _IterTag)



template&lt;typename _IIter , typename _Predicate , typename _IteratorTag &gt; _IIter __find_if_switch (_IIter __begin, _IIter __end, _Predicate __pred, _IteratorTag)



template&lt;typename _RAIter , typename _Predicate &gt; _RAIter __find_if_switch (_RAIter __begin, _RAIter __end, _Predicate __pred, random_access_iterator_tag)



template&lt;typename _IIter , typename _Tp , typename _IteratorTag &gt; _IIter __find_switch (_IIter __begin, _IIter __end, const _Tp &amp;__val, _IteratorTag)



template&lt;typename _RAIter , typename _Tp &gt; _RAIter __find_switch (_RAIter __begin, _RAIter __end, const _Tp &amp;__val, random_access_iterator_tag)



template&lt;typename _IIter , typename _Tp , typename _IterTag &gt; _IIter __find_switch (_IIter, _IIter, const _Tp &amp;, _IterTag)



template&lt;typename _IIter , typename _Function , typename _IteratorTag &gt; _Function __for_each_switch (_IIter __begin, _IIter __end, _Function __f, _IteratorTag)



template&lt;typename _RAIter , typename _Function &gt; _Function __for_each_switch (_RAIter __begin, _RAIter __end, _Function __f, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _IIter , typename _Function , typename _IterTag &gt; _Function __for_each_switch (_IIter, _IIter, _Function, _IterTag)



template&lt;typename _OIter , typename _Size , typename _Generator , typename _IterTag &gt; _OIter __generate_n_switch (_OIter, _Size, _Generator, _IterTag)



template&lt;typename _OutputIterator , typename _Size , typename _Generator , typename _IteratorTag &gt; _OutputIterator __generate_n_switch (_OutputIterator __begin, _Size __n, _Generator __gen, _IteratorTag)



template&lt;typename _RAIter , typename _Size , typename _Generator &gt; _RAIter __generate_n_switch (_RAIter __begin, _Size __n, _Generator __gen, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _FIter , typename _Generator , typename _IterTag &gt; void __generate_switch (_FIter, _FIter, _Generator, _IterTag)



template&lt;typename _FIterator , typename _Generator , typename _IteratorTag &gt; void __generate_switch (_FIterator __begin, _FIterator __end, _Generator __gen, _IteratorTag)



template&lt;typename _RAIter , typename _Generator &gt; void __generate_switch (_RAIter __begin, _RAIter __end, _Generator __gen, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Tp , typename BinaryFunction1 , typename BinaryFunction2 &gt; _Tp __inner_product_switch (_RAIter1, _RAIter1, _RAIter2, _Tp, BinaryFunction1, BinaryFunction2, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism=__gnu_parallel::parallel_unbalanced)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp , typename _BinaryFunction1 , typename _BinaryFunction2 , typename _Tag1 , typename _Tag2 &gt; _Tp __inner_product_switch (_IIter1, _IIter1, _IIter2, _Tp, _BinaryFunction1, _BinaryFunction2, _Tag1, _Tag2)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Tp , typename _BinaryFunction1 , typename _BinaryFunction2 &gt; _Tp __inner_product_switch (_RAIter1 __first1, _RAIter1 __last1, _RAIter2 __first2, _Tp __init, _BinaryFunction1 __binary_op1, _BinaryFunction2 __binary_op2, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_unbalanced)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp , typename _BinaryFunction1 , typename _BinaryFunction2 , typename _IteratorTag1 , typename _IteratorTag2 &gt; _Tp __inner_product_switch (_IIter1 __first1, _IIter1 __last1, _IIter2 __first2, _Tp __init, _BinaryFunction1 __binary_op1, _BinaryFunction2 __binary_op2, _IteratorTag1, _IteratorTag2)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _IteratorTag1 , typename _IteratorTag2 &gt; bool __lexicographical_compare_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _Predicate __pred, _IteratorTag1, _IteratorTag2)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Predicate &gt; bool __lexicographical_compare_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _IterTag1 , typename _IterTag2 &gt; bool __lexicographical_compare_switch (_IIter1, _IIter1, _IIter2, _IIter2, _Predicate, _IterTag1, _IterTag2)



template&lt;typename _FIter , typename _Compare , typename _IterTag &gt; _FIter __max_element_switch (_FIter, _FIter, _Compare, _IterTag)



template&lt;typename _FIterator , typename _Compare , typename _IteratorTag &gt; _FIterator __max_element_switch (_FIterator __begin, _FIterator __end, _Compare __comp, _IteratorTag)



template&lt;typename _RAIter , typename _Compare &gt; _RAIter __max_element_switch (_RAIter __begin, _RAIter __end, _Compare __comp, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Compare , typename _IterTag1 , typename _IterTag2 , typename _IterTag3 &gt; _OIter __merge_switch (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Compare, _IterTag1, _IterTag2, _IterTag3)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Compare &gt; _OIter __merge_switch (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Compare, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Compare , typename _IteratorTag1 , typename _IteratorTag2 , typename _IteratorTag3 &gt; _OutputIterator __merge_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Compare __comp, _IteratorTag1, _IteratorTag2, _IteratorTag3)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Compare &gt; _OutputIterator __merge_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Compare __comp, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _FIter , typename _Compare , typename _IterTag &gt; _FIter __min_element_switch (_FIter, _FIter, _Compare, _IterTag)



template&lt;typename _FIterator , typename _Compare , typename _IteratorTag &gt; _FIterator __min_element_switch (_FIterator __begin, _FIterator __end, _Compare __comp, _IteratorTag)



template&lt;typename _RAIter , typename _Compare &gt; _RAIter __min_element_switch (_RAIter __begin, _RAIter __end, _Compare __comp, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _IteratorTag1 , typename _IteratorTag2 &gt; pair&lt; _IIter1, _IIter2 &gt; __mismatch_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _Predicate __pred, _IteratorTag1, _IteratorTag2)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Predicate &gt; pair&lt; _RAIter1, _RAIter2 &gt; __mismatch_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _IterTag1 , typename _IterTag2 &gt; pair&lt; _IIter1, _IIter2 &gt; __mismatch_switch (_IIter1, _IIter1, _IIter2, _Predicate, _IterTag1, _IterTag2)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper , typename _Tag1 , typename _Tag2 &gt; _OIter __partial_sum_switch (_IIter, _IIter, _OIter, _BinaryOper, _Tag1, _Tag2)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter __partial_sum_switch (_IIter, _IIter, _OIter, _BinaryOper, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation , typename _IteratorTag1 , typename _IteratorTag2 &gt; _OutputIterator __partial_sum_switch (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __bin_op, _IteratorTag1, _IteratorTag2)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator __partial_sum_switch (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __bin_op, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _FIter , typename _Predicate , typename _IterTag &gt; _FIter __partition_switch (_FIter, _FIter, _Predicate, _IterTag)



template&lt;typename _FIterator , typename _Predicate , typename _IteratorTag &gt; _FIterator __partition_switch (_FIterator __begin, _FIterator __end, _Predicate __pred, _IteratorTag)



template&lt;typename _RAIter , typename _Predicate &gt; _RAIter __partition_switch (_RAIter __begin, _RAIter __end, _Predicate __pred, random_access_iterator_tag)



template&lt;typename _FIter , typename _Predicate , typename _Tp , typename _IterTag &gt; void __replace_if_switch (_FIter, _FIter, _Predicate, const _Tp &amp;, _IterTag)



template&lt;typename _FIterator , typename _Predicate , typename _Tp , typename _IteratorTag &gt; void __replace_if_switch (_FIterator __begin, _FIterator __end, _Predicate __pred, const _Tp &amp;__new_value, _IteratorTag)



template&lt;typename _RAIter , typename _Predicate , typename _Tp &gt; void __replace_if_switch (_RAIter __begin, _RAIter __end, _Predicate __pred, const _Tp &amp;__new_value, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _FIter , typename _Tp , typename _IterTag &gt; void __replace_switch (_FIter, _FIter, const _Tp &amp;, const _Tp &amp;, _IterTag)



template&lt;typename _FIterator , typename _Tp , typename _IteratorTag &gt; void __replace_switch (_FIterator __begin, _FIterator __end, const _Tp &amp;__old_value, const _Tp &amp;__new_value, _IteratorTag)



template&lt;typename _RAIter , typename _Tp &gt; void __replace_switch (_RAIter __begin, _RAIter __end, const _Tp &amp;__old_value, const _Tp &amp;__new_value, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _RAIter , typename _Integer , typename _Tp , typename _BiPredicate &gt; _RAIter __search_n_switch (_RAIter, _RAIter, _Integer, const _Tp &amp;, _BiPredicate, random_access_iterator_tag)



template&lt;typename _FIter , typename _Integer , typename _Tp , typename _BiPredicate , typename _IterTag &gt; _FIter __search_n_switch (_FIter, _FIter, _Integer, const _Tp &amp;, _BiPredicate, _IterTag)



template&lt;typename _RAIter , typename _Integer , typename _Tp , typename _BinaryPredicate &gt; _RAIter __search_n_switch (_RAIter __begin, _RAIter __end, _Integer __count, const _Tp &amp;__val, _BinaryPredicate __binary_pred, random_access_iterator_tag)



template&lt;typename _FIterator , typename _Integer , typename _Tp , typename _BinaryPredicate , typename _IteratorTag &gt; _FIterator __search_n_switch (_FIterator __begin, _FIterator __end, _Integer __count, const _Tp &amp;__val, _BinaryPredicate __binary_pred, _IteratorTag)



template&lt;typename _FIter1 , typename _FIter2 , typename _IterTag1 , typename _IterTag2 &gt; _FIter1 __search_switch (_FIter1, _FIter1, _FIter2, _FIter2, _IterTag1, _IterTag2)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _BiPredicate &gt; _RAIter1 __search_switch (_RAIter1, _RAIter1, _RAIter2, _RAIter2, _BiPredicate, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _FIter1 , typename _FIter2 , typename _BiPredicate , typename _IterTag1 , typename _IterTag2 &gt; _FIter1 __search_switch (_FIter1, _FIter1, _FIter2, _FIter2, _BiPredicate, _IterTag1, _IterTag2)



template&lt;typename _RAIter1 , typename _RAIter2 &gt; _RAIter1 __search_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _FIterator1 , typename _FIterator2 , typename _IteratorTag1 , typename _IteratorTag2 &gt; _FIterator1 __search_switch (_FIterator1 __begin1, _FIterator1 __end1, _FIterator2 __begin2, _FIterator2 __end2, _IteratorTag1, _IteratorTag2)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _BinaryPredicate &gt; _RAIter1 __search_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, _BinaryPredicate __pred, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _FIterator1 , typename _FIterator2 , typename _BinaryPredicate , typename _IteratorTag1 , typename _IteratorTag2 &gt; _FIterator1 __search_switch (_FIterator1 __begin1, _FIterator1 __end1, _FIterator2 __begin2, _FIterator2 __end2, _BinaryPredicate __pred, _IteratorTag1, _IteratorTag2)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OutputIterator , typename _IteratorTag1 , typename _IteratorTag2 , typename _IteratorTag3 &gt; _OutputIterator __set_difference_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Predicate __pred, _IteratorTag1, _IteratorTag2, _IteratorTag3)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Output_RAIter , typename _Predicate &gt; _Output_RAIter __set_difference_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, _Output_RAIter __result, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OIter , typename _IterTag1 , typename _IterTag2 , typename _IterTag3 &gt; _OIter __set_difference_switch (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, _IterTag1, _IterTag2, _IterTag3)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OutputIterator , typename _IteratorTag1 , typename _IteratorTag2 , typename _IteratorTag3 &gt; _OutputIterator __set_intersection_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Predicate __pred, _IteratorTag1, _IteratorTag2, _IteratorTag3)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Output_RAIter , typename _Predicate &gt; _Output_RAIter __set_intersection_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, _Output_RAIter __result, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OIter , typename _IterTag1 , typename _IterTag2 , typename _IterTag3 &gt; _OIter __set_intersection_switch (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, _IterTag1, _IterTag2, _IterTag3)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OutputIterator , typename _IteratorTag1 , typename _IteratorTag2 , typename _IteratorTag3 &gt; _OutputIterator __set_symmetric_difference_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Predicate __pred, _IteratorTag1, _IteratorTag2, _IteratorTag3)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Output_RAIter , typename _Predicate &gt; _Output_RAIter __set_symmetric_difference_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, _Output_RAIter __result, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OIter , typename _IterTag1 , typename _IterTag2 , typename _IterTag3 &gt; _OIter __set_symmetric_difference_switch (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, _IterTag1, _IterTag2, _IterTag3)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OutputIterator , typename _IteratorTag1 , typename _IteratorTag2 , typename _IteratorTag3 &gt; _OutputIterator __set_union_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Predicate __pred, _IteratorTag1, _IteratorTag2, _IteratorTag3)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _Output_RAIter , typename _Predicate &gt; _Output_RAIter __set_union_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter2 __end2, _Output_RAIter __result, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate , typename _OIter , typename _IterTag1 , typename _IterTag2 , typename _IterTag3 &gt; _OIter __set_union_switch (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, _IterTag1, _IterTag2, _IterTag3)



template&lt;typename _IIter , typename _OIter , typename _UnaryOperation , typename _IterTag1 , typename _IterTag2 &gt; _OIter __transform1_switch (_IIter, _IIter, _OIter, _UnaryOperation, _IterTag1, _IterTag2)



template&lt;typename _RAIIter , typename _RAOIter , typename _UnaryOperation &gt; _RAOIter __transform1_switch (_RAIIter, _RAIIter, _RAOIter, _UnaryOperation, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism=__gnu_parallel::parallel_balanced)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _UnaryOperation &gt; _RAIter2 __transform1_switch (_RAIter1 __begin, _RAIter1 __end, _RAIter2 __result, _UnaryOperation __unary_op, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _UnaryOperation , typename _IteratorTag1 , typename _IteratorTag2 &gt; _RAIter2 __transform1_switch (_RAIter1 __begin, _RAIter1 __end, _RAIter2 __result, _UnaryOperation __unary_op, _IteratorTag1, _IteratorTag2)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _RAIter3 , typename _BiOperation &gt; _RAIter3 __transform2_switch (_RAIter1, _RAIter1, _RAIter2, _RAIter3, _BiOperation, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism=__gnu_parallel::parallel_balanced)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _BiOperation , typename _Tag1 , typename _Tag2 , typename _Tag3 &gt; _OIter __transform2_switch (_IIter1, _IIter1, _IIter2, _OIter, _BiOperation, _Tag1, _Tag2, _Tag3)



template&lt;typename _RAIter1 , typename _RAIter2 , typename _RAIter3 , typename _BinaryOperation &gt; _RAIter3 __transform2_switch (_RAIter1 __begin1, _RAIter1 __end1, _RAIter2 __begin2, _RAIter3 __result, _BinaryOperation __binary_op, random_access_iterator_tag, random_access_iterator_tag, random_access_iterator_tag, __gnu_parallel::_Parallelism __parallelism_tag=__gnu_parallel::parallel_balanced)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _BinaryOperation , typename _Tag1 , typename _Tag2 , typename _Tag3 &gt; _OutputIterator __transform2_switch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _OutputIterator __result, _BinaryOperation __binary_op, _Tag1, _Tag2, _Tag3)



template&lt;typename _IIter , typename _OutputIterator , typename _Predicate , typename _IteratorTag1 , typename _IteratorTag2 &gt; _OutputIterator __unique_copy_switch (_IIter __begin, _IIter __last, _OutputIterator __out, _Predicate __pred, _IteratorTag1, _IteratorTag2)



template&lt;typename _RAIter , typename RandomAccessOutputIterator , typename _Predicate &gt; RandomAccessOutputIterator __unique_copy_switch (_RAIter __begin, _RAIter __last, RandomAccessOutputIterator __out, _Predicate __pred, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter , typename _OIter , typename _Predicate , typename _IterTag1 , typename _IterTag2 &gt; _OIter __unique_copy_switch (_IIter, _IIter, _OIter, _Predicate, _IterTag1, _IterTag2)



template&lt;typename _RAIter , typename _RandomAccess_OIter , typename _Predicate &gt; _RandomAccess_OIter __unique_copy_switch (_RAIter, _RAIter, _RandomAccess_OIter, _Predicate, random_access_iterator_tag, random_access_iterator_tag)



template&lt;typename _IIter , typename _Tp &gt; _Tp accumulate (_IIter, _IIter, _Tp)



template&lt;typename _IIter , typename _Tp &gt; _Tp accumulate (_IIter, _IIter, _Tp, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _Tp &gt; _Tp accumulate (_IIter, _IIter, _Tp, __gnu_parallel::_Parallelism)



template&lt;typename _IIter , typename _Tp , typename _BinaryOper &gt; _Tp accumulate (_IIter, _IIter, _Tp, _BinaryOper)



template&lt;typename _IIter , typename _Tp , typename _BinaryOperation &gt; _Tp accumulate (_IIter __begin, _IIter __end, _Tp __init, _BinaryOperation __binary_op, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _Tp , typename _BinaryOper &gt; _Tp accumulate (_IIter, _IIter, _Tp, _BinaryOper, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _Tp , typename _BinaryOper &gt; _Tp accumulate (_IIter, _IIter, _Tp, _BinaryOper, __gnu_parallel::_Parallelism)



template&lt;typename _IIter , typename _Tp , typename _BinaryOperation &gt; _Tp accumulate (_IIter __begin, _IIter __end, _Tp __init, _BinaryOperation __binary_op, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _IIter , typename _Tp , typename _BinaryOperation &gt; _Tp accumulate (_IIter __begin, _IIter __end, _Tp __init, _BinaryOperation __binary_op)



template&lt;typename _IIter , typename _OIter &gt; _OIter adjacent_difference (_IIter, _IIter, _OIter)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter adjacent_difference (_IIter, _IIter, _OIter, _BinaryOper)



template&lt;typename _IIter , typename _OIter &gt; _OIter adjacent_difference (_IIter, _IIter, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter adjacent_difference (_IIter, _IIter, _OIter, _BinaryOper, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter &gt; _OIter adjacent_difference (_IIter, _IIter, _OIter, __gnu_parallel::_Parallelism)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter adjacent_difference (_IIter, _IIter, _OIter, _BinaryOper, __gnu_parallel::_Parallelism)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator adjacent_difference (_IIter __begin, _IIter __end, _OutputIterator __result, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator adjacent_difference (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __bin_op, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator adjacent_difference (_IIter __begin, _IIter __end, _OutputIterator __result, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator adjacent_difference (_IIter __begin, _IIter __end, _OutputIterator __result)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator adjacent_difference (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __binary_op, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator adjacent_difference (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __binary_op)



template&lt;typename _FIter &gt; _FIter adjacent_find (_FIter, _FIter)



template&lt;typename _FIter &gt; _FIter adjacent_find (_FIter, _FIter, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _BiPredicate &gt; _FIter adjacent_find (_FIter, _FIter, _BiPredicate)



template&lt;typename _FIter , typename _BiPredicate &gt; _FIter adjacent_find (_FIter, _FIter, _BiPredicate, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator &gt; _FIterator adjacent_find (_FIterator __begin, _FIterator __end, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _BinaryPredicate &gt; _FIterator adjacent_find (_FIterator __begin, _FIterator __end, _BinaryPredicate __binary_pred, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator &gt; _FIterator adjacent_find (_FIterator __begin, _FIterator __end)



template&lt;typename _FIterator , typename _BinaryPredicate &gt; _FIterator adjacent_find (_FIterator __begin, _FIterator __end, _BinaryPredicate __pred)



template&lt;typename _IIter , typename _Tp &gt; iterator_traits&lt; _IIter &gt;


::difference_type count (_IIter __begin, _IIter __end, const _Tp &amp;__value, __gnu_parallel::sequential_tag)&quot;


template&lt;typename _IIter , typename _Tp &gt; iterator_traits&lt; _IIter &gt;


::difference_type count (_IIter __begin, _IIter __end, const _Tp &amp;__value, __gnu_parallel::_Parallelism __parallelism_tag)&quot;


template&lt;typename _IIter , typename _Tp &gt; iterator_traits&lt; _IIter &gt;


::difference_type count (_IIter __begin, _IIter __end, const _Tp &amp;__value)&quot;


template&lt;typename _IIter , typename _Predicate &gt; iterator_traits&lt; _IIter &gt;


::difference_type count_if (_IIter __begin, _IIter __end, _Predicate __pred, __gnu_parallel::sequential_tag)&quot;


template&lt;typename _IIter , typename _Predicate &gt; iterator_traits&lt; _IIter &gt;


::difference_type count_if (_IIter __begin, _IIter __end, _Predicate __pred, __gnu_parallel::_Parallelism __parallelism_tag)&quot;


template&lt;typename _IIter , typename _Predicate &gt; iterator_traits&lt; _IIter &gt;


::difference_type count_if (_IIter __begin, _IIter __end, _Predicate __pred)&quot;


template&lt;typename _IIter1 , typename _IIter2 &gt; bool equal (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate &gt; bool equal (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 &gt; bool equal (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate &gt; bool equal (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _Predicate __pred)



template&lt;typename _IIter , typename _Tp &gt; _IIter find (_IIter __begin, _IIter __end, const _Tp &amp;__val, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _Tp &gt; _IIter find (_IIter __begin, _IIter __end, const _Tp &amp;__val)



template&lt;typename _IIter , typename _FIter &gt; _IIter find_first_of (_IIter, _IIter, _FIter, _FIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _FIter , typename _BiPredicate &gt; _IIter find_first_of (_IIter, _IIter, _FIter, _FIter, _BiPredicate, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _FIter , typename _BiPredicate &gt; _IIter find_first_of (_IIter, _IIter, _FIter, _FIter, _BiPredicate)



template&lt;typename _IIter , typename _FIter &gt; _IIter find_first_of (_IIter, _IIter, _FIter, _FIter)



template&lt;typename _IIter , typename _FIterator &gt; _IIter find_first_of (_IIter __begin1, _IIter __end1, _FIterator __begin2, _FIterator __end2, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _FIterator , typename _BinaryPredicate &gt; _IIter find_first_of (_IIter __begin1, _IIter __end1, _FIterator __begin2, _FIterator __end2, _BinaryPredicate __comp, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _FIterator , typename _BinaryPredicate &gt; _IIter find_first_of (_IIter __begin1, _IIter __end1, _FIterator __begin2, _FIterator __end2, _BinaryPredicate __comp)



template&lt;typename _IIter , typename _FIterator &gt; _IIter find_first_of (_IIter __begin1, _IIter __end1, _FIterator __begin2, _FIterator __end2)



template&lt;typename _IIter , typename _Predicate &gt; _IIter find_if (_IIter __begin, _IIter __end, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _Predicate &gt; _IIter find_if (_IIter __begin, _IIter __end, _Predicate __pred)



template&lt;typename _IIter , typename _Function &gt; _Function for_each (_IIter __begin, _IIter __end, _Function __f, __gnu_parallel::sequential_tag)



template&lt;typename _Iterator , typename _Function &gt; _Function for_each (_Iterator __begin, _Iterator __end, _Function __f, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _Iterator , typename _Function &gt; _Function for_each (_Iterator __begin, _Iterator __end, _Function __f)



template&lt;typename _IIter , typename _Function &gt; _Function for_each (_IIter, _IIter, _Function)



template&lt;typename _FIter , typename _Generator &gt; void generate (_FIter, _FIter, _Generator)



template&lt;typename _FIter , typename _Generator &gt; void generate (_FIter, _FIter, _Generator, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Generator &gt; void generate (_FIter, _FIter, _Generator, __gnu_parallel::_Parallelism)



template&lt;typename _FIterator , typename _Generator &gt; void generate (_FIterator __begin, _FIterator __end, _Generator __gen, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Generator &gt; void generate (_FIterator __begin, _FIterator __end, _Generator __gen, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator , typename _Generator &gt; void generate (_FIterator __begin, _FIterator __end, _Generator __gen)



template&lt;typename _OIter , typename _Size , typename _Generator &gt; _OIter generate_n (_OIter, _Size, _Generator)



template&lt;typename _OIter , typename _Size , typename _Generator &gt; _OIter generate_n (_OIter, _Size, _Generator, __gnu_parallel::sequential_tag)



template&lt;typename _OIter , typename _Size , typename _Generator &gt; _OIter generate_n (_OIter, _Size, _Generator, __gnu_parallel::_Parallelism)



template&lt;typename _OutputIterator , typename _Size , typename _Generator &gt; _OutputIterator generate_n (_OutputIterator __begin, _Size __n, _Generator __gen, __gnu_parallel::sequential_tag)



template&lt;typename _OutputIterator , typename _Size , typename _Generator &gt; _OutputIterator generate_n (_OutputIterator __begin, _Size __n, _Generator __gen, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _OutputIterator , typename _Size , typename _Generator &gt; _OutputIterator generate_n (_OutputIterator __begin, _Size __n, _Generator __gen)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp &gt; _Tp inner_product (_IIter1, _IIter1, _IIter2, _Tp)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp &gt; _Tp inner_product (_IIter1, _IIter1, _IIter2, _Tp, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp &gt; _Tp inner_product (_IIter1, _IIter1, _IIter2, _Tp, __gnu_parallel::_Parallelism)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp , typename _BinaryFunction1 , typename _BinaryFunction2 &gt; _Tp inner_product (_IIter1, _IIter1, _IIter2, _Tp, _BinaryFunction1, _BinaryFunction2)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp , typename _BinaryFunction1 , typename _BinaryFunction2 &gt; _Tp inner_product (_IIter1, _IIter1, _IIter2, _Tp, _BinaryFunction1, _BinaryFunction2, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp , typename BinaryFunction1 , typename BinaryFunction2 &gt; _Tp inner_product (_IIter1, _IIter1, _IIter2, _Tp, BinaryFunction1, BinaryFunction2, __gnu_parallel::_Parallelism)



template&lt;typename _IIter1 , typename _IIter2 , typename _Tp , typename _BinaryFunction1 , typename _BinaryFunction2 &gt; _Tp inner_product (_IIter1 __first1, _IIter1 __last1, _IIter2 __first2, _Tp __init, _BinaryFunction1 __binary_op1, _BinaryFunction2 __binary_op2, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _IIter1 , typename _IIter2 &gt; bool lexicographical_compare (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate &gt; bool lexicographical_compare (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 &gt; bool lexicographical_compare (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate &gt; bool lexicographical_compare (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _Predicate __pred)



template&lt;typename _FIter &gt; _FIter max_element (_FIter, _FIter)



template&lt;typename _FIter &gt; _FIter max_element (_FIter, _FIter, __gnu_parallel::sequential_tag)



template&lt;typename _FIter &gt; _FIter max_element (_FIter, _FIter, __gnu_parallel::_Parallelism)



template&lt;typename _FIter , typename _Compare &gt; _FIter max_element (_FIter, _FIter, _Compare)



template&lt;typename _FIter , typename _Compare &gt; _FIter max_element (_FIter, _FIter, _Compare, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Compare &gt; _FIter max_element (_FIter, _FIter, _Compare, __gnu_parallel::_Parallelism)



template&lt;typename _FIterator &gt; _FIterator max_element (_FIterator __begin, _FIterator __end, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Compare &gt; _FIterator max_element (_FIterator __begin, _FIterator __end, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator &gt; _FIterator max_element (_FIterator __begin, _FIterator __end, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator &gt; _FIterator max_element (_FIterator __begin, _FIterator __end)



template&lt;typename _FIterator , typename _Compare &gt; _FIterator max_element (_FIterator __begin, _FIterator __end, _Compare __comp, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator , typename _Compare &gt; _FIterator max_element (_FIterator __begin, _FIterator __end, _Compare __comp)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter merge (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Compare &gt; _OIter merge (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Compare, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Compare &gt; _OIter merge (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Compare)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter merge (_IIter1, _IIter1, _IIter2, _IIter2, _OIter)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator merge (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Compare &gt; _OutputIterator merge (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Compare &gt; _OutputIterator merge (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result, _Compare __comp)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator merge (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __result)



template&lt;typename _FIter &gt; _FIter min_element (_FIter, _FIter)



template&lt;typename _FIter &gt; _FIter min_element (_FIter, _FIter, __gnu_parallel::sequential_tag)



template&lt;typename _FIter &gt; _FIter min_element (_FIter, _FIter, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIter , typename _Compare &gt; _FIter min_element (_FIter, _FIter, _Compare)



template&lt;typename _FIter , typename _Compare &gt; _FIter min_element (_FIter, _FIter, _Compare, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Compare &gt; _FIter min_element (_FIter, _FIter, _Compare, __gnu_parallel::_Parallelism)



template&lt;typename _FIterator &gt; _FIterator min_element (_FIterator __begin, _FIterator __end, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Compare &gt; _FIterator min_element (_FIterator __begin, _FIterator __end, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator &gt; _FIterator min_element (_FIterator __begin, _FIterator __end, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator &gt; _FIterator min_element (_FIterator __begin, _FIterator __end)



template&lt;typename _FIterator , typename _Compare &gt; _FIterator min_element (_FIterator __begin, _FIterator __end, _Compare __comp, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator , typename _Compare &gt; _FIterator min_element (_FIterator __begin, _FIterator __end, _Compare __comp)



template&lt;typename _IIter1 , typename _IIter2 &gt; pair&lt; _IIter1, _IIter2 &gt; mismatch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate &gt; pair&lt; _IIter1, _IIter2 &gt; mismatch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 &gt; pair&lt; _IIter1, _IIter2 &gt; mismatch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2)



template&lt;typename _IIter1 , typename _IIter2 , typename _Predicate &gt; pair&lt; _IIter1, _IIter2 &gt; mismatch (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _Predicate __pred)



template&lt;typename _RAIter &gt; void nth_element (_RAIter __begin, _RAIter __nth, _RAIter __end, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare &gt; void nth_element (_RAIter __begin, _RAIter __nth, _RAIter __end, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare &gt; void nth_element (_RAIter __begin, _RAIter __nth, _RAIter __end, _Compare __comp)



template&lt;typename _RAIter &gt; void nth_element (_RAIter __begin, _RAIter __nth, _RAIter __end)



template&lt;typename _RAIter , typename _Compare &gt; void partial_sort (_RAIter __begin, _RAIter __middle, _RAIter __end, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter &gt; void partial_sort (_RAIter __begin, _RAIter __middle, _RAIter __end, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare &gt; void partial_sort (_RAIter __begin, _RAIter __middle, _RAIter __end, _Compare __comp)



template&lt;typename _RAIter &gt; void partial_sort (_RAIter __begin, _RAIter __middle, _RAIter __end)



template&lt;typename _IIter , typename _OIter &gt; _OIter partial_sum (_IIter, _IIter, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter partial_sum (_IIter, _IIter, _OIter, _BinaryOper, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter &gt; _OIter partial_sum (_IIter, _IIter, _OIter __result)



template&lt;typename _IIter , typename _OIter , typename _BinaryOper &gt; _OIter partial_sum (_IIter, _IIter, _OIter, _BinaryOper)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator partial_sum (_IIter __begin, _IIter __end, _OutputIterator __result, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator partial_sum (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __bin_op, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator partial_sum (_IIter __begin, _IIter __end, _OutputIterator __result)



template&lt;typename _IIter , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator partial_sum (_IIter __begin, _IIter __end, _OutputIterator __result, _BinaryOperation __binary_op)



template&lt;typename _FIter , typename _Predicate &gt; _FIter partition (_FIter, _FIter, _Predicate, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Predicate &gt; _FIter partition (_FIter, _FIter, _Predicate)



template&lt;typename _FIterator , typename _Predicate &gt; _FIterator partition (_FIterator __begin, _FIterator __end, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Predicate &gt; _FIterator partition (_FIterator __begin, _FIterator __end, _Predicate __pred)



template&lt;typename _RAIter &gt; void random_shuffle (_RAIter __begin, _RAIter __end, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _RandomNumberGenerator &gt; void random_shuffle (_RAIter __begin, _RAIter __end, _RandomNumberGenerator &amp;__rand, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter &gt; void random_shuffle (_RAIter __begin, _RAIter __end)



template&lt;typename _RAIter , typename _RandomNumberGenerator &gt; void random_shuffle (_RAIter __begin, _RAIter __end, _RandomNumberGenerator &amp;&amp;__rand)



template&lt;typename _FIter , typename _Tp &gt; void replace (_FIter, _FIter, const _Tp &amp;, const _Tp &amp;)



template&lt;typename _FIter , typename _Tp &gt; void replace (_FIter, _FIter, const _Tp &amp;, const _Tp &amp;, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Tp &gt; void replace (_FIter, _FIter, const _Tp &amp;, const _Tp &amp;, __gnu_parallel::_Parallelism)



template&lt;typename _FIterator , typename _Tp &gt; void replace (_FIterator __begin, _FIterator __end, const _Tp &amp;__old_value, const _Tp &amp;__new_value, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Tp &gt; void replace (_FIterator __begin, _FIterator __end, const _Tp &amp;__old_value, const _Tp &amp;__new_value, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator , typename _Tp &gt; void replace (_FIterator __begin, _FIterator __end, const _Tp &amp;__old_value, const _Tp &amp;__new_value)



template&lt;typename _FIter , typename _Predicate , typename _Tp &gt; void replace_if (_FIter, _FIter, _Predicate, const _Tp &amp;)



template&lt;typename _FIter , typename _Predicate , typename _Tp &gt; void replace_if (_FIter, _FIter, _Predicate, const _Tp &amp;, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Predicate , typename _Tp &gt; void replace_if (_FIter, _FIter, _Predicate, const _Tp &amp;, __gnu_parallel::_Parallelism)



template&lt;typename _FIterator , typename _Predicate , typename _Tp &gt; void replace_if (_FIterator __begin, _FIterator __end, _Predicate __pred, const _Tp &amp;__new_value, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Predicate , typename _Tp &gt; void replace_if (_FIterator __begin, _FIterator __end, _Predicate __pred, const _Tp &amp;__new_value, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _FIterator , typename _Predicate , typename _Tp &gt; void replace_if (_FIterator __begin, _FIterator __end, _Predicate __pred, const _Tp &amp;__new_value)



template&lt;typename _FIter1 , typename _FIter2 &gt; _FIter1 search (_FIter1, _FIter1, _FIter2, _FIter2, __gnu_parallel::sequential_tag)



template&lt;typename _FIter1 , typename _FIter2 &gt; _FIter1 search (_FIter1, _FIter1, _FIter2, _FIter2)



template&lt;typename _FIter1 , typename _FIter2 , typename _BiPredicate &gt; _FIter1 search (_FIter1, _FIter1, _FIter2, _FIter2, _BiPredicate, __gnu_parallel::sequential_tag)



template&lt;typename _FIter1 , typename _FIter2 , typename _BiPredicate &gt; _FIter1 search (_FIter1, _FIter1, _FIter2, _FIter2, _BiPredicate)



template&lt;typename _FIterator1 , typename _FIterator2 &gt; _FIterator1 search (_FIterator1 __begin1, _FIterator1 __end1, _FIterator2 __begin2, _FIterator2 __end2, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator1 , typename _FIterator2 &gt; _FIterator1 search (_FIterator1 __begin1, _FIterator1 __end1, _FIterator2 __begin2, _FIterator2 __end2)



template&lt;typename _FIterator1 , typename _FIterator2 , typename _BinaryPredicate &gt; _FIterator1 search (_FIterator1 __begin1, _FIterator1 __end1, _FIterator2 __begin2, _FIterator2 __end2, _BinaryPredicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator1 , typename _FIterator2 , typename _BinaryPredicate &gt; _FIterator1 search (_FIterator1 __begin1, _FIterator1 __end1, _FIterator2 __begin2, _FIterator2 __end2, _BinaryPredicate __pred)



template&lt;typename _FIter , typename _Integer , typename _Tp &gt; _FIter search_n (_FIter, _FIter, _Integer, const _Tp &amp;, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Integer , typename _Tp , typename _BiPredicate &gt; _FIter search_n (_FIter, _FIter, _Integer, const _Tp &amp;, _BiPredicate, __gnu_parallel::sequential_tag)



template&lt;typename _FIter , typename _Integer , typename _Tp &gt; _FIter search_n (_FIter, _FIter, _Integer, const _Tp &amp;)



template&lt;typename _FIter , typename _Integer , typename _Tp , typename _BiPredicate &gt; _FIter search_n (_FIter, _FIter, _Integer, const _Tp &amp;, _BiPredicate)



template&lt;typename _FIterator , typename _Integer , typename _Tp &gt; _FIterator search_n (_FIterator __begin, _FIterator __end, _Integer __count, const _Tp &amp;__val, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Integer , typename _Tp , typename _BinaryPredicate &gt; _FIterator search_n (_FIterator __begin, _FIterator __end, _Integer __count, const _Tp &amp;__val, _BinaryPredicate __binary_pred, __gnu_parallel::sequential_tag)



template&lt;typename _FIterator , typename _Integer , typename _Tp &gt; _FIterator search_n (_FIterator __begin, _FIterator __end, _Integer __count, const _Tp &amp;__val)



template&lt;typename _FIterator , typename _Integer , typename _Tp , typename _BinaryPredicate &gt; _FIterator search_n (_FIterator __begin, _FIterator __end, _Integer __count, const _Tp &amp;__val, _BinaryPredicate __binary_pred)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_intersection (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_intersection (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_intersection (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_intersection (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_intersection (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_intersection (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_intersection (_IIter1, _IIter1, _IIter2, _IIter2, _OIter)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_intersection (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_symmetric_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_symmetric_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_symmetric_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_symmetric_difference (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_symmetric_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_symmetric_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_symmetric_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_symmetric_difference (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_union (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_union (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator &gt; _OutputIterator set_union (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _Predicate &gt; _OutputIterator set_union (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _IIter2 __end2, _OutputIterator __out, _Predicate __pred)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_union (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_union (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter &gt; _OIter set_union (_IIter1, _IIter1, _IIter2, _IIter2, _OIter)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _Predicate &gt; _OIter set_union (_IIter1, _IIter1, _IIter2, _IIter2, _OIter, _Predicate)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare &gt; void sort (_RAIter __begin, _RAIter __end, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare , typename _Parallelism &gt; void sort (_RAIter __begin, _RAIter __end, _Compare __comp, _Parallelism __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::default_parallel_tag __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::parallel_tag __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::multiway_mergesort_tag __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::multiway_mergesort_sampling_tag __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::multiway_mergesort_exact_tag __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::quicksort_tag __parallelism)



template&lt;typename _RAIter &gt; void sort (_RAIter __begin, _RAIter __end, __gnu_parallel::balanced_quicksort_tag __parallelism)



template&lt;typename _RAIter , typename _Compare &gt; void sort (_RAIter __begin, _RAIter __end, _Compare __comp)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare &gt; void stable_sort (_RAIter __begin, _RAIter __end, _Compare __comp, __gnu_parallel::sequential_tag)



template&lt;typename _RAIter , typename _Compare , typename _Parallelism &gt; void stable_sort (_RAIter __begin, _RAIter __end, _Compare __comp, _Parallelism __parallelism)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end, __gnu_parallel::default_parallel_tag __parallelism)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end, __gnu_parallel::parallel_tag __parallelism)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end, __gnu_parallel::multiway_mergesort_tag __parallelism)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end, __gnu_parallel::quicksort_tag __parallelism)



template&lt;typename _RAIter &gt; void stable_sort (_RAIter __begin, _RAIter __end, __gnu_parallel::balanced_quicksort_tag __parallelism)



template&lt;typename _RAIter , typename _Compare &gt; void stable_sort (_RAIter __begin, _RAIter __end, _Compare __comp)



template&lt;typename _IIter , typename _OIter , typename _UnaryOperation &gt; _OIter transform (_IIter, _IIter, _OIter, _UnaryOperation)



template&lt;typename _IIter , typename _OIter , typename _UnaryOperation &gt; _OIter transform (_IIter, _IIter, _OIter, _UnaryOperation, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter , typename _UnaryOperation &gt; _OIter transform (_IIter, _IIter, _OIter, _UnaryOperation, __gnu_parallel::_Parallelism)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _BiOperation &gt; _OIter transform (_IIter1, _IIter1, _IIter2, _OIter, _BiOperation)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _BiOperation &gt; _OIter transform (_IIter1, _IIter1, _IIter2, _OIter, _BiOperation, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OIter , typename _BiOperation &gt; _OIter transform (_IIter1, _IIter1, _IIter2, _OIter, _BiOperation, __gnu_parallel::_Parallelism)



template&lt;typename _IIter , typename _OutputIterator , typename _UnaryOperation &gt; _OutputIterator transform (_IIter __begin, _IIter __end, _OutputIterator __result, _UnaryOperation __unary_op, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _UnaryOperation &gt; _OutputIterator transform (_IIter __begin, _IIter __end, _OutputIterator __result, _UnaryOperation __unary_op, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _UnaryOperation &gt; _OutputIterator transform (_IIter __begin, _IIter __end, _OutputIterator __result, _UnaryOperation __unary_op)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator transform (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _OutputIterator __result, _BinaryOperation __binary_op, __gnu_parallel::sequential_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator transform (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _OutputIterator __result, _BinaryOperation __binary_op, __gnu_parallel::_Parallelism __parallelism_tag)



template&lt;typename _IIter1 , typename _IIter2 , typename _OutputIterator , typename _BinaryOperation &gt; _OutputIterator transform (_IIter1 __begin1, _IIter1 __end1, _IIter2 __begin2, _OutputIterator __result, _BinaryOperation __binary_op)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator unique_copy (_IIter __begin1, _IIter __end1, _OutputIterator __out, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator , typename _Predicate &gt; _OutputIterator unique_copy (_IIter __begin1, _IIter __end1, _OutputIterator __out, _Predicate __pred, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OutputIterator &gt; _OutputIterator unique_copy (_IIter __begin1, _IIter __end1, _OutputIterator __out)



template&lt;typename _IIter , typename _OutputIterator , typename _Predicate &gt; _OutputIterator unique_copy (_IIter __begin1, _IIter __end1, _OutputIterator __out, _Predicate __pred)



template&lt;typename _IIter , typename _OIter &gt; _OIter unique_copy (_IIter, _IIter, _OIter, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter , typename _Predicate &gt; _OIter unique_copy (_IIter, _IIter, _OIter, _Predicate, __gnu_parallel::sequential_tag)



template&lt;typename _IIter , typename _OIter &gt; _OIter unique_copy (_IIter, _IIter, _OIter)



template&lt;typename _IIter , typename _OIter , typename _Predicate &gt; _OIter unique_copy (_IIter, _IIter, _OIter, _Predicate)</code></pre>

<h2>Detailed Description</h2>

GNU parallel code, replaces standard behavior with parallel behavior.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
