---
title: "dc(1)"
name: "dc"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc/"
description: "dc – an arbitrary precision calculator"
---

<h2 class="name">NAME</h2>
<p> dc &#8211; an arbitrary precision calculator </p>
<h2>SYNOPSIS</h2>
<p> dc [-V] [&#8211;version] [-h] [&#8211;help]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[-e scriptexpression]&nbsp;[&#8211;expression=scriptexpression]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[-f scriptfile]&nbsp;[&#8211;file=scriptfile]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>dc</i> is a reverse-polish desk calculator which supports unlimited precision arithmetic. It also allows you to define and call macros. Normally <i>dc</i> reads from the standard input; if any command arguments are given to it, they are filenames, and <i>dc</i> reads and executes the contents of the files before reading from standard input. All normal output is to standard output; all error output is to standard error. </p>
<p> A reverse-polish calculator stores numbers on a stack. Entering a number pushes it on the stack. Arithmetic operations pop arguments off the stack and push the results. </p>
<p> To enter a number in <i>dc</i>, type the digits (using upper case letters <i>A</i> through <i>F</i> as &quot;digits&quot; when working with input bases greater than ten), with an optional decimal point. Exponential notation is not supported. To enter a negative number, begin the number with &#8220;_&#8221;. &#8220;-&#8221; cannot be used for this, as it is a binary operator for subtraction instead. To enter two numbers in succession, separate them with spaces or newlines. These have no meaning as commands.</p>
<h2>OPTIONS</h2>
<p> <i>dc</i> may be invoked with the following command-line options:</p>
<dl>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Print out the version of <i>dc</i> that is being run and a copyright notice, then exit.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message briefly summarizing these command-line options and the bug-reporting address, then exit.</p>
<dt><code>-e </code><i>script</i></p>
<dd>
<dt><code>&#8211;expression=</code><i>script</i></p>
<dd> Add the commands in <i>script</i> to the set of commands to be run while processing the input.</p>
<dt><code>-f </code><i>script-file</i></p>
<dd>
<dt><code>&#8211;file=</code><i>script-file</i></p>
<dd> Add the commands contained in the file <i>script-file</i> to the set of commands to be run while processing the input.</dl>
<p> If any command-line parameters remain after processing the above, these parameters are interpreted as the names of input files to be processed. A file name of <code>&#8211;</code> refers to the standard input stream. The standard input will processed if no script files or expressions are specified.</p>
<h2>Printing Commands</h2>
<dl>
<dt><code>p</code></p>
<dd> Prints the value on the top of the stack, without altering the stack. A newline is printed after the value.</p>
<dt><code>n</code></p>
<dd> Prints the value on the top of the stack, popping it off, and does not print a newline after.</p>
<dt><code>P</code></p>
<dd> Pops off the value on top of the stack. If it it a string, it is simply printed without a trailing newline. Otherwise it is a number, and the integer portion of its absolute value is printed out as a &quot;base (UCHAR_MAX+1)&quot; byte stream. Assuming that (UCHAR_MAX+1) is 256 (as it is on most machines with 8-bit bytes), the sequence <code>KSK0k1/_1Ss [ls*]Sxd0&gt;x [256~Ssd0&lt;x]dsxxsx[q]Sq[Lsd0&gt;qaPlxx] dsxxsx0sqLqsxLxLK+k</code> could also accomplish this function. (Much of the complexity of the above native-dc code is due to the ~ computing the characters backwards, and the desire to ensure that all registers wind up back in their original states.)</p>
<dt><code>f</code></p>
<dd> Prints the entire contents of the stack without altering anything. This is a good command to use if you are lost or want to figure out what the effect of some command has been.</dl>
<h2>Arithmetic</h2>
<dl>
<dt><code>+</code></p>
<dd> Pops two values off the stack, adds them, and pushes the result. The precision of the result is determined only by the values of the arguments, and is enough to be exact.</p>
<dt><code>&#8211;</code></p>
<dd> Pops two values, subtracts the first one popped from the second one popped, and pushes the result.</p>
<dt><code>*</code></p>
<dd> Pops two values, multiplies them, and pushes the result. The number of fraction digits in the result depends on the current precision value and the number of fraction digits in the two arguments.</p>
<dt><code>/</code></p>
<dd> Pops two values, divides the second one popped from the first one popped, and pushes the result. The number of fraction digits is specified by the precision value.</p>
<dt><code>%</code></p>
<dd> Pops two values, computes the remainder of the division that the <code>/</code> command would do, and pushes that. The value computed is the same as that computed by the sequence <code>Sd dld/ Ld*-</code> .</p>
<dt><code>~</code></p>
<dd> Pops two values, divides the second one popped from the first one popped. The quotient is pushed first, and the remainder is pushed next. The number of fraction digits used in the division is specified by the precision value. (The sequence <code>SdSn lnld/ LnLd%</code> could also accomplish this function, with slightly different error checking.)</p>
<dt><code>^</code></p>
<dd> Pops two values and exponentiates, using the first value popped as the exponent and the second popped as the base. The fraction part of the exponent is ignored. The precision value specifies the number of fraction digits in the result.</p>
<dt><code>|</code></p>
<dd> Pops three values and computes a modular exponentiation. The first value popped is used as the reduction modulus; this value must be a non-zero number, and should be an integer. The second popped is used as the exponent; this value must be a non-negative number, and any fractional part of this exponent will be ignored. The third value popped is the base which gets exponentiated, which should be an integer. For small integers this is like the sequence <code>Sm^Lm%</code>, but, unlike <code>^</code>, this command will work with arbitrarily large exponents.</p>
<dt><code>v</code></p>
<dd> Pops one value, computes its square root, and pushes that. The maximum of the precision value and the precision of the argument is used to determine the number of fraction digits in the result.</dl>
<p> Most arithmetic operations are affected by the &#8220;precision value&#8221;, which you can set with the <code>k</code> command. The default precision value is zero, which means that all arithmetic except for addition and subtraction produces integer results.</p>
<h2>Stack Control</h2>
<dl>
<dt><code>c</code></p>
<dd> Clears the stack, rendering it empty.</p>
<dt><code>d</code></p>
<dd> Duplicates the value on the top of the stack, pushing another copy of it. Thus, &#8220;4d*p&#8221; computes 4 squared and prints it.</p>
<dt><code>r</code></p>
<dd> Reverses the order of (swaps) the top two values on the stack. (This can also be accomplished with the sequence <code>SaSbLaLb</code>.)</p>
<dt><code>R</code></p>
<dd> Pops the top-of-stack as an integer <i>n</i>. Cyclically rotates the top <i>n</i> items on the updated stack. If <i>n</i> is positive, then the rotation direction will make the topmost element the second-from top; if <i>n</i> is negative, then the rotation will make the topmost element the <i>n</i>-th element from the top. If the stack depth is less than <i>n</i>, then the entire stack is rotated (in the appropriate direction), without any error being reported.</dl>
<h2>Registers</h2>
<p> <i>dc</i> provides at least 256 memory registers, each named by a single character. You can store a number or a string in a register and retrieve it later.</p>
<dl>
<dt><code>s</code><i>r</i></p>
<dd> Pop the value off the top of the stack and store it into register <i>r</i>.</p>
<dt><code>l</code><i>r</i></p>
<dd> Copy the value in register <i>r</i> and push it onto the stack. The value 0 is retrieved if the register is uninitialized. This does not alter the contents of <i>r</i>.</dl>
<p> Each register also contains its own stack. The current register value is the top of the register&#8217;s stack.</p>
<dl>
<dt><code>S</code><i>r</i></p>
<dd> Pop the value off the top of the (main) stack and push it onto the stack of register <i>r</i>. The previous value of the register becomes inaccessible.</p>
<dt><code>L</code><i>r</i></p>
<dd> Pop the value off the top of register <i>r</i>&#8216;s stack and push it onto the main stack. The previous value in register <i>r</i>&#8216;s stack, if any, is now accessible via the <code>l</code><i>r</i> command.</dl>
<h2>Parameters</h2>
<p> <i>dc</i> has three parameters that control its operation: the precision, the input radix, and the output radix. The precision specifies the number of fraction digits to keep in the result of most arithmetic operations. The input radix controls the interpretation of numbers typed in; all numbers typed in use this radix. The output radix is used for printing numbers. </p>
<p> The input and output radices are separate parameters; you can make them unequal, which can be useful or confusing. The input radix must be between 2 and 16 inclusive. The output radix must be at least 2. The precision must be zero or greater. The precision is always measured in decimal digits, regardless of the current input or output radix.</p>
<dl>
<dt><code>i</code></p>
<dd> Pops the value off the top of the stack and uses it to set the input radix.</p>
<dt><code>o</code></p>
<dd> Pops the value off the top of the stack and uses it to set the output radix.</p>
<dt><code>k</code></p>
<dd> Pops the value off the top of the stack and uses it to set the precision.</p>
<dt><code>I</code></p>
<dd> Pushes the current input radix on the stack.</p>
<dt><code>O</code></p>
<dd> Pushes the current output radix on the stack.</p>
<dt><code>K</code></p>
<dd> Pushes the current precision on the stack.</dl>
<h2>Strings</h2>
<p> <i>dc</i> has a limited ability to operate on strings as well as on numbers; the only things you can do with strings are print them and execute them as macros (which means that the contents of the string are processed as <i>dc</i> commands). All registers and the stack can hold strings, and <i>dc</i> always knows whether any given object is a string or a number. Some commands such as arithmetic operations demand numbers as arguments and print errors if given strings. Other commands can accept either a number or a string; for example, the <code>p</code> command can accept either and prints the object according to its type.</p>
<dl>
<dt><code>[</code><i>characters</i><code>]</code></p>
<dd> Makes a string containing <i>characters</i> (contained between balanced <code>[</code> and <code>]</code> characters), and pushes it on the stack. For example, <code>[foo]P</code> prints the characters <code>foo</code> (with no newline).</p>
<dt><code>a</code></p>
<dd> The top-of-stack is popped. If it was a number, then the low-order byte of this number is converted into a string and pushed onto the stack. Otherwise the top-of-stack was a string, and the first character of that string is pushed back.</p>
<dt><code>x</code></p>
<dd> Pops a value off the stack and executes it as a macro. Normally it should be a string; if it is a number, it is simply pushed back onto the stack. For example, <code>[1p]x</code> executes the macro <code>1p</code> which pushes <code>1</code> on the stack and prints <code>1</code> on a separate line.</dl>
<p> Macros are most often stored in registers; <code>[1p]sa</code> stores a macro to print <code>1</code> into register <code>a</code>, and <code>lax</code> invokes this macro.</p>
<dl>
<dt><code>&gt;</code><i>r</i></p>
<dd> Pops two values off the stack and compares them assuming they are numbers, executing the contents of register <i>r</i> as a macro if the original top-of-stack is greater. Thus, <code>1 2&gt;a</code> will invoke register <code>a</code>&#8216;s contents and <code>2 1&gt;a</code> will not.</p>
<dt><code>!&gt;</code><i>r</i></p>
<dd> Similar but invokes the macro if the original top-of-stack is not greater than (less than or equal to) what was the second-to-top.</p>
<dt><code>&lt;</code><i>r</i></p>
<dd> Similar but invokes the macro if the original top-of-stack is less.</p>
<dt><code>!&lt;</code><i>r</i></p>
<dd> Similar but invokes the macro if the original top-of-stack is not less than (greater than or equal to) what was the second-to-top.</p>
<dt><code>=</code><i>r</i></p>
<dd> Similar but invokes the macro if the two numbers popped are equal.</p>
<dt><code>!=</code><i>r</i></p>
<dd> Similar but invokes the macro if the two numbers popped are not equal.</p>
<dt><code>?</code></p>
<dd> Reads a line from the terminal and executes it. This command allows a macro to request input from the user.</p>
<dt><code>q</code></p>
<dd> exits from a macro and also from the macro which invoked it. If called from the top level, or from a macro which was called directly from the top level, the <code>q</code> command will cause <i>dc</i> to exit.</p>
<dt><code>Q</code></p>
<dd> Pops a value off the stack and uses it as a count of levels of macro execution to be exited. Thus, <code>3Q</code> exits three levels. The <code>Q</code> command will never cause <i>dc</i> to exit.</dl>
<h2>Status Inquiry</h2>
<dl>
<dt><code>Z</code></p>
<dd> Pops a value off the stack, calculates the number of decimal digits it has (or number of characters, if it is a string) and pushes that number. The digit count for a number does <i>not</i> include any leading zeros, even if those appear to the right of the radix point.</p>
<dt><code>X</code></p>
<dd> Pops a value off the stack, calculates the number of fraction digits it has, and pushes that number. For a string, the value pushed is 0.</p>
<dt><code>z</code></p>
<dd> Pushes the current stack depth: the number of objects on the stack before the execution of the <code>z</code> command.</dl>
<h2>Miscellaneous</h2>
<dl>
<dt><code>!</code></p>
<dd> Will run the rest of the line as a system command. Note that parsing of the !&lt;, !=, and !&gt; commands take precedence, so if you want to run a command starting with &lt;, =, or &gt; you will need to add a space after the !.</p>
<dt><code>#</code></p>
<dd> Will interpret the rest of the line as a comment.</p>
<dt><code>:</code><i>r</i></p>
<dd> Will pop the top two values off of the stack. The old second-to-top value will be stored in the array <i>r</i>, indexed by the old top-of-stack value.</p>
<dt><code>;</code><i>r</i></p>
<dd> Pops the top-of-stack and uses it as an index into the array <i>r</i>. The selected value is then pushed onto the stack.</dl>
<p> Note that each stacked instance of a register has its own array associated with it. Thus <code>1 0:a 0Sa 2 0:a La 0;ap</code> will print 1, because the 2 was stored in an instance of 0:a that was later popped.</p>
<h2>FILES</h2>
<dl>
<dt>~/.dcrc</p>
<dd> The commands in this file will be executed when <i>dc</i> is first run.</dl>
<h2>BUGS</h2>
<p> Email bug reports to <code>bug-dc [at] gnu.org</code>. </p>
<h2>Index</h2>
