---
title: "rrdgraph_rpn(1)"
name: "rrdgraph_rpn"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdgraph_rpn/"
description: "rrdgraph_rpn – About RPN Math in rrdtool graph"
---

<h2 class="name">NAME</h2>
<p> rrdgraph_rpn &#8211; About RPN Math in rrdtool graph </p>
<h2>SYNOPSIS</h2>
<p> <i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i>:=<i>vname</i>|<i>operator</i>|<i>value</i>[,<i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> If you have ever used a traditional <font SIZE="-1">HP</font> calculator you already know <font SIZE="-1"><code>RPN</code></font> (Reverse Polish Notation). The idea behind <font SIZE="-1"><code>RPN</code></font> is that you have a stack and push your data onto this stack. Whenever you execute an operation, it takes as many elements from the stack as needed. Pushing is done implicitly, so whenever you specify a number or a variable, it gets pushed onto the stack automatically. </p>
<p> At the end of the calculation there should be one and only one value left on the stack. This is the outcome of the function and this is what is put into the <i>vname</i>. For <font SIZE="-1"><code>CDEF</code></font> instructions, the stack is processed for each data point on the graph. <font SIZE="-1"><code>VDEF</code></font> instructions work on an entire data set in one run. Note, that currently <font SIZE="-1"><code>VDEF</code></font> instructions only support a limited list of functions. </p>
<p> Example: <tt>&quot;VDEF:maximum=mydata,MAXIMUM&quot;</tt> </p>
<p> This will set variable &#8220;maximum&#8221; which you now can use in the rest of your <font SIZE="-1">RRD</font> script. </p>
<p> Example: <tt>&quot;CDEF:mydatabits=mydata,8,*&quot;</tt> </p>
<p> This means: push variable <i>mydata</i>, push the number 8, execute the operator <i>*</i>. The operator needs two elements and uses those to return one value. This value is then stored in <i>mydatabits</i>. As you may have guessed, this instruction means nothing more than <i>mydatabits = mydata * 8</i>. The real power of <font SIZE="-1"><code>RPN</code></font> lies in the fact that it is always clear in which order to process the input. For expressions like <tt>&quot;a = b + 3 * 5&quot;</tt> you need to multiply 3 with 5 first before you add <i>b</i> to get <i>a</i>. However, with parentheses you could change this order: <tt>&quot;a = (b + 3) * 5&quot;</tt>. In <font SIZE="-1"><code>RPN</code></font>, you would do <tt>&quot;a = b, 3, +, 5, *&quot;</tt> without the need for parentheses.</p>
<h2>OPERATORS</h2>
<dl>
<dt>Boolean operators</p>
<dd> <font SIZE="-1"><code>LT</code></font><code>, </code><font SIZE="-1"><code>LE</code></font><code>, </code><font SIZE="-1"><code>GT</code></font><code>, </code><font SIZE="-1"><code>GE</code></font><code>, </code><font SIZE="-1"><code>EQ</code></font><code>, </code><font SIZE="-1"><code>NE</code></font> </p>
<p> Pop two elements from the stack, compare them for the selected condition and return 1 for true or 0 for false. Comparing an <i>unknown</i> or an <i>infinite</i> value will result in <i>unknown</i> returned &#8230; which will also be treated as false by the <font SIZE="-1"><code>IF</code></font> call. </p>
<p> <font SIZE="-1"><code>UN</code></font><code>, </code><font SIZE="-1"><code>ISINF</code></font> </p>
<p> Pop one element from the stack, compare this to <i>unknown</i> respectively to <i>positive or negative infinity</i>. Returns 1 for true or 0 for false. </p>
<p> <font SIZE="-1"><code>IF</code></font> </p>
<p> Pops three elements from the stack. If the element popped last is 0 (false), the value popped first is pushed back onto the stack, otherwise the value popped second is pushed back. This does, indeed, mean that any value other than 0 is considered to be true. </p>
<p> Example: <tt>&quot;A,B,C,IF&quot;</tt> should be read as <tt>&quot;if (A) then (B) else (C)&quot;</tt> </p>
<dt>Comparing values</p>
<dd> <font SIZE="-1"><code>MIN</code></font><code>, </code><font SIZE="-1"><code>MAX</code></font> </p>
<p> Pops two elements from the stack and returns the smaller or larger, respectively. Note that <i>infinite</i> is larger than anything else. If one of the input numbers is <i>unknown</i> then the result of the operation will be <i>unknown</i> too. </p>
<p> <font SIZE="-1"><code>LIMIT</code></font> </p>
<p> Pops two elements from the stack and uses them to define a range. Then it pops another element and if it falls inside the range, it is pushed back. If not, an <i>unknown</i> is pushed. </p>
<p> The range defined includes the two boundaries (so: a number equal to one of the boundaries will be pushed back). If any of the three numbers involved is either <i>unknown</i> or <i>infinite</i> this function will always return an <i>unknown</i> </p>
<p> Example: <tt>&quot;CDEF:a=alpha,0,100,LIMIT&quot;</tt> will return <i>unknown</i> if alpha is lower than 0 or if it is higher than 100. </p>
<dt>Arithmetics</p>
<dd> <code>+, -, *, /, %</code> </p>
<p> Add, subtract, multiply, divide, modulo </p>
<p> <font SIZE="-1"><code>ADDNAN</code></font> </p>
<p> NAN-safe addition. If one parameter is <font SIZE="-1">NAN/UNKNOWN</font> it&#8217;ll be treated as zero. If both parameters are <font SIZE="-1">NAN/UNKNOWN</font>, <font SIZE="-1">NAN/UNKNOWN</font> will be returned. </p>
<p> <font SIZE="-1"><code>SIN</code></font><code>, </code><font SIZE="-1"><code>COS</code></font><code>, </code><font SIZE="-1"><code>LOG</code></font><code>, </code><font SIZE="-1"><code>EXP</code></font><code>, </code><font SIZE="-1"><code>SQRT</code></font> </p>
<p> Sine and cosine (input in radians), log and exp (natural logarithm), square root. </p>
<p> <font SIZE="-1"><code>ATAN</code></font> </p>
<p> Arctangent (output in radians). </p>
<p> <font SIZE="-1"><code>ATAN2</code></font> </p>
<p> Arctangent of y,x components (output in radians). This pops one element from the stack, the x (cosine) component, and then a second, which is the y (sine) component. It then pushes the arctangent of their ratio, resolving the ambiguity between quadrants. </p>
<p> Example: <tt>&quot;CDEF:angle=Y,X,ATAN2,RAD2DEG&quot;</tt> will convert <tt>&quot;X,Y&quot;</tt> components into an angle in degrees. </p>
<p> <font SIZE="-1"><code>FLOOR</code></font><code>, </code><font SIZE="-1"><code>CEIL</code></font> </p>
<p> Round down or up to the nearest integer. </p>
<p> <font SIZE="-1"><code>DEG2RAD</code></font><code>, </code><font SIZE="-1"><code>RAD2DEG</code></font> </p>
<p> Convert angle in degrees to radians, or radians to degrees. </p>
<p> <font SIZE="-1"><code>ABS</code></font> </p>
<p> Take the absolute value.</p>
<dt>Set Operations</p>
<dd> <font SIZE="-1"><code>SORT</code></font><code>, </code><font SIZE="-1"><code>REV</code></font> </p>
<p> Pop one element from the stack. This is the <i>count</i> of items to be sorted (or reversed). The top <i>count</i> of the remaining elements are then sorted (or reversed) in place on the stack. </p>
<p> Example: <tt>&quot;CDEF:x=v1,v2,v3,v4,v5,v6,6,SORT,POP,5,REV,POP,+,+,+,4,/&quot;</tt> will compute the average of the values v1 to v6 after removing the smallest and largest. </p>
<p> <font SIZE="-1"><code>AVG</code></font> </p>
<p> Pop one element (<i>count</i>) from the stack. Now pop <i>count</i> elements and build the average, ignoring all <font SIZE="-1">UNKNOWN</font> values in the process. </p>
<p> Example: <tt>&quot;CDEF:x=a,b,c,d,4,AVG&quot;</tt> </p>
<p> <font SIZE="-1"><code>TREND</code></font><code>, </code><font SIZE="-1"><code>TRENDNAN</code></font> </p>
<p> Create a &#8220;sliding window&#8221; average of another data series. </p>
<p> Usage: CDEF:smoothed=x,1800,TREND </p>
<p> This will create a half-hour (1800 second) sliding window average of x. The average is essentially computed as shown here: </p>
<pre><code>
+ -- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!---&gt;now
        delay t0 &lt; -- -- -- -- -- -- ---&gt;delay t1 &lt; -- -- -- -- -- -- ---&gt;delay t2 &lt; -- -- -- -- -- -- ---&gt;Value at sample(t0)
will be the average between(t0 - delay) and (t0)
                                                Value at sample(t1)
will be the average between(t1 - delay) and (t1)
                                                Value at sample(t2)
will be the average between(t2 - delay) and (t2)
</code></pre>
<p> <font SIZE="-1">TRENDNAN</font> is &#8211; in contrast to <font SIZE="-1">TREND</font> &#8211; NAN-safe. If you use <font SIZE="-1">TREND</font> and one source value is <font SIZE="-1">NAN</font> the complete sliding window is affected. The <font SIZE="-1">TRENDNAN</font> operation ignores all NAN-values in a sliding window and computes the average of the remaining values. </p>
<p> <font SIZE="-1"><code>PREDICT</code></font><code>, </code><font SIZE="-1"><code>PREDICTSIGMA</code></font> </p>
<p> Create a &#8220;sliding window&#8221; average/sigma of another data series, that also shifts the data series by given amounts of of time as well </p>
<p> Usage &#8211; explicit stating shifts: CDEF:predict=&lt;shift n&gt;,&#8230;,&lt;shift 1&gt;,n,&lt;window&gt;,x,PREDICT CDEF:sigma=&lt;shift n&gt;,&#8230;,&lt;shift 1&gt;,n,&lt;window&gt;,x,PREDICTSIGMA </p>
<p> Usage &#8211; shifts defined as a base shift and a number of time this is applied CDEF:predict=&lt;shift multiplier&gt;,-n,&lt;window&gt;,x,PREDICT CDEF:sigma=&lt;shift multiplier&gt;,-n,&lt;window&gt;,x,PREDICTSIGMA </p>
<p> Example: CDEF:predict=172800,86400,2,1800,x,PREDICT </p>
<p> This will create a half-hour (1800 second) sliding window average/sigma of x, that average is essentially computed as shown here: </p>
<pre><code>
+ -- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!-- -!---&gt;now
        shift 1 t0 &lt; -- -- -- -- -- -- -- -- -- -- ---&gt;window &lt; -- -- -- -- -- -- ---&gt;shift 2 &lt; -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---&gt;window &lt; -- -- -- -- -- -- ---&gt;shift 1 t1 &lt; -- -- -- -- -- -- -- -- -- -- ---&gt;window &lt; -- -- -- -- -- -- ---&gt;shift 2 &lt; -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---&gt;window &lt; -- -- -- -- -- -- ---&gt;Value at sample(t0)
will be the average between(t0 - shift1 - window) and (t0 - shift1) and between(t0 - shift2 - window) and (t0 - shift2) Value at sample(t1)
will be the average between(t1 - shift1 - window) and (t1 - shift1) and between(t1 - shift2 - window) and (t1 - shift2)
</code></pre>
<p> The function is by design NAN-safe. This also allows for extrapolation into the future (say a few days) &#8211; you may need to define the data series whit the optional start= parameter, so that the source data series has enough data to provide prediction also at the beginning of a graph&#8230; </p>
<p> Here an example, that will create a 10 day graph that also shows the prediction 3 days into the future with its uncertainty value (as defined by avg+-4*sigma) This also shows if the prediction is exceeded at a certain point. </p>
<p> rrdtool graph image.png &#8211;imgformat=PNG \<br />
&nbsp;<wbr>&#8211;start=-7days &#8211;end=+3days &#8211;width=1000 &#8211;height=200 &#8211;alt-autoscale-max&nbsp;<wbr>\<br />
&nbsp;<wbr>DEF:value=value.rrd:value:AVERAGE:start=-14days&nbsp;<wbr>\<br />
&nbsp;<wbr>LINE1:value#ff0000:value&nbsp;<wbr>\<br />
&nbsp;<wbr>CDEF:predict=86400,-7,1800,value,PREDICT&nbsp;<wbr>\<br />
&nbsp;<wbr>CDEF:sigma=86400,-7,1800,value,PREDICTSIGMA&nbsp;<wbr>\<br />
&nbsp;<wbr>CDEF:upper=predict,sigma,3,*,+&nbsp;<wbr>\<br />
&nbsp;<wbr>CDEF:lower=predict,sigma,3,*,-&nbsp;<wbr>\<br />
&nbsp;<wbr>LINE1:predict#00ff00:prediction&nbsp;<wbr>\<br />
&nbsp;<wbr>LINE1:upper#0000ff:upper\&nbsp;<wbr>certainty\&nbsp;<wbr>limit&nbsp;<wbr>\<br />
&nbsp;<wbr>LINE1:lower#0000ff:lower\&nbsp;<wbr>certainty\&nbsp;<wbr>limit&nbsp;<wbr>\<br />
&nbsp;<wbr>CDEF:exceeds=value,UN,0,value,lower,upper,LIMIT,UN,IF&nbsp;<wbr>\<br />
&nbsp;<wbr>TICK:exceeds#aa000080:1 </p>
<p> Note: Experience has shown that a factor between 3 and 5 to scale sigma is a good discriminator to detect abnormal behavior. This obviously depends also on the type of data and how &#8220;noisy&#8221; the data series is. </p>
<p> This prediction can only be used for short term extrapolations &#8211; say a few days into the future-</p>
<dt>Special values</p>
<dd> <font SIZE="-1"><code>UNKN</code></font> </p>
<p> Pushes an unknown value on the stack </p>
<p> <font SIZE="-1"><code>INF</code></font><code>, </code><font SIZE="-1"><code>NEGINF</code></font> </p>
<p> Pushes a positive or negative infinite value on the stack. When such a value is graphed, it appears at the top or bottom of the graph, no matter what the actual value on the y-axis is. </p>
<p> <font SIZE="-1"><code>PREV</code></font> </p>
<p> Pushes an <i>unknown</i> value if this is the first value of a data set or otherwise the result of this <font SIZE="-1"><code>CDEF</code></font> at the previous time step. This allows you to do calculations across the data. This function cannot be used in <font SIZE="-1"><code>VDEF</code></font> instructions. </p>
<p> <font SIZE="-1"><code>PREV</code></font><code>(vname)</code> </p>
<p> Pushes an <i>unknown</i> value if this is the first value of a data set or otherwise the result of the vname variable at the previous time step. This allows you to do calculations across the data. This function cannot be used in <font SIZE="-1"><code>VDEF</code></font> instructions. </p>
<p> <font SIZE="-1"><code>COUNT</code></font> </p>
<p> Pushes the number 1 if this is the first value of the data set, the number 2 if it is the second, and so on. This special value allows you to make calculations based on the position of the value within the data set. This function cannot be used in <font SIZE="-1"><code>VDEF</code></font> instructions.</p>
<dt>Time</p>
<dd> Time inside RRDtool is measured in seconds since the epoch. The epoch is defined to be <tt>&quot;Thu Jan&nbsp;<wbr>&nbsp;<wbr>1 00:00:00 UTC 1970&quot;</tt>. </p>
<p> <font SIZE="-1"><code>NOW</code></font> </p>
<p> Pushes the current time on the stack. </p>
<p> <font SIZE="-1"><code>TIME</code></font> </p>
<p> Pushes the time the currently processed value was taken at onto the stack. </p>
<p> <font SIZE="-1"><code>LTIME</code></font> </p>
<p> Takes the time as defined by <font SIZE="-1"><code>TIME</code></font>, applies the time zone offset valid at that time including daylight saving time if your <font SIZE="-1">OS</font> supports it, and pushes the result on the stack. There is an elaborate example in the examples section below on how to use this.</p>
<dt>Processing the stack directly</p>
<dd> <font SIZE="-1"><code>DUP</code></font><code>, </code><font SIZE="-1"><code>POP</code></font><code>, </code><font SIZE="-1"><code>EXC</code></font> </p>
<p> Duplicate the top element, remove the top element, exchange the two top elements. </p>
</dl>
<h2>VARIABLES</h2>
<p> These operators work only on <font SIZE="-1"><code>VDEF</code></font> statements. Note that currently <font SIZE="-1">ONLY</font> these work for <font SIZE="-1"><code>VDEF</code></font>.</p>
<dl>
<dt><font SIZE="-1">MAXIMUM</font>, <font SIZE="-1">MINIMUM</font>, <font SIZE="-1">AVERAGE</font></p>
<dd> Return the corresponding value, <font SIZE="-1">MAXIMUM</font> and <font SIZE="-1">MINIMUM</font> also return the first occurrence of that value in the time component. </p>
<p> Example: <tt>&quot;VDEF:avg=mydata,AVERAGE&quot;</tt></p>
<dt><font SIZE="-1">STDEV</font></p>
<dd> Returns the standard deviation of the values. </p>
<p> Example: <tt>&quot;VDEF:stdev=mydata,STDEV&quot;</tt></p>
<dt><font SIZE="-1">LAST</font>, <font SIZE="-1">FIRST</font></p>
<dd> Return the last/first non-nan or infinite value for the selected data stream, including its timestamp. </p>
<p> Example: <tt>&quot;VDEF:first=mydata,FIRST&quot;</tt></p>
<dt><font SIZE="-1">TOTAL</font></p>
<dd> Returns the rate from each defined time slot multiplied with the step size. This can, for instance, return total bytes transferred when you have logged bytes per second. The time component returns the number of seconds. </p>
<p> Example: <tt>&quot;VDEF:total=mydata,TOTAL&quot;</tt></p>
<dt><font SIZE="-1">PERCENT</font>, <font SIZE="-1">PERCENTNAN</font></p>
<dd> This should follow a <font SIZE="-1"><code>DEF</code></font> or <font SIZE="-1"><code>CDEF</code></font> <i>vname</i>. The <i>vname</i> is popped, another number is popped which is a certain percentage (0..100). The data set is then sorted and the value returned is chosen such that <i>percentage</i> percent of the values is lower or equal than the result. For <font SIZE="-1">PERCENTNAN</font> <i>Unknown</i> values are ignored, but for <font SIZE="-1">PERCENT</font> <i>Unknown</i> values are considered lower than any finite number for this purpose so if this operator returns an <i>unknown</i> you have quite a lot of them in your data. <code>Inf</code>inite numbers are lesser, or more, than the finite numbers and are always more than the <i>Unknown</i> numbers. (NaN &lt; -INF &lt; finite values &lt; <font SIZE="-1">INF</font>) </p>
<p> Example: <tt>&quot;VDEF:perc95=mydata,95,PERCENT&quot;</tt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><tt>&quot;VDEF:percnan95=mydata,95,PERCENTNAN&quot;</tt></p>
<dt><font SIZE="-1">LSLSLOPE</font>, <font SIZE="-1">LSLINT</font>, <font SIZE="-1">LSLCORREL</font></p>
<dd> Return the parameters for a <code>L</code>east <code>S</code>quares <code>L</code>ine <i>(y = mx +b)</i> which approximate the provided dataset. <font SIZE="-1">LSLSLOPE</font> is the slope <i>(m)</i> of the line related to the <font SIZE="-1">COUNT</font> position of the data. <font SIZE="-1">LSLINT</font> is the y-intercept <i>(b)</i>, which happens also to be the first data point on the graph. <font SIZE="-1">LSLCORREL</font> is the Correlation Coefficient (also know as Pearson&#8217;s Product Moment Correlation Coefficient). It will range from 0 to +/-1 and represents the quality of fit for the approximation. </p>
<p> Example: <tt>&quot;VDEF:slope=mydata,LSLSLOPE&quot;</tt></dl>
<h2>SEE ALSO</h2>
<p> rrdgraph gives an overview of how <code>rrdtool graph</code> works. rrdgraph_data describes <font SIZE="-1"><code>DEF</code></font>,<font SIZE="-1"><code>CDEF</code></font> and <font SIZE="-1"><code>VDEF</code></font> in detail. rrdgraph_rpn describes the <font SIZE="-1"><code>RPN</code></font> language used in the <code>?DEF</code> statements. rrdgraph_graph page describes all of the graph and print functions. </p>
<p> Make sure to read rrdgraph_examples for tips&amp;tricks.</p>
<h2>AUTHOR</h2>
<p> Program by Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<p> This manual page by Alex van den Bogaerdt &lt;alex [at] vandenbogaerdt.nl&gt; with corrections and/or additions by several people </p>
<h2>Index</h2>
