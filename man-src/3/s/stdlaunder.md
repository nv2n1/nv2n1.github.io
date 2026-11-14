---
title: "stdlaunder(3)"
name: "stdlaunder"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlaunder/"
---

std::launder - std::launder

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;new&gt;

template &lt;class T&gt;                                  (since C++17)

constexpr T* launder(T* p) noexcept;                (until C++20)

template &lt;class T&gt;                                  (since C++20)

[[nodiscard]] constexpr T* launder(T* p) noexcept;</code></pre> 
Obtains a pointer to the object located at the address represented by p. 
Formally, given 
* the pointer p represents the address A of a byte in memory 
* an object X is located at the address A 
* X is within its lifetime 
* the type of X is the same as T, ignoring cv-qualifiers at every level 
* every byte that would be reachable through the result is reachable through p (bytes are reachable through a pointer that points to an object Y if those bytes are within the storage of an object Z that is pointer-interconvertible with Y, or within the immediately enclosing array of which Z is an element) 
Then std::launder(p) returns a value of type T* that points to the object X. Otherwise, the behavior is undefined. 
The program is ill-formed if T is a function type or (possibly cv-qualified) void. 
std::launder may be used in a core_constant_expression if the value of its argument may be used in a core constant expression. 

<h2>Notes</h2>

std::launder has no effect on its argument. Its return value must be used to access the object. Thus, it's always an error to discard the return value.

Typical uses of std::launder include: 
* Obtaining a pointer to an object created in the storage of an existing object of the same type, where pointers to the old object cannot be reused because the object has const or reference data members, or because either object is a base class subobject; 
* Obtaining a pointer to an object created by placement new from a pointer to an object providing storage for that object. 
The reachability restriction ensures that std::launder cannot be used to access bytes not accessible through the original pointer, thereby interfering with the compiler's escape analysis. int x[10];

auto p = std::launder(reinterpret_cast&lt;int (*)[10]&gt;(&amp;x[0])); // OK
int x2[2][10];

auto p2 = std::launder(reinterpret_cast&lt;int (*)[10]&gt;(&amp;x2[0][0]));

// Undefined behavior: x2[1] would be reachable through the resulting pointer to x2[0]

// but is not reachable from the source
struct X {
    int a[10];
} x3, x4[2]; // standard layout; assume no padding

auto p3 = std::launder(reinterpret_cast&lt;int (*)[10]&gt;(&amp;x3.a[0])); // OK

auto p4 = std::launder(reinterpret_cast&lt;int (*)[10]&gt;(&amp;x4[0].a[0]));

// Undefined behavior: x4[1] would be reachable through the resulting pointer to x4[0].a

// (which is pointer-interconvertible with x4[0]) but is not reachable from the source
struct Y {
    int a[10];
    double y;
} x5;

auto p5 = std::launder(reinterpret_cast&lt;int (*)[10]&gt;(&amp;x5.a[0]));

// Undefined behavior: x5.y would be reachable through the resulting pointer to x5.a

// but is not reachable from the source


<h2>Example</h2>

// Run this code <pre><code>#include &lt;new&gt;

#include &lt;cstddef&gt;

#include &lt;cassert&gt;
struct X {
    const int n; // note: X has a const member
    int m;
};
struct Y {
    int z;
};
struct A {
    virtual int transmogrify();
};
struct B : A {
    int transmogrify() override
    {
        new (this) A;
        return 2;
    }
};
int A::transmogrify()
{
    new (this) B;
    return 1;
}
static_assert(sizeof(B) == sizeof(A));
int main()

{
    X *p = new X{3, 4};
    const int a = p-&gt;n;
    X *np = new (p) X{5, 6};          // p does not point to new object because X::n is const; np does
    const int b = p-&gt;n;               // undefined behavior
    const int c = p-&gt;m;               // undefined behavior (even though m is non-const, p can't be used)
    const int d = std::launder(p)-&gt;n; // OK, std::launder(p) points to new object
    const int e = np-&gt;n;              // OK
    alignas(Y) std::byte s[sizeof(Y)];
    Y *q = new (&amp;s) Y{2};
    const int f = reinterpret_cast&lt;Y *&gt;(&amp;s)-&gt;z;               // Class member access is undefined behavior:
                                                              // reinterpret_cast&lt;Y*&gt;(&amp;s) has value &quot;pointer to s&quot;
                                                              // and does not point to a Y object
    const int g = q-&gt;z;                                       // OK
    const int h = std::launder(reinterpret_cast&lt;Y *&gt;(&amp;s))-&gt;z; // OK
    A i;
    int n = i.transmogrify();
    // int m = i.transmogrify(); // undefined behavior
    int m = std::launder(&amp;i)-&gt;transmogrify(); // OK
    assert(m + n == 3);
}
</code></pre>
