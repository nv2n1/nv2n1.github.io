---
title: "libmemcached_examples(3)"
name: "libmemcached_examples"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmemcached_examples/"
description: "libmemcached_examples – libmemcached Documentation"
---

<h2>NAME</h2>
<p> libmemcached_examples &#8211; libmemcached Documentation </p>
<p> Examples for libmemcached</p>
<h2>DESCRIPTION</h2>
<p> For full examples, test cases are found in tests/*.c in the main distribution. These are always up to date, and are used for each test run of the library.</p>
<h2>CONNECTING TO SERVERS</h2>
<pre><code>
const char *config_string= "--SERVER=host10.example.com --SERVER=host11.example.com --SERVER=host10.example.com"
memcached_st *memc= memcached(config_string, strlen(config_string);
{
...
}
 memcached_free(memc);
</code></pre>
<p> In the above code you create a <code>memcached_st</code> object with three server by making use of <code>memcached_create()</code>.</p>
<h2>CREATING A POOL OF SERVERS</h2>
<p> Creating a pool of Servers: </p>
<p>const char *config_string = &#8220;&#8211;SERVER=host10.example.com &#8211;SERVER=host11.example.com &#8211;SERVER=host10.example.com&#8221;;<br />
memcached_pool_st *pool = memcached_pool(config_string, strlen(config_string));<br />
memcached_return_t rc;<br />
memcached_st *memc = memcached_pool_pop(pool, false, &amp;rc);<br />
&#8230;.do work<br />
    /*<br />
      Release the memc_ptr that was pulled from the pool<br />
    */<br />
    memcached_pool_push(pool, memc);<br />
/*<br />
  Destroy the pool.<br />
*/<br />
memcached_pool_destroy(pool);</p>
<p> In the above code you create a <code>memcached_pool_st</code> object with three server by making use of <code>memcached_pool()</code>. </p>
<p> When <code>memcached_pool_destroy()</code> all memory will be released that is associated with the pool.</p>
<h2>ADDING A VALUE TO THE SERVER</h2>
<p> Adding a value to the Server: </p>
<p>char *key = &#8220;foo&#8221;;<br />
char *value = &#8220;value&#8221;;<br />
memcached_return_t rc = memcached_set(memc, key, strlen(key), value, value_length, (time_t)0, (uint32_t)0);<br />
if (rc != MEMCACHED_SUCCESS) {<br />
    &#8230; // handle failure<br />
}</p>
<p> It is best practice to always look at the return value of any operation.</p>
<h2>FETCHING MULTIPLE VALUES</h2>
<pre><code>
memcached_return_t rc;
char *keys[] = {"fudge", "son", "food"};
size_t key_length[] = {5, 3, 4};
unsigned int x;
uint32_t flags;
char return_key[MEMCACHED_MAX_KEY];
size_t return_key_length;
char *return_value;
size_t return_value_length;
rc = memcached_mget(memc, keys, key_length, 3);
x = 0;
while ((return_value = memcached_fetch(memc, return_key, &amp;return_key_length,
                                       &amp;return_value_length, &amp;flags, &amp;rc))) {
    free(return_value);
    x++;
}
</code></pre>
<p> Notice that you freed values returned from memcached_fetch(). The define <code>MEMCACHED_MAX_KEY</code> is provided for usage.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
