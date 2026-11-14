---
title: "utilities(3)"
name: "utilities"
section: "3"
letter: "u"
url: "/docs/linux/man/3-utilities/"
---

Utilities - Iterators are meant to build a sequence on the fly from one or more other sequences, without having to allocate place for storing it. A couple of examples: suppose we have a function which calculates the average of a sequence, and that for genericity we have implemented it as a template function which takes the beginning and the end of the sequence, so that its declaration is: <pre> template &lt;class Iterator&gt;
 typename Iterator::value_type
 average(const Iterator&amp; begin, const Iterator&amp; end)</pre>This kind of genericity allows one to use the same function to calculate the average of a std::vector, a std::list, a QuantLib::History, any other container, of a subset of any of the former. Now let's say we have two sequences of numbers, and we want to calculate the average of their products. One approach could be to store the products in another sequence, and to calculate the average of the latter, as in: <pre><code>// we have sequence1 and sequence2 and assume equal size:
// first we store their product in a vector...
std::vector&lt;double&gt; products;
std::transform(sequence1.begin(),sequence1.end(), // first sequence
sequence2.begin(),                 // second sequence
std::back_inserter(products),      // output
std::multiplies&lt;double&gt;());        // operation to perform
// ...then we calculate the average
double result = average(products.begin(),products.end());
</code></pre> The above works, however, it might be not particularly efficient since we have to allocate the product vector, quite possibly just to throw it away when the calculation is done. QuantLib::coupling_iterator allows us to do the same thing without allocating the extra vector: what we do is simply: <pre> // we have sequence1 and sequence2 and assume equal size:
 double result = average(
 make_coupling_iterator(sequence1.begin(),
 sequence2.begin(),
 std::multiplies&lt;double()),
 make_coupling_iterator(sequence1.end(),
 sequence2.end(),
 std::multiplies&lt;double()));</pre>The call to make_coupling_iterator creates an iterator which is really a reference to the two iterators and the operation we passed. Dereferencing such iterator returns the result of applying such operation to the values pointed to by the two contained iterators. Advancing the coupling iterator advances the two underlying ones. One can see how iterating on such iterator generates the products one by one so that they can be processed by average(), but does not need allocating memory for storing the results. The product sequence is generated on the fly. The other iterators share the same principle but have different functionalities:
<dl><dt>*
<dd>combining_iterator is the same as coupling_iterator, but works on $ N $ sequences while the latter works on 2;
<dt>*
<dd>filtering_iterator generates the elements of a given sequence which satisfy a given predicate, i.e., it takes a sequence $ [x_0,x_1,ots] $ and a predicate $ p $ and generates the sequence of those $ x_i $ for which $ p(x_i) $ returns true;
<dt>*
<dd>processing_iterator takes a sequence $ [x_0,x_1,ots] $ and a function $ f $ and generates the sequence $ [f(x_0),f(x_1),ots] $;
<dt>*
<dd>stepping_iterator takes a sequence $ [x_0,x_1,ots] $ and a step $ m $ and generates the sequence $ [x_0,x_m,x_{2m},ots] $</dl>
 

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
