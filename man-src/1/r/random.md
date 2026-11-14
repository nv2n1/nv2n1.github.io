---
title: "random(1)"
name: "random"
section: "1"
letter: "r"
url: "/docs/linux/man/1-random/"
---

<h2 class="name">NAME</h2>
 

 random - generate random number

<h3>Synopsis</h3>

 random [SEED]

<h3>Description</h3>

 The random command is used to generate a random number in the interval 0&lt;=N&lt;32767. If an argument is given, it is used to seed the random number generator. This can be useful for debugging purposes, where it can be desirable to get the same random number sequence multiple times. If the random number generator is called without first seeding it, the current time will be used as the seed.

<h3>Example</h3>

 The following code will count down from a random number to 1: 

 

 <pre>
for i in (seq (random) -1 1)
        echo $i
        sleep
end
</pre> 

 
&nbsp;<wbr> 

<h2>Index</h2>


