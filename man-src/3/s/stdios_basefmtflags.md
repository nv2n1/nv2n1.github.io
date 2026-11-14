---
title: "stdios_basefmtflags(3)"
name: "stdios_basefmtflags"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basefmtflags/"
---

std::ios_base::fmtflags - std::ios_base::fmtflags

<h2>Synopsis</h2>

<pre><code>typedef /*implementation defined*/ fmtflags;

static constexpr fmtflags dec = /*implementation defined*/

static constexpr fmtflags oct = /*implementation defined*/

static constexpr fmtflags hex = /*implementation defined*/

static constexpr fmtflags basefield = dec | oct | hex;

static constexpr fmtflags left = /*implementation defined*/

static constexpr fmtflags right = /*implementation defined*/

static constexpr fmtflags internal = /*implementation defined*/

static constexpr fmtflags adjustfield = left | right | internal;

static constexpr fmtflags scientific = /*implementation defined*/

static constexpr fmtflags fixed = /*implementation defined*/

static constexpr fmtflags floatfield = scientific | fixed;

static constexpr fmtflags boolalpha = /*implementation defined*/

static constexpr fmtflags showbase = /*implementation defined*/

static constexpr fmtflags showpoint = /*implementation defined*/

static constexpr fmtflags showpos = /*implementation defined*/

static constexpr fmtflags skipws = /*implementation defined*/

static constexpr fmtflags unitbuf = /*implementation defined*/

static constexpr fmtflags uppercase = /*implementation defined*/</code></pre> 
Specifies available formatting flags. It is a BitmaskType. The following constants are defined: 
Constant Explanation 
dec use decimal base for integer I/O: see std::dec 
oct use octal base for integer I/O: see std::oct 
hex use hexadecimal base for integer I/O: see std::hex 
basefield dec|oct|hex. Useful for masking operations 
left left adjustment (adds fill characters to the right): see std::left 
right right adjustment (adds fill characters to the left): see std::right 
internal internal adjustment (adds fill characters to the internal designated point): see std::internal 
adjustfield left|right|internal. Useful for masking operations 
scientific generate floating point types using scientific notation, or hex notation if combined with fixed: see std::scientific 
fixed generate floating point types using fixed notation, or hex notation if combined with scientific: see std::fixed 
floatfield scientific|fixed. Useful for masking operations 
boolalpha insert and extract bool type in alphanumeric format: see std::boolalpha 
showbase generate a prefix indicating the numeric base for integer output, require the currency indicator in monetary I/O: see std::showbase 
showpoint generate a decimal-point character unconditionally for floating-point number output: see std::showpoint 
showpos generate a + character for non-negative numeric output: see std::showpos 
skipws skip leading whitespace before certain input operations: see std::skipws 
unitbuf flush the output after each output operation: see std::unitbuf 
uppercase replace certain lowercase letters with their uppercase 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;equivalents in certain output operations: see std::uppercase 

<h2>Example</h2>

The following example shows several different ways to print the same result. 
 // Run this code <pre><code>#include &lt;iostream&gt;
int main()

{
    int num = 150;
    // using fmtflags as class member constants:
    std::cout.setf(std::ios_base::hex, std::ios_base::basefield);
    std::cout.setf(std::ios_base::showbase);
    std::cout &lt;&lt; num &lt;&lt; '\n';
    // using fmtflags as inherited class member constants:
    std::cout.setf(std::ios::hex, std::ios::basefield);
    std::cout.setf(std::ios::showbase);
    std::cout &lt;&lt; num &lt;&lt; '\n';
    // using fmtflags as object member constants:
    std::cout.setf(std::cout.hex, std::cout.basefield);
    std::cout.setf(std::cout.showbase);
    std::cout &lt;&lt; num &lt;&lt; '\n';
    // using fmtflags as a type:
    std::ios_base::fmtflags ff;
    ff = std::cout.flags();
    ff &amp;= ~std::cout.basefield; // unset basefield bits
    ff |= std::cout.hex;        // set hex
    ff |= std::cout.showbase;   // set showbase
    std::cout.flags(ff);
    std::cout &lt;&lt; num &lt;&lt; '\n';
    // not using fmtflags, but using manipulators:
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; num &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0x96 
&nbsp;<wbr>&nbsp;0x96 
&nbsp;<wbr>&nbsp;0x96 
&nbsp;<wbr>&nbsp;0x96 
&nbsp;<wbr>&nbsp;0x96

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;manages format flags 
flags <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets specific format flag 
setf <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears specific format flag 
unsetf <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the base used for integer I/O 
setbase <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the fill character 
setfill <i>(function template)</i> 
fixed 
scientific 
hexfloat 
defaultfloat changes formatting used for floating-point I/O 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether prefix is used to indicate numeric base 
showbase <i>(function)</i> 
noshowbase 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switches between textual and numeric representation of booleans 
boolalpha <i>(function)</i> 
noboolalpha 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether the + sign used with non-negative numbers 
showpos <i>(function)</i> 
noshowpos 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether decimal point is always included in floating-point representation 
showpoint <i>(function)</i> 
noshowpoint 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether output is flushed after each operation 
unitbuf <i>(function)</i> 
nounitbuf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether leading whitespace is skipped on input 
skipws <i>(function)</i> 
noskipws 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether uppercase characters are used with some output formats 
uppercase <i>(function)</i> 
nouppercase 
