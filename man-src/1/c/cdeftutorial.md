---
title: "cdeftutorial(1)"
name: "cdeftutorial"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdeftutorial/"
description: "cdeftutorial – Alex van den Bogaerdt’s CDEF tutorial"
---

<h2 class="name">NAME</h2>
<p> cdeftutorial &#8211; Alex van den Bogaerdt&#8217;s CDEF tutorial </p>
<h2>DESCRIPTION</h2>
<p> Intention of this document: to provide some examples of the commonly used parts of RRDtool&#8217;s <font SIZE="-1">CDEF</font> language. </p>
<p> If you think some important feature is not explained properly, and if adding it to this document would benefit most users, please do ask me to add it. I will then try to provide an answer in the next release of this tutorial. No feedback equals no changes! Additions to this document are also welcome. &#8212; Alex van den Bogaerdt &lt;alex [at] vandenbogaerdt.nl&gt;</p>
<h3>Why this tutorial?</h3>
<p> One of the powerful parts of RRDtool is its ability to do all sorts of calculations on the data retrieved from its databases. However, RRDtool&#8217;s many options and syntax make it difficult for the average user to understand. The manuals are good at explaining what these options do; however they do not (and should not) explain in detail why they are useful. As with my RRDtool tutorial: if you want a simple document in simple language you should read this tutorial. If you are happy with the official documentation, you may find this document too simple or even boring. If you do choose to read this tutorial, I also expect you to have read and fully understand my other tutorial.</p>
<h3>More reading</h3>
<p> If you have difficulties with the way I try to explain it please read Steve Rader&#8217;s rpntutorial. It may help you understand how this all works.</p>
<h2>What are CDEFs?</h2>
<p> When retrieving data from an <font SIZE="-1">RRD</font>, you are using a &#8220;<font SIZE="-1">DEF</font>&#8221; to work with that data. Think of it as a variable that changes over time (where time is the x-axis). The value of this variable is what is found in the database at that particular time and you can&#8217;t do any modifications on it. This is what CDEFs are for: they takes values from DEFs and perform calculations on them.</p>
<h2>Syntax</h2>
<pre>
   DEF:var_name_1=some.rrd:ds_name:CF
   CDEF:var_name_2=RPN_expression
</pre>
<p> You first define &#8220;var_name_1&#8221; to be data collected from data source &#8220;ds_name&#8221; found in <font SIZE="-1">RRD</font> &#8220;some.rrd&#8221; with consolidation function &#8220;<font SIZE="-1">CF</font>&#8221;. </p>
<p> Assume the ifInOctets <font SIZE="-1">SNMP</font> counter is saved in mrtg.rrd as the <font SIZE="-1">DS</font> &#8220;in&#8221;. Then the following <font SIZE="-1">DEF</font> defines a variable for the average of that data source: </p>
<pre>
   DEF:inbytes=mrtg.rrd:in:AVERAGE
</pre>
<p> Say you want to display bits per second (instead of bytes per second as stored in the database.) You have to define a calculation (hence &#8220;<font SIZE="-1">CDEF</font>&#8221;) on variable &#8220;inbytes&#8221; and use that variable (inbits) instead of the original: </p>
<pre>
   CDEF:inbits=inbytes,8,*
</pre>
<p> This tells RRDtool to multiply inbytes by eight to get inbits. I&#8217;ll explain later how this works. In the graphing or printing functions, you can now use inbits where you would use inbytes otherwise. </p>
<p> Note that the variable name used in the <font SIZE="-1">CDEF</font> (inbits) must not be the same as the variable named in the <font SIZE="-1">DEF</font> (inbytes)!</p>
<h2>RPN-expressions</h2>
<p> <font SIZE="-1">RPN</font> is short-hand for Reverse Polish Notation. It works as follows. You put the variables or numbers on a stack. You also put operations (things-to-do) on the stack and this stack is then processed. The result will be placed on the stack. At the end, there should be exactly one number left: the outcome of the series of operations. If there is not exactly one number left, RRDtool will complain loudly. </p>
<p> Above multiplication by eight will look like:</p>
<dl>
<dt>1.</p>
<dd> Start with an empty stack</p>
<dt>2.</p>
<dd> Put the content of variable inbytes on the stack</p>
<dt>3.</p>
<dd> Put the number eight on the stack</p>
<dt>4.</p>
<dd> Put the operation multiply on the stack</p>
<dt>5.</p>
<dd> Process the stack</p>
<dt>6.</p>
<dd> Retrieve the value from the stack and put it in variable inbits</dl>
<p> We will now do an example with real numbers. Suppose the variable inbytes would have value 10, the stack would be:</p>
<dl>
<dt>1.</p>
<dd> ||</p>
<dt>2.</p>
<dd> |10|</p>
<dt>3.</p>
<dd> |10|8|</p>
<dt>4.</p>
<dd> |10|8|*|</p>
<dt>5.</p>
<dd> |80|</p>
<dt>6.</p>
<dd> ||</dl>
<p> Processing the stack (step 5) will retrieve one value from the stack (from the right at step 4). This is the operation multiply and this takes two values off the stack as input. The result is put back on the stack (the value 80 in this case). For multiplication the order doesn&#8217;t matter, but for other operations like subtraction and division it does. Generally speaking you have the following order: </p>
<pre>
   y = A - B  --&gt;  y=minus(A,B)  --&gt;  CDEF:y=A,B,-
</pre>
<p> This is not very intuitive (at least most people don&#8217;t think so). For the function f(A,B) you reverse the position of &#8220;f&#8221;, but you do not reverse the order of the variables.</p>
<h2>Converting your wishes to RPN</h2>
<p> First, get a clear picture of what you want to do. Break down the problem in smaller portions until they cannot be split anymore. Then it is rather simple to convert your ideas into <font SIZE="-1">RPN</font>. </p>
<p> Suppose you have several RRDs and would like to add up some counters in them. These could be, for instance, the counters for every <font SIZE="-1">WAN</font> link you are monitoring. </p>
<p> You have: </p>
<pre>
   router1.rrd with link1in link2in
   router2.rrd with link1in link2in
   router3.rrd with link1in link2in
</pre>
<p> Suppose you would like to add up all these counters, except for link2in inside router2.rrd. You need to do: </p>
<p> (in this example, &#8220;router1.rrd:link1in&#8221; means the <font SIZE="-1">DS</font> link1in inside the <font SIZE="-1">RRD</font> router1.rrd) </p>
<pre><code>
router1.rrd : link1in
                  router1.rrd : link2in
                                    router2.rrd : link1in
                                                      router3.rrd : link1in
                                                                        router3.rrd : link2in-- -- -- -- -- -- -- -- -- --+(outcome of the sum)
</code></pre>
<p> As a mathematical function, this could be written: </p>
<p> <tt>&quot;add(router1.rrd:link1in , router1.rrd:link2in , router2.rrd:link1in , router3.rrd:link1in , router3.rrd:link2.in)&quot;</tt> </p>
<p> With RRDtool and <font SIZE="-1">RPN</font>, first, define the inputs: </p>
<pre>
   DEF:a=router1.rrd:link1in:AVERAGE
   DEF:b=router1.rrd:link2in:AVERAGE
   DEF:c=router2.rrd:link1in:AVERAGE
   DEF:d=router3.rrd:link1in:AVERAGE
   DEF:e=router3.rrd:link2in:AVERAGE
</pre>
<p> Now, the mathematical function becomes: <tt>&quot;add(a,b,c,d,e)&quot;</tt> </p>
<p> In <font SIZE="-1">RPN</font>, there&#8217;s no operator that sums more than two values so you need to do several additions. You add a and b, add c to the result, add d to the result and add e to the result. </p>
<pre>
   push a:         a     stack contains the value of a
   push b and add: b,+   stack contains the result of a+b
   push c and add: c,+   stack contains the result of a+b+c
   push d and add: d,+   stack contains the result of a+b+c+d
   push e and add: e,+   stack contains the result of a+b+c+d+e
</pre>
<p> What was calculated here would be written down as: </p>
<pre>
   ( ( ( (a+b) + c) + d) + e) &gt;
</pre>
<p> This is in <font SIZE="-1">RPN:</font> <tt>&quot;CDEF:result=a,b,+,c,+,d,+,e,+&quot;</tt> </p>
<p> This is correct but it can be made more clear to humans. It does not matter if you add a to b and then add c to the result or first add b to c and then add a to the result. This makes it possible to rewrite the <font SIZE="-1">RPN</font> into <tt>&quot;CDEF:result=a,b,c,d,e,+,+,+,+&quot;</tt> which is evaluated differently: </p>
<pre>
   push value of variable a on the stack: a
   push value of variable b on the stack: a b
   push value of variable c on the stack: a b c
   push value of variable d on the stack: a b c d
   push value of variable e on the stack: a b c d e
   push operator + on the stack:          a b c d e +
   and process it:                        a b c P   (where P == d+e)
   push operator + on the stack:          a b c P +
   and process it:                        a b Q     (where Q == c+P)
   push operator + on the stack:          a b Q +
   and process it:                        a R       (where R == b+Q)
   push operator + on the stack:          a R +
   and process it:                        S         (where S == a+R)
</pre>
<p> As you can see the <font SIZE="-1">RPN</font> expression <tt>&quot;a,b,c,d,e,+,+,+,+,+&quot;</tt> will evaluate in <tt>&quot;((((d+e)+c)+b)+a)&quot;</tt> and it has the same outcome as <tt>&quot;a,b,+,c,+,d,+,e,+&quot;</tt>. This is called the commutative law of addition, but you may forget this right away, as long as you remember what it means. </p>
<p> Now look at an expression that contains a multiplication: </p>
<p> First in normal math: <tt>&quot;let result = a+b*c&quot;</tt>. In this case you can&#8217;t choose the order yourself, you have to start with the multiplication and then add a to it. You may alter the position of b and c, you must not alter the position of a and b. </p>
<p> You have to take this in consideration when converting this expression into <font SIZE="-1">RPN</font>. Read it as: &#8220;Add the outcome of b*c to a&#8221; and then it is easy to write the <font SIZE="-1">RPN</font> expression: <tt>&quot;result=a,b,c,*,+&quot;</tt> Another expression that would return the same: <tt>&quot;result=b,c,*,a,+&quot;</tt> </p>
<p> In normal math, you may encounter something like &#8220;a*(b+c)&#8221; and this can also be converted into <font SIZE="-1">RPN</font>. The parenthesis just tell you to first add b and c, and then multiply a with the result. Again, now it is easy to write it in <font SIZE="-1">RPN:</font> <tt>&quot;result=a,b,c,+,*&quot;</tt>. Note that this is very similar to one of the expressions in the previous paragraph, only the multiplication and the addition changed places. </p>
<p> When you have problems with <font SIZE="-1">RPN</font> or when RRDtool is complaining, it&#8217;s usually a good thing to write down the stack on a piece of paper and see what happens. Have the manual ready and pretend to be RRDtool. Just do all the math by hand to see what happens, I&#8217;m sure this will solve most, if not all, problems you encounter.</p>
<h2>Some special numbers</h2>
<h3>The unknown value</h3>
<p> Sometimes collecting your data will fail. This can be very common, especially when querying over busy links. RRDtool can be configured to allow for one (or even more) unknown value(s) and calculate the missing update. You can, for instance, query your device every minute. This is creating one so called <font SIZE="-1">PDP</font> or primary data point per minute. If you defined your <font SIZE="-1">RRD</font> to contain an <font SIZE="-1">RRA</font> that stores 5-minute values, you need five of those PDPs to create one <font SIZE="-1">CDP</font> (consolidated data point). These PDPs can become unknown in two cases:</p>
<dl>
<dt>1.</p>
<dd> The updates are too far apart. This is tuned using the &#8220;heartbeat&#8221; setting.</p>
<dt>2.</p>
<dd> The update was set to unknown on purpose by inserting no value (using the template option) or by using &#8220;U&#8221; as the value to insert.</dl>
<p> When a <font SIZE="-1">CDP</font> is calculated, another mechanism determines if this <font SIZE="-1">CDP</font> is valid or not. If there are too many PDPs unknown, the <font SIZE="-1">CDP</font> is unknown as well. This is determined by the xff factor. Please note that one unknown counter update can result in two unknown PDPs! If you only allow for one unknown <font SIZE="-1">PDP</font> per <font SIZE="-1">CDP</font>, this makes the <font SIZE="-1">CDP</font> go unknown! </p>
<p> Suppose the counter increments with one per second and you retrieve it every minute: </p>
<p>counter value resulting rate 10&#8217;000 10&#8217;060 1;<br />
(10&#8217;060 &#8211; 10&#8217;000) / 60 == 1 10&#8217;120 1;<br />
(10&#8217;120 &#8211; 10&#8217;060) / 60 == 1 unknown unknown;<br />
you don&#8217;t know the last value 10&#8217;240 unknown;<br />
you don&#8217;t know the previous value 10&#8217;300 1;<br />
(10&#8217;300 &#8211; 10&#8217;240) / 60 == 1</p>
<p> If the <font SIZE="-1">CDP</font> was to be calculated from the last five updates, it would get two unknown PDPs and three known PDPs. If xff would have been set to 0.5 which by the way is a commonly used factor, the <font SIZE="-1">CDP</font> would have a known value of 1. If xff would have been set to 0.2 then the resulting <font SIZE="-1">CDP</font> would be unknown. </p>
<p> You have to decide the proper values for heartbeat, number of PDPs per <font SIZE="-1">CDP</font> and the xff factor. As you can see from the previous text they define the behavior of your <font SIZE="-1">RRA</font>.</p>
<h3>Working with unknown data in your database</h3>
<p> As you have read in the previous chapter, entries in an <font SIZE="-1">RRA</font> can be set to the unknown value. If you do calculations with this type of value, the result has to be unknown too. This means that an expression such as <tt>&quot;result=a,b,+&quot;</tt> will be unknown if either a or b is unknown. It would be wrong to just ignore the unknown value and return the value of the other parameter. By doing so, you would assume &#8220;unknown&#8221; means &#8220;zero&#8221; and this is not true. </p>
<p> There has been a case where somebody was collecting data for over a year. A new piece of equipment was installed, a new <font SIZE="-1">RRD</font> was created and the scripts were changed to add a counter from the old database and a counter from the new database. The result was disappointing, a large part of the statistics seemed to have vanished mysteriously &#8230; They of course didn&#8217;t, values from the old database (known values) were added to values from the new database (unknown values) and the result was unknown. </p>
<p> In this case, it is fairly reasonable to use a <font SIZE="-1">CDEF</font> that alters unknown data into zero. The counters of the device were unknown (after all, it wasn&#8217;t installed yet!) but you know that the data rate through the device had to be zero (because of the same reason: it was not installed). </p>
<p> There are some examples below that make this change.</p>
<h3>Infinity</h3>
<p> Infinite data is another form of a special number. It cannot be graphed because by definition you would never reach the infinite value. You can think of positive and negative infinity depending on the position relative to zero. </p>
<p> RRDtool is capable of representing (-not- graphing!) infinity by stopping at its current maximum (for positive infinity) or minimum (for negative infinity) without knowing this maximum (minimum). </p>
<p> Infinity in RRDtool is mostly used to draw an <font SIZE="-1">AREA</font> without knowing its vertical dimensions. You can think of it as drawing an <font SIZE="-1">AREA</font> with an infinite height and displaying only the part that is visible in the current graph. This is probably a good way to approximate infinity and it sure allows for some neat tricks. See below for examples.</p>
<h3>Working with unknown data and infinity</h3>
<p> Sometimes you would like to discard unknown data and pretend it is zero (or any other value for that matter) and sometimes you would like to pretend that known data is unknown (to discard known-to-be-wrong data). This is why CDEFs have support for unknown data. There are also examples available that show unknown data by using infinity.</p>
<h2>Some examples</h2>
<h3>Example: using a recently created <font SIZE="-1">RRD</font></h3>
<p> You are keeping statistics on your router for over a year now. Recently you installed an extra router and you would like to show the combined throughput for these two devices. </p>
<p> If you just add up the counters from router.rrd and router2.rrd, you will add known data (from router.rrd) to unknown data (from router2.rrd) for the bigger part of your stats. You could solve this in a few ways:</p>
<dl>
<dt>&bull;</p>
<dd> While creating the new database, fill it with zeros from the start to now. You have to make the database start at or before the least recent time in the other database.</p>
<dt>&bull;</p>
<dd> Alternatively, you could use <font SIZE="-1">CDEF</font> and alter unknown data to zero.</dl>
<p> Both methods have their pros and cons. The first method is troublesome and if you want to do that you have to figure it out yourself. It is not possible to create a database filled with zeros, you have to put them in manually. Implementing the second method is described next: </p>
<p> What we want is: &#8220;if the value is unknown, replace it with zero&#8221;. This could be written in pseudo-code as: if (value is unknown) then (zero) else (value). When reading the rrdgraph manual you notice the &#8220;<font SIZE="-1">UN</font>&#8221; function that returns zero or one. You also notice the &#8220;<font SIZE="-1">IF</font>&#8221; function that takes zero or one as input. </p>
<p> First look at the &#8220;<font SIZE="-1">IF</font>&#8221; function. It takes three values from the stack, the first value is the decision point, the second value is returned to the stack if the evaluation is &#8220;true&#8221; and if not, the third value is returned to the stack. We want the &#8220;<font SIZE="-1">UN</font>&#8221; function to decide what happens so we combine those two functions in one <font SIZE="-1">CDEF</font>. </p>
<p> Lets write down the two possible paths for the &#8220;<font SIZE="-1">IF</font>&#8221; function: </p>
<p>if<br />
true return a if false return b</p>
<p> In <font SIZE="-1">RPN:</font> <tt>&quot;result=x,a,b,IF&quot;</tt> where &#8220;x&#8221; is either true or false. </p>
<p> Now we have to fill in &#8220;x&#8221;, this should be the &#8220;(value is unknown)&#8221; part and this is in <font SIZE="-1">RPN:</font> <tt>&quot;result=value,UN&quot;</tt> </p>
<p> We now combine them: <tt>&quot;result=value,UN,a,b,IF&quot;</tt> and when we fill in the appropriate things for &#8220;a&#8221; and &#8220;b&#8221; we&#8217;re finished: </p>
<p> <tt>&quot;CDEF:result=value,UN,0,value,IF&quot;</tt> </p>
<p> You may want to read Steve Rader&#8217;s <font SIZE="-1">RPN</font> guide if you have difficulties with the way I explained this last example. </p>
<p> If you want to check this <font SIZE="-1">RPN</font> expression, just mimic RRDtool behavior: </p>
<pre>
   For any known value, the expression evaluates as follows:
   CDEF:result=value,UN,0,value,IF  (value,UN) is not true so it becomes 0
   CDEF:result=0,0,value,IF         &quot;IF&quot; will return the 3rd value
   CDEF:result=value                The known value is returned
   For the unknown value, this happens:
   CDEF:result=value,UN,0,value,IF  (value,UN) is true so it becomes 1
   CDEF:result=1,0,value,IF         &quot;IF&quot; sees 1 and returns the 2nd value
   CDEF:result=0                    Zero is returned
</pre>
<p> Of course, if you would like to see another value instead of zero, you can use that other value. </p>
<p> Eventually, when all unknown data is removed from the <font SIZE="-1">RRD</font>, you may want to remove this rule so that unknown data is properly displayed.</p>
<h3>Example: better handling of unknown data, by using time</h3>
<p> The above example has one drawback. If you do log unknown data in your database after installing your new equipment, it will also be translated into zero and therefore you won&#8217;t see that there was a problem. This is not good and what you really want to do is:</p>
<dl>
<dt>&bull;</p>
<dd> If there is unknown data, look at the time that this sample was taken.</p>
<dt>&bull;</p>
<dd> If the unknown value is before time xxx, make it zero.</p>
<dt>&bull;</p>
<dd> If it is after time xxx, leave it as unknown data.</dl>
<p> This is doable: you can compare the time that the sample was taken to some known time. Assuming you started to monitor your device on Friday September 17, 1999, 00:35:57 <font SIZE="-1">MET</font> <font SIZE="-1">DST</font>. Translate this time in seconds since 1970-01-01 and it becomes 937&#8217;521&#8217;357. If you process unknown values that were received after this time, you want to leave them unknown and if they were &#8220;received&#8221; before this time, you want to translate them into zero (so you can effectively ignore them while adding them to your other routers counters). </p>
<p> Translating Friday September 17, 1999, 00:35:57 <font SIZE="-1">MET</font> <font SIZE="-1">DST</font> into 937&#8217;521&#8217;357 can be done by, for instance, using gnu date: </p>
<pre>
   date -d &quot;19990917 00:35:57&quot; +%s
</pre>
<p> You could also dump the database and see where the data starts to be known. There are several other ways of doing this, just pick one. </p>
<p> Now we have to create the magic that allows us to process unknown values different depending on the time that the sample was taken. This is a three step process:</p>
<dl>
<dt>1.</p>
<dd> If the timestamp of the value is after 937&#8217;521&#8217;357, leave it as is.</p>
<dt>2.</p>
<dd> If the value is a known value, leave it as is.</p>
<dt>3.</p>
<dd> Change the unknown value into zero.</dl>
<p> Lets look at part one: </p>
<pre>
    if (true) return the original value
</pre>
<p> We rewrite this: </p>
<p>if (true)<br />
return &#8220;a&#8221; if (false) return &#8220;b&#8221;</p>
<p> We need to calculate true or false from step 1. There is a function available that returns the timestamp for the current sample. It is called, how surprisingly, &#8220;<font SIZE="-1">TIME</font>&#8221;. This time has to be compared to a constant number, we need &#8220;<font SIZE="-1">GT</font>&#8221;. The output of &#8220;<font SIZE="-1">GT</font>&#8221; is true or false and this is good input to &#8220;<font SIZE="-1">IF</font>&#8221;. We want &#8220;if (time &gt; 937521357) then (return a) else (return b)&#8221;. </p>
<p> This process was already described thoroughly in the previous chapter so lets do it quick: </p>
<p>if (x)<br />
then a else b<br />
        where x represents &#8220;time&gt;937521357&#8221; where a represents the original value<br />
            where b represents the outcome of the previous example<br />
                time &gt; 937521357 &#8212; &gt; TIME,<br />
    937521357, GT if (x) then a else b&#8211; &gt; x, a, b, IF substitute x&#8211; &gt; TIME, 937521357, GT, a, b, IF substitute a&#8211; &gt; TIME, 937521357, GT, value, b, IF substitute b&#8211; &gt; TIME, 937521357, GT, value, value, UN, 0, value, IF, IF</p>
<p> We end up with: <tt>&quot;CDEF:result=TIME,937521357,GT,value,value,UN,0,value,IF,IF&quot;</tt> </p>
<p> This looks very complex, however, as you can see, it was not too hard to come up with.</p>
<h3>Example: Pretending weird data isn&#8217;t there</h3>
<p> Suppose you have a problem that shows up as huge spikes in your graph. You know this happens and why, so you decide to work around the problem. Perhaps you&#8217;re using your network to do a backup at night and by doing so you get almost 10mb/s while the rest of your network activity does not produce numbers higher than 100kb/s. </p>
<p> There are two options:</p>
<dl>
<dt>1.</p>
<dd> If the number exceeds 100kb/s it is wrong and you want it masked out by changing it into unknown.</p>
<dt>2.</p>
<dd> You don&#8217;t want the graph to show more than 100kb/s.</dl>
<p> Pseudo code: if (number &gt; 100) then unknown else number or Pseudo code: if (number &gt; 100) then 100 else number. </p>
<p> The second &#8220;problem&#8221; may also be solved by using the rigid option of RRDtool graph, however this has not the same result. In this example you can end up with a graph that does autoscaling. Also, if you use the numbers to display maxima they will be set to 100kb/s. </p>
<p> We use &#8220;<font SIZE="-1">IF</font>&#8221; and &#8220;<font SIZE="-1">GT</font>&#8221; again. &#8220;if (x) then (y) else (z)&#8221; is written down as &#8220;CDEF:result=x,y,z,IF&#8221;; now fill in x, y and z. For x you fill in &#8220;number greater than 100kb/s&#8221; becoming &#8220;number,100000,GT&#8221; (kilo is 1&#8217;000 and b/s is what we measure!). The &#8220;z&#8221; part is &#8220;number&#8221; in both cases and the &#8220;y&#8221; part is either &#8220;<font SIZE="-1">UNKN</font>&#8221; for unknown or &#8220;100000&#8221; for 100kb/s. </p>
<p> The two <font SIZE="-1">CDEF</font> expressions would be: </p>
<pre>
    CDEF:result=number,100000,GT,UNKN,number,IF
    CDEF:result=number,100000,GT,100000,number,IF
</pre>
<h3>Example: working on a certain time span</h3>
<p> If you want a graph that spans a few weeks, but would only want to see some routers&#8217; data for one week, you need to &#8220;hide&#8221; the rest of the time frame. Don&#8217;t ask me when this would be useful, it&#8217;s just here for the example :) </p>
<p> We need to compare the time stamp to a begin date and an end date. Comparing isn&#8217;t difficult: </p>
<pre>
        TIME,begintime,GE
        TIME,endtime,LE
</pre>
<p> These two parts of the <font SIZE="-1">CDEF</font> produce either 0 for false or 1 for true. We can now check if they are both 0 (or 1) using a few <font SIZE="-1">IF</font> statements but, as Wataru Satoh pointed out, we can use the &#8220;*&#8221; or &#8220;+&#8221; functions as logical <font SIZE="-1">AND</font> and logical <font SIZE="-1">OR</font>. </p>
<p> For &#8220;*&#8221;, the result will be zero (false) if either one of the two operators is zero. For &#8220;+&#8221;, the result will only be false (0) when two false (0) operators will be added. Warning: *any* number not equal to 0 will be considered &#8220;true&#8221;. This means that, for instance, &#8220;-1,1,+&#8221; (which should be &#8220;true or true&#8221;) will become <font SIZE="-1">FALSE</font> &#8230; In other words, use &#8220;+&#8221; only if you know for sure that you have positive numbers (or zero) only. </p>
<p> Let&#8217;s compile the complete <font SIZE="-1">CDEF:</font> </p>
<pre>
        DEF:ds0=router1.rrd:AVERAGE
        CDEF:ds0modified=TIME,begintime,GT,TIME,endtime,LE,*,ds0,UNKN,IF
</pre>
<p> This will return the value of ds0 if both comparisons return true. You could also do it the other way around: </p>
<pre>
        DEF:ds0=router1.rrd:AVERAGE
        CDEF:ds0modified=TIME,begintime,LT,TIME,endtime,GT,+,UNKN,ds0,IF
</pre>
<p> This will return an <font SIZE="-1">UNKNOWN</font> if either comparison returns true.</p>
<h3>Example: You suspect to have problems and want to see unknown data.</h3>
<p> Suppose you add up the number of active users on several terminal servers. If one of them doesn&#8217;t give an answer (or an incorrect one) you get &#8220;NaN&#8221; in the database (&#8220;Not a Number&#8221;) and NaN is evaluated as Unknown. </p>
<p> In this case, you would like to be alerted to it and the sum of the remaining values is of no value to you. </p>
<p> It would be something like: </p>
<pre>
    DEF:users1=location1.rrd:onlineTS1:LAST
    DEF:users2=location1.rrd:onlineTS2:LAST
    DEF:users3=location2.rrd:onlineTS1:LAST
    DEF:users4=location2.rrd:onlineTS2:LAST
    CDEF:allusers=users1,users2,users3,users4,+,+,+
</pre>
<p> If you now plot allusers, unknown data in one of users1..users4 will show up as a gap in your graph. You want to modify this to show a bright red line, not a gap. </p>
<p> Define an extra <font SIZE="-1">CDEF</font> that is unknown if all is okay and is infinite if there is an unknown value: </p>
<pre>
    CDEF:wrongdata=allusers,UN,INF,UNKN,IF
</pre>
<p> &#8220;allusers,UN&#8221; will evaluate to either true or false, it is the (x) part of the &#8220;<font SIZE="-1">IF</font>&#8221; function and it checks if allusers is unknown. The (y) part of the &#8220;<font SIZE="-1">IF</font>&#8221; function is set to &#8220;<font SIZE="-1">INF</font>&#8221; (which means infinity) and the (z) part of the function returns &#8220;<font SIZE="-1">UNKN</font>&#8221;. </p>
<p> The logic is: if (allusers == unknown) then return <font SIZE="-1">INF</font> else return <font SIZE="-1">UNKN</font>. </p>
<p> You can now use <font SIZE="-1">AREA</font> to display this &#8220;wrongdata&#8221; in bright red. If it is unknown (because allusers is known) then the red <font SIZE="-1">AREA</font> won&#8217;t show up. If the value is <font SIZE="-1">INF</font> (because allusers is unknown) then the red <font SIZE="-1">AREA</font> will be filled in on the graph at that particular time. </p>
<pre>
   AREA:allusers#0000FF:combined user count
   AREA:wrongdata#FF0000:unknown data
</pre>
<h3>Same example useful with STACKed data:</h3>
<p> If you use stack in the previous example (as I would do) then you don&#8217;t add up the values. Therefore, there is no relationship between the four values and you don&#8217;t get a single value to test. Suppose users3 would be unknown at one point in time: users1 is plotted, users2 is stacked on top of users1, users3 is unknown and therefore nothing happens, users4 is stacked on top of users2. Add the extra CDEFs anyway and use them to overlay the &#8220;normal&#8221; graph: </p>
<pre>
   DEF:users1=location1.rrd:onlineTS1:LAST
   DEF:users2=location1.rrd:onlineTS2:LAST
   DEF:users3=location2.rrd:onlineTS1:LAST
   DEF:users4=location2.rrd:onlineTS2:LAST
   CDEF:allusers=users1,users2,users3,users4,+,+,+
   CDEF:wrongdata=allusers,UN,INF,UNKN,IF
   AREA:users1#0000FF:users at ts1
   STACK:users2#00FF00:users at ts2
   STACK:users3#00FFFF:users at ts3
   STACK:users4#FFFF00:users at ts4
   AREA:wrongdata#FF0000:unknown data
</pre>
<p> If there is unknown data in one of users1..users4, the &#8220;wrongdata&#8221; <font SIZE="-1">AREA</font> will be drawn and because it starts at the X-axis and has infinite height it will effectively overwrite the STACKed parts. </p>
<p> You could combine the two <font SIZE="-1">CDEF</font> lines into one (we don&#8217;t use &#8220;allusers&#8221;) if you like. But there are good reasons for writing two <font SIZE="-1">CDEFS:</font></p>
<dl>
<dt>&bull;</p>
<dd> It improves the readability of the script.</p>
<dt>&bull;</p>
<dd> It can be used inside <font SIZE="-1">GPRINT</font> to display the total number of users.</dl>
<p> If you choose to combine them, you can substitute the &#8220;allusers&#8221; in the second <font SIZE="-1">CDEF</font> with the part after the equal sign from the first line: </p>
<pre>
   CDEF:wrongdata=users1,users2,users3,users4,+,+,+,UN,INF,UNKN,IF
</pre>
<p> If you do so, you won&#8217;t be able to use these next GPRINTs: </p>
<pre>
   COMMENT:&quot;Total number of users seen&quot;
   GPRINT:allusers:MAX:&quot;Maximum: %6.0lf&quot;
   GPRINT:allusers:MIN:&quot;Minimum: %6.0lf&quot;
   GPRINT:allusers:AVERAGE:&quot;Average: %6.0lf&quot;
   GPRINT:allusers:LAST:&quot;Current: %6.0lf
&quot;
</pre>
<h2>The examples from the RRD graph manual page</h2>
<h3>Degrees Celsius vs. Degrees Fahrenheit</h3>
<p> To convert Celsius into Fahrenheit use the formula F=9/5*C+32 </p>
<pre>
   rrdtool graph demo.png --title=&quot;Demo Graph&quot; \
      DEF:cel=demo.rrd:exhaust:AVERAGE \
      CDEF:far=9,5,/,cel,*,32,+ \
      LINE2:cel#00a000:&quot;D. Celsius&quot; \
      LINE2:far#ff0000:&quot;D. Fahrenheit
