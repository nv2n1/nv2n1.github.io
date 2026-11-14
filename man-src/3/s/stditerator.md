---
title: "stditerator(3)"
name: "stditerator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stditerator/"
---

std::iterator - std::iterator

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;

        class Category,

        class T,

        class Distance = std::ptrdiff_t, (deprecated in C++ 17)

                                             class Pointer = T *,

        class Reference = T &amp;

        &gt;
    struct iterator;</code></pre> 
std::iterator is the base class provided to simplify definitions of the required types for iterators. 

<h2>Template parameters</h2>

Category - the category of the iterator. Must be one of iterator_category_tags. 
T - the type of the values that can be obtained by dereferencing the iterator. This type should be void for output iterators. 
Distance - a type that can be used to identify distance between iterators 
Pointer - defines a pointer to the type iterated over (T) 
Reference - defines a reference to the type iterated over (T)

<h2>Member types</h2>

Member type Definition 
iterator_category Category 
value_type T 
difference_type Distance 
pointer Pointer 
reference Reference

<h2>Example</h2>

The following example shows how to implement a input_iterator by inheriting from std::iterator 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;
template &lt;long FROM, long TO&gt;

class Range
{

  public:
    // member typedefs provided through inheriting from std::iterator
    class iterator : public std::iterator&lt;
                         std::input_iterator_tag, // iterator_category
                         long,                    // value_type
                         long,                    // difference_type
                         const long *,            // pointer
                         long                     // reference
                         &gt;
    {
        long num = FROM;

      public:
        explicit iterator(long _num = 0)
            : num(_num)
        {
        }
        iterator &amp;operator++()
        {
            num = TO &gt;= FROM ? num + 1 : num - 1;
            return *this;
        }
        iterator operator++(int)
        {
            iterator retval = *this;
            ++(*this);
            return retval;
        }
        bool operator==(iterator other) const
        {
            return num == other.num;
        }
        bool operator!=(iterator other) const
        {
            return !(*this == other);
        }
        reference operator*() const
        {
            return num;
        }
    };
    iterator begin()
    {
        return iterator(FROM);
    }
    iterator end()
    {
        return iterator(TO &gt;= FROM ? TO + 1 : TO - 1);
    }
};
int main()
{
    // std::find requires an input iterator
    auto range = Range&lt;15, 25&gt;();
    auto itr = std::find(range.begin(), range.end(), 18);
    std::cout &lt;&lt; *itr &lt;&lt; '\n'; // 18
                               // Range::iterator also satisfies range-based for requirements
    for (long l : Range&lt;3, 5&gt;()) {
        std::cout &lt;&lt; l &lt;&lt; ' '; // 3 4 5
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;18 
&nbsp;<wbr>&nbsp;3 4 5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides uniform interface to the properties of an iterator 
iterator_traits <i>(class template)</i> 
input_iterator_tag 
output_iterator_tag 
forward_iterator_tag 
bidirectional_iterator_tag 
random_access_iterator_tag 
contiguous_iterator_tag empty class types used to indicate iterator categories 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
