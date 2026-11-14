---
title: "small_page(3)"
name: "small_page"
section: "3"
letter: "s"
url: "/docs/linux/man/3-small_page/"
description: "Small_Page – Brief Introduction to Small This section describes the basics of Small, as compiled and interpreted with Embryo."
---

<p>Small_Page &#8211; Brief Introduction to Small This section describes the basics of Small, as compiled and interpreted with Embryo. </p>
<p> For the full documentation, of which this is a summary, see </p>
<p> This summary assumes that you are familar with C. For a full list of differences between C and Small, again, see the full documentation. </p>
<h2>Variables</h2>
<h3>Types</h3>
<p>There is only one type, known as the &#8216;cell&#8217;, which can hold an integer.</p>
<h3>Scope</h3>
<p>The scope and usage of a variable depends on its declaration. </p>
<dl COMPACT>
<dt>*</p>
<dd>A local variable is normally declared with the new keyword. E.g.</dl>
<pre> new variable </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd>A static function variable is defined within a function with the static keyword.</p>
<dt>*</p>
<dd>A global static variable is one that is only available within the file it was declared in. Again, use the static keyword, but outside of any function.</p>
<dt>*</p>
<dd>A stock variable is one that may not be compiled into a program if it is not used. It is declared using stock.</p>
<dt>*</p>
<dd>A public variable is one that can be read by the host program using <code>embryo_program_variable_find</code>. It is declared using public keyword.</dl>
<p> Remember that the keywords above are to be used on their own. That is, for example: </p>
<pre> public testvar </pre>
<p>&nbsp;<wbr>not:&nbsp;<wbr> </p>
<pre> new public testvar </pre>
<h3>Constants</h3>
<p>You can declare constants in two ways: </p>
<dl COMPACT>
<dt>*</p>
<dd>Using the preprocessor macro define.</p>
<dt>*</p>
<dd>By inserting const between the keyword and variable name of a variable declaration. For example, to declare the variable var1 constant, you type</dl>
<pre> new const var1 = 2 </pre>
<p>&nbsp;<wbr>Now var1 cannot be changed. </p>
<h3>Arrays</h3>
<p>To declare an array, append square brackets to the end of the variable name. The following examples show how to declare arrays. Note the use of the ellipsis operator, which bases the array based on the last two declared values: </p>
<pre>new msg[] = 'A message.'
new ints[] = {1, 3, 4}
new ints2[20] = {1, 3} // All other elements 0.
new ints3[10] = {1, ... } // All elements = 1
new ints4[10] = {10, 20, ... } // Elements = 10 -&gt; 100.
 // The difference can be negative.
new ints5[3][3] = &#123;&#123;1, 2, 3}, {4, 5, 6}, {7, 8, 9}}</pre>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>Array initialisers need to be constant.</dl>
<h2>Function Calls</h2>
<p>A typical function declaration is as follows: </p>
<pre>testfunc(param) {
 // Do something ...
 // over a couple of lines.
}</pre>
<p>You can pass by reference. That is, the parameter you pass is changed outside of the function. For example: </p>
<pre>testfunc(&amp;param) {
 param = 10
 // The passed variable will be set to 10 outside of the function.
}</pre>
<p>To pass an array: </p>
<pre>testfunc(param[]) {
 // Do something to the array
}</pre>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>Arrays are passed by reference.</dl>
<h2>Control Structures.</h2>
<p>Small has the following control structures, which similar to their C counterparts: </p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> if (expression) statement1 else statement2 </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> switch (expression) {
 case 0:
 statement1 // Can only be one statement. Look Ma, no breaks!
 case 1..3: // For values between 1 and 3 inclusive.
 statement2
 default: // Optional
 statement3
}</pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> while(expression) statement </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> do statement while (expression) </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> for (init_expression; before_iter_test_expression; after_iter_expression) statement </pre>
<h2>Preprocessor</h2>
<p>The following preprocessor directives are available: </p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> #assert constant_expression </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> #define pattern replacement </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> #define pattern(%1,%2,...) replacement </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> #include filename </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> #if constant_expression
 // Various bits of code
#else
 // Other bits of code
#endif </pre>
<p>&nbsp;<wbr></p>
<dl COMPACT>
<dt>*</p>
<dd></dl>
<pre> #undef pattern </pre>
<p>&nbsp;<wbr></p>
