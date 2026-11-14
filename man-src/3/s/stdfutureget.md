---
title: "stdfutureget(3)"
name: "stdfutureget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfutureget/"
description: "std::future<T>::get – std::future<T>::get"
---

<p>std::future&lt;T&gt;::get &#8211; std::future&lt;T&gt;::get</p>
<h2>Synopsis</h2>
<p>T get(); <code>(1)</code> (member only of generic future template)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i><br />
T&amp; get(); <code>(2)</code> (member only of future&lt;T&amp;&gt; template specialization)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i><br />
void get(); <code>(3)</code> (member only of future&lt;void&gt; template specialization)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i><br />
The get method waits until the future has a valid result and (depending on which template is used) retrieves it. It effectively calls wait() in order to wait for the result.<br />
The generic template and two template specializations each contain a single version of get. The three versions of get differ only in the return type.<br />
The behavior is undefined if valid() is false before the call to this function.<br />
Any shared state is released. valid() is false after a call to this method. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) The value v stored in the shared state, as std::move(v).<br />
2) The reference stored as value in the shared state.<br />
3) Nothing. </p>
<h2>Exceptions</h2>
<p>If an exception was stored in the shared state referenced by the future (e.g. via a call to std::promise::set_exception()) then that exception will be thrown.</p>
<h2>Notes</h2>
<p>The implementations are encouraged to detect the case when valid() is false before the call and throw a std::future_error with an error condition of std::future_errc::no_state. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;thread&gt;

#include &lt;future&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;chrono&gt;
std::string time()
{
    static auto start = std::chrono::steady_clock::now();
    std::chrono::duration&lt;double&gt; d = std::chrono::steady_clock::now() - start;
    return &quot;[&quot; + std::to_string(d.count()) + &quot;s]&quot;;
}

int main()
{
    using namespace std::chrono_literals;
    {
        std::cout &lt;&lt; time() &lt;&lt; &quot; launching thread
&quot;;
        std::future&lt;int&gt; f = std::async(std::launch::async, [] {
            std::this_thread::sleep_for(1s);
            return 7;
        });
        std::cout &lt;&lt; time() &lt;&lt; &quot; waiting for the future, f.valid() == &quot;
                  &lt;&lt; f.valid() &lt;&lt; &quot;
&quot;;
        int n = f.get();
        std::cout &lt;&lt; time() &lt;&lt; &quot; future.get() returned with &quot; &lt;&lt; n &lt;&lt; &quot;. f.valid() = &quot;
                  &lt;&lt; f.valid() &lt;&lt; '
';
    }
    {
        std::cout &lt;&lt; time() &lt;&lt; &quot; launching thread
&quot;;
        std::future&lt;int&gt; f = std::async(std::launch::async, [] {
            std::this_thread::sleep_for(1s);
            return true ? throw std::runtime_error(&quot;7&quot;) : 7;
        });
        std::cout &lt;&lt; time() &lt;&lt; &quot; waiting for the future, f.valid() == &quot;
                  &lt;&lt; f.valid() &lt;&lt; &quot;
&quot;;
        try {
            int n = f.get();
            std::cout &lt;&lt; time() &lt;&lt; &quot; future.get() returned with &quot; &lt;&lt; n
                      &lt;&lt; &quot; f.valid() = &quot; &lt;&lt; f.valid() &lt;&lt; '
';
        } catch (const std::exception &amp;e) {
            std::cout &lt;&lt; time() &lt;&lt; &quot; caught exception &quot; &lt;&lt; e.what()
                      &lt;&lt; &quot;, f.valid() == &quot; &lt;&lt; f.valid() &lt;&lt; &quot;
&quot;;
        }
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;[0.000004s] launching thread<br />
&nbsp;<wbr>&nbsp;[0.000461s] waiting for the future, f.valid() == 1<br />
&nbsp;<wbr>&nbsp;[1.001156s] future.get() returned with 7. f.valid() = 0<br />
&nbsp;<wbr>&nbsp;[1.001192s] launching thread<br />
&nbsp;<wbr>&nbsp;[1.001275s] waiting for the future, f.valid() == 1<br />
&nbsp;<wbr>&nbsp;[2.002356s] caught exception 7, f.valid() == 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the future has a shared state<br />
valid <i>(public member function)</i> </p>
