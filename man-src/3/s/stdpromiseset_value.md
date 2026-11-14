---
title: "stdpromiseset_value(3)"
name: "stdpromiseset_value"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromiseset_value/"
---

std::promise&lt;R&gt;::set_value - std::promise&lt;R&gt;::set_value

<h2>Synopsis</h2>

<pre><code>void set_value(const R &amp;value);
(1)(member only of generic promise template)(since C++ 11)

    void set_value(R &amp;&amp;value);
(2)(member only of generic promise template)(since C++ 11)

    void set_value(R &amp;value);
(3)(member only of promise&lt;R &amp;&gt; template specialization)(since C++ 11)

    void set_value();
(4)(member only of promise&lt;void&gt; template specialization)(since C++ 11)</code></pre> 
1-3) Atomically stores the value into the shared state and makes the state ready. 
4) Makes the state ready 
The operation behaves as though set_value, set_exception, set_value_at_thread_exit, and set_exception_at_thread_exit acquire a single mutex associated with the promise object while updating the promise object. 
An exception is thrown if there is no shared state or the shared state already stores a value or exception. 
Calls to this function do not introduce data races with calls to get_future (but they need not synchronize with each other). 

<h2>Parameters</h2>

value - value to store in the shared state

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

std::future_error on the following conditions: 

 
* *this has no shared state. The error category is set to no_state. 

 

 
* The shared state already stores a value or exception. The error category is set to promise_already_satisfied. 

 
Additionally: 
1, 3) Any exception thrown by the copy constructor of value 
2) Any exception thrown by the move constructor of value

<h2>Example</h2>

This example shows how promise&lt;void&gt; can be used as signals between threads. 
 // Run this code <pre><code>#include &lt;thread&gt;

#include &lt;future&gt;

#include &lt;cctype&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;

#include &lt;iostream&gt;

#include &lt;sstream&gt;
int main()

{
    std::istringstream iss_numbers{&quot;3 4 1 42 23 -23 93 2 -289 93&quot;};
    std::istringstream iss_letters{&quot; a 23 b,e a2 k k?a;si,ksa c&quot;};
    std::vector&lt;int&gt; numbers;
    std::vector&lt;char&gt; letters;
    std::promise&lt;void&gt; numbers_promise, letters_promise;
    auto numbers_ready = numbers_promise.get_future();
    auto letter_ready = letters_promise.get_future();
    std::thread value_reader([&amp;] {
        // I/O operations.
        std::copy(std::istream_iterator&lt;int&gt;{iss_numbers},
                  std::istream_iterator&lt;int&gt;{},
                  std::back_inserter(numbers));
        // Notify for numbers.
        numbers_promise.set_value();
        std::copy_if(std::istreambuf_iterator&lt;char&gt;{iss_letters},
                     std::istreambuf_iterator&lt;char&gt;{},
                     std::back_inserter(letters),
                     ::isalpha);
        // Notify for letters.
        letters_promise.set_value();
    });

    numbers_ready.wait();
    std::sort(numbers.begin(), numbers.end());
    if (letter_ready.wait_for(std::chrono::seconds(1)) ==
        std::future_status::timeout) {
        // output the numbers while letters are being obtained.
        for (int num : numbers)
            std::cout &lt;&lt; num &lt;&lt; ' ';
        numbers.clear(); // Numbers were already printed.
    }
    letter_ready.wait();
    std::sort(letters.begin(), letters.end());
    // If numbers were already printed, it does nothing.
    for (int num : numbers)
        std::cout &lt;&lt; num &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    for (char let : letters)
        std::cout &lt;&lt; let &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    value_reader.join();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;-289 -23 1 2 3 4 23 42 93 93 
&nbsp;<wbr>&nbsp;a a a a b c e i k k k s s

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the result to indicate an exception 
set_exception <i>(public member function)</i> 
