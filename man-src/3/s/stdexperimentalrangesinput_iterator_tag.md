---
title: "stdexperimentalrangesinput_iterator_tag(3)"
name: "stdexperimentalrangesinput_iterator_tag"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesinput_iterator_tag/"
---

std::experimental::ranges::input_iterator_tag, - std::experimental::ranges::input_iterator_tag,

<h2>Synopsis</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::experimental::ranges::forward_iterator_tag, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::experimental::ranges::bidirectional_iterator_tag, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::experimental::ranges::random_access_iterator_tag <pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    struct input_iterator_tag {
};

struct output_iterator_tag {
};

struct forward_iterator_tag : public input_iterator_tag {
};

struct bidirectional_iterator_tag : public forward_iterator_tag {
};

struct random_access_iterator_tag : public bidirectional_iterator_tag {
};</code></pre> 
Defines the category of an iterator. Each tag is an empty type and corresponds to 
one of the five iterator categories: 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>input_iterator_tag corresponds to InputIterator. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>forward_iterator_tag corresponds to ForwardIterator. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>bidirectional_iterator_tag corresponds to BidirectionalIterator. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>random_access_iterator_tag corresponds to RandomAccessIterator. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>output_iterator_tag corresponds to OutputIterator;&nbsp;<wbr>it is not used and provided 
&nbsp;<wbr>solely for backward compatiblity. 
Iterator category tags carry information that can be used to select the most 
efficient algorithms for the specific requirement set that is implied by the 
category. However, concept-based overloading is preferred. 
For every InputIterator type I, ranges::iterator_category_t&lt;I&gt;&nbsp;<wbr>must be defined to be 
an alias for the most specific category tag that describes the iterator's behavior. 

<h2>Example</h2>

&nbsp;<wbr>This section is incomplete 
&nbsp;<wbr>Reason: no example 

<h2>See also</h2>

input_iterator_tag 
output_iterator_tag 
forward_iterator_tag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>empty class types used to indicate iterator categories 
bidirectional_iterator_tag&nbsp;<wbr><i>(class)</i> 
random_access_iterator_tag 
contiguous_iterator_tag 
(C++20) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compatibility traits class that collects an iterator’s 
iterator_traits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>associated types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(alias template) 
