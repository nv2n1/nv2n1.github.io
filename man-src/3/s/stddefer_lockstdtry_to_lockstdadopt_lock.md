---
title: "stddefer_lockstdtry_to_lockstdadopt_lock(3)"
name: "stddefer_lockstdtry_to_lockstdadopt_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddefer_lockstdtry_to_lockstdadopt_lock/"
---

std::defer_lock,std::try_to_lock,std::adopt_lock - std::defer_lock,std::try_to_lock,std::adopt_lock

<h2>Synopsis</h2>

Defined in header &lt;mutex&gt; 
constexpr std::defer_lock_t defer_lock {}; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i> 
inline constexpr std::defer_lock_t defer_lock {}; <i>(since C++17)</i> 
constexpr std::try_to_lock_t try_to_lock {}; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i> 
inline constexpr std::try_to_lock_t try_to_lock {}; <i>(since C++17)</i> 
constexpr std::adopt_lock_t adopt_lock {}; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i> 
inline constexpr std::adopt_lock_t adopt_lock {}; <i>(since C++17)</i> 
std::defer_lock, std::try_to_lock and std::adopt_lock are instances of empty struct tag types std::defer_lock_t, std::try_to_lock_t and std::adopt_lock_t respectively. 
They are used to specify locking strategies for std::lock_guard, std::unique_lock and std::shared_lock. 
Type Effect(s) 
defer_lock_t do not acquire ownership of the mutex 
try_to_lock_t try to acquire ownership of the mutex without blocking 
adopt_lock_t assume the calling thread already has ownership of the mutex 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;mutex&gt;

#include &lt;thread&gt;
struct bank_account {
    explicit bank_account(int balance)
        : balance(balance)
    {
    }
    int balance;
    std::mutex m;
};
void transfer(bank_account &amp;from, bank_account &amp;to, int amount)

{
    // lock both mutexes without deadlock
    std::lock(from.m, to.m);
    // make sure both already-locked mutexes are unlocked at the end of scope
    std::lock_guard&lt;std::mutex&gt; lock1(from.m, std::adopt_lock);
    std::lock_guard&lt;std::mutex&gt; lock2(to.m, std::adopt_lock);
    // equivalent approach:

    //    std::unique_lock&lt;std::mutex&gt; lock1(from.m, std::defer_lock);

    //    std::unique_lock&lt;std::mutex&gt; lock2(to.m, std::defer_lock);

    //    std::lock(lock1, lock2);
    from.balance -= amount;
    to.balance += amount;
}
int main()

{
    bank_account my_account(100);
    bank_account your_account(50);
    std::thread t1(transfer, std::ref(my_account), std::ref(your_account), 10);
    std::thread t2(transfer, std::ref(your_account), std::ref(my_account), 5);
    t1.join();
    t2.join();
}
</code></pre>

<h2>See also</h2>

defer_lock_t 
try_to_lock_t 
adopt_lock_t tag type used to specify locking strategy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a lock_guard, optionally locking the given mutex 
constructor <i>(public member function of std::lock_guard&lt;Mutex&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a unique_lock, optionally locking the supplied mutex 
constructor <i>(public member function of std::unique_lock&lt;Mutex&gt;)</i> 
