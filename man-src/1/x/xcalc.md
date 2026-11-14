---
title: "xcalc(1)"
name: "xcalc"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcalc/"
description: "xcalc – scientific calculator for X"
---

<h2 class="name">NAME</h2>
<p> xcalc &#8211; scientific calculator for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xcalc</code> [-stipple] [-rpn] [-<i>toolkitoption&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>xcalc</i> is a scientific calculator desktop accessory that can emulate a TI-30 or an HP-10C.</p>
<h2>OPTIONS</h2>
<p> <i>xcalc</i> accepts all of the standard toolkit command line options along with two additional options: </p>
<dl>
<dt><code>-stipple</code></p>
<dd> This option indicates that the background of the calculator should be drawn using a stipple of the foreground and background colors. On monochrome displays improves the appearance.</dl>
<dl>
<dt><code>-rpn</code></p>
<dd> This option indicates that Reverse Polish Notation should be used. In this mode the calculator will look and behave like an HP-10C. Without this flag, it will emulate a TI-30.</dl>
<h2>OPERATION</h2>
<p> <i>Pointer Usage:</i> Operations may be performed with pointer button 1, or in some cases, with the keyboard. Many common calculator operations have keyboard accelerators. To quit, press pointer button 3 on the AC key of the TI calculator, or the ON key of the HP calculator. </p>
<p> <i>Calculator Key Usage (TI mode):</i> The numbered keys, the +/- key, and the +, -, *, /, and = keys all do exactly what you would expect them to. It should be noted that the operators obey the standard rules of precedence. Thus, entering &quot;3+4*5=&quot; results in &quot;23&quot;, not &quot;35&quot;. The parentheses can be used to override this. For example, &quot;(1+2+3)*(4+5+6)=&quot; results in &quot;6*15=90&quot;. </p>
<p> The entire number in the calculator display can be selected, in order to paste the result of a calculation into text. </p>
<p> The action procedures associated with each function are given below. These are useful if you are interested in defining a custom calculator. The action used for all digit keys is <code>digit(</code><i>n</i>), where <i>n</i> is the corresponding digit, 0..9.</p>
<dl>
<dt><code>1/x</code></p>
<dd> Replaces the number in the display with its reciprocal. The corresponding action procedure is <code>reciprocal()</code>.</p>
<dt><code>x^2</code></p>
<dd> Squares the number in the display. The corresponding action procedure is <code>square()</code>.</p>
<dt><code>SQRT</code></p>
<dd> Takes the square root of the number in the display. The corresponding action procedure is <code>squareRoot()</code>.</p>
<dt><code>CE/C</code></p>
<dd> When pressed once, clears the number in the display without clearing the state of the machine. Allows you to re-enter a number if you make a mistake. Pressing it twice clears the state, also. The corresponding action procedure for TI mode is <code>clear()</code>.</p>
<dt><code>AC</code></p>
<dd> Clears the display, the state, and the memory. Pressing it with the third pointer button turns off the calculator, in that it exits the program. The action procedure to clear the state is <code>off()</code>; to quit, <code>quit()</code>.</p>
<dt><code>INV</code></p>
<dd> Invert function. See the individual function keys for details. The corresponding action procedure is <code>inverse()</code>.</p>
<dt><code>sin</code></p>
<dd> Computes the sine of the number in the display, as interpreted by the current DRG mode (see DRG, below). If inverted, it computes the arcsine. The corresponding action procedure is <code>sine()</code>.</p>
<dt><code>cos</code></p>
<dd> Computes the cosine, or arccosine when inverted. The corresponding action procedure is <code>cosine()</code>.</p>
<dt><code>tan</code></p>
<dd> Computes the tangent, or arctangent when inverted. The corresponding action procedure is <code>tangent()</code>.</p>
<dt><code>DRG</code></p>
<dd> Changes the DRG mode, as indicated by &#8216;DEG&#8217;, &#8216;RAD&#8217;, or &#8216;GRAD&#8217; at the bottom of the calculator &#8220;liquid crystal&#8221; display. When in &#8216;DEG&#8217; mode, numbers in the display are taken as being degrees. In &#8216;RAD&#8217; mode, numbers are in radians, and in &#8216;GRAD&#8217; mode, numbers are in grads. When inverted, the DRG key has a feature of converting degrees to radians to grads and vice-versa. Example: put the calculator into &#8216;DEG&#8217; mode, and enter &quot;45 INV DRG&quot;. The display should now show something along the lines of &quot;.785398&quot;, which is 45 degrees converted to radians. The corresponding action procedure is <code>degree()</code>.</p>
<dt><code>e</code></p>
<dd> The constant &#8216;e&#8217;. (2.7182818&#8230;). The corresponding action procedure is <code>e()</code>.</p>
<dt><code>EE</code></p>
<dd> Used for entering exponential numbers. For example, to get &quot;-2.3E-4&quot; you&#8217;d enter &quot;2 . 3 +/- EE 4 +/-&quot;. The corresponding action procedure is <code>scientific()</code>.</p>
<dt><code>log</code></p>
<dd> Calculates the log (base 10) of the number in the display. When inverted, it raises &quot;10.0&quot; to the number in the display. For example, entering &quot;3 INV log&quot; should result in &quot;1000&quot;. The corresponding action procedure is <code>logarithm()</code>.</p>
<dt><code>ln</code></p>
<dd> Calculates the log (base e) of the number in the display. When inverted, it raises &quot;e&quot; to the number in the display. For example, entering &quot;e ln&quot; should result in &quot;1&quot;. The corresponding action procedure is <code>naturalLog()</code>.</p>
<dt><code>y^x</code></p>
<dd> Raises the number on the left to the power of the number on the right. For example &quot;2 y^x 3 =&quot; results in &quot;8&quot;, which is 2^3. For a further example, &quot;(1+2+3) y^x (1+2) =&quot; equals &quot;6 y^x 3&quot; which equals &quot;216&quot;. The corresponding action procedure is <code>power()</code>.</p>
<dt><code>not</code></p>
<dd> Performs a bitwise not. The corresponding action procedure is <code>not()</code>.</p>
<dt><code>and</code></p>
<dd> Performs a bitwise and. The corresponding action procedure is <code>and()</code>.</p>
<dt><code>or</code></p>
<dd> Performs a bitwise or. The corresponding action procedure is <code>or()</code>.</p>
<dt><code>xor</code></p>
<dd> Performs a bitwise exclusive or. The corresponding action procedure is <code>xor()</code>.</p>
<dt><code>trunc</code></p>
<dd> Truncates the number in the display to an integer. The corresponding action procedure is <code>trunc()</code>.</p>
<dt><code>PI</code></p>
<dd> The constant &#8216;pi&#8217;. (3.1415927&#8230;.) The corresponding action procedure is <code>pi()</code>.</p>
<dt><code>x!</code></p>
<dd> Computes the factorial of the number in the display. The number in the display must be an integer in the range 0-500, though, depending on your math library, it might overflow long before that. The corresponding action procedure is <code>factorial()</code>.</p>
<dt><code>(</code></p>
<dd> Left parenthesis. The corresponding action procedure for TI calculators is <code>leftParen()</code>.</p>
<dt><code>)</code></p>
<dd> Right parenthesis. The corresponding action procedure for TI calculators is <code>rightParen()</code>.</p>
<dt><code>base</code></p>
<dd> Changes the number base, as indicated by &#8216;DEC&#8217;, &#8216;HEX, or &#8216;OCT&#8217; at the bottom of the calculator display. When in &#8216;DEC&#8217; mode, numbers in the display are taken as being decimal (base 10). In &#8216;HEX&#8217; mode, numbers are in hexadecimal (base 16), and in &#8216;OCT&#8217; mode, numbers are in octal (base 8). The corresponding action procedure is <code>base()</code>.</p>
<dt><code>shl</code></p>
<dd> Performs an arithmetic bitwise shift left, For example, entering &quot;1 shl 2&quot; should result in &quot;4&quot;. The corresponding action procedure is <code>shl()</code>.</p>
<dt><code>shr</code></p>
<dd> Performs an arithmetic bitwise shift right, For example, entering &quot;8 shr 1&quot; should result in &quot;4&quot;. The corresponding action procedure is <code>shr()</code>.</p>
<dt><code>mod</code></p>
<dd> Performs the modulo operation, which calculates the remainder when dividing the first number by the second. For example, entering &quot;14 mod 8&quot; should result in &quot;6&quot;. The corresponding action procedure is <code>mod()</code>.</p>
<dt><code>/</code></p>
<dd> Division. The corresponding action procedure is <code>divide()</code>.</p>
<dt><code>*</code></p>
<dd> Multiplication. The corresponding action procedure is <code>multiply()</code>.</p>
<dt><code>&#8211;</code></p>
<dd> Subtraction. The corresponding action procedure is <code>subtract()</code>.</p>
<dt><code>+</code></p>
<dd> Addition. The corresponding action procedure is <code>add()</code>.</p>
<dt><code>=</code></p>
<dd> Perform calculation. The TI-specific action procedure is <code>equal()</code>.</p>
<dt><code>STO</code></p>
<dd> Copies the number in the display to the memory location. The corresponding action procedure is <code>store()</code>.</p>
<dt><code>RCL</code></p>
<dd> Copies the number from the memory location to the display. The corresponding action procedure is <code>recall()</code>.</p>
<dt><code>SUM</code></p>
<dd> Adds the number in the display to the number in the memory location. The corresponding action procedure is <code>sum()</code>.</p>
<dt><code>EXC</code></p>
<dd> Swaps the number in the display with the number in the memory location. The corresponding action procedure for the TI calculator is <code>exchange()</code>.</p>
<dt><code>+/-</code></p>
<dd> Negate; change sign. The corresponding action procedure is <code>negate()</code>.</p>
<dt><code>.</code></p>
<dd> Decimal point. The action procedure is <code>decimal()</code>. </p>
</dl>
<p> <i>Calculator Key Usage (RPN mode):</i> The number keys, CHS (change sign), +, -, *, /, and ENTR keys all do exactly what you would expect them to do. Many of the remaining keys are the same as in TI mode. The differences are detailed below. The action procedure for the ENTR key is <code>enter()</code>. </p>
<dl>
<dt><code>&lt;-</code></p>
<dd> This is a backspace key that can be used if you make a mistake while entering a number. It will erase digits from the display. (See BUGS). Inverse backspace will clear the X register. The corresponding action procedure is <code>back()</code>.</p>
<dt><code>ON</code></p>
<dd> Clears the display, the state, and the memory. Pressing it with the third pointer button turns off the calculator, in that it exits the program. To clear state, the action procedure is <code>off</code>; to quit, <code>quit()</code>.</p>
<dt><code>INV</code></p>
<dd> Inverts the meaning of the function keys. This would be the <i>f</i> key on an HP calculator, but <i>xcalc</i> does not display multiple legends on each key. See the individual function keys for details.</p>
<dt><code>10^x</code></p>
<dd> Raises &quot;10.0&quot; to the number in the top of the stack. When inverted, it calculates the log (base 10) of the number in the display. The corresponding action procedure is <code>tenpower()</code>.</p>
<dt><code>e^x</code></p>
<dd> Raises &quot;e&quot; to the number in the top of the stack. When inverted, it calculates the log (base e) of the number in the display. The action procedure is <code>epower()</code>.</p>
<dt><code>STO</code></p>
<dd> Copies the number in the top of the stack to a memory location. There are 10 memory locations. The desired memory is specified by following this key with a digit key.</p>
<dt><code>RCL</code></p>
<dd> Pushes the number from the specified memory location onto the stack.</p>
<dt><code>SUM</code></p>
<dd> Adds the number on top of the stack to the number in the specified memory location.</p>
<dt><code>x:y</code></p>
<dd> Exchanges the numbers in the top two stack positions, the X and Y registers. The corresponding action procedure is <code>XexchangeY()</code>.</p>
<dt><code>R v</code></p>
<dd> Rolls the stack downward. When inverted, it rolls the stack upward. The corresponding action procedure is <code>roll()</code>.</p>
<dt><i>blank</i></p>
<dd> These keys were used for programming functions on the HP-10C. Their functionality has not been duplicated in <i>xcalc</i>.</dl>
<p> Finally, there are two additional action procedures: <code>bell()</code>, which rings the bell; and <code>selection()</code>, which performs a cut on the entire number in the calculator&#8217;s &#8220;liquid crystal&#8221; display.</p>
<h2>ACCELERATORS</h2>
<p> Accelerators are shortcuts for entering commands. <i>xcalc</i> provides some sample keyboard accelerators; also users can customize accelerators. The numeric keypad accelerators provided by <i>xcalc</i> should be intuitively correct. The accelerators defined by <i>xcalc</i> on the main keyboard are given below: </p>
<table>
<tr VALIGN=top>
<td>TI Key</td>
<td>HP Key</td>
<td>Keyboard Accelerator</td>
<td>TI Function</td>
<td>HP Function
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>SQRT</td>
<td>SQRT</td>
<td>r</td>
<td>squareRoot()</td>
<td>squareRoot()
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td>ON</td>
<td>space</td>
<td>clear()</td>
<td>clear()
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td>&lt;-</td>
<td>Delete</td>
<td>clear()</td>
<td>back()
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td>&lt;-</td>
<td>Backspace</td>
<td>clear()</td>
<td>back()
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td>&lt;-</td>
<td>Control-H</td>
<td>clear()</td>
<td>back()
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td></td>
<td>Clear</td>
<td>clear()</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td>ON</td>
<td>q</td>
<td>quit()</td>
<td>quit()
</td>
</tr>
<tr VALIGN=top>
<td>AC</td>
<td>ON</td>
<td>Control-C</td>
<td>quit()</td>
<td>quit()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>INV</td>
<td>i</td>
<td>i</td>
<td>inverse()</td>
<td>inverse()
</td>
</tr>
<tr VALIGN=top>
<td>sin</td>
<td>s</td>
<td>s</td>
<td>sine()</td>
<td>sine()
</td>
</tr>
<tr VALIGN=top>
<td>cos</td>
<td>c</td>
<td>c</td>
<td>cosine()</td>
<td>cosine()
</td>
</tr>
<tr VALIGN=top>
<td>tan</td>
<td>t</td>
<td>t</td>
<td>tangent()</td>
<td>tangent()
</td>
</tr>
<tr VALIGN=top>
<td>DRG</td>
<td>DRG</td>
<td>d</td>
<td>degree()</td>
<td>degree()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>e</td>
<td></td>
<td>e</td>
<td>e()</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ln</td>
<td>ln</td>
<td>l</td>
<td>naturalLog()</td>
<td>naturalLog()
</td>
</tr>
<tr VALIGN=top>
<td>y^x</td>
<td>y^x</td>
<td>^</td>
<td>power()</td>
<td>power()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>PI</td>
<td>PI</td>
<td>p</td>
<td>pi()</td>
<td>pi()
</td>
</tr>
<tr VALIGN=top>
<td>x!</td>
<td>x!</td>
<td>!</td>
<td>factorial()</td>
<td>factorial()
</td>
</tr>
<tr VALIGN=top>
<td>(</td>
<td></td>
<td>(</td>
<td>leftParen()</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>)</td>
<td></td>
<td>)</td>
<td>rightParen()</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>/</td>
<td>/</td>
<td>/</td>
<td>divide()</td>
<td>divide()
</td>
</tr>
<tr VALIGN=top>
<td>*</td>
<td>*</td>
<td>*</td>
<td>multiply()</td>
<td>multiply()
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>subtract()</td>
<td>subtract()
</td>
</tr>
<tr VALIGN=top>
<td>+</td>
<td>+</td>
<td>+</td>
<td>add()</td>
<td>add()
</td>
</tr>
<tr VALIGN=top>
<td>=</td>
<td></td>
<td>=</td>
<td>equal()</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>0..9</td>
<td>0..9</td>
<td>0..9</td>
<td>digit()</td>
<td>digit()
</td>
</tr>
<tr VALIGN=top>
<td>+/-</td>
<td>CHS</td>
<td>n</td>
<td>negate()</td>
<td>negate()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>x:y</td>
<td>x</td>
<td></td>
<td>XexchangeY()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>ENTR</td>
<td>Return</td>
<td></td>
<td>enter()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>ENTR</td>
<td>Linefeed</td>
<td></td>
<td>enter()
</td>
</tr>
</table>
<h2>CUSTOMIZATION</h2>
<p> The application class name is XCalc. </p>
<p> <i>xcalc</i> has an enormous application defaults file which specifies the position, label, and function of each key on the calculator. It also gives translations to serve as keyboard accelerators. Because these resources are not specified in the source code, you can create a customized calculator by writing a private application defaults file, using the Athena Command and Form widget resources to specify the size and position of buttons, the label for each button, and the function of each button. </p>
<p> The foreground and background colors of each calculator key can be individually specified. For the TI calculator, a classical color resource specification might be: </p>
<p> XCalc.ti.Command.background:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>gray50</p>
<p> XCalc.ti.Command.foreground:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>white</p>
<p> For each of buttons 20, 25, 30, 35, and 40, specify:<br />
 XCalc.ti.button20.background:<tt>&nbsp;<wbr>&nbsp;</tt>black</p>
<p> XCalc.ti.button20.foreground:<tt>&nbsp;<wbr>&nbsp;</tt>white</p>
<p> For each of buttons 22, 23, 24, 27, 28, 29, 32, 33, 34, 37, 38, and 39:<br />
 XCalc.ti.button22.background:<tt>&nbsp;<wbr>&nbsp;</tt>white</p>
<p> XCalc.ti.button22.foreground:<tt>&nbsp;<wbr>&nbsp;</tt>black</p>
<h2>WIDGET HIERARCHY</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xcalc</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XCalc xcalc
        Form  ti  <i>or</i>  hp    <i>(the name depends on the mode)</i>
                Form  bevel
                        Form  screen
                                Label  M
                                Toggle  LCD
                                Label  INV
                                Label  DEG
                                Label  RAD
                                Label  GRAD
                                Label  P
                Command  button1
                Command  button2
                Command  button3
<i>and so on, ...</i>
                Command  button38
                Command  button39
                Command  button40
</pre>
<h2>APPLICATION RESOURCES</h2>
<dl>
<dt><code>rpn</code> (Class <code>Rpn</code>)</p>
<dd> Specifies that the rpn mode should be used. The default is TI mode.</p>
<dt><code>stipple</code> (Class <code>Stipple</code>)</p>
<dd> Indicates that the background should be stippled. The default is &#8220;on&#8221; for monochrome displays, and &#8220;off&#8221; for color displays.</p>
<dt><code>cursor</code> (Class <code>Cursor</code>)</p>
<dd> The name of the symbol used to represent the pointer. The default is &#8220;hand2&#8221;.</dl>
<h2>COLORS</h2>
<p> If you would like xcalc to use its ti colors, include the following in the #ifdef COLOR section of the file you read with xrdb: </p>
<p> *customization: -color </p>
<p> This will cause xcalc to pick up the colors in the app-defaults color customization file: <i>/etc/X11/app-defaults/XCalc-color</i>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), the Athena Widget Set</p>
<h2>BUGS</h2>
<p> HP mode is not completely debugged. In particular, the stack is not handled properly after errors.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994 X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> John Bradley, University of Pennsylvania<br />
 Mark Rosenstein, MIT Project Athena<br />
 Donna Converse, MIT X Consortium </p>
<h2>Index</h2>
